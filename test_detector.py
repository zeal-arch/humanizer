from humanizer.detector import score_text
import json

sample_ai = """In today's digital landscape, it is crucial to recognize that technology plays a pivotal role in spearheading innovation. Furthermore, in order to maximize productivity, organizations must leverage cutting-edge tools to facilitate seamless operations. Meticulously orchestrating these systems fosters a symbiotic relationship between humans and machines, unleashing the power of AI to obtain actionable insights."""

sample_human = """I got up early this morning to walk the dog, and the weather was freezing. I made a quick cup of coffee before heading out the door. The streets were completely empty, except for one guy sweeping the sidewalk in front of the bakery. It was peaceful, but I couldn't wait to get back inside and warm up."""

print("Scoring AI-generated text...")
res_ai = score_text(sample_ai)
print("AI TEXT RESULT:")
print(json.dumps(res_ai, indent=2))

print("\nScoring human-written text...")
res_human = score_text(sample_human)
print("HUMAN TEXT RESULT:")
print(json.dumps(res_human, indent=2))
