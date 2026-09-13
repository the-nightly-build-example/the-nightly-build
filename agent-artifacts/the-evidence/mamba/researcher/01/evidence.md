# Evidence: the-evidence/mamba (01)

The record supports the commission's arc firsthand. The Mamba paper (Gu and Dao,
arXiv:2312.00752) states its mechanism, its trained sizes, and its headline
numbers, and it says its own scale honestly: Section 5 admits the evaluation is
"limited to small model sizes, below the threshold of most strong open source
LLMs." The largest language model the paper actually trained is Mamba-2.8B; the
"Mamba-3B" of the abstract is that same 2.8B model rounded up. The paper's
"matches Transformers twice its size" claim is specifically zero-shot
common-sense reasoning at 2.8B and below, and the evidence that breaks the
"transformer is finished" reading is strong and comes from primaries: a peer
transformer beats a Mamba nearly five times its size at retrieval (Jelassi et
al., arXiv:2402.01032), and the Mamba authors' own follow-up keeps attention
layers because a pure state-space model cannot retrieve well (Dao and Gu,
arXiv:2405.21060). Where the record is thin: I could not open Appendix E.5's raw
throughput tables, so the throughput evidence is the main-text range (4-5×) and
Figure 8 rather than per-batch numbers; and claims about the state of the
frontier in 2026 rest on one secondary (IBM) plus the trajectory of the
primaries, since no primary owns a 2026 census of deployed models.

## Sources

```text
URL:         https://arxiv.org/abs/2312.00752
Kind:        primary — the paper the lesson teaches; Gu and Dao own every claim about Mamba's mechanism, sizes, and reported numbers. Version read: v2 (31 May 2024).
Establishes: What Mamba is and does. Authors: Albert Gu (Machine Learning Department, Carnegie Mellon University) and Tri Dao (Department of Computer Science, Princeton University), equal contribution, listed alphabetically by first name. First posted 1 Dec 2023.
Paraphrase:  Structured state-space models (SSMs) carry a compressed hidden state forward through a linear recurrence h_t = A·h_{t-1} + B·x_t, y_t = C·h_t, instead of re-reading every earlier token the way attention does. Prior SSMs (S4 and its line) kept the parameters (Delta, A, B, C) fixed across time so the recurrence could be recomputed as a convolution for fast parallel training; the paper calls this linear time invariance (LTI). The core change is "selection": make B, C, and the step size Delta functions of the current token (Algorithm 2, "S6"), so the model can choose per token whether to write an input into the state or ignore it. This breaks the convolution equivalence, so the model must run as a recurrence; the paper makes that recurrence fast with a hardware-aware "selective scan" (kernel fusion, a work-efficient parallel scan, and recomputation of intermediate states on the backward pass) that keeps the expanded state in fast GPU SRAM instead of writing it to HBM. The block interleaves no separate attention or MLP: one homogeneous Mamba block, repeated. Trained as a language model with scaling laws up to ~1.3B parameters on the Pile (Chinchilla protocol) and downstream models to 2.8B; also tested on DNA and audio. Section 5 lists limitations itself.
Locators:    Abstract; Sec 1 (Introduction, claims); Sec 2 (SSM background, Eqs 1-4); Sec 3.1-3.4 (selection, Algorithms 1-2, hardware-aware scan, architecture); Sec 3.5 Theorem 1 (gating form); Sec 4.2 and Table 3 (language modeling, downstream); Sec 4.5 and Figure 8 (speed); Sec 5 (Discussion / limitations).
Quote:       "our empirical evaluation is limited to small model sizes, below the threshold of most strong open source LLMs ... It remains to assess whether Mamba still compares favorably at these larger sizes." (Sec 5, Scaling)
```

