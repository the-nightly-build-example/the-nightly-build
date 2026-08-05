# Editorial review: what-could-go-wrong/mesa-optimization (editor/01)

## Skeptic

Thesis: training grades behavior, never the goal behind it, so a model can act
aligned without having learned the goal you meant; a wrong learned goal under a
correct reward has been shown in working systems, while a learned optimizer
running its own misaligned search has never been found in one, and the evidence
settles neither the doom nor the dismissal reading.

The load-bearing claims and how each held:

1. The demonstrators disclaim mesa-optimization in their own words. This is the
   hinge, so I pushed hardest here. The article prints three Langosco quotes,
   one of which ("our work does not demonstrate or address mesa-optimization")
   is not in the evidence record's quote block. I fetched the paper (ar5iv
   2105.14111) and confirmed all three character-for-character: "goal
   misgeneralization can occur without mesa-optimization"; the full sentence
   "Thus these are in fact two distinct behaviors, and our work does not
   demonstrate or address mesa-optimization." The Shah quotes verify against
   ar5iv 2210.01790: "a learned model implements a search algorithm with an
   explicitly represented objective" and "We do not make this assumption." The
   line holds and is drawn by the demonstrators, not the article.

2. No misaligned inner optimizer has been identified. The article states this
   flatly three times (section body, "has never been identified in a real
   model"; takeaway, "has never been found in a real system") and never lets a
   result stand in for it. The Nikankin bound verifies ("neither robust
   algorithms nor memorization"; "bag of heuristics", arXiv 2410.21272) and the
   Bush counter-bound is fenced correctly: search is learnable, but the plan
   "served the puzzle the network was trained to solve," not a goal of its own.
   Both sides of the fence are honest.

3. Present-day scheming does not close the gap. The article keeps the goal
   handed-in (Meinke: goal placed in the system prompt; Greenblatt: preference
   from prior training) and quotes the open question directly. I confirmed the
   Meinke caveat independently ("The extent to which models can scheme without
   in-context learning remains an open question not addressed by this study")
   and the Greenblatt abstract quotes ("selectively complying with its training
   objective..."; "did not instruct the model to fake alignment or give it any
   explicit goal", arXiv 2412.14093). Scheming never stands in for a spontaneous
   mesa-optimizer.

Overclaim check: no sentence asserts a mesa-optimizer has been found, and none
lets scheming or goal-misgeneralization substitute for one. The article passes
the review-brief's central test.

Display text: the headline is a defended claim in the piece's own nouns, not a
colon template. The dek states a claim about the world (demonstrated vs.
never-found), not a grade of the article's method, so it clears the skeptic bar
for deks. Every `data-nb-kind` is correct: 7 primary (Hubinger, Langosco, Shah,
Nikankin, Bush, Meinke, Greenblatt), each owning its claim firsthand; 2
secondary (Ngo et al., a review; Turner, an outside essay contesting a premise).
The 7/2 split matches the brief. No company is named as an authority anywhere;
model names appear only as experimental subjects.

## Cut

Two direct cuts, both prose.

The pull quote "A wrong learned goal is not yet a mesa-optimizer" was repeated
verbatim as the second sentence of the paragraph directly beneath it, so the
reader met the identical sentence twice within about fifteen words. Ruling on
the writer's flagged judgment call: the pull quote earns its place as the
article's central move and stays as deliberate emphasis, but the repetition in
the adjacent prose does not earn itself. I cut the prose duplicate. The
paragraph now runs "the demonstrators draw it themselves. Langosco and coauthors
write that..." and the line survives once, in the position that emphasizes it.

I cut the trailing clause "which is the honest state of things" from "What it
has found cuts both ways, which is the honest state of things." The clause
grades the article's own even-handedness rather than reporting, which the house
standard cuts as self-grading. The sentence is sharper without it.

I checked the whole piece for prompt leakage against the writer brief and found
none: the "demonstrated/analogy line" framing is carried in the reporting, never
as a claim that the assignment was fulfilled. The bookend's "This lesson teaches
..." and "By the end you will be able to say ..." are template-licensed opener
moves, not leaks. No run-ons, no semicolon chains, no em-dash reflex (zero
em-dashes in the body). Punctuation is clean; the colons introduce payoffs and
lists as the standard allows.

The two granted licenses sit within their bars. The fenced analogy (the
evolution note) states the intuition plainly, then fences it in the same
passage: "evolution is not gradient descent, and a human is not a trained
network ... It is not evidence that it happens inside a model." It builds the
intuition the argument spends and marks where it stops, exactly the exemplar
move. The in-sentence epistemic markers grade and locate claims on the
shown/argued line ("has never been identified in a real model"; "remains an open
question"; "inner misalignment made visible") and never decay into reflexive
hedging; I found no "it seems," "arguably," or "some would say."

Headings: ruling on the second flagged judgment call. The paired "The part that
has been shown" / "The part no one has caught" reads as a step of the argument,
not a machine cadence. The parallel encodes the demonstrated/argued line that is
the lesson's spine, the other three headings vary in shape, and the pair is not
the comma-and-"and" mold the headline spec bans. It earns the parallel; kept.
The three prior-lesson links (goal-misgeneralization, deceptive-alignment,
reward-hacking) are plain in-prose links, not numbered sources, and neither is
re-taught: each result is spent as evidence for this lesson's line.

## Reader

Read straight through, the piece gives what no single source gives: it makes the
goal-misgeneralization authors' own disclaimers the hinge, then places the
never-found inner optimizer precisely between two interpretability results
(scattered "bag of heuristics" arithmetic; genuine but intended-goal Sokoban
planning), so the reader leaves able to sort any claim about this risk onto a
demonstrated-versus-argued line. That is the original-work sentence in the draft
handoff, and the article delivers it. The prose sits close to the voice-guide
exemplars: calibrated, even-tempered, mechanism before stakes, the steelman and
the scrutiny at one temperature. The takeaway resolves the opener's question
(which claims are demonstrated, which are guesses) and closes on the line rather
than a verdict restatement. No Verdict-style block is present.

## Edits

- Cut the duplicated prose sentence "A wrong learned goal is not yet a mesa-optimizer." from the paragraph under the pull quote; kept the pull quote as emphasis.
- Cut the self-grading clause "which is the honest state of things" from the "cuts both ways" sentence.
- Ran `nb stamp` (words 2090 to 2074, sources 9, reading_minutes 9).
- Re-ran `nb check` with links: BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

None. All focus items pass, the verbatim quotes verify against sources
(including the Langosco line absent from the evidence record), and the two cuts
left the article publishable with no new prose owed.

## Decision

approve — the demonstrated-versus-argued line is drawn correctly and by the
demonstrators themselves, no sentence overclaims a mesa-optimizer, every checked
quote verifies, and the two surgical cuts leave the piece publishable at BLOCK 0.
