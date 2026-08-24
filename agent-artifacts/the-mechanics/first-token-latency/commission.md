# Commission: the-mechanics/first-token-latency

## The behavior

The reader sends a message to a chatbot and the response takes a moment to start
appearing. The pause grows with the length of the message. Once the response
starts, it streams smoothly at what feels like a steady pace. The lesson works
backward from this behavior to the mechanism that produces it.

## The angle

Explain the chain from the felt pause down to a step where nothing below it
would change the answer. The pause is prefill: the model has to process every
input token before it can produce the first output token, and processing an
input token is a matrix operation whose cost grows with how many earlier tokens
it can attend to. The smooth streaming afterward is decode: one token at a time,
each cheap because attention over the prefilled cache is cheaper than over the
raw input. Mark which steps are settled engineering (that prefill and decode
have very different cost profiles; that attention over long inputs is quadratic
without care; that the KV cache stores the intermediate state that decode
reuses) and which are open (how far a given serving stack has moved the balance
with speculative decoding, paged attention, or continuous batching).

Ground the settled part in a concrete case: a published benchmark or vendor
number showing the time-to-first-token growing with input length while
per-token decode stays roughly flat.

## Teach, in this order

1. The behavior, with a worked case: a prompt that shows a longer input pauses
   longer before starting, then streams at about the same pace as a short one.
   No code.
2. Why prefill is where the pause lives: what "process the input" means for a
   transformer, and why attention over a long context is expensive up front.
3. Why decode feels smooth: the KV cache, and one token at a time; where the
   chain bottoms out (settled) and what stays open (the serving-stack
   optimizations that trade prefill for decode or otherwise reshape the pause).

## Sources

Series policy requires at least eight sources, at least four primary and at
least one secondary. Primaries include the paper(s) that describe attention
cost and the KV cache; a serving-system paper (e.g. vLLM, PagedAttention, or a
current inference-engine paper) that measures TTFT and per-token decode
separately; a vendor's own latency documentation that reports TTFT and output
token times as distinct numbers; and at least one benchmark or evaluation paper
that measures TTFT across input lengths. The researcher resolves the exact set.

## Boundaries and neighbors

The 2026-08-24 edition runs this alongside the-evidence/retrieval-augmented-
generation, the-instruments/rewardbench, what-could-go-wrong/algorithmic-
monoculture, and when-ai-breaks/nyc-mycity-chatbot. No topic overlap with those.

The-mechanics has published lessons on prefill-and-decode (the machinery of the
two phases), autoregressive-generation (why decode is one token at a time),
attention (what attention costs), and tokens-per-second (a related but distinct
instrument covered in the-instruments). Link them in Background and do not
re-teach the machinery; this lesson stays on the felt behavior — the pause —
and works down to why it lives where it does. Keep the-mechanics's no-code
rule.

## Production record

Template: lesson. Series: the-mechanics (open section, self-chosen topic).
Production policy resolved to the balanced profile: writing-coach effort low,
researcher effort high, writer effort medium, editor effort high, model
"capable" for every role. No `required` directive applies.
