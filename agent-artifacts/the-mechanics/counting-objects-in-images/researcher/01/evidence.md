# Evidence: the-mechanics/counting-objects-in-images (01)

Every link in the commissioned causal chain is owned by a primary source. The
CLIP text encoder's architecture and its documented weakness at counting come
from the CLIP paper itself (Radford et al.). Its bag-of-words behavior on order,
relation, and attribution is measured by the ARO benchmark (Yuksekgonul et al.).
That the encoder specifically fails at quantity, and why caption data makes exact
counts scarce, is owned outright by "Teaching CLIP to Count to Ten" (Paiss et
al.), which also supplies a before/after counting-accuracy figure. The diffusion
side, denoising from noise steered by the text embedding through cross-attention
with no component that tracks a count, comes from the Latent Diffusion paper
(Rombach et al.) for the mechanism and "Make It Count" (Binyamin et al.) for the
absence of any counting/identity component. Official acknowledgment that a leading
system inherits this comes from Google's Imagen paper, which states plainly that
"CLIP is ineffective at counting" and whose DrawBench includes a counting
category. Measured counting-accuracy figures across many current models, and the
finding that the failure persists and that prompt refinement does not fix it,
come from T2I-CompBench++ (Huang et al.) and T2ICountBench (Guo et al., 2025). A
secondary explainer (The Conversation) confirms the lay framing.

Where the record is thin, and the writer must be careful: (1) the arXiv PDFs
returned as undecodable binary, so every reading below came through the HTML
mirror (ar5iv / arxiv.org/html) via the fetch tool's summarization layer, not
from raw parsed tables. Qualitative mechanism claims are reliable and several are
verbatim, but any exact table-cell percentage carries transcription risk and
should be re-confirmed against the paper before it is quoted as a precise number.
(2) The chain has two distinct loci of failure, the encoder's weak
representation of quantity AND the generation process having no per-object-identity
or counting step, and the sources split on which they emphasize. Both are
supported; the writer should present them as complementary causes, not collapse
everything onto the text encoder. This is expanded under Contradictions.

The evidence does NOT undermine the commissioned "still broken" angle. It
supports it, with one honest boundary: for small counts (roughly one to five
objects) the best current models are right much of the time, and several
demonstrated fixes exist, so the article must locate the failure precisely (worst
at higher counts, unsolved in general) rather than claim the models can never
count.

## Sources

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. Radford et al. (OpenAI) author both the CLIP model and the
             claim about what its text encoder is and where it is weak. It owns
             the encoder description and the counting-limitation statement.
Establishes: (a) the text encoder architecture and how the text embedding is
             produced; (b) that CLIP struggles with counting as an abstract,
             systematic task, and is near-random on a counting dataset.
Paraphrase:  The text encoder is a Transformer; the activations of its highest
             layer at the [EOS] token are the text feature, layer-normalized and
             linearly projected into the shared image-text embedding space. In
             the Limitations section the authors name counting the number of
             objects in an image as a task CLIP does poorly, and list CLEVRCounts
             among datasets where zero-shot CLIP is weak / near random.
Locators:    Sec 2.4 / "The Model" (text encoder); Sec 6 "Limitations."
Quote:       "As a base size we use a 63M-parameter 12-layer 512-wide model with
             8 attention heads." / "The transformer operates on a lower-cased
             byte pair encoding (BPE) representation of the text with a 49,152
             vocab size. For computational efficiency, the max sequence length
             was capped at 76." / "the activations of the highest layer of the
             transformer at the [EOS] token are treated as the feature
             representation of the text which is layer normalized and then
             linearly projected into the multi-modal embedding space." / "CLIP
             also struggles with more abstract and systematic tasks such as
             counting the number of objects in an image."
```

```text
URL:         https://arxiv.org/abs/2210.01936
Kind:        primary. Yuksekgonul et al. author the ARO benchmark and the
             finding. It owns the measured claim that CLIP-style VLMs behave
             like bags-of-words on order, relation, and attribution.
Establishes: that state-of-the-art VLMs including CLIP have poor relational
             understanding, blunder on object-attribute binding, and show a
             severe lack of order sensitivity; and that retrieval can be won
             without using composition/order, which is why the models never
             learn to represent it.
Paraphrase:  ARO ("Attribution, Relation, and Order") tests VLMs on Visual
             Genome Relation and Attribution and on COCO- and Flickr30k-Order,
             over 50,000 cases. CLIP scores near chance on relation and
             attribution and collapses on word order. Because contrastive
             pretraining rewards retrieval, and retrieval on these datasets can
             be won without word order or composition, the model is never forced
             to encode them. Composition-aware hard-negative mining (NegCLIP)
             substantially closes the gap.
