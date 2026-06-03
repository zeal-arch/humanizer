# Wikipedia: Signs of AI Writing — Complete Reference Notes

> **Source:** [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)  
> **Purpose:** Field guide to detect undisclosed AI-generated content. Used in our humanizer project to understand what patterns we must eliminate from AI output.  
> **Last verified:** June 2026 | Revision ID: 1357393965

---

## Overview

This is a list of writing and formatting conventions typical of AI chatbots such as ChatGPT, with real examples taken from Wikipedia articles, drafts, comments, and other content.

**Important disclaimers from Wikipedia:**
- Not all text featuring these indicators is AI-generated — LLMs are trained on human writing, including Wikipedia.
- This list is **descriptive**, not **prescriptive** — it is a set of observations, not rules.
- The patterns are *signs* of a problem, not the problem itself.
- Do not just "fix the signs" — that only makes detection harder. Fix the underlying issues (accuracy, sourcing, neutrality).
- This guide is **less useful for fiction writing** — fiction has its own separate AI tells (e.g., character names like "Elara Voss", "whispering woods", etc.).

---

## 1. CAVEATS

### 1.1 AI Detection Tools Are Unreliable
- Do **not** solely rely on AI detection tools like GPTZero.
- These tools perform better than random chance, but have **non-trivial error rates**.
- They can be fooled by: paraphrasing, markup changes, spacing changes, or using models the detector was never trained on.

### 1.2 Human Detection Ability Is Also Poor
- Humans are notoriously bad at distinguishing human vs LLM-generated text.
- A 2025 study showed human ability is **no better than random chance**.
- Another 2025 German study: humans got **57% accuracy on AI texts, 64% on human texts**.
- Heavy LLM users (~90% accurate) are the best detectors; casual users barely beat chance.
- Human speech and writing is increasingly **influenced by LLMs** — the two are converging (confirmed by 2024 studies on podcasts and word choices).
- Writers may also **adjust their behavior** to avoid accusations of AI use.

---

## 2. CONTENT INDICATORS

> **Core reason:** LLMs regress to the statistical mean — they smooth over specific facts into generic statements that could apply to many topics. Like a portrait fading from a sharp photograph into a blurry, generic sketch: the subject becomes simultaneously less specific and more exaggerated.

### 2.1 Undue Emphasis on Significance, Legacy, and Broader Trends

**What it looks like:** AI inflates the importance of any subject with grand-sounding language about its "impact," "legacy," or how it "reflects broader trends." This even happens for mundane subjects like etymology or population data.

**Words to watch for:**
- *stands/serves as*
- *is a testament/reminder*
- *a vital/significant/crucial/pivotal/key role/moment*
- *underscores/highlights its importance/significance*
- *reflects broader...*
- *symbolizing its ongoing/enduring/lasting...*
- *contributing to the...*
- *setting the stage for...*
- *marking/shaping the...*
- *represents/marks a shift*
- *key turning point*
- *evolving landscape*
- *focal point*
- *indelible mark*
- *deeply rooted*

**Real example (Statistical Institute of Catalonia, Sep 2024):**
> "The Statistical Institute of Catalonia was officially established in 1989, **marking a pivotal moment** in the evolution of regional statistics in Spain. [...] The founding of Idescat **represented a significant shift** [...] This initiative **was part of a broader movement** across Spain..."

**Real example (etymology, Dec 2024):**
> "During the Spanish colonial period, the name *Bakunutan* was hispanized to *Bacnotan* [...] **This etymology highlights the enduring legacy** of the community's resistance and **the transformative power** of unity in shaping its identity."

**Special note — biology articles:**
- AI over-emphasizes a species' connections to its broader ecosystem even when tenuous.
- It belabors conservation status and research efforts even when those efforts don't exist.

**Real biology example:**
> "Currently, **there is no specific conservation assessment** for *Lethrinops lethrinus* by the IUCN. However, the general health of the Lake Malawi ecosystem is **crucial for the survival of this and other endemic species**. Factors such as overfishing, pollution, and habitat destruction **could potentially** impact their populations."

---

### 2.2 Canned Emphasis on Notability, Attribution, and Media Coverage

**What it looks like:** AI "proves" notability by listing sources and specifying what type of sources they are (regional media, trade publications, etc.), often echoing the exact wording of Wikipedia's guidelines (e.g., "independent coverage").

**Words to watch for:**
- *independent coverage*
- *local/regional/national/[country name] media outlets*
- *music/business/tech outlets*
- *profiled in*
- *written by a leading expert*
- *active social media presence* / *strong digital presence*

**Additional AI notability behavior (2025+):**
- Newer AI tools (2025+) often **inaccurately attribute their own superficial analyses** to the source.
- AI will note that someone "**maintains an active social media presence**" — extremely idiosyncratic to AI and rare before ~2024.
- AI emphasizes sources **in body text** even for trivial coverage or uncontroversial facts — a human would just use an inline citation.

**Real social media example (Forum Mall Kochi, Jun 2025):**
> "The mall **maintains a strong digital presence**, particularly on Instagram, where it actively shares the latest updates and events."

---

### 2.3 Superficial Analyses

**What it looks like:** AI inserts superficial analytical-sounding statements that don't actually analyze anything. Often done by attaching a **present participle (-ing) phrase** at the end of sentences. This often involves vague attributions.

**Words to watch for:**
- *highlighting/underscoring/emphasizing ...*
- *ensuring ...*
- *reflecting/symbolizing ...*
- *contributing to ...*
- *cultivating/fostering ...*
- *encompassing ...*
- *valuable insights*
- *align/resonate with*

**AI sometimes claims things have generated discussions:**
> "The phenomenon has **generated debate** about authenticity, consent, and the psychological effects of digitally extending personhood."
> "GriefBots have **prompted broader reflection** on mortality and memory in a digital age. They blur boundaries between life and data, **raising philosophical questions** about identity, authenticity..."

