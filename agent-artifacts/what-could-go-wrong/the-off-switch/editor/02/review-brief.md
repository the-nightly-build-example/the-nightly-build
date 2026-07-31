# Review brief 02 — editor (revision re-read) — what-could-go-wrong/the-off-switch

## Why this round
Round 01 fixed a factually-backwards framing in the body directly, but the same false
claim sat in the dek ("instructing it to protect that goal above anything else"),
which only the writer can change (nb-meta.dek must match the rendered dekline). The
writer has revised (writer/02). Confirm the fix and re-settle.

## Inputs
- `editor/01/editorial-review.md`, `writer/02/draft-handoff.md`,
  `researcher/01/evidence.md` (Palisade's real conditions/numbers), the article
  `library/what-could-go-wrong/the-off-switch.html`.

Follow the **editor** skill; focused re-read only. Confirm (1) the new dek accurately
characterizes the empirical result — resistance appeared even when models were told
to allow shutdown / with no goal-protection instruction — and does NOT reassert the
false "protect that goal" causation; (2) nb-meta.dek == the rendered dekline; (3) the
dek is a claim, not a hedged-contrast mold; "AI race" absent; (4) no regression.
Re-run:
```
/home/user/the-nightly-build/nb check .nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html --series what-could-go-wrong --library /home/user/the-nightly-build/library-checkout
```

## Output
`editor/02/editorial-review.md` (what you re-checked; the decision). Return
`DONE editor <path>` if settled, else a REQUEST.
