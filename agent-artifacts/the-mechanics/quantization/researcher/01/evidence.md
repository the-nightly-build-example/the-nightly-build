# Evidence record: the-mechanics/quantization (01)

The evidence supports the commission's causal chain firmly. Weights live as 16-bit
numbers; quantization rounds each to a coarser integer grid; the per-weight error is
tiny but there are billions of weights; and the measured cost is small at 8-bit,
modest at 4-bit under good schemes, and catastrophic when a naive scheme meets the
large-magnitude outlier features that emerge at scale. Every degradation figure below
was verified against the primary that owns it by reading the paper's own tables, not a
summary. Two independent primaries fix the memory example (OPT/GPT-3-175B at 326-350 GB
in FP16; a 7B model dropping from 13.0 GB to 3.80 GB at 4-bit). The one place the
commission's wording needs sharpening: "usually cheap" holds only for good schemes down
to about 4 bits. Naive round-to-nearest is not cheap at scale (it collapses entirely at
3-bit for a 175B model), and below 4 bits even good schemes lose real accuracy. That
refines the angle rather than breaking it, because the commission already asks why it
sometimes costs a lot. The record is thin on the mechanistic *cause* of outlier
features: the primaries establish that they emerge and where, and offer partial
accounts (a phase shift at 6.7B parameters; a link to attention attending to delimiter
tokens), but no source closes the question of why they arise, which is exactly the part
the lesson should mark as open.

## Sources

```text
URL:         https://arxiv.org/abs/2208.07339
Kind:        primary. The paper that established outlier-aware 8-bit inference
             (LLM.int8(), Dettmers, Lewis, Belkada, Zettlemoyer, NeurIPS 2022). It owns
             the outlier-feature finding and the C4 8-bit degradation table. Read in
             full from the NeurIPS proceedings PDF
             (proceedings.neurips.cc/paper_files/paper/2022/file/c3ba4962c05c49636d4c6206a97e9c8a-Paper-Conference.pdf).
Establishes: (a) 8-bit made lossless up to 175B by isolating outliers into 16-bit while
             >99.9% of values stay in 8-bit; ~50% memory reduction (BLOOM-176B footprint
             cut 1.96x). (b) Large-magnitude outlier features emerge suddenly between 6B
             and 6.7B parameters; at 6.7B all layers and ~75% of sequence dimensions are
             affected. (c) Magnitudes up to 20x larger than other dimensions;
             ~150,000 outliers per 2048-token sequence concentrated in at most 7 feature
             dimensions (|O| <= 7 up to 13B). (d) Zeroing the outlier dimensions cuts
             top-1 attention softmax mass by >20% and degrades validation perplexity by
             600-1000%, though they are only ~0.1% of features; zeroing the same count
             of random features costs <=0.3% probability and ~0.1% perplexity. (e) The
             exact outlier criterion. (f) LLM.int8() saves memory but does not speed up
             inference (same runtime as FP16, sometimes slower below 6.7B).
Paraphrase:  A model's activations carry a handful of feature dimensions whose values
             are far larger than the rest. These appear only past ~6.7B parameters, sit
             in fewer than seven dimensions, and dominate the model's predictions.
             Quantizing a whole tensor with a single scale lets one such outlier stretch
             the range and crush the precision of everything else, so accuracy collapses
             at scale. LLM.int8() pulls the outlier dimensions out into a 16-bit
             multiply and keeps the other 99.9% in 8-bit, recovering full-precision
             quality with no degradation up to 175B. The paper defines an outlier
             feature precisely: a hidden dimension holding at least one value of
             magnitude >= 6.0, in the same dimension across at least 25% of layers, and
             in at least 6% of sequence positions.
Locators:    Abstract and Section 1 (emergence, 20x, 150k/6 dims, softmax and perplexity
             effects). Section 3.2 (threshold alpha = 6.0; |O| <= 7). Section 3.4 and
             Table 1 (C4 perplexities). Section 4.1 (formal outlier criterion). Figure 1
             (zero-shot accuracy vs scale). Figure 3 (phase shift). Section 3.4 last
             paragraph (runtime).
Quote:       "large features with magnitudes up to 20x larger than in other dimensions
             first appear in about 25% of all transformer layers ... At around 6.7B
             parameters, a phase shift occurs, and all transformer layers and 75% of all
             sequence dimensions are affected by extreme magnitude features. These
             outliers are highly systematic: at the 6.7B scale, 150,000 outliers occur
             per sequence, but they are concentrated in only 6 feature dimensions across
             the entire transformer." "we find that alpha = 6.0 is sufficient to reduce
             transformer performance degradation close to zero."
```

