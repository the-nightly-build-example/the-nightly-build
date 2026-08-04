# Evidence: the-mechanics/retrieval (researcher/01)

The evidence supports the commission's mechanism at every step, and sharpens two
of its claims. It is settled and directly sourced that a RAG system splits
documents into chunks, embeds each chunk as a vector, embeds the query the same
way, ranks chunks by embedding closeness, and returns the top-k via approximate
nearest-neighbor (ANN) search before the frozen model reads those chunks as
prompt tokens. Two of the commission's phrasings need care. First, "cosine
similarity" is the Sentence-BERT and common-production metric, but the RAG/DPR
lineage the commission cites ranks by raw **dot product** (inner product), not
cosine; cosine is dot product on length-normalized vectors, so the family is
right but the specific word is not universal. Second, the honesty note is
stronger than written: Lewis et al. 2020 did not jointly train the whole
retriever. They kept the document encoder and the document index **fixed**, and
fine-tuned only the query encoder and the generator. The concrete failure mode
is well sourced: an independent human audit of shipped citation systems found
only about half of generated sentences fully supported by their citations. What
the record cannot pin to a single owning paper is chunking strategy, which is an
unsettled heuristic precisely because no primary prescribes it. The evidence does
not undermine the commissioned angle; it tightens two lines the writer must not
overstate.

## Sources

```text
URL:         https://arxiv.org/abs/2005.11401
Kind:        primary — the paper that named and built RAG; the authors own the claim
Establishes: What "retrieval-augmented generation" originally denoted, and what
             was actually trained versus frozen.
Paraphrase:  Introduces RAG: a pre-trained seq2seq generator (parametric memory)
             combined with a dense vector index of Wikipedia (non-parametric
             memory) accessed by a pre-trained neural retriever. The retriever is
             DPR, a bi-encoder. The top-k documents are the k with highest prior
             p(z|x), computed as a Maximum Inner Product Search (MIPS) solved
             approximately in sub-linear time. During fine-tuning the document
             encoder BERT_d and the document index are kept fixed; only the query
             encoder BERT_q and the BART generator are trained. Two formulations:
             RAG-Sequence (same retrieved passages for the whole output) and
             RAG-Token (different passages per token).
Locators:    Abstract; Section 2 (Methods) "Retriever: DPR" and the training
             paragraph; NeurIPS 2020.
Quote:       "Calculating top-k(p_eta(.|x)), the list of k documents z with
             highest prior probability p_eta(z|x), is a Maximum Inner Product
             Search (MIPS) problem, which can be approximately solved in
             sub-linear time." / "we ... keep the document encoder (and index)
             fixed, only fine-tuning the query encoder BERT_q and the BART
             generator."
```

```text
URL:         https://arxiv.org/abs/2004.04906
Kind:        primary — introduces Dense Passage Retrieval; authors own the method
Establishes: That passage relevance can be decided by dense-vector closeness
             alone, the exact similarity function, and the dense-vs-lexical gap.
Paraphrase:  A dual-encoder (question encoder E_Q, passage encoder E_P) learns
             embeddings so that relevance is their similarity. The similarity is
             the dot product, sim(q,p) = E_Q(q)^T E_P(p). Passages are encoded
             once, indexed with FAISS, and searched by inner product at query
             time. DPR beats a strong Lucene-BM25 baseline by 9-19 absolute
             points in top-20 retrieval accuracy across open-domain QA sets.
Locators:    Abstract; Section 3.1 (definition of sim); Section 3.3 / inference
             (FAISS index); Table 2 (Natural Questions test); EMNLP 2020.
Quote:       "sim(q,p) = E_Q(q)^T E_P(p)" — the paper defines relevance as the
             dot product of the two embeddings, not cosine.
```

