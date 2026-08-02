# Commission: the-mechanics/over-refusal

## Assignment
A lesson on the behavior **the model refuses a harmless request.** The Mechanics
desk starts from a behavior anyone who uses AI has seen and works backward to
what produces it, step by step, to ground.

## Angle
Everyone has hit "I can't help with that" on something plainly benign: a
fictional villain's dialogue, how a common medication works, a chemistry
homework problem, the name of an attack move in a video game. Work backward: a
base model does not refuse anything; refusal is installed by fine-tuning; and it
is installed as a crude, surface-triggered switch, which is exactly why it
misfires on innocent prompts. Go down until the reader hits ground: a step
below which nothing changes the answer.

## Intended reader
House reader: smart, widely read, no codebase time. Teach on the spot, in plain
words: what "fine-tuning" adds on top of a pretrained model, what the "residual
stream" / an internal "direction" means when you need it, and keep it concrete
with real examples. Assume algebra and probability. No code.

## Contribution this piece must make
A reader who finishes can explain **why** a model refuses a harmless request:
that refusal is a trained behavior generalizing from labeled examples by
surface features rather than true intent, and that internally it looks like a
single crude switch rather than genuine understanding of harm. They can then
tell when someone's explanation of a refusal skips a step (e.g. treats the
model as "deciding" something is dangerous). The visible original work is the
step-by-step causal chain from the observed refusal down to the mechanism, with
each step marked settled engineering or open question.

## Teach at most three ideas, completely
1. **Refusal is added, not native.** The pretrained model just predicts likely
   next text; it will happily continue almost anything. Instruction and safety
   fine-tuning (supervised examples plus reinforcement learning from human or AI
   feedback) shift the output distribution so certain categories draw a refusal.
   The model learns the pattern from examples, so it generalizes by what those
   examples had in common on the surface (words, topics), not by a real theory
   of harm. Worked example: a benign request containing a trigger word or topic
   gets refused (false positive) = over-refusal.
2. **Internally, refusal is a crude switch.** Arditi et al. (2024, NeurIPS)
   found that across many open models, refusal is mediated largely by a single
   direction in the model's internal activations: erase that direction and the
   model stops refusing harmful prompts; add it and the model refuses even
   harmless ones. Explain what that shows: refusal behavior is shallow and
   nearly linear, not a considered judgment, which is why it both over-fires and
   can be switched off. Worked example from the paper's own results.
3. **Measuring the misfire, and the tradeoff.** Over-refusal benchmarks (XSTest,
   Röttger et al. 2024; and a broader over-refusal benchmark) quantify how often
   safe prompts get refused. There is a real safety/helpfulness tension: push
   refusals down and you risk letting genuinely harmful requests through (the
   mirror image of a jailbreak — link the covered jailbreaks lesson). Mark what
   is settled (fine-tuning causes refusal; it generalizes by surface features)
   and what is open (why refusal is represented so linearly; how to cut over-
   refusal without raising under-refusal).

If space is tight, keep ideas 1–2 whole and compress idea 3's benchmark detail.

## Source obligations (the-mechanics lesson)
- Minimum 8 sources; primary ≥ 4, secondary ≥ 1.
- Mechanism claims come from the primary papers, read first-hand.
- Every quantitative claim (refusal rates, effect of the direction) verified
  against the owning primary.

## Starting sources (researcher verifies and expands)
- **Arditi et al., "Refusal in Language Models Is Mediated by a Single
  Direction," NeurIPS 2024** (proceedings PDF; code at
  github.com/andyrdt/refusal_direction).
- **Röttger et al., "XSTest: A Test Suite for Identifying Exaggerated Safety
  Behaviours in Large Language Models," NAACL 2024** (arXiv).
- A broader over-refusal benchmark paper (e.g. **OR-Bench**, 2024).
- An RLHF/safety-tuning primary for how refusal is installed: **InstructGPT**
  (Ouyang et al. 2022) or **Constitutional AI** (Bai et al. 2022).
- A recent (2025–2026) primary studying over-refusal mechanisms, if solid.

## Relevant prior coverage — link, do not re-teach
- `the-evidence/instructgpt` — RLHF, how fine-tuning aligns a model. Background
  link for "refusal is added by fine-tuning."
- `what-could-go-wrong/jailbreaks` — the opposite failure: getting past
  refusal. Over-refusal is refusal firing when it should not; jailbreaks are it
  failing when it should fire. Link; do not re-teach jailbreaks.
- `the-mechanics/instructions-are-data` — relevant background on how the model
  reads a prompt. Link if used.

## Constraints and traps
- The term **"machinery" is banned (max 0)** — name the actual component,
  computation, or process instead.
- Do not overclaim the single-direction result: it was shown on open-weight
  models; say so, and do not imply it is proven identical in every closed model.

## Structures NOT to inherit (recent habits)
- Avoid comma-triad headings/deks; vary heading shape from recent Mechanics
  pieces (tool-use, instructions-are-data). No "The X a model actually sees"
  echo of instructions-are-data.

## Neighboring articles tonight (keep distinct)
alphago (Evidence), energy-per-query (Instruments), racing-dynamics (WCGW),
microsoft-tay (When AI Breaks). racing-dynamics is a safety *argument*; this is
the *mechanism* of a safety behavior — keep the boundary clean.

## Output paths
- Article: `.nb-work/the-mechanics/over-refusal/library/the-mechanics/over-refusal.html`
- Artifacts under the matching `agent-artifacts/the-mechanics/over-refusal/`.

## Production
harness `claude-code-routine`; writer model `claude-sonnet-5`. Effort:
researcher/editor high, writer medium, coach low. Template `lesson`; mode
`open`; order null; date 2026-08-02.
Tags (nb-meta): safety-tuning, rlhf, refusals, interpretability.
