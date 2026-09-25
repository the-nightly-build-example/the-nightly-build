# Evidence: the-instruments/mlperf (researcher 01)

The evidence supports the commission's spine directly. MLCommons' own rules
define the box a result lives in (division, availability category, scenario,
task, quality target) and its Messaging Guidelines state in plain terms that
results may only be compared inside compatible boxes and that any comparison
must disclose differences in version, division, category, verified status,
scenario, and chip count. The two founding papers give the metric definitions
(time-to-train to a quality target; per-scenario throughput/latency) and the
stated intent (fair, reproducible, comparable system measurement). For a
concrete results table I opened the MLPerf Training v5.0 submission logs
(MLCommons-owned) and pulled a clean comparable pair: the same submitter, same
benchmark, same division, same category, same accelerator, differing only in
chip count (256 vs 512 GB200 GPUs), with time-to-train falling from 205.6 to
106.5 minutes. That is the writer's illustration of why chip count is part of
the claim. For the misled case I have two documented, numbered instances: (a)
Google's TPU v4 paper showing that the raw MLPerf Training 2.0 leaderboard
ranks a 4,216-chip A100 system against a 256-chip Graphcore IPU, and that
normalizing to equal size changes the story; (b) recent press analysis of
MLPerf Inference v6.0, where NVIDIA's headline throughput "record" came from
the largest configuration ever submitted (288 GPUs) while AMD and Intel
submitted far smaller systems.

The evidence is thin in one place the commission may want more: I could not
open individual rows of the MLCommons interactive results dashboard (it renders
in JavaScript), so my exact per-submission numbers come from the primary
submission logs in the MLCommons results GitHub repository rather than from the
rendered web table. The logs are the same underlying MLCommons-owned records,
but they are one layer beneath the public dashboard. See Limits.

## Sources

```text
URL:         https://github.com/mlcommons/inference_policies/blob/master/inference_rules.adoc
Kind:        primary. MLCommons owns and publishes the inference rules; this
             document defines the terms it defines.
Establishes: The inference divisions (Closed, Network, Open); the four
             scenarios and their metrics; what a run and run result are.
Paraphrase:  Closed requires pre-/post-processing and model equivalent to the
             reference implementation, allows calibration for quantization, and
             allows no retraining. Network inherits all Closed requirements and
             adds a network fabric between LoadGen and the system under test;
             it supports only the Datacenter suite. Open allows arbitrary pre-/
             post-processing and model, including retraining. Every Open
             submission must be classified Available, Preview, or Research,
             Development, or Internal. The suite is split into Datacenter and
             Edge system types. The four scenarios: Single stream (LoadGen
             sends the next query when the system finishes the last; metric is
             the 90th-percentile early-stopping latency); Server/Interactive
             (Poisson arrivals; metric is the maximum Poisson throughput, i.e.
             queries per second, sustained under a tail-latency bound, 99%);
             Offline (all samples sent at once, at least 24,576; metric is
             measured throughput); Multistream (8 samples per query; metric is
             the 99th-percentile early-stopping latency).
Locators:    "Definitions" (run/run result); Section "Scenarios" with the
             scenario table; Section "Divisions" -> "Closed Division",
             "Network Division", "Open Division"; Open-division constraint
             list ("A open submission must be classified as ...").
Quote:       "The Closed division requires using pre-processing,
             post-processing, and model that is equivalent to the reference or
             alternative implementation. The closed division allows calibration
             for quantization and does not allow any retraining."
Quote:       "The Open division allows using arbitrary pre- or post-processing
             and model, including retraining."
```

