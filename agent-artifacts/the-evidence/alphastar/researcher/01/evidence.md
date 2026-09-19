# evidence: the-evidence/alphastar (01)

The evidence supports the commissioned angle firsthand and cleanly. The Nature
paper and DeepMind's own posts pin every fact the lesson needs: the training
pipeline (supervised imitation from 971,000 human replays, then league play with
main agents, main exploiters, and league exploiters), the interface (a camera-like
view plus a 22-action-per-5-seconds cap and reaction delays), all three races, and
exactly what "Grandmaster" meant (blind, anonymous play on Battle.net's European
ladder, above 99.8% of ranked players). The paper itself distinguishes the January
2019 showcase from the Nature version, and one of its own authors, the professional
player TLO, states on the record that the Nature version "doesn't feel superhuman."
The evidence confirms the commissioned angle; DeepMind's own posts and author
statement supply much of the correction the lesson wants to make.

Two things the record is careful about. First, the "it only won by clicking fast"
critique is strongest against the **January** version (no camera, looser action
limits) and weakest against the **Nature** version (camera, 22/5s cap), and the two
are routinely conflated in popular memory; the writer must keep them separate.
Second, ladder Grandmaster is not the same claim as beating the world's best in a
controlled series, and the paper says so explicitly. The one real limitation: I read
the paper's full text and Methods through a faithful PDF copy, but did not separately
open the downloadable Supplementary Data files (pseudocode, detailed-architecture.txt,
replays.zip, bnet.json), because those are code and raw data rather than prose
claims, and every methodological number the lesson rests on lives in the Methods,
which I read in full.

## Sources

```text
URL:         https://www.nature.com/articles/s41586-019-1724-z
Kind:        primary — the paper itself, authored by the team that built AlphaStar
             (Vinyals, Babuschkin, Czarnecki et al., DeepMind). It owns every claim
             about AlphaStar's method and results. (Read firsthand via a faithful
             full-text PDF; the nature.com page shows the abstract and gates the
             rest. The recorded URL is the paper's own page.)
Establishes: The full training pipeline, interface, APM/camera constraints, races,
             the Grandmaster result and its exact conditions, and the paper's own
             framing of the January demo and of "superhuman."
Paraphrase:  AlphaStar is a multi-agent reinforcement-learning agent that combines
             supervised imitation of human replays with a "league" of agents that
             play each other. Evaluated in the full game of StarCraft II against
             human players on Battle.net, it was rated Grandmaster for all three
             races and above 99.8% of officially ranked human players. Training:
             agents are first trained by supervised learning on a public dataset of
             971,000 anonymized human replays (versions 4.8.2–4.8.6) from players
             with MMR above 3,500 (the top 22%), one policy per race, then
             fine-tuned on 16,000 winning replays from players above 6,200 MMR
             (which raised the win rate against the built-in elite bot from 87% to
             96% in Protoss-vs-Protoss). Reinforcement learning then improves the
             agents against each other, with human data kept in the loop two ways:
             each agent is initialized to the supervised policy and penalized for
             drifting from it (a KL-divergence penalty), and agents are rewarded for
             following build-order "statistics" (z) sampled from human games. The
             league has three agent types: main agents (one per race) that never
             reset and are the agents actually deployed; main exploiters (one per
             race) that play only the current main agents to find their weaknesses;
             and league exploiters (two per race) that hunt weaknesses across the
             whole league. Interface: AlphaStar sees the game through a camera-like
             view it must move, has imperfect information (fog of war), is capped at
             22 non-duplicate actions per 5-second window, and has real-time delays.
             The December 2018 demo used a "different, preliminary version" without
             the limited camera and with looser action limits, on a single race and
             map. Grandmaster was measured under blind, anonymous ladder play, which
             the paper says does not directly measure susceptibility to repeated
             exploitation.
Locators:    Abstract (p.350); "Humans play StarCraft under physical constraints…"
             (p.350); "In StarCraft, each player chooses one of three races… three
             main agents… three main exploiter agents… six league exploiter agents…
             32 third-generation tensor processing units… over 44 days… almost 900
             distinct players" (p.352); "AlphaStar Final achieved ratings of 6,275…
             6,048… 5,835 MMR… above 99.8%… Grandmaster level for all three races"
             and "AlphaStar Supervised reached an average rating of 3,699… above 84%"
             (p.353); Methods — "Game and interface," "Camera view," "APM limits,"
             "Delays" (Methods pp.1–2); Methods — "Supervised learning" (971,000
             replays; MMR>3,500; fine-tune 16,000 replays MMR>6,200; 87%→96%; per-
             race supervised MMRs); Methods — "Multi-agent learning / Populating the
             league" (35% SP, 50% PFSP, 15% PFSP; reset rules; 2×10^9 and 4×10^9 step
             snapshots); Methods — "Evaluation / AlphaStar Battle.net evaluation"
             (~90,000 active European-server players; blind/anonymous; 30/60/+30
             games; midpoint halted after 50 games when anonymity was compromised);
             Methods — "StarCraft demonstration evaluation" (December 2018);
             "Professional player statement" (TLO).
Quote:       "Agents are limited to executing at most 22 non-duplicate actions per
             5-s window." (Methods, APM limits)
             "In particular, the agent did not have a limited camera, was less
             restricted in how often it could act, and played for and against a
             single StarCraft II race on a single map. AlphaStar won all ten games
             in both five-game series, although an early camera prototype lost a
             follow-up game against MaNa." (Methods, StarCraft demonstration
             evaluation)
             "The limitations that have been put in place for AlphaStar now mean
             that it feels very different from the initial show match in January.
             While AlphaStar has excellent and precise control it doesn't feel
             superhuman—certainly not on a level that a human couldn't theoretically
             achieve." (Professional player statement, Dario 'TLO' Wünsch)
             "These conditions were selected to estimate AlphaStar's strength under
             approximately stationary conditions, but do not directly measure its
             susceptibility to exploitation under repeated play." (Empirical
             evaluation, p.352)
```

