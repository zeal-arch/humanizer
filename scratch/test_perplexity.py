"""Test the GPT-2 perplexity scorer on known AI vs human text."""
import os, sys
sys.path.insert(0, '.')
os.environ['PYTHONIOENCODING'] = 'utf-8'

from humanizer.perplexity import (
    load_perplexity_model, sentence_perplexity, 
    find_hot_sentences, score_text_perplexity,
    find_predictable_tokens
)

print("=" * 60)
print("LOADING GPT-2 PERPLEXITY MODEL")
print("=" * 60)
load_perplexity_model()

# Test 1: Known AI-like text (should have LOW perplexity)
ai_sentences = [
    "The importance of education cannot be overstated in modern society.",
    "Technology has transformed the way we communicate and interact with each other.",
    "In conclusion, it is clear that climate change poses significant challenges.",
    "Furthermore, the implementation of these strategies requires careful planning.",
    "The results of this study demonstrate a significant correlation between the variables.",
]

# Test 2: Known human-like text (should have HIGHER perplexity)
human_sentences = [
    "Look, I get that school matters but honestly some days it just feels pointless.",
    "My phone basically runs my life at this point which is kinda scary ngl.",
    "Climate stuff freaks me out but like what am I supposed to do about it?",
    "We tried doing it the other way first and it was a total disaster lol.",
    "The numbers looked weird so I just eyeballed it and moved on.",
]

print("\n" + "=" * 60)
print("TEST 1: AI-LIKE TEXT (should be LOW perplexity < 35)")
print("=" * 60)
for s in ai_sentences:
    ppl = sentence_perplexity(s)
    label = "[AI]" if ppl < 35 else "[HUMAN]"
    print(f"  {label} PPL={ppl:.1f} | {s[:70]}...")

print("\n" + "=" * 60)
print("TEST 2: HUMAN-LIKE TEXT (should be HIGHER perplexity > 35)")
print("=" * 60)
for s in human_sentences:
    ppl = sentence_perplexity(s)
    label = "[AI]" if ppl < 35 else "[HUMAN]"
    print(f"  {label} PPL={ppl:.1f} | {s[:70]}...")

# Test 3: Find predictable tokens in an AI sentence
print("\n" + "=" * 60)
print("TEST 3: MOST PREDICTABLE TOKENS (to replace)")
print("=" * 60)
test_sent = "The importance of education cannot be overstated in modern society."
tokens = find_predictable_tokens(test_sent, top_n=8)
print(f"  Sentence: {test_sent}")
for tok, prob, pos in tokens:
    print(f"    Token: '{tok}' -> probability {prob:.3f} (position {pos})")

# Test 4: Score the actual humanized output from our pipeline
print("\n" + "=" * 60)
print("TEST 4: ACTUAL PIPELINE OUTPUT")
print("=" * 60)
pipeline_output = """Routines totally shape our days, but we hardly even notice. Stuff like waking up to the same alarm, driving the usual route, having those daily chats, doing the same old tasks it all becomes background noise. We get so caught up in the big moments, like promotions or parties, that we miss out on all the small things that actually make up most of our day-to-day life. Years later, we realize big changes take time. Skills get sharp with practice, friendships grow deeper with hangouts and we evolve bit by bit. The big shifts only seem dramatic when you look back. At the time, each step just felt normal, kinda routine. Tech has totally changed our daily lives, specially how we get info. Used to be, you had to go to the library, read newspapers, or talk to experts. Now, boom, info is right there in seconds. We jump from one thing to another super fast. It is great, but it comes with its own set of problems. With all the constant notifications and digital stuff, it is hard to stay focused on one thing. We are constantly switching between apps, messages, and tasks without even noticing how much. Talk about tech these days; it is not just about the gadgets anymore. It is all about how they influence our habits, focus, and day-to-day life. The big question now is, how do we use tech to help us concentrate better, find a good balance, and really connect with the world around us?"""

result = score_text_perplexity(pipeline_output)
print(f"  Avg perplexity: {result['avg_perplexity']}")
print(f"  Min perplexity: {result['min_perplexity']} (most AI-like)")
print(f"  Max perplexity: {result['max_perplexity']} (most human-like)")
print(f"  Variance: {result['variance']} (burstiness)")
print(f"  Hot sentences: {result['hot_sentence_count']}/{result['total_sentences']}")
print()
for sent, ppl in result['sentences']:
    label = "[AI]" if ppl < 35 else "[EDGE]" if ppl < 55 else "[HUMAN]"
    print(f"  {label} PPL={ppl:.1f} | {sent[:80]}...")
