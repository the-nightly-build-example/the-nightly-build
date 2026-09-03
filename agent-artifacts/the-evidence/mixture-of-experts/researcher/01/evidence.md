# Evidence record: the-evidence/mixture-of-experts (01)

The evidence supports a lesson built on one mechanism and one honesty problem. The mechanism is the Sparsely-Gated Mixture-of-Experts layer of Shazeer et al. 2017: a gating network scores many feed-forward experts, keeps the top few, and computes only those, so parameter count and per-example compute stop moving together. That decoupling is documented firsthand in the paper's own results, where a model with 4.3 billion parameters runs at 8.9 million operations per timestep. The honesty problem follows from it directly. A headline parameter count for a modern MoE model is not the compute a token pays, and three later primaries give exact total-versus-active figures a writer can use to show the gap: Switch Transformer (1.571 trillion parameters at fewer FLOPs per sequence than a dense 11-billion model), Mixtral (47 billion total, 13 billion active), and DeepSeekMoE (16.4 billion total, 2.8 billion active). The record is strong on numbers that each primary owns and on the one clean contradiction between primaries (Shazeer conjectured routing needs more than one expert; Switch routes to one and reports it works better). It is thinner on GShard's translation-quality figures, which rest on a single reading of one results table, and on training stability, which every primary names as unresolved without any of them closing it.

## Sources

```text
URL:         https://arxiv.org/abs/1701.06538
Kind:        primary. It owns the MoE layer, the mechanism, and all its reported figures. Authors are the party that built and measured the system.
Establishes: The Sparsely-Gated Mixture-of-Experts layer and its results. Authors: Noam Shazeer, Azalia Mirhoseini, Krzysztof Maziarz, Andy Davis, Quoc Le, Geoffrey Hinton, Jeff Dean (Google Brain / Google). Submitted 23 January 2017.
Paraphrase:  A layer holds up to thousands of feed-forward experts and a trainable gating network. The output is y = sum over i of G(x)_i * E_i(x), where E_i is expert i and G(x)_i is its gate weight. G(x) is sparse: where a gate weight is zero the expert is not computed, so only a few experts run per example. Gating is Noisy Top-K: score each expert with x*W_g, add tunable Gaussian noise, keep the top k and softmax them, set the rest to minus infinity. Experiments use k=4 for the flat MoE (k=2 per level for the hierarchical variant). Two auxiliary losses, an importance loss and a load loss, each the squared coefficient of variation of per-expert usage, stop the gate from collapsing onto a few experts. The paper credits the origin of the mixture-of-experts idea to earlier work (Jacobs, Jordan, Nowlan, Hinton 1991).
Locators:    Abstract; Section 2 (Eq. 1, the layer); Section 2.1 (Eqs. 2-5, softmax and noisy top-k gating); Section 4 and Appendix A (importance and load losses); Table 1 (1B Word benchmark); Section 5 / Appendix D (100B Word corpus, 137B model); machine-translation tables.
Quote:       "we route to only" is Switch's line, not this paper's. Shazeer's own framing: the layer is "consisting of up to thousands of feed-forward sub-networks" with "up to 137 billion parameters" at "only minor losses in computational efficiency" (abstract).
```

```text
URL:         https://arxiv.org/abs/2006.16668
Kind:        primary. It owns the 600-billion-parameter translation model and its training figures.
Establishes: GShard scaled a Sparsely-Gated MoE Transformer past 600 billion parameters for multilingual translation. Authors: Dmitry Lepikhin, HyoukJoong Lee, Yuanzhong Xu, Dehao Chen, Orhan Firat, Yanping Huang, Maxim Krikun, Noam Shazeer, Zhifeng Chen (Google). Submitted 30 June 2020.
Paraphrase:  Every other feed-forward layer of a Transformer is replaced with a position-wise MoE layer holding 2048 experts. Routing is group-level top-2: each token goes to at most two experts. An expert-capacity threshold caps how many tokens one expert accepts per batch, and an auxiliary loss pushes the token distribution toward uniform so no expert overflows. The 600-billion-parameter model (2048 experts, 36 layers) was trained on 2048 TPU v3 cores in 4 days and reports strong translation quality across 100 languages into English against per-language baselines.
Locators:    Abstract; Section 2.1 (architecture, top-2 gating); Section 2.2 (expert capacity, auxiliary loss l_aux); results table for the MoE(2048E, 36L) model; training-cost figure (2048 TPU v3 cores, 4 days, ~22 TPU v3 core-years).
Quote:       "scale up multilingual neural machine translation Transformer model with Sparsely-Gated Mixture-of-Experts beyond 600 billion parameters" and train it "on 2048 TPU v3 accelerators in 4 days" (abstract).
```

