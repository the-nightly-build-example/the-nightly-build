# editor brief: what-could-go-wrong/ai-environmental-cost (editor/01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md),
writer brief (../../writer/01/brief.md) + draft-handoff.md (../../writer/01/draft-handoff.md).
Article HTML: .nb-work/what-could-go-wrong/ai-environmental-cost/library/what-could-go-wrong/ai-environmental-cost.html
Output: ./editorial-review.md
Proof:  ./nb check .nb-work/what-could-go-wrong/ai-environmental-cost/library/what-could-go-wrong/ai-environmental-cost.html --series what-could-go-wrong --repo $(pwd)

Follow the nb-editor skill. Correct, reads well, good to read.

Correctness priorities: recompute every figure against the document that owns it,
with its accounting boundary and base year — training carbon (Strubell,
Patterson, Luccioni), aggregate electricity (IEA), projections (de Vries).
Verify the Strubell number is stated as the paper stated it (it was widely
misquoted). The load-bearing move is the per-unit vs aggregate distinction; if
the draft conflates a per-query figure with an aggregate claim, that is a
correctness fix. Verify the traced per-query "walked-back" figure is represented
accurately, with the correction. Present both alarmist and dismissive sides
fairly before naming the gap; name no company as an authority. Audit
data-nb-kind (Strubell/Patterson/Luccioni/IEA/de Vries primary; reporting
secondary). Open every href.

Recent-pattern enforcement: no "present-day relocation" closing mold; table (if
any) not a copy of a prior shape; dek carries no "and no one has measured"/
comma-triad mold; headings distinct. Read the last sentence of the piece and
each section hardest, and confirm the piece names the gap and leaves the
judgment to the reader. Confirm the takeaway resolves the opener and the body
never refers to itself. Redraft only for a wrong argument; else edit directly,
re-run nb stamp + proof to BLOCK: 0, record the decision.