```text
URL:         https://github.com/mlcommons/training_policies/blob/master/training_rules.adoc
Kind:        primary. MLCommons owns and publishes the training rules.
Establishes: The training divisions (Closed, Open); the time-to-train metric as
             a wall-clock measurement; the Closed-division models and quality
             targets for the current suite.
Paraphrase:  Two divisions: Closed requires the same preprocessing, model,
             training method, and quality target as the reference
             implementation; Open allows arbitrary training data,
             preprocessing, model, and/or training method but still requires
             supervised or reinforcement learning. A run is a complete
             execution training a model from initialization to the quality
             target; a run result is a wall-clock timing measurement of a
             contiguous period that includes model initialization above a
             maximum, on-clock data preprocessing, training, and quality
             evaluation unless the benchmark specifies otherwise. Current
             Closed-division targets include FLUX.1 at 0.586 eval loss,
             Llama3.1-8B at 3.3 log perplexity, Llama2-70B LoRA at 0.925 eval
             loss, DeepSeek-v3 671B at 3.6 log perplexity, and dlrm_v4_hstu at
             0.75 AUC.
Locators:    Section "Divisions" -> "Closed Division" (with the models/targets
             table) and "Open Division"; "Definitions" (run); "Metric" section
             ("A run result consists of a wall-clock timing measurement ...").
Quote:       "The Closed division requires using the same preprocessing, model,
             training method, and quality target as the reference
             implementation."
Quote:       "A run is a complete execution of an implementation on a system,
             training a model from initialization to the quality target."
```

```text
URL:         https://github.com/mlcommons/policies/blob/master/MLPerf_Results_Messaging_Guidelines.adoc
Kind:        primary. MLCommons owns this document; it defines the rules for
             stating and comparing MLPerf results.
Establishes: That MLPerf results may only be compared inside compatible boxes,
             and that a comparison must disclose every dimension of the box,
             including chip count. This is the rule the misled claims break.
Paraphrase:  Results may only be compared against compatible results (same
             benchmark and scenario, from compatible versions). When comparing,
             the main text, table, or figure must clearly identify any
             difference in version, division, category, verified/unverified
             status, scenario, or chip count. "Chip count" is defined as the
             count of the compute devices executing the largest number of ops,
             which could be processors or accelerators. When comparing Open and
             Closed results, any way the Open result would not qualify as
             Closed must be identified. A worked example in the document
             compares an 8-chip RDI Closed result against a 16-chip Available
             on-premise Closed result and requires both descriptions on the
             page. Each benchmark has one primary metric (e.g. time-to-train
             for Training image classification; queries/sec for the Server
             scenario of Datacenter Inference image classification); any
             comparison on a derived metric (power, cost, accuracy, model size)
             must state that basis.
Locators:    Sections "MLPerf results may only be compared against similar
             MLPerf results"; "When comparing MLPerf results, you must identify
             any submission differences"; "Comparisons based on secondary or
             derived metrics must be explicit."
Quote:       "When comparing results the main text, table, or figure must
             clearly identify any difference in version, division, category,
             verified or unverified status, scenario or chip count (count of
             the compute devices executing the largest number of ops, which
             could be processors or accelerators)."
Quote:       "MLPerf results may only be compared against compatible MLPerf
             results. Results are compatible if produced using the same
             benchmark and scenario from compatible versions of that
             benchmark."
```

```text
URL:         https://github.com/mlcommons/policies/blob/master/submission_rules.adoc
Kind:        primary. MLCommons owns this document; it defines the availability
             categories that group all results.
Establishes: The exact definitions of Available (cloud / on-premise), Preview,
             and Research, Development, or Internal (RDI), and that these
             categories apply to Closed, Network, and Open submissions alike.
Paraphrase:  Results are divided into categories by the availability of the
             hardware and software components. Available in cloud: available
             for rent in the cloud, with an available software stack. Available
             on premise: available for purchase, available software stack.
             Preview: must become available for rent or purchase by the next
             submission, or the submission after 140 days, whichever is longer,
             and the submitter commits to re-submitting as Available with equal
             or better performance (a Preview that is not later published as
             Available with matching performance is marked invalid). RDI: does
             not meet the Available or Preview requirements; RDI components may
             not be submitted as Available until the cycle after next or 221
             days, whichever is longer. Availability rules apply to Closed,
             Network, and Open divisions.
Locators:    Section "Results categories" (category table) and its
             subsections "Available Systems", "Preview Systems", "Research,
             Development, or Internal Systems".
Quote:       "Availability rules apply to Closed, Network and Open division
             submissions."
Quote:       "A research, development, or internal (RDI) component does not meet
             the requirements for an available or preview component."
```

