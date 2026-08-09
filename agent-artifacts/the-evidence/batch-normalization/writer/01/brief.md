# writer brief: the-evidence/batch-normalization (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and boundaries.
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting and every revision.
- `../../researcher/01/evidence.md` — the complete set of claims available to you; the Numbers section is exact; read its contradictions and its two writer cautions.
- The initialized article and template context under the workspace (edit in place).

Output: `draft-handoff.md` (this directory). The article you edit is
`.nb-work/the-evidence/batch-normalization/library/the-evidence/batch-normalization.html`.

Proof (run from `/home/user/the-nightly-build`, iterate `--no-check-links`,
finish with links until `BLOCK: 0`):

```
./nb check .nb-work/the-evidence/batch-normalization/library/the-evidence/batch-normalization.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

What the evidence establishes — spend it precisely:
- The spine: the paper's own "reduce internal covariate shift" explanation fails a
  controlled test (Santurkar 2018 added noise after batch norm to *increase*
  covariate shift and training stayed fast), while the technique delivers exactly
  the numbers the paper claimed (the ~14x fewer steps / 72.2% figure; the ensemble
  4.9% (4.82% test) top-5). Use the Numbers section's exact readings.
- Two cautions the evidence flags — honor both:
  - Keep the paper's *distributional* definition of internal covariate shift
    distinct from Santurkar's *gradient-based* reformulation; do not blur them.
  - Attribute the "exceeds human ~5.1%" reference to Russakovsky (its owner), with
    its 1,500-image single-annotator denominator — it is not the batch-norm paper's
    figure. State the smallness of that human baseline honestly.
- The positive replacement mechanism is NOT settled: Santurkar say landscape
  smoothing but show plain L1/L2/Linf normalization smooths as well or better;
  Bjorck credit larger learning rates. End on "the ICS story is wrong and the
  field has not agreed what replaces it" — do not sell a settled successor.
- Link `the-evidence/resnet` / `the-evidence/alexnet` and
  `the-mechanics/gradient-descent` where a claim needs them; do not re-teach
  residuals, AlexNet, or gradient descent.

Recent habits to break:
- Evidence openers lean on "You have almost certainly seen…" and close the Why
  card on "By the end you can say exactly…". Write the promise in this document's
  own terms, off that mold.
- The "method right, reason wrong" contrast is earned once; do not let it become
  the negative-parallelism reflex the slop standard flags, and keep total earned
  contrasts to a couple. Do not close on "Now you know…" / "The next time you
  see…". Do not reuse "None of this makes X fake." Vary any note label.

nb-meta: set `harness` to `claude-code-routine` and `model` to `Claude Opus 4.8`
(writer ran on Opus), matching the shelf's readable form. `nb stamp` writes counts.

If a training-curve figure earns its place, use only a verified source-asset the
evidence identifies (or an `nb chart` from the evidence's verified series);
inspect it. Do not use an unverified image.
