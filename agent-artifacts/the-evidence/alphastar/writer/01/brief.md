# writer brief: the-evidence/alphastar (01)

Inputs (artifact root is this file's grandparent directory):
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity
- ../../commission.md — the assignment and its boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting
- ../../researcher/01/evidence.md — the complete claim set; treat as evidence, not prose
- The initialized article: /home/user/the-nightly-build/.nb-work/the-evidence/alphastar/library/the-evidence/alphastar.html
- Template context: /home/user/the-nightly-build/.nb-work/the-evidence/alphastar/.nb-context/

Output: draft-handoff.md (this directory)

Proof (run from /home/user/the-nightly-build; iterate with `--no-check-links`, run `nb stamp` before the final pass, then run with links until `BLOCK: 0`):

```
./nb check .nb-work/the-evidence/alphastar/library/the-evidence/alphastar.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/6299876f-cc26-50aa-a765-ad85a93ca3c3/scratchpad/library-checkout
```

This round's focus:
- Publication date is 2026-09-19. Set nb-meta `date` to it, `harness` to "claude-code", and the writer `model` to the exact model you run as (e.g. `claude-opus-4-8`).
- The central correctness point from the evidence record: do NOT conflate the January 2019 showcase (looser action limits, whole-map vision, one race/one map, "doesn't feel superhuman" per the pro player TLO) with the Nature version (camera interface + the 22-actions-per-5-seconds cap), which reached Grandmaster with those limits, and whose own ablations show the limits reduced performance. The APM/whole-map critique lands hardest on the January agent.
- Grandmaster meant blind, anonymous ladder play above 99.8% of ~90,000 active European-server players; the paper explicitly says those conditions do not measure susceptibility to exploitation under repeated play, so it is not a claim to have beaten the world's best in a controlled series. TLO played Protoss off-race in the December series — note it where the "beat the pros" story appears.
- The Nature Methods were read fully; the downloadable supplementary code/data files were not opened. Claim nothing that would require them.

Recent shapes to break (do not inherit from the recent library):
- Deks that run as one long sentence carrying an embedded numeric contrast; give this dek a stance and one identifying detail.
- Headings that lead with a raw number or use the "X did, Y did not" contrast; vary construction.
- The recurring furniture stack (nb-stat-strip, nb-figure, nb-table, nb-note). Plan furniture from the supplied catalog for this piece.