**Real example (Douéra, Jun 2023):**
> "As of the April 2008 census, the population of Douera stood at approximately 56,998 inhabitants, **creating a lively community within its borders.** [...] **further enhancing its significance as a dynamic hub of activity and culture.**"

---

### 2.4 Promotional and Advertisement-Like Language

**What it looks like:** Text reads like marketing copy, press releases, or travel guides — not neutral encyclopedic writing. This can happen even when editors are **not** deliberately trying to advertise. Older LLMs (GPT-4) output more blatant positivity; newer LLMs are more subtly promotional.

**Words to watch for:**
- *boasts a*
- *vibrant*
- *rich*
- *profound*
- *enhancing*
- *showcasing*
- *exemplifies*
- *commitment to*
- *natural beauty*
- *nestled*
- *in the heart of*
- *groundbreaking*
- *renowned*
- *featuring*
- *diverse array*

**Subtypes of promotional language:**

**Cultural heritage inflation:** When writing about anything that could be considered "cultural heritage" (even a tech industry), AI constantly reminds you of its importance.

> "**Nestled** within the **breathtaking** region of Gonder in Ethiopia, Alamata Raya Kobo **stands as a vibrant town with a rich cultural heritage** [...] **offers visitors a fascinating glimpse into the diverse tapestry** of Ethiopia."

**Press release / company bio tone:**
> "These projects **align with KQ's goals of reducing its environmental footprint, improving operational efficiency, and fostering community development through job creation.** CEO Allan Kilavuka **emphasized the airline's commitment to sustainability, customer focus, and Africa's prosperity through responsible corporate practices.**"

**Note:** Not all promotional or spammy writing is AI-generated.

---

### 2.5 Vague Attributions and Overgeneralization of Opinions (Weasel Wording)

**What it looks like:** AI attributes opinions or claims to vague unnamed authorities. It also **exaggerates the quantity** of sources — e.g., presenting one scholar's view as widely held, or implying a list is non-exhaustive when sources give no indication that other examples exist.

**Words to watch for:**
- *Industry reports*
- *Observers have cited*
- *Experts argue*
- *Some critics argue*
- *several sources/publications* (when only a few are cited)
- *such as* (before exhaustive word lists)

**Real example:**
> "Due to its unique characteristics, the Haolai River is of interest to **researchers and conservationists**. Efforts are ongoing to monitor its ecological health..."

**Overgeneralization example (2 sources called "industry publications"):**
> "**Toy industry publications such as** *The Toy Insider* and *Mojo Nation* have presented Rubik's WOWCube as a STEM-oriented platform..."

---

### 2.6 Outline-Like Conclusions About Challenges and Future Prospects

**What it looks like:** AI-generated articles follow a rigid outline structure and end with a "Challenges" section (often: "Despite its [positive word], [subject] faces challenges...") followed by vague optimism or speculation.

**Words to watch for:**
- *Despite its... faces several challenges...*
- *Despite these challenges*
- *Challenges and Legacy*
- *Future Outlook*

**Note:** This sign is about the rigid formula, not simply mentioning challenges.

**Real example (Korattur, Apr 2024):**
> "**Despite its industrial and residential prosperity, Korattur faces challenges** typical of urban areas, including [...] With its **strategic location and ongoing initiatives**, Korattur **continues to thrive** as an integral part of the Ambattur industrial zone..."

---

### 2.7 Leads Treating Wikipedia Lists or Broad Article Titles as Proper Nouns

**What it looks like:** When AI writes an article with a non-proper-name title (like a list), it treats the article title as if it were a real-world standalone entity.

**Real examples:**
> "**'The "List of songs about Mexico" is a curated compilation'** of musical works that reference Mexico, its culture, geography, or identity as a central theme."
> "**'EuroGames editions is the chronological list'** of the biennial EuroGames..."

---

## 3. LANGUAGE AND GRAMMAR

> AI-generated text displays consistent patterns in syntax, word choice, and sentence construction that human writing doesn't display to nearly the same degree. These patterns occur **regardless of subject matter**, giving AI text an identifiable "voice."
> Note: GPT-4o (used by ChatGPT from May 2024 to August 2025) produces output with more syntactic variation than other contemporaneous models.

### 3.1 High Density of "AI Vocabulary" Words

These words are statistically over-represented in LLM output (corroborated by multiple peer-reviewed studies). They started appearing far more frequently in text after 2022. **Where there is one, there are likely others.**

| Word / Phrase | Notes |
|---|---|
| *Additionally* | Especially when beginning a sentence |
| *align with* | — |
| *boasts* (meaning "has") | — |
| *bolstered* | — |
| *crucial* | — |
| **delve** | **Extremely strong indicator** — heavily associated with ChatGPT |
| *emphasizing* | — |
| *enduring* | — |
| *enhance* | — |
| *fostering* | — |
| *garner* | — |
| **highlight** (as a verb) | "X highlights Y" |
| *interplay* | — |
| *intricate / intricacies* | — |
| *key* (as an adjective) | — |
| *landscape* (as an abstract noun) | — |
| *meticulous / meticulously* | — |
| *pivotal* | — |
| *robust* | — |
| *showcase* | — |
| **tapestry** (abstract noun) | e.g. "a rich tapestry of..." |
| *testament* | e.g. "a testament to..." |
| **underscore** (as a verb) | "This underscores the importance of..." |
| *valuable* | — |
| *vibrant* | — |

**AI Vocabulary by LLM Era** (these are not hard cutoffs, just rough guides):

| Era | Model | Key Overused Words |
|---|---|---|
| 2023 – mid-2024 | GPT-4 | *Additionally, boasts, bolstered, crucial, **delve**, emphasizing, enduring, garner, intricate/intricacies, interplay, key, landscape, meticulous/meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant* |
| Mid-2024 – mid-2025 | GPT-4o | *align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant* |
| Mid-2025 onward | GPT-5 | *emphasizing, enhance, highlighting, showcasing* (plus undue notability language) |