```text
URL:         https://arxiv.org/abs/1910.01500
Kind:        primary. This is the design paper by the benchmark's authors;
             it owns the claims about MLPerf Training's metric and intent.
Establishes: What a Training submission measures and why; the five stated
             goals; the Closed/Open division intent; the original v0.5 tasks
             and quality targets.
Paraphrase:  MLPerf's performance metric is the time to train to a defined
             quality target; timing begins when the system touches any training
             or validation data and stops when it reaches the defined quality
             target on the validation set. The metric is chosen to prevent
             quality-reducing optimizations while allowing system-scale and
             software flexibility. Five stated goals: enable fair comparison
             while encouraging innovation; accelerate ML progress through fair
             and useful measurement; enforce reproducibility; serve commercial
             and research communities; keep the effort affordable. The Closed
             division is intended for direct system comparison by requiring
             equivalence to reference implementations; the Open division is
             intended to encourage innovation and hardware/software co-design.
             The v0.5 suite: ResNet-50 v1.5 (74.9% Top-1), SSD-ResNet-34 (21.2
             mAP), Mask R-CNN (37.7 box / 33.9 mask AP), GNMT (21.8 Sacre
             BLEU), Transformer (25.0 BLEU), NCF (0.635 HR@10), MiniGo (40.0%
             pro move prediction).
Locators:    Sec 2 goals list ("MLPerf aims to create a representative
             benchmark suite ... to meet five high-level goals"); Sec 3.2
             "Time-to-Train Performance Metric" and 3.2.1 "Timing Rules"; Sec
             4.2.1 submission divisions; Table 1 (v0.5 benchmarks/targets).
Quote:       "MLPerf's performance metric is the time to train to a defined
             quality target. It incorporates both system speed and accuracy and
             is most relevant to ML practitioners." (Sec 3.2)
Quote:       "Timing begins when the system touches any training or validation
             data, and it stops when the system achieves the defined quality
             target on the validation data set." (Sec 3.2.1)
Quote:       "The closed division is intended for direct system comparison, so
             it strives to ensure workload equivalence by requiring that
             submissions be equivalent to reference implementations." (Sec
             4.2.1)
```

```text
URL:         https://arxiv.org/abs/1911.02549
Kind:        primary. The design paper by the benchmark's authors; owns the
             claims about MLPerf Inference's scenarios and intent.
Establishes: The four scenarios and their metrics; the two divisions; the
             stated design principles.
Paraphrase:  Four scenarios represent critical inference applications. Single-
             stream: metric is the query stream's 90th-percentile latency.
             Multistream (as defined in v0.5): metric is the integer number of
             streams the system supports while meeting the quality-of-service
             requirement. Server: Poisson arrivals; metric is the Poisson
             parameter, i.e. the queries-per-second sustained under the QoS
             constraint. Offline: metric is throughput in samples per second.
             Two divisions: closed (strict rules; same models, data sets, and
             quality targets to ensure comparability) and open (submitters may
             change the model and demonstrate different performance and quality
             targets). Stated aim is measurement that is architecturally
             neutral, representative, and reproducible, with rules to ensure
             comparability across submissions.
Locators:    Sec III-C "Realistic End-User Scenarios" (Single-stream,
             Multistream, Server, Offline definitions); Sec I contributions
             list (representative workloads; divisions); Sec V-A result
             submissions/divisions/categories.
Quote:       "The metric for the offline scenario is throughput measured in
             samples per second." (Sec III-C, Offline)
Quote:       "MLPerf Inference has two divisions: closed and open. Strict rules
             govern the closed division, which addresses the lack of a standard
             inference-benchmarking workflow." (Sec I)
Note:        The v0.5 paper defines the multistream metric as the number of
             streams supported. The current inference rules doc redefines
             multistream as 8 samples/query scored on 99th-percentile
             early-stopping latency. Recorded under Contradictions as an
             evolution, so the writer does not present the paper's metric as
             the one in force today.
```

