# Evidence record: the-instruments/big-bench-hard (01)

The evidence supports the commissioned angle on every load-bearing point. The
collaborative construction of BIG-bench (204 tasks, 450 authors, 132
institutions), the 23-task BBH selection rule (tasks where no prior model beat
the average human-rater), the exact chain-of-thought-vs-direct gains, and the
saturation/contamination story are all anchored to primaries read firsthand: the
BIG-bench paper, the BBH paper, the GPT-4 technical report, the BBEH paper, the
BIG-bench repository, and the Claude 3 model card. Two findings sharpen the angle
rather than confirm the naive version of it. First, the "average human-rater"
bar is the mean over a small, unspecified team of *expert* raters who were
allowed to use internet search, not a lay-person baseline, and BIG-bench itself
warns these are not the best achievable human scores. Second, "chain-of-thought
lifts models past the human bar" is model- and task-specific: on the 23-task
average, Codex-with-CoT (73.9%) clears the average human (67.7%) but PaLM-with-CoT
(65.2%) does not, even though PaLM-with-CoT surpasses the human bar on 10 of the
23 tasks individually. The record is thin on exactly one number the brief asked
for: the total count of human raters. BIG-bench's public text names "a team of
expert raters" and describes their protocol but never states how many people
they were or how many rated each task. That gap is itself reportable and does not
undermine the angle.

## Sources

```text
URL:         https://arxiv.org/abs/2206.04615
Kind:        primary. The BIG-bench paper (Srivastava et al., 2022), authored by
             the people who built the benchmark; it owns the task count,
             contributor count, and human-evaluation methodology.
Establishes: BIG-bench's size and collaborative construction, and how the human
             baseline was collected (the bar BBH later selects against).
Paraphrase:  BIG-bench consists of 204 tasks contributed by 450 authors across
             132 institutions, drawn from many fields and aimed at tasks
             believed beyond current models. A team of expert human raters
             performed the tasks to provide a baseline. The paper reports two
             human metrics per task: the mean score across raters and the max
             score across raters (a rater who did a task multiple times is
             averaged first). Raters were encouraged to use all available
             resources including internet search, spent 30 minutes to 2 hours
             per day over a period of weeks, and tasks were subsampled to fit
             the time window. The paper cautions these scores are not claimed to
             be the best achievable by a human.
Locators:    Abstract (204 tasks / 450 authors / 132 institutions); human-
             evaluation section (2.3.2 in the HTML) and Appendix E "Expert
             evaluation."
Quote:       "a team of human expert raters performed all tasks in order to
             provide a strong baseline." "the mean score on a task across all
             raters, and the max score on the task across all raters." "we
             encouraged evaluators to use all available resources (including
             internet search) when performing tasks." "We do not claim that
             these scores are the best possible achievable by a human."
```

```text
URL:         https://arxiv.org/abs/2210.09261
Kind:        primary. The BBH paper (Suzgun et al., 2022), authored by the team
             that defined BBH; it owns the 23-task rule and the CoT gains.
Establishes: The BBH selection rule, the human-rater bar, and the exact answer-
             only vs chain-of-thought scores that are the article's core numbers.
Paraphrase:  BBH is the 23 BIG-Bench tasks for which prior language-model
             evaluations did not outperform the average human-rater. The authors
             began from 209 BIG-Bench tasks, filtered to 78 clean multiple-choice
             or exact-match tasks with adequate examples and human baselines,
             found 36 where no previous model surpassed the average human-rater,
             then removed 13 extremely difficult domain-specific tasks, leaving
             23. Each task needed fewer than 103 examples (3 few-shot exemplars
             plus 100 for evaluation). "Answer-only" is standard 3-shot few-shot
             prompting; the authors also manually composed three chain-of-thought
             exemplars per task (3-shot CoT). Averaged over the 23 tasks: average
             human-rater 67.7%, max human-rater 94.4%; code-davinci-002 (Codex)
             56.6% answer-only and 73.9% CoT; PaLM 540B 52.3% answer-only and
             65.2% CoT. CoT lets PaLM surpass the average human-rater on 10 of 23
             tasks and Codex on 17 of 23 tasks.
Locators:    Abstract; task-selection section (Section 2 / filtering funnel);
             Table 2 (human and model averages).
Quote:       "23 challenging BIG-Bench tasks which we call BIG-Bench Hard (BBH).
             These are the task for which prior language model evaluations did
             not outperform the average human-rater." "applying chain-of-thought
             (CoT) prompting to BBH tasks enables PaLM to surpass the average
             human-rater performance on 10 of the 23 tasks, and Codex
             (code-davinci-002) to surpass the average human-rater performance on
             17 of the 23 tasks."
```

