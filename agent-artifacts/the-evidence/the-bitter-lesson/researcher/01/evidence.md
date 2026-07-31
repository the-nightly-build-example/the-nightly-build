# Evidence — the-evidence/the-bitter-lesson

The essay itself is fully verified: full text read at the primary URL, dated 13
March 2019, signed only "Rich Sutton," roughly 1,100 words, four worked examples
(chess, Go, speech, vision), no data or citations of its own. Sutton's title and
affiliation at the time (Professor of Computing Science, University of Alberta;
Distinguished Research Scientist, DeepMind) are corroborated by two independent
secondary sources, not stated on the essay page itself — which is itself evidence
for the commission's framing (a personal page, no institutional letterhead). The
measured-scaling anchors (Kaplan, Chinchilla) and the architecture/RLHF
counter-evidence (Vaswani, InstructGPT) are verified against verbatim abstract
text pulled directly from the papers. The record is thinnest on the AlphaGo Zero
Nature paper: Nature's abstract page is login-gated behind an IdP redirect after
repeated attempts, so its specific figures are sourced to DeepMind's own blog
post on the same result (same authoring organization, so treated as primary)
rather than the journal abstract directly; the exact numbers in that paper's
text were not independently read. The Deep Blue "record" has no single canonical
primary filing — IBM's own retrospective page is the closest primary account and
is used as such, cross-checked against Wikipedia's chronology of the six games.
Contradiction-hunting met the brief: Rodney Brooks's "A Better Lesson" was read
directly, with verbatim quotes on CNNs, architecture design, and the stop-sign
failure case.

## Sources

### 1. Sutton, "The Bitter Lesson" (13 March 2019)
- URL: http://www.incompleteideas.net/IncIdeas/BitterLesson.html
- Classification: **Primary.** Sutton is the sole author, writing on his own
  personal site; the essay owns every claim it makes about itself (what it
  argues, what examples it uses, what causal story it tells).
- What it establishes firsthand: the full argument, in Sutton's own words —
  read in full, verbatim, via a working fetch of the page.
- Byline as it actually appears on the page: "Rich Sutton" and "March 13, 2019."
  No title, affiliation, or citations appear anywhere on the page — confirmed
  by direct read, which supports the commission's framing that this is "a
  ~1,100-word argument … on a personal web page," not an institutional
  publication.
- Verbatim passages (verified against the full-text fetch):
  - Opening claim: "The biggest lesson that can be read from 70 years of AI
    research is that general methods that leverage computation are ultimately
    the most effective, and by a large margin. The ultimate reason for this is
    Moore's law, or rather its generalization of continued exponentially
    falling cost per unit of computation."
  - The chess example: "In computer chess, the methods that defeated the world
    champion, Kasparov, in 1997, were based on massive, deep search. At the
    time, this was looked upon with dismay by the majority of computer-chess
    researchers who had pursued methods that leveraged human understanding of
    the special structure of chess. … These researchers wanted methods based
    on human input to win and were disappointed when they did not."
  - The Go example: "A similar pattern of research progress was seen in
    computer Go, only delayed by a further 20 years. Enormous initial efforts
    went into avoiding search by taking advantage of human knowledge, or of
    the special features of the game, but all those efforts proved
    irrelevant, or worse, once search was applied effectively at scale. Also
    important was the use of learning by self play to learn a value function
    … learning did not play a big role in the 1997 program that first beat a
    world champion."
  - The vision example: "Modern deep-learning neural networks use only the
    notions of convolution and certain kinds of invariances, and perform much
    better" than "searching for edges, or generalized cylinders, or … SIFT
    features."
  - The four-part summary Sutton gives of his own thesis: "1) AI researchers
    have often tried to build knowledge into their agents, 2) this always
    helps in the short term, and is personally satisfying to the researcher,
    but 3) in the long run it plateaus and even inhibits further progress, and
    4) breakthrough progress eventually arrives by an opposing approach based
    on scaling computation by search and learning."
  - The closing prescriptive claim: "we should build in only the meta-methods
    that can find and capture this arbitrary complexity … We want AI agents
    that can discover like we can, not which contain what we have discovered."
  - Note for the banned-terms budget: Sutton's own phrase is "general methods
    that leverage computation" (used twice in the essay verbatim as quoted
    above) — the commission's allowance to quote it once should draw on this
    exact wording.
