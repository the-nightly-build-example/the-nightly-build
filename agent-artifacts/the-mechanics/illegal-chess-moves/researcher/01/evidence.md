# Evidence: the-mechanics/illegal-chess-moves (01)

The evidence firmly supports the core mechanism the commission asks for: a language
model is handed a chess game as a stream of move-notation text and predicts the next
token, with no external board it consults, so legality is whatever the learned text
distribution makes likely. That much is settled engineering, documented in every
experiment that ran it (Acher, Dynomight, Yedidia, Karvonen). Illegal-move rates are
measured and real: weak and chat-tuned models fall apart, and one completion model,
gpt-3.5-turbo-instruct, plays at roughly club strength with a near-zero illegal-move
rate, reproduced independently by at least four parties.

Two parts of the commissioned angle are weaker than the assignment assumes, and the
editor needs to know before the writer leans on them. First, "errors compound as the
game leaves well-trodden openings" holds for weak and chat models but is contradicted
for the strong completion model: Acher measured a roughly constant illegal-move rate
across game length, and Dynomight found gpt-3.5-turbo-instruct rarely plays an illegal
move even in the late game and in board positions that have never occurred in any
recorded game. Second, "the model has no board state" is true of any *external* board,
but the internal-representation research shows small transformers trained only on game
transcripts do build a linearly-decodable, causally-usable board representation
(Li et al., Nanda et al., Karvonen). The crucial limit: that research was done on
purpose-built small models, never on the large chat LLMs whose illegal moves the lesson
explains. Whether GPT-4-class chat models hold such a representation is untested and open.

Source floor: 13 sources, 12 primary, 1 secondary. Met.

## Sources

```text
URL:         https://arxiv.org/abs/2210.13382
Kind:        primary — Li, Hopkins, Bau, Viégas, Pfister, Wattenberg own the Othello-GPT
             experiment and its probe measurements. ICLR 2023 (oral).
Establishes: (settled, for this model) A GPT trained only to predict legal Othello moves
             develops an internal representation of the board recoverable by a probe. The
             original paper reports it as *nonlinear*: a 2-layer MLP probe reads the board
             far better than a linear probe. (Text was read via the ar5iv HTML mirror; the
             URL above is the document's own page.)
Paraphrase:  An 8-layer, 8-head, 512-dim GPT ("Othello-GPT") is trained on move sequences
             with no rules given. A linear probe of internal activations never gets board-
             state error below ~20%; a 2-layer MLP probe drops to 1.7% (synthetic data,
             layer 7). Interventional edits to the representation change the model's move
             predictions, and support "latent saliency maps."
Locators:    Abstract; probing section and error-rate table; intervention section.
Quote:       "Although the network has no a priori knowledge of the game or its rules, we
             uncover evidence of an emergent nonlinear internal representation of the board
             state."
```

```text
URL:         https://arxiv.org/abs/2309.00941
Kind:        primary — Nanda, Lee, Wattenberg. BlackboxNLP 2023. Owns the linear-probe
             reproduction that revises Li et al.'s "nonlinear" claim.
Establishes: (settled, for this model) The Othello-GPT board representation IS linear once
             encoded relative to the mover ("mine / yours / empty") rather than by absolute
             color, and it is causally used, not a spurious correlate.
Paraphrase:  Linear probes on the mine/yours/empty encoding reach ~98.3% at layer 4, rising
             to ~99.6% by layer 7. Vector-arithmetic edits along the probe directions flip or
             erase tiles with near-zero residual error and change the model's play, matching
             the earlier gradient-based intervention.
Locators:    Abstract; linear-probe accuracy table; intervention (flip/erase) results.
Quote:       "Our linear probes achieve high accuracy by layer 4."
```

