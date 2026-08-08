# Evidence record: the-evidence/word2vec (01)

The two word2vec papers were read firsthand for every figure the angle rests on,
and the numbers are solid: the analogy benchmark is exactly 19,544 questions
(8,869 semantic + 10,675 syntactic, 14 categories), the best word-analogy
accuracy is 65.6% (Skip-gram, 1000-dim, 6B words) in the first paper and 61%
(Skip-gram NEG-15 + subsampling, 300-dim, ~1B words) in the companion, and
"king - man + woman = queen" is a labeled example whose recovery is that measured
accuracy, not a parameter-free identity. The critique side is equally firm: Levy
& Goldberg (2014) prove the arithmetic is a balancing of three cosine
similarities and reproduce the "regularities" in plain sparse count vectors, and
Linzen (2016) shows the literal arithmetic returns one of the three input words
98% of the time unless they are excluded by hand, and that a baseline ignoring
the offset entirely (nearest neighbor of the third word) captures much of the
score. The evidence therefore strongly supports the commissioned angle: the
analogy result is real but weaker and more method-dependent than the folklore.
It is thin in only one place: exact per-cell numbers in the first paper's
architecture-comparison tables were read through ar5iv rendering rather than a
native-typeset PDF, so the low-config accuracies (Tables 2-4 of 1301.3781)
should be treated as read-carefully-but-verify; the headline numbers below were
cross-checked and are safe. One commission figure needs correction (the "6B
Google News" corpus belongs to the first paper, not the companion; see
Contradictions).

## Sources

```text
URL:         https://arxiv.org/abs/1301.3781
Kind:        primary — the document itself; Mikolov et al. own every claim about
             what this model is and what it scored. Full text read via
             https://ar5iv.labs.arxiv.org/abs/1301.3781
Establishes: CBOW and Skip-gram architectures and objectives; the
             Semantic-Syntactic Word Relationship test set (19,544 questions);
             the king-man+woman example; accuracy, dimensionality, corpus, and
             training-time numbers.
Paraphrase:  Proposes two shallow log-linear models. CBOW predicts the current
             word from the average of its surrounding context words (order
             ignored). Skip-gram does the reverse: it predicts the surrounding
             context words from the current word. Both drop the hidden layer of
             earlier neural language models, which is what makes them cheap. The
             quality test is a new analogy set the authors built; the striking
             finding is that vector('King') - vector('Man') + vector('Woman')
             lands closest to vector('Queen'), and this holds well enough across
             the set to report as an accuracy.
Locators:    Abstract; Sec. 1-4; Fig. 1 (architectures); Sec. 4.1 (test set
             description, "8869 semantic and 10675 syntactic questions"); Tables
             2-6 (accuracies); Sec. 5 (training time). Affiliation on p.1.
Quote:       "vector('King') - vector('Man') + vector('Woman') results in a
             vector that is closest to the vector representation of the word
             Queen." / "Overall, there are 8869 semantic and 10675 syntactic
             questions." / Affiliation: "Google Inc., Mountain View, CA".
```

