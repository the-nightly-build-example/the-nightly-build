# writer brief: the-instruments/fid (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and boundaries.
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting and every revision.
- `../../researcher/01/evidence.md` — the complete set of claims available to you; the Numbers section is exact; read its contradictions (defenses that bound the criticism).
- The initialized article and template context under the workspace (edit in place).

Output: `draft-handoff.md` (this directory). The article you edit is
`.nb-work/the-instruments/fid/library/the-instruments/fid.html`.

Proof (run from `/home/user/the-nightly-build`, iterate `--no-check-links`,
finish with links until `BLOCK: 0`):

```
./nb check .nb-work/the-instruments/fid/library/the-instruments/fid.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

What the evidence establishes — spend it precisely:
- Construction first: InceptionV3 pool3 (2048-dim) features, each set fit as one
  multivariate Gaussian (mean + covariance), the Fréchet/Wasserstein-2 distance
  between the two. Lean on `the-mechanics/reading-images` for how a model turns an
  image into a vector; link it, do not re-teach. Link `the-evidence/gans` for the
  generators FID judges.
- The strongest, fully-sourced misled case to work in full: Projected FastGAN and
  StyleGAN2 tie on FFHQ FID (5.28 vs 5.30) yet split under human inspection and a
  CLIP-feature distance (2.76 vs 4.67) — a near-equal FID that does not track the
  images people actually prefer. Support it with the other two failure modes:
  sample-size bias (teach it as a mechanism — FID is biased, roughly linear in
  1/N, so two FIDs at different sample counts are not comparable, and it can
  reverse a ranking; do NOT invent a single "X at 10k vs Y at 50k" headline the
  evidence does not carry), and resizing/implementation incomparability (Clean-FID).
- Keep the criticism honestly bounded, as the evidence's defenses require: the
  three failures all hold image quality fixed and move FID by changing sample
  count, ImageNet class frequencies, or resizing code — so FID breaks
  comparability across setups and can be gamed, while staying a sensible
  within-pipeline, fixed-N signal. Do not imply the number is worthless.

Recent habits to break:
- Instruments openers lean on "Every few months a lab announces…" and close the
  Why card on "By the end you can meet any … claim and say what it does and does
  not prove." Write the promise in FID's own terms, off that mold.
- Do not force the "score confused for a harder skill" shape the last two
  instruments pieces used; this is the anatomy of one number and the documented
  ways it lies. Do not reuse "None of this makes the metric worthless." Do not
  close on "read the claim precisely / now you know which one you are looking at."
  Vary any note label; do not default to "In plain language."

nb-meta: set `harness` to `claude-code-routine` and `model` to `Claude Opus 4.8`
(writer ran on Opus), matching the shelf's readable form. `nb stamp` writes counts.

If a figure earns its place (the FID-vs-human/CLIP split, or a sample-size curve),
build it only from the evidence's verified series via `nb chart`, or use a
verified source asset the evidence identifies; inspect the rendered result.
