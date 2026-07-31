# Draft handoff — writer/01 — the-evidence/the-bitter-lesson

## Original work

This article takes Sutton's own worked examples (Deep Blue, AlphaGo) apart against
the primary record each system actually left, showing each one carried more
hand-built structure than the essay's four sentences report (Deep Blue's
grandmaster-tuned evaluation function, AlphaGo 2016's supervised training on human
game data), and then holds that finding, plus the essay's own citation record,
against two things no single source in the evidence record puts side by side: the
measured scaling evidence that came after it (Kaplan's curves, corrected by
Chinchilla's 400-model sweep) and the hand-designed systems the field built anyway
(the Transformer, RLHF/InstructGPT). No source in the evidence record makes that
three-way comparison; it is the article's own act of testing the slogan against the
record instead of restating either the essay or any one counter-source.

## Files changed

- `library/the-evidence/the-bitter-lesson.html` — full draft, written by editing the
  initialized skeleton in place (chrome, section order, and required labels kept as
  supplied). Body: `orientation` (what Sutton claims, in his words, with the chess
  example run through at full strength) → `examples-under-the-record` (Deep Blue's
  hand-tuned evaluation function; AlphaGo 2016 vs. AlphaGo Zero) →
  `the-measured-evidence` (Kaplan vs. Chinchilla as measured evidence, with a
  comparison table) → `what-came-after` (the essay's citation record, the
  Transformer, InstructGPT, Brooks's critique, closed with a holds-up grid). Bookends
  written last, after the body.
- `agent-artifacts/the-evidence/the-bitter-lesson/writer/01/draft-handoff.md` — this
  file.

## Proof result

```
/home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
```

Final run: `BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`.

Warnings encountered and resolved during drafting (none left standing):
- `B-SOURCES-FORM` (Sutton essay URL was `http://`) — fixed to `https://` in both the
  Sources entry and the Go-deeper link.
- `W-LENGTH-HIGH` (peaked at 2,365 words against the lesson band's 2,200 ceiling) —
  trimmed prose across all four sections and both bookends without cutting any of
  the three commissioned ideas or any cited claim; final count is 2,198 words,
  inside the 1,200–2,200 band.
- `W-SENTENCE-DENSITY` (several sentences over the density threshold, up to 63
  words/4 joins) — split every flagged sentence; the house style's own preference
  for short, single-purpose sentences made this a net improvement, not just a proof
  fix.
- `W-CITE-ORDER` (source 11 was first cited before source 8) — renumbered sources
  8–11 to match actual first-citation order in the prose rather than reordering the
  prose around the evidence record's own numbering.
- `W-SELF-COUNT` (`nb-meta.words`/`reading_minutes` were left at 0 during drafting)
  — set to the measured 2,198 words and 10 min read after the final trim pass.

Banned-terms audit (all within the merged budget): `leverage` used exactly once,
in Sutton's own quoted opening sentence ("general methods that leverage
computation"), per the brief's allowance; em-dash count 0; `load-bearing`,
`revolutionary`/`revolutionize`, `transformative`, `game-changing`, "AI race", and
`machinery` all 0.

`nb-meta.dek` and the rendered `.nb-dekline` verified character-identical.

## Remaining questions

None. All eleven sources in the evidence record are cited (9 primary, 2 secondary,
comfortably above the series' 6-source/3-primary/1-secondary floor); every
argument-bearing claim traces to a source the researcher verified firsthand. No
researcher or writing-coach gap was found during drafting.
