"""Test the updated pipeline with structural perturbation passes enabled."""
import os, sys
# Manually load .env
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

from humanizer.pipeline import humanize_text, preload_model
from humanizer.detector import score_text
import json

# Preload the model first
print("Preloading model...")
preload_model()

test_text = """Routines run our lives, yet we barely notice. Daily activities seem minor and repetitive—waking up to an alarm, taking the same route, chatting with the same people, doing mundane tasks. They blend into the background, invisible. We focus on big events like achievements, celebrations, or sudden changes, while overlooking the small stuff that fills most of our time.

Years later, we see that meaningful outcomes built gradually, not overnight. Skills sharpen through practice, relationships deepen with regular interaction, and personal growth happens through tiny, cumulative adjustments. Major transformations seem dramatic only in hindsight; each step felt routine at the time.

Technology has also reshaped our everyday lives, especially how we access and consume information. Back then, getting info meant library visits, reading newspapers, or talking to experts. Now, info is instant. We hop from topic to topic in seconds. This easy access brings benefits but also new challenges. Constant notifications and digital content fragment our attention, making sustained focus tough. We switch between apps, messages, and projects without realizing how often.

The conversation around tech now isn't just about what devices can do, but how they shape our habits, attention, and daily routines. The real question is how we can use technology to support concentration, balance, and meaningful engagement with the world."""

print("\n--- Running full humanization pipeline ---")
result = humanize_text(test_text)
humanized = result['text']
print("\nHUMANIZED TEXT:")
print(humanized)
print(f"\nSTATS: {json.dumps(result['stats'], indent=2)}")

print("\n--- Scoring with DeBERTa detector ---")
score = score_text(humanized)
print(f"SCORE: {json.dumps(score, indent=2)}")

print("\n--- Scoring ORIGINAL for comparison ---")
score_orig = score_text(test_text)
print(f"ORIGINAL SCORE: {json.dumps(score_orig, indent=2)}")