```text
URL:         https://arxiv.org/abs/2402.01032
Kind:        primary — owns the copying/retrieval-limit finding for state-space models; Jelassi, Brandfonbrener, Kakade, Malach (Harvard) authored the theory and experiments. ICML 2024 (PMLR 235).
Establishes: The strongest evidence against "Mamba matches transformers." Title: "Repeat After Me: Transformers are Better than State Space Models at Copying." It proves and measures a capability gap on copying and retrieval from context, and shows it persists at scale on pretrained Mamba even though Mamba has lower language-modeling perplexity.
Paraphrase:  The authors group Mamba, S4, RNNs, and linear attention as "generalized state space models" (GSSMs): models with a fixed-size state that does not grow with input length. Theory: a depth-2 transformer can copy strings whose length is exponential in its number of heads, by storing and looking up n-grams; a GSSM must fail once the string carries more bits than its state holds (its error exceeds 1/2 when the state memory is below L·log(D) − 1). Experiments from scratch (~160M-parameter models): transformers learn to copy with about 100x fewer training examples than the best GSSM, and generalize to far longer strings while GSSM accuracy drops to zero almost immediately past the training length. Pretrained models (Pythia transformers vs Mamba, both trained on the Pile, matched sizes 410M-2.8B): on a phone-book lookup, even the smallest transformer (410M) beats the largest Mamba (2.8B) once the book is long enough (L >= 70); on copying natural-language strings, the smallest transformer beats the largest Mamba, and with word order shuffled the largest Mamba scores zero at length 300. The gap holds despite Mamba having slightly lower Pile perplexity. Balanced counter-note the paper itself records: on the "prefix-key" lookup variant, which needs only a running summary rather than the whole context, GSSMs generalize perfectly and even beat the NoPE and ALiBi transformers — GSSMs are limited at storing the full context, not at summarizing it.
Locators:    Abstract; Sec 2 Theorem 2.7 and Corollary 2.8 (state lower bound); Sec 3.2 (100x sample efficiency, Figure 1a); Sec 3.3 (length generalization, Figure 1b); Sec 3.5 (prefix vs suffix lookup, Figures 5-6); Sec 4.2-4.3 (pretrained copying and phone-book, Figures 1c, 7).
Quote:       "even the smallest transformer (410M parameters) outperforms the largest GSSMs (2.8B parameters) when the phone-book size is long enough (L >= 70)." (Sec 4.3, Phone-book lookup)
```

```text
URL:         https://arxiv.org/abs/2405.21060
Kind:        primary — the Mamba follow-up; Dao and Gu own Mamba-2 and the hybrid ablation. ICML 2024.
Establishes: That the Mamba authors themselves, one year on, (a) frame the match as "small to moderate scale," (b) speed up the core layer, and (c) find that keeping a small share of attention layers beats a pure state-space model — the retrieval weakness, addressed by putting some attention back.
Paraphrase:  Title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality." The paper connects state-space models and attention through "structured state space duality" (SSD) and derives Mamba-2, whose inner layer is 2-8x faster than Mamba's selective scan and allows an ~8x larger state. Mamba-2 at 2.7B (300B tokens, Pile) outperforms Mamba-2.8B, Pythia-2.8B, and Pythia-6.9B on standard downstream evals. The decisive part for the angle is Section 9.2.3: a hybrid of SSD and attention layers beats both a pure Mamba-2 and a strong transformer (Transformer++), and "around 10% of the total number of layers being attention performs best." At 2.7B, a model with 58 SSD layers and 6 attention layers reaches the best Pile perplexity in their table. The authors' hypothesis is that attention "act[s] as a retrieval mechanism to quickly refer to previous tokens" instead of forcing the model to compress all context into its state — the same weakness Jelassi et al. measured.
Locators:    Abstract; Sec 1 ("small to moderate scale"; Mamba-2-2.7B vs Pythia-6.9B); Sec 9.2.3 and Tables 2-3 (hybrid finding, 10% attention, 2.7B perplexities); Sec 9.3 (2-8x speed).
Quote:       "Empirically we find that having around 10% of the total number of layers being attention performs best. Combining SSD layers, attention layers, and MLP also works better than either pure Transformer++ or Mamba-2." (Sec 9.2.3)
```

