# Draft handoff: the-instruments/inception-score (01)

## Original-work sentence

The article fuses the scattered primary results into one teachable claim the
evidence never states outright, that a high Inception Score proves only
classifier confidence plus spread across categories and nothing else, and it
derives the blindness to within-class diversity directly from the
one-image-per-class structure of the attack as a consequence of the
construction, rather than reporting it as any paper's named finding.

## Proof result

`./nb check --series the-instruments --library /home/user/library-checkout`
(with link checking): **BLOCK: 0, WARN: 0, PUBLISHABLE**. Stamped words 1928,
reading 8 min, sources 8 (7 primary, 1 secondary). Zero em-dashes; no banned
terms; nb-meta dek and rendered dekline identical. No warning was left standing.

## How the brief's risk points were handled

- WGAN attack is the weight-bearing case: headline and table use the ~900
  (900.15) realistic-looking CIFAR-GAN result; the noise case (986.10) is
  presented and then conceded as the one a defender can set aside, against the
  authors' own caveat (carried in an nb-note quotation).
- Intra-class-diversity blindness is written as a consequence of the
  construction (the marginal is taken across categories, never within them), shown
  by the one-image-per-class attack, not attributed as a headline finding.
- "What it cost" is scoped to the record: years of rankings, the authors' own
  "most widely used" framing, BigGAN 166.5 as the single concrete headline
  figure, and Lucic et al. on tuning. No systematic-use claim.
- Scope cautions respected: BigGAN's 166.5 is never compared to a real-data IS;
  the 900.10-vs-900.15 discrepancy is stated in the table caption with both
  locations. "Order of 10" was dropped to avoid an apparent contradiction with
  BigGAN's 166.5 across protocols; the attacks are framed against the 1000 ceiling
  instead.
- FID is linked in prose (and Background), not re-taught; the IS-vs-FID
  divergence is limited to the step-by-step degradation finding, with FID's own
  single-scalar limit acknowledged.

## Furniture

One annotated nb-math equation (the definition, the one the lesson is about),
one nb-table (the attack scores against the ceiling), one nb-note (the authors'
caveat quotation). No stat-strip, no source asset, no chart.

## Open questions

- Source asset available but not used: Barratt & Sharma Fig. 1/2 (the image
  grids at 986.10 and 900.15). The argument would spend it, since "realistic-
  looking" is the weight-bearing claim, but the numbers and the one-per-class
  structure are carried in prose and the table. If the editor wants the visual,
  it is a clean `nb asset` capture from arXiv 1801.01973.
- No open evidence or voice questions; the named inputs settled the draft.
