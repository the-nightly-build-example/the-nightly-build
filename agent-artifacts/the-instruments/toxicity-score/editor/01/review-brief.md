# editor review-brief: the-instruments/toxicity-score (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the assignment, boundaries, and the reader's situation
- ../../writer/01/brief.md — the exact writer brief (needed to catch leakage and framing)
- ../../writing-coach/01/voice-guide.md — read first; the sound the piece should hold
- ../../researcher/01/evidence.md — the claim set to test the draft against
- ../../writer/01/draft-handoff.md — open the original-work sentence only on the third read
- the article: /home/user/the-nightly-build/.nb-work/the-instruments/toxicity-score/library/the-instruments/toxicity-score.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/toxicity-score/.nb-context/

Round focus:
- Push hardest on the fairness framing and its figures. Confirm the piece presents
  the failure as a structured penalty on identity mentions and African-American
  English hidden behind a decent aggregate agreement (RealToxicityPrompts' ~88%
  pairwise, Pearson 0.83), NOT as "the number is noise." Verify Sap 2019
  (r=0.42/0.35; ~46% vs 9% false-positive gap), Davidson 2019 (1.4x-2.65x), and
  Dixon 2018 ("gay" 3% of toxic vs 0.5% of all) against the evidence record, each
  at its exact scope.
- Confirm figures are date/endpoint-stamped (the classifier is a moving target)
  and that the two datasets are not merged (RTP-era classifier on Wikipedia Talk +
  news comments; Civil Comments is separate and later). The headline states the
  Dixon finding — verify it is exactly what Dixon owns.
- The writer flagged (in the handoff) that the Perspective 0.7 recommended
  threshold was omitted because its only source was an unverified FAQ; the piece
  uses 0.5 as RealToxicityPrompts' chosen cutoff. Confirm that is handled honestly.
- Body addresses no one; only the two bookends speak to the reader; no Verdict.

Recent-pattern notes (compare edges, headings, dek; flag any formula):
Recent the-instruments deks/headlines this piece must not echo in mold —
- "A model's \"37% hallucination rate\" was its wrong-answer share on SimpleQA"
- "Adding six wrong answers to each MMLU question fixed its guessing problem"
- "'Human parity' in speech recognition came down to how you count the humans"
- "A model can top the MTEB average and be ordinary at retrieval"
- "The same model scored 1673 or 2214 on Codeforces, depending on the scaffolding"
The most recent piece (simpleqa) opened with an nb-stat-strip and a "how X became
Y" nb-note; check this piece's shape and headings differ.
