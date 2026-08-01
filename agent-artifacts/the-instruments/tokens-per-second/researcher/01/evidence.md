# Evidence record — the-instruments/tokens-per-second

This record supports all four pillars the commission names. The prefill/decode
split and the batch-size/latency tradeoff are the best-grounded claims: the
vLLM/PagedAttention paper gives the mechanism, and MLCommons's own raw v5.1
results file gives a same-hardware, same-submitter number that falls ~40%
when the latency constraint tightens — a clean worked example that needs no
embellishment. The tokenizer point is grounded but thinner: it rests on
Artificial Analysis's methodology page rather than a dedicated tokenizer
paper, on the premise that the-mechanics/letter-counting already carries the
BPE mechanics and this piece should only link it. The misuse case is
well-sourced but is not one single named victim with a dollar figure; it is
three convergent, independently documented failures of the bare number —
Groq's own marketing figure versus Anyscale's independent measurement of the
same model, NVIDIA's unverified press figure versus its own audited MLPerf
submission, and the industry's own admission (MLCommons adding an Interactive
scenario, SemiAnalysis building InferenceMAX) that headline throughput
numbers were being read at interactivity levels no real user would accept.
I could not locate a single reported case of one named company incurring a
specific dollar cost from a bad tokens/sec read; I flag that gap explicitly
rather than invent one. Contradictory/fair-to-vendor evidence is present:
Cerebras's claims were independently corroborated by Artificial Analysis, and
Groq's and Anyscale's disagreeing numbers turn out to both be honest once the
measurement window is understood.

## Sources

### 1. MLPerf Inference rules (MLCommons) — scenario definitions and latency constraints
URL: https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc
Primary: MLCommons owns and publishes this document; it is the audited
procedure's own specification, not a description of it.
Establishes firsthand: the three relevant scenarios and what each measures.
- **Single-Stream**: LoadGen sends the next query only after the previous one
  completes, one sample per query, over 600 seconds. Metric: 90th-percentile
  latency. No throughput metric — this scenario measures latency, not tok/s.
- **Server**: queries arrive on a Poisson process over 600 seconds. A
  benchmark-specific latency bound applies. For Llama3.1-8B the rules give two
  bands as an example: "Conversational category: TTFT/TPOT: 2000 ms/100 ms"
  and "Interactive category: TTFT/TPOT: 500 ms/30 ms." Metric: the maximum
  Poisson arrival rate (queries/sec, convertible to tokens/sec) the system
  sustains while meeting the bound.
- **Offline**: all samples are issued as one query at the start; no latency
  bound. Metric: "measured throughput," samples/sec — this is the
  largest, most quotable number, and it assumes the system can batch as much
  as it wants, which live traffic never permits.
- For LLMs specifically, the rules define **TTFT** (latency of the first
  token) and **TPOT** (average interval between all generated tokens) as the
  two latency metrics collected per query.
Locator: scenario definitions and the LLM-specific TTFT/TPOT paragraph, read
via the rendered adoc file (no stable line numbers in the rendered view;
search the document for "Server scenario" and "TTFT").

### 2. MLPerf Inference v5.1 official results — raw results table
URL (browsable): https://github.com/mlcommons/inference_results_v5.1/blob/main/summary_results.json
URL (raw, fetched directly): https://raw.githubusercontent.com/mlcommons/inference_results_v5.1/main/summary_results.json
Primary: this is MLCommons's own published results file for the v5.1
round (the file GitHub's web UI calls too large to render; I downloaded it
directly and parsed it — 1,448 result rows). This is the actual "results
table" the commission asks for, not a summary of it.
Establishes firsthand: exact audited tokens/sec figures per submitter,
platform, model, and scenario. Full extraction method and figures are under
Numbers below. Each row carries fields including `Submitter`, `Platform`,
`Model`, `Scenario`, `Performance_Result`, `Performance_Units` ("Tokens/s"),
`Availability`, `Category` (closed/open), and `weight_data_types`
(precision/quantization used).
Locator: JSON array, field names as above; filtered on `Model in
{"llama2-70b-99","llama3.1-405b"}`, `Category=="closed"`,
`Availability=="available"`.

