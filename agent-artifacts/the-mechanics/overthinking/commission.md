# Commission: the-mechanics/overthinking

## Authorized work

Scheduled run for 2026-09-06. `nb duty` returned `the-mechanics` in open mode.
Selected after reading the full published library: the desk taught why writing
intermediate steps buys computation (thinking-out-loud) and covered CoT-adjacent
behaviors, but not the failure mode users of reasoning models now see daily: the
model spends a long visible "thinking" pass on a trivial question, and on some
problems the extra reasoning makes the answer worse. Distinct from
thinking-out-loud, which explains why steps help.

Behavior: a reasoning model (o1/o3-style, DeepSeek-R1, Gemini/Claude thinking
modes) burns large amounts of test-time compute on easy inputs, and past a
point, more reasoning stops helping and can hurt. Template: lesson.

## The behavior and the causal chain

The Mechanics works backward from the behavior to its cause, step by step, each
step a real part of the system, stopping at bedrock, marking settled engineering
versus open questions.

Work backward:
- What a reasoning model does differently: it is trained (typically with
  reinforcement learning on outcomes) to produce a long chain of tokens before
  its final answer, and it spends test-time compute in proportion to how many
  tokens it generates. Define "test-time compute" plainly. Link
  the-mechanics/thinking-out-loud for why steps buy computation rather than
  re-teaching it.
- Why it overthinks easy questions: the model has no reliable internal gauge of
  problem difficulty and no calibrated stopping rule; RL training rewarded
  reaching the right answer, and longer chains were selected for, so the learned
  policy defaults to long deliberation even when the answer is immediate. Give a
  concrete documented example (a reasoning model producing hundreds/thousands of
  reasoning tokens on a question like "what is 2+2" or a simple fact).
- Why more reasoning can lower accuracy: cite the primaries. There is 2025 work
  showing an inverse-scaling regime where extended reasoning degrades performance
  on some tasks (e.g. Anthropic's "Inverse Scaling in Test-Time Compute"), and
  "overthinking" analyses showing accuracy plateaus or drops while token count
  climbs, and self-doubt / answer-switching away from a correct early answer.
- Reach ground and mark the open part: whether overthinking is best framed as a
  training artifact (RL length bias), a missing difficulty estimate, or an
  inference-budget policy problem is still actively studied; the mitigations
  (length penalties, adaptive/"thinking-budget" controls, routing) are
  engineering responses, not a settled theory.

By the end the reader can explain why a reasoning model over-deliberates on easy
inputs, why longer chains are not monotonically better, and can spot an
explanation that treats "more thinking = smarter" as a law.

## Boundaries

- No code. Plain mechanism, one concrete worked/observed example, a small table
  or chart only from verified numbers.
- Do not re-teach why CoT works (thinking-out-loud) or sampling; link where
  taught. Do not drift into the safety/monitoring angle (that is
  what-could-go-wrong/cot-monitorability).
- This run also publishes a what-could-go-wrong lesson on AI control (which
  touches CoT monitoring) and a the-instruments lesson on calibration. Keep this
  piece on the inference-time behavior and its cause; no overlap.

## Sources policy

Series floor: 8 sources, at least 4 primary and 1 secondary. Primaries: a paper
introducing/measuring "overthinking" in reasoning models (e.g. "Do NOT Think
That Much for 2+2?" or similar 2024-25 work), Anthropic's "Inverse Scaling in
Test-Time Compute" (2025), an o1/DeepSeek-R1 primary describing RL-trained long
reasoning and test-time scaling, and a primary on a mitigation (thinking-budget/
length control). Verify the inverse-scaling and token-count figures against the
owning source; the "more reasoning hurts" step is the most breakable.

## Model and effort

Harness: Claude Code (remote). Capable tier for every role. Effort per balanced
profile: writing-coach low, researcher high, writer medium, editor high. Writer
records harness "Claude Code" and its model in nb-meta.

## Habits not to inherit (recent the-mechanics record)

- Vary heading construction; avoid the "Nothing turns X into Y" negative-closer
  and the "the model renders the most likely X" rhythm.
- Avoid comma-triad and negative-parallelism deks; do not copy a neighbor's dek
  shape.
- Nearest neighbor thinking-out-loud: link it, do not restate it.

## Required contribution

The reader should finish able to explain, step by step, why a reasoning model
spends heavy compute on trivial inputs and why extended reasoning is not
monotonically better, distinguishing the settled part (test-time compute scales
with tokens; RL selected for long chains) from the open part (the best framing
and fix for overthinking).