```text
URL:         https://deepmind.google/blog/alphastar-mastering-the-real-time-strategy-game-starcraft-ii/
Kind:        primary — DeepMind's own January 2019 announcement of the demo, written
             by the team. It owns the account of the December games and the
             January-version numbers.
Establishes: The January 2019 showcase: the 5-0 results, the raw (no-camera)
             interface used in December, the live game MaNa won against a camera-
             restricted prototype, and the January-version APM/delay figures.
Paraphrase:  AlphaStar beat TLO 5-0 and MaNa 5-0 in test matches (the MaNa series on
             19 December 2018). In those December games AlphaStar used a raw
             interface: it read its own and its opponent's visible units directly
             without moving a camera, "effectively playing with a zoomed out view of
             the game." A later, camera-restricted prototype trained for only 7 days
             lost a live exhibition game to MaNa. AlphaStar's average APM across the
             games was around 280 with a 350 ms observation-to-action delay,
             "significantly lower" than the pros (MaNa ~390, TLO ~678 by DeepMind's
             chart) "although its actions may be more precise." The league ran 14
             days, 16 TPUs per agent, each agent experiencing up to 200 years of
             real-time play. The network was first trained by supervised learning
             from anonymized human games released by Blizzard.
Locators:    Sections "Results," "How AlphaStar is trained," and "How AlphaStar
             plays the game" / interface-and-APM discussion of the post.
Quote:       "During the matches against TLO and MaNa, AlphaStar interacted with the
             StarCraft game engine directly via its raw interface, meaning that it
             could observe the attributes of its own and its opponent's visible units
             on the map directly, without having to move the camera - effectively
             playing with a zoomed out view of the game."
             "In its games against TLO and MaNa, AlphaStar had an average APM of
             around 280… significantly lower than the professional players, although
             its actions may be more precise."
             "In an exhibition match, MaNa defeated a prototype version of AlphaStar
             using the camera interface, that was trained for just 7 days."
```

```text
URL:         https://deepmind.google/blog/alphastar-grandmaster-level-in-starcraft-ii-using-multi-agent-reinforcement-learning/
Kind:        primary — DeepMind's October 2019 post accompanying the Nature paper.
Establishes: The Nature-version framing in DeepMind's own plain words: Grandmaster
             for all three races, above 99.8%, on the official server, anonymous,
             with a camera and tighter action limits set with a pro's help.
Paraphrase:  AlphaStar was ranked above 99.8% of active players on Battle.net and
             reached Grandmaster for all three races (Protoss, Terran, Zerg). It
             played on the official server, anonymously, under the same maps and
             conditions as humans, viewing the world through a camera, with stronger
             limits on how often it could act (capped at 22 agent actions per 5
             seconds), developed in collaboration with the professional player TLO.
             All game replays were released.
Locators:    Post body and the interface/limits footnote.
Quote:       "AlphaStar was ranked above 99.8% of active players on Battle.net, and
             achieved a Grandmaster level for all three StarCraft II races: Protoss,
             Terran, and Zerg."
```

