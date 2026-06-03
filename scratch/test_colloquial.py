import os, sys
from humanizer.detector import score_text
import json

colloquial_text = """To be honest, routines pretty much run our lives, even if we don't realize it. Most days are just a repeat of the same small stuff: waking up to an alarm, taking the same route, talking to the same people, and doing mundane tasks. It all just blends into the background after a while. We tend to focus on the big things—like achievements or sudden changes—while ignoring the small habits that fill most of our time. But years later, you realize that the meaningful stuff was built slowly, not overnight. Skills take practice, relationships take regular effort, and growth happens in tiny steps. The big shifts only look dramatic when you're looking back; at the time, every single step felt completely routine.

Actually, technology has also changed how we experience daily life, especially with how we access information. Back in the day, finding info meant visiting the library, reading newspapers, or talking to experts. Now, it's instant. We hop from topic to topic in seconds. This easy access has its benefits, but it also brings new challenges. Constant notifications and digital updates end up fragmenting our attention, making it really hard to focus. We constantly switch between apps and messages without even realizing how often it's happening.

So, the conversation around tech now isn't just about what devices can do, but how they shape our habits and daily routines. The real question is how we can use technology to support concentration, balance, and meaningful engagement with the world around us."""

print("Scoring colloquial human-like text...")
res = score_text(colloquial_text)
print("RESULT:")
print(json.dumps(res, indent=2))
