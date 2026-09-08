# Draft handoff: the-evidence/alphazero (01)

## Original-work sentence

This lesson pulls apart the two AlphaZero chess matches that citations collapse
into one, pinning the famous one-minute-per-move, no-opening-book conditions to
the December 2017 preprint rather than the 2018 Science paper of record, and it
splits the durable generality result (one algorithm, three games, from the rules
alone) from the temporary "stronger than Stockfish" ranking that Leela and
Stockfish's own NNUE later unsettled. The work is visible in the two-matches
section, the side-by-side conditions table, and the final section's convergence
argument.

## Proof result

`./nb check .nb-work/the-evidence/alphazero/library/the-evidence/alphazero.html
--series the-evidence --library <scratchpad>/library-checkout` reaches
**BLOCK: 0, WARN: 0** (with links). `nb stamp` written: words 1802,
reading_minutes 8, sources 9 (5 primary, 4 secondary; floor is 6 / 3 primary /
1 secondary). nb-meta dek is identical to the rendered dekline.

## Warnings intentionally left

None. No proof warnings remain.

## Open evidence question carried into the prose (not a proof warning)

Whether Stockfish was given its endgame tablebases in either match is not stated
in either paper's main text (the evidence record flags it as inferred, not
quoted, and the Science supplementary tables S8-S9 were not opened). Per the
brief, the article states this uncertainty plainly rather than asserting it, in
a note labeled "Not stated in either paper" in the two-matches section. If the
editor can open the Science supplement, this could be upgraded from silence to a
reported fact.

## Angle followed (per the writer brief's correction)

- The harsh conditions (1 min/move, Stockfish 8 on 64 threads, no opening book,
  4 TPUs) are pinned to the 2017 preprint, not the Science paper.
- The Science match is taught as the document of record: 1000 games at
  3 h + 15 s, Stockfish on 44 cores, plus the opening-book and latest-Stockfish
  matches, result 155-6-839. It answered most of the 2017 criticism and still
  won.
- Surviving caveats landed: unnormalized TPU-vs-CPU hardware (DeepMind's own
  "not directly comparable"), primary opponent still Stockfish 8, DeepMind's
  in-house match. Independent vindication from outside (Leela, TCEC S15, 2019);
  ranking did not stay put (Stockfish NNUE, 2020). Durable lesson framed as
  convergence on neural-evaluation-plus-search, not permanent AlphaZero
  supremacy. Generality claim taught plainly as solid and uncontested.
- AlphaGo linked, not re-taught (prose link plus Background row).