```text
URL:         https://arxiv.org/abs/2210.17323
Kind:        primary. GPTQ (Frantar, Ashkboos, Hoefler, Alistarh, 2022; ICLR 2023). It
             owns the 4-bit and 3-bit post-training weight-quantization figures for the
             OPT and BLOOM families and the single-GPU memory claim. Read in full from
             the ETH-hosted PDF (htor.inf.ethz.ch/publications/img/2023_iclr_gptq.pdf).
Establishes: (a) The concrete memory figure: "the parameters of GPT3-175B occupy 326GB
             of memory (counting in multiples of 1024) when stored in an already-compact
             float16 format," exceeding a single GPU. (b) 4-bit and 3-bit weight
             quantization of 175B-class models with negligible perplexity loss under
             GPTQ, and catastrophic loss under round-to-nearest (RTN) at 3-bit. (c) The
             deployment payoff: OPT-175B at 3-bit takes ~63 GB and fits one 80GB A100,
             versus 5x 80GB GPUs for FP16 and 3x for 8-bit LLM.int8(). (d) A full
             degradation-versus-bits-versus-scale series (Tables 2 and 4). (e) End-to-end
             speedups from weight-only 3-4 bit of ~2x on A100 and ~4x on A6000 in this
             version (see Contradictions on version drift). (f) GPTQ names LLM.int8()'s
             finding: "activation outliers in a few feature dimensions break the
             quantization of larger models."
Paraphrase:  Storing GPT-3-scale weights in 16-bit needs 326 GB, more than one GPU
             holds. Rounding each weight to the nearest 4-bit level (RTN) works at 8-bit
             but falls apart lower down; at 3-bit on OPT-175B, RTN perplexity explodes to
             tens of thousands while GPTQ, which uses second-order information to
             compensate each rounding decision, loses only a few tenths of a point.
             GPTQ's 3-bit OPT-175B fits inside a single 80GB A100 at about 63 GB.
Locators:    Section 1 (326 GB). Table 4 (OPT-175B and BLOOM-176B WikiText2/PTB/C4/
             LAMBADA at 16/4/3 bit). Table 2 (OPT family PTB, 125M-175B). "Practical
             Speedups" paragraph, Section 4 (63 GB, single 80GB A100, 5x/3x GPU
             comparison). Abstract (speedups; four GPU hours).
Quote:       "the parameters of GPT3-175B occupy 326GB of memory (counting in multiples
             of 1024) when stored in an already-compact float16 format." "quantized to 3
             bits, this model takes approximately 63GB of memory ... we can actually fit
             the entire quantized model into a single 80GB A100 GPU ... For reference,
             standard FP16 execution requires 5x80GB GPUs, and the state-of-the-art 8-bit
             LLM.int8() quantizer requires 3 such GPUs."
```

```text
URL:         https://arxiv.org/abs/2306.00978
Kind:        primary. AWQ (Lin, Tang, Tang, Yang, et al., MLSys 2024, Best Paper). It
             owns the clean 4-bit and 3-bit weight-only perplexity series on real Llama
             models and the "protect the salient 1%" result. Read in full from the arXiv
             PDF.
Establishes: (a) 4-bit is modest on real models: Llama-2-7B WikiText2 perplexity rises
             from 5.47 (FP16) to 5.60 (AWQ INT4, group-128), +0.13; Llama-2-13B 4.88 ->
             4.97; Llama-2-70B 3.32 -> 3.41. (b) 3-bit costs meaningfully more:
             Llama-2-7B 5.47 -> 6.24 (AWQ INT3), about +14%. (c) The salient-weight
             finding: keeping only the top ~0.1-1% of weight channels (chosen by
             activation magnitude, not weight magnitude) in FP16 recovers most of the
             loss; OPT-6.7B INT3-g128 RTN 23.54 -> 11.39 with 1% kept, near FP16 10.86.
             (d) Group/per-channel scaling is the hardware-friendly substitute for
             mixed precision: scaling salient channels before rounding reduces their
             relative error, with group size 128 used throughout. (e) Task-level, not
             just perplexity: 4-bit gives ~4x smaller models with near-lossless behavior
             on many benchmarks, but 3-bit can collapse a task (OpenFlamingo-9B COCO
             CIDEr drops -16.9 at INT3 for RTN/GPTQ versus -1.17 for AWQ at INT4).
Paraphrase:  Not all weights matter equally. A tiny fraction, identifiable from which
             channels see the biggest activations, carry most of the model's behavior.
             Protect those (by keeping them precise or by scaling them up before
             rounding, applied per small group of weights) and 4-bit weight-only
             quantization on Llama-2 costs about a tenth of a perplexity point. Drop to
             3-bit and the cost grows several-fold, and specific tasks can fall much
             further than perplexity alone suggests.
Locators:    Abstract and Section 3.1 (salient 1%). Table 1 (OPT keep-1% by activation
             vs weight vs random). Table 3 (OPT 3-bit series). Table 4 (Llama-2 and
             LLaMA, INT4-g128 and INT3-g128 WikiText2). Table 5 (Mistral/Mixtral). Table
             6 (OpenFlamingo COCO task drop). Section 5.1 (group size 128 throughout).
Quote:       "Protecting only 1% salient weights can greatly reduce quantization error.
             To identify salient weight channels, we should refer to the activation
             distribution, not weights."
```

