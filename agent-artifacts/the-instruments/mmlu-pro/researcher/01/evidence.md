# Evidence: the-instruments/mmlu-pro (01)

The record supports the commissioned angle firsthand. The MMLU-Pro paper owns every
construction and robustness figure the lesson needs: the pool it started from
(13,937 MMLU questions), the filtering, the expansion from four options to ten by
GPT-4-Turbo, the expert review, the final count (12,032 questions in 14
disciplines), the prompt-sensitivity drop (4-5% to about 2% across 24 prompt
styles), and the chain-of-thought advantage that flips sign versus MMLU (+19.1
points for GPT-4o). The original MMLU paper owns the four-option format, the
25% random baseline, and the 14,079-question test set that MMLU-Pro inherited.
Gema et al. owns the "misled" case: a measured 6.49% overall error rate in MMLU
and a worked ranking reversal (Llama 3.1 405B goes from rank 16 to rank 1 in
Virology once wrong keys are removed).

Where the record is thin, and where it complicates the angle: MMLU-Pro's guess-rate
fix is real but not uniform, because 17% of items carry fewer than ten options
(mean 9.47). Its composition shifted hard toward STEM (about 43% of items are newly
added from STEM websites, TheoremQA, and SciBench, and Math is now the single
largest discipline), so "MMLU-Pro" measures a different subject mix than MMLU, not
a strictly harder version of the same one. And the benchmark is saturating in 2026:
the live TIGER-Lab leaderboard now shows several models near 88%, with the top few
within a point, the same crowding that motivated MMLU-Pro in the first place. Two
sources caution the writer against reading small gaps as capability: the Llama 4
card reports MMLU-Pro under two settings that differ by roughly 18 points for the
same model, and Gupta et al. shows multiple-choice accuracy on MMLU (not tested on
MMLU-Pro) moves 6 to 27 points when answer order is shuffled. No source refutes the
core claim that ten options and the reasoning tilt did the work the paper reports.

## Sources

```text
URL:         https://arxiv.org/abs/2406.01574
Kind:        primary. Wang et al. authored MMLU-Pro; this document owns its
             construction, composition, and reported robustness numbers.
Establishes: What MMLU-Pro is, how each item is built and scored, and the paper's
             own before/after robustness figures against MMLU.
Paraphrase:  MMLU-Pro extends MMLU with harder, reasoning-focused questions and
             expands the choice set from four to ten options, removing trivial and
             noisy items. Accuracy drops 16% to 33% versus MMLU. Across 24 prompt
             styles, score sensitivity to the prompt falls from 4-5% in MMLU to
             about 2% in MMLU-Pro. Models using chain-of-thought beat direct
             answering on MMLU-Pro, reversing the MMLU finding.
Locators:    Abstract; Section 3 (construction); Section 5.1 and Table 2 (scores);
             Section 6.2 and Table 3 (CoT gap); Section 6.3 and Figure 5 (prompt
             sensitivity).
Quote:       "expanding the choice set from four to ten options... the sensitivity
             of model scores to prompt variations decreased from 4-5% in MMLU to
             just 2% in MMLU-Pro."
```

```text
URL:         https://arxiv.org/html/2406.01574v6
Kind:        primary. Full text of the same paper, used for the exact pipeline and
             composition tables.
Establishes: The step-by-step build and the per-discipline composition.
Paraphrase:  Starting pool: 13,937 MMLU questions. Initial filter removes items
             answered correctly by more than four of eight open-source models as
             "too easy," dropping 5,886 and leaving 8,051 from MMLU. Questions from
             STEM websites, TheoremQA, and SciBench are added; GPT-4-Turbo extracts
             short answers from their solutions. GPT-4-Turbo then expands options
             from four to ten with six "plausible distractors." Expert review runs
             in two phases: correctness verification, then Gemini-1.5-Pro re-checks
             every option to surface false negatives, followed by human review.
             Final set: 12,032 questions across 14 disciplines. Source mix: MMLU
             6,810 (56.60%), STEM website 4,083 (33.93%), TheoremQA 598 (4.97%),
             SciBench 541 (4.50%). Per discipline the largest is Math (1,351), then
             Physics (1,299), Chemistry (1,132), Law (1,101), Engineering (969).
             83% of items have ten options, 17% fewer, mean 9.47. The paper notes
             GPT-4-Turbo "does not gain additional advantage from such an
             augmentation procedure." GPT-4o leads Table 2 at 72.6% overall
             (5-shot CoT), ahead of Gemini-1.5-Pro (69.0%) and Claude-3-Opus (68.5%).
Locators:    Section 3.1 and 3.2 (pipeline, Figure 2); Table 1 (option/review
             stats); Table 5, Appendix A.1 (composition); Table 2 (leaderboard);
             Table 3 (CoT vs direct).
Quote:       "In our dataset, 83% have ten options, 17% have fewer, and the average
             options count per question is 9.47."
```

