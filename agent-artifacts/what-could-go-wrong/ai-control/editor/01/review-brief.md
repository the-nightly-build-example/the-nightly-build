# editor review-brief: what-could-go-wrong/ai-control (01)

Inputs (read all):
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/editorial-direction.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/commission.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/writer/01/brief.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/writing-coach/01/voice-guide.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/researcher/01/evidence.md
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/writer/01/draft-handoff.md
- Article: .nb-work/what-could-go-wrong/ai-control/library/what-could-go-wrong/ai-control.html
- Template context dir: .nb-work/what-could-go-wrong/ai-control/.nb-context/

Output:
- .nb-work/what-could-go-wrong/ai-control/agent-artifacts/what-could-go-wrong/ai-control/editor/01/editorial-review.md

Proof (read-only if you want to confirm your edits; orchestrator stamps before PR):
- ./nb check .nb-work/what-could-go-wrong/ai-control/library/what-could-go-wrong/ai-control.html --series what-could-go-wrong --library /home/user/library-checkout

Round focus: verify the numbers discipline — every control safety/usefulness
figure carries its exact setup and audit budget, and the four papers' numbers
are never ranked against each other (different tasks/models/budgets). Confirm the
demonstrated-vs-projected line holds and that the "degrades even at human-level
settings" refinement is supported by the evidence record (Control Tax low-budget
failure; the adaptive-injection 375-samples-scored-0 result), not overstated.
Check the proponents' stated limits are in their own words. The writer left ONE
warning standing: a ~50-word colon-plus-three-parallel-clauses sentence in the
final section, defended as the voice guide's Schneier register — judge it against
spec/slop.md and spec/editorial.md punctuation (keep it only if each clause
carries a fact/step; otherwise trim). Reassess the headline as the largest claim.

Recent-pattern notes (compare deks, headings, openers, closers, furniture; one article cannot show these):
- Deks: the desk's demonstrated-vs-projected framing is substance, but cut the recurring stock phrasings ("None has yet", "feasible on paper and unshown", "so far only in simulation") and the machine molds (comma-triad, semicolon-reversal, negative-parallelism, suspended question).
- Headings: full-sentence claims are house style; break any reuse of the "full strength / the opposite mistake / what the studies can and cannot show" heading set and any negative-closer or comma-and heading.
- Catchphrase/self-grading tells and decorative "underscoring/highlighting" verbs: cut.
- Press voice: no doom, no hype; the takeaway must not restate the finding as a verdict block; the body addresses no one.
