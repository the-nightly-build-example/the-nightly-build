# Evidence: the-evidence/alphazero (01)

The primary record strongly supports the generality claim and gives exact,
checkable numbers for training and for the chess match, and it supports the
commissioned angle with one correction the writer must not miss. There are two
DeepMind documents, and they describe two different chess matches. The December
2017 arXiv preprint reports a 100-game match at one minute per move, Stockfish 8
on 64 threads with a 1 GB hash and no opening book, AlphaZero on 4 TPUs: the
setup that drew the famous "unfair conditions" criticism. The December 2018
Science paper, the document of record, reports a *different* match: 1000 games at
3 hours per game plus a 15-second increment, Stockfish on 44 CPU cores (its TCEC
configuration), and it adds separate matches against the January 2018 Stockfish
development version and against a Stockfish given a strong opening book, all won
by AlphaZero. So the harshest conditions people cite belong to the preprint, and
a lesson that pins them on "the paper" while teaching the Science paper as the
document of record would be wrong. The angle still holds, because even the
Science match leaves two conditions unnormalized (TPU-vs-CPU hardware, and
Stockfish 8 as the primary opponent), it was DeepMind's own internal match rather
than an independent tournament, and neither paper reports giving Stockfish
endgame tablebases. The independent vindication came later and from outside
DeepMind: Leela Chess Zero, an open-source implementation of the method, beat
Stockfish in the TCEC Season 15 superfinal in 2019 under standard tournament
conditions. The record is thin on one point the brief asked for: neither paper
states in its main text whether Stockfish was given endgame tablebases, so that
condition is inferred, not quoted. The full tables S8-S9 that hold the match
conditions were not read (supplementary PDF not opened); the main-text and figure
figures below are all confirmed against the papers themselves.

## Sources

```text
URL:         https://arxiv.org/abs/1712.01815
Kind:        primary. The December 2017 preprint by the DeepMind authors; it owns
             the first-published AlphaZero claims and the first match description.
Establishes: The method (self-play RL from the rules alone, one network, MCTS, no
             human data, no opening book, no handcrafted evaluation), the training
             compute, and the original 100-game chess match and its conditions.
Paraphrase:  AlphaZero uses a single deep network (p,v)=f(s) and a general-purpose
             MCTS in place of a handcrafted evaluation and alpha-beta search;
             parameters are trained from randomly initialised weights by self-play,
             with a single network updated continually (no best-player gating as in
             AlphaGo Zero). Trained 700,000 steps (mini-batches of 4,096) using
             5,000 first-generation TPUs to generate self-play games and 64
             second-generation TPUs to train. It applied the same algorithm,
             architecture and hyper-parameters to chess, shogi and Go, training a
             separate instance per game. In chess it "outperformed Stockfish after
             just 4 hours (300k steps)". The evaluation match was 100 games at one
             minute per move; AlphaZero and AlphaGo Zero each used a single machine
             with 4 TPUs; "Stockfish and Elmo played at their strongest skill level
             using 64 threads and a hash size of 1GB." Methods: "we used Stockfish
             version 8 (official Linux release)". No opening book or tablebase is
             reported as given to either side; AlphaZero used none. The Domain
             Knowledge list states the only knowledge used is the rules (for MCTS
             simulation, input/output encoding, exploration-noise scaling, and a
             max-length draw rule).
Locators:    Abstract and pp. 2-5 (method, training paragraph, Table 1); Methods,
             "Evaluation" and Table S3 (Stockfish 8, 64 threads/1GB, training
             times/games); Table 1 (match score); Domain Knowledge list (p. 12).
Quote:       "We evaluated the fully trained instances of AlphaZero ... playing 100
             game matches at tournament time controls of one minute per move.
             AlphaZero and the previous AlphaGo Zero used a single machine with 4
             TPUs. Stockfish and Elmo played at their strongest skill level using 64
             threads and a hash size of 1GB." / "To evaluate performance in chess,
             we used Stockfish version 8 (official Linux release) as a baseline
             program, using 64 CPU threads and a hash size of 1GB."
```

