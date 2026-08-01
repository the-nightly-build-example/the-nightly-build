# Evidence record — the-instruments/tokens-per-second (invocation 02, correction round)

This is a complete replacement for `researcher/01/evidence.md`, not a diff. It
preserves everything from 01 that still stands and fixes one defect the
editor found: 01's Numbers row for a "Llama-13B batch-size sweep" (1,349 /
4,750 / 11,819 tok/s at batch 64/128/1,024) claimed "128 input / 128 output
tokens" was held fixed across all three rows, citing the NVIDIA/TensorRT-LLM
H200 launch table. It was not. I re-opened the primary and transcribed it in
full below (Sources, item 12): the table is a **max-throughput-across-configs
sweep**, not a batch-only sweep — each row reports the best throughput NVIDIA
found for a *different* input/output length pair, at whatever batch size
happened to be largest-by-power-of-two for that config. Batch size, input
length, and output length all move together across the three llama_13b rows.
That table cannot support a "batch size alone drives throughput" worked
example, and I should not have presented it as one.

I checked whether the same source contains a genuine apples-to-apples pair
(same model, hardware, input length, output length — only batch size
different). It does, but only barely: two llama_70b rows share identical
conditions (TP=1, 2048 input / 128 output tokens) and differ only in batch
size (64 vs. 32), giving a real but thin two-point comparison (341 vs. 303
tok/s/GPU). That is too weak to carry a worked example or a chart on its own.

I went looking for a stronger clean series in three other primaries the brief
named. The vLLM paper's own batch/throughput data turned out to be latency-
vs-request-rate curves across different serving systems, not a single-system
tokens/sec-vs-batch-size table with readable numbers (see Sources, item 11,
updated). What did work, and works well, is MLPerf's own raw results file
(already in this record as source 2): for 20 separate hardware platforms,
identical silicon reports Offline, Server, and Interactive throughput for the
same model (Llama2-70B) side by side. Offline has no latency bound (the
system batches as much as it can); Server and Interactive impose
progressively tighter per-token latency bounds, which mechanically caps how
much concurrent work the system can batch. Holding hardware and model fixed
and varying only the latency policy produces a clean, audited, 20-row series
showing a 32-66% throughput drop from Server to Interactive on the same
machines. This is now the primary evidence for pillar 2 and the candidate for
chart-1, replacing the flawed TensorRT-LLM table in that role. The rest of
01's evidence (prefill/decode mechanics, tokenizer normalization, MLPerf
scenario/latency definitions, the misuse-case sourcing) is unaffected by this
defect and is carried forward unchanged below, with the two updated entries
marked.

## Sources

### 1. MLPerf Inference rules (MLCommons) — scenario definitions and latency constraints
*(Unchanged from 01; re-verified URL resolves.)*
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
*(Unchanged source from 01; extraction expanded below — see Numbers.)*
URL (browsable): https://github.com/mlcommons/inference_results_v5.1/blob/main/summary_results.json
URL (raw, fetched directly): https://raw.githubusercontent.com/mlcommons/inference_results_v5.1/main/summary_results.json
Primary: this is MLCommons's own published results file for the v5.1
round (the file GitHub's web UI calls too large to render; I downloaded it
directly and parsed it — 1,448 result rows). This is the actual "results
table" the commission asks for, not a summary of it.
Establishes firsthand: exact audited tokens/sec figures per submitter,
platform, model, and scenario. **New in this round of research:** filtering
to `Model=="llama2-70b-99"`, `Category=="closed"`, `Availability=="available"`
and grouping by (Submitter, Platform), 20 distinct hardware platforms report
results for all three scenarios — Offline, Server, and Interactive — on
identical hardware. This is the clean, audited, same-model/same-hardware
series that replaces the flawed TensorRT-LLM batch table as the pillar-2
worked example. Full series in Numbers below.
Locator: JSON array, field names include `Submitter`, `Platform`, `Model`,
`Scenario`, `Performance_Result`, `Performance_Units` ("Tokens/s"),
`Availability`, `Category` (closed/open), `weight_data_types`. Filtered as
above; grouped by (Submitter, Platform) keeping only groups with all three
of {Offline, Server, Interactive} present.

