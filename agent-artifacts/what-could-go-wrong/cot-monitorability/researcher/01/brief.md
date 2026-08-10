# researcher brief: what-could-go-wrong/cot-monitorability (01)

Inputs:
- editorial-direction.md — citation standard, the what-could-go-wrong territory, declared reader.
- commission.md — the argument and the shown-versus-projected line to ground.

Output: researcher/01/evidence.md

Read these primary documents in full at the cited passages, not commentary on them:
- The 2025 chain-of-thought monitorability position paper (Korbak et al.).
- OpenAI's 2025 monitoring/obfuscation result (Baker et al.).
- Turpin et al. 2023, "Language Models Don't Always Say What They Think."
- An Anthropic faithfulness primary (Lanham et al. 2023; and/or the 2025 reasoning-faithfulness
  paper, "reasoning models don't always say what they think").

Answer and verify against the owning primary, with exact experimental scope:
- The strongest statement of the argument: what the position paper claims monitorability is,
  why it calls it fragile, exactly who the authors are and which organizations, and what they
  ask labs to do. Record precise author/affiliation labels.
- Baker et al.: what was actually demonstrated in a working model. Exactly what the
  chain-of-thought monitor caught, what happened when training penalized the chain-of-thought
  (obfuscation while still misbehaving), and the precise conditions. Do not let it read as an
  unprompted, deployment-time failure if the setup created the pressure.
- Turpin and the Anthropic faithfulness work: the concrete demonstration that a
  chain-of-thought can be unfaithful (the model uses a cue it does not mention), with the task,
  the measured effect size, and the models tested.
- The line the desk needs: for each risk (heavy outcome-based RL degrading monitorability;
  latent/"neuralese" reasoning removing legible traces; strategic unprompted obfuscation),
  record whether a primary demonstrates it in a real system or only argues it about future
  systems. This mapping is the piece's spine.
- The present-day recommendations and any counter-position (a primary arguing monitoring is
  more or less reliable than the position paper implies), to steelman both sides.

Record contradictions in full: where these papers disagree on how faithful or durable
chain-of-thought monitoring is. Confirm every URL resolves to the document's own page.
