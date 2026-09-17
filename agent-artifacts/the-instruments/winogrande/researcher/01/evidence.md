# Evidence: the-instruments/winogrande (01)

The evidence solidly supports teaching WinoGrande as a measurement whose
difficulty is engineered, not intrinsic. Read firsthand: the WinoGrande paper in
full (including the AFLITE section and the human-evaluation details), the KR-2012
Winograd Schema Challenge paper in full, the standalone AFLITE paper (Le Bras et
al. 2020), two model reports that publish WinoGrande figures (GPT-3, Llama 2),
the source that owns the "word-association" figure (Trichelair et al. 2018), the
system that held the WinoGrande leaderboard (UNICORN/RAINBOW, Lourie et al.
2021), and the retrospective co-authored by two original WSC authors ("The Defeat
of the Winograd Schema Challenge"). The exact problem count (43,972 all / 12,282
debiased), the human figure (94.0%), the publication-era machine best (RoBERTa
79.1%), and the training-size dependence (Table 4) are all confirmed against the
WinoGrande paper itself. The misled case is well documented and costed: WinoGrande
was built precisely because near-human WSC scores were hollow, and within about a
year the same pattern recurred on WinoGrande (models in the mid-80s to ~90s while
its own designers judge little reasoning gained).

The record is thin in three honest places. First, the original WSC's "small size"
has two owners: the KR-2012 paper describes only a collection of "more than 100"
schemas, while the widely cited "273" is the later standardized WSC273 test set
that WinoGrande and others quote. Second, the closest-to-human WinoGrande number
(UNICORN at 91.2%) is reported by the Defeat paper from the AI2 leaderboard, which
is now offline; the firsthand-verifiable UNICORN figure is 86.6% from its own
paper, and I flag the gap. Third, WinoGrande's own human-level extrapolation
("over 118K training instances") does not reconcile with its own log-linear fit,
so I record it as the paper's stated claim, not as arithmetic I endorse.

## Sources

```text
URL:         https://arxiv.org/abs/1907.10641
Kind:        primary. The dataset's own paper (Sakaguchi, Le Bras, Bhagavatula,
             Choi; Allen Institute for AI, Choi also University of Washington).
             Published AAAI 2020, pp. 8732-8740; arXiv v2. Owns every WinoGrande
             construction and result figure.
Establishes: The problem count, the crowdsourcing and validation procedure, the
             AFLITE algorithm and its parameters, the human figure (94.0%), the
             machine baselines at publication, the training-size learning curve,
             and transfer results to five related benchmarks.
Paraphrase:  WinoGrande is 44k WSC-inspired fill-in-the-blank problems built by
             crowd workers (primed by a random WikiHow anchor word), validated by
             three separate workers, then filtered by AFLITE, a lightweight
             adversarial filter that repeatedly trains linear classifiers over
             RoBERTa embeddings and discards instances those classifiers predict
             too easily. The filtered "debiased" set is far harder for models
             (RoBERTa 79.1%) than for humans (94.0%), and its difficulty tracks
             the training budget allowed.
Locators:    Abstract; §2 (crowdsourcing, 77k collected / 53k valid); §3 +
             Algorithm 1 (AFLITE; m=10,000, n=64, k=500, tau=0.75); §3 counts
             (43,972 all; 12,282 debiased); §4.2 Table 3 (baselines), Table 4 +
             Figure 2 (learning curve); §5 Table 5-6 (transfer); Figure 1 (KL).
Quote:       "The best state-of-the-art methods on WINOGRANDE achieve 59.4-79.1%,
             which are ~15-35% (absolute) below human performance of 94.0%,
             depending on the amount of the training data allowed (2%-100%
             respectively)."
```

```text
URL:         https://www.cs.nyu.edu/faculty/davise/papers/WSKR2012.pdf
Kind:        primary. The origin paper the commission names: Levesque (University
             of Toronto), Davis (New York University), Morgenstern (SAIC), "The
             Winograd Schema Challenge," Proc. KR 2012, pp. 552-561. Author-hosted
             full text (official listing: aaai.org/papers/59-4492-...). Owns the
             WSC design intent and definition.
Establishes: What a Winograd schema is, why it was designed to resist statistical
             shortcuts ("Google-proof"), how the challenge was meant to be scored,
             and how small the original collection was.
Paraphrase:  A Winograd schema is a pair of sentences differing in one or two
             words, with a pronoun whose referent flips with that word, resolvable
             only by world knowledge; the collection was designed so the answer is
             obvious to a person but not findable by selectional restrictions or
             corpus statistics. The paper reports a collection of "more than 100"
             schemas and proposes 50-question tests; it reports no machine scores.
Locators:    Abstract + §4 (definition, four features); §6 Pitfall 1 (selectional
             restrictions), Pitfall 2; §7 ("more than 100 examples" at WS.html; 50
             questions / 500 words); §8 (three summary constraints); §10.2.
Quote:       "A Winograd schema is a pair of sentences that differ only in one or
             two words and that contain a referential ambiguity that is resolved
             in opposite directions in the two sentences."
```

