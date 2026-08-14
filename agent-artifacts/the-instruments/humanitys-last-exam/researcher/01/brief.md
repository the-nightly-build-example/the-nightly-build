# researcher brief: the-instruments/humanitys-last-exam (01)

Inputs:
- `.nb-work/the-instruments/humanitys-last-exam/agent-artifacts/the-instruments/humanitys-last-exam/editorial-direction.md` — citation standard, the-instruments territory, declared reader.

Output: `.nb-work/the-instruments/humanitys-last-exam/agent-artifacts/the-instruments/humanitys-last-exam/researcher/01/evidence.md`

Subject and angle: Humanity's Last Exam (HLE), Center for AI Safety and Scale AI,
January 2025. The article teaches how the number is manufactured and what a given
HLE score can and cannot support, and it names a real case where the number
misled people.

Read first, primary, in full where relevant:
- The HLE paper and dataset documentation. Get: the exact question count at
  release (and any later revision after flawed questions were removed), the
  number and vetting of expert contributors, the subject coverage, the answer
  formats (multiple-choice vs exact-match short answer), how grading works, and
  the calibration-error metric reported alongside accuracy. Pin down the
  adversarial construction: questions were filtered against which frontier
  models, and what "the model failed it" meant at submission.
- The model reports or official leaderboard entries that own each score you cite:
  the launch-day scores (single digits) with the models and dates, and the most
  recent scores you can verify (2025 into 2026), clearly separating runs that
  used tools or web browsing from no-tool runs. Every score carries its model,
  date, and whether tools were allowed.

Then, for the misreading:
- Reporting and commentary that read the score or its climb as AI approaching the
  limit of human knowledge, or that conflated tool and no-tool numbers, or that
  read HLE as an expert/PhD-level threshold. Name who, with dates. Two
  independent confirmations for any contested characterization.
- Any correction from the authors about what the benchmark measures, and any
  documented issue with specific questions.

Questions the evidence must answer:
- Exactly how the number is produced, step by step, end to end.
- What a low HLE score means given adversarial filtering, and what a fast-rising
  score means and does not mean.
- The concrete tool-vs-no-tool gap on a comparable model, with figures.
- The clearest documented instance of the number being over-read, with the
  primary score it was over-read against.

Record contradictions in full. Preserve a verified score-over-time series
(model, date, tools yes/no, score) suitable for a chart, only from primary
numbers. Note source assets only if an exact table or figure from the HLE paper
or a model card would carry the argument better than prose.
