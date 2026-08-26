# writer brief: the-instruments/codeforces-rating (01)

Inputs:
- `editorial-direction.md` (artifact root) — house standard, press voice, series prompt.
- `writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages.
- `researcher/02/evidence.md` — the complete claim set (supersedes 01; 02 adds an 8th source to clear the series floor); draft only from what it opened.
- The initialized article: `.nb-work/the-instruments/codeforces-rating/library/the-instruments/codeforces-rating.html` — edit in place; do not recreate the skeleton.
- Effective template contract and furniture catalogs under `.nb-work/the-instruments/codeforces-rating/.nb-context/`.

Output: `.nb-work/the-instruments/codeforces-rating/agent-artifacts/the-instruments/codeforces-rating/writer/01/draft-handoff.md` (and the edited article in place).

Proof (run from repo root `/home/user/the-nightly-build`):
`./nb check --series the-instruments --library /home/user/library-checkout .nb-work/the-instruments/codeforces-rating/library/the-instruments/codeforces-rating.html`
Iterate with `--no-check-links`; run the full command (links on) to `BLOCK: 0` before handing off. Run `nb stamp` before the final check.

Do NOT re-teach Elo from scratch — link `the-instruments/chatbot-arena-elo` at first use; teach only the Codeforces-specific parts (rated rounds, tiers, how a rating maps to titles).

Evidence caveats you must respect (the record's Contradictions correct two framings
from the commission — honor the record, not the commission, where they differ):
- AlphaCode DID submit to the live Codeforces judge on finished contests, so do NOT
  claim "these ratings never went through the real judge." The honest, well-sourced
  spine: a Codeforces rating is an Elo-style standing relative to a live human field,
  and every AI figure is an ESTIMATE from simulated participation, condition-dependent.
- The contamination angle is weak for Codeforces specifically (LiveCodeBench found the
  memorization signal on LeetCode and reported Codeforces performance smooth over time);
  do not assert Codeforces-specific contamination inflated a rating.
- The strongest, cleanest cases to build on: (a) OpenAI's own paper reports the SAME
  base model at 1673 vs 2214 depending on hand-crafted test-time scaffolding; (b)
  AlphaCode's top-54.3% / 1238 rode on up to ~1,000,000 samples per problem filtered to
  10 submissions; (c) o3's announced "2727 / 175th best programmer" versus the paper's
  estimated, simulated 2724 — a headline quoted past its qualifier. Pin every rating to
  its exact source and conditions.
- Verified rating series available for a chart (OpenAI, arXiv 2502.06807): GPT-4o 808
  (11th pct) → o1-preview 1258 (62nd) → o1 1673 (89th) → o1-ioi 1807 (93rd) → 2214
  (98th) → o3 2724 (99.8th); AlphaCode 1238 / top 28% (Li et al., 2203.07814). If you
  build a chart, use `nb chart` and cite provenance; only from the verified series.
- Codeforces title-threshold cutoffs shifted since the 2013 post; date them if cited.

Set the nb-meta writer model field to `claude-opus-4-8`.

Recent Instruments habits to break (do not inherit; the last Instruments piece was
bfcl, and the adjacent Evidence piece clip):
- Do not close on the "Read [the number] as what it is, and ask separately whether..."
  takeaway mold — both bfcl and clip ended that way. Land the judgment in this
  article's own frame.
- Do not use "By the end you will be able to..." as the why-bookend closer.
- The phrase "doing the work" ("the attempts, not the model, are doing the work") is a
  house tic; do not use it.
Name your one original-work sentence in the handoff.
