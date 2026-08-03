# Draft handoff: what-could-go-wrong/self-replication (02)

Targeted revision applying editor/01's two required prose fixes. No redraft;
all settled work preserved.

## Original work (one act)

Unchanged and still holds: the lesson sets every headline self-replication
number beside the exact harness condition that produced it, in a single
comparison, to show the four figures measure four different tasks and cannot be
stacked into a claim about autonomous replication.

## Editorial requests resolved

- **(BLOCKING) METR o1-preview harness condition corrected.** The prior draft
  attributed the "bare harness of a shell, Python, and a submit-answer tool" to
  both GPT-4o and o1-preview. The bare harness now carries only GPT-4o's ~30-min
  result; the o1-preview ~35-min result is now stated as reached "through a
  heavier 'advisor' scaffold, a second model rating its options, not that bare
  harness." This rests on evidence source s9 (METR o1-preview report,
  https://metr.org/evaluations/openai-o1-preview-report/, "Scaffolding"
  section), which records METR invested most of its scaffolding effort in an
  "advisor" architecture (a model generating and rating action options for a
  separate action model). The fix sharpens the dismissive point — o1-preview
  needed *more* scaffolding to reach roughly the same easier-than-ARA level — and
  no longer understates the help. The four-row table's METR row (~30 min, "bare
  shell-and-Python harness") is GPT-4o's number and remains correct; left as is.
- **(minor) Figcaption tightened to fit both models.** "agree and know how far
  more often than they finish" → "agree and know how more often than they
  finish." "Far" overstated Qwen's gap (100 agree / 90 finish); the tightened
  wording is honest for both Qwen (100/100/90) and Llama (100/70/50).

## Proof

`./nb stamp` then the final links-included
`./nb check --series what-could-go-wrong ... --library <checkout>` returns
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE**. Stamped words=2200,
reading_minutes=10, sources=13 (12 primary, 1 secondary).

No warnings left standing. To keep the piece inside the 1200–2200 lesson band
after the load-bearing o1-preview correction (which necessarily splits the two
models' harness attributions and adds words), the corrected sentence was written
tightly; word count settled exactly at 2200.

## Byline

Not touched this round, per brief — byline still reads "8 min read" while
stamped reading_minutes is 10. The orchestrator sets the byline last to match
the final reading_minutes (10).

## Open questions

None. The evidence pinned the o1-preview scaffold precisely (s9, "advisor"
architecture); no researcher or voice request is outstanding.