```text
URL:         https://arxiv.org/abs/2303.08774
Kind:        primary. The GPT-4 Technical Report (OpenAI, 2023); it owns
             OpenAI's own statement about BIG-bench contamination in GPT-4's
             training data.
Establishes: A sharp, dated contamination case: OpenAI found BIG-bench in GPT-4's
             training set and withheld the result.
Paraphrase:  During contamination checking OpenAI found that portions of
             BIG-bench had been inadvertently mixed into GPT-4's training set, and
             excluded it from reported results. The report publishes no BBH score
             for GPT-4.
Locators:    Benchmark-evaluation section covering the pre-trained base model.
Quote:       "During our contamination check we discovered that portions of
             BIG-bench were inadvertently mixed into the training set, and we
             excluded it from our reported results."
```

```text
URL:         https://arxiv.org/abs/2502.19187
Kind:        primary. The BIG-Bench Extra Hard paper (Kazemi et al., 2025); it
             owns the claim that BBH is saturated and the design of its
             replacement.
Establishes: Why BBH stopped discriminating between frontier models and had to
             be replaced.
Paraphrase:  Recent LLM advances led to saturation on BIG-bench and its harder
             version BBH; state-of-the-art models achieve near-perfect scores on
             many BBH tasks, diminishing its utility. The authors built BBEH by
             replacing each BBH task with a novel task probing similar reasoning
             but markedly harder. On BBEH the best general-purpose model scored
             9.8% and the best reasoning-specialized model 44.8%, showing how
             much headroom BBH had lost.
Locators:    Abstract.
Quote:       "State-of-the-art models achieve near-perfect scores on many tasks
             in BBH, thus diminishing its utility." "recent advances in LLMs have
             led to saturation on BIG-Bench, and its harder version BIG-Bench Hard
             (BBH)."
```

```text
URL:         https://github.com/google/BIG-bench
Kind:        primary. The official BIG-bench repository (Google); it owns the
             canary mechanism the benchmark ships to detect contamination.
Establishes: BIG-bench's own anti-contamination design, and the fact that its
             tasks live in a public web repository (the leakage vector).
Paraphrase:  Every task file, including README.md and task.json, contains a
             fixed "canary" string that must not be edited, so that benchmark
             tasks can be detected if they leak into web-scraped training data.
             The README describes more than 200 tasks and a 24-task BIG-bench
             Lite subset. The specific canary GUID is present in the files but is
             the artifact meant to be searched for, not quoted in prose.
Locators:    Repository README, canary-string instructions.
Quote:       "All task files (including `README.md` and `task.json`) contain a
             'canary' string, which should not be edited. This is to prevent
             benchmark tasks from leaking into web-scraped training data."
```

