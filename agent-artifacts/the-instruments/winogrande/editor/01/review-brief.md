# editor review-brief: the-instruments/winogrande (01)

Inputs:
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/commission.md` — the assignment, boundaries, reader
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/writer/01/brief.md` — the exact writer brief, including this round's exactness
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/writing-coach/01/voice-guide.md` — read first
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/researcher/01/evidence.md` — the claim set
- `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/writer/01/draft-handoff.md` — original-work sentence (open on the third read)
- Article: `.nb-work/the-instruments/winogrande/library/the-instruments/winogrande.html` (chart at `winogrande/chart-1.png`, provenance `winogrande/chart-1.py`)
- Template context: `.nb-work/the-instruments/winogrande/.nb-context/`

Output: `.nb-work/the-instruments/winogrande/agent-artifacts/the-instruments/winogrande/editor/01/editorial-review.md`

Proof (the writer's exact command; the orchestrator re-stamps and re-proves after your direct cuts):
`./nb check .nb-work/the-instruments/winogrande/library/the-instruments/winogrande.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's focus (push hardest here on the first read):
- Attribution exactness: "273" belongs to the standardized WSC273 set, not the
  2012 paper ("more than 100" schemas). Verify. The near-human machine figure is
  UNICORN 86.6% (firsthand); the 91.2% leaderboard entry must not appear as
  verified anywhere. The "over 118K instances for human-level" is the paper's own
  claim (fit-mismatch noted), not endorsed arithmetic.
- The learning-curve spine (about 50.4% to 79.1% on the same filtered items vs
  human 94.0%) must carry the point that the difficulty is engineered, not fixed.
  Check every figure against the record's Numbers section.
- The counter-critique must be steelmanned fairly (the "Defeat of the WSC" paper
  and AFLite's own concession that it defines "hard" relative to one model's
  embeddings), and the misled case costed (IJCAI-16 58%; models mid-80s to ~90s
  while designers judge little reasoning gained; GPT-3 and Llama 2 still publish
  WinoGrande while flagging contamination).
- Inspect the chart: open `winogrande/chart-1.py` provenance, compare its numbers
  with the evidence and cited primary, and read the rendered image for honest
  axes, scale, and labels.

Recent-pattern notes (compare edges, headings, dek against these):
- the-instruments recently closed with clipscore's "What happens when the grade
  becomes the goal"; do not let a Goodhart-closer heading recur. Watch for the
  compression-definition heading mold ("One cosine, clipped and stretched",
  "Five words, averaged") and the "checked on X, trusted on Y" phrasing.
- Paper-wide: two-sentence terse-rebuttal headline; comma-triad dek closed with
  "and"; "What <Person> saw in <place>" heading.
