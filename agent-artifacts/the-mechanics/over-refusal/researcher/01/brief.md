# Researcher brief: the-mechanics/over-refusal

## Inputs (begin here)
- This brief and `commission.md`.
- `editorial-direction.md` for standards.

## Output (write only this)
`.nb-work/the-mechanics/over-refusal/agent-artifacts/the-mechanics/over-refusal/researcher/01/evidence.md`
Follow the researcher SKILL sections exactly.

## Source policy
the-mechanics lesson: **min 8 sources; primary ≥ 4, secondary ≥ 1.**

## Required primary documents (read first-hand)
1. **Arditi, Obeso, et al., "Refusal in Language Models Is Mediated by a Single
   Direction," NeurIPS 2024** (proceedings PDF:
   https://proceedings.neurips.cc/paper_files/paper/2024/file/f545448535dfde4f9786555403ab7c49-Paper-Conference.pdf
   ; repo github.com/andyrdt/refusal_direction). Record precisely: the claim
   (refusal mediated by one direction in the residual stream), the exact
   experiments (ablate the direction → stops refusing harmful prompts; add it →
   refuses harmless prompts), which models it was demonstrated on (open-weight
   families, list them), and stated limitations. Capture verbatim the key
   sentences.
2. **Röttger et al., "XSTest: A Test Suite for Identifying Exaggerated Safety
   Behaviours in LLMs," NAACL 2024** — the 250 safe + 200 unsafe prompt design,
   and any reported over-refusal rates on named models. Exact numbers.
3. **A broad over-refusal benchmark** (e.g. OR-Bench, 2024) — its size, method,
   and any headline over-refusal rates. Exact numbers.
4. **An RLHF / safety-tuning primary** for how refusal is installed:
   InstructGPT (Ouyang et al. 2022) and/or Constitutional AI (Bai et al. 2022).
   Record how refusal/harmlessness behavior is trained in (RLHF/RLAIF), enough
   to teach "refusal is added by fine-tuning" from a primary.

## Research questions to answer with exact readings
- The pretrained-vs-fine-tuned distinction: a first-hand basis for the claim
  that base models do not refuse and fine-tuning installs refusal (InstructGPT/
  CAI or a model card documenting refusal training).
- The surface-feature failure: first-hand evidence that refusals trigger on
  words/topics rather than intent (XSTest is built exactly to show this — get
  concrete example prompts it uses, e.g. benign uses of "kill"/"shoot" in
  cooking/photography). Capture 2–3 real example prompts.
- The single-direction result stated exactly, with the model list and the
  caveat that it is open-weight models.
- The safety/helpfulness tradeoff: a first-hand statement (paper or model card)
  that reducing refusals raises the risk of complying with harmful requests.
- Optional recent (2025–2026) work refining or complicating the single-
  direction picture (there is follow-up questioning whether refusal is truly
  one direction) — include it for honest nuance; classify carefully.

## Contradictions to hunt
- Is refusal really "a single direction"? Find and record any credible
  follow-up work that complicates this (multiple directions, task-conditioned
  refusal). The article should mark this as an open question, so this matters.
- Vendor framing ("the model understands and declines harmful requests") vs the
  mechanistic evidence (surface-triggered, linearly represented). Document both.

## Numbers section
Refusal/over-refusal rates from XSTest and the broad benchmark with the exact
model and denominator; the size of each benchmark; any effect sizes from the
direction ablation/addition experiments.

## Source assets
Consider one exact figure from a cited primary (e.g. XSTest example table, or an
Arditi et al. results figure) if it would let the reader test the argument;
else `None found`.

## Control
`DONE researcher <evidence-path>`; `BLOCKED researcher <reason>` if a required
primary cannot be opened after a real browser attempt.
