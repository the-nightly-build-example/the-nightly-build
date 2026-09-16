# Evidence record: the-evidence/flashattention (researcher 01)

The evidence strongly supports the commission's central angle and its correction. The 2022
FlashAttention paper was read in full (all 34 pages including appendices B–E, the algorithm
listings, the IO-complexity proofs, and the full benchmark tables), not summarized from its
abstract. Every figure the commission leans on is verified against the passage that owns it,
including the A100 memory-hierarchy numbers, which are additionally cross-checked against two
NVIDIA vendor documents. FlashAttention-2 and FlashAttention-3 are verified against their own
abstracts and stated results for the present-day section. The evidence is thin in one place: I
verified the A100's HBM capacity and bandwidth directly against NVIDIA's own datasheet and
architecture whitepaper, but the paper's on-chip SRAM bandwidth figure (~19 TB/s) traces only to
third-party microbenchmarking papers, not to any NVIDIA-published spec — the paper says so
itself ("estimated"), and I confirmed NVIDIA's own architecture whitepaper never states an
SRAM/shared-memory bandwidth figure at all. This is a genuine asymmetry in the sourcing of an
idea-2 number and the writer should not present both halves of "192KB SRAM at ~19TB/s" as
equally vendor-sourced. Separately, the paper's own speedup claims are scoped to different
things (an attention-op-only forward pass, a specific fwd+bwd config, and end-to-end training
wall-clock) and a careless retelling can conflate them; this record keeps them separated by
table/figure so the writer doesn't average or misattribute across benchmarks.

## Sources

