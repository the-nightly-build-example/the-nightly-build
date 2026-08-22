# Editorial review: the-mechanics/overused-words (editor/01)

## Skeptic

Thesis: a small set of style words spiked in published text after late 2022; the
step that concentrated them (post-training) is settled, but which words it landed
on is unknown, and the popular annotator-dialect explanation failed the one direct
test run on it — so the words flag a shifted population and can name no single
document.

The claims it stands on, tested:

- The measured spike (Kobak; Liang peer reviews). Held. Kobak's 14M-abstract
  counterfactual method, the post-ChatGPT abruptness, and the largest-ratio style
  words (delves, underscores, showcasing) match the evidence record. The arXiv
  page for Kobak now serves the revised version (13.5%, up to 40%, "over 15
  million"); the article deliberately cites the June-2024 v1 figures (10%, up to
  30%, 14M), calls them a moving lower bound, and states a later version revised
  them upward. That is exactly the "cite one version, flag the drift" handling the
  evidence record prescribes, so it holds and stays provable, though a reader
  clicking the link lands on the higher numbers — the article's own sentence
  ("A later version revised it upward") covers that.
- The proximate mechanism (next-token draw). Held; taught elsewhere and linked,
  not re-argued.
- The settled cause (post-training narrows the output distribution; Kirk). Held.
  Stated flatly as the settled core and cited to the base/SFT/RLHF diversity
  comparison, not blurred into the open question.
- The open question and the failed hypothesis (Juzek & Ward; Hern; Willison).
  Held at its real weak strength: one direct ICE test that did not support the
  dialect hypothesis, one indirect surprisal test only "consistent with" a
  between-model factor and unable to isolate rater dialect, with "delve" behaving
  unlike the other focal words. The abstract confirms the "delve behaves
  differently" and RLHF-consistency framing firsthand; the ICE "did not support"
  line is the researcher's verified verbatim quote. The article does not let the
  hypothesis read as the answer, and does not soften it to "merely unconfirmed."
- The detection consequence (Liang detectors; Sadasivan). Held. Population-level,
  correlational, no per-document verdict; defeatable by paraphrase; a distribution
  not a watermark; human writing converging. Abstract-only figures (Sadasivan
  99.3%->9.7%, per-word Kobak ratios, InstructGPT alignment-tax) are kept
  qualitative, as briefed.

Display text: headline, dek, and every subhead re-verified as claims. One
descriptor was wrong. The Liang table caption and its lead-in sentence pinned the
adjective multipliers to "the year before" / "the 2023 reviews." The Liang paper
reports the fold-increases for ICLR 2024 without defining the baseline as the
immediately prior year, and ICLR 2023 reviews straddle ChatGPT's launch, so "2023"
was precision the source does not carry. Recast both to "before ChatGPT" (change
logged below). data-nb-kind audit: 6 primary (Kobak, Liang x2, Juzek & Ward, Kirk,
Sadasivan), 2 secondary (Hern/Guardian, Willison) — all correct against the
primary/secondary test; the two secondaries are the journalistic origin and its
retelling and own no measurement. arXiv hrefs (s1-s4, s7, s8) opened and land on
the sources themselves; the Guardian slug carries the source's own "gadgest" typo
and is the real address (gated to automated fetch), and the writer's full
link-check returned BLOCK 0.

Ouyang judgment call (flagged in the handoff): correct as the writer left it. The
RLHF recipe is taught mechanics, linked to the-evidence/instructgpt per the "link,
never a numbered source" rule; the settled narrowing claim rests on Kirk, who is
cited. No claim rests on Ouyang, so no numbered citation is owed. 8 sources, policy
met.

## Cut

Three sentences failed the slop test and were cut, all at section edges:

- "Start where the claim can be checked." — a method signpost that also addressed
  the reader in the body (the lesson body speaks to no one; only the bookends do).
  The section opens cleanly on Kobak's measurement.
- "Here the reader's first question gets its answer." — self-reference, a gesture
  at a hypothetical reader, and a signpost describing where the piece had gone,
  all at once. The posed question after it carries the section.
- "It is an appealing story, and it has a real problem." — the "it is an appealing
  X, and it has a real Y" shape, and redundant with the two prior sentences that
  already show the story spread. Replaced with a plain "But" onto the failed test.

One borrowed clause: "measured crudely by frequency and nothing more" lifts Mark
Liberman's exact voice-guide phrase ("measured crudely by frequency in the Medline
corpus"). The point underneath — these are blunt frequency counts — is the
article's own, so I rewrote it in the article's terms rather than cut it. Two more
body-voice fixes: the imperative reader-address "Go up one level" recast to a posed
question, and "cannot tell you" to "cannot show." One grammar break fixed: "Two
independent corpora ... is" -> "are."

No repeated formula in the edges or headings after edits. The five section headings
each name a step in the piece's own nouns and skim as the argument; none is a
scaffold slot, and there is no "What's settled / What's open" heading. The overused
words appear only as quoted data, including at the edges — the piece does not
perform them.

Furniture: the body-closing "Verdict" note was removed. press/editorial.md is
explicit that a lesson lands its judgment in the takeaway bookend and must not
close the body with a Verdict note or any block that restates the finding; this one
restated, nearly sentence for sentence, what the takeaway bookend already lands.
Removing it resolves the violation and the redundancy. What remains is one table
(the Liang multipliers, which genuinely corroborate a second corpus) plus the two
bookends — furniture that does work, not a stack.

## Reader

What the piece gives beyond its sources: a single unbroken backward chain — counted
spike, to the sampler's draw, to post-training's measured narrowing as the settled
cause, to the specific-word question fixed at its true weak strength, to the
population-level limit on any per-document verdict — that no one source draws. The
draft-handoff's original-work sentence claims exactly this welding, and it survives
the read. The prose sits closer to the voice-guide exemplars than to a median
summary: it reports each figure with how it was obtained, marks settled from open
in plain voice without a labeled box, and lands its judgment on checkable facts
rather than on the writer's confidence. The headline, now a single committed claim,
reads as the largest claim the piece defends.

## Edits

- Rewrote the headline (title tag, nb-meta title, and h1, kept in sync) from the
  two-sentence "The 'delve' spike is real. The popular reason for it failed its one
  test." to "Chatbots overuse 'delve,' and the popular explanation for it failed
  its one direct test."
- Cut "Start where the claim can be checked." (orientation opener).
- Changed the Liang lead-in from "rare in the 2023 reviews" to "rare in reviews
  from before ChatGPT."
- Changed the Liang table caption from "than the year before" to "than in the years
  before ChatGPT."
- Rewrote "These are counts, measured crudely by frequency and nothing more." to
  "These are counts and nothing more, a blunt tally of how often a word shows up."
- Fixed "Two independent corpora ... is still hard to wave off" to "... are hard to
  wave off."
- Recast the-draw opener "Go up one level, to how the words reach the page at all."
  to "How do the words reach the page in the first place?"
- Cut "It is an appealing story, and it has a real problem." and bridged the next
  sentence with "But."
- Cut "Here the reader's first question gets its answer." (detection opener).
- Changed "cannot tell you that any one abstract" to "cannot show that any one
  abstract."
- Removed the body-closing "Verdict" nb-note-strong block.

## Required work

None. All items were resolved by direct edit. The orchestrator stamps before the
PR (nb-meta word count and reading time will recompute then); a `--no-check-links`
run after these edits returns BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve — the settled/open seam holds, the numbers and citations check out, the
forbidden body-closing Verdict is gone, the headline is a single committed claim,
and the slop and voice fixes were all within editing reach.
