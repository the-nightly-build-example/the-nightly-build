# Evidence: the-evidence/atari-dqn (01)

The record strongly supports the commission's angle. Every load-bearing figure was
read off the primary that owns it. The 2015 Nature DQN paper itself states the
"human-level" bar as **75% of a professional human games tester's score** and reports
DQN clearing it on **29 of 49 games**; I independently reproduced that count from the
paper's own Extended Data Table 2, and also verified the stricter reading (DQN at or
above the human's actual score, i.e. 100%+) holds on only **23 of 49**. Montezuma's
Revenge is confirmed at **0 (±0), 0.0% of human** directly from that table. The two
stabilization tricks are documented verbatim, with one correction to the commission:
**experience replay is present in the 2013 precursor, but the separate/periodically
updated target network is a 2015 Nature-paper addition** — the commission's idea #2
attributes both to "the paper," and the writer should attribute the target network to
the Nature version specifically. The Q-learning definition is anchored to Sutton &
Barto. The record is thin in one place the commission leans on: Henderson et al.'s
reproducibility results are on **policy-gradient methods (TRPO, DDPG, PPO) on MuJoCo
continuous control, not on DQN/Atari**. They establish that deep RL as a field is
seed- and hyperparameter-fragile, but they do not directly measure DQN's seed
sensitivity. Do not write that Henderson "showed DQN is sensitive to seeds"; write
that Henderson showed the fragility of the deep-RL methods DQN launched.

## Sources

```text
URL:         https://www.nature.com/articles/nature14236
Kind:        primary. Mnih, Kavukcuoglu, Silver et al. (Google DeepMind), the
             authoring party; Nature 518, 529-533 (26 Feb 2015), DOI
             10.1038/nature14236. Owns every DQN result. (Read in full text from
             the authors' DeepMind-hosted copy of the same paper; the address
             recorded is the paper's own Nature/DOI page.)
Establishes: 49 games; the 75%-of-a-professional-human-games-tester definition of
             human-level; the 29-of-49 count; Montezuma's Revenge = 0; experience
             replay; the separate target Q-network; the 84x84x4 input; 50M training
             frames (~38 days); the replay/target ablation (Extended Data Table 3).
Paraphrase:  A single convolutional network with one fixed set of hyperparameters
             learns 49 Atari games from raw pixels and the game score, matching a
             professional human tester on average and exceeding 75% of the human
             score on 29 of the 49 games. It fails on games needing long-horizon
             planning (Montezuma's Revenge). Stability comes from experience replay
             plus a periodically cloned target network.
Locators:    Abstract; main text p.529-531; Fig.3; Methods "Training details" and
             "Target network"/replay paragraphs; Extended Data Table 2 (per-game
             scores); Extended Data Table 3 (ablation).
Quote:       "our DQN agent performed at a level that was comparable to that of a
             professional human games tester across the set of 49 games, achieving
             more than 75% of the human score on more than half of the games (29
             games...)."
             "operationalized as a level of 75% or above."
             "We trained for a total of 50 million frames (that is, around 38 days
             of game experience in total) and used a replay memory of 1 million most
             recent frames."
             "every C updates we clone the network Q to obtain a target network ^Q
             and use ^Q for generating the Q-learning targets... for the following C
             updates."
             "temporally extended planning strategies still constitute a major
             challenge for all existing agents including DQN (for example,
             Montezuma's Revenge)."
```

