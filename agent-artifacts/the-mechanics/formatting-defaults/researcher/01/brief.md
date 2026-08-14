# researcher brief: the-mechanics/formatting-defaults (01)

Inputs:
- `.nb-work/the-mechanics/formatting-defaults/agent-artifacts/the-mechanics/formatting-defaults/editorial-direction.md` — citation standard, the-mechanics territory, declared reader.

Output: `.nb-work/the-mechanics/formatting-defaults/agent-artifacts/the-mechanics/formatting-defaults/researcher/01/evidence.md`

Subject and angle: why chatbots default to bulleted lists and bold headers, worked
backward from the visible output to the post-training stages that shaped it. The
evidence must support a step-by-step causal chain the writer can lay out and mark
as settled or open at each link. No code is needed in the article, but the
evidence must be precise about mechanism.

Gather the primary source that owns each step:
- Autoregressive generation: the output is sampled token by token from a next-
  token distribution. (Already taught in the-mechanics/autoregressive-generation;
  the researcher only needs a primary anchor if a specific claim rests on it.)
- Instruction tuning: papers showing supervised finetuning on formatted answer
  data teaches models to answer in the demonstrated shape (for example the
  InstructGPT paper and open instruction-tuning work). What the answer formatting
  in those datasets looks like.
- Preference tuning / RLHF: primary evidence that human raters and reward models
  prefer structured, skimmable, often longer answers. The strongest verifiable
  items: the style-controlled Chatbot Arena analysis quantifying how markdown
  (headers, bold, lists) and length raise win rate independent of content, and
  any published annotation or preference guidelines or lab notes that reward
  formatting. Give exact effect sizes where a source states them.
- Length and format bias in LLM-as-judge and preference data more broadly, from
  the papers that measured it.
- Any lab documentation or model card noting default markdown behavior, and the
  fact that a system prompt can request or suppress it.

Questions the evidence must answer:
- Concretely, what in pretraining, instruction tuning, and preference tuning each
  contributes to the formatting default, with a real example or figure per step.
- The strongest quantified evidence that preference optimization rewards
  formatting and length independent of answer quality.
- What is settled versus what is inferred or undisclosed (labs do not publish full
  reward-model details), stated plainly so the article can mark open questions.
- That the format is a learned policy, not a task requirement: evidence that
  instruction or system prompt changes it.

Record contradictions in full (for example, disagreement over how much length
versus markdown drives preference wins). Preserve any verified effect-size series
suitable for a chart (for example, win-rate contribution of length vs markdown),
only from primary numbers. Note source assets only if an exact figure or table
would carry the argument better than prose.
