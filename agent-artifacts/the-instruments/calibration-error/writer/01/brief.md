# writer brief: the-instruments/calibration-error (01)

Inputs:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/editorial-direction.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/commission.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writing-coach/01/voice-guide.md
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/researcher/01/evidence.md
- Article to edit: .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html
- Template context dir: .nb-work/the-instruments/calibration-error/.nb-context/

Output:
- .nb-work/the-instruments/calibration-error/agent-artifacts/the-instruments/calibration-error/writer/01/draft-handoff.md

Proof:
- ./nb stamp .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html
- ./nb check .nb-work/the-instruments/calibration-error/library/the-instruments/calibration-error.html --series the-instruments --library /home/user/library-checkout
  (iterate --no-check-links; final proof with links, to BLOCK: 0)

nb-meta: harness="Claude Code", model="claude-opus-4-8". Tags e.g. calibration, expected-calibration-error, reliability-diagram, overconfidence, rlhf.

This round's focus: define calibration in one sentence, build ECE step by step with the worked example (a small table of bins → per-bin gap → weighted ECE), teach the reliability diagram, then the honest limits and the misled case.

Accuracy cautions from the evidence record (respect exactly):
- The worked examples in the evidence record are CONSTRUCTED by the researcher to illustrate Guo's Equation 3 (the 12.0% ECE table, the coarse-binning case, the accuracy-blind constant predictor). Present them as illustrative constructions with the arithmetic shown, not as data from a source.
- "ECE" names two slightly different formulas (Naeini's positive-fraction form, K=10, vs Guo's top-label accuracy/confidence form, M=15). Pick ONE, define it, and keep it consistent. Brier has two conventions differing by a factor of two; if used, state which.
- The GPT-4 finding: pretrained ECE 0.007 → post-training (RLHF) 0.074; the report does not state the bin count (so those absolute numbers carry the same bin-dependence caveat the lesson teaches), and GPT-4's "confidence" there is its log-probability over answer choices, not typed confidence. Say both.
- CRITICAL distinction (do not blur): "ECE can be gamed by binning" (a metric flaw, per Kumar 2019 / Nixon 2019) and "RLHF degraded GPT-4's calibration" (a substantive finding OpenAI reported honestly using its own binning) are TWO DIFFERENT pitfalls. Do NOT present the GPT-4 numbers as an instance of binning manipulation.
- Kumar 2019: binned ECE lower-bounds true error. Nixon 2019: equal-width binning pathologies; adaptive binning as a fix. The accuracy-blind point: a constant predictor can be perfectly calibrated.

The mechanics of why a chatbot's typed confidence is untrustworthy is the-mechanics/false-confidence (in the library) — link it, do not re-teach it. If you build a reliability-diagram chart, use `nb chart` with the constructed illustrative series and cite it as illustrative.

Habits not to inherit (from commission): number-first dek is fine but avoid comma-triad and semicolon-reversal molds; vary heading construction; avoid negative-closer headings; nearest neighbors hallucination-rate, perplexity, truthfulqa.