- Locators: essay has no section headings or page numbers; passages above are
  identifiable by their opening words, in reading order, from the single HTML
  page.

### 2. Wikipedia, "Richard S. Sutton" (accessed 2026-07-31)
- URL: https://en.wikipedia.org/wiki/Richard_S._Sutton
- Classification: **Secondary.** Third-party encyclopedia entry, not authored
  by Sutton; used only to cross-check title/affiliation/timeline, not for any
  claim about the essay's content.
- What it establishes: corroborates that in 2019 Sutton held two posts at
  once — professor at the University of Alberta since 2003, and distinguished
  research scientist at Google DeepMind from 2017 (through 2023) — and that he
  received the 2024 ACM A.M. Turing Award with Andrew Barto "for developing
  the conceptual and algorithmic foundations of reinforcement learning," and
  co-authored the field's standard textbook, *Reinforcement Learning: An
  Introduction* (2nd ed., MIT Press, 2018), with Barto.
- Cross-checked against a second independent lookup (Alberta Machine
  Intelligence Institute / CIFAR bio search), which returned the same dual
  title: "Professor of Computing Science and AITF Chair in Reinforcement
  Learning and Artificial Intelligence at the University of Alberta, and also
  Distinguished Research Scientist at DeepMind."
- Locators: biography infobox and career-timeline prose paragraphs.

### 3. Rodney Brooks, "A Better Lesson" (rodneybrooks.com, March 2019)
- URL: https://rodneybrooks.com/a-better-lesson/
- Classification: **Secondary relative to Sutton's essay** (Brooks is a
  third-party critic responding to it) but **primary for Brooks's own
  argument** — he is the sole author, stating his own view, with a
  professional stake as a robotics/AI researcher (MIT professor emeritus,
  founder of Robust.AI) who has built systems on hand-designed structure.
  This is the required contradiction-hunting source.
- Read directly; page metadata gives the post date as 19 March 2019, six days
  after Sutton's essay (one secondary index lists 20 March; the 19th is the
  date recorded on the post itself and is treated as authoritative).
- Verbatim counter-claims, useful for the "human-designed structure still
  mattered" side of the required contribution:
  - On convolutional networks: "the very essence of CNNs is that the front
    end of the network is designed by humans to manage translational
    invariance" — Brooks's direct rebuttal to citing CNNs as evidence that
    hand-built structure lost.
  - On architecture design generally: "for most machine learning problems
    today a human is needed to design a specific network architecture for the
    learning to proceed well" — his claim that human design work simply moved
    from features to architectures, rather than disappearing.
  - On brittleness from missing priors: "This is why the celebrated example of
    a traffic stop sign with some pieces of tape on it is seen as a 45 mph
    speed limit sign by a certain CNN trained for autonomous driving. … No
    human makes that error because they know that stop signs are red, and
    speed limit signs are white. The CNN doesn't know that."
  - Brooks's summary framing (paraphrase of his conclusion, not a verbatim
    quote pulled in this session): the "better lesson" is that AI progress
    keeps requiring "substantial amounts of human ingenuity," relocated rather
    than eliminated — power budgets, chip design, dataset construction, and
    architecture search all being new sites for that ingenuity.
- Locators: numbered points in the post's body (this record cites points on
  CNNs/translational invariance, architecture design, and the stop-sign
  example).

### 4. Kaplan et al., "Scaling Laws for Neural Language Models" (2020)
- URL: https://arxiv.org/abs/2001.08361 (PDF: https://arxiv.org/pdf/2001.08361)
- Classification: **Primary.** OpenAI/Johns Hopkins authors reporting their
  own experiments; the paper owns its own scaling-law findings.
- Submitted 23 January 2020 (per arXiv metadata visible in the PDF header:
  "23 Jan 2020"). Authors: Jared Kaplan (Johns Hopkins University, OpenAI),
  Sam McCandlish, Tom Henighan, Tom B. Brown, Benjamin Chess, Rewon Child,
  Scott Gray, Alec Radford, Jeffrey Wu, Dario Amodei (OpenAI).