```text
URL:         https://arxiv.org/abs/1310.4546
Kind:        primary — the companion document; owns negative sampling,
             subsampling, the phrase model, and its own accuracy numbers.
             Published as NIPS (NeurIPS) 2013, pp. 3111-3119. Full text read via
             https://ar5iv.labs.arxiv.org/abs/1310.4546
Establishes: The Skip-gram training objective; negative sampling as a cheap
             replacement for the full softmax; hierarchical softmax; subsampling
             of frequent words; the phrase extension; word-analogy and
             phrase-analogy accuracies; corpus and dimensionality.
Paraphrase:  Extends Skip-gram three ways. Negative sampling trains each example
             against a handful of randomly drawn "negative" words instead of
             scoring the whole vocabulary (k = 5-20 for small data, 2-5 for
             large). Subsampling randomly drops very frequent words (threshold
             t ~ 1e-5). Phrases like "Air Canada" get their own vectors because
             the meaning does not compose from "Air" and "Canada." Vector
             addition also composes: vec('Russia') + vec('river') is near
             vec('Volga River'). Reports 61% on the word-analogy set and 72% on a
             separate phrase-analogy set.
Locators:    Abstract; Sec. 2 (Eq. 1 Skip-gram objective, Eq. 4 negative
             sampling); Sec. 2.1 (hierarchical softmax); Sec. 2.3 (Eq. 5
             subsampling); Table 1 (word-analogy accuracy); Sec. 5 (phrase
             analogy, 72%); Fig. 2 (country-capital PCA projection).
Quote:       "Values of k in the range 5-20 are useful for small training
             datasets, while for large datasets the k can be as small as 2-5." /
             "vec('Madrid') - vec('Spain') + vec('France') is closer to
             vec('Paris') than to any other word vector."
```

```text
URL:         https://aclanthology.org/W14-1618/
Kind:        primary — Levy & Goldberg own this analysis and its results; it is
             not reporting on the critique from outside, it is the critique.
             Full text (PDF) read in full.
Establishes: That the vector-offset method (3CosAdd) is mathematically a sum of
             three pairwise cosine similarities; that Mikolov's solver excludes
             the three input words and normalizes vectors to unit length; that
             the same "regularities" appear in traditional sparse count-based
             (PPMI) vectors, so the embedding process preserves rather than
             invents them; that a multiplicative objective (3CosMul) does better.
Paraphrase:  Solving "a is to a* as b is to ?" by taking argmax cos(x, b - a + a*)
             over the vocabulary (with a, a*, b excluded) is, once vectors are
             unit-normalized, identical to argmax [cos(x,b) - cos(x,a) +
             cos(x,a*)] — find a word similar to b and a* but unlike a. Because
             this is a linear sum, one large term can dominate ("soft-or"), which
             is why London:England::Baghdad returns Mosul, not Iraq, under
             3CosAdd. The regularities are not special to neural nets: sparse
             PPMI vectors recover a comparable amount.
Locators:    Authors/affiliation p.171 (Bar-Ilan University, Ramat-Gan, Israel;
             CoNLL 2014, pp.171-180, marked Best Paper on the authors' record);
             Sec. 3.2-3.3 (Eq. 1 and Eq. 3, the decomposition, "normalized to
             unit length"); Sec. 3.2 ("V ... excluding the question words b, a
             and a*"); Sec. 5 Table 1 and Sec. 7 Table 3 (accuracies); Sec. 6
             (3CosMul, London/Baghdad worked example); Sec. 11 (discussion).
Quote:       "solving analogy questions with vector arithmetic is mathematically
             equivalent to seeking a word (b*) which is similar to b and a* but
             is different from a." / "the neural embedding process is not
             discovering novel patterns, but rather is doing a remarkable job at
             preserving the patterns inherent in the word-context co-occurrence
             matrix."
```

