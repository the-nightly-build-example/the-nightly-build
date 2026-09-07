# researcher brief: the-instruments/math-benchmark (01)

Inputs:
- `editorial-direction.md` — citation standard, series territory, declared reader
- `commission.md` — the assignment, its boundary, and the source floor
- this brief

Output: `researcher/01/evidence.md`

Subject: the MATH benchmark from "Measuring Mathematical Problem Solving With the
MATH Dataset" (Hendrycks, Burns, Kadavath, Arora, Basart, Tang, Song, Steinhardt;
2021). Read the paper firsthand (arXiv 2103.03874) and the released dataset.

Answer these, each traceable to the owning source:

- How the dataset was built: the source competitions (AMC, AIME and others), the
  count (12,500 problems), the train/test split, the seven subjects, and the five
  difficulty levels. State exact figures.
- How a MATH score is computed: exact-match grading of a single final answer,
  what counts as correct, and how the paper handled answer formatting. What does
  the reported percentage actually measure?
- The accuracy trajectory: what the paper's own models scored at release, and how
  scores rose toward saturation on MATH afterward. Give real numbers with the
  model and date that owns each.
- At least one documented case where the number misled: contamination of
  competition problems in training data (find a study or model report that owns
  this finding), the "MATH-500" subset and numbers that share the name reporting
  different things, or exact-match grading marking a correct method wrong. Record
  what the confusion cost.
- What the benchmark can and cannot support today.

Meet the floor with sources that change the interpretation, not padding: at least
8 sources, at least 4 primary, at least 1 secondary. A model's MATH score is owned
by the model card or paper that reports it, not by a leaderboard aggregator; cite
the owner. Search for what breaks the commission's angle and record it in
Contradictions. Confirm every URL resolves to the document's own page.
