purpose: evidence record for the-evidence/alphago
inputs: brief.md, commission.md, editorial-direction.md (same run)

# Evidence: the-evidence/alphago

The evidence fully supports the commission's angle and every number the brief asked for.
I read the 2016 Nature paper (Silver et al., "Mastering the game of Go with deep neural
networks and tree search") in full, including Methods and all Extended Data tables, via
the DeepMind-hosted author copy — the same text as the published article, paginated
484–489 plus online Methods. I read the 2017 AlphaGo Zero paper (Silver et al.,
"Mastering the Game of Go without Human Knowledge") in full via the author's UCL
Discovery self-archived copy, which carries the identical abstract, section numbering,
and figures as Nature 550:354–359. Both papers confirm every figure and claim the brief
listed as needing verification: the KGS training set (29.4 million positions, 160,000
games), the 99.8% win rate, the Fan Hui score (5–0 formal) and his exact title
(professional 2 dan, European champion 2013–2015), the hardware counts, and AlphaGo
Zero's 100–0 result against AlphaGo Lee specifically (not AlphaGo Fan). The Lee Sedol
match is independently confirmed by three secondary sources (Wikipedia, a contemporaneous
People's Daily report, and Google's own announcement blog), all agreeing on the 9–15
March 2016 dates, the 4–1 score, and game 4 as Lee's sole win. For the present-day
question, the DeepSeek-R1 paper (arXiv 2501.12948, January 2025) is a first-party primary
account of an AI lab explicitly invoking AlphaGo/AlphaGo Zero's self-play-plus-search
recipe and explaining, in its own words, why it did not transfer to language-model
training — this is the strongest, most honestly qualified instance of the analogy I
found, and it argues against overstatement rather than for it. The evidence is thin only
on the internal engineering detail of exactly what fraction of "search plus self-play"
citations in 2024–2025 discourse are qualified versus hyped; I found one strong qualified
example and general survey/commentary material, but did not attempt an exhaustive census
of all such citations, which the commission does not ask for.

## Sources

### 1. Silver, D. et al. "Mastering the game of Go with deep neural networks and tree search." *Nature* 529, 484–489 (28 January 2016). DOI: 10.1038/nature16961.
- **URLs**: Canonical/DOI: https://www.nature.com/articles/nature16961 (paywalled; redirects
  to an institutional-login gate, confirmed gated not dead). Full text read via the
  DeepMind-hosted author PDF: https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf
  (resolved, 2.6MB, 6 pages of main article + 14 pages Methods/Extended Data, identical
  pagination to the print journal, 484–489).
- **Classification**: Primary. Authored by the DeepMind team that built AlphaGo; owns
  every claim about the system's architecture, training pipeline, scale, and the Fan Hui
  result reported inside it.
- **What it establishes firsthand**: The full architecture (SL policy network, RL policy
  network, rollout policy, value network, MCTS integration); the training pipeline and
  exact dataset sizes; the 99.8% tournament win rate; the Fan Hui match score, dates, and
  Fan Hui's rank/title; hardware configuration for both single-machine and distributed
  AlphaGo. It explicitly does NOT mention Lee Sedol anywhere in the text (confirmed by
  reading start to finish, including acknowledgements) — the paper predates and does not
  report that match.
