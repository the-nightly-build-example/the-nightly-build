# Evidence: the-mechanics/word-order (01)

The evidence supports the commission's spine firmly. Self-attention has no built-in
notion of order: the original Transformer paper states plainly that with no recurrence
and no convolution the model must be given position information, and a later survey
states the property formally as invariance to reordering the input. Each scheme the
brief names is documented from the paper that owns it: sinusoidal (Vaswani et al.),
learned absolute (GPT-1 and BERT), relative (Shaw et al.), rotary (Su et al., now the
common choice via LLaMA), and additive distance bias (ALiBi, Press et al.). What the
record settles firmly is the mechanism of each scheme. What it marks as open is length
extrapolation, and here the evidence complicates the commission rather than confirming
a tidy story. Two claims a casual reader might expect to hold do not: RoPE, though it
encodes relative offset, fails past its trained length in practice (this is the reason
YaRN and position interpolation exist), and a decoder-only Transformer with no positional
encoding at all still learns position from the causal mask and can match or beat explicit
schemes on small reasoning tasks (Haviv et al.; Kazemnejad et al.). The record is thinnest
on scale: the strongest "no encoding needed" and "relative wins" findings come from small
models on algorithmic tasks, and none of the sources claims a single scheme is settled as
best for large language models.

## Sources

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary — Vaswani et al., "Attention Is All You Need"; owns the sinusoidal
             scheme and the original motivation for injecting position.
Establishes: (a) why position must be added to a self-attention model; (b) the sinusoidal
             formula; (c) that extrapolation was a hypothesis, not a demonstrated result.
Paraphrase:  Self-attention has no recurrence or convolution, so order carries no signal
             unless position is injected. The paper adds fixed sinusoidal vectors of the
             same dimension as the token embeddings, summed into the input. It picked the
             sinusoidal form on the conjecture that it "may" help the model handle longer
             sequences than seen in training. It reports learned and sinusoidal encodings
             produced nearly identical results.
Locators:    Section 3.5 "Positional Encoding" (read in full via arxiv.org/html/1706.03762v7).
Quote:       "Since our model contains no recurrence and no convolution, in order for the
             model to make use of the order of the sequence, we must inject some information
             about the relative or absolute position of the tokens in the sequence."
             PE(pos,2i) = sin(pos/10000^(2i/d_model)); PE(pos,2i+1) = cos(pos/10000^(2i/d_model)).
             "We chose the sinusoidal version because it may allow the model to extrapolate
             to sequence lengths longer than the ones encountered during training."
```

```text
URL:         https://cdn.openai.com/research-covers/language-unsupervised/language_understanding_paper.pdf
Kind:        primary — Radford et al. 2018, "Improving Language Understanding by Generative
             Pre-Training" (GPT-1); owns the decision to learn position per slot.
Establishes: The first concrete form of "added, not computed": a decoder-only Transformer
             that replaces the fixed sinusoid with a trainable vector for each position.
Paraphrase:  GPT-1 is a 12-layer decoder-only Transformer. It swaps the original paper's
             fixed sinusoidal encoding for position embeddings the model learns during
             training, one vector per absolute slot.
Locators:    Section 3.1 / model-specification paragraph. Note: the PDF's text layer did
             not extract cleanly through the fetch tool; the exact sentence below was
             confirmed verbatim against the search index of this document, not read off a
             rendered page. The resolving page is the OpenAI-hosted PDF above.
Quote:       "We used learned position embeddings instead of the sinusoidal version proposed
             in the original work."
```

```text
URL:         https://arxiv.org/abs/1810.04805
Kind:        primary — Devlin et al., "BERT"; owns a second concrete form of learned
             absolute position, in an encoder rather than a decoder.
Establishes: That a learned position embedding is one of three vectors summed to build each
             input token, and that the scheme carries a hard length ceiling (512).
Paraphrase:  BERT builds each input representation by summing a token embedding, a segment
             embedding, and a position embedding. The position embeddings are learned per
             slot, and the model supports sequences only up to 512 tokens — a fixed table
             has no entry for a longer position, which is the concrete cost of learned
             absolute encoding.
Locators:    Section 3, "Input/Output Representations," and Figure 2 caption (read via arxiv
             abstract page and ar5iv full text). The 512 ceiling appears in the training
             configuration.
Quote:       "For a given token, its input representation is constructed by summing the
             corresponding token, segment, and position embeddings." Figure 2: "The input
             embeddings are the sum of the token embeddings, the segmentation embeddings
             and the position embeddings."
