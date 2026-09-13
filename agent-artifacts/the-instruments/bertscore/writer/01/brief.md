# writer brief: the-instruments/bertscore (01)

Inputs (all under the artifact root unless noted):
- ../../editorial-direction.md — house standard, slop/headline standards, the paper's voice, the lesson template identity, the series prompt
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete set of claims and figures available to you; use its recorded URLs and Numbers exactly
- ../../commission.md — the assignment, the desk's arc, the Background link candidates, the boundaries
- the initialized article to edit: /home/user/the-nightly-build/.nb-work/the-instruments/bertscore/library/the-instruments/bertscore.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/bertscore/.nb-context/

Output: draft-handoff.md (in this directory)

Proof (run from /home/user/the-nightly-build, iterate with --no-check-links, then final with links until BLOCK: 0):
  ./nb stamp .nb-work/the-instruments/bertscore/library/the-instruments/bertscore.html
  ./nb check .nb-work/the-instruments/bertscore/library/the-instruments/bertscore.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/1fc763aa-f362-5066-bfeb-fee58939daaf/scratchpad/library-checkout

Decisions the inputs do not settle (from the researcher's flags):
- There is no single clean "human-correlation advantage" figure; use the evidence record's indicative figures with their scope, and do not invent a headline number.
- Do not cite the paper's PAWS robustness result as a general robustness claim: a cited study (Hanna & Bojar) shows the opposite for subtle function-word errors. Weigh that contradiction in the prose.
- Do not claim practitioners do or do not follow the version-hash reporting request; that is unsourced. State the request exists and leave compliance unknown, or cut it.
- Define cosine similarity in one plain line at first use; recall F1 in a phrase (the reader has met it); do not re-teach embeddings or word-overlap metrics — link the prior lessons in Background per the commission.
- Set nb-meta tags to concrete topical tags (e.g. bertscore, text-generation-evaluation, embeddings). Fill nb-meta date 2026-09-13, harness, and the writer model you actually ran on.

Recent habits not to inherit (from the recent Instruments record):
- Headlines built on "a [metric] can hide / misled" and a single dramatic number. Find this piece's own headline.
- Keep the arc (where the number comes from / what it cannot support / a case where it misled) but name sections for BERTScore; no stock labels.