```text
URL:         https://www.neelnanda.io/mechanistic-interpretability/othello
Kind:        primary — Neel Nanda's own write-up of the reproduction (companion to the paper
             above; the accessible, plain-language version).
Establishes: (settled, for this model) The "my color / your color / empty" reframing is what
             turns the representation linear, and a single linear edit at the residual stream
             makes the model play legal moves on the edited board.
Paraphrase:  Rather than a direction for "F5 has a black counter," the model holds "F5 has one
             of my counters," because it plays both sides. Negating the coordinate along that
             probe direction after layer 4 causes the model to make legal moves for the new
             board — evidence for the linear representation hypothesis.
Locators:    "My color not their color" section; intervention section.
Quote:       "rather than having a direction saying eg 'square F5 has a black counter' it says
             'square F5 has one of my counters.'"
```

```text
URL:         https://arxiv.org/abs/2403.15498
Kind:        primary — Adam Karvonen, "Emergent World Models and Latent Variable Estimation
             in Chess-Playing Language Models." COLM 2024. Owns the chess-specific probing.
Establishes: (settled, for this model) A small GPT trained only on chess move text builds a
             linearly-decodable board state AND estimates a latent variable (player skill),
             and both can be edited to change play. This is the closest thing to a board-state
             probe of a chess model.
Paraphrase:  25M-param (8-layer) and 50M-param (16-layer) GPTs, 512-dim, 8 heads, trained
             character-by-character on ~16M Lichess games in PGN ("1.e4 e5 2.Nf3 ..."). The
             16-layer model wins 64% against Stockfish level 0 (~1300 Elo); 8-layer wins 46%;
             legal-move rate >99.6%. Best board-state linear probe: 99.6%. Elo-bucket probe
             (below 1550 vs above 2050): 90.5% vs 69.3% for a random-init control. Skill
             intervention lifts win rate from 16.7% to 43.2% on random starting boards.
Locators:    Abstract; board-probe and win-rate sections; latent-variable (skill) section;
             intervention results.
Quote:       "The model is given no a priori knowledge of the game and is solely trained on
             next character prediction, yet ... we find evidence of internal representations
             of board state."
```

```text
URL:         https://adamkarvonen.github.io/machine_learning/2024/01/03/chess-world-models.html
Kind:        primary — Karvonen's own blog account of the same Chess-GPT work; the readable
             companion with reproduction detail.
Establishes: (settled, for this model) Character-level PGN training; ~1300–1500 Elo; 99.8%
             legal moves; board probe classifies 99.2% of squares over 10,000 games; the
             model plays games unique by move 10, so it is not replaying memorized lines.
Paraphrase:  Input is strings like "1.e4 e5 2.Nf3 ..." over a 32-token vocabulary. A linear
             probe using the my/their encoding reads 99.2% of squares correctly across 10,000
             games. Every sampled game is unique by move 10, arguing for generalization over
             memorization.
Locators:    "How well does it play" and linear-probe sections.
Quote:       "The linear probe accurately classified 99.2% of squares over 10,000 games."
```

```text
URL:         https://github.com/adamkarvonen/chess_gpt_eval/blob/master/README.md
Kind:        primary — Karvonen's evaluation harness; owns the illegal-move measurement for
             gpt-3.5-turbo-instruct against Stockfish.
Establishes: (settled) gpt-3.5-turbo-instruct's illegal-move rate is effectively near zero,
             and gpt-4 mostly loses by playing illegal moves.
Paraphrase:  Over 8,205 moves, gpt-3.5-turbo-instruct made 5 or fewer illegal moves
             (ratio ≤0.0006), games running 15–147 moves (median 45), against Stockfish
             level 16 at 0.1s/move. gpt-4 "consistently loses ... usually due to forced
             resignation after 5 illegal moves."
Locators:    Results table; gpt-4 notes.
Quote:       "total moves: 8205, total illegal moves: 5 or less"
```