```text
URL:         https://arxiv.org/abs/2009.03300
Kind:        primary. Hendrycks et al. authored MMLU; this document owns MMLU's
             format, size, and scoring.
Establishes: What MMLU-Pro inherited and changed.
Paraphrase:  MMLU is 57 subjects of four-option multiple-choice questions grouped as
             Humanities, Social Science, STEM, and Other. Total collected 15,908,
             split into a 55-per-subject few-shot dev set, a 1,540-question
             validation set, and a 14,079-question test set. Score is classification
             accuracy averaged across examples and tasks; random chance is 25.0%.
             The best model at publication, few-shot GPT-3 175B, scored 43.9%
             overall against an estimated 89.8% expert level.
Locators:    Abstract; Section 3 (splits, subjects); Section 4.2 and Table 1
             (scoring, random baseline, GPT-3 result).
Quote:       "the test set has 14079 questions."
```

```text
URL:         https://arxiv.org/abs/2406.04127
Kind:        primary. Gema et al. authored the error analysis and MMLU-Redux; this
             document owns the MMLU error rate and the ranking reversals.
Establishes: The concrete case where an MMLU-family number misled: wrong answer
             keys and ambiguous items inflate or distort reported scores.
Paraphrase:  Manual re-annotation of MMLU finds numerous ground-truth errors. The
             current version estimates, by stratified sampling, that 6.49% of MMLU
             questions contain errors. In the Virology subset, 57% of analysed
             questions contain some error (33% wrong ground truth, 4% multiple
             correct answers, 14% unclear). The authors release MMLU-Redux, 5,700
             re-annotated questions across all 57 subjects (about 100 per subject),
             annotated by 14 experts under a five-type taxonomy. Removing erroneous
             items reorders models: in Virology, Llama 3.1 405B Instruct moves from
             0.57 (rank 16) on all items to 0.93 (rank 1) on correct items only.
Locators:    Abstract; Section 2.1 and Figure 2 (taxonomy); Section 3.1, Figure 3
             and Table 5 (error rates, Virology breakdown); Table 2 (ranking shifts).
Quote:       "we find that 57% of the analysed questions in the Virology subset
             contain errors... We estimate that 6.49% of MMLU questions contain
             errors."
```

```text
URL:         https://huggingface.co/datasets/TIGER-Lab/MMLU-Pro
Kind:        primary. The dataset owner's own card; it owns how MMLU-Pro is
             distributed, evaluated, and presently ranked.
Establishes: That the number is in live circulation, how it is scored today, and
             that MMLU-Pro is itself now saturating.
Paraphrase:  The card states 12,032 questions, 14 disciplines, ten options each,
             and recommends 5-shot chain-of-thought. It notes CoT can run 20% above
             direct scoring; GPT-4o falls from 0.7255 (CoT) to 0.5346 (direct). The
             live leaderboard (read 2026-08) shows top models near 88%: MiniMax-M2.1
             and Intern-S2-Preview at 88%, Qwen3.5-397B-A17B at 87.8%,
             DeepSeek-V4-Pro at 87.5%.
Locators:    Dataset card body (overview, "1. What's the difference..."), leaderboard
             table on the linked Space.
Quote:       "By increasing the distractor numbers, we significantly reduce the
             probability of correct guess by chance."
```