```text
URL:         https://www.science.org/doi/10.1126/science.aar6404
Kind:        primary. The peer-reviewed Science paper (Silver et al., Science 362,
             1140-1144, 7 Dec 2018); the document of record for the lesson. Its own
             page is gated (HTTP 403 / paywall, not dead); the full text was read
             from a freely hosted copy of the identical article (see note in
             Discarded) and every figure below is quoted from that text.
Establishes: The revised, stronger-condition chess match and its exact result; the
             additional matches (latest Stockfish, opening-book Stockfish, TCEC
             opening positions, time-odds); the match hardware; the revised training
             figures; the generality result across all three games.
Paraphrase:  Same method as the preprint. Trained 700,000 steps (mini-batches of
             4,096); "During training only, 5000 first-generation ... TPUs were
             used to generate self-play games, and 16 second-generation TPUs were
             used to train the neural networks. Training lasted for approximately 9
             hours in chess, 12 hours in shogi, and 13 days in Go." First
             outperformed Stockfish after 4 hours (300,000 steps), Elmo after 2
             hours (110,000 steps), AlphaGo Lee after 30 hours (74,000 steps). The
             opponent was "the 2016 TCEC (season 9) world champion Stockfish."
             Match hardware: "Stockfish and Elmo used 44 central processing unit
             (CPU) cores (as in the TCEC world championship), whereas AlphaZero and
             AlphaGo Zero used a single machine with four first-generation TPUs and
             44 CPU cores." "All matches were played by using time controls of 3
             hours per game, plus an additional 15 s for each move." Result: "In
             chess, AlphaZero defeated Stockfish, winning 155 games and losing 6
             games out of 1000." Fig. 2A gives per-colour rates: as white W 29.0% /
             D 70.6% / L 0.4%; as black W 2.0% / D 97.2% / L 0.8%. Additional
             matches (Fig. 2C-D and notes 26-28): AlphaZero also beat the "most
             recent development version of Stockfish" (note 27: newest available as
             of 13 January 2018) and a "variant of Stockfish that uses a strong
             opening book" (note 28: the Cerebellum book from Brainfish; AlphaZero
             used none, and used small opening randomisation, which "resulted in
             more losses"), and won matches from common human openings and from the
             2016 TCEC opening positions (note 26: many TCEC positions are
             unbalanced, "resulting in more losses for both players"). Time odds:
             AlphaZero still beat Stockfish "when given 1/10 as much thinking time."
             Search speed 60,000 positions/s (chess and shogi) vs 60 million for
             Stockfish and 25 million for Elmo. Note 24: "A first generation TPU is
             roughly similar in inference speed to a Titan V GPU, although the
             architectures are not directly comparable." No opening book or
             tablebase is stated as given to Stockfish in the main matches.
Locators:    p. 3 col. 3 (training TPUs/times); p. 4 col. 1 (first-outperformed
             times, match hardware, time control, 155/6/1000 result, additional
             matches); Fig. 2 caption and bars (per-colour rates, time-odds,
             opening-book, TCEC, latest Stockfish); notes 24, 26, 27, 28 (p. 5).
Quote:       "In chess, AlphaZero defeated Stockfish, winning 155 games and losing 6
             games out of 1000 (Fig. 2)." / "All matches were played by using time
             controls of 3 hours per game, plus an additional 15 s for each move." /
             "We played additional matches against the most recent development
             version of Stockfish (27) and a variant of Stockfish that uses a strong
             opening book (28). AlphaZero won all matches by a large margin."
```

```text
URL:         https://deepmind.google/discover/blog/alphazero-shedding-new-light-on-chess-shogi-and-go/
Kind:        primary. DeepMind's own accompanying material; owns DeepMind's public
             framing of the same results.
Establishes: Corroborates the Science match result, hardware, opponent identity and
             the opening-book match, in DeepMind's own words for a general reader.
Paraphrase:  DeepMind states AlphaZero beat "2016 TCEC (Season 9) world champion
             Stockfish," "winning 155 games and losing just six games out of 1,000,"
             at "three hours per game, plus an additional 15 seconds for each move."
             It ran on "a single machine with 4 first-generation TPUs and 44 CPU
             cores," while Stockfish used "44 CPU cores." It reports additional
             matches from common human openings, from the 2016 TCEC opening
             positions, and against "a variant of Stockfish that uses a strong
             opening book," and says "In all matches, AlphaZero won." It repeats that
             a first-generation TPU is "roughly similar in inference speed to
             commodity hardware such as an NVIDIA Titan V GPU," while noting "the
             architectures are not directly comparable."
Locators:    Body sections on the match, the additional matches, and the hardware
             note.
Quote:       "winning 155 games and losing just six games out of 1,000" / "a single
             machine with 4 first-generation TPUs and 44 CPU cores."
```

