# researcher brief: the-instruments/calibration-error (01)

Inputs:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/editorial-direction.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/commission.md

Output:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/researcher/01/evidence.md

Read the primaries and answer with locators:
- The definition of calibration and the binned ECE estimator: Naeini, Cooper,
  Hauskrecht 2015 (the binned estimator) and Guo, Pleiss, Sun, Weinberger 2017
  "On Calibration of Modern Neural Networks". Get the exact ECE formula (bin the
  predictions, per-bin |accuracy - confidence|, weight by bin size) and the
  reliability-diagram definition, in the sources' own terms. Extract enough to
  build a small worked example (a handful of bins with confidence, accuracy, and
  the resulting ECE).
- Guo et al.'s central finding: that modern networks are overconfident and that
  depth/width/batchnorm worsened calibration, with the figures they report, plus
  temperature scaling as their fix and how well it worked.
- ECE's pitfalls: a primary showing binned ECE is sensitive to bin count/
  placement and can understate error (e.g. Nixon et al. "Measuring Calibration
  in Deep Learning" 2019, and/or Kumar, Liang, Ma "Verified Uncertainty
  Calibration" 2019 on the bias of binned ECE). Record the specific way a
  coarser or adaptive binning changes the number.
- Proper scoring rules as alternatives: the Brier score and negative log-
  likelihood, and why a proper scoring rule cannot be gamed by binning. One
  primary suffices.
- The misled case: the GPT-4 technical report's calibration result (pretrained
  model well-calibrated; post-training/RLHF degraded calibration). Get the exact
  claim and the figure reference from the report itself. Note the accuracy-blind
  point: a constant predictor can be perfectly calibrated.

Record contradictions (e.g. debate over whether ECE is the right metric at all).
Confirm every URL resolves to the source's own page. Classify each primary/
secondary. Meet the 8-source, 4-primary / 1-secondary floor with sources that
change the interpretation.
