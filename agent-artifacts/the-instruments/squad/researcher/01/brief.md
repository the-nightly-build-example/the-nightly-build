# researcher brief: the-instruments/squad (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/commission.md — the angle, required contribution, and source floor
- /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-instruments/squad/agent-artifacts/the-instruments/squad/researcher/01/evidence.md

Answer these, from the primary documents:
- How EM and F1 are computed on SQuAD, exactly: the official eval script's
  normalization (lowercasing, article/punctuation stripping), token-overlap F1,
  and how multiple reference answers are handled (max over references). Get the
  precise definitions.
- SQuAD 1.0's construction and scale: number of questions, passages, source
  (Wikipedia), that every answer is a span of the passage. Exact figures.
- The human-performance number: how it was actually measured (who answered, how
  many questions, single-estimate vs multi-reference), the reported human EM/F1,
  and the exact date/systems of the early-2018 crossings (Microsoft R-Net/nlnet,
  Alibaba SLQA). Verify the "superhuman" framing against what the leaderboard and
  papers actually claimed.
- Jia & Liang (2017) adversarial SQuAD: the method (appending a distractor
  sentence), the exact drop in F1 for the top systems, and what it shows about
  span-matching vs comprehension.
- SQuAD 2.0: why it was built (unanswerable questions), how many were added, and
  how the metric changed. Exact figures.
- Contradictions: any defense that the human baseline was fair, later work
  arguing SQuAD scores did track real progress, or disputes over the
  adversarial-SQuAD interpretation. Record them.
Source floor: at least 8 sources, at least 4 primary, at least 1 secondary.
