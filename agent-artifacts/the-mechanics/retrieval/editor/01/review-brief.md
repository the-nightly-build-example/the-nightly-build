# editor review-brief: the-mechanics/retrieval (editor/01)

Inputs:
  ../../commission.md — behavior, angle, boundaries, the honesty note
  ../../editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
  ../../writer/01/brief.md — the exact writer brief (for prompt-leakage comparison)
  ../../writing-coach/01/voice-guide.md — register, licenses, do-not-reuse list
  ../../researcher/01/evidence.md — the claim set to test against
  ../../writer/01/draft-handoff.md — original-work sentence, proof state, open questions
  ../../../../library/the-mechanics/retrieval.html — the drafted article
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs
Output: ./editorial-review.md

Recent-pattern notes: the-mechanics has overused stacked short subject-verb
declarative headings and the "The X is the Y" identity heading; the neighbor
lesson `losing-the-thread` owns the "right document present, model still fails"
behavior — this piece must keep its own failure (a confident citation to an
unsupporting passage) and not reprise that U-shape framing. Check dek and
headings against the coach's do-not-reuse list.

Round focus: three technical claims must survive the skeptic read exactly as the
evidence states them — (1) ranking is closeness in embedding space, cosine named
as the common metric not the universal one (the RAG/DPR lineage ranks by dot
product); (2) Lewis et al. 2020 froze the document encoder and index and trained
only the query encoder and generator, while shipped RAG trains neither; (3) the
bad-citation failure is owned by either retrieval or generation, not pinned to
one (no cited source partitions the two). Confirm every linked prior-lesson href
resolves. Judge whether the one table and one stat strip earn their place. No
code is a series rule. Approve only if no publication-blocking work remains.
