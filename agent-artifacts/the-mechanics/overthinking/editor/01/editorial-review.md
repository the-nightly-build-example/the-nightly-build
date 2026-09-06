# Editorial review: the-mechanics/overthinking (editor/01)

## Skeptic

Thesis: a reasoning model over-deliberates on easy inputs because reinforcement
learning rewarded reaching correct answers and, on the hard problems that
trained it, long chains were what got there; it kept no gauge of difficulty, so
on a trivial input the extra reasoning is wasted compute rather than a wrong
answer. Separately, extended reasoning can lower accuracy, but conditionally,
and on the hardest problems the failure inverts to underthinking. The settled
half (test-time compute scales with tokens; RL lengthened the chains) is marked
off from the open half (which of three framings fits, and every fix so far being
a hand-set length control).

The piece's whole integrity rests on not fusing two phenomena, so I pushed
there hardest, checking each figure against its owner.

- Trivial-input overthinking is kept as an efficiency cost, not a wrong-answer
  cost. The 901-tokens-over-13-solutions example, the first round already
  correct in over 92% of cases, and the MATH500 mitigation cutting tokens 48.6%
  while accuracy moved only 92.8% to 93.2%, all point the same way and none
  claims the model gets 2 plus 3 wrong. Held.
- The accuracy collapses are shown as conditional. They appear only on the
  constructed distractor/spurious-feature/constraint tasks (Opus 4 ~100% to
  85-90%; R1 ~70% to 30%), and the piece states plainly that accuracy is
  maintained under extended reasoning on standard arithmetic benchmarks. The
  "built traps" heading and the "boundary that headline erases" paragraph carry
  this. Held.
- The two cause attributions are kept distinct: the RL length reward for the
  wasted compute, and amplified flawed heuristics ("a cause separate from the
  length reward") for the accuracy drops. The settled-vs-open section names all
  three live framings and that none is proven. Held.
- The underthinking flip is present as a third mechanism (225% more tokens, 418%
  more thought-switches on wrong AIME answers; 70%+ of wrong responses hold a
  dropped correct thought), with the Zeng corroboration. Held.
- thinking-out-loud is linked in prose (and in Background), not re-taught;
  test-time compute is defined where it first appears. Held.

Breaks found and handled:

- Cause conflation in the orientation transition. "Both trace back to how these
  models were trained, so that is where we start" implied a shared training
  cause for both halves, which the piece itself later denies for the accuracy
  drops. Recast to "Both start from the same place, a model trained to reason at
  length," which locates the shared origin (a model that reasons at length)
  without asserting a shared proximate cause. Fixed directly.
- Training-vs-test-time conflation in the regime table. Row two read "Standard
  math benchmark ... A longer chain that works the problem through ... Accuracy
  holds or climbs (AIME first-try 15.6% to 71.0%)." That AIME figure is the
  accuracy climb over the RL training run, not what extending one answer's chain
  does at test time, so the table attributed a training-progress number to
  "what the extra tokens do." The body (chain-grew section) is careful here; the
  table was not. Replaced the effect with the genuine test-time result the row's
  label promises, "Accuracy is maintained as the chain grows," sourced to the
  inverse-scaling paper (s3), and dropped the now-unused s2 from the caption.
  The AIME climb still lives, correctly framed, in the body. Fixed directly.
- Direction understated. The article said the 1.5B length-controlled model
  "matched GPT-4o at equal reasoning lengths"; the L1 abstract says it
  "surpasses GPT-4o at equal reasoning lengths" (verified against the source).
  Changed "matched" to "surpassed." Fixed directly.
- False size parity. "A conventional model of similar size answered in about
  thirty-nine" compared QwQ-32B-Preview with Llama-3.3-70B, which is more than
  twice the size. Removed "of similar size"; the token comparison stands on its
  own. Fixed directly.
- The 92% figure's scope. The draft attached it to "simple problems"; the owning
  paper reports it across its test sets (ASDIV, GSM8K, MATH500), phrased "in
  more than 92% of cases the initial round of solutions produces the correct
  answer." Rewrote to "In more than 92% of cases the first solution round
  already holds the correct answer," matching the source's scope. Fixed directly.

Display text audited descriptor by descriptor: headline (901 tokens, 2 plus 3),
dek (RL taught long chains, no difficulty gauge, efficiency not accuracy), and
every subhead check out against their owners. "The built traps" subhead
correctly signals constructed tasks rather than a general accuracy law. Every
`data-nb-kind` is right: seven primaries that own their claims and one secondary
(VentureBeat) used only to show the general-audience framing. Every `href` opens
on the cited source, and the internal thinking-out-loud link resolves to a real
library file. Sources meet the series floor (8; 7 primary, 1 secondary).

One figure I could not independently confirm and route below rather than settle:
"by the fourth attempt, the share of genuinely new reasoning has fallen below
30%." The evidence record supports it and the surrounding claim (first-round
redundancy) is well sourced, but the paper's text gives a relative drop versus
Solution#3 and the absolute below-30% reads off a figure I could not extract.

