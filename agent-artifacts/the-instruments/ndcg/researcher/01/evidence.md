# Evidence: the-instruments/ndcg (01)

The primary documents support the commission's angle firmly and, in one place,
more than the commission expected. The full construction of nDCG@k, term by
term, comes verbatim from Järvelin & Kekäläinen 2002, with the paper's own
worked vectors reproduced below and a second clean worked instance in the modern
`trec_eval` convention that I computed and checked. Two independent convention
choices are documented from primaries, not one: linear gain (Järvelin &
Kekäläinen) versus exponential gain 2^rel−1 (Burges 2010), and, separately, the
discount changed between the 2002 original (divide by log_b of the rank, with no
discount above rank 1 until the base) and the modern standard (divide by
log2(rank+1)). MTEB and BEIR both state in their own words that nDCG@10 is the
main retrieval metric and that MTEB reuses BEIR, computed with the official TREC
tool. The "number moved without the systems improving" case is supported twice:
the Ferrari Dacrema recommender reproducibility work (exact counts below), and,
more directly on the article's own subject, BEIR's own TREC-COVID experiment in
which filling judgment holes lifted an unchanged dense retriever from below BM25
to 6.7 nDCG@10 points above it. The counter-case is real and recorded: Sanderson
et al. 2010 found nDCG the best-correlated of the measures they tested against
user preference, and Wang et al. 2013 proved the standard log-discount nDCG can
still tell substantially different rankers apart even though its raw value drifts
to 1. Where the record is thin: the "collapses to rank-of-first-hit" claim for a
one-relevant-per-query collection is a derivation I did from the definitions plus
the documented sparsity of MS MARCO, not a single primary that states the
reduction in those words.

## Sources

```text
URL:         https://dl.acm.org/doi/10.1145/582415.582418
Kind:        primary. The paper that defines CG, DCG, and nDCG; the authors own
             the definitions the whole article rests on. (ACM DL page is the
             document's home and is gated to a 403; I read the full text from the
             open mirror https://faculty.cc.gatech.edu/~zha/CS8803WST/dcg.pdf)
Establishes: The exact term-by-term construction of cumulated gain, the
             discounted variant, the log discount, the ideal vector, and
             normalization to it. Uses graded relevance 0-3 (linear gain: the
             grade is the gain).
Paraphrase:  Relevance scores 0 to 3 are placed at each rank to turn a result
             list into a gain vector. CG is the running sum of gains. DCG divides
             each gain by the log (base b) of its rank before adding it, so a
             relevant document deep in the list contributes less; no discount is
             applied at rank 1 (log_b 1 = 0) or at ranks below the base. The
             ideal vector is the judged documents sorted by grade, high to low,
             out to the recall base. nDCG divides the DCG vector by the ideal DCG
             vector component by component, so 1 is ideal and [0,1) is the share
             of ideal reached.
Locators:    ACM TOIS Vol. 20, No. 4, October 2002, pp. 422-446. Sec. 2.1
             (Cumulated Gain, Eq. 1, pp. 424-425); Sec. 2.2 (Discounted Cumulated
             Gain, Eq. 2, pp. 425-426); Sec. 2.3 (Normalized (D)CG, Eq. 5,
             pp. 426-427).
Quote:       "Assume that the relevance scores 0 to 3 are used (3 denoting high
             value, 0 no value)." — p. 424.
             "DCG[i] = CG[i], if i < b; DCG[i-1] + G[i]/(b log i), if i >= b" —
             Eq. 2, p. 425 ("b log i" is log base b of rank i).
             "the normalized value 1 represents ideal performance, and values in
             the range [0, 1) the share of ideal performance cumulated by each
             technique" — p. 426.
```

