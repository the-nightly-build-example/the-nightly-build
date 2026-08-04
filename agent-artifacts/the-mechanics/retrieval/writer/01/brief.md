# writer brief: the-mechanics/retrieval (01)

Inputs:
  ../../commission.md — behavior, angle, boundaries, the honesty note, sources plan
  ../../editorial-direction.md — house + headline standard, press voice, lesson identity, series prompt
  ../../writing-coach/01/voice-guide.md — register, licenses, do-not-reuse list
  ../../researcher/01/evidence.md — the complete claim set; use its Numbers and Sources exactly
  ../../../../library/the-mechanics/retrieval.html — the initialized article to edit (do not recreate the skeleton)
  ../../../../.nb-context/ — effective template contract, runtime assets, furniture catalogs
Output: ./draft-handoff.md
Proof (links included, until BLOCK: 0):
  ./nb check .nb-work/the-mechanics/retrieval/library/the-mechanics/retrieval.html --series the-mechanics --library /home/user/library-checkout

Round focus: two evidence findings sharpen the commission — honor them exactly.
(1) Rank by "closeness in embedding space"; name cosine similarity as the common
production metric, not the universal one (the RAG/DPR lineage ranks by raw dot
product). (2) The honesty note is more precise than the commission stated: Lewis
et al. 2020 froze the document encoder and index and trained only the query
encoder and generator together, while shipped "RAG" typically trains neither —
state it that way. The bad-citation failure cannot be pinned to one step by the
evidence; present it as owned by either retrieval (wrong chunk returned) or
generation (right chunk ignored), not resolved to one. No code (series rule).
