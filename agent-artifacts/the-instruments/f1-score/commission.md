# Commission: the-instruments/f1-score

## The assignment

Teach the F1 score: the single number, the harmonic mean of precision and recall,
that sits under a large share of classification and question-answering
leaderboards. This is The Instruments: explain where the number comes from, step
by step, and show at least one real case where it misled people and what that
cost.

Selected because the course has just given the reader the background to understand
it. The library teaches AUROC (the-instruments/auroc) and a benchmark scored by F1
(the-instruments/squad), but never F1 itself. It is a foundational instrument the
reader keeps meeting without having been taught how it is built.

## What the lesson must do

- Explain where the number comes from, step by step. Define precision (of the
  items the system called positive, how many were right) and recall (of the items
  that were actually positive, how many the system found), each in plain words
  with a worked example, then F1 as their harmonic mean and why the harmonic mean
  punishes a lopsided pair. Name its origin in information retrieval (van
  Rijsbergen's F-measure) and the Fβ generalization that weights precision and
  recall differently.
- Show what the number can and cannot support. It collapses the precision-recall
  tradeoff into one figure, ignores true negatives, and depends on which class is
  labeled "positive" and on class balance; micro-, macro-, and weighted averaging
  give different F1s for the same multi-class predictions and can flip a ranking.
- Give at least one real case where the number misled people and what it cost. The
  researcher will identify the strongest documented case; candidates include the
  accuracy/F1 breakdown on heavily imbalanced data (the argument, with primary
  support, that F1 and accuracy mislead where a coefficient like MCC does not) and
  documented instances where a micro-vs-macro-F1 choice changed which system a
  leaderboard or paper called best.

## Boundaries

- One measurement. This is F1, not a survey of classification metrics; link auroc,
  calibration-error, and squad in Background rather than re-teaching them. Precision
  and recall are not separate library lessons, so build them here plainly.
- Work from the measurement's own literature: the papers that define and analyze
  F1 and its failure modes, not blog posts. Assume algebra and probability.

## Required contribution

The reader should finish able to compute the intuition behind F1, say what it hides
(the precision-recall split, true negatives, class balance), know that micro and
macro F1 can disagree, and read "state-of-the-art F1" and ask which averaging,
which positive class, and at what base rate.

## Source obligations

From `nb source-policy --series the-instruments`: at least 8 sources, at least 4
primary, at least 1 secondary. Primaries may include van Rijsbergen's F-measure
definition, Sasaki's analysis of the F-measure, Powers' precision/recall/F-measure
paper, and Chicco & Jurman's analysis of F1 vs MCC on imbalanced data. Verify each
formula and every reported figure against the owning primary.

## Recent habits not to inherit (the-instruments)

- Headlines have repeatedly been a single stat framed as an indictment of the
  metric; the move is fine but the mold is stale. Write the headline this
  measurement earns and keep negative parallelism out of it.
- The "when the number misled" section keeps landing last with a heading like
  "When the leaderboard rewrote its own answers"; vary the heading shape.
- Do not reach for the dek mold that packs a second clause with an outside
  comparison.

## Neighboring articles in tonight's edition

Running now, do not overlap: the-evidence/variational-autoencoder, the-mechanics/
lost-in-the-middle, what-could-go-wrong/alignment-faking, when-ai-breaks/
hirevue-facial-analysis. Keep this on how F1 is made and read.

## Production record

- Harness: Claude Code (remote). Model for every role: claude-opus-4-8 (capable
  tier; no stage required).
- Effort targets (`nb production-policy --series the-instruments`): researcher
  high, writer medium, editor high, writing-coach low. Recorded as targets.
- No source or production directive was traded down.
- Note: an earlier commissioning round in this run mistakenly selected already-
  published slugs; this slug was verified absent from the full library first.
