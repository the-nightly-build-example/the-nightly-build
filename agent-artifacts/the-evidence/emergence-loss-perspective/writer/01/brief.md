# writer brief: the-evidence/emergence-loss-perspective (01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the-evidence prompt, template identity.
- writing-coach/01/voice-guide.md — how a lesson in this domain should sound, with exemplar passages. (It was
  written for a neighboring emergent-abilities angle; read it for rhythm and register, not for this lesson's
  thesis.)
- researcher/01/evidence.md — the complete claim set: Du 2024 (the document), plus Schaeffer 2023 and Wei 2022
  for context, with figures, contradictions, and source kinds.
- The initialized article at library/the-evidence/emergence-loss-perspective.html and its .nb-context/ contract.

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/emergence-loss-perspective/library/the-evidence/emergence-loss-perspective.html --series the-evidence --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --series is required in local mode; use --no-check-links while iterating, links included until BLOCK: 0)

Set nb-meta the engine cannot compute: date 2026-08-10, harness claude-code-routine, model
"Claude Opus 4.8", and tags ["emergent-abilities", "pre-training-loss", "scaling"]. nb stamp writes the counts.

The lesson, and the hard distinctness requirement:
- Center the body on Du, Zeng, Dong, Tang (2024), "Understanding Emergent Abilities from the Loss Perspective."
  Its finding: plot task performance against pre-training loss (the model's average next-token prediction loss
  on held-out text, a smooth measure of language modeling), and certain tasks stay at random until loss falls
  below a threshold near 2.2, then climb, even under continuous metrics (CorrectChoiceProb, Brier Score) on
  MMLU and C-Eval. This answers Schaeffer's metric-artifact rebuttal by changing the x-axis, not the metric.
- The desk has ALREADY published the-evidence/emergent-abilities ("The sudden jump in AI benchmarks was mostly
  in the scoring"), which teaches Wei's claim and Schaeffer's metric-artifact rebuttal with a partial-credit
  worked example. That is taught ground. Link it in Background and refer to it in prose at first use; do NOT
  re-teach the metric-artifact mechanism or reproduce its accuracy-versus-partial-credit worked example here.
  The reader who does not open the link must still follow, so state the mirage claim in a sentence, then move to
  Du's answer.
- Teach as new: pre-training loss as an axis, and why plotting against loss instead of size or compute changes
  the picture. Keep the smooth loss axis distinct from the threshold effect throughout.
- Hold the debate open honestly. Record Du's own Brier baseline caveat (a context-free predictor scores 0.75 on
  four options) and that Du and Schaeffer use different tasks and models, so neither settles it. Confirm any
  exact figure (the ~2.2 threshold, the tasks, the metrics) against the evidence record's owning-primary entry.

If the evidence under-covers Du's loss-perspective method for a claim the lesson rests on, return a precise
researcher request rather than writing around it.

Recent habits to break (from the-evidence and the house record; the voice guide does not carry these):
- Do not open "Why this matters" with "If you have read this desk on X..." (batch-normalization).
- Do not end the opener with an enumerated roadmap. State stakes without touring the sections.
- Do not open the takeaway on a bare restated definition. Resolve what the opener set up.
- Do not reach for the headline mold "the paper got its own X wrong" / "scored N% on its own test". Find this
  document's own surprise.
