# Review brief 01 — editor — the-evidence/the-bitter-lesson

## Begin with these inputs
- `.../editor/01/review-brief.md` (this file)
- `.../editorial-direction.md`
- The exact **writer brief** `.../writer/01/brief.md` (for prompt-leak detection)
- `.../writing-coach/01/voice-guide.md`
- `.../researcher/01/evidence.md`
- `.../writer/01/draft-handoff.md` (open the original-work sentence only at the third read)
- The article: `library/the-evidence/the-bitter-lesson.html`
- `.nb-context/`

Follow the **editor** skill (Skill: `editor`; fallback `/home/user/the-nightly-build/skills/editor/SKILL.md`). Make the three ordered reads (skeptic, cut, reader). Edit prose/structure surgically in the article; cuts unbounded, new prose past a clause returns to the writer. Never edit markup/scripts/styles/assets.

## Watch especially for this piece
- **Skeptic:** verify the essay's date (13 Mar 2019), Sutton's exact title/affiliation, and any quoted wording against the primary. Confirm the piece treats the essay as an argument-from-history essay, not a study — and that its claims about Kaplan/Chinchilla match those primaries. Audit `data-nb-kind`: the essay and the scaling papers are primary; a critique is secondary.
- **Cut:** this desk's recent habit is "the headline number traces to a smaller foundation." That move fits here, but cut any sentence that *grades* the piece's own method or reuses last week's opener/verdict cadence. Check the headline is not a colon-subtitle and the dek is a claim, not a description of the article's selection.
- **Reader:** does the piece give more than either the essay or the scaling papers alone — specifically the separation of "what Sutton argued" from "the scripture it became"? Compare with the original-work sentence. Confirm it is neither a takedown nor an endorsement.
- Confirm it is not a takedown: the essay must get its due where it holds.

## Output
Write `.../editor/01/editorial-review.md` with the three required lines (`Skeptic`, `Cut`, `Reader`), direct edits made, required work by owner, and the decision. If you edit the article, the WRITER reruns the proof — note that any required change returns to the writer with a fresh proof. Return `DONE editor <path>` only if no redraft is required; else `REQUEST writer <need>` / `REQUEST researcher <need>` / `REQUEST orchestrator <need>`.
