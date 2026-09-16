# writer brief: the-instruments/mean-opinion-score (01)

Inputs:
- `.nb-work/the-instruments/mean-opinion-score/agent-artifacts/the-instruments/mean-opinion-score/editorial-direction.md` — house, slop, headline, press, template, series standards
- `.nb-work/the-instruments/mean-opinion-score/agent-artifacts/the-instruments/mean-opinion-score/writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages
- `.nb-work/the-instruments/mean-opinion-score/agent-artifacts/the-instruments/mean-opinion-score/researcher/01/evidence.md` — the complete claim set; draft only from this
- `.nb-work/the-instruments/mean-opinion-score/agent-artifacts/the-instruments/mean-opinion-score/commission.md` — the measurement, the five teaching ideas, the case to show
- `.nb-work/the-instruments/mean-opinion-score/library/the-instruments/mean-opinion-score.html` — the initialized lesson to edit in place
- `.nb-work/the-instruments/mean-opinion-score/.nb-context/` — effective template contract and furniture catalogs

Output: `.nb-work/the-instruments/mean-opinion-score/agent-artifacts/the-instruments/mean-opinion-score/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-instruments/mean-opinion-score/library/the-instruments/mean-opinion-score.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links` added; final run links included, to `BLOCK: 0`.)

Recent shapes to break (do not inherit): The Instruments has leaned on a headline
that states a surprising empirical finding then a dek explaining where the trust
came from. Find this lesson's own headline shape and vary heading construction.

This round's focus: the evidence record carries a same-stimuli re-rating result
and a set of differing ground-truth MOS values across papers that would support
an honest chart if a chart earns its place; and a "human parity" claim whose own
paper curated its reference set. Use these with their exact scope. Fill nb-meta
dek to match the rendered dekline exactly, and set harness and writer model
(model: claude-sonnet-5).
