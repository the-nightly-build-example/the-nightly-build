# researcher brief: the-evidence/alphazero (01)

Inputs:
- editorial-direction.md (artifact root) — citation standard, series territory, declared reader.
- commission.md (artifact root) — the document, the angle, what the lesson teaches, and the source floor.

Output: researcher/01/evidence.md

Research questions to answer from primary sources, reading the cited passages
themselves:

1. The AlphaZero method as the paper states it: no human game data, no opening
   book, no handcrafted evaluation; one network; self-play; the search (MCTS)
   at a high level. Pin each to the Science 2018 paper and note where the Dec
   2017 arXiv preprint differs.
2. The exact training figures: training steps/time, number of self-play games or
   the stated compute, and hardware (TPUs), for chess, shogi, and Go. Give
   figures with units and denominators.
3. The chess match against Stockfish, in full: which Stockfish version, the time
   control, whether an opening book or tablebases were used, the number of games,
   the score (wins/draws/losses), and the hardware each side ran on. This is the
   contested claim; get every condition from the primary. Note the difference
   between the preprint's match setup and the Science paper's revised, longer
   time-control match with expert-opening-book variants.
4. What the chess and computer-chess community said about those conditions at the
   time, and what open replication (Leela Chess Zero / Lc0) later showed about
   whether the method reproduces. Distinguish primary records (TCEC results,
   Lc0 project materials, statements by Stockfish developers) from secondary
   commentary.
5. Contradictions and limits: where the generality claim is solid, where the
   specific "stronger than Stockfish" claim is conditioned on the setup, and any
   correction or clarification DeepMind itself issued.

Classify each source primary or secondary with the reason. Meet the floor in
commission.md with sources that change the interpretation, not padding. If a
match condition cannot be pinned to a primary, record that gap explicitly.