```text
URL:         https://arxiv.org/abs/2002.04108
Kind:        primary. The dedicated AFLITE paper (Le Bras, Swayamdipta,
             Bhagavatula, Zellers, Peters, Sabharwal, Choi; AI2 / UW), ICML 2020.
             Owns the general theory and cross-dataset evidence for AFLITE.
Establishes: AFLITE as a model-based, bottom-up filter approximating an
             intractable optimum (AFOPT); that filtering makes benchmarks much
             harder for models while humans stay high; and the explicit limitation
             that filtering can also remove genuinely easy items.
Paraphrase:  AFLITE removes instances a model's own representation (RoBERTa
             embeddings) can predict, so "hardness" is defined relative to that
             representation. On SNLI, BERT falls from 92.0% to 63.5% after AFLITE;
             human accuracy on the filtered set also drops somewhat, and the
             authors warn this may reflect removal of genuinely easy examples, a
             limitation of any model-based bias reduction.
Locators:    Abstract; §1 (SNLI 92%->62% headline); §2 (formalization, AFOPT);
             §4 Table 3 (SNLI/MultiNLI drops); §4 text on the human-drop limitation
             ("removal of examples with spurious correlations could inadvertently
             lead to removal of genuinely easy examples").
Quote:       "removal of examples with spurious correlations could inadvertently
             lead to removal of genuinely easy examples; this might be a limitation
             of a model-based bias reduction approach such as AFLITE."
```

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary (model report). Brown et al. 2020, "Language Models are
             Few-Shot Learners" (GPT-3), OpenAI. Owns GPT-3's WinoGrande figures.
Establishes: A firsthand model-card WinoGrande number and, importantly, a
             firsthand acknowledgment of possible test-set contamination.
Paraphrase:  GPT-3 175B scores 70.2% (zero-shot), 73.2% (one-shot), and 77.7%
             (few-shot) on WinoGrande-XL, against a cited fine-tuned SOTA of 84.6%
             (T5) and a cited human figure of 94.0%. The paper flags "potential
             contamination of the Winograd test set" and cites the WSC to
             Levesque, Davis, Morgenstern 2012 [LDM12].
Locators:    §3.4 "Winograd-Style Tasks"; Table 3.5; Figure 3.5 (scaling).
Quote:       "See Section 4 for details on potential contamination of the Winograd
             test set."
```

```text
URL:         https://arxiv.org/abs/2307.09288
Kind:        primary (model report). Touvron et al. 2023, "Llama 2," Meta. Owns
             Llama 2's WinoGrande figure.
Establishes: A current-era model-card WinoGrande number, again with a contamination
             analysis in the same report.
Paraphrase:  Llama 2 70B (base) scores 80.2% on WinoGrande in the per-task
             appendix breakdown; the main table folds WinoGrande into an averaged
             "Commonsense Reasoning" group. The paper states it analysed potential
             data contamination (Section A.6).
Locators:    §2.3 + footnote listing WinoGrande among commonsense tasks; Table 3
             (grouped); appendix per-benchmark table (70B WinoGrande = 80.2);
             "We also analysed the potential data contamination ... Section A.6."
```

```text
URL:         https://arxiv.org/abs/1811.01778
Kind:        primary. Trichelair, Emami, Trischler, Suleman, Cheung, Diaz 2018,
             "On the Evaluation of Common-Sense Reasoning in NLU." Owns the
             word-association proportion of the original WSC.
Establishes: The firsthand figure WinoGrande cites for residual bias in the
             original WSC.
Paraphrase:  13.5% of WSC273 instances are "associative" (answerable from simple
             candidate-to-context word association, i.e. not Google-proof); the
             authors also count 131 "switchable" instances used to test whether
             models rely on such statistics.