```text
URL:         https://github.com/mlcommons/training_results_v5.0
Kind:        primary. These are the MLCommons-owned submission records for
             MLPerf Training v5.0. The results table is the set of these logs;
             the numbers are owned here.
Establishes: A concrete comparable pair from a named, dated round, with system,
             accelerator type and count, division, and availability category
             taken from the submission's own system-description JSON and its
             timing log.
Paraphrase:  NVIDIA "Tyche" system, MLPerf Training v5.0, benchmark
             llama31_405b (Llama 3.1 405B pretraining), division "closed",
             status "Available on-premise". Two entries differ only in scale:
             (1) 4x NVIDIA GB200 NVL72 = 64 nodes x 4 accelerators = 256 GB200
             GPUs; (2) 8x NVIDIA GB200 NVL72 = 128 nodes x 4 = 512 GB200 GPUs.
             The result_0 timing logs give run_start and run_stop timestamps
             (Unix ms). 256-GPU: run_stop - run_start = 12,336,441 ms = 205.61
             minutes. 512-GPU: 6,391,753 ms = 106.53 minutes. Doubling the chip
             count cut time-to-train by 1.93x, holding benchmark, division,
             category, and accelerator fixed. The log header records
             submission_division "closed" and submission_status "onprem".
Locators:    NVIDIA/systems/tyche_ngpu512_ngc25.04_nemo.json and
             NVIDIA/systems/tyche_ngpu256_ngc25.04_nemo.json (division, status,
             system_name, number_of_nodes, accelerators_per_node,
             accelerator_model_name). NVIDIA/results/
             tyche_ngpu512_ngc25.04_nemo/llama31_405b/result_0.txt and the
             matching 256-GPU path (run_start/run_stop MLLOG lines,
             submission_division, submission_status). Blob URLs:
             https://github.com/mlcommons/training_results_v5.0/blob/main/NVIDIA/systems/tyche_ngpu512_ngc25.04_nemo.json
             https://github.com/mlcommons/training_results_v5.0/blob/main/NVIDIA/results/tyche_ngpu512_ngc25.04_nemo/llama31_405b/result_0.txt
Quote:       (system JSON, 512-GPU) "division": "closed", "status": "Available
             on-premise", "system_name": "Tyche (8x NVIDIA GB200 NVL72)",
             "number_of_nodes": "128", "accelerators_per_node": "4",
             "accelerator_model_name": "NVIDIA Blackwell GPU (GB200)".
Note:        result_0.txt is one run. MLPerf reports a benchmark result from a
             set of runs whose count depends on the benchmark's variance and
             cost (training_rules.adoc, "Metric"); result_1.txt/result_2.txt
             exist for some configs. The single-run wall clock is recorded
             here; the published score for the entry may use the round's
             run-selection rule. See Limits.
```

```text
URL:         https://mlcommons.org/2025/06/mlperf-training-v5-0-results/
Kind:        primary. MLCommons' own announcement of the v5.0 round; owns the
             round-level counts and MLCommons' framing of purpose.
Establishes: The round is real, named, and dated, and that MLCommons frames the
             suite as a level playing field for comparison. Anchors the v5.0
             logs above to a published round.
Paraphrase:  MLPerf Training v5.0 published 201 performance results from 20
             submitting organizations (AMD, ASUSTeK, Cisco, CoreWeave, Dell,
             GigaComputing, Google Cloud, HPE, IBM, Krai, Lambda, MangoBoost,
             Nebius, NVIDIA, Oracle, Quanta Cloud Technology, SCITIX,
             Supermicro, TinyCorp, and one more). Publication date June 4,
             2025. David Kanter is identified as Head of MLPerf at MLCommons.
Locators:    Results-summary paragraph (submission and organization counts);
             attributed statement from David Kanter.
Quote:       David Kanter (Head of MLPerf, MLCommons): "The open-source and
             peer-reviewed benchmark suite provides a level playing field for
             competition that drives innovation, performance, and energy
             efficiency for the entire industry."
```

