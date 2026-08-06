# Draft handoff: the-evidence/gans (01)

## Original work

This lesson does one thing the evidence record does not: it seats the paper's
actual 2014 output (the blurry Figure 2 sample panels, captured as asset-1; the
two Parzen-window scores; the second-place finish on faces) directly beside the
later photoreal lineage's dates and the 2021 diffusion supersession, so the
reader can measure the paper's fame against the evidence it printed and separate
origin-of-technique (true) from origin-of-photoreal-images (false).

## Proof result

`nb check ... --series the-evidence --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left
standing.

Stamp: words 1927, reading 8 min, sources 9 (7 primary, 2 secondary; policy
floor is 6 / 3 primary / 1 secondary).

## Furniture used, and why

- **Source asset (Fig. 1 / asset-1.png):** Figure 2's four sample panels,
  clipped from the arXiv PDF p. 6 (110,352,396,290 pt), caption cropped away. It
  is the one visual the reputation never shows and the argument spends it
  directly: blurry gray faces and near-unrecognizable 32x32 blobs. The TFD panel
  also does the "not faces of nonexistent people" work.
- **Table:** Table 1's Parzen scores, reproduced exactly (MNIST + TFD, four
  models). Carries the "GANs lose the TFD column to Stacked CAE, 2110±50 vs
  2057±26" point that prose alone blurs.
- **Note (quotation):** the authors' verbatim metric caveat — the deadpan line
  the whole "weak evidence" case rests on.

## Open questions for the editor

- **MNIST 28x28 / TFD 48x48 resolutions were unverified in the evidence record.**
  I deliberately did not print those two numbers. The low-resolution point runs
  entirely on CIFAR-10's confirmed 32x32 (cited to the dataset owner); MNIST and
  TFD samples are described qualitatively ("handwritten digits", "small grayscale
  photographs of faces"). If the editor wants the other two sizes stated, they
  need a resolving canonical source first.
- **Citation count rests on Google Scholar alone** (~96,878 read 2026-08-06). It
  is presented as "roughly 97,000 ... an order-of-magnitude marker of fame rather
  than an exact count," per the evidence record's instruction.
- **"Four Parzen numbers" framing (brief) vs the table.** Table 1 has eight value
  cells; only two are the adversarial model's own scores. I framed it precisely
  as "two scores of its own against three earlier methods" rather than asserting
  a bare count of four, to keep the display text matching the paper exactly.
