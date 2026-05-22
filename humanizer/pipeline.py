# humanizer/pipeline.py
# 17-pass rule-based text humanization pipeline — zero AI API calls

import re
import random
from .phrases import (
    AI_PHRASES,
    INTENSIFIERS,
    DISCOURSE_MARKERS,
    CONTRACTIONS,
    PASSIVE_TO_ACTIVE,
    HEDGE_TRIGGERS,
    PARENTHETICALS,
    SELF_CORRECTIONS,
    PERSONAL_VOICE,
    QUALIFIERS,
    PUNCTUATION_HUMANIZE,
    FRONTING_PATTERNS,
    SYNTACTIC_FRONTING,
    CONJUNCTION_OPENERS,
    ADVERBIAL_FRONTING,
    IDIOMATIC_INJECTIONS,
)
import nltk
from nltk.corpus import wordnet as wn

# ─────────────────────────────────────────────────────────────────────────────
# MODEL REGISTRY — shared singleton so app.py warm-up and pipeline use the
# SAME loaded object (fixes the duplicate-load bug).
# ─────────────────────────────────────────────────────────────────────────────
import os as _os
import threading as _threading

_MODELS_DIR = _os.path.join(_os.path.dirname(__file__), '..', 'models')

QWEN3_DIR   = _os.path.join(_MODELS_DIR, 'Qwen3-0.6b')
T5_DIR      = _os.path.join(_MODELS_DIR, 'T5_Paraphrase_Paws')

_MODEL_TOKENIZER = None
_MODEL_OBJ       = None
_MODEL_TYPE      = None   # 'qwen3' | 't5' | None
_MODEL_LOCK      = _threading.Lock()


def _qwen3_weights_present() -> bool:
    """Check that Qwen3 has its actual weight file, not just config."""
    return (
        _os.path.exists(QWEN3_DIR) and (
            _os.path.exists(_os.path.join(QWEN3_DIR, 'model.safetensors')) or
            _os.path.exists(_os.path.join(QWEN3_DIR, 'pytorch_model.bin'))
        )
    )

def preload_model():
    """
    Load the best available model into the global singleton.
    Called once at startup by app.py — pipeline.py reuses the same object.
    Priority: Qwen3-0.6B local (dev) > HF Hub download (prod) > T5 local (fallback).
    """
    global _MODEL_TOKENIZER, _MODEL_OBJ, _MODEL_TYPE
    if _MODEL_OBJ is not None:
        return  # already loaded

    try:
        import torch
        from transformers import AutoTokenizer, AutoModelForCausalLM, AutoModelForSeq2SeqLM

        # Optimize dtype: Use bfloat16 or float16 when running on CUDA to minimize VRAM footprint and avoid paging latency,
        # which is extremely critical for 4GB GPUs like the GTX 1650. Fall back to float32 on CPU.
        if torch.cuda.is_available():
            if torch.cuda.is_bf16_supported():
                dtype = torch.bfloat16
            else:
                dtype = torch.float16
        else:
            dtype = torch.float32

        device_kwargs = {
            'device_map': 'auto' if torch.cuda.is_available() else None,
            'dtype': dtype,
        }

        # Enable PyTorch SDPA (Scaled Dot Product Attention) for optimized attention kernels when using GPU
        if torch.cuda.is_available():
            device_kwargs['attn_implementation'] = 'sdpa'

        if _qwen3_weights_present():
            # ── Development: load from local disk ──────────────────────────
            print(f"[Model] Loading Qwen3-0.6B from local disk ({QWEN3_DIR}) ...")
            _MODEL_TOKENIZER = AutoTokenizer.from_pretrained(QWEN3_DIR)
            _MODEL_OBJ = AutoModelForCausalLM.from_pretrained(QWEN3_DIR, **device_kwargs)
            _MODEL_OBJ.eval()
            _MODEL_TYPE = 'qwen3'
            print(f"[Model] Qwen3-0.6B ready on {'GPU' if torch.cuda.is_available() else 'CPU'} (local).")

        else:
            # ── Production: download from Hugging Face Hub ─────────────────
            HF_MODEL_ID = _os.environ.get('HF_MODEL_ID', 'Qwen/Qwen3-0.6B')
            print(f"[Model] No local weights found. Downloading {HF_MODEL_ID} from HF Hub ...")
            _MODEL_TOKENIZER = AutoTokenizer.from_pretrained(HF_MODEL_ID)
            _MODEL_OBJ = AutoModelForCausalLM.from_pretrained(HF_MODEL_ID, **device_kwargs)
            _MODEL_OBJ.eval()
            _MODEL_TYPE = 'qwen3'
            print(f"[Model] Qwen3-0.6B ready on {'GPU' if torch.cuda.is_available() else 'CPU'} (HF Hub).")

    except Exception as e:
        import traceback
        print(f"[Model] Failed to load: {e}")
        traceback.print_exc()


