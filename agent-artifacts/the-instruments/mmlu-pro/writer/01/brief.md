# writer brief: the-instruments/mmlu-pro (01)

All paths are relative to the repo root /home/user/the-nightly-build.
Let AR = .nb-work/the-instruments/mmlu-pro/agent-artifacts/the-instruments/mmlu-pro

Inputs:
- $AR/editorial-direction.md — house standard, paper voice, series prompt, template identity, furniture
- $AR/writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting and before every revision
- $AR/researcher/01/evidence.md — the complete claim set available to you
- $AR/commission.md — measurement, angle, the distinct contribution to make visible
- Article to edit: .nb-work/the-instruments/mmlu-pro/library/the-instruments/mmlu-pro.html (initialized from the lesson template)
- Template contract and furniture catalogs: .nb-work/the-instruments/mmlu-pro/.nb-context/

Output: $AR/writer/01/draft-handoff.md

Proof: ./nb check .nb-work/the-instruments/mmlu-pro/library/the-instruments/mmlu-pro.html --series the-instruments --library /home/user/library-checkout
(run from repo root; use --no-check-links while iterating, then the full command with links to BLOCK: 0)

Recent habits on this desk to break (do not inherit):
- Headline mold "A model can top the X average and be ordinary at Y" / "The score labs cite grades one Z, and usually never runs it" (the cited-number-is-hollow reveal) has run on mteb, bfcl, codeforces-rating. MMLU-Pro's story is partly a repair that worked; do not force the standard debunk headline — state what is actually surprising.
- Deks have leaned on the comma-triad and "one flat average over N datasets". Pick a different build; check the recent deks named in the commission.
- nb-table is the reflex here. One MMLU-vs-MMLU-Pro construction table may earn its place; do not add a second by habit.

This round's focus: teach how an MMLU-Pro item is built and scored, then grade each
repair against MMLU's named defects (guess rate, label noise, prompt sensitivity)
honestly — some fixed, some partial. Give the reader a rule for what a few-point
MMLU-Pro gap does and does not license. Link the published `mmlu` lesson in
Background rather than re-teaching what MMLU is.