```text
URL:         https://aclanthology.org/W16-2503/
Kind:        primary — Linzen owns this experiment and its numbers; it is the
             critique, not a report of one. Full text (PDF) read in full.
Establishes: That the literal offset method returns one of the three input words
             almost always unless they are excluded by hand; that baselines
             ignoring the offset ("only-b", "ignore-a") already score highly, so
             the offset's true added value is modest and category-dependent;
             that reversing the analogy direction changes accuracy even though
             the same offset is involved; conclusion that the method conflates
             offset consistency with neighborhood structure.
Paraphrase:  Run without excluding a, a*, b, the nearest word to a* - a + b is
             just b 93% of the time and a* 5% of the time — 98% an input word.
             Excluding them is a hand-built heuristic. Even then, a baseline that
             ignores the offset and returns the nearest neighbor of b captures
             much of the score (0.70 on plurals); the offset method beats
             "only-b" by only ~0.33-0.42 overall depending on the space.
             Reversing direction drops accuracy (mean -0.11), and that drop
             tracks the baseline's drop (r = 0.72), showing the offset is not
             doing the work the story claims.
Locators:    Author/affiliation p.13 (Tal Linzen, LSCP & IJN, Ecole Normale
             Superieure, PSL Research University; RepEval 2016, pp.13-18); Sec. 2
             (Eq. 2 offset method, Eq. 4-8 baselines, exclusion of a/a*/b);
             Sec. 4 (VANILLA 93%/5% result; Table 2 ADD vs baselines; reversal
             r=0.72; US cities .69->.17); Sec. 5 and footnote 1 (interpretation).
Quote:       "When these words were not excluded, the nearest neighbor of
             a* - a + b was b in 93% of the cases and a* in 5% of the cases (it
             was never a)." / "the offset method when applied to the Mikolov et
             al. (2013a) sets jointly evaluates the consistency of the offsets
             and the probability that b* is the nearest neighbor of b."
```

```text
URL:         https://papers.nips.cc/paper/2013/hash/9aa42b31882ec039965f3c4923ce901b-Abstract.html
Kind:        secondary — the publisher's bibliographic record; confirms venue and
             author list for the companion paper but does not itself own the
             research claims.
Establishes: That "Distributed Representations of Words and Phrases and their
             Compositionality" is the NeurIPS (NIPS) 2013 publication, authored
             by Mikolov, Sutskever, Chen, Corrado, and Dean.
Paraphrase:  Confirms the companion paper's canonical venue (Advances in Neural
             Information Processing Systems 26, 2013) and the five-author byline
             used when the piece cites the paper's home.
Locators:    NeurIPS 2013 proceedings page, title and author block.
Quote:       (none load-bearing)
```

```text
URL:         https://nlp.stanford.edu/pubs/glove.pdf
Kind:        secondary (in this record's use) — GloVe is a primary document for
             its own claims, but here it is context for "what followed" word2vec,
             not a source for what word2vec did.
Establishes: That within a year a competing method (GloVe, Pennington, Socher &
             Manning, Stanford, EMNLP 2014) targeted the same analogy benchmark
             and positioned itself against window-based prediction models like
             word2vec, evidence that the analogy set became the field's shared
             yardstick and that word2vec was quickly built past.
Paraphrase:  GloVe factorizes a global word-word co-occurrence matrix rather than
             predicting from local windows, and reports competitive-to-better
             results on the same Google analogy task, framing word2vec's
             window-prediction approach as the prior art it improves on.
Locators:    Title/authors/affiliation p.1; abstract and Sec. 1 (positioning vs
             prediction models); analogy-task evaluation section.
Quote:       (fetched via author-hosted PDF; canonical page
             https://aclanthology.org/D14-1162/)
```

## Contradictions

- Corpus misattribution in the commission. The commission text says to report
  "the 6B-word Google News set for the companion." The 6B-token Google News
  corpus (vocabulary capped at the 1 million most frequent words) belongs to the
  FIRST paper, 1301.3781. The companion's word-analogy results (Table 1, 61%)
  were trained on an internal ~1 billion-word news dataset at 300 dimensions; its
  best PHRASE-analogy model (72%) used ~33 billion words at 1000 dimensions. The
  writer should not attribute "6B Google News" to the companion.

- Two different analogy tests get one number in the folklore. The 19,544-question
  Google set (word analogies) and the phrase-analogy set are separate. Best word
  accuracy is 65.6% (paper 1) / 61% (paper 2); the 72% figure is the phrase set
  only. Keep them distinct.

