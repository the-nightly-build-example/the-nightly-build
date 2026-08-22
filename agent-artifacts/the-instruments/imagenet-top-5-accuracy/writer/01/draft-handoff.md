# Draft handoff: the-instruments/imagenet-top-5-accuracy (01)

## Original-work sentence

The article fuses facts the evidence record holds only separately: it plots the
year-by-year winning top-5 error against both the 5.1% human line and the ~6%
label-error band in one figure, and holds the three distinct error measurements
(Russakovsky's 0.3%, Northcutt's 6%, Beyer's 29%) apart in the same passage, so a
reader can see that once the score fell past the label floor it was measuring the
answer key as much as the model — a reading no single source states on its own.

## Proof result

Final `./nb check` with links included: **BLOCK: 0, WARN: 0** (verdict:
PUBLISHABLE). Stamped: 2185 words, 9 sources (7 primary, 2 secondary), 10 min.
Chart rendered via `nb chart` (chart-1.py committed beside the article) and
inspected; the full preview site builds with the draft merged and serves the
article and chart-1.png. No warnings left standing.

## Notes for the editor

- Followed the brief's guardrails: the misled case leads with the labels
  (single-label/multi-object plus noisy key); the human baseline is secondary and
  told in ImageNet's own record (Karpathy as annotator A1, A2 at ~12%), kept off
  GLUE's ground with the required Background link to the-instruments/glue. The
  three error rates are stated as three different measurements and never merged.
  The ranking point is stated exactly as Northcutt has it: overall rankings
  unaffected, instability confined to near-top (ResNet-18 over ResNet-50 once the
  mislabeled share rises 6%). This lesson defines top-1 and top-5.
- 2016–2017 figures (~2.99%, ~2.25%) were deliberately excluded per the evidence
  flag; the chart and prose stop at 2015 (ResNet 3.57%). If a later editor wants
  the curve extended, those need separate sourcing.
- labelerrors.com appears only as a Go-deeper pointer (companion site named in
  the Northcutt paper), not as a cited-as-read source, per the evidence note.

## Open question

None blocking. One judgment call worth a look: the dek carries the word
"superhuman" in single quotes as the public framing the piece then dismantles; if
the editor reads that as endorsing rather than quoting the claim, it can be recast
in ImageNet's plainer nouns.
