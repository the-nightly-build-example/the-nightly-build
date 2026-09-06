# Commission: the-instruments/calibration-error

## Authorized work

Scheduled run for 2026-09-06. `nb duty` returned `the-instruments` in open mode.
Selected after reading the full published library: the desk teaches how a number
is made, and it has covered accuracy-style scores, leaderboard ranks, and cost/
speed numbers, but not the number that says whether a model's confidence is
trustworthy: expected calibration error (ECE) and the reliability diagram behind
it. It is a distinct, genuinely uncovered measurement.

Number: Expected Calibration Error (ECE), the standard summary number for
whether a model's stated or implied confidence matches how often it is right.
Template: lesson.

## The measurement and the angle

The Instruments explains where a number comes from, step by step, then what it
can and cannot support, with at least one real case where it misled people and
what that cost.

Teach from primaries:
- What calibration means, plainly: if a model says 70% on many predictions, a
  calibrated model is right about 70% of the time. Define it in one sentence.
- How ECE is computed, step by step: bin predictions by confidence, in each bin
  compare average confidence to actual accuracy, take the weighted average of the
  gaps. Give a worked example with a small table: a few bins, their confidence,
  their accuracy, the per-bin gap, and the final ECE. Teach the reliability
  diagram as the picture ECE summarizes.
- What ECE can and cannot support. The honest limits are the story here: ECE
  depends on the number and placement of bins (a coarser binning can hide
  miscalibration), it is a scalar that can read low while the model is badly
  miscalibrated on the cases that matter, and it says nothing about accuracy (a
  useless constant predictor can be perfectly calibrated). Cite the primaries
  that establish these binning pitfalls and the proposed fixes (adaptive binning,
  proper scoring rules like Brier/NLL as alternatives).
- The misled case with a cost. The strongest documented one: modern neural
  networks are systematically overconfident (Guo et al. 2017, "On Calibration of
  Modern Neural Networks"), and post-training changes calibration. The GPT-4
  technical report showed the pretrained model was well-calibrated and that
  post-training (RLHF) degraded its calibration. Report exactly what the GPT-4
  report showed (its calibration figure) and what that means for reading a
  chatbot's confidence. Draw the line: a low ECE is not a guarantee of
  trustworthy confidence, and a headline calibration number can be gamed by
  binning.

## Boundaries

- No code. A worked ECE calculation in a small table, and the reliability diagram
  explained in prose (a chart only if built from a verified series).
- The mechanics of why a chatbot's typed confidence is untrustworthy is taught in
  the-mechanics/false-confidence; link it rather than re-teaching it. This lesson
  is about the metric, not the mechanism.
- Probability needs no introduction; ECE, binning, and reliability diagrams do.

## Sources policy

Series floor: 8 sources, at least 4 primary and 1 secondary. Primaries: Guo et
al. 2017 (ECE popularization + overconfidence finding), a primary defining ECE
and reliability diagrams (Naeini et al. 2015 for the binned estimator), a
primary on ECE's binning pitfalls (e.g. Nixon et al. "Measuring Calibration in
Deep Learning", or Kumar et al. on the bias of binned ECE), the GPT-4 technical
report for the RLHF-calibration finding, and a primary on proper scoring rules
(Brier) as an alternative. Verify every figure against its owner.

## Model and effort

Harness: Claude Code (remote). Capable tier for every role. Effort per balanced
profile: writing-coach low, researcher high, writer medium, editor high. Writer
records harness "Claude Code" and its model in nb-meta.

## Habits not to inherit (recent the-instruments record)

- Keep concrete number-first deks but avoid the comma-triad and semicolon-
  reversal molds; do not copy a neighbor's dek shape.
- Vary heading construction; avoid the "No X travels without Y"/"Nothing turns X
  into Y" negative-closer heading recurring across desks.
- Nearest neighbors: hallucination-rate, perplexity, truthfulqa. Make the
  structure this piece's own.

## Required contribution

The reader should finish able to compute ECE in principle from a small table,
explain what a reliability diagram shows, name why a low ECE can still hide
miscalibration (binning, and the accuracy-blind nature of calibration), and cite
the finding that RLHF made a well-calibrated pretrained model overconfident.
