# Evidence: the-evidence/resnet (01)

The evidence firmly supports the commission's core angle. Read against the
primary text, "Deep Residual Learning for Image Recognition" (He, Zhang, Ren &
Sun, Microsoft Research) documents a specific optimization failure it calls the
*degradation problem*: adding layers to a plain network raised its **training**
error, and the paper states plainly this is not overfitting (Fig. 1, Sec. 1).
The residual/skip-connection formulation, the depths (18/34/50/101/152 on
ImageNet; 110 and 1202 on CIFAR-10), the 3.57% ensemble top-5 error, the
five-task ILSVRC/COCO 2015 sweep, and the "8x deeper than VGG at lower
complexity" claim are all verified against the tables and figures that own
them. The present-day payoff is solid: "Attention Is All You Need" uses a
residual connection around every sub-layer and cites this paper by name, so the
training trick genuinely sits inside the transformer. Three later primaries
establish *why* residuals help: identity signal propagation (He 2016), an
ensemble-of-shallow-paths view (Veit 2016), and loss-landscape smoothing (Li
2018).

One finding cuts against the brief's framing and must reach the writer: the
brief and commission assume the paper "did not claim the residual trick would
generalize to other architectures." It did. The last line of the Introduction
says the principle "is generic, and we expect that it is applicable in other
vision and non-vision problems." It is a forecast, not a demonstration, and
names no architecture (transformers did not exist), but the flat claim that the
paper made no generalization claim is wrong. A second, subtler correction: the
paper explicitly argues the degradation problem is *not* vanishing gradients,
so the popular "ResNet solved vanishing gradients" gloss misreads it. The
record is thin on nothing the commission requires; its softest spot is that the
CIFAR-10 Table 6 figures were read from the arXiv full-text render (ar5iv), not
the downloaded PDF, which truncated at 6 pages before the CIFAR section.

## Sources

```text
URL:         https://arxiv.org/abs/1512.03385
Kind:        primary. It is the document under examination; it owns every claim
             about its own problem statement, method, and results. Read in full
             via the arXiv PDF (pages 1-6, verified firsthand) and the ar5iv
             full-text render for the CIFAR section and Table 6.
Establishes: The degradation problem (deeper plain nets have higher TRAINING
             error, not overfitting); the residual formulation F(x)+x with
             identity shortcut connections; depths 18/34/50/101/152 on ImageNet
             and 110/1202 on CIFAR-10; single-model and 3.57% ensemble ImageNet
             top-5 error; the five-task ILSVRC/COCO 2015 sweep; FLOPs vs VGG;
             the explicit "not vanishing gradients" argument; and the explicit
             forecast of applicability to "vision and non-vision problems."
Paraphrase:  Stacking layers onto a plain convolutional net past a point raised
             its training error, an optimization failure the authors separate
             from overfitting and from vanishing gradients (which they say
             batch normalization had already handled). Reformulating each block
             to learn a residual F(x)=H(x)-x and adding a parameter-free
             identity shortcut so the block computes F(x)+x reversed this: the
             34-layer residual net beat the 18-layer one where the 34-layer
             plain net had lost to the 18-layer plain net. Scaled to 152 layers
             the residual net reached lower error than VGG at lower compute; an
             ensemble hit 3.57% top-5 and won five 2015 competition tracks.
Locators:    Abstract; Sec. 1 (Introduction), incl. Fig. 1 caption and the
             degradation paragraph, p.1; the generality forecast at end of Sec.
             1, p.2; Fig. 2 and Sec. 3.1-3.2 (residual formulation, Eqn. 1),
             p.2; Fig. 3 caption (FLOPs), p.4; Table 1 (FLOPs by depth), p.5;
             Table 2 (plain vs ResNet, 18/34), p.5; the "unlikely...vanishing
             gradients" argument, Sec. 4.1, p.5; Tables 3-5 (single-model and
             ensemble ImageNet), p.6; CIFAR Sec. 4.2 and Table 6 (via ar5iv).
Quote:       "such degradation is not caused by overfitting, and adding more
             layers to a suitably deep model leads to higher training error"
             (Sec. 1, p.1). "This strong evidence shows that the residual
             learning principle is generic, and we expect that it is applicable
             in other vision and non-vision problems" (end of Sec. 1, p.2). "We
             argue that this optimization difficulty is unlikely to be caused
             by vanishing gradients... So neither forward nor backward signals
             vanish" (Sec. 4.1, p.5).
```