```text
URL:         https://www.anthropic.com/news/claude-3-family
             (model card PDF: https://www-cdn.anthropic.com/de8ba9b01c9ab7cbabf5c33b80b7bbc618857627/Model_Card_Claude_3.pdf)
Kind:        primary. The Claude 3 model card (Anthropic, 2024); it owns the
             published BBH figures and the evaluation setting, and is a concrete
             instance of the "X% on BBH" a reader meets.
Establishes: The anchor figure the reader has seen, with its CoT setting made
             explicit, plus the cross-report GPT-4 BBH number.
Paraphrase:  Table 1 reports BIG-Bench-Hard under the setting "3-shot CoT":
             Claude 3 Opus 86.8%, Claude 3 Sonnet 82.9%, Claude 3 Haiku 73.7%,
             GPT-4 83.1%, GPT-3.5 66.6%, Gemini 1.0 Ultra 83.6%, Gemini 1.5 Pro
             84.0%, Gemini 1.0 Pro 75.0%. Footnote 5 states Claude 3 models were
             evaluated using chain-of-thought prompting. Footnote 7 states the
             GPT-4 BBH figure (83.1%) was taken from the Gemini Technical Report,
             not OpenAI's own report.
Locators:    Table 1, "BIG-Bench-Hard" row; footnotes 3, 5, and 7.
Quote:       "BIG-Bench-Hard ... Mixed evaluations 3-shot CoT 86.8% 82.9% 73.7%
             83.1% 66.6% 83.6% 84.0% 75.0%." "Claude 3 models were evaluated
             using chain-of-thought prompting." "GPT-4 scores on MATH (4-shot
             CoT), MGSM, and Big Bench Hard were reported in the Gemini Technical
             Report."
```

```text
URL:         https://www.deeplearning.ai/the-batch/the-problem-with-benchmark-contamination-in-ai
Kind:        secondary. The Batch (DeepLearning.AI) reports on the contamination
             problem across benchmarks from outside the authoring parties.
Establishes: Context that benchmark contamination is a recognized, general
             problem, and that BIG-bench's canary string is a named detection
             method. Repetition supports that the concern is widely held, not
             that any specific figure is true.
Paraphrase:  The article frames contamination as test answers leaking into
             training data, inflating scores without real gains. It cites GSM8K
             models scoring up to ~10% higher than on held-out math sets, GPT-4
             reproducing material from AG News, WNLI, and XSum, and Codeforces
             performance dropping on post-2021 problems. It names BIG-bench's
             canary strings as one detection approach. It does not discuss GPT-4's
             BIG-bench exclusion or BBH specifically.
Locators:    Body, sections on detection and on specific benchmarks.
Quote:       "One approach is to embed canary strings -- unique markers within
             test datasets like BIG-bench -- that enable researchers to detect
             contamination."
```

```text
URL:         https://benchmarkingagents.com/bigbench-hard/
Kind:        secondary. A benchmark-explainer site reporting on BBH's protocol,
             scale, and saturation from outside the authoring parties.
Establishes: Context on BBH's standard protocol, its total example count, and
             frontier saturation; useful for the reader's orientation, not as the
             owner of any figure.
Paraphrase:  BBH spans 6,511 examples across the 23 tasks. The official protocol
             is 3-shot prompting with canonical CoT exemplars, and most published
             numbers use it. Frontier scores now exceed 90% (it cites Claude 3.5
             Sonnet at 93.1% per Anthropic's model card, and frontier models
             above 95% with CoT and majority vote from mid-2025), and for
             frontier comparisons other benchmarks (GPQA-Diamond, ARC-AGI-2,
             Humanity's Last Exam) discriminate better, while BBH remains useful
             for mid-tier and open-weight models. Treat the 93.1% and 6,511
             figures as secondary until confirmed against the owning model card /
             task files.
Locators:    Page body, protocol and saturation sections.
Quote:       "The official protocol is 3-shot prompting with canonical CoT
             exemplars." "Claude 3.5 Sonnet at 93.1%."
```

## Contradictions

- **Task count: 204 vs 209 vs "more than 200."** The BIG-bench paper's abstract
  reports 204 tasks. The BBH paper's filtering funnel begins from 209 "All
  BIG-Bench tasks." The BIG-bench README says "more than 200." Scope: 204 is the
  paper's headline count of accepted tasks; 209 is the number BBH's authors
  enumerated when starting to filter (task families and programmatic/JSON
  variants can be counted differently). The commission's "on the order of 200"
  is safe; if a single exact number is used, attribute it (204, BIG-bench paper)
  and note the BBH funnel started from 209.

