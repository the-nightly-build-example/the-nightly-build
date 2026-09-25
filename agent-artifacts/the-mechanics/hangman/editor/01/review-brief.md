# editor brief: the-mechanics/hangman (editor/01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md),
writer brief (../../writer/01/brief.md) + draft-handoff.md (../../writer/01/draft-handoff.md).
Article HTML: .nb-work/the-mechanics/hangman/library/the-mechanics/hangman.html
Output: ./editorial-review.md
Proof:  ./nb check .nb-work/the-mechanics/hangman/library/the-mechanics/hangman.html --series the-mechanics --repo $(pwd)

Follow the nb-editor skill. Correct, reads well, good to read.

Correctness priorities: verify the core mechanism against the evidence — chat
APIs are stateless, each turn conditions only on the visible transcript, a
withheld word is stored nowhere. The load-bearing precision is the EXCEPTION:
the piece must not claim models can never hold a commitment; scratchpad/hidden
reasoning/tool state can, within limits — check that this is stated accurately
and not overclaimed either way. Any transcript must be faithful to a cited
source, not fabricated as evidence (if the writer built an illustrative
transcript, it must be labeled as illustrative and consistent with how the
failure actually presents). Verify the conversation-memory link builds past it
rather than repeating it. Audit data-nb-kind (API docs / model papers primary;
behavior write-ups secondary). Open every href.

Recent-pattern enforcement: no reused "What the builders haven't settled"
heading or open-questions table; no mirror of the conversation-memory opener;
headings distinct; dek carries no comma-triad/"cause sits one level below" mold.
Read the last sentence of the piece and each section hardest. Confirm the
takeaway resolves the opener, teaches nothing new, and the body never refers to
itself. Redraft only for a wrong argument; else edit directly, re-run nb stamp +
proof to BLOCK: 0, record the decision.
