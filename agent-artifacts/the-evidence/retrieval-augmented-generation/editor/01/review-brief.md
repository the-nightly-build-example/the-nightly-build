# editor review-brief: the-evidence/retrieval-augmented-generation (01)

Inputs: .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/editorial-direction.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/commission.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/writer/01/brief.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/writing-coach/01/voice-guide.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/researcher/01/evidence.md
        .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/writer/01/draft-handoff.md
        .nb-work/the-evidence/retrieval-augmented-generation/library/the-evidence/retrieval-augmented-generation.html
        .nb-work/the-evidence/retrieval-augmented-generation/.nb-context/
Output: .nb-work/the-evidence/retrieval-augmented-generation/agent-artifacts/the-evidence/retrieval-augmented-generation/editor/01/editorial-review.md

Recent-pattern notes for the Cut and headline/dek/heading reads (paper-wide;
these travel with the article, not the voice guide):

- Why cards recently opened by telling the reader what they have heard ("You
  have read that...", "You keep hearing that..."). Flag if this draft slips
  into that mold.
- Why cards recently closed on the stamped "By the end you will know what A, B,
  C, and D" enumeration. Flag if present.
- Why cards recently narrated themselves ("This lesson builds/lays out..."). The
  bookend can address the reader; check that it does not do so with the
  "this lesson [verb]" formula.
- Takeaways recently resolved with "The question was whether..." and closers
  built as "That is real, and it is what X" (the empty "the X here is real, and
  it is Y" shape). Cut both.
- Headlines recently paired two independent clauses with a comma and "and." Check
  the construction is not that pattern.
- Deks: the comma-triad closed with "and," the semicolon reversal, and the
  suspended "...the real question is whether" are all stamped across the recent
  front. Cut on sight.

This round's focus: the writer flagged two open questions in the handoff. First,
Xu/Bai disagreement is currently carried through Xu et al.'s own acknowledgment
because the researcher's Bai entry lacks a URL; if you can settle it from the
draft plus record, do; if not, route the missing-URL evidence back. Second, the
Barnett 15,000-vs-4,017 inconsistency is handled in prose using the case-study
figure per the researcher's guidance. Read for whether the paper-vs-modern-RAG
line stays honest (Lewis et al. froze DPR document encoder + FAISS index and
fine-tuned only the query encoder together with BART, §2.4; modern RAG
fine-tunes neither), and whether the article claims a like-for-like
hallucination-with-vs-without-retrieval rate the record does not support.