```text
URL:         https://github.com/meta-llama/llama-models/blob/main/models/llama4/MODEL_CARD.md
Kind:        primary. Meta's own model card; primary for "this lab reports these
             MMLU-Pro figures," not for whether the figures are comparable across labs.
Establishes: MMLU-Pro is a headline number labs now publish, and the reported value
             depends heavily on the evaluation setting.
Paraphrase:  The card reports MMLU-Pro twice. Pretrained models, 5-shot,
             macro_avg/em: Llama 4 Scout 58.2, Maverick 62.9. Instruction-tuned
             models, 0-shot, macro_avg/acc: Scout 74.3, Maverick 80.5. The same
             Maverick model reads 62.9 or 80.5 depending on the setting and stage.
Locators:    Benchmarks tables, "Pre-trained models" and "Instruction tuned models"
             rows for MMLU-Pro / MMLU Pro.
Quote:       "MMLU-Pro | 5 | macro_avg/em | 53.8 | 61.6 | 58.2 | 62.9" and
             "MMLU Pro | 0 | macro_avg/acc | 68.9 | 73.4 | 74.3 | 80.5".
```

```text
URL:         https://arxiv.org/abs/2406.19470
Kind:        primary. Gupta et al. authored this order-sensitivity study; primary
             for its own finding, which is about MMLU, not MMLU-Pro.
Establishes: Multiple-choice accuracy is sensitive to answer order, a format flaw
             adjacent to the prompt sensitivity MMLU-Pro measures. The record keeps
             this to caution the writer, not to claim MMLU-Pro is order-robust.
Paraphrase:  Shuffling answer options lowers accuracy on MMLU for every model tested.
             Llama-3-70B Instruct drops 6.2 points (80.3 to 75.3); Falcon-40B
             Instruct drops 27.2 points (54.7 to 39.8); math subcategories show the
             largest degradation. MMLU-Pro is not tested; the paper only cites it as
             concurrent work.
Locators:    Abstract; results section (per-model drops); related-work mention of
             MMLU-Pro. Scope confirmed firsthand: the study evaluates the original
             MMLU only and cites MMLU-Pro as concurrent work, not as a test subject.
Quote:       "all explored models decrease in accuracy on MMLU" (when answer order
             is shuffled).
```

```text
URL:         https://arxiv.org/abs/2409.02257
Kind:        primary. Taghanaki et al. authored MMLU-Pro+; primary for its own
             probe of shortcut behavior on MMLU-Pro-style items.
Establishes: Even on MMLU-Pro's format, strong models lean on answer-selection
             shortcuts rather than full reasoning. This complicates "MMLU-Pro
             measures reasoning" without refuting it.
Paraphrase:  MMLU-Pro+ adds questions with multiple correct answers to test whether
             models resist simplistic strategies. It defines a shortcut selection
             ratio and a correct pair identification ratio. GPT-4o and Qwen2-72B show
             the highest rates of staying on an originally chosen answer;
             Gemini-1.5-Pro, Claude-3.5-Sonnet, and Llama-405B adapt more. All models
             score worst on items where both a first and second option are correct.
             The paper does not claim MMLU-Pro itself is broken; it builds a harder
             test for what MMLU-Pro cannot measure.
Locators:    Abstract; Section 3.1-3.3 and Figures 2-3 (metrics, model behavior).
Quote:       "MMLU-Pro+ ... tests LLMs' ability to engage in complex reasoning and
             resist simplistic problem-solving strategies."
```

```text
URL:         https://dataphoenix.info/hugging-faces-open-llm-leaderboard-v2-increases-difficulty-and-delivers-fairer-scores/
Kind:        secondary. Data Phoenix reports on Hugging Face's adoption of MMLU-Pro;
             it does not own MMLU-Pro or the leaderboard, so it is context, not the
             claim's owner.
Establishes: An independent, widely used evaluator judged MMLU-Pro good enough to
             replace MMLU on the Open LLM Leaderboard v2, and how the leaderboard
             frames the score.
Paraphrase:  The Open LLM Leaderboard v2 replaced MMLU with MMLU-Pro because MMLU was
             "noisy (some questions were unanswerable), and too easy (because of
             model contamination)." MMLU-Pro is described as "a higher-quality and
             more challenging version of the original MMLU." Leaderboard v2 normalizes
             every benchmark between the random baseline (0) and the maximum (100).
Locators:    Article body, sections on the six v2 benchmarks and "Normalized Scoring."
             Author Ellie Ramirez-Camara, 2024-06-28.
Quote:       "Scores are now normalized between the random baseline (0 points) and the
             maximum possible score (100 points), providing a fairer comparison across
             different benchmarks."
```

