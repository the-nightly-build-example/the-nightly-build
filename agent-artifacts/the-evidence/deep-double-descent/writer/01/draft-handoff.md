# Draft handoff: the-evidence/deep-double-descent (writer 01)

## Original-work sentence

The article turns the evidence record's approximate figure-reads into a verified
double-descent curve computed from Nakkiran et al.'s released raw runs, and sets
that curve against the papers' own "more data hurts" and label-noise results to
draw the line between the reproducible phenomenon and the "bigger is always
better" moral now attached to it.

## Proof result

Full proof (links included): `BLOCK: 0  WARN: 0  verdict: PUBLISHABLE`.
Stamped words=2200, reading_minutes=10, sources=6 (4 primary cited, 2 secondary
cited). No warning left standing.

## Decisions worth the editor's eye (not blockers)

- Fig. 1 is a chart built with `nb chart` from the authors' released raw data
  (bucket `cifar10-resnet18k-p15-adam-reps`, five runs, final-epoch error, the
  paper's own clean-to-noisy remap at p = 0.15). The chart's verified values
  (first minimum ~0.34 near k = 4, critical-region peak ~0.41 near k = 10, floor
  ~0.29 at k = 64) supersede the evidence record's approximate figure-reads
  (peak "near 0.48", floor "0.28"), exactly as the brief directed. `chart-1.py`
  beside the article carries the data and the transform as provenance; the
  caption cites source 2 with `data-nb-url` to the released repo.
- The Transformer "more data hurts" result is stated as a rise in test loss (with
  a one-clause gloss), not classification error, because the record's Numbers
  entry names cross-entropy test loss for that figure. The defined term "test
  error" is reserved for the image classifiers, where it is classification error.
- I taught the interpolation threshold using Belkin's random-Fourier-features
  run (n = 10^4) and dropped his fully-connected MNIST example (n = 4x10^3) for
  length; both were in the record, one carries the point.
- Both bookends and the "In plain language" note address the reader, the one
  self-reference the lesson template allows.

## Warnings intentionally left

None.

## Open evidence / voice needs

- Classical bias-variance origin. Per the brief's second caution, the classical
  view is anchored on the two primaries actually opened (Belkin's textbook
  corollary, source 1; Nakkiran's framing, source 2). Geman et al. 1992 was not
  read in full. If the editor wants a dedicated classical-statement citation,
  that is a researcher task (open Geman 1992 or Hastie et al. directly); it is
  not needed for the argument as written.
- No unresolved voice question.