```text
URL:         https://arxiv.org/abs/2304.01433
Kind:        primary. Google's TPU v4 paper (ISCA 2023) by the system's
             architects. It owns Google's analysis and its own measurements;
             it retells the MLPerf Training 2.0 leaderboard it cites.
Establishes: The clearest documented case of the commission's angle: the raw
             MLPerf Training 2.0 comparison across very different system scales,
             with the counter-explanation and numbers.
Paraphrase:  Section 6 ("MLPerf Benchmark Performance") compares TPU v4, NVIDIA
             A100, and Graphcore MK2 IPU (Bow) using published MLPerf Training
             2.0 results. Table 5 records the largest-scale MLPerf 2.0
             configuration as 4,216 chips for A100 and 256 chips for the IPU.
             The paper states that vendors are free to pick the system size
             they report, and that ideally MLPerf would benchmark systems of
             equal size, cost, or power, but does not require it. It states
             that the published MLPerf results for TPU v4 and A100 scale to much
             larger systems than the IPU (4096 vs 256 chips), and that for
             similar-sized systems TPU v4 is 1.15x faster than A100 on BERT and
             ~4.3x faster than the IPU, and 1.67x and ~4.5x faster respectively
             on ResNet. The abstract makes the same point: a 4x-larger 4096-chip
             system is "nearly 10x faster," but on equal-sized systems the gap
             is ~4.3-4.5x over the IPU. It also notes TPU v4's DLRM entry was in
             the research (RDI) category, and that peak FLOPS/second do not
             predict real performance (A100 has a 1.13x peak-FLOPS edge over TPU
             v4, yet TPU v4 is 1.15x-1.67x faster on these benchmarks).
Locators:    Sec 6 "MLPerf Benchmark Performance"; Table 5 ("Largest scale
             MLPerf 2.0 configuration": A100 4216 chips, Graphcore MK2 IPU 256
             chips); Figures 14-15 (reported MLPerf Training 2.0 performance by
             chip count); Sec 7.1 (peak FLOPS vs real performance).
Quote:       "Vendors are free to pick the size of the system for which they
             want to report results. Ideally, MLPerf would benchmark systems of
             equal size or cost or power, but that is not required." (Sec 6)
Quote:       "The published MLPerf results for TPU v4 and A100 both scale to
             much larger systems than the IPU (4096 vs 256 chips). For similar
             sized systems, TPU v4 is 1.15x faster for BERT than the A100 and
             ~4.3x faster than the IPU. For ResNet, TPU v4 is 1.67x and ~4.5x
             faster, respectively." (Sec 6)
Note:        Round is MLPerf Training 2.0 (2022). Google is a submitter, so the
             paper is primary for the claim it makes and its own measurements;
             it is a competing party's read on whether the raw comparison is
             fair, which is why the numbers it attributes to the leaderboard are
             cross-checked against the rules and the v5.0 logs rather than taken
             as MLCommons' own reading.
```

