from humanizer.detector import score_text
import json

failed_text = """Routines don't seem that important while they're happening, but they really shape our lives. Most days are just activities that seem small and repetitive, like waking up to an alarm, taking the same route, chatting with the same people, or doing tasks that feel innotable. But these things become invisible because they happen so often. We tend to focus on big events like achievements, celebrations, or sudden changes, but overlook the routine stuff that fills most of our time. Looking back, we realize that meaningful stuff builds up gradually, not all at once. Skills get better with practice, relationships grow stronger with regular contact, and personal growth happens through small changes over time. Big transformations only look dramatic in hindsight; the steps felt normal at the moment. Tech has also changed our everyday lives, especially how we get and use info. Before, getting info took effort—like going to libraries or reading newspapers. Now, info is instant. You can jump from one topic to another super quickly. While this has its perks, it's brought new challenges too. Constant notifications and digital content can scatter your attention and make focusing hard. A lot of us find ourselves switching between apps, messages, and projects without even noticing. So, talks about tech aren't just about what gadgets can do, but how they affect our habits, attention, and daily life. The real question now is how we can use tech to support concentration, balance, and meaningful interactions with the world."""

print("Scoring failed humanized text...")
res = score_text(failed_text)
print("RESULT:")
print(json.dumps(res, indent=2))
