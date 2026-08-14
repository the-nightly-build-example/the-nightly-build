# Evidence: Humanity's Last Exam (the-instruments/humanitys-last-exam, 01)

The evidence strongly supports the commissioned angle. Primary sources establish end to end how an HLE score is produced: nearly 1,000 expert contributors write closed-ended academic questions, each question is filtered against frontier LLMs before submission so that only questions the models fail enter the set, the public release holds 2,500 questions, and grading is automated with a model judge against a known answer. The paper's own Table 1 owns the launch no-tool scores (GPT-4o 2.7%, o1 8.0%, DeepSeek-R1 8.5%, o3-mini high 13.4%), and the official Scale/CAIS leaderboard owns the current no-tool scores. The tool-vs-no-tool gap is real and large, and the clearest documented misreading is well anchored: Fortune (Feb 12, 2025) reported OpenAI deep research's 26.6% as a "nearly threefold jump" over o1/DeepSeek at ~9% and called HLE "a benchmark for the frontier of human knowledge," without disclosing that 26.6% was achieved with browsing and Python tools while the ~9% figures were no-tool leaderboard numbers. That framing runs directly against the authors' own written caveat that a high HLE score "would not alone suggest autonomous research capabilities or 'artificial general intelligence.'"

Where the record is thin: the two cleanest primary tool-vs-no-tool figures live on OpenAI's own pages (the deep research announcement and the GPT-5 launch), and those pages return HTTP 403 to this fetcher (host-side bot blocking, not a proxy policy denial). The 26.6%-with-tools figure and the GPT-5 42.0%-with-tools / 24.8%-no-tools figures are therefore carried here through the HLE paper, the Fortune report, and a secondary (Vellum) that cites OpenAI, not through OpenAI's primary page. The current 2026 leaderboard state is a live board read on 2026-08-14; its model names and top scores are recorded as read, and the board rises over time. Two small primary-vs-primary discrepancies exist on the multiple-choice fraction (24% in the paper text vs ~20% on the official site) and on the bug-bounty removal count (described but not quantified). All noted below.

## Sources

```text
URL:         https://arxiv.org/abs/2501.14249
Kind:        primary — the benchmark's own paper (Center for AI Safety and Scale AI), the document that owns the design and launch results.
Establishes: The published dataset is 2,500 questions across dozens of subjects (mathematics, humanities, natural sciences), multiple-choice and short-answer, each with a known unambiguous answer "that cannot be quickly answered via internet retrieval." Version history: v1 submitted Jan 24, 2025; latest v11 dated Jul 28, 2026. Published in Nature (doi:10.1038/s41586-025-09962-4). Public release at lastexam.ai. 1,154+ listed authors.
Paraphrase:  HLE was built because frontier models had saturated older tests ("LLMs now achieve over 90% accuracy on popular benchmarks like MMLU"). State-of-the-art models "demonstrate low accuracy and calibration on HLE," which the authors read as a gap between current models and "the expert human frontier on closed-ended academic questions."
Locators:    Abstract and header (v11 landing page).
Quote:       "Each question has a known solution that is unambiguous and easily verifiable, but cannot be quickly answered via internet retrieval."
```

```text
URL:         https://arxiv.org/html/2501.14249v11
Kind:        primary — full text of the same paper.
Establishes: The production procedure and the launch scoreboard. Contributors: "nearly 1000 subject expert contributors affiliated with over 500 institutions across 50 countries"; reviewers held "a graduate degree (eg. Master's, PhD, JD, etc.)" in their field, across two review rounds. Adversarial filtering: "each question is first validated against several frontier LLMs prior to submission"; a multiple-choice question proceeds only if the models "on average do worse than random guessing," and an exact-match question proceeds only where the "LLMs cannot solve the question." The pipeline logged "over 70,000 attempts, resulting in approximately 13,000 questions which stumped LLMs." Formats: "24% of questions are multiple-choice with the remainder being exact-match" (so 76% exact-match); multimodal "around 14%." Grading: "We use o3-mini as a judge to verify answer correctness against model predictions" allowing equivalent forms (decimals vs fractions, estimations). Public/private split: "We publicly release these questions, while maintaining a private test set of held out questions to assess model overfitting." Scope caveat (Discussion): HLE tests closed-ended academic problems, not open-ended or autonomous research.
Paraphrase:  The number is manufactured by inverting a test: experts propose questions, and a question only counts if named frontier models already fail it, which guarantees launch scores are near the floor by construction. A separate judge model then marks each answer against the stored ground truth.
Locators:    Section 3 (Dataset), Table 1 (Main results), Discussion/Impact, Appendix B.2 (Post-Release).
Quote:       "High accuracy on HLE would demonstrate expert-level performance on closed-ended, verifiable questions and cutting-edge scientific knowledge, but it would not alone suggest autonomous research capabilities or 'artificial general intelligence.'" And: "HLE tests structured academic problems rather than open-ended research or creative problem-solving abilities."
```

