# researcher brief: the-instruments/alpacaeval (01)

Inputs:
- editorial-direction.md — citation standard, the-instruments territory, declared reader.
- commission.md — the measurement, the angle, and the two things to keep distinct.

Output: researcher/01/evidence.md

Read these primary documents in full at the cited passages, not coverage of them:
- The AlpacaEval benchmark's own paper and/or repository (Li et al. and collaborators).
- The length-controlled AlpacaEval paper (Dubois et al. 2024).
- The Chatbot Arena / human-preference reference used to validate correlation.
- A model report that quotes an AlpacaEval win rate.

Answer and verify against the owning primary, with figures and their scope:
- How the win rate is computed: the judge model, the reference model, the instruction-set size, and
  that it is a preference share, not an accuracy. Record the default judge and reference identities.
- The length bias, measured: how strongly the automatic judge prefers longer outputs, and any
  demonstration that a model can raise its win rate by verbosity alone. Give the exact effect size the
  paper reports.
- The length-controlled correction: what it does at a plain level, and the exact correlation with human
  preference (Chatbot Arena) before and after correction. Record the numbers, not "improves."
- How the number is cited in practice: a model report leading with an AlpacaEval win rate, with the
  judge/reference/version it used (so the writer can show two numbers are comparable only under matched
  settings).
- Any other documented failure mode of the automatic judge (self-preference, position bias) as context,
  if a primary supports it.

Record contradictions in full. Confirm every URL resolves to the document's own page, and note the
AlpacaEval version each figure belongs to (the benchmark and its judge have changed over time).
