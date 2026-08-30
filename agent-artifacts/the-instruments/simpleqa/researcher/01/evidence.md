# Evidence: the-instruments/simpleqa (01)

The evidence strongly supports the commissioned angle. SimpleQA is built from two
choices that the primary sources state plainly: questions were kept only if a
GPT-4-class model got them wrong (adversarial selection), and each answer is
graded correct / incorrect / not-attempted so that abstention is scored
separately from error (abstention-aware scoring). Both are verified against the
paper itself, not a summary. The raw percent-correct is therefore low by design,
and the paper says so ("GPT-4o and Claude both score less than 50%"). The misled
case is documented at first hand and is stronger than expected: OpenAI's own o1
System Card relabels the SimpleQA incorrect rate as a "hallucination rate" in a
table titled "Hallucination Evaluations," and mainstream coverage (ABC Science)
carries that framing forward as "GPT-4.5 hallucinated 37 per cent of the time."
The TruthfulQA contrast is clean and sourced to both papers. Where the record is
thin: I could not fetch OpenAI's "Introducing SimpleQA" blog page directly (HTTP
403); every substantive claim it would carry is covered by the paper, which I
read in full, and its 30 October 2024 date is corroborated across sources but not
read off the page itself. Cross-source scores for the "same" model differ by a
few points because they are different model snapshots and different evaluators;
these are recorded under Contradictions and Numbers, and none of them undermine
the angle.

## Sources

```text
URL:         https://arxiv.org/abs/2411.04368  (full text read at https://cdn.openai.com/papers/simpleqa.pdf)
Kind:        primary — the authoring document. OpenAI (Wei, Karina, Chung, Jiao, Papay, Glaese, Schulman, Fedus) owns the benchmark design, counts, grader definitions, metrics, and the model table. arXiv v1 dated 7 Nov 2024.
Establishes: What SimpleQA is; the 4,326-question count; how questions were written and verified; the adversarial "must be challenging" criterion; the three grades and their definitions; the correct / correct-given-attempted / F-score metrics; Table 3 scores; calibration; stated limitations.
Paraphrase:  "We present SimpleQA, a benchmark that evaluates the ability of language models to answer short, fact-seeking questions... First, SimpleQA is challenging, as it is adversarially collected against GPT-4 responses. Second, responses are easy to grade, because questions are created such that there exists only a single, indisputable answer." Data collection: AI trainers (human annotators) wrote question/answer pairs; a second independent trainer re-answered each, and only questions where both matched were kept. Inclusion criteria: single indisputable answer; answer must not change over time; reference answer backed by a linked webpage; and "Must be challenging" — trainers reviewed four OpenAI-model completions and kept a question only if at least one completion was incorrect ("For most of the data creation process, all four completion came from GPT-4 models of various release dates. Towards the end, we changed one model to GPT-3.5"). Questions had to be answerable as of 31 December 2023. Grading is done by a prompted ChatGPT classifier into correct / incorrect / not attempted. A single-number F-score is the harmonic mean of overall-correct and correct-given-attempted, = 2c/(2c+2i+n). The paper flags that F-score rewards guessing above 50% confidence, and offers a penalty-weighted alternative.
Locators:    Abstract (p.1); §1 Introduction and Table 1 (p.2); §2.1 criteria (p.3); §2.2 data quality (pp.3–4); §2.4 grading + Table 2 (p.5); metrics + F-score (p.6); §3 + Table 3 (pp.6–7); §4 calibration + Figure 2 (pp.7–8); §5 limitation (p.8); Appendix A grader template (pp.11–12); Appendix B F-score (p.13).
Quote:       "At least one of the four completions must be incorrect for the trainer to continue with that question; otherwise, the trainer was instructed to create a new question." (§2.1). Grader definitions (Table 2): Correct — "The predicted answer fully contains the reference answer without contradicting the reference answer." Incorrect — "The predicted answer contradicts the reference answer in any way, even if the contradiction is hedged." Not attempted — "The reference answer is not fully given in the answer, and there are no contradictions with the reference answer." Limitation (§5) — "while it is accurate, it only measures factuality under the constrained setting of short, fact-seeking queries with a single, verifiable answer."
```

