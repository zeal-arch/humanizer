Title: Live Content

Description: Fetched live

Source: https://en.wikipedia.org/w/index.php?title=Wikipedia:Signs_of_AI_writing&action=raw

{{redirect|Wikipedia:AI writing| other uses|WP:AI-INDEX}} {{WikiProject advice|wikiproject=WikiProject AI Cleanup|WP:AISIGNS|WP:AITELLS|WP:LLMSIGNS}} [[File:ChatGPT response screenshot 1.jpg|thumb|alt=A screenshot of ChatGPT reading: "[header] Legacy & Interpretation [body] The "Black Hole Edition" is not just a meme — it's a celebration of grassroots car culture, where ideas are limitless and fun is more important than spec sheets. Whether powered by a rotary engine, a V8 swap, or an imagined fighter jet turbine, the Miata remains the canvas for car enthusiasts worldwide."|LLMs tend to have an identifiable writing style.]] This is a list of writing and formatting conventions typical of [[AI chatbot]]s such as [[ChatGPT]], with real examples taken from Wikipedia articles, drafts, comments, and other content. It is a [[field guide]] to help detect [[WP:LLMDISCLOSE|undisclosed AI-generated content]] ''on Wikipedia'': while some of the signs may be broadly applicable, some may not apply in a non-Wikipedia context.{{efn|Specifically, this guide is less useful for texts which are not informational writing. For example, the many tells specific to fiction (whispering woods, [https://maxread.substack.com/p/who-is-elara-voss Elara Voss], etc.) are less relevant in Wikipedia and are not listed here.}} Not all text featuring these indicators is AI-generated, as the [[large language model]]s that power AI chatbots are trained on human writing, including Wikipedia. Many elements of AI writing can be found in editorials, blogs, or fan fiction.

Moreover, this list is {{em|descriptive}}, not {{em|prescriptive}}; it consists of observations, not rules. Advice about formatting or language to avoid can be found in the [[Wikipedia:PAG|policies and guidelines]] and the [[Wikipedia:MOS|Manual of Style]], but does not belong on this page.

The patterns here are also only potential {{em|signs}} of a problem, not {{em|the problem itself}}. While many of these issues are immediately obvious and easy to fix{{--}}e.g., excessive boldface, broken markup, citation style quirks{{--}}they can point to less outwardly visible problems that carry [[WP:AIFAIL|much more serious policy risks]]. Please do not merely treat these signs as the problems to be fixed; that could just make detection harder. The actual problems are those deeper concerns, so make sure to address them, either yourself or by flagging them, per the advice at {{slink|Wikipedia:Large language models#Handling suspected LLM-generated content}} and [[Wikipedia:WikiProject AI Cleanup/Guide]].

The [[Wikipedia:Speedy deletion|speedy deletion policy]] criterion [[WP:G15|G15]] (LLM-generated pages without human review) lists some signs of AI writing, but is limited to the most objective ones. The remaining signs covered here are not sufficient on their own for speedy deletion.

==Caveats== ===AI detection tools=== Do not solely rely on [[artificial intelligence content detection]] tools (such as [[GPTZero]]). While they perform better than random chance, these tools have non-trivial error rates.{{cite journal |last1=Dik |first1=Selin |last2=Erdem |first2=Osman |last3=Dik |first3=Mehmet |title=Assessing GPTZero's Accuracy in Identifying AI vs. Human-Written Essays |journal=arXiv |date=2025 |arxiv=2506.23517 }} Detectors can be susceptible to factors such as text modifications (e.g. paraphrasing, markup, and spacing changes) and the use of models not seen during detector training.{{cite conference|last1=Dugan|first1=Liam|last2=Hwang|first2=Alyssa|last3=Trhlik|first3=Filip|last4=Zhu|first4=Andrew|last5=Ludan|first5=Josh Magnus|last6=Xu|first6=Hainiu|last7=Ippolito|first7=Daphne|last8=Callison-Burch|first8=Chris|title=RAID: A Shared Benchmark for Robust Evaluation of Machine-Generated Text Detectors|conference=Proceedings of the 62nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)|year=2024|pages=12463–12492|location=Bangkok, Thailand|publisher=Association for Computational Linguistics|arxiv=2405.07940|url=https://aclanthology.org/2024.acl-long.674|access-date=2025-11-08|archive-date=2025-08-24|archive-url=https://web.archive.org/web/20250824132743/https://aclanthology.org/2024.acl-long.674/|url-status=live}}

===Your detection ability=== {{Shortcut|WP:AIDETECTIVE}} {{ombox|image=none|style=background-color: light-dark(#FFEFFC, #1E0517); color: light-dark(#202122, #eaecf0); height: 4em;|textstyle=text-align: center;|text='''Test your AI detection skills at [[Wikipedia:AI or not quiz]].'''}} Do not rely too much on your own judgment. Humans are notoriously bad at distinguishing human and LLM-generated text. While research on humans' abilities to detect AI-generated text is still limited, a 2025 study has shown that human ability to distinguish LLM text from human is no better than random chance.{{cite journal |last1=Cheng |first1=Adam |last2=Lin |first2=Yiqun |last3=Reedy |first3=Gabriel |last4=Joseph |first4=Christine |last5=Wirkowski |first5=Samantha |last6=Mallette |first6=Viviane |last7=Nagesh |first7=Vikhashni |last8=Krieser |first8=David |last9=Calhoun |first9=Aaron |title=Ability of AI detection tools and humans to accurately identify different forms of AI-generated written content |journal=Advances in Simulation |date=2025 |volume=10 |issue=1 |article-number=66 |doi=10.1186/s41077-025-00396-6 |doi-access=free |pmid=41272826 |pmc=12752165 }} Another 2025 study on German theses has shown that humans managed a "recognition rate of 57 % for AI texts and 64 % for human-generated texts".{{cite journal |last1=Fiedler |first1=Alexandra |last2=Döpke |first2=Jörg |title=Do humans identify AI-generated text better than machines? Evidence based on excerpts from German theses |journal=International Review of Economics Education |date=2025 |volume=49 |article-number=100321 |doi=10.1016/j.iree.2025.100321 }}

A 2025 preprint has shown that heavy users of LLMs can correctly determine whether an article was generated by AI about 90% of the time, which means that if you are an expert user of LLMs and you tag 10 pages as being AI-generated, you've probably made one false positive. People who don't use LLMs much do only slightly better than random chance (in both directions).

One has to be aware that human speech and writing is being influenced by LLMs, and thus they are becoming more similar. This was already evident in 2024, as shown by a study that detected a significant LLM influence in spoken content (e.g. conversational podcasts).{{cite journal |last1=Yakura |first1=Hiromu |last2=Lopez-Lopez |first2=Ezequiel |last3=Brinkmann |first3=Levin |last4=Serna |first4=Ignacio |last5=Gupta |first5=Prateek |last6=Soraperra |first6=Ivan |last7=Rahwan |first7=Iyad |title=Empirical evidence of Large Language Model's influence on human spoken communication |date=2024 |arxiv=2409.01754 |journal=arXiv}} Further studies seem to confirm this influence on language,{{cite book |last1=Geng |first1=Mingmeng |last2=Chen |first2=Caixi |last3=Wu |first3=Yanru |last4=Wan |first4=Yao |last5=Zhou |first5=Pan |last6=Chen |first6=Dongping |title=Findings of the Association for Computational Linguistics: ACL 2025 |chapter=The Impact of Large Language Models in Academia: From Writing to Speaking |date=2025 |pages=19303–19319 |doi=10.18653/v1/2025.findings-acl.987 }} including semantics and word choices.{{cite journal |last1=Galpin |first1=Riley |last2=Anderson |first2=Bryce |last3=Juzek |first3=Tom S. |title=Exploring the Structure of AI-Induced Language Change in Scientific English |journal=The International Flairs Conference Proceedings |date=2025 |volume=38 |doi=10.32473/flairs.38.1.138958 |arxiv=2506.21817 }}

It is also worth noting that writers may adjust their behavior to avoid accusations of AI, or may be defensive about using AI tropes.

==Content== {{Shortcut|WP:AIWTW|WP:AI-ISM|WP:LLMISM}}

LLMs (and [[artificial neural network]]s in general) use statistical algorithms to guess (infer) what should come next based on a large corpus of training material. It thus tends to [[regression to the mean|regress to the mean]]; that is, the result tends toward the most statistically likely result that applies to the widest variety of cases. It can simultaneously be a strength and a "tell" for detecting AI-generated content.

For example, LLMs are usually trained on data from the internet in which famous people are generally described with positive, important-sounding language. Consequently, the LLM tends to omit specific, unusual, nuanced facts (which are statistically rare) and replace them with more generic, positive descriptions (which are statistically common). Thus the highly specific "inventor of the first train-coupling device" might become "a revolutionary titan of industry". It is like shouting louder and louder that a portrait shows a uniquely important person, while the portrait itself is fading from a sharp photograph into a blurry, generic sketch. The subject becomes simultaneously less specific and more exaggerated.{{efn|This can be directly observed by examining images generated by [[text-to-image model]]s; they look acceptable at first glance, but specific details tend to be blurry and malformed. This is especially true for background objects and text.}}

This statistical regression to the mean, a smoothing over of specific facts into generic statements, that could equally apply to many topics, makes AI-generated content easier to detect.

===Undue emphasis on significance, legacy, and broader trends === {{shortcut|WP:AILEGACY|WP:AITREND}} {{tmbox|image=none|text=Words to watch: {{strong|''stands/serves as'', ''is a testament/reminder'', ''a vital/significant/crucial/pivotal/key role/moment'', ''underscores/highlights its importance/significance'', ''reflects broader'', ''symbolizing its ongoing/enduring/lasting'', ''contributing to the'', ''setting the stage for'', ''marking/shaping the'', ''represents/marks a shift'', ''key turning point'', ''evolving landscape'', ''focal point'', ''indelible mark'', ''deeply rooted'',  ...}}}} LLM writing often [[Wp:puffery|puffs up]] the importance of the subject matter by adding statements about how arbitrary aspects of the topic represent or contribute to a broader topic. There is a distinct and easily identifiable repertoire of ways that it writes these statements.

{{blockquote| The Statistical Institute of Catalonia was officially established in 1989, {{highlight|marking a pivotal moment}} in the evolution of regional statistics in Spain. [...]

The founding of Idescat {{highlight|represented a significant shift}} toward regional statistical independence, enabling [[Catalonia]] to develop a statistical system tailored to its unique socio-economic context. This initiative {{highlight|was part of a broader movement}} across Spain to decentralize administrative functions and enhance regional governance. |From [[Special:Diff/1252053288|this September 2024 revision]] to [[Statistical Institute of Catalonia]]}}

{{blockquote|Kumba has long been {{highlight|an important center}} for trade and agriculture. [...] The establishment of road networks connecting Kumba to other parts of the Southwest Region, such as Mamfe and Buea, helped {{highlight|solidify its role as a regional hub}}. |From [[Special:Diff/1248482444|this October 2024 revision]] to [[Kumba, Cameroon]]}}

LLMs may include these statements for even the most mundane of subjects like etymology or population data. Sometimes, they add hedging preambles acknowledging that the subject is of relatively low importance, before talking about its importance anyway.

'''Examples'''

{{blockquote|text=During the [[Spanish Colonial Period (Philippines)|Spanish colonial period]], the name ''Bakunutan'' was hispanized to ''Bacnotan'', a modification reflected in official documents preserved in the [[National Archives of the Philippines|National Archives]] in Manila. {{highlight|This etymology highlights the enduring legacy}} of the community's resistance and {{highlight|the transformative power}} of unity in shaping its identity.|title=From [[Special:Diff/1265870147|this December 2024 revision]] to [[Bacnotan]]}}

{{blockquote|text={{highlight|Though it saw only limited application}}, it {{highlight|contributes to the broader history}} of early aviation engineering and {{highlight|reflects the influence of French rotary designs}} on German manufacturers.|title=From Draft:Goebel Goe II (July 2025)}}

When talking about biology (e.g., when asked to discuss an animal or plant species), LLMs tend to over-emphasize connections to the broader ecosystem or environment, even when those connections are tenuous or generic. LLMs also tend to belabor the species' conservation status and research and preservation efforts, even if the status is unknown and no serious efforts exist.

'''Examples'''

{{blockquote|text=Currently, {{highlight|there is no specific conservation assessment}} for ''Lethrinops lethrinus'' by the International Union for Conservation of Nature (IUCN). However, the general health of the Lake Malawi ecosystem is {{highlight|crucial for the survival of this and other endemic species}}. Factors such as overfishing, pollution, and habitat destruction could potentially impact their populations. |title=From [[Special:Diff/1235454313|this July 2024 revision]] to [[Lethrinops lethrinus]]}}

{{blockquote|text=It {{highlight|plays a role in the ecosystem}} and {{highlight|contributes to Hawaii's rich cultural heritage}}. [...] {{highlight|Preserving this endemic species is vital}} not only for ecological diversity but also for sustaining the cultural traditions connected to Hawaii’s native flora.|title=From [[Special:Diff/1262033910|this December 2024 revision]] to [[Nototrichium divaricatum]]}}

===Canned emphasis on notability, attribution, and media coverage=== {{shortcut|WP:OVERATTRIBUTION|WP:AIATTR}}{{anchor|Attribution}} {{tmbox|image=none|text=Words to watch: {{strong|''independent coverage'', ''local/regional/national/[country name] media outlets'', ''music/business/tech outlets'', ''profiled in'', ''written by a leading expert'', ''active social media presence''}}}} Similarly, LLMs act as if the best way to prove that a subject is notable is to hit readers over the head with claims of notability, often by listing sources that a subject has been covered in and specifying what kind of sources they are (e.g., trade publications, regional media, etc). They often inaccurately attribute their own [[#Superficial analyses|superficial analyses]] to the source. This is more common in text from newer AI tools (2025 or later).

Human-written press releases have of course also cited news clippings for decades, but LLMs specifically asked to write a Wikipedia article often echo the exact wording of [[WP:N|Wikipedia's guidelines]], such as "independent coverage."

'''Examples''' {{blockquote| She spoke about AI on CNN, and was {{highlight|featured in}} Vogue, Wired, Toronto Star, and {{highlight|other media}}. [...] Her insights have also been {{highlight|featured in}} Wired, Refinery29, and {{highlight|other prominent media outlets}}. |From [[Special:Diff/1276225083|this February 2025 revision]] to [[Sinead Bovell]] (also note the [[#Use_of_Markdown|use]] of [[Markdown]])}}

{{blockquote|Her views have been {{highlight|cited in}} ''The New York Times'', ''BBC'', ''Financial Times'', and ''The Hindu''.|From [[Special:Diff/1285114966|this April 2025 revision]] to [[Shamika Ravi]]}}

{{blockquote|Its significance is {{highlight|documented in archived school event programs and regional press coverage}}, including the Mesabi Daily News, which regularly reviewed performances held there.|From [[Special:Diff/1294930957|this June 2025 revision]] to [[Virginia High School (Minnesota)]] (also note the [[#Use_of_Markdown|use]] of [[Markdown]])}}

{{blockquote|{{fmbox|image=none|text= The subject has been profiled in multiple high-quality, independent, and widely-read outlets, including The Australian, SBS News, 7News, and coverage syndicated through the Associated Press—appearing in platforms like The Senior and Perth Now. These sources provide significant, substantial, secondary coverage, not trivial mentions or press releases.
• Repeated national media coverage for both professional and advocacy work (reported by SBS, 7News, The Australian, etc.) • Leadership roles in international and national health campaigns (e.g., THINK Aorta ANZ and board member of Hearts4Heart) • National ambassador role for the National Heart Foundation of Australia, highlighted by multiple independent reports • Academic and economic contributions recognised by universities, specialist publications, and health system institutions (e.g., University of Sydney, Monash University, RANZCR) • Ongoing public presence in respected media and at speaking events over multiple years, including via independent news commentary, landmark survival stories, and national health initiatives Together, these factors clearly demonstrate significant, sustained, and verifiable coverage—meeting both WP:BIOSIGand WP:SIGCOV. }}|From [[Special:Diff/1320014555|this November 2025 revision]] to [[Wikipedia:WikiProject Articles for creation/Help desk]] (note that [[WP:BIOSIG]] is [[WP:AISHORTCUT|not a real shortcut]])}} {{blockquote|{{fmbox|image=none|text= {{fake section|Media coverage}}

IRNA – {{highlight|Coverage}} of his inter-city marathon events.
ISNA – {{highlight|Report}} on an 80 km provincial peace run.
IFRC – {{highlight|Feature}} on his humanitarian campaigns.
Fars News – {{highlight|Interview}} on his national running projects.
Varzesh3 – {{highlight|Report}} on a 17-day endurance run.
Borna News – {{highlight|Profile}} on his athletic background. }}|From a December 2025 version of {{oldid2|1326136318|Draft:Mojtaba Yadegari (Iranian runner)}} (note the [[#Use_of_Markdown|use of Markdown]])}}
On Wikipedia specifically, LLMs often painstakingly emphasize their sources in the body text—even for trivial coverage, uncontroversial facts, or other situations where a human Wikipedia editor would be more likely to either provide an inline citation or no source at all.

'''Examples''' {{blockquote|text=The restaurant {{highlight|has also been mentioned in [[ABC News (Australia)|ABC News]] coverage relating to}} incidents in the surrounding precinct, underscoring its role as a well-known late-night venue in the city [of [[Adelaide]]].|title= Trivial coverage with attribution, from [[Special:Permalink/1305163154|this August 2025 revision]] to [[The Original Pancake Kitchen]]; the reference added for this sentence did not exist.}}

In articles about people or entities that use social media, LLMs will often note that they "maintain an active social media presence" or something similar. This wording is particularly idiosyncratic to AI text and relatively uncommon on Wikipedia before ~2024.

'''Examples''' {{blockquote|The mall {{highlight|maintains a strong digital presence}}, particularly on Instagram, where it actively shares the latest updates and events. Forum Kochi has consistently demonstrated excellence in digital promotions, with high-quality, engaging, and impactful video content playing a key role in its outreach.|From [[Special:Diff/1297291381|this June 2025 revision]] to [[Forum Mall Kochi]]}}

===Superficial analyses=== {{shortcut|WP:SUPERFICIAL}} {{tmbox|image=none|text=Words to watch: {{strong|''highlighting/underscoring/emphasizing ...'', ''ensuring ...'', ''reflecting/symbolizing ...'', ''contributing to ...'', ''cultivating/fostering ...'', ''encompassing ...'', ''valuable insights'', ''align/resonate with'', }} }} AI chatbots tend to insert superficial analysis of information, often in relation to its significance, recognition, or impact.{{cite journal |last1=Reinhart |first1=Alex |last2=Markey |first2=Ben |last3=Laudenbach |first3=Michael |last4=Pantusen |first4=Kachatad |last5=Yurko |first5=Ronald |last6=Weinberg |first6=Gordon |last7=Brown |first7=David West |title=Do LLMs write like humans? Variation in grammatical and rhetorical styles |journal=[[Proceedings of the National Academy of Sciences]] |volume=122 |issue=8 |date=2025-02-25 |issn=0027-8424 |pmc=11874169 |doi=10.1073/pnas.2422455122 |url=https://pnas.org/doi/10.1073/pnas.2422455122 |access-date=2026-01-29}} This is often done by attaching a [[Participle#Forms|present participle]] ("-ing") phrase at the end of sentences, sometimes with [[WP:AIWEASEL|vague attributions]] to third parties (see below).

For the purpose of Wikipedia, such comments are usually [[WP:SYNTH|synthesis]] or unattributed opinions. Newer chatbots with [[retrieval-augmented generation]] (for example, an AI chatbot that can search the web) may attach these statements to [[#Undue emphasis on notability, attribution, and media coverage|named sources]]—e.g., "Roger Ebert highlighted the lasting influence"—regardless of whether those sources say anything close.

'''Examples''' {{blockquote|text=As of the April 2008 census, the population of Douera stood at approximately 56,998 inhabitants, {{highlight|creating a lively community within its borders.}} Situated in the central-north region of the country, Douera enjoys close proximity to the capital city, Algiers, {{highlight|further enhancing its significance as a dynamic hub of activity and culture.}} With its coastal charm and convenient location, Douera captivates both residents and visitors alike, {{highlight|offering a diverse range of experiences against the backdrop of Algeria's stunning natural beauty.}}|title=From {{diff||1161677884|label=this June 2023 revision}} to [[Douéra]]}}

{{blockquote| It holds a pivotal place in the [[East Central Railway Zone]] of [[Indian Railways]], {{highlight|serving as a major railway hub with historical significance.}} The station has {{RailGauge|1676mm|lk=on}} [[broad gauge]] along with 8 tracks and 6 platforms. [...] Historically, it has been crucial for linking [[Darbhanga]] with significant cities like [[Delhi]], [[Patna]], and [[Kolkata]], {{highlight|facilitating the movement of passengers and goods.}} The station has supported various services, including passenger trains and express trains like the [[Satyagrah Express]] and [[Mithila Express]], {{highlight|contributing to the socio-economic development of the region.}} [...] Over the years, Darbhanga Junction has seen several upgrades and modernization efforts aimed at improving facilities and operational efficiency, {{highlight|reflecting its continued relevance in the regional and national transportation landscape.}} |From [[Special:Diff/1240127604|this August 2024 revision]] to [[Darbhanga Junction railway station]]}}

{{blockquote| The civil rights movement emerged as a powerful continuation of this struggle, {{highlight|emphasizing the importance of solidarity and collective action in the fight for justice.}} This historical legacy has influenced contemporary African-American families, {{highlight|shaping their values, community structures, and approaches to political engagement.}} Economically, the enduring impacts of systemic inequality have led to both challenges and innovations within African-American communities, {{highlight|driving a commitment to empowerment and social change that echoes through generations.}} |From [[Special:Diff/1253182873|this October 2024 revision]] to [[African-American culture]]}}

{{blockquote| Situated just a few miles from the U.S.-Mexico border—{{highlight|a line that often represents separation and division}}—the temple {{highlight|stands as a counter-symbol, emphasizing unity, togetherness, and transcendent faith.}} In a region where many families and communities span both countries, the temple {{highlight|fosters a sense of connection and shared purpose.}} Through its inclusive design and symbolic features, the McAllen Texas Temple is seen as a bridge across divides, {{highlight|embodying the spirit of unity that underlies its sacred purpose.}} Its bilingual monument sign, with inscriptions in both English and Spanish, {{highlight|underscores its role in bringing together Latter-day Saints}} from the United States and Mexico.

The temple’s architectural and decorative elements are thoughtfully imbued with local symbolism, {{highlight|reflecting the rich culture and landscape of the Rio Grande Valley.}} Citrus blossom motifs, seen throughout the exterior and interior, {{highlight|celebrate the area’s agricultural roots and its vital citrus industry.}} The temple’s color palette of blue, green, and gold {{highlight|resonates with the region’s natural beauty,}} symbolizing Texas bluebonnets, the Gulf of Mexico, and the diverse Texan landscapes. These colors and patterns {{highlight|evoke enduring faith and resilience, qualities that resonate deeply within this close-knit, cross-border community.}}

In design and structure, the McAllen Texas Temple {{highlight|honors the Spanish colonial heritage that has historically shaped the area.}} By incorporating these architectural elements, the temple connects to both the Latin American influences and the historic roots of the border region, {{highlight|creating a space where the past and present come together.}} |From [[Special:Diff/1256905241|this November 2024 revision]] to [[McAllen Texas Temple]]}}

{{blockquote|text= {{fmbox|image=none|text= These works are now part of the Collections of the National Museum of Education - Réseau Canopé (France), {{highlight|highlighting their historical and pedagogical significance.}}

His influence persists in more recent studies. In 2010, ''Les néologismes dans l'hebdomadaire L'Express'' (1980) was cited in the ''Proceedings of the 1st International Congress on Neology in Romance Languages'' [...] {{highlight|demonstrating the ongoing relevance of his research on lexical evolution.}} [...] In 2004, the ''Cahiers de lexicologie'' (issues 84-87), published by the [[French National Centre for Scientific Research|CNRS]], cited the ''Grammaire Blois'', {{highlight|confirming its relevance in modern research.}} [...]

These citations, spanning more than six decades and appearing in recognized academic publications, {{highlight|illustrate Blois' lasting influence in computational linguistics, grammar, and neology.}}

Fridrichová analyzes the distinction made by Blois and Bar between acronyms, abbreviations, and truncations, {{highlight|emphasizing their critical view on the impact of truncations in the French language.}}

[...]

Fridrichová highlights that Blois and Bar perceive truncations as a distortion of the language rather than an enrichment, {{highlight|a perspective that still fuels linguistic debates today.}} This citation {{highlight|demonstrates the enduring relevance of Blois's work in modern linguistic studies and its critical reception by researchers.}} }} |title=From [[Special:Diff/1279776010|this March 2025 revision]] to [[Draft:Jacques Blois (linguist)]], the top and bottom paragraphs also feature [[WP:MARKDOWN|markdown]]}}

AI chatbots occasionally claim that certain things or actions have resulted in discussions about related concepts.

{{blockquote| {{fmbox|image=none|text= The phenomenon has generated debate about authenticity, consent, and the psychological effects of digitally extending personhood.

[...]

Collectively, these works have shaped emerging policy discussions about ownership, consent, and dignity in digital resurrection technologies.

[...]

GriefBots have prompted broader reflection on mortality and memory in a digital age. They blur boundaries between life and data, raising philosophical questions about identity, authenticity, and what it means to “live on” through algorithms. }} |From [[Special:Diff/1317624451|this October 2025 revision]] to [[Deadbot]]; each sentence here follows the [[WP:RO3|rule of three]], and the last one uses [[WP:AICURLY|curly quotation marks]]}}

===Promotional and advertisement-like language=== {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style/Words to watch#Puffery}} {{see also|Wikipedia:Marketing buzzspeak#Artificial intelligence and marketing buzzspeak}} {{Shortcut|WP:AIPUFFERY|WP:AIPEACOCK}} {{tmbox|image=none|text=Words to watch: {{strong|''boasts a'', ''vibrant'', ''rich'', ''profound'', ''enhancing'', ''showcasing'', ''exemplifies'', ''commitment to'', ''natural beauty'', ''nestled'', ''in the heart of'', ''groundbreaking'', ''renowned'', ''featuring'', ''diverse array'',  ...}}}} LLMs have serious problems keeping a neutral tone. Even when prompted to use an encyclopedic style, their output will often tend toward advertisement-like writing, or like the prose of a travel guide. This may happen when generating new text or rewriting existing text: for instance, an edit summary claiming a rewrite "removed promotional tone" while actually introducing it. This may also happen when editors are not [[WP:COI|deliberately trying to advertise]] a subject.{{cite web |last1=Walker Rettberg |first1=Jill |title=Genre glitches and unexpected promotional phrases as a sign of AI writing |url=https://jilltxt.net/genre-glitches-and-unexpected-promotional-phrases-as-a-sign-of-ai-writing/ |website=jilltxt |access-date=13 May 2026}}

Note: Not all promotional or spammy writing is AI-generated. LLMs tend to over-use the same set of promotional phrases no matter what the topic. Also, older LLMs (e.g., GPT-4) tend to output more blatantly positive text{{cite web |last1=Sussman |first1=Kristen |last2=Carter |first2=Daniel |title=Detecting Effects of AI-Mediated Communication on Language Complexity and Sentiment |url=https://arxiv.org/abs/2504.19556 |website=Companion Proceedings of the ACM Web Conference 2025 |publisher=arXiv |access-date=13 May 2026}} than newer LLMs, which are more subtly positive and tend to avoid obviously superlative statements like "the best."

====Subtypes====

When writing about something that could be considered "cultural heritage" (even Japan's electronics industry), LLMs [[#Undue emphasis on significance, legacy, and broader trends|constantly remind the reader of its importance]].

{{blockquote|text={{highlight|Nestled}} within the {{highlight|breathtaking}} region of Gonder in Ethiopia, Alamata Raya Kobo {{highlight|stands as a vibrant town with a rich cultural heritage and a significant place}} within the Amhara region. {{highlight|From its scenic landscapes to its historical landmarks}}, Alamata Raya Kobo {{highlight|offers visitors a fascinating glimpse into the diverse tapestry}} of Ethiopia. In this article, we will explore the {{highlight|unique characteristics}} that make Alamata Raya Kobo {{highlight|a town worth visiting}} and shed light on {{highlight|its significance}} within the Amhara region. |title=From {{diff||1162718043|label=this June 2023 revision}} to [[Alamata (woreda)]] }} {{blockquote|text= TTDC {{highlight|acts as the gateway}} to Tamil Nadu’s {{highlight|diverse attractions}}, seamlessly connecting the beginning and end of {{highlight|every traveller's journey}}. It offers {{highlight|dependable, value-driven experiences}} that showcase the state’s {{highlight|rich history, spiritual heritage, and natural beauty}}. |title=From {{diff||1299567515|label=this July 2025 revision}} to [[Tamil Nadu Tourism Development Corporation]] }}

When writing about people or companies, LLMs will often adopt a press-release or commercial-esque tone.

{{blockquote|text=These projects {{highlight|align with KQ's goals of reducing its environmental footprint, improving operational efficiency, and fostering community development through job creation.}} CEO Allan Kilavuka {{highlight|emphasized the airline's commitment to sustainability, customer focus, and Africa's prosperity through responsible corporate practices.}}|title=from [[Special:Diff/1259548187|this November 2024 revision]] to [[Kenya Airways]]; note the multiple [[#Superficial analyses|superficial analyses]]}}

{{blockquote|text=The SOLLEI’s exterior design {{highlight|communicates a powerful emotional presence, staying true to Cadillac's signature bold proportions.}} Its low, elongated silhouette is highlighted by a wide stance and an extended coupe door, {{highlight|which enhances accessibility to the spacious rear cabin.}} Smooth, uninterrupted surfaces and a pronounced A-line {{highlight|accentuate the vehicle’s overall length,}} while a sleek, low tail {{highlight|imparts a sense of refined dynamism.}} A mid-body line runs seamlessly from the headlamps to the taillights, {{highlight|reinforcing the car’s cohesive and elegant design.}} Traditional door handles have been replaced with discrete buttons, {{highlight|preserving the vehicle’s clean and modern profile.}} In a nod to Cadillac’s legacy of bold color choices, the exterior is finished in "Manila Cream"—a distinctive hue originally offered in 1957 and 1958. This heritage color has been thoughtfully revived and hand-painted by Cadillac artisans, {{highlight|showcasing the brand’s dedication to craftsmanship and historical reverence.}}|title=From [[Special:Diff/1285549984|this April 2025 revision]] to [[Cadillac Sollei]]}}

===Vague attributions and overgeneralization of opinions=== {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style/Words to watch#Unsupported attributions}} {{Shortcut|WP:AIWEASEL}} {{tmbox|image=none|text=Words to watch: {{strong|''Industry reports'', ''Observers have cited'', ''Experts argue'', ''Some critics argue'', ''several sources/publications'' (when only few sources are cited), ''such as'' (before exhaustive word lists),  ...}}}} AI chatbots tend to attribute opinions or claims to some vague authority—a practice called [[weasel wording]].

'''Examples'''

{{quote|Due to its unique characteristics, the Haolai River is of interest to {{highlight|researchers and conservationists}}. Efforts are ongoing to monitor its ecological health and preserve the surrounding grassland environment, which is part of a larger initiative to protect China’s semi-arid ecosystems from degradation. |title=From [[Special:Diff/1295362066|this June 2025 revision]] to [[Haolai River]]}}

{{quote|The Kwararafa (Kororofa) confederacy is {{highlight|described in scholarship}} as a shifting [[Benue valley]] coalition led by [[Jukun]] groups and incorporating a range of [[Middle Belt]] peoples. Because much of the historical record derives from [[Hausa]] chronicles, Bornu sources and oral tradition, {{highlight|modern researchers treat}} Kwararafa as a fluid political and cultural formation rather than a fixed state. |From [[Special:Diff/1323819205|this November 2025 revision]] to [[Kwararafa Confederacy]]}}

AI chatbots also commonly exaggerate the quantity of sources that these opinions are attributed to. They may present views from one or two sources as widely held (often combined with the vague attributions above), mention the existence or opinion of multiple "reviewers" or "scholars" while only citing one person, or imply that lists of examples are non-exhaustive when the sources give no indication that other examples exist.

'''Examples''' {{blockquote| While Pakistan was not directly named, the reference to cross-border terrorism, {{highlight|according to Indian sources,}} was widely interpreted as aimed at Islamabad.{{Cite web |date=2025-07-07 |title=BRICS leaders condemn April 22 Pahalgam attack: On terror, zero tolerance |url=https://indianexpress.com/article/india/brics-leaders-condemn-jk-pahalgam-attack-on-terror-zero-tolerance-10110505/ |access-date=2025-07-10 |website=The Indian Express |language=en}} |From [[Special:Diff/1299755238|this July 2025 revision]] to [[BRICS]]}}

{{blockquote| {{highlight|Toy industry publications such as}} ''The Toy Insider'' and ''Mojo Nation'' have presented Rubik's WOWCube as a STEM-oriented platform that brings the Rubik's Cube "into the future" with motion controls and an open software ecosystem.{{cite web |date=31 October 2025 |title=Rubik’s WOWCube |url=https://thetoyinsider.com/products/rubiks-wow-cube/ |access-date=2 December 2025 |website=The Toy Insider}}{{cite web |date=26 July 2025 |title=Cubios Inc teams with Spin Master for Rubik’s WOWCube gaming platform |url=https://www.mojo-nation.com/cubios-inc-teams-with-spin-master-for-rubiks-wowcube-gaming-platform/ |access-date=2 December 2025 |website=Mojo Nation}}| From [[Special:Diff/1325377957|this December 2025 revision]] to [[Rubik's WOWCube]].}} {{Reflist-talk|group=overgen}}

=== Outline-like conclusions about challenges and future prospects === {{tmbox|image=none|text=Words to watch: {{strong|''Despite its... faces several challenges...'', ''Despite these challenges'', ''Challenges and Legacy'', ''Future Outlook'' ...}}}} Many LLM-generated Wikipedia articles include a "Challenges" section, which typically begins with a sentence like "Despite its [positive/promotional words], [article subject] faces challenges..." and ends with either a vaguely positive assessment of the article subject, or speculation about how ongoing or potential initiatives could benefit the subject. Such paragraphs usually appear at the end of articles with a rigid outline structure, which may also include a separate section for "Future Prospects."

Note: This sign is about the rigid formula, not simply the mention of challenges or challenging.

'''Examples'''

{{blockquote|{{fmbox|image=none|text= {{fake section|level=2|Challenges and Future Directions}} As the global economy continues to evolve, international economic law {{highlight|faces new challenges and opportunities.}} [...] The future of international economic law lies in its ability to {{highlight|adapt to these emerging trends|lightgreen}} and continue to facilitate a stable and equitable global economic order. }}|From [[Special:Diff/1189640895|this December 2023 revision]] to [[International economic law]]}}

{{blockquote|text=The future of hydrocarbon economies {{highlight|faces several challenges,}} including[...] This section would speculate on {{highlight|potential developments|lightgreen}} and the changing landscape of global energy.|title=From {{diff||1201557771|label=this January 2024 revision}} to [[Hydrocarbon economy]]}}

{{blockquote|text={{highlight|Despite its industrial and residential prosperity, Korattur faces challenges}} typical of urban areas, including[...] With its {{highlight|strategic location and ongoing initiatives|lightgreen}}, Korattur {{highlight|continues to thrive|lightgreen}} as an integral part of the Ambattur industrial zone, embodying the synergy between industry and residential living.|title=From {{diff||1218690551|label=this April 2024 revision}} to [[Korattur]]}}

{{blockquote|Operating in the current Afghan media environment {{highlight|presents numerous challenges,}} including[...] {{highlight|Despite these challenges,|lightgreen}} Amu TV has managed to {{highlight|continue to provide a vital service|lightgreen}} to the Afghan population​​.|From [[Special:Diff/1241301672|this August 2024 revision]] to [[Amu Television]]}}

{{blockquote|text={{highlight|Despite their promising applications, pyroelectric materials face several challenges}} that must be addressed for broader adoption. One key limitation is[...] {{highlight|Despite these challenges|lightgreen}}, the versatility of pyroelectric materials {{highlight|positions them as critical components|lightgreen}} for sustainable energy solutions and next-generation sensor technologies.|title=From [[Special:Diff/1277706730|this February 2025 revision]] to [[Pyroelectricity]]}}

{{blockquote|text={{highlight|Despite its success, the Panama Canal faces challenges}}, including[...] {{highlight|Future investments in technology, such as automated navigation systems, and potential further expansions could enhance the canal’s efficiency|lightgreen}} and maintain its relevance in global trade.|title=From {{diff||1279428086|label=this March 2025 revision}} to [[Panama Canal]]}}

{{blockquote|For example, while the methodology supports transdisciplinary collaboration in principle, applying it effectively in large, heterogeneous teams {{highlight|can be challenging.}} [...]

SCE continues to evolve {{highlight|in response to these challenges.|lightgreen}}|From [[Special:Diff/1297629115|this June 2025 revision]] to [[Draft:Socio-cognitive engineering]]}}

===Leads treating Wikipedia lists or broad article titles as proper nouns === In AI-generated articles about topics with a title that is not a [[proper name]], such as a [[Wikipedia:Manual of Style/Lists|list]], the first sentence of the lead may introduce or define the article's title as if it were a standalone real-world entity. While the [[Wikipedia:Manual_of_Style/Lead_section#Format_of_the_first_sentence|MOS]] does allow such titles to be included at the beginning of the lead "in a natural way", these AI leads tend not to be so natural.

'''Examples'''

{{blockquote|{{highlight|'''Catchment area (health)''' refers to}} the geographic area from which a health facility, such as a hospital or clinic, draws its patients.|From [[Special:Diff/1248996099|this October 2024 revision]] to now-deleted article Catchment area (health)}}

{{blockquote|{{highlight|EuroGames editions is the chronological list}} of the biennial EuroGames, a European LGBT+ multi-sport event organized by the European Gay and Lesbian Sport Federation (EGLSF).|From [[Special:Diff/1299100685|this July 2025 revision]] to [[EuroGames editions]]}}

{{blockquote|{{highlight|The “'''List of songs about Mexico'''” is a curated compilation}} of musical works that reference Mexico its culture, geography, or identity as a central theme.|From [[Special:Diff/1300476090|this July 2025 revision]] to [[List of songs about Mexico]]}}

==Language and grammar== AI-generated text displays consistent patterns in syntax, word choice, and sentence construction that human writing does not display to nearly the same degree. Conversely, it often struggles to match some syntactic and linguistic patterns characteristic of human writing. Some LLMs deviate more from human writing than others; for example, GPT-4o, the language model used by ChatGPT from May 2024 to August 2025, produces output with more syntactic variation than other contemporaneous language models.

Since these are linguistic patterns, they occur regardless of the subject matter, which often gives AI-generated text an identifiable "voice."

=== High density of "AI vocabulary" words === {{Shortcut|WP:AIVOCAB|WP:AIWORDS}}

{{tmbox|image=none|text=Words to watch: {{strong|''Additionally'' (especially beginning a sentence), ''align with'', ''boasts'' (meaning "has"), ''bolstered'', ''crucial'', ''delve'',{{Cite web|last=Kriss|first=Sam|date=December 3, 2025|title=Why Does A.I. Write Like … That?|work=The New York Times|url=https://www.nytimes.com/2025/12/03/magazine/chatbot-writing-style.html|url-access=subscription|access-date=December 6, 2025}} ''emphasizing'', ''enduring'', ''enhance'', ''fostering'', ''garner'', ''highlight'' (as a verb), ''interplay'', ''intricate/intricacies'', ''key'' (as an adjective),{{citation needed|date=November 2025}} ''landscape'' (as an abstract noun), ''meticulous/meticulously'',{{cite web |last1=Juzek |first1=Tom S. |last2=Ward |first2=Zina B. |title=Word Overuse and Alignment in Large Language Models: The Influence of Learning from Human Feedback |url=https://arxiv.org/pdf/2508.01930 |access-date=27 February 2026}} ''pivotal'', ''robust'', ''showcase'', ''tapestry'' (as an abstract noun),<ref name="Reinhart /> ''testament'', ''underscore'' (as a verb), ''valuable'', ''vibrant'' }} }}

Many studies have demonstrated that LLMs overuse specific words. These words started appearing far more frequently in text produced after 2022, when LLM chatbots became widely accessible.{{cite conference |last1=Juzek |first1=Tom S. |last2=Ward |first2=Zina B. |title=Why Does ChatGPT "Delve" So Much? Exploring the Sources of Lexical Overrepresentation in Large Language Models |conference=Findings of the Association for Computational Linguistics: ACL 2025 |publisher=[[Association for Computational Linguistics]] |date=2025 |arxiv=2412.11385 |url=https://aclanthology.org/2025.coling-main.426.pdf |access-date=October 13, 2025 |via=[[ACL Anthology]] |archive-date=January 21, 2025 |archive-url=https://web.archive.org/web/20250121111136/https://aclanthology.org/2025.coling-main.426.pdf |url-status=live }}{{cite journal |last1=Kobak |first1=Dmitry |last2=González-Márquez |first2=Rita |last3=Horvát |first3=Emőke-Ágnes |last4=Lause |first4=Jan |title=Delving into LLM-assisted writing in biomedical publications through excess vocabulary |journal=[[Science Advances]] |volume=11 |issue=27 |date=2 July 2025 |issn=2375-2548 |pmid=40601754 |pmc=12219543 |doi=10.1126/sciadv.adt3813 |url=https://www.science.org/doi/10.1126/sciadv.adt3813 |access-date=21 November 2025}} They often co-occur in LLM output: where there is one, there are likely others.{{cite conference |last1=Kousha |first1=Kayvan |last2=Thelwall|first2=Mike |title=How much are LLMs changing the language of academic papers after ChatGPT? A multi-database and full text analysis|conference=ISSI 2025 Conference |date=2025 |arxiv=2509.09596 |url=https://arxiv.org/pdf/2509.09596|access-date=4 November 2025|archive-date=14 September 2025 |archive-url=https://web.archive.org/web/20250914165435/https://arxiv.org/pdf/2509.09596 |url-status=live}} While most of these studies have analyzed scientific abstracts or fiction, "AI vocabulary" words are also ubiquitous in LLM-based encyclopedias, such as [[Grokipedia]], and in AI-generated Wikipedia text. One or two of these words appearing in an edit may be coincidental, but an edit (post-2022) introducing lots of them, lots of times, is one of the strongest tells for AI use.

The distribution of "AI vocabulary" is slightly different depending on which chatbot or LLM was used, and has changed over time. For instance, the word ''[[wikt:delve|delve]]'' was famously overused by ChatGPT in 2023 and early 2024, but became less frequent later in 2024, then dropped off sharply in 2025.{{cite news |last1=Merrill |first1=Jeremy B. |last2=Chen |first2=Szu Yu |last3=Kumer |first3=Emma |title=What are the clues that ChatGPT wrote something? We analyzed its style. |url=https://www.washingtonpost.com/technology/interactive/2025/how-detect-chatgpt-em-dash/ |access-date=14 November 2025 |work=The Washington Post |date=13 November 2025}}{{cite web |last1=Geng |first1=Mingmeng |last2=Trotta |first2=Roberto |title=Human-LLM Coevolution: Evidence from Academic Writing |url=https://aclanthology.org/2025.findings-acl.657.pdf |website=aclanthology.org |access-date=17 December 2025}} Below is a breakdown of which words frequently recur together during which LLM "era." While these are not hard cutoffs, they should give you a rough idea of how "earlier" vs "later" LLM output reads.

'''2023 to mid-2024''' (GPT-4): ''Additionally'', ''boasts'', ''bolstered'', ''crucial'', ''delve'', ''emphasizing'', ''enduring'', ''garner'', ''intricate/intricacies'', ''interplay'', ''key'', ''landscape'', ''meticulous/meticulously'', ''pivotal'', ''underscore'', ''tapestry'', ''testament'', ''valuable'', ''vibrant''
'''Mid-2024 to mid-2025''' (GPT-4o): ''align with'', ''bolstered'', ''crucial'', ''emphasizing'', ''enhance'', ''enduring'', ''fostering'', ''highlighting'', ''pivotal'', ''showcasing'', ''underscore'', ''vibrant''
'''Mid-2025 and on''' (GPT-5): ''emphasizing'', ''enhance'', ''highlighting'', ''showcasing'' (plus words associated with [[#Undue_emphasis_on_notability,_attribution,_and_media_coverage|"Undue emphasis on notability, attribution, and media coverage"]])
Please keep context in mind. For example, while the figurative use of "underscore" is ubiquitous in earlier AI text, the word can also refer to a literal underline mark or to [[incidental music]].

'''Examples''' {{blockquote| The inscriptions also offer {{highlight|valuable}} insights into the construction of the mosque. They record the names of the {{highlight|key}} craftsmen involved, including Mason Ahmad b. Muhammad, known as Haddad (the smith or iron-worker), and Hjajji Muhammad, the tile-cutter from [[Tabriz]]. These names {{highlight|highlight}} the collaborative nature of mosque construction and {{highlight|emphasize}} the contributions of skilled artisans. [...] For example, the repeated invocation of the names of Muhammad and the Twelve Imams in Kufic script {{highlight|highlights}} the Shi'ite character of the mosque and links its construction to the broader context of the Ilkhanid state's official adoption of Shi'ism under [[Öljaitü|Oljeitu]]. [...] This inscription, commissioned during the reign of the Aq Qoyunlu ruler Uzun Hasan, also {{highlight|underscores}} the {{highlight|enduring}} practice of pious patronage for mosque upkeep and renovation. |From [[Special:Diff/1263234661|this 2024 revision]] to [[Jameh Mosque of Ashtarjan]], which contains text pasted from [[Special:Diff/1263233100|this revision]] to a user subpage}}

{{blockquote|{{fmbox|image=none|text= Somali cuisine is an {{highlight|intricate}} and diverse fusion of a multitude of culinary influences, drawing from the rich {{highlight|tapestry}} of [[Arab cuisine|Arab]], [[Indian cuisine|Indian]], and [[Italian cuisine|Italian]] flavours. This culinary {{highlight|tapestry}} is a direct result of Somalia's longstanding heritage of {{highlight|vibrant}} trade and bustling commerce. [...]

{{highlight|Additionally,}} a distinctive feature of Somali culinary tradition is the incorporation of [[camel]] [[meat]] and [[milk]]. They are considered a delicacy and serve as cherished and fundamental elements in the rich {{highlight|tapestry}} of Somali cuisine. [...]

An {{highlight|enduring testament}} to the influence of [[Italian Somaliland|Italian colonial rule in Somalia]] is the widespread adoption of [[pasta]] and [[Lasagna|lasagne]] in the local culinary {{highlight|landscape}}, espicially in the south, {{highlight|showcasing}} how these dishes have integrated into the traditional diet alongside rice. [...]

{{highlight|Additionally,}} Somali merchants played a {{highlight|pivotal}} role in the global coffee trade, being one of the first to export coffee beans. }}|From [[Special:Diff/1292567688|this 2025 revision]] to [[Somali people]]}}

{{anchor|Concrete}} {{shortcut|WP:CONCRETE}} When writing comments instead of article content, AI chatbots tend to use the word "concrete" as an adjective. This is often the case in comments that emphasize the apparent [[WP:NOPROOFOFAI|lack of "concrete evidence"]] of AI use or are requests for accusers to [[WP:WHERESTHEAI|provide "concrete examples"]] of text that appears AI-generated.

'''Examples''' {{blockquote|Review: The use of "significantly more" is subjective and requires specific figures to validate this claim. Without concrete financial data from reliable sources, this statement could be misleading or exaggerated. The source provided is a blog. |From [[Special:Diff/1241601880|this August 2024 revision]] to [[Talk:Eric Dick (lawyer)]]}}

{{blockquote|In the absence of concrete evidence, I propose removing the AI-generated tag immediately to maintain the article's integrity. |From [[Special:Diff/1316902424|this October 2025 revision]] to [[Talk:Slavery in Portugal]]}}

{{blockquote|Without concrete examples, your concern cannot be evaluated in line with WP:V, WP:RS and WP:BURDEN. |From [[Special:Diff/1348114931|this April 2026 revision]] to [[Talk:House of Dust (architecture)]]}}

===Avoidance of basic copulatives ("is"/"are" phrases)=== {{tmbox|image=none|text=Words to watch: {{strong|''serves as/stands as/marks/represents [a]'', ''boasts/features/maintains/offers [a]'', ''refers to''}}}}

LLM-generated text often replaces simple constructions that use [[Copula (linguistics)|copula]]s such as ''is'' or ''are'' with constructions such as ''serves as a'' or ''mark the''. This pattern has been observed in GPT and Gemini models. One study documented an over 10% decrease in the usage of the words ''is'' and ''are'' in academic writing in 2023, with no major changes in their frequency before that.{{cite web |last1=Geng |first1=Mingmeng |last2=Trotta |first2=Roberto |title=Is ChatGPT Transforming Academics' Writing Style? |url=https://arxiv.org/abs/2404.08627 |access-date=8 January 2026}} Similarly, LLMs prefer to use [[WP:BUZZ|marketing]]-related verbs like ''features'', ''offers'', and the like to their neutral synonym ''has''. (Note: This does not apply to ''has'' used in the [[past participle]] form.) Sometimes these constructions are more elaborate, e.g., ''ventured into politics as a candidate'' versus ''was a candidate''.

A similar decline in "is"/"are" constructions has been observed on Wikipedia, especially when controlling for lead paragraphs (which usually follow a formulaic structure of "[article subject] is...]" and thus skew the data).{{cite web |last1=Huang |first1=Siming |last2=Xu |first2=Yuliang |last3=Geng |first3=Mingmeng |last4=Wan |first4=Yao |last5=Chen |first5=Dongping |title=Wikipedia in the Era of LLMs: Evolution and Risks |url=https://openreview.net/pdf?id=ahVmnYkVLt |access-date=13 May 2026}} It is particularly visible in AI copyedits, which will often "improve" text in this way. The study above also demonstrated that when GPT-3.5 was prompted to "Revise the following sentence" in 10,000 abstracts, the words ''is'' and ''are'' appeared less often in the revised versions.

In lead sentences, LLMs will sometimes avoid ''is'' by writing ''refers to'' [[Wikipedia:Signs of AI writing#Leads treating Wikipedia lists or broad article titles as proper nouns|as though the article were about the word or term]] instead of the subject directly.

'''Examples''' {{textdiff|Gallery 825 on [[La Cienega Boulevard]], which was purchased in 1958, is LAAA's exhibition arm for [[contemporary art]]. There are four individual gallery spaces[...]|Gallery 825 on [[La Cienega Boulevard]] serves as LAAA's exhibition space for contemporary art. The gallery features four separate spaces[...]}}

{{bi|1=—From [[Special:Diff/1168694674|this August 2023 revision]] to [[Los Angeles Art Association]]}}

{{textdiff|It is Malaysia's first [[Malay language|Malay]] daily afternoon [[Tabloid (newspaper format)|Tabloid]] [...] The ''Harian Metro'' was established in March 1991 and is the first and oldest Malay-language tabloid [...]|It was established in March 1991 as Malaysia's first Malay-language afternoon [[Tabloid journalism|tabloid]] [...] Harian Metro holds the distinction of being the first and oldest Malay-language tabloid [...]}}

{{bi|1=—From [[Special:Diff/1259995938|this November 2024 revision]] to [[Harian Metro]]}}

===Negative parallelisms=== {{Shortcut|WP:AIPARALLEL}} When LLMs describe a subject, their output may seem as though it is clearing up a common misconception, or as though the audience may be reaching an incomplete or incorrect conclusion about that subject. This kind of contrast can come across as trying to retroactively challenge such thinking by pointing out another characteristic that the subject may possess alongside (or in the place of) one or more previously-mentioned characteristics. While it is common among human writers (especially in "common misconceptions" or "myths busted" [[listicle]]s), it is stereotypically an "AI sign."

====Not just X, but also Y==== It is common for LLMs to use parallel constructions involving "not", "but", or "however" such as "{{xt|Not only ... but ...}}" or "{{xt|It is not just ..., it's ...}}".{{cite web |last1=Robbins |first1=Hollis |title=How to Tell if Something is AI Written |url=https://hollisrobbinsanecdotal.substack.com/p/how-to-tell-if-something-is-ai-written |website=Anecdotal Value |publisher=Substack |access-date=7 December 2025}}{{cite conference |last1=Russell |first1=Jenna |last2=Karpinska |first2=Marzena |last3=Iyyer |first3=Mohit |year=2025 |url=https://aclanthology.org/2025.acl-long.267/ |location=Vienna, Austria |title=People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text |conference=Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers) |publisher=Association for Computational Linguistics |pages=5342–5373 |arxiv=2501.15654 |doi=10.18653/v1/2025.acl-long.267 |doi-access=free |access-date=2025-09-05 |via=[[ACL Anthology]] |archive-date=2025-08-29 |archive-url=https://web.archive.org/web/20250829184825/https://aclanthology.org/2025.acl-long.267/ |url-status=live }}

'''Examples''' {{blockquote| In your most recent exchange, you referred to another editor’s comment as "bizarre" and "totally incorrect," following up with an assertion that their viewpoint was "bogus." This choice of language is not only dismissive but also unnecessarily harsh and confrontational. It shuts down the possibility of constructive dialogue and disrespects the effort that others put into contributing to this platform.

This kind of dismissive and confrontational attitude is not new. [...] This remark doesn’t just undermine the editor’s argument; it questions their very right to participate based on how long they’ve been active, which is contrary to the inclusive nature that Wikipedia aims to foster. New contributors should be encouraged, not belittled, and it’s disheartening to see you take such a dismissive stance.

Your sarcastic remark about adding "Eric Dick is a secret Democrat. [citation needed]" to the article further exemplifies this problematic behavior. Rather than engaging in a meaningful discussion, you chose to mock another editor’s argument, which only serves to create a hostile environment. This approach doesn’t help resolve disputes or improve content; it only escalates tensions and discourages productive collaboration.

Moreover, in another instance, you accused an editor of "bludgeoning discussion with screeds of AI generated waffle" and dismissed their contributions as "acres of fanciful extrapolation on Wikipedia policies." These comments are not just dismissive—they’re outright disrespectful. Accusations like these don’t belong in a professional and collaborative setting. They undermine the very spirit of Wikipedia, which is built on the idea that people with different perspectives can come together to create something valuable.

It’s important to recognize that everyone who contributes to Wikipedia—whether they’re new or experienced, whether they agree with you or not—deserves to be treated with respect. Collaboration, not confrontation, should be the goal. By continuing to engage with others in such a dismissive and harsh manner, you not only discourage participation but also damage the collaborative spirit that is essential to Wikipedia’s success. |From [[Special:Diff/1241947673|this August 2024 revision]] to [[Talk:Eric Dick (lawyer)]]}}

{{blockquote|text='''Self-Portrait''' by Yayoi Kusama, executed in 2010 and currently preserved in the famous Uffizi Gallery in Florence, constitutes {{highlight|not only a work of self-representation, but}} a visual document of her obsessions, visual strategies and psychobiographical narratives.|title=From [[Special:Diff/1288184349|this April 2025 revision]] to [[Self-portrait (Yayoi Kusama)]]}}

{{blockquote| I appreciate the feedback so far, but I want to clarify something that’s being overlooked. The issue here isn’t just sourcing—it’s framing. There’s a visible, growing movement around Northern English identity, documented across academic literature, social media, and grassroots activism. The fact that it doesn’t always use the exact phrase “Northern English nationalism” doesn’t mean it doesn’t exist. Movements evolve before they’re neatly labelled.

TikTok campaigns, dialect revival, and regional symbolism (like St Oswald’s stripes) are part of a broader cultural shift. Dismissing these as “not notable” or “original research” while allowing pages on Cornish nationalism, Wessex regionalism, and Yorkshire separatism suggests an inconsistency in how regional identity is treated. That’s not just a sourcing issue—it’s a systemic bias. |From [[Special:Diff/1308162770|this August 2025 revision]] to [[Wikipedia:Articles for deletion/Northern English nationalism]]; this example also contains [[WP:AIDASH|em dashes]] and [[WP:AICURLY|curly quotation marks]]}}

Here is an example of a negative parallelism across multiple sentences: {{blockquote|text=He hailed from the esteemed Duse family, renowned for their theatrical legacy. Eugenio's life, however, took a path that intertwined both personal ambition and familial complexities.|title=From [[Special:Diff/1284729136|this April 2025 revision]] to [[Eugenio Duse]]}}

====Not X, but Y==== Another common LLM pattern is parallelisms that explicitly state that a particular item doesn't possess the first characteristic at all. Such constructions are often expressed as "{{xt|It's not ..., it's ...}}" or "{{xt|no ..., no ..., just ...}}".

'''Examples''' {{blockquote|{{fmbox|image=none|text= The viewer is presented with a self-image that {{highlight|is not grounded in visual mastery, but in what Amelia Jones terms “the performative enactment of subjectivity”}}.

[...]

This dispersal {{highlight|is not dissolution. Rather, it constitutes what Deleuze might describe as “becoming”}}—an identity in flux, constituted through iterative difference. Through this lens, Kusama’s self-portrait {{highlight|is not a mirror but a portal}}: {{highlight|not a representation of self, but a mechanism}} for its constant reinvention. }}|From [[Special:Diff/1288356293|this May 2025 revision]] to [[Self-portrait (Yayoi Kusama)]]}}

{{blockquote|{{fmbox|image=none|text= You say these sources “cover multiple events”? False. They echo the same viral incident and do it through a limited lens. {{highlight|This isn’t WP:NBIO — it’s WP:1EVENT in disguise}}, trying to wear a press badge like armor.

[...]

Now let’s talk BLP1E: This person is only in the news because of one isolated controversy. {{highlight|Not a career, not a body of work, not sustained relevance — just an algorithmic moment}}. And if we’re really upholding Wikipedia’s values, we don’t preserve pages built on the backs of virality alone, especially when it risks long-term harm to a living subject without lasting notability.

“Might as well get back on topic.”

Then let’s stay on topic, and the topic {{highlight|is not who feels warm fuzzies from visibility, it’s whether this article meets the threshold for inclusion}}. It doesn’t.

And finally — if you don’t want “a wall of text,” maybe don’t build a wall of shallow logic and expect people not to knock it down. {{highlight|This ain’t bludgeoning — it’s surgical teardown}} of a weak argument hiding behind fake neutrality. }}|title=From [[Special:Diff/1296115128|this June 2025 revision]] to [[Wikipedia:Articles for deletion/Lilly Contino]]}}

===Rule of three=== {{shortcut|WP:RO3}} LLMs overuse the '[[Rule of three (writing)|rule of three]]'. This can take different forms, from "adjective, adjective, adjective" to "short phrase, short phrase, and short phrase". LLMs often use this structure to make [[#Superficial analyses|superficial analyses]] appear more comprehensive.

'''Examples''' {{blockquote|

Standard Rotary Saws: Typically used for drywall and light materials.
Heavy-Duty Rotary Saws: Designed for tougher materials such as tiles, metals, and plastics.
Corded and Cordless Versions: Corded rotary saws offer continuous power, while cordless versions provide portability and convenience [...]
Construction and Renovation: For cutting drywall, plywood, and other construction materials.
Electrical and Plumbing: To create openings for electrical outlets, switches, and plumbing fixtures.
Hobby and Craft: Used in model making, woodworking, and other craft projects.
Automotive: Employed in auto body repair and modification tasks. |From [[Special:Diff/1237779206|this July 2024 revision]] to [[Rotary saw]] (note that these are [[WP:AILIST|canned-format lists]] that used [[WP:MARKDOWN|Markdown]])}}
===Lexical diversity/elegant variation=== {{For|a non-AI-specific style essay about this|Wikipedia:The problem with elegant variation}} {{Further|Lexical diversity}} {{shortcut|WP:AIELEVAR}} Generative AI has a repetition-penalty code, meant to discourage it from reusing words too often.{{cite web |last=Belcher|first=Wendy|title=10 Ways AI Is Ruining Your Students' Writing.|website=Chronicle of Higher Education|date=September 16, 2025|url=https://www.chronicle.com/article/10-ways-ai-is-ruining-your-students-writing|access-date=October 1, 2025|archive-date=October 1, 2025|archive-url=https://web.archive.org/web/20251001071208/https://www.chronicle.com/article/10-ways-ai-is-ruining-your-students-writing/|url-status=live}} This pattern has also been observed on Wikipedia on a broad level: both when comparing Wikipedia text from before 2023 to Wikipedia text from after 2023, and comparing the older Wikipedia text to "Wikipedia-style articles" generated by GPT-4o-mini and Gemini-1.5-Flash.

Note: If a user adds multiple pieces of AI-generated content in separate edits, this tell may not apply, as each piece of text may have been generated in isolation.

'''Examples''' {{sidebox|text= {{legend|pink|Soviet artistic constraints}} {{legend|lightblue|Non-conformist artists}} {{legend|plum|Their creativity}} }} {{blockquote| Vierny, after a visit in Moscow in the early 1970’s, committed to supporting artists resisting {{highlight|the constraints of socialist realism|pink}} and discovered Yankilevskly, among others such as Ilya Kabakov and Erik Bulatov. In {{highlight|the challenging climate of Soviet artistic constraints|pink}}, Yankilevsky, alongside other {{highlight|non-conformist artists|lightblue}}, faced obstacles in expressing {{highlight|their creativity|plum}} freely. Dina Vierny, recognizing {{highlight|the immense talent|plum}} and the struggle {{highlight|these artists|lightblue}} endured, played a pivotal role in aiding {{highlight|their artistic aspirations|plum}}. [...]

In this new chapter of his life, Yankilevsky found himself amidst a community of {{highlight|like-minded artists|lightblue}} who, despite diverse styles, shared a common goal—to break free from {{highlight|the confines of state-imposed artistic norms|pink}}, particularly socialist realism. [...]

The move to Paris facilitated an environment where Yankilevsky could further explore and exhibit {{highlight|his distinctive artistic vision|plum}} without {{highlight|the constraints imposed by the Soviet regime|pink}}. Dina Vierny's unwavering support and commitment to the {{highlight|Russian avant-garde artists|lightblue}} played a crucial role in fostering a space where {{highlight|their creativity|plum}} could flourish, contributing to the rich tapestry of artistic expression in the vibrant cultural landscape of Paris. Vierny's commitment culminated in the groundbreaking exhibition "Russian Avant-Garde - Moscow 1973" at her Saint-Germain-des-Prés gallery, showcasing the {{highlight|diverse yet united front of non-conformist artists|lightblue}} challenging {{highlight|the artistic norms|pink}} of their time. |From [[Special:Diff/1205035512|this February 2024 revision]] to [[Vladimir Yankilevsky]]}}

It must be noticed however that editors who are not native English speakers might prefer to avoid repeated words as well. For example Italian schools often teach to avoid repeating words.{{cite web |last1=Birattari |first1=Massimo |title=Come evitare le ripetizioni “moleste” quando scriviamo? |url=https://www.illibraio.it/news/grammatica/come-evitare-ripetizioni-quando-scriviamo-540892/ |website=Il Libraio |access-date=29 May 2026}}{{cite web |last1=Cortelazzo |first1=Michele A. |title=Non sempre è necessario usare parole diverse |url=http://www.maldura.unipd.it/buro/gel/gel13.html |website=SEMPLIFICAZIONE DEL LINGUAGGIO AMMINISTRATIVO «MANUALE DI STILE» |publisher=Università di Padova |access-date=29 May 2026}}

==Style== ===Title case=== {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style/Capital letters#Headings, headers, and captions}} {{Shortcut|WP:AITITLECASE}}

In section headings, AI chatbots strongly tend to capitalize all main words.

'''Examples''' {{blockquote|{{fmbox|image=none|text= {{fake section|level=2|Impact of Technology and Digitalization}} The advent of digital technology and the internet has revolutionized international economic law. [...] {{fake section|level=2|Sustainable Development and Environmental Law}} The integration of sustainable development goals into international economic law is increasingly important. [...] {{fake section|level=2|Human Rights and Economic Law}} The relationship between human rights and international economic law is a growing area of focus. [...] }}|From [[Special:Diff/1189640895|this December 2023 revision]] to [[International economic law]]}}

===Overuse of boldface=== {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style/Text formatting#Boldface}} {{shortcut|WP:AIBOLD}} AI chatbots may display various phrases in [[boldface]] for emphasis in an excessive, mechanical manner. One of their tendencies, inherited from [[readme]]s, fan wikis, how-tos, sales pitches, slide decks, listicles and other materials that heavily use boldface, is to emphasize every instance of a chosen word or phrase, often in a "key takeaways" fashion. Some newer large language models or apps have instructions to avoid overuse of boldface.

'''Examples''' {{blockquote|A '''leveraged buyout (LBO)''' is characterized by the extensive use of '''debt financing''' to acquire a company. This financing structure enables '''private equity firms''' and '''financial sponsors''' to control businesses while investing a relatively small portion of their own equity. The acquired company’s '''assets and future cash flows''' serve as collateral for the debt, making lenders more willing to provide financing.|From [[Special:Diff/1274574473|this revision]] to [[Leveraged buyout]]}}

{{blockquote|'''50 Scientists and Thinkers in AI Safety with significant''' influence on the field of alignment, containment, and risk mitigation. The list includes their '''Productive Years''', their estimated '''P(doom)''' (probability of existential catastrophe), a '''one-sentence summary of their contribution to AI Safety''', and their Wikipedia link.|From [[Special:Diff/1324781030|this revision]] to [[P(doom)]]}}

{{blockquote| {{fmbox|image=none|text= I am initiating this '''[[Request for Comments|Request for Comment (RfC)]]''' to seek input from '''experienced editors and administrators''' regarding '''persistent policy compliance issues''' in this article, which covers a '''high-profile proposed acquisition involving [[Warner Bros. Discovery]]'''.

Despite repeated editing and cleanup efforts, the article continues to exhibit '''systemic problems''' that significantly undermine its encyclopedic quality and neutrality.

{{fake section|level=3|Key Issues Requiring Community Review}}

'''Undue Weight and Apparent Bias''' The article places '''disproportionate emphasis on Netflix''', exceeding its relevance to the subject and creating an imbalanced narrative. This raises ongoing concerns under '''[[WP:NPOV]]''' and '''[[WP:UNDUE]]'''.
'''News Aggregation and Excessive Detail''' Large portions of the article read as '''compiled news reporting''', with dense, minimally summarized content that appears to be copied or lightly paraphrased from sources. This conflicts with '''WP:NOTNEWS''' and '''[[WP:SUMMARYSTYLE]]'''.
'''Lack of High-Level Overview''' The article fails to present a clear, concise overview of the proposed acquisition. Instead, readers are confronted with fragmented detail without sufficient contextual framing.
'''Misplacement of Content''' Speculative analysis, reporting detail, and tangential information are frequently placed in '''inappropriate sections''', weakening article structure and reader comprehension.
{{fake section|level=3|Prior Cleanup Efforts}} I have personally conducted '''substantial editing''', including:

[...]

However, these efforts have not resolved the underlying issues, suggesting that '''individual edits alone are insufficient''' and that '''broader consensus and oversight are required'''.

{{fake section|level=3|Questions for Comment}} I respectfully request community input on the following:

Does the article currently give '''undue weight''' to Netflix or other peripheral entities?
Is the article failing to meet '''[[WP:NOTNEWS]]''' and '''[[WP:SUMMARYSTYLE]]''' standards due to excessive, real-time reporting?
Does the article require '''structural reorganization''' to provide a proper overview and improve section relevance?
Would '''administrative measures''' (e.g., guided restructuring, closer monitoring, or temporary page protection) be appropriate given the article’s visibility and edit patterns?
{{fake section|level=3|Closing}} Given the prominence of this topic and the likelihood of continued drive-by or promotional editing, this article requires '''careful scrutiny by experienced contributors'''. The goal of this RfC is to establish clear consensus on how the article should be structured, weighted, and maintained in line with Wikipedia’s core content policies. }} |From [[Special:Diff/1336034644|this revision]] to [[Talk:Proposed acquisition of Warner Bros. Discovery]]; this example also includes [[WP:AILIST|lists]] and uses [[WP:AITITLECASE|title case]] for subheadings}}

===Inline-header vertical lists=== {{shortcut|WP:AILIST}} {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style/Lists#Use prose where understood easily}} AI chatbots output often includes vertical lists formatted in a specific way: an ordered or unordered list where the list marker (number, bullet, dash, etc.) is followed by an inline boldfaced header, separated with a colon from the remaining descriptive text.

Instead of [[H:LIST|proper wikitext]], a bullet point in an unordered list may appear as a bullet character (•), hyphen (-), en dash (–), [[Wikipedia:Signs_of_AI_writing#Use_of_Markdown|hash]] (#), [[Wikipedia:Signs_of_AI_writing#Emoji_as_formatting|emoji]], or similar character. Ordered lists (i.e. numbered lists) may use explicit numbers (such as {{code|1.}}) instead of standard wikitext. When [[WP:SCOPY|copied as bare text appearing on the screen]], some of the formatting information is lost, and line breaks may be lost as well.

'''Examples''' {{blockquote| Conflict of Interest (COI)/Autobiography: While I understand the concern regarding my username [...]
Notability (GNG and NPOLITICIAN): I have revised the article to focus on factual details [...]
Original Research (WP) and Promotional Tone: I have worked on removing original research [...]
Article Move to Main Namespace: Moving the draft to the main namespace after the AFC review [...] |From [[Special:Diff/1251078728|this October 2024 revision]] to [[Wikipedia:Articles for deletion/Sarwan Kumar Bheel]]}}

{{blockquote|

Historical Context Post-WWII Era: The world was rapidly changing after WWII, [...]
Nuclear Arms Race: Following the U.S. atomic bombings, the Soviet Union detonated its first bomb in 1949, [...]
Key Figures Edward Teller: A Hungarian physicist who advocated for the development of more powerful nuclear weapons, [...]
Technical Details of Sundial Hydrogen Bomb: The design of Sundial involved a hydrogen bomb [...]
Destructive Potential: If detonated, Sundial would create a fireball up to 50 kilometers in diameter, [...]
Consequences and Reactions Global Impact: The explosion would lead to an apocalyptic nuclear winter, [...]
Political Reactions: The U.S. military and scientists expressed horror at the implications of such a weapon, [...]
Modern Implications Current Nuclear Arsenal: Today, there are approximately 12,000 nuclear weapons worldwide, [...]
Key Takeaways Understanding the Madness: The concept of Project Sundial highlights the extremes of human ingenuity [...]
Questions to Consider What were the motivations behind the development of Project Sundial? [...] |From [[Special:PermanentLink/1255717748|this November 2024 revision]] to [[Sundial (weapon)]]}}
{{blockquote|{{fmbox|image=none|text= AVO consists of three key layers:

'''SEO (Search Engine Optimization):''' Traditional methods for improving visibility in search engine results through content, technical, and on-page optimization.
'''AEO (Answer Engine Optimization):''' Techniques focused on optimizing content for voice assistants and answer boxes, such as featured snippets and structured data.
'''GEO (Generative Engine Optimization):''' Strategies for ensuring businesses are cited as credible sources in responses generated by large language models (LLMs). }}|From [[Special:Diff/1316572059|this October 2025 revision]] to [[Draft:AI Visibility Optimization (AVO)]]. Also note the [[WP:AISIGNS#Rule of three|rule of three]].}}
{{blockquote|{{fmbox|image=none|text= Key highlights:

'''Route Details''': Starts at Medak, passes through Yellareddy, Banswada, Nasrullabad, Varni, Rudrur, Bodhan, Shatapur, Navipet, Fakirabad, Basar, Mudhol, and ends at Bhainsa (via Yencha). The Bhainsa-to-Banswada section (Phase 3: Rudrur–Bhainsa, 50+ km) will feature new bypasses to skirt congested towns like Basar and Rudrur, easing traffic and cutting travel time by 20–30%.
'''Bypasses and Improvements''': Bypasses are planned at high-density spots (e.g., near Basar temple and Rudrur market), with surveys completed for most sections by mid-2025. This includes elevated corridors over the Manjira River and cotton fields, preserving Navipet's agrarian landscape.
'''Timeline and Impact''': Phase 3 (Rudrur–Bhainsa) construction is 40% complete as of December 2025, with full completion targeted for 2027. Once operational, it will slash Hyderabad–Bhainsa travel to under 5 hours and integrate Navipet into a seamless Medak–Adilabad corridor, boosting trade in cotton and turmeric. Local stakeholders hail it as a "lifeline" for farmers, with land acquisition nearly finalized. }}|From [[Special:Diff/1327088410|this December 2025 revision]] to [[Navipet]]}}
{{blockquote|{{fmbox|image=none|text= Mass Content Removal: The user removed over 20,000 characters of reliably sourced content in a single edit, reducing the number of citations from 34 to 8, without any prior engagement on the Talk page.Disruptive Tagging: Despite the article being supported by 34 high-quality international secondary sources (Wall Street Journal, Bloomberg, Financial Times, etc.), the user implemented excessive "citation needed" tags as a form of visual vandalism to discredit the content.Refusal to engage (WP:BRD): The user was notified of WP:V and WP:DE policies on their talk page but has failed to justify these massive deletions, suggesting a coordinated attempt at de-legitimizing the subject.Context: Given the high-profile nature of the subject in global finance and mining (notably the AstraZeneca/EsoBiotec $1B M&A), the page is currently vulnerable to reputation-based sabotage. }}|From [[Special:Diff/1345180164|this March 2026 revision]] to [[Wikipedia:Requests for page protection/Increase]]}}

===Overuse of em dashes=== {{For|non-AI-specific guidance about the use of dashes|Wikipedia:Manual of Style#Dashes}} {{Shortcut|WP:AIDASH}} While human editors and writers often use [[em dash]]es (—), LLM output uses them more often than nonprofessional human-written text of the same genre, and uses them in places where humans are more likely to use commas, parentheses, colons, or (misused) hyphens (-) and [[en dash]]es (–). LLMs especially tend to use em dashes in a formulaic, pat way, often mimicking "punched up" sales-like writing by over-emphasizing clauses or parallelisms.

This sign is most useful when taken in combination with other indicators, not by itself. It is much more common on discussion pages than in article text. Also, because LLMs' use of em-dashes has become somewhat notorious, some AI companies have attempted to make their newer chatbots suppress their use, most notably OpenAI's [[GPT-5.1]].{{cite news |last1=Edwards |first1=Benj |title=Forget AGI—Sam Altman celebrates ChatGPT finally following em dash formatting rules |url=https://arstechnica.com/ai/2025/11/forget-agi-sam-altman-celebrates-chatgpt-finally-following-em-dash-formatting-rules/ |access-date=24 February 2026 |work=Ars Technica |date=14 November 2025}}

'''Examples''' {{"|{{fmbox|image=none|text= I referred to Wikipedia's policies in a discussion with another user, using AI to help me organize my thoughts and better explain the policies I was referencing — something that was reported by the user. [...] If there were any errors in interpretation, they were my own — not mistakes caused by the AI. [...]
[...] Ultimately, one of the admins blocked me — not because of the AI usage itself, which had already been addressed — but because I didn’t respond to their continued questioning. }}|From [[Special:Diff/1284418886|this April 2025 revision]] to a user talk page}}

{{"|{{fmbox|image=none|text= In practice, many Dutch organizations and businesses use it for '''their own convenience''', even placing it in addresses — e.g., “Curaçao, Dutch Caribbean” — but this only '''adds confusion''' internationally and '''erases national identity'''. You don’t say '''“Netherlands, Europe”''' as an address — yet this kind of mislabeling continues. }}|title=From {{diff||1286082047|label=this April 2025 revision}} to [[Talk:Dutch Caribbean]]; the message also [[WP:AIBOLD|overuses boldface]]}}

{{"|{{fmbox|image=none|text= you're right about one thing — we do seem to have different interpretations of what policy-based discussion entails. [...]

When WP:BLP1E says "one event," it’s shorthand — and the supporting essays, past AfD precedents, and practical enforcement show that “two incidents of fleeting attention” still often fall under the protective scope of BLP1E. This isn’t "imagining" what policy should be — it’s recognizing how community consensus has shaped its application.

Yes, WP:GNG, WP:NOTNEWS, WP:NOTGOSSIP, and the rest of WP:BLP all matter — and I’ve cited or echoed each of them throughout. [...] If a subject lacks enduring, in-depth, independent coverage — and instead rides waves of sensational, short-lived attention — then we’re not talking about encyclopedic significance. [...]

[...] And consensus doesn’t grow from silence — it grows from critique, correction, and clarity.

If we disagree on that, then yes — we’re speaking different languages. }}|From [[Special:Diff/1296093591|this June 2025 revision]] to [[Wikipedia:Articles for deletion/Lilly Contino]]}}

=== Unusual use of tables === {{shortcut|WP:AITABLE}} In rare cases, some AIs may create unnecessary small tables that could be better represented as prose or an [[WP:INFOBOX|infobox]].

'''Examples'''

{{Fake heading|Market and Statistics}} The Indian biobanking market was valued at approximately USD 2,101 million in 2024. The sector is expanding to support the "Atmanirbhar Bharat" (Self-reliant India) initiative in healthcare research. {| class="wikitable" |+Key Statistics of Indian Biobanking (2024-2025) !Metric !Figure |- |Market Valuation (2024) |~USD 2.1 billion |- |Major Accredited Facilities |NLDB, CBR Biobank, THSTI, Karkinos |- |GenomeIndia Diversity |99 ethnic groups (32 tribal, 53 non-tribal) |}
{{bi|1=—From [[Special:Diff/1323402246|this November 2025 revision]] to [[Draft:Biobanks in India]]}}
{{fake heading|level=2|Management}} The mall employs approximately 3,167 staff members across all operations. Key management personnel of Pacific Development Corporation Private Limited include: {| class="wikitable" ! Name !! Designation |- | S. K. Bansal || Chairman |- | Abhishek Bansal || Managing Director |- | Saket Bansal || Managing Director |- | Mehak Khanna || VP Marketing |}
{{bi|1=—From [[Special:Diff/1352783863|this May 2026 revision]] to [[Draft:Pacific Mall, Tagore Garden]]}}
===Curly quotation marks and apostrophes=== {{For|non-AI-specific guidance about this|Wikipedia:Manual of Style#Quotation characters|Wikipedia:Manual of Style#Apostrophes}} {{Shortcut|WP:AICURLY}}

ChatGPT and [[DeepSeek]] typically use curly quotation marks (“...” or ‘...’) instead of straight quotation marks ("..." or '...'). In some cases, AI chatbots inconsistently use pairs of curly and straight quotation marks in the same response. They also tend to use the curly apostrophe (’), the same character as the curly [[right single quotation mark]], instead of the straight apostrophe ('), such as in [[Contraction (grammar)|contractions]] and [[English possessive|possessive forms]]. They may also do this inconsistently.

Curly quotes alone do not prove LLM use. Directional quotation marks (curly or typographer) are often used in published works written and edited using the [[Chicago Manual of Style]].{{cite web|url=https://www.chicagomanualofstyle.org/qanda/data/faq/topics/SpecialCharacters/faq0002.html|title=CMOS 18th edition 6.123|website=Chicago Manual of Style}} [[Microsoft Word]] has a "[[smart quotes]]" feature that converts straight quotes to curly quotes. So does the default system-wide configuration on [[macOS]] and [[iOS]] devices, except on some applications (or if turned off, as may be necessary for [[computer programming|programming]]). Grammar correcting tools such as [[LanguageTool]] may also have such a feature. Curly quotation marks and apostrophes are common in professionally typeset works such as major newspapers. Citation tools like [https://citer.toolforge.org/ Citer] may repeat those that appear in the title of a web page: for example,

McClelland, Mac (2017-09-27). [https://www.nytimes.com/2017/09/27/magazine/when-not-guilty-is-a-life-sentence.html "When ‘Not Guilty’ Is a Life Sentence"]. {{em|The New York Times}}. Retrieved 2025-08-03.
Note that Wikipedia allows users to [[WP:CUSTOM|customize]] the fonts used to display text. Some fonts display matched curly apostrophes as straight, in which case the distinction is invisible to the user. Additionally, [[Gemini (language model)|Gemini]] and [[Claude (language model)|Claude]] models typically do not use curly quotes.
===Skipping heading levels=== AI chatbots tend to skip level 2 headings (==) and start sections from the third level (===). [[Wikipedia:Manual_of_Style/Accessibility#Headings|Because doing so is against Wikipedia's accessibility and style conventions]], it is therefore very unlikely for a manually-formatted page to have this quirk.<!--

'''Examples''' -->

===Thematic breaks before headings=== AI chatbots sometimes include a thematic break (----) before each heading in a text (this is common in Markdown output).

'''Examples'''

=== Distinction from French “''[[List of English words of French origin|chiffon]]''” === Some claims have suggested that ''Ichafu'' derives from the French word chiffon (“rag” or "light cloth”). However, early lexicographic records do not support this interpretation and later sources differ in their explanations.
[...]
== History == Headwrapping practices among Igbo women are documented in historical and ethnographic sources and are generally understood to predate the colonial period.

[...]
== Form and construction == {{block indent|1=— From [[Special:Diff/1344638960|this revision]] to [[Draft:Ichafu]] and [https://web.archive.org/web/20260323205345/https://en.wikipedia.org/wiki/Ichafu_(headdress) this archived revision] to [[Ichafu (headdress)]]}}

==Communication intended for the user== ===Collaborative communication=== {{Shortcut|WP:CERTAINLY|WP:COLLABCOMM}} {{tmbox|image=none|text=Words to watch: {{strong|''I hope this helps'', ''Of course!'', ''Certainly!'', ''You're absolutely right!'', ''Would you like...'', ''is there anything else'', ''let me know'', ''more detailed breakdown'', ''here is a'' ...}} }} Editors sometimes paste text from an AI chatbot that was meant as correspondence, prewriting or advice, rather than article content. This may appear in article text or within comments (<-- -->). Chatbots prompted to produce a Wikipedia article or comment may also explicitly state that the text is meant for Wikipedia, and may mention various [[WP:PG|policies and guidelines]] in the output—often explicitly specifying that they're {{em|Wikipedia}}'s conventions. Often the advice given by an AI chatbot is incorrect, misleading, or in contravention with policies or guidelines.

'''Examples''' {{blockquote|text=In this section, we will discuss the background information related to the topic of the report. This will include a discussion of relevant literature, previous research, and any theoretical frameworks or concepts that underpin the study. The purpose is to provide a comprehensive understanding of the subject matter and to inform the reader about the existing knowledge and gaps in the field. |title=From {{diff||1172646802|label=this August 2023 revision}} to [[Metaphysics]] }}

{{blockquote|If you plan to add this information to the "Animal Cruelty Controversy" section of Foshan's Wikipedia page, ensure that the content is presented in a neutral tone, supported by reliable sources, and adheres to Wikipedia's guidelines on verifiability and neutrality.|From [[Special:Diff/1280200320|this March 2025 revision]] to [[Foshan]]}}

{{blockquote|Here's a template for your wiki user page. You can copy and paste this onto your user page and customize it further.|From [[Special:Diff/1290281175|this May 2025 revision]] to a user page}}

{{blockquote|Including photos of the forge (as above) and its tools would enrich the article’s section on culture or economy, [...] Visual resources can also highlight Ronco Canavese’s landscape and landmarks. For instance, a map [...] could be added to orient readers geographically. The village’s scenery [...] could be illustrated with an image. Several such photographs are available (e.g., on Wikimedia Commons) that show Ronco’s panoramic view, [...] Historical images, if any exist [...] would also add depth to the article. Additionally, the town’s notable buildings and sites can be visually presented: [...] Including an image of the Santuario di San Besso [...] could further engage readers. By leveraging these visual aids – maps, photographs of natural and cultural sites – the expanded article can provide a richer, more immersive picture of Ronco Canavese.|From [[Special:Diff/1291175393|this May 2025 revision]] to [[Ronco Canavese]]}}

{{blockquote|text= Final important tip: The ~~~~ at the very end is Wikipedia markup that automatically |title=From {{diff||1297191187|label=this June 2025 revision}} to [[Talk:Test automation management tools]]; the message also [[#Abrupt cut offs|ends unexpectedly]] }}

{{blockquote|text=

|title=From [[User:Gurkubondinn/Draft:Triple Entry Accounting|Draft:Triple Entry Accounting]] in May 2026, incorrectly advising a user with a COI to self-report to COI/N "after submission". }}
===Knowledge-cutoff disclaimers and speculation about gaps in sources=== {{shortcut|WP:AICUTOFF|WP:AIDISCLAIMER}} {{tmbox|image=none|text=Words to watch: {{strong|''as of [date]'',{{efn|not unique to AI chatbots; is produced by the {{tl|as of}} template}} ''Up to my last training update'', ''as of my last knowledge update'', ''While specific details are limited/scarce...'', ''not widely available/documented/disclosed'', ''...in the provided/available sources/search results...'', ''based on available information'' ...}}}} A knowledge-cutoff disclaimer is a statement used by an AI chatbot to indicate that the information provided may be incomplete, inaccurate, or outdated.

If an LLM has a fixed [[knowledge cutoff]] (usually the model's last training update), it is unable to provide any information on events or developments past that time. Older LLMs would often remind the user about this by outputting a disclaimer that the information in its response is accurate only up to a certain date, and may explicitly mention the knowledge cutoff in doing so.

Newer chatbots with [[retrieval-augmented generation]] may also fail to find sources on a given topic, or to find information within the sources a user provides. In these cases, they may output a statement, similar to a knowledge-cutoff disclaimer, claiming that the information is not publicly available. They may also pair it with text about what that information "likely" may be and why it is significant. This information is entirely [[WP:OR|speculative]] (including the very claim that it's "not documented") and may be based on loosely related topics or completely fabricated. When that unknown information is about an individual's personal life, this disclaimer often claims that the person "maintains a low profile", "keeps personal details private", etc. This is also speculative.

'''Examples''' {{blockquote|text={{highlight|As of my last knowledge update in January 2022}}, I don't have specific information about the current status or developments related to the "Chester Mental Health Center" in today's era.|title=From {{diff||1186779926|label=this November 2023 revision}} to [[Chester Mental Health Center]]}}

{{blockquote|text=Though the details of these resistance efforts {{highlight|aren't widely documented}}, they highlight her bravery...|title=From [[Special:Diff/1261964722|this December 2024 revision]] to [[Throwing Curves: Eva Zeisel]]}}

{{blockquote|text=While specific information about the fauna of Studniční hora {{highlight|is limited in the provided search results}}, the mountain likely supports...|title=From [[Special:Diff/1280231958|this March 2025 revision]] to [[Studniční hora]]}}

{{blockquote|text=While specific details about Kumarapediya's history or economy {{highlight|are not extensively documented in readily available sources}}, ...|title=From [[Special:Diff/1301052898|this July 2025 revision]] to [[Kumarapediya]]}}

{{blockquote|text=Below is a detailed overview {{highlight|based on available information}}:|title=From [[User:SuperPianoMan9167/Knowledge cutoff example 1|Draft:The Good, The Bad, The Dollar Menu 2]] (2025)}}

{{blockquote|text=As an underground release, detailed lyrics are {{highlight|not widely transcribed on major sites like Genius or AZLyrics}}, likely due to the artist's limited mainstream exposure. {{Highlight|My analysis is based on available track titles}}, featured artists, public song snippets from streaming platforms (e.g., Spotify, Apple Music, Deezer), and Honcho's overall discography themes. Where lyrics aren't fully accessible, {{highlight|I've inferred common motifs from similar trap tracks and Honcho's style.}} ...For deeper insights, listening to tracks on platforms like Spotify or Deezer is recommended, as {{highlight|lyrics and production details aren't fully documented in public sources.}}|title=From [[Draft:Haiti Honcho]] (2026)}}

===Phrasal templates and placeholder text=== AI chatbots may generate responses with fill-in-the-blank [[phrasal template]]s (as seen in the game ''[[Mad Libs]]'') for the LLM user to replace with words and phrases pertaining to their use case. However, some LLM users forget to fill in those blanks. Note that non-LLM-generated templates exist for drafts and new articles, such as [[Wikipedia:Artist biography article template/Preload]] and pages in [[:Category:Article creation templates]].

'''Examples''' {{blockquote| I hope this message finds you well. I am writing to request an edit for the Wikipedia entry

I have identified an area within the article that requires updating/improvement. {{highlight|[Describe the specific section or content that needs editing and provide clear reasons why the edit is necessary, including reliable sources if applicable]}}.|From [[Special:Diff/1210511971|this February 2024 revision]] to [[Talk:Spaghetti]]}}

{{blockquote|We remain committed to creating content that aligns with Wikipedia's mission and are open to further guidance. Please find our revised article [link to the revised article] and a detailed list of sources [link to source list]. We hope to resubmit our work once these changes have been made.

Thank you for your understanding and assistance in this matter.

Best regards, [Your Name] and Chloe |From [[Special:Diff/1261926945|this December 2024 revision]] to [[Wikipedia:WikiProject Articles for creation/Help desk]]}}

{{blockquote| I am writing to express my deep concern about the spread of misinformation on your platform. Specifically, I am referring to the article about {{highlight|[Entertainer's Name]}}, which I believe contains inaccurate and harmful information. |From [[Special:Diff/1278589409|this March 2025 revision]] to [[Talk:Kjersti Flaa]]}}

Large language models may also insert placeholder dates like "2025-xx-xx" into citation fields, particularly the access-date parameter and [[Special:PermaLink/1295449767#References|rarely the date parameter as well]], producing errors.

'''Examples''' {{blockquote| {{cite web |title=Canadian Screen Music Awards 2025 Winners and Nominees |url=URL |website=Canadian Screen Music Awards |date=2025 |access-date=2025-XX-XX }}

{{cite web |title=Best Original Score, Dramatic Series or Special – Winner: "Murder on the Inca Trail" |url=URL |website=Canadian Screen Music Awards |date=2025 |access-date=2025-XX-XX }} |From [[Special:Diff/1324292862|this November 2025 revision]] to [[Michelle Osis]]}}

'''Links to searches'''

[https://en.wikipedia.org/w/index.php?search=insource%3A%2F20%5B0-9%5D%5B0-9%5D-%28XX%7Cxx%29-%28XX%7Cxx%29%2F&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1 insource:/20[0-9][0-9]-(XX|xx)-(XX|xx)/]
In some cases, LLM-generated citations may also contain placeholders in other fields.

'''Examples''' {{blockquote|text= {{cite web
{{!}}url={{highlight|INSERT_SOURCE_URL_30}}
{{!}}title=Deputy Monitoring of Regional Assistance to Mobilized Soldiers
{{!}}date={{highlight|2022-11-XX}}
{{!}}publisher={{highlight|SOURCE_PUBLISHER}}
{{!}}accessdate=2024-07-21
}} |source=From [[Special:Diff/1330090335|this December 2025 revision]] to [[Dmitry Kuznetsov (politician)]]}}

{{blockquote|text= {{((}}cite web
{{!}}title{{=}}Ecos de Amor – Spotify
{{!}}url{{=}}{{highlight|PASTE_SPOTIFY_TRACK_URL_HERE}}
{{!}}website{{=}}Spotify
{{!}}access-date{{=}}2026-02-09
{{))}}
{{((}}cite web
{{!}}title{{=}}Jesse & Joy – Ecos de Amor (Official Music Video)
{{!}}url{{=}}{{highlight|PASTE_YOUTUBE_VIDEO_URL_HERE}}
{{!}}website{{=}}YouTube
{{!}}access-date{{=}}2026-02-09
{{))}} |source=From [[Special:Diff/1337437306|this February 2026 revision]] to [[Nelly Joy]]}}

LLM-generated infobox edits may contain comments stating that text or images should be added if sources are found. Note: Comments in infoboxes, especially older infoboxes, are common—some templates automatically include them—and not an indicator of AI use. Anything but "Add \_\_\_\_", or variations on that specific wording, is actually more likely to indicate human text.

'''Examples''' {{blockquote|{{!}} leader_name {{=}} {{highlight|}}|From [[Special:Diff/1301011748|this July 2025 revision]] to [[Pindi Saidpur]]}}

==Markup==

===Use of Markdown=== {{Shortcut|WP:MARKDOWN}}

A lot of AI chatbots are not proficient in [[H:WT|wikitext]], the [[markup language]] used to instruct Wikipedia's [[MediaWiki]] software how to format an article. As wikitext is a niche markup language, found mostly on wikis running on MediaWiki and other MediaWiki-based platforms like [[Miraheze]], LLMs wikitext-formatted content is not prominent in their training data. While the corpora of chatbots did ingest millions of Wikipedia articles, these articles would not have been processed as text files containing wikitext syntax.

In chatbot apps, the output display is formatted with Markdown, a markup language conceptually similar to wikitext but much more widely applied. Meanwhile, the chatbots' preprompts typically instruct them to use markdown in their answers, such as when providing lists and writing with headings. That is, their system-level instructions often direct them to format outputs using Markdown, and the chatbot apps render its syntax as formatted text on a user's screen. For example, the system prompt for Claude Sonnet 3.5 (November 2024) includes:{{cite web |title=System Prompts |url=https://platform.claude.com/docs/en/release-notes/system-prompts#claude-sonnet-3-5 |website=Claude Docs |publisher=Anthropic |access-date=9 January 2026}}

{{blockquote|Claude uses Markdown formatting. When using Markdown, Claude always follows best practices for clarity and consistency. It always uses a single space after hash symbols for headers (e.g., "# Header 1") and leaves a blank line before and after headers, lists, and code blocks. For emphasis, Claude uses asterisks or underscores consistently (e.g., italic or bold). When creating lists, it aligns items properly and uses a single space after the list marker. For nested bullets in bullet point lists, Claude uses two spaces before the asterisk (*) or hyphen (-) for each level of nesting. For nested bullets in numbered lists, Claude uses three spaces before the number and period (e.g., "1.") for each level of nesting.}}

As the above indicates, Markdown syntax is completely different from wikitext. Markdown uses asterisks (\*) or underscores (\_) instead of single-quotes (') for bold and italic formatting, hash symbols (#) instead of equals signs (=) for section headings, parentheses (()) instead of square brackets ([]) around URLs, and three symbols (---, \*\*\*, or \_\_\_) instead of four hyphens (----) for thematic breaks.

When told to "generate an article", chatbots often default to using Markdown for the generated output. This formatting is preserved in clipboard text by the copy functions on some chatbot platforms. If instructed to generate content for Wikipedia, the chatbot might "realize" the need to generate Wikipedia-compatible code, and might include a message like {{tqi|Would you like me to ... turn this into actual Wikipedia markup format (wikitext)?}}{{efn|[[Special:PermanentLink/1300700102|Example]] (deleted, administrators only)}} in its output. If the chatbot is told to proceed, the resulting syntax is often rudimentary, syntactically incorrect, or both. The chatbot might put its attempted-wikitext content in a Markdown-style [https://www.markdownguide.org/extended-syntax/#fenced-code-blocks fenced code block] (its syntax for [[WP:PRE]]) surrounded by Markdown-based syntax and content, which may also be preserved by platform-specific copy-to-clipboard functions, leading to a telling footprint of both markup languages' syntax. This might include the appearance of three backticks in the text, such as:
