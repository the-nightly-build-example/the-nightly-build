# editor review-brief: the-evidence/direct-preference-optimization (01)

Inputs:
- Editorial direction: ../../editorial-direction.md — house standard, paper voice, series prompt.
- Commission: ../../commission.md — the assignment, boundaries, and the reader's situation.
- Writer brief: ../../writer/01/brief.md — the exact instructions the writer worked to.
- Voice guide: ../../writing-coach/01/voice-guide.md — the exemplar passages the writer read before drafting.
- Evidence record: ../../researcher/01/evidence.md — the claim set behind the draft.
- Draft handoff: ../../writer/01/draft-handoff.md — the original-work sentence and proof result.
- The article: ../../../../library/the-evidence/direct-preference-optimization.html
- Template context: ../../../../.nb-context/

Output: ./editorial-review.md (editor/01/editorial-review.md)

Proof (for your verification if needed; the writer owns running it): from repo root —
`./nb check .nb-work/the-evidence/direct-preference-optimization/library/the-evidence/direct-preference-optimization.html --series the-evidence --library /tmp/claude-0/-home-user-the-nightly-build/b1bf3c94-3553-5519-8a12-b9ebb7eba930/scratchpad/library-checkout`

## Recent-pattern notes (compare edges, deks, headings against these `the-evidence` tics)

- Dek: the "[Researcher] did A, and that/then [the part it leaves out]" mold
  (named authors up front + comma-and reversal).
- Headings: "X did A, then/never B" reversal; possessive "the paper's own
  [test/hedge]"; "Where the X comes from."
- Opener: the arXiv-upload moment; "comes from a single paper."
- Closer: "the difference between what was named and what was proved"; the
  reader-directed "the next time... the useful question is."
- Diction: "the difference between...", "outran what it proved", the two-beat
  reversal ("The scale did not vanish. It moved."), the "What it named.../What it
  established..." antithesis. Cross-series: "By the end you will be able to...",
  "The next time..., ask...", "honest" as a virtue word.

## This round's focus

- The verdict is a split one (DPO's method sound and widely adopted, but "equals
  PPO" qualified). Check that both halves are earned from the evidence and that
  the takeaway lands it without a Verdict block.
- Display-text and figure check: the writer stated DPO's code result
  qualitatively ("close to zero") because the evidence record's 3.2% did not
  match the paper's table (~0.0%); confirm the printed figures (PPO 22.4%
  CodeContests, AlphaCode 16.4%, human-eval PPO 45 to DPO 29, Zephyr MT-Bench
  7.34) against their owning primaries, and confirm the dialogue Best-of-128
  substitution caveat is present and accurate.
- Confirm the closed-form idea is conveyed in plain words (no algebra creeping in),
  and that InstructGPT / deep-rl-from-human-preferences are linked, not re-taught.
