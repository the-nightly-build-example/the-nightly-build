# Draft handoff: the-mechanics/speech-to-text-hallucination (01)

## Original-work sentence
The article assembles the scattered evidence into one backward causal chain, from a fabricated clinical line down to the single fact that Whisper's output stage is an audio-conditional language model, so that the invented sentence over silence reads as the designed output of that stage rather than a glitch; and it turns the sources' incompatible hallucination "rates" into the lesson that no single rate exists, because each figure measures different audio, a different Whisper version, and a different unit (per-segment vs per-file). The chain and the rate table are the visible work; neither the evidence record nor any single source does either.

## Proof
`nb stamp` then `nb check ... --series the-mechanics --library <checkout>` (links included): BLOCK: 0, WARN: 0, verdict PUBLISHABLE. words=2121, reading_minutes=9, sources=8 (7 primary, 1 secondary). No warnings left standing. Preview build merges the draft cleanly; the rate table and the "What Whisper writes over silence" note render, and the `orientation` section id is intact (its heading is named for the piece, "A sentence the doctor never heard").

Handled during iteration: restored the required `data-nb-section="orientation"` id (renaming it had also pushed the flex-section count to 5, over the 0–4 cap); renumbered citations to first-appearance order after Frieske's distinction landed before Koenecke's rates (Frieske=s3, Koenecke=s4, discussion #928=s6, model card=s7); split several dense sentences to clear W-SENTENCE-DENSITY.

## Notes for the editor
- The "recognize speech" / "wreck a nice beach" pair is a deliberate generic illustration of what a mishearing is, presented hypothetically ("the audio says... and the transcript reads..."), not a Whisper output and not drawn from the evidence record. It is there to define the contrast class before the invention is defined; flagging so it is not read as an uncited claim.
- AP is carried as the single secondary (`data-nb-kind="secondary"`), consistent with the evidence record's framing; the other seven sources are primary, meeting the ≥4-primary / ≥1-secondary floor.

## Open evidence/voice questions
None blocking. The two contradictions the brief flagged (no single trustworthy rate; low-information audio rather than strict digital silence) are taught explicitly rather than smoothed over. Nabla's dispute is represented in both the orientation and the rate table with its scope attached.
