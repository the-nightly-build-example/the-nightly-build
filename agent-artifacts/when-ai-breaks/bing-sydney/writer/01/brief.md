# writer brief: when-ai-breaks/bing-sydney (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- ../../commission.md — the incident, the angle, source direction, nb-meta values.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only from it.
- ../../../../.nb-context/ — the effective template contract and runtime assets.
- ../../../../library/when-ai-breaks/bing-sydney.html — the initialized article to edit in place.

Output: ./draft-handoff.md

Proof (run from repo root; iterate --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/when-ai-breaks/bing-sydney/library/when-ai-breaks/bing-sydney.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/53d4ed2b-ac4b-53e6-97a0-447483501c29/scratchpad/library-checkout --no-check-links`
- Final: same WITHOUT `--no-check-links`, and run `./nb stamp` first, until `BLOCK: 0`.

nb-meta: date `2026-08-11`, harness `claude-code-routine`, model `Claude Opus 4.8`,
three descriptive tags in nb-meta directly. Keep nb-meta `dek` identical to the
rendered dekline.

This round's focus: tell the incident in order (what Bing chat was and when it
launched, what it did, who it affected, what Microsoft did afterward), naming
people and dates; then explain why that kind of system fails that way — persona
instability under long context and no separation of instructions from data — using
what the course taught; then close on where the weakness lives now. Keep the sharp
line the record demands: what transcripts and Microsoft's statements show firsthand
versus what is inference about the model's internals (label inference). A single
screenshot shows the model produced that text on that occasion, not that the
behavior was universal. Link `the-mechanics/instructions-are-data`,
`the-mechanics/sycophancy`, `when-ai-breaks/microsoft-tay`, and
`when-ai-breaks/air-canada-chatbot` in Background rather than re-teaching. Link
only already-published library pages — do NOT link tonight's siblings (including
the-mechanics/conversation-memory, which is not yet published).

Habits not to inherit (house formulas across the last three of every desk):
- No "By the end you will be able to..." close on the opener.
- No second-person "ask the two questions..." / "Two questions are worth carrying
  into any [system]..." checklist as the takeaway — this exact move closes every
  recent when-ai-breaks piece (robodebt, tesla, optum). Break it.
- No "demonstrated-vs-unproven" final sort.
- The desk's recent openers all use a present-tense generalized-practice frame
  naming the deployers in a comma list plus a scale-of-reach number
  ("Hospitals, insurers, and clinics rank... about 200 million people"); do not
  reuse that shape. Recent takeaways open on a "the tool was not broken / did
  exactly what it was built to do" working-as-designed reframe — do not reuse it.
  Vary headings away from the desk's heavy "The X that Y" relative-noun-phrase
  mold and the "the same [gap] still runs / on the road now" final-heading turn.
- No "this desk" self-reference.
