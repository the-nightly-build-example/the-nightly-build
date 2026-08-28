# writer brief: what-could-go-wrong/autonomous-weapons (02) — revision

Inputs:
- editorial-direction.md
- writing-coach/01/voice-guide.md   (reread before revising)
- researcher/02/evidence.md   (the CURRENT evidence record — supersedes 01; read its new Harpy and Russell findings)
- editor/01/editorial-review.md   (apply every required item)
- writer/01/draft-handoff.md   (your prior handoff)
- the article at library/what-could-go-wrong/autonomous-weapons.html  (already carries the editor's 13 direct edits — preserve them)
- .nb-context/

Output: agent-artifacts/what-could-go-wrong/autonomous-weapons/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/what-could-go-wrong/autonomous-weapons/library/what-could-go-wrong/autonomous-weapons.html --series what-could-go-wrong

Apply exactly these required items (from editor/01 and researcher/02); do not re-open settled work or expand the
claim set beyond the new evidence:

1) HARPY DATE — reframe every instance. The precise "since the 1990s" fielding year is NOT sourceable. Re-anchor
   the "already deployed, and it predates the 2015 debate" point to what researcher/02 CAN source: the Jamestown
   Foundation (Shichor, 2005) establishes the Sino-Israeli Harpy deal was negotiated in the mid-1990s and that by
   1999 Israel had reportedly sold China about 100 Harpy UAVs — i.e., a finished, exported weapon system more than
   a decade and a half before the 2015 open letter. Use that (a datable, sourced fact) as the "predates the
   debate" anchor. If you keep any decade-level phrasing about its origin, cap it at what the record supports
   ("developed in the late 1980s," decade precision, per INSS/Aviationist) and cite it. Update ALL occurrences
   consistently: the dek, both bookends (Why this matters / The takeaway), the body sentences, the holds-up grid,
   and the closing section. The nb-meta dek and the rendered dekline must remain identical after the change.

2) RUSSELL ROLE — he is NOT the letter's "drafter" (the named contacts were Toby Walsh and Max Tegmark). Per
   researcher/02, he "presented"/"helped launch" the 2015 FLI letter (FLI retrospective, with Walsh) and signed
   it (KQED); NPR calls him "a leading force behind" it. Use "presented"/"helped launch" or "signatory" —
   whichever fits the sentence — and cite the supporting source. Do not call him the drafter.

3) Clear the remaining proof warning: editor/01 noted one W-SENTENCE-DENSITY warning (~58 words) it could not
   isolate. Find and split that sentence (and any other density/length flag) so the final proof is clean.

4) Preserve the editor's 13 direct edits already in the article (named-person fixes, the added IHL-distinction
   plank, the slop cuts, the ellipsis on the Kallenborn quote, etc.). Do not reintroduce anything the editor cut.

Then run `./nb stamp` and the exact `nb check` above with links included until BLOCK: 0 (aim for WARN: 0). Do the
display-text self-test. Write draft-handoff.md with one line per required item resolved, the proof result, and any
warning intentionally left. nb-meta model field stays "claude-sonnet-5".
