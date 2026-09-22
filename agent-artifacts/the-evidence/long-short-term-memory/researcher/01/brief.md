# researcher brief: the-evidence/long-short-term-memory (01)

Inputs:
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/editorial-direction.md — the standing editorial, sourcing and slop standards for this article.
- .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/commission.md — the assignment, angle, boundaries, and the resolved source obligations (minimums and the must-open primary documents).

Output: .nb-work/the-evidence/long-short-term-memory/agent-artifacts/the-evidence/long-short-term-memory/researcher/01/evidence.md

Work from these inputs. Do not tour the repository, the Git history or the archive for background. You may use web, document and nb history tools. Read the primary documents themselves, not coverage of them; open the cited passage and record honest locators. Where something you need is missing, ask me.

Run-environment note: outbound HTTPS is proxied; a 403 or paywall means gated, not dead — try a proper browser request before giving up, and record the address where the document lives, not the fetch route.

Priority questions to answer (meet the source minimums in commission.md with sources that could change the interpretation, not padding):
- What problem the 1997 LSTM paper states it solves, in its own words, and how it frames the vanishing/exploding gradient problem (cross-check Hochreiter 1991).
- The exact architecture the 1997 paper defines: the constant error carousel, the input and output gates. Confirm the 1997 paper has NO forget gate, and that Gers/Schmidhuber/Cummins 2000 added it.
- The experiments in the 1997 paper: which tasks, sequence lengths, network sizes, and success criteria. Get concrete numbers; show how small they are.
- The present: LSTM in production speech (Graves & Schmidhuber) and machine translation (Sutskever et al. 2014 seq2seq), then transformer displacement (2017+), then xLSTM (Beck et al. 2024). What today's 'LSTM' citations mean vs the 1997 model.
- A source asset: any figure from the paper (e.g. the memory-cell/gate diagram) worth showing.