```text
URL:         https://arxiv.org/abs/1603.05027
Kind:        primary. Same authors' follow-up (ECCV 2016); it owns its own
             ablation results and its analysis of why identity shortcuts help.
Establishes: That a clean identity mapping on the skip path lets forward and
             backward signals pass directly between any two blocks, and that a
             re-ordered ("pre-activation") residual unit trains more easily and
             generalizes better than the original 2015 block. It reports a
             1001-layer ResNet at 4.62% error on CIFAR-10.
Paraphrase:  The 2015 block was not the last word: keeping the shortcut a pure
             identity and moving activations improves signal propagation enough
             to train a 1001-layer net and lower CIFAR-10 error below the
             original design. This is the mechanistic account of "why residuals
             help" and a correction to the first paper's specific block.
Locators:    Abstract; the propagation analysis is the paper's central section.
Quote:       "the forward and backward signals can be directly propagated from
             one block to any other block, when using identity mappings as the
             skip connections and after-addition activation."
```

```text
URL:         https://arxiv.org/abs/1605.06431
Kind:        primary. Independent group (Veit, Wilber, Belongie, Cornell; NIPS
             2016); owns its lesion and gradient-path experiments firsthand.
Establishes: The "ensemble of relatively shallow paths" reading. A residual net
             is an implicit collection of many paths of different lengths; the
             gradient during training comes from short paths, not the full
             depth; and deleting a layer from a trained ResNet at test time
             barely dents accuracy, whereas deleting a VGG layer collapses it.
Paraphrase:  This complicates the paper's own "depth" headline. Very deep
             residual nets may work not because all 110 layers are used end to
             end, but because they behave like an ensemble of much shallower
             networks; only short paths carry meaningful gradient. Their
             resilience to layer removal is the evidence.
Locators:    Abstract; lesion study Sec. 4.1 (Figs. 3-4); path-length gradient
             analysis Sec. 5 (Fig. 6).
Quote:       "almost all of the gradient updates during training come from paths
             between 5 and 17 modules long" (Sec. 5). "most of the gradient in a
             residual network with 110 layers comes from paths that are only
             10-34 layers deep" (Abstract). Deleting any single VGG layer
             "reduces performance to chance levels," while for ResNet "no other
             block removal lead to a noticeable change" (Sec. 4.1).
```

```text
URL:         https://arxiv.org/abs/1712.09913
Kind:        primary. Li, Xu, Taylor, Studer, Goldstein (NeurIPS 2018); owns
             its own visualization method and the surfaces it produces.
Establishes: That skip connections reshape the optimization landscape. Without
             them, a deep net's loss surface turns chaotic and non-convex as
             depth grows; with them it stays smooth and near-convex, which is
             why the deep net is trainable at all.
Paraphrase:  A third mechanistic account, geometric rather than signal- or
             ensemble-based: the residual connection keeps the loss surface a
             navigable bowl instead of a fractured one as layers pile up. Its
             ResNet-56 with/without-skip figure is the field's canonical picture
             of the effect.
Locators:    Abstract; the "Shortcut Connections" analysis (Sec. 5-6); the
             headline visualization is Figure 1.
Quote:       "as network depth increases, the loss surface of the VGG-like nets
             spontaneously transitions from (nearly) convex to chaotic." Fig. 1
             caption: "The loss surfaces of ResNet-56 with/without skip
             connections."
```