```

```text
URL:         https://arxiv.org/abs/1803.02155
Kind:        primary — Shaw et al. 2018, "Self-Attention with Relative Position
             Representations"; owns the relative-vs-absolute distinction.
Establishes: That position can be encoded as the distance between two tokens inside the
             attention computation, rather than as an absolute slot added at the input.
Paraphrase:  The Transformer as originally built encodes neither relative nor absolute
             position in its structure; the paper adds learned representations of the
             relative distance between token pairs, clipped at a maximum distance, into the
             self-attention operation. On WMT translation this beat absolute encodings, and
             combining relative with absolute added nothing further.
Locators:    Abstract; Section 3 (relation-aware self-attention); Section 4 (results).
Quote:       The original Transformer "does not explicitly model relative or absolute
             position information in its structure." Reported gains: "1.3 BLEU and 0.3 BLEU
             over absolute position representations" on En-De and En-Fr; "combining relative
             and absolute position representations yields no further improvement in
             translation quality."
```

```text
URL:         https://arxiv.org/abs/2104.09864
Kind:        primary — Su et al., "RoFormer: Enhanced Transformer with Rotary Position
             Embedding"; owns RoPE.
Establishes: What RoPE does mechanically, and its designed property that the attention
             score depends on relative offset.
Paraphrase:  RoPE multiplies the query and key vectors by a rotation whose angle is set by
             each token's absolute position. Because a query rotated by angle for position m
             and a key rotated for position n meet in an inner product, the score depends
             only on the difference m − n, i.e. the relative offset. The paper reports a
             built-in decay of attention as relative distance grows and claims flexibility
             with sequence length.
Locators:    Abstract; the formulation and theoretical-property sections. Confirmed as the
             common modern choice by the LLaMA entry below.
Quote:       RoPE "incorporates the explicit relative position dependency in self-attention
             formulation," with "decaying inter-token dependency with increasing relative
             distances."
```

```text
URL:         https://arxiv.org/abs/2302.13971
Kind:        primary — Touvron et al., "LLaMA"; owns the fact that RoPE is the encoding a
             flagship modern LLM family adopted.
Establishes: That RoPE is now a default in practice, not a research curiosity — the point
             the brief asks to support.
Paraphrase:  LLaMA drops absolute position embeddings and applies rotary embeddings at every
             layer, citing Su et al. This is the concrete grounding for "RoPE is now the
             common choice."
Locators:    Section 2.2, architecture improvements, "Rotary Embeddings [RoPE]" (read via
             ar5iv full text).
Quote:       "We remove the absolute positional embeddings, and instead, add rotary
             positional embeddings (RoPE), introduced by Su et al. (2021), at each layer of
             the network."
```

```text
URL:         https://arxiv.org/abs/2108.12409
Kind:        primary — Press et al., "Train Short, Test Long: Attention with Linear Biases
             Enables Input Length Extrapolation" (ALiBi); owns the additive-distance-bias
             scheme and its extrapolation claim.
Establishes: What ALiBi does, and its specific extrapolation result and efficiency figures.
Paraphrase:  ALiBi adds no position vectors to the token embeddings. It subtracts a penalty
             from each query-key attention score in proportion to the distance between them,
             scaled by a head-specific slope m that is fixed, not learned. This recency bias
             lets a model trained on short sequences keep low perplexity when evaluated on
             longer ones. A 1.3B model trained on 1024-token inputs extrapolates to 2048.
Locators:    Abstract; Section 3 (method); Figures 1 and 3.
Quote:       ALiBi "biases query-key attention scores with a penalty that is proportional to
             their distance." It reaches "the same perplexity as a sinusoidal position
             embedding model trained on inputs of length 2048 but training 11% faster and
             using 11% less memory."
```

```text
URL:         https://arxiv.org/abs/2309.00071
Kind:        primary for its own finding, secondary reporting on RoPE — Peng et al., "YaRN:
             Efficient Context Window Extension of Large Language Models." Peng et al. are
             not the RoPE authors, so on RoPE's behavior this is an outside party.
Establishes: The central contradiction to a naive reading of the angle: RoPE, a relative
             scheme, does not extrapolate past its trained length without extra work.
Paraphrase:  Models using RoPE fail to generalize past the sequence length they were trained
             on. YaRN is a method to extend the trained context window efficiently (it cites
             roughly 10x fewer tokens and 2.5x fewer steps than prior methods), which is only
             necessary because raw RoPE does not extrapolate on its own. This places RoPE's
             length behavior in the "open / needs engineering" column, not "solved."
Locators:    Abstract; introduction. The mechanistic reason (some RoPE frequencies never
             complete a rotation within the trained window) is corroborated by secondary
             explainers below but not quoted from a primary here.
