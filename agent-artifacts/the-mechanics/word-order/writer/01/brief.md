# writer brief: the-mechanics/word-order (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and boundaries.
- `../../editorial-direction.md` — house standard, voice, series prompt, slop rules.
- `../../writing-coach/01/voice-guide.md` — how this piece should sound; reread before drafting and before every revision.
- `../../researcher/01/evidence.md` — the complete set of claims available to you; the Numbers section is exact.
- The initialized article and its template context under the workspace (edit the article in place; do not recreate its skeleton).

Output: `draft-handoff.md` (this directory). The article you edit is
`.nb-work/the-mechanics/word-order/library/the-mechanics/word-order.html`.

Proof (run from the checkout root `/home/user/the-nightly-build`, iterate with
`--no-check-links`, finish with links until `BLOCK: 0`):

```
./nb check .nb-work/the-mechanics/word-order/library/the-mechanics/word-order.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/632ac40d-a33e-56d6-bd33-4716eafda51c/scratchpad/library-checkout
```

Two seams the evidence flags — respect both (do not write around them):
- The clean "self-attention cannot tell word orders apart" claim is exact for an
  *unmasked* attention layer. A causal decoder gets some position for free from
  the causal mask (Haviv et al.). Teach the order-blindness on the attention
  operation itself, and link `the-mechanics/autoregressive-generation` for the
  mask rather than re-teaching it, so the claim stays true.
- RoPE being a relative scheme does not mean it extrapolates. It degrades past
  its trained length in practice, which is why interpolation/YaRN exist. Teach
  length extrapolation as open and engineered-around, not solved.

Recent habits to break (this desk and its siblings, last run):
- Openers lean on "Every [behavior] you have seen…" and close the Why card on
  "By the end you can look at any … and say which…". Write the promise in this
  lesson's own terms, off that mold.
- The last two mechanics lessons both hinged on a clean two-way split. This piece
  is a descent from the behavior to the mechanism that supplies order, marking
  settled vs open — keep it a descent, not an A-vs-B.
- Do not close on the second-person "Now you know which one you are looking at."
- Do not reuse "None of this makes X worthless/fake." Vary any note label; do not
  default to "In plain language."

nb-meta: set `harness` to `claude-code-routine` and `model` to `claude-opus-4-8`
(the writer ran on Opus), matching the library's existing convention. `nb stamp`
writes the counts.

Source-asset note: the evidence flags ALiBi Fig. 1 (extrapolation curves) and
Fig. 3 (distance-bias mechanism) as verified candidates, and warns the popular
sinusoidal heatmap is not a verified Vaswani figure — do not use an unverified
image. Use an asset only if the argument spends what it shows.
