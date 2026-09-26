# editor review-brief: the-mechanics/agent-loops (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — assignment, cause chain, and the "Angle refinement" the writer drafted to.
- writer/01/brief.md (../../writer/01/brief.md) — the exact writer brief.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — read first.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — open when a claim needs testing.
- writer/01/draft-handoff.md (../../writer/01/draft-handoff.md).
- Article: /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/library/the-mechanics/agent-loops.html

Output:
- /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/agent-artifacts/the-mechanics/agent-loops/editor/01/editorial-review.md

Proof (run yourself after edits, links included): /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/library/the-mechanics/agent-loops.html --series the-mechanics --repo /home/user/the-nightly-build

## Test hardest on this piece

- Huang et al. must read as SIGNAL-QUALITY (intrinsic self-correction often
  degrades; oracle/external signal helps), never as "models cannot self-correct."
- The greedy-decoding contribution (ReAct footnote 6) and the precise line drawn
  to the-mechanics/repetition-loops (shared decoding-level cause) — confirm it is
  accurate and not overstated as fully separate.
- The "ground" proposition and the temperature point are the lesson's own
  synthesis; confirm they are NOT cited as if a single paper established them
  (the-mechanics/sampling-temperature linked, not cited as owner).
- The concrete example (SWE-agent) is faithful to the record; the AutoGPT #1994
  instance carries its single-unreplicated caveat; any harness cap number carries
  its version caveat.
- NO code listings (series rule). The open question (why models under-weight
  their own error feedback) is marked as open.
- Every figure/number/name in headline, dek, subheads verified against the record;
  data-nb-kind audited; every citation href opens to the source.

## Recent-pattern notes

- Reject the "You have probably ..." / "Chatbots are good at ..." opener molds and
  the "By the end you will know A, B, and C" closer.
- Do not accept a dek copied from hangman's compact-causal mold; this dek should be
  its own. Check headings against the recent the-mechanics record so they are not
  stamped.

## Your job

Decide whether it publishes; edit anything except the facts. Cut slop (placeholder
test on the edges), catch briefing leaks (read commission.md) and voice-guide
borrowings, check it repeats neither the recent record nor a neighbour. Fix what
you can from the record and this checkout and run the proof to BLOCK: 0 after
edits (direct cuts that still pass owe no writer round). Redraft only if it needs a
different argument. Write editorial-review.md (Correct / Reads well / The
experience / Edits / Decision). Report the review path, the decision, the final
BLOCK count, and anything for the orchestrator.