Naming note for the writer: the dataset and leaderboard are the work of TIGER-Lab
(the "TIGER-AI-Lab" GitHub organization), the research group led by Wenhu Chen at
the University of Waterloo. The paper lists 17 authors; Yubo Wang is first author,
Wenhu Chen is senior author. Call the producer "TIGER-Lab" or the paper's authors,
not a company. The Open LLM Leaderboard that adopted MMLU-Pro is Hugging Face's, and
it retired to read-only in March 2025, so the live host today is the TIGER-Lab Space.

## Contradictions

- The Gema error figure changed between versions. The June 2024 v1 stated "more than
  9%" over 3,000 questions across 30 subjects with 14 experts. The current version
  (v3, 2025-01, and the NAACL 2025 camera-ready) states 6.49% over 5,700 questions
  across all 57 subjects. Cite 6.49% and 5,700 as the settled figures; do not use the
  v1 numbers.
- MMLU's own test count (14,079) does not match the denominator Gema reports it
  projected over (about 14,042). The gap is small and both are the primaries for
  their own step. State MMLU's size as 14,079 test questions per Hendrycks et al.
- The commission frames MMLU-Pro as "a harder MMLU" that repairs named defects. The
  composition undercuts the "same test, harder" reading: about 43% of items are new,
  drawn from STEM websites, TheoremQA, and SciBench, and Math is now the largest
  discipline. MMLU-Pro is partly a different benchmark, weighted toward STEM
  reasoning, not only a filtered MMLU. The writer should say this plainly.
- The guess-rate fix is uniform only for the 83% of items that have ten options.
  17% have fewer (mean 9.47), so random-guess accuracy lands near, not exactly at,
  10%.
- MMLU-Pro's own robustness claim (about 2% prompt sensitivity) is measured over 24
  prompt styles, not over answer-order permutations. Gupta et al. shows order
  permutation alone moves MMLU accuracy 6 to 27 points, and did not test MMLU-Pro.
  The writer cannot state MMLU-Pro is order-robust; the paper did not measure it.
- The "more robust and challenging" premise is time-limited. In 2026 the live
  leaderboard shows several models near 88% within about a point of one another, the
  same saturation that ended MMLU's usefulness. A small MMLU-Pro gap at the top now
  carries little signal.

## Numbers

```text
Figure: 12,032 questions, 14 disciplines
Owner:  MMLU-Pro paper (Table 5) and TIGER-Lab dataset card
Scope:  final released MMLU-Pro test set
```

```text
Figure: four options -> ten options; random-guess accuracy 25% -> ~10%
Owner:  MMLU paper (25.0% baseline) and MMLU-Pro paper (ten options)
Scope:  per-item chance level; ~10% is exact only for the 83% of items with ten
        options (mean 9.47 options, so slightly above 10% overall)
```

```text
Figure: 13,937 MMLU questions in -> 5,886 filtered as too easy -> 6,810 MMLU
        questions retained (56.60% of the final 12,032)
Owner:  MMLU-Pro paper (Section 3.2, Table 5)
Scope:  MMLU contribution to the final set; remainder added from STEM website
        (4,083), TheoremQA (598), SciBench (541)
```

```text
Figure: prompt sensitivity 4-5% (peaks 10.98%) on MMLU -> ~2% (max 3.74%) on
        MMLU-Pro
Owner:  MMLU-Pro paper (Section 6.3, Figure 5)
Scope:  spread of a model's score across 24 prompt styles
```

```text
Figure: chain-of-thought minus direct answering: GPT-4o +1.5 pts on MMLU,
        +19.1 pts on MMLU-Pro; GPT-4-Turbo -0.2 pts on MMLU, +15.3 pts on MMLU-Pro
Owner:  MMLU-Pro paper (Table 3); corroborated by dataset card (GPT-4o 0.7255 CoT
        vs 0.5346 direct)
Scope:  same model, same benchmark, CoT prompt vs direct answer
```

```text
Figure: accuracy drop MMLU -> MMLU-Pro of 16% to 33%
Owner:  MMLU-Pro paper (Abstract, Figure 4)
Scope:  same models scored on both; worked examples GPT-4o 88.7 -> 72.6,
        GPT-4-Turbo 86.5 -> 63.7
```