```text
URL:         https://aiimpacts.org/the-unexpected-difficulty-of-comparing-alphastar-to-humans/
Kind:        secondary — an independent analysis by Rick Korzekwa (AI Impacts,
             17 September 2019) of the January demo. It reports on and re-measures
             DeepMind's result from outside the team; it does not own the result.
Establishes: The core of the APM/camera fairness debate, with its own measurements:
             that AlphaStar's average action rate was human-plausible but its combat
             bursts and its lack of wasted actions were not.
Paraphrase:  Korzekwa's own analysis of a game found AlphaStar's average APM lower
             than MaNa's (he measures roughly 180 vs 270 in that game), but that
             AlphaStar banked its capped action budget and spent it in bursts:
             14 windows over 400 APM and 6 windows over 500 APM sustained for 5
             seconds in combat, executed with perfect accuracy and no spam-clicking,
             which a human's raw APM count inflates. In the December games AlphaStar
             also saw the whole map without needing to move a camera or select units
             to inspect them. His assessment is that AlphaStar had a large enough
             speed advantage over MaNa to have substantially influenced the result.
Locators:    Body of the post; the APM-burst count and the map-vision point.
Quote:       "I found 14 cases in which the agent was able to average over 400 APM
             for 5 seconds in combat, and six times when the agent averaged over 500
             APM for more than 5 seconds."
```

```text
URL:         https://www.engadget.com/2019-01-24-deepmind-ai-starcraft-ii-demonstration-tlo-mana.html
Kind:        secondary — contemporaneous reporting (AJ Dellinger, Engadget, 24
             January 2019) on the demonstration broadcast. Reports the event from
             outside DeepMind.
Establishes: How the January result was reported to the public: the 10-1 headline,
             the Protoss-vs-Protoss matchup on Catalyst, the whole-map-vs-camera
             difference, and that AlphaStar acted fewer times per minute than its
             human opponent.
Paraphrase:  AlphaStar went 10-0 in the pre-recorded December games (5-0 vs TLO, 5-0
             vs MaNa) in Protoss-vs-Protoss on the Catalyst map, then lost a live
             game to MaNa after DeepMind switched to a camera-limited version,
             making the record 10-1. In the pre-recorded games AlphaStar "essentially
             sees the map entirely zoomed out"; the live version had to focus a
             camera "in the same way a human would." AlphaStar performed fewer
             actions per minute than MaNa and had about a 350 ms reaction time,
             slower than most pros.
Locators:    Article body.
Quote:       "AlphaStar actually performed fewer actions per minute than his human
             opponent" and had "a reaction time of about 350 milliseconds, which is
             slower than most pros."
```

```text
URL:         https://www.nature.com/articles/d41586-019-03298-6
Kind:        secondary — Nature news report (Dan Garisto, 30 October 2019) on the
             paper. Journalism about the result, not the result. (The lede is public;
             the body is gated. The recorded URL is the article's own page.)
Establishes: How a science-news outlet framed the Grandmaster result on publication,
             confirming the percentile and the population it was measured against.
Paraphrase:  AlphaStar achieved a Grandmaster rating on the European servers,
             placing within the top 0.15% of the region's roughly 90,000 players; the
             dek says it "beat all but the very best humans."
Locators:    Headline, dek, and opening paragraph.
Quote:       "achieved a grandmaster rating after it was unleashed on the game's
             European servers, placing within the top 0.15% of the region's 90,000
             players."
```

## Contradictions

**The APM/camera fairness debate (the core contested question).** After the January
2019 showcase, independent analysts argued that AlphaStar's win owed more to
mechanical speed than to superior strategy, so the "superhuman" framing was
premature. Korzekwa (AI Impacts, secondary) measured AlphaStar sustaining over 400
APM for 5-second windows 14 times and over 500 APM 6 times in combat, executed with
no wasted clicks, while its average rate stayed human-plausible; combined with the
whole-map vision in the December games, he judged the speed advantage large enough
to have substantially influenced the result. This directly steelmans the case
against a naive "AI out-strategized the pros" reading.

The primary sources partly concede and partly rebut this, and the distinction turns
entirely on **which version** is in question:

- DeepMind's own January post (primary) reports AlphaStar's average APM (~280) as
  *lower* than the pros', and reporting (Engadget, secondary) repeated that framing.
  So the dispute was never about the average; it was about bursts, precision, and
  the no-camera vision, none of which the average APM captures.
