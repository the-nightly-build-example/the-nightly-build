# editor review-brief: the-evidence/wavenet (01)

Inputs to read (in the order the skill names):
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/writing-coach/01/voice-guide.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/editorial-direction.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/commission.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/writer/01/brief.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/researcher/01/evidence.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/writer/01/draft-handoff.md
  the article: .nb-work/the-evidence/wavenet/library/the-evidence/wavenet.html
  template context under .nb-work/the-evidence/wavenet/.nb-context/

Output: .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/editor/01/editorial-review.md

Recent-pattern notes (compare edges, headings, dek, furniture against these; an opener/closer/heading built like one of these is a formula to break):
  - Evidence headline molds recently used: "X beat Y on nine of twelve datasets" (gpt-1); "X did A. Its authors did B." (mamba, alphazero-style reversal).
  - Recent dek shape: "Author-and-year's paper does X, and Y" with a trailing "and/though/while" clause.
  - Recurring desk heading mold: "The [noun] that [verb]" ("The half that survived").
  - Recent openers name author+team+year then a single figure.

This round's focus (highest-risk claims to break first):
  - Attribution integrity is the spine: the 2016 paper makes NO generation-speed claim; every speed figure (172 timesteps/s, 24,000 needed, 500,000+, 1000x, 50ms) belongs to Parallel WaveNet (2017) / DeepMind 2017 posts. Confirm no later figure reads as the 2016 paper's.
  - The four MOS readings sit on different corpora with different human baselines; the headline/dek must not let one test's MOS read as another's, and must not imply human parity. Check the MOS numbers, scopes, and baselines against the evidence record and the mean-opinion-score point (MOS does not travel).
  - Verify data/task scale figures and the three non-reconcilable gap-closure percentages (51%, 69%, ">70%") are each tied to their own test.
  - Confirm Background links (autoregressive-generation, mean-opinion-score) are plain prose links, not numbered sources, and that the piece does not re-teach them.