- Category-count phrasing differs across the primaries. Paper 1 states "8869
  semantic and 10675 syntactic questions" and its Table 1 defines 5 semantic
  categories + 9 syntactic categories (14 total). Levy & Goldberg describe the
  same set as "7 ... semantic ... and 7 ... morpho-syntactic." Linzen lists all
  14 categories individually. The total (19,544) and the semantic/syntactic
  question counts are the paper's own; the "5+9 vs 7+7" grouping is a labeling
  difference, not a disagreement about the set. Levy & Goldberg also drop 286
  out-of-vocabulary items, evaluating on 19,258.

- Does the arithmetic "really do analogies"? The primaries genuinely disagree in
  emphasis, and this is the steelman the commission wants. Mikolov et al. present
  the offsets as the space "naturally" encoding relations. Levy & Goldberg agree
  the regularities are real and robust (they survive in plain count vectors) but
  reframe the mechanism as similarity-balancing, not relation-application. Linzen
  goes furthest: the literal method mostly returns an input word, exclusion of
  inputs is a hand-built crutch, and an offset-free baseline captures much of the
  remaining score. The honest synthesis: the regularities exist and reproduce,
  but "vector arithmetic does analogies" overstates how much the offset itself
  contributes. This SUPPORTS the commissioned angle; it does not undermine it.

## Numbers

```text
Figure: 19,544 analogy questions total (8,869 semantic + 10,675 syntactic), 14 categories
Owner:  Mikolov et al. 2013, arXiv:1301.3781, Sec. 4.1
Scope:  The Semantic-Syntactic Word Relationship test set (the "Google analogy set")
```

```text
Figure: 65.6% total (66.1% semantic, 65.1% syntactic) — best word-analogy accuracy in paper 1
Owner:  arXiv:1301.3781, Table 6
Scope:  Skip-gram, 1000-dim vectors, 6B-word Google News corpus, distributed training
```

```text
Figure: Skip-gram 55% semantic / 59% syntactic; CBOW 24% / 64% — architecture comparison
Owner:  arXiv:1301.3781, Table 3
Scope:  320M-word training subset, 640-dim vectors (read via ar5iv; verify against PDF)
```

```text
Figure: 61% total (61% semantic, 61% syntactic) — best word-analogy accuracy in paper 2
Owner:  arXiv:1310.4546, Table 1
Scope:  Skip-gram, NEG-15 with 1e-5 subsampling, 300-dim, ~1B-word internal news dataset
```

```text
Figure: Word-analogy accuracy by method (300-dim, ~1B words): NEG-5 59%, NEG-15 61%,
        HS-Huffman 47%, NCE-5 53%; with 1e-5 subsampling NEG-5 60%, NEG-15 61%, HS 55%
Owner:  arXiv:1310.4546, Table 1
Scope:  Same corpus/dimensionality; "Time [min]" column shows 14-97 min training
```

```text
Figure: 72% — best phrase-analogy accuracy
Owner:  arXiv:1310.4546, Sec. 5
Scope:  Hierarchical softmax, 1000-dim, ~33B words (separate phrase test set, not the 19,544)
```

```text
Figure: <1 day to train on 1.6B words; CBOW ~1 day and Skip-gram ~3 days on Google News subset;
        optimized single machine >100B words/day (companion)
Owner:  1301.3781 (abstract, Sec. 5) and 1310.4546 (Sec. 3)
Scope:  Training-cost claims; the selling point vs earlier neural language models
```

```text
Figure: Vocabulary capped at 1,000,000 most frequent words (30k in limited experiments)
Owner:  arXiv:1301.3781; companion filters to 692K words (min 5 occurrences)
Scope:  Google News 6B corpus (paper 1); internal news corpus (paper 2)
```

```text
Figure: 3CosAdd accuracy on Google set — neural embedding 62.70%, sparse PPMI 45.05%;
        3CosMul — embedding 66.72%, PPMI 68.24%
Owner:  Levy & Goldberg 2014, Tables 1 and 3
Scope:  600-dim skip-gram (NEG-15, 1e-5) vs explicit PPMI vectors, 1.5B-token Wikipedia,
        vocab 189,533; shows the sparse baseline matches or beats the embedding under 3CosMul
```