Quote:       RoPE-based models "fail to generalize past the sequence length they were trained
             on." YaRN lets LLaMA models "extrapolate to context lengths much longer than
             their original pre-training would allow."
```

```text
URL:         https://arxiv.org/abs/2305.19466
Kind:        primary — Kazemnejad et al. 2023, "The Impact of Positional Encoding on Length
             Generalization in Transformers" (NoPE); owns the no-encoding finding.
Establishes: That a decoder-only Transformer with no explicit positional encoding can
             generalize to longer sequences and can beat ALiBi, rotary, and absolute on the
             tested tasks — and the bounds on that claim.
Paraphrase:  On a set of small reasoning and mathematical tasks, a decoder-only model given
             no positional encoding at all (NoPE) generalized to longer inputs better than
             absolute, rotary, and ALiBi encodings, at no extra compute. The paper shows NoPE
             can in principle represent both absolute and relative position, and that after
             training it behaves most like T5's relative scheme. Bounds: the result is for
             decoder-only models on algorithmic/reasoning tasks, not a claim about large
             general-purpose LLMs, and the paper notes a scratchpad does not reliably help.
Locators:    Abstract; theory section; task results. NeurIPS 2023.
Quote:       "Explicit position embeddings are not essential for decoder-only Transformers to
             generalize well to longer sequences." "NoPE outperforms other explicit
             positional encoding methods while requiring no additional computation."
```

```text
URL:         https://arxiv.org/abs/2203.16634
Kind:        primary — Haviv et al. 2022, "Transformer Language Models without Positional
             Encodings Still Learn Positional Information."
Establishes: The sharpest qualification of the order-blindness claim. A decoder-only model
             is not fully order-blind even with no positional encoding, because the causal
             mask itself carries position.
Paraphrase:  Causal (autoregressive) language models with no positional encoding remain
             competitive and still acquire position information. The mechanism is the causal
             mask: a token can attend only to earlier tokens, so counting how many tokens are
             visible approximates its absolute position. This breaks the permutation symmetry
             that makes an unmasked attention layer order-blind. The effect holds across
             datasets, model sizes, and lengths.
Locators:    Abstract; analysis sections.
Quote:       "Causal attention enables the model to infer the number of predecessors that
             each token can attend to, thereby approximating its absolute position."
```

```text
URL:         https://arxiv.org/abs/2102.11090
Kind:        secondary — Dufter, Schmitt, Schütze, "Position Information in Transformers: An
             Overview." A survey by parties who authored none of the schemes; useful for the
             formal framing and the state of the field.
Establishes: The order-blindness property stated formally, and that the field has no single
             agreed-best scheme.
Paraphrase:  The survey states that a Transformer is by definition invariant to reordering
             its input, which is why position must be supplied externally. It catalogs
             absolute, relative, sinusoidal, and learned variants under one notation and does
             not name any as universally best, which matches the fragmented picture the
             primaries show.
Locators:    Abstract; taxonomy sections.
Quote:       "By definition a Transformer is invariant with respect to reordering of the
             input."
