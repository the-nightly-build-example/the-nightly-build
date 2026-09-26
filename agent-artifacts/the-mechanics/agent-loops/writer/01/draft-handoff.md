# Draft handoff: the-mechanics/agent-loops (01)

## The one thing this article does that the evidence does not

This lesson places the repeated-action loop inside the plain architecture of an
agent, a stateless model re-reading a transcript and a harness executing what it
returns, and reduces the behavior to the floor below which nothing changes it, so
a reader can tell a real fix (one that changes the transcript or the harness)
from a cosmetic one (retrying, nudging the prompt, or raising temperature).

Where this is visible on the page: the "Below the transcript and the harness"
section states the reduction as the article's own reasoning (cited to the
component pieces, not asserted as a sourced claim), and the "What breaks the loop"
section sorts every fix by where it acts (transcript / harness / outside the loop)
in prose and in the table, which is what makes the real-vs-cosmetic distinction a
tool the reader can apply rather than a slogan.

## Proof result

Command: `nb check .../the-mechanics/agent-loops.html --series the-mechanics --repo /home/user/the-nightly-build` (full run, links included).

- BLOCK: 0
- WARN: 0
- verdict: PUBLISHABLE
- words 2195 (band 1200-2200), sources 9 (8 primary, 1 secondary; series policy min 8 / primary >=4 / secondary >=1 met).

No warnings left standing. The initial run carried W-LENGTH-HIGH, two
W-SENTENCE-DENSITY, and one W-PLACEHOLDER (all-caps table header row); all four
were fixed by trimming, splitting the dense sentences, and setting the table
headers in sentence case.

## Angle-refinement compliance (notes for the editor)

- Huang et al. is drawn as a signal-quality finding, not "models cannot
  self-correct": intrinsic self-correction holds flat or degrades (GPT-4 GSM8K
  95.5 -> 91.5 -> 89.0), while an oracle signal lifts accuracy (GPT-3.5
  CommonSenseQA 75.8 -> 89.7), with the explicit line "The finding is not that a
  model cannot revise."
- Greedy decoding is credited as a contributor via ReAct footnote 6, and the line
  to the-mechanics/repetition-loops is drawn as a shared decoding-level cause
  ("Some action-level looping shares that decoding-level cause"), not as two
  wholly separate phenomena.
- The "ground" proposition and the "temperature is noise, not strategy" point are
  presented as the lesson's synthesis; sampling-temperature is linked, not cited
  as owning the claim.
- ReAct's 47% reasoning-error figure is stated with the caveat that the repeated
  loop is only one part of that row (not reported as a looping rate).
- The SWE-agent repeated-edit case is the concrete anchor. The AutoGPT #1994 log
  is used once with its "one unreplicated report, not a rate" caveat. LangGraph's
  recursion limit is given with its version caveat (1000 as of v1.0.6, 25 earlier)
  and no fragile harness-cap number is leaned on.
- Marked open on the page: why models under-weight the error already in their
  transcript, and whether reliable self-correction is possible with no outside
  signal. Marked settled: the architecture and that scaffolding (memory,
  guardrail, outside judge) helps.

## Open questions for the orchestrator

None blocking. The claim set was not expanded beyond the evidence record. The one
genuinely unresolved item is the in-article open question above, left open by the
sources and by the refinement, not a gap to fill before publication.
