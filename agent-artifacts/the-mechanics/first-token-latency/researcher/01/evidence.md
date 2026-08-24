# Evidence: the-mechanics/first-token-latency

The sources support the commission's core chain. The pause before the first
token is the prefill phase, which reads the whole input in one forward pass and
produces both the first output token and the key-value cache that the decode
loop then reuses. Prefill is compute-bound and its cost per request grows with
input length; decode is memory-bandwidth-bound and its cost per token is roughly
flat once the cache is in place. This story is stated in nearly the same words
by two academic serving-system papers (vLLM/PagedAttention at SOSP 2023; Pope
et al. at MLSys 2023), a serving-system paper that explicitly measures the two
phases separately (DistServe, OSDI 2024), and two vendor pages (Together AI,
Anthropic). The attention paper itself supplies the per-layer complexity that
makes prefill grow with n (O(n^2 * d) for self-attention, O(n * d^2) for the
position-wise feed-forward).

The record is thin in two places. First, the naive "TTFT grows quadratically in
input tokens" claim is only true in the long-context regime. For typical chatbot
prompts the feed-forward and projection costs dominate, so TTFT grows nearly
linearly and each input token costs about 1% of an output token in end-to-end
time (Kadous et al. for Anyscale/LLMPerf). The super-linear growth shows up at
32K-plus tokens (an NVIDIA GH200 Llama 3.1 70B run relayed by Redis, and a
Baseten Mistral 7B run). Second, the "smooth streaming" story is only smooth
inside one request in isolation. DistServe's Figure 2 shows that a single new
prefill inserted into a batch of ongoing decodes lengthens time-per-output-token
for all the streaming users; chunked prefill (Sarathi, Sarathi-Serve) softens
that but explicitly trades TTFT for TPOT; speculative decoding (Leviathan et
al.) speeds decode without touching prefill. These optimizations reshape the
pause-versus-stream picture in ways the simple two-phase account does not
capture. Numbers below are pulled from each paper's own tables and figures.

## Sources

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary. The paper that introduces the Transformer and gives the
             self-attention complexity everyone else cites.
Establishes: The per-layer computational cost of self-attention as a function of
             sequence length n and representation dimension d, and where that
             cost sits relative to the recurrent and convolutional alternatives.
Paraphrase:  Section 4 (page 6) gives Table 1: self-attention has complexity
             per layer O(n^2 * d) and O(1) sequential operations; a recurrent
             layer is O(n * d^2) and O(n) sequential; a convolutional layer is
             O(k * n * d^2). The text notes that self-attention is faster than
             recurrent layers only when n < d, which is "most often the case"
             for sentence-length inputs but stops being true for very long
             contexts. To keep long-sequence attention tractable the authors
             suggest restricted self-attention over a neighborhood r, giving
             O(r * n * d) per layer at the cost of longer path length O(n/r).
Locators:    Section 4, "Why Self-Attention", page 6; Table 1 on page 6.
Quote:       "As noted in Table 1, a self-attention layer connects all
             positions with a constant number of sequentially executed
             operations, whereas a recurrent layer requires O(n) sequential
             operations. In terms of computational complexity, self-attention
             layers are faster than recurrent layers when the sequence length n
             is smaller than the representation dimensionality d..."
```

```text
URL:         https://arxiv.org/abs/2309.06180
Kind:        primary. Kwon et al., "Efficient Memory Management for Large
             Language Model Serving with PagedAttention" (vLLM), SOSP 2023.
             The authors are the ones who built the system and ran the
             throughput and latency measurements.
Establishes: The named two-phase decomposition of an LLM request (prompt
             phase / autoregressive generation phase); why prompt-phase
             computation can be parallelized while decode cannot; the KV cache
             as the state the decode loop reuses; and that decode "becomes
             memory-bound, being responsible for most portion of the latency of
             a single request".
Paraphrase:  Section 2.1 defines the prompt phase as taking the whole user
             prompt x_1..x_n as input and computing P(x_{n+1} | x_1..x_n),
             producing the first new token and the key/value vectors k_1..k_n
             and v_1..v_n along the way; because all prompt tokens are known,
             this phase "can be parallelized using matrix-matrix multiplication
             operations" and "can efficiently use the parallelism inherent in
             GPUs." Section 2.1 then defines the autoregressive generation
             phase: at iteration t the model takes one token x_{n+t} and
             computes the next distribution using the key/value vectors k_1..
             k_{n+t}, v_1..v_{n+t}, where the values for positions 1..n+t-1
             "are cached at previous iterations" and only the new k_{n+t},
             v_{n+t} are computed. The iterations "cannot be parallelized due
             to the data dependency and often uses matrix-vector
             multiplication, which is less efficient. As a result, this phase
             severely underutilizes GPU computation and becomes memory-bound,
             being responsible for most portion of the latency of a single
             request." Section 2.2 introduces the KV cache as the cached key
             and value vectors of existing tokens, noting the cache is unique
             to each sequence and position. Section 6 reports vLLM sustains
             1.7x-2.7x higher request rates than Orca (Oracle) and 2.7x-8x
             higher than Orca (Max) at the same normalized latency on
             ShareGPT.
