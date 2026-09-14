# Editorial review: the-mechanics/hedging (editor/01)

## Skeptic

Thesis: when a question has one fairly clear answer and an assistant still
returns "it depends," the cause is three separate training stages that each
tilt the answer toward the hedge; the reward-model stage is the best-supported
link, and two things stay open (how much each stage contributes, and whether a
given hedge is deliberate policy or overshoot). The defensible target is the
overshoot, not all non-commitment.

The piece rests on these claims, each tested against the source it prints:

- **Base model completes toward the balanced register.** Presented as reasoning
  with no measurement, and the section says so in its own words. I pushed on
  whether it smuggles an unsourced empirical claim. It does not: the only
  empirical anchor (a base model is calibrated, so the hedge is not ignorance)
  is taught ground linked to `false-confidence`, per press policy, not re-cited.
  The lone W-CITE-DENSITY warning on `raw-predictor` is the honest resolution of
  a genuine reasoning step, and it stands.

- **The reward model was paid to prefer the hedge.** Strongest link, and it
  holds. Opened InstructGPT (s1) in full. The §4.3 overhedge quote is verbatim.
  The epistemic-humility quote is verbatim. The K=4-to-9 ranking with all
  pairwise comparisons (§3.5) is confirmed. Sycophancy is carved correctly: the
  hedge appears in the first reply before any pushback, sycophancy needs a
  stated user position, and the shared step is the reward model. Sycophancy is
  linked.

- **The policy asks for the hedge on purpose.** The Model Spec answer-type
  ranking blockquote is genuine. The small fetcher could not surface it in the
  live 2025-12-18 page (a large single-file doc), so I confirmed the exact
  string two other ways: verbatim in the archived 2024-05-08 spec, and quoted
  verbatim by Lambert (s5). Anthropic's balanced-information goal and its
  bullet-points penalty (s4) are confirmed. Lambert's intentional-hierarchy and
  hard-by-design reading (s5) is confirmed.

- **The same training can push the other way.** Kalai et al. (s6) confirmed:
  training and evaluation reward guessing over acknowledging uncertainty,
  models optimized as test-takers. Three of four authors are OpenAI-affiliated,
  so "OpenAI researchers" holds. The task-dependence scoping is stated and
  correct.

- **No blanket rate.** Confirmed the piece never claims a general "hedges X%"
  figure. It scopes every measured number to its domain.

Breaks found and fixed:

1. **Wrong denominator label on the s8 figures (display furniture).** The
   stat-strip labeled 2.4% / 28.6% as "share of prompts hedged." The primary
   (2502.19463, Table 5) defines the rate as the share of the 205 identities on
   which a model hedged at least once, not a share of prompts. The numbers are
   right; the label was wrong, and a wrong label in a stat strip reaches every
   scanner. Fixed both labels to "share of 205 identities it hedged on" /
   "same 205 identities" and tightened the s8 tooltip to match. Number, source,
   and claim unchanged.

2. **Wrong section locator on the epistemic-humility quote.** The note carried
   `§5.3 / limitations`. The quote and its companion overhedge quote both sit in
   the §4.3 "InstructGPT still makes simple mistakes" discussion (the
   epistemic-humility sentence explains "behavior (2)," the overhedge, in the
   adjacent paragraph); the overhedge note already prints §4.3. Confirmed §4.3
   across repeated reads of the arXiv HTML plus a search snippet. Aligned the
   locator to `§4.3 / qualitative results`. The evidence record's §5.3 locator
   for this quote is the underlying error (see Required work).

Every citation href was opened as printed. All eight source URLs resolve and
land on the source's own page (arXiv abstract pages, the Model Spec, the
Anthropic post, the Interconnects post, the LessWrong post). data-nb-kind
audit: s1, s2, s3, s4, s6, s8 primary and correct (each owns its claim); s5
(Lambert) secondary and correct (outside analysis of OpenAI's spec). s7
(LessWrong) is labeled secondary/low-weight; it owns its own small measurement,
so the label is conservative rather than inflating, and it hides no missing
independent source because nothing central rests on it (see below).

Source s7 audit: cited only for direction (imperative phrasing moves the hedge;
factual prompts floor out), and flagged in prose as small, unreviewed, and not
a rate. The central three-stage chain does not lean on it. Verified its content:
three lightweight models, subjective hedging dropped under a demand, objective
near-floor. It is a properly caveated, nonessential illustration. No cut or
route needed.

## Cut

Ran the sentence-by-sentence pass, the edge pass, the arrived-from-a-link pass,
and the delete test. Five sentences failed and were cut or repaired; the rest of
the prose is clean and holds the voice guide's register (a single reused
example, boundary-marking in the first person, the textbook-then-observed turn).