- **Verbatim passages** (page numbers refer to the printed Nature pagination visible in
  the PDF):
  - Abstract, p. 484: "Here we introduce a new approach to computer Go that uses 'value
    networks' to evaluate board positions and 'policy networks' to select moves... Using
    this search algorithm, our program AlphaGo achieved a 99.8% winning rate against other
    Go programs, and defeated the human European Go champion by 5 games to 0."
  - Policy/value/MCTS roles, p. 484: "We use these neural networks to reduce the effective
    depth and breadth of the search tree: evaluating positions using a value network, and
    sampling actions using a policy network." And: "Monte Carlo tree search (MCTS) uses
    Monte Carlo rollouts to estimate the value of each state in a search tree. As more
    simulations are executed, the search tree grows larger and the relevant values become
    more accurate."
  - MCTS action selection, p. 486: "AlphaGo combines the policy and value networks in an
    MCTS algorithm... Each edge (s, a) of the search tree stores an action value Q(s, a),
    visit count N(s, a), and prior probability P(s, a)... an action a_t is selected from
    state s_t [that maximizes] action value plus a bonus... proportional to the prior
    probability but decays with repeated visits to encourage exploration."
  - SL policy training / KGS dataset, p. 485 (main text) and Methods "Policy network:
    classification" (unnumbered Methods page, page 5 of the PDF's article body): main
    text states "We trained a 13-layer policy network, which we call the SL policy
    network, from 30 million positions from the KGS Go Server. The network predicted
    expert moves on a held out test set with an accuracy of 57.0%..." The Methods section
    gives the exact figures: "This data set contains 29.4 million positions from 160,000
    games played by KGS 6 to 9 dan human players; 35.4% of the games are handicap games.
    The data set was split into a test set (the first million positions) and a training
    set (the remaining 28.4 million positions)."
  - Rollout policy training data, Methods: "the weights π of the rollout policy are
    trained from 8 million positions from human games on the Tygem server."
  - RL policy network, p. 485: "The RL policy network p_ρ is identical in structure to
    the SL policy network... We play games between the current policy network p_ρ and a
    randomly selected previous iteration of the policy network... When played head-to-head,
    the RL policy network won more than 80% of games against the SL policy network...
    Using no search at all, the RL policy network won 85% of games against Pachi."
  - Value network training, p. 486: "we generated a new self-play data set consisting of
    30 million distinct positions, each sampled from a separate game... Training on this
    data set led to MSEs of 0.226 and 0.234 on the training and test set respectively,
    indicating minimal overfitting."
  - Hardware, p. 487: "The final version of AlphaGo used 40 search threads, 48 CPUs, and 8
    GPUs. We also implemented a distributed version of AlphaGo that exploited multiple
    machines, 40 search threads, 1,202 CPUs and 176 GPUs."
  - Tournament win rate, p. 488: "single-machine AlphaGo is many dan ranks stronger than
    any previous Go program, winning 494 out of 495 games (99.8%) against other Go
    programs... AlphaGo won 77%, 86%, and 99% of handicap games against Crazy Stone, Zen
    and Pachi, respectively. The distributed version of AlphaGo was significantly
    stronger, winning 77% of games against single-machine AlphaGo and 100% of its games
    against other programs."
  - Fan Hui match, p. 488: "we evaluated the distributed version of AlphaGo against Fan
    Hui, a professional 2 dan, and the winner of the 2013, 2014 and 2015 European Go
    championships. Over 5–9 October 2015 AlphaGo and Fan Hui competed in a formal
    five-game match. AlphaGo won the match 5 games to 0... This is the first time that a
    computer Go program has defeated a human professional player, without handicap, in the
    full game of Go — a feat that was previously believed to be at least a decade away."
  - Informal games detail, Methods ("Evaluation" subsection): "Five formal games and five
    informal games were played with 7.5 komi, no handicap, and Chinese rules. AlphaGo won
    these games 5–0 and 3–2 respectively... it was also agreed that the overall match
    outcome would be determined solely by the formal games." Extended Data Table 1 lists
    each of the ten games by date (5/10/15 through 9/10/15), colour, and result.
  - Fan Hui's BayesElo rating used to anchor the scale, Methods "Evaluation": "The scale
    was anchored to the BayesElo rating of professional Go player Fan Hui (2,908 at date
    of submission)."
- **Locators**: Main article pp. 484–489; Methods and Extended Data Tables 1–11
  (unpaginated in the PDF but immediately following p. 489, in the order: Methods text,
  Extended Data Table 1 [Fan Hui match log], Table 2 [input features], Table 3 [SL
  results], Table 4 [rollout/tree policy features], Table 5 [AlphaGo parameters], Tables
  6–11 [tournament and scalability cross-tables]).

### 2. Silver, D. et al. "Mastering the Game of Go without Human Knowledge." *Nature* 550, 354–359 (19 October 2017). DOI: 10.1038/nature24270.
- **URLs**: Canonical/DOI: https://www.nature.com/articles/nature24270 (paywalled;
  redirects to an institutional-login gate, confirmed gated not dead). Full text read via
  the author's institutional repository copy: https://discovery.ucl.ac.uk/10045895/
  (landing page; direct PDF at
  https://discovery.ucl.ac.uk/id/eprint/10045895/1/agz_unformatted_nature.pdf, resolved,
  2.4MB, 42 pages including Methods/Extended Data/references). This is the authors'
  unformatted preprint of the identical Nature text, self-archived per UCL's institutional
  repository policy — same title, author list (including David Silver, Julian
  Schrittwieser, Karen Simonyan et al., "DeepMind, 5 New Street Square, London EC4A 3TW"),
  abstract, and figures as the published article.
