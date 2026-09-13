# writer brief: the-mechanics/speech-to-text-hallucination (01)

Inputs (all under the artifact root unless noted):
- ../../editorial-direction.md — house standard, slop/headline standards, the paper's voice, the lesson template identity, the series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete set of claims and figures available to you; use its recorded URLs and its Numbers section exactly
- ../../commission.md — the assignment, the work-backward arc, the Background link candidates, the boundaries
- the initialized article to edit: /home/user/the-nightly-build/.nb-work/the-mechanics/speech-to-text-hallucination/library/the-mechanics/speech-to-text-hallucination.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/speech-to-text-hallucination/.nb-context/ (effective contract, runtime assets, furniture catalogs)

Output: draft-handoff.md (in this directory)

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then final with links until BLOCK: 0):
  ./nb stamp .nb-work/the-mechanics/speech-to-text-hallucination/library/the-mechanics/speech-to-text-hallucination.html
  ./nb check .nb-work/the-mechanics/speech-to-text-hallucination/library/the-mechanics/speech-to-text-hallucination.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/1fc763aa-f362-5066-bfeb-fee58939daaf/scratchpad/library-checkout

Decisions the inputs do not settle:
- There is no single trustworthy hallucination rate. Teach the mechanism and cite each figure with its scope (population, per-segment vs per-file, Whisper version), never a lone headline rate. The evidence record's Contradictions and Numbers carry the ranges; honor them.
- Set nb-meta tags to concrete topical tags for this piece (e.g. speech-recognition, hallucination, whisper). Fill nb-meta date 2026-09-13, harness, and the writer model you actually ran on.

Recent habits not to inherit (from the recent Mechanics record):
- Headlines built on "Ask [system] for X and it Y" or "A model can X and still Y". Find this piece's own claim.
- Keep the work-backward arc but name every section for this behavior; no stock labels, and do not reuse a prior mechanics piece's section shape.
