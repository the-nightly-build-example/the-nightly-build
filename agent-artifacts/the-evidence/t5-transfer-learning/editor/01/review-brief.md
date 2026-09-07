# editor review-brief: the-evidence/t5-transfer-learning (01)

Inputs:
- `editorial-direction.md` — the standard, voice, and series direction
- `commission.md` — the assignment, boundary, and the reader's situation
- `writer/01/brief.md` — the exact brief the writer worked from
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplars
- `researcher/01/evidence.md` — the evidence record; read it against the claims
- `writer/01/draft-handoff.md` — the original-work sentence and any warning left
- the article at
  `.nb-work/the-evidence/t5-transfer-learning/library/the-evidence/t5-transfer-learning.html`
- template context under `.nb-work/the-evidence/t5-transfer-learning/.nb-context/`

Output: `editor/01/editorial-review.md`

This round's focus: verify the piece attributes figures to the source that owns
them. The paper's "about 750 GB" for C4 belongs to the paper; the released dataset
(about 807 GiB) and t5.1.1 checkpoints belong to the artifacts, and the article
must not blur them. Scale is given in tokens, not a compute figure the paper never
states. Confirm the present-day reckoning is stated plainly and holds against the
record: 18 of 24 tasks best-of-their-time but all three WMT translation tasks lost,
2019-era scores since surpassed, the encoder-decoder-best finding in tension with
the field's decoder-only turn, instruction tuning as later work (Flan-T5). The
draft sits at the top of the word band (2200); trim from middles where a sentence
does no work rather than letting length ride the ceiling.

My recent-pattern notes (compare edges, dek, and headings against these; this
series' last eight lessons):

- Dek mold "<Authors>'s <year> paper <did X>, then/and <measured Y>" (dropout,
  constitutional-ai, denoising-diffusion, adversarial-examples). The "company's own
  report can't/does X" headline (llama-3-herd-of-models). The phrasings "measured
  it directly" and "in its own experiments." Catch any of these as formula.

The lesson template allows only the two bookend cards to address the reader; hold
every other sentence to the no-self-reference rule.
