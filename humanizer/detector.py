# humanizer/detector.py
# Rule-based AI probability scorer — mirrors the signals Turnitin measures
# Zero AI API calls — purely statistical/heuristic

import re
import math
from .phrases import AI_PHRASES, INTENSIFIERS


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 1 — AI Phrase Density
# Count how many known AI phrases exist per 100 words
# ─────────────────────────────────────────────────────────────────────────────

def _ai_phrase_density(text: str) -> float:
    """
    Returns a 0.0–1.0 score based on how many AI phrases per 100 words.
    Saturates at ~12 hits per 100 words = 1.0
    """
    word_count = max(len(text.split()), 1)
    hits = 0
    combined = {**AI_PHRASES, **INTENSIFIERS}
    lower_text = text.lower()
    for phrase in combined:
        count = lower_text.count(phrase.lower())
        hits += count

    # Normalize: 12 hits per 100 words → score of 1.0
    density = (hits / word_count) * 100
    return min(density / 12.0, 1.0)


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 2 — Burstiness (sentence length variance)
# Humans have high variance in sentence length. AI flatlines.
# ─────────────────────────────────────────────────────────────────────────────

def _tokenize_sentences(text: str) -> list[str]:
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z])', text)
    return [p.strip() for p in parts if p.strip() and len(p.split()) > 2]


def _burstiness_score(text: str) -> float:
    """
    Returns 0.0–1.0 where 1.0 = very AI-like (low burstiness).
    Low std dev in sentence length → higher AI score.
    """
    sentences = _tokenize_sentences(text)
    if len(sentences) < 4:
        return 0.5  # not enough data

    lengths = [len(s.split()) for s in sentences]
    mean = sum(lengths) / len(lengths)
    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    std_dev = math.sqrt(variance)

    # Human text typically has std_dev > 12 words
    # AI text typically has std_dev < 7 words
    # Map: std_dev=0 → score=1.0, std_dev=15 → score=0.0
    ai_score = max(0.0, min(1.0, 1.0 - (std_dev / 15.0)))
    return ai_score


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 3 — Paragraph Opener Uniformity
# AI starts many paragraphs with "The", "This", "In", "It"
# ─────────────────────────────────────────────────────────────────────────────

AI_OPENERS = {
    "the ", "this ", "these ", "those ", "in ", "it ", "by ", "with ",
    "as ", "one ", "another ", "such ", "each ", "every "
}

def _opener_uniformity(text: str) -> float:
    """
    Returns 0.0–1.0 where 1.0 = all paragraphs start with AI opener words.
    """
    paragraphs = [p.strip() for p in text.split('\n') if len(p.strip().split()) >= 5]
    if not paragraphs:
        return 0.5

    ai_starts = sum(
        1 for p in paragraphs
        if any(p.lower().startswith(op) for op in AI_OPENERS)
    )
    return ai_starts / max(len(paragraphs), 1)


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 4 — Average sentence length
# AI tends to write sentences of 20–35 words, very consistently
# Humans write shorter AND longer sentences
# ─────────────────────────────────────────────────────────────────────────────

def _avg_sentence_length_score(text: str) -> float:
    """
    Returns 0.0–1.0. Sentences clustered between 20-35 words = AI-like.
    """
    sentences = _tokenize_sentences(text)
    if not sentences:
        return 0.5

    lengths = [len(s.split()) for s in sentences]
    avg = sum(lengths) / len(lengths)

    # AI sweet spot: 22–32 words avg → score near 1.0
    # Very short (<12) or very long (>40) → more human-like
    if 20 <= avg <= 35:
        return 0.85
    elif 15 <= avg < 20 or 35 < avg <= 40:
        return 0.55
    else:
        return 0.2


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 5 — Intensifier / filler word density
# ─────────────────────────────────────────────────────────────────────────────

FILLER_WORDS = [
    "very", "quite", "extremely", "highly", "incredibly", "absolutely",
    "essentially", "fundamentally", "primarily", "significantly", "substantially",
    "undoubtedly", "undeniably", "seamlessly", "effectively", "efficiently",
    "comprehensive", "robust", "innovative", "leverage", "leveraged", "leveraging",
    "leverages", "utilize", "utilized", "utilizing", "utilizes", "ensure",
    "ensured", "ensuring", "ensures", "facilitate", "facilitated", "facilitating",
    "facilitates", "facilitation", "demonstrate", "demonstrated", "demonstrating",
    "demonstrates", "demonstration", "demonstrations", "implement", "implemented",
    "implementing", "implements", "implementation", "implementations", "paramount",
    "pivotal",
    # Modern AI cliches (GPT-4o, GPT-5, Claude Opus, Gemini) and their variations
    "delve", "delves", "delved", "delving", "tapestry", "tapestries", "myriad",
    "orchestrate", "orchestrates", "orchestrated", "orchestrating", "orchestration",
    "orchestrations", "catalyst", "catalysts", "foster", "fosters", "fostered",
    "fostering", "unleash", "unleashes", "unleashed", "unleashing", "empower",
    "empowers", "empowered", "empowering", "empowerment", "empowerments", "beacon",
    "beacons", "spearhead", "spearheads", "spearheaded", "spearheading", "meticulously",
    "harmonious", "synergize", "synergizes", "synergized", "synergizing", "synergy",
    "synergies", "frictionless", "actionable", "catalyze", "catalyzes", "catalyzed",
    "catalyzing", "democratize", "democratizes", "democratized", "democratizing",
    "democratization", "transformative", "groundbreaking", "cutting-edge", "nuanced",
    "multifaceted", "holistic", "paradigm", "paradigms", "unprecedented", "revolutionize",
    "revolutionizes", "revolutionized", "revolutionizing", "harness", "harnesses",
    "harnessed", "harnessing",
]