### 3. MLCommons, "Llama 2 70B: An MLPerf Inference Benchmark for Large Language Models" (2024-03)
URL: https://mlcommons.org/2024/03/mlperf-llama2-70b/
Primary: MLCommons's own account of how its task force designed this
benchmark — the owning body explaining its own procedure.
Establishes firsthand: dataset choice (a curated 24,576-sample subset of
Open Orca, capped at 1,024 input and 1,024 output tokens), why Q&A was chosen
over multi-turn dialogue ("one of the most common ways that LLMs are being
used in serving applications today"), why tokens/sec was chosen over
queries/sec ("queries can have different input and output token lengths"),
and the original Server-scenario latency bound: TTFT ≤ 2 s, TPOT ≤ 200 ms,
anchored explicitly to "approximately 240 words per minute," an average adult
reading speed.
Locator: sections on dataset selection, scenario definition, and latency
constraints (page has no numbered sections; content organized under those
headers).

### 4. MLCommons, "MLPerf Inference v5.0 Advances Language Model Capabilities for GenAI" (2025-04)
URL: https://mlcommons.org/2025/04/llm-inference-v5/
Primary: MLCommons's own announcement of the new benchmarks in the v5.0
round, including the rationale for a new scenario.
Establishes firsthand: the Llama2-70B-Interactive scenario's latency bound —
99th-percentile TTFT ≤ 450 ms, 99th-percentile TPOT ≤ 40 ms (i.e., a floor of
25 tokens/sec/user) — added because "state-of-the-art model serving has
advanced" and MLCommons surveyed "industry research, user surveys, and
performance data from leading platforms like ChatGPT and Perplexity AI" to
conclude the original 200 ms TPOT bound (5 tokens/sec/user) no longer
represented real interactive use. Also gives Llama3.1-405B's bound: 99th-pct
TTFT ≤ 6 s, TPOT ≤ 175 ms, on a dataset averaging ~9,400 input / ~680 output
tokens, with a 128K context window.
Locator: paragraphs describing the Llama2-70B-Interactive and Llama3.1-405B
benchmarks.

### 5. MLCommons, "MLCommons Releases New MLPerf Inference v5.0 Benchmark Results" (2025-04-02)
URL: https://mlcommons.org/2025/04/mlperf-inference-v5-0-results/
Primary: MLCommons's own release announcement for the round.
Establishes firsthand: round context — 17,457 performance results from 23
submitting organizations; Llama2-70B was the most-submitted benchmark (17
organizations); "the median submitted score has doubled" year over year and
"the best score is 3.3 times faster" than v4.0; five first-time submitters
including CoreWeave and MangoBoost; new hardware included NVIDIA B200 and
Google TPU Trillium.
Locator: summary paragraphs near the top of the post.

### 6. NVIDIA Technical Blog, "NVIDIA Blackwell Delivers Massive Performance Leaps in MLPerf Inference v5.0" (2025)
URL: https://developer.nvidia.com/blog/nvidia-blackwell-delivers-massive-performance-leaps-in-mlperf-inference-v5-0/
Primary for NVIDIA's own claims about its own audited submission (NVIDIA is
the submitter reporting its own MLPerf v5.0 numbers); secondary in the sense
that it restates MLPerf's own published constraints rather than owning them.
Establishes firsthand: NVIDIA's audited B200 NVL8 (8-GPU) results for
Llama2-70B — 98,443 tokens/sec (Server), 98,858 tokens/sec (Offline) — versus
H200 NVL8 at 33,072 / 34,988 tokens/sec, a 3x/2.8x gain. States the
Llama2-70B-Interactive bound as "450 ms TTFT and 40 ms TPOT (25 tokens per
second per user)" and the Llama3.1-405B bound as "6 seconds for TTFT and 175
ms for TPOT." Cross-checked below against the raw v5.1 results file (source
2), which shows the same order of magnitude one round later.
Locator: results tables and callouts under the Llama2-70B and Llama2-70B-
Interactive headings.