```text
URL:         https://arxiv.org/abs/2403.19887
Kind:        primary — for its own architecture and results; Lieber et al. (AI21 Labs) built and released Jamba. Its characterization of Mamba's standing is that team's assessment, weighed as such.
Establishes: That the production answer to "what replaced attention" was a hybrid, not a pure state-space model, and a direct industry statement that pure Mamba still trails size-matched transformers.
Paraphrase:  Title: "Jamba: A Hybrid Transformer-Mamba Language Model." Jamba interleaves Transformer and Mamba layers with mixture-of-experts (MoE); the released model has 12B active and 52B total parameters, fits one 80GB GPU, and supports 256K-token context under an Apache 2.0 license. The implemented configuration uses a 1:7 ratio of attention-to-Mamba layers, with MoE every other layer (16 experts, top-2). AI21 call it "the first production-grade Attention-SSM hybrid model" and report it comparable to Mixtral-8x7B and Llama-2 70B with roughly 3x Mixtral's throughput at long context. Their stated reason for the hybrid, an assessment of Mamba: SSMs like Mamba are more efficient and better at long distances than RNNs "but still lag behind the performance of comparably sized Transformer language models." Note: ablations were run up to 7B parameters and 250B tokens.
Locators:    Abstract; Sec 1 (hybrid rationale, "still lag behind"; "first production-grade Attention-SSM hybrid"; comparisons; 1:7 ratio; ablation scale); Figure 1 (block layout).
Quote:       "Recent state space models (SSMs) like Mamba are more efficient to train than RNNs and are more capable at handling long distance relationships, but still lag behind the performance of comparably sized Transformer language models." (Sec 1)
```

```text
URL:         https://arxiv.org/abs/2111.00396
Kind:        primary — for the lineage Mamba builds on; Gu, Goel, Ré (Stanford) own S4. ICLR 2022. Use only as deep as the mechanism story needs.
Establishes: What "structured state-space model" meant before Mamba, and what property Mamba later removed. S4 = Structured State Space sequence model.
Paraphrase:  A state-space model maps an input signal to an output through a latent state via x'(t) = Ax(t) + Bu(t), y(t) = Cx(t) + Du(t). The earlier LSSL made this work in principle but was impractical (O(N^2·L) time, O(N·L) memory). S4's contribution is a parameterization of the state matrix A (a normal-plus-low-rank decomposition reducing to a Cauchy-kernel computation) that makes the model efficient while keeping its long-range strengths. S4 is time-invariant (LTI) and runs as a convolution. Reported results: 91% on sequential CIFAR-10, generation ~60x faster than transformers, and state-of-the-art on every Long Range Arena task including Path-X (length 16k), which prior models failed. This is the "fixed dynamics, computed as a convolution" model whose LTI constraint Mamba's selection mechanism lifts.
Locators:    Abstract; Sec 1 (LSSL cost O(N^2·L) / O(N·L); LRA and Path-X results).
Quote:       "SoTA on every task from the Long Range Arena benchmark, including solving the challenging Path-X task of length 16k that all prior work fails on." (Abstract)
```

```text
URL:         https://arxiv.org/abs/2410.05355
Kind:        primary — Zuo et al. (Technology Innovation Institute) own Falcon Mamba; cited for how far a pure state-space model actually scaled.
Establishes: The high-water mark for a pure (attention-free) Mamba language model as of late 2024, and that this mark is 7B, not frontier.
Paraphrase:  Title: "Falcon Mamba: The First Competitive Attention-free 7B Language Model." A 7B pure-Mamba model trained on 5.8T tokens. The authors report it as the best Mamba model at that scale, surpassing existing Mamba and hybrid Mamba-Transformer models, surpassing open-weight transformers Mistral 7B, Llama3.1 8B, and Falcon2 11B on standard benchmarks, and on par with Gemma 7B. This shows a pure state-space model can be competitive at 7B on standard (largely short-context reasoning) leaderboards; it does not overturn the copying/retrieval gap, and 7B is well below frontier model scale. Weigh the benchmark "surpasses" claim against the copying/retrieval evidence: it is measured on the same short-context category where Mamba was always competitive.
Locators:    Abstract (title, 7B, 5.8T tokens, comparison models).
Quote:       "the best-performing Mamba model in the literature at this scale, surpassing both existing Mamba and hybrid Mamba-Transformer models."
```

