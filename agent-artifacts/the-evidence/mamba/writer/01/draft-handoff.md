# Draft handoff: the-evidence/mamba (01)

## Original work
The article splits Mamba's single famous "matches transformers" headline into
the two distinct claims it actually is — same-size parity on short-context
reasoning at up to 2.8B, which the paper proved, versus parity on retrieval,
long context, and frontier scale, which it never tested — and then uses the
authors' own re-addition of attention in Mamba-2, plus the Jamba/IBM hybrid
verdict, to fix the exact point where the "transformer is finished" reading
outruns the evidence. The evidence record supplies these claims separately; the
article is what puts them on one axis and lands the boundary.

## Proof
`nb stamp` then `nb check ... --series the-evidence --library <checkout>` (links
included): **BLOCK: 0, WARN: 0, PUBLISHABLE.** Words 2147 (band 1200–2200),
7 sources (6 primary, 1 secondary; floor met). No warnings left standing.
Render probe skipped: no Chrome in this environment, so the two math figures
(the linear recurrence and the annotated N=1 selective gate) were verified by
valid KaTeX source and a clean preview build, not by a rendered screenshot —
worth a visual glance if a render-check runs in CI.

## Open questions
- Evidence use, not a blocker: the record flags "Repeat After Me" Figure 1(c)
  as the single clearest picture of the copying/retrieval gap. I taught the
  mechanism with the annotated gate equation and carried the gap in prose
  instead, to keep the lesson at the depth a no-code reader needs and avoid a
  benchmark-figure dump. If the editor wants the contradiction shown visually,
  that asset (not a chart — a captured source figure) is the one to add.
- No open voice question. The body speaks to no one; the two bookends address
  the reader as the template allows.