```text
URL:         https://arxiv.org/abs/2109.07958  (TruthfulQA)
Kind:        primary — Lin, Hilton, Evans own the TruthfulQA design. Used for the Background contrast.
Establishes: What TruthfulQA measures — imitative falsehoods, i.e., false answers a model learns by mimicking human text, targeting common human misconceptions. This is a different quantity from SimpleQA's obscure-fact recall.
Paraphrase:  817 questions across 38 categories (health, law, finance, politics, etc.). Questions were "crafted so that some humans would answer falsely due to a false belief or misconception." The benchmark measures whether a model reproduces widespread human errors rather than whether it recalls a rare fact. Best model was truthful on 58% of questions vs 94% for humans; larger models were often *less* truthful because they better absorbed the misconceptions.
Locators:    Abstract; benchmark description.
Quote:       Questions are designed such that "some humans would answer falsely due to a false belief or misconception"; models "generated many false answers that mimic popular misconceptions."
```

```text
URL:         https://arxiv.org/abs/2412.16720  (OpenAI o1 System Card, 5 Dec 2024; PDF read directly)
Kind:        primary — OpenAI owns the o1 SimpleQA numbers reported here. This is also the in-house origin of the "hallucination rate" relabeling.
Establishes: o1-family SimpleQA scores, and that OpenAI presents SimpleQA inside a section titled "Hallucination Evaluations," with the incorrect share renamed "hallucination rate."
Paraphrase:  §4.1.4 "Hallucination Evaluations" lists SimpleQA as an eval "that aim[s] to elicit hallucinations," described as "A diverse dataset of four-thousand fact-seeking questions with short answers and measures model accuracy for attempted answers." Table 3 reports two metrics per dataset: accuracy and "hallucination rate (lower is better)." For SimpleQA: GPT-4o accuracy 0.38 / hallucination rate 0.61; o1 0.47 / 0.44; o1-preview 0.42 / 0.44; GPT-4o-mini 0.09 / 0.90; o1-mini 0.07 / 0.60. (Note: for GPT-4o, 0.38 + 0.61 = 0.99, so "hallucination rate" here is just the SimpleQA incorrect share; the residual is not-attempted.)
Locators:    §4.1.4 and Table 3 (p.5).
Quote:       "SimpleQA: A diverse dataset of four-thousand fact-seeking questions... We consider two metrics: accuracy (did the model answer the question correctly) and hallucination rate (checking how often the model hallucinated)."
```

```text
URL:         https://cdn.openai.com/gpt-4-5-system-card-2272025.pdf  (OpenAI GPT-4.5 System Card, 27 Feb 2025; PDF read directly)
Kind:        primary — OpenAI owns this document. Relevant caveat below about which benchmark its hallucination table actually uses.
Establishes: That OpenAI's GPT-4.5 System Card measures "hallucination" with PersonQA, NOT SimpleQA. Its Table 4 "Hallucination Evaluations" reports PersonQA accuracy (GPT-4o 0.50, o1 0.55, GPT-4.5 0.78) and PersonQA hallucination rate (0.30, 0.20, 0.19). The widely-cited "GPT-4.5 SimpleQA 62.5% / 37.1%" figure does NOT come from this system card's hallucination section; it comes from OpenAI's simple-evals leaderboard (see next source). This corrects a likely misattribution.
Paraphrase:  §3.1.3 uses PersonQA (facts about people) as the hallucination probe, with accuracy and "hallucination rate (lower is better)." The intro frames GPT-4.5 as having "fewer hallucinations" and says scaling unsupervised learning "decreases hallucination rates."
Locators:    §3.1.3 and Table 4 (p.4); Introduction (p.1).
Quote:       "PersonQA is a dataset of questions and publicly available facts about people that measures the model's accuracy on attempted answers... We consider two metrics: accuracy... and hallucination rate."
```

```text
URL:         https://github.com/openai/simple-evals
Kind:        primary — OpenAI's repository that hosts the SimpleQA dataset and the grader, and publishes the leaderboard. Owns the deployed dataset/grader and the reported leaderboard scores.
Establishes: Where the dataset and grader live, and the SimpleQA overall-correct leaderboard figures that circulated at model launches, including the GPT-4.5 number.
Paraphrase:  README describes SimpleQA as "Measuring short-form factuality in large language models," links the OpenAI release post, MIT-licensed. SimpleQA leaderboard column (overall correct): gpt-4.5-preview-2025-02-27 = 62.5; o3 = 49.4; o3-high = 48.6; o1 = 42.6; o1-preview = 42.4; gpt-4o-2024-11-20 = 38.8; Claude 3.5 Sonnet = 28.9.
Locators:    README benchmark table and SimpleQA entry.
Quote:       "Measuring short-form factuality in large language models."
```

