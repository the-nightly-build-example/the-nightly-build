# Evidence: the-mechanics/prefill-and-decode (01)

The evidence cleanly supports the commission's spine. Four independent
first-party systems papers (vLLM/PagedAttention, Splitwise, DistServe,
Sarathi-Serve) plus the original Transformer paper and FlashAttention establish,
firsthand and in agreement, the two-phase structure and its cause: prefill runs
all prompt tokens through one parallel forward pass and is compute-bound; decode
generates one token per step, and because each step must read the whole KV cache
back from memory while doing little arithmetic, decode is memory-bandwidth-bound.
The KV cache and its per-token size are pinned to a primary with an exact formula
(vLLM: 800 KB per token for OPT-13B; 1.6 GB for one 2048-token sequence). The two
user-visible metrics (time-to-first-token and inter-token latency / time-per-output-token)
are defined by a first-party inference doc (NVIDIA NIM benchmarking) and mapped
explicitly to the two phases. What is settled is the two-phase split, the cache,
and the memory-bound character of decode: every primary agrees, and no primary
contradicts it. What is not settled is how to organize the two phases across
hardware — the frontier splits between disaggregation (Splitwise, DistServe put
prefill and decode on separate machines) and fusion (Sarathi-Serve interleaves
them with chunked prefill), a genuine live disagreement the lesson can mark. The
record is thin in exactly one place the writer must respect: every throughput,
latency, and utilization number is model- and GPU-specific and must be labeled
illustrative, never universal. The common wrong explanation to avoid (decode is
compute-bound; the KV cache is optional) appears only in secondary explainers,
never in the primaries.

## Sources

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — it authored the attention mechanism and the query/key/value
             construction the KV cache stores. Owns the definition of "keys" and "values".
Establishes: What keys (K) and values (V) are, and why an autoregressive decoder can
             reuse them. Attention output is a weighted sum of values, weights set by
             query-key dot products; the decoder is autoregressive and causally masked,
             so token t depends only on tokens 1..t.
Paraphrase:  Scaled dot-product attention computes Attention(Q,K,V)=softmax(QK^T/sqrt(d_k))V:
             each output is a weighted sum of the value vectors, the weight on each value
             set by the compatibility (dot product) of the query with that value's key.
             The decoder is auto-regressive, consuming previously generated symbols as
             additional input when generating the next, and masking prevents any position
             from attending to later positions. Because a past token's key and value never
             change once computed, they can be cached rather than recomputed — the structural
             basis for the KV cache.
Locators:    Section 3.2.1 (Scaled Dot-Product Attention); Section 3 intro (auto-regressive
             decoder); Section 3.2.3 (masking to preserve the auto-regressive property).
Quote:       "The output is computed as a weighted sum of the values, where the weight
             assigned to each value is computed by a compatibility function of the query
             with the corresponding key." / "At each step the model is auto-regressive,
             consuming the previously generated symbols as additional input when generating
             the next." / "We need to prevent leftward information flow in the decoder to
             preserve the auto-regressive property."
```

```text
URL:         https://arxiv.org/abs/2205.14135
Kind:        primary — the paper that owns the IO-aware analysis of attention; authored
             by Dao et al. It defines compute-bound vs memory-bound for GPU operations.
Establishes: The precise definitions of memory-bound and compute-bound, and that most
             Transformer operations are bottlenecked by memory (HBM) accesses, not compute.
             This is the general principle under decode's memory-bandwidth bound.
Paraphrase:  A compute-bound operation's runtime is set by its arithmetic-operation count,
             with HBM-access time much smaller; a memory-bound operation's runtime is set by
             its number of memory accesses, with computation time much smaller (examples:
             elementwise ops, softmax, layer norm). As compute has gotten faster relative to
             memory, operations are increasingly bottlenecked by memory accesses, and for
             attention the number of HBM accesses is the primary factor affecting runtime.
Locators:    Section 2.1 (Hardware Performance — bound definitions); Section 3.2 / Figure 2
             (HBM access as the primary runtime factor).
Quote:       "Compute-bound: the time taken by the operation is determined by how many
             arithmetic operations there are, while time accessing HBM is much smaller." /
             "Memory-bound: the time taken by the operation is determined by the number of
             memory accesses, while time spent in computation is much smaller." / "As compute
             has gotten faster relative to memory speed, operations are increasingly
             bottlenecked by memory (HBM) accesses."