Locators:    Section 2 "Background", subsections 2.1 and 2.2, pages 2-3;
             throughput results in Section 6, Figure 12, pages 9-11.
Quote:       "As a result, this phase severely underutilizes GPU computation
             and becomes memory-bound, being responsible for most portion of
             the latency of a single request."
```

```text
URL:         https://arxiv.org/abs/2211.05102
Kind:        primary. Pope et al., "Efficiently Scaling Transformer
             Inference", MLSys 2023 (Outstanding Paper). Google authors giving
             their own PaLM 540B measurements.
Establishes: The explicit split of an inference request into a "prefill" step
             that processes the input in parallel and a "decode" (or
             "generation") step that runs sequentially; the KV cache as the
             per-layer state that must be held on-chip and re-read per token;
             the observation that at small batch sizes and short contexts
             "the time to load weights dominates" while at large batches and
             long contexts "the time to load the KV cache dominates"; and
             concrete numbers for PaLM 540B (29 ms per generated token at low
             batch size, 76% MFU during large-batch input processing).
Paraphrase:  Section 2.2 (page 3) writes: "The latency is the total time for
             an inference and can be broken down into the time to process the
             input tokens present at the start of the inference (which we call
             'prefill') and the time to autoregressively generate output
             tokens (which we term 'decode'). The decode latency can also be
             measured 'per step', i.e. divided by the number of tokens in each
             sequence." Section 2 also introduces the KV cache as the
             per-layer key/value tensors from all previous tokens, held in
             on-device high-bandwidth memory. The abstract reports a
             low-batch-size latency of 29 ms per token during generation
             (with int8 weight quantization) and 76% MFU during large-batch
             input processing on the PaLM 540B model on 64 TPU v4 chips.
             Section 3 explains that lower latency can be achieved with
             smaller batches but at the cost of worse MFU. For a chatbot
             deployment, the authors recommend combining batch-1 prefill with
             batch-32-to-64 decode to keep the KV cache manageable.
Locators:    Abstract; Section 2.2 "Inference cost tradeoffs", page 3;
             Section 3, pages 4-5.
Quote:       "The latency is the total time for an inference and can be
             broken down into the time to process the input tokens present at
             the start of the inference (which we call 'prefill') and the
             time to autoregressively generate output tokens (which we term
             'decode')."
```

```text
URL:         https://arxiv.org/abs/2401.09670
Kind:        primary. Zhong et al., "DistServe: Disaggregating Prefill and
             Decoding for Goodput-optimized Large Language Model Serving",
             OSDI 2024. Peking University, StepFun, and UC San Diego. First-
             hand measurements of TTFT vs TPOT on a 13B and 66B model on
             NVIDIA A100 80GB GPUs.
Establishes: That the two phases carry distinct latency metrics -- time to
             first token (TTFT) for prefill and time per output token (TPOT)
             for decode -- and that colocating them on the same GPU causes
             "prefill-decoding interference" that inflates both. Also that
             chunked prefill "trades TTFT for TPOT."
Paraphrase:  Section 1 (page 1) writes: "an LLM service's latency is uniquely
             measured by two key metrics: the time to first token (TTFT),
             which is the duration of the prefill phase, and the time per
             output token (TPOT), which represents the average time taken to
             generate a token for each request (except for the first token)."
             Section 3 states that prefill "tends to be compute-bound", while
             decode "batches multiple m x 1 matrix-vector multiplications" and
             is memory-bound. Section 2.3 (Figure 2) shows that adding a
             single prefill job to a batch of decoding requests significantly
             extends both TTFT and TPOT: "the decoding tasks in the batch
             must wait for lengthier prefill jobs to complete, thus extending
             TPOT; the slowdown intensifies with a longer prefill." Section
             2.3 addresses chunked prefill directly: an "advanced variant of
             continuous batching attempts to balance TTFT and TPOT by
             segmenting long prefill into chunks and attaching decoding jobs
             with a chunked prefill -- but essentially, it trades TTFT for
             TPOT... batching prefill and decoding invariably leads to
             compromises in either TTFT or TPOT." The paper reports
             "computing the prefill of a 512-token sequence makes an A100
             GPU compute-bound." DistServe itself is claimed to serve 7.4x
             more requests, or a 12.6x tighter SLO, than prior systems under
             the same latency constraints.
