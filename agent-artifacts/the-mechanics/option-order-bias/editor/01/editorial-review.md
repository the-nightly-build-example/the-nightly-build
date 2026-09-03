# Editorial review: the-mechanics/option-order-bias (editor/01)

## Skeptic

Thesis: a model's choice among fixed multiple-choice options changes when the
options are reordered; the effect is robustly measured, but which of three
parts of the system drives it is genuinely unsettled. The claims it stands on:

1. The reorder moves the pick, and the effect generalizes. Held. Pezeshkpour &
   Hruschka show a single GPT-4 flip and a best-vs-worst gap of ~13 to 75 points
   across five benchmarks, with GPT-4 still swinging 13.1 despite >90% accuracy;
   Zheng et al. show llama-30B moving 53.1 -> 68.2 (answer forced to A) -> 41.2
   (forced to D); Wei et al. reproduce it independently. All three checked against
   the owning primaries via the printed hrefs (s1, s2, s3), which resolve.

2. There are three distinct causes, and none is the sole cause. Held. Position
   weighting (Liu, primacy/recency, owned on long-context retrieval and carried to
   options as a conjecture), the prior on the A/B/C/D label tokens (Zhao's
   common-token bias; Zheng's token bias), and the scoring probe that decides what
   counts as the answer. The draft never lets one stand alone: the position section
   ends "it has a rival," the letters section stages the direct Zheng-vs-Pezeshkpour
   contradiction, and the note lands "The behavior is settled. Its decomposition is
   not." This is the round's central requirement, and it is met.

3. The scoring probe is a real third cause, not a footnote. Held, and it earns its
   own section. First-token/option-ID probability disagrees with the generated
   answer 56.8% (Gemma-7b), 51.4% (Llama2-7b) and 10.2% (Mistral-7b) per Wang et
   al.; a second group (s8) puts the aggregate above 60%. I confirmed against s8's
   abstract that "over 60%" and "worst on models most heavily fine-tuned on
   conversational or safety data" are both stated there, and that the draft uses
   only that abstract-level aggregate, never an unverified per-model figure from s8
   — exactly as the brief required. The HF three-way MMLU table (0.636 / 0.637 /
   0.488, "not at all comparable") verified against s9.

Display text checked descriptor by descriptor: headline (GPT-4 flipping on a
reorder is precisely Pezeshkpour's Fig. 1), dek (13-75 across five benchmarks;
the two papers split on position vs letters — a claim about the world, not a
grade of the article's method), every subhead, the stat strip, and both position
cards. All nine `data-nb-kind` labels hold (8 primary, 1 secondary; meets the
commission's 8/>=4/>=1 floor). Every citation href opened as printed; all nine
land on the cited source, and the three internal sibling-lesson links
(prompt-sensitivity, word-order, instructions-are-data) exist in the library.

One paraphrase drift found and fixed: the Pezeshkpour position card read "more
than one choice could be right over 94% of the time," where the source (and the
body prose) say "highly probable." Aligned the card to the source. One
observation left as-is: the stat strip's +15.2 does not equal the rounded
68.2 - 53.1 = 15.1 in the prose; both figures are Zheng Table 1's own (the paper
reports the delta directly), so this is source rounding, not an article error,
and not mine to alter.

prompt-sensitivity is linked (Background row and body), not re-taught. The piece
reaches ground in the takeaway (the token sequence becomes a next-token
preference; no order-free answer sits underneath) and stops there.

## Cut

Ran the slop pass over body, display text, and furniture prose. Six sentences
failed and were cut or repaired; the recurring pattern was edge-of-passage
signposting and self-reference.

- Why-this-matters closed on the flagged formula (a "This lesson works back...,
  names..., and is honest about..." method list) plus self-grading ("is honest
  about"). Rewrote it to land the payoff in the piece's own particulars.
- The orientation section signposted its own structure ("The rest of this lesson
  takes them one at a time..."), which the body may not do; cut.
- The letters section opened on a framing phrase ("The narrow point here is
  that...") and closed a clause on a stray "tonight"; both removed.
- "This is where the two headline papers collide" reported where the argument
  stood without doing the reasoning; cut, since the quote and the "argue against"
  clause deliver the collision and the two position cards show it.
- "In plain engineering terms" (throat-clearing) and "Here it is enough that"
  (filler frame) trimmed.

Two reflex-punctuation repairs: a semicolon splitting one thought in the position
section became a period; a semicolon joining a fragment to a clause in the table
caption became a colon. Grammar repair: the prompt-sensitivity link sentence
("That scoring can move a score as much as the answer has its own lesson")
garden-paths and asserts an unquantified comparison; rewritten to a clean line
that keeps the link and does not re-teach.

Checked distinctive phrasing against the voice-guide quotations (Karpathy, Olah,
Evans): no borrowed clauses. Checked authored text against the commission and
briefs for leakage: the only lifted framing was the "works back / names / is
honest" preview, now rewritten. Edges, headings, dek, and furniture checked
against the recent-pattern notes: the dek avoids the semicolon reversal,
suspended question, and comma triad; headings are built in the piece's own nouns
and vary in construction (no reflex "reveal" declarative); the takeaway does not
close on a stamped present-tense one-liner. No banned lexical terms; zero
em-dashes.

## Reader

Read straight through as the paper's reader, the article and nothing else: I come
away able to say why a reorder moves the answer — position in the token sequence,
the pull of the A/B/C/D tokens, and the scoring rule that decides what counts as
the answer — and, importantly, able to tell that a leaderboard gap can reflect
answer format rather than what the model knows. No single source gives that; each
owns one piece, and the article braids them into one causal walk with the
settled/open line drawn where the two headline papers actually diverge. The
original-work sentence claims exactly this composition, and it survives the
comparison: the record lists the pieces and the disagreement but never composes
them. The prose sits closer to the voice-guide exemplars than a median summary —
each part is named in plain words as it appears, inference is marked as inference,
and the scoring section makes the honest "some of this belongs to the ruler, not
the model" move. Headline reread as the largest claim: true, concrete, and
defended by the piece.

## Edits

- Rewrote the Why-this-matters closing sentence off the "This lesson..." method
  list and self-grading onto the piece's own particulars.
- Cut the orientation signpost "The rest of this lesson takes them one at a
  time, and marks which parts are settled and which are still open."
- Cut "The narrow point here is that" and the stray "tonight" from the letters
  section's first paragraph.
- Cut the signpost "This is where the two headline papers collide."
- Pezeshkpour position card: "could be right" -> "could be highly probable" to
  match the source and the body.
- Position section: reflex semicolon -> period ("...where a token sits. The
  position of each one...").
- Table caption: semicolon -> colon ("...scored three ways: the numbers are...").
- Cut throat-clearing "In plain engineering terms,".
- Rewrote the prompt-sensitivity link sentence for grammar and cut the "Here it
  is enough that" frame before the scoring section's conclusion.

## Required work

- orchestrator: re-stamp before the PR. The cuts removed roughly fifty words, so
  the `nb-meta` `words` field (2189) is now stale; a re-stamp brings the count and
  reading time back in line. This is the mechanical stamp step, not a further
  editorial round.

Optional, non-blocking (writer, holds the asset tooling): Pezeshkpour's Fig. 1
(GPT-4 flipping "hen house" to "outside bedroom window" on a reorder) would make
the opening worked case land visually, in the voice guide's smallest-concrete-case
register. The prose case stands on its own, so this is a suggestion, not a
condition.

## Decision: approve

The central reckoning holds, every figure and link verifies, and the slop,
formula, and clarity issues were mine to fix and are fixed; only a routine
re-stamp remains.
