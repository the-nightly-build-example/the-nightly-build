# writer brief: what-could-go-wrong/recommender-radicalization (01)

Inputs:
- ../../editorial-direction.md — house standard, the paper's voice, the series prompt.
- ../../commission.md — the argument, required three-part structure, boundaries, required contribution, source floor, recent-pattern habits to break.
- ../../writing-coach/01/voice-guide.md — how this piece should sound (read before drafting).
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers exactly and address its Contradictions in the prose.
- Initialized article to edit in place: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/recommender-radicalization/library/what-could-go-wrong/recommender-radicalization.html
- Template context: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/recommender-radicalization/.nb-context/

Output: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/recommender-radicalization/agent-artifacts/what-could-go-wrong/recommender-radicalization/writer/01/draft-handoff.md

Proof (from repo root /home/user/the-nightly-build; iterate with --no-check-links, final with links until BLOCK: 0):
  ./nb stamp .nb-work/what-could-go-wrong/recommender-radicalization/library/what-could-go-wrong/recommender-radicalization.html
  ./nb check .nb-work/what-could-go-wrong/recommender-radicalization/library/what-could-go-wrong/recommender-radicalization.html --series what-could-go-wrong

This round (carry these bounds; they are the whole point of the piece):
- Open the argument at full strength (Pariser's filter bubble; Tufekci's "Great Radicalizer") before a word against it. Then the empirical test. Then the two-sided gap.
- Every disconfirming null is bounded, and the prose must carry the bound: the panel/experiment studies measure population-level effects and cannot rule out individual radicalization (Hosseinmardi's own caveat); Chen et al. observed in 2020, after YouTube's 2019 recommender changes, so the nulls do not reach the 2016-era system Tufekci described; the Meta feed experiment ran in a window Meta had altered with ~63 "break glass" changes (the UMass reanalysis). Because of these, the dismissive "recommenders are harmless" reading also outruns the proof. Name the gap on both sides; leave the reader to decide.
- Use figures exactly as scoped in the evidence (e.g. Guess feed experiment: design + verbatim null + "about 23,000 users" from the Science news report, flagged as not verified against the paywalled body — do not invent a per-platform figure).
- Link, do not re-teach (Background/prose links): when-ai-breaks/facebook-myanmar is the strongest (owns the engagement-ranking mechanism and a real-harm case). Stay distinct from what-could-go-wrong/gradual-disempowerment, which already cites the same chronological-feed null — link it, do not overlap its argument. ai-persuasion and algorithmic-monoculture are adjacent; name only to stay distinct.
- Break the "What Bainbridge saw" opener mold and the "The floor labs stand on now / Where the same X lives" closer mold. Fresh dek that commits to the specific find (the studies built to detect it mostly did not), no comma-triad / semicolon-reversal.
- nb-meta: date "2026-09-15", harness "claude-code-routine", model "claude-sonnet-5".
