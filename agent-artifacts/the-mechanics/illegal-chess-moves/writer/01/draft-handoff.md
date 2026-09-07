# Draft handoff: the-mechanics/illegal-chess-moves (01)

## Original-work sentence

The article resolves one chatbot illegal move into a single causal chain the
sources never assemble in one place — no external board is ever checked (settled);
small models trained only on transcripts nonetheless build a provable, causally
used internal board (settled, but only on purpose-built small models); and the
late-game collapse everyone assumes is universal is actually a weak-model property
that the strongest completion model refutes — then pins the whole model-to-model
legality gradient to the quality of learned next-token statistics, with the
rules-holding engine as the floor beneath it.

## Proof result

Final `nb check` WITH links: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
Stamped: 2199 words, 10 min, 13 sources (12 primary + 1 secondary; source floor
met). All 13 source URLs resolved under link checking. No warnings left standing.

Reaching BLOCK/WARN 0 took a long trim: the first clean draft ran 2411 words
(lesson band ceiling 2200). Cut to 2199 by tightening prose only — no source,
number, contradiction, or settled/open mark was dropped. Two W-SENTENCE-DENSITY
notes and one W-PLACEHOLDER (all-caps stat label) were fixed, not waived.

## How the brief's two flagged lines were handled

- **"The model has no board."** Written as the honest version the brief asked
  for: there is no separate board the model checks a move against, and any board
  knowledge lives in learned next-token statistics (section "There is no board").
  The counter-evidence gets its own section: small transcript-trained models
  (Othello-GPT, Chess-GPT) build a linearly-decodable, causally-usable internal
  board. The chat-model case is marked open in a dedicated "Open question" note:
  no board-representation study has been run on GPT-4/Claude/any chat LLM, and
  that is named as the record's most important limit.

- **"Errors compound as the game leaves book openings."** Not stated as a law.
  Taught as the failure mode of weak/chat models (Yedidia: illegal by ~move 14),
  then explicitly refuted for gpt-3.5-turbo-instruct (Acher: roughly constant
  rate; Dynomight: legal deep into never-before-seen positions). The
  counter-example is given real space as the section's turn.

Also handled from the record's Contradictions: the harness-dependence of illegal
rates (Karvonen's ≤5/8,205 vs Acher's 16% of games, same model) is stated
plainly; the Li→Nanda nonlinear→linear correction is reported in order; the
Elo≥1800 pretraining filter is given only as "reported / not confirmed against a
primary OpenAI document." The engine (AlphaZero/Stockfish) is kept as contrast,
not subject. No code.

## Open questions for the editor

- **None blocking; no researcher gap.** The one substantive open item (whether a
  large chat model holds a board representation) is the article's marked open
  question, not a hole.
- **One judgment call to sanity-check:** David Barry is "1800 FIDE" with a "1900
  blitz rating" in the evidence. I describe him as "an 1800-rated human" (his
  FIDE rating, the label the evidence leads with) even though the cited result is
  a blitz match. Accurate as written; flagging in case the editor prefers the
  blitz figure named instead.

## Furniture used

Stat strip (orientation, the strong model's competence), one table (the per-model
legality gradient, Acher's single harness), one "Open question" note (the chat-LLM
limit). No chart or source asset: the house rule requires charts be redrawn from
data, and the gradient reads cleanly as a table; no source visual was load-bearing
enough to spend an asset on.