```text
URL:         https://developer.nvidia.com/blog/nvidia-blackwell-delivers-up-to-2-6x-higher-performance-in-mlperf-training-v5-0/
Kind:        primary for the claim NVIDIA makes; secondary for whether the
             comparison is fair (NVIDIA is the submitter and the marketer).
Establishes: A real vendor "N times faster" set of headline claims from a named
             round, and that the well-formed ones hold the box fixed. Gives the
             writer a legitimate same-box comparison to contrast with the
             stripped-box cases.
Paraphrase:  NVIDIA's MLPerf Training v5.0 post claims "up to 2.6x higher
             performance per GPU" for Blackwell (GB200 NVL72) versus Hopper
             (H100) across the v5.0 benchmarks. Component claims: Llama 3.1 405B
             pretraining 2.2x faster at 512 GPUs vs 512 GPUs (121.09 vs 269.12
             min); Llama 2 70B LoRA 2.5x faster at 8 GPUs vs 8 GPUs (11.14 vs
             27.93 min); Stable Diffusion v2 2.6x per-GPU at 8 vs 8 GPUs (12.86
             vs 33.97 min); R-GAT 2.25x per-GPU at 8 vs 8 GPUs (4.97 vs 11.18
             min). Each pairs the same benchmark and the same GPU count across
             two hardware generations.
Locators:    Per-benchmark result callouts in the post body; the "up to 2.6x
             per GPU" summary line.
Quote:       "up to 2.6x higher performance per GPU compared to Hopper across
             all seven MLPerf Training v5.0 benchmarks"
Note:        These are same-count, same-benchmark, same-division generational
             comparisons, which the rules permit; they are the honest kind, and
             the writer can use them to show what the misled claims omit. The
             512-GPU Llama figures here (121.09 / 269.12 min) are NVIDIA's, at a
             different NeMo/system config than the Tyche 256/512 logs I opened,
             so I keep the two sets separate and do not blend the numbers.
```

```text
URL:         https://the-decoder.com/nvidia-sets-new-mlperf-records-with-288-gpus-while-amd-and-intel-focus-on-different-battles/
Kind:        secondary. Trade-press analysis (THE DECODER, Maximilian
             Schreiner) of a specific round; reports on the claims from outside
             the submitting parties.
Establishes: A recent, named instance of a scale-dependent "record" and an
             explicit statement that cross-vendor MLPerf numbers are only
             partly comparable because each vendor picks favorable
             configurations.
Paraphrase:  For MLPerf Inference v6.0 (reported published April 1, 2026),
             NVIDIA connected four GB300 NVL72 systems, 288 GPUs total, over
             Quantum-X800 InfiniBand and reached roughly 2.49 million tokens per
             second on DeepSeek-R1 in the Offline scenario, described as the
             largest configuration ever submitted to MLPerf Inference. AMD used
             single-node eight-GPU setups for direct comparisons and up to 94
             GPUs on Llama 2 70B and GPT-OSS-120B; Intel showed four Arc Pro
             B70 cards in workstation configurations. The piece states results
             are only partially comparable because NVIDIA, AMD, and Intel use
             different system configurations, models, and scenarios, and each
             company frames its numbers around its own strengths.
Locators:    Body paragraphs on NVIDIA's 288-GPU submission and the 2.49M
             tokens/sec DeepSeek-R1 offline figure; paragraphs on AMD's and
             Intel's configurations; the comparability caveat.
Quote:       (Schreiner) results are "only partially comparable: Nvidia, AMD,
             and Intel use different system configurations, models, and
             scenarios," and "each company frames its numbers to put its own
             strengths front and center."
Note:        A secondary source supports that the claim was made and frames its
             fairness; it does not own the throughput number. The 2.49M
             tokens/sec figure is MLCommons-owned and should be cited to the
             v6.0 results if the writer uses it; I did not open the v6.0 log for
             that specific row (see Limits).
```

## Contradictions

- The commission's angle is that "N times faster" headlines "strip away the
  box." The rules cut against a simple version of that: MLCommons' Messaging
  Guidelines require any compliant comparison to disclose version, division,
  category, verified status, scenario, and chip count, and allow comparison
  only inside compatible boxes. So MLPerf does not hide the box; the failure is
  downstream, when marketing or coverage drops the required disclosures or a
  reader ignores them. The writer should locate the fault there, not in a
  claim that MLPerf conceals scale.

- Not every MLPerf "N times faster" claim is misleading. NVIDIA's v5.0
  per-GPU generational claims hold benchmark, chip count, division, and
  category fixed and vary only the hardware generation, which the rules permit.
  The angle needs the distinction between a same-box comparison and a
  stripped-box one, or it overreaches.

- The multistream inference metric changed. The 2019 inference paper defines it
  as the number of streams a system supports; the current inference rules doc
  defines it as 8 samples per query scored on 99th-percentile early-stopping
  latency. A lesson that cites the paper for "how the number is made" must use
  the current rules for what is measured today.

