# editor review-brief: the-instruments/alpacaeval (editor/01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the-instruments prompt, template identity.
- commission.md — the measurement, the angle, the reader's situation, the source policy.
- writer/01/brief.md — the exact brief the writer worked from (for leak-checking against instructions).
- writing-coach/01/voice-guide.md — how this piece should sound, with the exemplar passages the writer read.
- researcher/01/evidence.md — the claim set, the source entries, and contradictions.
- writer/01/draft-handoff.md — the writer's original-work sentence, the left warning, and notes.
- The article at library/the-instruments/alpacaeval.html and its .nb-context/ contract.

Output: editor/01/editorial-review.md

Round's focus:
- Source count (the writer left W-SOURCES-MIN, 7 versus the series floor of 8). The writer treated Chatbot
  Arena as taught ground linked in prose, which is correct. But the evidence record holds distinct primaries
  the article does not cite as numbered sources, including the AlpacaEval 2.0 leaderboard CSV (evidence source
  2) and the Zephyr model card (evidence source 6). If a figure the article already displays is owned by one
  of those, for example the 2.0 leaderboard reading of Zephyr's win rate, attribute it to that owning primary
  in place. That is a citation fix, not new reporting, and it reaches 8 without padding or citing taught
  ground. Only if no displayed claim is genuinely owned by an uncited primary should the warning stand, and
  then record the press-rule justification explicitly.
- Verify every number carries its version, judge, and reference (1.0 versus 2.0), and that length control is
  not presented as a complete fix (the null-model result). Confirm the length-swing figures and the 0.94-to-0.98
  correlation against the owning primary; do not let the unpinned judge-human-agreement digit appear.
- Keep two things distinct: a model genuinely preferred versus one winning by length under a biased judge.

Recent-pattern notes (compare edges, deks, headings, furniture against these; break any match without copying prior structure):
- the-instruments headline tic: the "two measures disagree / both are true" reveal (fid, tokens-per-second,
  energy-per-query).
- House opener tic: the enumerated roadmap closing "Why this matters".
- House takeaway tic: opening on a bare restated definition of the subject.
- the-instruments heading tic: the holdup-section phrasing "Where the number keeps its word" (fid).
- Dek molds banned in spec/headlines.md: the semicolon reversal, the suspended question, the comma triad. Check
  the dek and every heading against the recent library.