```text
URL:         https://arxiv.org/abs/1908.10084
Kind:        primary — introduces Sentence-BERT; authors own the method
Establishes: The passage/sentence-embedding primary, and the source that does use
             cosine similarity; also why you precompute embeddings instead of
             re-running the model per pair.
Paraphrase:  BERT must see both sentences together, so comparing 10,000 sentences
             pairwise is ~50 million inferences (~65 hours). SBERT uses siamese/
             triplet training to produce a single fixed vector per sentence that
             can be compared with cosine similarity. Finding the most similar pair
             drops from ~65 hours to ~5 seconds. This is the design that makes a
             one-vector-per-chunk index (the thing an ANN library searches)
             possible.
Locators:    Abstract; EMNLP 2019.
Quote:       "derive semantically meaningful sentence embeddings that can be
             compared using cosine-similarity." / "This reduces the effort for
             finding the most similar pair from 65 hours with BERT / RoBERTa to
             about 5 seconds with SBERT."
```

```text
URL:         https://arxiv.org/abs/1603.09320
Kind:        primary — introduces HNSW; authors own the algorithm
Establishes: The ANN-search primary. Finding the closest vectors fast is settled
             engineering with a named, graph-based method.
Paraphrase:  Hierarchical Navigable Small World graphs do approximate K-nearest-
             neighbor search over a multi-layer proximity graph, searching from a
             coarse top layer down. The hierarchy gives logarithmic complexity
             scaling. Fully graph-based, no auxiliary search structure. This is
             the index type DPR uses on CPU and one of the two defaults (with
             FAISS) in shipped vector search.
Locators:    Abstract; final revision 2018 (arXiv 1603.09320); later in IEEE
             TPAMI. The arXiv abstract page is the source's own page.
Quote:       "Starting search from the upper layer together with utilizing the
             scale separation boosts the performance ... and allows a logarithmic
             complexity scaling."
```

```text
URL:         https://arxiv.org/abs/1702.08734
Kind:        primary — the FAISS paper; authors (FAIR) own the system
Establishes: The other ANN-search primary and the "settled at scale" evidence:
             billion-vector similarity search is a solved engineering problem.
Paraphrase:  A GPU design for similarity search whose k-selection runs at up to
             55% of theoretical peak, 8.5x faster than prior GPU state of the art.
             Builds an exact k-NN graph on 95M images in 35 minutes and connects 1
             billion vectors in under 12 hours on 4 GPUs. FAISS is the library DPR
             and RAG index with; the point for the lesson is that the top-k lookup
             is not where the difficulty lives.
Locators:    Abstract; 2017 (arXiv 1702.08734).
Quote:       "a graph connecting 1 billion vectors in less than 12 hours on 4
             Maxwell Titan X GPUs."
```

```text
URL:         https://doi.org/10.1561/1500000019
Kind:        primary — Robertson & Zaragoza's own monograph on BM25/PRF
Establishes: The lexical baseline. BM25 is a bag-of-words scoring function, not an
             embedding method, and it is the thing dense retrieval is measured
             against and rerankers are bolted onto.
Paraphrase:  BM25 emerged from the Probabilistic Relevance Framework and scores a
             document by summing, over query terms, an IDF weight times a
             term-frequency term with saturation (parameter k1) and document-
             length normalization (parameter b). It matches on shared terms, so it
             answers a different question than embedding closeness: exact-term
             overlap, not semantic nearness. Described by its authors as "one of
             the most successful text-retrieval algorithms."
Locators:    Abstract and Section on BM25 term weighting; Foundations and Trends
             in Information Retrieval. Original pagination Vol. 3, No. 4 (2009),
             333-389; Emerald's re-host lists Vol. 4, Issue 1-2, pp. 1-174, 2009.
             DOI 10.1561/1500000019 resolves to the publisher's article page.
Quote:       "The Probabilistic Relevance Framework (PRF) is a formal framework for
             document retrieval ... which led to the development of one of the most
             successful text-retrieval algorithms, BM25."
```

