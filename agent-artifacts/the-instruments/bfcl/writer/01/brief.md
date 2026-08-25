# writer brief: the-instruments/bfcl (01)

Inputs:
- editorial-direction.md (artifact root): house standard, voice, lesson
  template rules, the-instruments series prompt.
- commission.md (artifact root): the angle, scoring mechanics to convey, the
  "misled people" case, boundaries, and "Recent shapes to break."
- writing-coach/01/voice-guide.md: how this piece should sound.
- researcher/01/evidence.md: the complete claim set. Use its Numbers section
  exactly; address every item in its Contradictions in the prose.
- The initialized article to edit in place:
  .nb-work/the-instruments/bfcl/library/the-instruments/bfcl.html
- Template contract and furniture under
  .nb-work/the-instruments/bfcl/.nb-context/

Output: agent-artifacts/the-instruments/bfcl/writer/01/draft-handoff.md

Proof (from /home/user/the-nightly-build; iterate with --no-check-links, then
final with links):
  ./nb check .nb-work/the-instruments/bfcl/library/the-instruments/bfcl.html \
    --series the-instruments \
    --library /tmp/claude-0/-home-user-the-nightly-build/795ad1d0-7e30-55f8-9f00-32962f849f5d/scratchpad/library-checkout
Drive to BLOCK: 0. Run `./nb stamp <article>` before the final check.

This round's focus (decisions the inputs leave to you):
- The "misled people" case rests on the documented fact and scale of BFCL's
  own data corrections (e.g. a 2024-10-16 fix touching 547 of ~1,053
  live-multiple cases) plus the reliability gap the τ-bench numbers show. There
  is NO published before/after leaderboard delta tied to a specific
  correction; do not invent or imply one. Make the point from the correction's
  scale and from the single-call-vs-multi-step gap.
- Anchor the reader with a concrete score (e.g. the ICML Table 1 top model at
  66.4% overall, near-zero on agentic memory). Reconfirm any decimal cell you
  quote against the typeset table.
- Link (not re-teach) `tool-use`; contrast with `tau-bench` rather than
  re-explaining it.
