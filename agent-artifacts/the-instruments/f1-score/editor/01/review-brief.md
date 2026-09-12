# editor review-brief: the-instruments/f1-score (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md          (house standard, press voice, series prompt)
- ../../writer/01/brief.md              (the exact brief the writer worked from)
- ../../writing-coach/01/voice-guide.md
- ../../researcher/01/evidence.md
- ../../writer/01/draft-handoff.md      (original-work sentence; open in the third read)
- Article to edit (in place):
  /home/user/the-nightly-build/.nb-work/the-instruments/f1-score/library/the-instruments/f1-score.html
- Effective template context:
  /home/user/the-nightly-build/.nb-work/the-instruments/f1-score/.nb-context/

Output: ./editorial-review.md

Recent-pattern notes (the-instruments back catalogue; use these to catch formula
and catchphrase, which no single article can show):
- Recent headlines are a single statistic framed as an indictment of the metric
  ("Adding six wrong answers to each MMLU question fixed its guessing problem"; "The
  function-calling score labs cite grades one call, and usually never runs it";
  "Barratt and Sharma drove the Inception Score to 900 of 1000 with one image per
  class"). Flag this draft's headline if it stamps that mold.
- Recent deks pack a second clause naming an outside comparison.
- Recent section headings / closers: "A single percentage stands in for using tools
  well", "How one call gets graded", "When the leaderboard rewrote its own answers",
  "Why the field stopped ranking on a single number", "The number that took MMLU's
  place". Watch the misleading-case section heading and the closer against these.

This round's focus:
- Verify the numbers against the evidence record, especially: precision/recall/F1
  on the worked confusion matrix, Sasaki's harmonic-mean example, and every Chicco
  figure (use Chicco's confusion-matrix numbers, not its inconsistent prose labels;
  the source mislabels use case A1 once and prints MCC as -0.03 vs -0.04).
- Check the fairness balance holds: F1 ignoring true negatives is correct in the
  retrieval setting; the draft must present F1 as misleading when true negatives
  matter and classes are skewed, not as broken in general, and must keep the
  MCC-is-no-free-lunch caveat.
- Confirm no invented named-leaderboard micro-vs-macro flip (the record does not
  support one); the real ranking flip is Chicco's metric-choice colon-cancer case.
- Confirm origin attributions are exact (van Rijsbergen E and beta; MUC-4/Chinchor
  F-measure name and Fβ; Sasaki harmonic mean) and Dice/Sørensen is not overclaimed.
- The writer left one deliberate W-SENTENCE-DENSITY on the opener's three-question
  setup (paired to the takeaway). Judge whether it earns its place; if you change
  prose, a fresh writer proof is owed before PR.
- press/editorial.md check: the takeaway bookend carries the judgment. If the body
  closes on a Verdict note or any block that restates the finding, remove it (it is
  a leftover from the paper's earlier template, not a model). Confirm the body does
  not end on such a block.