- **Classification**: Primary. Same authoring team and organization (DeepMind) reporting
  its own new system and result; owns the claim that removing human data still surpassed
  the 2016 system, and the exact 100–0 figure.
- **What it establishes firsthand**: AlphaGo Zero trains "tabula rasa" — solely by
  self-play reinforcement learning starting from random play, with no human game data,
  no supervised pretraining, and no domain knowledge beyond the rules — and that this
  version, after 72 hours of training, beat "the exact version of AlphaGo Lee that
  defeated Lee Sedol" by 100 games to 0. It explicitly distinguishes AlphaGo Fan (beat Fan
  Hui, October 2015) from AlphaGo Lee (beat Lee Sedol, "the winner of 18 international
  titles," March 2016) as two different named prior systems, and states which one Zero's
  100–0 result was measured against.
- **Verbatim passages**:
  - Abstract, p. 1: "A long-standing goal of artificial intelligence is an algorithm that
    learns, tabula rasa, superhuman proficiency in challenging domains... Here, we
    introduce an algorithm based solely on reinforcement learning, without human data,
    guidance, or domain knowledge beyond game rules. AlphaGo becomes its own teacher: a
    neural network is trained to predict AlphaGo's own move selections and also the
    winner of AlphaGo's games... Starting tabula rasa, our new program AlphaGo Zero
    achieved superhuman performance, winning 100-0 against the previously published,
    champion-defeating AlphaGo."
  - Distinguishing AlphaGo Fan and AlphaGo Lee, p. 2: "AlphaGo was the first program to
    achieve superhuman performance in Go. The published version, which we refer to as
    AlphaGo Fan, defeated the European champion Fan Hui in October 2015... A subsequent
    version, which we refer to as AlphaGo Lee, used a similar approach (see Methods), and
    defeated Lee Sedol, the winner of 18 international titles, in March 2016."
  - Three architectural/training differences from the 2016 system, p. 2: "Our program,
    AlphaGo Zero, differs from AlphaGo Fan and AlphaGo Lee in several important aspects.
    First and foremost, it is trained solely by self-play reinforcement learning, starting
    from random play, without any supervision or use of human data. Second, it only uses
    the black and white stones from the board as input features. Third, it uses a single
    neural network, rather than separate policy and value networks. Finally, it uses a
    simpler tree search that relies upon this single neural network to evaluate positions
    and sample moves, without performing any Monte-Carlo rollouts."
  - First (small) training run and the specific 100–0 result, p. 8: "AlphaGo Zero
    outperformed AlphaGo Lee after just 36 hours; for comparison, AlphaGo Lee was trained
    over several months. After 72 hours, we evaluated AlphaGo Zero against the exact
    version of AlphaGo Lee that defeated Lee Sedol, under the 2 hour time controls and
    match conditions as were used in the man-machine match in Seoul... AlphaGo Zero used a
    single machine with 4 Tensor Processing Units (TPUs), while AlphaGo Lee was distributed
    over many machines and used 48 TPUs. AlphaGo Zero defeated AlphaGo Lee by 100 games to
    0."
  - Scale of the (first, smaller) training run, p. 6: "Training started from completely
    random behaviour and continued without human intervention for approximately 3 days.
    Over the course of training, 4.9 million games of self-play were generated, using
    1,600 simulations for each MCTS, which corresponds to approximately 0.4s thinking time
    per move. Parameters were updated from 700,000 mini-batches of 2,048 positions. The
    neural network contained 20 residual blocks."
  - Scale of the second (larger, final) training run, p. 10: "We subsequently applied our
    reinforcement learning pipeline to a second instance of AlphaGo Zero using a larger
    neural network and over a longer duration. Training again started from completely
    random behaviour and continued for approximately 40 days. Over the course of training,
    29 million games of self-play were generated... The neural network contained 40
    residual blocks."
  - Final Elo comparison, p. 12: "The raw neural network, without using any lookahead,
    achieved an Elo rating of 3,055. AlphaGo Zero achieved a rating of 5,185, compared to
    4,858 for AlphaGo Master, 3,739 for AlphaGo Lee and 3,144 for AlphaGo Fan." And: "we
    evaluated AlphaGo Zero head to head against AlphaGo Master in a 100 game match with 2
    hour time controls. AlphaGo Zero won by 89 games to 11."
  - Conclusion / plain framing of what the human-data bootstrap was, p. 13: "a pure
    reinforcement learning approach requires just a few more hours to train, and achieves
    much better asymptotic performance, compared to training on human expert data."
- **Locators**: Main text pp. 1–14 of the author PDF (sections numbered 1 "Reinforcement
  Learning in AlphaGo Zero" through 5 "Conclusion"), matching Nature 550:354–359; page
  numbers above refer to the author-PDF's own page footers (1–14), which is the full
  main-text length; Methods, Extended Data Figures/Tables and references follow to page 42
  (not needed for this lesson's claims, skimmed to confirm no contradiction).

### 3. DeepSeek-AI. "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning." arXiv:2501.12948 (22 January 2025).
- **URLs**: https://arxiv.org/abs/2501.12948 (abstract/metadata, resolved); full text read
  via https://ar5iv.labs.arxiv.org/html/2501.12948 (resolved, HTML rendering of the same
  arXiv preprint).
- **Classification**: Primary. This is a first-party technical report by the lab (DeepSeek-AI)
  that tried the AlphaGo-style approach and reports, in its own voice, what happened when
  it did — it owns the claim about why the analogy did and did not transfer, unlike any
  commentary written by an outside party.
- **What it establishes firsthand**: That a leading 2025 reasoning-model lab explicitly
  modeled part of its research program on AlphaGo and AlphaGo Zero, tried to import their
  method (MCTS at inference time, paired with a trained value model, iteratively
  improved through self-play), and found the transfer did not work for token-by-token
  language generation — a direct, first-party account of where the AlphaGo analogy holds
  and where it strains, exactly the honesty check the commission asks for.
- **Verbatim passage** (Section 4.2, "Unsuccessful Attempts"): "Inspired by AlphaGo (Silver
  et al., 2017b) and AlphaZero (Silver et al., 2017a), we explored using Monte Carlo Tree
  Search (MCTS) to enhance test-time compute scalability... unlike chess, where the search
  space is relatively well-defined, token generation presents an exponentially larger
  search space. To address this, we set a maximum extension limit for each node, but this
  can lead the model to get stuck in local optima. [...] the value model directly
  influences the quality of generation since it guides each step of the search process.
  Training a fine-grained value model is inherently difficult, which makes it challenging
  for the model to iteratively improve. [...] While MCTS can improve performance during
  inference when paired with a pre-trained value model, iteratively boosting model
  performance through self-search remains a significant challenge."
- **Note on scope**: this is the strongest, most explicit primary instance I found of
  AlphaGo being invoked in the 2024–2025 reasoning-model literature. It is a case where
  the citing document itself supplies the caveat the commission wants surfaced (Go's
  well-defined, small, terminal-reward search space versus language's combinatorially
  larger and reward-sparser one) — it argues the disanalogy, not the analogy. I did not
  find a 2024–2025 primary or serious secondary source that cites AlphaGo to claim models
  can "bootstrap ability from nothing" without qualification; the closest overreach risk
  is informal commentary (blog posts, social media) conflating AlphaGo Zero's "no human
  data" finding with the 2016 AlphaGo paper's method, which the "Contradictions" section
  below documents directly against the two Nature papers rather than against a specific
  named offender.
- **Locator**: Section 4.2 of the arXiv v1 preprint (page number varies by renderer; the
  ar5iv HTML section is titled "4.2 Unsuccessful Attempts").

### 4. "AlphaGo versus Lee Sedol." *Wikipedia* (accessed 2 August 2026).
- **URL**: https://en.wikipedia.org/wiki/AlphaGo_versus_Lee_Sedol (resolved).
- **Classification**: Secondary. Written and maintained by editors with no stake in
  AlphaGo's or Lee Sedol's outcome; synthesizes contemporaneous press coverage and match
  records. Not authored by DeepMind, Lee Sedol, or the Korea Baduk Association.
- **What it repeats/confirms** (not a first-party record, but consistent with the two
  contemporaneous news reports below, so treated as corroborated, not merely repeated):
  match played 9–15 March 2016 in Seoul; final score AlphaGo 4, Lee Sedol 1; Lee Sedol won
  game 4 (13 March 2016) by resignation, his only win; Lee Sedol's rank given as
  "professional 9 dan," described as "one of the strongest players in the history of the
  game" and a national figure in South Korea, not as a formal "world champion" title.
- **Locator**: Match summary and game-by-game infobox/table near the top of the article;
  "Game 4" section for the resignation detail.

### 5. "AlphaGo defeats Lee Sedol 4-1 in historic Go match." *People's Daily Online* (15 March 2016).
- **URL**: https://en.people.cn/n3/2016/0315/c202936-9030581.html (resolved).
- **Classification**: Secondary. A wire-style news report from a state media outlet with
  no financial or research stake in AlphaGo; a contemporaneous record of the event as it
  happened, useful as an independent confirmation of the score and dates alongside the
  Wikipedia summary.
- **What it establishes**: Confirms final score 4-1, that the series began "last
  Wednesday" (9 March 2016) in Seoul, that Lee Sedol won game 4 ("the fourth match," on
  the "Sunday" of the series, i.e. 13 March), and describes Lee Sedol as a "Go
  grandmaster" and "the 33-year-old" human champion — not as a formally titled "world
  champion."
