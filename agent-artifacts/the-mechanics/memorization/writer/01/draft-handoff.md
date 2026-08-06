# Draft handoff: the-mechanics/memorization (01)

## Original work
This lesson turns the extraction literature's scattered aggregate figures into one
continuous descent on a single specimen sentence (`Call me Ishmael.`), showing how
that exact string gets fixed in the weights by next-token training and why, and it
repurposes the New York Times filing's own in-weights-versus-fetched split as the
concrete demonstration of the memorization/retrieval boundary the numbers alone leave
open.

## Proof result
`nb check` with links: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** No warnings left
standing. Stamped: 2138 words, 9 sources (6 primary, 5 required; 3 secondary),
9 min read.

## Decisions worth an editor's eye
- **NYT boundary taught in prose, not captured as an `nb asset`.** The evidence
  record offered several complaint-exhibit crops (side-by-side GPT-4-vs-original,
  the red-highlighted spans, the Bing/Oct-2023 frame). I judged no source asset
  genuinely warranted: the argument spends the memorization/retrieval boundary fully
  in prose via the filing's own two-mechanism split (para 102) and its post-cutoff
  Bing example (paras 108-114), and the public-domain specimen carries the "what
  verbatim looks like" weight without reproducing NYT article text from a legal
  filing. If the editor wants the split shown rather than told, the Bing/Oct-2023
  exhibit is the one asset that would earn its place.
- **No chart.** The evidence record supplies the log-linear *slope* (+19 pts per 10x,
  R² 99.8%) and the drivers, but not a verified point-by-point series to plot
  honestly, so I kept the numbers in prose and the definition-dependence in a table
  rather than fabricating a Figure 1 reconstruction.
- **`0.00000015%` cited to Carlini 2023 (s3), not 2021.** Following the evidence
  Numbers block, whose owner line reads "Carlini et al. 2023 restating Carlini et al.
  2020/2021"; the 2023 paper is where the four-orders-of-magnitude contrast with the
  1% figure is actually drawn. The 604-example count is cited to its 2021 owner (s2).
- **Commission's "duplication threshold" not used.** Framed as the log-linear
  "more copies, steadily more likely, with no single count" per the brief and the
  Contradictions note.

## Open questions
None blocking. One standing choice for the editor to confirm: whether the lesson
should carry the NYT exhibit image (above) or remain image-light with the table and
pull quote as its only furniture.
