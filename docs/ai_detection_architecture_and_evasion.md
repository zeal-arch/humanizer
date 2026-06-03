# Advanced AI Detection Architecture & Evasion Strategy

This document provides a comprehensive technical breakdown of our project's dual-architecture: **The Detector** (fine-tuned DeBERTa) and **The Humanizer** (a 17-pass rule-based pipeline powered by LLM-guided perplexity perturbation).

---

## 1. High-Level System Architecture

Our system operates as a continuous adversarial pipeline. Input text is first scored by a detector to identify AI signatures. If flagged, it is passed through a highly specialized rewriting engine that algorithmically strips those signatures and mathematically guarantees a human-like statistical profile.

```mermaid
graph TD
    A[Input Text] --> B(DeBERTa-v3 Detector Model)
    
    B -->|Score <= 20% AI| C[Output: Flagged as Human]
    B -->|Score > 20% AI| D[The 17-Pass Humanizer Engine]
    
    subgraph The Humanizer Pipeline
    D --> E[Pass 1-14: Rule-Based Stylistic Edits]
    E --> F[Pass 15: Perplexity Guided Perturbation]
    F --> G[Pass 16-17: Final Punctuation & Polish]
    end
    
    G --> B
    
    style B fill:#ff9999,stroke:#333,stroke-width:2px
    style D fill:#99ccff,stroke:#333,stroke-width:2px
    style F fill:#ffcc99,stroke:#333,stroke-width:4px
```

---

## 2. The 17-Pass Evasion Pipeline

Traditional humanizers (like QuillBot) rely on simple "linear paraphrasing" (swapping synonyms blindly or prompting an LLM to rewrite a paragraph). Modern AI detectors easily catch this using "Paraphraser Shields" that detect unnatural vocabulary. 

Instead of full rewrites, our architecture uses **17 surgical passes** to break specific mathematical metrics used by detectors (Burstiness, Perplexity, and Stylistic Uniformity).

```mermaid
flowchart TD
    Start([Raw AI Text]) --> P1[Pass 1-2: Strip AI Vocabulary & Intensifiers]
    P1 --> P3[Pass 3: Inject Burstiness]
    
    P3 -.-> |Splits long sentences| P3a[Increases variance in sentence length]
    
    P3 --> P4[Pass 4-7: Opener Diversity & Active Voice]
    P4 --> P8[Pass 8-12: Hedging, Parentheticals, & Personal Voice]
    
    P8 -.-> |Adds 'we noticed', 'usually', 'or rather'| P8a[Adds Affective Friction & Human Doubt]
    
    P8 --> P13[Pass 13-14: Punctuation & Fronting]
    
    P13 --> P15((Pass 15: Perplexity Perturbation))
    
    P15 --> End([Fully Humanized Text])
    
    style P15 fill:#ffcc00,stroke:#333,stroke-width:3px
```

### Key Statistical Interventions:
*   **Burstiness Injection (Pass 3):** AI models write sentences of very uniform lengths. This pass algorithmically splits overly long sentences and merges short ones using semicolons. This creates a chaotic standard deviation in sentence length, perfectly mimicking human "bursty" thought patterns.
*   **Affective Friction (Passes 8-12):** AI is inherently objective and confident. These passes inject hedging (e.g., *"usually," "largely"*), parenthetical asides mid-sentence, and self-corrections (e.g., *"Or rather,"*).

---

## 3. The Core Evasion Engine: Perplexity-Guided Perturbation (Pass 15)

This is the most critical and computationally complex part of the architecture. It is designed specifically to defeat advanced token-probability detectors like **GPTZero** and **Turnitin**.

AI detectors look at the **Perplexity (PPL)** of a sentence. Perplexity measures how easily a language model can predict the next word. 
- **Low Perplexity (< 35):** The sentence is highly predictable (100% AI).
- **High Perplexity (> 35):** The sentence contains unexpected word choices (Human).

To evade detection without destroying readability, we use a smaller, local LLM (like **Qwen3-0.6B** or **GPT-2**) purely as a "predictability scanner."

```mermaid
sequenceDiagram
    participant Pipeline
    participant Qwen/GPT-2
    participant WordNet Dictionary
    
    Pipeline->>Qwen/GPT-2: Send Sentence "The system is highly effective."
    Qwen/GPT-2-->>Pipeline: Returns Perplexity Score: 12 (Low/AI)
    
    Note over Pipeline,WordNet Dictionary: Sentence flagged for perturbation!
    
    Pipeline->>Qwen/GPT-2: Identify most predictable tokens
    Qwen/GPT-2-->>Pipeline: Tokens: ['highly', 'effective']
    
    Pipeline->>WordNet Dictionary: Fetch student-level synonyms for 'effective'
    WordNet Dictionary-->>Pipeline: Returns ['useful', 'potent']
    
    Note over Pipeline: Swaps words and re-scores
    
    Pipeline->>Qwen/GPT-2: Send Sentence "The system is quite useful."
    Qwen/GPT-2-->>Pipeline: Returns Perplexity Score: 45 (High/Human)
    
    Note over Pipeline: Threshold passed. Moves to next sentence.
```

### Why this defeats the "Paraphraser Shield":
If a humanizer blindly swaps synonyms everywhere, the resulting text looks unnatural and flags the detector's Paraphraser Shield (a secondary detector looking for weird vocabulary). 

Our architecture avoids this by **only attacking Low Perplexity sentences**. If Qwen determines a sentence already has a Perplexity > 35, the pipeline skips it completely. We only perturb the exact statistical weak points of the essay, preserving the original flow and logic while guaranteeing passage through GPTZero.
