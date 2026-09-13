# editor review-brief: the-mechanics/speech-to-text-hallucination (editor/01)

Inputs:
- ../../editorial-direction.md — the standard to edit against
- ../../commission.md — the assignment, the work-backward arc, the boundaries
- ../../writer/01/brief.md — the exact writer brief (check the draft against it for leakage and carried decisions)
- ../../writing-coach/01/voice-guide.md — read first; register and exemplar passages to check borrowed phrasing against
- ../../researcher/01/evidence.md — the claim set; reread cited passages for what breaks a claim
- ../../writer/01/draft-handoff.md — original-work sentence (open on the third read) and the writer's editor-facing note
- the article: /home/user/the-nightly-build/.nb-work/the-mechanics/speech-to-text-hallucination/library/the-mechanics/speech-to-text-hallucination.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/speech-to-text-hallucination/.nb-context/

Round's focus (things to check hardest for this piece):
- Rates must carry scope. There is no single trustworthy hallucination rate: confirm the Koenecke 1.4% figure is scoped (aphasic interview audio, chosen for long pauses, version-dependent) and that any other rate carries its scope; no lone headline rate.
- The writer's note: a "recognize speech / wreck a nice beach"-type homophone pair is a deliberate hypothetical illustration of mishearing, not a Whisper output and not from the evidence record. Confirm it reads unmistakably as an illustration, never as a sourced result.
- Mechanism accuracy: the decoder is an audio-conditional language model that falls back on its language prior when the audio carries little; the invention over silence is a distinct failure from mis-hearing faint speech. Check the draft keeps that line and does not overclaim "from digital silence" where the evidence says low-information audio broadly.
- Confirm the chatbot-hallucination lesson is linked, not duplicated; keep the focus on the audio-to-text modality and the empty-input trigger.

Recent-pattern notes (compare edges, headings, dek against the recent Mechanics record):
- Headlines built on "Ask [system] for X and it Y" or "A model can X and still Y" recur; flag any echo as formula.
- Section headings must be this behavior's own steps, never stock labels; do not reuse a prior mechanics piece's section shape.