Locators:    Abstract; results tables (VG-Relation, VG-Attribution, COCO-Order,
             Flickr30k-Order); the retrieval-shortcut analysis section.
Quote:       "We show where state-of-the-art VLMs have poor relational
             understanding, can blunder when linking objects to their
             attributes, and demonstrate a severe lack of order sensitivity." /
             "it is possible to perform well on retrieval over existing datasets
             without using the composition and order information."
```

```text
URL:         https://arxiv.org/abs/2302.12066
Kind:        primary. Paiss et al. (Google Research, Tel Aviv U., Weizmann)
             author both the diagnosis (CLIP cannot count) and the CountBench
             benchmark and the fix. It owns the quantity-specific encoder claim
             and the caption-scarcity cause.
Establishes: (a) CLIP fails to encode counting; (b) WHY, in caption statistics:
             captions specifying an exact count become extremely rare as the
             count rises and are skewed toward small numbers; (c) that counting
             barely helps the contrastive objective, so the encoder has no
             pressure to learn it; (d) a measured before/after counting accuracy.
Paraphrase:  CLIP-style VLMs fail to encapsulate compositional concepts such as
             counting. Accurate-count captions are rare in web data and get
             rarer as the number grows; beyond about six objects captions use
             "a group of" or "many" instead of a number. Counting also does
             little for the discriminative training objective because nouns and
             object categories are more informative, so the encoder never needs
             to represent exact quantity. Their CountBench (540 verified
             image-text pairs) measures the gap and their fine-tuned model
             closes much of it.
Locators:    Introduction; the "why counting is hard to learn" / data-analysis
             section; CountBench definition; results.
Quote:       "they fail to encapsulate compositional concepts such as counting."
             / "Captions that accurately specify the number of objects become
             extremely rare in the data as the number of objects increases ...
             For more than six objects, captions would typically contain a
             general form of quantity, e.g., 'a group of ...' or 'many ...',
             rather than an accurate count." / "The task of counting ... does not
             sufficiently contribute to the VLM's discriminative training
             objective. This is because other textual and visual features (e.g.,
             nouns and object categories) are more informative."
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. Rombach et al. author the Latent Diffusion / Stable
             Diffusion architecture. It owns the mechanism by which text steers
             generation.
Establishes: that diffusion generates by iterative denoising, and that text
             conditioning enters through cross-attention layers added to the
             UNet, with the query from the image features and key/value from the
             text encoder output. There is no counting component in this
             description; conditioning is a soft attention over the whole latent.
Paraphrase:  The model is a sequence of denoising steps. The text prompt is
             encoded by a domain-specific encoder; cross-attention layers in the
             UNet take their query from the (flattened) intermediate image
             features and their key and value from the text embedding, so the
             prompt modulates the whole denoising field. Attention is
             softmax(QK^T/sqrt(d))V.
Locators:    Abstract; Sec 3.3 "Conditioning Mechanisms" (cross-attention).
Quote:       "By introducing cross-attention layers into the model architecture,
             we turn diffusion models into powerful and flexible generators for
             general conditioning inputs such as text or bounding boxes."
```

```text
URL:         https://arxiv.org/abs/2406.10210
Kind:        primary. Binyamin et al. (Bar-Ilan, NVIDIA, Tel-Aviv U.), CVPR
             2025. Authors the claim that diffusion has no counting/identity
             mechanism and a generation-side fix.
Establishes: (a) controlling object count with text is hard for diffusion
             models; (b) the reason is on the generation side: the model would
             need to hold a separate identity for each instance and do a global
             count implicitly, which nothing in the process does; (c) a measured
             counting-accuracy improvement over baselines.
Paraphrase:  Even successful text-to-image diffusion models find controlling the
             depicted number of objects surprisingly hard. Getting counts right
             would require the model to keep a separate sense of identity for
             every instance, even overlapping identical ones, and carry out a
             global computation implicitly during generation; existing models
             have no such mechanism. Their CountGen method identifies and
             corrects object instances mid-denoising and raises count accuracy.
Locators:    Abstract; method motivation; evaluation on CoCoCount and
             T2I-CompBench-Count.
Quote:       "Despite the unprecedented success of text-to-image diffusion
             models, controlling the number of depicted objects using text is
             surprisingly hard." / "the generative model needs to keep a sense of
             separate identity for every instance of the object ... and then
             carry out a global computation implicitly during generation."