Locators:    Abstract; Section 1 pages 1-2; Section 2.3 "Problems and
             Opportunities", pages 3-4; Section 3.1 "Analysis for Prefill
             Instance", page 4; Figure 1 (13B on one A100, input length 512,
             output 64) and Figure 2 (prefill-decoding interference).
Quote:       "an advanced variant of continuous batching attempts to balance
             TTFT and TPOT by segmenting long prefill into chunks and
             attaching decoding jobs with a chunked prefill -- but essentially,
             it trades TTFT for TPOT."
```

```text
URL:         https://arxiv.org/abs/2308.16369
Kind:        primary. Agrawal et al., "Sarathi: Efficient LLM Inference by
             Piggybacking Decodes with Chunked Prefills", Microsoft Research
             India. Own measurements on LLaMA-13B on an A6000 and LLaMA-33B
             on an A100.
Establishes: A tight quantitative gap between prefill cost per token and
             decode cost per token; the observation that a single 512-token
             prefill saturates GPU compute at batch=1; and the specific
             mechanism (chunked prefill + decode-maximal batching) that
             changes the balance between TTFT and per-decode-step latency.
Paraphrase:  Section 1 (page 1) writes: "while the prefill phase effectively
             saturates GPU compute at small batch sizes, the decode phase
             results in low compute utilization as it generates one token at
             a time per request." Section 1 and Section 3.1 report that for
             LLaMA-13B on an A6000, "the decode cost per token can be as high
             as ~200 times the prefill cost per token" at batch size 1, 100x
             at batch 2, and 16.7x at batch 18. Figure 3 (page 5) profiles
             the six transformer operations across batch sizes for a fixed
             sequence length of 1024 and shows prefill has "almost constant
             per-token cost across various batch sizes" while decode cost
             per token drops sharply with batch size. Section 3.1 explains
             the difference by arithmetic intensity: prefill operations sit
             above the GPU's roofline; decode operations "drop by more than
             two orders of magnitude" and only become compute-bound at batch
             size 256 or above. Sarathi's chunked prefill splits a long
             prompt into equal-sized chunks and piggybacks decode requests
             onto each chunk, yielding "up to 10x" decode throughput on
             LLaMA-13B/A6000 and 1.33x end-to-end throughput; and 4.25x
             decode throughput / 1.25x end-to-end on LLaMA-33B/A100.
Locators:    Abstract; Section 1, page 1; Section 3.1 "Analyzing Prefill and
             Decode Throughput", pages 4-5; Figures 3 and 4, page 5.
Quote:       "For example, on an A6000 GPU, for the LLaMA-13B model, a
             prefill with a sequence length of 512 tokens saturates GPU
             compute even at a batch size of just one."
```

```text
URL:         https://proceedings.mlr.press/v202/leviathan23a.html
Kind:        primary. Leviathan, Kalman, and Matias (Google Research), "Fast
             Inference from Transformers via Speculative Decoding", ICML 2023.
             Authors' own measurements on T5-XXL.
Establishes: That speculative decoding accelerates the sequential decode loop
             specifically, without changing prefill; a 2x-3x wall-clock speedup
             on T5-XXL is reported; and the "acceptance rate" alpha that
             governs the achievable speedup.
Paraphrase:  Abstract (arXiv version, page 1): "We demonstrate speculative
             decoding on T5-XXL, an existing off-the-shelf implementation
             (Roberts et al., 2022), showing an out-of-the-box latency
             improvement of 2X-3X, without any change to the outputs." The
             mechanism is that a smaller "approximation model" M_q proposes
             several tokens in serial and the larger "target model" M_p then
             evaluates all proposals in one parallel forward pass, and any
             prefix that agrees with the target model's own distribution is
             accepted. The expected wall-time improvement is derived as
             (1 - alpha^(gamma+1)) / ((1 - alpha) * (gamma * c + 1)), where
             alpha is the per-token acceptance rate and c is the cost ratio
             between the small and large models (Theorem 3.8). Because the
             mechanism batches multiple candidate tokens through the target
             model at once, "the target model's weights and KV cache can" be
             loaded once per accepted group; it does not reduce the cost of
             the initial prefill.
Locators:    ICML 2023 PMLR volume 202 pages 19274-19286; arXiv 2211.17192
             Section 1 page 3; Section 3 "Analysis", pages 4-6; Table 3.
Quote:       "showing an out-of-the-box latency improvement of 2X-3X,
             without any change to the outputs."