```text
URL:         https://www.chess.com/news/view/google-s-alphazero-destroys-stockfish-in-100-game-match
Kind:        secondary. Contemporary reporting (FM Mike Klein, chess.com, updated 6
             Dec 2017) of the preprint, carrying named third-party expert reaction.
Establishes: The immediate chess-community reaction to the 2017 preprint's match
             conditions, from named figures qualified to judge.
Paraphrase:  GM Hikaru Nakamura called the match setup unfair, objecting above all
             to Stockfish playing without its standard opening book (he treated the
             hardware gap as the larger issue). GM Larry Kaufman, lead chess
             consultant for the Komodo engine, made the same opening-book point and
             called for testing AlphaZero on standard PC hardware rather than
             Google's specialised hardware. The article notes Stockfish lacked "its
             standard opening knowledge" in the match.
Locators:    Reaction section (Nakamura and Kaufman quotes).
Quote:       Kaufman: "It should be pointed out that AlphaZero had effectively built
             its own opening book, so a fairer run would be against a top engine
             using a good opening book." Nakamura (on Stockfish's handicap): "I am
             pretty sure God himself could not beat Stockfish 75 percent of the time
             with White without certain handicaps."
```

```text
URL:         https://lichess.org/forum/general-chess-discussion/reaction-from-stockfish-author-statement
Kind:        primary (for the statement it carries) via a repost. The statement is by
             Tord Romstad, an original Stockfish author, a party with direct stake;
             it was first published by chess.com in December 2017 and is reproduced
             here verbatim by a forum user. A repost supports that the statement was
             made; its authority is Romstad's, not the forum's.
Establishes: The Stockfish side's own account of why the 2017 match conditions make
             the raw result hard to read.
Paraphrase:  Romstad said the result "by themselves are not particularly meaningful
             because of the rather strange choice of time controls and Stockfish
             parameter settings": the fixed one-minute-per-move control denied
             Stockfish its time-management heuristics; the Stockfish version was a
             year old; it ran with far more search threads than had been well tested
             and with hash tables too small for that thread count. He called the
             comparison "apples to orangutans" given the different hardware and
             approaches, while granting that a genuinely new approach is more
             interesting than another incremental engine.
Locators:    Reposted statement body.
Quote:       "The games were played at a fixed time of 1 minute/move, which means
             that Stockfish has no use of its time management heuristics" /
             "Stockfish vs AlphaZero is very much a comparison of apples to
             orangutans."
```

```text
URL:         https://www.chess.com/news/view/updated-alphazero-crushes-stockfish-in-new-1-000-game-match
Kind:        secondary. chess.com reporting (updated 17 Apr 2019) of the Science
             paper's 1000-game update.
Establishes: How the field read the 2018 update against the 2017 criticism; useful
             for the "how it is cited now" half of the lesson.
Paraphrase:  Reports "+155 -6 =839" against "Stockfish 8" at "three hours each game
             plus a 15-second increment per move," and says this control "would seem
             to make obsolete one of the biggest arguments against ... last year's
             match." Notes the opening-book variant helped Stockfish win a
             substantial number of games as Black but not enough to take the match,
             and that AlphaZero stayed dominant at time odds up to 10-to-1, with
             Stockfish only outscoring it at 30-to-1.
Locators:    Result, time-control, opening-book and time-odds paragraphs.
Quote:       "The updated AlphaZero crushed Stockfish 8 in a new 1,000-game match,
             scoring +155 -6 =839." / "Stockfish only began to outscore AlphaZero
             when the odds reached 30-to-1."
```

```text
URL:         https://lczero.org/
Kind:        primary. The Leela Chess Zero project's own site; owns the project's
             self-description.
Establishes: That Lc0 is a deliberate open-source implementation of the AlphaZero
             method (self-play, neural network), i.e. the replication vehicle.
Paraphrase:  The project describes itself as "a direct open-source implementation
             inspired by DeepMind's AlphaZero project," using "a neural network that
             learned chess through self-play, resulting in a unique style, free from
             all human bias." (The GitHub repository, github.com/LeelaChessZero/lc0,
             carries the same framing and the topics "alphazero" and
             "alphazero-inspired.")
Locators:    Front-page description; GitHub repo topics/README.
Quote:       "a direct open-source implementation inspired by DeepMind's AlphaZero
             project" / "a neural network that learned chess through self-play ...
             free from all human bias."
```

