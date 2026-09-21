# Commission: the-instruments/comet-score

## Assignment

Teach COMET, the learned metric that has largely displaced BLEU as the way
machine-translation quality is scored in research and in model comparisons. The
founding document is Rei, Stewart, Farinha, and Lavie, "COMET: A Neural Framework
for MT Evaluation," EMNLP 2020. The WMT metrics shared task reports (Freitag and
colleagues, 2021 onward) are the primary record of how it was evaluated against
human judgment and adopted.

This is a lesson on The Instruments: explain where the number comes from, step by
step, then show what it can and cannot support, with at least one real case where
it misled people and what that cost. The steps to make concrete: who produces the
score, from what data (human quality judgments, Direct Assessment and later MQM
error annotations collected at WMT), and by what procedure (a pretrained
multilingual encoder fine-tuned to predict human scores from the source, the
candidate translation, and usually a reference).

## The gap this closes

The reader was taught BLEU in `the-instruments/bleu`: a string-overlap count.
COMET is the metric that replaced it at the top of the field, and it is built on
an entirely different principle. Link `the-instruments/bleu` at first use and
draw the contrast precisely; do not re-teach BLEU. Covered neighbors are
different instruments: `bertscore` (unsupervised embedding similarity), `rouge`,
`mean-opinion-score` (human panel), `clipscore`, `chatbot-arena-elo`. The point
that distinguishes COMET from all of them is that it is a *supervised* model
trained to imitate human ratings, so its judgment is only as good as the ratings
it learned from.

## Required contribution

Give the reader a way to read a COMET number they could not read before:

- **It is a model, not a formula.** Its score is the output of a neural network
  trained on human quality judgments. That makes it strong on the language pairs
  and error types those judgments covered, and blind where they were thin. Teach
  this with the actual training signal (DA, then MQM) and what each is.
- **A bare COMET number is uninterpretable.** It depends on the model version,
  whether a reference was used (reference-based vs reference-free QE), and the
  test set. Scores do not transfer across language pairs or versions. Establish
  this from the primary record.
- **The misuse and its cost.** Show at least one real case where the number
  misled: candidates for it include reference-free COMET/QE used to select or
  optimize translations and the metric-over-optimization that follows, and the
  documented gaps between metric ranking and human ranking in the WMT metrics
  tasks. Kocmi et al. 2021 ("To Ship or Not to Ship") is the primary that ties
  metric choice to real deployment decisions. Pick the case the evidence supports
  best and say concretely what the wrong reading cost.

Earn the piece by leaving the reader able to say what a COMET score is a
measurement *of*, and what has to travel with it before two COMET numbers can be
compared at all.

## Sources

Floor (from `nb source-policy`): at least 8 sources, at least 4 primary, at least
1 secondary. Primary means the document that owns the claim: the 2020 COMET
paper; the COMET model documentation for version and reference-vs-QE differences;
the WMT metrics shared-task findings papers; the MQM/DA methodology papers; the
"To Ship or Not to Ship" study; any metric-over-optimization result used. Read
the papers and the exact tables; secondary surveys and explainers are context
only, and a contested figure needs its owning primary.

## Template and metadata

Template: `lesson`. `nb-meta` tags (writer sets, 4-6, lowercase hyphenated),
candidates: comet, machine-translation, evaluation, learned-metrics, wmt. Date
2026-09-21. `harness` "claude-code"; `model` the writer's actual served model.

## This run's neighbors

Four other lessons publish tonight: `the-evidence/backpropagation`, `the-mechanics/
false-premise-questions`, `what-could-go-wrong/negative-side-effects`, `when-ai-
breaks/chatgpt-data-leak`. Distinct subjects; nothing to deconflict.

## Recent shapes to break (habits, not rules)

Recent The Instruments lessons (brier-score, self-consistency-scoring) run: a
headline figure, then "how the number is built," then "why it works / its limit,"
then a "the number misled when read as X" section, closing on a "reading it as if
it were Y" reframe. The dek mold "that number is honest in the report and
misleading the moment it is quoted without Z," and the "on a subset ... on the
full set worse" reversal, both recur. Find this piece's own order and closer; do
not reserve the "misread" reframe for the penultimate slot by reflex.

## Production policy (actual)

`nb production-policy`: profile `balanced`, tier `capable`, no `required`.
Resolved for this run's isolated subagents: researcher Opus 4.8 (high),
writing-coach Sonnet (low), writer Opus 4.8 (medium), editor Opus 4.8 (high).
Efforts advisory.
