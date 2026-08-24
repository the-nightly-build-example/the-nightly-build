# writer brief: the-evidence/retrieval-augmented-generation (01)

Inputs: .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/editorial-direction.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/writing-coach/01/voice-guide.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/researcher/01/evidence.md
        .nb-work/the-evidence/retrieval-augmented-generation/library/the-evidence/retrieval-augmented-generation.html   the initialized article; edit it in place
        .nb-work/the-evidence/retrieval-augmented-generation/.nb-context/   effective template contract, runtime assets, and furniture catalogs
Output: .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/the-evidence/retrieval-augmented-generation/library/the-evidence/retrieval-augmented-generation.html --series the-evidence --library /home/user/library-checkout

Recent habits to break (paper-wide, from the last several published lessons; the
voice guide names no prior article):

- Why cards keep opening by telling the reader what they have heard ("You have
  read that...", "You keep hearing that..."). Open on this lesson's particulars.
- Why cards keep closing on "By the end you will know what A, B, C, and D."
  Avoid that enumeration.
- Why cards keep narrating themselves ("This lesson builds/lays out..."). Address
  the reader without the "this lesson [verb]" frame.
- Takeaways keep resolving with "The question was whether..." and closers built
  as "That is real, and it is what X." Avoid both.
- Headlines keep pairing two independent clauses with a comma and "and." Vary the
  construction.
- Deks: avoid the comma-triad closed with "and," the semicolon reversal, and the
  suspended "...the real question is whether."

Outline: derive this piece's sections from its own argument, not the near-fixed
arc recent lessons run.

This round's focus: the evidence record's Contradictions are load-bearing. The
paper's "joint training" is specifically that Lewis et al. froze the DPR
document encoder and the FAISS index and fine-tuned only the query encoder
together with BART (§2.4). Modern RAG fine-tunes neither side; the contrast
holds, but do not overstate the paper's joint training. The record contains no
like-for-like "hallucination with vs without retrieval on the same model" rate;
say what RAGTruth and the paper's Jeopardy evaluation actually measured. Xu and
Bai disagree on whether retrieval helps long-context models; carry the
disagreement in prose. Link the-mechanics/retrieval in Background rather than
re-teaching the mechanism; this lesson stays on the paper.