```text
URL:         https://www.microsoft.com/en-us/research/publication/from-ranknet-to-lambdarank-to-lambdamart-an-overview/
Kind:        primary. States the exponential-gain DCG convention firsthand; the
             report defines the metric it optimizes. (Read from the MSR PDF at
             .../uploads/2016/02/MSR-TR-2010-82.pdf)
Establishes: The second gain convention in wide use: gain = 2^rel − 1, discount
             1/log(1+i). Five relevance levels {0,1,2,3,4}. Confirms nDCG = DCG /
             maxDCG in [0,1] and the @T=10 cutoff example.
Paraphrase:  Burges defines DCG at truncation T as the sum over the top T results
             of (2^{l_i} − 1) / log(1 + i), with l_i the label of the i-th URL,
             and gives T = 10 as the "first page" example; NDCG divides by the
             maximum attainable DCG@T for that query.
Locators:    Christopher J.C. Burges, "From RankNet to LambdaRank to LambdaMART:
             An Overview," Microsoft Research Technical Report MSR-TR-2010-82,
             2010. Sec. 2 (Information Retrieval Measures), Eq. 5.
Quote:       "DCG@T ≡ sum_{i=1}^{T} (2^{l_i} − 1)/log(1 + i)" — Eq. 5.
             "We typically use five levels of relevance: l_i ∈ {0, 1, 2, 3, 4}."
```

```text
URL:         https://arxiv.org/abs/1304.6480
Kind:        primary. The theoretical result on nDCG consistency; the authors own
             the theorems.
Establishes: (a) Standard nDCG with a logarithmic discount converges to 1 as the
             number of items grows, for any ranking function; (b) despite that,
             log-discount nDCG has "consistent distinguishability" and can decide
             which of two substantially different rankers is better on almost all
             datasets; (c) whether nDCG keeps this property depends on how fast
             the discount decays, with r^{-1} the critical point. This both
             tempers and defends the angle, so it is quoted precisely to avoid
             overstatement.
Paraphrase:  The raw normalized value is not meaningful in isolation for large
             collections, since it tends to 1 regardless of ranker; the log
             discount is nonetheless a good enough choice that the measure still
             ranks substantially different systems consistently. A poorly chosen
             discount (decaying too slowly, past the r^{-1} threshold) loses even
             that.
Locators:    Yining Wang, Liwei Wang, Yuanzhi Li, Di He, Tie-Yan Liu, Wei Chen,
             "A Theoretical Analysis of NDCG Type Ranking Measures," COLT 2013
             (arXiv:1304.6480, Apr 2013). Abstract; Sec. 1 (Introduction).
Quote:       "the standard NDCG which adopts a logarithmic discount, converges to
             1 as the number of items to rank goes to infinity."
             "For every pair of substantially different ranking functions, the
             ranking measure can decide which one is better in a consistent
             manner on almost all datasets."
             "whether NDCG has consistent distinguishability depends on how fast
             the discount decays, and r−1 is a critical point." — all Abstract.
```

```text
URL:         https://arxiv.org/abs/2210.07316
Kind:        primary. States firsthand that nDCG@10 is MTEB's main retrieval
             metric. (Read from the arXiv PDF; quotes verbatim from extracted
             text.)
Establishes: nDCG@10 is the headline number for the retrieval task on the MTEB
             leaderboard, and MTEB does not build its own retrieval judgments: it
             reuses BEIR's datasets and evaluation.
Paraphrase:  For retrieval, MTEB scores each dataset with nDCG@k, MRR@k,
             precision@k and recall@k for several k, and reports nDCG@10 as the
             main metric; the datasets and their qrels come from BEIR.
Locators:    Niklas Muennighoff, Nouamane Tazi, Loïc Magne, Nils Reimers, "MTEB:
             Massive Text Embedding Benchmark," 2022 (arXiv:2210.07316; EACL
             2023). Sec. 3.2 (Tasks and Evaluation), "Retrieval" paragraph.
Quote:       "nDCG@10 serves as the main metric. MTEB reuses datasets and
             evaluation from BEIR (Thakur et al., 2021)." — Sec. 3.2.
```

