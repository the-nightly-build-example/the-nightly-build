# Editorial review: what-could-go-wrong/capability-elicitation (editor/01)

## Skeptic

Thesis: a safety score measures the model plus the effort spent drawing the
capability out, so any single score is a floor set by that effort and never a
ceiling; a passed evaluation therefore cannot prove safety, but the large
elicitation gaps that have been shown are not themselves proof that a dangerous
capability sits hidden.

The claims it stands on, and how each held:

- **Capability score = model + elicitation effort; change the effort and the
  number changes with the model fixed.** Carried by three owned figures, each
  checked against its primary. PaLM 540B on GSM8K, 17.9% standard prompt to 56.9%
  with chain-of-thought (Wei et al., s4). Repeated sampling on SWE-bench Lite,
  15.9% at one attempt to 56% at 250, past the 43% single-attempt state of the
  art (Brown et al., s5). GPT-4 Turbo buffer overflow, 0.05 on CyberSecEval 2
  (Bhatt/Meta, s6) to 1.00 once Project Zero added a scaffold (Naptime, s7). The
  figures, the models, the direction, and the "solved by any attempt" reading of
  coverage all match the papers. The writer correctly used the owned 0.05→1.00
  pair rather than Barnett and Thiergart's "71% single attempt" secondary
  rendering, per the evidence verification note.
- **Careful evaluators read scores as lower bounds.** METR's stated goal ("the
  full capabilities of the model that are likely to be accessible with plausible
  amounts of post-training enhancement," s1), AISI's underestimation warning
  (s2), and OpenAI's "any one-time capability elicitation ... as a lower bound,
  rather than a ceiling" (s3) are all verbatim to their primaries and cited to
  the owning document.
- **Elicitation surfaces latent capability; it does not create it.** The GPT-4
  biochemical red-team failure is quoted as "engineer new biochemical
  substances." I opened the GPT-4 System Card and confirmed the phrase is
  verbatim (§2.6: "Red teamers could not successfully compel the model to
  engineer new biochemical substances"). The repeated-sampling ceiling — coverage
  above 95% at 10,000 tries but selection plateauing near 100 without a verifier —
  matches Brown et al. and lands the verifier point the round focus asked for.
- **The GPT-4/ARC case is a floor, not a hidden capability.** I confirmed both
  blockquote sentences verbatim against the System Card; the eval correctly found
  the model could not autonomously replicate, with fine-tuning untested and
  flagged as able to change the result. The article does not overread it.

Breaks found and fixed: one misquote. The article rendered Barnett and
Thiergart's phrase as "no principled method" (singular); the source reads "no
principled methods" (plural). Fixed directly, right source in hand, claim
unchanged.

The shown-versus-inference seam holds: the piece states that no figure shows a
dangerous capability a passing test hid, keeps that worry as an inference, and
closes both steelmen on "we cannot rule it out" rather than "it is there." The
distinction from the reader's sandbagging lesson is explicit and early (the
model's choice versus the tester's effort). No company is set up as an authority;
relief and alarm are held at equal distance. Display text checks out: headline,
dek, and every subhead are argument-specific claims; the model name, benchmark
names, institutions, and figures all match their primaries.

## Cut

A dedicated slop pass, then the edges alone, then the delete test. Five sentences
cut, four of them at edges.

- **Reader-addressed imperative in the body.** "Read that closely." The lesson
  template reserves direct address for the two bookends; this is also a lecturing
  opener under spec/slop.md. Cut.
- **Newsroom self-reference.** "This is the seam the desk always looks for."
  Narrates the desk; spec/slop.md rules it out. The sentences after it carry the
  shown-versus-inferred point unaided. Cut.
- **Signpost opener.** "Follow that through, and the evaluators' argument appears
  on its own." Reports where the argument is heading without doing the reasoning
  the next sentence does. Cut; the section now opens on the conditional that
  carries the logic.
- **Restated distinction.** The sandbagging paragraph stated the model-versus-
  tester contrast abstractly ("The elicitation gap is not about the model's
  choice. It is about the tester's.") and again, more concretely, at the
  paragraph's end. Cut the abstract pair; the concrete example and the closing
  "leave on the table" pair keep the distinction, which the round asked to be
  explicit and early.

No repeated formula against the recent-record notes: the piece does not close on
"the researchers built the setup themselves" and does not open by naming a
thinker who "argues/predicted." Section headings are this argument's own steps.
The dek is number-led, not one of the banned molds. Punctuation is within the
house standard and the proof reported zero banned-term and em-dash blocks.
Surviving edge sentences that read like restatements ("The target is not what the
model does out of the box. It is the most a determined person could get it to
do." and the alarm-steelman contrasts) were kept: each names a real misreading
and carries a reasoning step, so they pass the delete test.

## Reader

Read straight through as the paper's reader, the piece gives what no single
source gives: the separate results — a prompting gain, a sampling gain, a
scaffold gain, a lab's own hedge, a review's framing — assembled into one tested
claim that a safety score is a floor set by the tester's effort, with the
shown-versus-inferred line drawn where the individual papers leave it undrawn,
and the claim held equidistant from relief and alarm. The original-work sentence
in the handoff describes exactly this, and the article delivers it. The prose
sits closer to the voice-guide exemplars than to a median summary: the mechanism
is built concretely before any conclusion, the verdict is sized to the evidence,
and both directions of overconfidence are weighed. The headline holds as the
largest claim.

## Edits

- Cut "The elicitation gap is not about the model's choice. It is about the tester's." from the sandbagging paragraph (redundant abstract restatement of a distinction the paragraph makes concretely).
- Cut "Follow that through, and the evaluators' argument appears on its own." (signpost opener) from "Why a failed test is only a floor."
- Cut "Read that closely." (body addressing the reader; lecturing opener).
- Cut "This is the seam the desk always looks for." (newsroom self-reference).
- Changed the Barnett and Thiergart quotation from `there is "no principled method"` to `there are "no principled methods"` to match the source verbatim.

## Required work

None. No evidence gap, broken central claim, or source-policy failure remains.
The orchestrator stamps and proofs after these edits (word count remains within
the 1200–2200 band after the cuts).

## Decision

Approve — every load-bearing claim traces to its cited primary and both quotes I
opened are verbatim; the slop and one misquote were fixable directly, and nothing
publication-blocking is left for the researcher or writer.