```text
URL:         https://arxiv.org/abs/2412.19437  (DeepSeek-V3 Technical Report; PDF read directly)
Kind:        primary — a different lab (DeepSeek-AI) self-reporting a SimpleQA score in its own model card. Each lab owns the number it reports.
Establishes: That an outside lab adopts SimpleQA as a factuality benchmark, reports its own overall-correct score, and uses the same simple-evals grading. Shows the raw-percent gap between open and closed models on English facts, and that a lab can trade English-fact coverage for another axis (Chinese facts).
Paraphrase:  DeepSeek-V3 reports SimpleQA (Correct) = 24.9, and in the same Table 6 comparison GPT-4o-0513 = 38.2 and Claude-3.5-Sonnet-1022 = 28.4. The report states it "trails behind GPT-4o and Claude-Sonnet-3.5 in English factual knowledge (SimpleQA)" while surpassing them on Chinese SimpleQA (C-SimpleQA Correct: DeepSeek-V3 64.8 vs GPT-4o 59.3). For SimpleQA the report "adopt[s] the evaluation prompts from the simple-evals framework" and cites OpenAI's "Introducing SimpleQA" post as the source.
Locators:    Abstract (factuality summary); Evaluation Configurations; Table 6 "SimpleQA (Correct)" and "C-SimpleQA (Correct)" rows; post-training discussion.
Quote:       "While it trails behind GPT-4o and Claude-Sonnet-3.5 in English factual knowledge (SimpleQA), it surpasses these models in Chinese factual knowledge (Chinese SimpleQA)."
```

```text
URL:         https://www.abc.net.au/news/science/2025-03-20/openai-generative-ai-hallucinations-chatbot-gpt45-test/105041122
Kind:        secondary — ABC Science (Ellen Phiddian, 20 Mar 2025) reporting on OpenAI's numbers from outside. This is the misled-case exhibit.
Establishes: That a SimpleQA incorrect rate is reported to a general audience as a plain "hallucination rate" ("hallucinated 37 per cent of the time"), which is the exact misreading the article warns against. Notably, this piece also carries the correct caveats, so it is a good teaching contrast rather than a pure error.
Paraphrase:  Reports "OpenAI ran GPT-4.5 through the quiz, finding it hallucinated 37 per cent of the time," and "The next most recent GPT model, GPT-4o, hallucinated 62 per cent of the time" — i.e., the SimpleQA incorrect shares restated as raw hallucination frequencies. It does explain the adversarial construction ("added questions to the final SimpleQA list if at least one of the models got the answer wrong") and quotes an academic (Daswin de Silva) that the eval "is flawed from the start... It's only testing for short, fact-based queries and that's not really the first-use case for ChatGPT."
Locators:    Body paragraphs on the SimpleQA run and the expert critique.
Quote:       "OpenAI ran GPT-4.5 through the quiz, finding it hallucinated 37 per cent of the time." / "It's only testing for short, fact-based queries and that's not really the first-use case for ChatGPT."
```

```text
URL:         https://www.aimon.ai/posts/the-llm-unleaderboard-self-reported-hallucination-accuracy-top-models/
Kind:        secondary — AIMon (Puneet Anand, Jun/Aug 2025) compiling self-reported SimpleQA scores across labs. Context, not an owner of any number.
Establishes: That SimpleQA scores are pulled from model cards across labs and compared side by side, and that doing so is risky. Also that Google reports SimpleQA in Gemini cards while, per this compilation, Anthropic does not report SimpleQA in its own cards.
Paraphrase:  Compiles SimpleQA figures it attributes to model cards: OpenAI o1 47% acc / 44% halluc.; o3 49% / 51%; o4-mini 20% / 79%; GPT-4.5 62.5% / 37.1%; GPT-5 (main) 46% / 47%; Google Gemini 1.5 Pro 24.9% acc, Gemini 2.0 Flash 29.9% acc; Anthropic — none reported. Warns that "Relying solely on public scores like TruthfulQA or SimpleQA creates a false sense of readiness." Groups SimpleQA with TruthfulQA and PersonQA as "factuality/hallucination" benchmarks — itself part of the conflation the lesson should untangle.
Locators:    Self-reported-scores table and the readiness caution.
Quote:       "Relying solely on public scores like TruthfulQA or SimpleQA creates a false sense of readiness."
```

### Gated / not directly readable

