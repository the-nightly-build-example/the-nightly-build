# writer brief: the-evidence/alphazero (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, paper voice, series prompt, citation standard.
- writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- researcher/01/evidence.md — the complete set of claims available to you; use the Numbers section exactly.
- commission.md (artifact root) — subject, teaching list, source floor, habits not to inherit.
- The initialized article: library/the-evidence/alphazero.html (edit it in place; keep chrome exact).
- .nb-context/ (effective template contract, furniture catalogs, runtime assets).

Output: writer/01/draft-handoff.md (plus the edited article).

Proof: ./nb check .nb-work/the-evidence/alphazero/library/the-evidence/alphazero.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout

This round's focus — the evidence corrects the commission's angle; follow the evidence:
- Do NOT pin the flimsy match conditions (one minute per move, no opening book, Stockfish 8 on 64 threads) on the Science 2018 paper. Those belong to the December 2017 arXiv preprint. The lesson teaches the Science paper as the document of record, and it already answered most of the 2017 criticism: 1000 games at a 3-hour + 15-second increment control, the latest Stockfish, 44 CPU cores, plus a separate opening-book match, and it still won (155-6-839). Teach that honestly.
- The caveats that genuinely survive for the Science match are the ones to land: TPU-vs-CPU hardware is never normalized (DeepMind itself calls it not directly comparable), the primary opponent is still Stockfish 8, and it was DeepMind's own internal match. Independent vindication came later and from outside DeepMind (Leela Chess Zero winning TCEC Season 15, 2019), and the ranking did not stay put once Stockfish adopted its own neural evaluation (NNUE, 2020). The durable lesson is convergence on neural-evaluation-plus-search, not that AlphaZero permanently out-ranks Stockfish. The generality claim (one algorithm, three games, from the rules alone) is solid and uncontested.
- One condition is only inferred, not quoted (whether Stockfish had endgame tablebases): state the uncertainty, do not assert it.

Habits not to inherit (from commission.md): vary heading construction (recent the-evidence pieces use full-sentence claim headings almost exclusively); avoid the comma-and dek mold and the abstract "what it is asked to have settled" closer-heading; no colon-subtitle headline. Background rows may link ../the-evidence/alphago.html and other confirmed library lessons; do not re-teach AlphaGo, link it.
