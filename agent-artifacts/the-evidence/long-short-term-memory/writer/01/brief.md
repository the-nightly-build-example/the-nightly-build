# writer brief: the-evidence/long-short-term-memory (01)

Inputs:
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/editorial-direction.md
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/commission.md
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/writing-coach/01/voice-guide.md
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/researcher/01/evidence.md — the complete claim set; treat it as the only claims available.
- .nb-work/the-evidence/long-short-term-memory/library/the-evidence/long-short-term-memory.html — the article to edit.
- .nb-work/the-evidence/long-short-term-memory/.nb-context/ — the template contract and furniture catalogs. Documented markup only.

Output: .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-evidence/long-short-term-memory/library/the-evidence/long-short-term-memory.html --series the-evidence --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where something you need is missing, ask me (the orchestrator).

The angle, stated precisely (do not overshoot it):
- The lesson's contribution is the gap between how SMALL the 1997 evidence was and how load-free the reputation is. "Modest evidence" is about SCALE, not strength. The 1997 within-scope result was strong and genuinely new: it solved long-time-lag tasks no prior recurrent method could. Do NOT write, or let a heading imply, that the famous paper was weak or flimsy. Show the small scale honestly and credit the real result — that tension is the piece.
- Concrete 1997 scale from the record: only small synthetic sequence tasks; networks roughly 264 to ~6,000 weights; two to four memory cells; time lags up to ~1000 steps; no real-world benchmark; the paper itself lists speech as future work. Use the record's exact numbers and task descriptions.

Corrections you MUST honour:
- The forget gate is NOT in the 1997 model. It was added by Gers, Schmidhuber & Cummins 2000 ("Learning to Forget"). The researcher could not open that 2000 paper firsthand (paywalled), so do not present a firsthand quote from it; its existence, 2000 date, purpose (resetting cell state on continual input streams), and absence from 1997 are established from three clean primaries in the record (the 1997 paper's silence, the 2024 xLSTM paper from Hochreiter's group, and Graves & Schmidhuber 2005). Attribute accordingly.
- The 2013 real-speech result is Graves, Mohamed & Hinton (Toronto), NOT Graves & Schmidhuber. Get the authorship right in prose and in the source list.

Teaching spine (series form: what the document is, what it did, how big, then the present): the vanishing/exploding gradient problem (teach it here, from Hochreiter 1991 and the 1997 paper); the constant error carousel and the input/output gates as the 1997 fix; the size of the demonstrations; then the present — LSTM in production speech (Graves & Schmidhuber 2005; Graves, Mohamed & Hinton 2013) and machine translation (Sutskever, Vinyals & Le 2014 seq2seq), transformer displacement (Vaswani et al. 2017), and the 2024 xLSTM revival — and what today's "LSTM" (the forget-gate "vanilla" cell) means versus the 1997 model.

Boundaries: backpropagation and gradient descent are taught — link the-evidence/backpropagation and the-mechanics/gradient-descent in Background and reference them with plain prose links at first mention, not numbered sources. Link the-evidence/seq2seq and the-mechanics/word-embeddings where the lesson leans on them rather than re-teaching. This is the document desk: stay on what the paper claimed and showed, not a general RNN tutorial.

Recent shapes to break: do NOT reuse the "the paper never measured/reports the thing it is famous for" dek mold (wavenet, imagenet) — it is not true here. Avoid the two-sentence dek whose second sentence reverses the first with a bare "actually/still." Avoid comma-triad headings closed with "and." Vary heading construction; outline your reasoning before naming sections.

Process reminder: body first, then both bookends; number sources in first-citation order with correct data-nb-kind; add data-nb-locator where the record gives one; a source asset (the memory-cell/gate diagram) via nb asset is welcome only if you capture it from the cited paper and use what it shows; a small table of the 1997 tasks/network sizes is a natural furniture choice, built only from the record; fill nb-meta (date 2026-09-22, harness "Claude Code", model = the model you run as); iterate with --no-check-links, then nb stamp and the exact nb check above until BLOCK: 0; put your one-sentence original-work statement in draft-handoff.md.