```

```text
URL:         https://arxiv.org/abs/2309.06180
Kind:        primary — the vLLM/PagedAttention paper (Kwon et al., SOSP 2023). Owns the
             KV-cache definition used across the field and the per-token size formula.
Establishes: (a) What the KV cache is and why caching avoids recomputation; (b) prompt/prefill
             is parallelizable and uses GPU parallelism well; (c) autoregressive generation is
             sequential, underutilizes compute, and is memory-bound; (d) exact KV-cache size.
Paraphrase:  The key and value vectors of existing tokens are cached to generate future tokens
             (the KV cache). Because all prompt tokens are known, the prompt phase is
             parallelized with matrix-matrix multiplication and uses GPU parallelism
             efficiently. At each generation step only the new token's key and value are
             computed; positions 1..n+t-1 are already cached. Generation cannot be
             parallelized across steps because of the data dependency and uses matrix-vector
             multiplication, so it "severely underutilizes GPU computation and becomes
             memory-bound." For OPT-13B, one token's KV cache needs 800 KB
             (2 x 2 x 5120 x 40 x 2 bytes); one 2048-token request can need up to 1.6 GB.
Locators:    Section 2.2 (prompt vs autoregressive phases, KV cache definition); Section 3
             (KV cache size formula and 1.6 GB figure).
Quote:       "The computation at different iterations cannot be parallelized due to the data
             dependency and often uses matrix-vector multiplication, which is less efficient.
             As a result, this phase severely underutilizes GPU computation and becomes
             memory-bound." / "for the 13B parameter OPT model, the KV cache of a single token
             demands 800 KB of space, calculated as 2 (key and value vectors) x 5120 (hidden
             state size) x 40 (number of layers) x 2 (bytes per FP16)."
             [Note: the source's prose writes the factors as 2 x 2 x 5120 x 40 x 2; see
             Numbers section for the exact arithmetic and the ambiguity to preserve.]
```

```text
URL:         https://arxiv.org/abs/2311.18677
Kind:        primary — Splitwise (Patel et al., ISCA 2024). Owns a hardware-level
             characterization of the two phases and one side of the disaggregation frontier.
Establishes: The two-phase split named as prompt-computation (compute-intensive) vs
             token-generation (memory-bandwidth-and-capacity bound); that the split can be
             disaggregated onto separate machines. Distinct actors from DistServe, so the
             frontier claim has independent primary backing.
Paraphrase:  The prompt-computation phase runs all input prompt tokens through the forward
             pass in parallel to generate the first output token and is computationally
             intensive. The token-generation phase generates subsequent tokens sequentially
             from the last token plus the cached context (KV cache); lacking compute
             parallelism, it is memory-bandwidth and capacity bound, and its power draw does
             not rise as more tokens are processed. Splitwise runs prefill and decode on
             separate instances, each with its own KV-cache pool, and reports a 1.4x
             throughput gain at 20% lower cost.
Locators:    Section I (Introduction — phase characterization); Section II-B (Generative LLM
             Inference Phases); Section III-B/D/F (batch utilization, throughput, power).
Quote:       "the token generation phase, in which subsequent output tokens are generated
             sequentially based on the forward pass of the last token and all the cached
             context from previous tokens in the sequence. Given the lack of compute
             parallelism, this phase tends to be more memory bandwidth and capacity bound."
```

```text
URL:         https://arxiv.org/abs/2401.09670
Kind:        primary — DistServe (Zhong et al., OSDI 2024). Owns the goodput case for
             disaggregation and gives clean prefill/decode + TTFT/TPOT definitions.
Establishes: Prefill processes all prompt tokens concurrently and is compute-bound for
             non-trivial prompts; decode processes one new token per step yet incurs
             prefill-level I/O and is memory-bandwidth constrained; TTFT = prefill duration,
             TPOT = average per-output-token time; KV cache exists to avoid recomputation.
Paraphrase:  The prefill step processes a new sequence's many tokens concurrently; each
             decoding step processes only one new token. For a 13B LLM, prefilling a
             512-token sequence makes an A100 compute-bound. Decoding, though it processes one
             token per step, incurs I/O similar to prefill and is therefore constrained by GPU
             memory bandwidth. TTFT is the duration of the prefill phase; TPOT is the average
             time to generate each token after the first. KV caches are the per-token
             intermediate states saved in GPU memory to avoid recomputing them in later steps.
