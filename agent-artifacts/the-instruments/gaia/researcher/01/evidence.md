# Evidence: the-instruments/gaia (01)

The evidence supports the full mechanics of a GAIA score. The paper owns the
question count (466), the three-level split (146 / 245 / 75), the quasi-exact-match
grading rule against one reference answer, the format instruction that grading
depends on, the 166-released / 300-withheld design, and the release-time baselines
(92% for annotators, 15% for GPT-4 with plugins). Hugging Face owns the leaderboard
and now scores only the withheld test set. The misleading case is well documented:
OpenAI announced Deep Research on 2 February 2025 as "a new state of the art" on
GAIA at 67.36% on the public validation set, and that figure was read and repeated
as a general leaderboard result even though the validation answers are public and
the ranked leaderboard runs on the withheld test set. Two parties in a position to
know confirm the validation set is exposed: the GAIA authors, who withhold the test
answers precisely because public answers leak into pretraining, and H2O.ai, a
leaderboard participant, which states the validation set carries "known data leaks"
while the test set has none. The concrete cost is a cross-set comparison that does
not hold: a system reported at 67% on validation and a system reported at 75% on
test were treated as directly comparable, and JD's own JoyAgent report shows the
same system scoring 75.2 on validation and 67.1 on test.

The record is thin in two places. First, current live leaderboard standings could
not be verified against a source I could open on the reading date, 10 September
2026: the leaderboard Space renders its table client-side, the dataset viewer is
gated (HTTP 401), and the third-party aggregators that list current numbers are
unreliable. I anchor recent test-set
numbers to primary system reports (H2O 75%, JoyAgent 67.1) with their dates rather
than to a live ranking. Second, the paper's per-level baseline table does not state
plainly whether GPT-4 and human scores are computed over all 466 questions or the
166-question developer set; the headline aggregates (92%, 15%) are firm, the
per-level denominator is not separately confirmed.

## Sources

```text
URL:         https://arxiv.org/abs/2311.12983
Kind:        primary. The benchmark's own paper; it owns every construction, grading, and baseline figure. Full text read at https://arxiv.org/html/2311.12983v1.
Establishes: What GAIA is, its counts, its grading rule, its split design, and its release-time human and model scores.
Paraphrase:  GAIA is a benchmark of real-world questions requiring reasoning, multimodality, web browsing, and tool use. The authors devise 466 questions with answers, release 166 as a developer set and withhold answers to the other 300 to power a Hugging Face leaderboard. Grading is a quasi-exact match against one ground-truth answer, with normalization by answer type. Human annotators score 92% aggregated; GPT-4 with plugins scores 15%.
Locators:    Abstract; Section 3 (dataset and levels); Section on evaluation/scoring; results tables.
Quote:       "we show that human respondents obtain 92% vs. 15% for GPT-4 equipped with plugins." / "Using GAIA's methodology, we devise 466 questions and their answer. We release our questions while retaining answers to 300 of them to power a leader-board." / "evaluation is done via quasi exact match between a model's answer and the ground truth (up to some normalization that is tied to the 'type' of the ground truth)." / "YOUR FINAL ANSWER should be a number OR as few words as possible OR a comma separated list of numbers and/or strings." / "We release a developer set of 166 annotated questions and release the remaining 300 questions without annotations." / "we estimate the annotator's success rate to be 92% when aggregated on all levels of difficulty, and report this as the human score for GAIA."
```

```text
URL:         https://huggingface.co/datasets/gaia-benchmark/GAIA
Kind:        primary. The dataset card published by the benchmark's own org; it owns the distributed data and its gating terms.
Establishes: Hugging Face hosts and gates the data; three levels; the test set answers are private; users agree not to reshare.
Paraphrase:  The dataset holds more than 450 questions across three levels, split into a public development set and a test set whose answers and metadata are private. Access is gated, and users agree not to reshare the data outside a gated or private repository to prevent leakage into training data. The card links the leaderboard.
Locators:    Dataset card body; gating notice.
Quote:       Users "agree to not reshare this dataset outside of a gated or private repository on the HF hub."
```