```text
URL:         https://arxiv.org/abs/2104.08663
Kind:        primary. States firsthand nDCG@10 as BEIR's single reported metric,
             its reasoning, the qrels structure, and BEIR's own judgment-hole
             experiment. (Read from the arXiv PDF; quotes verbatim.)
Establishes: (a) Why BEIR picked nDCG@10 over Precision/Recall (rank-unaware) and
             MRR/MAP (fail on graded judgments); computed with the official TREC
             tool (trec_eval, linear gain). (b) Most BEIR datasets have binary
             qrels, a few graded; average relevant-docs-per-query ranges from
             under 2 to ~500. (c) The TREC-COVID hole study: unchanged systems,
             re-judged pool, and nDCG@10 moved enough to flip the ranking.
Paraphrase:  Precision and Recall are rank-unaware; MRR and MAP cannot use graded
             labels; nDCG@k handles both, so BEIR computes nDCG@10 for every
             dataset with trec_eval. Some datasets have fewer than two relevant
             documents per query. In TREC-COVID, dense retrievers left many top-10
             hits unjudged (holes): TAS-B 31.8%, ANCE 14.4%, versus BM25 6.4% and
             docT5query 2.8%. After BEIR manually judged 980 missing pairs and
             recomputed, docT5query barely moved (0.713 to 0.714) while ANCE rose
             from 0.654 (below BM25) to 0.735, 6.7 points above BM25, and ColBERT
             gained 5.8 points. No retrieval system changed; only the labels did.
Locators:    Nandan Thakur, Nils Reimers, Andreas Rücklé, Abhishek Srivastava,
             Iryna Gurevych, "BEIR: A Heterogeneous Benchmark for Zero-shot
             Evaluation of Information Retrieval Models," NeurIPS 2021 Datasets &
             Benchmarks (arXiv:2104.08663). Sec. 3 and Table 1 (qrels, Avg. D/Q);
             Sec. 3.3 (Evaluation Metric); Sec. 4 hole analysis and Table 4
             ("Hole@10 analysis on TREC-COVID").
Quote:       "Binary rank-aware metrics such as MRR ... and MAP ... fail to
             evaluate tasks with graded relevance judgements. We find that
             Normalised Cumulative Discount Gain (nDCG@k) provides a good balance
             suitable for both tasks involving binary and graded relevance
             judgements. ... we utilize the Python interface of the official TREC
             evaluation tool ... and compute nDCG@10 for all datasets." — Sec. 3.3
             "Some datasets contain few relevant documents for a query (< 2)" —
             Sec. 3.
             "for the dense retrieval system ANCE, the performance improves from
             0.654 (slightly below BM25) to 0.735, which is 6.7 points above the
             BM25 performance." — Sec. 4.
```

```text
URL:         https://arxiv.org/abs/2003.07820
Kind:        primary. The track organizers document MS MARCO's sparse labels and
             their own dense NIST judgments, and name nDCG@10 the main metric.
             (Read from arXiv PDF; quotes verbatim.)
Establishes: MS MARCO's training/dev labels are sparse, often one relevant per
             query; TREC built dense, four-point (0-3) NIST judgments for the test
             topics; the main metric on the dense judgments is nDCG@10, chosen
             because it uses the four-level grades and weights the top.
Paraphrase:  The large MS MARCO-derived training labels have no negatives and
             often a single positive per query. NIST pooled and additionally
             judged (including for queries with many relevant) on a 0-3 scale to
             get comprehensive labels. The track's main metric is nDCG@10.
Locators:    Nick Craswell, Bhaskar Mitra, Emine Yilmaz, Daniel Campos, Ellen M.
             Voorhees, "Overview of the TREC 2019 Deep Learning Track," 2019/2020
             (arXiv:2003.07820). Sec. 2.1-2.2 (four-point judging scale); Sec. 3
             (Datasets, sparse labels); "Overall results" (main metric).
Quote:       "These are sparse, with no negative labels and often only one
             positive label per query, analogous to some real-world training data
             such as click logs." — Sec. 3.
             "Our main metric in both tasks is Normalized Discounted Cumulative
             Gain (NDCG)—specifically, NDCG@10, since it makes use of our 4-level
             judgments and focuses on the first results that users will see." —
             Overall results.
```