## Cut

The prose was already lean, so the cut took few sentences. Five failed and were
removed or trimmed:

- "That is one half of the behavior this lesson takes apart" narrated the piece;
  the body speaks to no one, so the self-reference went (handled in the recast
  above).
- "so that is where we start" was a pure signpost; deleted.
- "Follow the incentive down one link at a time" announced the reasoning the
  next two sentences actually do; deleted rather than repaired.
- "and the conditions decide everything" reduced to "the X decide everything," a
  line about anything; deleted, leaving "It is true that more reasoning can
  lower accuracy. It is not true in general."
- One prose semicolon ("not idle; it is actively steering the model wrong")
  became a period, per the punctuation standard.

The negative-parallelism contrasts that remain each correct a misconception the
piece names and earns its keep: "an efficiency cost, not a wrong answer" is the
article's central distinction, "not a property of thinking longer" corrects the
headline the piece quotes, and "a claim with conditions, not a law" (takeaway)
answers the "more thinking means a smarter answer" belief set up in the opener.
I left them.

Edge sentences, read alone and out of order, hold: openers introduce their own
nouns, and the closer ("the model still cannot tell on its own that 2 plus 3 did
not need 901 tokens") states the conclusion the argument built. Against the
recent the-mechanics record, the headline, dek, and five subheads avoid the
flagged molds: no "Nothing turns X into Y" negative-closer, no "renders the most
likely X" rhythm, no comma-and heading, and the dek is a plain cause-consequence
sentence rather than a comma-triad or semicolon reversal. The one note component
carries a verbatim sourced quotation with a purpose ("The length was learned")
and there is no verdict block, matching the press voice. No prompt leakage: the
"In this article" goals sit in the template-allowed bookend, and the reader
situation the commission describes appears only as reported fact.

## Reader

Read straight through, the piece gives what no single source does: one
difficulty-conditioned account of "more tokens," with each regime pinned to its
own mechanism, plus a clear line between the settled engineering and the open
framing dispute. That matches the draft handoff's original-work claim, and both
answers survive, so this is not a restatement of its sources. The prose sits
closer to the voice-guide exemplars than to a median summary: it walks the
incentive link by link in the Dan Luu manner, states the plausible wrong idea
before the mechanism in the Ciechanowski manner, and names the three-way
disagreement plainly where a summary would smooth it over.

## Edits

- Orientation: removed "of similar size" from the QwQ-versus-conventional token
  comparison (false size parity with Llama-3.3-70B).
- Orientation: recast "That is one half of the behavior this lesson takes
  apart ... Both trace back to how these models were trained, so that is where
  we start" to "That is one half of the behavior. The other half sounds like its
  opposite ... Both start from the same place, a model trained to reason at
  length" (cut self-reference and signpost; removed shared-cause implication).
- Chain-grew: deleted the signpost "Follow the incentive down one link at a
  time."
- No-gauge: rewrote "On simple problems the first solution round already
  contains the correct answer more than 92% of the time" to "In more than 92% of
  cases the first solution round already holds the correct answer" (source
  scope).
- Built-traps: trimmed "It is not true in general, and the conditions decide
  everything" to "It is not true in general."
- Built-traps: changed the semicolon in "not idle; it is actively steering the
  model wrong" to a period.
- Built-traps table: replaced row-two effect "Accuracy holds or climbs (AIME
  first-try 15.6% to 71.0%)" with "Accuracy is maintained as the chain grows,"
  and removed the s2 citation from the table caption (training figure no longer
  in the table).
- Hits-ground: changed "matched GPT-4o at equal reasoning lengths" to
  "surpassed GPT-4o at equal reasoning lengths" (source direction).

## Required work

- writer: confirm "by the fourth attempt, the share of genuinely new reasoning
  has fallen below 30%" reads off Figure 6 of the overthinking paper (s1). The
  evidence record supports it, but the paper's text states a relative decrease
  versus Solution#3 and the absolute figure sits in a plot; verify against the
  figure or cut the sentence. Non-blocking; the first-round-redundancy claim it
  supports is separately sourced.
- orchestrator: re-stamp before PR. My edits removed roughly a dozen words, so
  the stamped word count (2192) is now slightly high; the read-only check still
  returns BLOCK 0, WARN 0, PUBLISHABLE.

## Decision

approve. The two phenomena stay distinct through the whole piece, every number
traces to its owner, and the remaining verification is a non-blocking figure
check the writer can settle before or alongside the orchestrator's re-stamp.
