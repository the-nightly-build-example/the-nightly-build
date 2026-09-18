# editor review-brief: the-mechanics/typo-robustness (01)

Inputs to read (in the order the skill names):
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/writing-coach/01/voice-guide.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/editorial-direction.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/commission.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/writer/01/brief.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/researcher/01/evidence.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/writer/01/draft-handoff.md
  the article: .nb-work/the-mechanics/typo-robustness/library/the-mechanics/typo-robustness.html
  template context under .nb-work/the-mechanics/typo-robustness/.nb-context/

Output: .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/editor/01/editorial-review.md

Recent-pattern notes (break any edge/heading built like these):
  - Standing mechanics headline mold: "A [system] does X but can't Y" (poetic-meter, illegal-chess-moves). This behavior is a success, so a forced contrast headline is a formula here.
  - Recurring heading molds: "Why the X land and the Y limps", "The floor beneath the failure".
  - Recent openers use an imperative "Ask for a haiku, then count..." rhythm; don't let this one echo it.

This round's focus (break the highest-risk claims first):
  - The load-bearing mechanism claim: the writer resolved a real tension in the evidence — the folk assumption that training data is typo-laden versus Alahmari 2025's statement that LLM training sets are curated and "lack human-induced errors, such as typos" — by grounding meaning-preservation in BPE's frequency-based merge rule (a misspelling's fragments are common, well-trained pieces regardless of whether that misspelling appeared in training). Verify this resolution is faithful to the evidence and not an overreach; it is the piece's central original claim.
  - "No spell-checker" must read as an inference from the documented architecture (Vaswani/Radford), never as a quotation.
  - Verify the tiktoken example exactly (necessary = 1 token; neccessary = 3: "ne"/"ccess"/"ary"; emoji byte-fallback) against the evidence record.
  - Settled vs open must stay honest: everyday robustness strong but not absolute; PromptRobust, the 2025 Scientific Reports study, Pruthi's double-edged mechanism mark the open edge; Boucher's imperceptible attacks are categorically different from a typo. Confirm nothing overstates robustness as proven/absolute.
  - Confirm glitch-tokens (inverse failure), word-embeddings, autoregressive-generation/attention are LINKED in prose, not re-taught.
  - Length is at the 2200 ceiling; a required addition needs an equal cut (writer's dropped vocab-size figures are optional — do not require them).