```text
URL:         https://huggingface.co/spaces/gaia-benchmark/leaderboard
Kind:        primary. The leaderboard operator's own Space; its configuration file states how submission and scoring work. Read the file at .../blob/main/content.py.
Establishes: Who runs the leaderboard, that it now scores the test set only, and the submission and scoring procedure.
Paraphrase:  The public leaderboard is restricted to the test set; the validation leaderboard was closed. Scores are the percentage of correct answers for a split. Grading uses quasi-exact match with normalization by answer type. A submission is a JSON-lines file of task ids, model answers, and optional reasoning traces, with the scoring function available in the repository. The citation names Mialon, Fourrier, Swift, Wolf, LeCun, and Scialom (2023).
Locators:    content.py INTRODUCTION, submission-guide, and CITATION strings.
Quote:       "Scores are expressed as the percentage of correct answers for a given split." Submissions "restricted to the test set only" (validation leaderboard closed).
```

```text
URL:         https://h2o.ai/blog/2025/h2o-ai-tops-the-general-ai-assistant-test/
Kind:        primary. H2O.ai's own report of its own result; it owns the 75% test-set claim and the cross-set comparison it draws.
Establishes: A participant's 75% test-set score, its claim to the top spot, and its explicit statement that rivals were scored on validation with known leaks.
Paraphrase:  On 17 March 2025 H2O.ai reports its h2oGPTe Agent at 75% on the GAIA test set, claims the number-one spot, and calls it the first grade of C on the test set. It places itself ahead of OpenAI Deep Research and level with Manus, and states that Deep Research and Manus were evaluated on validation data while H2O's result is on the test set, which it describes as having no known data leaks.
Locators:    Headline; results paragraph; comparison paragraph.
Quote:       "our h2oGPTe Agent has once again claimed the #1 spot on the prestigious GAIA (General AI Assistants) benchmark with an impressive 75% accuracy rate." / "while OpenAI Deep Research and Manus were evaluated on validation data, our results are evaluated on the test set data, a more rigorous and extensive evaluation involving nearly double the number of questions with no known data leaks." / "This achievement places us ahead of OpenAI's Deep Research while matching the performance of newcomer Manus."
```

```text
URL:         https://openai.com/index/introducing-deep-research/
Kind:        primary. OpenAI's own announcement; it owns the "state of the art on GAIA" claim. The page returns HTTP 403 to automated fetch (gated, not dead) and the CDN PDF is image-based; the figure below is taken from the Hugging Face writeup that reports it, recorded as secondary.
Establishes: The origin of the widely repeated "SOTA on GAIA" claim, dated 2 February 2025.
Paraphrase:  OpenAI announces Deep Research on 2 February 2025 and states it reaches a new state of the art on GAIA, topping the external leaderboard. The reported figure is 67.36% on the validation set (see the Hugging Face source for the read value).
Locators:    "Introducing deep research," 2 February 2025; GAIA/benchmarks section.
Quote:       Not read firsthand (gated). Figure verified via the Hugging Face open-deep-research post.
```

```text
URL:         https://arxiv.org/abs/2510.00510
Kind:        primary. JD's JoyAgent-JDGenie technical report; it owns its own validation and test scores. Read at https://arxiv.org/html/2510.00510v1.
Establishes: A single system's own validation-versus-test gap, which shows the two sets are not interchangeable.
Paraphrase:  The report (Jiarun Liu, Shiyue Xu and colleagues; JD team with Haofen Wang of Tongji University) reports GAIA validation pass@1 of 75.2 and pass@3 of 82.4, and test pass@1 of 67.1. The same system scores about eight points lower on the withheld test set than on the public validation set at pass@1.
Locators:    Section 4.2 results; Table 1.
Quote:       Validation pass@1 75.2, pass@3 82.4; test pass@1 67.1.
```

```text
URL:         https://huggingface.co/blog/open-deep-research
Kind:        secondary. Hugging Face's engineering post reporting on OpenAI's result and its own reproduction. Near-authoritative for this number because its authors include Clémentine Fourrier, a GAIA co-author who maintains the leaderboard, but it reports OpenAI's figure rather than owning it.
Establishes: The read value of OpenAI Deep Research's GAIA score and the split it was measured on, plus that open reproductions also report validation numbers.
Paraphrase:  The post states OpenAI Deep Research reached near 67% correct on one-shot on average and 47.6% on level 3, on the GAIA validation set, and that Hugging Face's own open reproduction reached 55.15% on the same validation set. Authors include Aymeric Roucher, Thomas Wolf, and Clémentine Fourrier.
Locators:    Opening framing; results paragraph.
Quote:       "they successfully reached near 67% correct answers on 1-shot on average, and 47.6% on especially challenging 'level 3' questions." / "our current performance of 55.15% on the validation set."
```