```text
Figure: MMLU error rate 6.49% overall; Virology 57% (33% wrong key, 4% multiple
        correct, 14% unclear)
Owner:  Gema et al. (current version, Section 3.1, Figure 3, Table 5)
Scope:  stratified-sample estimate over MMLU; Virology is the worst subject
```

```text
Figure: ranking reversal, Virology: Llama 3.1 405B Instruct 0.57 (rank 16, all
        items) -> 0.93 (rank 1, correct items only)
Owner:  Gema et al. (Table 2)
Scope:  one subject after removing erroneous items; illustrates how label noise
        distorts a reported rank
```

```text
Figure: Llama 4 MMLU-Pro, same benchmark two settings: Maverick 62.9 (pretrained,
        5-shot, EM) vs 80.5 (instruction-tuned, 0-shot, acc); Scout 58.2 vs 74.3
Owner:  Meta Llama 4 model card
Scope:  cautions that a cross-model or cross-report gap can be an eval-setup gap
```

```text
Figure: live leaderboard top near 88% (MiniMax-M2.1, Intern-S2-Preview 88%,
        Qwen3.5-397B 87.8%, DeepSeek-V4-Pro 87.5%)
Owner:  TIGER-Lab MMLU-Pro dataset card / leaderboard Space (read 2026-08)
Scope:  current saturation; top models within about a point
```

## Source assets

```text
Asset: MMLU-Pro paper, Figure 2 (the construction pipeline diagram)
Shows: the five build stages in order: MMLU pool, easy-item filter, added sources,
       option expansion to ten, two-phase expert review.
Crop:  keep all five stages and the arrow order; a partial crop loses the sequence
       the lesson is teaching.
```

```text
Asset: MMLU-Pro paper, Figure 4 (per-model accuracy, MMLU vs MMLU-Pro)
Shows: the same models dropping 16-33 points from MMLU to MMLU-Pro.
Crop:  retain both bars per model and the axis; the point is the paired drop.
```

```text
Asset: MMLU-Pro paper, Figure 5 (prompt-sensitivity spread across 24 prompts)
Shows: the narrower MMLU-Pro spread beside the wider MMLU spread.
Crop:  keep both distributions and the shared axis scale; a single distribution
       proves nothing on its own.
```

```text
Asset: Gema et al., Figure 3 (per-subject error-rate bars, Virology at 57%)
Shows: how uneven the error is across subjects, with Virology far out on the tail.
Crop:  keep the subject labels and the Virology bar; the outlier is the argument.
```

```text
Asset: TIGER-Lab live leaderboard table (2026 top rows)
Shows: several 2026 models clustered near 88%, the saturation that limits a small
       gap's meaning today.
Crop:  keep the top rows and the score column; note the read date, since the table
       updates.
```

Note on rendering: house rule renders charts from a committed chart script, not from
screenshots of a source. These assets name where the evidence lives; if the writer
wants a figure, the underlying numbers here (the paired MMLU/MMLU-Pro scores, the
per-subject error rates) are what the script should plot, with the source cited in
the caption.

## Discarded

```text
URL: https://arxiv.org/html/2406.04127v1 — superseded. The June 2024 v1 states ~9%
     error over 3,000 questions across 30 subjects; the current version's 6.49% over
     5,700 across 57 subjects is authoritative. Used only to confirm the change.
URL: https://intuitionlabs.ai/articles/mmlu-pro-ai-benchmark-explained — secondary
     explainer; every figure it carries is available firsthand from the paper and
     dataset card, so it adds no interpretation.
URL: https://pricepertoken.com/leaderboards/benchmark/mmlu-pro and
     https://benchmarkingagents.com/mmlu-pro/ — third-party leaderboard aggregators;
     the TIGER-Lab card is the owner's own live ranking, so these are redundant.
URL: https://huggingface.co/blog/open-llm-leaderboard-v2 and the raw blog markdown —
     returned 404 to the fetch. The leaderboard's adoption of MMLU-Pro and its 0-100
     normalization are recorded through the Data Phoenix report instead.
URL: https://huggingface.co/spaces/TIGER-Lab/MMLU-Pro — the Space shell did not render
     its table to the fetch; the live top scores are recorded from the dataset card,
     which mirrors the same leaderboard.
```