```text
URL:         https://arxiv.org/abs/1907.06902
Kind:        primary. The reproducibility study; the authors own the counts and
             the conclusion. (ACM DOI 10.1145/3298689.3347058 is the published
             home and is gated to 403; the arXiv version is the same paper, read
             in full.)
Establishes: The "misleading offline number" case in recommendation. Exact
             counts, the metrics involved (nDCG among them), the simple baselines,
             and the authors' own statement about phantom progress.
Paraphrase:  From 18 neural top-n recommendation papers at four top venues
             (2015-2018), only 7 could be reproduced with reasonable effort; of
             those, 6 could often be beaten by simple heuristics (nearest-neighbor
             and graph-based), and the 7th beat those baselines but did not
             consistently beat a well-tuned non-neural linear model. Results are
             reported with hit rate, Precision, Recall, MAP, MRR and NDCG at
             several cutoffs (NDCG@5, @10, @20, @50, @100 appear in the tables).
             Baselines: TopPopular, ItemKNN and content/hybrid variants, P3-alpha,
             RP3-beta.
Locators:    Maurizio Ferrari Dacrema, Paolo Cremonesi, Dietmar Jannach, "Are We
             Really Making Much Progress? A Worrying Analysis of Recent Neural
             Recommendation Approaches," RecSys 2019 (Best Paper). Abstract;
             Sec. 2.1 and Table 1 (reproducibility, 7/18); Sec. 3 (baselines);
             Sec. 4 (results, metrics).
Quote:       "we considered 18 algorithms ... Only 7 of them could be reproduced
             with reasonable effort. For these methods, it however turned out that
             6 of them can often be outperformed with comparably simple heuristic
             methods ... The remaining one clearly outperformed the baselines but
             did not consistently outperform a well-tuned non-neural linear
             ranking method." — Abstract.
             "Hit rate and NDCG are the performance [measures]" — Sec. 4.
```

```text
URL:         https://arxiv.org/abs/1911.07698
Kind:        primary. The extended journal version, with a larger, harder count.
             (ACM DOI 10.1145/3434185; arXiv version read for the abstract counts.)
Establishes: The scaled-up figure the writer may prefer: 12 reproducible neural
             methods examined, 11 beaten by conceptually simple methods, none
             consistently better than existing matrix-factorization or linear
             models.
Paraphrase:  Extends the RecSys 2019 analysis; 11 of 12 reproducible neural
             collaborative-filtering methods are outperformed by simple methods
             such as nearest-neighbor heuristics, and no complex neural method was
             consistently better than established learning-based techniques.
Locators:    Maurizio Ferrari Dacrema, Simone Boglio, Paolo Cremonesi, Dietmar
             Jannach, "A Troubling Analysis of Reproducibility and Progress in
             Recommender Systems Research," ACM TOIS Vol. 39, No. 2, Article 20,
             January 2021 (arXiv:1911.07698). Abstract.
Quote:       "11 out of the 12 reproducible neural approaches can be outperformed
             by conceptually simple methods, e.g., based on the nearest-neighbor
             heuristics." — Abstract.
             "None of the computationally complex neural methods was actually
             consistently better than already existing learning-based
             techniques" — Abstract.
```

```text
URL:         https://dl.acm.org/doi/10.1145/1835449.1835542
Kind:        primary (counter-case). The authors gathered the user-preference data
             firsthand and computed the correlations. (ACM DL gated to 403; read
             in full from the open copy
             http://www.ccs.neu.edu/home/ekanou/research/papers/mypapers/sigir10d.pdf)
Establishes: The strongest defense of nDCG in the record: of nDCG, MRR and P(10),
             nDCG agreed with crowd user preferences most often, significantly so.
             Also the limit on that defense.
Paraphrase:  Crowd workers were shown pairs of rankings and asked which they
             preferred. nDCG matched the preferred system in 63% of applicable
             pairs (160 of 252), MRR in 53% (127 of 241), P(10) in 50% (106 of
             214); a t-test found nDCG significantly more in agreement than the
             other two, which did not differ from each other. The caveat: user
             agreement was much stronger when one system returned no relevant
             documents than when both returned some, so part of nDCG's edge comes
             from the easy zero-relevant case, and even at its best nDCG matched
             users only about two times in three.
Locators:    Mark Sanderson, Monica Lestari Paramita, Paul Clough, Evangelos
             Kanoulas, "Do user preferences and evaluation measures line up?"
             SIGIR 2010, pp. 555-562. Sec. 4.2 and Table 4 (traditional measures);
             Sec. 6 (Conclusions).
Quote:       "nDCG was significantly more in agreement with user preferences than
             the other two measures. There was no significant difference between
             MRR and P(10)." — Sec. 4.2.
             "user preferences between pairs of systems where one had failed to
             retrieve any relevant documents were notably stronger than when both
             rankings had at least one relevant document" — Sec. 6.
```

