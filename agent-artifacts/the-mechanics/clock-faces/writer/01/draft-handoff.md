# Draft handoff: the-mechanics/clock-faces (01)

## Original work
The article assembles four separately sourced facts (the diffusion training
objective, the 10:10 advertising convention, the analog-clock reading
benchmarks, and the 2026 generation demonstrations) into one backward causal
chain that splits the behavior into two distinct causes (a lopsided training
prior and the absence of any step that turns a requested time into a hand
angle), and uses that split to tell a real mechanism apart from the "AI is bad
at clocks" hand-wave and to predict where else the most likely appearance beats
the correct one. The evidence record holds these as separate claims with
caveats; it does not connect them into the two-cause explanation or draw the
generalization. That connection and generalization are visible in the
"Nothing turns 3:15 into two hand angles" section and the takeaway.

## Proof result
`nb check ... --series the-mechanics` (links on): **BLOCK: 0, WARN: 0**,
verdict PUBLISHABLE. Stamped words=1949, reading_minutes=8, sources=9. No
warnings intentionally left.

Warnings resolved while iterating (all fixed, none carried):
- W-SENTENCE-DENSITY x3: split the why-bookend closer, the smile-study
  sentence, and the orientation opener; also broke the counting/hands aside off
  its clause. The orientation opener tripped the detector because each time
  colon (3:15, 10:10) scores as a clause join, so the two times now sit in
  separate sentences.
- B-SOURCES-FORM: Polymath07 source URL switched from http to https.

## How the evidence's scoping caveats were honored
- The generation behavior (ask 3:15, get 10:10) is presented as what
  reputable demonstrations show, not a measured result; the 2026 GPT Image 2
  near-hit is labeled a demonstration, not a study, and the piece states the
  demonstration cannot say what changed (data, tooling, or design).
- "Training data skews to 10:10" is stated as a well-grounded inference from the
  advertising convention, with an explicit line that no one has counted the
  times across a training set of that size.
- The strongest version is scoped to watches; wall clocks are noted as more
  varied (Digital Camera World's Firefly test).
- The reading gap closing fast is built into the body as the honest present
  state and as evidence for the mechanism (settled/open line stated outright in
  the last section): ClockBench 13.3% (Sep 2025) to 66.7% now vs 90.7% human,
  and TickTockVQA 1.41% to 46.22% after targeted tuning.

## Furniture
One table (the closing reading gap, from the verified figures) and one note (the
verbatim MeasureBench quotation, the bridge showing the pose leaks into the
reading task). No source asset captured: the most argument-relevant visuals
(the Polymath07 model grid, the benchmark tables) sit on secondary
demonstrations and external pages, and the numeric table already carries the
closing-gap comparison from figures verified in the evidence record.

## Open evidence or voice questions
None blocked the draft.
