from humanizer.detector import score_text
import json
import os
import sys

# Force the detector to reload the model from disk (just in case)
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

samples = [
    {
        "name": "Talk Page Wikilawyering (AI)",
        "text": "Subject: Request for Permission to Edit\nIn the absence of concrete evidence, I propose removing the AI-generated tag immediately to maintain the article's integrity. Let's focus on content instead of conduct. Per WP:PRESERVE, we should not blindly cut this well-referenced material. As per WP:NOTAI and WP:BIOSIG, the subject is clearly notable. I welcome any constructive criticism or suggestions for improvement."
    },
    {
        "name": "Wikipedia Article Era GPT-4 (AI)",
        "text": "The Indira Gandhi National Centre for the Arts stands as a testament to the rich tapestry of Indian cultural heritage. Furthermore, it delves into the intricate mechanisms that underscore its pivotal role in the region. This organization boasts an active social media presence and has been featured in prominent media outlets, meticulously orchestrating a paradigm shift in how we view the arts."
    },
    {
        "name": "Knowledge Cutoff Speculation (AI)",
        "text": "As of my last knowledge update, the lyrics for this album are not widely transcribed on major sites like Genius or AZLyrics. While specific details about his early life are limited, John Smith maintains a low profile and keeps personal details private."
    },
    {
        "name": "Standard Human Revision (Human)",
        "text": "I reverted the recent additions by the IP user because they broke the infobox formatting completely. Also, the claim that the book was released in 2005 is incorrect; the official website clearly says it was 2006. If anyone finds a reliable source for the 2005 claim, please discuss it here before adding it back."
    }
]

def main():
    print("Evaluating Fine-Tuned Detector against Wikipedia AI Patterns...\n")
    
    for s in samples:
        print(f"--- {s['name']} ---")
        # score_text runs the DeBERTa model from humanizer.detector
        res = score_text(s['text'])
        print(f"Score:   {res['overall_pct']}% AI")
        print(f"Label:   {res['label']}")
        print(f"Signals: {res['signals']}")
        print()

if __name__ == "__main__":
    main()
