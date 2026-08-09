# review-brief: the-instruments/fid (editor/01)

Inputs:
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writer/01/brief.md` — the exact writer brief (for spotting instruction leakage).
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; read first.
- `../../researcher/01/evidence.md` — the evidence to test claims against; note the defenses that bound the criticism.
- `../../writer/01/draft-handoff.md` — the original-work sentence (open on the third read).
- The article: `.nb-work/the-instruments/fid/library/the-instruments/fid.html`, and its chart at `library/the-instruments/fid/chart-1.py` / `chart-1.png`.
- Template context under `.nb-context/`.

Round focus — the load-bearing checks:
- Inspect the chart as evidence: compare chart-1.py's numbers against the evidence
  record and the owning primary (the Projected FastGAN 5.28 / StyleGAN2 5.30
  Inception-FID tie vs CLIP 2.76 / 4.67 split). Read the rendered image as a
  reader — axes, scale, legend, and the grouped bars must be honest and labeled,
  and the caption a factual cited line. The writer's original work is recomputing
  FID's distance on CLIP features and drawing the tie beside the split; confirm
  that is what the chart shows and that it is not overstated.
- Verify the construction is correct and not overclaimed: InceptionV3 pool3
  (2048-dim), Gaussian mean+covariance per set, Fréchet/Wasserstein-2 distance.
  Check the annotated equation's terms against the evidence.
- Verify the failure-mode figures descriptor by descriptor (the ImageNet-class
  lever 5.30→1.78 with CLIP moving ~4%; sample-size bias linear in 1/N and rank
  reversal; resizing/JPEG gaps). Confirm the criticism stays honestly bounded (the
  three failures hold image quality fixed and break comparability; FID still rises
  monotonically on Heusel's degradations) rather than implying the number is
  worthless.
- Open every citation href as printed; audit every data-nb-kind (9 primary / 1
  secondary claimed); verify display text.

Recent-pattern notes (compare against the recent library; a formula shows only
across articles):
- Instruments openers lean on "Every few months a lab announces…" and close the
  Why card on "By the end you can meet any … claim and say what it does and does
  not prove." Flag if this Why card falls into that mold.
- The last two instruments pieces hinged on "the score is confused for a harder
  skill"; this one is the anatomy of one number plus documented ways it lies.
  Flag any forcing into the "confused-for" mold, any reuse of "None of this makes
  the metric worthless," and the second-person "now you know which one you are
  looking at" / "read the claim precisely" closers.
- "In plain language" note label recurs across the shelf; check any note names the
  move it makes. Check headings vary in construction (comma + "and" joins recur).