```

```text
URL:         https://arxiv.org/abs/2205.11487
Kind:        primary. Saharia et al. (Google) author Imagen and DrawBench. Used
             here as an official statement from a leading text-to-image system.
Establishes: (a) an official acknowledgment that CLIP is ineffective at
             counting; (b) that a leading system's own eval set (DrawBench)
             carries a dedicated counting category; (c) that this class of
             system conditions the diffusion model on a frozen text encoder via
             cross-attention, matching the mechanism the article traces.
Paraphrase:  Imagen encodes the prompt with a frozen T5-XXL encoder and
             conditions the diffusion model on the full sequence of text
             embeddings by adding cross-attention at multiple resolutions.
             DrawBench spans 11 prompt categories testing capabilities including
             the number of objects, spatial relations, and text rendering. In
             discussing evaluation the paper states that CLIP is ineffective at
             counting.
Locators:    Sec 2.1 (pretrained text encoders / T5-XXL); Sec 2.5 (cross-
             attention conditioning); Sec 3 (DrawBench categories and the CLIP
             counting remark).
Quote:       "DrawBench contains 11 categories of prompts, testing different
             capabilities of models such as the ability to faithfully render
             different colors, numbers of objects, spatial relations, text in
             the scene, and unusual interactions between objects." / "CLIP is
             ineffective at counting."
```

```text
URL:         https://arxiv.org/abs/2307.06350
Kind:        primary. Huang et al. author T2I-CompBench (and the extended
             T2I-CompBench++). Owns a measured numeracy/counting score across
             many current text-to-image models.
Establishes: numeracy (generating a specified number of objects, one to eight)
             is a standing compositional weakness, with per-model scores that let
             the writer show older vs newer systems.
Paraphrase:  The benchmark's numeracy category has prompts naming object
             categories with numeric quantities from one to eight, evaluated with
             a detection-based (UniDet) metric. Scores rise with model
             generation but stay well short of reliable: Stable Diffusion v1.4
             ~0.45, SD v2 ~0.46, DALL-E 3 ~0.59, Stable Diffusion 3 ~0.62,
             FLUX.1 ~0.62 (higher is better; scores are detection-based, not
             plain percent-correct).
Locators:    Numeracy category definition; numeracy results table.
Quote:       "Each prompt in this category involves one or multiple object
             categories with numerical quantities, ranging from one to eight."
```

```text
URL:         https://arxiv.org/abs/2503.06884
Kind:        primary. Guo et al. author T2ICountBench and the evaluation. Owns
             the "still broken across current models" figures and the
             prompt-refinement-does-not-help finding.
Establishes: (a) all state-of-the-art diffusion models tested fail to generate
             the correct number of objects, and accuracy drops sharply as the
             requested count rises; (b) prompt refinement makes counting worse,
             not better; (c) per-model and per-difficulty accuracy figures.
Paraphrase:  Across 15 current models evaluated on counts from one to fifteen,
             none reliably produces the requested number. Accuracy is high for
             small counts and collapses as the count grows. Four families of
             prompt refinement all reduced accuracy rather than helping, cutting
             average accuracy across the 15 models by more than 40% relative to
             the plain prompt.
Locators:    Abstract; per-model results; per-difficulty (easy/medium/hard)
             breakdown; prompt-refinement experiments.
Quote:       "all state-of-the-art diffusion models fail to generate the correct
             number of objects, with accuracy dropping significantly as the
             number of objects increases." / "All four types of prompt refinement
             lead to worse performance ... the average accuracy across 15 models
             decreases by more than 40% relative to the original accuracy."
```

```text
URL:         https://theconversation.com/if-ai-image-generators-are-so-smart-why-do-they-struggle-to-write-and-count-208485
Kind:        secondary. A reported explainer for a general audience by an AI
             academic; it interprets the primary literature, it does not own the
             finding. Author: Seyedali Mirjalili, Professor of Artificial
             Intelligence, Torrens University Australia. The Conversation, 4 July
             2023.
Establishes: the lay framing the reader has likely met: models lack a clear
             concept of a quantity like "four," and the diversity of quantities
             in training images undermines an exact count. Useful for register
             and for confirming the phenomenon is publicly noted; not a source
             for any mechanism claim on its own.
Paraphrase:  AI image generators lack a clear understanding of quantities such
             as the abstract concept of "four"; asked for four apples they draw
             on many images of apples in varying amounts and often return the
             wrong number. The diversity of associations in training data
             undermines quantity accuracy.
Locators:    Body of the article.
Quote:       "AI models lack a clear understanding of quantities, such as the
             abstract concept of 'four'."
