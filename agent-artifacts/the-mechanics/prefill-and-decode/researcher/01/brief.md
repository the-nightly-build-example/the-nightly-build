# researcher brief: the-mechanics/prefill-and-decode (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/commission.md — assignment, angle, boundaries, source floor
- /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/editorial-direction.md — citation standard, series territory, declared reader

Output: /home/user/the-nightly-build/.nb-work/the-mechanics/prefill-and-decode/agent-artifacts/the-mechanics/prefill-and-decode/researcher/01/evidence.md

Source floor: >= 8 sources, >= 4 primary, >= 1 secondary. Read the systems
papers themselves, at the sections that define the mechanism.

Questions the evidence must answer:
1. Primary definition of the prefill and decode (generation) phases of LLM
   inference, from a paper or first-party engineering source that owns the
   terms. Establish that prefill processes all prompt tokens in parallel and
   decode generates one token per step. (Sarathi-Serve, Splitwise, DistServe,
   or vLLM/PagedAttention are candidate primaries.)
2. The KV cache: what keys and values are cached, why caching avoids recomputing
   attention over the full prefix each step, and the cost it moves — decode
   becomes memory-bandwidth-bound because each step streams the whole cache.
   Source this to attention/transformer or inference-systems primaries, not
   explainers. Confirm the "memory-bandwidth-bound decode vs compute-bound
   prefill" characterization against a primary.
3. Time-to-first-token vs inter-token latency / tokens-per-second as the two
   user-visible metrics that map to the two phases. A first-party inference doc
   defining them is ideal. A concrete order-of-magnitude illustration (e.g. how
   TTFT grows with prompt length, or a published prefill-vs-decode throughput
   gap) with its exact source and conditions — label it as illustrative, not
   universal.
4. What is settled vs open/variable: the two-phase structure and the cache are
   settled; exact throughput, batching/continuous-batching effects, and
   prefill/decode disaggregation are active engineering. Find a primary showing
   the split being actively re-engineered (disaggregation) so the lesson can
   mark that frontier honestly.
5. One small, real, concrete example to anchor the mechanism (e.g. a documented
   KV-cache size formula or a stated per-token memory-read cost), sourced.

Watch for and record: sources that oversimplify (claiming decode is
compute-bound, or that the KV cache is optional) so the writer can avoid the
common wrong explanation. In Numbers, record any figure with owner, scope, and
the hardware/model conditions it assumes. Note any honest chart opportunity
(e.g. TTFT vs prompt length) only if a verified series exists.
