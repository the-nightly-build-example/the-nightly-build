# Commission: the-instruments/helm

## The assignment
This desk teaches how a number used to compare AI systems is made, and where it
misleads. Tonight's number is HELM: the Holistic Evaluation of Language Models
(Percy Liang and 50+ co-authors, Stanford CRFM, 2022) and the mean-win-rate
leaderboard it produces. Teach the reader, step by step, how HELM's headline
ranking is built: the scenarios (task + domain + who is represented), the seven
metrics measured for every scenario (accuracy, calibration, robustness, fairness,
bias, toxicity, efficiency), the standardized 5-shot prompting run across every
model on every scenario, and how per-scenario results are reduced to a single
"mean win rate" that orders the models on the leaderboard.

Then show what that one number can and cannot support. HELM's own authors argue
against collapsing a model to a single score; the leaderboard does exactly that.
Give at least one real case where the aggregate number misled: the ranking order
changes when you reweight scenarios or drop the efficiency/robustness axes, so a
"#1 on HELM" claim depends on choices most people quoting it never see. Use the
paper's own reported numbers (it measures 30 models on 42 scenarios) and, where
possible, the finding that accuracy and calibration/robustness diverge across
models.

## The one-sentence contribution this article owes
Show that HELM's single leaderboard rank is an average of choices (which
scenarios, which metrics, how weighted), and that the same underlying results
produce a different order under different, equally defensible choices — so the
rank compares the choices as much as the models.

## Boundaries and what not to re-teach
- Individual benchmarks HELM aggregates (MMLU, etc.) are covered: link, do not
  re-teach. The library has `the-instruments/mmlu`, `the-instruments/calibration-error`,
  `the-instruments/perplexity`, `the-instruments/big-bench-hard` — link the ones
  the lesson leans on in Background.
- Do NOT lean on "LLM-as-a-judge / evaluators prefer longer answers." That is
  llm-as-a-judge's territory (covered) and would collide with tonight's mechanics
  lesson. HELM's win rate is computed from scenario metrics, not from a model
  judge; keep the lesson on aggregation and metric choice.
- Few-shot prompting and accuracy are taught; introduce only what the number
  needs.

## Source obligations (resolved)
`nb source-policy --series the-instruments`: minimum 8 sources; at least 4
primary, at least 1 secondary. Primary: the HELM paper (Liang et al. 2022,
arXiv:2211.09110) read into its methods and results sections; the HELM/CRFM
leaderboard site and its documentation; the follow-on HELM releases (HELM Lite,
HELM MMLU / "classic" vs "lite") where they change the ranking method;
the primary docs for any specific divergence claim. Secondary: reputable
reporting/commentary for context only, never for a figure. Read the paper for the
exact model count, scenario count, metric definitions, and how mean win rate is
defined.

## Production record (resolved)
`nb production-policy --series the-instruments`: profile balanced. researcher high
/ capable; writer medium / capable; editor high / capable; writing-coach low /
capable. None required; use the most capable available model per role and record
actuals in `nb-meta`.

## Tonight's neighbours (one paper, no overlap)
- the-evidence/long-short-term-memory — the 1997 LSTM paper.
- the-mechanics/answer-length-bias — why chatbot answers run long (RLHF length
  bias). Keep clear of it: do not build HELM's story on "judges reward length."
- what-could-go-wrong/responsibility-gap.
- when-ai-breaks/iruda-chatbot.

## Recent shapes and habits to break (from the last ~2 weeks of this desk)
- The desk keeps landing on one mold: "the number moves when the thing it
  measures doesn't" (comet-score, brier-score, winogrande). HELM's real problem
  is different — aggregation hides disagreement between axes — so frame it as
  that, not as another "score is unstable" piece.
- Avoid the dek that states a precise number then reverses it in a second
  sentence (brier-score: "beat by 0.002 ... actually scored worse").
- Avoid comma-triad headings closed with "and". Vary heading construction.
- Do not headline with a bare superlative; put the specific finding first.