### 7. Groq, "Groq LPU™ Inference Engine Crushes First Public LLM Benchmark" (2024)
URL: https://groq.com/blog/groq-lpu-inference-engine-crushes-first-public-llm-benchmark
Primary: Groq is the vendor; this is its own account of its own throughput
claim and, notably, its own explanation for why an independent benchmark
reported a different number for the same model.
Establishes firsthand: Groq's headline claim of 270+ tokens/sec/user for
Llama 2 70B on its own dashboard, versus a 185 tokens/sec median reported by
Anyscale's independent LLMPerf leaderboard for the same model on Groq's
service (Anyscale figure independently confirmed via source 15 below). Groq's
own explanation: the LLMPerf test used a 150-output-token completion and
folded prompt-processing time into the per-token average, while Groq's own
270+ figure is computed after the first token, over a longer (~1,000-token)
completion — "if you were to test with 1000 output tokens, the result would
be closer to the 270+ tokens/s per user you see on groq.com." Also discloses
precision: "All Llama 2 calculations on the LPU are done in FP16, but we
store some of the weights in FP8," and "we have no sparsity."
Locator: body paragraphs comparing the Anyscale number to groq.com's own
figure; technical-specs paragraph near the end.

### 8. Cerebras, "Introducing Cerebras Inference: AI at Instant Speed" (2024-08)
URL: https://www.cerebras.ai/blog/introducing-cerebras-inference-ai-at-instant-speed
Primary: Cerebras's own launch claim for its own hardware.
Establishes firsthand: launch-day claims of 1,800 tokens/sec for Llama3.1-8B
and 450 tokens/sec for Llama3.1-70B, both described as "output speed per
user" (i.e., a single-stream/low-concurrency figure, not aggregate fleet
throughput), run at "native 16-bit weights." Footer disclaimer: "Performance
comparisons are based on third-party benchmarking or internal testing.
Observed inference speed improvements versus GPU-based systems may vary
depending on workload, configuration, date and models being tested."
Locator: headline figures and footer disclaimer.