```text
URL:         https://arxiv.org/abs/2104.08663
Kind:        primary — the BEIR benchmark; authors own the evaluation
Establishes: "Retrieval can miss." Dense retrievers trained in one setting do not
             reliably transfer to new domains, which is why keyword search and
             rerankers are kept in the stack.
Paraphrase:  BEIR evaluates 10 retrieval systems (lexical, sparse, dense, late-
             interaction, reranking) across 18 datasets in a zero-shot / out-of-
             distribution setting. BM25 is a robust baseline. Reranking and
             late-interaction models get the best average zero-shot scores but at
             high computational cost. Plain dense and sparse retrievers are
             cheaper but often underperform, showing real room to improve their
             generalization. This is the primary for "the embedding model decides
             relevant and can be wrong on unfamiliar text."
Locators:    Abstract; NeurIPS 2021 Datasets and Benchmarks Track.
Quote:       "our results show BM25 is a robust baseline and re-ranking and late-
             interaction-based models on average achieve the best zero-shot
             performances ... dense and sparse-retrieval models ... often
             underperform other approaches, highlighting the considerable room for
             improvement in their generalization capabilities."
```

```text
URL:         https://arxiv.org/abs/2304.09848
Kind:        primary — Liu, Zhang, Liang's own human-evaluation audit
Establishes: The concrete failure mode with a number: a citation attached to a
             sentence the cited source does not support.
Paraphrase:  A human evaluation of four shipped generative search engines (Bing
             Chat, NeevaAI, perplexity.ai, YouChat) across varied queries.
             Responses read fluent and informative but frequently contain
             unsupported statements and inaccurate citations. On average only
             51.5% of generated sentences are fully supported by their citations,
             and only 74.5% of citations actually support the sentence they are
             attached to. This is the "confident citation to a passage that does
             not support the claim," measured.
Locators:    Abstract; Findings of EMNLP 2023.
Quote:       "on average, a mere 51.5% of generated sentences are fully supported
             by citations and only 74.5% of citations support their associated
             sentence."
```

```text
URL:         https://arxiv.org/abs/2312.10997
Kind:        secondary — a survey; it reports on and organizes others' work rather
             than owning a method
Establishes: That "RAG" in shipped products now denotes a looser pipeline than the
             trained system Lewis et al. built, and gives the vocabulary for the
             open engineering choices.
Paraphrase:  Surveys RAG for LLMs and organizes it into three paradigms: Naive RAG
             (index, retrieve, stuff chunks into the prompt of a frozen model),
             Advanced RAG (adds pre- and post-retrieval steps), and Modular RAG.
             Frames RAG as a fix for hallucination, stale knowledge, and opaque
             reasoning. Useful for the honesty line (product RAG = embed, search,
             stuff, no joint training) and for locating chunking and reranking as
             tunable stages rather than settled ones. Use for framing only; take
             every load-bearing mechanism claim from the primaries above.
Locators:    Abstract; taxonomy section naming Naive/Advanced/Modular RAG; arXiv
             2312.10997 (2023, rev. 2024).
Quote:       Abstract names "the progression of RAG paradigms, encompassing the
             Naive RAG, the Advanced RAG, and the Modular RAG."
```

## Contradictions

- **Cosine similarity vs. dot product (settled family, unsettled word).** The
  commission and step 2 say relevance is decided by cosine similarity. The
  passage-embedding primary (Sentence-BERT) does use cosine. But the RAG/DPR
  lineage the commission builds on ranks by the raw dot product,
  sim(q,p) = E_Q(q)^T E_P(p), and RAG frames top-k as Maximum Inner Product
  Search. Cosine is the dot product after normalizing both vectors to unit
  length, so the underlying idea (closeness in embedding space) is identical, but
  "cosine similarity" is not the universal metric. Settled: relevance = geometric
  closeness of whole-passage embeddings. Not settled across systems: whether that
  closeness is cosine, dot product, or Euclidean. The writer should say closeness
  in embedding space and name cosine as the common default, not assert every
  system uses cosine.