```

```text
URL:         https://platform.claude.com/docs/en/test-and-evaluate/strengthen-guardrails/reduce-latency
Kind:        primary. Anthropic's own product documentation. Vendor's stated
             definitions and recommendations.
Establishes: A vendor-side definition of "time to first token" as a metric
             distinct from overall latency; the recommendation to stream
             responses so users see something before generation finishes;
             and the model-level factors (model size, prompt length) that
             Anthropic itself cites as affecting TTFT.
Paraphrase:  The "How to measure latency" section defines baseline latency as
             the total time the model takes to process the prompt and produce
             the response, and defines "Time to first token (TTFT)" as "the
             time it takes for the model to generate the first token of the
             response, from when the prompt was sent." The page notes TTFT
             is "particularly relevant when you're using streaming" and
             recommends Claude Haiku 4.5 for latency-sensitive applications.
             The "Optimize prompt and output length" section says: "The
             fewer tokens the model has to process and generate, the faster
             the response will be."
Locators:    Sections "How to measure latency" and "How to reduce latency /
             2. Optimize prompt and output length" and "3. Stream responses".
Quote:       "Time to first token (TTFT): This metric measures the time it
             takes for the model to generate the first token of the response,
             from when the prompt was sent."
```

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/streaming
Kind:        primary. Anthropic's own streaming-API reference (accessed via
             the canonical redirect from docs.anthropic.com/en/api/messages-
             streaming). Establishes the wire format the reader sees when a
             chatbot streams.
Establishes: The exact server-sent-event sequence a Claude client receives
             during a streamed response: message_start, then per-content-
             block content_block_start/content_block_delta*/content_block_
             stop, then message_delta and message_stop, with occasional ping
             events. Grounds the "why do we see tokens appear one at a time"
             half of the felt behavior.
Paraphrase:  "When creating a Message, you can set 'stream': true to
             incrementally stream the response using server-sent events
             (SSE)." Each response consists of: (1) a message_start event
             containing a Message object with empty content and initial usage
             (input tokens and one output token), (2) a series of content
             blocks, each with a content_block_start, one or more
             content_block_delta events (text_delta, input_json_delta, or
             thinking_delta), and a content_block_stop, (3) one or more
             message_delta events with cumulative usage, and (4) a final
             message_stop event. Ping events may be interleaved. The sample
             sequence shows the first text_delta arriving after
             message_start, content_block_start, and (optionally) a ping.
Locators:    Sections "Event types" and "Basic streaming request" (Example
             response near the end of the page).
Quote:       "1. message_start: contains a Message object with empty content.
             2. A series of content blocks, each of which has a
             content_block_start, one or more content_block_delta events,
             and a content_block_stop event... 3. One or more message_delta
             events, indicating top-level changes to the final Message
             object. 4. A final message_stop event."
```

```text
URL:         https://docs.together.ai/learn/ttft-and-tps
Kind:        primary. Together AI's own explanatory documentation for the
             two headline inference metrics on their platform.
Establishes: A second vendor page that names the same two-phase decomposition,
             says in the vendor's own words that prefill is compute-bound and
             decode is memory-bound, and warns that decode speed does not
             scale linearly with parameter count (e.g. a 400B MoE with ~17B
             active parameters decodes at roughly the speed of a 17B dense
             model).
Paraphrase:  The page defines TTFT as "how long you wait between sending your
             request and seeing the first word of the response appear" and
             TPS as "how fast each word appears after that." It writes that
             during prefill "the model processes your entire prompt in one
             pass" and "compute in this phase is parallel across positions",
             so prefill is "compute-bound, meaning the GPU is multiplying
             matrices flat-out, and the limiting factor is how fast it can
             do the math." Decode "generates output tokens one at a time,
             with each token depending on the previous one" and is
             "memory-bound, meaning the GPU spends most of its time reading
             model weights and the cached state from memory rather than
             actually multiplying." Illustrative user-experience contrasts
             include "A 5-second TTFT followed by 100 TPS feels sluggish to
             start and then snappy once it gets going" and "A 200ms TTFT
             followed by 20 TPS feels responsive at first and then laggy."
Locators:    Sections defining the two phases and their bottlenecks.
Quote:       "Prefill is compute-bound, meaning the GPU is multiplying
             matrices flat-out, and the limiting factor is how fast it can
             do the math. Decode is memory-bound, meaning the GPU spends
             most of its time reading model weights and the cached state
             from memory rather than actually multiplying."
```