```text
URL:         https://blog.mathieuacher.com/GPTsChessEloRatingLegalMoves/
Kind:        primary — Prof. Mathieu Acher, "Debunking the Chessboard." Owns a large,
             adversarial game set (hundreds of games vs Stockfish) with per-model legality and
             Elo. Also the strongest single source on the compounding question.
Establishes: (settled) A per-model gradient of legality, PGN as the input format, and — the
             counter-point — that the illegal-move rate does NOT clearly rise with game length
             for the strong completion model.
Paraphrase:  gpt-3.5-turbo-instruct over 573 games: 16% of games contained an illegal move,
             0.3% of individual moves illegal, games up to 174 moves (avg ~50), estimated
             1750 ±50 Elo. gpt-4/ChatGPT-4 over 179 games: 32% illegal games, 0.66% illegal
             moves, ~1305–1371 Elo. gpt-3.5-turbo (chat) over 53 games: 93% illegal games.
             text-davinci-003 over 73 games: 99% illegal games. Acher reports the illegal-move
             rate stayed roughly constant across the game rather than accumulating.
Locators:    Per-model results tables; the section on game length and illegal-move timing.
Quote:       (paraphrased finding) illegal-move rates remained consistent throughout the game,
             contradicting the hypothesis that errors accumulate as games progress.
```

```text
URL:         https://dynomight.net/chess/  (with follow-up https://dynomight.net/more-chess/)
Kind:        primary — "Dynomight," ran the games. November 2024. Owns the completion-vs-chat
             finding and the late-game/novel-position observation.
Establishes: (settled, observed) Only gpt-3.5-turbo-instruct plays well; chat and instruction-
             tuned models fail; the strong model plays legal moves late and in never-seen
             positions. (open) Why the gap exists — several competing hypotheses.
Paraphrase:  Models played Stockfish on its lowest level, 50 games each (10 for instruct on
             cost). "No other LLM is remotely close." gpt-3.5-turbo-instruct "rarely suggests
             illegal moves, even in the late game," and succeeds in board states "that have
             never existed in any game before in history." Prompt tricks (three in-context
             examples; making the model regurgitate the full move list) lifted gpt-4o to
             ~1540 Elo vs ~1750 for instruct; head-to-head gpt-4o went 10 wins / 5 draws /
             35 losses. Proposed but unresolved causes: OpenAI's data curation, instruction
             tuning degrading play, architecture, and data-fraction "competition."
Locators:    Main post (per-model results, theories); follow-up (examples, regurgitation,
             fine-tuning, board-tracking discussion).
Quote:       "gpt-3.5-turbo-instruct rarely suggests illegal moves, even in the late game."
```

```text
URL:         https://www.lesswrong.com/posts/F6vH6fr8ngo7csDdf/chess-as-a-case-study-in-hidden-capabilities-in-chatgpt
Kind:        primary — Adam Yedidia, Aug 19 2023. The originating public report, and the best
             source on legality degrading with game progression for the *chat* model.
Establishes: (settled, observed) For chat ChatGPT-3.5, legality decays as the game lengthens
             and prompting sharply changes how long it lasts. An edit note records the later,
             stronger instruct result.
Paraphrase:  Without a strong prompt the chat model "becomes unable to make a legal move by
             move 14"; with a game-score prompt it plays ~1000 Elo and stays legal until
             about move 20–30. It beats Stockfish level 1 (~850 Elo) but attempts illegal
             moves against level 2–3 by the twenties/thirties. Edit note: "gpt-3.5-turbo-
             instruct, when prompted correctly, plays consistently legal moves at around the
             1800–2000 Elo level."
Locators:    Body (chat-model games, "magic prompt"); edit note at top.
Quote:       "gpt-3.5-turbo-instruct, when prompted correctly, plays consistently legal moves
             at around the 1800-2000 Elo level."
```

```text
URL:         https://pappubahry.substack.com/p/gpt-versus-one-node-leela
Kind:        primary — David Barry (1800 FIDE), an independent, careful reproduction of the
             instruct-model strength claim against search-free Leela networks and in person.
Establishes: (settled) The ~1750–1900-ish strength claim survives independent testing by a
             titled-adjacent human player, with PGN prompting and a five-retry allowance on
             illegal output.
Paraphrase:  100-game matches vs single-node (no-search) Leela networks. Against the strongest
             modern net at temperature 0, GPT scored 21.5/100; it did better against 2018-era
             nets. In ten 3-minute blitz games Barry lost 9–1, putting GPT ~380 Elo above his
             1900 blitz rating at temperature 0 (~240 at temperature 1). Illegal moves got up
             to five retries before a forfeit.
Locators:    Match-result tables; personal blitz section; methods (retries).
Quote:       "I lost the ten games 9-1."
```