```text
URL:         https://arxiv.org/abs/2211.10438
Kind:        primary. SmoothQuant (Xiao, Lin, Seznec, Wu, Demouth, Han, ICML 2023). It
             owns the W8A8 (8-bit weight, 8-bit activation) result and the
             migrate-the-difficulty framing for activation outliers. Read in full from
             the arXiv PDF.
Establishes: (a) An independent confirmation of the memory figure: "the GPT-3 model
             contains 175B parameters, which will consume at least 350GB of memory to
             store and run in FP16, requiring 8x48GB A6000 GPUs or 5x80GB A100 GPUs."
             (b) Weights are easy to quantize; activations are hard because of outliers,
             but the outliers are consistent across tokens per channel, so their
             difficulty can be moved offline into the weights by an equivalent
             per-channel scaling. (c) W8A8 with negligible accuracy loss, up to 1.56x
             speedup and 2x memory reduction, serving a 530B model on one node. (d) A
             stated limit of LLM.int8()'s fix: keeping outliers in FP16 is accurate but
             "hard to implement ... efficiently on hardware accelerators," which is why
             the later schemes avoid mixed precision.
Paraphrase:  The outlier problem is not only about weights. Activations carry the worst
             outliers, and a single scale per tensor wastes most of the integer range on
             them. SmoothQuant divides each outlier-heavy activation channel down and
             multiplies the matching weight channel up by the same factor, an exact
             algebraic swap that leaves the math unchanged but makes both sides easy to
             quantize to 8-bit. It confirms the same root cause as LLM.int8() from the
             activation side and shows the mixed-precision fix has a hardware cost the
             field then worked to avoid.
Locators:    Abstract (W8A8, 1.56x, 2x, 530B). Section 1 (350GB, 8x/5x GPU). Section 1
             and Figure 2 (migrate difficulty; per-channel scaling). Section 1 (mixed
             precision hard on accelerators). Section 3 and Table 2 (O1-O3 settings).
Quote:       "even if activations are much harder to quantize than weights due to the
             presence of outliers ... different tokens exhibit similar variations across
             their channels. Based on this observation, SmoothQuant offline migrates the
             quantization difficulty from activations to weights."
```

