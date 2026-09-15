# writer brief: the-mechanics/text-to-speech-pronunciation (01)

Inputs:
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the behavior, the backward chain to teach, boundaries, required contribution, source floor, recent-pattern habits to break.
- ../../writing-coach/01/voice-guide.md — how this piece should sound (read before drafting).
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers exactly and address its Contradictions.
- Initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html
- Template context: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/text-to-speech-pronunciation/agent-artifacts/the-mechanics/text-to-speech-pronunciation/writer/01/draft-handoff.md

Proof (from repo root /home/user/the-nightly-build; iterate with --no-check-links, final with links until BLOCK: 0):
  ./nb stamp .nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html
  ./nb check .nb-work/the-mechanics/text-to-speech-pronunciation/library/the-mechanics/text-to-speech-pronunciation.html --series the-mechanics

This round (honor these attributions from the evidence Contradictions):
- Attribute examples to the right system type. The vivid "read as the wrong words" normalization errors (e.g. a currency amount voiced as "euros," a unit as "two units") come from an experimental pure-RNN normalizer in Sproat & Jaitly, and that same paper shows production systems add a finite-state filter to suppress those "silly" errors. Present them as evidence of the mechanism and difficulty, not as something a deployed voice reliably says. For real deployed failures, use the documented named ones (Tacotron 2 on names; Siri on "Mobile, Ala.," "Des Moines").
- Keep the homograph figure honest: ~99% is measured on a balanced set of ~162 known homographs with the target word already located, over an ~85% most-frequent-word baseline; it does not mean homographs are solved in the wild. Use it exactly as scoped.
- "Almost always a front-end error" is a classic-pipeline claim; note honestly that end-to-end systems (Tacotron 2) also produce back-end failures (skipped words, prosody). Mark settled vs open as the series demands.
- The mechanism holds: pronunciation is decided in the text-analysis front end before any audio exists; WaveNet still consumes front-end phonemes; Tacotron 2 trains on pre-normalized text and still mispronounces names. Reach the floor step (a genuinely ambiguous sentence no system can resolve).
- Link, do not re-teach: the-mechanics/speech-to-text-hallucination is the primary Background link (Whisper, the opposite direction). No code.
- Break the "The answer it won't give" opener mold and the "Where the same X lives / The tendency no rule removes" closer mold. Fresh dek, no comma-triad / semicolon-reversal.
- nb-meta: date "2026-09-15", harness "claude-code-routine", model "claude-sonnet-5".