```

## Contradictions

- Two causes, not one. The article's spine ("the encoder is quantity-weak") is
  owned by CLIP, ARO, and Paiss. But "Make It Count" locates the difficulty on
  the generation side: the model would have to keep a separate identity for each
  instance and count implicitly during denoising, and nothing does. These are
  complementary, not rival, but they are different claims. If the draft says the
  wrong number comes out ONLY because the text encoder can't represent quantity,
  it overstates what the encoder sources own and drops the generation-side cause
  that Make It Count establishes. Present both: a prompt whose count is weakly
  encoded, painted by a process with no counting or per-object-identity step.

- "Substantially solved?" Tested against the angle, and the angle holds, with a
  boundary. Small counts are often right: T2ICountBench reports roughly 60-80%
  accuracy for one-to-five objects even as it falls below 10% for eleven-to-
  fifteen; the failure is a function of count size, worst at larger numbers.
  Newer models beat older ones on T2I-CompBench numeracy (SD1.4 ~0.45 vs SD3 /
  FLUX ~0.62). So "image generators can't count" is too strong as stated; the
  accurate claim is that no current model counts reliably, especially past a
  handful of objects, and that the trend is improving without being solved.

- Fixes exist, which tensions any "fundamental / can-never" framing. NegCLIP
  (ARO) improves order/composition; CountBench fine-tuning roughly doubles CLIP's
  counting accuracy (see Numbers); CountGen / Make It Count raises generation
  count-accuracy well above its baseline. The honest boundary for the open-
  question mark: these are targeted interventions (hard negatives, count-aware
  captions, mid-denoising instance correction), not evidence that scale or better
  captions alone have solved it. And T2ICountBench found the cheapest
  intervention, prompt refinement, makes counting worse, so the fix is not on the
  user's side.

- One official-source caveat. The commission named the DALL-E 3 system card /
  "Improving Image Generation with Better Captions" as a candidate for the
  official caption-quality acknowledgment. Both OpenAI PDFs exceeded the fetch
  tool's size limit and could not be read firsthand, so neither is cited. The
  official acknowledgment is instead carried by Imagen ("CLIP is ineffective at
  counting," a DrawBench counting category), and the caption-scarcity cause by
  Paiss. If the writer wants the specific DALL-E 3 caption-quality thesis, it is
  not yet primary-sourced in this record and should not be attributed to OpenAI
  from memory.

## Numbers

```text
Figure: CLIP text encoder = 63M params, 12 layers, 512 wide, 8 heads; BPE vocab
        49,152; max sequence length 76; text feature = [EOS] activations of the
        top layer, projected into the shared embedding space
Owner:  CLIP paper (2103.00020), Sec 2.4
Scope:  base-size CLIP text encoder as specified; architecture fact, not a
        measurement
```

```text
Figure: CLIP is near chance on ARO relation/attribution and collapses on word
        order. Readings via the HTML mirror: VG-Relation ~59% and VG-Attribution
        ~62-63% against a 50% two-choice chance baseline; COCO-Order ~46% and
        Flickr30k-Order ~59% on the order tasks (lower chance baseline). NegCLIP
        lifts order/composition sharply (e.g. COCO-Order ~46% -> ~86%).
Owner:  ARO / Yuksekgonul (2210.01936), results tables
Scope:  ARO test set, >50,000 cases; specific CLIP variant per cell. TREAT THE
        PERCENTAGES AS APPROXIMATE. The fetch summarizer returned VG-Relation as
        both ~59% and ~63% in different sentences, so the exact cell must be
        re-confirmed against the paper before any precise figure is quoted. The
        qualitative finding (near chance on relation/attribution, order collapse)
        is firmly owned. ARO measures order/relation/attribution, NOT counting;
        it is the bag-of-words evidence, not the counting number.
```

```text
Figure: CLIP-B/32 counting accuracy on CountBench 31.67%, rising to 75.93% after
        count-aware fine-tuning; mean count deviation 1.53 -> 0.49
Owner:  Teaching CLIP to Count to Ten (2302.12066)
Scope:  CountBench, 540 verified image-text pairs; this is the ENCODER's counting
        accuracy (does the image match a counted caption), not a generator's
        output accuracy. Read via HTML mirror; re-confirm the two decimals if
        quoted exactly.
```

```text
Figure: T2I-CompBench(++) numeracy scores (one-to-eight objects, UniDet metric,
        higher better): SD v1.4 ~0.45, SD v2 ~0.46, Composable+SD2 ~0.43,
        DALL-E 3 ~0.59, Stable Diffusion 3 ~0.62, FLUX.1 ~0.62