- Cut "That sentence sets the target for the rest of this lesson." Method
  signpost and body self-reference; the two sentences after it do the scoping.
- Cut "Hold the password-manager reply in mind." Reader address in the body,
  no fact lost; the example recurs on its own.
- Cut the throat-clearer "It is worth being clear about what this step does not
  show." The content sentence follows immediately.
- Replaced the lecturing opener "Now think about where a question like ...
  appears in written text. It appears in ..." with a direct statement.
- Replaced the imperative "Read the ranking from the model's side." with "From
  the model's side, ...".

Also removed the vague attribution "security researchers agree that you should"
(the "experts agree" reflex) in favor of the plain illustrative answer, and
fixed a comma splice ("...how often it is right, an earlier lesson ... shows"
-> "...how often it is right, as an earlier lesson ... shows").

Headline, dek, and headings checked against the recent-pattern notes. No
inherited mold: the recent behavior-as-cute-finding title shape and the
"X is a Y, and a Y with almost nothing... still produces" dek rhythm are both
absent, and no heading joins two clauses with a comma and "and." The negative
parallelisms that remain ("not every refusal to commit / the hedge that lands
on...", "not an accident", "a stance the model is withholding rather than a
fact it lacks") each correct a misconception the piece actually names, so they
are earned and stay. No prompt leakage: the behavior framing is reworded
reporting, not lifted planning labels.

Furniture: the two nb-note pull-quotes and the nb-stat-strip each carry
distinct evidence and earn their place; nothing reads as a stack of blocks.

## Reader

Read straight through as the paper's reader. What I have that the sources alone
would not give me: one everyday hedge traced through three distinct
mechanisms (imitation, reward, written policy), with the one settled link marked
against two named open questions and the sycophancy boundary drawn exactly where
the two behaviors share a reward model. No single source integrates these; the
draft-handoff original-work sentence claims precisely this threading, and it
survives the read. The prose sits closer to the voice-guide exemplars than to a
median summary: it opens on a concrete hedge, reuses the one example, and marks
where its certainty runs out in the first person rather than rounding an open
step up to a finding. The headline, reread as the largest claim, now states the
mechanism accurately ("push toward the hedge") rather than implying all three
stages are reward-based.

## Edits

- nb-meta title and h1: "each reward the hedge" -> "each push toward the hedge"
  (only the middle stage literally rewards; the headline now matches the body's
  own "three pressures / push toward" framing without changing the claim).
- Orientation: "There is a fairly clear answer: security researchers agree that
  you should." -> "...: yes, you should." (removed vague attribution).
- Orientation: cut "That sentence sets the target for the rest of this lesson."
- Orientation: cut "Hold the password-manager reply in mind."
- raw-predictor: cut lecturing opener; "A question like ... appears in forum
  threads, buying guides, and explainer articles..." now leads directly.
- raw-predictor: cut "It is worth being clear about what this step does not
  show."
- raw-predictor: fixed comma splice with "as an earlier lesson ... shows".
- reward-model note: locator §5.3 -> §4.3; attribution "limitations" ->
  "qualitative results".
- policy-target: "Read the ranking from the model's side. When it is unsure..."
  -> "From the model's side, when it is unsure..."
- policy-target: "An RLHF researcher reading the spec from outside OpenAI..." ->
  "Nathan Lambert, an RLHF researcher outside OpenAI,..." (named the source).
- the-other-way stat-strip: labels "share of prompts hedged" / "same prompts"
  -> "share of 205 identities it hedged on" / "same 205 identities".
- the-other-way s8 tooltip: rewritten to "Share of 205 identities each model
  hedged on at least once, over UDHR-derived human-rights prompts;
  domain-specific, not a general rate."

`./nb check ... --no-check-links` after edits: BLOCK 0, one WARN
(W-CITE-DENSITY on raw-predictor, deliberate and upheld), verdict PUBLISHABLE.

## Required work

- researcher (record hygiene, non-blocking): the evidence record locates the
  epistemic-humility quote at §5.3 (Limitations, "InstructGPT still makes simple
  mistakes"). In the arXiv version cited, that discussion is under §4.3
  Qualitative results, alongside the overhedge quote. The article is corrected;
  the evidence record should be reconciled so a later invocation does not
  reintroduce §5.3. No article change depends on this.
- writer: none blocking. Word count dropped slightly from the cuts (was 2189 of
  a 2200 band), so the orchestrator's `nb stamp` will reset words /
  reading_minutes; nothing needs rewriting.

## Decision

approve — the three-stage chain is sourced and correctly scoped, the sycophancy
carve-out and the no-blanket-rate discipline hold, and the two correctness
defects (the s8 denominator label and the InstructGPT locator) plus the slop
were fixable in place without new reporting.
