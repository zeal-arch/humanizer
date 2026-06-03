import os, sys
sys.path.insert(0, '.')
from huggingface_hub import InferenceClient
from humanizer.detector import score_text
import json

env_vars = {}
if os.path.exists(".env"):
    with open(".env", "r") as f:
        for line in f:
            if "=" in line:
                k, v = line.strip().split("=", 1)
                env_vars[k.strip()] = v.strip()

token = env_vars.get("HF_API_TOKEN") or env_vars.get("humanizeread")
if not token:
    print("Error: HF token not found!")
    sys.exit(1)

client = InferenceClient(model="Qwen/Qwen2.5-72B-Instruct", token=token)

original_text = """Because routines rarely feel important while they are happening, citizenry much underestimate how much ordinary routines shape their living. This finding suggests, without question, most days are made up of activity. Seem minor and repetitive: arouse up at a companion clip, travelling the same route, public speaking with the same citizenry, or completing labor that appear insignificant on their own. In light of this, naturally, they can turn most invisible,, you know,. These actions repeat so oftentimes. Sometimes, multitude unremarkably pay attention to large events such as achievements, you know, celebrations, or unexpected changes, while overlooking the wont that occupy most of their clip. When individuals reflect on their lives after various years, they often realize that many meaningful outcomes were built gradually rather than appearing abruptly, Yet. No uncertainty, skills are developed through repeated drill, relationships are strengthened through regular interaction, and personal growth ofttimes occurs through minor adjustments that accumulate over long periods. This finding suggests, frequently, major transformation oftentimes look dramatic only when viewed from a space,. The individual steps that create them seemed ordinary at the time. The evidence indicates, technology has also changed the way people experience ordinary life, peculiarly in how they pass and consume info. These results, no uncertainty, in previous contemporaries, obtaining info ofttimes required deliberate attempt, such as visiting libraries, indication newspapers. Too, speaking directly with knowledgeable individuals. What we 're seeing is: nowadays, info is available almost instantly,. People can move from one topic to another within s. Without question, patch this availability has created many advantages, it has too introduced new challenges. The constant flow of notifications, updates,. Digital content can watershed attending and make sustained focus more difficult. Many individual have noticed that they switch between applications, messages,. Project without realizing how frequently these interruptions occur. As a result, discussions approximately engineering increasingly focus not only on what devices can do. Also on how they work habits, attention, and daily behavior. Building upon this, surprisingly, the question is no longer simply whether technology improves life, but as well how citizenry can use it in a way that supports concentration, equilibrium, and meaningful conflict with the world around them."""

styles = {
    "Sophisticated_Essayist": """You are an expert academic essayist and writer. Rewrite the following text to make it sound completely human, organic, and natural.
Follow these rules strictly:
1. Write in a sophisticated, intellectual, yet natural tone. Use clear and precise language.
2. ENFORCE HIGH BURSTINESS: Make sentence lengths vary dramatically. Follow a long, multi-clause sentence (e.g. 25-35 words) with a short, punchy sentence (e.g. 3-6 words). Never write sentences of similar lengths back-to-back.
3. USE ORGANIC SYNTAX: Use dashes (—), semicolons (;), or parentheses naturally to break up sentences and add complexity, just like a human writer would.
4. BAN ALL AI filler words, transitions, and phrases (e.g. 'Furthermore', 'Moreover', 'In addition', 'Consequently', 'Indeed', 'Tapestry', 'Testament', 'Delve', 'Pivotal', 'Leverage', 'However', 'Therefore', 'So', 'Honestly', 'Basically').
5. Keep the exact meaning and facts of the original text. Output ONLY the raw rewritten text, no intro, no comments.""",

    "Direct_Journalistic": """You are an investigative journalist. Rewrite the following text to make it sound human, punchy, and highly engaging.
Follow these rules strictly:
1. Write in a direct, active, and clean style. Cut all unnecessary words.
2. High sentence length variance: mix short sentences with longer ones. Keep the rhythm unpredictable.
3. Use active voice and strong verbs (e.g., "Routines run our lives" instead of "Our lives are shaped by routines").
4. Ban all AI-like transitions, signposting, or concluding summary phrases (like 'In conclusion', 'Ultimately', 'The real question is'). Just state facts and thoughts directly.
5. Keep the exact meaning and facts. Output ONLY the raw rewritten text, no markdown, no intro.""",

    "Natural_Academic": """You are a university professor writing a reflective piece. Rewrite the following text to make it sound human-written.
Rules:
1. Write in a thoughtful, academic, but accessible style.
2. Avoid uniform sentences. Vary the structure: use introductory clauses, question-answer pairs, or parallel structures that are slightly offset.
3. Do not use AI clichés or logical transition signals.
4. Keep the exact meaning and facts. Output ONLY the raw rewritten text."""
}

results = {}
for name, system_prompt in styles.items():
    print(f"\nGenerating rewrite for {name}...")
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Please rewrite this text:\n\n{original_text}"}
    ]
    response = client.chat_completion(
        messages=messages,
        max_tokens=800,
        temperature=0.95,
        top_p=0.90
    )
    rewritten_text = response.choices[0].message.content.strip()
    
    # Strip thoughts or quotes
    import re
    rewritten_text = re.sub(r'<think>.*?</think>', '', rewritten_text, flags=re.DOTALL).strip()
    rewritten_text = re.sub(r'^(Rewritten|Output|Here is|Here\'s|Result)[:\s]+', '', rewritten_text, flags=re.IGNORECASE).strip()
    
    print(f"Scoring {name}...")
    score = score_text(rewritten_text)
    
    results[name] = {
        "text": rewritten_text,
        "score": score
    }

print("\n" + "="*50)
print("FINAL RESULTS")
print("="*50)
for name, res in results.items():
    print(f"\nStyle: {name}")
    print(f"Overall AI Probability: {res['score']['overall_pct']}%")
    print(f"Label: {res['score']['label']}")
    print(f"Text snippet: {res['text'][:120]}...")