- The TPU v4 numbers come from a submitter (Google) reading a leaderboard on
  which it competes. They are consistent with the rules (vendors do pick system
  size; MLPerf does not require equal-size comparison) and with the v5.0 logs
  (scale moves time-to-train sharply), so I treat them as reliable, but the
  editor should note they are one competitor's framing of the A100 and IPU
  entries, not MLCommons' own commentary.

## Numbers

```text
Figure: 205.61 min (12,336,441 ms) time-to-train, Llama 3.1 405B pretraining
Owner:  MLCommons, MLPerf Training v5.0 (NVIDIA "Tyche" submission log)
Scope:  256 NVIDIA GB200 GPUs (64 nodes x 4); Closed division; Available
        on-premise; result_0.txt single run. Run stops at the benchmark's
        log-perplexity target; I did not read the exact target value (the
        MLCommons Llama 3.1 405B page states the metric is log perplexity to a
        defined target but does not give the number). See Limits.
```

```text
Figure: 106.53 min (6,391,753 ms) time-to-train, Llama 3.1 405B pretraining
Owner:  MLCommons, MLPerf Training v5.0 (NVIDIA "Tyche" submission log)
Scope:  512 NVIDIA GB200 GPUs (128 nodes x 4); Closed division; Available
        on-premise; result_0.txt single run. Same benchmark/division/category/
        accelerator as the 256-GPU entry above; only chip count differs.
```

```text
Figure: 1.93x faster (256-GPU time / 512-GPU time = 205.61 / 106.53)
Owner:  Derived from the two MLCommons v5.0 Tyche logs above.
Scope:  The gain from doubling chip count within one box; not a per-chip
        capability gain. This is the writer's comparable pair.
```

```text
Figure: A100 4,216 chips vs Graphcore MK2 IPU 256 chips (largest-scale entries)
Owner:  MLPerf Training 2.0, as tabulated in Google's TPU v4 paper, Table 5
Scope:  The raw leaderboard ranks systems of ~16x different chip counts against
        each other; the "record" position tracks scale. Non-comparable pair.
```

```text
Figure: TPU v4 1.15x faster than A100 on BERT; 1.67x on ResNet (equal size)
Owner:  Google TPU v4 paper, Sec 6 (its normalization of MLPerf 2.0 results)
Scope:  Per-similar-size comparison; contrast with ~4.3x-4.5x over the IPU on
        the same two benchmarks at equal size. Shows how normalizing to chip
        count changes the ordering the raw table implies.
```

```text
Figure: ~2.49 million tokens/sec, DeepSeek-R1, Offline scenario
Owner:  MLCommons, MLPerf Inference v6.0 (reported by THE DECODER; NVIDIA
        submission). I did not open the v6.0 log row for this figure.
Scope:  288 NVIDIA GB300 GPUs (four GB300 NVL72 systems) - the largest
        configuration submitted; not comparable to an 8-GPU competitor entry.
```

```text
Figure: MLPerf Training v5.0 = 201 performance results, 20 organizations
Owner:  MLCommons v5.0 results announcement
Scope:  Round-level context, published June 4, 2025.
```

```text
Figure: NVIDIA v5.0 marketing: 2.2x (Llama 3.1 405B, 512 vs 512 GPU), 2.5x
        (Llama 2 70B LoRA, 8 vs 8), 2.6x per-GPU (Stable Diffusion v2, 8 vs 8),
        2.25x per-GPU (R-GAT, 8 vs 8), Blackwell GB200 vs Hopper H100
Owner:  NVIDIA developer blog (vendor claim); underlying runs MLPerf v5.0
Scope:  Same-benchmark, same-count, cross-generation. The legitimate kind of
        MLPerf comparison, kept separate from the Tyche 256/512 logs.
```

## Limits