```text
URL:         https://en.wikipedia.org/wiki/Discounted_cumulative_gain
Kind:        secondary. A widely-read reference that reports, from outside the
             authoring parties, that the two gain conventions coexist and where
             each is used; used only to corroborate the convention split and its
             industrial spread, not as the origin of any claim.
Establishes: That the linear and exponential DCG forms are both standard, that the
             exponential form dominates industry and Kaggle, and that they
             coincide only for binary relevance.
Paraphrase:  The article gives DCG = sum rel_i/log2(i+1) and the alternative
             (2^rel_i − 1)/log2(i+1), states the exponential form is common in
             industrial applications and on Kaggle, notes the two agree only when
             relevance is binary, and defines nDCG = DCG/IDCG.
Locators:    "Discounted cumulative gain," Wikipedia, sections "Discounted
             Cumulative Gain" and "Normalized DCG" (retrieved 2026-09-26).
Quote:       "The latter formula is commonly used in industrial applications
             including major web search companies and data science competition
             platforms such as Kaggle." (as rendered)
             "These two formulations of DCG are the same when the relevance values
             of documents are binary." (as rendered)
```

## Contradictions

- Against the angle (nDCG is arbitrary / weakly tied to users): Sanderson et al.
  2010 found nDCG the best of the three tested measures at predicting real user
  preference, significantly better than MRR and P(10). The article must not imply
  nDCG is a poor measure. The honest framing is narrower: a single nDCG@10 number
  hides the choices that produced it and can move without systems improving, which
  is compatible with nDCG being the best available ranking metric. The same paper
  also limits its own defense: nDCG matched users only ~63% of the time, and its
  advantage leaned on the case where one system returned nothing relevant.

- Against the "raw number is uninformative" reading: Wang et al. 2013 proves the
  standard log-discount nDCG still distinguishes substantially different rankers
  consistently, even though its value tends to 1 as the collection grows. Do not
  say nDCG "cannot tell systems apart." Say the absolute value is not meaningful
  in isolation and that the discount is a load-bearing choice (past the r^{-1}
  decay threshold the property fails).

- On whether the reproducibility critique was itself contested: I searched for
  published rebuttals to Ferrari Dacrema et al. and found none of substance. The
  RecSys 2019 paper won Best Paper, the authors extended it to a TOIS 2021 journal
  version with a larger count (11 of 12), and follow-on work (e.g., Rendle et al.
  on baseline tuning) reinforced rather than rebutted it. This weakens, not
  strengthens, any counter to the angle: the misleading-number finding stands
  largely unchallenged. Record this as a searched-for absence, not a claim that no
  criticism could exist.

- Internal to the sources, on the gain convention: MTEB/BEIR compute nDCG with
  trec_eval, which uses linear gain (the grade is the gain, Järvelin & Kekäläinen
  style), while Burges 2010 and much web-search/LTR/Kaggle practice use
  exponential gain 2^rel−1. A leaderboard nDCG@10 and an industrial nDCG@10 are
  therefore not directly comparable. There is also a second, quieter split: the
  2002 original discounts by log_b(rank) with no discount before the base rank,
  whereas the modern standard (trec_eval, Burges) discounts by log2(rank+1). Both
  are called "the log discount." State which convention any cited number uses.

## Numbers

```text
Figure: relevance grades 0-3 (0 = no value, 3 = high value)
Owner:  Järvelin & Kekäläinen 2002, p. 424
Scope:  the graded-relevance scale used throughout the defining paper's examples
```

```text
Figure: DCG discount = divide gain by log_b(rank); no discount at rank 1, none
        below the base rank
Owner:  Järvelin & Kekäläinen 2002, Eq. 2, p. 425
Scope:  original 2002 definition; b is the log base (they test b=2 and b=10)
```

```text
Figure: modern standard DCG = sum (gain)/log2(rank+1); exponential gain = 2^rel-1
Owner:  Burges 2010, Eq. 5 (exponential gain + log2(1+i) discount); trec_eval
        implements linear gain with the same discount
Scope:  the convention behind MTEB/BEIR (linear gain) and web-search/LTR/Kaggle
        (exponential gain)
```