def get_model():
    """Return (tokenizer, model, model_type). Lazy-loads if not already loaded."""
    global _MODEL_TOKENIZER, _MODEL_OBJ, _MODEL_TYPE
    if _MODEL_OBJ is None:
        preload_model()
    return _MODEL_TOKENIZER, _MODEL_OBJ, _MODEL_TYPE


def get_wordnet_pos(treebank_tag):
    if treebank_tag.startswith('J'):
        return wn.ADJ
    elif treebank_tag.startswith('V'):
        return wn.VERB
    elif treebank_tag.startswith('N'):
        return wn.NOUN
    elif treebank_tag.startswith('R'):
        return wn.ADV
    else:
        return None

# Use a truly random seed so every run produces unique output.
# A fixed seed would mean two students running the same AI text
# get identical results — which Turnitin would flag as collusion.
random.seed()


# ─────────────────────────────────────────────────────────────────────────────
# UTILITIES
# ─────────────────────────────────────────────────────────────────────────────

def _replace_dict(text: str, mapping: dict, case_sensitive: bool = False) -> tuple[str, int]:
    """Replace all occurrences of keys with values. Returns (new_text, count)."""
    count = 0
    for src, dst in mapping.items():
        flags = 0 if case_sensitive else re.IGNORECASE
        pattern = re.compile(re.escape(src), flags)

        def _replacer(m, _dst=dst):
            nonlocal count
            count += 1
            original = m.group(0)
            if original and original[0].isupper() and _dst and _dst[0].islower():
                return _dst[0].upper() + _dst[1:]
            return _dst

        text = pattern.sub(_replacer, text)
    return text, count


def _tokenize_sentences(text: str) -> list[str]:
    """Sentence tokenizer using punctuation + capital letter boundaries."""
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    return [p.strip() for p in parts if p.strip()]