- I could not open individual rows of the MLCommons interactive results
  dashboard at mlcommons.org/benchmarks/training and /inference; it renders in
  JavaScript that a fetch does not execute. My exact per-submission numbers come
  from the primary submission logs in mlcommons/training_results_v5.0, which are
  the same MLCommons-owned records one layer beneath the dashboard. This is the
  single most important limit: a reader clicking the public dashboard sees a
  rendered table, not the raw logs I read, so the writer should link the
  dashboard for the reader and can cite the repo for the exact figure.

- The time-to-train figures I computed are from result_0.txt, one run.
  MLCommons reports a benchmark result from a set of runs (count set per
  benchmark by variance and cost). I did not reconstruct the round's
  run-selection to produce the single "official" published number for each
  entry, so treat 205.61 and 106.53 minutes as the run_0 wall clock, accurate
  to the second from the log timestamps, not as a claim about which run
  MLCommons published.

- I did not open the MLPerf Inference v6.0 log row for the 2.49M tokens/sec
  DeepSeek-R1 figure; it rests on THE DECODER's report. If the writer uses that
  number, it should be pulled from the v6.0 results (MLCommons-owned) before
  publication.

- HPCwire's December 2021 piece on competitors disputing MLPerf comparisons and
  its April 2025 v5.0 piece both returned HTTP 403 (gated), so I could not read
  a second independent trade-press account of a disputed record. The documented
  misled case rests on the TPU v4 paper (primary) and THE DECODER (secondary),
  which is sufficient for the floor but leaves the cross-vendor dispute with one
  secondary voice rather than two.

- I did not independently re-derive the Llama 3.1 405B v5.0 quality target from
  the log; I carried it from the benchmark definition. The writer should
  confirm the exact target value against the current training rules if the
  lesson states it.

## Source assets

```text
Asset: The MLPerf Training v5.0 results dashboard/table at
       mlcommons.org/benchmarks/training, filtered to one benchmark (e.g.
       Llama 3.1 405B), showing the System, Processor/Accelerator and count,
       Division, and Availability columns side by side.
Shows: That every published row carries the box - accelerator count, division,
       category - next to the time. It makes concrete that the number is a row
       in a labeled table, not a bare speed.
Crop:  Must keep the column headers (system, accelerator + count, division,
       category, result) and at least two rows that differ in chip count.
       Cannot crop away the division/category columns, which are the point.
```

```text
Asset: The worked comparison example in the MLPerf Results Messaging
       Guidelines (the "8 chips in the RDI category of Closed Division ...
       faster than ... 16 chips in the Available on-premise category" passage).
Shows: MLCommons' own template for a compliant comparison, spelling out every
       box dimension a claim must disclose. Strong for the lesson's rule
       section.
Crop:  Keep the full sentence with both systems' chip counts, categories, and
       divisions; a partial crop that drops one side loses the lesson.
```

```text
Asset: Figure 14/15 of the TPU v4 paper (arXiv:2304.01433): reported MLPerf
       Training 2.0 performance plotted against number of chips, with columns
       labeled by chip count and IPU/A100/TPU v4 points.
Shows: Visually that leaderboard position rises with chip count, and that
       equal-size comparison is a different reading than the raw ranking.
Crop:  Keep the chip-count axis labels and the per-system points; the axis is
       the argument. This is a third-party figure; caption it as Google's, not
       MLCommons'.
```

## Discarded

```text
URL: https://www.hpcwire.com/2021/12/01/nividia-dominates-latest-mlperf-results-but-competitors-start-speaking-up/ - HTTP 403 (gated); could not open to read or quote. Noted in Limits.
URL: https://www.hpcwire.com/2025/04/02/mlperf-v5-0-reflects-the-shift-toward-reasoning-in-ai-inference/ - HTTP 403 (gated); could not read.
URL: https://ar5iv.labs.arxiv.org/html/2304.01433 - redirects to the arXiv abstract (no ar5iv HTML for this paper); read the paper's PDF text instead.
URL: https://mlcommons.org/2025/05/training-llama31405b/ - read, but thin: confirms the Llama 3.1 405B metric is log perplexity to a target and that it replaced the GPT-3 benchmark; no results, no distinct numbers beyond the rules doc, so not carried as its own Sources entry.
```
