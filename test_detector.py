from humanizer.detector import score_text
import json

sample_ai = """In today's digital landscape, it is crucial to recognize that technology plays a pivotal role in spearheading innovation. Furthermore, in order to maximize productivity, organizations must leverage cutting-edge tools to facilitate seamless operations. Meticulously orchestrating these systems fosters a symbiotic relationship between humans and machines, unleashing the power of AI to obtain actionable insights."""

sample_human = """Honestly, I feel like everyone is just obsessed with productivity apps these days. My professor last week was literally going on and on about how 'essential' they are for our future careers, but to be fair, half of them are just distracting. If you actually want things to run smoothly, you just need a simple calendar and a bit of discipline. When people try to overcomplicate it with AI and complicated tools, it usually just ends up wasting more time than it saves. But hey, thats just my two cents."""

print("Scoring AI-generated text...")
res_ai = score_text(sample_ai)
print("AI TEXT RESULT:")
print(json.dumps(res_ai, indent=2))

print("\nScoring human-written text...")
res_human = score_text(sample_human)
print("HUMAN TEXT RESULT:")
print(json.dumps(res_human, indent=2))
