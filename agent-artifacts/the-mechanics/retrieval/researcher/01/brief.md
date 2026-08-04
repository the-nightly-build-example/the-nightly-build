# researcher brief: the-mechanics/retrieval (01)

Inputs:
  ../../commission.md — behavior (grounded answer from an untrained document), angle, boundaries, sources plan
  ../../editorial-direction.md — citation standard, declared reader, series territory
Output: ./evidence.md

Round focus: verify the mechanism against the owning papers — that retrieval
ranks chunks by embedding closeness (cosine similarity), that approximate
nearest-neighbor search returns top-k, and what the RAG paper (Lewis et al.
2020) actually built (jointly trained retriever+generator) versus what "RAG"
now denotes in shipped products. Establish the concrete failure mode (a citation
to a retrieved chunk that does not support the claim) from a retrieval-quality
or citation-faithfulness primary. Fill Contradictions with what is settled
engineering versus unsettled heuristic (chunking, reranking, whether the model
uses what it retrieved).

Run-environment caveat: published library at `/home/user/library-checkout` for
`nb history`.