```text
URL:         https://lczero.org/blog/2019/02/leela-booms-stockfish-and-tcec/
Kind:        primary. The Lc0 project's own blog during the TCEC Season 15
             superfinal.
Establishes: The project's contemporaneous account of leading Stockfish in the
             superfinal (the head-to-head that the wiki entry below records as the
             final win).
Paraphrase:  Reports Leela leading Stockfish partway through the superfinal ("A
             33-31 score in favor of Leela") and frames it as evidence that the
             neural-network approach "has huge potential" and that Stockfish, once
             thought near-unbeatable before DeepMind, "is not in fact perfect or
             unbeatable."
Locators:    Post body.
Quote:       "This shows that this new approach of Chess engines has huge potential."
```

```text
URL:         https://www.chessprogramming.org/Leela_Chess_Zero
Kind:        secondary (reference). Community reference; used for the settled
             competitive record, which is itself owned by the TCEC results archive
             (tcec-chess.com), not read directly here.
Establishes: That an AlphaZero-method engine beat Stockfish in an independent
             tournament under standard conditions, and the exact score.
Paraphrase:  States Lc0's goal is to follow "the same type of deep learning along
             with Monte-Carlo tree search (MCTS) techniques of AlphaZero as described
             in DeepMind's 2017 and 2018 papers, but using distributed training,"
             and that "Like AlphaZero, Lc0 evaluates positions using non-linear
             function approximation based on a deep neural network." Records that
             "Lc0 aka LCZero v0.21.1-nT40.T8.610 won the superfinal in May 2019
             versus Stockfish with +14 =79 -7, 53.5-46.5," the first neural-network
             engine to win a TCEC superfinal.
Locators:    Overview (AlphaZero relationship); competitive-results section (TCEC
             Season 15).
Quote:       "won the superfinal in May 2019 versus Stockfish with +14 =79 -7,
             53.5-46.5."
```

```text
URL:         https://www.chessprogramming.org/Stockfish_NNUE
Kind:        secondary (reference). Community reference for Stockfish's own turn to a
             neural network.
Establishes: That the "neural nets beat handcrafted alpha-beta" story did not end
             with AlphaZero/Lc0: Stockfish adopted a neural evaluation and reclaimed
             the top, so the two paradigms converged rather than one replacing the
             other.
Paraphrase:  Stockfish merged NNUE (an efficiently updatable neural network
             evaluation) to master in August 2020; Stockfish 12, the first release
             including it, shipped 2 September 2020. NNUE made Stockfish "stronger
             than the classical one at least 80 Elo" despite roughly halving search
             speed. (Stockfish subsequently won TCEC Seasons 19 and 20 over Leela in
             2020-2021, per those seasons' records.)
Locators:    Timeline and strength sections.
Quote:       "Stockfish NNUE was stronger than the classical one at least 80 Elo."
```

## Contradictions

- **Two different chess matches, one headline.** The preprint match (100 games,
  1 minute per move, Stockfish 8 on 64 threads / 1 GB hash, no opening book,
  AlphaZero on 4 TPUs, result 28 wins / 72 draws / 0 losses) is not the Science
  match (1000 games, 3 hours + 15 s increment, Stockfish on 44 CPU cores, result
  155 wins / 6 losses / 839 draws). The widely-repeated "one minute per move, no
  opening book" conditions describe the *preprint*. Teaching the Science paper as
  the document of record while attributing those conditions to it would be a
  factual error.
- **Preprint vs Science on internal figures.** Second-generation training TPUs:
  64 (preprint) vs 16 (Science). Go training: 34 hours and "outperformed AlphaGo
  Lee after 8 hours (165k steps)" (preprint) vs 13 days and "after 30 hours
  (74,000 steps)" (Science). Chess search speed: 80,000 positions/s vs 70 million
  for Stockfish (preprint) vs 60,000 vs 60 million (Science). The chess and shogi
  first-outperformed times (4 h / 2 h) and the 700,000-step / 4,096-batch figures
  agree across both. The writer should use Science figures and flag the Go and
  TPU-count changes if the difference is taught.
- **Community criticism vs DeepMind's later setup.** Nakamura, Kaufman and
  Romstad attacked the 2017 conditions (no opening book, old version, one minute
  per move, thread/hash settings, hardware). The 2018 Science paper answered most
  of these directly: a realistic increment time control, a match against a
  Stockfish *with* a strong opening book, a match against the January 2018
  Stockfish development build, and Stockfish on 44 cores as in TCEC. AlphaZero
  still won all of them. So the criticism lands on the preprint far harder than on
  the document of record.