```text
URL:         https://github.com/ggml-org/llama.cpp/pull/1684
Kind:        primary. The llama.cpp k-quants pull request (ikawrakow, 2023) and its
             maintained perplexity table: the measurement produced by the tooling that
             actually ships these schemes to on-device users. It owns the
             degradation-versus-bits series people meet in practice (GGUF quant types).
Establishes: The full 7B and 13B degradation-versus-bits series on LLaMA, measured as
             WikiText perplexity against the FP16 baseline, with file sizes. For 7B
             (F16 = 5.9066 ppl, 13.0 GB): Q8_0 near-identical; Q6_K 5.9110 (+0.1%, 5.15
             GB); Q5_K_M 5.9208 (+0.2%, 4.45 GB); Q4_K_M 5.9601 (+0.9%, 3.80 GB); Q4_K_S
             6.0215 (+2.0%, 3.56 GB); Q3_K_M 6.1503 (+4.1%, 3.06 GB); Q3_K_S 6.4571
             (+9.3%, 2.75 GB); Q2_K 6.7764 (+14.8%, 2.67 GB). Same monotone worsening at
             13B (F16 = 5.2543, 25.0 GB; Q4_K_M 5.3002 = +0.9%, 7.32 GB; Q2_K 5.8545 =
             +11.4%, 5.13 GB). The named memory drop: a 7B model falls from 13.0 GB to
             3.80 GB at 4-bit (about 3.4x, an effective ~4.85 bits per weight), which is
             what lets it run on a consumer GPU or laptop.
Paraphrase:  The tool most on-device users run publishes exactly how much quality each
             bit-width costs. Eight-bit is free to two decimal places. Six-bit is within
             0.1%. Four-bit (the recommended default, Q4_K_M) costs under 1% perplexity
             while cutting the 7B file from 13.0 GB to 3.80 GB. Below four bits the cost
             climbs fast: three-bit is a few to nine percent, two-bit near fifteen.
Locators:    PR #1684 description, the LLaMA-7B and LLaMA-13B perplexity/size tables.
             Corroborated by the maintainers' quantization summary in
             github.com/ggml-org/llama.cpp/discussions/2094 (same origin).
Quote:       "6-bit quantized perplexity is within 0.1% or better from the original fp16
             model."
```

```text
URL:         https://arxiv.org/abs/2212.09720
Kind:        primary. "The case for 4-bit precision: k-bit Inference Scaling Laws"
             (Dettmers, Zettlemoyer, ICML 2023). It owns the cross-scale claim about
             where the accuracy-per-bit tradeoff is best. Read from the arXiv abstract
             page.
Establishes: Across more than 35,000 experiments spanning 3-to-8-bit precision and
             19M-to-176B parameters (BLOOM, OPT, NeoX/Pythia, GPT-2), 4-bit precision is
             "almost universally optimal" for the tradeoff between total model bits and
             zero-shot accuracy, and it is hard to improve that tradeoff. What helps most
             is a small block size (independently quantized blocks) and the choice of
             data type (integer vs float). This is the settled-versus-open anchor: 4-bit
             is the sweet spot, and pushing below it loses accuracy per bit.
Paraphrase:  If you fix an accuracy budget and ask which bit-width gives it in the fewest
             total bits, the answer across model families and scales is four. Above four
             you are spending bits you do not need; below four you lose accuracy faster
             than you save memory. Small per-block scales and the numeric format are the
             levers that matter.
Locators:    Abstract (4-bit universally optimal; 35,000 experiments; 3-8 bit; 19M-176B;
             block size and data type).
Quote:       "we find that 4-bit precision is almost universally optimal for total model
             bits and zero-shot accuracy."
```

```text
URL:         https://arxiv.org/abs/2109.12948
Kind:        primary. "Understanding and Overcoming the Challenges of Efficient
             Transformer Quantization" (Bondarenko, Nagel, Blankevoort, EMNLP 2021). An
             earlier primary on where transformer quantization outliers come from,
             relevant only to the open "why do outliers arise" step. Read from the arXiv
             abstract page.
Establishes: Transformer activations carry "structured outliers in the residual
             connections that encourage specific attention patterns, such as attending to
             the special separator token." This predates LLM.int8() and gives a partial
             mechanistic account: the outliers are not noise, they are tied to the model
             using particular dimensions to steer attention toward low-information
             delimiter tokens. It is a partial account, not a settled cause.
Paraphrase:  Even before billion-parameter LLMs, transformer quantization ran into
             activation values that were large, structured, and located in fixed
             dimensions. This work traces some of them to attention machinery: certain
             residual-stream dimensions blow up to make attention park on a separator
             token. That is a candidate reason outliers exist, and it is why the lesson
             can say the effect is real and located but its cause is only partly
             understood.
Locators:    Abstract (structured outliers in residual connections; attention to the
             separator token).
Quote:       "these activations contain structured outliers in the residual connections
             that encourage specific attention patterns, such as attending to the special
             separator token."
```

