"""Test the full pipeline with perplexity-guided perturbation."""
import os, sys
sys.path.insert(0, '.')
os.environ['PYTHONIOENCODING'] = 'utf-8'

# Load .env
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

from humanizer.pipeline import humanize_text, preload_model
from humanizer.perplexity import load_perplexity_model, score_text_perplexity
from humanizer.detector import score_text
import json

print("=" * 60)
print("PRELOADING ALL MODELS")
print("=" * 60)
preload_model()
load_perplexity_model()

test_text = """Routines run our lives, yet we barely notice. Daily activities seem minor and repetitive. Waking up to an alarm, taking the same route, chatting with the same people, doing mundane tasks. They blend into the background, invisible. We focus on big events like achievements, celebrations, or sudden changes, while overlooking the small stuff that fills most of our time.

Years later, we see that meaningful outcomes built gradually, not overnight. Skills sharpen through practice, relationships deepen with regular interaction, and personal growth happens through tiny, cumulative adjustments. Major transformations seem dramatic only in hindsight; each step felt routine at the time.

Technology has also reshaped our everyday lives, especially how we access and consume information. Back then, getting info meant library visits, reading newspapers, or talking to experts. Now, info is instant. We hop from topic to topic in seconds. This easy access brings benefits but also new challenges. Constant notifications and digital content fragment our attention, making sustained focus tough. We switch between apps, messages, and projects without realizing how often.

The conversation around tech now is not just about what devices can do, but how they shape our habits, attention, and daily routines. The real question is how we can use technology to support concentration, balance, and meaningful engagement with the world."""

print("\n--- PERPLEXITY BEFORE (original text) ---")
before = score_text_perplexity(test_text)
print(f"  Avg PPL: {before['avg_perplexity']}")
print(f"  Hot sentences: {before['hot_sentence_count']}/{before['total_sentences']}")

print("\n" + "=" * 60)
print("RUNNING FULL PIPELINE")
print("=" * 60)
result = humanize_text(test_text)
humanized = result['text']

print("\n--- HUMANIZED TEXT ---")
for i, para in enumerate(humanized.split('\n')):
    if para.strip():
        print(f"\nParagraph {i+1}: {para}")

print(f"\n--- PIPELINE STATS ---")
print(json.dumps(result['stats'], indent=2))

print("\n--- PERPLEXITY AFTER (humanized text) ---")
after = score_text_perplexity(humanized)
print(f"  Avg PPL: {after['avg_perplexity']} (was {before['avg_perplexity']})")
print(f"  Min PPL: {after['min_perplexity']} (was {before['min_perplexity']})")
print(f"  Variance: {after['variance']} (was {before['variance']})")
print(f"  Hot sentences: {after['hot_sentence_count']}/{after['total_sentences']} (was {before['hot_sentence_count']}/{before['total_sentences']})")

print("\n--- DeBERTa SCORE (humanized) ---")
deberta = score_text(humanized)
print(json.dumps(deberta, indent=2))

print("\n--- DeBERTa SCORE (original, for comparison) ---")
deberta_orig = score_text(test_text)
print(json.dumps(deberta_orig, indent=2))