- **What Lewis et al. trained (sharper than the honesty note).** The commission's
  honesty note says the RAG paper "trained the retriever and generator together."
  The paper is narrower: it keeps the document encoder and the document index
  fixed and fine-tunes only the query encoder and the generator. So even the
  original was not a fully joint retriever+generator train; the document side was
  frozen for cost reasons. This makes the gap to product RAG smaller in one
  respect (product RAG also freezes the document embeddings) and larger in
  another (product RAG usually trains nothing, using an off-the-shelf embedding
  model and a frozen chat model). Precise line: Lewis et al. trained the query
  encoder and generator together against a fixed index; shipped RAG typically
  trains neither.

- **Which step owns the bad-citation failure — genuinely unsettled.** Two
  candidate causes, and the evidence does not cleanly assign blame. Retrieval can
  return a plausible-but-wrong chunk: BEIR shows dense retrievers generalize
  poorly out of domain, so the top-k can simply be off. Or the model can ignore a
  correct chunk and generate from parametric memory: Liu et al. measure the
  outcome (only 51.5% of sentences fully supported) but audit end-to-end shipped
  systems, so their number blends both causes and cannot isolate one. Honest
  framing: the failure can originate at retrieval (wrong chunk retrieved) or at
  generation (right chunk ignored), the visible symptom is the same, and no cited
  source cleanly partitions the two.

- **Settled engineering vs. unsettled heuristic.** Settled and sourced: embedding
  a query and chunks and ranking by vector closeness (DPR, SBERT); returning
  top-k by ANN search (HNSW logarithmic scaling, FAISS at billion scale). These
  are not where the open questions live. Unsettled: chunking strategy has no
  owning primary that prescribes chunk size or boundaries — its absence from the
  primary record is itself the evidence that it is a heuristic, and the survey
  treats it as a tunable pre-retrieval stage. Reranking is a real lever, not a
  settled default: BEIR shows rerankers win on zero-shot quality but at high
  computational cost, so whether to pay for one is a tradeoff, not a solved
  choice. Whether the model uses what it retrieved is open: Liu et al. show it
  often does not (unsupported sentences, inaccurate citations).

## Numbers

```text
Figure: 78.4% top-20 / 85.4% top-100 (DPR) vs 59.1% / 73.7% (BM25)
Owner:  Karpukhin et al. 2020 (DPR), Table 2, test set
Scope:  Natural Questions, fraction of questions whose top-20 (top-100) retrieved
        passages contain the answer span. Shows dense retrieval beats lexical on
        in-domain QA — the counterweight to BEIR's out-of-domain result.
```

```text
Figure: 9-19 percentage points absolute, top-20 passage retrieval accuracy
Owner:  Karpukhin et al. 2020 (DPR), Abstract
Scope:  DPR over a strong Lucene-BM25 baseline, across a range of open-domain QA
        datasets. The headline dense-vs-lexical gap.
```

```text
Figure: sim(q,p) = E_Q(q)^T E_P(p) (dot product)
Owner:  Karpukhin et al. 2020 (DPR), Section 3.1
Scope:  The exact relevance function in the RAG/DPR lineage; not cosine.
```

```text
Figure: 51.5% of generated sentences fully supported by their citations;
        74.5% of citations support their associated sentence
Owner:  Liu, Zhang & Liang 2023, Abstract
Scope:  Human evaluation, average across four generative search engines (Bing
        Chat, NeevaAI, perplexity.ai, YouChat) over a diverse query set. The
        quantified failure mode.
```

```text
Figure: ~65 hours -> ~5 seconds to find the most similar pair; 10,000 sentences
        ~= 50 million BERT inferences
Owner:  Reimers & Gurevych 2019 (Sentence-BERT), Abstract
Scope:  Why one precomputed vector per chunk (searchable by ANN) replaces
        re-running the model on every pair. Makes the index feasible.
```