```text
URL:         https://arxiv.org/abs/2501.14249v1
Kind:        primary — the original January 2025 version of the paper.
Establishes: At first release the paper described 3,000 questions, not 2,500. The count in the published/current version (2,500 public) is lower than the original announcement.
Paraphrase:  The launch abstract put the set at 3,000 questions; the public release settled at 2,500, with the difference accounted for by a held-out private set and by later removal of flagged questions (the exact split is not quantified in the paper text).
Locators:    v1 abstract.
Quote:       "HLE consists of 3,000 questions across dozens of subjects, including mathematics, humanities, and the natural sciences."
```

```text
URL:         https://agi.safe.ai/
Kind:        primary — the official HLE site (Center for AI Safety / Safe.ai), which owns the dataset description and the calibration framing.
Establishes: Dataset "2,500 questions across over 100 subjects." Format split as stated on the site: "Approximately 80% of questions are exact-match ... while the remaining 20% are multiple-choice," multimodal "about 10%." Calibration is measured by having models "provide both an answer and their confidence from 0% to 100%"; calibration error captures how far over- or under-confident the model is. The site records that "Questions flagged in the bug bounty program and searchable questions have been removed and replaced" (dated update).
Paraphrase:  The official framing pairs accuracy with a calibration-error number precisely because low accuracy plus high confidence is the failure mode the benchmark wants to expose. The site also documents that some released questions were later pulled as flawed or searchable.
Locators:    Front page dataset and calibration sections; dataset-update note.
Quote:       "Questions flagged in the bug bounty program and searchable questions have been removed and replaced."
```

```text
URL:         https://labs.scale.com/leaderboard/humanitys_last_exam
Kind:        primary — the official Scale/CAIS HLE leaderboard, which owns the ongoing no-tool scores.
Establishes: This board is a no-tool, no-browsing evaluation: every model is run "on all public questions of Humanity's Last Exam with temperature 0.0 when configurable," using "o3-mini-2025-01-31 as an automatic extractor and judge." Top of board as read 2026-08-14: gemini-3.1-pro-preview (thinking high) 46.44±1.96%, cal. err. 51; gpt-5.4-pro-2026-03-05 44.32±1.95%, cal. err. 38; Muse Spark 40.56±1.92%, cal. err. 50; gemini-3-pro-preview 37.52±1.90%, cal. err. 57; gpt-5.4-2026-03-05 (xhigh) 36.24±1.88%, cal. err. 42. The board notes "systematic high calibration errors (greater than 80%) paired with low accuracy (less than 10%)" among weaker models as "strong evidence for confabulation/hallucination."
Paraphrase:  The default public leaderboard is explicitly a closed-book, no-tool measurement. Even the current leaders sit below ~47% and still carry calibration error in the 38–57 range, so overconfidence persists as scores climb. Model names and figures are recorded as read on 2026-08-14; the board is live and moves.
Locators:    Leaderboard table and methodology note (accessed 2026-08-14).
Quote:       "each model on the leaderboard is evaluated on all public questions of Humanity's Last Exam with temperature 0.0 when configurable."
```