```text
URL:         https://www.maartengrootendorst.com/blog/quantization/
Kind:        secondary. "A Visual Guide to Quantization" (Maarten Grootendorst, 2024), an
             independent educational explainer with no stake in any of the methods it
             describes. It reports and illustrates the primaries; it does not own any
             claim. Read via the newsletter mirror
             (newsletter.maartengrootendorst.com/p/a-visual-guide-to-quantization).
Establishes: A reader-facing statement of the same mechanics: why weights dominate the
             memory (billions of weights vs millions of biases, so biases are often kept
             higher precision and effort goes to weights); the range-versus-precision
             tradeoff that outliers force ("The major advantage of constraining the
             quantization range is that the quantization error of the non-outliers is
             reduced significantly, however, the quantization error of outliers
             increases"); and plain descriptions of GPTQ and GGUF/block-wise
             quantization. Useful as context and as a model for how to pitch the idea to a
             non-specialist; every load-bearing number in the article still traces to a
             primary above.
Paraphrase:  An outside educator lays out the same picture the primaries establish:
             fewer bits means a coarser grid, outliers force a bad choice between clipping
             them (hurting the outliers) or spanning them (hurting everything else), and
             practical tools quantize weights in small blocks. It confirms the framing is
             not idiosyncratic to the method authors.
Locators:    Sections on memory motivation, calibration/clipping tradeoff, GPTQ, and
             GGUF.
Quote:       "the quantization error of the non-outliers is reduced significantly,
             however, the quantization error of outliers increases."
```

## Contradictions

The primaries agree with each other on the substance; the tensions worth flagging are
between the evidence and loose framings, plus small within-source and cross-version
discrepancies.

- Against "usually cheap" as an unqualified claim. Cheapness is a property of good
  schemes at >= 4 bits, not of quantization in general. Naive round-to-nearest is
  catastrophic exactly where the model is large: GPTQ Table 4 gives OPT-175B WikiText2
  at 8.34 (FP16), 8.37 (GPTQ 4-bit), but 7.3e4 (RTN 3-bit); RTN 4-bit is already 10.54.
  LLM.int8() Table 1 shows Int8 absmax at 13B is 19.08 versus a 12.45 baseline, worse
  than absmax at 6.7B (14.59), i.e. naive 8-bit degradation grows with scale. And below
  4 bits even good schemes lose real ground (AWQ Llama-2-7B 5.47 -> 6.24 at 3-bit;
  llama.cpp Q2_K +14.8%). The commission anticipates this in its "sometimes costs a lot"
  step, so the evidence sharpens the angle rather than opposing it.

- Perplexity can understate task damage at low bits. AWQ Table 6: OpenFlamingo-9B COCO
  CIDEr falls -16.9 at INT3 (RTN and GPTQ) versus -1.17 for AWQ at INT4. A lesson that
  leans only on perplexity would undersell how bad 3-bit can get on a real task.

- Within AWQ, an unexplained number gap. Figure 2's caption reports OPT-6.7B INT3-g128
  RTN perplexity of 43.2 (recovered to 13.0 by keeping 1% salient in FP16), while Table
  1 and Table 3 report RTN 23.54 for what is described as the same INT3-g128 setting.
  Use the table values (23.54 -> 11.39), which are the reproducible experimental numbers;
  treat the 43.2 -> 13.0 pair as an illustrative figure caption.

- GPTQ speedup figures drift by version. The version read here (arXiv v1) states
  end-to-end speedups of "around 2x" on A100 and "4x" on A6000 (abstract and Section 1,
  "1.9-4x"). Search summaries and a later abstract circulate "3.25x / 4.5x." If the
  lesson cites a speedup, cite the version. Speed is also not the same win as memory:
  LLM.int8() explicitly saves memory with no speedup (same runtime as FP16, sometimes
  slower below 6.7B), whereas GPTQ/AWQ deliver speed from smaller weight transfers. The
  "faster" in the commission's opening behavior comes from the weight-only 4-bit tools,
  not from 8-bit LLM.int8().

## Numbers

```text
Figure: GPT-3/OPT-175B FP16 footprint = 326 GB (counting in 1024s); ">= 350GB" decimal
Owner:  GPTQ (326 GB, Section 1); SmoothQuant (350 GB, Section 1) as independent check
Scope:  175B parameters x 16 bits; whole-model weights. FP16 needs 5x 80GB A100.
```

```text
Figure: OPT-175B WikiText2 perplexity by bits: 8.34 (FP16) / 8.37 (GPTQ 4b) / 8.68
        (GPTQ 3b) / 8.45 (GPTQ 3b, group-1024) / 10.54 (RTN 4b) / 7.3e4 (RTN 3b)
Owner:  GPTQ, Table 4
Scope:  OPT-175B, WikiText2 perplexity, lower is better. RTN = naive round-to-nearest.
```

