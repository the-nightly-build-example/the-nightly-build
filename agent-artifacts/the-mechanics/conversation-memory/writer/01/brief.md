# writer brief: the-mechanics/conversation-memory (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt.
- ../../commission.md — the behavior, the angle, source direction, nb-meta values.
- ../../writing-coach/01/voice-guide.md — how this piece should sound; read before drafting.
- ../../researcher/01/evidence.md — the complete claim set; cite only from it.
- ../../../../.nb-context/ — the effective template contract and runtime assets.
- ../../../../library/the-mechanics/conversation-memory.html — the initialized article to edit in place.

Output: ./draft-handoff.md

Proof (run from repo root; iterate --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-mechanics/conversation-memory/library/the-mechanics/conversation-memory.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/53d4ed2b-ac4b-53e6-97a0-447483501c29/scratchpad/library-checkout --no-check-links`
- Final: same WITHOUT `--no-check-links`, and run `./nb stamp` first, until `BLOCK: 0`.

nb-meta: date `2026-08-11`, harness `claude-code-routine`, model `Claude Opus 4.8`,
three descriptive tags in nb-meta directly. Keep nb-meta `dek` identical to the
rendered dekline.

This round's focus: work backward from the behavior ("it remembers what I said")
to the stateless resend, in a short list of steps taught completely, each step
marked settled or product-dependent. No code. Do not drift into tokenization or
positional encoding. Link `the-mechanics/prefill-and-decode`, `the-mechanics/knowledge-cutoff`,
`the-mechanics/retrieval`, and `the-instruments/context-window` in Background
rather than re-teaching them, and draw the clean distinction from knowledge-cutoff
(training freeze) versus this (a live conversation). Link only already-published
library pages — do NOT link tonight's siblings.

Orchestrator correction to the evidence record (course placement only, not
mechanism): the evidence record states that only `the-mechanics/word-order` is
published and the neighbor lessons are not. That is an artifact of an incomplete
`nb history` index, not the truth. The pages `the-mechanics/prefill-and-decode`,
`the-mechanics/knowledge-cutoff`, `the-mechanics/retrieval`, and
`the-instruments/context-window` ARE published in `origin/library` and are valid
Background link targets, as the commission directs. Link them. Your own
`nb check` (links included) is the safety net: if any specific link does not
resolve, drop that one. The researcher's mechanism findings stand; in particular
present "memory features store facts outside the weights" as reasoning from the
cited pages, not as a quotation, and cite the Anthropic memory-tool page (not the
gated OpenAI FAQ) for the product-memory mechanism.

Habits not to inherit (house formulas across the last three of every desk):
- No "By the end you will be able to..." close on the opener.
- No second-person "now you know which of the two you are looking at" takeaway,
  and no portable "next time, ask..." checklist.
- Critical for this desk: do NOT write the verbatim catchphrase "The mechanism is
  settled. What is not settled is..." — it appears in two of the last three
  the-mechanics pieces and is the single most-worn line in the section. Mark
  settled-versus-open where the material needs it, in this lesson's own words,
  and never as the closing beat.
- The-mechanics' recent openers all use a second-person twin-example contrast
  ("'The dog bit the man' and 'The man bit the dog'..."); the recent deks all use
  a two-clause "..., and [the catch]" mold. Do not reuse either shape. Vary
  headings away from the desk's full-declarative-sentence heading habit and the
  "...too" additive tail.
- No "this desk" self-reference.