```text
URL:         https://www.futurehouse.org/research-announcements/hle-exam
Kind:        primary — FutureHouse owns this audit finding firsthand.
Establishes: Of 321 text-only chemistry and biology questions audited, "29 ± 3.7% (95% CI)" had answers that conflict with peer-reviewed literature. Method: their PaperQA2 agent ("Crow") searched for supporting or contradicting evidence for each HLE rationale, followed by independent expert review (150 questions, Likert scale). Crow initially flagged 53.3% (n=171) of rationales as directly conflicting (chemistry 57.0%, biology/health 51.6%); expert review narrowed the confident figure to ~29%. The HLE team's own September 2025 follow-up "found about 18% of a subset of questions in Bio/Chem were problematic," and their three-expert process saw "25% of the time at least one reviewer disagreed."
Paraphrase:  An independent lab found that roughly three in ten of the bio/chem answers HLE grades against are themselves wrong or misleading, which means a model can be marked wrong for giving the better answer. The benchmark's own authors, re-checking, put the problematic share at ~18%, still material.
Locators:    Research announcement body; released dataset "HLE Bio/Chem Gold" on HuggingFace.
Quote:       "29 ± 3.7% (95% CI)" of the audited chemistry/biology answers conflict with published evidence.
```

```text
URL:         https://www.fortune.com/2025/02/12/openai-deepresearch-humanity-last-exam
Kind:        primary — for the misreading, this article is the artifact: it owns its own framing, and the framing is the evidence.
Establishes: The clearest documented over-read. Headline: "OpenAI's deep research can complete 26% of Humanity's Last Exam—a benchmark for the frontier of human knowledge." Author Greg McKenna, Feb 12, 2025. It defines HLE as "a global benchmark created to determine when AI can answer questions on any topic better than a world-class expert in the field," reports that "Deep research successfully completed 26.6% of the recently developed test," and calls this "a nearly threefold jump" over o1/DeepSeek R1 at ~9%. The article does not disclose that the 26.6% run used web browsing and Python tools while the ~9% figures were no-tool leaderboard numbers.
Paraphrase:  A major outlet took a tool-and-browsing agent score (26.6%) and compared it directly to no-tool model scores (~9%) as a like-for-like leap, while describing the benchmark as a measure of whether AI can beat world-class experts on any topic. Both moves overstate what the number supports, and the tool/no-tool conflation is the concrete mechanism of the error.
Locators:    Headline, opening paragraphs.
Quote:       Headline: "OpenAI's deep research can complete 26% of Humanity's Last Exam—a benchmark for the frontier of human knowledge." Body: "a global benchmark created to determine when AI can answer questions on any topic better than a world-class expert in the field."
```

```text
URL:         https://en.wikipedia.org/wiki/Humanity%27s_Last_Exam
Kind:        secondary — encyclopedia summary, useful for corroboration and dated context.
Establishes: Corroborates 2,500 questions "in the publicly released set," questions "crowdsourced from subject matter experts," and that items "typically require graduate-level expertise." Cites the FutureHouse audit: "An independent investigation by FutureHouse, published in July 2025, suggested that around 30% of the HLE answers for text-only chemistry and biology questions could be incorrect." Carries a current results table dated 14 August 2026.
Paraphrase:  Independent corroboration of the release size, the expert-sourcing, the graduate-level framing, and the FutureHouse error finding. Its live results table matches the leaderboard picture read the same day.
Locators:    Lead, "Reception"/criticism section (ref 5), results table.
Quote:       "around 30% of the HLE answers for text-only chemistry and biology questions could be incorrect."
```

```text
URL:         https://www.vellum.ai/blog/gpt-5-benchmarks
Kind:        secondary — reports OpenAI's GPT-5 HLE figures; used only because the OpenAI primary is host-blocked to this fetcher.
Establishes: GPT-5's HLE gap between a tool-using and a no-tool run of the same family: "GPT-5 Pro (with tools and reasoning): 42%"; "GPT-5 base (no tools): 6.3% (without thinking), 24.8% (with thinking)." Presented as OpenAI's reported numbers.
Paraphrase:  On one model family, adding retrieval and a code tool roughly doubles the HLE score (about 24.8% no-tool with reasoning to 42% with tools), which is the concrete tool-vs-no-tool gap the commission asked for. Held as secondary because it relays OpenAI's figures rather than owning them; the OpenAI primary (openai.com/index/introducing-gpt-5) returns 403 to this fetcher.
Locators:    GPT-5 benchmark table, HLE row.
Quote:       "GPT-5 Pro (with tools and reasoning): 42%"; "GPT-5 base (no tools): ... 24.8% (with thinking enabled)."
```

