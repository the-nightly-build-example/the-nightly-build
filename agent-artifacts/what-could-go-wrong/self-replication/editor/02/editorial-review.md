# Editorial review: what-could-go-wrong/self-replication (editor/02)

Confirmation round scoped to editor/01's required work. I reread only the
sentences the two fixes touch, checked them against the owning evidence, and
swept the load-bearing invariants for regression. No new standard applied; no
settled matter reopened.

## Skeptic

The load-bearing fix landed and is now correct. Editor/01 broke exactly one
number: the METR o1-preview ~35-min result was attributed to the same "bare
harness of a shell, Python, and a submit-answer tool" as GPT-4o, in the costly
direction — understating the help. The revised passage now reads: GPT-4o
matched a human given 30 minutes "through a bare harness of a shell, Python,
and a submit-answer tool," while "o1-preview a month later matched a human
given about 35 — but through a heavier 'advisor' scaffold, a second model
rating its options, not that bare harness."

Checked descriptor by descriptor against evidence s9 (METR o1-preview report):
the entry records METR "invested most of its scaffolding effort in an 'advisor'
architecture (o1-preview/o1-mini generating and rating multiple action options
for a separate action model)" and quotes performance "comparable to humans
given around 35 minutes per task." The article's "heavier 'advisor' scaffold, a
second model rating its options" is a faithful compression of that architecture,
and the "not that bare harness" clause states the direction correctly:
o1-preview needed *more* scaffolding to reach the same easier-than-ARA level.
This sharpens the dismissive point instead of weakening it. The bare harness now
carries GPT-4o's ~30-min number alone. The four-row table's METR row (~30 min,
"bare shell-and-Python harness") is GPT-4o's figure and stays correct. The
"designed to be easier than ARA" claim is now attributed to "both reports" and
cites s8 and s9; the evidence confirms both reports state it. The fix holds and
is sourced.

## Cut

Nothing to cut. The one edit was surgical prose I do not own and did not need to
trim. Swept the invariants editor/01 settled:

- **Numbers never stacked.** "These figures cannot be stacked: each measures a
  different task under a different amount of help" survives verbatim, and the
  table caption still says the numbers "answer different questions and do not
  compose." Intact.
- **End-to-end ARA gap still named.** The penultimate body paragraph ("the
  capability the frameworks defined ... has no public measurement: no test yet
  builds that situation") and the takeaway ("What no public test has shown is
  the full loop run unaided") both stand. Intact.
- **No new tell, no broken sentence.** The revised sentence is grammatical; the
  em-dash carries a genuine reversal (more help for the same result), not a
  reflex flourish. The elided "minutes" after "about 35" reads cleanly against
  the parallel "30 minutes per task" immediately prior. No signpost, no
  self-grading, no prompt leakage entered with the edit.

## Reader

Unchanged from editor/01 and still earns its keep: every headline number set
beside the exact harness condition that produced it, then the demotion story
attributed document by document, then the Shanghai success-rate-is-not-risk
reframing. The o1-preview correction strengthens this — the piece now shows the
one case where more scaffolding bought the same modest result, which is the
essay's whole thesis working on its hardest example. Prose sits closer to the
voice-guide exemplars than to a median summary.

## Inspect visual evidence

The figcaption fix landed. It now reads "the models agree and know how more
often than they finish" — "far" removed. Honest for both series: Qwen 100 agree
/ 100 know-how / 90 finish (100 > 90, "more often" not "far more"), and Llama
100 / 70 / 50. The chart image, provenance, and numbers were verified sound in
editor/01 and are untouched this round.

## Edits

- None. Both required fixes were the writer's to make and landed correctly; no
  surgical cut was warranted. Ran `./nb check ... --revision --no-check-links`
  read-only: BLOCK 0, WARN 0, verdict PUBLISHABLE. Stamped counts stand at
  words=2200, reading_minutes=10, sources=13 (12 primary, 1 secondary).

## Required work

- **orchestrator** — Byline still reads "8 min read"; stamped reading_minutes is
  10. Reset the byline to "10 min read" to match before PR. Per the brief this
  reset is the orchestrator's, not the editor's.

## Decision

approve — both editor/01 required fixes landed correctly: the METR o1-preview
~35-min figure now carries its true "advisor" scaffold condition (checked
against s9) with the direction stated right, and the figcaption is honest for
both models; no invariant regressed. The only remaining item is the
orchestrator's byline reset to 10 min read.