### 3. MLCommons, "Llama 2 70B: An MLPerf Inference Benchmark for Large Language Models" (2024-03)
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Updated: re-checked for a batch-only throughput table; none found with
readable numbers. Definitional content from 01 stands; batching-evidence
claim narrowed.)*
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
Orca."
**Re-examined for this round:** Section 6 ("Evaluation") does NOT contain a
single-system tokens/sec-vs-batch-size table with readable axis values. Its
quantitative batching evidence is a set of normalized-latency-vs-request-rate
curves (Figure 12, Figure 14) comparing vLLM against FasterTransformer and
three Orca variants across several models/datasets/parallelism settings — a
cross-system comparison at varying load, not a controlled batch-size sweep
on one system. The one directly-quotable batching number from prose: "vLLM
can sustain 1.7×-2.7× higher request rates compared to Orca (Oracle) ... and
2.7×-8× compared to Orca (Max), while maintaining similar latencies" (§6.1,
ShareGPT results), and Figure 13 reports concrete average-batch-size counts
at a fixed request rate for OPT-13B: at 2 req/s on ShareGPT, mean batched
requests were Orca (Max) 7.00, Orca (Pow2) 9.81, Orca (Oracle) 13.62, vLLM
30.42; at 30 req/s on Alpaca: 7.00 / 43.24 / 72.75 / 132.44 respectively. This
is a real, quotable number (different systems achieve different amounts of
batching at the same offered load, and more batching room is exactly the
"batch size" lever) but it compares serving systems, not batch size within
one fixed system, so it is not a substitute for a controlled sweep. Figure 1
(right panel, page 1) does show measured throughput vs. batch size for
existing-systems vs. vLLM on a single 13B/A100 setup, but the axis gridline
values were not legible at the resolution fetched (unchanged limitation from
01 — see Source assets).
Locator: Section 2.2 "LLM Service & Autoregressive Generation" (page 3);
Section 2.3 "Batching Techniques for LLMs" (page 3); Abstract (page 1);
§6.1 and Figure 12-13 (pages 10-11); Figure 1 (page 1).

### 12. NVIDIA/TensorRT-LLM, H200 launch blog post (docs/source/blogs/H200launch.md) — CORRECTED
URL: https://github.com/NVIDIA/TensorRT-LLM/blob/main/docs/source/blogs/H200launch.md
Raw URL (fetched directly and read in full): https://raw.githubusercontent.com/NVIDIA/TensorRT-LLM/main/docs/source/blogs/H200launch.md
Primary: NVIDIA's own TensorRT-LLM repository documenting its own
benchmark numbers for its own inference engine.
**Correction: this table is NOT a batch-size sweep at fixed input/output
length.** It is titled "H200 FP8 Max throughput," and its own footnote (1)
states the batch size shown per row is "Largest batch supported on given TP
configuration by power of 2" — i.e., for each model/input-length/output-
length configuration NVIDIA chose to report, the batch size listed is simply
whatever the largest power-of-two batch happened to be that fit, not an
independently varied test parameter. Full transcription of every row, verbatim
from the raw file:

| Model | Batch Size | TP | Input Length | Output Length | Throughput (out tok/s/GPU) |
|---|---|---|---|---|---|
| llama_13b | 1024 | 1 | 128 | 128 | 11,819 |
| llama_13b | 128 | 1 | 128 | 2048 | 4,750 |
| llama_13b | 64 | 1 | 2048 | 128 | 1,349 |
| llama_70b | 512 | 1 | 128 | 128 | 3,014 |
| llama_70b | 512 | 2 | 128 | 2048 | 1,654 |
| llama_70b | 64 | 1 | 2048 | 128 | 341 |
| llama_70b | 32 | 1 | 2048 | 128 | 303 |

Footnotes on the table: "(1) Largest batch supported on given TP
configuration by power of 2." "(2) TP = Tensor Parallelism." Caption:
"Preliminary measured performance, subject to change. TensorRT LLM v0.5.0,
TensorRT v9.1.0.4 | H200, H100 FP8." The page opens with an explicit note
that "the below data is using TensorRT LLM v0.5. There have been significant
improvements in v0.6 & later" and points to a different, newer document for
current Llama numbers — this table is a preliminary, superseded snapshot from
the H200 launch (late 2023), not current TensorRT-LLM performance.

