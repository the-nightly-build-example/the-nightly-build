# Brief 02 — writer (revision) — the-evidence/the-bitter-lesson

## Why this round
The editor's round-01 review approved the piece after its own surgical cuts, with one
remaining required change that is a markup edit only the writer makes.

## Begin with these inputs
1. `editor/01/editorial-review.md` — apply every required item. The required change:
   **change source 11's `data-nb-kind` from `primary` to `secondary`.** Source 11 is
   Rodney Brooks, "A Better Lesson," used only to critique Sutton's essay, so it is a
   secondary. (The editor already made its factual/prose cuts directly in the article;
   do not undo them.)
2. `writer/01/draft-handoff.md`, `researcher/01/evidence.md`, `editorial-direction.md`.
3. The article (already editor-edited): `library/the-evidence/the-bitter-lesson.html`.

Follow the **writer** skill (Skill: `writer`; fallback file). Make only the required
change (and any nb-meta count sync if needed). Do not expand the claim set.

## Verify source policy after the flip
The series floor is primary ≥ 3, secondary ≥ 1. Confirm the new counts still satisfy
it (the flip should leave ample primary). The proof reports the counts.

## Prove and hand off
Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
```
Write `writer/02/draft-handoff.md`. Return `DONE writer <writer/02/draft-handoff-path>`
after `BLOCK: 0`, or a REQUEST.
