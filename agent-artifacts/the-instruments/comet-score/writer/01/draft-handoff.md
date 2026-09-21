# Draft handoff: the-instruments/comet-score (writer 01)

## Original-work sentence

The article takes the evidence record's separate facts about COMET's versions,
language directions, and software releases and turns them into a single
walk-down procedure for reading one number down to what it actually stands for;
it then ties COMET's number-and-name blind spot back to the exact
training-on-human-ratings that also makes it beat BLEU, so the reader sees why
the same property both ranks systems well and, used as a target, chooses a
translation that flips 1970 to 1980.

## Proof result

`nb check ... --series the-instruments --repo ...` (links included):
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**

No warnings intentionally left. The two initial W-SENTENCE-DENSITY warnings (the
MQM error-weight sentence and the encoder-introduction sentence) were fixed by
splitting each into two sentences.

## Notes for the editor

- The commission's "misled" case is built on over-optimization (Amrhein &
  Sennrich 2022; over-optimization framed via Zouhar et al. 2024), not on a
  claim that COMET ranks systems worse than BLEU. The over-optimization section
  states plainly that COMET is the stronger ranker (WMT22 first vs BLEU last;
  83.4 vs 74.6 in Kocmi) and that the blind spot appears only when COMET is the
  optimization target, not the judge.
- All three recorded contradictions the brief flagged are handled in prose: the
  Kocmi exoneration, the minimal-pair-vs-realistic-pool nuance ("COMET is not
  oblivious to a wrong number"), and the newer-MQM-checkpoint-is-more-blind
  figure (16.6% vs 7.2%).
- The Kocmi 83.4 / 74.6 accuracies are used only as a within-table (All pairs)
  comparison, as the record scopes them.
- Recent-habit breaks: the dek avoids the "honest in the report, misleading the
  moment it is quoted" mold; the body does not reserve the misread reframe for
  the penultimate slot; the takeaway closes on a concrete check rather than a
  "reading it as if it were X" reframe.

## Open evidence or voice questions

None. The evidence record supported every claim the piece rests on; no
researcher request was needed.
