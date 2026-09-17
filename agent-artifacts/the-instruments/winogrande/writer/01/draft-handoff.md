# Draft handoff: the-instruments/winogrande (01)

## Original-work sentence

The article sets WinoGrande's own learning curve (the same filtered items scored
50.4% at 160 training examples and 79.1% at ~41K) directly beside the return of
near-human scores and the two model cards that flag their own contamination, so
that facts the evidence records separately become one argument: the number's
difficulty is a dial set by construction and training budget, not a fixed measure
of reasoning, and the piece states exactly what a current WinoGrande score does
and does not license.

## Proof result

`./nb check ... --series the-instruments --library <checkout>` (links included):
**BLOCK: 0, WARN: 0 — PUBLISHABLE.** `nb stamp` written (words 2200,
reading_minutes 10, sources 8). No warnings left standing.

- 8 sources, 7 primary + 1 secondary (Defeat paper carries the secondary role for
  its outside critique of WinoGrande). Sources numbered in first-citation order.
- Chart-1 (learning curve, Table 4) rendered with `nb chart`, log x-axis labeled,
  human 94.0% reference line; script committed beside the article as provenance.
- Furniture: stat strip (100 / 43,972 / 12,282), a labeled quotation note, the
  learning-curve figure, and a holds-up grid. No article-authored scripts/styles.

## Exactness confirmed against evidence

- WSC size: 2012 paper described "more than 100" schemas; 273 attributed to the
  later standardized WSC273 set, not the 2012 paper.
- Near-human machine score uses UNICORN's own-paper 86.6%; the 91.2% leaderboard
  entry is deliberately not used anywhere (AI2 leaderboard offline, unverifiable).
- 118K "human-level" extrapolation reported as the paper's own claim, with the
  note that its printed fit does not reach 94% at that size.
- Habits broken: no Goodhart closer, no compression-definition heading mold, no
  "checked on X / trusted on Y" phrasing. bert/glue/superglue linked in Background,
  not re-taught. 0 em-dashes.

## Open evidence / voice question

None.
