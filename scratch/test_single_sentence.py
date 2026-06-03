# scratch/test_single_sentence.py
import os, sys
sys.path.insert(0, '.')

# Load .env
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

from humanizer.pipeline import humanize_text, preload_model
from humanizer.perplexity import load_perplexity_model
from humanizer.detector import score_text
import json

preload_model()
load_perplexity_model()

# A highly robotic AI-style sentence
original_text = "Furthermore, it is highly crucial to recognize that in order to maximize productivity, organizations must leverage cutting-edge tools to facilitate seamless operations."

print("=" * 60)
print("ORIGINAL TEXT:")
print(original_text)
print("=" * 60)

res = humanize_text(original_text)
humanized_text = res['text']

print("\nHUMANIZED TEXT:")
print(humanized_text)
print("=" * 60)

print("\nORIGINAL AI SCORE:")
deberta_orig = score_text(original_text)
print(json.dumps(deberta_orig, indent=2))

print("\nHUMANIZED AI SCORE:")
deberta_hum = score_text(humanized_text)
print(json.dumps(deberta_hum, indent=2))