```text
Figure: Literal offset returns b 93% / a* 5% (98% an input word) when a, a*, b not excluded
Owner:  Linzen 2016, Sec. 4
Scope:  Skip-gram-NS spaces on ukWaC + 2013 Wikipedia; the case for exclusion being a crutch
```

```text
Figure: ADD overall .53/.60/.58 across spaces s2/s5/s10; ADD advantage over "only-b" baseline
        only .42/.36/.33; over "ignore-a" .41/.29/.26; "only-b" reaches .70 on plurals
Owner:  Linzen 2016, Table 2 and Sec. 4
Scope:  How little the offset itself adds beyond nearest-neighbor structure
```

```text
Figure: Reversing analogy direction: mean accuracy change -0.11; correlates with baseline
        change r=0.72; US cities .69 -> .17 on reversal
Owner:  Linzen 2016, Sec. 4
Scope:  Evidence the offset is not direction-consistent as the story implies
```

## Source assets

```text
Asset: Figure 1 in arXiv:1301.3781 — the CBOW and Skip-gram architecture diagram
Shows: The two models side by side: CBOW pulls context in to predict the center
       word; Skip-gram pushes the center word out to predict context. The whole
       "predict-the-neighbors" idea in one picture.
Crop:  Keep both panels and their INPUT/PROJECTION/OUTPUT labels; a one-panel crop
       loses the contrast that is the point.
```

```text
Asset: Figure 2 in arXiv:1310.4546 — 2-D PCA projection of country and capital vectors
Shows: Countries and their capitals arranged so the country->capital offset is
       roughly the same direction and length across pairs — the geometric picture
       behind "vector arithmetic recovers relations," learned with no supervision.
Crop:  Retain enough labeled country-capital pairs to see the parallel offsets;
       do not crop to a single pair.
```

```text
Asset: Table 1 in arXiv:1310.4546 — word-analogy accuracy by training method
Shows: The real numbers behind the folklore: 47-61% depending on method, with
       training times of 14-97 minutes. Good for a small accuracy table in the piece.
Crop:  Keep the method, total-accuracy, and time columns; the semantic/syntactic
       split is optional.
```

```text
Asset: Table 3 (and Table 1) in Levy & Goldberg 2014 — 3CosAdd vs 3CosMul,
       neural embedding vs sparse PPMI on MSR and Google
Shows: The sparse count-based baseline matching or beating the neural embedding
       (Google: 68.24% explicit vs 66.72% embedding under 3CosMul) — the visual
       proof that the regularities are not a neural-network magic trick.
Crop:  Keep both representation rows and both objectives so the comparison reads.
```

```text
Asset: Figure 4 in Linzen 2016 — accuracy of all analogy functions (incl. the
       offset-free baselines) per category on space s5
Shows: How close the "only-b" and "ignore-a" baselines run to the real offset
       method in many categories, and how wildly performance varies by category.
Crop:  Keep the ADD, MULTIPLY, ONLY-B, and IGNORE-A columns; the category labels
       must stay legible.
```

## Discarded

```text
URL: https://levyomer.wordpress.com/2014/04/25/linguistic-regularities-in-sparse-and-explicit-word-representations/ — author's blog post about his own paper; a secondary retelling of a primary already read. Used the paper instead.
URL: https://www.researchgate.net/publication/301408902_... — ResearchGate mirror of Levy & Goldberg; a re-hosting, not the document's own page. Used the ACL Anthology PDF instead.
URL: https://www.aclweb.org/aclwiki/Google_analogy_test_set_(State_of_the_art) — community leaderboard wiki; useful orientation but no owned claim, and superseded by the primaries for every figure the angle needs.
URL: arXiv abstract pages (both papers) as a source for author affiliation — the abs pages omit affiliations; resolved "Google Inc., Mountain View, CA" from the paper body via ar5iv full text instead.
```
