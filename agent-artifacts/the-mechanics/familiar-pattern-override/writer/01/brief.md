# writer brief: the-mechanics/familiar-pattern-override (01)

Inputs:
- ../../commission.md — assignment: backward causal chain, boundaries, the three
  neighbours to stay distinct from, habits to break.
- ../../editorial-direction.md — house standard, paper voice, series prompt, template identity.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only what it opened; Numbers section used exactly.
- article to edit: /home/user/the-nightly-build/.nb-work/the-mechanics/familiar-pattern-override/library/the-mechanics/familiar-pattern-override.html
- template context: /home/user/the-nightly-build/.nb-work/the-mechanics/familiar-pattern-override/.nb-context/

Output: ./draft-handoff.md

Proof (from repo root /home/user/the-nightly-build, links included, until BLOCK: 0):
  ./nb check .nb-work/the-mechanics/familiar-pattern-override/library/the-mechanics/familiar-pattern-override.html --series the-mechanics --library .nb-work/library
Run ./nb stamp before the final check.

This round's focus and corrections to the commission (the evidence overrides it):
- The commission's anchor said the trick "fades on obscure puzzles." No study
  tested that directly; it is only an inference from general frequency-effect
  research (Razeghi et al.; McCoy et al.). Do NOT state it as measured. Either
  frame it explicitly as an inference from frequency effects, or drop it. Do not
  build the anchor on an untested claim.
- The "reasoning training partly fixes it" side of the open question is NOT clean:
  Jang et al. (PuzzleTrivial) show a reasoning-trained model overriding a stated
  condition MORE than its base model in worked examples. Present the open question
  honestly — reasoning training does not cleanly fix this and can worsen it. Note
  Jang et al.'s Tables 2-3 numbers were not reliably extractable, so cite its
  worked examples, not those tables (the record marks this).
- Keep the mechanism the spine: a strong memorized prior (the canonical puzzle and
  its answer appear many times in training) can dominate a lightly-changed prompt.
  Mark settled (models complete high-probability familiar patterns) vs. open (what
  this proves about reasoning; whether training fixes it).
- Keep sharply distinct from the published neighbours: irrelevant-context (adds a
  true-but-useless sentence to an intact problem), memorization (verbatim recall),
  prompt-sensitivity (rephrasing changes the answer). Link them; do not re-teach.
  Confirm library URLs via a specific ./nb history query if needed. No code.
- Ground in real cited examples (the AIW collapse; a modified-classic-puzzle
  result). Break the recent habits the commission lists; give the open-question
  section a heading in this behaviour's own nouns, not a stock reasoning-boundary
  heading. Outline the reasoning before naming sections.

nb-meta fields to fill: "date": "2026-09-20"; "harness": "claude-code"; "model":
your exact running model ID (capable-tier this run; if unknown use
"claude-sonnet-4-5"); "tags": 3-5 concrete topical tags; "dek": identical to the
rendered dekline. ./nb stamp writes counts.

Do not tour the repository or expand the claim set. If a needed fact is missing,
return a precise researcher request. Report the draft-handoff path, the
original-work sentence, the final BLOCK count, and any gap.
