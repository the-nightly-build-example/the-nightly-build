# Evidence record: when-ai-breaks/galactica (01)

The record supports the commissioned angle firmly. Galactica was a Meta AI /
Papers with Code language model trained on 106 billion tokens of scientific
text (48 million papers, textbooks, references, compounds, proteins), released
with a public demo at galactica.org on 15 November 2022 and paused by its own
team on 17 November 2022. The specific failure the commission names is
documented at the primary level three ways over: in firsthand experiments run
during the live window (Ernest Davis and Andrew Sundstrom at NYU), in the
paper's own ablation tables, which measure the model hallucinating citations,
and in the critics' and the team's own posts. The mechanism the commission wants
to teach is confirmed by the paper's own language: it names hallucination as an
inherent property of storing knowledge in weights, and it flags that the model
"likely requires augmentation before being used in a production environment."
Two facts complicate the angle without breaking it, and the writer must carry
both: the demo displayed an explicit per-output warning that outputs may be
unreliable, and Meta's later framing is that Galactica was a research demo whose
gap from a product expectation was too large, not a product it stood behind. The
record is thin in one place that matters: the three pivotal social-media posts
(the team's withdrawal statement, LeCun's, and Michael Black's) could not be
opened at their own pages in this session, so their wording rests on
reproduction in reporting while their timestamps were recovered independently
from the tweet IDs.

## Sources

```text
URL:         https://arxiv.org/abs/2211.09085  (paper also at https://galactica.org/static/paper.pdf)
Kind:        primary — the model's authoring team owns every claim about what Galactica is, how it was trained, and its measured behavior.
Establishes: Title "Galactica: A Large Language Model for Science." Nine authors in order: Ross Taylor, Marcin Kardas, Guillem Cucurull, Thomas Scialom, Anthony Hartshorn, Elvis Saravia, Andrew Poulton, Viktor Kerkez, Robert Stojnic. Affiliation: "Meta AI." v1 submitted 16 Nov 2022 18:06:33 UTC; only one version. Corpus is 106 billion tokens from "48 million papers, textbooks and lecture notes, millions of compounds and proteins, scientific websites, encyclopedias and more." Largest model is 120B parameters. The paper presents the model as "a new interface for science" and states "We open source the model." Crucially, it documents the failure at issue itself: (a) it names hallucination as intrinsic to weight memory; (b) its citation ablation (Table 26) measures the model producing hallucinated citations, worst for rarely-cited papers; (c) the Limitations section warns the model "likely requires augmentation before being used in a production environment"; (d) it discloses that "Galactica was used to help write this paper," including recommending citations.
Paraphrase:  The team built a science language model, benchmarked it above general models on technical tasks, and open-sourced it as a knowledge interface, while acknowledging in its own text that storing knowledge in weights produces hallucination and that title-based citation prediction carries a measurable hallucination rate.
Locators:    Abstract; §1 Introduction (p.2, corpus and "used to help write this paper"); §2 Related Work, "Language Models as Knowledge Bases" (hallucination named); §3.1 (title citations "more prone to hallucination error at lower scales"); §7.1 Limitations, "Citation Bias" and "General Knowledge" and "Verification"; §8 Conclusion ("We open source the models"); Appendix A.3, Table 26 (citation hallucination rates); dataset section, "Total dataset size = 106 billion tokens."
Quote:       "Storing information in weights is more unreliable in the sense models may blend information together, hallucination..." / "some bias towards popular papers still remains with the 120B scale model, so the model likely requires augmentation before being used in a production environment." / "We open source the model for the benefit of the scientific community."
```

```text
URL:         https://arxiv.org/abs/2211.09085
Kind:        primary — the arXiv record is the authoritative timestamp for the paper artifact.
Establishes: Exact submission stamp of the paper: "[v1] Wed, 16 Nov 2022 18:06:33 UTC (10,715 KB)." No later revision. Author list and abstract as above.
Paraphrase:  The paper's public record is dated 16 November 2022, one day after the demo went live.
Locators:    Submission history block on the abstract page.
Quote:       "[v1] Wed, 16 Nov 2022 18:06:33 UTC"
```

```text
URL:         https://cs.nyu.edu/~davise/papers/ExperimentWithGalactica.html
Kind:        primary (firsthand) — Ernest Davis (Professor of Computer Science, NYU) and Andrew Sundstrom ran these prompts against the live demo and recorded the outputs. They own the observation.
Establishes: Dated 15 November 2022, the launch day. Specific fabrications produced by the live model: (1) asked for a wiki article on the experiment to determine the gravitational constant, it conflated the task with Gravity Probe B and gave a false biography, claiming Leonard Schiff "went on to become a professor at the University of Maryland" (he was at Stanford). (2) Asked for a wiki article on the transit of Venus, it produced a gibberish list of pre-telescope transit dates (e.g. 362 BC, 283 BC) and asserted "The last known transit of Venus was in 1882," ignoring the 2004 and 2012 transits. (3) Asked about a nonexistent "Solomonov-Russell paradox," it invented an entire coin-flipping thought experiment. (4) Asked about a nonexistent "Crick-Watson-Solomonov-Russell paradox," it fabricated content attributing a paradox to Crick and Watson (1970) with an invented citation to "Toffoli (1978)."
Paraphrase:  Running the demo on launch day, two NYU researchers obtained fluent, authoritative articles for both real topics (told wrong) and entirely invented topics (fabricated wholesale, with made-up citations).
Locators:    Numbered query sections on the page (gravitational constant; transit of Venus; Solomonov-Russell; Crick-Watson-Solomonov-Russell; Streep-Seinfeld).
Quote:       "The last known transit of Venus was in 1882." (false; transits occurred in 2004 and 2012)
```

```text
URL:         https://garymarcus.substack.com/p/a-few-words-about-bullshit
Kind:        primary — Gary Marcus's own published critique. Owns his position; the examples he relays trace to other origins (see Contradictions).
Establishes: Published 16 November 2022. Marcus's characterization: Galactica produces "Pitch perfect and utterly bogus imitations of science and math, presented as the real thing" and "prevaricates. A lot." He credits David Chapman as "perhaps first to point this out" (the "bears in space" fabrication) and links the NYU experiment page for further examples.
Paraphrase:  A prominent critic framed the failure on release day as fluent fabrication indistinguishable from real science, pointing readers to firsthand examples rather than originating most of them.
Locators:    Opening (Hofstadter epigraph); body naming Chapman and linking cs.nyu.edu.
Quote:       "Pitch perfect and utterly bogus imitations of science and math, presented as the real thing." / "Is this really what AI has come to, automatically mixing reality with bullshit so finely we can no longer recognize the difference?"
```

```text
URL:         https://x.com/paperswithcode/status/1593259033787600896
Kind:        primary — the operator's own withdrawal statement. Papers with Code is the Meta team that shipped Galactica.
Establishes: The team paused the public demo. Tweet ID resolves to 17 Nov 2022 15:05:29 UTC (derived from the tweet-ID snowflake). This is the operator's own account of the takedown and the earliest primary timestamp for it.
Paraphrase:  Meta's Galactica team announced it had paused the demo while keeping the models available to researchers, thanking users for feedback rather than conceding a specific fault.
Locators:    Single tweet.
Quote:       "Thank you everyone for trying the Galactica model demo. We appreciate the feedback we have received so far from the community, and have paused the demo for now. Our models are available for researchers who want to learn more about the work and reproduce results in the paper."
Access note: The tweet could not be opened at x.com in this session (HTTP 402) and archive mirrors are blocked by egress policy; the wording above is reproduced identically across MIT Technology Review and multiple search reproductions, and the timestamp was computed from the tweet ID independently of any of them.
```

```text
URL:         https://x.com/ylecun/status/1593293058174500865
Kind:        primary — Yann LeCun's own words. LeCun was VP and Chief AI Scientist at Meta, the model's most prominent promoter.
Establishes: LeCun's reaction as the demo came down. Tweet ID resolves to 17 Nov 2022 17:20:41 UTC, roughly two hours after the team's pause statement. Confirms the demo was offline by that time and captures the promoter's dismissive framing of the criticism as "misuse."
Paraphrase:  Meta's chief AI scientist acknowledged the demo was offline and characterized the critics' inputs as people casually misusing the tool, not as the tool failing.
Locators:    Single tweet.
Quote:       "Galactica demo is off line for now. It's no longer possible to have some fun by casually misusing it. Happy?"
Access note: Same access limitation as the Papers with Code tweet. LeCun's separate launch-day promotion — "Type a text and Galactica will generate a paper with relevant references, formulas, and everything" — is quoted in MIT Technology Review; I could not pin its own tweet ID or timestamp, so it is carried as a secondary-reproduced quote, not an independently dated primary.
```

```text
URL:         https://x.com/Michael_J_Black/status/1593133722316189696
Kind:        primary (firsthand) — Michael J. Black, Director of the Max Planck Institute for Intelligent Systems (Perceiving Systems Dept., Stuttgart), tested the live model and reported the results in a nine-tweet thread.
Establishes: The best-documented expert critique, posted during the live window. Tweet ID resolves to 17 Nov 2022 06:47:33 UTC — hours before both the team's pause and LeCun's tweet, showing the criticism was live and public before the takedown. Black's thesis: the model generates authoritative-sounding pseudo-science and fabricates citations to real researchers.
Paraphrase:  A senior AI scientist reported that on topics he knew well the model was consistently wrong or biased yet sounded authoritative, that it fabricated citations, and that this risked "an era of deep scientific fakes."
Locators:    Thread, tweets 1/9 onward.
Quote:       "I asked #Galactica about some things I know about and I'm troubled. In all cases, it was wrong or biased but sounded right and authoritative. I think it's dangerous." / "It offers authoritative-sounding science that isn't grounded in the scientific method. It produces pseudo-science based on statistical properties of science 'writing.'" / "This could usher in an era of deep scientific fakes."
Access note: The full nine-tweet thread could not be opened at x.com (HTTP 402) or via archive mirrors (blocked by egress policy). The quotes above are reproduced in MIT Technology Review, aibusiness.com, the-decoder.com, and siliconrepublic.com; individual per-tweet examples beyond these quotes were not readable at the primary. Timestamp computed from the tweet ID.
```

```text
URL:         https://galactica.org/  (demo home and per-result interface, November 2022)
Kind:        primary — the demo artifact's own on-screen text. The live site is gone and its archive snapshot is blocked in this session, so the wording is carried through reporting.
Establishes: The public demo displayed a standing caution and tagged each generated result with a hallucination warning. This is material to the angle: Meta did warn users, and the failure is that fluent authority overrode the warning.
Paraphrase:  Every Galactica output shipped under a printed disclaimer that the text might be unreliable and should never be acted on without verification.
Locators:    Demo result caption and header, as reproduced.
Quote:       "WARNING: Outputs may be unreliable! Language Models are prone to hallucinate text." / "NEVER FOLLOW ADVICE FROM A LANGUAGE MODEL WITHOUT VERIFICATION."
Access note: galactica.org no longer serves the demo; its Wayback snapshot (web.archive.org/web/20221116213630) exists but web.archive.org is blocked by this session's egress policy. Wording reproduced across contemporaneous accounts; treat as primary-in-origin, secondary-in-access.
```

```text
URL:         https://www.technologyreview.com/2022/11/18/1063487/meta-large-language-model-ai-only-survived-three-days-gpt-3-science/
Kind:        secondary — Will Douglas Heaven reporting for MIT Technology Review, from outside Meta.
Establishes: Dated 18 November 2022. Quotes the Papers with Code pause statement, LeCun's launch promotion, Black's "wrong or biased but sounded right and authoritative," and Miles Cranmer (Princeton astrophysicist): "You should never keep the output verbatim or trust it." Reports the model blocked queries on topics like "racism" and "AIDS" with "Sorry, your query didn't pass our content filters." Frames the run as "only survived three days."
Paraphrase:  A reliable outlet, the day after the pause, assembled the promoter's, operator's, and critics' words and the content-filter behavior into one contemporaneous account, and set the "three days" framing.
Locators:    Body; pull-quotes from LeCun, Black, Cranmer; Meta statement.
Quote:       "Sorry, your query didn't pass our content filters." (Galactica's response to blocked topics, as reported)
```

```text
URL:         https://venturebeat.com/ai/what-meta-learned-from-galactica-the-doomed-model-launched-two-weeks-before-chatgpt
Kind:        secondary — Sharon Goldman reporting for VentureBeat, a year later.
Establishes: Dated 14 November 2023. Carries Meta's own retrospective framing via Joelle Pineau (VP of AI Research, Meta): the demo was pulled "to make sure that people were not misled into using it," it lacked "a responsible use guide which we've learned to do," and "The gap between the expectation, and where the research was, was too big." Gives the takedown as 17 November 2022, "3 days publicly available."
Paraphrase:  Meta's later account treats Galactica as a research demo that met an unintended product expectation, not a product it defended, and names the missing responsible-use guidance as the lesson it drew.
Locators:    Body; Pineau quotes.
Quote:       "The gap between the expectation, and where the research was, was too big." (Joelle Pineau)
```

## Contradictions

**The takedown date: 17 November vs 18 November.** The most-repeated secondary
framing is "18 November" and "only survived three days" (MIT Technology Review,
title and body). The primary timestamps place the pause on 17 November 2022: the
team's own Papers with Code statement resolves to 17 Nov 15:05 UTC, LeCun's
"offline" tweet to 17 Nov 17:20 UTC, and Black's critical thread to 17 Nov 06:47
UTC. VentureBeat (2023) and louisbouchard.ai also give 17 November, the latter
calling it "two days after launch." Resolution: the demo was paused on 17
November 2022; the "18 November" in some outlets is the reporting date, not the
takedown. The writer should state 15–17 November and note that "three days" is
the popular framing.

**The interval: "three days" / "72 hours" vs roughly two days.** Launch was 15
November 2022; the pause statement is timestamped 17 November ~15:05 UTC. That is
about two days (~48–54 hours) of live public availability, not 72 hours. "Three
days" counts the calendar days 15, 16, 17 inclusively; "72 hours" and "two days"
both circulate. The exact launch hour on 15 November is not pinned in the primary
material I could open, so the interval is best given as "about two days, released
15 November and paused 17 November," with "three days" noted as the common
shorthand.

**Whether Meta stood behind it.** LeCun's contemporaneous posture (critics were
"casually misusing it") and Pineau's later posture ("the gap between the
expectation and where the research was was too big") both frame the fault as
misuse or misread expectation rather than a model defect. This sits against the
critics' claim (Black, Marcus) and against the paper's own text, which documents
hallucination and warns against production use. The evidence favors the critics
on the substance: the failure mode was real, foreseeable, and partly
self-documented. The team's framing is a genuine second account and must be
steelmanned, not omitted.

