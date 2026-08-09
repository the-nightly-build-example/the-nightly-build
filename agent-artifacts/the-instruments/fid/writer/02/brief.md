# writer brief: the-instruments/fid (02)

Apply the one required item in `../../editor/01/editorial-review.md` (Required
work, owner: writer). The editor's own cuts are already in the article; change
nothing else.

The fix: the "Why this matters" bookend closes on a shelf-wide Formula — "By the
end you will be able to follow the calculation yourself and see which FID
comparisons carry weight and which ones only look like they do." Every recent
Instruments Why card closes on that same "By the end you [will/can] … claim and
…" mold, which `spec/slop.md` bans as Formula. Rewrite that closing promise in
FID's own particulars, off that shape. The lesson identity still requires the
opener to convey what the reader will understand by the end — so keep that
substance, but deliver it without the "By the end you will be able to…" cadence
and without the "which ones carry weight / which only look like they do"
antithesis. Do not touch anything else in the bookend or body; add no new claim.

Inputs:
- `../../editor/01/editorial-review.md` — the required item in full.
- `../../writing-coach/01/voice-guide.md` and `../../editorial-direction.md` — voice and standard for the rewritten sentence.
- The article: `.nb-work/the-instruments/fid/library/the-instruments/fid.html`

Output: `draft-handoff.md` (this directory), one line on the rewrite.

Proof (run from `/home/user/the-nightly-build`, finish with links until `BLOCK: 0`):

```
./nb check .nb-work/the-instruments/fid/library/the-instruments/fid.html --series the-instruments --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

Run `nb stamp` after the edit. nb-meta `model` should read `Claude Opus 4.8`.
