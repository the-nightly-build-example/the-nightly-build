# researcher brief: the-evidence/adam-optimizer (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/commission.md — the angle, the required contribution, and the source floor
- /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-evidence/adam-optimizer/agent-artifacts/the-evidence/adam-optimizer/researcher/01/evidence.md

Answer these, from the primary documents:
- What Adam is, exactly: the update rule, the two moment estimates, bias
  correction, the default hyperparameters the paper recommends. Quote the paper's
  own statement where wording is evidence.
- What the 2015 paper actually demonstrated and at what scale: enumerate every
  experiment (task, dataset, model size). The reader must see how small the
  foundation is relative to modern models.
- The convergence claim (Theorem 4.1 / the regret bound): what it asserts and
  under what assumptions.
- How Reddi, Kale & Kumar (2018) broke it: the exact counterexample (the simple
  convex/online setting), what fails, and what AMSGrad changes. Verify the claim
  against their paper, not summaries.
- How the field actually uses Adam today and whether AMSGrad displaced it (it
  largely did not); where AdamW fits as the variant that did displace plain Adam
  in transformer training. Get a primary or well-sourced secondary for the
  "AMSGrad rarely helps in practice" point and label it honestly.
- Contradictions: search for defenses of the original proof, corrected
  convergence results for Adam under other assumptions, and any dispute over how
  damning the counterexample is. Record them.
Source floor: at least 6 sources, at least 3 primary, at least 1 secondary.