- **Locator**: Full short article (single page, no pagination).

### 6. Google. "AlphaGo's ultimate challenge: a five-game match against the legendary Lee Sedol." *Google Blog* (announcement, prior to the March 2016 match).
- **URL**: https://blog.google/technology/ai/alphagos-ultimate-challenge/ (resolved).
- **Classification**: Secondary for the purpose of this lesson's claims about the match
  record (it is Google/DeepMind's own promotional announcement of an event about to
  happen, not a peer-reviewed account of what the 2016 Nature paper measured, and it makes
  no scientific claim this lesson relies on) — noted separately from the two Nature papers
  because it is marketing copy, not a research report; used only for match logistics and
  framing, cross-checked against the two independent news reports above.
- **What it establishes/repeats**: Confirms the match dates (9–15 March 2016, Seoul) and
  schedule (5 games, one every two days); describes Lee Sedol as "the top Go player of the
  past decade" and frames the match as "the outstanding grand challenge for artificial
  intelligence" — notably, Google's own framing does not claim Lee Sedol is a formal
  "world champion," which matters for the popular-claim contradiction below.
- **Locator**: Full blog post (single page).

## Contradictions

1. **"AlphaGo beat the world's best" vs. what the 2016 paper actually measured.** The
   *only* opponent result inside the 2016 Nature paper is against Fan Hui, described by
   the paper itself as "a professional 2 dan, and the winner of the 2013, 2014 and 2015
   European Go championships" (Nature 2016, p. 488) — a continental, not global, title,
   and a mid-tier professional dan (2 dan of 9 possible professional dan ranks; see Figure
   4a's professional-dan axis in the same paper, which places Fan Hui's Elo well below top
   9-dan professionals on the same chart). Popular retellings collapse this into "AlphaGo
   beat the world champion," which is true only of the later, separate Lee Sedol match
   (March 2016, described by Google's own announcement as facing "the top Go player of the
   past decade," not a formally titled world champion either — Go has no single "world
   champion" title in the way boxing or chess do). The 2016 paper does not claim,
   anywhere, to have beaten "the world's best"; its own Discussion section claims only
   that AlphaGo "plays at the level of the strongest human players" (p. 488), a
   population-level claim, not a claim about a specific title match against the literal
   best living player.
2. **"AlphaGo learned Go from scratch / from nothing" is true of AlphaGo Zero (2017), not
   the AlphaGo of the 2016 paper.** The 2016 paper is explicit that its policy network
   pipeline "begins by training a supervised learning (SL) policy network pσ directly from
   expert human moves" (p. 484) using 29.4 million positions from 160,000 human games (see
   Numbers below); only the 2017 AlphaGo Zero paper trains "tabula rasa... without human
   data, guidance, or domain knowledge beyond game rules" (abstract, p. 1). A claim that
   "AlphaGo" (unqualified) learned Go from nothing is accurate only if the speaker means
   AlphaGo Zero specifically, and is false of the system the 2016 Nature paper describes
   and which beat Fan Hui and (separately) Lee Sedol. The two papers use different named
   systems (AlphaGo Fan / AlphaGo Lee vs. AlphaGo Zero) precisely so this distinction can
   be made precisely; the 2017 paper itself makes this distinction explicit (see Source 2,
   "AlphaGo Fan"/"AlphaGo Lee" passage above).