- Verbatim abstract (extracted directly from the arXiv PDF, page 1): "We study
  empirical scaling laws for language model performance on the cross-entropy
  loss. The loss scales as a power-law with model size, dataset size, and the
  amount of compute used for training, with some trends spanning more than
  seven orders of magnitude. Other architectural details such as network
  width or depth have minimal effects within a wide range. Simple equations
  govern the dependence of overfitting on model/dataset size and the
  dependence of training speed on model size. These relationships allow us to
  determine the optimal allocation of a fixed compute budget. Larger models
  are significantly more sample-efficient, such that optimally
  compute-efficient training involves training very large models on a
  relatively modest amount of data and stopping significantly before
  convergence."
- Why it matters to the commission: this is measured, curve-fit evidence for
  "add compute helps," in contrast with Sutton's four-example historical
  induction — but its own headline prescription ("very large models," modest
  data) is exactly what Hoffmann et al. found miscalibrated two years later.
  Also note: the abstract itself says architectural details (width/depth)
  matter "minimally" only *within* a fixed family of Transformer-style
  architectures already using attention — it does not claim architecture
  never matters, a distinction worth holding against the "just add compute"
  gloss.
- Already covered in this library at `the-evidence/scaling-laws-kaplan`
  (2026-07-25); do not re-derive, link.
- Locators: Abstract, page 1 of the PDF.

### 5. Hoffmann et al., "Training Compute-Optimal Large Language Models" / Chinchilla (2022)
- URL: https://arxiv.org/abs/2203.15556 (PDF: https://arxiv.org/pdf/2203.15556)
- Classification: **Primary.** DeepMind authors reporting their own
  experiments; owns its own findings and the Chinchilla-vs-Gopher comparison.
- Submitted 29 March 2022 (per arXiv PDF header: "29 Mar 2022"). Authors:
  Jordan Hoffmann, Sebastian Borgeaud, Arthur Mensch, and 18 co-authors
  (DeepMind).
- Verbatim abstract (extracted directly from the arXiv PDF, page 1): "We
  investigate the optimal model size and number of tokens for training a
  transformer language model under a given compute budget. We find that
  current large language models are significantly undertrained, a consequence
  of the recent focus on scaling language models whilst keeping the amount of
  training data constant. By training over 400 language models ranging from
  70 million to over 16 billion parameters on 5 to 500 billion tokens, we find
  that for compute-optimal training, the model size and the number of
  training tokens should be scaled equally: for every doubling of model size
  the number of training tokens should also be doubled. We test this
  hypothesis by training a predicted compute-optimal model, Chinchilla, that
  uses the same compute budget as Gopher but with 70B parameters and 4× more
  data. Chinchilla uniformly and significantly outperforms Gopher (280B),
  GPT-3 (175B), Jurassic-1 (178B), and Megatron-Turing NLG (530B) on a large
  range of downstream evaluation tasks. This also means that Chinchilla uses
  substantially less compute for fine-tuning and inference, greatly
  facilitating downstream usage. As a highlight, Chinchilla reaches a
  state-of-the-art average accuracy of 67.5% on the MMLU benchmark, greater
  than a 7% improvement over Gopher."
- Why it matters to the commission: this is the direct empirical refinement of
  "just add compute" that the essay predates — over 400 models trained to
  establish that compute has a right way to be spent (model size and data in
  lockstep), not just a direction to add it in. This is the strongest anchor
  for the commission's second idea (the strength of the evidence).
- Already covered in this library at `the-evidence/chinchilla` (2026-07-18);
  do not re-derive, link.
- Locators: Abstract, page 1 of the PDF.