Owner:  T2I-CompBench++ (2307.06350), numeracy results
Scope:  1,000 numeracy prompts, counts one to eight; a detection-based composite
        score, NOT plain percent-of-images-correct. Do not present as "62%
        correct." Read via HTML mirror.
```

```text
Figure: Generation-side counting accuracy, one-to-fifteen objects: best model
        (Imagen-3) ~43% average; DALL-E 3 ~30%, FLUX 1.1 ~35%, SD 3.5 ~26%.
        By difficulty: easy (1-5 objects) ~60-80%, medium (6-10) ~10-30%, hard
        (11-15) <10% for nearly all. Prompt refinement lowers average accuracy
        by >40% relative.
Owner:  T2ICountBench / Guo et al. (2503.06884)
Scope:  15 models, counts 1-15, human-judged exact-count correctness. The
        per-model averages are single figures from the summarizer; re-confirm any
        exact per-model number before quoting. The pattern (high at small counts,
        collapse at large; refinement hurts) is the load-bearing, well-supported
        result.
```

```text
Figure: CountGen (Make It Count) generation count-accuracy: ~54% on CoCoCount vs
        ~26% for the SDXL baseline; ~48% on T2I-CompBench-Count vs ~29% for SDXL;
        reported to beat DALL-E 3 (~38% / ~36%) on those two
Owner:  Make It Count (2406.10210)
Scope:  Two count benchmarks; a targeted mid-denoising method, evidence that the
        generation-side failure is improvable, not solved. Body/table reading via
        HTML mirror; re-confirm exact figures if quoted.
```

## Source assets

```text
Asset: T2ICountBench accuracy-versus-requested-count curve/bars (per-difficulty
       easy/medium/hard breakdown), in Guo et al. (2503.06884)
Shows: the single clearest visual for the lesson, that accuracy is high for a
       few objects and collapses as the count grows, across many current models
Crop:  must retain the x-axis (object count / difficulty) and the downward trend;
       omit nothing that identifies which models are plotted if models are named
Note:  figure exists per the reading but was not visually confirmed; verify the
       exact chart and axis labels before rendering or describing it precisely
```

```text
Asset: CountBench qualitative image-text pairs and the failure examples, in
       Paiss et al. (2302.12066)
Shows: what "the encoder can't tell four from five" looks like concretely, and
       the caption forms ("a group of", "many") that replace exact counts at
       higher numbers
Crop:  keep a correct low-count pair beside a high-count pair to show the
       small-number skew; keep the caption text legible
Note:  not visually confirmed; confirm figure contents before use
```

```text
Asset: Make It Count / CountGen side-by-side generations (baseline wrong count
       vs corrected count), in Binyamin et al. (2406.10210)
Shows: the generation-side failure and that a targeted fix changes the count,
       supporting the "improvable, not solved" boundary
Crop:  keep matched prompts and both counts visible; do not crop out the
       requested-number label
Note:  not visually confirmed; confirm before use
```

```text
Asset: The cross-attention conditioning schematic of the Latent Diffusion UNet,
       in Rombach et al. (2112.10752)
Shows: where the text embedding enters generation (as key/value into UNet
       cross-attention), i.e. that conditioning is a soft attention over the
       whole latent with no counting stage
Crop:  keep the text-encoder-to-cross-attention path; a heavy crop loses the
       point, which is that the prompt touches the whole field at once
Note:  a diagram redraw is likely cleaner than the source figure for a lay reader
```

## Discarded

```text
URL: https://cdn.openai.com/papers/dall-e-3.pdf — "Improving Image Generation
     with Better Captions." Exceeded the fetch tool's 10MB size limit; could not
     be read firsthand, so not cited despite being a named candidate.
URL: https://cdn.openai.com/papers/DALL_E_3_System_Card.pdf — DALL-E 3 System
     Card. Also exceeded the fetch size limit; not read, not cited.
URL: https://openreview.net/forum?id=kL3pz7YSQF — OpenReview page for the
     T2ICountBench paper. Gated behind a browser-verification interstitial that
     returned no content; used the arXiv page (2503.06884) instead, which is the
     source's own page.
URL: https://arxiv.org/pdf/2103.00020 and https://arxiv.org/pdf/2210.01936 —
     the arXiv PDF endpoints returned undecodable binary. Not a rejection of the
     sources; the readable HTML mirrors (ar5iv / arxiv.org/html) were used for
     the same papers and are recorded as the abstract-page URLs above.
```