Locators:    Table 1 ("Assoc. ... 13.5%"); §Associativity (131 switchable).
```

```text
URL:         https://arxiv.org/abs/2103.13009
Kind:        primary. Lourie, Le Bras, Bhagavatula, Choi 2021, "UNICORN on
             RAINBOW," AAAI 2021. Owns UNICORN's reported WinoGrande result.
Establishes: The firsthand-verifiable near-human WinoGrande score from the system
             that topped the leaderboard.
Paraphrase:  UNICORN (multitask T5-11B) reports new state of the art on WinoGrande
             at 86.6%, roughly 7 points under the 94% human figure, achieved by
             multitask transfer rather than any WinoGrande-specific reasoning
             advance.
Locators:    Abstract + "SOTA on RAINBOW" section (WINOGRANDE 86.6%); §
             experimental setup (WinoGrande handled via a learning curve).
```

```text
URL:         https://arxiv.org/abs/2201.02387
Kind:        dual role. Kocijan (Kumo.ai), Davis (NYU), Lukasiewicz (TU Wien /
             Oxford), Marcus (Robust AI), Morgenstern (PARC), "The Defeat of the
             Winograd Schema Challenge," Artificial Intelligence (2023). Primary
             for the WSC's design intent and its "defeat" (Davis and Morgenstern
             are original WSC authors, with stake); secondary/expert analysis for
             its critique of WinoGrande (they are outside WinoGrande's team).
Establishes: That near-human WSC scores were reached without the reasoning the
             test targeted; the 2016 competition and its outcome; the residual
             artifacts remaining after filtering; and a pointed critique of
             WinoGrande's construction.
Paraphrase:  By 2019 transformer systems passed 90% on WSC273 while, in the
             authors' judgment, not acquiring commonsense reasoning; the sole WSC
             competition (IJCAI-16) drew six systems whose best scored 58% on 60
             PDPs and no better than chance on unseen items. The authors argue
             WinoGrande's crowdsourced schemas "are often flawed and do not come
             close to meeting Levesque's guidelines," many being solvable by word
             correlation, and report a WinoGrande leaderboard entry (UNICORN) at
             91.2%. They quote Elazar et al. (2021): perceived progress reflects
             lax evaluation, residual dataset artifacts, and knowledge leakage
             from large training data.
Locators:    §1 + Table 1 (timeline); §3.1 (IJCAI-16, 58%); §4 (Elazar three
             explanations); §5 (proxy-problem lessons); Appendix A.6 (WinoGrande
             critique, UNICORN 91.2%, twin-fraction dispute); Table A.2 (human
             baselines).
Quote:       "Solving Winograd schemas is not a surrogate for the ability to do
             commonsense reasoning, let alone for intelligence."
```

## Contradictions

- **Does the score track reasoning or the construction of the filtered set?**
  This is the contradiction the editor will push on, and the sources split
  cleanly. WinoGrande's authors frame AFLITE as removing "spurious" bias so the
  remaining score reflects reasoning. But AFLITE defines "easy" relative to one
  model family's embeddings (RoBERTa), and the AFLITE paper's own authors concede
  filtering can strip "genuinely easy examples" and that the filtered set is
  "somewhat harder even for humans." So part of the low machine score is a
  property of the filter's target representation and the training budget, not of
  reasoning demand. The WinoGrande learning curve (Table 4) makes the same point
  from the other side: identical filtered items yield 50.4% at 160 training
  examples and 79.1% at 40,938, so the "difficulty" is a function of how much
  training the scorer is granted.

- **How small was the original WSC, and who owns "273"?** The KR-2012 paper
  itself describes only a collection of "more than 100" schemas and never states
  273. The "273" is the later standardized WSC273 test set (used at IJCAI-16 and
  quoted in WinoGrande's Table 5 as "WSC 273"). The piece should attribute 273 to
  the standardized set, not to the 2012 paper.

- **Citation year of the WSC.** WinoGrande cites "Levesque, Davis, and
  Morgenstern 2011" (the AAAI Spring Symposium precursor, single-authored by
  Levesque). The canonical three-author paper the commission names is KR-2012.
  GPT-3 cites it correctly as 2012 [LDM12]. Both versions exist and read almost
  identically; the commissioned source is the 2012 KR paper (read in full here).

- **Did AFLITE actually strip the surface cues?** WinoGrande claims a clean
  debiased set (KL-divergence 2.53 -> 0.12). The Defeat paper (two original WSC
  authors) counters that many released WinoGrande items remain solvable by word
  correlation and "are not actually Winograd schemas," giving concrete examples
  (e.g. "anxiety"/"nerves" more associated than "bipolar"/"nerves"). Elazar et
  al., quoted therein, attribute residual progress partly to "artifacts ... that
  remain despite efforts to remove them." This complicates, but does not
  undermine, the commissioned angle: it sharpens the lesson that the number is a
  property of an imperfect construction rather than a clean reasoning meter.

- **What fraction of the debiased set are twins?** WinoGrande states "about 1/3
  of questions are not twins" in WinoGrandedebiased. The Defeat authors' own
  count puts it at 56% (their footnote 17; their main text says "slightly more
  than 1/2"). A direct numeric disagreement about the released set.

- **Near-human WinoGrande score: 86.6% or 91.2%?** UNICORN's own paper reports
  86.6%; the Defeat paper reports a UNICORN leaderboard entry at 91.2%. I could
  not reconcile these against the now-offline AI2 leaderboard. Use 86.6% as the
  firsthand-verifiable figure and cite 91.2% as leaderboard-reported if the piece
  needs the closest-to-human point, with the source named.

- **The 118K extrapolation.** WinoGrande says reaching the 94% human level "would
  need over 118K training instances," but its stated log fit
  (y = 4.8463 ln(x) + 26.215) yields only ~83% at 118K. Report the paper's claim
  as its own extrapolation; do not present the arithmetic as sound.

## Numbers

```text
Figure: 273 problems (original WSC, WSC273 standardized set)
Owner:  the standardized WSC273 test set; quoted in WinoGrande Table 5 ("WSC 273")
Scope:  full expert-authored test collection; the KR-2012 paper itself reports
        only "more than 100" schemas in its own collection
```

```text
Figure: 43,972 problems (WinoGrande all); 12,282 (WinoGrande debiased)
Owner:  WinoGrande paper (§3, Table 5)
Scope:  all = 40,938 train + 1,267 dev + 1,767 test (all twins); debiased =
        9,248 train + 1,267 dev + 1,767 test (about a third not twins per authors)
```

```text
Figure: 77k questions collected (38k twins) -> 53k validated (68%)
Owner:  WinoGrande paper (§2 crowdsourcing / data validation)
Scope:  raw crowdsourced pool before AFLITE; 6k used to fine-tune RoBERTa_embed,
        47k embedded and filtered, final debiased 12,282, 31k filtered-out released
```

```text
Figure: Human performance 94.0% (test), 94.1% (dev)
Owner:  WinoGrande paper (§4.2, Table 3), majority vote of three crowd workers
Scope:  WinoGrande debiased test/dev set
```

```text
Figure: Best machine at publication RoBERTa 79.1% (test), 79.3% (dev)
Owner:  WinoGrande paper (Table 3)
Scope:  WinoGrande debiased; trained on full XL training set (40,938). Other
        baselines (test): WKH 49.6, EnsembleLMs 50.9, BERT 64.9, BERT-DPR 51.0,
        RoBERTa-DPR 58.9, BERT/RoBERTa local-context 51.9 / 50.0
```

```text
Figure: Learning curve by training size (RoBERTa, test acc)
Owner:  WinoGrande paper (Table 4)
Scope:  XS(160)=50.4, S(640)=58.6, M(2,558)=67.6, L(10,234)=74.7, XL(40,938)=79.1;
        same filtered items, so difficulty scales with training budget, not the set
```

```text
Figure: AFLITE parameters m=10,000, n=64, k=500, tau=0.75
Owner:  WinoGrande paper (§3, Algorithm 1)
Scope:  the specific settings used to produce WinoGrande debiased
```

```text
Figure: KL-divergence between answer-option distributions 2.53 -> 0.12
Owner:  WinoGrande paper (Figure 1)
Scope:  WinoGrande all (2.53) vs debiased (0.12); random-reduction 2.51, PMI 2.42
```

```text
Figure: SNLI drop 92.0% -> 63.5% (BERT) under AFLITE; MultiNLI RoBERTa 93.7 -> 77.7
Owner:  Le Bras et al. 2020 (Table 3)
Scope:  cross-dataset evidence that AFLITE hardens sets for models while human
        accuracy stays high (though it drops somewhat on the filtered set)
```

```text
Figure: 13.5% of WSC273 "associative" (word-association solvable)
Owner:  Trichelair et al. 2018 (Table 1)
Scope:  original WSC273; equals 37/273 (the Defeat paper rounds this to 13.6%)
```

```text
Figure: GPT-3 175B WinoGrande-XL 70.2 / 73.2 / 77.7 (zero/one/few-shot)
Owner:  Brown et al. 2020 (Table 3.5)
Scope:  vs fine-tuned SOTA 84.6 (T5) and cited human 94.0; contamination flagged
```

```text
Figure: Llama 2 70B WinoGrande 80.2%
Owner:  Touvron et al. 2023 (per-task appendix table)
Scope:  base model; contamination analysed in the same report (§A.6)
```

```text
Figure: UNICORN WinoGrande 86.6% (own paper) / 91.2% (leaderboard, per Defeat)
Owner:  Lourie et al. 2021 (86.6%); Kocijan et al. 2023 reporting the AI2
        leaderboard (91.2%)
Scope:  best transfer system vs 94% human; 91.2% unverified (leaderboard offline)
```

```text
Figure: IJCAI-16 WSC competition best 58% (6 systems, 60 PDPs)
Owner:  Kocijan et al. 2023 (§3.1, citing Davis et al. 2017)
Scope:  the sole running of the WSC as a competition; best system Liu et al. 2017
```

## Source assets

```text
Asset: WinoGrande Figure 1 (PCA scatter plots + 1-D histograms of RoBERTa
       embeddings for "all", random-12k, PMI-12k, and debiased-12k), with the
       KL-divergence printed on each panel (2.53 down to 0.12).
Shows: What AFLITE does, visually: the two answer-option clusters that a linear
       model can separate in the unfiltered set collapse into one after filtering.
Crop:  Keep the leftmost ("all", 2.53) and rightmost ("debiased", 0.12) panels and
       the blue/red option coloring; the middle baselines can be omitted. Retain
       the KL numbers; they carry the argument.
```

```text
Asset: WinoGrande Figure 2 (learning curve: dev accuracy vs number of training
       examples on a log x-axis, with the log-fit line y=4.8463 ln(x)+26.215).
Shows: The score is a function of training budget on a fixed filtered set: it
       climbs smoothly from ~50% to ~79% as data grows.
Crop:  Keep the log x-axis label and the plotted curve; if the piece redraws this
       as an honest chart, it must label the log scale and cite the paper.
```

```text
Asset: WinoGrande Tables 1 and 2 (twin-sentence examples with the trigger word
       marked, and Table 2's polarity-bias examples AFLITE removed).
Shows: What a Winograd schema is (one word flips the answer) and what a
       dataset-specific shortcut looks like (sentiment aligned with the answer).
Crop:  A two-row excerpt from Table 1 (trophy/suitcase) plus one Table 2 removed
       example is enough; do not reproduce whole tables.
```

```text
Asset: GPT-3 Figure 3.5 (zero/one/few-shot WinoGrande accuracy vs model size).
Shows: WinoGrande rising with scale and in-context examples, still short of human.
Crop:  Retain the human/SOTA reference line if the piece uses it; keep axis labels.
```

```text
Asset: Le Bras et al. 2020 Figure 1 (ImageNet butterfly/chickadee images retained
       vs removed by AFLITE).
Shows: Vivid intuition for "what a filter keeps vs discards," but it is a vision
       example, off this lesson's NLP spine.
Crop:  None recommended; note as available but likely a digression for this piece.
```

## Discarded

```text
URL: http://commonsensereasoning.org/2011/papers/Levesque.pdf — the 2011 AAAI
     Spring Symposium precursor (Levesque, sole author). Read in full only to
     confirm it is the earlier single-author version WinoGrande cites as "2011";
     not the commissioned KR-2012 paper, so not used for the origin's figures.
URL: https://cdn.aaai.org/ojs/19068/19068-13-22935-1-10-20211013.pdf — a 2-page
     AAAI OJS reprint stub of the WSC paper, not the full text; superseded by the
     complete KR-2012 PDF read here.
URL: https://leaderboard.allenai.org/winogrande/submissions/public — the AI2
     WinoGrande leaderboard, now offline (DNS does not resolve). Could not verify
     the UNICORN 91.2% entry firsthand; recorded via the Defeat paper instead.
```

## Access failures

The AI2 WinoGrande leaderboard (leaderboard.allenai.org) is offline, so the
closest-to-human leaderboard figure (UNICORN 91.2%) could not be confirmed against
its owning primary. The firsthand-verifiable UNICORN figure (86.6%, from the
UNICORN paper) is recorded in its place, with the 91.2% attributed to the Defeat
paper's report of the leaderboard. No other required source was inaccessible.