```text
URL:         https://www.anyscale.com/blog/reproducible-performance-metrics-for-llm-inference
Kind:        primary. Kadous, Huang, Ding, Xie, Narayan, and Xu (Anyscale),
             1 November 2023, "Reproducible Performance Metrics for LLM
             Inference." Companion to Anyscale's open-source LLMPerf
             benchmark. Their own regression numbers on Llama 2 70b served
             through Anyscale Endpoints.
Establishes: A concrete quantitative statement of how weak the "input tokens
             cause the pause" claim is at everyday prompt lengths: "100 input
             tokens have approximately the same impact on latency as a single
             output token." Also gives working definitions of TTFT and ITL
             used throughout the industry.
Paraphrase:  The post defines TTFT as "how long before the LLM returns the
             first token" in streaming and ITL as "the average time between
             consecutive tokens," measured at P50/P90/P95/P99. In their
             regression on Llama 2 70b served on Anyscale Endpoints, "each
             additional input token adds 0.3-0.7 ms to the end-to-end time,
             compared to each output token which adds 30-60 ms." They
             conclude input tokens have "approximately 1% of the impact of
             output tokens on end-to-end latency." A separate scatterplot in
             the same post shows "there does not seem to be any discernible
             relationship between input tokens and TTFT between 250 token
             input and 800 token input" at 5 concurrent requests, because
             the input-length variation is "swamped by other latency
             sources." This directly qualifies the naive "TTFT grows with
             prompt length" picture: at typical short prompts it does not,
             visibly, until you push past a few thousand tokens.
Locators:    "Common metrics" section (TTFT, ITL); "How does prompt length
             affect performance?" section (regression, scatter, and 100:1
             ratio claim).
Quote:       "Each additional input token adds 0.3-0.7 ms to the end-to-end
             time, compared to each output token which adds 30-60 ms... The
             practical implication of this is that reducing input tokens has
             very little effect on latency compared to reducing output tokens."
```

```text
URL:         https://artificialanalysis.ai/methodology/performance-benchmarking
Kind:        primary. Artificial Analysis's own benchmarking methodology
             page. They are the party doing the measurement, so this owns
             the metric definitions and the workload sizes used across the
             leaderboard.
Establishes: The industry-standard operational definitions of TTFT and
             Output Speed, and the specific input-length brackets against
             which frontier chat APIs are tested today (1k, 10k, 100k input
             tokens).
Paraphrase:  Under "Key Definitions": TTFT is "the time in seconds between
             sending a request to the service or system and receiving the
             first token of the response"; Output Speed is "the average
             number of tokens received per second, after the first token is
             received"; End-to-End Response Time is "the total time to
             receive a complete response, including input processing time,
             model reasoning time, and answer generation time." Workloads
             tested include 1k, 10k, and 100k input token prompts; the 10k
             workload is now the default and the deprecated 100-token
             workload is no longer visible. Testing is performed from a VM
             in Google Cloud's us-central1-a zone, and the page warns that
             "TTFT is sensitive to server location" because it includes
             network latency. On input-length dependence: "Longer prompts
             can result in both longer time to first token and slower output
             tokens per second compared to shorter prompts."
Locators:    "Key Definitions", "Workload Types", "Server Location".
Quote:       "Longer prompts can result in both longer time to first token
             and slower output tokens per second compared to shorter prompts."
```

```text
URL:         https://redis.io/blog/prefill-vs-decode/
Kind:        secondary. Redis (Jim Allen Wallace, 2026-04-28) is not the
             party that ran the underlying benchmarks. The post synthesises
             the vLLM, Sarathi, and NVIDIA developer-blog claims for a
             product audience. It carries the argument forward by naming
             concrete numbers from a Llama 3.1 70B benchmark that make the
             super-linear regime visible; those numbers themselves are
             borrowed and the underlying NVIDIA post is the primary owner.
Establishes: A reasonable outside-in framing of the two-phase mechanism, and
             a specific quantitative bridge from "attention is quadratic" to
             a felt TTFT curve at long contexts.
Paraphrase:  Wallace writes: "If your chatbot feels sluggish before the
             first word appears, that's usually a prefill problem. If it
             crawls once tokens start coming, that's decode." He notes:
             "Every token in your prompt has to interact with every other
             token, so the work grows faster than the prompt itself.
             Doubling a long prompt from 16K to 32K tokens roughly
             quadruples the attention work." He cites an NVIDIA Llama 3.1
             70B benchmark: "32,768 input tokens: 472 ms TTFT" and
             "122,880 input tokens: ~2.2 seconds TTFT," and observes that
             "TTFT grew faster than the prompt itself, and that gap widens
             as contexts get longer." Because the numbers are relayed, they
             are treated here as coverage; the underlying benchmark is the
             NVIDIA developer post that Wallace links. He also acknowledges
             the interference story: "Prefill requests can block decode
             streams and cause visible stuttering for users already
             receiving tokens."
Locators:    Sections "What 'prefill vs decode' actually means", "Why longer
             prompts mean longer waits", "Prefill vs decode tradeoffs".
Quote:       "32,768 input tokens: 472 ms TTFT... 122,880 input tokens:
             ~2.2 seconds TTFT... TTFT grew faster than the prompt itself,
             and that gap widens as contexts get longer."
```