**Special note on "concrete" in comments:**  
When AI-assisted editors write *talk page* comments, they frequently use the word **"concrete"** as an adjective — especially in statements like "there is no *concrete evidence*" of AI use, or requests for accusers to "provide *concrete examples*." This is a strong tell in discussion contexts.
> "In the absence of concrete evidence, I propose removing the AI-generated tag immediately to maintain the article's integrity."

---

### 3.2 Avoidance of Basic Copulatives ("is"/"are" phrases)

**What it looks like:** AI tends to avoid simple, direct sentences using "is" or "are." Instead it uses more complex constructions that sound "sophisticated" but are actually harder to read.

**Human writing:** "John Smith is a physicist."  
**AI writing:** "John Smith, a distinguished figure in the field of theoretical physics, has dedicated his career to the exploration of quantum phenomena."

AI turns simple facts into elaborate constructions. Simpler is better.

---

### 3.3 Negative Parallelisms

AI frequently uses specific rhetorical structures involving negation. These appear so frequently they are reliable indicators.

#### 3.3.1 "Not just X, but also Y"
> "The museum is **not just** a repository for artifacts, **but also** a living testament to the community's heritage."

#### 3.3.2 "Not X, but Y"
> "This is **not** a simple administrative decision, **but** a transformative moment in the region's governance."

---

### 3.4 Rule of Three

**What it looks like:** AI obsessively lists things in groups of three, often using the same grammatical structure.

**Examples:**
- "innovative, efficient, and reliable"
- "It shaped the culture, transformed the economy, and inspired generations."
- "The project aims to reduce costs, improve quality, and enhance sustainability."

The "rule of three" is a real rhetorical device, but AI applies it mechanically to almost every description.

**Real example (Deadbot, Oct 2025):**
> "The phenomenon has generated debate about authenticity, consent, and the psychological effects of digitally extending personhood."

---

### 3.5 Lexical Diversity / Elegant Variation

**What it looks like:** AI tries too hard to use synonyms to avoid repeating the same word, leading to awkward or unnatural word choices.

**Example:** Instead of saying "the company" multiple times, AI cycles through "the organization," "the enterprise," "the firm," "the entity," "the institution" — even when some don't fit.

This looks like sophistication but signals AI. Human writers often deliberately repeat a key term for clarity.

---

## 4. STYLE

### 4.1 Title Case

**What it looks like:** AI incorrectly capitalizes words using Title Case in places where sentence case should be used.

**Wikipedia standard:** Sentence case for headings.  
**AI mistake:** "The Role of International Organizations in Modern Governance" (heading) instead of "The role of international organizations in modern governance."

---

### 4.2 Overuse of Boldface

**What it looks like:** Wikipedia only bolds the article title in the first sentence and sometimes key defined terms. AI bolds many words throughout — acting like a textbook or blog post.

---

### 4.3 Inline-Header Vertical Lists

**What it looks like:** A classic ChatGPT output format — bulleted lists where each bullet starts with a **bolded inline header** followed by a colon and explanation.

**Example:**
- **Innovation:** The project introduced new methods of...
- **Collaboration:** Teams from different departments worked together...
- **Impact:** The results were felt across multiple sectors...

This is extremely common in ChatGPT output and very rare in good encyclopedic writing.

---

### 4.4 Overuse of Em Dashes

**What it looks like:** AI uses em dashes (—) excessively, often where a comma, semicolon, or new sentence would be more appropriate.

---

### 4.5 Unusual Use of Tables

**What it looks like:** AI creates tables for information that doesn't need tabular format, or formats them in ways inconsistent with Wikipedia standards.

---

### 4.6 Curly Quotation Marks and Apostrophes

**What it looks like:** AI outputs "curly" / "smart" typographic quotes (`"like this"` and `'like this'`) instead of the straight ASCII quotes Wikipedia uses. This is a direct artifact of AI generation.

---

### 4.7 Skipping Heading Levels

**What it looks like:** AI sometimes skips from Level 2 directly to Level 4 in the heading hierarchy, violating standard document structure.

---

### 4.8 Thematic Breaks Before Headings

**What it looks like:** AI sometimes inserts horizontal rules (`---`) before headings, which is not standard Wikipedia practice.

---

## 5. COMMUNICATION INTENDED FOR THE USER

Phrases that "slip through" from the AI's conversation mode into the article text — content meant for the person prompting the AI, not for the encyclopedia.

### 5.1 Collaborative Communication

**What it looks like:** AI uses first-person collaborative language inside the article.

**Examples:**
- "Here is the revised article for your review..."
- "Feel free to adjust the tone as needed..."
- "I have tried to maintain a neutral point of view..."
- "Let me know if you'd like me to expand any section..."

**Real example with reference character `↩`:**
> "Would you like help formatting and submitting this to Wikipedia, or do you plan to post it yourself? I can guide you step-by-step through that too."
> *(This appeared in the References section of a draft)*

---

### 5.2 Knowledge-Cutoff Disclaimers and Speculation About Gaps in Sources

**What it looks like:** AI inserts disclaimers about its own limitations into article text. Newer AI with web access may also claim information is "not publicly available" when it simply couldn't find it, and then *speculate* about what that information "likely" is — this speculation is entirely fabricated.

**Speculative personal-life variant:** When a knowledge gap is about an individual's personal life, AI often says the person **"maintains a low profile"** or **"keeps personal details private"** — this is pure speculation with no sourcing.

**Words to watch for:**
- *as of my last knowledge update in [date]*
- *up to my last training update*
- *while specific details are limited/scarce...*
- *not widely available/documented/disclosed*
- *in the provided/available sources/search results...*
- *based on available information*
- *maintains a low profile / keeps personal details private* (speculative)

**Examples:**
- "As of my knowledge cutoff in [year]..."
- "Note: More recent information may be available..."
- "This information may have changed since [date]..."
- "I was unable to find sources confirming..."
- "Further research may be needed to verify..."
- "While specific details about [X] are not extensively documented in readily available sources..."
- "As an underground release, detailed lyrics are *not widely transcribed on major sites like Genius or AZLyrics*..."