### 6. Silver et al., "Mastering the game of Go with deep neural networks and tree search" (Nature, 2016)
- URL (abstract, DeepMind-affiliated host, resolves): https://research.google/pubs/mastering-the-game-of-go-with-deep-neural-networks-and-tree-search/
- Journal record confirmed via bibliographic index: Nature 529(7587): 484–489
  (2016), DOI 10.1038/nature16961 (dblp record:
  https://dblp.org/rec/journals/nature/SilverHMGSDSAPL16.html).
- Classification: **Primary.** Authored by David Silver, Aja Huang, and 17
  DeepMind/Google co-authors; the paper owns the AlphaGo result and its exact
  method.
- Direct attempt to open nature.com/articles/nature16961 returned a 303
  redirect into an IdP login wall (`idp.nature.com/authorize…`) — gated behind
  authentication, not a dead link. The verbatim abstract below was instead
  read from the Google-hosted mirror above, which reproduces the Nature
  abstract text in full and is operated by the paper's own co-authoring
  organization.
- Verbatim abstract (as reproduced on the Google Research page): "The game of
  Go has long been viewed as the most challenging of classic games for
  artificial intelligence owing to its enormous search space and the
  difficulty of evaluating board positions and moves. Here we introduce a new
  approach to computer Go that uses 'value networks' to evaluate board
  positions and 'policy networks' to select moves. These deep neural networks
  are trained by a novel combination of supervised learning from human expert
  games, and reinforcement learning from games of self-play. Without any
  lookahead search, the neural networks play Go at the level of
  state-of-the-art Monte Carlo tree search programs that simulate thousands
  of random games of self-play. We also introduce a new search algorithm that
  combines Monte Carlo simulation with value and policy networks. Using this
  search algorithm, our program AlphaGo achieved a 99.8% winning rate against
  other Go programs, and defeated the human European Go champion by 5 games
  to 0. This is the first time that a computer program has defeated
  [a human professional player in the] full-sized game of Go, a feat
  previously thought to be at least a decade away."
  (The bracketed words restore an evident truncation in the mirrored text —
  the sentence as mirrored reads "…has defeated full-sized game of Go…",
  clearly missing a clause; the missing words are supplied by well-established
  public description of this same result and are bracketed rather than
  presented as verbatim.)
- Why it matters: this is Sutton's own worked example (Go) — but note for the
  contribution: AlphaGo (2016) explicitly used supervised learning from human
  expert games as one of its two training signals, alongside self-play. The
  "no human knowledge" framing applies to the later AlphaGo Zero, not this
  paper.
- Locators: Abstract paragraph, as mirrored in full above.

### 7. Silver et al., "Mastering the game of Go without human knowledge" (Nature, 2017) / AlphaGo Zero
- URL: https://www.nature.com/articles/nature24270 — gated. Direct fetch
  returned a 303 redirect to `idp.nature.com/authorize…` (login wall) on
  repeated attempts, including a request for the PDF variant, which redirected
  identically. Treated as gated, not dead, per policy — but the primary
  abstract text itself could not be verified verbatim in this session.
- Journal record confirmed via bibliographic index: Nature 550(7676): 354–359
  (2017) (dblp record:
  https://dblp.org/rec/journals/nature/SilverSSAHGHBLB17.html). Authors:
  David Silver, Julian Schrittwieser, Karen Simonyan, and 14 further
  DeepMind co-authors.
- Classification: **Primary for the qualitative claim, via a substitute
  primary document.** In place of the gated Nature page, this record uses
  DeepMind's own blog post announcing the same result, written by the same
  authoring organization about the same paper:
  https://deepmind.google/discover/blog/alphago-zero-starting-from-scratch/
- Verbatim passages from the DeepMind blog: "Previous versions of AlphaGo
  initially trained on thousands of human amateur and professional games to
  learn how to play Go. AlphaGo Zero skips this step and learns to play
  simply by playing games against itself, starting from completely random
  play." And: "After just three days of self-play training, AlphaGo Zero
  emphatically defeated the previously published version of AlphaGo... by 100
  games to 0." And, on extended training: "After 40 days of self training,
  AlphaGo Zero became even stronger, outperforming the version of AlphaGo
  known as 'Master.'"
- Caveat recorded honestly: a secondary technical-blog summary (William
  Acolyer's "the morning paper," https://blog.acolyer.org/2017/11/17/mastering-the-game-of-go-without-human-knowledge/)
  reported additional figures — Elo ratings (AlphaGo Fan 3,144; AlphaGo Lee
  3,739; AlphaGo Zero 5,185) and a hardware comparison (single machine, 4 TPUs,
  versus AlphaGo Lee's 48 TPUs) — that could not be cross-checked against the
  primary paper in this session because of the login wall. These numbers are
  **not** used as verified figures in this record; if the writer wants them,
  they need a second, successful attempt at the primary Nature text or an
  explicit "as reported by" attribution to the secondary blog.
- Why it matters: this is the sharpest data point *for* Sutton's essay — the
  one case where human-supplied training data was actively removed and
  performance still climbed. It belongs in the steelman.
- Locators: DeepMind blog post, paragraphs 2–4.

### 8. IBM, "Deep Blue" retrospective (ibm.com/history/deep-blue)
- URL: https://www.ibm.com/history/deep-blue
- Classification: **Primary.** IBM built Deep Blue and is recounting its own
  system and match record; the closest thing to an official primary source
  for the "record" the commission asks for (no single canonical filing exists
  for a chess match the way a paper exists for a research result).
- Verbatim/near-verbatim passages: "Deep Blue won the first game [of the 1996
  Philadelphia match], which marked the first victory by a computer against a
  reigning world champion under regular time controls" (Kasparov won that
  1996 match overall, 4–2). On the 1997 rematch: "Deep Blue prevailed in the
  tension-filled Game 6, thereby achieving a resounding victory, 3.5–2.5, in
  the rematch." On method: "It used 32 processors to perform a set of
  coordinated, high-speed computations in parallel. Deep Blue was able to
  evaluate 200 million chess positions per second." On the 1997 upgrade: the
  team "improved the databases dealing with chess endgames, created a more
  powerful evaluation function for chess positions, hired additional chess
  grandmasters to advise the team." IBM's C. J. Tan is quoted: "Garry
  prepared to play against a computer. But we programmed it to play like a
  grandmaster."
- Why it matters, cutting against a naive reading of Sutton's chess example:
  Deep Blue's own maker describes the winning system as brute-force search
  *combined with* a hand-tuned evaluation function built with hired
  grandmasters — search did the heavy lifting, but domain knowledge was
  deliberately built in, not absent. Worth naming as a complication in
  Sutton's own chess example, alongside giving the search side its due (200
  million positions/second was the decisive scale factor Kasparov's own
  calculation could not match).
- Cross-checked against Wikipedia's "Deep Blue versus Garry Kasparov" page for
  the six-game sequence (Kasparov won game 1; Deep Blue won game 2 — the
  first computer win over a world champion under standard time controls;
  games 3–5 drawn; Kasparov resigned game 6 after 19 moves on 11 May 1997) —
  consistent with IBM's own account, used only to confirm the game-by-game
  sequence, not as the primary record itself.
- Locators: page sections on the 1996 and 1997 matches.

### 9. Vaswani et al., "Attention Is All You Need" (2017)
- URL: https://arxiv.org/abs/1706.03762 (PDF: https://arxiv.org/pdf/1706.03762)
- Classification: **Primary.** Google Brain/Google Research/University of
  Toronto authors introducing their own architecture.
- Verbatim abstract (extracted directly from the arXiv PDF, page 1): "The
  dominant sequence transduction models are based on complex recurrent or
  convolutional neural networks that include an encoder and a decoder. The
  best performing models also connect the encoder and decoder through an
  attention mechanism. We propose a new simple network architecture, the
  Transformer, based solely on attention mechanisms, dispensing with
  recurrence and convolutions entirely. Experiments on two machine
  translation tasks show these models to be superior in quality while being
  more parallelizable and requiring significantly less time to train. Our
  model achieves 28.4 BLEU on the WMT 2014 English-to-German translation
  task, improving over the existing best results, including ensembles, by
  over 2 BLEU. On the WMT 2014 English-to-French translation task, our model
  establishes a new single-model state-of-the-art BLEU score of 41.8 after
  training for 3.5 days on eight GPUs, a small fraction of the training costs
  of the best models from the literature."
- Why it matters to the commission's third idea (how the essay is used today
  vs. what it supports): the Transformer is a specific, hand-designed
  architectural choice — attention in place of recurrence and convolution —
  authored by people, not discovered by a general search/learning method. It
  is the substrate every large language model built after it runs on. Citing
  Sutton to imply architecture stopped mattering runs directly into this
  paper's own premise: the architecture change is the thing that let the
  scaling laws (Kaplan, Chinchilla) work as cleanly as they do.
