# writer brief: the-evidence/flashattention (01)

Inputs:
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/editorial-direction.md` — house, slop, headline, press, template, series standards
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/researcher/01/evidence.md` — the complete claim set; draft only from this
- `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/commission.md` — the document, the five teaching ideas, the misreading to correct
- `.nb-work/the-evidence/flashattention/library/the-evidence/flashattention.html` — the initialized lesson to edit in place
- `.nb-work/the-evidence/flashattention/.nb-context/` — effective template contract and furniture catalogs (engine, press, template)

Output: `.nb-work/the-evidence/flashattention/agent-artifacts/the-evidence/flashattention/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/the-evidence/flashattention/library/the-evidence/flashattention.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links` added; final run links included, to `BLOCK: 0`.)

Recent shapes to break (do not inherit): The Evidence has leaned on a two-sentence
headline whose second sentence is a short numeric reversal; find a different
headline shape. Recent openers use a short concrete noun-phrase heading — fine,
but do not copy a neighbor's exact rhythm.

This round's focus: the evidence record's Contradictions and Numbers sections
flag several differently-scoped "speedup" figures that must not be conflated, and
one bandwidth figure that is a third-party estimate rather than a vendor spec.
Honor those distinctions in the prose. Fill nb-meta dek to match the rendered
dekline exactly, and set harness and the writer model in nb-meta (model:
claude-sonnet-5; harness: the runtime you are running under).