```text
URL:         https://the-decoder.com/nearly-29-percent-of-humanitys-last-exam-questions-are-wrong-or-misleading/
Kind:        secondary — reports the FutureHouse finding; second retelling for confirmation of the audit's magnitude.
Establishes: Independent restatement that ~29% of the audited chemistry/biology answers are wrong or misleading, matching the FutureHouse primary. Confirms the finding was picked up in mainstream AI press.
Paraphrase:  A second outlet reproduces the ~29% figure and attributes it to FutureHouse, supporting that the claim was reported, not that it independently re-verified it. Weight rests on the FutureHouse primary above.
Locators:    Headline and lead.
Quote:       Headline: "Nearly 29 percent of 'Humanity's Last Exam' chemistry/biology answers are wrong or misleading."
```

## Contradictions

- Multiple-choice fraction, primary vs primary. The paper text states "24% of questions are multiple-choice" (76% exact-match); the official site states "Approximately 80% ... exact-match ... the remaining 20% ... multiple-choice." A 4-point disagreement between two first-party sources. Report as "roughly 20–24% multiple-choice, the rest exact-match" rather than a false precision.
- Multimodal fraction. Paper says "around 14%"; official site says "about 10%." Report as roughly 10–14%.
- Question count over time. The original January 2025 abstract said 3,000; the published set is 2,500 public plus an unquantified private holdout, and the official site records flagged/searchable questions "removed and replaced." No single primary gives the exact arithmetic from 3,000 to 2,500, so do not state a precise removal count.
- Size of the flaw problem. FutureHouse's audited figure is ~29% of bio/chem answers wrong; the HLE authors' own re-check put it at ~18%. Both are material; give the range and attribute each to its owner. This does not undermine the commission — it strengthens the "what the number cannot support" half — but the article must not present ~29% as undisputed.
- The commission's angle survives contact with the counter-evidence. The one thing that could soften it, the authors' framing, actually supports it: the authors themselves warn the score does not imply AGI or autonomous research, so the misreading is a misreading against the benchmark's own stated scope, not against a critic's interpretation.

## Numbers

```text
Figure: 2,500 questions (public release)
Owner:  HLE paper (arXiv 2501.14249, Section 3) and agi.safe.ai
Scope:  Public set; a separate private held-out set exists (size not stated). Original Jan 2025 abstract said 3,000.
```

```text
Figure: nearly 1,000 expert contributors; 500+ institutions; 50 countries
Owner:  HLE paper (Section 3)
Scope:  Contributors to the dataset; reviewers held graduate degrees, two review rounds.
```

```text
Figure: ~70,000 model attempts -> ~13,000 questions that stumped LLMs
Owner:  HLE paper (Section 3)
Scope:  Adversarial filtering pipeline before final selection.
```

```text
Figure: ~20-24% multiple-choice, ~76-80% exact-match; ~10-14% multimodal
Owner:  HLE paper and agi.safe.ai (the two disagree; see Contradictions)
Scope:  Composition of the public set.
```

```text
Figure: Launch no-tool accuracy / calibration error (Jan 2025), HLE paper Table 1
Owner:  HLE paper Table 1
Scope:  No tools, no browsing, public set, o3-mini judge.
        GPT-4o                2.7% / cal. err. 89%
        Grok 2                3.0% / 87%
        Claude 3.5 Sonnet     4.1% / 84%
        Gemini 1.5 Pro        4.6% / 88%
        Gemini 2.0 Flash Thk  6.6% / 82%
        o1                    8.0% / 83%
        DeepSeek-R1           8.5% / 73%
        o3-mini (high)       13.4% / 80%
```

```text
Figure: OpenAI deep research 26.6% WITH web browsing + Python tools (Feb 2025)
Owner:  OpenAI deep research announcement (primary, but openai.com returns 403 to this fetcher); reported by Fortune (Feb 12, 2025) and widely. The ~9% comparison figures (o1, DeepSeek-R1) are the no-tool leaderboard numbers.
Scope:  Tool-and-browsing agent run; NOT comparable to the no-tool board. This is the tool/no-tool conflation at the center of the misreading.
```

```text
Figure: GPT-5 family tool-vs-no-tool gap (Aug 2025)
Owner:  OpenAI (reported via Vellum, secondary; OpenAI primary 403 to this fetcher)
Scope:  Same model family. No tools, with reasoning: 24.8%. With tools (GPT-5 Pro, Python + search): 42.0%. About a doubling from tool access alone.
```

