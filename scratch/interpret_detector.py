import os
import sys
import re
import math
import torch

# Add project root to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from humanizer.detector import load_detector

# Text to interpret
TEXT = (
    "In order to leverage robust systems, it is crucial to implement a detailed method "
    "that seamlessly integrates with existing workflows. Furthermore, this approach "
    "fosters a symbiotic relationship between development and operations."
)

def fast_score_text(text: str, tokenizer, model) -> int:
    """Helper to score text extremely fast on CPU without padding to 512 tokens."""
    encoded = tokenizer(
        text,
        padding=True,
        truncation=True,
        return_tensors='pt'
    )
    with torch.inference_mode():
        outputs = model(input_ids=encoded['input_ids'], attention_mask=encoded['attention_mask'])
        logit = outputs["logits"].item()
        prob = 1.0 / (1.0 + math.exp(-(logit - 5.0) / 1.6))
    return round(prob * 100)

def interpret_text(text: str):
    print("Loading detector model...")
    tokenizer, model = load_detector()
    if tokenizer is None or model is None:
        print("Error: Could not load local detector model.")
        return

    # 1. Get original score
    orig_score = fast_score_text(text, tokenizer, model)
    print(f"\nOriginal AI Score: {orig_score}%")
    
    # 2. Tokenize into words
    words = text.split()
    word_scores = []
    
    print("\nAnalyzing word-level contributions (Leave-One-Out Perturbation)...")
    for i in range(len(words)):
        # Leave one out
        modified_words = words[:i] + words[i+1:]
        modified_text = " ".join(modified_words)
        
        # Score the modified text
        mod_score = fast_score_text(modified_text, tokenizer, model)
        
        # Contribution: how much did removing this word lower/raise the score?
        contribution = orig_score - mod_score
        word_scores.append((words[i], contribution))
        
        # Show progress
        sys.stdout.write(f"\rProcessed {i+1}/{len(words)} words...")
        sys.stdout.flush()
    print("\nDone!")
    
    # 3. Sort by contribution
    print("\n--- TOP WORDS DRIVING AI SCORE (Positive Contribution) ---")
    pos_contrib = sorted([ws for ws in word_scores if ws[1] > 0], key=lambda x: x[1], reverse=True)
    for word, score in pos_contrib[:10]:
        clean_word = re.sub(r'[^a-zA-Z]', '', word)
        print(f"  Word: '{clean_word:<15}' | Added +{score}% to AI Likelihood")
        
    print("\n--- TOP WORDS REDUCING AI SCORE (Human/Negative Contribution) ---")
    neg_contrib = sorted([ws for ws in word_scores if ws[1] < 0], key=lambda x: x[1])
    for word, score in neg_contrib[:10]:
        clean_word = re.sub(r'[^a-zA-Z]', '', word)
        print(f"  Word: '{clean_word:<15}' | Reduced AI score by {score}%")

    # 4. Color-coded text output in terminal (using ANSI colors)
    print("\n--- COLOR-CODED TEXT INFLUENCE MAP ---")
    print("(\x1b[31mRed\x1b[0m = drives AI score up, \x1b[32mGreen\x1b[0m = drives AI score down/more human)\n")
    
    colored_words = []
    for word, score in word_scores:
        if score > 0:
            # Red color for strong AI contribution
            colored_words.append(f"\x1b[31;1m{word}\x1b[0m")
        elif score < 0:
            # Green color for human contribution
            colored_words.append(f"\x1b[32;1m{word}\x1b[0m")
        else:
            colored_words.append(word)
            
    print(" ".join(colored_words))
    print("\x1b[0m\n")

if __name__ == '__main__':
    interpret_text(TEXT)
