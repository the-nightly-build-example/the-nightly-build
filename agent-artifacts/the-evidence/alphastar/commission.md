# Commission: the-evidence/alphastar

## Assignment

One lesson for The Evidence reading the document behind "AI reached Grandmaster at
StarCraft II": Vinyals et al., "Grandmaster level in StarCraft II using multi-agent
reinforcement learning" (Nature, 2019). Read the paper itself, alongside the
January 2019 demonstration materials and DeepMind's own posts, so the reader knows
what AlphaStar actually did and under what conditions.

## What this lesson teaches

State what the document is, who built it, and why it became famous. Walk through
what it actually did: the training pipeline (supervised imitation from human
replays, then a league of agents playing each other with main agents and
exploiters), the interface the agent used, and how "Grandmaster" was measured
(anonymous play on the official Blizzard ladder, reaching the top tier). Show the
scale and the caveats honestly: the actions-per-minute limits and camera-interface
constraints that changed between the January 2019 showcase and the Nature version,
the reliance on human replays (unlike a pure self-play system), and what
"Grandmaster on the ladder" does and does not claim versus beating the world's best
in a controlled series.

Then bring it to the present: how the result is cited now as a milestone for
reinforcement learning in real-time, imperfect-information games, whether that
framing matches the paper, and what the APM/camera debate and the human-replay
bootstrap mean for the "superhuman" claim. When the popular memory does not match
what the paper showed, say so plainly.

## Boundaries and neighbors

Distinct from the library's existing game-playing lessons; link them in Background,
do not retread:
- the-evidence/alphago (Go, bootstrapped on human positions, matches vs Fan Hui/Lee Sedol)
- the-evidence/alphazero (pure self-play, no human data, Go/chess/shogi)
- the-evidence/atari-dqn (Atari, the DQN stabilization tricks)
AlphaStar's own subject is the league training, the human-replay start, the
real-time imperfect-information setting, and the interface constraints. The reader
is smart and widely read but new to reinforcement learning; define league play,
actions per minute, and imperfect information in plain words at first use.

## Contribution the article must add

Separate what AlphaStar demonstrated (Grandmaster-tier ladder play from imitation
plus league RL, under a constrained interface) from how it is remembered
("AI crushed the pros"), and make the APM/camera and human-replay caveats legible
to a reader who only saw the headline. The writer states the exact original-work
sentence in the handoff.

## Sources

Series/template floor: at least 6 sources, at least 3 primary, at least 1
secondary. Primaries available: the Nature 2019 paper and its supplementary
material; DeepMind's AlphaStar blog posts (January and October 2019); Blizzard/
ladder details on the play conditions. Secondary: contemporaneous reporting and the
players' (TLO, MaNa) commentary for context.

## This edition (keep distinct from the run's other four lessons)

- the-instruments/self-consistency-scoring
- the-mechanics/output-diversity
- what-could-go-wrong/mind-crime
- when-ai-breaks/amazon-rekognition-congress (already published tonight)

No subject overlap. Like several pieces tonight it turns on "the headline overstated
the result," so root this one in AlphaStar's specific training method and play
conditions rather than a generic debunk.

## Habits not to inherit (from the recent library)

- Recent The Evidence deks run as one long sentence carrying an embedded numeric
  contrast; give this dek a stance and one identifying detail.
- Recent headings lead with a raw number or use the "X did, Y did not" contrast;
  vary construction.
- The recurring furniture stack is nb-stat-strip, nb-figure, nb-table, nb-note.
  Plan furniture from the supplied catalog for this piece.

## Production

Profile balanced. Model: capable (Claude Opus 4.8) for every role. Effort per
production policy: writing-coach low, researcher high, writer medium, editor high.
No required directive is in force. The writer records the actual writer model in
nb-meta per the library's convention (harness "claude-code").