```text
URL:         https://www.ibm.com/think/topics/mamba-model
Kind:        secondary — reputable technical explainer (IBM Think, by Dave Bergmann, Senior Staff Writer, AI Models). Cited only for the present-day framing and the state of the field, which no single primary owns.
Establishes: How Mamba is positioned two years on, and that transformers remained dominant while hybrids, not pure SSMs, are the practical path.
Paraphrase:  IBM calls Mamba "the first competitive alternative to the transformer architecture for autoregressive large language models," and says transformers "have remained the dominant mode of LLM in the 2 years following the release of the original Mamba paper." It names the same capability gaps the primaries prove: transformers "still outpace both Mamba and Mamba-2 on tasks requiring in-context learning (such as few-shot prompting), copying, or long-context reasoning." It states a hybrid "could outperform both pure transformers or SSMs," pointing to IBM's own Bamba / Granite 4.0. It repeats the paper's throughput headline ("5 times greater throughput than equivalent transformers"). No claim that pure SSMs displaced transformers.
Locators:    IBM Think, "What Is A Mamba Model?" (definition; two-years-dominant statement; capability gaps; hybrid paragraph).
Quote:       "transformers still outpace both Mamba and Mamba-2 on tasks requiring in-context learning (such as few-shot prompting), copying, or long-context reasoning."
```

## Contradictions

The commission's angle already holds the tension it wants tested, and the
evidence lands squarely on the skeptical side. Everything below breaks or
qualifies the "the transformer is finished" reading.

1. **A retrieval gap that scale does not close (strongest).** Jelassi et al.
   prove a fixed-state model must fail to copy strings longer than its state,
   and measure it: even a 410M transformer beats a 2.8B Mamba at phone-book
   lookup once the book is long, and transformers learn copying with ~100x
   fewer examples. Crucially this holds even though the Mamba models have lower
   Pile perplexity — so "matches on perplexity" and "matches on what you'd use
   it for" are different claims, and Mamba's headline is the first kind.

2. **The Mamba authors put attention back.** Mamba-2 (same authors) finds a
   hybrid with ~10% attention layers beats both pure Mamba-2 and a strong
   transformer, and attributes the gain to attention's ability to retrieve
   earlier tokens rather than compress everything into the state. This is the
   copying/retrieval weakness of point 1, conceded and patched by the
   architecture's own creators.

3. **The production winner was a hybrid, not a pure SSM.** Jamba (AI21) is a
   Transformer-Mamba hybrid and states plainly that pure Mamba "still lag[s]
   behind the performance of comparably sized Transformer language models."
   IBM's explainer says the same and points to its own hybrid Granite 4.0.

4. **The "matches transformers twice its size" claim is narrow.** In the paper,
   that comparison is zero-shot common-sense reasoning at 2.8B and below:
   Mamba-2.8B averages 63.3 across the reported tasks vs 59.1 for Pythia-2.8B
   (~4 points) and 61.7 for Pythia-6.9B. It is not a long-context, retrieval, or
   frontier-scale claim, and the paper never ran those at language-model scale.
   The paper says its evaluation is "limited to small model sizes, below the
   threshold of most strong open source LLMs."

5. **The throughput advantage is setup-specific, not universal.** The 4-5x is
   inference *generation* throughput, and comes from Mamba having no KV cache so
   it can run much larger batches; the training-time scan only overtakes
   FlashAttention-2 beyond sequence length 2K. Mamba-2 itself notes the whole
   model "might not be as efficient to train as Transformer at short sequence
   length (e.g. at 2K)." So the win is long-sequence, large-batch generation,
   not a blanket speedup.

6. **Counter-evidence that a pure SSM can be competitive at 7B.** Falcon Mamba
   (7B, attention-free) reports beating Mistral 7B and Llama3.1 8B on standard
   leaderboards. This cuts toward Mamba — but on the short-context reasoning
   category where SSMs were already competitive, at 7B, not frontier scale, and
   it does not test or overturn the copying/retrieval gap. Steelman it, then
   weigh it against points 1-3.

7. **The paper's own "No Free Lunch" caveat.** Selection helps discrete data
   (text, DNA) but "can impede ... performance on data that LTI SSMs excel on,"
   and the sole complex-valued audio experiment shows the tradeoff. Mamba is not
   a strict superset of what came before.

Minor internal inconsistencies to keep the writer precise: the paper markets
"Mamba-3B" and "5x throughput" in the abstract, while the trained model is
Mamba-2.8B and Section 4.5 reports the honest range "4-5x." Use 2.8B and 4-5x.

## Numbers

```text
Figure: 5x higher inference throughput (abstract headline); "4-5x higher inference throughput than a Transformer of similar size" (Sec 4.5)
Owner:  Mamba paper (arXiv:2312.00752), Sec 4.5 and Figure 8
Scope:  Inference generation throughput on A100 80GB, prompt length 2048; advantage comes from no KV cache allowing much larger batch sizes; e.g. an (untrained) Mamba-6.9B out-throughputs a Transformer-1.3B (5x smaller). Prefer the 4-5x range over the abstract's rounded "5x."
```