```text
Worked example A — from the primary, verbatim (Järvelin & Kekäläinen 2002, b=2):
  Gain vector      G0  = <3, 2, 3, 0, 0, 1, 2, 2, 3, 0, ...>
  Cumulated gain   CG0 = <3, 5, 8, 8, 8, 9, 11, 13, 16, 16, ...>
  Discounted       DCG0 = <3, 5, 6.89, 6.89, 6.89, 7.28, 7.99, 8.66, 9.61, 9.61, ...>
  Ideal gain       I0  = <3, 3, 3, 2, 2, 2, 1, 1, 1, 1, 0, ...>
  Ideal DCG        DCG_I0 = <3, 6, 7.89, 8.89, 9.75, 10.52, 10.88, 11.21, 11.53, 11.83, ...>
  nDCG = DCG0 / DCG_I0 componentwise (e.g. at rank 3: 6.89/7.89 = 0.87)
Owner:  Järvelin & Kekäläinen 2002, Secs. 2.1-2.3, pp. 424-427
Scope:  original log_b(rank) discount; illustrates CG, DCG, ideal, normalization
```

```text
Worked example B — modern trec_eval convention, computed and checked by me:
  Ranked grades (system) : [3, 2, 3, 0, 1, 2]   (6 results, cut at k=6)
  Ideal order            : [3, 3, 2, 2, 1, 0]
  LINEAR gain (grade = gain), discount 1/log2(rank+1):
    DCG@6  = 3/1 + 2/1.585 + 3/2 + 0 + 1/2.585 + 2/2.807 = 6.861
    IDCG@6 = 3/1 + 3/1.585 + 2/2 + 2/2.322 + 1/2.585 + 0 = 7.141
    nDCG@6 = 6.861 / 7.141 = 0.961
  EXPONENTIAL gain (2^grade - 1), same ranking, same discount:
    gains [7,3,7,0,1,3], ideal [7,7,3,3,1,0]
    DCG@6 = 13.848, IDCG@6 = 14.595, nDCG@6 = 0.949
Owner:  construction follows Järvelin & Kekäläinen (linear) and Burges 2010
        (exponential); arithmetic verified with Python
Scope:  same ranking, two conventions, two numbers (0.961 vs 0.949) — the
        "only comparable if computed the same way" point, on one example
```

```text
Derivation — the shallow-pool collapse (one binary relevant per query):
  With exactly one judged relevant document (grade 1) and k=10, IDCG@10 = 1
  (the relevant doc at rank 1), so nDCG@10 = 1/log2(1 + rank_of_the_hit) if the
  hit is in the top 10, else 0. Values: rank 1 -> 1.000, rank 2 -> 0.631,
  rank 3 -> 0.500, rank 5 -> 0.387, rank 10 -> 0.289, below 10 -> 0. The score is
  a strictly decreasing function of the rank of the single hit: a discounted
  reciprocal rank, i.e. a rank-of-first-hit measure.
Owner:  derivation from the definitions above; sparsity fact owned by Craswell et
        al. 2019 ("often only one positive label per query") and BEIR ("< 2"
        relevant for some datasets)
Scope:  a consequence of the definition plus documented MS MARCO sparsity, not a
        verbatim claim from one primary (see Limits)
```

```text
Figure: TREC-COVID nDCG@10, systems unchanged, judgment holes filled
Owner:  BEIR (Thakur et al. 2021), Sec. 4 / Table 4
Scope:  ANCE 0.654 (below BM25) -> 0.735 (6.7 pts above BM25) after judging 980
        missing pairs; docT5query 0.713 -> 0.714; ColBERT +5.8 pts. Hole@10:
        BM25 6.4%, docT5query 2.8%, ANCE 14.4%, TAS-B 31.8%.
```

```text
Figure: recommender reproducibility counts
Owner:  Ferrari Dacrema et al. 2019 (RecSys) and 2021 (TOIS)
Scope:  2019: 18 examined, 7 reproducible, 6 of 7 beaten by simple heuristics;
        2021: 11 of 12 reproducible neural methods beaten by simple methods
```

## Limits