- **GPT-4's BBH number: withheld by its owner, published by a rival.** OpenAI's
  GPT-4 Technical Report excluded BIG-bench because it was found in GPT-4's
  training data and reports no BBH score. Yet a GPT-4 BBH figure of 83.1%
  circulates in model cards (the Claude 3 card, which attributes it to Google's
  Gemini Technical Report). Same model, same benchmark: the party that trained
  the model withheld the number for contamination, and a third party published
  one anyway. This is the sharpest documented case of "reading a BBH percentage
  naively misses whether the tasks leaked."

- **"CoT beats humans" is not true on the 23-task average for every model.** The
  abstract's headline (CoT surpasses the average human-rater on 10/23 tasks for
  PaLM, 17/23 for Codex) is per-task. On the 23-task *average*, Codex-with-CoT
  (73.9%) clears the average human-rater (67.7%) but PaLM-with-CoT (65.2%) does
  not. A reader who hears "chain-of-thought beat humans on BBH" should know the
  claim is model- and task-dependent, and that it clears the *average* of the
  human raters, well below the *max* human-rater (94.4%).

- **What "average human-rater" means.** BBH selects against the *average* human-
  rater, which is the mean over BIG-bench's team of *expert* raters (not
  laypeople) who were permitted to use internet search. BIG-bench explicitly
  disclaims that its human scores are the best achievable. So "beats the average
  human" means beats the mean of a small expert team allowed to look things up,
  not beats a typical person, and it sits far below the max-human bar of 94.4%.

- **Codex CoT gain arithmetic.** The endpoint cells (Table 2) are answer-only
  56.6% and CoT 73.9%, a gain of 17.3 points. One automated read of a derived
  "gain" cell returned 16.7; the endpoint figures were consistent across
  independent reads, so the gain is 73.9 - 56.6 = 17.3. PaLM gain is 65.2 - 52.3
  = 12.9; InstructGPT (text-davinci-002) 68.4 - 51.8 = 16.6. Compute deltas from
  the endpoint cells rather than citing a gain column.

## Numbers

```text
Figure: 204 tasks
Owner:  BIG-bench paper (Srivastava et al., 2022), abstract
Scope:  Accepted tasks in the full BIG-bench benchmark. Cf. 209 "All BIG-Bench
        tasks" as BBH's filtering start; "more than 200" in the repo README.
```

```text
Figure: 450 authors across 132 institutions
Owner:  BIG-bench paper, abstract
Scope:  Contributors to the full benchmark as of the 2022 paper.
```

```text
Figure: 23 tasks (from 209 -> 78 clean -> 36 -> minus 13 -> 23)
Owner:  BBH paper (Suzgun et al., 2022), task-selection section
Scope:  Selection rule: tasks where no prior model surpassed the average human-
        rater, after removing multi-subtask / too-few-example / no-human-baseline
        / non-exact-match tasks and 13 extremely hard domain-specific tasks.
```

```text
Figure: average human-rater 67.7%; max human-rater 94.4%
Owner:  BBH paper, Table 2
Scope:  Mean over the 23 BBH tasks. "Average" = mean across BIG-bench's expert
        rater team; "max" = best single rater. Raters could use internet search.
```

```text
Figure: PaLM 540B 52.3% answer-only -> 65.2% CoT (+12.9)
Owner:  BBH paper, Table 2
Scope:  3-shot; averaged over 23 BBH tasks. CoT average still below 67.7% human
        average; surpasses human on 10/23 tasks individually.
```

```text
Figure: Codex (code-davinci-002) 56.6% answer-only -> 73.9% CoT (+17.3)
Owner:  BBH paper, Table 2
Scope:  3-shot; averaged over 23 BBH tasks. CoT average clears the 67.7% human
        average; surpasses human on 17/23 tasks individually.
```

```text
Figure: InstructGPT (text-davinci-002) 51.8% answer-only -> 68.4% CoT (+16.6)
Owner:  BBH paper, Table 2 (via first full-text read)
Scope:  3-shot; averaged over 23 BBH tasks.
```