```text
URL:         https://arxiv.org/abs/2101.03961
Kind:        primary. It owns the trillion-parameter Switch models, the top-1 routing claim, and Table 9.
Establishes: Switch Transformer simplifies MoE routing to one expert per token and scales to 1.571 trillion parameters. Authors: William Fedus, Barret Zoph, Noam Shazeer (Google). Submitted 11 January 2021 (v3 revised 16 June 2022).
Paraphrase:  Each token is routed to a single expert (top-1, "Switch routing"), against the earlier belief that more than one expert is needed for usable gradients to the router. The design keeps FLOPs per token roughly constant while growing the parameter count. Training is stabilized by casting the router computation to float32 while keeping bfloat16 elsewhere, by reducing the weight-initialization scale (factor 0.1), and by expert dropout during fine-tuning. A single differentiable load-balancing auxiliary loss with coefficient 0.01 replaces the two losses of Shazeer 2017. Switch-Base at 64 experts reaches T5-Base quality about 7.5x sooner in training steps; Switch-C reaches its scale at lower FLOPs per sequence than dense T5-XXL.
Locators:    Abstract; Section 2.1 (top-1 Switch routing and the argument against k>1); Section 2.2 (load-balancing loss, alpha = 0.01); Section 2.3 / Table 2 (selective float32 precision); Table 4 (expert dropout 0.4); Section 3.1 (7.5x speedup); Table 9 (Switch-XXL, Switch-C, T5-XXL scale and FLOPs).
Quote:       "we instead use a simplified strategy where we route to only a single expert" (Section 2.1). Table 9: Switch-C, 2048 experts, 1571B parameters, 890B FLOPs/seq; Switch-XXL, 64 experts, 395B parameters, 6.3T FLOPs/seq; T5-XXL, 11B parameters, 6.3T FLOPs/seq.
```

```text
URL:         https://arxiv.org/abs/2401.04088
Kind:        primary. Mistral AI's own report on the model it built and released.
Establishes: Mixtral 8x7B, a shipped sparse-MoE language model, with stated total and active parameter counts. Authors: Albert Q. Jiang, Alexandre Sablayrolles, Antoine Roux, Arthur Mensch, and further Mistral AI co-authors. Submitted January 2024.
Paraphrase:  Each layer holds 8 feed-forward experts. A router selects 2 of the 8 per token and sums their outputs. A token has access to 47 billion total parameters but uses only 13 billion of them per token at inference. On reported benchmarks Mixtral matches or beats Llama 2 70B (e.g. MMLU 70.6 vs 69.9; MBPP code 60.7 vs 49.8) at a fraction of the active compute.
Locators:    Abstract (47B / 13B); architecture section (8 experts, top-2 router, Softmax(TopK(x*W_g)) with K=2); benchmark tables vs Llama 2 70B and GPT-3.5.
Quote:       "each token has access to 47B parameters, but only uses 13B active parameters during inference" (abstract).
```

```text
URL:         https://arxiv.org/abs/2401.06066
Kind:        primary. DeepSeek-AI's own report on DeepSeekMoE.
Establishes: DeepSeekMoE 16B, a shipped sparse-MoE model, with stated total and active parameters and two architectural changes to the routing. Authors: Damai Dai, Chengqi Deng, Chenggang Zhao, and further DeepSeek-AI co-authors. Submitted 11 January 2024.
Paraphrase:  Two ideas refine the MoE layer. Fine-grained segmentation splits each expert into m smaller experts (narrower FFN) and activates m times as many, buying far more routing combinations at the same compute. Shared-expert isolation reserves a few experts that every token always uses, to hold common knowledge and cut redundancy in the routed experts. DeepSeekMoE 16B has about 16.4 billion total parameters and about 2.8 billion activated per token; each token uses 2 shared experts plus 6 of 64 routed experts. It reports parity with dense DeepSeek 7B at roughly 40% of the compute, and beats LLaMA2 7B on most listed benchmarks.
Locators:    Abstract; architecture section (fine-grained segmentation, shared-expert isolation); Section 5.1.2 (16.4B total, ~2.8B active, 2 shared + 6-of-64 routed); Section 5.2 / Tables 3-4 (vs DeepSeek 7B and LLaMA2 7B, "about 40%" of computations).
Quote:       "DeepSeekMoE 16B ... achieves comparable performance with LLaMA2 7B, with only about 40% of computations" (abstract).
```