- **What did not get normalized, even in Science.** Hardware is still
  cross-paradigm (4 first-generation TPUs + 44 CPU cores for AlphaZero vs 44 CPU
  cores for Stockfish; DeepMind itself calls a TPU "roughly similar" to a Titan V
  GPU but "not directly comparable"). The primary opponent is still Stockfish 8.
  The match was DeepMind's own, not an independent event. And neither paper's main
  text states that Stockfish was given endgame tablebases (a standard Stockfish
  component the Methods describes but does not report enabling for the match).
- **Reproduces, but the ranking did not stay put.** Lc0, an open-source
  AlphaZero-method engine, beat Stockfish in the TCEC Season 15 superfinal (2019)
  under standard tournament conditions, confirming the method reproduces outside
  DeepMind. But Stockfish then adopted its own neural network (NNUE, 2020) and
  retook the top in TCEC Seasons 19-20. The durable finding is that neural
  evaluation plus search beats pure handcrafted alpha-beta, and the field
  converged on the hybrid, not that AlphaZero's approach permanently out-ranks
  Stockfish.

## Numbers

```text
Figure: 700,000 training steps, mini-batches of 4,096 positions
Owner:  Science 2018 (p. 3) and preprint (p. 4); agree
Scope:  Per game; a separate instance trained for chess, shogi, Go
```

```text
Figure: Self-play generation 5,000 first-generation TPUs; training 16
        second-generation TPUs (Science) / 64 second-generation TPUs (preprint)
Owner:  Science 2018 (p. 3) and preprint (p. 4)
Scope:  During training only; the two documents disagree on the training-TPU count
```

```text
Figure: Training wall-clock: chess ~9 h, shogi ~12 h, Go ~13 days (Science) /
        Go 34 h (preprint Table S3)
Owner:  Science 2018 (p. 3); preprint Table S3
Scope:  Full training run per game; chess and shogi agree, Go differs sharply
```

```text
Figure: First surpassed the baseline: Stockfish after 4 h (300,000 steps); Elmo
        after 2 h (110,000 steps); AlphaGo Lee after 30 h (74,000 steps)
Owner:  Science 2018 (p. 4). Preprint agrees on chess/shogi; gives Go as 8 h /
        165,000 steps
Scope:  Elo crossover point during a single training run, 1 s/move evaluation
```

```text
Figure: Chess match result (Science): 155 wins, 6 losses, 839 draws
Owner:  Science 2018 (p. 4); corroborated by DeepMind blog
Scope:  1000 games vs 2016 TCEC S9 Stockfish (Stockfish 8), 3 h/game + 15 s/move
```

```text
Figure: Chess match per-colour rates (Science): white W 29.0% / D 70.6% / L 0.4%;
        black W 2.0% / D 97.2% / L 0.8%
Owner:  Science 2018, Fig. 2A
Scope:  500 games per colour within the 1000-game match (reconciles to 155/6/839)
```

```text
Figure: Chess match result (preprint): 28 wins, 72 draws, 0 losses
Owner:  Preprint, Table 1 (white 25/25/0; black 3/47/0)
Scope:  100 games vs Stockfish 8, 1 minute/move, 64 threads, 1 GB hash
```

```text
Figure: Match hardware (Science): AlphaZero 4 first-generation TPUs + 44 CPU cores;
        Stockfish 44 CPU cores
Owner:  Science 2018 (p. 4); DeepMind blog. Preprint: AlphaZero 4 TPUs; Stockfish
        64 threads, 1 GB hash
Scope:  Head-to-head evaluation configuration
```

```text
Figure: Search speed (Science): AlphaZero ~60,000 positions/s vs Stockfish 60
        million, Elmo 25 million
Owner:  Science 2018 (p. 4), table S4. Preprint: 80,000 vs 70 million (chess)
Scope:  Positions evaluated per second during play
```

```text
Figure: Shogi result: 91.2% overall vs Elmo (98.2% as black); Go: 61% vs AlphaGo
        Zero (3-day)
Owner:  Science 2018 (p. 4). Preprint Table 1: shogi 90/2/8 over 100 games; Go
        AlphaZero 60 wins / 40 losses over 100 games
Scope:  Same 1000-game (Science) / 100-game (preprint) match structure
```

