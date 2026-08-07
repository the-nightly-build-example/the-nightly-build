# Draft handoff: the-evidence/resnet (01)

## Original work

This article stages the paper's degradation result as a construction the reader
performs before it is named: build the 56-layer network by copying a working
20-layer net and setting the 36 extra layers to pass their input through
unchanged, confirm the shallower solution provably sits inside the deeper
network, then watch training fail to reach it. The evidence record owns the
facts (higher *training* error, explicitly not overfitting; the identity
construction is the paper's own argument); the article's work is turning that
into a derivation the reader runs, and then reusing the same identity
construction as the bridge to why adding the input back (F(x)+x) makes "doing
nothing" the optimizer's default.

## Proof

`nb check` with links against the series library: **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. `nb stamp` written (words 2007, 9 min, 6 sources). No
warnings left standing.

## Evidence handling

- Honored both researcher corrections. The "not vanishing gradients" point is
  the article's hinge (named as a belief a careful reader holds, then separated
  from the record with the paper's Sec. 4.1 quote). The generality forecast is
  stated as a forecast that named no architecture and did not foresee the
  transformer, not as an absence of any generalization claim.
- Chart (Fig. 1 in article) is built from the verified Table 2 series (ImageNet
  top-1 validation error, 10-crop). Zero baseline with value labels, so bar
  length is honest and the small plain-net increase stays legible. The
  training-error / test-error distinction is kept in the prose, not the chart,
  which is validation error and captioned as such.

## Open questions

None blocking. One judgment call for the editor: I used a chart of the Table 2
reversal rather than capturing the paper's Figure 1 training-error panel as a
source asset. The prose carries the "higher training error, not overfitting"
point; if the editor wants the canonical training-error image on the page, that
asset is available in the evidence record (Source assets, Fig. 1) and would need
`nb asset pdf`.
