# Commission: the-mechanics/illegal-chess-moves

## Assignment

Teach the reader why a chatbot playing chess eventually makes an impossible move:
it tries to move a piece that is not there, ignores a check, or loses track of
where the pieces stand. This is The Mechanics: start from a behavior the reader
has seen and work backward to its cause, step by step, until nothing below the
last step would change the answer.

Work the chain down. A language model plays chess by predicting the next token in
a stream of move notation (a game written as text, for example "1. e4 e5 2. Nf3"),
not by holding a board and checking a move against the rules. Show what that means
concretely: the model has no separate board state it consults, so legality is
whatever the learned text distribution makes likely, and errors compound as a game
leaves the well-trodden openings its training text covered densely. Teach the one
genuinely surprising and contested fact honestly: some models play far better than
this picture suggests (the noted case of gpt-3.5-turbo-instruct playing at roughly
club strength), and research on whether models build any internal representation of
the board (the Othello-GPT line of work) is a real, open question. Mark which steps
are settled engineering and which are open.

By the end the reader can explain why the illegal move happens, not just that it
does, and can tell when someone's explanation skips a step. No code.

## Boundary and contribution

One behavior: illegal or board-losing moves in chess (and the same failure in
other exact state-tracking games). The required contribution: the reader can name
the mechanism (next-token prediction over notation with no enforced board state),
hold it against the counter-evidence (models that play surprisingly well, and the
internal-representation research), and say what is settled versus open. Do not
drift into a general essay on reasoning or a review of game-playing AI like
AlphaZero, whose search-plus-board design is the contrast, not the subject.

Reader is the paper's declared reader (see `editorial-direction.md`): smart,
widely read, no time in a codebase. Autoregressive next-token generation,
in-context learning, and tool use are taught in this library; link, do not
re-teach. Candidates for Background linking: the-mechanics/autoregressive-generation,
the-mechanics/tool-use, the-mechanics/false-confidence.

## Source policy

Series and lesson floor (from `nb source-policy --series the-mechanics`): at least
8 sources, at least 4 primary, at least 1 secondary. Primary owns its claim: a
paper reporting a chess-playing experiment and its results, the Othello-GPT world-
representation paper and any follow-up that reproduces or disputes it, and
documented, reproducible reports of a specific model's chess strength (the
gpt-3.5-turbo-instruct case). Secondary reporting supplies context.

## Production policy

From `nb production-policy --series the-mechanics`: profile balanced, model tier
"capable", none required. Effort: researcher high, writer medium, editor high,
writing-coach low. Runtime: roles run as Claude Code Agent subagents; researcher,
writer, and editor on claude-opus-4-8, writing-coach on a capable model at low
effort. The writer records its actual model (claude-opus-4-8) and harness
("Claude Code") in nb-meta. Publication date: 2026-09-07.

## This edition's neighbors

Four other lessons publish tonight; keep this piece distinct from each:
the-evidence/t5-transfer-learning, the-instruments/math-benchmark,
what-could-go-wrong/sleeper-agents, when-ai-breaks/replit-agent-deletes-database.

## Recent habits to break

Checked against the last eight The Mechanics lessons. Break these:

- The headline mold "Ask <system> for <X> and it <does Y>" is heavily used
  (clock-faces, random-numbers). Do not write "Ask a chatbot to play chess and it
  makes an illegal move." Find the real surprise and state it.
- Opening the piece on an image-generation behavior is the recent default; this
  is a text-generation behavior, which already separates it. Do not import the
  "an image generator <does X>" dek shape.
- The mechanism line "a model has no <X> to reach for" appears verbatim in
  random-numbers. Do not reuse it; describe the missing board state in this
  lesson's own terms.