```text
URL:         https://arxiv.org/abs/1706.03762
Kind:        primary for the reuse claim. "Attention Is All You Need" (Vaswani
             et al., 2017) owns the transformer's design; it states firsthand
             that its sub-layers use a residual connection and cites this
             paper. (It is secondary about ResNet itself, but primary about the
             fact that transformers reuse the trick.)
Establishes: That the residual connection is a load-bearing part of the
             transformer's "Add & Norm" step, around every encoder and decoder
             sub-layer, and that the transformer authors attribute it to He et
             al.'s ResNet.
Paraphrase:  The present-day payoff, sourced. The transformer does not treat
             residuals as optional; every attention and feed-forward sub-layer
             is wrapped in one, and the paper points back to ResNet for it.
Locators:    Sec. 3.1 (Encoder and Decoder Stacks); reference [11] in the
             bibliography.
Quote:       "We employ a residual connection [11] around each of the two
             sub-layers, followed by layer normalization. That is, the output of
             each sub-layer is LayerNorm(x + Sublayer(x))" (Sec. 3.1).
             Reference [11]: "Kaiming He, Xiangyu Zhang, Shaoqing Ren, and Jian
             Sun. Deep residual learning for image recognition. In ... CVPR,
             pages 770-778, 2016."
```

```text
URL:         https://www.semanticscholar.org/paper/2c03df8b48bf3fa39054345bafabfeff15bfd11d
Kind:        secondary. A citation index aggregating others' references to the
             paper; it reports on the paper's reach from outside, does not own
             any claim in it.
Establishes: A dated measure of the paper's fame. As of 2026-08-07 the
             Semantic Scholar record lists 235,644 citations and 32,660 "highly
             influential" citations, with venue CVPR 2016 (DOI
             10.1109/cvpr.2016.90). Supports "one of the most-cited papers in
             all of science" as a defensible order-of-magnitude claim, not an
             exact rank.
Paraphrase:  Retrieved via the Semantic Scholar Graph API for arXiv:1512.03385.
             A six-figure citation count from a single index confirms the paper
             sits among the most-cited scientific works of any field; the exact
             figure drifts daily and differs across indexes (Google Scholar
             typically reports a higher number).
Locators:    Semantic Scholar Graph API record for arXiv:1512.03385, fields
             citationCount / influentialCitationCount, read 2026-08-07.
Quote:       (none; numeric record)
```

## Contradictions

- **Against the brief/commission premise.** The brief asks to "confirm from
  text" that the paper "did not claim the residual trick would generalize to
  other architectures." The text says the opposite: "the residual learning
  principle is generic, and we expect that it is applicable in other vision and
  non-vision problems" (end of Sec. 1). It is a forward-looking expectation, not
  a demonstration, and names no architecture. The writer can still say the paper
  did not *show* generalization and did not foresee transformers, but must not
  claim it made no generalization claim at all.
- **Against the popular "ResNet solved vanishing gradients" story.** The paper
  explicitly rejects this for its own setting: the plain nets are trained with
  batch normalization, "neither forward nor backward signals vanish," and the
  degradation is a separate optimization difficulty (Sec. 4.1). The commission's
  "optimization failure, not just added layers" framing is correct, but the
  specific mechanism is not the one most retellings assume.
- **Depth alone did not drive the gain (supports the angle).** The 1202-layer
  CIFAR-10 net trained fine (training error <0.1%, "no optimization difficulty")
  yet scored 7.93% test error, WORSE than the 110-layer net's 6.43%. The paper
  attributes this to overfitting on a small dataset, not optimization. This
  directly refutes "just add more layers" and belongs in the lesson honestly.
- **The paper's "depth" headline vs later understanding.** Veit et al. argue the
  useful computation runs through short paths (5-17 modules), so a 110-layer net
  behaves like an ensemble of far shallower ones. This does not contradict the
  results, but it complicates the "we made 152 real layers work" reading; the
  gain is better framed as trainability, which the commission already prefers.
