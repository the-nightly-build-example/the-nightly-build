# writer brief: the-mechanics/model-self-identity (01)

Inputs:
  ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
  ../../commission.md — the behavior, what to teach, distinctness lines, recent-pattern habits
  ../../writing-coach/01/voice-guide.md — how this lesson should sound; read before drafting
  ../../researcher/01/evidence.md — the complete claim set available to you
  ../../../../library/the-mechanics/model-self-identity.html — the initialized article to edit in place
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/model-self-identity/library/the-mechanics/model-self-identity.html --series the-mechanics --library /tmp/claude-0/library-checkout
       (iterate with --no-check-links; final run with links, until BLOCK: 0)

This round's focus:
- Use both cases to carry the mechanism split: DeepSeek V3 answering "ChatGPT"
  (TechCrunch, 27 Dec 2024; 5 of 8 generations; OpenAI's 29 Jan 2025 distillation
  accusation) and Grok in Dec 2023 citing OpenAI policy, which xAI's Igor
  Babuschkin attributed on the record to web text full of ChatGPT output while
  denying any training on OpenAI data. The two together show the same behavior
  from two different roots.
- Mark settled vs open exactly as the evidence record does: whether DeepSeek's
  slip came from web contamination or distillation is not knowable from outside
  (open); the Grok case is developer-attributed to web contamination.
- Handle the key contradiction: self-reports correlate with real exposure to
  OpenAI output (steelman: the report reflected provenance), but the Grok case
  shows the identical behavior with, per xAI, no OpenAI-data training, so a
  self-report cannot distinguish the two and is not proof of provenance. Keep
  xAI's 2023 denial and Musk's 2026 "Partly" testimony as separate events; do not
  read one onto the other.
- Display-text caution: the exact professional titles for Mike Cook and Heidy
  Khlaaf were not captured verbatim in the record. Do not put an unverified title
  in the headline, dek, or a subhead; if you use either name in display text,
  confirm the title first or omit the title.
- Ground the mechanism in the primaries: the OpenAI Model Spec's own example that
  a model has no independent knowledge of its base, Anthropic's published system
  prompt that injects identity, the imitation/distillation transfer result, and
  the introspection-is-unreliable finding.
- Link, do not re-teach: knowledge-cutoff, instructions-are-data, hallucination
  (draw the line: this is a specific mechanistic case, not generic fabrication),
  memorization, conversation-memory.
- Break the desk's recent comma-and dek mold.