```text
URL:         https://arxiv.org/abs/1312.5602
Kind:        primary. Mnih et al., "Playing Atari with Deep Reinforcement Learning"
             (NIPS 2013 Deep Learning Workshop). The authoring party; the precursor.
Establishes: The 2013 seven-game version; experience replay already present;
             preprocessing to 84x84 grayscale, last 4 frames stacked; and the
             ABSENCE of a periodically cloned target network (targets use previous-
             iteration weights, not a separate frozen network).
Paraphrase:  The first deep network trained by a Q-learning variant on raw Atari
             pixels, tested on seven games, using experience replay to break
             correlations between consecutive frames. It beats prior methods on six
             of seven games and a human expert on three. It does not yet use the
             separate target network of the 2015 paper.
Locators:    Abstract; Sec 4 "Experiments"; Sec 4.1 "Preprocessing and Model
             Architecture"; Sec 3/Algorithm 1; Eq. for y_i (Sec 3).
Quote:       "We apply our method to seven Atari 2600 games... it outperforms all
             previous approaches on six of the games and surpasses a human expert on
             three of them."
             "The raw frames are preprocessed by first converting their RGB
             representation to gray-scale and down-sampling it to a 110x84 image. The
             final input representation is obtained by cropping an 84 x 84 region...
             [phi] applies this preprocessing to the last 4 frames of a history and
             stacks them."
             "randomizing the samples breaks these correlations and therefore reduces
             the variance of the updates."
```

```text
URL:         https://arxiv.org/abs/1709.06560
Kind:        primary (for its own reproducibility findings). Henderson, Islam,
             Bachman, Pineau, Precup, Meger, "Deep Reinforcement Learning that
             Matters" (AAAI 2018). Independent of DeepMind; owns the experiments it
             reports.
Establishes: That deep-RL results are highly sensitive to random seeds and
             hyperparameters. SCOPE: policy-gradient algorithms (TRPO, DDPG, PPO,
             ACKTR) on MuJoCo continuous control (HalfCheetah-v1, Hopper-v1). NOT
             DQN and NOT Atari.
Paraphrase:  Running the same algorithm with the same hyperparameters and only
             different random seeds can produce statistically different performance
             distributions. Ten TRPO runs on HalfCheetah split into two groups of
             five yield two averages that differ significantly. Network architecture,
             activation function, and reward scaling also move results substantially.
Locators:    Abstract; Sec "Random Seeds and Trials"; Fig.5; Sec "Hyperparameters"/
             Figs 2-3.
Quote:       "We then split the trials into two sets of 5 and average these two
             groupings together... we find that the performance of algorithms can be
             drastically different. We demonstrate that the variance between runs is
             enough to create statistically different distributions just from varying
             random seeds."
             "The average 2-sample t-test across entire training distribution
             resulted in t = -9.0916, p = 0.0016."
```

```text
URL:         http://incompleteideas.net/book/the-book-2nd.html
Kind:        primary (for the definition of Q-learning). Sutton & Barto,
             "Reinforcement Learning: An Introduction," 2nd ed. (MIT Press, 2018).
             The canonical reference that owns the textbook definition. (Read from
             the authors' freely posted RLbook2020.pdf linked on that page.)
Establishes: The definition of Q-learning as an off-policy temporal-difference
             control method that learns the action-value function Q(s,a) and
             converges to the optimal q*, acting greedily (e.g. epsilon-greedy) on it.
Paraphrase:  Q(s,a) is the expected return of taking action a in state s and then
             acting optimally. Q-learning updates Q toward the reward plus the
             discounted best next-state value (a bootstrapped target), independent of
             the behavior policy. This is the value-based method DQN scales with a
             neural network.
Locators:    Sec 6.5 "Q-learning: Off-policy TD Control," Eq. 6.8, p.131.
Quote:       "One of the early breakthroughs in reinforcement learning was the
             development of an off-policy TD control algorithm known as Q-learning
             (Watkins, 1989)... the learned action-value function, Q, directly
             approximates q*, the optimal action-value function, independent of the
             policy being followed."
```