```text
URL:         https://towardsdatascience.com/gaia-the-llm-agent-benchmark-everyones-talking-about/
Kind:        secondary. An explainer by Shuai Guo, 29 May 2025. Reports on the benchmark from outside the authoring team.
Establishes: Reception of the validation-versus-test distinction and an estimate of ground-truth error.
Paraphrase:  The piece warns that validation questions and answers are widely available online, so models may have memorized them, and frames the public set as an open-book exam against the test set's closed exam. It states that about 5% of GAIA data, across both splits, contains errors or ambiguities in the ground-truth answers.
Locators:    Sections on validation-versus-test and on data quality.
Quote:       "The questions and answers for the validation set are widely available online. So it is highly likely that the models might have 'memorized' them during their training rather than deriving solutions from genuine reasoning." / "About 5% of the GAIA data (across both validation and test sets) contains errors/ambiguities in the ground truth answers."
```

```text
URL:         https://arxiv.org/abs/2510.11977
Kind:        secondary. The Holistic Agent Leaderboard (Sayash Kapoor, Arvind Narayanan and colleagues, Princeton and others). Reports on agent evaluation across nine benchmarks including GAIA. Read at https://arxiv.org/html/2510.11977v1.
Establishes: That a recent, independent agent-evaluation effort uses GAIA as a standard web-search-plus-reasoning benchmark and raises no GAIA-specific integrity concern. Included so the writer does not overstate a consensus that the benchmark is broken.
Paraphrase:  The paper lists GAIA among its benchmarks as combining web search with reasoning for complex questions and reports prior GAIA evaluations in a table. It does not single out GAIA for overfitting, gaming, or contamination.
Locators:    Section 3 (experimental setup); Table 1.
Quote:       "GAIA (Mialon et al., 2023) Combine web search with reasoning for complex questions."
```

## Contradictions

- Split counts. The paper states 166 released and 300 withheld (466 total). The
  distributed Hugging Face dataset is commonly cited as 165 validation and 301 test
  (also 466). The one-question difference could not be confirmed against the dataset
  viewer, which is gated (HTTP 401). Attribute 166 / 300 to the paper and treat the
  165 / 301 reading as the shipped dataset's split, unverified here.

- The benchmark is not broadly accused of being broken. The Holistic Agent
  Leaderboard uses GAIA as a routine benchmark and raises no integrity flag. The
  documented problem is narrower: comparing a validation figure against a test
  figure, and the public validation set's exposure to memorization. The writer
  should not generalize the misleading case into a claim that GAIA measures nothing.

- "Beats humans" does not hold on the test set at the dates checked. The human
  baseline is 92%. The highest verified test-set figure in this record is H2O's 75%
  (March 2025). Validation figures approach or exceed 90% in some reports, which is
  the reading that feeds a "beats humans" headline, but that number is on the
  contamination-exposed set, not the ranked test set.

- The human 92% is an annotator success rate, not a strict human ceiling. The
  paper reports it as the annotators' own rate, with web and tool access, taking
  roughly 6 to 17 minutes to answer a question. It is not a casual, tool-free human.

## Numbers

```text
Figure: 466 questions total
Owner:  GAIA paper (arXiv:2311.12983)
Scope:  Full benchmark, all three levels
```

```text
Figure: Level 1 = 146, Level 2 = 245, Level 3 = 75
Owner:  GAIA paper (arXiv:2311.12983), full text
Scope:  Full benchmark; sums to 466. Level 1 = no tool or one tool, up to ~5 steps; Level 2 = roughly 5 to 10 steps combining tools; Level 3 = arbitrarily long sequences, any number of tools.
```

```text
Figure: 166 released (developer set) / 300 withheld (test)
Owner:  GAIA paper (arXiv:2311.12983)
Scope:  Full benchmark. Answers to the 300 power the leaderboard. Shipped dataset commonly cited as 165 / 301 (unverified here).
```

```text
Figure: Human (annotator) score = 92% aggregated
Owner:  GAIA paper (arXiv:2311.12983)
Scope:  Annotator success rate across all levels. Per-level as reported: L1 94%, L2 92%, L3 87%. Denominator (full set vs developer set) not separately confirmed.
```