---

### 5.3 Phrasal Templates and Placeholder Text

**What it looks like:** AI leaves in literal placeholder text.

**Examples:**
- "[Insert citation here]"
- "[Add image]"
- "[Source needed]"
- "[CITATION]"
- "Note to editor: please verify this fact"

---

## 6. MARKUP ISSUES

### 6.1 Use of Markdown

**What it looks like:** Wikipedia uses wikitext syntax. AI trained on the general internet often outputs Markdown instead.

| Markdown (Wrong for Wikipedia) | Wikitext (Correct) |
|---|---|
| `**bold text**` | `'''bold text'''` |
| `*italic text*` | `''italic text''` |
| `## Heading` | `== Heading ==` |
| `[Link text](URL)` | `[URL Link text]` |
| `![image](url)` | `[[File:image.jpg]]` |
| `---` / `***` / `___` | `----` |

**Why it happens:**
1. **Niche format:** Wikitext is niche (used mostly on MediaWiki platforms) and not prominent as raw text in LLM training corpora.
2. **System instructions:** Chatbots have system-level instructions directing them to format outputs using Markdown (e.g., Claude's system prompts specifying bold/italic asterisks, header hashes, and list indents).
3. **Copier error:** When a user copies the text from a chatbot interface, the Markdown syntax is carried along in the clipboard.
4. **The Fenced Code Block / Three Backticks Tell:** If a user instructs the chatbot to convert its response to wikitext, the chatbot might place its attempted wikitext inside a fenced code block. Users often copy the entire block including the code fences, leading to a telling footprint of both markup languages' syntax. This might include the appearance of three backticks in the text, such as: ` ```wikitext ` or ` ``` ` at the beginning/end of the content.

**Ineffective Indicator Warning:**
Markdown *alone* is not a strong indicator of AI use. Software developers, researchers, and technical writers frequently use Markdown in platforms like Slack, Reddit, Discord, Obsidian, and GitHub, and many text editors (like Windows Notepad, macOS/iOS Notes, or Google Docs) support Markdown. Some new human editors simply assume Wikipedia supports Markdown by default.

**Real example (Villers-Chief, Jun 2025):**
AI used `## Geography`, `## History`, `## Administration` — which MediaWiki renders as a numbered list, not headings.

**Real example of Markdown link copied into talk page (Talk:Dana Klisanin, May 2025):**
> `- The Wikipedia entry does not explicitly mention the "Cyberhero League" being recognized as a winner... as detailed in the interview with THE FUTURIST ([https://consciouscreativity.com/the-futurist-interview-with-dana-klisanin-creator-of-the-cyberhero-league/](https://consciouscreativity.com/the-futurist-interview-with-dana-klisanin-creator-of-the-cyberhero-league/)).`

---

### 6.2 Broken Wikitext

**What it looks like:** AI generates syntactically incorrect wikitext — unclosed tags, wrong template syntax, mismatched brackets, garbled code.

**Notable case:** The `{{AfC submission}}` template is often garbled by AI when new editors ask chatbots how to submit their Articles for Creation draft.

---

### 6.3 `turn0search0` and Image Artifacts

**What it looks like:** ChatGPT may include `citeturn0search0` (surrounded by Unicode points in the Private Use Area) at the ends of sentences, with the number after "search" increasing as the text progresses (e.g., `turn0search1`, `turn0search2`). This was first observed in February 2025.

**Variants include:**
- **Standard Search:** `citeturn0search0` (and increasing digits)
- **Short Form:** Just the increasing number surrounded by PUA Unicode: `0`, `1`, `2`
- **Image Sets:** `iturn0image0turn0image1turn0image4turn0image5`
- **News, Files, or Generated IDs:** `citeturn0news0`, `citeturn1file0`, or `citegenerated-reference-identifier`

**What it means:** These are citation or media placeholders. The chatbot linked to an external source or image, but a human pasting the text into Wikipedia copied it in a way that converted the links into placeholder code surrounded by special Unicode PUA markers.

**Real example (Bangladesh School List, Feb 2025):**
> "...recognized as an International Fellowship Centre by Cambridge International Examinations. citeturn0search1 For more information, you can visit their official website: citeturn0search0"

**Real example (Draft:Reze (Chainsaw Man), 2025):**
> "* **Japanese:** Reze is voiced by Reina Ueda, an established voice actress known for roles such as Cha Hae-In in ''Solo Leveling'' and Kanao Tsuyuri in ''Demon Slayer''.2"

---

### 6.4 Reference Markup Bugs

Several markup patterns are dead giveaways:

| Artifact | Source | What it is |
|---|---|---|
| `:contentReference[oaicite:0]{index=0}` | ChatGPT (OpenAI) | Citation bug |
| `oai_citation` | ChatGPT (OpenAI) | Citation artifact |
| `Example+1` / `Wikipedia+1` | ChatGPT (OpenAI) | Citation artifact |
| `[attached_file:1]` / `[web:1]` | Perplexity AI | File attachment artifact |
| `<grok-card data-id="..." data-type="citation_card">` | Grok (xAI) | Citation card |
| `grok_render_citation_card_json={...}` | Grok (xAI) | Citation render artifact |
| `【85†L261-269】` | ChatGPT with file upload | Lenticular bracket / dagger artifacts (since Jun 2025) |
| `{"attribution":{"attributableIndex":"X-Y"}}` | ChatGPT | JSON attribution artifact |

---

### 6.5 `attribution` and `attributableIndex`

**What it looks like:** ChatGPT may add JSON-formatted code at end of sentences:
```
({"attribution":{"attributableIndex":"1009-1"}})
```
with X and Y being increasing numeric indices.

---

### 6.6 Non-Existent or Out-of-Place Categories

**What it looks like:** AI adds categories that don't exist, or exist but are inappropriate (wrong spelling/hyphenation). Sometimes deleted categories re-appear because AI was trained on old data.

**Real example:** AI wrote `[[Category:American hip hop musicians]]` when the correct category is `[[Category:American hip-hop musicians]]` (hyphenated).

**Note:** Earlier revisions may show broken categories that were later deleted, so checking earlier revisions can help.

---

### 6.7 Non-Existent Templates

**What it looks like:** AI invents plausible-sounding infobox templates or template parameters that don't exist. Also uses templates deleted after AI's knowledge cutoff (e.g., the `lang-??` series deleted in Sep 2024).

**Real example — hallucinated infobox:**
AI used `{{Infobox ancient population}}` (doesn't exist) instead of `{{Infobox archaeological culture}}`.

---

## 7. CITATIONS

### 7.1 Broken External Links

**Strong indicator** when a new article or draft has **multiple** broken links that aren't found in web archives — suggesting they were never real.

**Watch out for (NOT necessarily AI):**
- Links that work through a university library but not publicly
- Links mangled by bots (incorrect identifiers added)
- Links with missing start/end (human copy-paste error)

---

### 7.2 Invalid DOIs and ISBNs

**What it looks like:** AI generates ISBNs and DOIs that are syntactically formatted correctly but don't exist. ISBN checksum failures are flagged by citation templates automatically. Unresolvable DOIs are strong hallucination indicators.

---

### 7.3 DOIs That Lead to Unrelated Articles

**What it looks like:** Even more insidious — AI generates a DOI that resolves, but to a completely unrelated paper.

**Real documented example (ChatGPT-generated Ohm's Law text):**
- DOI `10.1109/PROC.1967.6033` was cited for a 1967 paper by C.L. Fortescue — but Fortescue was dead for 30+ years in 1967, and the volume/issue cited doesn't contain any matching article.

---

### 7.4 Book Citations Without Page Numbers or URLs

**What it looks like:** AI cites books without page numbers, making citations unverifiable. Sometimes page numbers are given but the pages don't verify the claim.

**Real example:** AI cited Barry Goldwater's *The Conscience of a Conservative*, p. 12 for a claim about Edmund Burke — but searching the book for "Burke" returns no results.

---

### 7.5 Incorrect or Unconventional Use of References

**What it looks like:**
- Placing `<ref>` tags in wrong locations.
- Incorrect syntax for re-using named references (e.g. placing `<sup>[3]</sup>` literal text or repeating a named reference tag with empty content).
- References in the `<references>` section not used inline (generating cite errors).
- **Footnote Back-links:** Using the `↩` or `↩2` symbols to indicate footnotes, which are copy-pasted directly from chatbot interfaces.
- **Irrelevant PMID Citations:** Citing highly specific, completely irrelevant papers because they share low-number IDs. For example, a chatbot might generate a reference that leads to PMID 3 (a 1975 paper on metal substitutions in carbonic anhydrase) and cite it for Traumatic Brain Injury software.
  - *Note:* In older revisions (2018–2023), a VisualEditor bug occasionally caused human editors to cite PMID 3 or PMID 9 (a rat liver paper) by mistake, which is not AI.

**Real example of `↩` footnote marker (Draft:CureMD, 2025):**
> "'''Footnotes'''
> # KLAS Research. (2024). *Top Performing RCM Vendors 2024*. https://klasresearch.com ↩ ↩<sup>2</sup>
> # PR Newswire. (2025, February 18). *CureMD AI Scribe Launch Announcement*. https://www.prnewswire.com/news-releases/curemd-ai-scribe ↩"

**Real example of irrelevant PMID citation (Cognitive orthotics, 2023):**
The AI chatbot cited:
> `<ref>{{Cite journal |last=Smith |first=R. J. |last2=Bryant |first2=R. G. |date=1975-10-27 |title=Metal substitutions incarbonic anhydrase: a halide ion probe study |url=https://pubmed.ncbi.nlm.nih.gov/3 |journal=Biochemical and Biophysical Research Communications |volume=66 |issue=4 |pages=1281–1286 |doi=10.1016/0006-291x(75)90498-2 |issn=0006-291X |pmid=3}}</ref>`
to verify a claim about psychologists developing cognitive rehabilitation software for brain injuries in the early 1980s.

---

### 7.6 `utm_source=` Parameters

**What it looks like:** ChatGPT appends tracking parameters to URLs:
- `?utm_source=chatgpt.com`
- `?utm_source=openai`
- Microsoft Copilot: `?utm_source=copilot.com`
- Grok: `?referrer=grok.com`
- Gemini and Claude use UTM parameters less often

**Note:** This **near-definitively proves ChatGPT's involvement**, but doesn't on its own prove ChatGPT also generated the writing — some editors use AI only to find citations.

---

### 7.7 Named References Declared in References Section But Unused in Article Body

**What it looks like:** AI creates a `<references>` block with `<ref name="...">` declarations that are never called in the article body. This produces "list-defined reference named X is not used" errors.

---

## 8. MISCELLANEOUS

### 8.1 Pronounced Shift in Writing Style

**What it looks like:**
- Sudden shift to flawless grammar compared to other communication
- Especially suspicious if pre-2022 writing predates LLMs
- Because AI writing has changed over time, multi-year AI users may show **corresponding shifts** in their writing style over time

**English variety mismatch:** A user from India writing about an Indian university would normally use British/Indian English. If the article uses American English by default (LLM default), that's suspicious. However: non-native English speakers often mix varieties regardless of AI.

**Note the reverse too:** Consistent style *between* old and new edits (including the same quirks, even bad ones) is a sign of human writing.

---

### 8.2 Overwhelmingly Exhaustive Edit Summaries

**What it looks like:** AI edit summaries are formal, first-person paragraphs without abbreviations. They:
- Echo Wikipedia policy language exactly (e.g., "WP:NPOV", "encyclopedic tone")
- Mention things "ensured" or "avoided"
- Include verbose justifications of minor edits
- May also contain AI vocabulary, emoji, Markdown, or list formatting

**Real example (2023):**
> "ChatGPT I revised the content to provide a neutral and informative description of the Indira Gandhi National Centre for the Arts (IGNCA). The focus was on presenting the institution's objectives, approach, and programs in a way that adheres to Wikipedia's guidelines. The tone was adjusted to be more encyclopedic and less promotional."

**Real example (2025):**
> "**Concise edit summary:** Improved clarity, flow, and readability of the plot section; reduced redundancy and refined tone for better encyclopedic style."

**Real example (2026):**
> "Added sourced Impact section including restrictions, healthcare strain, and economic effects (2020–2022)." *(This edit summary was accompanied by ChatGPT UTM parameters in the references)*

**AI edit summaries strongly suggest the edits themselves are also AI-generated.**

---

### 8.3 "Submission Statements" in AfC Drafts

**What it looks like:** AI inserts formal statements explaining why a draft meets Wikipedia criteria — specifically addressed to reviewers. This immediately reveals AI generation and results in decline.

**Real example (Draft:Jorge Patrão, Oct 2025):**
> "Reviewer note (for AfC): This draft is a neutral and well-sourced biography [...] It meets WP:RS and WP:BLP standards and demonstrates clear notability per WP:NBIO through: – Presidency of Serra da Estrela Tourism Region... [note WP:BIOSIG is not a real shortcut]"

---

### 8.4 Pre-Placed Maintenance Templates

**What it looks like:**
- AI-created drafts with `{{AfC submission|d}}` already set to "declined" with no reviewer reasoning
- Protection templates (`{{pp}}`, `{{pp-move}}`) on new articles/sandboxes
- Maintenance tags (`{{Cleanup}}`, `{{Refimprove}}`) placed by the same editor who created the article

**Real example in a sandbox:**
```wikitext
{{pp|small=yes}}
{{pp-move}}
{{Use American English|date=September 2022}}
```
*(These were placed by the article's creator in a sandbox)*

---

### 8.5 Permissions Gaming

**What it looks like:** Making many benign-seeming edits quickly across unrelated topics to raise edit count and unlock higher access levels — done easily with AI rewrites. If someone suspected of permissions gaming added a lot of AI-looking text rapidly, those edits are likely AI.

**Note:** This sign should only be used in one direction — don't accuse someone of permissions gaming just because they add a lot of AI text.

---

### 8.6 Differences Between LLMs

Each model and version has a distinctive writing style (idiolect). Key differences:

- **ChatGPT (GPT-4o era):** Heavy use of em dashes, "delve," inline-header bullet lists, `oaicite`/`contentReference` artifacts, more focus on broader context and legacy
- **Grok (xAI):** `grok_card`, `+1` artifacts, `referrer=grok.com`, focus on broader context, very long output (Grokipedia articles are extremely long)
- **Gemini:** Less verbose, fewer legacy-emphasis patterns, UTM params rare
- **Claude:** More concise, fewer verbose patterns, UTM params rare
- **Perplexity:** `[attached_file:1]` and `[web:1]` artifacts

**ChatGPT is likely the most prevalent chatbot used for Wikipedia edits.**

---

## 9. INDICATORS OF AI-WRITTEN COMMENTS

These signs apply to **talk page comments, edit summaries, and discussion posts**. Many general signs (boldface, em dashes, curly apostrophes, negative parallelisms, vertical lists, Markdown, rule of three) also appear in comments but are covered in earlier sections.

### 9.1 Canned Emphasis on Quality, Good Faith, and Adherence to Policies

**What it looks like:** AI invokes policies, guidelines, and standards in a broad, formal, abstract, legalese-like way. Very formulaic.

**Words to watch for:**
- *align(s) with Wikipedia's aim/goal(s)*
- *adhere(s) to Wikipedia's policies/guidelines/standards*
- *I am/we are committed to ...*
- *I assure you that ...*
- *my intention/goal is to ...*

**Real example (Talk:Dog, 2024):**
> "I understand the importance of **adhering to Wikipedia's guidelines and policies**, and **I am committed to** contributing in a responsible and constructive manner. **My intention is to** provide well-referenced and reliable information that **aligns with Wikipedia's standards.**"

---

### 9.2 Canned Offers to Receive Constructive Criticism

**What it looks like:** AI comments offer to receive feedback in a formulaic way.

**Words to watch for:**
- *If you have any concerns/suggestions*
- *If there are specific sections/areas that...*

**Example:**
> "I welcome any constructive criticism or suggestions for improvement. Please feel free to share your thoughts and I will do my best to address any concerns."

---

### 9.3 Canned Calls to Focus on Content Instead of Conduct

**What it looks like:** When accused of wrongdoing, AI-assisted editors pivot to "let's focus on content, not conduct" — a specific deflection pattern.

---

### 9.4 Subject Lines

**What it looks like:** Some AI-generated talk page posts begin with text meant to be pasted into a Subject/email field.

**Real examples:**
- "Subject: Request for Permission to Edit Wikipedia Article - 'Dog'"
- "Subject: Edit Request for Wikipedia Entry"
- "Subject: Request for Review and Clarification Regarding Draft Article"
- "Subject: Concerns about Inaccurate Information"
- "Subject: Behavioral issues and Wikihounding by User:Binksternet"

---

### 9.5 Section Titles in Plain Text

**What it looks like:** AI generates messages broken into sections separated by plain text that appears to be section titles — either as Markdown or plain text without any Wiki markup.

**Real example:**
> `Importance of Thorough Research`
> Wikipedia's content guidelines emphasize...
> `Risk of Violating Wikipedia's Policy on Biographies of Living Persons`
> Wikipedia's Biographies of Living Persons (BLP) policy...

---

### 9.6 Non-Existent Policies or Guidelines

**What it looks like:** AI fabricates Wikipedia policy shortcuts or misquotes real ones. Sometimes it quotes policies that are real but doesn't quote what they actually say.

**Real examples:**
- Citing `WP:NOTENGLISH` with a fake quote
- Citing `WP:LAW` with invented wording
- Citing `WP:BIOSIG` (not a real shortcut)
- `WP:UNDERREP` (not a real shortcut)
- `WP:NOTAI` (not a real shortcut)
- `WP:AFDPURPOSE` (not a real shortcut)
- `WP:NOTELOCAL` (not a real shortcut)
- `WP:ENGLISHONLY` (not a real shortcut)

---

### 9.7 Transclusion of Article Maintenance Banners

**What it looks like:** When AI mentions maintenance templates in talk page posts, it writes them in curly brackets (e.g. `{{Disputed}}`), which causes them to be **accidentally transcluded** (rendered as the actual template banner) rather than just mentioned.

This can cause giant maintenance banners to appear in the middle of talk page comments.

---

### 9.8 Wikilawyering

**What it looks like:** Using elaborate, technical policy arguments to defend AI-generated content. AI selectively cites or interprets policies, often affirming what the user wants others to believe regardless of whether the points hold up.

Common pattern: When article is tagged as AI, user asks accusers to "point to specific passages" or reassures that content is "neutral" and "verified" — formulaically using policy language.

#### Invoking WP:PRESERVE
AI wikilawyers particularly invoke `WP:PRESERVE` to argue against deletion, even when the deletion argument is that core policies (notability, verifiability) are violated — which is exactly when PRESERVE doesn't apply.

---

### 9.9 Emoji as Formatting

**What it looks like:** AI uses emoji as structural/formatting elements in talk page posts — bullet points replaced with 📌, headings marked with ✅, 🧠, 🚨, etc.

**Real examples:**
- 🧠 Cognitive Dissonance Pattern:
- 🧱 Structural Gatekeeping:
- 🚨 Underlying Motivation:
- 🪷 Traditional Sanskrit Name: Trikoṇamiti

---

### 9.10 Confusion Over the Reason for a Declined Draft

**What it looks like:** AI cannot read the decline notice — it can only respond to information the user gives it. So AI-generated help desk questions express confusion about why a draft was declined, **even when the decline notice is very clear**.

**Real examples (all AI-generated, different people, nearly identical phrasing):**
> "I am trying to understand **whether the issue is mainly source quality, article tone, or both**"
> "Is the primary issue related to **notability, sourcing, tone, conflict of interest, or article structure**?"
> "I would like to understand: Whether the issue relates to **notability, sourcing, or tone**"

---

### 9.11 Canned Request for Source Assessment

**What it looks like:** Instead of researching sources, AI-assisted editors post nearly identical formulaic requests asking others to assess whether their sources meet notability requirements.

**Real examples (two completely different people, nearly identical wording):**
> "Could **an experienced editor** please advise which of these sources, if any, **count as reliable, independent, significant coverage** for a biography article?"
> "Could **an uninvolved editor** advise which of the current references, if any, **count as significant independent secondary coverage** for notability purposes..."

---

## 10. SIGNS OF HUMAN WRITING

### 10.1 Age of Text Relative to ChatGPT Launch

- ChatGPT launched publicly: **November 30, 2022**
- Text written **before November 30, 2022** = AI use can be **safely ruled out**
- Earlier LLMs (pre-2022) were paid services not known to the public
- While some older writing may coincidentally display AI-like patterns, the vastness of Wikipedia means these are coincidences

---

### 10.2 Ability to Explain One's Own Editorial Choices

**What it looks like:** A human editor can give a specific, contextual explanation for their edits. Ask the editor how a mix-up occurred rather than jumping to conclusions. If they can supply the correct link or share the relevant passage from the real source, that points to ordinary human error.

---

## 11. INEFFECTIVE INDICATORS

**False accusations of AI use can drive away new editors.** Before claiming AI was used, consider whether Dunning-Kruger effect and confirmation bias might be clouding your judgment.

These things are **NOT reliable signs** of AI writing:

- **Perfect grammar** — many human editors are skilled writers or come from professional writing backgrounds
- **Combination of casual and formal registers** — may be someone in a technical field, youth, neurodivergence, or multiple editors contributing
- **"Bland" or "robotic" prose** — AI actually skews positive and verbose; it doesn't always scan as "robotic" to people unfamiliar with AI writing
- **"Fancy", "academic", or "formal" prose** — AI overuses *specific words*, not all formal prose
- **Letter-like writing (in isolation)** — humans formatted talk page posts like letters/emails long before LLMs existed
- **Transition words in isolation** — *Additionally*, *Consequently*, *Notably* were used by humans too, and some style guides accept them
- **Unsourced content** — 570,000+ Wikipedia articles lack citations, most predating LLMs; meanwhile modern AI often does include citations (just inaccurate ones)
- **Bizarre wikitext that isn't listed here** — random-seeming HTML tags like `<span>` are more likely a browser extension or Wikipedia's Content Translation tool bug; misplaced formatting like `''Catch-22 i''s` is more likely a VisualEditor mistake
- **Correct wikitext** — getting formatting correct, even for complex templates, is normal using the visual editor or Preview

---

## 12. HISTORICAL INDICATORS (Now Less Common)

These patterns were strong indicators in 2022–2024 but are much less frequent now. Still useful for finding older undetected AI-generated edits.

### 12.1 Didactic Disclaimers (November 2022 – 2024)

**What it looks like:** Older LLMs (~2023) often added disclaimers about topics being "important to note," safety warnings, or disambiguation for topics that vary by locale/jurisdiction.

**Words to watch for:**
- *it's important/critical/crucial to note/remember/consider*
- *worth noting*
- *may vary*

**Real examples:**
> "However, **it's important to note** that these caucuses operate outside the formal ANC structure and their influence on policy decisions **may vary**."
> "**It is crucial to differentiate** the independent AI research company... **to prevent confusion**."
> "**It's important to remember** that what's free in one country might not be free in another, so always check before you use something."

---

### 12.2 Section Summaries

**What it looks like:** Older LLMs added "Conclusion" sections and ended paragraphs with sentences that summarized and restated the paragraph's core idea.

**Words to watch for:**
- *In summary*
- *In conclusion*
- *Overall*

**Real example (Nurse scientist, 2023):**
> "**In summary**, the educational and training trajectory for nurse scientists typically involves a progression from a master's degree in nursing to a Doctor of Philosophy in Nursing, followed by postdoctoral training in nursing research."

---

### 12.3 Prompt Refusal

**What it looks like:** Early chatbots occasionally declined prompts with apologies and reminders that they are AI. These refusals were accidentally pasted into Wikipedia. Now very rare. (Gemini 3.0 even uses profanity at times.)

**Real example:**
> "As an AI language model, I can't directly add content to Wikipedia for you, but I can help you draft your bibliography."

---

### 12.4 Abrupt Cut-Offs

**What it looks like:** Older AI tools hit token limits, causing articles to end mid-sentence. Now very rare due to larger context windows.

**Note:** Not foolproof — a malformed copy/paste or a copyright violation can also cause abrupt endings.

---

### 12.5 Outdated `access-date` Parameters

**What it looks like:** Citations include access dates significantly older than when the edit was made (e.g., article created December 2025 with `|access-date=12 December 2024`).

**Note:** Newer chatbots rarely produce this error. Older access dates can also occur legitimately (copied citations, offline work, batch merges).

---

## Quick Reference Cheat Sheet

### 🚩 Highest Confidence AI Indicators
1. `oaicite`, `contentReference`, `grok_card`, `grok_render_citation_card_json`, `turn0search0` (including PUA characters like `citeturn0search0` and `0`), `【N†LN-N】` in text
2. `utm_source=chatgpt.com` / `utm_source=openai` / `referrer=grok.com` in URLs
3. Markdown syntax in Wikipedia (`**`, `*`, `##`) or fenced code blocks (` ```wikitext ` / ` ``` `)
4. Knowledge-cutoff disclaimers left in article text
5. Placeholder text like "[Insert citation here]" or empty template parameters like `access-date=2025-XX-XX`
6. Invalid / unresolvable DOIs and ISBNs
7. "Featured in *X*, *Y*, and **other prominent media outlets**" phrasing
8. Pre-placed `{{AfC submission|d}}` with no decline notice content
9. Subject lines beginning "Subject: Request for Permission to Edit..."

### 🟡 Strong AI Vocabulary Words (Source-Backed)
`delve` • `underscore` • `tapestry` • `testament` • `pivotal` • `robust` • `vibrant` • `highlight` (verb) • `fostering` • `enduring` • `enhance` • `showcase` • `garner` • `bolstered` • `intricate` • `meticulous` • `valuable` • `align with` • `landscape` (abstract) • `boasts` (meaning "has") • `Additionally` (sentence-start)

### 🟡 AI Structural Patterns
- Inline-header bulleted lists (**Bold:** description)
- "Not just X, but also Y" / "Not X, but Y" constructions
- Rule of three adjectives/clauses
- Over-explained "significance" and "legacy"
- Predictable "Despite challenges... continues to thrive" endings
- Excessive use of em dashes
- Overuse of bold text
- Rigid article outline: Intro → Background → Significance → Challenges → Future Prospects

### ✅ Signs of Human Writing
- Text predates ChatGPT (before Nov 30, 2022)
- Editor can explain specific editorial choices
- Specific facts, dates, names — not vague generalizations
- Simple copulative sentences ("X is Y")
- Consistent and stable writing style over time
- Consistent English variety (matching user's location/topic national ties)
- Same stylistic quirks (even imperfections) across old and new edits

---

## Notes for Our Humanizer Project

Based on this complete guide, the humanizer must specifically:

1. **Remove or replace AI vocabulary words** — delve, testament, tapestry, pivotal, underscore, bolstered, fostering, enduring, enhance, garner, intricate, meticulous, vibrant, align with, boasts, showcase, landscape (abstract), highlight (verb), valuable, Additionally (sentence-start)
2. **Break up inline-header lists** into flowing prose
3. **Eliminate "Not just X, but also Y" and "Not X, but Y"** constructions
4. **Remove excessive emphasis on significance/legacy/trends** — no more "pivotal moments," "evolving landscapes," "testament to"
5. **Replace elegant variation** with natural repetition of key terms
6. **Simplify to direct "X is Y" sentences** instead of complex participial constructions
7. **Remove vague attributions** ("experts believe," "critics note," "researchers argue") — replace with specific ones or remove
8. **Eliminate em dash overuse** — use commas, semicolons, or new sentences
9. **Remove any residual AI artifacts** (oaicite, contentReference, utm_source, turn0search0, etc., including PUA unicode points like `citeturn0search0` and `0`)
10. **Break the "rule of three"** pattern — vary list lengths
11. **Add specificity** — replace generic statements with concrete details
12. **Remove puffery and promotional language** — "nestled," "vibrant," "diverse array," "in the heart of"
13. **Remove superficial -ing phrase analyses** — "...contributing to the broader narrative"
14. **Remove "challenges and future prospects"** boilerplate endings
15. **Remove "active social media presence"** and similar notability-claiming language
16. **Remove conservation status boilerplate** in biology articles when status is unknown
17. **Ensure no knowledge-cutoff disclaimers** leak into output
18. **Ensure no collaborative communication phrases** leak into output
19. **Vary sentence-opening words** — don't start consecutive sentences with the same structure
20. **Ensure no Markdown fenced code blocks (three backticks ` ``` ` or ` ```wikitext `)** remain in the output.
21. **Replace "maintains a low profile" / "keeps personal details private"** speculative phrases.
22. **Remove "concrete evidence" / "concrete examples"** phrasing in defensive talk-page-style text.
23. **Correct any knowledge-cutoff disclaimers** like "not widely documented/transcribed/available in sources."

---

*Last updated from Wikipedia source: June 2026 (full line-by-line audit)*  
*Source revision ID: 1357393965*
