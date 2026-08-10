# researcher brief: the-mechanics/prompt-sensitivity (01)

Inputs:
- editorial-direction.md — citation standard, the-mechanics territory, declared reader.
- commission.md — the behavior and the causal chain to ground at each step.

Output: researcher/01/evidence.md

Read these primary documents in full at the cited passages, not coverage of them:
- Sclar et al. 2023, "Quantifying Language Models' Sensitivity to Spurious Features in Prompt Design"
  (FormatSpread).
- Lu et al. 2022, "Fantastically Ordered Prompts and Where to Find Them" (few-shot example ordering).
- At least two more primaries measuring prompt, format, or order sensitivity, or how it changes with model
  scale or instruction-tuning.

Answer and verify against the owning primary, with figures and their scope:
- The measured size of format sensitivity: how much a trivial formatting change (separators, casing,
  spacing) moves accuracy, on which models and tasks, in FormatSpread's own numbers (the spread, not a
  rounded impression).
- The measured size of order sensitivity: how much reordering the same few-shot examples moves accuracy,
  and whether a best order is predictable in advance.
- The mechanism support: that the model conditions on the literal token sequence, with a concrete
  demonstration that semantically equivalent prompts are not equivalent inputs. Keep this grounded in what
  the measurements show; do not overclaim a single cause.
- Whether the effect shrinks with scale, instruction-tuning, or newer models, and where it persists, from a
  primary. Mark this as the open part.
- One concrete, reproducible example of two trivially different formats and their different outcomes, as
  data (not a runnable harness), for the writer's worked example.

Record contradictions in full. Confirm every URL resolves to the document's own page. Note the model
generations tested, since sensitivity figures are generation-dependent.
