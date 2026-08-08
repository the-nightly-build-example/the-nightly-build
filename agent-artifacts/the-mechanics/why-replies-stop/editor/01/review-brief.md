# editor review-brief: the-mechanics/why-replies-stop (01)

Inputs:
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/editorial-direction.md — the standard you enforce
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/writing-coach/01/voice-guide.md — read first; judge licensed forms against it
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/researcher/01/evidence.md — the claim set; open as an opponent
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/writer/01/brief.md — the EXACT writer brief (instruction-leakage checks)
- .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/writer/01/draft-handoff.md — original-work sentence (third read only)
- .nb-work/the-mechanics/why-replies-stop/library/the-mechanics/why-replies-stop.html — the article
- .nb-work/the-mechanics/why-replies-stop/.nb-context/ — template context

Output: .nb-work/the-mechanics/why-replies-stop/agent-artifacts/the-mechanics/why-replies-stop/editor/01/editorial-review.md

After any direct cuts, run `./nb stamp` (from /home/user/the-nightly-build); the
writer runs the proof. Do not edit markup, assets, or sources — route those.

Recent-pattern notes to enforce:
- the-mechanics shelf recently uses a line-by-line token table ("watch a product
  appear one line at a time") and a repeating declarative-heading cadence. Check the
  headings are named from this piece's own descent and the probability table is not
  that copied framing.

Round focus, hardest push:
- The two precision claims must hold exactly: base models emit a document-end token
  (NOT "never stop"); the stop-token probability micro-example is an ILLUSTRATION on
  a documented method, not measured numbers attributed to a named model. Confirm the
  prose labels it illustrative and attributes nothing false.
- Confirm the model-vs-serving-layer distinction stays two clearly named actors, and
  that `<code>` is used only for literal token strings a reader would match
  character-for-character.
