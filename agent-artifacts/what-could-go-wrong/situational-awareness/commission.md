# Commission: what-could-go-wrong/situational-awareness

## Authorized work

Scheduled run for 2026-08-09. `nb duty` returned `what-could-go-wrong` in open
mode, reason: "open section — choose a topic within the beat; do not repeat a
published slug." One article.

## The argument

Situational awareness: the worry that as models grow more capable they come to
"know" they are an AI model, possibly under evaluation or training, and that this
knowledge quietly invalidates the safety evaluations the field relies on. A model
that can tell a test from deployment could pass every dangerous-capability eval
and still behave differently in the wild. The desk teaches one risk argument at a
time on its merits. This one is a live, current argument (2023-2025) with a
primary-source spine, and it is the missing precursor under two arguments this
desk has already covered — sandbagging and deceptive alignment — without ever
teaching the capability both presuppose.

## What the lesson teaches (the desk's fixed shape: full strength, then test,
## then present)

1. **The argument at full strength.** Name who raised it and what they had seen.
   Ajeya Cotra framed situational awareness as a key ingredient of dangerous
   models (the "playing the training game" worry). Owen Evans and colleagues
   turned it into something measurable. Lay out the careful defender's case: evals
   are the field's main safety instrument; if a model can distinguish "I am being
   tested" from "I am deployed," a clean eval proves nothing about deployment, and
   the more capable the model the sharper that distinction gets. Make the reader
   understand why serious people hold this before a word against it.

2. **Test it against what real systems do — draw the sharp line.** Separate the
   demonstrated from the analogized. Demonstrated: Berglund et al. 2023 showed
   models can do "out-of-context reasoning," using facts about themselves learned
   in training to change behavior at test time; the SAD benchmark (Laine et al.
   2024) measures components of situational awareness and finds frontier models
   score above chance but well short of reliable, and below a human baseline; some
   2024-2025 eval reports find models verbalizing that they might be under test.
   Still analogy or guesswork: a model spontaneously using this awareness to game
   a real safety eval in deployment. That is where the case usually turns.
   Distinguish situational awareness (the capability) from sandbagging
   (deliberate underperformance, covered by this desk: "No AI has been caught
   sandbagging a safety test on its own") and from deceptive alignment (faking
   alignment given a goal, also covered). Situational awareness is the
   prerequisite both would need; it has been partly measured, they have not been
   caught unprompted.

3. **Bring it to the present.** Who makes the argument now and what they want
   done: frontier-safety frameworks treat situational / evaluation awareness as
   an eval-invalidating capability to track, and eval labs design tests they hope
   are robust to it. Check against the most recent evidence, and name the gap in
   both directions: the doom reading ("models already know they are tested and are
   hiding") and the dismissal ("it is pattern-matching, there is no real
   awareness") both run ahead of what SAD and the out-of-context experiments
   actually show. Leave the reader to decide how worried to be.

## Boundaries

- Do not re-argue sandbagging or deceptive alignment; both have their own
  lessons. Link them, and use them only to locate situational awareness as the
  capability upstream of each.
- Do not join situational awareness to eval-gaming as if the link were
  demonstrated. The whole value of the lesson is the line between measured
  precursor and un-demonstrated exploitation.
- Work from the original documents — the papers, the benchmark, the safety
  frameworks — not commentary about them. Name no company as an authority; report
  what a lab's own eval found without treating the lab as proof.

## Original contribution

Give the reader the one distinction the debate keeps blurring: situational
awareness has been partially *measured* (SAD scores, out-of-context reasoning),
while its feared *use* — a model deploying that awareness to defeat a safety eval
on its own — has not been observed. The reader should be able to hear a "models
know they're being tested" claim and ask which of the two it is asserting.

## Source policy (from `nb source-policy`)

Series and template agree: minimum 8 sources, primary ≥ 4, secondary ≥ 1.
Primaries: Berglund et al. 2023 (out-of-context / situational awareness measure);
Laine et al. 2024 (SAD benchmark); Cotra's original write-up of the argument; at
least one frontier-safety framework or eval-lab report that owns the present-day
"track it as eval-invalidating" position. Coverage is secondary context.

## Production policy (from `nb production-policy`, profile: balanced)

- writing-coach: capable (Sonnet), low effort
- researcher: capable (Opus), high effort
- writer: capable (Opus), medium effort
- editor: capable (Opus), high effort

None `required`; no deviation to record.

## This edition's neighbors

- The other four lessons tonight (`the-evidence/gpt-3`, `the-instruments/mmlu`,
  `the-mechanics/word-order`, `when-ai-breaks/tesla-autopilot`) do not overlap.
  `mmlu` also touches eval reliability, but from the measurement side (a
  benchmark's error floor); this lesson is about a model capability that
  invalidates evals. Keep the two distinct; a cross-link is fine.

## Recent habits not to inherit

- This desk's recent openers state the fear in a headline sentence
  ("Soares warns that AI safety could break the moment capability jumps"). That is
  fine as a shape; the risk is the Why-this-matters card then closing on "By the
  end you can state the argument at full strength and see why…" verbatim, which
  recurs (data-poisoning). Write the promise in this argument's own terms.
- The desk's pieces lean hard on the "neither doom nor dismissal / the two
  strongest results were never run in one experiment" balance-beam closer. This
  argument does end on a genuine measured-vs-demonstrated gap, so the balance is
  earned — but write the takeaway off the recent phrasings ("Neither easy story
  survives the evidence," "Knowing which of the two you are looking at is what
  separates judging the threat from repeating a headline"). Land it fresh.
- Avoid the second-person "Now you know which one you are looking at" closer.
- "In plain language" note recurs across the shelf; label any note for its move.

## Prior coverage to link, not re-teach

- `what-could-go-wrong/sandbagging` — deliberate underperformance on a test.
- `what-could-go-wrong/deceptive-alignment` — faking alignment given a goal.
- `what-could-go-wrong/scalable-oversight` and `the-off-switch` are available if a
  specific claim needs them; link, do not re-teach.