```text
URL:         https://www.nbcnews.com/tech/innovation/ai-learned-atari-games-humans-do-now-it-beats-them-n312206
Kind:        secondary. NBC News, 25 Feb 2015. Reports on the paper from outside the
             authoring party; useful as a record of how the result was received and
             re-stated in the press.
Establishes: The contemporaneous "how it is cited" framing, AND a reported count
             that differs from the paper's headline number: NBC says DQN "outscored
             humans on 23 out of 49 games." This is the >=100%-of-human reading, not
             the paper's >=75% (29-game) reading. It also reports the long-horizon
             failure mode in plain terms.
Paraphrase:  A mainstream outlet framed the paper as a machine that learns Atari "the
             way a person might" and beats humans, while noting it does poorly on
             games needing long-term planning and pathfinding.
Locators:    Body paragraphs; quotes attributed to Hassabis and Mnih.
Quote:       "The AI outscored humans on 23 out of 49 games, such as Road Runner,
             Space Invaders and Breakout."
             "Games where the system doesn't do well are ones that require long-term
             planning."
```

```text
URL:         https://www.technologyreview.com/2020/04/01/974997/deepminds-ai-57-atari-games-but-its-still-not-versatile-enough/
Kind:        secondary. MIT Technology Review, Will Douglas Heaven, 1 Apr 2020.
             Independent retrospective written for the "bring it to the present"
             section.
Establishes: That five years on, the DQN lineage was still narrow: agents failed for
             years on hard-exploration games (Montezuma's Revenge, Pitfall) and on
             long-delayed-reward games (Solaris, Skiing), and even the 2020 agent that
             finally beat all 57 games cannot generalize across games.
Paraphrase:  The template held and improved, but the resulting agents remain one-game
             specialists. Montezuma's Revenge and Pitfall demanded extensive
             exploration the value-learning approach could not supply.
Locators:    Body.
Quote:       "In Montezuma's Revenge and Pitfall, an AI must try a lot of different
             strategies before hitting on a winning one."
             "Agent57 can learn to play 57 games, but it cannot learn to play 57
             games at once. It needs to retrain for each new game."
```

```text
URL:         https://deepmind.google/blog/agent57-outperforming-the-human-atari-benchmark/
Kind:        first-party retrospective (treat as corroboration, not an independent
             secondary; authored by DeepMind, the same lab as the paper). Puigdomenech
             et al., 31 Mar 2020.
Establishes: Independent-of-time confirmation that DQN-lineage agents scored nothing
             on Montezuma's Revenge (and Pitfall, Solaris, Skiing) for years, and that
             beating the human baseline on all 57 Atari games was only reached in 2020.
Paraphrase:  DeepMind's own account: for years every deep-RL agent "consistently
             failed to score" on four games including Montezuma's Revenge; Agent57
             (2020) was the first to clear the human baseline on all 57.
Locators:    Blog body.
Quote:       "all deep reinforcement learning agents have consistently failed to score
             in four games: Montezuma's Revenge, Pitfall, Solaris and Skiing."
```

## Contradictions

- **"29 of 49" (paper) vs "23 of 49" (NBC News).** Both are correct under different
  thresholds, and both are verifiable from Extended Data Table 2. The paper's headline
  29 is the count of games where DQN reached **at least 75%** of the professional
  tester's score. NBC's 23 is the count where DQN **matched or beat** the tester's
  actual score (normalized DQN >= 100%). I reproduced both counts by hand from the
  table's "Normalized DQN (% Human)" column (see Numbers). The six games that fall in
  the 75-100% band are H.E.R.O. (76.5%), Q*Bert (78.5%), Ice Hockey (79.3%), Up and
  Down (92.7%), Fishing Derby (93.5%), Enduro (97.5%). This is the sharpest support for
  the commission's angle: "human-level" is doing work at 75%, and the stricter "beat
  the human" bar is met on fewer than half the games (23 of 49).

