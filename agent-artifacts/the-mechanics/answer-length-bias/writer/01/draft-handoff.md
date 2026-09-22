# Draft handoff: the-mechanics/answer-length-bias (writer 01)

## Original work
This lesson assembles the scattered length-in-RLHF findings into one causal
chain for a lay reader, from a padded answer back to the reward model's measured
length correlation, and puts the decomposition in a single cross-dataset table
that shows how much of RLHF's apparent gain is length while marking exactly where
the measurement stops (7B models, a GPT-4 simulator, no frontier decomposition)
and what it still cannot separate (length itself versus the thoroughness that
rides with it).

## Proof
`nb check ... --series the-mechanics --repo ...` (links included): BLOCK: 0,
WARN: 0, verdict PUBLISHABLE. `nb stamp` wrote words=1942, reading_minutes=8,
sources=8 (7 primary, 1 secondary; meets the resolved minimum of 8 / >=4 primary
/ >=1 secondary). No warning left standing on purpose.

## Hard constraints honored
- The length-share fractions (non-length share 2.0/27.2/53.4%, correlations
  0.72/0.55/0.67, length-only-reward wins 56/59/64%) are framed throughout as
  Llama-7B / three-open-dataset / GPT-4-simulator measurements, in prose and in
  the table caption. The piece states plainly that no published source decomposes
  a frontier assistant this way and that the tie to today's chatbots is by
  mechanism, not a matching number.
- The 62% real human preference (AlpacaFarm) is stated and sourced, with RLHF
  framed as amplifying a modest but real signal (Park's ~2x amplification past the
  data's own length gap), not inventing one.
- The setting-specific qualifier is included: Stack technical QA (53.4% of the
  gain is not length) and the harmlessness reward model's negative ~0.3
  correlation.
- The length-vs-thoroughness open question is named as this lesson's own closing
  section ("Length itself, or the thoroughness with it"), not the stock
  "What the builders haven't settled" label.
- length-control is distinguished explicitly (the opposite failure) and linked in
  prose and in Background; the taught RLHF lessons (instructgpt,
  deep-rl-from-human-preferences, proximal-policy-optimization) are plain prose
  links at first mention and Background rows, never numbered sources.

## Open question / notes for the orchestrator
- The one open item is the lesson's own subject matter, not a gap in the record:
  no source read separates a rater's length preference from the informativeness
  that usually accompanies it. It is presented as unresolved.
- Furniture: one nb-table (SFT-era Singhal decomposition across the three
  datasets) built solely from the record's verified numbers. No chart or source
  asset was needed; the table carries the quantitative case faster than prose and
  nothing else earned a component.
- No missing evidence blocked drafting.
