# Commission: the-mechanics/structured-output

## The behavior

Ask a chatbot a question in plain prose and it answers well. Ask it the same
question but demand the answer as strict JSON, or fill a fixed schema, and it
gets the answer wrong more often. Anyone who has wired a model into a program
and told it to "return only JSON" has seen the quality slip.

## Why this lesson, now

The course taught that a model writes one token at a time
(the-mechanics/prefill-and-decode), that a transformer can only compute more by
writing more (the-mechanics/thinking-out-loud), and that the JSON a model emits
to "call a tool" is just text (the-mechanics/tool-use). It has not taught why
pinning the output to a format costs accuracy, which is the behavior behind a
developer's choice between clean data and correct data. This lesson works
backward from the slip to its cause and sets up later lessons on agents and
evaluation.

## The angle to test

Walk down the causal chain and stop where nothing below changes the answer:

1. The model still emits one token at a time from a probability spread over its
   vocabulary (taught; link decoding lessons only, do not re-teach).
2. A schema is enforced by constrained decoding: at each step the program masks
   out every next token that would break the grammar, so the model may only pick
   among format-valid tokens. Give the plain mechanism with a small concrete
   example of a token being masked.
3. That mask can block the model from writing the intermediate reasoning it would
   otherwise use, and since a transformer computes more only by writing more
   (link thinking-out-loud), taking away the scratch space lowers accuracy. This
   is the core cause.
4. Even with no hard constraint, the instruction to produce a format competes
   with the task, and following the format spends some capability.

Mark what is settled and what is disputed. Settled: constrained decoding masks
tokens; that is mechanical. Disputed: how large the pure-formatting penalty is.
The "Let Me Speak Freely?" study (Tam et al., 2024) reported sizable drops from
format restriction; practitioners who build constrained decoders replied that
placing the reasoning inside a string field first, or prompting for reasoning
then JSON, recovers most of the gap. So the honest finding is: the behavior is
real, its cause is the lost reasoning room, and the fix is to give the model
room to reason before it is forced into the format. No code in the article; a
short worked example of a masked step is fine as prose or a small committed
chart if a comparison is the point.

The researcher must source each rung: constrained/grammar-guided decoding from a
primary that implements it (for example the Outlines or guidance documentation,
or a provider's structured-output docs), the reasoning-room mechanism from the
thinking-out-loud literature this desk already used, the Tam et al. study, and
at least one primary rebuttal or measurement showing the gap narrows when
reasoning is preserved. Verify that constrained decoding masks logits before the
draw, and that "JSON mode" and "structured outputs / schema-constrained" are not
the same thing.

## Boundaries

Do not re-teach next-token generation, sampling, or that tool-call JSON is inert;
link prefill-and-decode, thinking-out-loud, and tool-use in Background. Keep to
why the format costs accuracy. This is one of five lessons tonight; no overlap
with a fine-tuning paper, an embedding benchmark, an AI-safety argument, or a
deployment failure.

## Source policy

Series floor: 8 sources, at least 4 primary and at least 1 secondary. The
constrained-decoding implementations, the Tam et al. study, and the provider
structured-output docs are primary to their claims. Meet the floor with sources
that carry a rung, not padding.

## Production

Profile balanced; no stage required. This run: writing-coach and researcher on
the strong model, researcher at high effort; writer at medium effort; editor at
high effort.

## Recent habits not to inherit

- The two-clause "and/but" dek is the current house default; build the dek
  another way and avoid the three banned molds in `spec/headlines.md`.
- "How...", "What...", "Where..." heading openers are overused across the desk.
  Name each section step in this piece's own nouns.
- The desk recently closed a piece by returning to its opening image; do not
  reuse that return-to-the-opener closing move.