```

## Contradictions

- **RoPE being relative does not make it extrapolate.** The commission's arc could be
  read to suggest relative/rotary schemes solved position, including length. They did
  not. Su et al. claim flexibility with length, but Press et al.'s Figure 1 shows rotary
  perplexity degrading as inputs grow past training length, and Peng et al. (YaRN) state
  plainly that RoPE models "fail to generalize past the sequence length they were trained
  on." The writer should present RoPE's length behavior as engineered around (position
  interpolation, NTK scaling, YaRN), not solved by RoPE itself.

- **A decoder-only model is not strictly order-blind.** The clean statement "self-attention
  cannot tell word orders apart" is exact for a single unmasked attention layer (Vaswani;
  Dufter). It is too strong for a causal decoder: Haviv et al. show the causal mask alone
  lets a model without any positional encoding recover absolute position, and Kazemnejad
  et al. show such a model can beat explicit encodings on small tasks. The lesson must
  distinguish "attention with no mask and no encoding is order-blind" from "a masked
  decoder still gets some position for free." The brief flags the causal mask as taught
  elsewhere; this is the seam to link it.

- **No scheme is settled as best.** The sources disagree on which encoding wins, and the
  winner depends on the test. Shaw: relative beats absolute on translation. Press: ALiBi
  beats sinusoidal, rotary, and T5 on extrapolation. Kazemnejad: no encoding beats all
  three on small reasoning tasks. Dufter names none as universally best. A verdict that
  crowns one scheme would overreach the evidence.

- **ALiBi's extrapolation buys locality.** ALiBi's recency penalty is what lets it
  extrapolate, and the same penalty gives it a restricted effective receptive field
  (windowed-attention-like behavior). Distant tokens are down-weighted by construction, so
  "handles longer sequences" is not the same as "attends usefully across the whole length."
  This nuance is drawn from secondary explainers, not an ALiBi-authored quote, so the
  writer should hold it as context, not a headline claim.

## Numbers

```text
Figure: model contains no recurrence and no convolution — position must be injected
Owner:  Vaswani et al. 2017, Section 3.5
Scope:  architectural statement about the original Transformer; no denominator
```

```text
Figure: sinusoidal wavelengths form a geometric progression from 2π to 10000·2π
Owner:  Vaswani et al. 2017, Section 3.5
Scope:  the fixed sinusoidal encoding as defined; per embedding dimension i
```

```text
Figure: 512 tokens — BERT's maximum supported sequence length
Owner:  Devlin et al. 2018, training configuration
Scope:  hard ceiling of the learned absolute position table; longer positions have no vector
```

```text
Figure: +1.3 BLEU (En-De), +0.3 BLEU (En-Fr) for relative over absolute
Owner:  Shaw et al. 2018, Section 4
Scope:  WMT 2014 test sets; relative vs absolute position representations, same model
```

```text
Figure: train on 1024 tokens, extrapolate to 2048 at inference; 11% faster, 11% less memory
Owner:  Press et al. 2021, abstract and results
Scope:  1.3B-parameter model; ALiBi vs a sinusoidal model trained at length 2048
```

```text
Figure: ~10x fewer tokens, ~2.5x fewer training steps than prior context-extension methods
Owner:  Peng et al. 2023 (YaRN), abstract
Scope:  cost of extending a RoPE model's context window; comparison to prior extension work
```

## Source assets

```text
Asset: ALiBi Figure 1 — perplexity (y, lower better) vs inference sequence length (x), two
       panels for models trained at L=512 and L=1024, curves for sinusoidal, rotary, T5, and
       ALiBi (arxiv.org/abs/2108.12409).
Shows: The extrapolation gap made visual: sinusoidal and rotary perplexity climb as inputs
       exceed training length while ALiBi stays flat. Teaches both the ALiBi claim and the
       RoPE-does-not-extrapolate contradiction in one image.
Crop:  Keep all four labeled curves and both axes with units; keep the x-axis mark of the
       training length so the reader sees where degradation begins. Do not crop to only the
       ALiBi curve — the comparison is the lesson.
```

```text
Asset: ALiBi Figure 3 — schematic of the query-key attention scores with the added constant
       distance-bias column, scaled by head-specific slope m, before softmax (same URL).
Shows: The mechanism in one picture: a penalty growing with distance is added to raw
       attention scores. Makes "biases attention by distance" concrete without algebra.
Crop:  Retain the bias values increasing with distance and the label that m is fixed, not
       learned. Omit surrounding running text.
```

```text
Asset: Vaswani et al., sinusoidal encoding — the paper defines the formula but I did not
       confirm a clean heatmap figure of the encoding pattern inside the paper itself. The
       widely circulated position-vs-dimension heatmap is from later expositions, not a
       verified Vaswani figure.
Shows: n/a — flagged so the writer does not attribute a borrowed visual to the source paper.
Crop:  n/a
```

Other named primaries (Shaw, Su/RoFormer, Kazemnejad, Haviv, GPT-1, BERT, LLaMA): no single
figure verified as clean and self-teaching for a general reader. None found beyond the two
ALiBi figures above.

## Discarded

```text
https://learnopencv.com/rope-position-embeddings/ : secondary explainer; used only to
  corroborate why RoPE frequencies fail to complete a rotation within the trained window.
  Not cited as a primary; the claim is owned by YaRN and the RoPE paper.
https://www.emergentmind.com/topics/rotary-positional-embeddings-rope-extension : aggregator
  overview of RoPE extensions; no firsthand claim, superseded by the YaRN primary.
https://arxiv.org/abs/2203.10995 (Word Order Does Matter, And Shuffled LMs Know It) : read
  far enough to see it is relevant to order-sensitivity, but it addresses masked-LM
  robustness to shuffling, a different question than positional-encoding mechanism; out of
  the commission's scope and left for a possible future lesson.
https://arxiv.org/abs/2010.04903 (What Do Position Embeddings Learn?) : interesting empirical
  probing of learned embeddings, but not needed to establish any claim the brief asks for;
  would pad the count without changing the interpretation.
Various Medium/blog posts on long-context limits : secondary, no firsthand claim, not cited.
```