```text
Figure: GPT-4 with plugins = 15% overall
Owner:  GAIA paper (arXiv:2311.12983), abstract
Scope:  Release-time baseline. Per-level as reported: L1 30.3%, L2 9.7%, L3 0%. Weighted by the level counts this reconciles to ~15%.
```

```text
Figure: GPT-4 (no plugins) = L1 9.1%, L2 2.6%, L3 0%; AutoGPT = L1 14.4%, L2 0.4%, L3 0%
Owner:  GAIA paper (arXiv:2311.12983), results table
Scope:  Release-time baselines. GPT-4 without an agentic setup stays under ~7% overall.
```

```text
Figure: OpenAI Deep Research = 67.36% (near 67% one-shot average; 47.6% on Level 3)
Owner:  OpenAI announcement, 2 Feb 2025 (claim); read value via Hugging Face open-deep-research post
Scope:  GAIA validation set. Reported as a new state of the art on GAIA.
```

```text
Figure: Hugging Face open reproduction = 55.15%
Owner:  Hugging Face open-deep-research post
Scope:  GAIA validation set.
```

```text
Figure: h2oGPTe Agent = 75%
Owner:  H2O.ai blog, 17 Mar 2025
Scope:  GAIA test set. Claimed number-one spot and first "grade of C" on the test set.
```

```text
Figure: JoyAgent-JDGenie = validation pass@1 75.2, pass@3 82.4; test pass@1 67.1
Owner:  JoyAgent-JDGenie technical report (arXiv:2510.00510)
Scope:  Same system, both splits; about 8 points lower on the test set at pass@1.
```

```text
Figure: ~5% of GAIA data has erroneous or ambiguous ground-truth answers
Owner:  Towards Data Science explainer (Shuai Guo), 29 May 2025
Scope:  Both splits. Single-source estimate; not confirmed against a benchmark-owner statement.
```

## Source assets

```text
Asset: The results table in the GAIA paper listing human 92% and model scores by level (arXiv:2311.12983).
Shows: The size of the release-time gap between the annotator baseline and the best model, level by level, in one view.
Crop:  Retain the human row and the GPT-4-with-plugins and AutoGPT rows with their level columns and the overall figures. Omit any rows for configurations the lesson does not name.
```

```text
Asset: The level-definition description in the GAIA paper (steps and tools per level).
Shows: What separates Level 1 from Level 3 in concrete terms a reader can hold.
Crop:  Retain the three level definitions verbatim; the surrounding prose is not needed.
```

```text
Asset: The comparison paragraph in the H2O.ai blog naming validation vs test for rival systems.
Shows: A participant stating in its own words that scores were measured on different sets, which is the misleading case in one primary sentence.
Crop:  Retain the sentence contrasting validation and test and the "no known data leaks" clause. Omit surrounding marketing.
```

```text
Asset: None found for the live leaderboard standings.
Shows: The Space renders its table client-side and did not return standings to any tool available here; no static image of a current ranking was verified.
Crop:  n/a.
```

## Discarded

```text
URL: https://leaderboard.steel.dev/leaderboards/gaia/ — claims a current leader ("OPS-Agentic-Search 92.36%") but is a third-party aggregator whose figure could not be verified against the benchmark's own leaderboard; do not cite the number.
```

```text
URL: https://benchlm.ai/benchmarks/gaia and https://rapidclaw.dev/blog/gaia-benchmark-leaderboard-2026 — aggregator pages reading as machine-generated; no primary standing verified; rejected.
```

```text
URL: https://qaskills.sh/blog/gaia-benchmark-ai-agents-explained-2026 — third-party explainer; adds nothing the paper or the Hugging Face pages do not own firsthand.
```

```text
URL: https://datasets-server.huggingface.co/rows?dataset=gaia-benchmark/results_public... — a fetch/API endpoint, not a source page, and it returned 404; not recorded as a citable address.
```

```text
URL: https://arxiv.org/pdf/2311.12983 and https://cdn.openai.com/API/docs/deep_research_blog.pdf — the document binaries themselves, not separate sources; the paper was read via its HTML rendering and the OpenAI figure via the Hugging Face post. Recorded here only to note the PDFs were not text-extractable in this environment.
```

Production record: written by Claude Opus 4.8 (claude-opus-4-8), effort=high.
