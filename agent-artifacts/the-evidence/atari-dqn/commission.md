# Commission: the-evidence/atari-dqn

## The document

The 2015 Nature paper "Human-level control through deep reinforcement
learning" (Mnih, Kavukcuoglu, Silver, et al., DeepMind; Nature 518, 529-533,
DOI 10.1038/nature14236), with its 2013 NIPS-workshop precursor "Playing Atari
with Deep Reinforcement Learning" (arXiv:1312.5602) as context. This is the
Deep Q-Network (DQN) paper: one network, one set of hyperparameters, learning
to play 49 Atari 2600 games from raw pixels and the game score alone.

## Why this document, why now

The reader has met the RL lineage from the top down: AlphaGo, RLHF
(deep-rl-from-human-preferences), and RL-trained reasoning (deepseek-r1) are all
published in this desk. None of them taught the founding document those results
descend from, and none taught value-based RL at all. DQN is the paper the course
"just made readable": it is where "a deep network trained by reinforcement
learning" first worked, and its "human-level" headline is a textbook case of a
famous phrase outrunning what the tables underneath it show.

## The angle (the desk's signature tension)

How it is cited: the arrival of "human-level" AI control, the birth of deep RL,
the ancestor of everything from AlphaGo to reasoning models.

What it actually did: "human-level" was defined as scoring at least 75% of a
professional human games tester's score, and DQN cleared that bar on 29 of 49
games. On games needing any long-horizon plan it collapsed. Montezuma's Revenge
is the sharp case: it scored 0. The model held no model of the game, ran no
search, and planned nothing. Its real contribution was two stabilization tricks
that made a neural network trainable by Q-learning at all.

Thesis for the writer to prove: "human-level control" was a median claim across
49 games with enormous variance, and the paper's durable contribution is
experience replay plus the target network, not a machine that understood what it
was playing.

## What this lesson teaches (2-3 ideas, taught completely)

1. Value-based RL / Q-learning: the model learns Q(s,a), the expected future
   score of taking action a in state s, then acts greedily on it. Ground it in
   one concrete Atari moment (a Breakout paddle decision), with the actual
   inputs the paper used: four stacked 84x84 grayscale frames.
2. The two tricks that made "neural network + Q-learning" stop diverging:
   experience replay (store transitions, train on random minibatches to break
   the correlation between consecutive frames) and the separate target network
   (hold the training target fixed for a stretch so the network is not chasing a
   number it is simultaneously moving). Say plainly why the naive version
   diverges.
3. What "human-level" meant and where it failed: the 75%-of-a-tester
   definition, the 29-of-49 record, and Montezuma's Revenge at 0 as the case
   that exposes what value learning without exploration or planning cannot do.

Keep the list to these. Depth over coverage.

## Bring it to the present

What later work confirmed, corrected, or replaced: the "deep net + RL" template
held and generalized (the desk's AlphaGo and reasoning pieces are its
descendants), while the specific method proved brittle and sample-hungry.
Reproducibility work (Henderson et al. 2018, "Deep Reinforcement Learning that
Matters") showed how sensitive these results are to random seeds and
hyperparameters. Atari-from-pixels needs tens of millions of frames, weeks of
play, to reach those scores. Say where the citation ("human-level") no longer
matches the record.

## Boundaries (do not repeat; link instead)

- Gradient descent is taught in the-mechanics/gradient-descent. The reader has
  it. Link at first use; do not re-teach.
- AlphaGo (this desk) taught tree search and self-play. DQN is different: no
  search, no self-play, value-based, and it predates AlphaGo. Do not import
  AlphaGo's machinery or retell it.
- deep-rl-from-human-preferences and deepseek-r1 (this desk) cover RLHF and RL
  reasoning. Do not re-teach RL as if new; DQN is the earlier, different thing.
- Do not teach the full Bellman-equation math. Teach the idea of a value
  learned by bootstrapping, at the level the declared reader needs.

## Source obligations

Floor (lesson + series): at least 6 sources; primary >= 3, secondary >= 1.
Prefer, as primaries: the 2015 Nature paper and its supplementary per-game score
table, the 2013 arXiv precursor, and Henderson et al. 2018. Sutton & Barto's
textbook is a fair primary for the definition of Q-learning. A retrospective or
contemporaneous report can serve as secondary. Every number (the 49 games, the
75% threshold, the 29-of-49 count, the Montezuma's Revenge score) must be read
off the primary that owns it.

## Production policy (balanced profile; none required)

writing-coach effort low, researcher high, writer medium, editor high; model
"capable" for all, none required. Recorded run: harness claude-code-routine,
model claude-opus-4-8.

## Recent library shapes to break

Recent the-evidence deks lean on a "the paper never did X" reveal
(attention-is-all-you-need: "never trained a language model"; alphago: "never
mentions Lee Sedol"). The Montezuma's-Revenge-zero fact is strong, but do not
copy that exact "never" dek mold; find this piece's own line. Vary heading shape
from the recent run's comma-and-clause cadence.

## Neighboring articles this run (for coherence, not overlap)

the-instruments/parameter-count, the-mechanics/reading-images,
what-could-go-wrong/mesa-optimization, when-ai-breaks/ai-overviews. No topical
collision; keep this piece self-contained.