```text
Figure: 1 billion vectors indexed in under 12 hours on 4 GPUs; k-selection at up
        to 55% of theoretical peak; 8.5x faster than prior GPU state of the art
Owner:  Johnson, Douze & Jegou 2017 (FAISS), Abstract
Scope:  Billion-scale ANN. Evidence the top-k lookup is a solved engineering
        problem, not the seat of RAG's errors.
```

```text
Figure: logarithmic complexity scaling for search
Owner:  Malkov & Yashunin 2018 (HNSW), Abstract
Scope:  Approximate K-NN over a hierarchical proximity graph. The "fast" in
        "find the closest vectors fast."
```

```text
Figure: BM25 term-frequency saturation parameter k1; length-normalization
        parameter b
Owner:  Robertson & Zaragoza 2009, BM25 term-weighting section
Scope:  The lexical baseline's mechanism: term overlap with saturation and length
        normalization, a bag-of-words score, not an embedding.
```

## Source assets

```text
Asset: Karpukhin et al. 2020, Table 2 (top-20 / top-100 retrieval accuracy,
       DPR vs BM25, across open-domain QA datasets).
Shows: The dense-over-lexical gap in one grid; concrete for "embedding closeness
       finds the right passage better than keyword match, in domain."
Crop:  Keep the Natural Questions row and column headers and the BM25 vs DPR
       columns; a full multi-dataset crop is fine. Omit training-set-size ablation
       columns if present. Must retain that these are retrieval-accuracy percents,
       not end-QA scores.
```

```text
Asset: Lewis et al. 2020, Figure 1 (the RAG overview: query -> query encoder ->
       MIPS over document index -> top-k documents -> generator -> output).
Shows: The exact two-stage shape the lesson teaches: retrieve by inner product,
       then generate conditioned on retrieved text. Diagram-in-prose can follow it.
Crop:  Keep the query-encoder, MIPS/retriever, and generator boxes and the arrow
       from retrieved documents into the generator. The reader needs to see the
       retrieved passages entering the generator's input.
```

```text
Asset: Malkov & Yashunin 2018, Figure 1 (the hierarchical layered-graph
       illustration of HNSW search from top layer to bottom).
Shows: Why ANN search is fast — coarse-to-fine hops down the layers rather than
       scanning every vector.
Crop:  Keep the layered graph with the entry point at the top and the descent
       path. Decorative only if the lesson chooses to depict ANN; not required.
```

```text
Asset: Liu et al. 2023 — reported citation-precision / citation-recall figures
       (per-engine bars behind the 51.5% / 74.5% averages).
Shows: That the bad-citation failure is measured and common across shipped
       systems, not anecdotal.
Crop:  If a per-engine chart is used, retain axis labels (precision vs recall) and
       the engine names; must not imply a single system. The two average numbers
       alone carry the point if no clean chart crop exists.
```

For BM25 (Robertson & Zaragoza 2009), HNSW/FAISS text claims, Sentence-BERT, and
the RAG survey, no figure improves on prose for this lesson: None found.

## Discarded

```text
URL: https://www.nowpublishers.com/article/Details/INR-019 — the original
     publisher page for the BM25 monograph returned HTTP 403 to the fetcher and is
     not the most durable link. Replaced by the DOI (10.1561/1500000019), which
     resolves to the publisher's current article page. Not a rejection of the
     source, only of that URL.
```

```text
URL: https://www.staff.city.ac.uk/~sbrp622/papers/foundations_bm25_review.pdf —
     Robertson's own hosted copy of the BM25 monograph. Real and author-hosted,
     but the PDF text did not extract cleanly for verification, so the citation
     rests on the DOI page instead. Usable as a free-read backup if the writer
     wants one.
```

```text
URL: (none rejected on substance) — no source was read and dropped for being
     wrong; the discards above are URL-hygiene swaps for the same BM25 source.
```