Locators:    Section 1 (Introduction — TTFT/TPOT, phase overview); Section 2.1 (phase
             definitions, compute- vs memory-bound, KV cache).
Quote:       "The decoding phase, despite processing only one new token per step, incurs a
             similar level of I/O to the prefill phase, making it constrained by the GPU's
             memory bandwidth." / "The time to first token (TTFT), which is the duration of
             the prefill phase, and the time per output token (TPOT), which represents the
             average time taken to generate a token for each request (except for the first
             token)." / "for a 13B LLM, computing the prefill of a 512-token sequence makes an
             A100 compute-bound."
```

```text
URL:         https://arxiv.org/abs/2403.02310
Kind:        primary — Sarathi-Serve (Agrawal et al., OSDI 2024). Owns the arithmetic-intensity
             framing and the other side of the frontier (fuse via chunked prefill, not split).
Establishes: Prefill has high arithmetic intensity (compute-bound); decode has very low
             arithmetic intensity (memory-bound); decode needs all prior keys and values; a
             concrete cost ratio between a decode token and prefill tokens. Also that the
             prefill/decode split is being actively re-engineered by fusion rather than
             disaggregation — a direct counter-design to Splitwise/DistServe.
Paraphrase:  During prefill all prompt tokens are processed in parallel in a single iteration,
             using GPU compute efficiently; prefill batches amortize the cost of fetching
             linear-operator weights from HBM over many tokens, giving high arithmetic
             intensity (compute-bound). Decode does a full forward pass over one token and
             requires access to all keys and values of previously processed tokens; decode
             batches have very low compute intensity and are bottlenecked by memory-fetch time
             (memory-bound). Because of this, the linear-operator cost of one decode token is
             nearly the same as 128 prefill tokens (Mistral-7B, single A100). Sarathi-Serve
             splits prefills into chunks and schedules them alongside ongoing decodes
             ("stall-free"), the opposite of disaggregation.
Locators:    Section 2.2 (phase definitions, KV cache access); Section 3.2 (arithmetic
             intensity, the 1-decode-token ≈ 128-prefill-tokens figure); Figure 3 (batching
             boosts decode throughput ~linearly, marginal on prefill); Figure 6 (arithmetic
             intensity, LLaMA2-70B on 4xA100).
Quote:       "During the prefill phase all these prompt tokens are processed in parallel in a
             single iteration." / "the decode phase ... requires access to all the keys and
             values associated with all the previously processed tokens." / "the cost of
             linear operation for 1 decode token is nearly same as 128 prefill tokens."
```

```text
URL:         https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html
Kind:        primary (first-party) — NVIDIA's own NIM/AIPerf benchmarking documentation. It
             owns these metric definitions for its tooling, and defines them for the field.
Establishes: The two user-visible metrics and their exact mapping to the two phases: TTFT
             (prefill-side) and inter-token latency / time-per-output-token (decode-side),
             with the ITL formula. Anchors the felt "pause then steady stream" to named metrics.
Paraphrase:  Time to first token (TTFT) is the time from query submission to the first
             received token; it includes request queuing, prefill, and network latency.
             Inter-token latency (ITL), also called time per output token (TPOT), is the
             average time between consecutive tokens; computed as
             (end-to-end latency - TTFT) / (total output tokens - 1), so it excludes the first
             token and characterizes only decoding. Total tokens per second (TPS) is total
             output-token throughput across concurrent requests.
Locators:    "Time to First Token", "Inter-token Latency", and "Total tokens per second (TPS)"
             sections of the metrics page.
Quote:       "Inter-token latency (ITL) is defined as the average time between consecutive
             tokens and is also known as time per output token (TPOT)." /
             "ITL = (e2e_latency - TTFT) / (Total_output_tokens - 1)"
```

```text
URL:         https://www.databricks.com/blog/llm-inference-performance-engineering-best-practices
Kind:        secondary — reputable engineering explainer (Databricks/Mosaic). Reports and
             synthesizes the primary characterization for practitioners; does not own the
             mechanism. Use for context and framing only, not as the authority on any claim.
Establishes: That the compute-bound-prefill / memory-bound-decode split and the TTFT / output-
             tokens-per-second metric pair are the standard practitioner framing — useful to
             confirm the lesson matches how engineers actually talk, not to establish fact.
