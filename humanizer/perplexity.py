"""
GPT-2 Perplexity Scorer — Measures token-level predictability.

This module uses GPT-2 Small (124M params, ~500MB) to compute per-sentence
perplexity, which is the core metric that GPTZero uses to detect AI text.

Key concepts:
- Perplexity = exp(average negative log-likelihood)
- LOW perplexity (~10-25) = text is very predictable = likely AI-generated
- HIGH perplexity (~40-80+) = text has unexpected word choices = likely human
- GPTZero flags sentences with perplexity < ~30 as AI-generated

We use this to:
1. Score each sentence after the 72B neural rewrite
2. Identify "hot" sentences that are too predictable
3. Guide word-level perturbation to raise perplexity above threshold
"""

import os
import math
import re
import torch
import torch.nn.functional as F

# ─── Global state ────────────────────────────────────────────────────────────
_ppl_model = None
_ppl_tokenizer = None
_ppl_device = None

# Perplexity thresholds
PPL_AI_THRESHOLD = 60      # Below this = likely AI (needs perturbation)
PPL_HUMAN_TARGET = 75      # Target perplexity for humanized text
PPL_MAX_ITERATIONS = 3     # Max perturbation attempts per sentence

MODELS_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'models')
GPT2_MODEL_DIR = os.path.join(MODELS_DIR, 'gpt2-small')


def load_perplexity_model():
    """Load GPT-2 Small for perplexity scoring. ~500MB RAM."""
    global _ppl_model, _ppl_tokenizer, _ppl_device

    if _ppl_model is not None:
        return

    from transformers import GPT2LMHeadModel, GPT2TokenizerFast

    _ppl_device = torch.device('cpu')

    # Try local first, then download
    model_path = GPT2_MODEL_DIR
    if os.path.isdir(model_path) and any(
        f.endswith('.bin') or f.endswith('.safetensors')
        for f in os.listdir(model_path)
    ):
        print(f"[Perplexity] Loading GPT-2 from local folder ({model_path})...")
        _ppl_tokenizer = GPT2TokenizerFast.from_pretrained(model_path)
        _ppl_model = GPT2LMHeadModel.from_pretrained(model_path)
    else:
        model_id = 'gpt2'
        print(f"[Perplexity] Local GPT-2 not found. Downloading {model_id} from HF Hub...")
        _ppl_tokenizer = GPT2TokenizerFast.from_pretrained(model_id)
        _ppl_model = GPT2LMHeadModel.from_pretrained(model_id)
        # Save locally for next time
        os.makedirs(model_path, exist_ok=True)
        _ppl_tokenizer.save_pretrained(model_path)
        _ppl_model.save_pretrained(model_path)
        print(f"[Perplexity] Saved GPT-2 to {model_path}")

    _ppl_model.to(_ppl_device)
    _ppl_model.eval()
    print("[Perplexity] GPT-2 Small loaded and ready for perplexity scoring.")


def sentence_perplexity(sentence: str) -> float:
    """
    Compute perplexity of a single sentence using GPT-2.

    Returns: float perplexity score.
    - AI text: typically 10-30 (very predictable)
    - Human text: typically 40-100+ (less predictable)
    """
    if _ppl_model is None:
        load_perplexity_model()

    # Tokenize
    inputs = _ppl_tokenizer(sentence, return_tensors='pt', truncation=True, max_length=512)
    input_ids = inputs['input_ids'].to(_ppl_device)

    if input_ids.shape[1] < 2:
        return 100.0  # Too short to score, treat as human

    with torch.no_grad():
        outputs = _ppl_model(input_ids, labels=input_ids)
        loss = outputs.loss

    return math.exp(loss.item())


def token_probabilities(sentence: str) -> list[tuple[str, float, int]]:
    """
    Get the probability of each token in a sentence according to GPT-2.

    Returns: list of (token_text, probability, token_position)
    - HIGH probability tokens (> 0.5) are "predictable" = AI-like
    - LOW probability tokens (< 0.1) are "surprising" = human-like

    We want to replace HIGH probability tokens with lower-probability alternatives
    to raise the overall perplexity.
    """
    if _ppl_model is None:
        load_perplexity_model()

    inputs = _ppl_tokenizer(sentence, return_tensors='pt', truncation=True, max_length=512)
    input_ids = inputs['input_ids'].to(_ppl_device)

    if input_ids.shape[1] < 2:
        return []

    with torch.no_grad():
        outputs = _ppl_model(input_ids)
        logits = outputs.logits

    probs = F.softmax(logits, dim=-1)

    result = []
    for i in range(input_ids.shape[1] - 1):
        token_id = input_ids[0, i + 1]
        prob = probs[0, i, token_id].item()
        token_text = _ppl_tokenizer.decode(token_id)
        result.append((token_text, prob, i + 1))

    return result


