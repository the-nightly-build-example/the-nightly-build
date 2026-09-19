# Editorial review: the-mechanics/output-diversity (editor/01)

## Skeptic

Thesis: a chatbot keeps returning the same few names, tones, and shapes because
alignment reshaped the distribution it draws from, piling probability onto a few
high-reward answers; turning up temperature samples that narrowed range more
loosely but cannot rebuild variety that training removed. The piece states its
thesis cleanly, and a reader could recover it from the headings alone.

The claims it stands on, and how each held:

- **Base models spread probability widely; alignment narrows it.** Held.
  Mohammadi (higher base token-level entropy, used by direction only, no exact
  value or the 2.32-bit ceiling quoted) and the Wu book-review ladder (base
  Llama-2 5.9% vs the human 2.8%, rising to 82.1% at RLHF) both support it, and
  the article uses each correctly.

- **The reward term does the narrowing; the KL penalty is only a leash.** Held,
  and this is where the piece earns its keep. The InstructGPT objective is
  reproduced faithfully (checked term by term against the evidence record's
  Equation (2)), the reward term is named as the concentrator, and Kirk's finding
  that raising the KL coefficient lowered diversity *further* is used exactly as
  the evidence record frames it. The article does not attribute narrowing to the
  penalty. Good.

- **Temperature cannot restore removed range.** Held (Mohammadi's T=1 attractors;
  Wu's 82.1%→58.1% best-case sweep, "still far above" the base 5.9%). One break
  here: the draft said the attractors "persist even at a temperature of 1, high
  enough that the base model shows no such trapping," which pins the base model's
  behavior to T=1. Mohammadi's actual finding is that the base model shows no
  attractors even at *low* temperatures. I rewrote the sentence to state both
  facts as the record has them, using no fact the record does not carry.

- **The claim is narrow, not total.** Held and honestly represented, not buried:
  the scope section gives Shypula's contradicting result (preference-tuned models
  score higher on effective semantic diversity among high-quality outputs, by a
  wide margin) its own paragraph before landing the calibrated claim, and marks
  what is settled vs open, with the KL penalty named as ruled out as the main
  cause. This matches the round's insistence.