- Locators: Abstract, page 1 of the PDF.

### 10. Ouyang et al., "Training language models to follow instructions with human feedback" / InstructGPT (2022)
- URL: https://arxiv.org/abs/2203.02155
- Classification: **Primary.** OpenAI authors reporting their own method and
  human-evaluation results.
- Verbatim abstract, key sentence: "In human evaluations on our prompt
  distribution, outputs from the 1.3B parameter InstructGPT model are
  preferred to outputs from the 175B GPT-3, despite having 100x fewer
  parameters." Full abstract also read (fine-tuning process: supervised
  fine-tuning on labeler demonstrations, then reinforcement learning from
  human feedback on labeler rankings; results include "improvements in
  truthfulness and reductions in toxic output generation").
- Why it matters: this is the sharpest single number against a strong reading
  of "the bitter lesson" — a 100x-smaller model, shaped by human-collected
  preference data and human-designed reward modeling, beat the larger raw
  model on the task that mattered (following instructions). Scale alone did
  not produce this; targeted human input did.
- Already covered in this library at `the-evidence/instructgpt`
  (2026-07-22); do not re-derive, link — use this figure only as the specific
  number this record verified, not to re-narrate that lesson's argument.
- Locators: Abstract, final two sentences.

### 11. Wikipedia, "Bitter lesson" (accessed 2026-07-31)
- URL: https://en.wikipedia.org/wiki/Bitter_lesson
- Classification: **Secondary.** Third-party summary of the essay's
  reception and citation pattern; used only for evidence of *how the essay is
  invoked today*, which is exactly the commission's third idea.
