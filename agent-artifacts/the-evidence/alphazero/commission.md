# Commission: the-evidence/alphazero

## The document

AlphaZero, as reported by David Silver and coauthors at DeepMind. Two texts
carry it: the December 2017 arXiv preprint "Mastering Chess and Shogi by
Self-Play with a General Reinforcement Learning Algorithm," and the December 2018
Science paper "A general reinforcement-learning algorithm that masters chess,
shogi, and Go through self-play." The lesson teaches the Science paper as the
document of record and uses the preprint where the two differ, because the
difference is part of the story.

## Why this document now

AlphaZero is invoked constantly as the proof that an AI can master a hard problem
from nothing but the rules and self-play, and as the ancestor of the "learn from
scratch" framing applied to today's reasoning models. The paper the course
already has on AlphaGo (`../the-evidence/alphago.html`) covers the earlier system
that learned from human games; AlphaZero is the one that dropped the human data.
The reader keeps meeting the claim "it taught itself" and cannot check what that
did and did not mean.

## The angle

What the paper actually did, held against how it is cited. The lesson lands on
the gap between the two. The chess result that made AlphaZero famous, a match win
over Stockfish, was run under conditions the paper states and its readers rarely
do: a fixed one-minute-per-move time control, a specific and now-old Stockfish
version, default settings without its opening book, and AlphaZero running on
hardware (TPUs) the comparison does not normalize. The generality claim is real
and worth teaching plainly, and so is the fact that a later, harder-fought
rematch context (TCEC-style conditions, and Stockfish's own later versions)
changes the picture the single headline number left. The paper is not wrong; the
citation of it usually is.

## What to teach (short list, in order)

1. What "self-play reinforcement learning from the rules alone" means here: no
   human games, no opening book, no handcrafted evaluation, one network trained
   against copies of itself. Contrast with AlphaGo's human-game bootstrap in one
   linked sentence, do not re-teach AlphaGo.
2. What the paper measured: three games (chess, shogi, Go), training compute and
   wall-clock, and the match results with their exact conditions. Give the real
   numbers and the denominators (games played, time control, hardware).
3. The one comparison that travels furthest and deserves the most care: AlphaZero
   vs Stockfish in chess. State the conditions the paper set, and what those
   conditions do and do not license as a claim about "stronger than Stockfish."
4. What holds up and what later work adjusted: the generality result stands; the
   specific strength claim was conditioned on a setup the chess community
   contested, and open replications (Leela Chess Zero) show the method reproduces
   while the headline margin depended on the match rules.

Keep it to these. Cut, do not compress, if the piece runs long.

## Template, bands, sources

- Template: lesson. Word band 1200-2200. Sections: why, orientation, 0-4 flex
  sections you name, takeaway, sources.
- Source floor (the-evidence/lesson): at least 6 sources, at least 3 primary and
  at least 1 secondary. Primary here means the documents that own the claim: the
  Science paper, the arXiv preprint, DeepMind/Google's own materials, and the
  Stockfish/TCEC/Leela primary records. Contemporary chess-community and press
  analysis of the match conditions is secondary and welcome for context, but the
  match conditions themselves must be pinned to a primary.

## Production policy (resolved)

Profile balanced. writing-coach: effort low, model capable. researcher: effort
high, model capable. writer: effort medium, model capable. editor: effort high,
model capable. None marked required. Roles run under the Claude Code harness on
this run's model; the writer records the actual harness and model it ran as in
nb-meta.

## Background links available in the library (verify and link, do not re-teach)

`../the-evidence/alphago.html` (the human-game predecessor),
`../the-evidence/atari-dqn.html`,
`../the-evidence/deep-rl-from-human-preferences.html`,
`../the-evidence/the-bitter-lesson.html` (Sutton's "scale and search beat
handcrafting" essay, which AlphaZero is cited to support). Use Background rows
only for lessons the reader may want and this piece does not re-explain.

## This run's neighbors (for coherence, not overlap)

Four other lessons publish tonight: the-instruments/auroc, the-mechanics/
attribute-binding, what-could-go-wrong/encoded-reasoning, and when-ai-breaks/
waymo-recall. None touch game-playing RL; no coordination needed beyond keeping
the paper's shared voice.

## Habits not to inherit (voice and shape)

Recent the-evidence pieces open on a flat surprise line and close on an abstract
"what it is asked to have settled" heading. Recent deks lean on the "X did A, and
B" comma-and mold. Do not copy either. Vary heading construction; the recent set
uses full-sentence claim headings almost exclusively, so a shorter noun-phrase
heading where the argument allows is a welcome break. No colon-subtitle headline.