```text
Figure: OPT-175B 3-bit memory = ~63 GB, fits one 80GB A100 (vs 5x for FP16, 3x for 8-bit)
Owner:  GPTQ, "Practical Speedups", Section 4
Scope:  3-bit weights + FP16 embeddings/output + ~9 GB KV cache at 2048 tokens.
```

```text
Figure: LLM.int8() C4 validation perplexity, 32-bit vs Int8 absmax vs LLM.int8(),
        by model size (125M / 1.3B / 2.7B / 6.7B / 13B):
          32-bit Float:          25.65 / 15.91 / 14.43 / 13.30 / 12.45
          Int8 absmax (naive):   87.76 / 16.55 / 15.11 / 14.59 / 19.08
          Int8 absmax vec-wise:  35.84 / 16.82 / 14.98 / 14.13 / 16.48
          Absmax LLM.int8():     25.83 / 15.93 / 14.44 / 13.24 / 12.45
Owner:  LLM.int8(), Table 1
Scope:  C4 validation perplexity, lower is better. Naive 8-bit at 13B (19.08) is worse
        than at 6.7B (14.59); LLM.int8() matches the 32-bit baseline (12.45) at 13B.
```

```text
Figure: Effect of zeroing outlier feature dimensions: top-1 attention softmax mass
        -20%+, validation perplexity +600-1000%, from ~0.1% of features.
        Control (same count of random features): <=0.3% probability, ~0.1% perplexity.
Owner:  LLM.int8(), Abstract / Section 1 / Section 4.2
Scope:  6.7B-13B transformers; outliers = at most 7 feature dimensions.
```

```text
Figure: Outlier emergence: magnitudes up to 20x other dims; ~150,000 per 2048-token
        sequence in <=7 dimensions; sudden phase shift between 6B and 6.7B parameters
        (then all layers, ~75% of sequence positions affected).
Owner:  LLM.int8(), Abstract / Figure 3 / Section 4
Scope:  Criterion for an outlier feature: magnitude >= 6.0, in >=25% of layers, in >=6%
        of sequence positions.
```

```text
Figure: Llama-2 WikiText2 perplexity, FP16 vs AWQ, INT4-g128 and INT3-g128 (7B/13B/70B):
          FP16:          5.47 / 4.88 / 3.32
          AWQ INT4-g128: 5.60 / 4.97 / 3.41
          AWQ INT3-g128: 6.24 / 5.32 / 3.74
          RTN INT4-g128: 5.73 / 4.98 / 3.46   (naive baseline, for contrast)
Owner:  AWQ, Table 4
Scope:  WikiText2 perplexity, lower is better. 4-bit costs ~+0.13 on 7B; 3-bit ~+0.77.
```

```text
Figure: Salient-weight recovery, OPT INT3-g128 WikiText: RTN vs keep-1%-FP16 vs AWQ
          OPT-6.7B: FP16 10.86 / RTN 23.54 / keep-1% 11.39 / AWQ 11.39
          selecting the 1% by weight magnitude instead of activation: 22.37 (no help)
Owner:  AWQ, Table 1 and Table 3
Scope:  Shows the fix is protecting activation-salient channels, not any 1%.
```

```text
Figure: llama.cpp k-quant degradation-vs-bits, LLaMA-7B (perplexity / file size /
        %-vs-F16). Full series for a chart:
          F16    5.9066 / 13.0 GB / baseline
          Q6_K   5.9110 / 5.15 GB / +0.1%
          Q5_K_M 5.9208 / 4.45 GB / +0.2%
          Q4_K_M 5.9601 / 3.80 GB / +0.9%
          Q4_K_S 6.0215 / 3.56 GB / +2.0%
          Q3_K_M 6.1503 / 3.06 GB / +4.1%
          Q3_K_S 6.4571 / 2.75 GB / +9.3%
          Q2_K   6.7764 / 2.67 GB / +14.8%
Owner:  llama.cpp k-quants, PR #1684
Scope:  WikiText perplexity, lower is better; 8-bit (Q8_0) is within rounding of F16.
        13B mirrors this (F16 5.2543 -> Q4_K_M 5.3002 = +0.9% -> Q2_K 5.8545 = +11.4%).
```