### 9. Cerebras, "Cerebras Inference now 3x faster: Llama3.1-70B breaks 2,100 tokens/s" (2024-11)
URL: https://www.cerebras.ai/blog/cerebras-inference-3x-faster
Primary: Cerebras's own updated claim.
Establishes firsthand: the 450 tokens/sec figure above rose to 2,100
tokens/sec for the same model (Llama3.1-70B) three months later, attributed
to speculative decoding, with an explicit variance caveat: "20% higher or
lower than the 2,100 tokens/sec average is normal." States the number was
"rigorously tested by Artificial Analysis, a third-party benchmarking
organization" — i.e., Cerebras points to an independent measurer rather than
asking readers to take the number on faith. Independent corroboration: a
2024-08 measurement by Artificial Analysis (reported via secondary coverage,
not independently re-verified by me on AA's own site — see Numbers) put
Cerebras above 446 tokens/sec around the time of the first claim, consistent
in direction with Cerebras's own reported trajectory.
Locator: opening paragraphs and footer disclaimer (same disclaimer text as
source 8).

### 10. NVIDIA NIM documentation, "Optimization" (large-language-models, v1.0.0)
URL: https://docs.nvidia.com/nim/large-language-models/1.0.0/optimization.html
Primary: NVIDIA's own documentation for its own inference server product;
this is an engineering source defining terms for its own system, not a
report about someone else's.
Establishes firsthand: exact definitions — "Time to First Token (TTFT): The
latency between the initial inference request to the model and the return of
the first token." "Inter-Token Latency (ITL): The latency between each token
after the first." "Total Throughput: The total number of tokens generated
per second by the NIM." Does not itself discuss batch-size or prefill/decode
interaction (see source 11 and 12 for that).
Locator: metrics-definition section of the page.

### 11. Kwon et al., "Efficient Memory Management for Large Language Model Serving with PagedAttention" (vLLM paper, SOSP '23 / arXiv:2309.06180)
URL: https://arxiv.org/abs/2309.06180 (full text read via https://arxiv.org/pdf/2309.06180)
Primary: this is the engineering paper that introduces vLLM and
PagedAttention; it owns the claims about its own system's throughput and is
the standard citation for continuous-batching-era serving mechanics.
Establishes firsthand, with exact language: Section 2.2 defines the two
phases directly. "The prompt phase takes the whole user prompt … as input …
Since prompt tokens are all known, the computation of the prompt phase can be
parallelized using matrix-matrix multiplication operations. Therefore, this
phase can efficiently use the parallelism inherent in GPUs." Contrast: "The
autoregressive generation phase generates the remaining new tokens
sequentially… The computation at different iterations cannot be parallelized
due to the data dependency and often uses matrix-vector multiplication, which
is less efficient. As a result, this phase severely underutilizes GPU
computation and becomes memory-bound, being responsible for most portion of
the latency of a single request." Section 2.3 (batching): "the compute
utilization in serving LLMs can be improved by batching multiple requests,"
but naive batching is inefficient because requests "arrive at different
times" and "have vastly different input and output lengths." Abstract:
"vLLM improves the throughput of popular LLMs by 2-4× with the same level of
latency compared to state-of-the-art systems such as FasterTransformer and
Orca. The improvement is more pronounced with longer sequences, larger
models, and more complex decoding algorithms." Figure 1 (right panel) plots
measured throughput (tokens/sec) against batch size (# requests) for a
13B-parameter model on an NVIDIA A100 40GB, showing existing systems'
throughput plateauing early while vLLM's continues climbing — a direct visual
of the batch-size lever on tokens/sec (see Source assets).
Locator: Section 2.2 "LLM Service & Autoregressive Generation" (page 3);
Section 2.3 "Batching Techniques for LLMs" (page 3); Abstract (page 1);
Figure 1 (page 1).

### 12. NVIDIA/TensorRT-LLM, H200 launch blog post (docs/source/blogs/H200launch.md)
URL: https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/H200launch.md
Primary: NVIDIA's own TensorRT-LLM repository documenting its own
benchmark numbers for its own inference engine.
Establishes firsthand: a concrete, same-model illustration of the batch-size
lever. For Llama-13B at 128 input/128 output tokens, tensor-parallel 1, on
H200: batch 64 → 1,349 tok/s; batch 128 → 4,750 tok/s; batch 1,024 → 11,819
tok/s — roughly an 8.8x range on the same model and hardware, driven only by
batch size. Also contrasts an offline/summarization workload (Llama-70B,
2,048 input / 128 output — H200 1.9x over H100) against an online-chat
workload (GPT-3 175B, 80 input / 200 output — H200 1.6x over H100), showing
context length and workload shape change the reported speedup even for the
same hardware generation.
Locator: performance tables in the body of the markdown file.

### 13. Artificial Analysis, "Language Model API Performance Benchmarking" (methodology)
URL: https://artificialanalysis.ai/methodology/performance-benchmarking
Primary/independent for Artificial Analysis's own measurement methodology
and its own measured numbers; secondary when it is merely repeating a
vendor's claim.
Establishes firsthand, with exact language: "Output Speed (output tokens per
second) is defined as the average number of tokens received per second,
after the first token is received." "Time to First Token is the time in
seconds between sending a request to the service or system and receiving the
first token of the response." Test conditions: three prompt-length workloads
(1K, 10K default, 100K input tokens), tested both single-stream and with "10
prompts sent to the model's API simultaneously"; results reported as median
(P50) over the trailing 72 hours (14 days for the 100K workload). All
providers tested with temperature 0 (0.6 for reasoning models), top_p 1, and
—critically for the tokenizer point—"OpenAI's tiktoken library for
standardized token counting across different models," because "different
tokenizers create pricing [and count] incomparability across models."
Discloses testing runs from Google Cloud's us-central1-a zone and that some
providers use undisclosed quantization affecting speed and quality.
Locator: "Output Speed" and "Time to First Token" definitions; "Test
Conditions" section; "Key Caveats" discussion of tokenizer normalization.

### 14. Artificial Analysis, Llama 3.1 70B provider comparison page
URL: https://artificialanalysis.ai/models/llama-3-1-instruct-70b/providers
Primary/independent for AA's own live measured numbers on this page.
Establishes firsthand: for the identical model (Llama 3.1 70B, 128K context),
measured output speed varies roughly 3x across providers under AA's
standardized 10K-input-token test — Amazon Bedrock (latency-optimized) 119.6
tok/s / 1.26 s TTFT; Amazon Bedrock (standard) 93.9 tok/s / 1.38 s TTFT;
DeepInfra (Turbo, FP8) 38.2 tok/s / 1.66 s TTFT; DeepInfra (standard) 37.9
tok/s / 1.79 s TTFT. Page notes the model is now deprecated by some
providers, so this is a snapshot, not a live figure at publication time — use
directionally (same model, different serving stack and quantization, large
spread), not as a current-as-of-today number.
Locator: provider comparison table.

### 15. Anyscale, "Reproducible Performance Metrics for LLM Inference" + ray-project/llmperf-leaderboard
URL: https://www.anyscale.com/blog/reproducible-performance-metrics-for-llm-inference
URL: https://github.com/ray-project/llmperf-leaderboard
Primary/independent: Anyscale built and owns the LLMPerf tool and ran these
specific measurements; this is the firsthand source for the 185 tokens/sec
Groq figure cited (secondhand, via Groq) in source 7.
Establishes firsthand: LLMPerf's test parameters — mean input 550 tokens
(σ=150), mean output 150 tokens (σ=20), 5 concurrent requests, 150 completed
requests — chosen to reflect real Anyscale Endpoints traffic rather than
synthetic sequences. Defines output-token throughput as tokens returned per
second across the full request including time-to-first-token, which is the
specific methodological difference from Groq's own "after first token" AA-
style definition (source 7's explanation matches this). Reports Groq's Llama
2 70B: median 185 tok/s, mean 184 tok/s, min 148, max 208, median TTFT 0.22 s.
Locator: methodology section of the Anyscale post; leaderboard table and
`token_benchmark_ray.py` invocation shown in the GitHub README.

### 16. IEEE Spectrum, "Nvidia Blackwell Ahead in AI Inference, AMD Second" (2025-04-02)
URL: https://spectrum.ieee.org/ai-inference
Secondary: independent engineering journalism reporting on the MLPerf v5.0
round; IEEE Spectrum has no stake in NVIDIA's or MLCommons's numbers.
Establishes: press framing of the round, and explicitly separates NVIDIA's
audited submission from a marketing figure — "In an unverified result the
company shared with reporters, a full rack of GB200-based computers delivers
869,200 tokens per second on Llama2 70B" — flagging it as distinct from "the
officially reported MLPerf benchmarks." Also states the Llama2-70B-Interactive
scenario requires systems to "produce at least 25 tokens per second" and
"cannot take more than 450 milliseconds to begin an answer," in plain
language consistent with sources 4 and 6.
Locator: paragraphs comparing Blackwell/Hopper results and discussing the
unverified full-rack figure.

### 17. SemiAnalysis, "InferenceMAX™: Open Source Inference Benchmarking" (2025-10)
URL: https://newsletter.semianalysis.com/p/inferencemax-open-source-inference
URL: https://inferencex.semianalysis.com/blog/inferencemax-open-source-inference-benchmarking
Primary/independent for SemiAnalysis's own benchmark design and its own
measured comparisons; the piece is built with participation from NVIDIA, AMD,
OpenAI, Microsoft and others, so treat any vendor-attributed number inside it
as secondary unless it is SemiAnalysis's own measurement.
Establishes firsthand: an explicit statement of the batch/concurrency
tradeoff mechanism in plain terms — "you can serve individual users fast and
efficiently, usually by serving fewer users at a time, but doing so will come
with the cost of lower overall GPU throughput" — and a direct warning about
headline-number abuse: "if GPU A delivers 4x the throughput of GPU B at a
given interactivity level -- take 5 tokens/s/user as an example for a
human-facing AI chatbot application, the fact that this interactivity level
is far too slow to be practical means that this performance difference has
little real-world significance." States practical operating ranges for real
deployments, e.g., roughly 150-200 tok/s/user for GPT-OSS-120B and around 90
tok/s/user for other tested workloads — i.e., the benchmark was built because
vendors were (and are) citing throughput at interactivity levels ("5
tokens/s/user") that no chat product would ship. Test workloads: Chat (1,024
in / 1,024 out), Reasoning (1,024 in / 8,192 out), Summarization (8,192 in /
1,024 out).
Locator: sections explaining the throughput/interactivity tradeoff and the
practical operating-range discussion.

## Contradictions

- **Groq vs. Anyscale, same model, same vendor's service, different honest
  numbers.** Groq's own dashboard reports 270+ tokens/sec/user for Llama 2
  70B; Anyscale's independent LLMPerf leaderboard measured a 185 tokens/sec
  median on the same Groq service (source 15, corroborating source 7's own
  account). Both are real measurements of the same system. The disagreement
  is fully explained by methodology, not deception: LLMPerf's 150-token
  completions fold prompt-processing time into the per-token average and
  divide over a short output; Groq's figure is computed strictly after the
  first token, over a longer completion. This is the clean "two honest
  measurements disagree" case the commission asks the article to explain.

- **NVIDIA's unverified press figure vs. its own audited MLPerf submission.**
  NVIDIA told reporters a "full rack" of GB200 systems reached 869,200
  tokens/sec on Llama2-70B (source 16), explicitly labeled unverified — not
  reviewed under MLPerf's audit process. Its own audited v5.0 submission for
  an 8-GPU B200 system (source 6) was 98,443-98,858 tokens/sec. These are not
  actually inconsistent once GPU count is normalized: 98,858/8 ≈ 12,357
  tokens/sec/GPU versus 869,200 tokens/sec across a 72-GPU NVL72 rack ≈ 12,072
  tokens/sec/GPU — nearly identical per-GPU rates. The real gap is
  procedural, not numerical: one number went through MLCommons's audit and
  one did not, and press coverage did not always preserve that distinction
  (source 16 is the one outlet in this record that did). This is a fair
  vendor case: the unverified number appears defensible on a per-GPU basis,
  even though "unverified" is a real and material caveat MLPerf itself
  requires reporters to carry.

- **Same hardware, same submitter, two audited MLPerf numbers 40% apart.**
  Within the single v5.1 results file (source 2), identical 8x B200 systems
  from the same submitters report both scenarios. Example (Nebius,
  B200-SXM-180GBx8): Server 101,611 tokens/sec vs. Interactive 59,622.7
  tokens/sec — a 41% drop on the same silicon. The only variable is the
  latency bound: Server allows 200 ms/token (5 tok/s/user), Interactive
  requires 40 ms/token (25 tok/s/user, source 4/6). This is not sources
  disagreeing; it is the same audited procedure proving the commission's
  batch-size/latency point on a single set of machines. See Numbers for the
  full comparison table.

- **Cerebras is the case that survives scrutiny.** Unlike the Groq/Anyscale
  gap, Cerebras's headline numbers (450 → 2,100 tok/s for Llama3.1-70B,
  sources 8-9) are reported as independently tested by Artificial Analysis,
  and secondary coverage of AA's own measurements around the same period
  (~446 tok/s in August 2024) points the same direction. I did not
  independently re-pull AA's historical Cerebras-specific data page (AA's
  provider pages for this model no longer list Cerebras as an active
  provider at time of writing — see source 14, where Cerebras does not
  appear), so I cannot certify the exact 2,100 figure against a live AA
  measurement today; I can only report that Cerebras cites a named
  independent verifier and that no source in this record contradicts the
  claim. Use this as the "vendor number defensible under stated conditions"
  example, with that limitation stated plainly.