3. **AlphaGo Zero's 100–0 result is against AlphaGo Lee, not AlphaGo Fan or "the 2016
   paper's AlphaGo."** The commission's angle statement risks a shorthand ("beat that
   version 100–0") that could be misread as beating the exact system reported in the 2016
   Nature paper. The 2016 paper's own final released system, evaluated by BayesElo at
   roughly 3140 (distributed) in that paper's internal tournament, is "AlphaGo Fan" in the
   2017 paper's naming; the system Zero explicitly measured itself against 100–0 was
   "AlphaGo Lee" — a later, separately-trained, stronger version that beat Lee Sedol and
   which the 2017 paper states scored 3,739 Elo on its own final comparison scale, versus
   AlphaGo Fan's 3,144 (Source 2, Elo comparison passage). These are related but distinct
   systems; the write-up should say "AlphaGo Lee," not simply "the 2016 system" or "the
   original AlphaGo," when reporting the exact 100–0 figure.
4. **No contradiction found between the two DeepMind papers and the three independent
   Lee Sedol accounts.** Wikipedia, People's Daily, and Google's own blog agree on dates
   (9, 10, 12, 13, 15 March 2016), score (4–1), and that game 4 was Lee Sedol's sole win.
   I looked for a discrepancy (e.g., disputed dates, disputed game count, disputed
   resignation vs. score-based wins) and found none; treat this as solidly corroborated
   rather than resting on one source.
5. **On present-day usage, I found qualification rather than overstatement in the
   strongest primary example (DeepSeek-R1), which cuts against the commission's working
   assumption that today's citations often overreach.** The commission's brief asks to
   "flag any overstatement," anticipating that some 2024–2025 reasoning-model discourse
   cites AlphaGo/AlphaGo Zero to claim search-plus-self-play generalizes cleanly. The
   strongest primary artifact found (DeepSeek-R1, Source 3) does the opposite: it names
   the AlphaGo/AlphaZero inspiration and then explains, precisely, why the transfer to
   token generation failed (exponentially larger search space, no easy fine-grained value
   model). This is worth stating honestly in the write-up rather than manufacturing an
   overreach that the best available evidence does not support; if a rhetorical
   overstatement is wanted as a foil, it exists mainly in informal/secondary commentary
   (the search results returned several blog/Medium pieces asserting a loose "AlphaGo
   showed X, now reasoning models do X too" lineage without DeepSeek-R1's caveats), not in
   a citable first-party research document.

## Numbers

| Figure | Exact reading | Owning primary | Locator |
|---|---|---|---|
| SL policy network training data | 29.4 million positions from 160,000 games (KGS 6–9 dan players; 35.4% handicap games); split into 1M-position test set / 28.4M-position training set. Main text rounds this to "30 million positions from the KGS Go Server." | Silver et al. 2016 | Methods, "Policy network: classification"; main text p. 485 |
| SL policy network accuracy | 57.0% (all input features) / 55.7% (raw board + move history only) on held-out test set, vs. 44.4% state of the art at submission | Silver et al. 2016 | p. 485 |
| Rollout policy training data | 8 million positions from human games on the Tygem server; 24.2% move-prediction accuracy; 2 μs per move selection | Silver et al. 2016 | p. 485; Methods "Rollout policy" |
| RL policy network self-play result | RL policy network won >80% of games against the SL policy network head-to-head; won 85% of games (no search) against Pachi, an open-source program ranked 2 amateur dan on KGS running 100,000 simulations/move | Silver et al. 2016 | p. 485 |
| Value network training data | Over 30 million distinct self-play positions, one per game, generated by the RL policy network playing itself | Silver et al. 2016 | p. 486 |
| Tournament win rate vs. other Go programs | 494 of 495 games won (99.8%), single-machine AlphaGo vs. Crazy Stone, Zen, Pachi, Fuego, GnuGo | Silver et al. 2016 | p. 488 |
| Handicap-game win rates | 77% (vs. Crazy Stone), 86% (vs. Zen), 99% (vs. Pachi), each given 4 free handicap stones | Silver et al. 2016 | p. 488 |
| Distributed vs. single-machine AlphaGo | Distributed version won 77% of games against single-machine AlphaGo, 100% against all other programs | Silver et al. 2016 | p. 488 |
| Hardware, single machine | 40 search threads, 48 CPUs, 8 GPUs | Silver et al. 2016 | p. 487 |
| Hardware, distributed | 40 search threads, 1,202 CPUs, 176 GPUs (Elo 3,140 in internal tournament; other configurations up to 64 threads/1,920 CPUs/280 GPUs tested, Elo 3,168) | Silver et al. 2016 | p. 487; Extended Data Tables 6, 8 |
| Fan Hui match | 5 games to 0 (formal match); separately, 3–2 to AlphaGo in five informal games (not counted in the official result); played 5–9 October 2015 | Silver et al. 2016 | p. 488; Methods "Evaluation"; Extended Data Table 1 |
| Fan Hui's rank/title | Professional 2 dan; winner of the 2013, 2014, and 2015 European Go championships | Silver et al. 2016 | p. 488 |
| Fan Hui's BayesElo rating (anchor point) | 2,908 "at date of submission" | Silver et al. 2016 | Methods "Evaluation" |
| Lee Sedol match | AlphaGo 4, Lee Sedol 1; played 9–15 March 2016 in Seoul; Lee Sedol's sole win was game 4 (13 March), by resignation | Not in either Nature paper (secondary sources only) | Wikipedia "AlphaGo versus Lee Sedol"; People's Daily 15 Mar 2016; Google blog announcement |
| AlphaGo Zero, first (smaller) training run | 4.9 million self-play games; ~3 days; 1,600 MCTS simulations/move (~0.4s/move); 700,000 mini-batches of 2,048 positions; 20 residual blocks | Silver et al. 2017 (Zero) | p. 6 |
| AlphaGo Zero vs. AlphaGo Lee | 100 games to 0, evaluated after 72 hours of training, under the same 2-hour time controls used in the Seoul match; AlphaGo Zero ran on 1 machine / 4 TPUs vs. AlphaGo Lee's distributed 48 TPUs | Silver et al. 2017 (Zero) | p. 8 |
| AlphaGo Zero, second (final, larger) training run | 29 million self-play games; ~40 days; 3.1 million mini-batches of 2,048 positions; 40 residual blocks | Silver et al. 2017 (Zero) | p. 10 |
| Final Elo comparison (5-second-per-move tournament) | Raw network (no search) 3,055; AlphaGo Zero 5,185; AlphaGo Master 4,858; AlphaGo Lee 3,739; AlphaGo Fan 3,144 | Silver et al. 2017 (Zero) | p. 12 |
| AlphaGo Zero vs. AlphaGo Master | 89 games to 11, 100-game match, 2-hour time controls | Silver et al. 2017 (Zero) | p. 12 |
| Elo-to-win-probability scale (both papers use this convention) | A 200-point Elo gap ≈ 75% win probability (2017 paper); a 230-point gap ≈ 79% win probability, "roughly one amateur dan rank" (2016 paper) | Both papers (each states its own convention) | 2016 paper Fig. 4 caption; 2017 paper Fig. 6 caption |

## Source assets

**Recommended**: Figure 4 of Silver et al. 2016 ("Tournament evaluation of AlphaGo,"
p. 488 of the Nature PDF, https://storage.googleapis.com/deepmind-media/alphago/AlphaGoNaturePaper.pdf).
Panel (a) plots every tested Go program (GnuGo, Fuego, Pachi, Zen, Crazy Stone, AlphaGo,
distributed AlphaGo) and Fan Hui himself on a single Elo axis, with a professional/amateur/
kyu dan-rank scale drawn alongside it. This is the single image that lets a reader see, at
a glance, both (1) how far ahead of other Go software AlphaGo was and (2) exactly where
Fan Hui's own rating sits on the professional-dan scale relative to the top of that scale
— the visual evidence for the "European champion, not world number one" distinction the
commission's angle rests on. A crop must retain: the full Elo y-axis with its numeric
tick labels, the professional/amateur/kyu dan-rank labels running alongside it, and the
labeled bars for at least "distributed AlphaGo," "AlphaGo," and "Fan Hui" (the other
program bars can be cropped tightly around if space is short, but Fan Hui's own bar and
its confidence interval must stay legible next to the dan-rank axis, not just the Elo
number). Do not crop out the dan-rank scale — the number alone (2,908 vs 3,140) does not
convey the argument as directly as seeing Fan Hui's position relative to the professional
9-dan ceiling on the same chart.

**Secondary candidate**: Figure 1 of the same paper ("Neural network training pipeline
and architecture," p. 485) is the clearest single diagram of the four-stage pipeline
(rollout policy / SL policy network / RL policy network / value network) and could
illustrate idea 2 (training pipeline) if the piece wants a visual there instead of prose;
panel (a) shows human-expert-positions feeding SL+rollout training, self-play-positions
feeding RL then value-network training, which maps directly onto the lesson's three-stage
narrative (imitate humans, then self-play, then learn to evaluate).

None found for AlphaGo Zero (2017) beyond the Elo-over-training-time line chart (Figure 3a
in that paper), which is useful but less central to this lesson's three ideas than the
2016 paper's Figure 4.

## Discarded

- **Nature.com direct URLs** (https://www.nature.com/articles/nature16961 and
  /nature24270): both return a 303 redirect to an institutional-login gate (idp.nature.com)
  when fetched directly — gated, not dead. Superseded by the author-hosted full-text
  copies (Sources 1 and 2 above), which carry identical text; kept the nature.com URLs in
  the citation record as the canonical DOI-bearing reference, not as the access route.
- **research.google publication landing page**
  (https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/):
  metadata/abstract page only, no full text; an automated summary of it also mis-stated
  the page range (484–503 instead of 484–489). Discarded once the full author PDF was
  read directly; not cited for any claim.
- **Michael Wollowski, course slide deck "Summary of Silver et al., Mastering the game of
  Go without human knowledge"** (fetched from
  https://www.rose-hulman.edu/class/cs/csse313/schedule/day17/AlphaGoZero.pdf while
  searching for the Zero paper's full text): this is a third party's teaching slide deck,
  not the paper itself, and its numbers (4.9 million self-play games, 3-day training, 100-0
  result) turned out to match the primary once found — but it is not authoritative and was
  dropped in favor of the actual UCL Discovery author copy (Source 2). Not cited.
- **An early automated single-pass summary of the 2016 paper's own PDF**, produced before I
  read the underlying document directly: this pass mis-stated the KGS figure as "150,000
  professional games" and conflated the Fan Hui match record with Lee Sedol's ("4-1,
  professional 2 dan"), which is wrong — Fan Hui's match was 5-0 formal and his rank is
  correctly 2 dan, but the 4-1 score belongs to the later, separate Lee Sedol match. This
  discrepancy is exactly why I re-read the underlying PDF page images myself rather than
  rely on an automated single-pass summary for any figure in this record; every number
  above was verified against the actual page text, not against that summary.
- **The self-play survey PDF** (victorchen96.github.io/auto_research/self_play_survey.pdf),
  found while searching for present-day AlphaGo citations in reasoning-model discourse:
  the automated fetch could not extract a coherent, quotable passage connecting AlphaGo to
  2024–2025 reasoning models from this document (likely a rendering/extraction issue with
  this particular PDF), so it was not used as a source; DeepSeek-R1 (Source 3) supplied a
  stronger, directly quotable, first-party passage instead.
- **General web-search summaries of "Noam Brown / o1 / test-time compute"**: useful for
  triangulating that the Go/chess/self-play lineage is widely discussed in 2024–2025
  reasoning-model commentary, but I could not independently open and verify a specific
  primary transcript or paper passage from Noam Brown himself within this session (only
  aggregated search-engine summaries of podcasts were available); not cited as a source
  for any specific quoted claim, used only as corroborating context for why DeepSeek-R1
  was worth pursuing as the citable primary instance.
