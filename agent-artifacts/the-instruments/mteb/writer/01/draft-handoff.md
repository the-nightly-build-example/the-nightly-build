# Draft handoff: the-instruments/mteb (01)

## Original-work sentence

The article rebuilds the single MTEB rank as a chain of folds (a per-dataset
metric, then a grouping into task types, then a flat unweighted mean over all
datasets) and uses that construction to separate the benchmark's two famous
flaws by their timelines: task imbalance as a limitation the 2022 authors stated
on day one, and contamination as a judgment those same authors first dismissed
in 2022 and only reversed by 2025. The evidence lists these facts; it does not
fold them into one mechanism or hold the two timelines apart, which is what the
piece does.

## Proof result

`./nb check ... --series the-instruments --library /home/user/library-checkout`
(links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** No warnings left standing.
Stamp: words 1973, reading 9 min, sources 8 (6 primary, 2 secondary), within the
lesson band (1200-2200) and above the series floor (8 sources, >=4 primary,
>=1 secondary). Render probe skipped (no Chrome in this environment); the added
component is a table authored to the documented `nb-table` markup, and the
preview site built with the draft merged (190 articles) without error.

## Open questions

- **Evidence, retrieval example direction (flagged in the record's
  Contradictions).** No single named model is documented topping the overall mean
  while being specifically weak at retrieval. Per the record's caution I wrote the
  "top the average, ordinary at retrieval" point as a property of the averaging
  method, stated in both directions, not as a named scandal, and cited the
  authors' own imbalance limitation plus the independent Modal statement of the
  opposite-direction case. If editorial wants a named chart-topper who flopped at
  retrieval, it is not in this evidence and would need a new researcher artifact.

- **Voice, Silver's gap arithmetic.** The voice guide offers Silver's move of
  putting a number on how far two models sit apart (top vs middle, or model to
  next) and setting it beside the score's own error. The record carries no
  verified between-model MTEB point gap or error bar, so I did not invent one. The
  concrete anchor the piece uses instead is the imbalance count (retrieval 15
  datasets vs summarization 1). Flag if a between-model gap figure is wanted; it
  would need new evidence.

- **Contamination worked figure.** The e5-mistral-7b-instruct 95% zero-shot / ~5%
  leak case is from Maintaining MTEB (English, v2), a different dated version than
  the v3 counts the rest of the piece is pinned to. I used it as the maintainers'
  own worked illustration of the zero-shot score and named it as such; the version
  difference is not called out in prose. Raise if that should be made explicit.