```text
URL:         https://huggingface.co/blog/moe
Kind:        secondary. Hugging Face staff summarizing the MoE literature from outside the authoring teams. Useful for the present-day framing of the total-versus-active confusion, not for owning any figure.
Establishes: A plain statement of why an MoE parameter count misleads, aimed at practitioners. Authors: Omar Sanseviero, Lewis Tunstall, Philipp Schmid, Sourab Mangrulkar, Younes Belkada, Pedro Cuenca. Published 11 December 2023.
Paraphrase:  In a dense model every parameter runs on every input; sparsity means only some of the system runs per token. For Mixtral, the total is 47 billion rather than 8*7 = 56 billion because only the FFN blocks are separate experts and the rest of the model is shared, and per-token inference cost is close to a 12-billion model. It attributes MoE's origin to the 1991 "Adaptive Mixture of Local Experts" and its sparse scaling to Shazeer et al. 2017's 137B LSTM, and notes router z-loss (from ST-MoE) as a later stability fix.
Locators:    Post body: definition and sparsity; the "Why 47B and not 8 x 7B = 56B" paragraph; the history paragraph.
Quote:       "in MoE models, only the FFN layers are treated as individual experts, and the rest of the model parameters are shared." And: "assuming just two experts are being used per token, the inference speed (FLOPs) is like using a 12B model (as opposed to a 14B model)."
```

## Contradictions

- How many experts a token needs. Shazeer et al. 2017 route to k experts with k > 1 (k=4 in the flat MoE) and conjecture that routing to more than one is needed to get useful gradients into the gating network. Switch Transformer (Fedus et al. 2021, Section 2.1) rejects this directly, routes each token to one expert, and reports it "preserves model quality, reduces routing computation and performs better." This is a genuine disagreement between two primaries, and both are Google papers with Noam Shazeer as an author. The writer can present it as the field correcting its own earlier claim, not as an outside critique.

- Whether MoE is stable to train. Every primary here treats load balancing and training stability as an active problem, and none reports it solved. Shazeer 2017 needs two auxiliary losses to stop expert collapse. GShard adds a hard expert-capacity cap plus its own auxiliary loss because tokens still pile onto some experts. Switch's own abstract says MoE adoption "has been hindered by complexity, communication costs and training instability" and offers precision and initialization fixes; the HF post notes a further fix, router z-loss, arriving later in ST-MoE. Settled: routing is sparse and load-balancing losses are required. Open: no single balancing-and-stability recipe is common to all of them, and each new primary changes it.

- Mixtral's exact totals. The paper's abstract rounds to 47B total / 13B active. The commonly cited precise figures are 46.7B / 12.9B, and the HF post approximates active cost as "like a 12B model." The rounding is consistent, but a writer quoting "13B active" should know the finer number is 12.9B and cite the paper's own 47B/13B when using the paper.

## Numbers

```text
Figure: 137 billion parameters (largest MoE model)
Owner:  Shazeer et al. 2017 (arXiv 1701.06538)
Scope:  MoE layer with 131,072 experts, hierarchical gating, trained on a 100-billion-word Google News corpus. The results table prints the count in millions (137,577.6 million); the abstract states it as 137 billion. Its reported test perplexity is about 28-29 after 1 epoch on that corpus.
```

```text
Figure: 4.3 billion parameters at 8.9 million ops/timestep, test perplexity 34.1
Owner:  Shazeer et al. 2017 (arXiv 1701.06538), Table 1 (1 Billion Word benchmark), model MoE-4096-h
Scope:  Per-timestep operation count held near the low-compute budget while parameters grow into the billions. This is the clean decoupling figure: the previous best published result (2xLSTM-8192-1024) scored 34.7 at 151 million parameters and 151 million ops/timestep, so the MoE beats it on quality using roughly 17x fewer ops per timestep and about 28x more parameters.
```

```text
Figure: 28.0 test perplexity at 142.7 million ops/timestep, 4.4 billion parameters
Owner:  Shazeer et al. 2017 (arXiv 1701.06538), Table 1, high-budget MoE model
Scope:  1 Billion Word benchmark, 10 epochs. Shows that spending more per-token compute on the same MoE design lowers perplexity from 34.1 to 28.0, below the prior best of 34.7.
```

```text
Figure: +1.34 BLEU (En->Fr) and +1.12 BLEU (En->De) over GNMT
Owner:  Shazeer et al. 2017 (arXiv 1701.06538), machine-translation tables
Scope:  WMT'14. En->Fr: MoE 40.56 vs GNMT 39.22. En->De: MoE 26.03 vs GNMT 24.91. The MoE translation model used a 2048-expert layer.
```

```text
Figure: 600 billion parameters; 2048 experts per MoE layer; 2048 TPU v3 cores x 4 days (~22 core-years)
Owner:  GShard, Lepikhin et al. 2020 (arXiv 2006.16668)
Scope:  Multilingual translation, 100 languages into English, MoE(2048E, 36L). The reported average BLEU (about 44.3) and delta over baselines (about +13.5) rest on a single reading of one results table and should be treated as unconfirmed pending a second look; the 600B / 2048-expert / training-cost figures are firm.
```