Reading the seven rows correctly: for llama_13b, all three rows use
different input AND output lengths (128/128, 128/2048, 2048/128) as well as
different batch sizes — three variables move together, so none of the three
throughput figures can be attributed to batch size alone. For llama_70b, two
rows (batch 64 and batch 32) DO share identical model, TP (1), input length
(2048), and output length (128) — a genuine matched pair, differing only in
batch size: 341 tok/s/GPU (batch 64) vs. 303 tok/s/GPU (batch 32), a 12.5%
increase for a 2x batch increase. This is real and clean, but it is only two
points and a modest effect size — too thin to carry a worked example alone.
The document separately states, in prose (not a table), two workload-level
comparisons that also confound batch size with everything else (model,
context length, TP, GPU count) and should not be read as a batch-only
comparison either: "an offline summarization scenario (ISL/OSL=2048/128)
with Llama-70B on a single H200 is 1.9x more performant than H100" (TP1) and
"an online chat agent scenario (ISL/OSL=80/200) with GPT3-175B on a full HGX
(TP8) H200 is 1.6x more performant than H100" (TP8) — these compare H200 to
H100 at fixed (but different-from-each-other) workloads, not batch sweeps.
Locator: the single table under "H200 FP8 Max throughput"; footnotes
immediately below it; "Max Throughput TP1"/"Max Throughput TP8" prose
paragraphs under "H200 vs H100."

### 13. Artificial Analysis, "Language Model API Performance Benchmarking" (methodology)
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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
*(Unchanged from 01.)*
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

- **NEW — the batch-vs-sequence-length confound trap (this is the defect the
  editor caught).** The NVIDIA/TensorRT-LLM H200 "Max throughput" table
  (source 12) looks, at a glance, like a batch-size sweep: three llama_13b
  rows, three batch sizes, three throughput numbers, invitingly close to a
  clean story. It is not one. Input length and output length change on every
  row along with batch size, because the table's actual purpose is reporting
  the best throughput NVIDIA found per workload shape, not isolating batch
  size as a variable. The only way to tell is reading the footnote and
  comparing every column, not just the batch-size and throughput columns.
  Any writer or reader building a "batch size alone" argument from a
  throughput table must first check that every other column (model, TP,
  input length, output length, hardware, precision) is actually held
  constant across the rows being compared — this table is a documented
  example of why that check matters.

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

- **Same hardware, same submitter, two (now twenty) audited MLPerf numbers
  30-66% apart.** Within the single v5.1 results file (source 2), identical
  hardware platforms report all three scenarios. This is not sources
  disagreeing; it is the same audited procedure proving the commission's
  batch-size/latency point on a single set of machines, repeated across 20
  independent platforms from 10+ different submitters and two GPU
  generations (B200, H200) plus AMD MI300X/MI325X. See Numbers for the full
  table — this is now the primary worked example for pillar 2.

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
| MLPerf v5.0 round participation | 17,457 performance results, 23 submitting orgs | Source 5 | v5.0 round, April 2025 |
| Median Llama2-70B score, v5.0 vs. v4.0 | Doubled; best score 3.3x faster | Source 5 | Year-over-year, same benchmark |
| Groq Llama2-70B, Groq's own figure | 270+ tokens/sec/user | Source 7 | After first token, ~1,000-token completion, FP16 compute/FP8-stored weights, no sparsity |
| Groq Llama2-70B, Anyscale LLMPerf independent measurement | 185 tok/s median (184 mean, 148-208 range); TTFT 0.22 s median | Sources 7, 15 | 550 input / 150 output tokens, 5 concurrent requests, includes TTFT in per-token average |
| Cerebras Llama3.1-8B launch claim | 1,800 tokens/sec | Source 8 | "Output speed per user," 16-bit weights, Aug 2024 |
| Cerebras Llama3.1-70B launch claim | 450 tokens/sec | Source 8 | "Output speed per user," 16-bit weights, Aug 2024 |
| Cerebras Llama3.1-70B updated claim | 2,100 tokens/sec (±20% normal variance) | Source 9 | Speculative decoding added, Nov 2024, "rigorously tested by Artificial Analysis" per Cerebras |
| Llama 3.1 70B, live AA-measured spread across providers | 37.9 to 119.6 tokens/sec (~3x) | Source 14 | Identical model, 10K-input-token AA standard workload, snapshot at time of research |
| vLLM vs. Orca (Oracle)/Orca (Max), request-rate sustained | 1.7x-2.7x / 2.7x-8x higher | Source 11 | OPT-13B/66B/175B, ShareGPT dataset, similar end-to-end latency |
| vLLM vs. Orca variants, mean batched requests at fixed request rate | ShareGPT @ 2 req/s: Orca(Max) 7.00, Orca(Pow2) 9.81, Orca(Oracle) 13.62, vLLM 30.42. Alpaca @ 30 req/s: 7.00 / 43.24 / 72.75 / 132.44 | Source 11, Figure 13 | OPT-13B, one system per column, same fixed request rate — compares systems' batching capacity, not a single-system batch sweep |

