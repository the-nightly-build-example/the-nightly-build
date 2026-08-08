# writer brief: the-instruments/needle-in-a-haystack (01)

Inputs:
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/editorial-direction.md — governing standard, headline standard, press voice, lesson identity, series prompt
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/commission.md — subject, angle, required contribution, boundaries
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writing-coach/01/voice-guide.md — craft standard and licenses (deflate by mechanism, not attitude)
- .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/researcher/01/evidence.md — complete claim set; use its Numbers section exactly
- .nb-work/the-instruments/needle-in-a-haystack/library/the-instruments/needle-in-a-haystack.html — the initialized article to EDIT in place
- .nb-work/the-instruments/needle-in-a-haystack/.nb-context/ — effective contract, runtime assets, furniture catalogs

Output: .nb-work/the-instruments/needle-in-a-haystack/agent-artifacts/the-instruments/needle-in-a-haystack/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-instruments/needle-in-a-haystack/library/the-instruments/needle-in-a-haystack.html --series the-instruments --library /home/user/library-checkout --no-check-links`
then `./nb stamp` and the same command WITHOUT `--no-check-links` until `BLOCK: 0`.

nb-meta: date `2026-08-08`, harness `claude-code-routine`, model `claude-opus-4-8`;
keep nb-meta `dek` identical to the rendered dekline.

Precision the evidence flags (the editor will check):
- A few headline percentages and any verbatim quotes were read through a fetch
  summarizer. If you print a verbatim quote, RE-OPEN the cited page and confirm it
  character-for-character. Check the RULER ranked-model count against its own table
  before stating it (the record notes ~4 hold at 32K vs a 10-flagship/17-total
  framing — state only what the table supports).
- Keep "finding the planted fact" (verbatim retrieval) and "using the whole
  document" (reasoning) as two clearly separate capabilities; the whole lesson is
  that a near-perfect score on the first says little about the second.
- Be fair: NIAH caught a genuine, fixable failure in Claude 2.1 (27% -> 98% after
  adding the "Here is the most relevant sentence" line), so a green grid is
  necessary but not sufficient. That fairness point is the lesson, not a hedge.

Source asset: the NIAH green/red grid is strong evidence. If you use one, capture it
with `./nb asset` from the cited primary (the evidence records three candidate lab
grids), crop per the record, give it useful alt text and a factual cited caption.
Only use a grid the evidence record identifies; never an external image URL.

Recent the-instruments shapes to break: no "From <raw> to one <number>" heading, no
reflexive nb-stat-strip; name headings from the eval's construction. Link (plain
prose link) to the-instruments/context-window rather than re-teaching the raw
context-length number.

This round's focus: the reader can explain how a NIAH score is produced and read,
and why a "perfect recall at N tokens" claim resting on NIAH alone proves little
about long-context reasoning.
