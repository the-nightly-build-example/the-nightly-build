# researcher brief: the-evidence/mixture-of-experts (01)

Inputs:
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/editorial-direction.md — house standard, source rules, The Evidence series direction
  - this brief

Output: .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/researcher/01/evidence.md

This article reads Shazeer et al. 2017, "Outrageously Large Neural Networks: The
Sparsely-Gated Mixture-of-Experts Layer" (arXiv 1701.06538). Build the evidence
record from primary documents.

Source obligations: minimum 6 sources, primary >= 3, secondary >= 1. Every URL
resolves; cite only passages you have read.

Establish, each with a primary citation and the exact figure:
  - The mechanism in the paper's own terms: the gating network, top-k routing to
    experts, and the sparsity that makes only a few experts compute per example.
  - The real scale: the largest parameter count reported (the ~137B LSTM MoE),
    the expert counts, and the reported compute vs quality results on language
    modeling / translation. Give the numbers, not "huge".
  - The size/compute decoupling: what "active" vs "total" parameters means and
    how the paper frames the compute cost. This is the spine of the honesty
    section.
  - Later primaries that scaled or corrected it: GShard (Lepikhin et al. 2020)
    and Switch Transformer (Fedus et al. 2021) — the trillion-parameter figure,
    the active fraction per token, and the routing/load-balancing/stability
    problems they addressed. Read them directly.
  - Present-day usage: at least one shipped-MoE technical report (e.g. Mixtral or
    DeepSeek-MoE) stating total vs active parameters, so the writer can show where
    a headline "N-billion-parameter" number diverges from per-token compute.

Flag any figure the sources dispute or you could not verify. Keep reported fact
distinct from estimate. Mark what is settled vs open (e.g. routing stability).
