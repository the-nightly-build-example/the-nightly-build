# researcher brief: the-mechanics/option-order-bias (01)

Inputs:
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/editorial-direction.md — house standard, source rules, The Mechanics series direction
  - this brief

Output: .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/researcher/01/evidence.md

This lesson explains, mechanism by mechanism, why a model's choice among presented
options changes when the options are reordered. Build the evidence record from
primary sources.

Source obligations: minimum 8 sources, primary >= 4, secondary >= 1. Every URL
resolves; cite only what you read.

Establish, each with a primary citation and exact figures where they exist:
  - The behavior: how large the reordering effect is, on which models and
    benchmarks, from Zheng et al. 2023 ("Large Language Models Are Not Robust
    Multiple Choice Selectors") and Pezeshkpour & Hruschka 2023 ("...Sensitivity
    to the Order of Options"). Give the measured swings.
  - Each candidate cause as a real, separable mechanism, with a primary source:
      * options read as a token sequence (position/primacy-recency effects);
      * priors over the option-label tokens (A/B/C/D "token bias");
      * how the answer is scored (first-token / label probability) and how that
        interacts with the above.
    For each, state what the source demonstrates vs conjectures.
  - What is settled vs open: the bias is robustly measured (cite a second
    independent measurement); the exact decomposition (label-prior vs position) is
    not fully settled — mark it and cite any source that says so.
  - The debiasing fixes proposed (e.g. permuting and averaging, calibration) and
    what they reveal about the cause.

Keep primary distinct from secondary. Flag disputed or unverifiable claims. Do not
overstate a single mechanism as the sole cause.