```text
URL:         https://arxiv.org/abs/2205.14135
Kind:        primary — Dao, Fu, Ermon, Rudra, and Ré are the paper's authors; it is the
             document that owns every FlashAttention v1 claim, algorithm, and benchmark number.
Establishes: The algorithm (tiling + recomputation), the IO-complexity theorems, the A100
             memory-hierarchy figures the paper cites, and all v1 training/benchmark numbers.
Paraphrase:  FlashAttention computes exact attention — bit-for-bit the same output as standard
             attention — by never materializing the full N×N score matrix in slow GPU memory.
             It tiles the computation into blocks that fit in fast on-chip memory, keeps a
             running (online) softmax across tiles, and in the backward pass recomputes the
             score blocks from the same tiles rather than storing them. This trades additional
             floating-point operations for far fewer memory reads/writes, and IO — not FLOPs —
             is what standard attention was actually bottlenecked on.
Locators:    Abstract; §2.1 "Hardware Performance"; §2.2 "Standard Attention Implementation";
             §3.1 "An Efficient Attention Algorithm With Tiling and Recomputation" (Theorem 1);
             §3.2 "Analysis: IO Complexity" (Theorem 2); §4 "Experiments" (Tables 1–6, Figs. 1–3);
             Appendix E.6 (Tables 8–21, full benchmark series).
Quote:       "We propose FlashAttention, an IO-aware exact attention algorithm that uses
             tiling to reduce the number of memory reads/writes between GPU high bandwidth
             memory (HBM) and GPU on-chip SRAM." (Abstract). "Even with the increased FLOPs due
             to recomputation, our algorithm both runs faster ... and uses less memory ..."
             (§1, p.2). "As an example, the A100 GPU has 40-80GB of high bandwidth memory (HBM)
             with bandwidth 1.5-2.0TB/s and 192KB of on-chip SRAM per each of 108 streaming
             multiprocessors with bandwidth estimated around 19TB/s [44, 45]." (§2.1, p.3).

URL:         https://arxiv.org/abs/2307.08691
Kind:        primary — Dao is the sole author; the paper that owns every FlashAttention-2
             claim and number cited for the present-day section.
Establishes: That FlashAttention-2 is a faster, still-exact successor; its speedup over v1 and
             its fraction of theoretical peak FLOPs/s on A100; that PyTorch's own maintainers
             integrated it (credited in the acknowledgments, not claimed by Dao as adoption).
Paraphrase:  FlashAttention v1 still only reached 25-40% of the FLOPs/s a raw matrix-multiply
             achieves on A100, because of suboptimal work partitioning across GPU thread blocks
             and warps. FlashAttention-2 restructures the parallelism (more thread blocks, less
             non-matmul work, less inter-warp communication) to reach 50-73% of peak, roughly a
             2x speedup over v1, while still computing exact attention.
Locators:    Abstract; §1 Introduction (background paragraph on v1's 25-40% figure); §3.1.1
             "Correctness, runtime, and memory requirement"; Acknowledgments.
Quote:       "FlashAttention is still not nearly as fast as optimized matrix-multiply (GEMM)
             operations, reaching only 25-40% of the theoretical maximum FLOPs/s." "...yield
             around 2x speedup compared to FlashAttention, reaching 50-73% of the theoretical
             maximum FLOPs/s on A100..." "...training speed of up to 225 TFLOPs/s per A100 GPU
             (72% model FLOPs utilization)." "Algorithm 1 returns the correct output
             O=softmax(QK^T)V (with no approximation)." "We thank Driss Guessous for
             integrating FlashAttention to PyTorch."

URL:         https://arxiv.org/abs/2407.08608
Kind:        primary — Shah, Bikshandi, Zhang, Thakkar, Ramani, and Dao are the paper's
             authors; the document that owns every FlashAttention-3 claim.
Establishes: The Hopper-specific (H100) technique (warp specialization/asynchrony, FP8
             low-precision) and its own headline speedup/throughput numbers, kept separate from
             v1/v2's A100 numbers.
Paraphrase:  On H100, plain FlashAttention-2 only reaches about 35% utilization because it
             doesn't exploit H100's asynchronous Tensor Cores and data-movement engine.
             FlashAttention-3 overlaps computation and data movement via warp specialization and
             adds FP8 support, reaching 1.5-2.0x the speed of FlashAttention-2 on H100: up to 740
             TFLOPs/s in FP16 (75% utilization) and close to 1.2 PFLOPs/s in FP8, with FP8 error
             2.6x lower than a naive FP8 baseline.
Locators:    Abstract.
Quote:       "...achieving merely 35% efficiency on H100 GPUs" (paraphrase of stated H100
             utilization gap; verified via fetched abstract, not the full PDF — see limitation
             below). "speedups of 1.5-2.0x with FP16 reaching 740 TFLOPs/s (75% utilization),"
             "FP8 reaching close to 1.2 PFLOPs/s," "FP8 FlashAttention-3 achieves 2.6x lower
             numerical error than a baseline FP8 attention."

URL:         https://images.nvidia.com/aem-dam/en-zz/Solutions/data-center/nvidia-ampere-architecture-whitepaper.pdf
Kind:        primary — NVIDIA's own architecture whitepaper for the A100 GPU; it owns the SM
             count, on-chip memory size, and HBM2 bandwidth figures for the 40GB A100.
Establishes: That the FlashAttention paper's "108 streaming multiprocessors" and "192KB of
             on-chip SRAM per SM" match NVIDIA's own published A100 die specification exactly,
             and that the 1.5TB/s end of the paper's HBM bandwidth range matches the 40GB SKU.
             Also establishes, by absence, that NVIDIA does not publish an SRAM/shared-memory
             bandwidth figure anywhere in this document.
Paraphrase:  The full GA100 die has 128 SMs; the shipped A100 product enables 108 of them. Each
             SM has 192KB of combined L1 data cache / shared memory (up from 128KB on V100) —
             this is the "on-chip SRAM" the FlashAttention paper means. The 40GB A100 SKU has
             1,555 GB/s of HBM2 bandwidth. The whitepaper's only "TB/s" figures anywhere in the
             document describe NVLink/NVSwitch interconnect bandwidth, not on-chip memory
             bandwidth.
Locators:    p.15 "A100 GPU Streaming Multiprocessor (SM)" (192KB vs 128KB per SM); p.16 "40 GB
             HBM2 and 40 MB L2 Cache" (1555 GB/sec); p.19 "NVIDIA A100 Tensor Core GPU
             Architecture In-Depth" (128 SMs full die; 108 SMs shipped A100); p.35 "A100 HBM2
             and L2 Cache Memory Architectures" (1555 GB/sec, 1215 MHz DDR, 5 HBM2 stacks); p.36
             Table 4 "Comparison of NVIDIA Data Center GPUs" (SMs: 56/80/108 for
             P100/V100/A100).
Quote:       "The larger and faster L1 cache and shared memory unit in A100 provides 1.5x the
             aggregate capacity per SM compared to V100 (192 KB vs 128 KB per SM)..." (p.15).
             "...7 GPCs, 7 or 8 TPCs/GPC, 2 SMs/TPC, up to 16 SMs/GPC, 108 SMs" (p.19, A100
             implementation) vs. "128 SMs per full GPU" (p.19, full GA100 die). "...the NVIDIA
             A100 GPU has 40 GB of high-speed HBM2 memory with a class-leading 1555 GB/sec of
             memory bandwidth..." (p.16).

URL:         https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/a100/pdf/nvidia-a100-datasheet-us-nvidia-1758950-r4-web.pdf
Kind:        primary — NVIDIA's own product datasheet; it owns the per-SKU memory capacity and
             bandwidth spec across all four A100 configurations.
Establishes: The 80GB SKU half of the FlashAttention paper's "40-80GB ... 1.5-2.0TB/s" range,
             which the architecture whitepaper alone does not cover (that document only
             describes the original 40GB A100).
Paraphrase:  The A100 ships in four capacity/form-factor combinations. The two SXM4 variants —
             the form factor FlashAttention's own benchmarks use — are 40GB HBM2 at 1,555 GB/s
             and 80GB HBM2e at 2,039 GB/s. The 80GB PCIe variant is slightly slower at 1,935
             GB/s. So the paper's stated upper bound of "2.0TB/s" matches the 80GB SXM4 card
             specifically, not the 80GB PCIe card.
Locators:    p.1, table "NVIDIA A100 TENSOR CORE GPU SPECIFICATIONS (SXM4 AND PCIe FORM
             FACTORS)", rows "GPU Memory" and "GPU Memory Bandwidth".
Quote:       "GPU Memory: 40GB HBM2 | 80GB HBM2e | 40GB HBM2 | 80GB HBM2e. GPU Memory
             Bandwidth: 1,555GB/s | 1,935GB/s | 1,555GB/s | 2,039GB/s" (columns are 40GB PCIe /
             80GB PCIe / 40GB SXM / 80GB SXM, p.1).

URL:         https://pytorch.org/blog/out-of-the-box-acceleration/
Kind:        secondary — PyTorch's own engineering blog reporting on its own integration of
             FlashAttention; secondary with respect to FlashAttention's technical claims (it
             reports on and benchmarks the paper's algorithm rather than owning any of the
             algorithm's own claims), but it is the primary record of PyTorch's adoption
             decision itself.
Establishes: That FlashAttention (cited directly, linking arXiv:2205.14135) was built into
             PyTorch's native torch.nn.functional.scaled_dot_product_attention as of the
             PyTorch 2.0 release, giving the "adoption into standard training and inference
             stacks" claim a citable, dated primary action (not just reputation).
Paraphrase:  As part of PyTorch 2.0, PyTorch added a native fused-attention op that dispatches
             to a FlashAttention kernel (or a memory-efficient-attention kernel, or a plain C++
             fallback) depending on the input shapes and hardware. Reported gains: 5-20% faster
             inference, 10-70% faster training, and up to 3x speedup / 40x memory savings in
             isolated small-head-dimension benchmarks — with the caveat that gains shrink as
             head dimension grows (3.4x at head dim 8 down to 1.01x at head dim 128 in their own
             benchmark) because the SRAM tile size / head-dimension tradeoff the FlashAttention
             paper itself describes starts to bind.
Locators:    Body text, opening paragraph ("This implementation leverages fused kernels from
             FlashAttention..."); section "Flash Attention, Memory-efficient attention & math
             differences"; section "Head dimension influence on speedups, memory savings."
Quote:       "This implementation leverages fused kernels from FlashAttention and
             Memory-efficient attention, and supports both training and inference." "...the
             highest speedups for flash attention are in a regime where the ratio d^2/M is
             small enough" (echoing the FlashAttention paper's own IO-complexity term).
             Note: the page gave no clear original publication date (only a "last updated"
             stamp); it describes the PyTorch 2.0 release, which shipped March 2023 — I did not
             independently confirm the post's original publish date and say so rather than
             guess.

URL:         https://huggingface.co/docs/transformers/attention_interface
Kind:        secondary — Hugging Face's own library documentation, reporting on its own
             integration of FlashAttention-2 and FlashAttention-3 as named backends; secondary
             to the FlashAttention papers, primary to Hugging Face's adoption decision.
Establishes: That the "present-day" adoption claim extends past PyTorch's core op into the
             standard inference/training library stack, and names FlashAttention-2 and
             FlashAttention-3 as distinct, currently supported backend options a model can be
             loaded with by name.
Paraphrase:  Transformers' AttentionInterface lets a model be loaded with
             attn_implementation="flash_attention_2" or "flash_attention_3" (plus paged
             variants for inference serving), alongside PyTorch's own "sdpa" backend and a
             from-scratch "flex_attention" path. The library describes FlashAttention-2 as
             tiling into blocks that use fast on-chip memory, and FlashAttention-3 as improving
             on it by overlapping operations and fusing forward/backward more tightly —
             language consistent with the papers' own framing, not a rival characterization.
Locators:    Section "Attention backends" (backend table); code example under "Set an attention
             backend."
Quote:       "\"flash_attention_2\" — tiles computations into smaller blocks and uses fast
             on-chip memory" / "\"flash_attention_3\" — improves FlashAttention-2 by also
             overlapping operations and fusing forward and backward passes more tightly."
```