```text
URL:         https://openai.com/index/introducing-simpleqa/
Kind:        primary (the release post) — gated: HTTP 403 on fetch; not read off the page.
Establishes: (intended) the 30 October 2024 release date and OpenAI's hallucination framing.
Status:      I could not load the page (403, a gating response, not a dead link). Its substance is fully duplicated by the SimpleQA paper, which I read in full; the 30 October 2024 date and the "hallucinations" framing are corroborated by multiple search results and by the DeepSeek-V3 report's citation of this URL, but I am not citing any claim as read from this page. Any article claim that rests only on the blog should be sourced to the paper instead.
```

## Contradictions

- **The "same" model scores differently across sources — snapshots and evaluators differ.** GPT-4o SimpleQA overall-correct appears as 38.2 (SimpleQA paper, Table 3), 0.38 (o1 System Card), 38.8 (simple-evals, gpt-4o-2024-11-20), and 38.2 (DeepSeek-V3 report, GPT-4o-0513). "Claude 3.5 Sonnet" appears as 28.9 (paper / simple-evals, the 2024-06-20 snapshot) and 28.4 (DeepSeek-V3, the -1022 snapshot). o1-preview is 42.7 (paper) vs 42.4 (simple-evals). These are small differences from different model dates and different runs, not disagreements about the benchmark. They matter for the article only as a caution against treating a single SimpleQA figure as exact.
- **"Hallucination rate" vs "incorrect rate."** OpenAI's o1 System Card names the SimpleQA incorrect share a "hallucination rate," and ABC restates it as how often the model "hallucinated." The SimpleQA paper never uses "hallucination rate" as a metric; its metric is percent incorrect on adversarially-selected questions. This is the core tension the commission is about, and it is a genuine cross-source framing conflict, recorded here rather than resolved silently.
- **Which benchmark carries GPT-4.5's "hallucination" claim.** The GPT-4.5 System Card's hallucination section uses PersonQA (0.19 hallucination rate), while the SimpleQA "37.1%" attached to GPT-4.5 comes from the simple-evals leaderboard (62.5% correct). Coverage that says the GPT-4.5 card shows a 37% SimpleQA hallucination rate is conflating two different tables. The article should attribute the 62.5% / 37.1% to simple-evals, not to the system card's hallucination section.
- **No contradiction to the adversarial-selection or abstention-scoring claims.** Searched for a primary source describing SimpleQA questions as a representative fact sample or the raw percent as a general accuracy rate; none found. The paper is explicit that questions are adversarially selected and that abstention is scored apart from error.

## Numbers

```text
Figure: 4,326 questions
Owner:  SimpleQA paper (also stated in simple-evals and the release post)
Scope:  Total questions in the SimpleQA dataset.
```

```text
Figure: "at least one of four completions must be incorrect" for a question to be kept
Owner:  SimpleQA paper §2.1
Scope:  The adversarial inclusion rule; four completions from GPT-4-class models (one switched to GPT-3.5 late in collection).
```

```text
Figure: ~94.4% third-trainer agreement; estimated benchmark error rate ~3%
Owner:  SimpleQA paper §2.2
Scope:  1,000-example re-answer check by a third trainer, graded by the ChatGPT autograder; after manual review the authors estimate a ~3% label error rate.
```

```text
Figure: grader disagreement — 2 of 300 completions
Owner:  SimpleQA paper §2.4
Scope:  Manual read of 100 correct + 100 incorrect + 100 not-attempted; only two disagreements with the prompted grader. (No formal grader study was done.)
```

```text
Figure: F-score = 2c / (2c + 2i + n)
Owner:  SimpleQA paper §2.4 / Appendix B
Scope:  Single-number metric; c=correct, i=incorrect, n=not attempted; harmonic mean of overall-correct and correct-given-attempted. Rewards guessing above 50% confidence (noted limitation).
```

```text
Figure: SimpleQA Table 3 (paper) — Correct / Not attempted / Incorrect / Correct-given-attempted / F-score
Owner:  SimpleQA paper §3, Table 3
Scope:  Claude-3-haiku 5.1 / 75.3 / 19.6 / 20.6 / 8.2; Claude-3-sonnet 5.7 / 75.0 / 19.3 / 22.9 / 9.2; Claude-3-opus 23.5 / 39.6 / 36.9 / 38.8 / 29.3; Claude-3.5-sonnet (2024-06-20) 28.9 / 35.0 / 36.1 / 44.5 / 35.0; GPT-4o-mini 8.6 / 0.9 / 90.5 / 8.7 / 8.6; GPT-4o 38.2 / 1.0 / 60.8 / 38.0 / 38.4; o1-mini 8.1 / 28.5 / 63.4 / 11.3 / 9.4; o1-preview 42.7 / 9.2 / 48.1 / 47.0 / 44.8. (All percent. Note how Claude models abstain far more than GPT-4o: Claude-3.5-sonnet not-attempted 35.0% vs GPT-4o 1.0%, which is why their F-scores end up close despite very different correct rates.)
```

