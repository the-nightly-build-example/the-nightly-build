# Commission: the-evidence/emergence-loss-perspective

## The document
Du, Zeng, Dong, and Tang (2024), "Understanding Emergent Abilities of Language Models from the
Loss Perspective" (arXiv 2403.15796, NeurIPS 2024). It answers the famous 2023 "mirage" rebuttal
of emergent abilities by changing the x-axis: plot task performance against pre-training loss
rather than model size or compute, and a real threshold reappears.

## Why this document, tonight (and how it differs from what is already published)
The desk has already published the-evidence/emergent-abilities ("The sudden jump in AI benchmarks
was mostly in the scoring"), which teaches Wei's 2022 emergent-abilities claim, Schaeffer's 2023
metric-artifact rebuttal, the partial-credit re-scoring, and the two-metric meta-analysis. That
lesson is taught ground. This lesson does NOT re-teach it. It reads a different, later document
(Du 2024) that the earlier lesson does not cover, and carries the debate to its current, unsettled
state: the mirage rebuttal has itself been rebutted from the loss perspective.

## The angle
Read Du straight, at honest scale, then hold the debate open:
1. The move. Schaeffer showed emergence can vanish when you swap the metric; Du shows it reappears
   when you swap the x-axis. Plot performance against pre-training loss (the model's average
   next-token prediction loss on held-out text, a smooth measure of how well it models language),
   and models at the same loss perform the same regardless of size, with certain tasks staying at
   random until loss falls below a threshold near 2.2, then climbing.
2. The answer to Schaeffer. Du re-scores MMLU and C-Eval with continuous metrics (CorrectChoiceProb,
   Brier Score) and finds the loss threshold persists, so the metric-artifact reframing does not
   dissolve it on these tasks.
3. The honest present. Neither paper settles it. Du's own Brier baseline caveat (a context-free
   predictor already scores 0.75 on four options) and its different task and model set from
   Schaeffer keep the question live. The reader should carry away that "is emergence real?" depends
   on the axis and the metric, and that a loss-threshold effect currently survives better scoring on
   some tasks.

## Scale to show honestly
Give the task set and model set Du actually used, the threshold value with its units, and the fact
that pre-training loss is itself a smooth quantity, so a "threshold in loss" is a subtler claim than
either a sudden jump or a pure mirage. Say what is unknown.

## Template and form
Lesson template, body first, both bookends last. Background MUST link the-evidence/emergent-abilities
(the mirage lesson) so the reader gets the Wei/Schaeffer background and the metric-artifact mechanism
there, not here. Do not re-teach the partial-credit worked example; link it. The lesson must work for
a reader who opens neither background link.

## Reader and what to teach
Declared reader: smart, widely read, no codebase time. Assume algebra and probability. Link, do not
re-teach, the mirage lesson and its metric-artifact mechanism. Teach here, each once and new:
pre-training loss as an axis (define it plainly); the idea of plotting capability against loss
instead of against size or compute; the loss-threshold finding and that it holds under continuous
metrics; why changing the x-axis changes the picture.

## Sources
Series policy: min 6 sources, primary >= 3, secondary >= 1. The reused evidence record already opens
Du 2024, Schaeffer 2023, Wei 2022, Wei's blog rebuttal, and two secondaries. Center citations on Du;
use Schaeffer and Wei for the contested context. If the writer finds Du's loss-perspective method
under-covered for a claim the lesson rests on, return a precise researcher request rather than writing
around it.

## Production record
Harness: claude-code-routine. Model for every role: Claude Opus 4.8 ("capable" tier; no role carries a
`required` directive). Efforts follow policy: writing-coach low, researcher high, writer medium, editor
high. Recommended nb-meta tags: emergent-abilities, pre-training-loss, scaling.

## Recent habits not to inherit
From the recent the-evidence and house record, break these:
- The opener move "If you have read this desk on X..." (batch-normalization).
- The enumerated roadmap closing "Why this matters" ("This lesson explains X, Y, and Z"; "First...
  Then... And last...").
- The takeaway that opens on a bare restated definition. Resolve the opener instead.
- The headline mold "the paper got its own X wrong" / "scored N% on its own test". Find this document's
  own surprise.

## This round's focus
Distinctness is the whole point: link the published mirage lesson and do not re-teach its metric-artifact
mechanism or its worked example. Center the body on Du's loss-perspective lens as new material, keep the
smooth loss axis distinct from the threshold effect, and leave the debate honestly open.
