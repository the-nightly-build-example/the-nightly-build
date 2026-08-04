# Draft handoff: the-evidence/alexnet (writer 02 — revision)

## Original work

Unchanged and still holding: the article welds facts the evidence record lists
separately into one reading — the real ~10-point win set beside the sharpening
that the famous 15.3% is a seven-net ensemble (two nets pre-trained on extra
2011 data) while the single model the paper describes scored 18.2%, then the
whole result reframed as one contest win standing on three preconditions
(DanNet's pre-AlexNet GPU-CNN victories as evidence the method predated the
paper; BatchNorm, the Vision Transformer, and Recht et al. as three
separately-owned retirements), so credit and correction land in the same
generous breath rather than as a debunk.

## Editorial requests resolved (editor/01, both writer-owned, both blocking)

- **Chart honesty.** Rebuilt chart-1 from a false line into a discrete bar
  chart, so it asserts nothing across the omitted contests and draws no smooth
  slope through them. I took the editor's explicitly-sanctioned second option
  ("a form that does not imply the missing years") rather than adding 2011/2013,
  because the primary (Russakovsky, s2) states those two winning errors only in
  Figure 9's graphic, not its text — I could not read them pixel-exact — and the
  paper's own year-series text uses 16.4% (provided-data) for 2012, which would
  contradict the article's headline 15.3%. Plotting unverifiable values, or
  mixing measurement bases, would have risked a fresh content error in the round
  meant to remove one. The bar chart uses only the three points the evidence
  record verifies exactly (28.2% 2010, 15.3% 2012, 6.7% 2014). The house
  template renders them on a numeric year axis, so ticks at 2011 and 2013 stand
  visibly empty — the skipped contests are shown as absent, not interpolated —
  and the x-axis is labeled "contests shown, not every year." The 28.2%→15.3%
  bar drop reads AlexNet's 2012 break as a discrete step. Axes labeled, zero
  baseline kept, AlexNet annotation kept. Re-rendered with `nb chart` and
  inspected the PNG as a reader; provenance comment in chart-1.py updated to
  record the data source and why the form is bars. Caption and alt text
  rewritten to name the three plotted years and state the 2011/2013 contests are
  not shown.
- **Byline placeholder.** Visible byline now reads "9 min read", matching the
  stamped `reading_minutes: 9` (nb.js has no reading-time injection, so the value
  had to be written into the display text). Confirmed the "N" no longer appears.

Nothing else in the body was changed. The editor's Recht content-error cut and
all other settled work are preserved; the claim set was not expanded.

## Proof

`./nb check .nb-work/the-evidence/alexnet/library/the-evidence/alexnet.html
--series the-evidence --library /home/user/library-checkout` (links included):
**BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing.
`nb stamp`: words=2141, reading_minutes=9, sources=8 (unchanged 7 primary + 1
secondary; the +10 words over 2131 are the longer honest caption and alt text).

Display-text pass redone on everything touched: byline "9 min read" matches
nb-meta; the caption's years (2010, 2012, 2014) and the alt text's values
(28.2%, 15.3%, 6.7%) match the chart and the evidence Numbers block; the figure
is attributed to s2 (Russakovsky), the primary that owns the year-over-year
series.

## Open question

- **For the desk, non-blocking.** The chart now shows three of the challenge's
  first five contests. If the desk wants the full annual 2010–2014 series (which
  would sharpen "AlexNet was a discontinuity" by putting 2011's ~26% next to
  2012's break), that needs a new researcher artifact fixing the 2011 and 2013
  winning top-5 errors against a source that states them in text, and settling
  the 2012 basis (15.3% winning entry vs 16.4% provided-data) so all five points
  share one measurement basis. That is an evidence expansion, out of scope for
  this revision. The editor's optional Recht-significance note was left unmade
  (polish only, non-blocking).