- **Which tricks the paper introduced.** The commission (idea #2) frames experience
  replay AND the target network as the paper's tricks. The 2013 precursor
  (arXiv:1312.5602) already uses experience replay; the periodically cloned/frozen
  **target network is new in the 2015 Nature paper**. Attribute experience replay to
  the lineage and the target network to the Nature version.

- **The human baseline is one person, briefly.** "100% = human-level" is the score of a
  single professional games tester over ~20 episodes of up to 5 minutes each, no
  pausing/saving/reloading. Not a population, not a champion. The Nature text calls this
  "a professional human games tester," and the writer should use exactly that label,
  not "human experts" or "humans" generally. The word "human-level" rests on this thin
  baseline.

- **Henderson's scope does not include DQN.** No contradiction of the commission's
  broad point (deep RL is fragile), but a boundary: Henderson et al. test TRPO/DDPG/
  PPO/ACKTR on MuJoCo, not DQN on Atari. Their seed result (t=-9.09, p=0.0016) is a
  HalfCheetah/TRPO finding. Present it as evidence about the field DQN founded, not
  about DQN's own Atari runs.

## Numbers

```text
Figure: 49 (games learned by one network/hyperparameter set)
Owner:  Mnih et al. 2015, Nature (abstract; Extended Data Table 2 lists all 49)
Scope:  Atari 2600 via the Arcade Learning Environment; 2015 paper. (The 2013
        precursor used 7 games.)
```

```text
Figure: 75% (of the professional human games tester's score = the "human-level" bar)
Owner:  Mnih et al. 2015, Nature (Fig.3 caption; main text p.531)
Scope:  Normalized score = 100 x (DQN - random)/(human - random); "human-level" is
        operationalized as >= 75% on this scale.
```

```text
Figure: 29 of 49 (games at >= 75% of human)
Owner:  Mnih et al. 2015, Nature (main text p.531: "29 games")
Scope:  Count over the 49 games; independently reproduced from Extended Data Table 2.
```

```text
Figure: 23 of 49 (games at >= 100% of human, i.e. DQN matched or beat the tester)
Owner:  Extended Data Table 2 (my count of the Normalized DQN column); reported
        independently by NBC News (25 Feb 2015).
Scope:  Count over the 49 games. Games >= 100%: Assault, Atlantis, Beam Rider,
        Boxing, Breakout, Crazy Climber, Demon Attack, Freeway, Gopher, James Bond,
        Kangaroo, Krull, Kung-Fu Master, Name This Game, Pong, Road Runner, Robotank,
        Space Invaders, Star Gunner, Tennis, Time Pilot, Tutankham, Video Pinball.
```

```text
Figure: 0 (±0) raw DQN score on Montezuma's Revenge; 0.0% of human
Owner:  Mnih et al. 2015, Nature, Extended Data Table 2 (Montezuma's Revenge row)
Scope:  DQN mean over 30 evaluation episodes. Random play = 0; human tester = 4367;
        DQN = 0. It is the single lowest-normalized game in Figure 3 (bottom of the
        chart, "Below human-level").
```

```text
Figure: 84 x 84 x 4 (network input: 4 stacked grayscale frames at 84x84)
Owner:  Mnih et al. 2015, Nature (main text p.530; Methods "Preprocessing")
Scope:  The Y/luminance channel of each frame, rescaled to 84x84; the 4 most recent
        frames stacked. (2013 version: RGB->grayscale, downsample to 110x84, crop to
        84x84, stack last 4.)
```

```text
Figure: 50 million training frames ~= 38 days of game experience; 1M-frame replay memory
Owner:  Mnih et al. 2015, Nature (Methods "Training details")
Scope:  Per game, for the main results. Supports the "tens of millions of frames,
        weeks of play" sample-cost point. (Ablation table used a shorter 10M-frame
        run.)
```

```text
Figure: Replay/target-network ablation on Breakout: 316.8 (both on) -> 240.7 (replay,
        no target Q) -> 10.2 (no replay, target Q) -> 3.2 (neither)
Owner:  Mnih et al. 2015, Nature, Extended Data Table 3
Scope:  10M-frame runs, best avg episode score, standard hyperparameters, 3 learning
        rates. Removing replay collapses Breakout ~30x (316.8 -> 10.2); removing both
        drops it ~100x (to 3.2). Companion collapses: Seaquest 2894.4 -> 275.8;
        Enduro 1006.3 -> 29.1; River Raid 7446.6 -> 1453.0; Space Invaders 1088.9
        -> 302.0. This is the quantitative case that the two tricks are the
        contribution.
```

```text
Figure: TRPO on HalfCheetah-v1, 10 identical runs split into two groups of 5:
        two-sample t = -9.0916, p = 0.0016
Owner:  Henderson et al. 2018 (Fig.5)
Scope:  Same algorithm, same hyperparameters, seeds only differ. Evidence of deep-RL
        seed fragility as a field property. NOT DQN, NOT Atari.
```

```text
Figure: 7 games (2013 precursor); beat prior methods on 6, beat a human expert on 3
Owner:  Mnih et al. 2013, arXiv:1312.5602 (abstract)
Scope:  Beam Rider, Breakout, Enduro, Pong, Q*bert, Seaquest, Space Invaders.
```

## Source assets

```text
Asset: Extended Data Table 2, Mnih et al. 2015 (per-game scores: Random / Best Linear
       Learner / Contingency (SARSA) / Human / DQN±std / Normalized DQN % Human).
Shows: The entire variance story in one place: DQN from 0.0% (Montezuma's Revenge) to
       2539.4% (Video Pinball) of human, and exactly where the 75% and 100% lines
       fall. The single strongest asset for the "median claim, enormous variance"
       thesis.
Crop:  Must retain the Game, Human, DQN, and Normalized-DQN columns and at least the
       extremes (Montezuma's Revenge at 0.0% and a top game). A crop may omit the
       Best Linear Learner and Contingency columns without losing the argument. Do not
       drop the Montezuma's Revenge row.
```

```text
Asset: Figure 3, Mnih et al. 2015 (horizontal bar chart, DQN normalized performance
       per game, with a "human-level" line and games sorted best-to-worst).
Shows: At a glance which games sit above/below human-level; Montezuma's Revenge sits
       alone at the bottom under "Below human-level," the long right tail shows the
       few games where DQN is many multiples of human.
Crop:  Keep the human-level (100%) reference line and both ends of the sort (top games
       and the Montezuma's Revenge bottom). A crop that hides the reference line
       destroys the point.
```

```text
Asset: Extended Data Table 3, Mnih et al. 2015 (replay x target-Q ablation, 5 games).
Shows: The two tricks are load-bearing: Breakout falls from 316.8 to 3.2 with both
       disabled; every one of the five games collapses.
Crop:  Retain all four condition columns and at least the Breakout and Seaquest rows.
```

```text
Asset: Figure 1, Mnih et al. 2013 / schematic in 2015 (the CNN reading 84x84x4 frames).
Shows: The concrete input the network sees (4 stacked frames), useful for teaching
       idea #1 (the Breakout paddle decision from raw pixels).
Crop:  None prescribed; the pixel-stack-to-Q-values path is the informative part.
```

Sutton & Barto and Henderson: None found (text/equation sources; the Henderson Fig.5
seed plot is decorative for this lesson and better told as the t/p numbers).

## Discarded

```text
URL: https://pubmed.ncbi.nlm.nih.gov/25719670/ - PubMed index entry only; no full
     text of the numbers. The Nature article page is the primary of record.
URL: https://github.com/kuz/DeepMind-Atari-Deep-Q-Learner - a third-party
     reimplementation of the DQN code; not authoritative for any published figure.
URL: https://www.researchgate.net/figure/... (ATARI DQN architecture diagram) -
     secondary redraw of the architecture; the paper's own Fig.1 is the primary.
URL: https://lifeboat.com/blog/2019/05/dqn-... - low-authority blog repost; adds
     nothing the primary or the two chosen secondaries do not.
URL: https://syncedreview.com/2018/11/27/uber-ai-beats-montezumas-revenge-video-game/
     and OpenAI RND / Go-Explore coverage - real follow-on exploration work, but out
     of scope for this lesson (commission caps the teaching at 3 ideas and warns
     against importing later-method machinery). Held in reserve only to support the
     one-line "later exploration methods eventually scored on Montezuma" note.
```