Paraphrase:  Prefill (first-token generation) is compute-limited and is sped up by more FLOPS;
             decode is memory-bound, its speed limited by memory access and bandwidth rather
             than raw compute. Memory bandwidth is often the more useful predictor of inference
             speed than peak compute. The visible metrics are TTFT and output tokens per second.
Locators:    Sections on prefill vs decode and on latency metrics (TTFT, TPOT).
Quote:       "Generating the first token is typically compute-bound, while subsequent
             decoding is memory-bound operation." / "Available and achieved memory bandwidth
             in inference hardware is a better predictor of speed of token generation than
             their peak compute performance." (secondary — confirms the practitioner framing,
             not the authority on the fact.)
```

## Contradictions

- **Real design disagreement at the frontier (not a factual conflict).** Splitwise
  (https://arxiv.org/abs/2311.18677) and DistServe (https://arxiv.org/abs/2401.09670)
  argue the two phases should be *disaggregated* onto separate machines because
  colocating them causes prefill-decode interference. Sarathi-Serve
  (https://arxiv.org/abs/2403.02310) argues the opposite organization: keep them on
  the same GPU and *fuse* them with chunked prefill and "stall-free" scheduling.
  Both are primaries by parties in a position to know. This is not a contradiction
  about the mechanism (all three agree prefill is compute-bound and decode is
  memory-bound); it is the live engineering argument about what to do with that
  asymmetry. The lesson should present it as the honest open frontier, and must not
  imply the field has settled on one architecture.

- **No primary contradicts the core characterization.** A deliberate search for
  sources claiming decode is compute-bound, or that the KV cache is optional/avoidable,
  found this framing only in informal secondary explainers, never in a primary. Every
  primary read (vLLM, Splitwise, DistServe, Sarathi-Serve, FlashAttention) states the
  same direction: prefill compute-bound, decode memory-bandwidth-bound. The core claim
  is as settled as anything in this record. See Discarded for the wrong-explanation
  pattern the writer should pre-empt.

- **One in-source arithmetic ambiguity (not a contradiction between sources).** The
  vLLM paper's prose for the 800 KB/token figure lists the factors slightly
  differently across renderings (whether the leading "2 x 2" is stated once or twice).
  The arithmetic that yields 800 KB is 2 (key and value) x 5120 (hidden size) x 40
  (layers) x 2 (FP16 bytes) x 2 — see Numbers. Preserve the paper's own factors; do
  not "correct" them silently.

## Numbers

Every figure below is model- and hardware-specific. Label each **illustrative**, never
universal. The direction of each claim (prefill compute-bound, decode memory-bound) is
universal; the magnitudes are not.

```text
Figure: 800 KB of KV cache per token
Owner:  vLLM/PagedAttention, https://arxiv.org/abs/2309.06180, Section 3
Scope:  OPT-13B, FP16. Factors: (key and value) x 5120 hidden size x 40 layers x 2 bytes
        per FP16. Grows linearly with layers, hidden size, and precision; a different
        model or dtype gives a different number. Illustrative.
```

```text
Figure: up to 1.6 GB of KV cache for a single request
Owner:  vLLM/PagedAttention, https://arxiv.org/abs/2309.06180, Section 3
Scope:  OPT-13B, one sequence at its 2048-token maximum context, FP16. Scales with
        sequence length. Illustrative; larger-context models today are far larger.
```

```text
Figure: cost of 1 decode token ~= cost of 128 prefill tokens (linear-operator cost)
Owner:  Sarathi-Serve, https://arxiv.org/abs/2403.02310, Section 3.2
Scope:  Mistral-7B, single NVIDIA A100. This is the arithmetic-intensity gap made
        concrete: decode wastes compute because it reads weights for one token.
        The exact ratio is model/GPU specific. Illustrative.
```

```text
Figure: a 512-token prefill makes an A100 compute-bound
Owner:  DistServe, https://arxiv.org/abs/2401.09670, Section 2.1
Scope:  13B-class LLM, NVIDIA A100. The threshold prompt length at which prefill
        saturates compute depends on model and GPU. Illustrative.
```

```text
Figure: batching boosts decode throughput ~linearly but has marginal effect on prefill throughput
Owner:  Sarathi-Serve, https://arxiv.org/abs/2403.02310, Figure 3
Scope:  Mistral-7B, single A100. Explains why decode is batched aggressively and prefill
        is not; the shape is general, the crossover points are hardware-specific. Illustrative.