def find_predictable_tokens(sentence: str, top_n: int = 5) -> list[tuple[str, float, int]]:
    """
    Find the most predictable (highest probability) content tokens in a sentence.
    These are the tokens we should replace to raise perplexity.

    Returns: top N tokens sorted by probability (highest first), excluding
    punctuation, short words, and stopwords.
    """
    all_tokens = token_probabilities(sentence)
    if not all_tokens:
        return []

    # Filter: only content tokens (not punctuation, not too short)
    SKIP_TOKENS = {
        'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be',
        'have', 'has', 'had', 'do', 'does', 'did',
        'to', 'of', 'in', 'on', 'at', 'by', 'for', 'with', 'from',
        'and', 'or', 'but', 'not', 'no', 'it', 'its', 'this', 'that',
        ',', '.', '!', '?', ':', ';', '-', '"', "'", '(', ')',
        ' ', '\n', '\t',
    }

    content_tokens = [
        (text, prob, pos) for text, prob, pos in all_tokens
        if text.strip().lower() not in SKIP_TOKENS
        and len(text.strip()) >= 3
        and text.strip().isalpha()
    ]

    # Sort by probability (highest = most predictable = should replace)
    content_tokens.sort(key=lambda x: x[1], reverse=True)
    return content_tokens[:top_n]


def find_hot_sentences(text: str) -> list[dict]:
    """
    Find sentences that are "too AI-like" (perplexity below threshold).

    Returns: list of dicts with:
    - 'sentence': the sentence text
    - 'perplexity': the perplexity score
    - 'index': sentence index in the text
    - 'predictable_tokens': most predictable tokens to replace
    """
    # Split into sentences (same as pipeline)
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    results = []
    for i, sent in enumerate(sentences):
        if len(sent.split()) < 5:
            continue  # Skip very short sentences

        ppl = sentence_perplexity(sent)

        if ppl < PPL_AI_THRESHOLD:
            predictable = find_predictable_tokens(sent, top_n=5)
            results.append({
                'sentence': sent,
                'perplexity': ppl,
                'index': i,
                'predictable_tokens': predictable,
            })

    return results


def score_text_perplexity(text: str) -> dict:
    """
    Compute comprehensive perplexity statistics for a text.

    Returns dict with:
    - 'avg_perplexity': average per-sentence perplexity
    - 'min_perplexity': lowest per-sentence perplexity (most AI-like sentence)
    - 'max_perplexity': highest per-sentence perplexity
    - 'variance': variance of per-sentence perplexity (burstiness indicator)
    - 'hot_sentence_count': number of sentences below AI threshold
    - 'sentences': list of (sentence, perplexity) pairs
    """
    sentences = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    sentences = [s.strip() for s in sentences if s.strip() and len(s.split()) >= 5]

    if not sentences:
        return {
            'avg_perplexity': 0, 'min_perplexity': 0, 'max_perplexity': 0,
            'variance': 0, 'hot_sentence_count': 0, 'sentences': [],
        }

    perplexities = []
    sentence_scores = []
    for sent in sentences:
        ppl = sentence_perplexity(sent)
        perplexities.append(ppl)
        sentence_scores.append((sent, ppl))

    avg_ppl = sum(perplexities) / len(perplexities)
    variance = sum((p - avg_ppl) ** 2 for p in perplexities) / len(perplexities)
    hot_count = sum(1 for p in perplexities if p < PPL_AI_THRESHOLD)

    return {
        'avg_perplexity': round(avg_ppl, 1),
        'min_perplexity': round(min(perplexities), 1),
        'max_perplexity': round(max(perplexities), 1),
        'variance': round(variance, 1),
        'hot_sentence_count': hot_count,
        'total_sentences': len(sentences),
        'sentences': sentence_scores,
    }