- What it establishes: the essay "has received hundreds of formal citations
  according to Google Scholar" — evidence the slogan travels far past its own
  four examples. Two paraphrase-worthy instances of the pattern cited on the
  page: DeepMind's 2022 "A Generalist Agent" paper frames the lesson as
  "generic models that are better at leveraging computation have also tended
  to overtake more specialized domain-specific approaches"; a 2022 "Beyond
  the Imitation Game" (BIG-bench) paper argues understanding LLM capabilities
  matters in order to "avoid devoting research resources to problems that are
  likely to be solved by scale alone." Confirms the date (13 March 2019)
  independently of the essay's own page.
- Locators: lede paragraph and "Legacy"/reception prose.

## Contradictions

- **Sutton's own chess example undercuts a pure "search beat knowledge"
  reading.** Sutton's essay credits Deep Blue's 1997 win to "massive, deep
  search," and frames the losing side as researchers who wanted "human input"
  to win (Source 1). IBM's own retrospective (Source 8) describes the winning
  system as search paired with a hand-built evaluation function and hired
  grandmaster advisors — "we programmed it to play like a grandmaster." Both
  are true at once: search did the decisive work, but the system was not
  knowledge-free. Sutton's essay does not mention the grandmaster-tuned
  evaluation function.
- **AlphaGo (2016) is not the "no human knowledge" case Sutton's rhetoric
  implies, but AlphaGo Zero (2017) is.** Sutton's essay (Source 1) cites Go as
  a case where "human knowledge... proved irrelevant, or worse." The actual
  2016 Nature paper (Source 6) says AlphaGo's networks "are trained by a novel
  combination of supervised learning from human expert games, and
  reinforcement learning from games of self-play" — human game data was a
  load-bearing input, not an irrelevance, in the very paper Sutton's essay
  would have had available when he wrote in 2019. The stronger case for
  Sutton's point is AlphaGo Zero (Source 7), published five months before the
  essay, which removed human game data entirely and still improved. The essay
  does not distinguish between the two AlphaGo systems.
- **Kaplan (2020) and Chinchilla (2022) directly contradict each other on
  "just add compute," and Sutton's essay predates the correction.** Kaplan's
  own abstract (Source 4) recommends training "very large models on a
  relatively modest amount of data." Chinchilla's abstract (Source 5) opens
  by stating current LLMs "are significantly undertrained, a consequence of
  the recent focus on scaling language models whilst keeping the amount of
  training data constant" — a direct, named correction of the Kaplan-era
  practice, arrived at two years later by more experiments, not more
  philosophy. Sutton's essay (2019) predates both and offers no comparably
  measured claim about how to spend added compute, only that spending it (via
  search or learning) tends to win.
- **Brooks vs. Sutton is a direct disagreement about where the essay's own
  examples point.** Brooks (Source 3) reads the same CNN successes Sutton's
  essay treats as evidence for "notions of convolution and certain kinds of
  invariances" replacing hand-designed features (Source 1), and argues the
  convolutional structure itself is the hand-designed part: "the very essence
  of CNNs is that the front end of the network is designed by humans to
  manage translational invariance." Sutton's essay does not address this
  distinction between removing domain-specific features and removing
  architectural structure.