```text
Figure: Named on-device memory drop: LLaMA-7B 13.0 GB (F16, ~16 bpw) -> 3.80 GB
        (Q4_K_M, ~4.85 effective bpw), about 3.4x. Clean arithmetic: 6.7B x 4 bits / 8
        = 3.35 GB.
Owner:  llama.cpp k-quants, PR #1684 (measured sizes)
Scope:  The 4-bit size is what fits a 7B model on a consumer GPU / laptop.
```

```text
Figure: 4-bit is the optimal accuracy-per-total-bit point across 3-8 bit and 19M-176B
        parameters (>35,000 experiments).
Owner:  k-bit Inference Scaling Laws, Abstract
Scope:  Zero-shot accuracy vs total model bits; establishes the low-bit floor framing.
```

## Source assets

```text
Asset: LLM.int8() Figure 1 (OPT mean zero-shot accuracy for WinoGrande, HellaSwag, PIQA,
       LAMBADA vs parameters, three lines: 16-bit baseline, naive 8-bit, LLM.int8()).
Shows: The single clearest picture of the whole lesson: naive 8-bit tracks 16-bit until
       ~6.7B, then falls to near-random, while the outlier-aware method stays on the
       16-bit line to 175B. This is the "same model, weaker answers" behavior made
       visible, with the exact scale where it starts.
Crop:  Keep all three lines, the x-axis parameter scale, and the "emergence of outlier
       features" marker at 6.7B. Do not crop out the divergence point.
```

```text
Asset: LLM.int8() Figure 3(a) (percentage of layers and sequence positions affected by
       outlier features vs model size, with the phase-shift marker).
Shows: The suddenness of the emergence: a near-step from few layers affected to all
       layers around 6.7B. Supports "sometimes it barely matters" (small models) turning
       into "sometimes a lot" (large models).
Crop:  Retain the emergence marker and the y-axis (percent affected). Panel (a) is the
       clean one; panel (b) recasts the same data against perplexity.
```

```text
Asset: llama.cpp PR #1684 perplexity table (7B and 13B by quant type, with file sizes).
Shows: The degradation-versus-bits curve a reader can act on: the near-flat top from
       8-bit through 4-bit and the steepening drop below it. This is the raw data for a
       chart of perplexity (or %-over-FP16) against bits-per-weight or file size.
Crop:  Table, not an image; reproduce the rows, label bits/size axis, cite the PR in the
       caption. Note WikiText perplexity and the FP16 baseline explicitly.
```

```text
Asset: AWQ Figure 2 (three-panel: RTN rounding of a small weight block vs keeping 1%
       salient in FP16 vs scaling salient channels before rounding).
Shows: In one diagram, why a single scale damages large-magnitude values and how
       per-channel scaling protects them without mixed precision. Good for the "what the
       better schemes do" step. Caveat: its printed PPL numbers (43.2 -> 13.0) differ
       from the paper's tables; use the figure for the mechanism, cite Table 3 for the
       numbers.
Crop:  Keep the three panels side by side; the contrast is the point. Do not quote the
       caption's perplexity figures as the headline numbers.
```

```text
Asset: SmoothQuant Figure 2 (activation with an outlier channel stretching the range,
       then the smoothed activation and adjusted weight after migrating difficulty).
Shows: The range-stealing problem and the equivalent-transformation fix from the
       activation side. Optional; only if the lesson chooses to mention that outliers
       hit activations too, which the boundary keeps light.
Crop:  Keep the before/after pair and the "migrate difficulty" arrow.
```

## Discarded

```text
URL: https://arxiv.org/abs/2110.02861 : "8-bit Optimizers via Block-wise Quantization"
     (Dettmers). Retrieved by a wrong arXiv id while looking for outlier-origin work; it
     is about optimizer-state quantization during training, not inference weight
     precision. Out of scope.
URL: https://scispace.com/... and https://www.semanticscholar.org/... LLM.int8() mirror
     pages: aggregator restatements, not the source's own page; superseded by the arXiv
     and NeurIPS primary.
URL: https://medium.com/athina-ai/...gptq... : third-party GPTQ summary; every figure it
     carries traces to the GPTQ primary already read, and it adds no interpretation the
     record needs.
URL: A first WebFetch summary of the GPTQ PDF returned wrong table values (OPT-175B FP16
     WikiText2 as 10.87 and a 42 GB footprint). Discarded in favor of the paper's own
     Table 4 (8.34 FP16) and Section 4 (63 GB), read directly from the PDF. Recorded here
     as a caution: the checked numbers are the table numbers, not the summary's.
```
