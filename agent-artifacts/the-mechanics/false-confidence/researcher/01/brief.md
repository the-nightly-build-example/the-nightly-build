# researcher brief: the-mechanics/false-confidence (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/commission.md — the behavior-to-cause chain, required contribution, source floor
- /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/false-confidence/agent-artifacts/the-mechanics/false-confidence/researcher/01/evidence.md

Answer these, from the primary documents:
- Calibration, defined: what it means for predicted probabilities to be
  calibrated, and the reliability-diagram / ECE idea. Guo et al. 2017 ("On
  Calibration of Modern Neural Networks") is the primary for the definition and
  for the finding that modern nets are often miscalibrated (overconfident).
- The GPT-4 technical report calibration result: the exact before-RLHF and
  after-RLHF calibration on the MMLU-style multiple-choice task (the figure and
  its numbers/ECE), stated precisely, with the report as the primary owner.
- The distinction between the model's token-probability distribution (softmax
  over logits) and the confidence it states in words. Find primary work on
  verbalized confidence and on whether models "know what they know": Kadavath et
  al. 2022 ("Language Models (Mostly) Know What They Know") and at least one
  verbalized-confidence study (e.g. Lin, Hilton & Evans, or Tian et al.). Report
  what each actually measured and found.
- What is settled vs open: which parts (softmax gives a next-token distribution;
  verbalized confidence is generated text) are settled engineering, and which
  (why RLHF degrades calibration; how much internal states encode truth) are
  open. Represent the open questions without overstating.
- Contradictions: evidence that some models are well-calibrated after tuning,
  that verbalized confidence can be made informative, or that RLHF need not hurt
  calibration. Record them.
Source floor: at least 8 sources, at least 4 primary, at least 1 secondary.
