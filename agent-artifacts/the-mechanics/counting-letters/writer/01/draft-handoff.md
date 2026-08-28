# Draft handoff: the-mechanics/counting-letters (01)

## Original-work sentence
The article stages the evidence's four scattered primary findings as one
step-by-step descent on a single word, strawberry, that draws the line the
record asserts but never walks a reader across: settled, that byte-pair
encoding tokens are frequency-merged word-pieces so a token carries no direct
index of its letters; open, how much of that buried character information a
model recovers, which is why it can spell the word out yet miscount it.

## Proof result
`./nb check ... --series the-mechanics` (links included): BLOCK: 0, WARN: 0,
verdict PUBLISHABLE. Stamped words=2069, reading_minutes=9, sources=10 (8
primary, 2 secondary). No warnings intentionally left; all six from the first
pass were fixed (three sentence-density splits, one cite-order renumber so
first-appearance is ascending, and the two self-count notes resolved by stamp).

The proof ran without `--library`, so its note says open-mode dedupe and
commission checks were skipped (no published library state is present in this
workspace). Nothing in the file depends on that; flagged only so the CI/PR proof
against real library state is the one that closes those checks.

## Record traps, handled
- The GPT-4o/Claude "two r's" instance is attributed in prose as reported by
  TechCrunch and carries `data-nb-kind="secondary"` (source 1). All mechanism
  claims rest on primaries; the secondary carries only the public instance.
- CUTE (source 8) is cited only for spelling, character containment, and
  manipulation, never as a counting or letter-counting benchmark. The four
  contradiction findings (spell-but-not-manipulate; failure survives splitting,
  <=3.5%; probe recovers characters; finer tokenization helps) are all rendered.

## Continuity
Three neighbors are linked, not re-taught: multilingual-gap and text-in-images
and getting-math-wrong sit in the Background band; text-in-images and
getting-math-wrong are also distinguished in the closing section (same root
cause different surface; different mechanism, do not conflate). The tokenizer
and byte-pair encoding are defined on first use here, as the voice guide
requires, rather than deferred to those links.

## Open question for the editor
Neighbor link text and hrefs are unverified. No published library is reachable
from this workspace (`nb history` returns nothing, no library checkout is
mounted), so the three Background rows use descriptive titles and inferred slugs
(`multilingual-gap`, `text-in-images`, `getting-math-wrong`) built from the
commission's descriptions. The link-checked proof passed because it verifies
only `data-nb-source` URLs, not internal bookend links. Confirm the real
published slugs and titles against library state before publish.
