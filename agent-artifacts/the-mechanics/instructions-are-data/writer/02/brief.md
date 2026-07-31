# Brief 02 — writer (revision) — the-mechanics/instructions-are-data

## Why this round
The editor's round-01 review requires one true redraft item. Apply it, preserve all
other settled work, and re-prove.

## Begin with these inputs
1. `editor/01/editorial-review.md` — **apply every required item in it.** The key
   required change: the "Delimiters flatten into the same stream" section currently
   describes Simon Willison's demonstration as using the course-recommended
   delimiters and being defeated from *inside* them. The source shows the opposite —
   the demonstration deliberately uses **no delimiters**, and the model obeys the
   injected passage anyway. Renarrate the anecdote to match the source. (The editor
   already made its own surgical cuts directly in the article; do not undo them.)
2. `writer/01/draft-handoff.md` (prior round), `researcher/01/evidence.md` (the only
   claim set — reopen the Willison source entry to get the demonstration right),
   `writing-coach/01/voice-guide.md` (reread before revising), `editorial-direction.md`.
3. The article to edit (already editor-edited): `library/the-mechanics/instructions-are-data.html`.

Follow the **writer** skill (Skill: `writer`; fallback file). Reread the voice guide.
Do not independently expand the claim set; if the renarration needs a fact the
evidence lacks, `REQUEST researcher`. Keep it architectural; no code; `machinery` banned.

## Prove and hand off
Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-mechanics/instructions-are-data/library/the-mechanics/instructions-are-data.html --series the-mechanics --library /home/user/the-nightly-build/library-checkout
```
Keep nb-meta counts honest if the word count moved. Write
`writer/02/draft-handoff.md` (what changed, every editor item addressed, proof
result). Return `DONE writer <writer/02/draft-handoff-path>` after `BLOCK: 0`, or a REQUEST.
