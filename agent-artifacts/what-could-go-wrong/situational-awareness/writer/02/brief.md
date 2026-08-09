# writer brief: what-could-go-wrong/situational-awareness (02)

Apply the one required item in `../../editor/01/editorial-review.md` (Required
work, owner: writer). Nothing else changes; the editor's own cuts are already in
the article.

The fix: the SAD table's ceiling column is headed "Human" and its caption says
90.7% "matches an informed person," but 90.7% is the SAD paper's **Upper
Baseline** — a composite that uses human roleplay on only some categories and an
oracle (100%) on tasks no human can do (SAD §3.1, Table 1). Correct the
display text so the label is true: rename the column header to name the upper
baseline rather than a human, and fix the caption so it does not present 90.7% as
a human ceiling. Keep the figure 90.7% and keep the body prose (already correct,
"far below the reachable ceiling"). Do not introduce new claims.

Inputs:
- `../../editor/01/editorial-review.md` — the required item, stated in full.
- `../../researcher/01/evidence.md` — for the exact, accurate description of the 90.7% upper baseline.
- `../../writing-coach/01/voice-guide.md` and `../../editorial-direction.md` — voice and standard for any caption wording you touch.
- The article: `.nb-work/what-could-go-wrong/situational-awareness/library/what-could-go-wrong/situational-awareness.html`

Output: `draft-handoff.md` (this directory), one line on the fix applied.

Proof (run from `/home/user/the-nightly-build`, finish with links until `BLOCK: 0`):

```
./nb check .nb-work/what-could-go-wrong/situational-awareness/library/what-could-go-wrong/situational-awareness.html --series what-could-go-wrong --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

Also, while here, set nb-meta `model` to `Claude Opus 4.8` (shelf's readable
form) if it currently reads otherwise, and re-run `nb stamp`.
