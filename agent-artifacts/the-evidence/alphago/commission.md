# Commission: the-evidence/alphago

## Assignment
A lesson on the document **"Mastering the Game of Go with Deep Neural Networks
and Tree Search"** (Silver, Huang, Maddison, et al., *Nature* 529:484–489, 28
Jan 2016; DOI 10.1038/nature16961). The Evidence desk reads a famous AI
document so the reader knows what it actually says.

## Angle
Separate three things the public memory has fused: (1) what the *Nature* paper
actually built and measured, (2) the Lee Sedol match everyone remembers, and
(3) what later work changed. The paper's headline result was a 5–0 win over the
**European** champion Fan Hui in October 2015. The famous 4–1 win over Lee
Sedol happened in March 2016 and is **not** in this paper. And in 2017 a
successor, AlphaGo Zero, threw away the human-game training the 2016 system
depended on and beat that version 100–0, which revises what the original result
proved. Then assess, plainly, which of today's citations of AlphaGo the paper
actually supports.

## Intended reader
The house reader: smart, widely read, no time in a codebase. They have heard
"AI beat the world champion at Go" and cannot check what was really shown.
Reinforcement learning, self-play, and tree search are almost certainly new to
them and must be taught on the spot in plain words. Algebra and probability may
be assumed.

## Contribution this piece must make
A reader who finishes can (a) explain in plain words how AlphaGo combined two
neural networks with a search, and how it was trained; (b) state the honest
scale and opponent behind the 2016 result; and (c) judge when someone citing
AlphaGo today is overreaching (e.g., invoking it as proof that models can
bootstrap ability "from nothing" or "without data"). The visible original work
is the ledger that maps popular claims about AlphaGo onto what each cited
document (2016 paper, 2017 Zero paper, the Lee Sedol record) actually
establishes.

## Teach at most three ideas, completely
1. **The architecture: two networks guiding a search.** A *policy network*
   proposes plausible moves; a *value network* estimates who is winning from a
   position; Monte Carlo Tree Search uses both to look ahead selectively
   instead of reading every branch. Teach MCTS in plain words with a small
   concrete example. The advance was the combination, not any single part.
2. **How it was trained, and the honest scale.** Supervised learning first
   (the policy network learned to imitate human expert moves from a large set
   of amateur/expert games on the KGS server), then reinforcement learning by
   self-play (the network played itself and kept what won), then the value
   network trained on self-play positions. Give the real numbers the paper
   reports (number of games/positions, the Fan Hui result, hardware). Show how
   big or small the foundation is.
3. **What later work changed.** AlphaGo Zero (Silver et al., *Nature* 2017,
   "Mastering the game of Go without human knowledge") removed the human-game
   bootstrap and still surpassed the 2016 version. State what that revises: the
   human data was a shortcut, not a necessity. Bring it to the present: "search
   plus self-play" is cited again in 2024–2025 reasoning-model debates; say
   where that analogy holds (a game with perfect rules and a cheap win/loss
   signal) and where it strains (open-ended tasks with no such signal).

If three ideas do not fit 1200–2200 words, cut idea 3 to the Zero result plus a
one-paragraph present-day note; do not shrink ideas 1–2.

## Source obligations (the-evidence lesson)
- Minimum 6 sources; primary ≥ 3, secondary ≥ 1.
- The 2016 *Nature* paper is the primary that owns the method/scale claims —
  read the actual paper (or its author-hosted full text), not coverage of it.
- The 2017 AlphaGo Zero *Nature* paper is a required primary for idea 3.
- At least one secondary for the Lee Sedol match record and its date/score.
- Every number (games, positions, win rates, hardware, dates, Fan Hui's rank)
  verified against the owning primary.

## Starting sources (researcher verifies and expands)
- Nature 2016 paper landing + Google Research copy:
  https://www.nature.com/articles/nature16961 ;
  https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/
  (find a readable full text / author PDF; do not cite what you could not open).
- AlphaGo Zero 2017: "Mastering the game of Go without human knowledge",
  *Nature* 550:354–359 (DOI 10.1038/nature24270).
- Lee Sedol match (March 2016, 4–1): a contemporaneous report of record.
- Optional present-day: a primary or serious secondary tying test-time
  search/self-play in reasoning models back to AlphaGo.

## Relevant prior coverage — link, do not re-teach
- `the-evidence/the-bitter-lesson` — Sutton's argument that scaled search and
  learning beat hand-built knowledge; AlphaGo is his central example. Strong
  Background link.
- `the-evidence/deep-rl-from-human-preferences` — reinforcement learning from a
  learned signal; relevant contrast (Go has a free win/loss signal; language
  does not). Link if you invoke RLHF.
Do not cover ground these already teach as if new.

## Structures NOT to inherit (recent habits)
- Do **not** open with "The number X published about itself" — that opener was
  used twice in the last week (google-flu-trends, tokens-per-second).
- Avoid the comma-triad heading ("The tokenizer, the chip, and the prompt
  length"); it has recurred. Vary heading shape.
- Check recent deks before settling yours; no semicolon-reversal, suspended
  question, or comma-triad dek.

## Neighboring articles tonight (keep distinct)
energy-per-query (Instruments), over-refusal (Mechanics), racing-dynamics
(What Could Go Wrong), microsoft-tay (When AI Breaks). No overlap expected;
AlphaGo is the only RL/game-playing piece.

## Output paths
- Article: `.nb-work/the-evidence/alphago/library/the-evidence/alphago.html`
- Artifacts under `.nb-work/the-evidence/alphago/agent-artifacts/the-evidence/alphago/`
- Generated context under `.nb-work/the-evidence/alphago/.nb-context/`

## Production
harness `claude-code-routine`; writer model `claude-sonnet-5` (record these in
nb-meta). Effort guidance: researcher/editor high, writer medium, coach low.
Template `lesson`; mode `open`; order null; date 2026-08-02.
Tags (nb-meta, descriptive): reinforcement-learning, self-play, monte-carlo-tree-search, deepmind.
