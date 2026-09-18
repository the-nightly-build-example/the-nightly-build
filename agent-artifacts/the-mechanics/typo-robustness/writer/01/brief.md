# writer brief: the-mechanics/typo-robustness (01)

Inputs:
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/editorial-direction.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/commission.md — angle, boundaries, reader
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/writing-coach/01/voice-guide.md
  .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/researcher/01/evidence.md
  the initialized article: .nb-work/the-mechanics/typo-robustness/library/the-mechanics/typo-robustness.html
  template contract and catalogs under .nb-work/the-mechanics/typo-robustness/.nb-context/

Output: .nb-work/the-mechanics/typo-robustness/agent-artifacts/the-mechanics/typo-robustness/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/typo-robustness/library/the-mechanics/typo-robustness.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/67c352f8-06f4-5e83-b6d0-5e6a0d5d584d/scratchpad/library-checkout
       (--no-check-links while iterating; nb stamp before final check; final check BLOCK: 0 with links included)

Recent shapes to break: the desk's standing headline mold is "A [system] does X but can't Y" (contrast mold). This behavior is a success; write a headline that states what actually happens, not a forced contrast. Avoid heading molds "Why the X land and the Y limps" and "The floor beneath the failure", and the imperative-opener rhythm of the last lesson. Headings in this piece's own nouns.

This round's focus (from the evidence record):
  - The "no spell-correction stage" point is established inferentially from complete architecture descriptions (Vaswani 2017; Radford 2019), not a quoted denial. State it as what the documented pipeline does and does not contain; do NOT present it as a direct quotation denying a spell-checker.
  - Use the verified live example: tiktoken v0.14.0 tokenizes `necessary` as 1 token but `neccessary` as 3 ("ne"/"ccess"/"ary"), plus the emoji byte-fallback example. Show the real split.
  - The settled/open split is not a clean binary. Present everyday-typo robustness as strong and well-explained, NOT proven or absolute: character-level perturbations that are neither invisible nor imperceptible still measurably degrade GPT-4-class models (PromptRobust 2023; 2025 Scientific Reports), and Pruthi et al. 2019 show the same subword flexibility gives an adversary precise leverage. Mark clearly what is settled vs open.
  - Link the-mechanics/glitch-tokens (the inverse failure) and word-embeddings / autoregressive-generation where taught rather than re-teaching. No code; a tokenization example shown as text or a small table is fine.
