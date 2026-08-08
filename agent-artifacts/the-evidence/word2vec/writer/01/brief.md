# writer brief: the-evidence/word2vec (01)

Inputs:
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/editorial-direction.md — governing standard, headline standard, press voice, lesson identity, series prompt
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/commission.md — subject, angle, required contribution, boundaries
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/writing-coach/01/voice-guide.md — craft standard and licenses (generous deflation; deflate-by-demonstration)
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/researcher/01/evidence.md — complete claim set; use its Numbers section exactly
- .nb-work/the-evidence/word2vec/library/the-evidence/word2vec.html — the initialized article to EDIT in place
- .nb-work/the-evidence/word2vec/.nb-context/ — effective contract, runtime assets, furniture catalogs

Output: .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-evidence/word2vec/library/the-evidence/word2vec.html --series the-evidence --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same command WITHOUT `--no-check-links` until `BLOCK: 0`.

nb-meta: date `2026-08-08`, harness `claude-code-routine`, model `claude-opus-4-8`;
keep nb-meta `dek` identical to the rendered dekline.

Corrections the evidence requires (the editor will check every one):
- The 6B-word Google News corpus belongs to the FIRST paper (1301.3781), NOT the
  companion. The companion's word-analogy results used a ~1B-word set (300-dim).
- Keep word-analogy and phrase-analogy numbers DISTINCT: the 19,544-question set
  (8,869 semantic + 10,675 syntactic) is the WORD-analogy test; the companion's 72%
  is a SEPARATE phrase-analogy test at ~33B words. The folklore collapses these; do
  not. Safe headline figures: 65.6% best word-analogy (paper 1, Skip-gram 1000-dim,
  6B words) and 61% (paper 2, Table 1).
- The deflation is grounded, not attitude: Levy & Goldberg show the arithmetic is a
  balancing of three cosine similarities and reproduces in plain sparse count
  vectors; Linzen shows the literal arithmetic returns one of the three input words
  ~98% of the time unless they are excluded by hand, and an offset-free nearest-
  neighbor baseline captures much of the score. Steelman both sides: the regularities
  are real and robust, but "vector arithmetic does analogies" overstates the offset.

Recent the-evidence shapes to break: do not use the "result beneath the <hype>"
opener or a reflexive nb-figure+nb-math pairing; name headings from these papers'
steps. Link (plain prose link, not a numbered source) to the-mechanics/word-embeddings
rather than re-teaching what an embedding is — this is a document lesson.

This round's focus: the reader leaves able to separate the measured word-analogy
accuracy on a defined test from the "vectors capture meaning" folklore.
