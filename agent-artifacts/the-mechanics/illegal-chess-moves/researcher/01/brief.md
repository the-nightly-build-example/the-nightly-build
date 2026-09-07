# researcher brief: the-mechanics/illegal-chess-moves (01)

Inputs:
- `editorial-direction.md` — citation standard, series territory, declared reader
- `commission.md` — the assignment, its boundary, and the source floor
- this brief

Output: `researcher/01/evidence.md`

Subject: why language models make illegal or board-losing moves in chess, and the
mechanism behind it. Read the primary experiments and representation research
firsthand, not commentary about them.

Answer these, each traceable to the owning source:

- How a language model is given a chess game as input and asked to continue it:
  move notation as a token stream, no separate board the model consults. Establish
  this from a paper or documented experiment that actually ran it.
- What the measured failure looks like: rates of illegal moves, and how errors
  rise as a game leaves common opening lines. Give real numbers with the model and
  study that owns each.
- The genuine counter-evidence: the documented case of gpt-3.5-turbo-instruct
  playing at roughly club strength (and how much better it plays than chat models),
  from a reproducible source. State what is claimed and how firmly it holds.
- The internal-representation question: the Othello-GPT work ("Emergent World
  Representations", Li et al. 2023) and any follow-up (for example Neel Nanda's
  linear-probe reproduction) or dispute, plus any chess-specific probing. What is
  actually shown about whether models build a board state, and what remains open?
- The contrast that grounds the mechanism: engines such as AlphaZero or Stockfish
  hold a board and search legal moves. Keep this to the contrast, not the subject.

Meet the floor with sources that change the interpretation, not padding: at least
8 sources, at least 4 primary, at least 1 secondary. Mark each claim as settled
engineering or open question, since the lesson must draw that line. Search for what
breaks the commission's angle (evidence that models do track the board well) and
record it in Contradictions. Confirm every URL resolves to the document's own page.