```text
Figure: Current no-tool leaderboard leaders (accessed 2026-08-14)
Owner:  Scale/CAIS official leaderboard
Scope:  No tools, temperature 0, public set. gemini-3.1-pro-preview 46.44%, gpt-5.4-pro 44.32%, gemini-3-pro-preview 37.52%. Calibration error still 38-57%. Live board; figures move.
```

```text
Figure: ~29% (95% CI 29 +/- 3.7%) of audited bio/chem answers wrong or misleading
Owner:  FutureHouse (audit of 321 text-only chem/bio questions)
Scope:  Chemistry + biology text-only subset only, not the whole set. HLE authors' own re-check: ~18% problematic.
```

Suggested chart series (primary numbers only; keep tool and no-tool as separate series, never merged):
No-tool track: GPT-4o 2.7% (Jan 2025) -> o1 8.0% (Jan 2025) -> o3-mini high 13.4% (Jan 2025) -> GPT-5 (reasoning, no tools) 24.8% (Aug 2025) -> gemini-3.1-pro-preview 46.44% (Aug 2026 board).
With-tools track (label explicitly): deep research 26.6% (Feb 2025); GPT-5 Pro 42.0% (Aug 2025). The whole point of the chart is that plotting the with-tools points on the no-tool curve is exactly the error Fortune made.

## Source assets

```text
Asset: HLE paper, Table 1 (main results: accuracy and calibration error per model).
Shows: That launch scores were single digits by construction AND that calibration error was 70-89%, i.e. models were confidently wrong. Carries the "low score is manufactured" and "the second column matters" points at once.
Crop:  Must retain both the accuracy column and the calibration-error column; a crop that keeps only accuracy loses the overconfidence finding, which is half the lesson.
```

```text
Asset: HLE paper, the dataset/pipeline figure showing question flow from expert submission through frontier-model filtering to final selection.
Shows: Visually, that a question only enters the set if the models already fail it, which explains why the starting number is near zero.
Crop:  Keep the filter stage ("validated against frontier LLMs" / "stumped LLMs") legible; that node is the argument.
```

```text
Asset: Fortune headline as published (the misreading artifact itself).
Shows: The exact over-read in the wild: a 26.6% tool-assisted score framed as "the frontier of human knowledge." A screenshot of the headline is stronger evidence than a paraphrase.
Crop:  Retain the full headline including "a benchmark for the frontier of human knowledge"; retain the byline/date for attribution. Do not crop out the outlet name.
```

```text
Asset: Scale/CAIS leaderboard table (current no-tool board).
Shows: Current leaders below ~47% with calibration error still 38-57%, and the explicit no-tool methodology note.
Crop:  Keep the methodology line stating temperature 0 / all public questions so the reader sees these are no-tool numbers; that context is what makes the tool-conflation visible.
```

## Discarded

```text
URL: https://openai.com/index/introducing-deep-research/  — Primary for the 26.6%-with-tools figure, but returns HTTP 403 to this fetcher (host-side bot block, not a proxy policy denial; proxy recentRelayFailures was empty). Figure carried via Fortune + HLE paper instead. Writer should link the OpenAI page as the owner even though it was not directly read here.
```

```text
URL: https://openai.com/index/introducing-gpt-5/  — Primary for GPT-5 tool/no-tool HLE figures; also 403 to this fetcher. Carried via Vellum (secondary).
```

```text
URL: https://www.techradar.com/computing/artificial-intelligence/openais-deep-research-smashes-records-... — Fetched but returned only nav/membership chrome, no article body. Not usable as a source; the Fortune primary covers the same misreading better.
```

```text
URL: https://labs.scale.com/leaderboard/humanitys_last_exam_text_only  — Not separately opened; the main board already establishes the no-tool methodology and current scores. Named here only so a later invocation knows a text-only variant exists.
```

```text
URL: https://labs.adaline.ai/... , https://letsdatascience.com/... , https://airank.dev/... , https://pricepertoken.com/... , various leaderboard-aggregator blogs — surfaced in search, not opened as sources. They repeat the official leaderboard without owning any figure; use the Scale/CAIS board and the paper instead.
```
