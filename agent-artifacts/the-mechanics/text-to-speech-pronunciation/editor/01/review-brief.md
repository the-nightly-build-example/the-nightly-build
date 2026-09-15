# editor review-brief: the-mechanics/text-to-speech-pronunciation (editor/01)

Inputs (read in the order your skill names):
- ../../writing-coach/01/voice-guide.md — read first.
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the assignment, the backward chain to teach, boundaries, required contribution.
- ../../writer/01/brief.md — the exact writer brief (check authored text against it for leaks).
- ../../researcher/01/evidence.md — open on the skeptic read.
- ../../writer/01/draft-handoff.md — the original-work sentence; open on the reader read.
- Article under edit: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/agent-artifacts/the-mechanics/text-to-speech-pronunciation/editor/01/editorial-review.md

Proof (the orchestrator stamps and runs this after your edits): from repo root /home/user/the-nightly-build:
  ./nb check .nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html --series the-mechanics

Recent-pattern notes (flag any formula against these):
- Opener mold "The answer it won't give" / "A sentence the doctor never heard" recurs in this series.
- Closer mold "The tendency no decoding rule removes" / "Where the same X lives" recurs.
- Comma-triad and semicolon-reversal dek molds are banned by spec/headlines.md.

This round's focus:
- The lesson identity's stricter term rule: a technical term enters only when the lesson cannot proceed without it, defined in plain words in the same sentence or the one just before. The writer flagged one deliberate sequencing choice for your judgment: WaveNet's front-end/back-end split is introduced before "phoneme" is built up in the G2P section. Check the order holds for a first-time reader; fix it in place if a term is used before it is built.
- Verify the scoped figures against the evidence: the ~99% homograph accuracy is on a located-homograph benchmark over an 85.0% no-context baseline (not "homographs are solved"); the vivid normalization errors are an experimental RNN's output with a production FST filter noted, not what a shipping voice says; "almost always a front-end error" is the classic-pipeline claim, with Tacotron 2's ~23/100 unnatural-prosody sentences as a distinct back-end failure. Confirm the two real Siri failures ("Mobile, Ala.," "Des Moines") are each traced to the correct pipeline step.
- The required contribution is the reader being able to name which of two failures (normalization/G2P vs homograph) they just heard. Confirm that diagnostic actually lands and is the article's own work, not restated evidence.
- No code anywhere; confirm. The primary Background link is the-mechanics/speech-to-text-hallucination (opposite direction).
- The lesson allows only its two bookends to address the reader; hold all other prose to no-self-reference.