## Contradictions

- **Naive "TTFT is quadratic in n" vs. what benchmarks actually show at
  chatbot lengths.** The attention paper (Vaswani 2017 Table 1) gives
  self-attention layer cost O(n^2 * d) and calls self-attention faster than
  recurrent layers only "when the sequence length n is smaller than the
  representation dimensionality d". For today's models d is several thousand,
  so at prompt lengths of a few hundred to a few thousand tokens the
  position-wise feed-forward (O(n * d^2)) and the linear query/key/value
  projections dominate, and prefill grows roughly linearly with n. Anyscale's
  Llama 2 70b regression bears this out: an extra input token adds only
  0.3-0.7 ms, and TTFT shows "no discernible relationship" with prompt length
  between 250 and 800 input tokens. The super-linear regime is real but sits
  at long contexts: the NVIDIA / Llama 3.1 70B numbers cited in the Redis
  post jump from 472 ms at 32K tokens to about 2.2 s at ~123K tokens
  (roughly 3.8x prompt for roughly 4.7x TTFT), and Baseten's Mistral 7B
  benchmark shows TTFT going "from a few hundred milliseconds at a batch
  size of 72 to many seconds with a batch size of 96" for 1000-token inputs
  once the compute slots saturate. A lesson that leads with "attention is
  quadratic" without saying "in n^2 but with a smaller constant than the
  linear FFN term until n is large" will mislead the reader whose everyday
  prompts sit under a few thousand tokens.

- **"Decode is smooth" is a per-request idealisation.** DistServe's Figure 2
  shows that in a colocated system a single new prefill inserted into an
  ongoing batch of decodes significantly extends TPOT for every user in
  that batch, and the slowdown "intensifies with a longer prefill." Sarathi
  observes the mirror image: prefill cost per token dwarfs decode cost per
  token, so bursts of new arrivals starve decode. The smooth streaming the
  reader sees only stays smooth when the system either disaggregates the
  two phases (DistServe) or explicitly chunks prefill so decode always has
  work (Sarathi-Serve). Chunked prefill itself trades TTFT for TPOT (DistServe,
  Section 2.3 verbatim): the individual user waiting for their first token
  gets a slightly longer wait so that ongoing users see less stutter.

- **Speculative decoding does not touch the pause.** Leviathan et al.'s
  method accelerates the decode loop by verifying several draft tokens in
  a single target-model forward pass; it does not accelerate the initial
  prefill. Any TTFT improvement from a serving stack that ships speculative
  decoding therefore has to come from elsewhere (bigger prefill batches,
  chunked prefill, prefix caching), not from the speculative mechanism
  itself. The commission's "smooth streaming feels steady" line already
  holds under speculative decoding, but the specific decoder speed depends
  on the acceptance rate alpha and the small-model cost ratio c
  (Theorem 3.8, Section 3), so the reader who cranks up speculative
  decoding does not automatically get a 3x speedup: the paper's headline
  number is 2x-3x on T5-XXL specifically.

- **Prefix caching and KV cache reuse.** Neither Anthropic's latency page
  nor the vLLM paper measure prompt caching numerically, but PagedAttention
  is the mechanism that makes shared prompt KV blocks possible ("the KV
  cache of the prompt part, which accounts for 12% of the total KV cache
  memory in our experiment, can be shared to minimize memory usage",
  Section 4). For a chatbot with a long, repeated system prompt, this can
  collapse the pause on the second turn to near zero even though the
  attention math on the raw input would still be O(n^2). The pause is not
  purely a function of input length; it depends on how much of the input's
  KV cache the system has already computed.

- **Vendor "TTFT" numbers include the network.** Artificial Analysis warns
  in its methodology page that "TTFT is sensitive to server location"
  because it "includes network latency". Anthropic's own latency page also
  lists "network latency" among the factors. A vendor's stated 200 ms TTFT
  for a small model is not the same quantity as the pure prefill compute
  time an academic paper measures on-GPU. A lesson that quotes TTFT
  numbers has to say what is included.

## Numbers

```text
Figure: Self-attention complexity per layer O(n^2 * d); position-wise
        feed-forward and recurrent O(n * d^2); restricted self-attention
        O(r * n * d).
Owner:  Vaswani et al. 2017, Table 1, page 6.
Scope:  Per layer; n = sequence length; d = representation dimension;
        r = restricted-attention neighborhood.
```