```

```text
Figure: PagedAttention raised KV-cache memory utilization from 20-40% to ~96%; ~2-4x throughput
Owner:  vLLM/PagedAttention, https://arxiv.org/abs/2309.06180 (abstract/eval)
Scope:  vs FasterTransformer and Orca baselines, specific models/GPUs in the paper.
        Peripheral to this lesson (it is about memory fragmentation, not the phase split);
        include only if the lesson touches why the cache is hard to manage. Illustrative.
```

```text
Figure: ITL = (e2e_latency - TTFT) / (total_output_tokens - 1)
Owner:  NVIDIA NIM/AIPerf docs, https://docs.nvidia.com/nim/benchmarking/llm/latest/metrics.html
Scope:  Definitional, not empirical. Safe to state as the definition of inter-token
        latency / time-per-output-token. Not hardware-dependent.
```

```text
Figure: Splitwise reports ~1.4x throughput at ~20% lower cost via phase disaggregation
Owner:  Splitwise, https://arxiv.org/abs/2311.18677
Scope:  Specific model/GPU mix (H100/A100 pools) in the paper. A design result, not a
        universal constant. Illustrative; use only to show the frontier is active.
```

## Source assets

```text
Asset: Sarathi-Serve Figure 3 — decode vs prefill throughput as batch size grows
       (https://arxiv.org/abs/2403.02310), Mistral-7B on one A100.
Shows: Batching lifts decode throughput almost linearly while barely moving prefill —
       the single clearest visual of the compute-bound / memory-bound asymmetry.
Crop:  Must keep both curves, both axis labels (batch size; throughput), and the model/GPU
       caption. Do not crop to one curve; the contrast is the point. Reproduce only if the
       lesson licenses a chart, and cite Mistral-7B / A100 in the caption.
```

```text
Asset: DistServe Figure 1 — goodput of prefill-only vs decode-only vs colocated serving
       (https://arxiv.org/abs/2401.09670), OPT-13B on A100-80GB, in=512/out=64.
Shows: Why the two phases pull hardware in different directions; motivates disaggregation.
Crop:  Keep all three bars/lines and the SLO framing; keep the model/GPU/input-output caption.
       Secondary to the lesson's core; use only if the frontier gets real space.
```

```text
Asset: vLLM KV-cache size formula for OPT-13B (prose/inset, Section 3)
       (https://arxiv.org/abs/2309.06180).
Shows: The per-token cache cost as a concrete arithmetic expression — better rendered as a
       small formula/callout than a chart.
Crop:  If reproduced, keep every factor (key/value, hidden size, layers, bytes) so the reader
       can rebuild 800 KB themselves. Not a decorative image.
```

```text
Asset: TTFT-vs-prompt-length series (the most on-point chart for this lesson's felt pause).
Shows: How the initial wait grows with prompt length — the reader's "pause."
Crop:  None found as a clean, extracted numeric series in the primaries read. The claim that
       TTFT scales with prompt length is well supported qualitatively (prefill is O(prompt)),
       but I did not verify a published numeric series with stated model/GPU conditions. If
       the writer wants this chart, it needs a sourced series first; do not fabricate one.
```

## Discarded

```text
URL: https://www.emergentmind.com/topics/prefill-decode-p-d-disaggregated-architectures
     — aggregator/topic page; correct in gist but secondary-of-secondary. Superseded by the
     primaries it summarizes (Splitwise, DistServe). Not cited.
URL: Various Medium/Towards-AI explainers surfaced while searching for the common wrong
     explanation (e.g. medium.com "KV Cache: Hidden Memory Monster", pub.towardsai.net
     "Inside LLM Inference"). Read far enough to confirm they carry the *correct* direction
     but at explainer depth with no owned claims; a few informal posts elsewhere blur decode
     as "compute" work. Recorded here as the pattern to pre-empt, not cited: the lesson should
     state plainly that decode is memory-bandwidth-bound and the KV cache is what makes it so,
     so a reader can catch an explanation that skips this.
URL: https://www.usenix.org/system/files/osdi24-agrawal.pdf — the USENIX-hosted Sarathi-Serve
     PDF returned HTTP 403 to the fetch tool (gated, not dead). Used the arXiv version of the
     same paper (https://arxiv.org/abs/2403.02310) instead; the canonical citation is the
     arXiv abstract page recorded above.
```
