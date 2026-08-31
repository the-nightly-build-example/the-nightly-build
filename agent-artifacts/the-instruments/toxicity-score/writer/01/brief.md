# writer brief: the-instruments/toxicity-score (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the angle, boundaries, source policy, nb-meta values, habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- the initialized article: /home/user/the-nightly-build/.nb-work/the-instruments/toxicity-score/library/the-instruments/toxicity-score.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/toxicity-score/.nb-context/

Output: draft-handoff.md (in this directory), plus the edited article.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/the-instruments/toxicity-score/library/the-instruments/toxicity-score.html --series the-instruments
  (iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.)

This round's focus — precision the evidence forces (see evidence limitation and Contradictions):
- The honest misleading-case is NOT "the number is noise." RealToxicityPrompts'
  own manual check found about 88% pairwise agreement (Pearson 0.83) between human
  judgments and Perspective scores in aggregate. Frame the failure as: a decent
  average hides a structured penalty on identity mentions and African-American
  English — established by Sap 2019 (r=0.42/0.35; roughly a 46% vs 9%
  false-positive gap), Davidson 2019 (1.4x-2.65x cross-dataset ratios), and Dixon
  2018 ("gay" in 3% of toxic vs 0.5% of all training comments). Use those figures
  exactly.
- The classifier is a moving target. Every score figure is endpoint- and
  date-specific (the RTP-era CNN model vs the current model; Sap queried Dec 2018,
  etc.). Date-stamp figures; do not present one score as timeless.
- Do NOT merge two datasets: the RTP-era classifier was trained on Wikipedia Talk
  plus news comments; Civil Comments is a separate, later Jigsaw dataset. Keep
  them distinct; do not import the Civil Comments lineage.
- Perspective's own score-meaning/FAQ pages are JavaScript apps that do not fetch;
  the "score = probability a reader perceives the text as toxic" claim rests on
  RTP's isotonic-calibration statement and the model card, per the evidence. Cite
  accordingly.
- Verified figures: RTP 100K headline prompts (Table 1 sums to 99,016; ~22K
  toxic); the two metrics defined at k=25. Use the Numbers section exactly.

nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
series `the-instruments`, slug `toxicity-score`. Dek must match the rendered
dekline exactly. Only the two bookends address the reader; no Verdict block at the
body's close.