## Numbers

| Figure | Value | Source | Conditions/denominator |
|---|---|---|---|
| Server-scenario latency bound, Llama2-70B (original) | TTFT ≤ 2,000 ms, TPOT ≤ 200 ms | Sources 3, 6 | Implies a floor of 1000/200 = 5 tokens/sec per user |
| Server-scenario latency bound, Llama2-70B-Interactive | TTFT ≤ 450 ms, TPOT ≤ 40 ms | Sources 4, 6, 16 | Implies a floor of 1000/40 = 25 tokens/sec per user |
| Server-scenario latency bound, Llama3.1-8B (rules example) | Conversational 2,000/100 ms; Interactive 500/30 ms | Source 1 | Implies 10 and 33.3 tok/s/user respectively |
| Server-scenario latency bound, Llama3.1-405B | TTFT ≤ 6,000 ms, TPOT ≤ 175 ms | Source 4, 6 | ~9,400 input / ~680 output tokens average, 128K context |
| Llama2-70B, B200 NVL8, Server (audited, v5.0) | 98,443 tokens/sec | Source 6 (NVIDIA's own audited MLPerf v5.0 submission) | 8x B200 GPUs |
| Llama2-70B, B200 NVL8, Offline (audited, v5.0) | 98,858 tokens/sec | Source 6 | 8x B200 GPUs |
| Llama2-70B, H200 NVL8, Server (audited, v5.0) | 33,072 tokens/sec | Source 6 | 8x H200 GPUs |
| Llama2-70B, "full rack" GB200, unverified | 869,200 tokens/sec | Source 16 (press briefing, not MLCommons-audited) | Not through MLPerf review; ~72 GPUs |
| Llama2-70B, Nebius B200x8, Server (audited, v5.1) | 101,611 tokens/sec | Source 2 (raw results file) | Same hardware as row below |
| Llama2-70B, Nebius B200x8, Interactive (audited, v5.1) | 59,622.7 tokens/sec | Source 2 | Same hardware as row above; 41% lower, driven only by the tighter latency bound |
| Llama2-70B, Nebius B200x8, Offline (audited, v5.1) | 101,246 tokens/sec | Source 2 | Same hardware |
| Llama2-70B, MangoBoost multi-node, Server (audited, v5.1, highest in file) | 153,076 tokens/sec | Source 2 | 32xMI300X + 16xMI325X multi-node system |
| Llama3.1-405B, NVIDIA GB200-NVL72, Server (audited, v5.1) | 11,614.3 tokens/sec | Source 2 | 4 accelerators/node x 18 nodes = 72 GPUs |
| Llama3.1-405B, single 8x B200 node, Server (audited, v5.1) | 1,279.53 tokens/sec | Source 2 | Nebius, 8x B200 GPUs, single node |
| MLPerf v5.0 round participation | 17,457 performance results, 23 submitting orgs | Source 5 | v5.0 round, April 2025 |
| Median Llama2-70B score, v5.0 vs. v4.0 | Doubled; best score 3.3x faster | Source 5 | Year-over-year, same benchmark |
| Groq Llama2-70B, Groq's own figure | 270+ tokens/sec/user | Source 7 | After first token, ~1,000-token completion, FP16 compute/FP8-stored weights, no sparsity |
| Groq Llama2-70B, Anyscale LLMPerf independent measurement | 185 tok/s median (184 mean, 148-208 range); TTFT 0.22 s median | Sources 7, 15 | 550 input / 150 output tokens, 5 concurrent requests, includes TTFT in per-token average |
| Cerebras Llama3.1-8B launch claim | 1,800 tokens/sec | Source 8 | "Output speed per user," 16-bit weights, Aug 2024 |
| Cerebras Llama3.1-70B launch claim | 450 tokens/sec | Source 8 | "Output speed per user," 16-bit weights, Aug 2024 |
| Cerebras Llama3.1-70B updated claim | 2,100 tokens/sec (±20% normal variance) | Source 9 | Speculative decoding added, Nov 2024, "rigorously tested by Artificial Analysis" per Cerebras |
| Llama 3.1 70B, live AA-measured spread across providers | 37.9 to 119.6 tokens/sec (~3x) | Source 14 | Identical model, 10K-input-token AA standard workload, snapshot at time of research |
| TensorRT-LLM, Llama-13B, H200, batch-size sweep (same model/HW/context) | 1,349 (batch 64) -> 4,750 (batch 128) -> 11,819 (batch 1,024) tokens/sec | Source 12 | 128 input / 128 output tokens, TP=1 |
| vLLM vs. prior systems (FasterTransformer, Orca) | 2-4x higher throughput at same latency | Source 11 | "More pronounced with longer sequences, larger models, more complex decoding" |

## Source assets

- **vLLM paper, Figure 1 (right panel).** Location: page 1 of source 11 (PDF
  page 1, right column figure). Shows measured throughput (tokens/sec) versus
  batch size (# requests) for a 13B model on an NVIDIA A100 40GB, plotting
  "Existing systems" against "vLLM," with the existing-systems line
  flattening early while vLLM's keeps climbing. Reader value: a direct visual
  of the exact mechanism the commission's pillar 2 describes — throughput
  rising with batch size, with a ceiling that depends on the serving system.
  I could not read precise axis values reliably from the fetched image (the
  y-axis gridline labels were not legible at the resolution retrieved); a
  crop must keep both axis labels, the legend, and the full curve for both
  systems, and must not use the numeric gridline values without re-verifying
  them from the primary PDF at higher resolution. Do not crop out the axis
  titles ("Throughput (tok/s)", "Batch size (# requests)").

- **MLCommons v5.1 raw results file — same-hardware Server-vs-Interactive
  comparison.** Location: source 2, filtered as shown in the Numbers table.
  This is a table, not an image, but it is chart-ready: for each submitter
  running an identical 8x B200 platform, plotting Server-scenario tokens/sec
  against Interactive-scenario tokens/sec (bars or a slope chart) would carry
  the "same hardware, different latency bound, ~40% throughput gap" argument
  better than prose. I pulled 6 matched platform pairs (Nebius, Supermicro,
  Google, Dell, NVIDIA, GigaComputing, all 8x B200) plus 3 matched H200 pairs
  (Nebius, Dell, HPE) with Server/Offline/Interactive figures for each; full
  set available on request from the raw JSON if the writer wants more rows.

- **NVIDIA TensorRT-LLM H200 launch post — batch-size table.** Location:
  source 12, performance-table section. The raw numbers (1,349 / 4,750 /
  11,819 tokens/sec at batch 64/128/1,024, same model/hardware/context) are
  themselves chart-ready as a simple line or bar chart illustrating pillar 2
  without needing MLPerf's more complex scenario framing.

- No source asset found for the tokenizer pillar (pillar 3) beyond prose
  methodology text; None found beyond what is already in Numbers/Sources.

## Discarded

- https://mlcommons.org/benchmarks/inference-datacenter/ — describes the
  results-table interface but the actual data is rendered client-side by an
  interactive dashboard; no usable figures retrievable via fetch. Superseded
  by the raw results JSON (source 2), which is the actual authoritative data.
- https://www.coreweave.com/lp/mlperf-benchmark-results — CoreWeave's own
  MLPerf landing page; contains only v6.0-era marketing language and no
  disclosed v5.0 figures. Superseded by source 6 (NVIDIA's own reporting of
  the same round) and source 2 (raw data).
- https://wavect.io/blog/taalas-hc1-llm-asic-review/ ("17,000 Tokens/s Is
  Real. The Buying Decision Is Harder.") — a third-party consulting blog
  reviewing a little-known ASIC startup (Taalas); the underlying vendor claim
  is not independently corroborated anywhere else in this research, and the
  publisher's own authority/stake is unclear. Not needed: sources 8, 9, and
  17 already carry the "headline number omits the real buying question"
  point with better-established primaries.
- Several SEO/content-farm results returned by search (neuraplus-ai.github.io,
  kickllm.com, aistoollab.com, tokenmix.ai, aisotools.com, presenc.ai,
  lyceum.technology) — appeared in search result lists only; not fetched or
  cited, no evident authorship or verification standard, and every factual
  claim they carried was available from a stronger primary source already in
  this record.
- Anecdotal user complaints about Groq API slowness in third-party forum/blog
  posts (surfaced during search) — not verifiable, not tied to a specific
  measurement methodology, and plausibly explained by unrelated causes
  (network/agent overhead) rather than the tokens/sec definitional issue this
  article teaches. Not used.
- OpenAI tiktoken documentation and cookbook pages — read only at search-
  snippet depth, not fully fetched; the specific point they would support
  (same text, different token counts under different tokenizers) is already
  established via source 13 and is explicitly the-mechanics/letter-counting's
  territory per the commission, which this piece should link rather than
  re-source.
- General web search for a single named company/buyer harmed by a
  misleading tokens/sec claim, with a specific reported cost — searched
  repeatedly; found none I could verify firsthand. The misuse case in this
  record rests instead on three convergent, well-sourced mechanisms (Groq/
  Anyscale gap, NVIDIA unverified-vs-audited gap, and the industry's own
  corrective actions in sources 4 and 17). Flagging this so the writer does
  not overstate a single-victim narrative the sourcing does not support.
