# Evidence: the-instruments / model-flops-utilization

Every source below was opened and read. Every URL returned HTTP 200 on a live
check (2026-09-09). github.com was avoided (blocked egress); all primaries are
arXiv or official vendor documentation. Floor met: 8 sources, 6 primary, 2
secondary.

## Source list

### S1 (primary) — Google Research · "PaLM: Scaling Language Modeling with Pathways" (Chowdhery et al., 2022)
URL: https://arxiv.org/abs/2204.02311 (read full text via ar5iv HTML mirror)
Facts it supports:
- Coins and defines **Model FLOPs Utilization (MFU)**: "the ratio of the observed
  throughput (tokens-per-second) relative to the theoretical maximum throughput
  of a system operating at peak FLOPs. Crucially, the 'theoretical maximum'
  throughput only accounts for the required operations to compute the
  forward+backward passes, and not rematerialization."
- Defines **Hardware FLOPs Utilization (HFU)** as the ratio of FLOPs actually
  observed on a device to its theoretical peak, including rematerialization
  (activation recompute).
- **PaLM 540B: MFU = 46.2%, HFU = 57.8%** (Table 3). The HFU exceeds the MFU
  because rematerialization does extra hardware FLOPs that are not model FLOPs.
- **Observed throughput: 238.3K tokens/sec** for PaLM 540B (batch size 2048).
- Trained on **6144 TPU v4 chips** across two TPU v4 Pods.
- Model FLOPs per token counted as ~6N for a dense Transformer, plus an attention
  term (paper's Appendix B), which is why the exact figure is 46.2% rather than
  the ~45.7% the bare 6N estimate gives.

### S2 (primary) — OpenAI · "Scaling Laws for Neural Language Models" (Kaplan et al., 2020)
URL: https://arxiv.org/abs/2001.08361 (read full text via ar5iv HTML mirror)
Facts it supports:
- The **6-FLOPs-per-parameter-per-token** estimate. Quote: "Accounting for the
  backwards pass (approximately twice the compute as the forwards pass), we then
  define the estimated non-embedding compute as C ≈ 6N floating point operators
  per training token."
- Forward pass alone: "C_forward ≈ 2N + 2·n_layer·n_ctx·d_model add-multiply
  operations" (~2N per token, section 2.1).
- Non-embedding parameter count N ≈ 12·n_layer·d_model² (Table 1), deliberately
  excluding embeddings for cleaner scaling.

### S3 (primary) — NVIDIA · "NVIDIA H100 Tensor Core GPU" product/specs page
URL: https://www.nvidia.com/en-us/data-center/h100/
Facts it supports (H100 SXM, peak per GPU, headline figures shown **with
sparsity**, marked by "* With sparsity"):
- **FP16 / BF16 Tensor Core: 1,979 teraFLOPS** (with sparsity) → dense ≈ 989.5.
- **FP8 Tensor Core: 3,958 teraFLOPS** (with sparsity) → dense ≈ 1,979.
- **TF32 Tensor Core: 989 teraFLOPS** (with sparsity).
- **FP64: 34 teraFLOPS.**
- INT8 Tensor Core: 3,958 TOPS.
- Dense = one-half the sparse headline. So on ONE H100 the fp8-with-sparsity
  headline (3,958) is 4x the dense bf16 peak (~990): the denominator's range.

### S4 (primary) — NVIDIA / Microsoft · "Reducing Activation Recomputation in Large Transformer Models" (Korthikanti et al., 2022)
URL: https://arxiv.org/abs/2205.05198 (read full text via ar5iv HTML mirror)
Facts it supports:
- Independent definition of MFU and HFU: MFU is model FLOPs per second divided by
  the accelerator's theoretical peak FLOPs per second; HFU counts the extra
  hardware FLOPs of recomputation.
- Model FLOPs per iteration formula: 72·B·L·s·h²·(1 + s/6h + v/12hL).
- **530B GPT model on 2240 A100 GPUs: MFU = 56.0%, HFU = 57.0%** (Table 5); a
  data-parallel configuration reports **54.2% MFU**.
- Per-GPU peak used: **A100 = 312 teraFLOP/s** (bf16), footnote 5. Different peak
  from the H100, so MFU across chip generations is not a like-for-like capability
  comparison.

### S5 (primary) — DeepMind · "Training Compute-Optimal Large Language Models" (Chinchilla; Hoffmann et al., 2022)
URL: https://arxiv.org/abs/2203.15556 (read full text via ar5iv HTML mirror)
Facts it supports:
- Corroborates the 6ND estimate: "FLOPs(N,D) ≈ 6ND" (Appendix F), backward pass
  twice the forward, multiply-accumulate counted as 2.
- Table A4: the 6ND approximation vs a detailed FLOP count stays within a ratio
  of 0.99–1.10 across model sizes — the estimate is accurate to ~10%.

### S6 (primary) — Google Cloud · "TPU v4" system-architecture documentation
URL: https://docs.cloud.google.com/tpu/docs/v4
Facts it supports:
- **Peak compute per TPU v4 chip: 275 teraflops (bf16 or int8).** This is the
  denominator per chip for the PaLM worked example: 6144 × 275 TFLOP/s = 1.69
  ExaFLOP/s aggregate peak.

### S7 (secondary) — EleutherAI · "Transformer Math 101" (Anthony, Biderman, Hoang, 2023)
URL: https://blog.eleuther.ai/transformer-math/
Facts it supports:
- The compute estimate in explainer form: "C ≈ τT = 6PD" (6 FLOPs per parameter
  per token).
- The peak-is-never-reached point: "While GPU accelerator whitepapers usually
  advertise their theoretical FLOPs, these are never met in practice (especially
  in a distributed setting!)."
- A concrete achieved figure: "GPT-NeoX achieves 150 TFLOP/s/A100 with normal
  attention and 180 TFLOP/s/A100 with Flash Attention" against an A100 peak of
  312 — i.e. roughly 48–58% of peak.

### S8 (secondary) — Epoch AI · "Estimating training compute of Deep Learning models"
URL: https://epoch.ai/blog/estimating-training-compute
Facts it supports:
- Confirms the forward/backward 2x relation ("peak performance numbers of GPU
  specs usually consider a FMA as 2 FLOP").
- Utilization guidance and observed range: "We suggest using a utilization rate
  of 0.3 for large language models"; observed utilization "between 30% and 75%"
  (single GPU), OpenAI's "utilization of 33%" for multi-GPU, and "between 43% and
  52%" in distributed-system research. Anchors the typical MFU band and confirms
  peak is a ceiling, not an operating point.

## Worked numbers verified against sources

**PaLM MFU, reproduced from the parts (S1, S2, S6):**
- Model FLOPs per token ≈ 6N = 6 × 540e9 = 3.24e12.
- Achieved model FLOP/s = 238,300 tok/s × 3.24e12 = 7.72e17.
- Aggregate peak = 6144 × 275e12 = 1.6896e18.
- MFU = 7.72e17 / 1.6896e18 = 0.457 ≈ 46%. Paper reports 46.2% (its numerator
  adds the attention FLOPs term). The bare 6N estimate reproduces the reported
  figure to within a few tenths of a percent.

**Denominator range on one H100 (S3):**
- Dense bf16 peak ≈ 989.5 TFLOP/s; fp8-with-sparsity headline = 3,958 TFLOP/s.
- Ratio = 4.0x. A run honestly at ~47% MFU against the dense bf16 peak reads
  ~12% (47/4) if someone divides the same achieved FLOPs by the 3,958 headline.
  Same silicon, same run; only the spec-sheet line changed.

## Notes / limits
- Google's TPU v4 benchmarking PDF (services.google.com/fh/files/blogs/
  tpu_v4_benchmarking.pdf) resolved but its text did not extract cleanly, so it
  was NOT cited. The 275 TFLOP/s figure is taken instead from the official Google
  Cloud TPU v4 docs (S6), which state it plainly.
- No claim rests on an unopened source. Every figure above was read in the cited
  document.
