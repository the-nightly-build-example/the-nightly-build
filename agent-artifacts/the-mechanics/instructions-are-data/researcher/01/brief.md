# Brief 01 — researcher — the-mechanics/instructions-are-data

## Begin with these inputs only
- `agent-artifacts/the-mechanics/instructions-are-data/editorial-direction.md`
- `agent-artifacts/the-mechanics/instructions-are-data/commission.md` (behavior,
  step-by-step angle, required contribution, source obligations, starting sources)

Do not browse the archive as background. `nb` at `/home/user/the-nightly-build/nb`.

## Task
Follow the **researcher** skill (Skill tool: `researcher`). This lesson is
mechanistic, so the "numbers" are fewer; the burden is establishing each mechanistic
step from primary material.

- Establish, from a real **chat-template / special-token spec** (OpenAI ChatML docs,
  or a HuggingFace chat-template/tokenizer doc, or Llama/Mistral prompt-format docs),
  that role markers (system/user/assistant) are ordinary tokens in one sequence, not
  a protected channel. Quote the exact format.
- Establish that **instruction-following is trained**, from InstructGPT (Ouyang et
  al. 2022) — the reader already met it; pull the precise claim.
- Read **Simon Willison's** original prompt-injection posts (simonwillison.net, Sept
  2022 and key follow-ups): confirm he named the term and when, and his framing that
  it stems from concatenating trusted and untrusted text.
- Read **Greshake et al. 2023** (arXiv 2302.12173) for a demonstrated *indirect*
  injection through retrieved content — what they showed and on what systems.
- Read **Wallace et al. 2024** "The Instruction Hierarchy" (OpenAI) — the field's
  attempt to *add* priority; its existence proves the default has none. State exactly
  what it claims to achieve and its limits.
- Read **OWASP Top 10 for LLM Applications, LLM01: Prompt Injection** (owasp.org) as
  an authoring body's own document, and at least one frontier lab safety doc/system
  card acknowledging injection is unsolved.
- Contradiction/steelman: the best current defenses (instruction hierarchy,
  delimiting/spotlighting, filtering) and honest evidence they reduce but do not
  eliminate the problem.
- Classify each source primary/secondary with reason; verify claims (who coined the
  term and when; what the instruction-hierarchy paper actually promises); confirm
  every URL resolves.

## Source policy to meet
min 8 sources; **primary ≥ 4, secondary ≥ 1.**

## Output (write only this)
`agent-artifacts/the-mechanics/instructions-are-data/researcher/01/evidence.md`
(stable sections; in Numbers, record any concrete figures such as injection
success rates from the papers, with exact conditions). Return `DONE researcher <path>`.