```text
Figure: Lc0 beat Stockfish in the TCEC Season 15 superfinal, +14 =79 -7 (53.5-46.5)
Owner:  Chess Programming Wiki, from the TCEC S15 record (tcec-chess.com)
Scope:  100-game superfinal, May 2019, standard tournament conditions
```

```text
Figure: Stockfish NNUE gain: at least +80 Elo over classical Stockfish
Owner:  Chess Programming Wiki (Stockfish NNUE); merged Aug 2020, Stockfish 12 on
        2 Sep 2020
Scope:  Self-play/testing Elo at the time of adoption
```

## Source assets

```text
Asset: Preprint Table 1 / Science Fig. 2A - the chess, shogi and Go match results
       as win/draw/loss bars from AlphaZero's perspective, split by colour.
Shows: The raw margin the headline rests on, and how lopsided it is toward draws
       when AlphaZero has black. Fig. 2A's stacked bars are cleaner than the
       table for a general reader.
Crop:  Keep the chess row (both colours) with the W/D/L labels and percentages; a
       crop may omit the shogi and Go rows if the lesson stays on chess, but must
       keep the "AlphaZero white / AlphaZero black" labels so the draw-heavy black
       result is not read as the whole match.
```

```text
Asset: Science Fig. 2B-D - scalability with thinking time (time-odds bars) and the
       extra-condition bars (latest Stockfish, opening-book Stockfish, human and
       TCEC opening positions).
Shows: That AlphaZero held up when its own conditions were made harder, which is
       the evidence that answers the 2017 criticism.
Crop:  A crop must keep the condition labels (e.g. "Opening Book," "Latest
       Stockfish," "1/10 time") with their W/D/L bars; a bar without its condition
       label is unreadable and misleading.
```

```text
Asset: Science Fig. 1 / preprint Fig. 1 - Elo vs training steps for chess, shogi,
       Go, with the Stockfish/Elmo/AlphaGo baselines drawn as horizontal lines.
Shows: How fast AlphaZero crossed each baseline (the 4-hour chess crossover),
       grounding the "from scratch in hours" claim in a curve.
Crop:  Keep the axis labels (Elo, thousands of steps) and the baseline line with
       its label; note the horizontal baseline is a fixed reference, not a curve.
```

```text
Asset: Science Fig. 4 - AlphaZero's MCTS search tree for one position from game 1
       vs Stockfish, showing the handful of variations it explores deeply.
Shows: The "searches ~60,000 vs 60 million positions per second, more selectively"
       point made concrete - the mechanism behind the generality claim.
Crop:  Retain the position inset and at least the 10^4-10^6 simulation panels with
       their move labels; a crop must not drop the move annotations that show which
       lines are explored.
```

## Discarded

```text
URL: https://turing.iimas.unam.mx/~luis/cursos/IA2025-2/lecturas/AlphaZero.pdf
     Not a source in its own right - a course-hosted copy of the Science paper
     used only to read the paywalled article's full text. The claim is credited to
     the Science DOI (its own page), which returns 403 (gated, not dead).
```

```text
URL: https://arxiv.org/pdf/1712.01815v2
     404. No accessible v2 of the arXiv preprint; the peer-reviewed revision lives
     as the Science paper, which is cited directly instead.
```

```text
URL: https://www.mendeley.com/... , https://scispace.com/... , https://pubmed.ncbi.nlm.nih.gov/30523106/
     Catalog/index entries for the Science paper, no primary content beyond the
     abstract. Superseded by the full paper.
```

```text
URL: https://en.wikipedia.org/wiki/TCEC_Season_15
     Secondary retelling of the TCEC S15 result; the same figure is carried by the
     Chess Programming Wiki entry cited above and owned by the TCEC archive, so it
     adds no independent confirmation.
```

```text
URL: https://www.chess.com/forum/... , https://www.talkchess.com/forum/... , various
     Forum threads relaying the papers and the Romstad statement. Retellings of
     origins already cited; a repetition supports that a claim was made, not that
     it is true, so they are not counted toward the floor.
```

Source floor: met. Ten sources read; five primary (the 2017 preprint, the 2018
Science paper, the DeepMind blog, Romstad's statement, and the Lc0 project's own
site/blog), three secondary reports/references (chess.com contemporary reporting
x2, and the Chess Programming Wiki entries), comfortably clearing "at least 6
sources, at least 3 primary, at least 1 secondary." Each match condition the
brief asked for is pinned to a primary, except the endgame-tablebase question,
which neither primary's main text answers and which is recorded as a gap.