```text
Figure: Prefill of a 512-token sequence saturates an NVIDIA A6000 at batch
        size 1 for LLaMA-13B.
Owner:  Agrawal et al. (Sarathi) 2023, Section 1, page 1.
Scope:  LLaMA-13B model, A6000 GPU, batch size 1.
```

```text
Figure: Decode cost per token is ~200x prefill cost per token at batch 1,
        ~100x at batch 2, ~16.7x at batch 18.
Owner:  Agrawal et al. (Sarathi) 2023, Section 3.1 / Figure 3, page 5.
Scope:  LLaMA-13B, fixed total sequence length 1024, A6000 GPU.
```

```text
Figure: 29 ms per token generation latency (int8 weight quantization);
        76% MFU during large-batch input processing.
Owner:  Pope et al. 2023, Abstract, page 1.
Scope:  PaLM 540B on 64 TPU v4 chips, context length 2048.
```

```text
Figure: vLLM sustains 1.7x-2.7x higher request rates than Orca (Oracle)
        and 2.7x-8x higher than Orca (Max) at the same normalized latency.
Owner:  Kwon et al. 2023 (vLLM), Section 6, Figure 12, pages 9-11.
Scope:  ShareGPT workload, OPT-13B, OPT-66B, OPT-175B.
```

```text
Figure: 2x-3x wall-clock latency improvement for speculative decoding.
Owner:  Leviathan et al. 2023, Section 1 and Table 3.
Scope:  T5-XXL model, T5X implementation, greedy and non-greedy sampling.
```

```text
Figure: DistServe delivers up to 7.4x more requests within TTFT/TPOT SLOs
        than prior systems, or a 12.6x tighter SLO at the same load, on
        13B-parameter workloads at input length 512.
Owner:  Zhong et al. 2024 (DistServe), Abstract; Figure 1 and Section 6.
Scope:  13B LLM, one NVIDIA A100 80GB, synthetic workload with input
        length 512 and output length 64.
```

```text
Figure: Each input token adds ~0.3-0.7 ms end-to-end; each output token
        adds ~30-60 ms end-to-end; input tokens have ~1% of the impact of
        output tokens.
Owner:  Kadous et al. 2023 (Anyscale/LLMPerf), "How does prompt length
        affect performance?" section.
Scope:  Llama 2 70b served on Anyscale Endpoints, regression analysis;
        prompt-length range 250-800 input tokens visible in the scatter.
```

```text
Figure: TTFT of 472 ms at 32,768 input tokens; ~2.2 s at 122,880 input
        tokens (roughly 3.8x prompt for roughly 4.7x TTFT).
Owner:  NVIDIA developer blog (Llama 3.1 70B on Blackwell / GH200), as
        relayed by Wallace (Redis) 2026. The Redis post owns the paraphrase;
        NVIDIA owns the underlying measurement.
Scope:  Llama 3.1 70B, GH200 NVL32 hardware.
```

```text
Figure: TTFT jumps "from a few hundred milliseconds at a batch size of 72
        to many seconds with a batch size of 96" once compute slots for
        prefill saturate; a 1000-token input at batch 96 pushes TTFT past
        10 s.
Owner:  Baseten "Benchmarking fast Mistral 7B inference" blog.
Scope:  Mistral 7B on Baseten's stack, 1000-token input.
```

```text
Figure: Anthropic's streaming SSE sequence: message_start, then per-block
        (content_block_start, content_block_delta*, content_block_stop),
        then message_delta*, then message_stop, with occasional ping
        events. The first text_delta is what the user sees as the "first
        token."
Owner:  Anthropic streaming docs, "Event types" section.
Scope:  Claude Messages API streaming.
```

```text
Figure: Artificial Analysis benchmarks TTFT and Output Speed at 1k, 10k
        (default), and 100k input tokens from a Google Cloud us-central1-a
        VM. TTFT is defined as time from request to first response token
        and includes network latency.
Owner:  Artificial Analysis methodology page.
Scope:  Public frontier and OSS chat models on their leaderboard.
```

## Source assets

```text
Asset: Vaswani et al. 2017, Table 1 ("Maximum path lengths, per-layer
       complexity and minimum number of sequential operations for
       different layer types"), page 6.
Shows: The three cost columns for self-attention, recurrent,
       convolutional, and restricted self-attention side by side. This is
       the single image that lets a reader see, without algebra, why n^2
       is not the only term that matters and why n < d changes which
       column wins.
Crop:  Must keep all four rows and all three columns; omitting the
       recurrent and convolutional rows kills the point of the table.
```

