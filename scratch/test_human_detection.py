import os, sys
sys.path.insert(0, '.')
from humanizer.detector import score_text
import json

human_text = """I've always found that routines are one of those things you don't really think about until they're gone. Like, you wake up, get your coffee, head to work, and it just feels like background noise. But then something changes—you get a new job or move to a different city—and suddenly you realize how much those tiny habits were actually keeping you grounded. It's the small stuff that really defines our days, not just the big milestones.

Actually, technology has made this even more obvious. I remember when finding a recipe meant looking through an actual cookbook or asking my mom. Now I just Google it in two seconds. It's incredibly convenient, sure, but it also means my attention span is absolutely shot. I'll be in the middle of reading an article and suddenly find myself checking Instagram for no reason. It's a constant struggle to just stay focused on one thing at a time."""

print("Scoring human-written text...")
res = score_text(human_text)
print("RESULT:")
print(json.dumps(res, indent=2))
