import os
from huggingface_hub import InferenceClient
from humanizer.detector import score_text
import json

# Read .env file manually
env_vars = {}
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                env_vars[k.strip()] = v.strip()

token = env_vars.get("HF_API_TOKEN") or env_vars.get("humanizeread")
if not token:
    print("Error: No HF token found in .env!")
    exit(1)

client = InferenceClient(model="Qwen/Qwen2.5-72B-Instruct", token=token)

original_text = """Because routines rarely feel important while they are happening, citizenry much underestimate how much ordinary routines shape their living. This finding suggests, without question, most days are made up of activity. Seem minor and repetitive: arouse up at a companion clip, travelling the same route, public speaking with the same citizenry, or completing labor that appear insignificant on their own. In light of this, naturally, they can turn most invisible,, you know,. These actions repeat so oftentimes. Sometimes, multitude unremarkably pay attention to large events such as achievements, you know, celebrations, or unexpected changes, while overlooking the wont that occupy most of their clip. When individuals reflect on their lives after various years, they often realize that many meaningful outcomes were built gradually rather than appearing abruptly, Yet. No uncertainty, skills are developed through repeated drill, relationships are strengthened through regular interaction, and personal growth ofttimes occurs through minor adjustments that accumulate over long periods. This finding suggests, frequently, major transformation oftentimes look dramatic only when viewed from a space,. The individual steps that create them seemed ordinary at the time. The evidence indicates, technology has also changed the way people experience ordinary life, peculiarly in how they pass and consume info. These results, no uncertainty, in previous contemporaries, obtaining info ofttimes required deliberate attempt, such as visiting libraries, indication newspapers. Too, speaking directly with knowledgeable individuals. What we 're seeing is: nowadays, info is available almost instantly,. People can move from one topic to another within s. Without question, patch this availability has created many advantages, it has too introduced new challenges. The constant flow of notifications, updates,. Digital content can watershed attending and make sustained focus more difficult. Many individual have noticed that they switch between applications, messages,. Project without realizing how frequently these interruptions occur. As a result, discussions approximately engineering increasingly focus not only on what devices can do. Also on how they work habits, attention, and daily behavior. Building upon this, surprisingly, the question is no longer simply whether technology improves life, but as well how citizenry can use it in a way that supports concentration, equilibrium, and meaningful conflict with the world around them."""

# We will test two paragraphs from the text
paras = [p.strip() for p in original_text.split("\n\n") if p.strip()]

prompt_instructions = """You are a regular person writing a casual blog post or email. Rewrite the following text paragraph-by-paragraph to make it sound completely human, organic, and natural.
Follow these CRITICAL styling rules to bypass advanced AI detectors:
1. Use an informal, conversational, and slightly unpolished human tone. Write like a student reflecting on their thoughts.
2. ENFORCE HIGH BURSTINESS (SENTENCE LENGTH VARIATION): Mix very short, punchy sentences (e.g. 2-6 words) with medium and occasionally long sentences. Never use consecutive sentences of the same length or structure.
3. INJECT NATURAL IMPERFECTIONS: Use contractions (don't, can't, it's, we're) constantly. Add natural conversational markers/phrases occasionally (e.g., "Honestly,", "Basically,", "Like,", "I mean,", "kind of", "pretty much").
4. AVOID ROBOTIC AI TRANSITIONS: Ban all logical connectors like "Furthermore", "In addition", "Therefore", "Moreover", "Consequently", "While X...", "So...". Start sentences directly.
5. SHATTER PREDICTABLE PATTERNS: Do not use balanced parallel structures (e.g. "X does Y, A does B, and C does D").
6. Keep the exact core meaning, facts, and info from the original text, but present it in a relaxed, personal voice.

Output ONLY the raw rewritten paragraph. Do not include any introductory text, quotes, or markdown formatting."""

rewritten_paras = []
for idx, para in enumerate(paras):
    print(f"\n--- Rewriting Paragraph {idx+1} ---")
    messages = [
        {"role": "system", "content": "You are a human writer. You rewrite texts to sound completely natural, informal, and bursty. Do not explain anything, output only the rewritten text."},
        {"role": "user", "content": f"{prompt_instructions}\n\nOriginal text:\n{para}\n\nHuman rewrite:"}
    ]
    response = client.chat_completion(
        messages=messages,
        max_tokens=400,
        temperature=0.95,
        top_p=0.90
    )
    result = response.choices[0].message.content.strip()
    print("OUTPUT:")
    print(result)
    rewritten_paras.append(result)

full_rewritten = "\n\n".join(rewritten_paras)
print("\n=== SCORING FULL REWRITTEN TEXT ===")
res = score_text(full_rewritten)
print(json.dumps(res, indent=2))
