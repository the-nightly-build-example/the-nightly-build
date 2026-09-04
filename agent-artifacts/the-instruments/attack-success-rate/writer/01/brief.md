# writer brief: the-instruments/attack-success-rate (01)

Inputs:
- .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/writer/01/brief.md — this brief
- .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/editorial-direction.md — the standing editorial direction
- .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/commission.md — the assignment and boundaries; its "habits not to inherit" binds your headline, dek, and section headings
- .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/writing-coach/01/voice-guide.md — how this piece should sound
- .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/researcher/01/evidence.md — your complete claim set; use Numbers and Contradictions exactly
- the initialized article: .nb-work/the-instruments/attack-success-rate/library/the-instruments/attack-success-rate.html
- the effective template contract and furniture catalogs under .nb-work/the-instruments/attack-success-rate/.nb-context/

Output: .nb-work/the-instruments/attack-success-rate/agent-artifacts/the-instruments/attack-success-rate/writer/01/draft-handoff.md

Proof: from the repo root, ./nb check .nb-work/the-instruments/attack-success-rate/library/the-instruments/attack-success-rate.html --series the-instruments

Record model claude-opus-4-8, harness claude-code-routine, and date 2026-09-04 in nb-meta.

Two decisions the evidence record settles:
- The number misleads in both directions, and the piece should teach both as
  failure modes of the same number: a lenient judge overstates jailbreaks (it
  counts vacuous non-refusal as a success, as with the Gaelic case), and a static
  benchmark understates exposure when a cheap new attack defeats it (the
  past-tense rewrite, the DeepSeek R1 result). Do not present only the
  low-score-defeated direction.
- You may cite XSTest once as a primary for the over-refusal confound (a model
  lowers its ASR by refusing more, which trades against a measurable
  over-refusal cost the number hides). Link the published over-refusal mechanics
  lesson in prose for the mechanism rather than re-teaching it. Attach every rate
  to the attack and the judge that produced it; a bare ASR is not a figure.