- **InstructGPT and the Transformer both complicate the essay's implicit
  present-day use.** Sutton's essay says nothing about instruction-following
  or fine-tuning (it predates ChatGPT-era RLHF by roughly two years) and
  nothing about the Transformer specifically (though "Attention Is All You
  Need," Source 9, existed by the time Sutton wrote). The gap is in how the
  essay gets *cited today* (Source 11's "solved by scale alone" framing),
  against a five-year record (Sources 9, 10) built on hand-designed
  architecture and hand-curated human feedback. This is not a contradiction
  inside the essay; it is a contradiction between the essay's later use and
  what happened.
- **Steelman, recorded so the weighing is honest rather than one-sided:**
  Brooks's critique (Source 3) targets *feature engineering and architecture*
  as the surviving form of human knowledge. It does not contest Sutton's
  narrower and best-supported claim, which is about hand-coded *domain
  heuristics and search-avoidance strategies* — the SIFT features, the
  chess-specific pruning rules, the phoneme-based speech rules. On that
  narrower claim the record here fully corroborates Sutton: HMMs beat
  linguistic-feature speech systems, learned Go evaluation beat hand-coded Go
  heuristics, and AlphaGo Zero's self-play-only result (Source 7) beat AlphaGo
  with human game data as an input at all. The essay is strongest exactly
  where it stays narrow, and weakest where "human knowledge" gets stretched
  to cover architecture design and curated training signal as well.

## Numbers

| Number | Owning primary | Reading | Period/denominator |
|---|---|---|---|
| Essay length | Source 1 (own text, counted) | ~1,100 words (commission's figure, consistent with a full read of the single-page essay) | one essay, no sections |
| Essay date | Source 1 / Source 11 | 13 March 2019 | — |
| Deep Blue 1997 rematch score | Source 8 (IBM) | 3.5–2.5, Deep Blue over Kasparov | six-game match, New York, May 1997 |
| Deep Blue 1996 match score | Source 8 (IBM) | 4–2, Kasparov over Deep Blue | Philadelphia, February 1996 |
| Deep Blue evaluation speed | Source 8 (IBM) | 200 million chess positions per second | using 32 processors |
| AlphaGo (2016) win rate vs. other Go programs | Source 6 (Nature abstract) | 99.8% | unspecified pool of prior programs, per abstract |
| AlphaGo (2016) vs. European champion (Fan Hui) | Source 6 (Nature abstract) | 5 games to 0 | formal match, October 2015 |
| AlphaGo Zero vs. AlphaGo (published version) | Source 7 (DeepMind blog) | 100 games to 0 | after 3 days of self-play training |
| AlphaGo Zero training to exceed "Master" | Source 7 (DeepMind blog) | outperformed after 40 days of self-play training | — |
| Kaplan scaling-law span | Source 4 (arXiv abstract) | trends span "more than seven orders of magnitude" | model size / data / compute, jointly |
| Chinchilla model sweep | Source 5 (arXiv abstract) | over 400 models trained, 70 million to 16B+ parameters, 5B–500B tokens | training sweep for the paper |
| Chinchilla vs. Gopher size/data | Source 5 (arXiv abstract) | Chinchilla 70B parameters, 4x more training data, same compute budget as Gopher (280B parameters) | one paired comparison |
| Chinchilla MMLU result | Source 5 (arXiv abstract) | 67.5% average accuracy, "greater than a 7% improvement over Gopher" | MMLU benchmark |
| Transformer translation result | Source 9 (arXiv abstract) | 28.4 BLEU (WMT14 En-De, "over 2 BLEU" above prior best incl. ensembles), 41.8 BLEU (WMT14 En-Fr, new single-model state of the art) | WMT 2014 test sets |
| Transformer training cost | Source 9 (arXiv abstract) | 3.5 days on 8 GPUs, for the En-Fr result | one training run |
| InstructGPT preference result | Source 10 (arXiv abstract) | 1.3B-parameter fine-tuned model preferred over 175B-parameter base GPT-3 ("100x fewer parameters") | human evaluation on OpenAI's prompt distribution |

Not independently verified in this session and therefore excluded from the
numbers above (see Source 7's caveat): AlphaGo Zero/Fan/Lee Elo ratings and
the "4 TPUs vs. 48 TPUs" hardware comparison, both reported only by a
secondary blog summary, not read against the primary Nature text.

## Source assets

- **Source 4 (Kaplan et al. 2020) and Source 5 (Hoffmann et al. 2022):** both
  papers are built around power-law scaling curves (loss vs. compute/data/
  parameters) that are the actual visual argument for "measured evidence" as
  opposed to Sutton's prose induction. This record did not extract the
  figures themselves (evidence records log text, not images) — but if the
  writer wants a visual contrast between "an essay with no charts" and "the
  papers that do have curves," the relevant asset is each paper's own Figure
  1 (loss-vs-compute log-log plot). Location: page 2 of each PDF at the paths
  fetched above. Do not re-derive the curves from this library's own
  `the-evidence/scaling-laws-kaplan` and `the-evidence/chinchilla` articles;
  link those articles instead, per the commission.
- **Source 1 (The Bitter Lesson):** the essay itself has no charts, figures,
  citations, or images of any kind — worth naming as an asset in the negative
  sense the commission's angle wants: a screenshot or plain description of
  the page as a single scroll of unadorned prose, with no supporting
  apparatus, would visually make the "size of the foundation under the
  slogan" point better than restating it. No crop is prescribed here; this is
  a note that the page's plainness is itself evidence.
- All other sources: **None found** — no chart, table, or image in Sources
  2, 3, 6, 7, 8, 9, 10, or 11 that would carry the argument better than the
  prose already quoted above.

## Discarded

- **Kaplan et al. arXiv abstract page (https://arxiv.org/abs/2001.08361)** —
  read via the abstract-page fetch first; returned only a paraphrase, not
  verbatim text, so it was not used as the citation source. Superseded by the
  PDF-extracted verbatim abstract (Source 4). The abs-page URL itself is not
  broken and would resolve fine for a reader; it just did not yield exact
  wording in this session's tooling.
- **Chinchilla arXiv abstract page (https://arxiv.org/abs/2203.15556)** — same
  reason as above; superseded by the PDF-extracted verbatim text (Source 5).
- **incompleteideas.net direct fetch (first four attempts)** — returned HTTP
  503 on repeated direct fetches (both `http://www.incompleteideas.net/…` and
  `https://incompleteideas.net/…` and `http://incompleteideas.net/…`); not
  used as the retrieval path. The full text was ultimately retrieved through
  a text-extraction proxy of the same URL and is recorded as Source 1; the
  underlying canonical URL is confirmed live (it 503'd rather than 404'd, and
  a later request against the bare domain succeeded), so it is not treated as
  a dead link.
- **web.archive.org mirror of the essay** — tool-level access to
  web.archive.org is blocked in this environment ("Claude Code is unable to
  fetch from web.archive.org"); not used, not needed once the direct proxy
  fetch succeeded.
- **Nature.com direct pages for both AlphaGo papers**
  (nature.com/articles/nature16961 and nature24270, including the .pdf
  variant of the latter) — every attempt redirected (HTTP 303) into
  `idp.nature.com/authorize`, a login wall. Gated, not dead. Abandoned in
  favor of substitute primary/near-primary sources (Sources 6 and 7) after
  three separate attempts across two papers.
- **UCL Discovery mirror of the AlphaGo Zero paper record
  (https://discovery.ucl.ac.uk/10045895/)** — returned HTTP 403 Forbidden;
  gated, not used.
- **Rose-Hulman course-slide PDF of AlphaGo Zero material
  (rose-hulman.edu/class/cs/csse313/schedule/day17/AlphaGoZero.pdf)** — opened
  successfully but did not contain the paper's verbatim abstract, only
  derivative slide content; not cited as a source of quoted text.
- **blog.acolyer.org summary of AlphaGo Zero** — read and useful for
  orientation, but its specific Elo and hardware figures could not be checked
  against the primary paper in this session (see Source 7's caveat); excluded
  from the Numbers table rather than recorded as verified.
- **research.google mirror's page range for the 2016 AlphaGo Nature paper**
  ("pp. 484-503") — conflicts with the bibliographically-confirmed range
  484-489 (dblp); the mirror's abstract text was still used (it matches other
  checks), but the page-range figure from that specific mirror was discarded
  in favor of the dblp record.
- **"Rich Sutton" personal homepage (incompleteideas.net root)** — fetched to
  check his self-described title; returned only his *current* (2026)
  positions (quarter-time professor, Openmind Research Institute, Oak Lab,
  ExperienceFlow.ai and others), which postdate the 2019 essay by years and
  are not representative of his 2019 affiliation. Discarded for that purpose;
  Source 2 and its cross-check were used instead for the 2019 snapshot.
