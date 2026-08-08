# editor review-brief: the-evidence/word2vec (01)

Inputs:
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/editorial-direction.md — the standard you enforce
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/writing-coach/01/voice-guide.md — read first; judge licensed forms against it
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/researcher/01/evidence.md — the claim set; open as an opponent in the skeptic read
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/writer/01/brief.md — the EXACT writer brief (for instruction-leakage checks)
- .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/writer/01/draft-handoff.md — original-work sentence (open only in the third read)
- .nb-work/the-evidence/word2vec/library/the-evidence/word2vec.html — the article
- .nb-work/the-evidence/word2vec/.nb-context/ — template context

Output: .nb-work/the-evidence/word2vec/agent-artifacts/the-evidence/word2vec/editor/01/editorial-review.md

After any direct cuts, run `./nb stamp` on the article (from /home/user/the-nightly-build)
so counts stay honest; the writer runs the proof. Do not edit markup, assets, or
sources — route those to the writer.

Recent-pattern notes to enforce (break formulas, do not copy any prior structure):
- the-evidence shelf recently opens on "the result beneath the <hype> headline" and
  pairs nb-figure with nb-math; this piece deliberately avoids both. Check the
  opener and headings are named from these papers' own steps, not a stock shape.
- Verify the two attribution traps did not slip in: word-analogy (19,544-question
  set) must stay distinct from the companion's phrase-analogy 72%; the 6B Google
  News corpus belongs to the FIRST paper. A wrong frame here is a display/analysis
  error, not a quibble.

Round focus: hardest push on whether the "deflation" is earned by the cited
decomposition (Levy & Goldberg; Linzen's ~98%-returns-an-input) rather than asserted,
and whether the piece separates measured analogy accuracy from the "vectors capture
meaning" folklore without overclaiming in either direction.