```text
Figure: o1 System Card Table 3 — SimpleQA accuracy / hallucination rate
Owner:  OpenAI o1 System Card
Scope:  GPT-4o 0.38 / 0.61; o1 0.47 / 0.44; o1-preview 0.42 / 0.44; GPT-4o-mini 0.09 / 0.90; o1-mini 0.07 / 0.60. "hallucination rate" = SimpleQA incorrect share (lower is better).
```

```text
Figure: simple-evals SimpleQA leaderboard (overall correct)
Owner:  OpenAI simple-evals repo
Scope:  gpt-4.5-preview-2025-02-27 62.5; o3 49.4; o3-high 48.6; o1 42.6; o1-preview 42.4; gpt-4o-2024-11-20 38.8; Claude 3.5 Sonnet 28.9.
```

```text
Figure: DeepSeek-V3 SimpleQA (Correct) = 24.9
Owner:  DeepSeek-V3 Technical Report, Table 6
Scope:  Same table: GPT-4o-0513 38.2, Claude-3.5-Sonnet-1022 28.4. English overall-correct via simple-evals prompts. C-SimpleQA (Correct): DeepSeek-V3 64.8 vs GPT-4o 59.3.
```

```text
Figure: TruthfulQA — 817 questions, 38 categories; best model truthful on 58% vs 94% for humans
Owner:  TruthfulQA paper (Lin, Hilton, Evans)
Scope:  Imitative-falsehood benchmark; the contrast quantity for Background. Not a SimpleQA number.
```

## Source assets

```text
Asset: Table 3, "Performance of various models on SimpleQA" (SimpleQA paper, p.7)
Shows: The five-column breakdown — correct, not attempted, incorrect, correct-given-attempted, F-score — for each model. It makes abstention visible: Claude models sit in the high-70s for not-attempted while GPT-4o is near 1%, which is the whole reason correct-given-attempted and F-score exist.
Crop:  Keep the column headers and at least the GPT-4o and Claude-3.5-sonnet rows so the not-attempted contrast is legible. Do not crop away the "Not attempted" column — it carries the lesson.
```

```text
Asset: Figure 2, calibration plots (SimpleQA paper, p.8)
Shows: Left — stated-confidence vs accuracy, with every model's curve below the y=x line (models overstate confidence). Right — answer-frequency vs accuracy. Demonstrates the "know what they know" purpose behind the not-attempted grade.
Crop:  The left panel alone carries the overconfidence point; keep the y=x reference line and axis labels.
```

```text
Asset: Table 2, grading categories with example completions (SimpleQA paper, p.5)
Shows: The exact correct / incorrect / not-attempted definitions with worked example answers to one question. Good for teaching how a hedged wrong answer counts as incorrect and an honest "I don't know" counts as not-attempted.
Crop:  Retain all three rows and the example question caption; the three-way distinction only makes sense together.
```

```text
Asset: Table 3, "Hallucination Evaluations" (o1 System Card, p.5)
Shows: SimpleQA presented with an "accuracy" row and a "hallucination rate (lower is better)" row — the relabeling at its source. This is the primary exhibit for the misled case.
Crop:  Keep the "hallucination rate" label and the SimpleQA rows; that label beside a SimpleQA score is the point.
```

## Discarded

```text
URL: https://arxiv.org/abs/2509.07968 (SimpleQA Verified, a later Google DeepMind reliability revision) — out of scope for a lesson on the original SimpleQA; a follow-up benchmark, not this number's origin.
URL: https://arxiv.org/abs/2411.07140 (Chinese SimpleQA) — a separate Chinese-language benchmark; relevant only as a passing note, not a primary for this commission.
URL: https://medium.com/@aiintransit/openais-new-qa-benchmark-simpleqa-... — secondary summary that adds nothing the paper does not own; not needed.
URL: https://felo.ai/blog/felo-simpleqa-accuracy/ and https://www.tavily.com/blog/tavily-...-sota-on-simpleqa-... — vendor posts claiming SimpleQA SOTA for their own retrieval products; promotional, and they illustrate (rather than reliably source) the "high SimpleQA = generally accurate" misreading.
URL: https://www.kaggle.com/benchmarks/openai/simpleqa — a leaderboard mirror; superseded by the simple-evals repo, which owns the data.
```
