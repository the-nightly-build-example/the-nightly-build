# writer brief: the-mechanics/prompt-sensitivity (01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the-mechanics prompt, template identity.
- writing-coach/01/voice-guide.md — how this lesson should sound, with exemplar passages.
- researcher/01/evidence.md — the complete claim set: verified figures, the modern-magnitude contradiction, source kinds.
- The initialized article at library/the-mechanics/prompt-sensitivity.html and its .nb-context/ contract.

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-mechanics/prompt-sensitivity/library/the-mechanics/prompt-sensitivity.html --series the-mechanics --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --series is required in local mode; use --no-check-links while iterating, links included until BLOCK: 0)

Set nb-meta the engine cannot compute: date 2026-08-10, harness claude-code-routine, model
"Claude Opus 4.8", and tags ["prompting", "robustness", "in-context-learning"]. nb stamp writes the counts.

Angle precision the evidence requires (the mechanism holds; the present-day magnitude does not, so be honest):
- The settled teaching is the mechanism: the model conditions on the literal token sequence, with no stored
  meaning held apart from surface form, so trivially different formats and example orders are different inputs.
  This is well-supported; keep it central.
- Do not imply a 2025 frontier chat model shows 76-point swings in ordinary use. The largest magnitudes come
  from 2021-2023 open models (GPT-2/3, LLaMA-2) under log-likelihood or exact-match scoring. Attribute the
  worked example to 1-shot LLaMA-2-7B (FormatSpread Table 1), not a frontier model.
- Report the modern-magnitude contradiction as the open part: Hua et al. 2025 find most of the measured spread
  in modern models collapses under LLM-as-judge grading, arguing today's sensitivity is more an artifact of
  evaluation than a model flaw. Mark settled (the mechanism, and that models are format/order sensitive) versus
  open (how large the effect is in current frontier models) at the right step.
- Keep three cases distinct throughout: the model is genuinely worse, the surface form moved the score, and the
  grader missed a correctly-phrased answer. Confirm any exact decimal in display text against the cited table.
- Series constraint: No code. Show format variants as inline data (the strings themselves), never a runnable
  harness.

Recent habits to break (from the-mechanics and the house record; the voice guide does not carry these):
- Do not use the mechanics headline molds "can't tell X from Y" or the "like any other token/word" tag, or the
  "A chatbot does X without Y" shape. Find this behavior's own surprise.
- Do not end the opener with an enumerated roadmap ("First... Then... And last..."). State stakes without
  touring the sections.
- Do not open the takeaway on a bare restated one-liner. Resolve what the opener set up.