```text
URL:         https://arxiv.org/abs/2503.04421
Kind:        primary — Yifei Yuan and Anders Søgaard (U. Copenhagen), 2025. A follow-up that
             tests the world-model claim with a method designed to answer the probe-
             spuriousness objection.
Establishes: (settled-leaning, still debated) The Othello board layout is recoverable across
             several architectures without supervised probes, addressing the worry that probe
             success is a measurement artifact.
Paraphrase:  Seven models (GPT-2, T5, BART, Flan-T5, LLaMA-2, Mistral, Qwen2.5) reach up to
             99% accuracy in unsupervised grounding of the board; representation-alignment
             (borrowed from cross-lingual embeddings) is used instead of trained probes to
             avoid spurious correlations. Concludes the models "induce the Othello board
             layout." GPT-2 vs BART alignment similarity 93.1% on synthetic data.
Locators:    Abstract; unsupervised-grounding results; alignment-similarity table.
Quote:       "these models not only learn to play Othello, but also induce the Othello board
             layout."
```

```text
URL:         https://arxiv.org/abs/1712.01815
Kind:        primary — Silver et al., AlphaZero (published Science 2018). Used only for the
             engine contrast, not as subject.
Establishes: (settled) A chess engine operates on an explicit game state with the rules
             encoded and searches; it is given the game rules, so it cannot emit an illegal
             move by construction — the opposite of a text predictor.
Paraphrase:  "Starting from random play, and given no domain knowledge except the game rules,"
             AlphaZero learns by self-play with Monte Carlo tree search over the game's legal
             moves. The rules and board are part of the environment, not learned from text.
Locators:    Abstract.
Quote:       "given no domain knowledge except the game rules."
```

```text
URL:         https://simonwillison.net/2024/Nov/21/llm-chess/
Kind:        secondary — Simon Willison summarizing and contextualizing Dynomight's work. Not
             an author of the experiments; supplies framing.
Establishes: Context only: the completion-vs-chat distinction and the prompt tricks, plus a
             widely-repeated claim that OpenAI's pretraining chess data was filtered to Elo
             ≥1800. That last claim is repetition, not something Willison owns — see
             Contradictions; treat as unverified.
Paraphrase:  Restates that completion models "naturally output good next-turn suggestions"
             while the chat interface "dramatically reduces the quality," and that examples
             plus move-list regurgitation recover much of the gap. Attributes to an OpenAI
             December 2023 paper the claim that only games with players Elo ≥1800 were in
             pretraining.
Locators:    Full post.
Quote:       "only games with players of Elo 1800 or higher were included in pretraining"
             (Willison's paraphrase of an OpenAI source, not verified here).
```

## Contradictions

- **The "errors compound as the game leaves openings" step is contradicted for the
  strong model.** The commission's mechanism says errors rise as a game leaves the
  densely-covered opening lines. This holds for chat/weak models (Yedidia: legality
  gone by move 14–33) but not for gpt-3.5-turbo-instruct: Acher measured a roughly
  constant illegal-move rate across game length, and Dynomight found it rarely plays
  illegally even in the late game and in positions never seen in any recorded game.
  The writer can still teach compounding as the failure mode of weak models, but must
  not present it as universal, and should not tie illegal moves specifically to "leaving
  book openings" without this caveat.

- **"The model has no board" needs care.** True for any external board or consulted
  rulebook (settled). But small models trained only on transcripts DO build an internal
  board representation that is linear (Nanda et al.), causally used (Nanda, Karvonen),
  and recoverable without probes (Yuan & Søgaard). "No internal representation" would be
  false for these models. The safe, accurate line: there is no separate board the model
  checks moves against; any board knowledge is baked into learned next-token statistics
  and is only as reliable as those statistics.