def _filler_density(text: str) -> float:
    """
    Returns 0.0–1.0 based on filler word density.
    Saturates at 8 per 100 words = 1.0
    """
    words = text.lower().split()
    if not words:
        return 0.0
    count = sum(1 for w in words if w.strip('.,;:!?') in FILLER_WORDS)
    density = (count / len(words)) * 100
    return min(density / 8.0, 1.0)


# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL 6 — Transition phrase overuse
# AI loves "furthermore", "moreover", "in addition", "additionally"
# ─────────────────────────────────────────────────────────────────────────────

TRANSITION_PHRASES = [
    "furthermore", "moreover", "in addition", "additionally", "consequently",
    "therefore", "thus", "hence", "as a result", "subsequently",
    "in conclusion", "to summarize", "in summary", "last but not least",
    "first and foremost", "it is worth noting", "it should be noted",
    "it is important to note", "needless to say",
]

def _transition_overuse(text: str) -> float:
    """
    Returns 0.0–1.0. Saturates at 3 transitions per 100 words.
    """
    word_count = max(len(text.split()), 1)
    lower = text.lower()
    hits = sum(lower.count(t) for t in TRANSITION_PHRASES)
    density = (hits / word_count) * 100
    return min(density / 3.0, 1.0)


# ─────────────────────────────────────────────────────────────────────────────
# AGGREGATE SCORER
# ─────────────────────────────────────────────────────────────────────────────

# Weights for each signal (must sum to 1.0)
WEIGHTS = {
    'ai_phrases':       0.28,
    'burstiness':       0.25,
    'opener_uniformity':0.15,
    'avg_sent_length':  0.12,
    'filler_density':   0.12,
    'transitions':      0.08,
}

def score_text(text: str) -> dict:
    """
    Score a block of text for AI likelihood.
    Returns dict with individual signal scores and overall percentage.
    """
    if not text or len(text.split()) < 20:
        return {
            'overall_pct': 0,
            'label': 'Insufficient text',
            'signals': {},
        }

    signals = {
        'ai_phrases':        _ai_phrase_density(text),
        'burstiness':        _burstiness_score(text),
        'opener_uniformity': _opener_uniformity(text),
        'avg_sent_length':   _avg_sentence_length_score(text),
        'filler_density':    _filler_density(text),
        'transitions':       _transition_overuse(text),
    }

    weighted = sum(signals[k] * WEIGHTS[k] for k in signals)
    pct = round(weighted * 100)

    if pct >= 75:
        label = 'Very likely AI-generated'
    elif pct >= 50:
        label = 'Likely AI-generated'
    elif pct >= 30:
        label = 'Possibly AI-assisted'
    elif pct >= 15:
        label = 'Mostly human-sounding'
    else:
        label = 'Reads as human-written'

    return {
        'overall_pct': pct,
        'label': label,
        'signals': {k: round(v * 100) for k, v in signals.items()},
    }


# ─────────────────────────────────────────────────────────────────────────────
# DOCX SCORER
# ─────────────────────────────────────────────────────────────────────────────

def score_docx(path: str) -> dict:
    """
    Extract all prose text from a .docx file and score it.
    Returns score dict plus word count and paragraph count.
    """
    from docx import Document

    doc = Document(path)
    prose_blocks = []

    for para in doc.paragraphs:
        t = para.text.strip()
        if t and len(t.split()) >= 5:
            prose_blocks.append(t)

    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for para in cell.paragraphs:
                    t = para.text.strip()
                    if t and len(t.split()) >= 5:
                        prose_blocks.append(t)

    full_text = '\n'.join(prose_blocks)
    word_count = len(full_text.split())
    result = score_text(full_text)
    
    # Score chunks individually
    chunks = []
    for block in prose_blocks:
        block_score = score_text(block)
        chunks.append({
            'text': block,
            'pct': block_score['overall_pct']
        })
        
    result['word_count'] = word_count
    result['paragraph_count'] = len(prose_blocks)
    result['chunks'] = chunks
    return result
