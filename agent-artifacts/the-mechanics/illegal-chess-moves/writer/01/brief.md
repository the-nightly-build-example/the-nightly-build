# writer brief: the-mechanics/illegal-chess-moves (01)

Inputs:
- `editorial-direction.md` — house standard, this paper's voice, the series direction
- `writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting
- `researcher/01/evidence.md` — the complete set of claims available to you
- the initialized article at
  `.nb-work/the-mechanics/illegal-chess-moves/library/the-mechanics/illegal-chess-moves.html`
- the effective template context under
  `.nb-work/the-mechanics/illegal-chess-moves/.nb-context/`

Output: `writer/01/draft-handoff.md`

Proof (run from `/home/user/the-nightly-build`; iterate with `--no-check-links`,
then a final run with links until `BLOCK: 0`):

```text
./nb stamp .nb-work/the-mechanics/illegal-chess-moves/library/the-mechanics/illegal-chess-moves.html
./nb check .nb-work/the-mechanics/illegal-chess-moves/library/the-mechanics/illegal-chess-moves.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/7638a680-eec9-5b00-bc28-2a2eeb252ef4/scratchpad/library-checkout
```

nb-meta to fill: date `2026-09-07`, harness `Claude Code`, model `claude-opus-4-8`,
and subject tags of your choosing. Keep nb-meta `dek` identical to the rendered
dekline.

This round's focus: the evidence record's Contradictions section changes the
lesson, so build the mechanism around it rather than overclaiming. Two lines need
care, both flagged by the researcher:

- "The model has no board." True of any external board it consults, and that is
  settled. But small models trained only on game transcripts (Othello-GPT,
  Chess-GPT) do build a probeable internal board state, and no study has probed a
  large general-purpose chat model either way. Write the honest version: there is
  no separate board the model checks a move against; whatever board knowledge
  exists lives in learned next-token statistics and is only as reliable as those
  statistics. Mark the chat-model case as open.
- "Errors compound as the game leaves book openings." True for weak and chat
  models, but the strongest counter-example (gpt-3.5-turbo-instruct) holds a
  near-constant, near-zero illegal-move rate deep into novel positions. Do not
  state compounding as a universal law. The counter-example is the surprise the
  commission asked you to teach honestly, so give it real space.

Mark each step settled engineering or open question, as the series requires. The
contrast is an engine that holds a board and searches legal moves (AlphaZero,
Stockfish); keep it as contrast, not subject. No code.

Recent shapes to break (checked against the last eight lessons in this series):

- Do not use the headline mold "Ask <system> for <X> and it <does Y>" (clock-faces,
  random-numbers). Do not reuse the line "a model has no <X> to reach for"
  (random-numbers). Do not import the "an image generator <does X>" dek shape;
  this is a text behavior.

Link rather than re-teach: the-mechanics/autoregressive-generation,
the-mechanics/tool-use, the-mechanics/false-confidence. Background links use a
relative `../<series>/<slug>.html` href; Go deeper links point beyond the paper.
