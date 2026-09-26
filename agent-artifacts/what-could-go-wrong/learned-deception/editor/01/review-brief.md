# editor review-brief: what-could-go-wrong/learned-deception (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — assignment and the "Angle refinement" the writer drafted to.
- writer/01/brief.md (../../writer/01/brief.md) — the exact writer brief.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — read first.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — open when a claim needs testing; every example logged with its condition (game / prompted / lab).
- writer/01/draft-handoff.md (../../writer/01/draft-handoff.md).
- Article: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/learned-deception/library/what-could-go-wrong/learned-deception.html

Output:
- /home/user/the-nightly-build/.nb-work/what-could-go-wrong/learned-deception/agent-artifacts/what-could-go-wrong/learned-deception/editor/01/editorial-review.md

Proof (run yourself after edits, links included): /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/learned-deception/library/what-could-go-wrong/learned-deception.html --series what-could-go-wrong --repo /home/user/the-nightly-build

## Test hardest on this piece

- The behavioral definition holds throughout: no intent claim slips in (Park and
  Hagendorff both concede no intent). Flag any sentence that treats the model as
  having motives.
- The shown-vs-speculative line. Confirm the strong "unintended by-product of
  training" case rests on CICERO and Meta's negotiation agents; TaskRabbit,
  Hagendorff, and Scheurer are framed as elicited/existence-proof, not
  spontaneous deployment deception; poker is the intended-game boundary case.
  Each example's condition (game/prompted/lab) must be on the page.
- The distinction from the scheming cluster (deceptive-alignment, alignment-faking,
  sleeper-agents, cot-monitorability): confirm the piece does not re-litigate them
  and that the three-question test genuinely sorts learned deception from the
  unproven scheming claim. This test is the article's original work; make sure it
  earns that.
- Fairness: the argument is stated at full strength in its holders' words before
  it is tested; the present-day gap is named in BOTH directions (doom and
  dismissal). No company is treated as an authority.
- Attribution: Meta's "largely honest and helpful" phrasing is attributed as
  quoted-in-Park (Science gated). Confirm it is not presented as read firsthand.
- Every name/date/venue in headline, dek, subheads verified; data-nb-kind audited;
  every citation href opens to the source (gated Patterns/PNAS/Science DOIs that
  403 the probe are acceptable canonical homes).

## Optional furniture note

The writer cut a shown-vs-condition summary table for the word band (the condition
sort survives as cited prose). If you judge a small table would make the
shown-vs-speculative line land faster AND you can keep within the 1200-2200 band,
you may restore one; it is not required.

## Recent-pattern notes

- Reject the "You have probably ..." opener mold and the "By the end you will know
  A, B, and C" closer. Do not accept a dek/headings echoing deceptive-alignment
  ("handed a goal, not grown on its own") or value-lock-in ("feasible on paper and
  unshown"). Check against the recent what-could-go-wrong record.

## Your job

Decide whether it publishes; edit anything except the facts. Cut slop (placeholder
test on the edges), catch briefing leaks (read commission.md) and voice-guide
borrowings, check it repeats neither the recent record nor the scheming
neighbours. Fix what you can from the record and this checkout and run the proof
to BLOCK: 0 after edits (restamp if counts change; direct cuts that still pass owe
no writer round). Redraft only if it needs a different argument. Write
editorial-review.md (Correct / Reads well / The experience / Edits / Decision).
Report the review path, the decision, the final BLOCK count, and anything for the
orchestrator.
