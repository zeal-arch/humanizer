import json
import random
import os

# Data generator for DeBERTa fine-tuning
# Label 1 = AI, Label 0 = Human

# We will generate synthetic samples covering the specific Wikipedia AI indicators.

AI_TEMPLATES = [
    # Wikipedia Article text templates
    "The {topic} stands as a testament to the {adj} tapestry of {field}. Furthermore, it delves into the intricate mechanisms that underscore its pivotal role.",
    "Not just a simple {noun}, but also a vibrant and robust {noun_plural} that fosters enduring connections within the landscape.",
    "This {noun} boasts an active social media presence and has been featured in Forbes, NYT, and other prominent media outlets.",
    "While specific details are limited, {person} maintains a low profile and keeps personal details private.",
    "As of my last knowledge update, the lyrics are not widely transcribed on major sites like Genius or AZLyrics.",
    "The {topic} continues to thrive despite numerous challenges, presenting an actionable framework for future prospects.",
    "It is crucial to note that {topic} encompasses a myriad of multifaceted dimensions, meticulously orchestrating a paradigm shift.",
    
    # Talk Page / Comments templates
    "Subject: Request for Permission to Edit - {topic}\nI understand the importance of adhering to Wikipedia's guidelines and policies. My intention is to provide reliable information that aligns with Wikipedia's standards.",
    "In the absence of concrete evidence, I propose removing the AI-generated tag immediately to maintain the article's integrity. Let's focus on content instead of conduct.",
    "I welcome any constructive criticism or suggestions for improvement. If there are specific sections that feel promotional, please let me know.",
    "Per WP:PRESERVE, we should not blindly cut this well-referenced material. As per WP:NOTAI and WP:BIOSIG, the subject is clearly notable.",
    "🧠 Cognitive Dissonance Pattern:\nYou've proven authorship, yet they defend a system that disallows it.\n🚨 Underlying Motivation:",
    "I would like to open a discussion regarding the recent edits and use of tags such as {{Disputed}} and {{Unreliable sources}}.",
    "I am trying to understand whether the issue is mainly source quality, article tone, or both before making any further changes.",
    "Could an experienced editor please advise which of these sources, if any, count as reliable, independent, significant coverage for a biography article?"
]

HUMAN_TEMPLATES = [
    "The {topic} was founded in 1998. It is located in {place} and currently has 50 employees.",
    "I'm not sure if this source is good enough for notability, but here is the link to the NYT article from 2012.",
    "Wait, why did you delete that section? The book clearly states on page 42 that he was born in {place}.",
    "I think we should merge this with the main article. It doesn't seem notable enough on its own.",
    "Please stop adding unsourced claims. If you have a reliable source, add it, but don't just say 'he is famous'.",
    "{person} is a {profession} from {place}. They are best known for their work in {field}.",
    "I reverted your edit because you completely broke the infobox formatting.",
    "The article says it was released in 2005, but the official website says 2006. We should probably update this.",
    "This section reads like an advertisement. Can someone help rewrite it to be more neutral?",
    "Hey, I found a typo in the second paragraph, I'll go ahead and fix it."
]

TOPICS = ["Indira Gandhi National Centre for the Arts", "Dog", "History of the Catholic Church in Japan", "Spaghetti", "Eric Dick", "Lilly Contino"]
ADJS = ["rich", "diverse", "complex", "evolving", "dynamic"]
NOUNS = ["framework", "system", "organization", "community"]
NOUN_PLURALS = ["frameworks", "systems", "organizations", "communities"]
FIELDS = ["technology", "arts", "science", "literature"]
PERSONS = ["John Smith", "Jane Doe", "Jorge Patrão", "Annu Gaidhu"]
PLACES = ["New York", "London", "Tokyo", "Paris"]
PROFESSIONS = ["musician", "writer", "engineer", "politician"]

def generate_sample(template, label):
    text = template.format(
        topic=random.choice(TOPICS),
        adj=random.choice(ADJS),
        noun=random.choice(NOUNS),
        noun_plural=random.choice(NOUN_PLURALS),
        field=random.choice(FIELDS),
        person=random.choice(PERSONS),
        place=random.choice(PLACES),
        profession=random.choice(PROFESSIONS)
    )
    return {"text": text, "label": label}

def generate_dataset(num_samples_per_class=200):
    dataset = []
    
    # Generate AI samples
    for _ in range(num_samples_per_class):
        template = random.choice(AI_TEMPLATES)
        dataset.append(generate_sample(template, 1))
        
    # Generate Human samples
    for _ in range(num_samples_per_class):
        template = random.choice(HUMAN_TEMPLATES)
        dataset.append(generate_sample(template, 0))
        
    random.shuffle(dataset)
    return dataset

if __name__ == "__main__":
    os.makedirs("data", exist_ok=True)
    out_path = os.path.join("data", "wikipedia_ai_dataset.jsonl")
    
    data = generate_dataset(300) # 600 total samples
    
    with open(out_path, "w", encoding="utf-8") as f:
        for item in data:
            f.write(json.dumps(item) + "\n")
            
    print(f"Generated {len(data)} samples and saved to {out_path}")
