# researcher brief: the-mechanics/thinking-out-loud (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader
- commission.md — subject, angle, boundaries, source policy

Output: researcher/01/evidence.md

Research questions (answer each against the owning primary):
- The behavior: a documented case where writing intermediate steps changes a
  model's accuracy on a hard task (the chain-of-thought finding; and a reasoning
  model's measured gain from longer 'thinking'). Record what was tested and the
  size of the effect.
- The mechanism: read the theory primaries on WHY generating tokens buys
  computation — transformer expressivity / bounded compute per token and how CoT
  expands it (e.g. Feng et al. 2023 'Towards Revealing the Mystery behind CoT';
  Merrill & Sabharwal 2023 on the expressive power of CoT/log-depth). Record, in
  plain terms, the settled claim: a transformer does bounded computation per
  emitted token, so serial reasoning requires emitting tokens the model can read
  back.
- A concrete worked example: a specific multi-step problem a model gets right
  only when it writes the steps, with a real source or a clearly reproducible
  description (no code in the article, but you may describe the setup).
- Settled vs open: cite the faithfulness evidence that the written steps may NOT
  reflect the real computation (Turpin et al. 2023 'Language Models Don't Always
  Say What They Think'; Anthropic/Lanham 2023 measuring CoT faithfulness). Mark
  this as the open question; do not resolve it.
Contradiction hunt: evidence that CoT is 'just' more compute vs evidence it
elicits latent reasoning; cases where CoT did not help or hurt. Record both.

Verify every number against the primary that owns it. Record each source's own
resolvable URL (not the fetch route). Classify primary vs secondary with a
reason. Fill the Contradictions section only after a real search for what breaks
the angle. Meet the source policy in the commission. Report the evidence path,
the record's most important limitation, and whether the evidence undermines the
commissioned angle.