```text
Figure: 1.571 trillion parameters at 890 billion FLOPs/seq (Switch-C)
Owner:  Switch Transformer, Fedus et al. 2021 (arXiv 2101.03961), Table 9
Scope:  Switch-C has 2048 experts. Its 890B FLOPs/seq is lower than dense T5-XXL's 6.3T FLOPs/seq, though Switch-C carries about 143x T5-XXL's 11B parameters. Switch-XXL (64 experts, 395B parameters) matches T5-XXL's 6.3T FLOPs/seq exactly. This is the strongest single primary illustration that parameters and compute sit on different axes.
```

```text
Figure: Mixtral 8x7B, 47 billion total / 13 billion active per token; top-2 of 8 experts
Owner:  Mixtral, Jiang et al. 2024 (arXiv 2401.04088), abstract
Scope:  Per-token inference. The "8x7B" name does not equal 8*7=56B total, because only FFN blocks are separate experts and the rest of the model is shared (HF secondary, for the reason).
```

```text
Figure: DeepSeekMoE 16B, 16.4 billion total / 2.8 billion active per token; 2 shared + 6-of-64 routed experts
Owner:  DeepSeekMoE, Dai et al. 2024 (arXiv 2401.06066), Section 5.1.2
Scope:  Per-token inference. Reports parity with dense DeepSeek 7B at about 40% of its compute.
```

## Source assets

```text
Asset: Shazeer et al. 2017, Figure 1 (the MoE layer diagram, showing the gating network selecting a sparse subset of experts between two LSTM layers)
Shows: The mechanism at a glance: many experts, a gate that lights up only two or four of them, the rest dark and uncomputed. Carries the "sparse routing" idea better than any prose restatement.
Crop:  Must retain the gate box, at least one selected and one unselected expert, and the labels that mark which experts are active. Omit surrounding page text.
```

```text
Asset: Shazeer et al. 2017, Table 1 (1 Billion Word benchmark: model, test perplexity, #params, ops/timestep)
Shows: Parameters climbing into the billions while ops/timestep stays small, next to the perplexity that falls anyway. The decoupling as a table the reader can scan.
Crop:  Must keep the #params and ops/timestep columns side by side with perplexity. Omit rows the article does not discuss to keep it legible.
```

```text
Asset: Switch Transformer, Fedus et al. 2021, Table 9 (T5-XXL vs Switch-XXL vs Switch-C: experts, parameters, FLOPs/seq)
Shows: 1.571 trillion parameters at fewer FLOPs per sequence than an 11-billion dense model. The clearest total-versus-compute contrast in any of the primaries.
Crop:  Must keep the parameter column beside the FLOPs/seq column for all three rows. Nothing else is needed.
```

```text
Asset: Switch Transformer, Fedus et al. 2021, Figure 1 (the Switch routing diagram: one token going to one expert)
Shows: Top-1 routing in one picture, the concrete contrast with Shazeer's top-4 gate.
Crop:  Must retain the single highlighted routing path from token to one expert.
```

```text
Asset: Mixtral, Jiang et al. 2024, the router/layer figure (8 experts per layer, 2 selected)
Shows: A shipped model's version of the same gate: 8 experts, 2 chosen. Anchors the 47B/13B split visually.
Crop:  Must keep all 8 experts visible with the 2 selected ones marked.
```

```text
Asset: GShard, Lepikhin et al. 2020, training-cost figure (600B MoE core-years vs 100 bilingual baselines)
Shows: One 600B sparse model trained for fewer TPU core-years than the fleet of dense baselines it beats. A compute-accounting visual, if the article goes into training cost.
Crop:  Must keep both cost bars and their labels. Optional for the lesson; include only if training cost is in scope.
```

```text
Asset: DeepSeekMoE, Dai et al. 2024, architecture figure (shared experts plus fine-grained routed experts)
Shows: The two refinements in one diagram: always-on shared experts beside the segmented routed pool.
Crop:  Must keep the shared-expert block distinct from the routed-expert block. None found beyond this that adds to the lesson.
```

## Discarded

```text
URL: https://ar5iv.org/abs/1701.06538  Rejected as a source address: it is a redirecting mirror hostname, not the document's home. The paper's own page is https://arxiv.org/abs/1701.06538, recorded above; the ar5iv rendering was only the route used to read the full text.
```

```text
URL: (GShard synthesized total "36,684 experts across the model")  Rejected as a figure: it was a derived product of one summary read, not a count the paper prints. Only the firm per-layer count (2048 experts per MoE layer) and the 600B total are recorded.
```