- **The 2015 block was not optimal.** The same authors' 2016 follow-up shows a
  re-ordered identity-mapping unit trains better and reaches 4.62% on CIFAR-10
  with 1001 layers, i.e. the original paper's specific residual block was
  quickly improved. Worth a sentence so the lesson does not present the 2015
  design as final.

## Numbers

```text
Figure: degradation example: 20-layer vs 56-layer "plain" net, deeper has
        higher TRAINING and test error on CIFAR-10
Owner:  ResNet paper (arXiv:1512.03385), Fig. 1, p.1
Scope:  CIFAR-10; plain (non-residual) nets; training-error curve is the point
```

```text
Figure: ImageNet val top-1 error (%, 10-crop): plain-18 27.94, plain-34 28.54,
        ResNet-18 27.88, ResNet-34 25.03
Owner:  ResNet paper, Table 2, p.5
Scope:  ImageNet-2012 validation (50k images); 10-crop testing; ResNets here
        have no extra params vs plain counterparts. Shows the reversal: plain
        gets worse 18->34, residual gets better 18->34.
```

```text
Figure: "the 34-layer ResNet is better than the 18-layer ResNet (by 2.8%)";
        "the 34-layer ResNet reduces the top-1 error by 3.5%" vs plain-34
Owner:  ResNet paper, Sec. 4.1, p.5
Scope:  ImageNet validation, top-1
```

```text
Figure: single-model ImageNet val error: ResNet-50 20.74/5.25, ResNet-101
        19.87/4.60, ResNet-152 19.38 top-1 / 4.49 top-5
Owner:  ResNet paper, Table 4, p.6 (multi-scale, fully-convolutional testing)
Scope:  ImageNet-2012 validation; top-1/top-5 %. (Table 3, 10-crop, gives the
        weaker ResNet-152 5.71 top-5 -- cite the test-time method with the
        number.) Single-model best top-5 = 4.49%.
```

```text
Figure: 3.57% top-5 error (ensemble), ImageNet test set; 1st place ILSVRC 2015
Owner:  ResNet paper, Abstract and Table 5, p.6 (reported by the test server)
Scope:  ImageNet-2012 test set (100k images); ensemble of residual nets
```

```text
Figure: ILSVRC/COCO 2015 sweep -- 1st place on 5 tracks: ImageNet
        classification, ImageNet detection, ImageNet localization, COCO
        detection, COCO segmentation; "28% relative improvement" on COCO
        detection
Owner:  ResNet paper, Abstract, p.1
Scope:  2015 competition results; the 28% figure is relative improvement on the
        COCO object-detection dataset
```

```text
Figure: FLOPs by depth: 18=1.8e9, 34=3.6e9, 50=3.8e9, 101=7.6e9, 152=11.3e9;
        VGG-19 = 19.6e9; VGG-16 test error 28.07 top-1 / 9.33 top-5
Owner:  ResNet paper, Table 1 (FLOPs) p.5; Fig. 3 caption (VGG-19 19.6e9) p.4;
        Table 3 (VGG-16 error) p.6
Scope:  Multiply-add FLOPs per forward pass; ImageNet. Backs "152 layers, 8x
        deeper than VGG, at lower complexity" -- 11.3e9 vs 19.6e9.
```

```text
Figure: CIFAR-10 test error: ResNet-110 = 6.43% (mean 6.61 +/- 0.16 over 5
        runs), 1.7M params; ResNet-1202 = 7.93%, 19.4M params, training error
        <0.1% and "no optimization difficulty"
Owner:  ResNet paper, Table 6 and Sec. 4.2 (CIFAR-10 and Analysis), read via
        ar5iv full-text render
Scope:  CIFAR-10 (small dataset); the 1202-layer net trains fine but overfits,
        the honest counter to "deeper is always better"
```

```text
Figure: 1001-layer ResNet = 4.62% error on CIFAR-10 (improved residual unit)
Owner:  He et al. 2016, Identity Mappings (arXiv:1603.05027), Abstract
Scope:  CIFAR-10; pre-activation identity-mapping block
```

