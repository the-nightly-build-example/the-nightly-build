# writer brief: the-evidence/mamba (01)

Inputs (all under the artifact root unless noted):
- ../../editorial-direction.md — house standard, slop/headline standards, the paper's voice, the lesson template identity, the series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete set of claims and figures available to you; use its recorded URLs and its Numbers section exactly
- ../../commission.md — the assignment, the desk's arc, the Background link candidates, the boundaries
- the initialized article to edit: /home/user/the-nightly-build/.nb-work/the-evidence/mamba/library/the-evidence/mamba.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/mamba/.nb-context/ (effective contract, runtime assets, furniture catalogs)

Output: draft-handoff.md (in this directory)

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then final with links until BLOCK: 0):
  ./nb stamp .nb-work/the-evidence/mamba/library/the-evidence/mamba.html
  ./nb check .nb-work/the-evidence/mamba/library/the-evidence/mamba.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/1fc763aa-f362-5066-bfeb-fee58939daaf/scratchpad/library-checkout

Decisions the inputs do not settle:
- The desk's arc requires honest scale. The evidence lands on the skeptical side of "the transformer is finished": present Falcon Mamba (a pure 7B state-space model beating some size-matched transformers on short-context leaderboards) as the genuine counter-current, not a strawman, and be precise that the sharpest copying/retrieval-gap evidence tests the original Mamba, with the Mamba-2/hybrid case more indirect. Do not claim the gap is proven at frontier scale; say what the record actually shows.
- Do not re-teach attention; link a prior lesson in Background per the commission. Define state, recurrence, and perplexity in plain words on the spot, briefly.
- Set nb-meta tags to concrete topical tags (e.g. mamba, state-space-models, sequence-modeling). Fill nb-meta date 2026-09-13, harness, and the writer model you actually ran on.

Recent habits not to inherit (from the recent Evidence record):
- Opening the piece by naming authors and year ("X et al.'s 2023 paper..."); deks built as "A [noun], whose [twist]" or comma-clause chains. Find this piece's own entry and dek.
- Keep the arc (what it is / method and scale / present) but name sections for this document; no stock labels.