- The exact phrase "nDCG@10 collapses to a rank-of-first-hit measure" is my
  derivation from the definitions plus the documented one-relevant-per-query
  sparsity of MS MARCO, not a single primary that states the reduction in those
  words. The math is exact and checked; the writer should present it as a
  consequence, and may cite Craswell et al. (sparsity) and the definitions, not a
  source that names the collapse.
- MS MARCO's public leaderboard uses MRR@10 on its sparse dev set, not nDCG. The
  clean illustration that sparse labels degrade nDCG lives in the TREC Deep
  Learning track (which added dense NIST labels precisely to use nDCG@10) and in
  BEIR's TREC-COVID hole study. The article should not claim the MS MARCO
  leaderboard itself reports a degraded nDCG.
- I did not locate a primary stating the specific fraction of MS MARCO dev queries
  with exactly one relevant passage (secondary sources say >94% and ~1.1 on
  average). Craswell et al. support "often only one positive label per query"
  firsthand; use that wording, not a precise percentage, unless the writer finds
  the MS MARCO paper's own figure.
- MTEB and BEIR metric statements are quoted from the arXiv PDFs' extracted text,
  which I confirmed line by line; the ACM/NeurIPS pagination is not reproduced, so
  locators are by section, not page.
- Everything else the commission asked for is established: the term-by-term
  construction, why normalization matters, both gain conventions with a worked
  numeric difference, the shallow-pool problem, the offline-vs-online / phantom-
  progress case, and the counter-case.

## Source assets

```text
Asset: Järvelin & Kekäläinen 2002, the worked vectors G0, CG0, DCG0, ideal I0 and
       ideal DCG (Secs. 2.1-2.3, pp. 424-427)
Shows: the whole construction on one running example, in the definers' own numbers
Crop:  keep the gain row, the discounted row, and the ideal row aligned by rank; a
       reader must see gain, then discount, then normalization against the ideal
```

```text
Asset: BEIR Table 4, "Hole@10 analysis on TREC-COVID" (Sec. 4)
Shows: unchanged retrieval systems whose nDCG@10 ranking flips after judgment
       holes are filled; the single clearest on-subject "the number moved, the
       system did not" table in the record
Crop:  must retain the before/after nDCG@10 columns and the Hole@10 column for at
       least BM25, docT5query, ANCE and TAS-B, so the reader sees the holes and
       the score change together; omit rows that dilute the ANCE-vs-BM25 flip
```

```text
Asset: BEIR Table 1 (dataset statistics), the "Relevancy" and "Avg. D/Q" columns
Shows: that most datasets are binary-judged and that relevant-docs-per-query runs
       from under 2 to ~500, i.e. the pool depth the metric silently depends on
Crop:  keep dataset name, Relevancy (binary/graded), and Avg. D/Q; drop corpus
       size and other columns
```

```text
Asset: Ferrari Dacrema et al. 2019 results tables (Sec. 4), the HR@k / NDCG@k
       columns comparing a neural method against ItemKNN / P3-alpha / RP3-beta
Shows: simple baselines matching or beating the neural method on NDCG
Crop:  keep the baseline rows beside the neural row and the NDCG@10 column; a crop
       must not drop the baseline that wins
```

```text
Asset: worked example A/B above (no figure in a source owns example B)
Shows: same ranking, linear vs exponential gain, two nDCG numbers
Crop:  a small table of six ranks with grade, linear term, exponential term is
       enough; none needed from a source
```

## Discarded

```text
URL: https://futureagi.com/blog/what-is-mrr-map-ndcg-2026/ — vendor blog, no
     primary standing; only restated definitions available elsewhere.
URL: https://towardsdatascience.com/... NDCG "ultimate ranking metric" — secondary
     explainer, adds nothing the Wikipedia entry or the primaries do not own.
URL: https://zeroentropy.dev/concepts/ms-marco/ — useful phrasing on the one-
     relevant collapse but secondary and unsourced; the claim is better carried by
     the derivation plus Craswell et al.
URL: https://ir-datasets.com/msmarco-passage.html — dataset catalog, corroborates
     sparsity but is a tertiary listing, not the owner of the judgment figures.
URL: https://scispace.com/... and researchgate/academia mirrors of the cited
     primaries — used only to locate the papers; the primaries themselves are
     cited at their own homes.
```