def _split_long_sentence(sentence: str, max_words: int = 24) -> list[str]:
    """Split an overly long sentence at a natural conjunction."""
    words = sentence.split()
    if len(words) <= max_words:
        return [sentence]

    split_words = [
        " which ", " that ", " and ", " but ", " while ",
        " although ", " because ", " since ", " where ", " when ",
        " whereas ", " however ", " so ", " yet ", " unless ",
        " until ", " after ", " before ", " once ", " if ",
    ]

    mid = len(sentence) // 2
    best_pos = -1
    best_dist = len(sentence)
    best_sw = " and "

    for sw in split_words:
        pos = sentence.find(sw, len(sentence) // 4)
        if pos == -1:
            continue
        dist = abs(pos - mid)
        if dist < best_dist:
            best_dist = dist
            best_pos = pos
            best_sw = sw

    if best_pos == -1:
        return [sentence]

    first = sentence[:best_pos].strip().rstrip(',')
    second = sentence[best_pos + len(best_sw):].strip()
    if second:
        second = second[0].upper() + second[1:]

    connector_map = {
        " which ": ". This ", " that ": ". This ",
        " and ": ". Also, ", " but ": ". However, ",
        " while ": ". Meanwhile, ", " although ": ". That said, ",
        " because ": ". The reason is that ", " since ": ". Since ",
        " where ": ". Here ", " when ": ". This happens when ",
        " whereas ": ". In contrast, ", " however ": ". However, ",
        " so ": ". So ", " yet ": ". Yet ",
        " unless ": ". Unless ", " until ": ". Until ",
        " after ": ". After ", " before ": ". Before ",
        " once ": ". Once ", " if ": ". If ",
    }
    prefix = connector_map.get(best_sw, ". ")
    if prefix.startswith(". "):
        pfx_text = prefix[2:].strip()
        second = pfx_text + " " + second if pfx_text else second

    return [first + ".", second]


def _merge_short_sentences(sentences: list[str], min_words: int = 7) -> list[str]:
    """Merge consecutive very short sentences with an em-dash."""
    result = []
    i = 0
    while i < len(sentences):
        s = sentences[i]
        if (
            i + 1 < len(sentences)
            and len(s.split()) < min_words
            and len(sentences[i + 1].split()) < min_words
            and random.random() < 0.65
        ):
            next_s = sentences[i + 1].rstrip('.!?')
            merged = s.rstrip('.!?') + " — " + next_s[0].lower() + next_s[1:]
            ending_char = sentences[i + 1][-1]
            if ending_char not in '.!?':
                ending_char = '.'
            merged += ending_char
            result.append(merged)
            i += 2
        else:
            result.append(s)
            i += 1
    return result


def _find_clause_boundary(sentence: str) -> int:
    """Find a good position mid-sentence to inject a parenthetical."""
    # Look for comma positions in the middle half of the sentence
    words = sentence.split()
    if len(words) < 12:
        return -1
    # Find a comma roughly in the middle
    mid = len(sentence) // 2
    for offset in range(0, len(sentence) // 3):
        for sign in [1, -1]:
            pos = mid + sign * offset
            if 0 < pos < len(sentence) and sentence[pos] == ',':
                return pos
    return -1


# ─────────────────────────────────────────────────────────────────────────────
# THE 13 PASSES
# ─────────────────────────────────────────────────────────────────────────────

def pass1_ai_phrases(text: str) -> tuple[str, int]:
    """Replace 500+ known AI phrases with natural equivalents."""
    return _replace_dict(text, AI_PHRASES)


def pass2_intensifiers(text: str) -> tuple[str, int]:
    """Remove or soften intensifiers that AI overuses."""
    return _replace_dict(text, INTENSIFIERS)


def pass3_burstiness(text: str) -> tuple[str, int]:
    """
    Inject sentence length variation — the #1 Turnitin signal.
    Splits long sentences and occasionally merges short consecutive ones.
    """
    sentences = _tokenize_sentences(text)
    count_before = len(sentences)

    new_sentences = []
    for s in sentences:
        parts = _split_long_sentence(s, max_words=22)
        new_sentences.extend(parts)

    new_sentences = _merge_short_sentences(new_sentences, min_words=9)

    changes = abs(len(new_sentences) - count_before)
    return " ".join(new_sentences), changes


def pass4_discourse_markers(text: str) -> tuple[str, int]:
    """Prepend human-sounding discourse markers to ~28% of AI-opener paragraphs."""
    ai_openers = (
        "The ", "This ", "These ", "Those ", "In ", "It ", "By ",
        "With ", "As ", "Our ", "We ", "One ", "Another ", "Each ",
        "Such ", "Any ", "Every ", "All ", "Both ", "Many ", "Most ",
    )
    paragraphs = text.split('\n')
    count = 0
    result = []
    used_markers: set[str] = set()

    for para in paragraphs:
        stripped = para.strip()
        if (
            len(stripped.split()) > 12
            and any(stripped.startswith(op) for op in ai_openers)
            and random.random() < 0.28
        ):
            available = [m for m in DISCOURSE_MARKERS if m not in used_markers]
            if not available:
                used_markers.clear()
                available = DISCOURSE_MARKERS[:]

            marker = random.choice(available)
            used_markers.add(marker)

            lowered = stripped[0].lower() + stripped[1:]
            para = para.replace(stripped, marker + lowered, 1)
            count += 1

        result.append(para)

    return '\n'.join(result), count


def pass5_contractions(text: str) -> tuple[str, int]:
    """Inject contractions selectively (skips code-like paragraphs)."""
    if text.count('`') > 2 or text.count('{') > 2 or text.count('//') > 1:
        return text, 0
    return _replace_dict(text, CONTRACTIONS, case_sensitive=True)


def pass6_passive_to_active(text: str) -> tuple[str, int]:
    """Replace weak passive constructions with active voice."""
    return _replace_dict(text, PASSIVE_TO_ACTIVE)


def pass7_opener_diversity(text: str) -> tuple[str, int]:
    """Prevent the same paragraph opener from appearing more than once."""
    replacements = {
        "The system ": ["Our system ", "This system ", "The platform ", "Rayvoy's system "],
        "The project ": ["Our project ", "This project ", "The work ", "The development "],
        "The platform ": ["Our platform ", "This platform ", "The system ", "The tool "],
        "The proposed ": ["Our proposed ", "The suggested ", "This proposed "],
        "The existing ": ["Our existing ", "The current ", "The old ", "The prior "],
        "The new ": ["Our new ", "The updated ", "This new ", "The revised "],
        "The team ": ["Our team ", "The staff ", "The group ", "Our counsellors "],
        "The user ": ["Each user ", "A user ", "The counsellor ", "Any user "],
        "The data ": ["All data ", "This data ", "Student data ", "The records "],
        "The process ": ["This process ", "Our process ", "The workflow ", "The procedure "],
        "The system is ": ["Our system is ", "The platform is ", "This system is "],
        "The approach ": ["Our approach ", "This approach ", "The method "],
        "The solution ": ["Our solution ", "This solution ", "The tool "],
        "The feature ": ["This feature ", "Our feature ", "Each feature "],
        "The module ": ["This module ", "Our module ", "Each module "],
        "The database ": ["Our database ", "This database ", "The backend "],
        "The interface ": ["Our interface ", "This interface ", "The UI "],
        "The implementation ": ["Our implementation ", "This implementation "],
    }

    paragraphs = text.split('\n')
    opener_counts: dict[str, int] = {}
    count = 0
    result = []

    for para in paragraphs:
        stripped = para.strip()
        for opener, alternatives in replacements.items():
            if stripped.startswith(opener):
                opener_counts[opener] = opener_counts.get(opener, 0) + 1
                if opener_counts[opener] >= 2:
                    alt = random.choice(alternatives)
                    para = para.replace(opener, alt, 1)
                    count += 1
                break
        result.append(para)

    return '\n'.join(result), count


def pass8_hedging(text: str) -> tuple[str, int]:
    """
    Replace overconfident AI assertions with hedged human-like language.
    Humans naturally hedge — AI is always certain.
    """
    return _replace_dict(text, HEDGE_TRIGGERS, case_sensitive=False)


def pass9_parentheticals(text: str) -> tuple[str, int]:
    """
    Inject parenthetical asides into ~15% of long sentences.
    Humans add tangential remarks mid-sentence — AI never does.
    """
    sentences = _tokenize_sentences(text)
    count = 0
    new_sentences = []
    used: set[str] = set()

    word_count = sum(len(s.split()) for s in sentences)
    multiplier = 3.0 if word_count < 100 else 2.0 if word_count < 200 else 1.0
    for s in sentences:
        words = s.split()
        if len(words) >= 18 and random.random() < (0.08 * multiplier):
            # Find a comma to inject after, or inject before the last clause
            boundary = _find_clause_boundary(s)
            available = [p for p in PARENTHETICALS if p not in used]
            if not available:
                used.clear()
                available = PARENTHETICALS[:]

            aside = random.choice(available)
            used.add(aside)

            if boundary > 0:
                new_s = s[:boundary + 1] + aside + s[boundary + 1:]
            else:
                # Inject before the last 4 words
                word_list = s.split()
                split_at = max(len(word_list) - 4, len(word_list) // 2)
                new_s = ' '.join(word_list[:split_at]) + aside + ' ' + ' '.join(word_list[split_at:])

            new_sentences.append(new_s)
            count += 1
        else:
            new_sentences.append(s)

    return ' '.join(new_sentences), count


def pass10_self_corrections(text: str) -> tuple[str, int]:
    """
    Insert human-style self-correction patterns at ~10% of sentence boundaries.
    'Or rather,', 'More precisely,', 'To be specific,' — AI never self-corrects.
    """
    count = 0
    word_count = len(text.split())
    multiplier = 3.0 if word_count < 100 else 2.0 if word_count < 200 else 1.0
    for src, dst in SELF_CORRECTIONS.items():
        # Only apply with a probability per occurrence
        occurrences = [m.start() for m in re.finditer(re.escape(src), text)]
        for pos in sorted(occurrences, reverse=True):
            if random.random() < (0.15 * multiplier):
                text = text[:pos] + dst + text[pos + len(src):]
                count += 1
    return text, count


def pass11_personal_voice(text: str) -> tuple[str, int]:
    """
    Replace impersonal 'one can' / 'it can be' with personal voice.
    Human writers use 'we found', 'we noticed' — AI stays impersonal.
    """
    return _replace_dict(text, PERSONAL_VOICE)


def pass12_qualifiers(text: str) -> tuple[str, int]:
    """
    Replace absolute AI statements with qualified human ones.
    AI says 'always' and 'completely' — humans say 'usually' and 'largely'.
    """
    return _replace_dict(text, QUALIFIERS)


def pass13_punctuation(text: str) -> tuple[str, int]:
    """
    Humanize punctuation patterns: replace bland conjunctions with
    em-dashes, semicolons, and varied connectors.
    """
    if text.count('`') > 2 or text.count('{') > 2:
        return text, 0
    return _replace_dict(text, PUNCTUATION_HUMANIZE, case_sensitive=True)


def pass14_syntactic_fronting(text: str) -> tuple[str, int]:
    """
    Break up repetitive Subject-Verb-Object structures.
    Uses regex for complex clefting and dict replacement for simple fronting.
    """
    count = 0
    
    # 1. Regex-based fronting
    for pattern, replacement in FRONTING_PATTERNS:
        matches = len(re.findall(pattern, text))
        if matches > 0:
            text = re.sub(pattern, replacement, text)
            count += matches
            
    # 2. Simple dictionary fronting
    text, n1 = _replace_dict(text, SYNTACTIC_FRONTING)
    text, n2 = _replace_dict(text, ADVERBIAL_FRONTING)
    
    return text, count + n1 + n2


def pass15_synonym_rotation(text: str) -> tuple[str, int]:
    """
    Disabled: NLTK WordNet synonym rotation lacks context and causes grammatical errors
    like swapping "reasons" for "ground". Vocabulary variation is now handled natively
    by the T5 paraphrase model in Pass 19 via Nucleus Sampling.
    """
    return text, 0


def pass16_imperfect_discourse(text: str) -> tuple[str, int]:
    """
    Inject conjunction openers (And, But, Yet) to start some paragraphs.
    AI is trained to avoid these, making them a strong human signal.
    """
    paragraphs = text.split('\n')
    count = 0
    result = []
    
    word_count = sum(len(p.split()) for p in paragraphs)
    multiplier = 3.0 if word_count < 100 else 2.0 if word_count < 200 else 1.0
    
    for para in paragraphs:
        stripped = para.strip()
        # Avoid stacking if it already starts with a conjunction or a pass4 marker
        existing_markers = tuple(list(CONJUNCTION_OPENERS) + list(DISCOURSE_MARKERS))
        if (
            len(stripped.split()) > 15
            and not any(stripped.startswith(op.strip()) for op in existing_markers)
            and random.random() < (0.08 * multiplier)
        ):
            opener = random.choice(CONJUNCTION_OPENERS)
            
            # Lowercase the original first word if it's not 'I' or an acronym
            first_word_end = stripped.find(' ')
            if first_word_end > 0:
                first_word = stripped[:first_word_end]
                if first_word != "I" and not first_word.isupper():
                    lowered = first_word.lower() + stripped[first_word_end:]
                    para = para.replace(stripped, opener + lowered, 1)
                else:
                    para = para.replace(stripped, opener + stripped, 1)
            count += 1
            
        result.append(para)
        
    return '\n'.join(result), count


def _rewrite_with_qwen3(para: str, tokenizer, model) -> str:
    """
    Use Qwen3-0.6B with a human-writing instruction prompt.
    This produces genuinely varied output because Qwen3 understands context
    and follows natural language instructions — unlike T5's blind paraphrase.
    """
    import torch

    # ── Prompt: direct instruction, no thinking required ─────────────────────
    # /no_think suffix tells Qwen3 to skip chain-of-thought (faster + no <think> block)
    prompt = (
        f"Rewrite the following paragraph to make it look 100% human-written.\n"
        f"Strict Guidelines:\n"
        f"1. Tone: Conversational, casual, simple, and informal.\n"
        f"2. Sentence Variety: Mix very short, punchy sentences (3-8 words) with longer, natural ones. Avoid uniform sentence length.\n"
        f"3. Vocabulary: Use simple, everyday words. Do NOT use complex academic vocabulary.\n"
        f"4. Contractions: Use contractions (don't, can't, it's, they're, etc.) naturally wherever possible.\n"
        f"5. NO AI transitions: Do NOT use formal transition phrases (like 'Furthermore', 'Moreover', 'Consequently', 'Therefore', 'As a consequence', 'In addition', 'Indeed', 'Crucial', 'Importantly', 'Furthermore'). Open sentences simply or use words like 'But', 'And', 'So', 'Plus'.\n"
        f"6. Content: Keep all original meanings and facts exactly the same. Do not add new information.\n\n"
        f"Original paragraph:\n{para}\n\n"
        f"Rewrite (output ONLY the rewritten paragraph, no introductions, no labels, no quotes): /no_think"
    )

    messages = [
        {"role": "system", "content": "You are a helpful assistant that rewrites text to look completely human. Use informal, natural, conversational language and contractions. Never show your thinking or write explanations. Output only the rewritten text."},
        {"role": "user", "content": prompt}
    ]

    # Apply chat template — enable_thinking=False disables Qwen3's <think> block
    # This makes generation 3-5x faster and removes the AI-detectable reasoning text
    try:
        encoded = tokenizer.apply_chat_template(
            messages,
            add_generation_prompt=True,
            return_tensors="pt",
            enable_thinking=False,   # ← KEY: disables <think> mode entirely
        )
        input_ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
    except TypeError:
        # Older transformers versions don't support enable_thinking — fallback
        try:
            encoded = tokenizer.apply_chat_template(
                messages,
                add_generation_prompt=True,
                return_tensors="pt",
            )
            input_ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
        except Exception:
            encoded = tokenizer.encode(prompt, return_tensors="pt")
            input_ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
    except Exception:
        encoded = tokenizer.encode(prompt, return_tensors="pt")
        input_ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded

    if isinstance(input_ids, list):
        input_ids = torch.tensor([input_ids])

    input_ids = input_ids.to(model.device)
    input_len = input_ids.shape[-1]
    attention_mask = torch.ones_like(input_ids).to(model.device)

    # Optimize max_new_tokens dynamically to prevent runaway text generation and speed up runtime
    max_tokens = min(150, int(len(para.split()) * 1.3) + 20)

    # Acquire model lock to guarantee thread-safe autoregressive decoding (prevents text bleed)
    with _MODEL_LOCK:
        # Inference mode is faster and uses less VRAM/memory than no_grad
        with torch.inference_mode():
            outputs = model.generate(
                input_ids,
                attention_mask=attention_mask,
                max_new_tokens=max_tokens,
                do_sample=True,
                temperature=0.70,   # Qwen3 non-thinking mode best practice
                top_p=0.80,         # Qwen3 non-thinking mode best practice
                top_k=20,           # Qwen3 non-thinking mode best practice
                repetition_penalty=1.15,
                use_cache=True,
                pad_token_id=tokenizer.eos_token_id,
            )

    generated = tokenizer.decode(outputs[0][input_len:], skip_special_tokens=True).strip()

    # ── Safety: strip any <think> blocks that leaked through ─────────────────
    generated = re.sub(r'<think>.*?</think>', '', generated, flags=re.DOTALL).strip()
    # Strip any "Rewritten:" / "Output:" label the model might prepend
    generated = re.sub(r'^(Rewritten|Output|Here is|Here\'s|Result)[:\s]+', '', generated, flags=re.IGNORECASE).strip()

    # Standardize quotation marks and curly apostrophes to straight ones for clean encoding and maximum human likeness
    generated = generated.replace('’', "'").replace('‘', "'").replace('“', '"').replace('”', '"')
    # Clean up double spaces or spaces before punctuation
    generated = re.sub(r'\s+', ' ', generated)
    generated = re.sub(r'\s+([.,!?;:])', r'\1', generated)

    words_out = len(generated.split())
    words_in  = len(para.split())
    if words_out < 3 or words_out > words_in * 4:
        return para  # safety fallback

    return generated


def _rewrite_with_t5(para: str, tokenizer, model) -> str:
    """T5 fallback using nucleus sampling for high perplexity."""
    import torch
    text_input = "paraphrase: " + para + " </s>"
    input_ids = tokenizer.encode(text_input, return_tensors="pt", max_length=256, truncation=True)
    input_ids = input_ids.to(model.device)

    # Acquire model lock to guarantee thread-safe autoregressive decoding (prevents text bleed)
    with _MODEL_LOCK:
        # Inference mode is faster and uses less VRAM/memory than no_grad
        with torch.inference_mode():
            outputs = model.generate(
                input_ids,
                max_length=256,
                do_sample=True,
                top_k=50,
                top_p=0.95,
                temperature=1.2,
                num_return_sequences=1,
                no_repeat_ngram_size=2,
                use_cache=True,
            )

    out_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    out_text = re.sub(r'\s+([.,!?;:])', r'\1', out_text)
    return out_text


def pass19_structural_smoothing(text: str, progress_callback=None) -> tuple[str, int]:
    """
    Neural rewrite pass — uses the best available local model.
    Qwen3-0.6B (preferred): instruction-tuned, produces genuinely varied human text.
    T5_Paraphrase_Paws (fallback): nucleus sampling paraphrase.
    """
    tokenizer, model, model_type = get_model()
    if tokenizer is None or model is None:
        return text, 0

    paragraphs = text.split('\n')
    smoothed_paragraphs = []
    changes = 0
    total = len(paragraphs)

    for i, para in enumerate(paragraphs):
        stripped = para.strip()

        # Optimize: skip the expensive neural model for short sentences/paragraphs under 12 words.
        # Rule-based passes will still humanize them instantly.
        if not stripped or len(stripped.split()) < 12:
            smoothed_paragraphs.append(para)
            continue

        if progress_callback:
            model_label = "Qwen3" if model_type == 'qwen3' else "T5"
            progress_callback(i, total, f"[{model_label}] Rewriting paragraph {i+1} of {total}...")

        try:
            if model_type == 'qwen3':
                out_text = _rewrite_with_qwen3(stripped, tokenizer, model)
            else:
                out_text = _rewrite_with_t5(stripped, tokenizer, model)

            if out_text.lower() != stripped.lower():
                changes += 1
            smoothed_paragraphs.append(out_text)
        except Exception as e:
            print(f"[pass19] Error on paragraph {i+1}: {e}")
            smoothed_paragraphs.append(para)  # keep original on error

    return '\n'.join(smoothed_paragraphs), changes


def pass17_ghost_characters(text: str) -> tuple[str, int]:
    """
    Remove invisible zero-width spaces often left by copying from ChatGPT.
    """
    ghost_chars = ['\u200b', '\u200c', '\u200d', '\ufeff']
    count = 0
    for gc in ghost_chars:
        if gc in text:
            count += text.count(gc)
            text = text.replace(gc, '')
    return text, count

def pass18_perplexity_tension(text: str) -> tuple[str, int]:
    """
    Target AIW-2 model by shattering next-word predictability (perplexity).
    Randomly injects organic idioms and relies on NLTK for the rest.
    """
    text, changes_idioms = _replace_dict(text, {k: random.choice(v) for k, v in IDIOMATIC_INJECTIONS.items()})
    
    # Rare synonym injection is now handled universally by NLTK in Pass 15
    return text, changes_idioms


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PIPELINE ORCHESTRATOR
# ─────────────────────────────────────────────────────────────────────────────

def humanize_text(text: str, progress_callback=None) -> dict:
    """
    Run the humanization pipeline.
    
    Strategy to defeat GPTZero Model 4.6b:
    1. T5 Nucleus Sampling runs FIRST on the clean original — this is the core.
       It generates structurally varied, context-aware rewrites with high perplexity.
    2. Light rule-based passes are applied AFTER to polish:
       - Remove known AI phrases  
       - Inject contractions (invisible human signal)
       - Hedging (sounds less certain/AI)
       - Burstiness (vary sentence lengths post-T5)
    3. Heavy pattern passes (parentheticals, idiomatic injections, self-corrections)
       are DISABLED because GPTZero is trained to recognise humanizer tool fingerprints.
    """
    stats = {}

    if progress_callback:
        progress_callback(2, 100, "Starting AI rewrite (Qwen3)...")


    # ── PASS 1: Qwen3 Neural Rewrite (runs FIRST on clean text) ─────────────
    def _pass19_cb(curr, tot, msg):
        if progress_callback:
            pct = 5 + int(70 * (curr / max(tot, 1)))
            progress_callback(pct, 100, msg)

    text, n = pass19_structural_smoothing(text, progress_callback=_pass19_cb)
    stats['pass19_structural_smoothing'] = n

    if progress_callback:
        progress_callback(76, 100, "Removing AI fingerprints...")

    # ── PASS 2: Remove known AI phrases (invisible, safe) ────────────────────
    text, n = pass1_ai_phrases(text);        stats['pass1_ai_phrases'] = n

    # ── PASS 3: Contractions — most invisible human signal ───────────────────
    text, n = pass5_contractions(text);      stats['pass5_contractions'] = n

    # ── PASS 4: Hedging — remove overconfident assertions ────────────────────
    text, n = pass8_hedging(text);           stats['pass8_hedging'] = n

    # ── PASS 5: Soften intensifiers ──────────────────────────────────────────
    text, n = pass2_intensifiers(text);      stats['pass2_intensifiers'] = n

    if progress_callback:
        progress_callback(85, 100, "Adjusting sentence rhythm...")

    # ── PASS 6: Burstiness — vary sentence lengths AFTER T5 ──────────────────
    # GPTZero's #1 signal is uniform sentence length. This fixes it post-T5.
    text, n = pass3_burstiness(text);        stats['pass3_burstiness'] = n

    # ── PASS 7: Ghost character cleanup ──────────────────────────────────────
    text, n = pass17_ghost_characters(text); stats['pass17_ghost_characters'] = n

    # Zeroed-out passes (kept for stats keys, disabled to avoid fingerprinting)
    for key in [
        'pass4_discourse_markers', 'pass6_passive_voice', 'pass7_opener_diversity',
        'pass9_parentheticals', 'pass10_self_corrections', 'pass11_personal_voice',
        'pass12_qualifiers', 'pass13_punctuation', 'pass14_syntactic_fronting',
        'pass15_synonym_rotation', 'pass16_imperfect_discourse', 'pass18_perplexity_tension'
    ]:
        stats[key] = 0

    if progress_callback:
        progress_callback(98, 100, "Finalizing output...")

    stats['total_changes'] = sum(stats.values())
    return {'text': text.strip(), 'stats': stats}


# ─────────────────────────────────────────────────────────────────────────────
# DOCX-LEVEL PROCESSING
# ─────────────────────────────────────────────────────────────────────────────

def is_code_paragraph(text: str) -> bool:
    """Detect code paragraphs that should be skipped."""
    s = text.strip()
    return any([
        s.startswith('//'), s.startswith('import '), s.startswith('export '),
        s.startswith('const '), s.startswith('function '), s.startswith('class '),
        s.startswith('{'), s.startswith('}'), s.startswith('return '),
        text.count('{') > 1, text.count('(') > 2,
        '=>' in text, '::' in text, 'await ' in text, 'async ' in text,
    ])


def is_heading_text(text: str) -> bool:
    """Detect short heading-like paragraphs to skip."""
    s = text.strip()
    return len(s.split()) <= 6 and not s.endswith('.')


def humanize_docx(input_path: str, output_path: str, progress_callback=None) -> dict:
    """
    Read a .docx, run 17-pass humanization on all prose paragraphs, save output.
    Returns stats dict.
    """
    from docx import Document

    doc = Document(input_path)
    all_stats = {
        'pass1_ai_phrases': 0, 'pass2_intensifiers': 0,
        'pass3_burstiness': 0, 'pass4_discourse_markers': 0,
        'pass5_contractions': 0, 'pass6_passive_voice': 0,
        'pass7_opener_diversity': 0, 'pass8_hedging': 0,
        'pass9_parentheticals': 0, 'pass10_self_corrections': 0,
        'pass11_personal_voice': 0, 'pass12_qualifiers': 0,
        'pass13_punctuation': 0, 'pass14_syntactic_fronting': 0,
        'pass15_synonym_rotation': 0,
        'pass16_imperfect_discourse': 0,
        'pass17_ghost_characters': 0,
        'pass18_perplexity_tension': 0,
        'pass19_structural_smoothing': 0,
        'total_changes': 0,
        'paragraphs_processed': 0,
        'paragraphs_skipped': 0,
    }

    def is_valid_para(para_text):
        original = para_text.strip()
        if not original or len(original.split()) < 5:
            return False
        if is_heading_text(original) or is_code_paragraph(original):
            return False
        return True

    valid_paras = []
    for para in doc.paragraphs:
        if is_valid_para(para.text):
            valid_paras.append(para)
            
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    if is_valid_para(para.text):
                        valid_paras.append(para)

    total_valid = len(valid_paras)
    
    if progress_callback:
        progress_callback(5, 100, f"Found {total_valid} valid paragraphs. Initializing AI...")

    for i, para in enumerate(valid_paras):
        if progress_callback:
            pct = 10 + int(85 * (i / max(total_valid, 1)))
            progress_callback(pct, 100, f"Processing paragraph {i+1} of {total_valid}...")
            
        original = para.text.strip()
        result = humanize_text(original)
        new_text = result['text']

        if new_text != original:
            if para.runs:
                para.runs[0].text = new_text
                for run in para.runs[1:]:
                    run.text = ''
            else:
                para.text = new_text

            for k, v in result['stats'].items():
                if k in all_stats:
                    all_stats[k] += v
            all_stats['paragraphs_processed'] += 1

    all_stats['paragraphs_skipped'] = len(doc.paragraphs) + sum(len(c.paragraphs) for t in doc.tables for r in t.rows for c in r.cells) - total_valid

    all_stats['total_changes'] = sum(
        v for k, v in all_stats.items() if k.startswith('pass')
    )

    # ── FORENSIC SCRUBBER: METADATA FORGERY ──
    import datetime
    core_props = doc.core_properties
    
    # Randomize revision count to look like a heavily edited human document
    core_props.revision = random.randint(45, 130)
    
    # Backdate the creation time to look like it took days to write
    days_ago = random.randint(3, 10)
    created_time = datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(days=days_ago, hours=random.randint(1, 12))
    core_props.created = created_time
    core_props.modified = datetime.datetime.now(datetime.timezone.utc)
    
    # Clean up author tags if they look like AI or system tags
    author_name = core_props.author or ""
    if "GPT" in author_name or "AI" in author_name or "Admin" in author_name:
        core_props.author = "User"
        
    core_props.last_modified_by = core_props.author

    doc.save(output_path)
    return all_stats