```text
Asset: Kwon et al. 2023 (vLLM), Figure 1 ("Left: Memory layout when
       serving an LLM with 13B parameters on NVIDIA A100..."), page 2.
Shows: The KV cache occupying more than 30% of an A100 40GB while
       parameters take 65%. Makes concrete why decode is memory-bound: the
       state that the model must reread every token is a significant
       fraction of the GPU's memory.
Crop:  Keep the labeled slice for KV cache and the "Others"/"Parameters"
       fractions; the "Existing systems" reservation curve at the right
       is optional.
```

```text
Asset: Agrawal et al. 2023 (Sarathi), Figure 3 ("Per-token prefill and
       decode time with different batch sizes on A6000 GPU"), page 5.
Shows: The prefill line staying nearly flat across batch sizes while the
       decode line drops sharply as batch grows. This is the clearest
       single image of "prefill is compute-bound per token, decode is
       memory-bound per token."
Crop:  Keep both phases and the full batch-size sweep so the crossover
       is visible.
```

```text
Asset: Zhong et al. 2024 (DistServe), Figure 2 (prefill-decoding
       interference: adding one prefill job to a batch of decodes
       increases TPOT sharply with prefill length).
Shows: The counter to "decode feels smooth" -- a new user's arrival
       (their prefill) makes ongoing users' streams stutter.
Crop:  Keep both the "decoding-with-one-prefill" curve and the
       "prefill slowdown" curve.
```

```text
Asset: Leviathan et al. 2023 (Speculative Decoding), Figure 1
       (illustration of green speculative tokens accepted by the target
       model, only 9 serial target-model runs producing 33 tokens).
Shows: The mechanism visually: draft model runs, target model verifies,
       multiple tokens accepted per target step.
Crop:  Keep the coloured token sequence with the accepted/rejected marks.
```

```text
Asset: Anyscale / LLMPerf, "TTFT vs prompt length" scatter (Llama 2 70b
       on Anyscale Endpoints, 250-800 input tokens, 5 concurrent requests).
Shows: No visible upward trend in TTFT against input length in the range
       tested. Grounds the surprising finding that at short prompts
       prefill is not what the user is waiting for.
Crop:  Keep both axes; the shape only reads if the reader sees "TTFT (s)"
       and "input tokens".
```

```text
Asset: Together AI TTFT/TPS page, side-by-side "prefill compute-bound /
       decode memory-bound" diagram.
Shows: A vendor's own two-panel diagram of the mechanism, in the same
       language the article uses.
Crop:  None found in text extraction; check the live page.
```

## Discarded

```text
https://medium.com/@alice_gjw/how-llm-inference-works-prefill-decode-phase-ab39464ecc68 : rehashes the vLLM story without adding measurement; medium.com author has no stake.
https://machinelearningmastery.com/from-prompt-to-prediction-understanding-prefill-decode-and-the-kv-cache-in-llms/ : same, secondary summary of already-cited primaries.
https://pub.towardsai.net/inside-llm-inference-kv-cache-prefill-and-the-decode-bottleneck-1ea12d883123 : summary post without independent measurement.
https://www.cognitivetoday.com/2026/05/llm-inference-secrets/ : content-farm rewrite of the vLLM and Sarathi papers.
https://godofprompt.ai/blog/llm-latency-benchmarks-use-case/ : listicle of TTFT numbers with no methodology and no primary link.
https://aimultiple.com/llm-latency-benchmark : listicle, no reproducible methodology.
https://inworld.ai/resources/fastest-llm-inference-api : marketing page; benchmarks lack methodology detail.
https://infercom.ai/blog/llm-inference-speed-explained/ : summary blog, no primary measurement.
https://dev.to/wheynelau/how-to-benchmark-llm-inference-performance-ttft-itl-and-throughput-metrics-416p : how-to guide, no measurement of its own.
https://tokendyno.com/blog/llm-tokens-per-second/ : summary post, no primary measurement.
https://arxiv.org/abs/2507.09019 : useful survey ("On Evaluating Performance of LLM Inference Serving Systems") but its measurements duplicate DistServe / vLLM without adding a new fact the article needs.
https://arxiv.org/abs/2403.02310 : Sarathi-Serve, largely restates Sarathi's TTFT/TPOT trade-off; the 2023 Sarathi paper is enough.
https://www.linkedin.com/posts/waleedkadous_reproducible-performance-metrics-for-llm-... : the LinkedIn share is the same content as the Anyscale blog itself.
https://vllm.ai/blog/2023-06-20-vllm : vLLM promo blog by the paper authors; the SOSP paper is the primary and carries the numbers.
```
