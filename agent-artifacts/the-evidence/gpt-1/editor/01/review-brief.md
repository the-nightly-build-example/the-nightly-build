# editor review-brief: the-evidence/gpt-1 (01)

Inputs:
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/commission.md` — the assignment, boundaries, reader
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/writer/01/brief.md` — the exact writer brief, including this round's exactness
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/writing-coach/01/voice-guide.md` — read first
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/researcher/02/evidence.md` — the claim set (round 02 carries round 01 forward plus the two secondaries)
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/writer/01/draft-handoff.md` — original-work sentence (open on the third read)
- Article: `.nb-work/the-evidence/gpt-1/library/the-evidence/gpt-1.html` (assets at `gpt-1/asset-1.png`, `gpt-1/chart-1.png`, provenance `gpt-1/chart-1.py`)
- Template context: `.nb-work/the-evidence/gpt-1/.nb-context/`

Output: `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/editor/01/editorial-review.md`

Proof (the writer's exact command; the orchestrator re-stamps and re-proves after your direct cuts):
`./nb check .nb-work/the-evidence/gpt-1/library/the-evidence/gpt-1.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's focus (push hardest here on the first read):
- The parameter count must be attributed to the GPT-2 report, not the 2018 paper
  (the paper gives only 12 layers / width 768 / 12 heads / FFN 3072 and no total).
  The corpus is "over 7,000 unique unpublished books" with the 11,038 BooksCorpus
  origin flagged, not blended. Verify both against the record.
- Results honesty: 9 of 12 datasets improved, three losses, the GLUE figure stated
  as the record has it (72.8 vs 68.9), the ablation's pre-training effect and the
  auxiliary-objective wash. The "ImageNet moment" reception must stay held apart
  from the modest 2018 margins (the record's Contradictions note). Push on any
  sentence that lets the paradigm framing borrow the small numbers' authority.
- Confirm the BERT-vs-GPT-1 head-to-head is linked, not rebuilt, and that the
  decoder and tokenization are linked, not re-taught.
- Inspect the visual evidence as the skill requires: open the captured Figure 1
  source asset (the four input-transformation diagrams) — crop must retain the
  evidence and omit clutter, caption factual and cited — and inspect the gains
  chart's committed provenance (`gpt-1/chart-1.py`) against the evidence numbers,
  reading the rendered image for honest axes/labels.

Recent-pattern notes (compare edges, headings, dek against these):
- the-evidence recently leaned on a lead figure plus a reversal in the dek
  (flashattention, mamba, imagenet-database, computing-machinery) and used a
  heading "The one number in the paper". Flag any echo, and the two-sentence
  "[Claim]. [Terse rebuttal]." headline mold and the full-sentence-with-a-figure
  heading rhythm on every subhead.
- Paper-wide: comma-triad dek closed with "and"; a "What <Person> saw in <place>"
  heading; a penultimate "what would settle it" section.
