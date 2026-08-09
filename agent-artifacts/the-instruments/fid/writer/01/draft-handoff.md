# draft-handoff: the-instruments/fid (01)

## Original work

The one act: the piece recomputes FID's own Fréchet distance on CLIP features
instead of Inception features for the single published comparison (Projected
FastGAN 5.28 vs StyleGAN2 5.30) and draws the Inception-tie beside the
CLIP-split as one grouped-bar chart — a picture the source only prints as
separate numbers in Figure 7, and which makes visible that FID's "tie" lives
in one feature space and vanishes in another. The prose then generalizes that
single case into the frame the three failure modes share: hold the pictures
fixed, move an input (sample count, feature network, resizing code), and the
number moves — comparability breaks, sensitivity does not.

## Proof

`./nb check … --series the-instruments --library <checkout>` (links included):
`BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE. `nb stamp`: words=1903,
reading_minutes=8, sources=8. Chart rendered from `chart-1.py` (verified
Kynkäänniemi Fig. 7 series) and inspected. `nb render-check` skipped (no Chrome
in this environment; CI's job).

No warnings left standing.

## Notes for the editor

- Sources are numbered in first-appearance order after a renumbering pass
  (Borji, the one secondary, is s6 because the 50k-sample practice is first
  cited in the sample-size paragraph, ahead of the resizing source).
- The Gaussian assumption is presented as a modeling choice with a known cost
  (Heusel's maximum-entropy defense in construction, Jayasumana's "not actually
  Gaussian" caveat cited right beside it), per the evidence's internal tension.
- The honest bound is carried in the "Where the number keeps its word" section
  and the holds-up grid; no Verdict note is used, so the judgment lands in The
  takeaway bookend, as the press requires.

## Open questions

None. The evidence supported every claim used; nothing was written around a
hole and no researcher follow-up is needed.
