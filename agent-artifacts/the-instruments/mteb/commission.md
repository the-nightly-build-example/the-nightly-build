# Commission: the-instruments/mteb

## The measurement

The rank a text-embedding model earns on MTEB, the Massive Text Embedding
Benchmark (Muennighoff, Tazi, Magne, Reimers, 2022), and the leaderboard built
on it. An embedding model turns a piece of text into a vector; MTEB runs a
frozen model over many datasets grouped into task types (retrieval,
classification, clustering, reranking, semantic similarity, and more), scores
each dataset with the metric that task uses (for example nDCG@10 for retrieval,
accuracy for classification), and reports the average across everything. The
leaderboard ranks models by that mean.

## Why this lesson, now

The course taught what an embedding is (the-mechanics/word-embeddings) and how
embeddings drive retrieval-augmented answering (the-mechanics/retrieval,
the-evidence/retrieval-augmented-generation), but never how anyone decides which
embedding model to trust. Every team building retrieval reaches for the MTEB
leaderboard, and the number that sorts it is meeting the reader now the way a
model-card benchmark score does. This lesson shows how that single average is
built and where it quietly misleads.

## The angle to test

Explain, step by step, how a pile of very different tasks becomes one rank: the
per-dataset metric, the grouping into task types, and the plain average that
sits on top. Then show what the number cannot support. The average hides that
retrieval, the task most readers actually care about, is one slice among many,
so a model can top the overall mean while being ordinary at retrieval, and the
tasks are weighted by how many datasets each happens to have, not by importance.
The real case where it misled: models have been tuned to the benchmark. The MTEB
maintainers themselves have flagged contamination and task imbalance, and rebuilt
the benchmark (MMTEB / an MTEB v2) partly to answer it; report the specific
concern and what changed, from the maintainers' own writing, not commentary.

The researcher must verify the task-type and dataset counts the original paper
reports (they have grown over time, so pin the number to a dated version), the
per-task metrics named above, and the exact form of the contamination or overfit
concern the maintainers acknowledged. Distinguish the benchmark (MTEB, the
datasets and scoring) from the leaderboard (the ranked table people read).

## Boundaries

Do not re-teach what an embedding or a vector is, or how retrieval works; link
word-embeddings and retrieval in Background. Keep the piece about how the MTEB
number is built and what it supports, not a tour of embedding models. This is
one of five lessons tonight; no overlap with a fine-tuning paper, format-
constrained decoding, an AI-safety argument, or a deployment failure.

## Source policy

Series floor: 8 sources, at least 4 primary and at least 1 secondary. The MTEB
paper, its leaderboard/model-card documentation, and the maintainers' revision
writeup are primary to their own claims. Meet the floor with sources that carry
the argument, not padding.

## Production

Profile balanced; no stage required. This run: writing-coach and researcher on
the strong model, researcher at high effort; writer at medium effort; editor at
high effort.

## Recent habits not to inherit

- The two-clause "and/but" dek is the current house default; build the dek
  another way and avoid the three banned molds in `spec/headlines.md`.
- "How...", "What...", "Where..." heading openers are overused across the desk.
  Name each section step in this piece's own nouns.
- The desk keeps a late "When the leaderboard rewrote its own answers"-style
  reveal section; name the present-day section in this piece's own nouns.
