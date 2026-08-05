# Editorial review: the-evidence/atari-dqn (editor/01)

## Skeptic

Thesis: the famous phrase "human-level control" carries more than the DQN
paper's own tables support; the paper's durable contribution was two
stabilization tricks that first made a neural network trained by Q-learning
converge, not a machine that understood the games.

The claims it stands on, and how each held:

- **Headline, "29 of the 49 games" on the 75% bar.** Held. The paper
  operationalizes human-level as reaching at least 75% of the way from random
  up to the professional tester and reports 29 of 49 clearing it. The
  researcher reproduced the count from Extended Data Table 2; the article
  cites the figure and the operational-definition quote to the primary
  (p. 531). I tried to break this by reading the quote in context: the 75%
  reading is the paper's own, not the writer's gloss. It holds.

- **Dek, "the human was one professional games tester ... about twenty short
  sessions."** Held against Methods; the article restates it in the body
  ("about twenty sessions of up to five minutes each"). This is a claim about
  the world, not a grade of the article's method. It does not use the
  recently-worn "the paper never did X" mold, and it is a two-clause line, not
  the banned comma-triad.

- **The two-trick attribution (the correction that mattered most, so I pushed
  hardest here).** Held and correct. Experience replay is attributed to the
  2013 precursor (arXiv:1312.5602, cited at Sec. 4.1 / Algorithm 1); the
  separate periodically-cloned target network is attributed to the 2015 Nature
  addition, with the paper's own "every C updates we clone the network Q"
  quote and the note that the 2013 version had no frozen copy. I checked the
  opposite failure mode (that the piece might credit both tricks to "the
  paper") and it does not.

- **The ablation, 316.8 -> 3.2.** Held. Table rows (316.8 / 240.7 / 10.2 /
  3.2) match the evidence record's Extended Data Table 3 figures. The prose
  claim "removing experience replay alone collapsed the score about
  thirtyfold" checks: replay off with the target network on is the 10.2 row,
  and 316.8 / 10.2 = 31. "Removing both dropped it to the floor of random
  play" is fair for 3.2.

- **Montezuma's Revenge = 0.** Held. DQN 0, tester 4,367, random 0, so 0.0% of
  human, cited to Extended Data Table 2. The value-learning explanation (an
  action never rewarded is never reinforced) is reasoning shown, not asserted.

- **Henderson et al. 2018 scope.** Held and precise. The article states its
  tests were policy-gradient methods on simulated robot control, "not DQN and
  not Atari, so this is not a measurement of DQN's own runs," and uses it only
  as evidence about the field DQN founded. No drift.

Source decisions confirmed:

- **(a) Sutton & Barto swap.** The printed href
  (`.../10-703/textbook/BartoSutton.pdf`) resolves under the live link check
  (no link warning). The file is too large to fetch inline, but it is the same
  2nd edition, and the locator "Sec. 6.5, Eq. 6.8" is edition-stable and was
  cited independently by both researcher and writer. Accepted.

- **(b) Agent57 retrospective (s7).** Labeled primary and attributed in prose
  as "DeepMind's own retrospective is blunter," so it never reads as
  independent confirmation. The desk source floor (>= 3 primary, >= 1
  secondary) holds without leaning on it: four other primaries (s1 Nature, s2
  Sutton & Barto, s3 2013 precursor, s5 Henderson) and two secondaries (s4
  NBC, s6 MIT Technology Review). Accepted.

Other checks: gradient descent is a plain in-prose link to
the-mechanics/gradient-descent at first use, not re-taught; no AlphaGo tree
search or self-play is imported, and the piece states plainly that DQN holds
no model and searches nothing. Display text verified descriptor by descriptor
(49 games, the 75% and 100% thresholds and their 29/23 counts, the stat strip,
the Breakout ablation, Montezuma 0) against the evidence record. Headings are
argument steps and vary in shape; none use the comma-and-"and" cadence. No
break retired a claim.

## Cut

The draft was 2305 words, over the 2200 lesson-band ceiling (a live
W-LENGTH-HIGH warning). I brought it to 2193 by removing what did not earn its
place, taking nothing from the three worked ideas. The cuts fall into three
kinds:

- **Signposts describing where the piece goes:** "Start with the decision the
  network made tens of millions of times," "Return to the headline," "Start
  with what the scores cost," and the rhetorical "So where does the citation
  break?" Each announced a move the next sentence already made.

- **Restatement:** a second orientation sentence naming Space Invaders /
  Breakout / Boxing that repeated "one fixed set of hyperparameters ... 49
  games"; a target-network paraphrase already carried word-for-word by the
  paper's own quote right after it; a Henderson sentence ("the results
  differed enough to form statistically distinct groups") that the t/p numbers
  in the next sentence state exactly; and a citation-break bridge ("the
  paper's own tables describe something narrower") that the following sentence
  elaborates.

- **Soft tails and an editorial flourish:** the Montezuma paragraph's closing
  restatement ("value learning could not take the first step toward a point it
  had never seen"), which softened the harder line before it ("an action that
  is never rewarded is never reinforced"); a bootstrapping-paragraph tail
  re-derived in full in the next section; and "which rests on shakier
  foundations than its headline numbers suggest," an unearned tail on the
  Henderson point.

The worst tell was the reflex signpost opening a paragraph with a direction
rather than a fact. No repeated cross-article formula survived into the piece.
The one hedged-contrast in the body ("not that a network reached some
particular score, but that these two changes made ... stop diverging") is
earned: it corrects the real misreading the whole lesson is about, and it is
the only one. I ran nb stamp; the file now reads 2193 words, 10-minute read,
and the body byline still matches.

## Reader

Read straight through, the piece gives a reader what the sources alone would
not: the paper's own operational definition and Extended Data Table numbers
set directly against the phrase everyone quotes, plus a worked reconstruction
of why a value-based agent scores exactly zero on Montezuma's Revenge. That is
the draft-handoff's original-work claim, and it survives the read intact. The
prose sits closer to the voice-guide exemplars than to a median summary: it
builds the naive network, shows the two named failures, and introduces each
trick as the removal of one (the Olah engine), and it seats the reader inside
one Breakout decision (the licensed Karpathy "you"). The numbers convict the
phrase without a verdict adverb. The headline, reread as the largest claim,
still commits to what the body proves: 29 of 49, on a bar the piece defines.

## Edits

- Cut orientation signpost "Start with the decision the network made tens of millions of times."
- Cut redundant orientation sentence naming Space Invaders, Breakout, and Boxing.
- Cut bootstrapping-paragraph tail "That self-reference is exactly what makes the plain version fall apart."
- Cut target-network paraphrase "Refresh it only every C updates, by cloning the live weights into it." (carried by the quote that follows).
- Cut signpost "Return to the headline."
- Cut Montezuma soft tail "On its own, value learning could not take the first step toward a point it had never seen."
- Cut signpost "Start with what the scores cost."
- Cut Henderson restatement "The results differed enough to form statistically distinct groups."
- Cut Henderson editorial tail ", which rests on shakier foundations than its headline numbers suggest."
- Cut rhetorical signpost "So where does the citation break?"
- Cut citation-break bridge "The paper's own tables describe something narrower."
- Ran nb stamp: words 2193, reading_minutes 10, sources 7. nb check is BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

None. No item needs new prose, evidence, markup, or asset work.

## Decision

approve. The three corrections and both source decisions hold, display text is
accurate, and the cut read brought the piece within the lesson band (2193
words) without thinning any worked idea; the proof is clean.