Verification done against the primaries, not just the record: I opened all eight
citation hrefs. Every URL resolves to its source and every source title in the
Sources list matches the paper (Kirk, Wu, Ouyang, Padmakumar/He, Mohammadi,
Shypula, TODAY, Hacker News). The Kirk quotation is verbatim in Section 6.2
("RLHF substantially decreases the diversity of outputs sampled for a given input
compared to SFT"); the article quotes the true substring. The Padmakumar numbers
(0.154 / 0.158 / 0.166) round the record's 0.1536 / 0.1578 / 0.1660 correctly,
and the direction (InstructGPT highest, statistically significant) is right. The
Wu table (2.8 / 5.9 / 44.7 / 82.1 / 100) matches the record cell for cell. The
Hacker News per-model name spread (Aldric, Lila, Elinor) checks out, so the
"strong tendency, not a fixed law" framing is earned. Every `data-nb-kind` is
correct: six primaries, two secondaries (TODAY and the HN thread are labeled
secondary, which is honest for the convergence anecdote). Sources floor met.

Headline as a claim: "Chatbots keep naming the heroine Elara because alignment
narrowed their range" states the finding with its actor, and the body qualifies
Elara as a tendency in its first paragraph, so the headline does not overreach
past what the piece defends.

## Cut

No slop survived into the final piece that I could find on the sentence pass, the
edge pass, or the delete pass. The furniture broke the flagged recurring stack
(no stat-strip / note / holds-up): the table earns its place as a five-row
one-shape comparison, and the annotated equation is the documented at-most-one
annotated form, used to separate the two forces the lesson turns on. No Verdict
note or any finding-restating block closes the body — the press rule is satisfied,
and the takeaway bookend carries the judgment as the template intends.

Cuts and repairs made (six sentences touched):

- Two self-grading frames removed. "The honest claim is that models lean hard on
  a few names, not that every model always picks the same one" grades the
  article's own honesty; recast to state the fact and keep the earned contrast.
  "So the accurate statement is a specific one:" grades the article's own
  precision; dropped, leaving the calibrated claim to stand on "So alignment
  trims...".
- One method-signpost opener replaced. "The claim has to be stated narrowly,
  because one careful study cuts against a loose version of it" narrates the
  article's own claim-calibration; rewritten to lead with the study.
- Punctuation brought to the house default. A chained three-clause semicolon in
  the equation caption (banned outright) became three sentences; two standalone
  semicolons where a period does the job became periods.
- One term-drift fix: the takeaway said "that narrowed set" where the piece names
  the concept "range" / "distribution" throughout; changed to "range".

No borrowed phrasing from the voice-guide exemplars, no prompt leakage against the
brief or commission (the reader-situation language in the bookends is the paper's
own, not lifted), and no formula against the recent-pattern notes: headings are
declarative and varied, no "Nothing in the pipeline checks" or "The model never
sees X" opener, no "floor/ground beneath the failure" closer, no question-shaped
heading. The dek is one sentence joined with "and", not the flagged causal "so"
compression and none of the banned molds (no semicolon reversal, suspended
question, or comma triad); I weighed tightening it and judged it accurate and
within form, so I left it.

## Reader

Read straight through, the piece gives what the sources alone do not: one backward
chain from a behavior the reader has seen (the recurring Elara) down to the training
step that produces it, with temperature isolated as powerless against a narrowing
that happens at training time rather than at the draw. No single source draws that
line; the article assembles six findings into it. The original-work sentence in the
handoff claims exactly this, and the article delivers it in the reward-narrowing and
temperature sections. Both answers survive. The prose sits closer to the voice-guide
exemplars than a median summary: it names each real part before leaning on it
(distribution, mode, entropy, the reward term, the leash), fixes the requirement in
figures the way Ciechanowski does, and states the settled/open split flatly in
Gawande's register. The equation is the heaviest element for a no-codebase reader,
and I judged it earns its place: it is the cleanest anchor for the reward-vs-leash
distinction the lesson is built on, the two load-bearing terms are color-separated
and named in plain words, and the prose carries the mechanism for anyone who skips
the math.

## Edits

- Rewrote the Mohammadi attractor sentence to state that the aligned model's
  attractors persist at T=1 while the base model shows no trapping even at low
  temperatures (corrects a misattribution of temperature to the base model).
- Orientation: "The honest claim is that models lean hard on a few names, not that
  every model always picks the same one" → "Models lean hard on a few names, but no
  model always picks the same one."
- Orientation: semicolon split — "The base model stays close to people. Each
  further step of alignment piles the reviews onto the positive end."
- Equation caption: unchained the three-clause semicolon into three sentences.
- Reward-narrowing: semicolon split — "The narrowing lives in the reward chase. The
  penalty only bounds how far the chase can run."
- Scope: "The claim has to be stated narrowly, because one careful study cuts
  against a loose version of it." → "A loose version of this claim does not survive
  one careful study."
- Scope: dropped the self-grading "So the accurate statement is a specific one:"
  frame, leaving "So alignment trims the variety of words and sentence shapes...".
- Takeaway: "that narrowed set" → "that narrowed range"; semicolon split into two
  sentences.

## Required work

None publication-blocking. One non-blocking note for the writer, who holds the
tooling: the handoff flagged that the KaTeX equation and its colored legend terms
were not Chrome-verified in both schemes. The markup is the documented annotated
form and the engine styles the `nb-mc*` colors for both schemes, so this is a
final-proof look rather than a fix. The writer re-runs the proof and the
orchestrator stamps after these edits.

## Decision

approve — every item in this round's focus holds (press rule, the narrow claim
with Shypula represented, the reward-vs-KL-leash attribution, the numbers, the
equation's weight), and the one accuracy break was an editor-fixable prose repair
made from the evidence record, now corrected.
