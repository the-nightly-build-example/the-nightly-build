# Draft handoff: what-could-go-wrong/encoded-reasoning (01)

## Original work

The article turns a scattered set of papers into one ordered test a lay reader
can run for themselves: it separates ordinary unfaithful rationalization
(Turpin, Lanham) from deliberate concealment, sorts the concealment evidence
into hand-built-on-a-toy-task, emergent-from-ordinary-training, and
still-unobserved, and places the live worry in the emergent middle tier that
both the alarm and the dismissal skip over. The evidence record names the
three-tier correction but does not teach it; the article builds the path
(the "words already come apart" section, then the three tiers weighed against
what each paper actually measured in "How far the evidence actually reaches").

## Proof

Command (from brief, links included):
`./nb check .nb-work/what-could-go-wrong/encoded-reasoning/library/what-could-go-wrong/encoded-reasoning.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout`

Result: `BLOCK: 0` / `WARN: 0` / verdict PUBLISHABLE. `nb stamp` run before the
final check (words=2049, reading_minutes=9, sources=8).

Three W-SENTENCE-DENSITY warnings from the first (`--no-check-links`) pass were
fixed, not carried: the Roger & Greenblatt caveat sentence, the crux sentence in
"How far the evidence actually reaches," and the Potts closing sentence were each
split. The Potts split also removed an "optimized for X, not for Y" construction
in favor of "optimized to get answers right, with nothing rewarding honesty."

## Warnings intentionally left

None. The final proof is clean (WARN: 0).

## Notes for the editor (not warnings)

- Source composition: 8 sources, 7 primary + 1 secondary (Potts), meeting the
  what-could-go-wrong/lesson floor (>=8, >=4 primary, >=1 secondary). Numbered in
  first-citation order; each `data-nb-kind` carried from the evidence record.
- No source asset or chart was used. The evidence offered R&G Figure 1 as a
  candidate asset; the two approximate accuracies (~80% / ~54%) plus the
  ~3 bits/KB ceiling are carried by a stat strip and stated in prose as
  approximate, which serves the "hidden channel bought real performance" point
  without over-precise capture from a plot.
- Jose et al. model count is stated as "about fifteen, all but the Claude
  models." The evidence flagged the exact count as read from the abstract and
  worth confirming against the paper body; the phrasing is deliberately
  approximate so the claim does not outrun what was verified.
- Lab statements (Baker et al./OpenAI; the cross-lab monitorability position
  paper; Lanham et al./Anthropic) are attributed to their authors as stated
  positions, with no company named as an authority, per the series direction.
- Background links to `../the-mechanics/thinking-out-loud.html` and
  `../what-could-go-wrong/cot-monitorability.html` are plain prose/band links,
  not numbered sources, per press editorial.
