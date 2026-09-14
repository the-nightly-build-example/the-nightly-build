# Draft handoff: the-mechanics/hedging (01)

## Original-work sentence

It threads the evidence's separate findings into one backward-traced causal
chain for a single recurring hedge (the password-manager answer), pins each
stage of the chain to the source that owns it, marks the one settled link
(labelers were told to reward epistemic humility and the reward model picked it
up) against the two things no source resolves (how much each stage contributes
to a given hedge, and whether a particular hedge is deliberate policy or
overshoot), and draws the sycophancy boundary exactly where the two behaviors
share a reward model.

## Proof result

`./nb check ... --series the-mechanics --library <library-checkout>` (links
included): **BLOCK: 0**, verdict PUBLISHABLE. `nb stamp` written: words 2189,
reading_minutes 10, sources 8 (6 primary, 2 secondary; floor is 8 / >=4 / >=1).
All source URLs resolve, including the dated Model Spec URL
(model-spec.openai.com/2025-12-18.html).

## Warning intentionally left

- **W-CITE-DENSITY, section `raw-predictor`: no inline citations.** This is the
  base-model completion step, which the brief and the evidence both mark as
  reasoning-only: no source measures how strongly a base model pulls toward
  hedged prose on advice-shaped prompts. The section says so in its own text and
  carries no fabricated citation for a claim no source measured. The one
  empirical anchor it leans on (a base model is well-calibrated, so the hedge is
  not ignorance) is taught ground owned by `the-mechanics/false-confidence`, so
  it is linked in prose per press policy rather than re-cited as a numbered
  source. Leaving the warning is the honest resolution; do not paper over it with
  a padded citation.

## Scoping and boundaries honored

- Behavior scoped to the InstructGPT §4.3 overshoot (a hedge where "one fairly
  clear answer" exists), not all non-commitment. No general "assistants hedge
  X%" rate is claimed; the two measured rates (2.4% / 28.6%) are labeled
  domain-specific (human-rights prompts) in prose and in a data-nb-note.
- Countervailing pressure (Kalai) is stated: the same pipeline rewards confident
  guessing on closed factual tasks, so the bias is task-dependent.
- Deliberate-vs-overshoot line drawn in the policy section; correct-design case
  (contested normative questions, Model Spec ranking) preserved.
- Sycophancy carved out explicitly at the reward-model step and linked
  (Background + prose). Over-refusal linked in Background.

## Open questions for the editor

- **politeness-and-pressure link.** The commission marks this link optional
  ("link where the reader might conflate them"). The student-study paragraph
  touches prompt-wording-moves-output territory, which is the nearest conflation
  point. I left it unlinked: the word count is at the top of the band (2189 of
  2200), the stronger conflation risk (sycophancy) is fully handled, and adding
  the row would push over the band. If you judge the conflation risk higher than
  I did, add `../the-mechanics/politeness-and-pressure.html` and trim ~25 words
  elsewhere to stay in band.
- **Source s7 (LessWrong student study).** Used for direction only (the hedge is
  a controllable default that prompt phrasing moves), explicitly flagged in prose
  as small, unreviewed, and not a rate, per the evidence record's low-weight
  caveat. It is one of the two secondaries meeting the floor. If you would rather
  not carry a non-peer-reviewed source, the floor still needs a replacement
  secondary and a second-secondary substitute.