### CORRECTED — TensorRT-LLM H200 "Max throughput" table (full, verbatim; NOT a batch-only sweep)

| Model | Batch size | TP | Input length | Output length | Throughput (out tok/s/GPU) |
|---|---|---|---|---|---|
| llama_13b | 1,024 | 1 | 128 | 128 | 11,819 |
| llama_13b | 128 | 1 | 128 | 2,048 | 4,750 |
| llama_13b | 64 | 1 | 2,048 | 128 | 1,349 |
| llama_70b | 512 | 1 | 128 | 128 | 3,014 |
| llama_70b | 512 | 2 | 128 | 2,048 | 1,654 |
| llama_70b | 64 | 1 | 2,048 | 128 | 341 |
| llama_70b | 32 | 1 | 2,048 | 128 | 303 |

Source: source 12. Batch size, input length, and output length all vary
row-to-row for llama_13b — do not present those three rows as an isolated
batch-size effect. The one legitimate isolated pair, everything held constant
except batch size, is the last two llama_70b rows: **batch 64 → 341 tok/s/GPU
vs. batch 32 → 303 tok/s/GPU** (2,048 input / 128 output tokens, TP=1) — a
real but small (12.5%) effect from 2x the batch, and only two data points.
Not recommended as a standalone worked example or chart; usable only as a
supporting aside that even this modest, apples-to-apples pair moves in the
expected direction.

### NEW — MLPerf v5.1, same-hardware Offline/Server/Interactive throughput, Llama2-70B (clean apples-to-apples series for pillar 2 / chart-1)

Source: source 2 (raw results file), `Model=="llama2-70b-99"`,
`Category=="closed"`, `Availability=="available"`, grouped by
(Submitter, Platform), keeping only platforms reporting all three scenarios.
Same model, same hardware, per row; only the latency policy differs
(Offline = unconstrained; Server = 200 ms TPOT bound / 5 tok/s/user floor;
Interactive = 40 ms TPOT bound / 25 tok/s/user floor — bounds per sources 3,
4, 6). All figures in tokens/sec, aggregate across the full accelerator
count named.

| Submitter | Platform | Offline | Server | Interactive | Server→Interactive drop |
|---|---|---:|---:|---:|---:|
| Supermicro | SYS-422GS-NBRT-LCC_B200-SXM-180GBx8_TRT | 102,498.0 | 99,181.1 | 60,131.0 | 39.4% |
| NVIDIA | B200-SXM-180GBx8_TRT | 101,527.0 | 99,123.0 | 59,545.4 | 39.9% |
| Dell | XE9680L_B200_SXM_180GBx8_TRT | 101,253.0 | 99,139.2 | 60,137.6 | 39.3% |
| Nebius | B200-SXM-180GBx8_TRT | 101,246.0 | 101,611.0 | 59,622.7 | 41.3% |
| GigaComputing | G894-SD1_B200-SXM-180GBx8_TRT | 98,607.7 | 99,066.0 | 62,851.2 | 36.6% |
| Google | B200-SXM-180GBx8_TRT | 78,463.5 | 99,169.8 | 52,140.7 | 47.4% |
| NVIDIA | GB200-NVL72_GB200-186GB_aarch64x4_TRT | 51,736.9 | 49,359.6 | 29,745.6 | 39.7% |
| Dell | XE9680_H200_SXM_141GBx8_TRT | 35,316.7 | 33,244.3 | 21,915.6 | 34.1% |
| HPE | HPE_Cray_XD670_H200_SXM_141GBx8_TRT | 34,964.6 | 33,164.4 | 20,432.1 | 38.4% |
| Nebius | H200-SXM-141GBx8_TRT | 34,812.1 | 34,029.4 | 23,079.9 | 32.2% |
| Cisco | C885_H200x8_TRT | 34,548.2 | 33,163.3 | 19,621.9 | 40.8% |
| GigaComputing | 8xMI325X_2xEPYC_9575F | 34,483.2 | 32,139.4 | 18,825.9 | 41.4% |
| ASUSTeK | ESC_A8A_MI325X_256GBx8 | 33,987.4 | 31,241.0 | 15,566.2 | 50.2% |
| Vultr | 8xMI325X_2xEPYC_9554 | 33,762.5 | 30,339.4 | 17,709.6 | 41.6% |
| MiTAC | 8xMI325X_2xEPYC_9755 | 33,703.0 | 31,755.7 | 18,846.1 | 40.7% |
| Quanta Cloud Technology | D75T-7U_8xMI325X | 32,760.5 | 31,401.4 | 17,633.0 | 43.8% |
| Dell | XE7745_H200_NVL_141GBx8_TRT | 31,267.4 | 29,070.3 | 16,419.2 | 43.5% |
| AMD | 8xMI300X_2xEPYC_9575F | 27,803.9 | 24,593.8 | 8,840.4 | 64.1% |
| Dell | XE9680_MI300X_192GBx8 | 27,325.9 | 24,747.6 | 8,455.1 | 65.8% |
| Quanta Cloud Technology | D75E-4U_H200-NVL-141GBx4_TRT | 15,057.6 | 13,736.1 | 6,709.7 | 51.2% |

