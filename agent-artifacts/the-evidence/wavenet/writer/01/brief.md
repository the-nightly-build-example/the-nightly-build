# writer brief: the-evidence/wavenet (01)

Inputs:
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/editorial-direction.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/commission.md — angle, boundaries, reader
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/writing-coach/01/voice-guide.md
  .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/researcher/01/evidence.md
  the initialized article: .nb-work/the-evidence/wavenet/library/the-evidence/wavenet.html
  the effective template contract and catalogs under .nb-work/the-evidence/wavenet/.nb-context/

Output: .nb-work/the-evidence/wavenet/agent-artifacts/the-evidence/wavenet/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-evidence/wavenet/library/the-evidence/wavenet.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/67c352f8-06f4-5e83-b6d0-5e6a0d5d584d/scratchpad/library-checkout
       (run with --no-check-links while iterating; run nb stamp before the final check; final check must reach BLOCK: 0 with links included)

Recent shapes to break (do not inherit): the desk's headline molds "X beat Y on nine of twelve datasets" and "X did A. Its authors did B."; deks built as "Author-and-year's paper does X, and Y"; and the heading mold "The [noun] that [verb]". Find this piece's own headline, dek, and heading constructions in its own nouns.

This round's focus: the evidence record notes the 2016 paper makes no generation-speed claim at all — every speed figure comes from Parallel WaveNet (2017) and DeepMind blog posts, and the four MOS readings sit on different corpora with different human baselines. Keep those attributions exact: do not let a later figure read as the 2016 paper's, and use the mean-opinion-score lesson's point (MOS does not travel) to keep the headline honest. Link the-mechanics/autoregressive-generation and the-instruments/mean-opinion-score in Background rather than re-teaching them.
