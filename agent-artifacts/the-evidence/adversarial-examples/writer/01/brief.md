# writer brief: the-evidence/adversarial-examples (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the angle, boundaries, source policy, nb-meta values, habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- the initialized article: /home/user/the-nightly-build/.nb-work/the-evidence/adversarial-examples/library/the-evidence/adversarial-examples.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/adversarial-examples/.nb-context/

Output: draft-handoff.md (in this directory), plus the edited article.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/the-evidence/adversarial-examples/library/the-evidence/adversarial-examples.html --series the-evidence
  (iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.)

This round's focus — precision the evidence forces (see evidence limitation and Contradictions):
- Frame "still unsolved" honestly as a wide remaining gap WITH real, measured
  progress, not "nothing works." Carry both: no cheap general defense, yet
  Madry's PGD adversarial training is a durable partial defense, certified
  defenses (randomized smoothing) exist, and CIFAR-10 robust accuracy rose from
  about 46% (2018, under 20-step PGD) to about 74% (Bartoldson 2024, under the
  stronger AutoAttack) against roughly 94% clean. Bartoldson argues the ceiling
  is real.
- The paper's linear explanation is genuinely contested (boundary-tilting;
  non-robust features; no field consensus). Present it as the paper's claim and
  say it is disputed, don't state it as settled fact.
- The paper's own proposed defense, single-step FGSM adversarial training, was
  later shown to give little real robustness (gradient masking); the "harnessing"
  half held up only in the stronger multi-step (PGD) form. Say so.
- Provenance: Goodfellow and Szegedy co-authored BOTH the 2013 predecessor and
  this 2015 paper. "What this paper added" is the same researchers advancing
  their own prior work, not one group correcting a rival — frame accordingly.
- Verified figures to use exactly: perturbation epsilon 0.007; panda 57.7% to
  gibbon 99.3% on GoogLeNet; plus the MNIST figures in the Numbers section.

nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
series `the-evidence`, slug `adversarial-examples`. Dek must match the rendered
dekline exactly. Only the two bookends address the reader; no Verdict block at the
body's close.