```text
Figure: Selective scan up to 20-40x faster than a standard PyTorch scan; faster than FlashAttention-2 beyond sequence length 2K; hardware-aware algorithm "up to 3x faster on A100 GPUs" vs prior SSM methods
Owner:  Mamba paper, Sec 3.3 / Sec 4.5 / Figure 8 (and Sec 1 for the 3x-vs-prior-methods)
Scope:  Training-time kernel benchmark, state expansion N=16. The 20-40x is against a naive scan; the "faster than FlashAttention-2" crossover is at ~2K sequence length; the 3x is against previous convolution-based SSMs, not against transformers.
```

```text
Figure: Language-model scaling laws to ~1.3B params; downstream models 130M, 370M, 790M, 1.4B, 2.8B; largest LM trained = 2.8B
Owner:  Mamba paper, Sec 4.2, Figure 4, Table 3
Scope:  Pile dataset, Chinchilla protocol; downstream models trained to 300B tokens at context length 2048. No 7B+ language model trained in this paper.
```

```text
Figure: Mamba-2.8B downstream average 63.3; Pythia-2.8B 59.1; Pythia-6.9B 61.7 (~4-point edge over Pythia-2.8B; exceeds Pythia-6.9B)
Owner:  Mamba paper, Table 3 (zero-shot: LAMBADA, HellaSwag, PIQA, Arc-E, Arc-C, WinoGrande averaged)
Scope:  Zero-shot common-sense reasoning, short context. This is the specific evidence behind "matches Transformers twice its size" — not retrieval or long-context.
```

```text
Figure: Selective copying accuracy — S4 (no selection) 18.3%; Mamba (S6) 99.8%; H3+S6 99.7%
Owner:  Mamba paper, Table 1
Scope:  Synthetic selective-copy task; shows selection, not architecture gating, is what solves it.
```

```text
Figure: Induction-heads extrapolation — trained at length 256, generalizes to 1M tokens (~4000x); "no other method goes beyond 2x"
Owner:  Mamba paper, Sec 4.1.2, Table 2
Scope:  Synthetic associative-recall task; attention models tested only to length 16384 due to memory. This is the paper's own recall showcase — read alongside Jelassi et al., whose realistic retrieval tasks show the opposite ranking.
```

```text
Figure: Transformers need ~100x fewer training samples than the best GSSM to learn copying; GSSM length-generalization accuracy falls to ~0 just past training length
Owner:  Jelassi et al. (arXiv:2402.01032), Sec 3.2-3.3, Figure 1a-b
Scope:  From-scratch models ~160M params (LSTM ~40M); string copying, uniform tokens.
```

```text
Figure: State lower bound — a GSSM's copy error exceeds 1/2 once its state memory is below L·log(D) − 1; a depth-2 transformer copies strings of length exponential in its number of heads
Owner:  Jelassi et al., Sec 2, Theorem 2.7 / Corollary 2.8 / Corollary 2.5
Scope:  Representational-capacity theory for the copy task; D = vocabulary size, L = sequence length.
```

```text
Figure: Mamba-2 inner layer 2-8x faster than Mamba's scan, ~8x larger state; hybrid with ~10% attention best; at 2.7B, 58 SSD + 6 attention layers gives best Pile perplexity (5.95) vs pure Mamba-2 (6.09) and Transformer++ (6.13)
Owner:  Dao and Gu (arXiv:2405.21060), Sec 9.2.3 Tables 2-3, Sec 9.3
Scope:  2.7B models, 300B tokens, Pile, GPT-NeoX tokenizer; matched params/hyperparameters. Perplexity differences are small but consistent and the ranking is the point.
```

```text
Figure: Jamba — 12B active / 52B total parameters; 256K context; 1:7 attention-to-Mamba layer ratio; ~3x Mixtral-8x7B throughput at long context
Owner:  Lieber et al. (arXiv:2403.19887), Abstract and Sec 1
Scope:  Released production model (Apache 2.0); ablations to 7B / 250B tokens.
```

