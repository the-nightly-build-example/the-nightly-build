# review-brief: the-evidence/batch-normalization (editor/01)

Inputs:
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writer/01/brief.md` — the exact writer brief (for spotting instruction leakage).
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; read first.
- `../../researcher/01/evidence.md` — the evidence to test claims against; note its two writer cautions and the "positive mechanism unsettled" limitation.
- `../../writer/01/draft-handoff.md` — the original-work sentence (open on the third read).
- The article: `.nb-work/the-evidence/batch-normalization/library/the-evidence/batch-normalization.html`
- Template context under `.nb-context/`.

Round focus — the load-bearing checks:
- The spine is "the technique is right, the paper's stated reason (reduce internal
  covariate shift) is wrong." On the skeptic read, confirm the piece keeps two
  things distinct that are easy to blur: the paper's *distributional* definition of
  internal covariate shift versus Santurkar's *gradient-based* reformulation. A
  slide between them would break the argument.
- Verify display text descriptor by descriptor against the evidence: the ~14x
  speedup / 72.2% figure; the 4.82% ensemble top-5; and especially that the
  "exceeds human ~5.1%" figure is attributed to Russakovsky with its
  single-annotator, 1,500-image denominator — not to the batch-norm paper.
- Confirm the ending does NOT sell a settled replacement mechanism: Santurkar's
  landscape-smoothing is one account (and their own paper shows plain Lp norms
  smooth too); Bjorck credits larger learning rates. The honest landing is "the
  ICS story fails a controlled test and the field has not agreed what replaces
  it." Flag any overclaim of a settled successor.
- Check the annotated equation (the normalization) against the evidence, and the
  note carrying the paper's verbatim ICS definition. Open every citation href as
  printed and confirm it resolves; audit every data-nb-kind (5 primary / 1
  secondary claimed).

Recent-pattern notes (compare against the recent library; a formula shows only
across articles):
- Evidence openers lean on "You have almost certainly seen…" and close the Why
  card on "By the end you can say exactly…". Flag if this Why card falls into that
  mold.
- The "method right, reason wrong" contrast is earned, but watch it does not
  multiply into the negative-parallelism reflex the slop standard flags (keep
  earned contrasts to a couple). Flag any "None of this makes X fake," the
  second-person "Now you know…" / "The next time you see…" closer, and any default
  "In plain language" note label that does not name its move.
- Check headings vary in construction (comma + "and" joins recur across the paper).
