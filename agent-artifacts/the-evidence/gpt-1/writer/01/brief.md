# writer brief: the-evidence/gpt-1 (01)

Inputs:
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/editorial-direction.md` — house standard, paper voice, series prompt
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/writing-coach/01/voice-guide.md` — how this piece should sound; read before drafting
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/researcher/02/evidence.md` — the complete claim set (round 01 carried forward plus the two secondaries); use the Numbers section exactly
- `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/commission.md` — assignment, boundaries, habits to break
- Article to edit in place: `.nb-work/the-evidence/gpt-1/library/the-evidence/gpt-1.html`
- Template context: `.nb-work/the-evidence/gpt-1/.nb-context/`

Output: `.nb-work/the-evidence/gpt-1/agent-artifacts/the-evidence/gpt-1/writer/01/draft-handoff.md`

Proof (run with links, until BLOCK: 0):
`./nb check .nb-work/the-evidence/gpt-1/library/the-evidence/gpt-1.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/fb9d317b-0db5-5e4f-9677-1de8446e916f/scratchpad/library-checkout`

This round's exactness (the evidence forces these):
- The GPT-1 paper states no total parameter count. The familiar "117 million" is
  the GPT-2 report's figure for its smallest model, which that report calls
  equivalent to the original GPT. Do not write "GPT-1 had 117M parameters" as if
  the 2018 paper said so; either attribute the figure to the GPT-2 report or state
  that the paper gave only the shape (12 layers, width 768, 12 heads, FFN 3072)
  and left the total unstated.
- Report the results honestly. Several headline gains are small (e.g., SNLI about
  +0.6); the model lost to a prior baseline on 3 of 12 datasets; the ablation
  shows the auxiliary language-model objective slightly lowered the average; and
  the GLUE gain is stated two ways in the paper (intro 5.5% vs body 3.9 points).
  The paradigm's reach is the claim, not the size of the 2018 numbers. Keep those
  two distinct, as the record's Contradictions note warns.
- The corpus: the paper says "over 7,000 unique unpublished books"; the
  BooksCorpus origin paper reports 11,038. Cite the paper's own figure and note
  the discrepancy rather than blending them.
- The present: the surviving half of the 2018 recipe is unsupervised generative
  pre-training; per-task fine-tuning and the task-specific input transformations
  were displaced (GPT-2 "without any parameter or architecture modification,"
  GPT-3 without gradient updates, prompting at scale). Cite firsthand.
- Link, do not re-teach: the-evidence/bert (do not rebuild the BERT-vs-GPT-1
  head-to-head), the-evidence/attention-is-all-you-need (the decoder),
  transformers-first-principles/tokenization and /embeddings.
- Set nb-meta `harness` to `claude-code`, `model` to the model you run as, date
  2026-09-17. Keep nb-meta `dek` identical to the rendered dekline.