```text
Figure: S4 — LSSL cost O(N^2·L) time and O(N·L) memory (the bottleneck S4 removes); ~60x faster generation than transformers; SoTA on all Long Range Arena tasks incl. Path-X (length 16k)
Owner:  Gu, Goel, Ré (arXiv:2111.00396), Abstract and Sec 1
Scope:  Lineage only. N = state dimension, L = sequence length. S4 is time-invariant (convolutional).
```

Worked-example material for the writer (commission direction 5): the core
contrast is compression. The Mamba paper frames it directly — attention "does
not compress context at all" and stores the whole context (the KV cache), which
is why its inference is linear-time and its training quadratic; a recurrent model
has a fixed finite state, so inference is constant-time per step, but its quality
is bounded by how well that state compressed the context (Sec 3.1). "Selective"
is the content-based decision to keep or discard a token as it arrives. The paper
gives the cleanest concrete anchor in Theorem 1: with the state reduced to one
dimension, the selective recurrence becomes exactly an input-controlled gate,
h_t = (1 − g_t)·h_{t-1} + g_t·x_t with g_t = sigmoid(Linear(x_t)) — when g_t is
near 0 the token is ignored, near 1 it overwrites the state. That is a faithful,
real worked example of "selective" at N=1, buildable in plain words.

## Source assets

```text
Asset: Repeat After Me, Figure 1(c) "Lookup with pretrained models" (phone-book accuracy vs book length, Pythia 410M/1.4B/2.8B against Mamba 360M/1.4B/2.8B)
Shows: The single clearest picture of the contradiction — every transformer curve stays high while every Mamba curve collapses as the book grows, and the smallest transformer sits above the largest Mamba.
Crop:  Must retain both model-family legends and the x-axis (phone-book length) so the reader sees the crossover is about context length, not model size. Do not crop out the small-transformer curve.
```

```text
Asset: Mamba, Figure 8 "Efficiency Benchmarks" (Left: training scan speed vs sequence length; Right: inference throughput vs batch size)
Shows: Where the efficiency win is real — the scan overtakes FlashAttention-2 only past ~2K length (left), and throughput pulls ahead at large batch (right).
Crop:  Keep the axis labels and the 2K crossover on the left panel; the honest story is in the crossover, not the endpoint. A bare "5x" pulled from the right panel without the batch-size axis would mislead.
```

```text
Asset: Mamba, Figure 4 "Scaling Laws" (perplexity vs FLOPs on the Pile, Mamba vs Transformer++ and other subquadratic models)
Shows: The defensible core claim — Mamba's curve matches the strong Transformer++ recipe at these small sizes, more so at longer context.
Crop:  Retain the parameter/FLOPs range on the axis so the reader sees the curves stop at ~1.3B; the claim is about small-to-mid scale and the axis says so.
```

```text
Asset: Mamba, Figure 1 (Overview) and Figure 3 (Architecture)
Shows: The mechanism — a single channel's input mapped through a higher-dimensional latent state, and the homogeneous Mamba block that drops separate attention/MLP.
Crop:  Useful only if the lesson goes into the block; for a no-code reader Theorem 1's one-line gate may teach the idea better than the block diagram. Note: house rules require any chart to be a committed script rendered from cited data, so a paper figure cannot be lifted as the article's chart — it can be described, or its underlying comparison rebuilt.
```

## Discarded

```text
URL: https://medium.com/@raktims2210/mamba-selective-state-space-models-and-the-rise-of-post-transformer-ai-... — Medium post; useful as proof the "post-transformer" framing circulates, but self-published and not a reliable secondary; the "post-transformer" discourse is better attributed to the primaries' own hedged language and the IBM explainer.
URL: https://www.ai21.com/blog/rise-of-hybrid-llms/ — AI21 (Jamba's vendor) marketing blog; its substance ("attention was never enough," hybrids win) is already owned by the Jamba paper and IBM, so citing the blog adds vendor framing without new fact.
URL: https://www.sciencedirect.com/science/article/abs/pii/S0952197625012801 (Mamba-360 survey) and https://arxiv.org/abs/2404.09516 (SSM survey) — survey material; good for breadth but every point the lesson needs is owned by a primary above, so a survey would be secondary padding.
URL: https://arxiv.org/abs/2410.03105 (Mamba in Vision survey) — off-topic for a language-modeling lesson.
```
