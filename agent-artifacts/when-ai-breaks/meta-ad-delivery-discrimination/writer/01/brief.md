# writer brief: when-ai-breaks/meta-ad-delivery-discrimination (01)

Inputs:
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/editorial-direction.md` — house, slop, headline, press, template, series standards
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/writing-coach/01/voice-guide.md` — how this piece should sound, with exemplar passages
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/researcher/01/evidence.md` — the complete claim set; draft only from this
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/commission.md` — the incident, its six steps, the disputed cause
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html` — the initialized lesson to edit in place
- `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/.nb-context/` — effective template contract and furniture catalogs

Output: `.nb-work/when-ai-breaks/meta-ad-delivery-discrimination/agent-artifacts/when-ai-breaks/meta-ad-delivery-discrimination/writer/01/draft-handoff.md`

Proof: `./nb check .nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/d5bad8fd-c10f-5854-a93d-2fb67333d30d/scratchpad/library`
(iterate with `--no-check-links` added; final run links included, to `BLOCK: 0`.)

Recent shapes to break (do not inherit): When AI Breaks has leaned on a two-
sentence headline whose second sentence is a short flat reversal; find another
shape. Use an "X, not Y" heading only where it corrects a misconception the piece
names.

This round's focus: the evidence record flags that the Justice Department filing
could not be opened at justice.gov; cite the court documents where they resolve
(the litigation-clearinghouse host that carries the filed complaint and
settlement, and Meta's own whitepaper that quotes the filing), never a dead or
401 URL, and confirm each href resolves. Do not state the 2019 civil-rights
settlement dollar figure without the record's support. Handle the ending with the
record's nuance: the later independent audit found the remediation reduces
housing-ad skew but not the employment/credit skew it was extended to, partly by
reaching fewer people per dollar. Fill nb-meta dek to match the rendered dekline
exactly, and set harness and writer model (model: claude-sonnet-5).
