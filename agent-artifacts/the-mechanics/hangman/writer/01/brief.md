# writer brief: the-mechanics/hangman (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md).
Article + context under .nb-work/the-mechanics/hangman/ (HTML at
library/the-mechanics/hangman.html; .nb-context/ has furniture + contract).
Output: ./draft-handoff.md (+ edited article HTML)
Proof:  ./nb check .nb-work/the-mechanics/hangman/library/the-mechanics/hangman.html --series the-mechanics --repo $(pwd)

Work from these inputs only; ask me where something is missing.

Focus: work backward from the behavior to ground. Spine: the model "cheats" at
hangman (a concrete, faithful transcript showing inconsistent answers) -> it has
no hidden state, so a withheld word is written nowhere and does not exist; each
turn regenerates from the visible transcript -> distinguish the settled claim (a
plain chat holds no commitment) from the real exception (scratchpad/hidden
reasoning/tool state can) -> where trusting a chatbot to "hold" something
unwritten bites in real use. Original-work sentence in draft-handoff.md: the
model is not lying about a secret it holds; it has no secret to lie about, and
"cheating at hangman" is what a stateless system looks like when asked to hold a
commitment. Link conversation-memory and build past it (commitment, not recall);
do not re-teach the resend.

Any transcript must be faithful to the evidence's sources, not invented as
captured proof. Be precise about the exception; do not claim models can never
hold state.

Recent-pattern notes to break (the-mechanics): do NOT reuse the "What the
builders haven't settled" heading or an open-questions table for the settled/
exception section; do not mirror the conversation-memory opener. Headings
distinct from each other. Dek: one lean sentence with a concrete detail; no
comma-triad, no "the cause sits one level below" mold.

Furniture: a short transcript (as a note or a styled block per the catalog) or a
small table contrasting "performing a commitment" vs "holding one" can carry the
point; use documented markup only. nb-meta: date 2026-09-25, harness+model
"Claude Opus 4.8", 4-5 tags, dek identical to rendered dekline. nb stamp, then
proof to BLOCK: 0.
