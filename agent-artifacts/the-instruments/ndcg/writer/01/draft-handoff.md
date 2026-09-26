# Draft handoff: the-instruments/ndcg (01)

## Original-work sentence

This article shows that a single leaderboard nDCG@10 is a compound of five
separable choices (which documents were judged, the grade scale, the gain
convention, the discount convention, and the rank cutoff), and it makes that
compound visible on the page by working one ranking to two different scores
under the two gain conventions (0.961 vs 0.949) and setting BEIR's TREC-COVID
re-judging beside it, where filling 980 judgment holes moved a dense retriever
from below BM25 to 6.7 points above it with no retrieval system changed.

That work is carried by three tables read in order: the by-hand worked
calculation (DCG 6.861 / IDCG 7.141 = 0.961), the same ranking under linear vs
exponential gain (0.961 vs 0.949), and TREC-COVID before/after (ANCE
0.654 to 0.735 while docT5query stays 0.713 to 0.714).

## Proof result

`nb check ... --series the-instruments` with links included: **BLOCK: 0,
WARN: 0**, verdict PUBLISHABLE. Stamp: words 2154, reading 9 min, sources 9
(8 primary, 1 secondary), inside the lesson band (1200-2200) and the
the-instruments source policy (min 8, primary >=4, secondary >=1).

No warnings left standing. Three W-SENTENCE-DENSITY notes on the first draft
(the why-bookend opener, the "takes it apart" list sentence, and the
shallow-pool worked sentence) were all fixed by splitting, not repunctuated.

The gated ACM homes for Jarvelin & Kekalainen (s3) and Sanderson (s8) return
403 to the probe; per `engine/nb/links.py` a 403 is "unverified" and never
blocks, and the brief permits gated pages at their resolving canonical address.
They are cited at their ACM DOI homes with full section/page locators. All
arXiv, MSR, Wikipedia and GitHub links resolve 200.

## Open questions

- **TREC-COVID table built from the record, not captured from BEIR Table 4.**
  The evidence Numbers block gives complete before/after nDCG@10 only for ANCE
  and docT5query (plus ColBERT's +5.8 delta and the four Hole@10 percentages);
  it does not state BM25's or TAS-B's before/after nDCG values. I therefore
  built the two-row nb-table from the figures the record owns and carried BM25
  and ColBERT in prose, rather than `nb asset`-capturing Table 4, which would
  put cell values on the page that the record does not supply. If a captured
  Table 4 crop is wanted, the record needs those additional cell values (or
  explicit clearance to read them off the BEIR PDF).

- **The "collapses to a rank-of-first-hit measure" claim** is presented as a
  derivation from the definitions plus documented sparsity, cited to Craswell
  (s6) for "often only one positive label per query," not attributed to a
  single primary that states the reduction. This follows the angle refinement;
  no new evidence requested.

- No voice questions. The voice guide's "state the wrong intuition, then the
  numbers that break it" move is used to open the construction section (the
  count-the-relevant-hits intuition, broken before the discount is named).
