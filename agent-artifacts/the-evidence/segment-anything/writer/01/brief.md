# writer brief: the-evidence/segment-anything (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series prompt
- ../../commission.md — angle, course boundary, and the recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available; use its Numbers section exactly
- ../../../../library/the-evidence/segment-anything.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract, runtime assets, and furniture catalogs (engine, press, template)

Output: ./draft-handoff.md

Proof: nb check .nb-work/the-evidence/segment-anything/library/the-evidence/segment-anything.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/c80f7a7e-0800-5248-bdf5-999f03f80465/scratchpad/library-checkout

Run the proof from the main checkout root (/home/user/the-nightly-build) with the
checkout's ./nb. Iterate with --no-check-links, then finish on the full command
above until BLOCK: 0. The evidence records that SA-1B's automatic-mask quality
rests on Meta's own 500-image study and that zero-shot SAM trails task-specific
models; both belong in the lesson, cited to the evidence. The masks-not-labels
boundary is the spine — keep it sharp against clip and vision-transformer, linked
as Background rather than re-taught.