```text
Figure: gradient carried by paths of 5-17 modules (paper body) / "10-34 layers
        deep" (abstract) in a 110-layer ResNet
Owner:  Veit et al. 2016 (arXiv:1605.06431), Sec. 5 / Abstract
Scope:  ImageNet/CIFAR ResNets; "modules" (each ~2-3 layers) vs "layers"
        accounts for the two numbers; report the unit with the figure
```

```text
Figure: 235,644 citations; 32,660 highly influential citations (as of
        2026-08-07)
Owner:  Semantic Scholar index record for arXiv:1512.03385
Scope:  Single index; a comparison, not an exact rank. Google Scholar reports
        a higher count. Use as "hundreds of thousands of citations."
```

## Source assets

```text
Asset: Figure 1 -- CIFAR-10 training-error (left) and test-error (right) curves
       for 20-layer vs 56-layer plain nets, ResNet paper p.1
Shows: The degradation problem itself: the deeper (56-layer) plain net sits
       ABOVE the shallower (20-layer) one on the TRAINING curve, the single
       image that proves "not overfitting." This is the lesson's central visual.
Crop:  Must retain the training-error (left) panel with both curves labeled and
       the y-axis; the training panel is the load-bearing half. Do not crop to
       only the test-error panel, which would lose the "training error" point.
```

```text
Asset: Figure 2 -- the residual building block diagram (x -> weight layers ->
       F(x), with an identity shortcut arrow bypassing them, summed to F(x)+x),
       ResNet paper p.2
Shows: What a skip connection is, in one picture: the input is added back to the
       block's output. Anchors the mechanism before any equation.
Crop:  Retain the identity/shortcut arrow and the addition node; omitting the
       curved bypass arrow destroys the point.
```

```text
Asset: Figure 4 -- ImageNet training curves, plain-18/34 (left) vs ResNet-18/34
       (right), ResNet paper p.5
Shows: The reversal on real ImageNet scale: on the left the 34-layer plain net
       is worse than the 18-layer; on the right the 34-layer ResNet is better.
       Pairs the CIFAR toy result with the headline dataset.
Crop:  Keep both panels side by side; the contrast is the whole content. Retain
       the 18/34 curve labels.
```

```text
Asset: Figure 1 of Li et al. 2018 -- 3D loss surfaces of ResNet-56 with vs
       without skip connections (arXiv:1712.09913)
Shows: A smooth bowl (with skip connections) beside a jagged, chaotic surface
       (without). The most vivid available answer to "why does the skip
       connection make depth trainable." Strong candidate if the lesson wants
       one figure on mechanism.
Crop:  Keep both surfaces for the contrast; retain the with/without labels.
       This is a different paper's figure -- attribute to Li et al. 2018.
```

```text
Asset: Table 1 (FLOPs by depth) and Fig. 3 caption (VGG-19 = 19.6e9 FLOPs),
       ResNet paper
Shows: The "8x deeper, lower complexity" claim as concrete numbers (ResNet-152
       11.3e9 vs VGG-19 19.6e9). Better as a two-row comparison than prose.
Crop:  If excerpted, keep the 152-layer column and a VGG reference number.
```

## Discarded

```text
URL: https://ar5iv.org/abs/1512.03385 -- redirects to ar5iv.labs.arxiv.org; a
     transport host, not the source's home. Used only to reach the full text;
     the citable address is https://arxiv.org/abs/1512.03385.
URL: https://www.analyticsvidhya.com/blog/2023/02/deep-residual-learning-for-image-recognition-resnet-explained/
     -- secondary blog explainer surfaced in search; adds nothing the primary
     does not own, and paraphrases the "vision and non-vision" line rather than
     quoting it. Not needed.
URL: https://viso.ai/deep-learning/resnet-residual-neural-network/ -- secondary
     explainer; same reason. Rejected as padding.
```
