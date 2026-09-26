# researcher brief: the-instruments/ndcg (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/agent-artifacts/the-instruments/ndcg/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/agent-artifacts/the-instruments/ndcg/commission.md

Output:
- /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/agent-artifacts/the-instruments/ndcg/researcher/01/evidence.md

Work from these inputs. Read the primary documents, not coverage of them. Where
something you need is missing, ask me.

Source policy (the-instruments): at least 8 sources, at least 4 primary, at
least 1 secondary. Meet counts with sources that change the interpretation.

## Documents to read in full

1. Järvelin & Kekäläinen 2002, "Cumulated Gain-Based Evaluation of IR
   Techniques," ACM TOIS 20(4). The definitional primary. Capture: the exact
   definitions of gain, cumulated gain, the discounted variant, the log-based
   discount, and normalization to the ideal. Record the exact formulas and the
   locators. Note the gain formulations the paper uses.
2. The exponential-gain formulation of DCG (gain = 2^rel - 1), and where it
   comes from (commonly traced to Burges et al. 2005 "Learning to Rank using
   Gradient Descent" and the LETOR/Yahoo Learning-to-Rank materials). Establish,
   from a primary that states it, that two gain conventions are in use and give
   different numbers for the same ranking. Record the exact definition and
   source.
3. Wang, Wang, Li, He, Liu 2013, "A Theoretical Analysis of NDCG Type Ranking
   Measures" (COLT / arXiv:1304.6480). Capture its actual result about when
   nDCG is (in)consistent, precisely enough that the article does not overstate
   it.
4. MTEB (Muennighoff, Tazi, Magne, Reimers 2022, arXiv:2210.07316) and/or BEIR
   (Thakur, Reimers, Rücklé, Srivastava, Gurevych 2021, arXiv:2104.08663).
   Confirm and locate the statement that nDCG@10 is the primary retrieval
   metric these benchmarks report, and how the judgments/qrels are sourced.
5. Ferrari Dacrema, Cremonesi, Jannach 2019, "Are We Really Making Much
   Progress? A Worrying Analysis of Recent Neural Recommendation Approaches"
   (RecSys 2019), and its extended journal version (Ferrari Dacrema et al.,
   ACM TOIS 2021). Capture: how many of the examined neural methods failed to
   beat properly tuned simple baselines, which offline ranking metrics were
   involved (nDCG among them), and the authors' own statement of what this
   implies about reported progress. This is the "the number misled people, and
   here is the cost" case; get the exact counts and wording.

## Questions the record must answer

- The exact construction of nDCG@k, term by term, with a small concrete numeric
  illustration the writer can reuse (a short ranked list with graded labels; the
  DCG, IDCG, and nDCG). Supply the definitions and one clean worked instance
  from or consistent with the primary; do not invent labels the primary would
  reject.
- Why normalization matters (queries with different numbers of relevant docs).
- The two gain conventions and that a score is only comparable to another
  computed the same way.
- The shallow-pool / sparse-judgment problem: on a collection with about one
  judged relevant passage per query (e.g., MS MARCO), what nDCG@10 effectively
  reduces to, and who has documented this.
- The offline-vs-online gap: the documented case that offline ranking-metric
  gains did not reflect real improvement.

## Look for what breaks the angle

The angle is that a single nDCG@10 hides many choices and can move without
systems improving. Search for the counter-case: defenses of nDCG as robust and
well-correlated with user satisfaction, and any evidence that the
reproducibility critique was itself contested or answered. Record it in full.

## Source assets

Identify any figure or table worth showing (for example a small qrels/ranking
table, or a results table from the reproducibility paper). Give its location and
what a crop must retain. Do not prescribe crop coordinates.

Classify each source primary/secondary by authorship and stake. Record exact
author names, venues, and years as the documents state them.