Reading: across every one of these 20 platforms, tightening the per-token
latency bound from 200 ms (Server) to 40 ms (Interactive) — with hardware,
model, and precision held fixed — cuts aggregate audited throughput by
roughly a third to two-thirds. The drop is not uniform (32% to 66%),
reflecting differences in how much headroom each software stack has, but the
direction is universal and the effect size is large on every single platform.
This is the clean, audited, same-hardware series this pillar needs; I
recommend the writer/dataviz use a representative subset (e.g., the 6 B200
rows, or one B200 + one H200 + one MI300X row) rather than all 20, to keep a
chart readable.

## Source assets

- **UPDATED — primary chart-1 candidate: MLPerf same-hardware Offline/Server/
  Interactive table above.** Not an image; a clean tabular series ready to
  chart (grouped bars or a slope chart per platform, Server vs. Interactive,
  or Offline/Server/Interactive as three bars per platform). This replaces
  the TensorRT-LLM batch table as the recommended source for chart-1. Keep
  whichever subset is charted honestly labeled with the actual latency bound
  each scenario enforces (200 ms/40 ms TPOT), not just the scenario name, so
  the chart carries the mechanism and not just a label.

- **DOWNGRADED — TensorRT-LLM H200 table.** Still usable as a small supporting
  aside (the one clean llama_70b pair, 341 vs. 303 tok/s/GPU) but not as a
  standalone chart or worked example; the full seven-row table mixes three
  variables and would mislead if charted as "throughput vs. batch size."
  If used at all, present only the matched pair, explicitly labeled with all
  four held-constant conditions (model, TP, input length, output length).

- **vLLM paper, Figure 1 (right panel).** Location: page 1 of source 11 (PDF
  page 1, right column figure). Shows measured throughput (tokens/sec) versus
  batch size (# requests) for a 13B model on an NVIDIA A100 40GB, plotting
  "Existing systems" against "vLLM," with the existing-systems line
  flattening early while vLLM's keeps climbing. Reader value: a direct visual
  of the batch-size lever, from the single system vLLM itself (unlike the
  cross-system Figure 12-14 curves). I could not read precise axis values
  reliably from the fetched image (the y-axis gridline labels were not
  legible at the resolution retrieved); a crop must keep both axis labels,
  the legend, and the full curve for both systems, and must not use the
  numeric gridline values without re-verifying them from the primary PDF at
  higher resolution. Do not crop out the axis titles ("Throughput (tok/s)",
  "Batch size (# requests)"). Given the MLPerf table above is now a stronger,
  fully-numeric primary for the same point, this figure is a secondary/visual
  supplement, not the load-bearing asset.

- No source asset found for the tokenizer pillar (pillar 3) beyond prose
  methodology text; None found beyond what is already in Numbers/Sources.

## Discarded

*(All 01 discards stand; one addition below.)*

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
- NEW: TensorRT-LLM H200 table's three llama_13b rows, as a "batch-size
  sweep" — this is the corrected defect itself. Retained above in full,
  correctly labeled, because the table is still useful evidence (just not
  for the claim 01 attached to it). Do not reuse the 01 framing ("128
  input/128 output tokens... driven only by batch size") anywhere in the
  article; that framing is retracted.