**Did the demo warn users?** Yes — the per-output banner ("Outputs may be
unreliable! Language Models are prone to hallucinate text") is documented. This
does not contradict the fabrication finding; it sharpens it. The critics' point
is that a small disclaimer is defeated when the output reads as authoritative
science. Any draft that implies Meta gave no warning would be wrong.

**Attribution overlap (the "two retellings count as one" test).** The vivid
examples cluster around two firsthand origins. The transit-of-Venus, fabricated-
paradox, and false-biography examples originate with Davis and Sundstrom (NYU
page, read directly here). The "bears in space" example originates with David
Chapman; Marcus relays it and I could not open Chapman's original post, so it
counts as one firsthand origin accessed through a retelling. Black's citation-
fabrication and pseudo-science examples are a separate firsthand origin. Marcus's
post is one confirmation of the critique, not an independent second confirmation
of the examples it borrows.

## Numbers

```text
Figure: Released 15 Nov 2022; public demo paused 17 Nov 2022 (~15:05 UTC per the team's own statement)
Owner:  Papers with Code / Meta (pause statement); launch date corroborated across primary and secondary
Scope:  Public demo at galactica.org; interval about two days live (popularly "three days" / "72 hours")
```

```text
Figure: arXiv v1 submitted 16 Nov 2022 18:06:33 UTC
Owner:  arXiv record for 2211.09085
Scope:  Single version; the paper, distinct from the demo
```

```text
Figure: 106 billion training tokens; 48 million source documents (papers, textbooks, lecture notes) plus millions of compounds and proteins
Owner:  Galactica paper (dataset section; §1)
Scope:  Full training corpus
```

```text
Figure: Largest model 120B parameters; open-sourced family also 125M, 1.3B, 6.7B, 30B
Owner:  Galactica paper (§1, §3) and the released model weights
Scope:  Model sizes
```

```text
Figure: Self-documented citation hallucination — at 6.7B, title-based method citations for singly-cited papers (k=1): 13.8% correct, 54.5% hallucinated, 31.7% incorrect
Owner:  Galactica paper, Appendix A.3, Table 26
Scope:  1,705 Papers-with-Code methods; hallucination falls sharply for heavily-cited papers (≥500 mentions: 78.6% correct, 0.0% hallucinated). This is the model's own measurement that it invents citations for obscure work.
```

```text
Figure: Headline benchmark claims — LaTeX equations 68.2% vs GPT-3 49.0%; mathematical MMLU 41.3% vs Chinchilla 35.7%; MATH 20.4% vs PaLM 540B 8.8%; PubMedQA 77.6%; MedMCQA dev 52.9%
Owner:  Galactica paper (Abstract, §1)
Scope:  The team's own reported results; these are the promotional figures, not independently reproduced here
```

## Source assets

```text
Asset: Galactica paper, Table 26 (Appendix A.3), "Citation Processing Ablation"
Shows: The model's own numbers on hallucinated citations, worst for rarely-cited papers and near-zero for popular ones. A reader sees the failure quantified by the builders themselves and the scale-dependence of it.
Crop:  Keep the "Titles" columns (Correct / Hallucinated / Incorrect) and the k-bucket rows; the "IDs" columns and the dataset-citation twin table can be omitted. Retain the caption's "1,705 methods" and "6.7 billion" so the scope is not lost.
```

```text
Asset: The galactica.org demo per-output warning line ("WARNING: Outputs may be unreliable! Language Models are prone to hallucinate text")
Shows: That the fabrication shipped under an explicit disclaimer, the exact tension the lesson turns on. A screenshot would carry more than prose.
Crop:  The demo interface is gone and no snapshot was openable in this session, so no verified image exists to crop. If the writer wants the visual, it must be re-sourced; do not reconstruct it.
```

```text
Asset: Ernest Davis / Andrew Sundstrom transit-of-Venus output on the NYU page
Shows: A concrete, checkable fabrication — a confident false claim ("last known transit was in 1882") a reader can verify against the real 2004 and 2012 transits.
Crop:  Retain the prompt and the false date list together so the reader sees input and invented output side by side.
```

## Discarded

```text
URL: https://web.archive.org/web/20221119053137/... (Black thread) and web.archive.org/web/20221116213630/https://galactica.org/ — snapshots exist and would be the cleanest primary access, but web.archive.org is blocked by this session's egress policy; recorded as the correct address for a reader, not usable by me here.
URL: https://archive.ph/... (Michael Black thread mirror) — blocked by egress policy in this session.
URL: https://x.com/... direct tweet pages — returned HTTP 402/429; content recovered through reporting and IDs instead.
URL: https://sh-tsang.medium.com/... , https://declom.com/galactica , https://theaifiles.app/stories/galactica , gigazine.net, techtimes.com, newsbytesapp.com, mezha.ua — secondary retellings adding nothing the named primaries and the two cited secondaries do not already establish; several disagree on the takedown date and were not relied on.
URL: https://officechai.com/... — reproduces LeCun's "offline" quote (used to corroborate) but is a thin aggregator; not counted as an independent source.
URL: https://link.springer.com/article/10.1007/s00146-024-02088-7 ("Galactica's dis-assemblage") — a 2024 scholarly analysis that likely reproduces the demo disclaimer verbatim; not opened in full here, noted as a stronger re-source for the demo-warning text if the writer needs a citable secondary for it.
```
