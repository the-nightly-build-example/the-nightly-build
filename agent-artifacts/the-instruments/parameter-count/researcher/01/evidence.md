# Evidence: the-instruments/parameter-count (01)

The record supports the commission's core figures firsthand from the primaries
that own them. GPT-3's 175B is read off Brown et al. 2020. Mixtral's exact
46.7B total and 12.9B active-per-token come from Mistral AI's own announcement
(the paper's abstract rounds these to 47B/13B). DeepSeek-V3's 671B total /
37B activated come from the DeepSeek-V3 technical report and model card.
Chinchilla (~70B) beating Gopher (~280B) at equal compute is read off Hoffmann
et al. 2022. Sparse routing (a few experts fire per token, decoupling parameter
count from per-token compute) is grounded in two MoE primaries, Shazeer et al.
2017 and the Switch Transformer. The source floor is met with room to spare:
9 primary, 1 secondary.

The record is thin on, and the writer must be careful about, one thing the
commission's angle understates: "active parameters" is the right number for
**compute and speed per token**, but **not for memory**. An MoE still loads all
its total parameters into memory, so total parameter count drives VRAM and
deployment cost even though only the active fraction does arithmetic per token.
The "same cost as a 12.9B model" claim is a claim about compute/speed, not
memory. This is recorded under Contradictions and is the most important
limitation on the "active is the real number" framing. The per-expert
sub-breakdown of Mixtral (attention ~5B, each FFN expert ~5.25B) is an
approximation from secondary discussion and is not asserted as a verified
figure; only the headline 46.7B / 12.9B are primary-owned.

## Sources

```text
URL:         https://arxiv.org/abs/2005.14165
Kind:        primary — the paper that trained and owns GPT-3; the authoring party.
Establishes: GPT-3's parameter count of 175 billion, firsthand.
Paraphrase:  Brown et al. train GPT-3, an autoregressive language model with 175
             billion parameters, described as 10x larger than any previous
             non-sparse (dense) language model.
Locators:    Abstract; "Language Models are Few-Shot Learners," Brown et al., 2020.
Quote:       "we train GPT-3, an autoregressive language model with 175 billion
             parameters, 10x more than any previous non-sparse language model"
```

```text
URL:         https://arxiv.org/abs/2401.04088
Kind:        primary — the Mixtral paper by its authors (Mistral AI).
Establishes: Mixtral's architecture (8 experts per layer, router picks 2 per
             token) and the rounded total/active counts.
Paraphrase:  Mixtral 8x7B is a sparse mixture-of-experts model with the same
             architecture as Mistral 7B except each feed-forward block is
             replaced by 8 expert blocks; a router picks 2 experts per token per
             layer and sums their outputs. Each token "has access to" 47B
             parameters but uses only 13B active during inference (rounded).
Locators:    Abstract and Section 2 (Architectural details); "Mixtral of
             Experts," Jiang et al., 2024.
Quote:       "each token has access to 47B parameters, but only uses 13B active
             parameters during inference." / "For every token, at each layer, a
             router network selects two experts to process the current state and
             combine their outputs."
```

```text
URL:         https://mistral.ai/news/mixtral-of-experts/
Kind:        primary — Mistral AI's own announcement of the model it built.
Establishes: The EXACT figures the commission requires: 46.7B total, 12.9B per
             token, and the compute/speed cost equivalence to a 12.9B model.
Paraphrase:  Mistral states Mixtral has 46.7B total parameters but uses only
             12.9B per token, so it processes input and generates output at the
             same speed and for the same cost as a 12.9B model. Sparse
             mixture-of-experts: 8 expert groups per layer, router selects 2 per
             token.
Locators:    Body of the announcement page, architecture description.
Quote:       "Mixtral has 46.7B total parameters but only uses 12.9B parameters
             per token. It, therefore, processes input and generates output at
             the same speed and for the same cost as a 12.9B model."
```

```text
URL:         https://huggingface.co/mistralai/Mixtral-8x7B-v0.1
Kind:        primary — the official model card published by the authoring party.
Establishes: The card's headline size label and the "Sparse Mixture of Experts"
             description.
Paraphrase:  The official card labels the model "47B params" (rounded) and
             describes it as a pretrained generative Sparse Mixture of Experts.
             It does not itself break out active-vs-total or the 46.7B figure;
             that precision lives on the announcement page above.
Locators:    Model card header ("Model size: 47B params") and description.
Quote:       "Model size: 47B params" / "pretrained generative Sparse Mixture of
             Experts"
```

```text
URL:         https://arxiv.org/abs/2412.19437
Kind:        primary — the DeepSeek-V3 technical report by its authors (DeepSeek-AI).
Establishes: DeepSeek-V3's 671B total parameters and 37B activated per token.
Paraphrase:  DeepSeek-V3 is a Mixture-of-Experts language model with 671B total
             parameters, of which 37B are activated for each token. It uses
             DeepSeekMoE and Multi-head Latent Attention. (The HF release totals
             685B on disk: 671B main weights plus a 14B Multi-Token Prediction
             module used for speculative decoding, not part of the base model.)
Locators:    Abstract; "DeepSeek-V3 Technical Report," DeepSeek-AI, 2024.
Quote:       "DeepSeek-V3, a strong Mixture-of-Experts (MoE) language model with
             671B total parameters with 37B activated for each token."
```

```text
URL:         https://huggingface.co/deepseek-ai/DeepSeek-V3
Kind:        primary — the official DeepSeek-V3 model card by the authoring party.
Establishes: Confirms 671B total / 37B activated and the on-disk 685B (671B main
             + 14B MTP module).
Paraphrase:  The card restates 671B total parameters with 37B activated per
             token, and notes the HuggingFace checkpoint is 685B because it
             bundles the 14B Multi-Token Prediction module alongside the 671B
             main model. Uses 256 routed experts (per the conversion script's
             --n-experts 256) under DeepSeekMoE.
Locators:    Model card body; "Model Summary" / weights note.
Quote:       "671B total parameters with 37B activated for each token" / weights
             note: "671B of the Main Model weights and 14B of the Multi-Token
             Prediction (MTP) Module weights."
```

```text
URL:         https://arxiv.org/abs/2203.15556
Kind:        primary — the Chinchilla paper (DeepMind), authoring party of the result.
Establishes: The equal-compute result: a ~70B model (Chinchilla) trained on 4x
             more data beats the ~280B Gopher, GPT-3 (175B), and larger models.
Paraphrase:  Hoffmann et al. train Chinchilla with the same compute budget as
             Gopher but with 70B parameters and 4x more training data. Chinchilla
             uniformly and significantly outperforms Gopher (280B), GPT-3 (175B),
             Jurassic-1 (178B), and Megatron-Turing NLG (530B); e.g. 67.5% vs
             Gopher's ~60% on MMLU. Demonstrates that model size and training
             tokens should scale together, so more parameters at fixed compute
             is not better.
Locators:    Abstract; "Training Compute-Optimal Large Language Models,"
             Hoffmann et al., 2022.
Quote:       "Chinchilla, that uses the same compute budget as Gopher but with
             70B parameters and 4x more data." / "Chinchilla uniformly and
             significantly outperforms Gopher (280B), GPT-3 (175B), Jurassic-1
             (178B), and Megatron-Turing NLG (530B)."
```

```text
URL:         https://arxiv.org/abs/2101.03961
Kind:        primary — the Switch Transformer paper (Google), owns the top-1 sparse routing design.
Establishes: Sparse routing where each token goes to a single expert, and the
             central claim that parameter count can grow while per-token compute
             (FLOPs) stays roughly constant.
Paraphrase:  Fedus, Zoph, and Shazeer route each token to exactly one expert
             (top-1), producing a sparsely-activated model with very large
             parameter counts but a constant computational cost per token. This
             is the mechanism by which total parameters and per-token compute are
             decoupled.
Locators:    Abstract and Section 2 (Switch routing); "Switch Transformers:
             Scaling to Trillion Parameter Models with Simple and Efficient
             Sparsity," Fedus et al., 2021.
Quote:       "The result is a sparsely-activated model -- with outrageous numbers
             of parameters -- but a constant computational cost."
```

```text
URL:         https://arxiv.org/abs/1701.06538
Kind:        primary — the foundational sparsely-gated MoE paper (Shazeer et al., Google Brain).
Establishes: The definition of a sparsely-gated MoE layer: a gating network
             selects a small subset (top-k) of many experts per example, so only
             a few experts activate; conditional computation raises capacity
             without proportional compute.
Paraphrase:  A trainable gating network picks a sparse combination of experts for
             each example out of up to thousands, activating only a few. This
             conditional computation increases model capacity dramatically
             (>1000x, up to 137B parameters here) with only minor added
             computation per example. This is the primary that owns "only a few
             experts fire per token."
Locators:    Abstract and Section 1; "Outrageously Large Neural Networks: The
             Sparsely-Gated Mixture-of-Experts Layer," Shazeer et al., 2017.
Quote:       "Conditional computation, where parts of the network are active on a
             per-example basis, has been proposed in theory as a way of
             dramatically increasing model capacity without a proportional
             increase in computation." / "a trainable gating network determines a
             sparse combination of these experts to use for each example."
```

```text
URL:         https://www.interconnects.ai/p/mixtral
Kind:        secondary — independent analysis by Nathan Lambert (AI researcher,
             then at Allen Institute for AI / previously Hugging Face). Not a
             party to Mixtral; reports on and explains it. Context only.
Establishes: The exact "8x7B is not 56B, and why" explanation the commission's
             misled-case requires, stated plainly by an independent expert.
Paraphrase:  Lambert states Mixtral does NOT have 56B parameters (from 7x8=56)
             but 46.7B, because the expert split happens only in the feed-forward
             (FFN) blocks, not the attention layers or other shared components,
             which are counted once. Notes the SMoE trades higher VRAM (all
             experts must be resident) for faster inference at the active-param
             cost.
Locators:    Body of "Mixtral: The best open model..." (Interconnects, Dec 2023).
Quote:       "This is why the new network Mixtral doesn't have 56 billion
             parameters, from 7x8=56, but only 46.7 billion." / "This happens in
             every feed-forward network (FFN), rather than all of the attention
             layers or other compute-heavy areas."
```

## Contradictions

- **"Active parameters is the real cost number" is only half true.** The
  commission frames active-per-token as the number marketing hides and cost
  really tracks. That holds for compute and speed per token (the sense in which
  Mistral says Mixtral costs the same as a 12.9B model). It does NOT hold for
  memory: an MoE must load ALL total parameters into memory/VRAM because any
  expert may be needed for the next token. So Mixtral's memory footprint tracks
  46.7B, not 12.9B, and DeepSeek-V3 must hold ~671B in memory to serve 37B of
  compute per token. Nathan Lambert's piece explicitly frames SMoE as trading
  increased VRAM for faster inference. The honest teaching is: total parameters
  drive memory cost, active parameters drive compute/speed cost. Neither single
  number is "the" cost. This complicates, but does not break, the angle: the
  point that total and active are different numbers routinely conflated stands;
  the writer should not overclaim that active is simply the true cost.

- **Parameter count is not meaningless within a fixed recipe.** Chinchilla shows
  more parameters at equal compute is not better, and MoE breaks cross-model
  comparison. But within one model family trained the same way (GPT-2 to GPT-3),
  scaling parameters did reliably raise capability. The defensible claim is the
  commission's actual one: parameter count "by itself" predicts neither
  capability nor cost across systems with different data, training budgets, or
  sparsity. It should not be overstated into "parameter count tells you
  nothing." Chinchilla's result is about compute-optimal allocation, not about
  parameters being irrelevant.

- **Rounding gap in Mixtral's own materials.** The Mixtral paper abstract and the
  HF model card say 47B / 13B (rounded); only the mistral.ai announcement gives
  46.7B / 12.9B. All three are the authoring party and consistent; the writer
  should cite the announcement for the exact figures and can note the rounded
  47B as the same number. No genuine disagreement, but worth flagging so an
  editor does not read 47B vs 46.7B as a conflict.

## Numbers

```text
Figure: 175 billion parameters (GPT-3, largest model)
Owner:  Brown et al. 2020 (arxiv 2005.14165), abstract
Scope:  Total learnable weights of the dense GPT-3 model; fixed at training. All
        175B are active on every token (dense, not MoE).
```

```text
Figure: 46.7B total parameters (Mixtral 8x7B)
Owner:  Mistral AI announcement (mistral.ai/news/mixtral-of-experts); rounded to
        47B in the paper abstract and HF card.
Scope:  All learnable weights across the 8 experts plus shared attention,
        embeddings, and norms. NOT 56B: 8x7B=56B wrongly assumes eight full 7B
        models; only the FFN blocks are replicated, while attention/embeddings
        are shared and counted once.
```

```text
Figure: 12.9B active parameters per token (Mixtral 8x7B)
Owner:  Mistral AI announcement (mistral.ai/news/mixtral-of-experts); rounded to
        13B in the paper abstract.
Scope:  Parameters that do arithmetic for a single token: shared attention/
        embeddings plus the 2 of 8 FFN experts the router selects. NOT 14B
        (2x7B), for the same shared-attention reason. Governs compute/speed per
        token, not memory footprint.
```

```text
Figure: 671B total parameters / 37B activated per token (DeepSeek-V3)
Owner:  DeepSeek-V3 Technical Report (arxiv 2412.19437) and model card
Scope:  671B total across 256 routed experts + shared components under
        DeepSeekMoE; 37B activated per token. On-disk HF checkpoint is 685B
        (adds a 14B Multi-Token Prediction module). Active fraction ~5.5%.
```

```text
Figure: Chinchilla ~70B vs Gopher ~280B, equal training compute
Owner:  Hoffmann et al. 2022 (arxiv 2203.15556), abstract
Scope:  Same compute budget as Gopher (280B) but 70B parameters and 4x more
        training data; Chinchilla outperforms Gopher, GPT-3 (175B), Jurassic-1
        (178B), Megatron-Turing NLG (530B). MMLU 67.5% vs Gopher ~60%. Shows
        parameter count at fixed compute does not predict capability.
```

```text
Figure: Active fraction comparison (for the total-vs-active teaching)
Owner:  Derived from the owning primaries above (each figure is primary-owned).
Scope:  Dense GPT-3: 175B / 175B = 100% active. Mixtral: 12.9B / 46.7B ~= 28%
        active. DeepSeek-V3: 37B / 671B ~= 5.5% active. Ratios are exact
        arithmetic on primary-owned figures; useful if a chart compares total
        vs active across dense and MoE models.
```

## Source assets

```text
Asset: Mixtral routing / architecture figure (Figure 1, arxiv 2401.04088),
       showing the router selecting 2 of 8 experts per token.
Shows: That per token only a subset of expert blocks activate, the visual root
       of total-vs-active.
Crop:  Keep the router and the highlighted (selected) vs greyed (idle) experts;
       omit dense equation notation. Note: the commission warns against turning
       this into an MoE-mechanics lesson, so use sparingly if at all.
```

```text
Asset: Total-vs-active comparison across GPT-3 (dense), Mixtral, DeepSeek-V3.
Shows: A dense model activates 100% of its parameters; MoEs advertise a large
       total while ~5-28% fires per token. This is the article's own point.
Crop:  Not a source image. This is best built by the writer as a committed
       chart-N.py bar chart (two bars per model: total vs active), per the house
       charts rule, from the primary-owned figures in the Numbers section. All
       inputs are cited above.
```

```text
Asset: Chinchilla vs Gopher performance-at-equal-compute (Hoffmann et al. 2022,
       results tables / MMLU comparison).
Shows: The smaller 70B model beating the 280B model, the anchor for "count does
       not equal capability."
Crop:  If used, keep the head-to-head Chinchilla-vs-Gopher rows; the commission
       says link the-evidence/chinchilla rather than re-derive, so prefer a
       single sentence over a large asset.
```

Otherwise: None found. The core teaching (a definitional count, frozen at
inference) is prose, not a source visual.

## Discarded

```text
URL: https://patmcguinness.substack.com/p/mixtral-8x7b-and-mixture-of-experts — secondary explainer, redundant with the stronger Lambert secondary and the primary figures; not needed to meet the floor.
URL: https://galileo.ai/blog/mixtral-8x7b-guide-review — vendor blog, secondary, no figure the primaries do not own; rejected as padding.
URL: https://d-central.tech/ai/model/mixtral-8x7b/ — low-authority aggregator; every figure it carries is owned upstream by Mistral. Rejected.
URL: https://skywork.ai/... and https://www.ankursnewsletter.com/... — restated marketing/spec pages, no independent verification; rejected.
URL: WebSearch summary snippets giving a per-expert breakdown (attention ~5B, each FFN expert ~5.25B) — plausible arithmetic but not read off a primary; recorded in the opening as approximate and NOT asserted as a verified figure.
```
