# writer brief: the-evidence/batch-normalization (02)

Apply the one required item in `../../editor/01/editorial-review.md` (Required
work, owner: writer). The editor's own cuts are already in the article; change
nothing else.

The fix: the takeaway closes on an engineered antithesis coda — "The technique is
not in doubt. The explanation printed in its title is." The voice guide directs
the "not X, it's Y" contrast to be earned once, on the mechanism, and explicitly
NOT in the takeaway; the draft landed it twice. Reland the takeaway's ending on
the finding the lesson already established — batch norm works and delivers its
numbers, while the internal-covariate-shift reason the paper's own title gives is
the part a controlled test overturned, with no agreed replacement — without the
"not X / it's Y" coda and without inventing a new closer formula. Keep the
technique's intact standing clear. The takeaway must still teach nothing new and
resolve the opener. Touch only the takeaway ending; add no claim.

Inputs:
- `../../editor/01/editorial-review.md` — the required item in full.
- `../../writing-coach/01/voice-guide.md` — the register, and where the one earned contrast belongs.
- `../../editorial-direction.md` — house standard and the takeaway rules.
- The article: `.nb-work/the-evidence/batch-normalization/library/the-evidence/batch-normalization.html`

Output: `draft-handoff.md` (this directory), one line on the reland.

Proof (run from `/home/user/the-nightly-build`, finish with links until `BLOCK: 0`):

```
./nb check .nb-work/the-evidence/batch-normalization/library/the-evidence/batch-normalization.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

Run `nb stamp` after the edit. nb-meta `model` should read `Claude Opus 4.8`.