- The paper (primary) states that the December version "did not have a limited
  camera, was less restricted in how often it could act." The speed/vision critique
  therefore lands hardest on the January version. The Nature-version agent played
  with the camera and the 22-actions-per-5-seconds cap, and still reached
  Grandmaster. A writer who cites the January APM-burst critique against the Nature
  ladder result would be conflating two different agents.
- The paper's own author, the professional player TLO, states the Nature version
  "doesn't feel superhuman—certainly not on a level that a human couldn't
  theoretically achieve," and that with a limited camera "when I multi-task it
  doesn't always catch everything at the same time." This is DeepMind conceding, on
  the record, that the January version's fairness was open to question and that the
  constraints were added in response.

**Grandmaster ladder rating versus beating the world's best.** Popular memory ("AI
crushed the pros") merges two different claims. The controlled series were the
December 2018 demo against TLO and MaNa (a preliminary, less-constrained agent). The
Nature "Grandmaster" result was blind, anonymous ladder play against whichever
opted-in humans matchmaking supplied, and the paper explicitly says these conditions
"do not directly measure its susceptibility to exploitation under repeated play."
The paper does not claim AlphaStar beat the world's top players in a controlled
series under the Nature constraints.

**A caveat inside the "beat the pros" story.** TLO, described in the January post as
a "top professional Zerg player," played Protoss in the December series, not his
professional race (the paper: "TLO did not play the same StarCraft II race that he
plays professionally"). MaNa is a Protoss main. This weakens the demo as evidence
against the very best, independent of the interface debate.

**A minor numeric discrepancy, not a conflict.** DeepMind's January post gives
AlphaStar's average APM as ~280 (MaNa ~390); Korzekwa's independent analysis of a
single game reports lower figures (~180 vs ~270). These differ because they measure
different games and different action definitions (raw versus effective actions), not
because either is wrong. Attribute the ~280 figure to DeepMind and the burst
measurements to Korzekwa; do not blend them.

## Numbers

```text
Figure: 971,000 human replays used for supervised imitation
Owner:  Nature paper (Methods, Supervised learning)
Scope:  StarCraft II versions 4.8.2–4.8.6; players with MMR > 3,500 (the top 22%);
        one policy trained per race
```

```text
Figure: 16,000 winning replays (from players with MMR > 6,200) used for fine-tuning
Owner:  Nature paper (Methods, Supervised learning)
Scope:  Fine-tuning raised win rate vs the built-in elite bot from 87% to 96% in
        Protoss-vs-Protoss
```

```text
Figure: supervised-only agent MMR — Terran 3,947, Protoss 3,607, Zerg 3,544
        (average 3,699, above 84% of human players)
Owner:  Nature paper (Methods, Supervised learning; and p.353)
Scope:  After supervised training plus fine-tuning, before league RL
```

```text
Figure: 22 non-duplicate actions per 5-second window (the APM cap, Nature version)
Owner:  Nature paper (Methods, APM limits; also stated in DeepMind Oct 2019 post)
Scope:  Enforced by a "monitoring layer"; Fig. 1a labels it "Actions limit ~22 per 5 s"
```

```text
Figure: delays (Nature version) — ~110 ms observation-to-action; observe-next chosen
        on average 370 ms ahead
Owner:  Nature paper (Methods, Delays)
Scope:  Real-time evaluation only, not training. NB: the January version was reported
        at ~350 ms observation-to-action delay (DeepMind Jan 2019 post) — a different
        figure for a different version.
```

```text
Figure: league scale — 3 main agents (one per race), 3 main exploiters (one per
        race), 6 league exploiters (two per race); ~900 distinct players created
Owner:  Nature paper (p.352 and Methods, Infrastructure)
Scope:  Full league training
```

```text
Figure: compute — 32 third-generation (v3) TPUs per agent, over 44 days
Owner:  Nature paper (p.352)
Scope:  Nature version. NB: DeepMind's Jan 2019 post gave the January league as 14
        days, 16 TPUs per agent — a different, earlier run.
```

```text
Figure: AlphaStar Final ladder ratings — 6,275 MMR Protoss, 6,048 MMR Terran,
        5,835 MMR Zerg; above 99.8% of ranked players; Grandmaster for all three races
Owner:  Nature paper (p.353); percentile echoed by DeepMind Oct 2019 post and Nature
        news (top 0.15% for the final average)
Scope:  Blind, anonymous play on Battle.net's European server, against ~90,000 active
        (league-placed) players. Fig. 2a: supervised top ~16%, midpoint top ~0.5%,
        final on average top ~0.15%.
```

```text
Figure: demonstration record — 10-0 in the December 2018 series (5-0 vs TLO, 5-0 vs
        MaNa), then a live game lost to MaNa, for 10-1 overall
Owner:  Nature paper (Methods, demonstration evaluation) and DeepMind Jan 2019 post;
        the "10-1" framing from contemporaneous reporting (Engadget)
Scope:  Protoss-vs-Protoss on a single map (Catalyst); a preliminary, less-constrained
        agent; the live loss was to a 7-day camera-restricted prototype
```

```text
Figure: network size — 139 million weights total, 55 million used at inference
Owner:  Nature paper (Methods, Architecture)
Scope:  Per-agent policy network
```

```text
Figure: MMR-validation check — AlphaStar's MMR method gave TLO 6,334 vs Battle.net's
        reported 6,336
Owner:  Nature paper (Methods, Evaluation)
Scope:  Validation of the rating computation on TLO's 200 most recent matches
```

## Source assets

```text
Asset: Figure 2a — the Battle.net ranking chart (Nature paper, p.351). Plots the
       three AlphaStar snapshots (Supervised, Mid, Final) against the seven ladder
       leagues Bronze→Grandmaster and the percentile axis.
Shows: How far the agent climbed at each training stage, and exactly where
       Grandmaster sits on the human distribution (the top sliver above ~99.7%).
Crop:  Must retain the percentile axis and the Grandmaster band label; a crop that
       drops the axis loses the whole point (how thin the top tier is).
```

```text
Asset: Figure 2c — effective-actions-per-minute (EPM) distributions for AlphaStar
       Final (blue) versus human players (red), per race, with dashed mean lines
       (Nature paper, p.351).
Shows: That AlphaStar's typical effective action rate sits within the human
       distribution rather than above it — the paper's visual answer to "it just
       clicked faster." (It does not show the combat bursts the debate turns on.)
Crop:  Keep both distributions and the dashed means together; showing only
       AlphaStar's curve would mislead.
```

```text
Asset: Figure 3g and 3h — ablations for APM limits and for the camera interface
       (Nature paper, p.352), shown as Elo bars.
Shows: 3h: the camera interface *reduces* AlphaStar's performance versus a non-camera
       interface (the constraint cost it strength). 3g: cutting APM below the used
       limit hurts, and, unexpectedly, raising APM also hurts. Direct evidence that
       the Nature agent was handicapped by, not helped by, its interface limits.
Crop:  Retain the baseline/limit labels; the comparison is meaningless without them.
```

```text
Asset: Figure 1a — the interface-and-monitoring-layer diagram (Nature paper, p.350).
       Shows the camera view, the "Actions limit ~22 per 5 s" monitoring layer, and
       the requested-delay path.
Shows: In one picture, the three constraints the lesson explains: camera vision,
       action cap, and reaction delay.
Crop:  Keep the monitoring-layer callout and the camera-vision panel; these are the
       teachable parts.
```

```text
Asset: Figure 1c — the league-composition/training diagram (Nature paper, p.350),
       showing main agents, league exploiters, and main exploiters over time with
       reinitialization arrows.
Shows: How the three agent types relate — who trains against whom, and which ones
       reset to the supervised agent. This carries "league play" better than prose.
Crop:  Retain all three agent rows and the "Reinitialization" legend.
```

## Discarded

```text
URL: https://raw.githubusercontent.com/utilForever/rl-paper-study/main/2nd/200914%20-%20Grandmaster%20Level%20in%20StarCraft%20II%20using%20Multi-agent%20Reinforcement%20Learning,%20O.%20Vinyals%20et%20al,%202019.pdf
     — a third-party Korean study-notes slide deck, not the paper. Its figures happen
     to match the paper, but it is a secondary summary and cannot be cited for the
     paper's numbers. Used only to locate the real full text, then verified every
     figure against the paper itself.
```

```text
URL: https://en.wikipedia.org/wiki/AlphaStar_(software)
     — tertiary encyclopedia summary. Useful for orientation only; every claim it
     carries is available in the primaries above, which own them.
```

```text
URL: https://arxiv.org/abs/1902.01724
     — "AlphaStar: an evolutionary computation perspective." A commentary/analysis
     paper, not the primary result and not needed for this lesson's claims.
```
