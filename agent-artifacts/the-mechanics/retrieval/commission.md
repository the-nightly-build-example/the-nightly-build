# Commission: the-mechanics/retrieval

## Authorized work
Scheduled duty for 2026-08-04 returned `the-mechanics` as an open section. This
commission fills it with one lesson working backward from one behavior. One
article.

## The behavior
You give a chatbot a document it never saw in training — a PDF you upload, your
own files, a web page — and it answers with specifics from that document and
often cites the exact passage. Its weights were frozen when training ended
(`the-mechanics/knowledge-cutoff`), so it did not "learn" your document. How
does it find and use the right passage?

## Angle
The Mechanics method: name the behavior, work backward step by step to the parts
that produce it, mark settled engineering versus open questions, and stop at
ground. The two mechanisms doing the real work: (1) a **nearest-neighbor search
over embeddings** picks a few relevant chunks, and (2) the model **reads those
chunks as ordinary prompt tokens** (`the-mechanics/instructions-are-data`) and
generates conditioned on them. Then show the concrete failure everyone has seen
— a confident citation to a retrieved passage that does not actually support the
claim — and attribute it to a specific step. No code.

## Steps to walk (verify the mechanism against primaries)
1. The system does not feed the whole corpus to the model. It retrieves a few
   relevant chunks and inserts them into the prompt. This is retrieval-augmented
   generation (RAG), named by Lewis et al. 2020.
2. How "relevant" is decided: documents are split into chunks; an embedding
   model turns each chunk into a vector; the query is embedded the same way;
   relevance is vector closeness (cosine similarity). Build on
   `the-mechanics/word-embeddings` (link it) but be exact that these are
   whole-passage embeddings, not the frozen word vectors that lesson described.
3. Finding the closest vectors fast: approximate nearest-neighbor search (e.g.,
   HNSW / FAISS). Settled engineering. The top-k chunks are returned.
4. Generation: the retrieved chunks sit in the prompt; the model generates an
   answer over them; a citation is produced by tracking or quoting the chunk
   used.
5. Ground and open questions: the embedding model decides "relevant" and can
   miss (a passage the query needs but that is not semantically near it), which
   is why keyword search (BM25) and rerankers are bolted on. Chunking strategy,
   retrieval-quality measurement, and whether the model actually uses what it
   retrieved (`the-mechanics/losing-the-thread`) are unsettled. The visible
   failure — a citation to a chunk that does not support the answer — is either
   retrieval returning a plausible-but-wrong chunk or the model ignoring the
   chunk and falling back on `the-mechanics/hallucination`. Name which step owns
   the failure.

## An honesty note worth making
The paper that *named* RAG (Lewis et al. 2020) describes a system whose
retriever and generator were trained together on knowledge tasks. The "RAG"
every product ships today is a looser pipeline that embeds, searches, and stuffs
chunks into the prompt of a frozen model. Worth one precise line: what the
document built versus what the term now denotes.

## Boundaries
- Work backward from the one behavior. Do not survey every retrieval
  architecture or turn this into a vector-database tutorial. Two or three
  mechanisms taught completely beats six named.
- No code, per the series prompt. Diagrams-in-prose and a small worked example
  (a query and why one chunk ranks above another) carry it.
- Link, do not re-teach: `word-embeddings`, `instructions-are-data`,
  `knowledge-cutoff`, `losing-the-thread`, `hallucination`.

## Sources plan
Series policy: min 8 sources, at least 4 primary and at least 1 secondary.
Target primaries: Lewis et al. 2020 (RAG); Karpukhin et al. 2020 (Dense Passage
Retrieval); an ANN-search primary (Malkov & Yashunin 2018 HNSW, or Johnson et
al. 2019 FAISS); a sentence/passage-embedding primary (Reimers & Gurevych 2019
Sentence-BERT); Robertson & Zaragoza 2009 (BM25) for the lexical baseline; a
retrieval-generalization primary (Thakur et al. 2021 BEIR) for "retrieval can
miss." At least one strong secondary on RAG failure modes / citation
faithfulness. Researcher owns final selection and verifies the mechanism claims
(cosine similarity, ANN, top-k) against the owning papers.

## Neighboring articles this run (avoid overlap)
Tonight also publishes `the-evidence/alexnet`, `the-instruments/training-compute`,
`what-could-go-wrong/cyber-uplift`, `when-ai-breaks/nh-predict`. This is the only
retrieval/embeddings piece. `alexnet` touches vision and this touches embeddings;
they do not overlap — keep each in its lane.

## Recent shapes to break
The Mechanics desk's recent headings run as short declarative claims ("The pause
is the model reading your prompt"). That shape is good but now frequent; vary
cadence and avoid a stack of identically-shaped subject-verb headings. Avoid the
comma-and-"and" heading and dek molds. Coach supplies the do-not-reuse list from
the recent library.

## Production record
- Profile: balanced. Model directive: `capable` for every stage (not required).
  Effort directives: writing-coach low, researcher high, writer medium, editor
  high.
- Actual harness: roles run as isolated subagents on model `claude-opus-4-8`.
  Per-stage effort inherited (not independently settable); recorded as a
  permitted deviation. Writer records the model string in `nb-meta`.
