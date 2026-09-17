# editor review-brief: the-mechanics/poetic-meter (01)

Inputs:
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/commission.md` — the assignment, boundaries, reader
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/writer/01/brief.md` — the exact writer brief, including this round's reframe
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/writing-coach/01/voice-guide.md` — how the piece should sound; read first
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/researcher/01/evidence.md` — the claim set
- `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/writer/01/draft-handoff.md` — the original-work sentence (open on the third read)
- Article: `.nb-work/the-mechanics/poetic-meter/library/the-mechanics/poetic-meter.html`
- Template context: `.nb-work/the-mechanics/poetic-meter/.nb-context/`

Output: `.nb-work/the-mechanics/poetic-meter/agent-artifacts/the-mechanics/poetic-meter/editor/01/editorial-review.md`

Proof (the writer's exact command; the orchestrator re-stamps and re-proves after your direct cuts):
`./nb check .nb-work/the-mechanics/poetic-meter/library/the-mechanics/poetic-meter.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

Recent-pattern notes (compare edges, headings, dek against these):
- the-mechanics recently used "A [system] does X for one of two reasons"
  (text-to-speech-pronunciation), "answers silence with a sentence no one spoke"
  (speech-to-text-hallucination), and watermarks' dek tail "a mechanism distinct
  from the rarer case where...". Flag any echo of these molds.
- Paper-wide molds to catch: the two-sentence "[Claim]. [Terse rebuttal]."
  headline; the comma-triad dek closed with "and"; a "What <Person> saw in
  <place>" heading; a penultimate section built as "what would settle it / what
  it actually shows". Every subhead a full declarative sentence in one rhythm is
  itself a formula.

This round's focus:
- Verify the reframe is honored: the piece must not claim the model has "no
  phonological representation." Sound is latently present (phonemes recoverable
  from embeddings ~96%) but unreliable and not used for exact counting. Push on
  any sentence that overstates the mechanism.
- The syllable-counting measurement is the spine; metrical-foot/scansion claims
  must stay proportionate to the thin direct evidence. Check that the settled
  claims and the open question (why some models scan better) are marked as such.
- Confirm the three taught lessons (autoregressive-generation, counting-letters,
  tokenization) are linked, not re-taught.
