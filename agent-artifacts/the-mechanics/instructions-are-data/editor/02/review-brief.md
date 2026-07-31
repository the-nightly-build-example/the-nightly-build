# Review brief 02 — editor (revision re-read) — the-mechanics/instructions-are-data

## Why this round
Round 01 required one redraft: renarrate Simon Willison's delimiter demonstration,
which the draft described backwards (it used course-recommended delimiters defeated
from inside, when the source shows a delimiter-free passage the model obeys anyway).
The writer has revised (writer/02). Confirm the fix and re-settle.

## Inputs
- `editor/01/editorial-review.md`, `writer/02/draft-handoff.md`,
  `researcher/01/evidence.md` (reopen the Willison entry to check the renarration is
  faithful), the article `library/the-mechanics/instructions-are-data.html`.

Follow the **editor** skill; focused re-read only. Confirm (1) the delimiter section
now matches the source (no delimiters; the model obeys the injected passage anyway);
(2) the mechanism chain and settled/open marking remain correct; (3) no code, no
banned "machinery", no regression. Re-run:
```
/home/user/the-nightly-build/nb check .nb-work/the-mechanics/instructions-are-data/library/the-mechanics/instructions-are-data.html --series the-mechanics --library /home/user/the-nightly-build/library-checkout
```

## Output
`editor/02/editorial-review.md` (what you re-checked; the decision). Return
`DONE editor <path>` if settled, else a REQUEST.
