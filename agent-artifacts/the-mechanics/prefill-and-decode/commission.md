# Commission: the-mechanics/prefill-and-decode

## Assignment
Start from a behavior anyone who uses a chatbot has felt: you send a long
message, there is a pause, and then the answer streams out word by word at a
steady pace. Work backward to the cause. This is the the-mechanics desk: name a
real part of the system at each step, keep going until the reader hits ground,
and mark which steps are settled engineering and which are open.

## The behavior and its cause
Two phases run under every response. Prefill: the model reads the whole prompt
in one parallel pass and fills the key/value cache — this is the pause, and it
scales with prompt length. Decode: the model then generates one token at a time,
each step reading the whole cache to produce the next token, appending it, and
repeating — this is the steady stream, and it is sequential by construction. The
lesson explains why reading 10,000 prompt tokens is fast and cheap per token
while writing 500 output tokens is slow and expensive per token: prefill is
compute-bound and parallel; decode is memory-bandwidth-bound and serial, because
each new token depends on all the tokens before it.

## Teach these, completely (2–3 ideas, not six)
1. Prefill vs decode as two different jobs on the same weights: one parallel
   pass over the prompt vs one-token-at-a-time generation. Ground it in the
   felt behavior (time-to-first-token vs tokens-per-second).
2. The KV cache and why it exists: without it, each new token would recompute
   attention over the whole sequence from scratch; the cache stores the per-token
   keys and values so each decode step is cheap in compute but must stream the
   growing cache from memory. This is the settled-engineering core.
3. The consequence the reader can now predict: long prompts raise the initial
   wait and memory footprint but are cheap per token; long outputs are what make
   a response slow, because decode cannot be parallelized across its own future
   tokens. Connect to why output tokens cost more (one sentence; the dollars are
   cost-per-token's lesson, not this one).

## Boundaries
- One lesson, lesson template, 1200–2200 words. No code.
- Build on published lessons by linking, not re-teaching: attention
  (the-mechanics/attention), autoregressive-generation
  (the-mechanics/autoregressive-generation), sampling-temperature. Link these in
  prose or Background; assume the reader can meet them there. This lesson's new
  ground is the prefill/decode split and the KV cache as the *cause of latency*,
  which the attention and autoregressive lessons do not cover.
- Mark honestly what is settled (the two-phase structure, the cache, the
  memory-bandwidth bound in decode) vs where numbers vary (exact throughput,
  batching effects, hardware specifics). Do not overclaim precise figures.

## Source policy (from `nb source-policy --series the-mechanics`)
- Minimum 8 sources; primary >= 4, secondary >= 1.
- Primary = papers/engineering write-ups that own the mechanism: the original
  transformer/attention paper for the KV structure, vLLM/PagedAttention and
  FlashAttention papers, systems papers on LLM inference (e.g. Splitwise or
  Sarathi on prefill/decode disaggregation), first-party inference docs that
  define time-to-first-token vs inter-token latency. Secondary = reputable
  engineering explainers for context only.

## Production policy (from `nb production-policy --series the-mechanics`, profile balanced)
- writing-coach: capable / low  → claude (sonnet)
- researcher: capable / high     → claude (opus, claude-opus-4-8)
- writer: capable / medium       → claude (opus, claude-opus-4-8)
- editor: capable / high         → claude (opus, claude-opus-4-8)
No `required` directive; capable tier honored, no deviation.

## Tags
No tag prompt-fragments configured for this series; ships with empty tag list.

## This edition's neighbors (keep distinct, one paper)
Runs tonight with the-evidence/alphafold, the-instruments/cost-per-token,
what-could-go-wrong/self-replication, when-ai-breaks/amazon-hiring-tool. Nearest
neighbor is cost-per-token (also involves tokens and output-token expense). Seam:
this lesson explains *why decode is slow* (mechanism); it does not price it.
Hand the dollar question to that lesson in a single sentence and link nothing to
it (both publish tonight, so no cross-link exists yet).

## Recent shapes in this series to break (do not inherit)
The series overuses the "A model that X never Y" / "The instant a model writes a
token" declarative-mechanism headline (tool-use, losing-the-thread,
autoregressive-generation). Find a fresh headline that names the prefill/decode
split or the felt pause-then-stream, without copying that opener frame. Avoid
comma-triad and semicolon-reversal deks.
