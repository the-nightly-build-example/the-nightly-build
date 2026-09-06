# researcher brief: the-mechanics/overthinking (01)

Inputs:
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/editorial-direction.md
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/commission.md

Output:
- .nb-work/the-mechanics/overthinking/agent-artifacts/the-mechanics/overthinking/researcher/01/evidence.md

Establish the causal chain from primaries, with locators:
- That reasoning models are trained (usually RL on outcomes) to emit a long
  chain before answering, and that test-time compute scales with generated
  tokens: an o1/o3 or DeepSeek-R1 primary describing test-time scaling and
  RL-trained long reasoning. Get concrete numbers on how much compute/latency a
  long reasoning pass costs.
- The overthinking behavior on easy inputs: a primary that measures reasoning
  models spending excessive tokens on trivial problems (e.g. "Do NOT Think That
  Much for 2+2?" or comparable 2024-25 overthinking study). Record the exact
  demonstration (token counts on simple vs hard problems) and any efficiency
  metric it defines.
- That more reasoning is not monotonically better: Anthropic's "Inverse Scaling
  in Test-Time Compute" (2025) and/or a study showing accuracy plateaus or drops
  as reasoning length grows, and answer-switching from a correct early answer.
  Record the tasks, the direction and size of the effect, and the conditions,
  with denominators. This is the most breakable claim; pin it to its owner.
- A mitigation primary: thinking-budget / reasoning-effort controls, length
  penalties, or adaptive routing, and what it achieved.

Record contradictions in full: where extended reasoning clearly helps (hard math/
code), so the piece does not overclaim that reasoning hurts. Note which framing
of the cause (RL length bias vs missing difficulty estimate vs budget policy) is
supported vs speculative. Confirm every URL resolves to the source's own page.
Classify each primary/secondary. Meet the 8-source, 4-primary / 1-secondary floor
with sources that change the interpretation.
