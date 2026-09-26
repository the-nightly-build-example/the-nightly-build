# Commission: the-instruments/ndcg

## The measurement

Normalized Discounted Cumulative Gain, nDCG, and specifically nDCG@10 as the
headline number that sorts modern retrieval and text-embedding leaderboards
(MTEB, BEIR, TREC, MS MARCO). This desk teaches one measurement; this is it.

## The assignment

Explain where the number comes from, step by step, then show what it can and
cannot support, with at least one real case where it misled people and what
that cost.

1. What it measures. nDCG scores a ranked list of results against human
   relevance judgments. Build it up in order, teaching each term the moment it
   is needed:
   - relevance judgments (qrels), graded (e.g., 0-3) or binary;
   - gain, the credit a result earns for its relevance grade;
   - the position discount (the log-based penalty that makes a relevant result
     worth less the further down the list it sits);
   - DCG, the discounted gain summed down to a cutoff k;
   - the ideal DCG (IDCG), the DCG of the best possible ordering of the judged
     results;
   - nDCG = DCG / IDCG, which lands every query on a 0-to-1 scale so scores can
     be averaged across queries;
   - the cutoff @k (why leaderboards report @10).
   Carry this to a small worked example with real numbers: a short ranked list
   with graded labels, the DCG, the IDCG, and the resulting nDCG@k. The writer
   builds the arithmetic from the definitions in the record.
2. Who produces it and from what. A test collection (queries + human relevance
   labels), a system's ranked output, and a standard scorer (trec_eval /
   pytrec_eval). On MTEB/BEIR the reported retrieval number is nDCG@10.
3. What it can and cannot support. It is designed for graded relevance and for
   caring most about the top of the list. Its limits, each taught concretely:
   - it is only as good as its relevance labels: shallow or incomplete
     judgment pools bias it, and on a collection with roughly one judged
     relevant document per query nDCG@10 collapses toward a rank-of-first-hit
     measure;
   - the @10 cutoff is blind to everything below rank 10;
   - gain and discount are conventions, and the two common gain formulations
     (linear vs exponential) can produce different numbers for the same run, so
     an nDCG is only comparable to another computed the same way;
   - it is an offline proxy for user satisfaction.
4. The real case where it misled, and the cost. Use the documented finding that
   a wave of neural ranking/recommendation models reported as state-of-the-art
   on offline ranking metrics (nDCG among them) failed to beat well-tuned
   simple baselines once those baselines were tuned properly (the RecSys
   reproducibility work by Ferrari Dacrema, Cremonesi, Jannach). Say plainly
   what the misleading number cost: years of reported "progress" that did not
   replicate. If the record turns up an equally concrete IR case (e.g., the
   consequences of shallow judgment pools on TREC-style nDCG comparisons), the
   writer may use that instead or alongside, whichever the evidence supports
   best.

## The one thing this article does that the sources do not

Show the reader that an nDCG@10 is a compound of choices (which documents were
judged, on what grade scale, with which gain and discount, cut at which rank)
and that a single leaderboard number hides all of them, then demonstrate with a
documented case where the number moved without the underlying systems getting
better.

## Angle refinement (post-research, orchestrator decision)

The record met the source policy (10 sources, 9 primary) and constrains the
framing. Draft to these:

1. Keep the NARROW angle the commission wrote: a single nDCG@10 hides the choices
   behind it (which documents were judged, the grade scale, the gain convention,
   the discount convention, the cutoff) and can move without any system
   improving. Do NOT argue "nDCG is a bad metric." Two primaries defend it and
   must be respected: Sanderson et al. 2010 found nDCG the best of the tested
   measures at predicting user preference, and Wang et al. 2013 proved the
   standard log-discount nDCG still distinguishes substantially different rankers
   even as its raw value drifts toward 1.
2. Use BEIR's TREC-COVID "hole" experiment as the central "the number misled,
   here is the mechanism" case (it is cleaner and on nDCG's own turf): with the
   retrieval systems entirely unchanged, filling 980 missing relevance judgments
   lifted ANCE's nDCG@10 from 0.654 (below BM25) to 0.735 (above BM25) and moved
   ColBERT 5.8 points, while lexical docT5query barely moved (0.713 to 0.714).
   The number moved and the ranking flipped from labeling alone. The Ferrari
   Dacrema et al. reproducibility result can stand as a second, shorter example
   of offline-metric "progress" that did not replicate, but the BEIR hole case
   should carry the section.
3. There are TWO independent convention axes, not one: gain (linear, used by
   trec_eval and therefore MTEB/BEIR, vs exponential 2^rel-1, used in web-search
   / learning-to-rank) and discount (the original 2002 log with a base floor vs
   the modern log2(rank+1)). So a leaderboard nDCG@10 is not directly comparable
   to an industrial one. The record has two arithmetic-verified worked examples;
   use one to teach the construction and, if room allows, note the convention
   gap with the second.
4. The "nDCG@10 collapses toward a rank-of-first-hit measure on a collection with
   ~one judged relevant doc per query" is a derived consequence, not a direct
   quote from one primary. Present it as a consequence and cite Craswell et al.
   (MS MARCO sparsity) plus the definitions; do not attribute the exact reduction
   to a source that does not state it.

## Boundaries — do not re-teach taught ground

Link at first use; do not re-teach:
- the-instruments/mteb — nDCG@10 is MTEB's retrieval metric; that lesson
  already dissects MTEB's cross-task averaging. Do not repeat the averaging
  critique; this lesson is about the per-ranking metric itself.
- the-mechanics/retrieval — how embeddings and nearest-neighbor search return
  passages. Do not re-teach embeddings.
- the-instruments/mean-average-precision — a sibling ranking metric. Name the
  difference (MAP assumes binary relevance and averages precision; nDCG uses
  graded relevance and a position discount) and move on.
Assume algebra and probability. The log and the discount are arithmetic, not a
new concept to apologize for.

## Sources (the-instruments policy: min 8, primary >=4, secondary >=1)

Primary must include: Järvelin & Kekäläinen 2002, "Cumulated gain-based
evaluation of IR techniques" (ACM TOIS), the paper that defines DCG/nDCG; the
MTEB paper (Muennighoff et al. 2022) and/or BEIR (Thakur et al. 2021) for where
nDCG@10 is the number in circulation; the Ferrari Dacrema et al. RecSys 2019
paper (and/or its 2021 TOIS journal version) for the misleading-progress case.
A strong further primary: Wang et al. 2013, "A Theoretical Analysis of NDCG
Type Ranking Measures" (COLT), on when nDCG is and is not consistent. Cite each
figure to the document that owns it, at a real locator.

## Recent shapes to break (compare against the recent library)

- Do not default to the "You have probably ..." opener or the "By the end you
  will know A, B, and C" tricolon closer.
- Check the dek and headings against recent the-instruments pieces (mlperf,
  attack-success-rate, helm, calibration-error) so this one is built
  differently. Recent instruments deks pair a specific number with a reversal;
  find a different move if the number does not truly carry it.

## Production record

Profile balanced. Models "capable" for all roles. Effort targets: researcher
high, writer medium, editor high, writing-coach low. Roles run as isolated
subagents on a capable model (Claude Opus-class); per-role reasoning-effort is
not separately dialed in this harness (recorded deviation). No `required`
directive traded down.