## Contradictions

- **The central one the commission asked me to check for.** The common shorthand — "FlashAttention approximates attention" or "skips work" or "uses fewer FLOPs" — directly contradicts the paper's own claims at every level: the title itself ("Exact Attention"), the abstract ("IO-aware exact attention algorithm"), Theorem 1 ("Algorithm 1 returns O = softmax(QK^T)V" — the literal correct output, no approximation), and the FLOPs table in Figure 2 (standard attention 66.6 GFLOPs vs. FlashAttention **75.2 GFLOPs** — FlashAttention uses *more* FLOPs, not fewer, because it recomputes attention scores in the backward pass rather than storing them). The paper is explicit about the source of its speedup: "Even though FlashAttention has higher FLOP count compared to standard attention (due to recomputation in the backward pass), it has much fewer HBM accesses, resulting in much faster runtime" (§3.2, discussing Fig. 2 left). This is squarely the misreading idea 5 asks the lesson to correct, and the primary source supports the correction cleanly with a table, not just a quote.
- **One real exception the writer must not blur past.** The paper *does* introduce an approximate variant — "block-sparse FlashAttention" — which skips some blocks entirely and is explicitly called "an approximate attention algorithm" (§1, p.2) with its own, smaller IO complexity (Proposition 4). Anyone citing "FlashAttention is approximate" using block-sparse results as the evidence is technically citing a real thing, just not the algorithm most people mean by "FlashAttention." The lesson should name this distinction if it discusses block-sparse at all, so it doesn't accidentally create the very confusion idea 5 is trying to dispel.
- **Multiple "speedup" numbers exist in the same paper, scoped to different things, and are not interchangeable.** In descending order of what's measured: (1) "7.6x" is a single-configuration, attention-computation-only forward-pass number illustrated in Figure 1 (right panel), with the benchmark configuration not fully specified in the caption; (2) 41.7ms→7.3ms (~5.7x) is forward+backward runtime for one specific config — GPT-2 medium, seq length 1024, head dim 64, 16 heads, batch size 64, A100 (Figure 2 left / its table); (3) "up to 3x" (intro bullet, "Benchmarking Attention") is the forward-pass-only runtime advantage over PyTorch's standard attention across seq lengths 128–2048 with dropout+masking (Table 9: e.g., 0.78ms→0.21ms at seq 512, ~3.7x, so "up to 3x" is if anything a slightly conservative rounding); (4) the *end-to-end training wall-clock* numbers are different again and smaller, because they include everything else in the model: 15% for BERT-large (Table 1), and up to 3x for GPT-2 small / 3.0x for GPT-2 medium vs. HuggingFace, but only ~1.7-1.8x vs. Megatron-LM (Table 2; and the paper's own running text in §4 undersells this slightly, rounding "up to 3x" against HuggingFace when Table 2 actually shows 3.5x for GPT-2 small). None of these four numbers is "the" FlashAttention speedup; each is scoped to a specific operation, config, and baseline, and the lesson's idea-4 worked numbers should keep them separated rather than picking the single biggest one.
- **No contradiction found between the paper and FlashAttention-2/3 on the exactness claim.** FlashAttention-2's abstract and its own Theorem restatement both explicitly repeat "no approximation," and FlashAttention-3's abstract frames its FP8 mode as introducing bounded numerical error from low-precision arithmetic (a different, orthogonal source of inexactness from the sparsity/approximation the v1 paper distinguishes) — worth a careful sentence if the lesson touches FP8, since "FP8 has 2.6x lower error than a naive FP8 baseline" is not the same claim as "attention is computed exactly."
- **No contradiction found on the A100 HBM figures.** NVIDIA's architecture whitepaper (40GB SKU) and its own datasheet (all four SKUs) agree with each other and with the FlashAttention paper's stated "40-80GB ... 1.5-2.0TB/s" range once the range is read as spanning the 40GB SXM (1,555 GB/s) to 80GB SXM (2,039 GB/s) configurations — the form factor the paper's own benchmarks actually use (Table 7 names "A100-SXM4-40GB" explicitly).
- **A real sourcing asymmetry, not a contradiction, but the writer should not treat it as one.** The HBM capacity/bandwidth figures in "40-80GB HBM ... 1.5-2.0TB/s" trace cleanly to NVIDIA's own published datasheet and architecture whitepaper (verified above). The on-chip SRAM bandwidth figure ("~19TB/s") does not: NVIDIA's architecture whitepaper contains no SRAM/shared-memory bandwidth figure anywhere (confirmed by a full-text search of the document — its only "TB/s" figures describe NVLink/NVSwitch interconnect bandwidth). The FlashAttention paper itself flags this by saying the SRAM figure is "estimated" and citing two third-party microbenchmarking papers ([44] Jia & Van Sandt 2021, [45] Jia et al. 2018) rather than an NVIDIA document. If the lesson presents "192KB @ ~19TB/s" and "40GB @ ~1.5TB/s" side by side as two vendor-spec facts, it would overstate the SRAM number's provenance.

## Numbers

```text
Figure: 108 streaming multiprocessors on the shipped A100 (128 on the full GA100 die)
Owner:  NVIDIA Ampere Architecture Whitepaper, p.19 / Table 4, p.36; matches FlashAttention
        paper §2.1
Scope:  Per-GPU; A100 product (not the uncut GA100 test-chip die)

Figure: 192KB combined L1 data cache / shared memory per SM ("on-chip SRAM" in the paper)
Owner:  NVIDIA Ampere Architecture Whitepaper, p.15
Scope:  Per streaming multiprocessor; 1.5x V100's 128KB

Figure: 40GB HBM2 @ 1,555 GB/s (A100 40GB SXM4); 80GB HBM2e @ 2,039 GB/s (A100 80GB SXM4);
        80GB HBM2e @ 1,935 GB/s (A100 80GB PCIe)
Owner:  NVIDIA A100 datasheet, p.1 (SKU table); whitepaper p.16/p.35 confirms the 40GB/1555
        figure independently
Scope:  Per-GPU, per-SKU; the FlashAttention paper's "1.5-2.0TB/s" spans the two SXM4 SKUs

Figure: ~19 TB/s estimated on-chip SRAM bandwidth
Owner:  FlashAttention paper §2.1, citing third-party microbenchmarking (refs [44],[45]) — NOT
        an NVIDIA-published figure (absent from both NVIDIA documents I read)
Scope:  Per SM; explicitly labeled "estimated" by the paper itself

Figure: N×N attention score matrix for N=1024, d=64 (the paper's own GPT-2 example)
Owner:  FlashAttention paper §2.2 ("Often N ≫ d, e.g., for GPT2, N=1024 and d=64")
Scope:  One matrix S = QK^T ∈ R^(N×N); entry count = 1024×1024 = 1,048,576. NOTE: the paper
        does not itself state a byte size here — this entry-count and any byte-size the writer
        derives from it (e.g., ~2.1MB at 2 bytes/entry for one head, one batch item, in FP16;
        the paper trains in FP16 per Appendix E.1/E.2) is arithmetic on the paper's own N,d
        values, not a number printed in the paper, and should be labeled as computed if used.

Figure: GFLOPs 66.6 (standard) vs. 75.2 (FlashAttention); HBM R/W 40.3GB vs. 4.4GB;
        runtime 41.7ms vs. 7.3ms
Owner:  FlashAttention paper, Figure 2 (left) and its table
Scope:  Forward+backward pass; GPT-2 medium config specifically — seq length 1024, head dim 64,
        16 heads, batch size 64, on one A100 GPU. Not a general "FlashAttention vs standard"
        number; scoped to this one configuration.

Figure: BERT-large training time: 20.0 ± 1.5 min (Nvidia MLPerf 1.1) vs. 17.4 ± 1.4 min
        (FlashAttention) — 15% faster
Owner:  FlashAttention paper, Table 1
Scope:  Training to 72.0% target masked-language-modeling accuracy, averaged over 10 runs,
        8×A100 GPUs

Figure: GPT-2 training time/perplexity — small: HuggingFace 9.5 days (18.2 ppl) vs.
        Megatron-LM 4.7 days (18.2 ppl, 2.0x) vs. FlashAttention 2.7 days (18.2 ppl, 3.5x);
        medium: HuggingFace 21.0 days (14.2 ppl) vs. Megatron-LM 11.5 days (14.3 ppl, 1.8x)
        vs. FlashAttention 6.9 days (14.3 ppl, 3.0x)
Owner:  FlashAttention paper, Table 2
Scope:  End-to-end training wall-clock on 8×A100 GPUs, OpenWebText, 400K steps

Figure: Long-Range Arena average accuracy/speedup: standard Transformer 59.3 (baseline);
        FlashAttention 59.8, 2.4x speedup; block-sparse FlashAttention 59.6, 2.8x speedup
Owner:  FlashAttention paper, Table 3
Scope:  Average across 5 LRA tasks (ListOps, Text, Retrieval, Image, Pathfinder), seq lengths
        1024-4096, geometric-mean speedup

Figure: GPT-2 small, longer context — Megatron-LM at 1k context: 18.2 ppl, 4.7 days (1.0x);
        FlashAttention at 4k context: 17.5 ppl, 3.6 days — 0.7 better perplexity, 30% faster
        (1.3x) than the 1k Megatron baseline
Owner:  FlashAttention paper, Table 4 / §4.2
Scope:  8×A100 GPUs; 4x the context length still beats the shorter-context baseline on speed

Figure: Long-document classification lift — MIMIC-III: 16K seq length (57.1 F1) vs. 512
        (52.8 F1) = +4.3 points; ECtHR: 8K (80.7 F1) vs. 512 (72.2 F1) = +8.5 points; the
        abstract's "6.4 points of lift" is the average of these two deltas ((4.3+8.5)/2=6.4)
Owner:  FlashAttention paper, Table 5 / §4.2 / Abstract
Scope:  Micro-F1, pretrained RoBERTa with repeated positional embeddings; two distinct datasets
        and two distinct best sequence lengths, not one apples-to-apples comparison

Figure: Path-X (seq length 16,384): FlashAttention 61.4% accuracy (first Transformer to beat
        chance). Path-256 (seq length 65,536): dense FlashAttention did not attempt it (✗ in
        Table 6); block-sparse FlashAttention 63.1% (first model to beat chance)
Owner:  FlashAttention paper, Table 6 / §4.2
Scope:  Binary path-connectivity classification benchmark from Long Range Arena; Path-256's
        result specifically requires the approximate (block-sparse), not dense, variant

Figure: Memory footprint (MB) vs. sequence length, FlashAttention: 128→22, 256→44, 512→104,
        1024→209, 2048→418, 4096→836, 8192→1672, 16384→3344, 32768→6688, 65536→13376.
        Standard PyTorch attention over the same range: 128→36, 256→104, 512→336, 1024→1184,
        2048→4416, 4096→17024, then out of memory (no entry beyond 4096)
Owner:  FlashAttention paper, Appendix E.6, Table 21 ("Memory usage (MB) ... by sequence
        length")
Scope:  Combined forward+backward pass, no dropout/no masking, 8 heads, head dim 64, batch 16,
        one A100 (40GB); this is the exact numeric series behind the "grows linearly" claim
        and behind Figure 3 (right)'s plot — see Source assets below

Figure: "up to 20x more memory efficient than exact attention baselines"; "2x more efficient
        than Linformer" at 64K
Owner:  FlashAttention paper §4.3 "Memory Footprint"
Scope:  Comparing FlashAttention's linear memory curve (Table 21 above) against other exact
        and approximate baselines' curves in the same Table 21/Figure 3 series

Figure: FlashAttention-2 reaches 50-73% of theoretical max FLOPs/s on A100 (vs. 25-40% for v1);
        ~2x speedup over v1; up to 225 TFLOPs/s (72% model FLOPs utilization) in end-to-end
        GPT-style training
Owner:  FlashAttention-2 paper, Abstract / §1
Scope:  A100 GPU; the 225 TFLOPs/s figure is specifically an end-to-end training throughput
        number, not a microbenchmark of the attention op alone

Figure: FlashAttention-3 on H100: 1.5-2.0x speedup over FlashAttention-2; FP16 up to 740
        TFLOPs/s (75% utilization); FP8 close to 1.2 PFLOPs/s; FP8 error 2.6x lower than a
        naive FP8 baseline
Owner:  FlashAttention-3 paper, Abstract
Scope:  H100 GPU specifically (Hopper architecture), not A100; verified against the fetched
        abstract only — I did not obtain and read the full FlashAttention-3 PDF the way I did
        for the 2022 paper, so table-level locators for these numbers (which section/table)
        are not confirmed. See Discarded/limitation note.
```

## Source assets

```text
Asset: FlashAttention paper, Figure 1 (left) — the memory-hierarchy pyramid diagram (GPU SRAM /
       GPU HBM / Main Memory DRAM) with size and bandwidth annotated at each tier (SRAM: 19TB/s,
       20MB; HBM: 1.5TB/s, 40GB; DRAM: 12.8GB/s, >1TB), next to a block diagram of the tiling
       algorithm's outer/inner loop structure over Q, K, V blocks.
Shows: The two-tier (fast/small vs. slow/large) memory picture idea 2 needs to teach, already
       drawn with the exact capacity/bandwidth numbers the lesson wants — this is very close to
       a ready-made version of the diagram idea 2 asks for, from the primary source itself.
Crop: Keep the pyramid and its three tiers with their labeled sizes/bandwidths; the algorithm
      block-diagram half of the same figure is a separate, more complex claim (the tiling loop
      structure) and can be omitted without losing the memory-hierarchy point.

Asset: FlashAttention paper, Figure 2 — bar/line charts of GFLOPs, HBM R/W (GB), and runtime
       (ms) for standard vs. FlashAttention (left); HBM-access-vs-block-size effect on runtime
       (middle); block-sparse speedup vs. sparsity (right), all for the GPT-2 medium A100 config.
Shows: The exact "more FLOPs, less HBM traffic, faster anyway" relationship idea 3 and idea 5
       need — this figure is the single clearest visual evidence for the exact/more-FLOPs
       correction, straight from the paper.
Crop: The left panel (GFLOPs / HBM R/W / Runtime table) alone carries the argument; the middle
      and right panels are about block size and block-sparsity, a level of engineering detail
      the lesson's ideas don't need.

Asset: FlashAttention paper, Appendix E.6, Table 21 (memory usage in MB by sequence length,
       FlashAttention vs. eight baselines including standard PyTorch attention) — full numeric
       series, not just a plot.
Shows: The exact linear-vs-quadratic memory-scaling comparison the commission specifically asked
       whether a chart could be supported from, across sequence lengths 128 through 65,536.
Crop: None needed as a "crop" — this is already a clean numeric table; a chart built from it
      should plot FlashAttention's full 128-to-65536 linear series against standard attention's
      128-to-4096 series (it goes out of memory beyond that), to show both the linear curve and
      the point where the quadratic baseline breaks.

Asset: FlashAttention paper, Figure 3 (right) — "Attention Memory Usage," log-scale plot of
       memory footprint vs. sequence length for FlashAttention, block-sparse FlashAttention,
       PyTorch attention, Megatron attention, Linformer, and OpenAI sparse attention, with the
       20x and 2x crossover gaps annotated directly on the chart.
Shows: The same relationship as Table 21 but as the paper's own rendered chart, with the
       "crossover points" and efficiency-multiple call-outs already drawn in.
Crop: If used as a reproduction reference rather than redrawing from Table 21, keep only the
      right-hand memory panel — the left-hand runtime panel answers a different question
      (speed, not memory) and would crowd a single chart with two claims.

Asset: NVIDIA A100 architecture whitepaper, Table 4 (p.36) — "Comparison of NVIDIA Data Center
       GPUs" (P100/V100/A100 across SM count, cores, memory size, bandwidth, and more).
Shows: The generational memory-bandwidth growth (703 MHz → 877.5 MHz → 1215 MHz DDR; SMs 56 →
       80 → 108) that could anchor a reader's sense of "why the newer chip changed the
       bottleneck," if the lesson wants a comparison point beyond the single A100 snapshot.
Crop: The Memory Interface / Memory Size / Memory Data Rate rows alone would carry this point;
      the compute-throughput rows (TFLOPS by precision) are a different, unrelated argument.
```

## Discarded

```text
URL: https://docs.pytorch.org/docs/stable/generated/torch.nn.functional.scaled_dot_product_attention.html
     — attempted fetch returned only a redirect notice with no substantive page content; could
     not verify anything from it, so nothing from this URL is cited. Superseded by the PyTorch
     blog post (pytorch.org/blog/out-of-the-box-acceleration/), which was read in full and
     covers the same integration with more detail and dated context.

URL: https://arxiv.org/html/2205.14135 and https://arxiv.org/html/2307.08691 (arXiv HTML
     renderings, accessed via an intermediate small-model summarization tool) — used only as a
     first pass to orient the search before reading the primary sources directly. Every figure
     initially surfaced this way was re-verified against either the actual FlashAttention v1
     PDF (read page-by-page above) or the FlashAttention-2 paper's own quoted abstract text; no
     claim in this record rests on the summarization pass alone.
```

## Limitations and unresolved items to flag to the orchestrator

- **FlashAttention-3's full text was not read.** Unlike the 2022 paper (read as a complete PDF,
  all sections and appendices) and the 2022 A100 vendor documents (read as extracted PDF text),
  FlashAttention-3's numbers here come from its arXiv abstract only, via a WebFetch summarization
  pass, because a direct PDF download/extraction pass was not run for it in this session. The
  headline numbers (1.5-2.0x, 740 TFLOPs/s, 1.2 PFLOPs/s, 2.6x lower FP8 error) are consistent
  across two independent web searches and the abstract fetch, so I'm confident they're accurate,
  but I cannot give the writer a section/table locator inside the FlashAttention-3 paper the way
  I can for the other two papers, and I did not verify the paper's own exactness language
  (beyond the abstract's title/framing) the way I verified it word-for-word in v1 and v2. If the
  writer wants to quote FlashAttention-3 on the exact-vs-approximate distinction specifically
  (as opposed to citing its speed numbers), that passage should be located and read before
  publication.
- **FlashAttention-3 author affiliations are not confirmed.** I have the author list (Shah,
  Bikshandi, Zhang, Thakkar, Ramani, Dao) but did not independently verify each author's
  institutional affiliation from the paper itself; the lesson doesn't need this for its five
  ideas, so I did not chase it further, but flagging it in case the writer wants to name
  affiliations.
- **The commission's idea 1 wants "one real sequence length and show the resulting table size."**
  The paper's own worked dimensions (N=1024, d=64, from its GPT-2 example in §2.2) are verified,
  but the *byte size* of the resulting matrix is my own arithmetic on those numbers, not a figure
  the paper states directly — flagged clearly in the Numbers section above so it isn't presented
  to the reader as a quoted paper figure.
- **Nothing in this record undermines the commissioned angle.** If anything, the primary source
  makes the correction (idea 5) more sharply than a paraphrase would: the paper's own FLOPs table
  shows FlashAttention using *more* compute, not less, which is a stronger and more concrete
  rebuttal of "fewer FLOPs" than a general exactness claim alone would be.
