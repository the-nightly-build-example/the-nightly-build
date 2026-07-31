# Review brief 02 — editor (revision re-read) — the-evidence/the-bitter-lesson

## Why this round
You approved this piece in round 01 after your own surgical cuts, with one required
markup change returned to the writer: flip source 11's `data-nb-kind` from `primary`
to `secondary`. The writer has now revised (writer/02). Confirm the fix and re-settle.

## Begin with these inputs
- `editor/01/editorial-review.md` (your prior read and the required item)
- `writer/02/draft-handoff.md` (what the writer changed)
- the article `library/the-evidence/the-bitter-lesson.html`
- `researcher/01/evidence.md` if you need to re-check the Brooks classification

Follow the **editor** skill. This is a focused re-read, not a full re-litigation:
you already did the three reads. Confirm (1) source 11 is now `data-nb-kind="secondary"`
and that classification is correct (Brooks "A Better Lesson" is a critique = secondary);
(2) source-kind counts still meet the floor (primary ≥ 3, secondary ≥ 1); (3) no
regression was introduced. Re-run the proof to confirm:
```
/home/user/the-nightly-build/nb check .nb-work/the-evidence/the-bitter-lesson/library/the-evidence/the-bitter-lesson.html --series the-evidence --library /home/user/the-nightly-build/library-checkout
```

## Output
Write `editor/02/editorial-review.md` (brief: what you re-checked, the decision).
Return `DONE editor <editor/02/editorial-review-path>` if settled, else a REQUEST.
