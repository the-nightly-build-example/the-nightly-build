# editor review-brief: what-could-go-wrong/capability-elicitation (editor/01)

Inputs:
- ../../editorial-direction.md — the standard to edit against
- ../../commission.md — the assignment, the desk's arc, the boundaries
- ../../writer/01/brief.md — the exact writer brief (check the draft against it for leakage and carried decisions)
- ../../writing-coach/01/voice-guide.md — read first; register and exemplar passages to check borrowed phrasing against
- ../../researcher/01/evidence.md — the claim set; reread cited passages for what breaks a claim
- ../../writer/01/draft-handoff.md — original-work sentence (open on the third read) and the writer's note
- the article: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/capability-elicitation/library/what-could-go-wrong/capability-elicitation.html
- template context: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/capability-elicitation/.nb-context/

Round's focus (things to check hardest for this piece):
- The distinction from the reader's existing `sandbagging` lesson must be explicit and early: sandbagging is the model's deliberate choice to underperform; the elicitation gap is that a cooperative model's measured capability still depends on tester effort. Confirm the piece does not blur into sandbagging.
- The shown-versus-speculative line: elicitation figures (prompting, scaffolding, repeated sampling, cheap safety-removal) are the shown half; the lurking-dangerous-capability worry is inference. Confirm the piece lands on "a passed eval cannot prove safety" without tipping into "the danger is therefore there," and that repeated-sampling gains are noted to collapse without a verifier.
- No company named as an authority; doom and dismissal held equidistant. Steelman both directions of overconfidence.
- Both Background links (sandbagging, open-weights-release) resolve in the library checkout; the writer verified this.

Recent-pattern notes (compare edges, headings, dek against the recent What Could Go Wrong record):
- The closing beat "the researchers built the setup themselves" and openers naming a thinker who "argues/predicted" recur across recent lessons; flag either as formula.
- Section headings must be this argument's own steps, never stock labels.
