# writer brief: the-mechanics/agent-loops (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — the assignment, the cause chain to reach ground, and the post-research angle refinement. Read the refinement closely.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — reread before drafting.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — the complete claim set; use the Numbers section exactly.

Output:
- /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/agent-artifacts/the-mechanics/agent-loops/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/library/the-mechanics/agent-loops.html --series the-mechanics --repo /home/user/the-nightly-build

Article file to edit:
/home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/library/the-mechanics/agent-loops.html

Work from these inputs. Do not tour the repository or archive. Ask the
orchestrator if you need something the record does not carry; do not invent or
expand the claim set.

## This round's focus

- No code listings. Explain the loop in prose, a numbered-steps component, or a
  table.
- Work backward from the behavior to ground, naming a real part of the system at
  each step, with the SWE-agent concrete case (per the refinement) making it
  land. Mark settled engineering vs open questions.
- Honor the angle refinement precisely: do not round Huang et al. to "models
  cannot self-correct" (it is about signal quality: oracle signal helps,
  intrinsic often does not); acknowledge greedy decoding as a contributor and
  draw the exact line to the-mechanics/repetition-loops; present the "ground"
  proposition and the temperature point as the lesson's synthesis (link
  the-mechanics/sampling-temperature); mark "why models under-weight their own
  error feedback" as open. Avoid a fragile harness-cap number.
- Put the one-sentence original-work claim in draft-handoff.md and make that work
  visible on the page.

## Recent shapes to break (the-mechanics)

- Recent openers: "Chatbots are good at sounding like ..." (hangman), "You have
  probably noticed ..." (answer-length-bias). Do not default to those.
- Do not close the opener on "By the end you will know A, B, and C."
- hangman's dek is a compact causal sentence ("... stop agreeing because a plain
  chat stores nothing between turns ..."). Build this dek differently; do not
  copy that mold.
- Check headings against recent the-mechanics pieces so they are not stamped.

## Craft reminders

- Lesson form: Why this matters, body, The takeaway. Body first; bookends after,
  addressing the reader, no citations. The body speaks to no one and never
  mentions the lesson.
- Teach a short list of ideas completely; each a plain statement, a concrete
  example, and why it matters here.
- Cite per-section (why/takeaway exempt). Number sources in first-citation order;
  carry data-nb-kind from the evidence record; prefer real locators over
  homepages. Link the named earlier lessons in Background (tool-use, react,
  conversation-memory/hangman, repetition-loops, sampling-temperature) at first
  use in prose; do not re-teach them.
- Fill nb-meta: harness "Claude Code (nb-orchestrator edition)", model the one
  you run as, real dates for 2026-09-26. Run `nb stamp` then the exact proof
  above until BLOCK: 0 (use --no-check-links while iterating; full check before
  handoff). Confirm nb-meta dek and rendered dekline are identical.
- Check headline/dek/subheads against the evidence record, spec/headlines.md,
  and spec/slop.md before handoff.

Write draft-handoff.md with the original-work sentence, the proof result (and any
warning left on purpose with its reason), and any open question. Report the
handoff path and any warning left.