- **The representation evidence is not about the model the reader used.** Every board-
  representation result comes from small models trained *exclusively* on game
  transcripts (Othello-GPT ~25M–param scale; Chess-GPT 25–50M). None probes GPT-4,
  Claude, or any general chat LLM. Whether a large chat model holds a comparable board
  representation is untested and open. This is the record's most important limitation.

- **Illegal-move rates disagree across harnesses, because prompting differs.** Karvonen's
  eval: ≤0.0006 illegal for gpt-3.5-turbo-instruct. Acher: 0.3% of moves but 16% of
  games touched by an illegal move. Same model, different prompt format and retry policy.
  Legality is a property of the prompt-plus-model, not the model alone. Numbers must
  always carry their harness.

- **Original nonlinear vs. later linear finding.** Li et al. reported the representation
  as nonlinear; Nanda et al. showed it is linear under a mover-relative encoding. Not a
  factual dispute about whether a representation exists — both agree it does — but a
  correction of its geometry. Report both, in order.

- **The "Elo ≥1800 pretraining filter" claim is unverified.** Repeated by Willison and
  Dynomight, attributed to an OpenAI source. Not confirmed against a primary OpenAI
  document here. Do not state it as fact; at most, "reported."

## Numbers

```text
Figure: linear probe board-state error never below ~20% (21.9% → 20.4%); 2-layer MLP probe
        1.7% (synthetic, layer 7)
Owner:  Li et al. (arxiv 2210.13382)
Scope:  Othello-GPT internal activations by layer; synthetic random-legal-move training set
```

```text
Figure: legal next-move prediction error — synthetic-trained 0.01%; championship-trained
        5.17%; untrained baseline 93.29%
Owner:  Li et al. (arxiv 2210.13382)
Scope:  Othello-GPT top-1 legal-move prediction; the 5.17% shows varied real games are harder
```

```text
Figure: linear probe (mine/yours/empty) 98.3% at layer 4 → 99.6% at layer 7
Owner:  Nanda, Lee, Wattenberg (arxiv 2309.00941)
Scope:  Othello-GPT board-state classification, per layer
```

```text
Figure: Chess-GPT board-state linear probe 99.6% (paper) / 99.2% of squares over 10,000 games
        (blog); legal-move rate >99.6% (paper) / 99.8% (blog)
Owner:  Karvonen (arxiv 2403.15498; adamkarvonen.github.io blog)
Scope:  50M-param, 16-layer GPT trained char-level on ~16M Lichess PGN games
```

```text
Figure: Chess-GPT win rate vs Stockfish level 0 (~1300 Elo): 64% (16-layer), 46% (8-layer)
Owner:  Karvonen (arxiv 2403.15498)
Scope:  self-play-trained chess GPT vs Stockfish level 0
```

```text
Figure: skill-probe intervention lifts win rate 16.7% → 43.2% on random starting boards
Owner:  Karvonen (arxiv 2403.15498)
Scope:  16-layer Chess-GPT, activation edit along the learned player-skill direction
```

```text
Figure: gpt-3.5-turbo-instruct illegal moves ≤5 of 8,205 (ratio ≤0.0006)
Owner:  Karvonen chess_gpt_eval README
Scope:  vs Stockfish level 16, 0.1s/move; games 15–147 moves, median 45
```

```text
Figure: gpt-3.5-turbo-instruct 1750 ±50 Elo; 16% of games with an illegal move; 0.3% of moves
        illegal, over 573 games
Owner:  Acher (blog.mathieuacher.com)
Scope:  vs Stockfish; PGN completion prompting
```

```text
Figure: gpt-4/ChatGPT-4 ~1305–1371 Elo; 32% illegal games; 0.66% illegal moves, over 179 games
Owner:  Acher (blog.mathieuacher.com)
Scope:  vs Stockfish; comparison model, weaker and less legal than instruct
```

```text
Figure: chat ChatGPT-3.5 ~1000 Elo; legal until ~move 20–30 with a strong prompt; unable to
        make a legal move by move 14 without one
Owner:  Yedidia (LessWrong, Aug 19 2023)
Scope:  chat model, illustrating legality decay with game progression
```