```text
Figure: Claude 3 Opus 86.8% BBH (3-shot CoT); GPT-4 83.1%; GPT-3.5 66.6%;
        Sonnet 82.9%; Haiku 73.7%; Gemini 1.0 Ultra 83.6%; 1.5 Pro 84.0%;
        1.0 Pro 75.0%
Owner:  Claude 3 model card (Anthropic, 2024), Table 1, "BIG-Bench-Hard" row
Scope:  Setting labeled "3-shot CoT." GPT-4's 83.1% is sourced by the card from
        the Gemini Technical Report, not OpenAI's own report (which withheld BBH).
```

```text
Figure: BBEH best general-purpose model 9.8%; best reasoning model 44.8%
Owner:  BBEH paper (Kazemi et al., 2025), abstract
Scope:  Accuracy on the BBEH replacement benchmark, illustrating how much
        headroom frontier models had lost on saturated BBH.
```

```text
Figure: BBH ~6,511 examples across 23 tasks; frontier now >90% (Claude 3.5
        Sonnet 93.1%)
Owner:  benchmarkingagents.com (secondary); 93.1% attributed to Anthropic's
        Claude 3.5 model card
Scope:  Secondary; confirm the 6,511 count against the task files and the 93.1%
        against the Claude 3.5 model card before citing as fact.
```

## Source assets

```text
Asset: BBH paper, Table 2 (human average/max vs each model's answer-only and CoT
       averages over the 23 tasks).
Shows: The whole argument in one grid: direct answering leaves every model below
       the average human, chain-of-thought lifts Codex above it and PaLM close to
       it, and every model stays below the max-human 94.4%.
Crop:  Retain the two human-rater rows (avg 67.7%, max 94.4%) alongside the
       answer-only and CoT columns for at least Codex and PaLM. A committed
       chart-N.py rebuild (grouped bars: answer-only vs CoT per model, with two
       human reference lines) would serve better than a table screenshot and
       keeps axes labeled and the source cited.
```

```text
Asset: BBH paper, per-task chain-of-thought-vs-direct results (the task-level
       figure/appendix tables behind the "10 of 23" and "17 of 23" counts).
Shows: That the human-beating result is uneven across tasks, not a uniform lift.
Crop:  If used, keep enough tasks to show both wins and losses; do not crop to
       only the tasks where CoT wins.
```

```text
Asset: Claude 3 model card, Table 1, "BIG-Bench-Hard" row with its "3-shot CoT"
       setting label and footnotes 5 and 7.
Shows: A real "X% on BBH" the reader has seen, with the CoT setting and the
       cross-report GPT-4 sourcing visible.
Crop:  Must retain the "3-shot CoT" setting label and footnote 7 (GPT-4 figure
       from the Gemini report); cropping them off would present the numbers as
       directly comparable when the setting and provenance are the point.
```

```text
Asset: BIG-bench repository task file / README canary-string instruction.
Shows: The concrete anti-contamination mechanism and that BBH's tasks live in a
       public repo (the leakage vector). None found beyond the plain text; the
       canary GUID itself is a string, not a visual.
Crop:  None; quote the instruction rather than image it.
```

## Discarded

```text
URL: https://www.alignmentforum.org/posts/JbE7KynwshwkXPJAJ/anthropic-release-claude-3-claims-greater-than-gpt-4
     Secondary reproduction of the Claude 3 numbers; did not surface the BBH row
     cleanly and adds nothing over the primary model card, which was read
     directly. Not cited.
```

```text
URL: https://llm-stats.com/benchmarks/big-bench-hard and other live leaderboards
     Live, undated aggregations with unclear provenance and evaluation settings;
     current-frontier ranks change and are not needed. Saturation is anchored to
     the BBEH primary and the model-card trajectory instead.
```

```text
URL: General data-contamination survey/detection papers returned in search
     (e.g. arXiv:2310.18018, 2502.17521, 2410.03249)
     Real and on-topic, but the contamination case is already carried by two
     primaries specific to BIG-bench (the GPT-4 report's exclusion and the repo
     canary), which are sharper than a general survey. Held in reserve, not
     cited, to avoid padding.
```
