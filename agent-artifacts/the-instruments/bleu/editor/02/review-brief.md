# Review brief 02 — editor (revision re-read) — the-instruments/bleu

## Why this round
Round 01 required one markup change: convert the Callison-Burch Table 4 n-gram counts
in "The evaluation where the ranking flipped" from packed prose into a table/listing.
The writer has revised (writer/02). Confirm the fix and re-settle.

## Inputs
- `editor/01/editorial-review.md`, `writer/02/draft-handoff.md`,
  `researcher/01/evidence.md` (Numbers has the verified Callison-Burch figures), the
  article `library/the-instruments/bleu.html`.

Follow the **editor** skill; focused re-read only. Confirm (1) those n-gram counts now
live in a table/listing, not packed prose; (2) the numbers are unchanged and still
match the evidence record (no new/altered figures); (3) no regression, and the
arithmetic you verified in round 01 still stands. Re-run:
```
/home/user/the-nightly-build/nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
```

## Output
`editor/02/editorial-review.md` (what you re-checked; the decision). Return
`DONE editor <path>` if settled, else a REQUEST.