```text
Figure: gpt-4o with in-context examples + move-list regurgitation ~1540 Elo; head-to-head vs
        gpt-3.5-turbo-instruct 10 wins / 5 draws / 35 losses over 50 games
Owner:  Dynomight (dynomight.net/more-chess)
Scope:  Prompt-engineering recovery of a chat model toward the completion model's strength
```

```text
Figure: independent human test — David Barry (1800 FIDE) lost a 10-game blitz match 9–1 to
        gpt-3.5-turbo-instruct; ~+380 Elo over his 1900 blitz rating at temperature 0
Owner:  David Barry (pappubahry.substack.com)
Scope:  independent reproduction of the strength claim; five-retry allowance on illegal moves
```

## Source assets

```text
Asset: Li et al. — the probe-error-by-layer figure/table (linear vs 2-layer MLP), arxiv 2210.13382
Shows: the whole point in one image — a linear read of the board fails (~20%+ error) while a
       nonlinear read nearly succeeds (down to 1.7%), which is why the "linear vs nonlinear"
       correction later mattered
Crop:  keep both probe curves and the y-axis (error %) and layer axis; omit surrounding text
```

```text
Asset: Karvonen — the board-state heatmap / probe-accuracy visualization of Chess-GPT tracking
       the board, on his blog (adamkarvonen.github.io, Jan 3 2024)
Shows: a chess model with no board given to it nonetheless holding a recoverable board — the
       single strongest visual for the "it does build a representation" counter-point
Crop:  keep one clear board+probe pairing; omit the multi-panel training-curve clutter
```

```text
Asset: Acher — the per-model results table (games played, % illegal games, % illegal moves,
       Elo), blog.mathieuacher.com
Shows: the legality gradient across models at a glance — instruct near-clean, gpt-4 middling,
       chat-3.5 and davinci mostly illegal
Crop:  keep the model rows and the illegal-rate and Elo columns; a screenshot table, redrawn as
       a chart per spec/charts.md if used in the article
```

```text
Asset: Dynomight — the per-model performance chart (centipawn loss / results vs Stockfish),
       dynomight.net/chess
Shows: "no other LLM is remotely close" — one model far ahead of a crowded floor
Crop:  keep the full model list and the axis; do not crop out the poorly-performing models,
       since the gap is the point
```

Note on charting: the house rule (spec/editorial.md, spec/charts.md) requires charts be PNGs
rendered from a committed script, not screenshots of a source figure. Any figure above used in
the article should be redrawn from the underlying numbers, which are in the Numbers section.

## Discarded

```text
https://www.alignmentforum.org/posts/4KLHJY9sPE7q8HK8N/when-fine-tuning-fails-to-elicit-gpt-3-5-s-chess-abilities: read; a narrower negative result about fine-tuning eliciting chess ability, not needed for the mechanism or the strength claim, which stronger sources cover.
https://arxiv.org/abs/2512.15033 (Geometric Stability Analysis of LLMs in Chess Evaluation): too recent and tangential (evaluation-stability methodology), adds no load-bearing number the cited sources lack.
https://arxiv.org/abs/2601.16823 (Disentangling generalization and memorization ... using chess): interesting but off-target for this lesson's mechanism; the memorization-vs-generalization point is already covered firsthand by Karvonen's "unique by move 10."
https://github.com/DeanHazineh/Emergent-World-Representations-Othello: a third-party reimplementation, not an owning source; the primaries (Li, Nanda) are cited directly.
https://arxiv.org/abs/2511.00059 (Finding Rule-Based Neurons in OthelloGPT): a deeper mechanistic follow-up beyond what the lesson needs; would over-specify.
https://news.ycombinator.com/item?id=37625298 and .../37564604 (HN threads): discussion, not owning sources; used only to locate the primaries, which are cited instead. HN returned 429 on fetch besides.
https://x.com/GrantSlatton/status/1703913578036904431 (origin tweet): gated (X login) and superseded as a citable document by Yedidia's dated LessWrong post and the reproductions.
```
