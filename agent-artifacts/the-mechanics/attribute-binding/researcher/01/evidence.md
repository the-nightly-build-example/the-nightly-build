# evidence: the-mechanics/attribute-binding (01)

The evidence supports the commission's angle firmly on its settled half and
cleanly marks its open half. Binding failure is real, measured, and reproduces
across systems and prompt sets: on the standard compositional benchmark, Stable
Diffusion v1.4 scores 0.38 on color binding and 0.12 on spatial relationships
(0-1); an independent relational study found only ~22% of DALL-E 2 images matched
a basic relation prompt. The pipeline claims are owned by their primaries: latent
diffusion conditions the image generator on text through cross-attention (Rombach
et al.), and the CLIP text encoder is trained to align a whole caption with a
whole image, not to preserve which adjective modifies which noun (Radford et al.).
The localization is supported by two method papers that improve binding by
intervening on exactly the two suspected parts: StructureDiffusion restructures
the text encoding, Attend-and-Excite manipulates cross-attention. Where the
evidence is genuinely thin is the commission's own open question: the split of
blame. The two fix papers each favor the part they intervene on, and their own
numbers disagree about how much of the problem lives where. No single cited
primary gives a clean "one object works, two objects fail" accuracy pair; the
closest is Attend-and-Excite's full-prompt vs minimum-object CLIP gap. One
secondary survey argues the cause is architectural and that incremental fixes are
insufficient, which is a live challenge to the "just re-attach the attribute"
reading of fixability.

## Sources

```text
URL:         https://arxiv.org/abs/2307.06350
Kind:        primary. It owns the benchmark and the measured per-category scores.
             The authoring group (Huang, Sun, Xie, Li, Liu) built the prompt set
             and ran the evaluations; the numbers are theirs firsthand.
Establishes: That attribute and relation binding fails systematically, with
             measured rates on a 6,000-prompt (original) / 8,000-prompt (++) set
             spanning color, shape, texture binding, spatial and non-spatial
             relations, and complex compositions.
Paraphrase:  T2I-CompBench is a benchmark of compositional prompts in categories
             for attribute binding (color, shape, texture), object relationships
             (spatial, non-spatial), and complex compositions. Stable Diffusion
             and peers score low on binding and far lower still on spatial
             relationships. B-VQA (BLIP-VQA) scores attribute binding, UniDet
             scores spatial relations, CLIP scores non-spatial relations.
Locators:    Original: Huang et al., "T2I-CompBench," NeurIPS 2023 (Datasets &
             Benchmarks), proceedings hash f8ad010cdd9143dbb0e9308c093aff24. The
             arXiv id 2307.06350 now hosts the enhanced "T2I-CompBench++"
             (Huang, Duan, Sun, Xie, Li, Liu); the SD v1.4/v2 category scores
             below are the same values carried forward. Score tables VIII-XI in
             the ++ HTML (arxiv.org/html/2307.06350v3).
Quote:       "6,000 compositional text prompts from 3 categories (attribute
             binding, object relationships, and complex compositions) and 6
             sub-categories" (original benchmark composition).
```

```text
URL:         https://arxiv.org/abs/2208.00005
Kind:        primary. Conwell & Ullman designed the relation set, generated the
             images, and ran the human study; the ~22% figure is their firsthand
             measurement.
Establishes: That a text-to-image model (DALL-E 2) fails at basic relations
             systematically, not occasionally, judged by humans.
Paraphrase:  15 basic relations (8 physical: in, on, under, covering, near,
             occluded by, hanging over, tied to; 7 agentic: pushing, pulling,
             touching, hitting, kicking, helping, hindering) crossed with entity
             pairs gave 75 prompts, 18 images each, 1,350 images. 169 human
             judges (after 11 removed for failed attention checks) rated whether
             each image matched its prompt. Only ~22% matched overall; physical
             relations ~17%, agentic ~28%. Only three relations exceeded 25%
             average agreement (touching, helping, kicking) and none reached 50%.
             The authors read this as evidence the model lacks a grasp of even
             basic relations. Directional/reversibility failures appear (the
             model does not reliably distinguish a relation from its inverse).
Locators:    Abstract; Methods (relation and entity lists, stimulus counts);
             Results (overall and physical-vs-agentic rates); title "Testing
             Relational Understanding in Text-Guided Image Generation," 2022.
Quote:       "only ~22% of images matched basic relation prompts."
```

```text
URL:         https://arxiv.org/abs/2301.13826
Kind:        primary. Chefer et al. own the two named failure modes as diagnosed
             on Stable Diffusion, the method, and the reported metrics.
Establishes: (a) Cross-attention is a place the fault lives: intervening only on
             cross-attention activations at inference, without retraining or
             touching the encoder, substantially improves both subject presence
             and attribute binding. (b) Names the failure modes: "catastrophic
             neglect" and "incorrect attribute binding."
Paraphrase:  Stable Diffusion exhibits catastrophic neglect (one or more subjects
             missing) and attribute-binding failure (a color attaches to the
             wrong subject). Their method, Generative Semantic Nursing /
             Attend-and-Excite, edits cross-attention on the fly during inference
             so every subject token is strongly attended. Evaluated on three
             prompt sets: Animal-Animal ("a [animalA] and a [animalB]"),
             Animal-Object ("a [animal] and a [color][object]"), Object-Object
             ("a [colorA][objectA] and a [colorB][objectB]"), 66 pairs each, 64
             seeds per prompt. CLIP full-prompt similarity for SD is 0.83-0.84
             but minimum-object similarity is only 0.60-0.63, showing one object
             is captured while the other is neglected; Attend-and-Excite raises
             minimum-object similarity to 0.69-0.72. In a user study SD was
             preferred on 2.32% / 13.92% / 5.71% of the three sets vs
             Attend-and-Excite's 90.70% / 77.64% / 77.16%.
Locators:    Abstract; Sec. quantitative evaluation; Fig. 8 (CLIP similarities);
             Table 1 (text-text similarity); Table 2 (user study); Fig. 2
             (failure examples). SIGGRAPH 2023.
Quote:       the model "fails to correctly bind attributes (e.g., colors) to
             their corresponding subjects."
```

```text
URL:         https://arxiv.org/abs/2212.05032
Kind:        primary. Feng et al. own the encoder-side diagnosis and method and
             the reported improvements.
Establishes: (a) The text encoder is a place the fault lives: the CLIP encoder's
             causal attention blends each token with the tokens before it, so
             adjective and noun representations entangle. (b) Restructuring the
             text encoding with linguistic parse structure improves binding,
             which is evidence for encoder involvement, but the measured gains
             are small.
Paraphrase:  StructureDiffusion (training-free) parses the prompt and feeds
             structured noun-phrase encodings into the cross-attention keys and
             values, which the authors say carry object layout and content. On
             CC-500, human annotation of outputs: two objects present 38.0% vs
             34.5% baseline; two objects with correct colors 22.7% vs 19.2%
             baseline. User study on ABC-6K (attribute binding): 42.2% prefer
             StructureDiffusion, 35.6% baseline, 22.2% tie. The cause statement:
             "Due to the causal attention masks, tokens in the later part of a
             sequence are blended with the token semantics before them," and
             inaccurate cross-attention maps send an attribute's features to the
             wrong region.
Locators:    Abstract; method (structured cross-attention); user study tables;
             automatic-metric table (CC-500); cause discussion. ICLR 2023.
Quote:       "Due to the causal attention masks, tokens in the later part of a
             sequence are blended with the token semantics before them."
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. Rombach et al. own the latent-diffusion architecture and
             its text-conditioning mechanism.
Establishes: How a modern text-to-image pipeline maps text to image: a domain
             encoder turns the prompt into a set of vectors, and the image
             generator attends to those vectors through cross-attention while it
             denoises. This is the pipeline the commission needs at step 2.
Paraphrase:  A domain-specific encoder tau_theta projects the conditioning input
             y (e.g. a language prompt) to an intermediate representation
             tau_theta(y) in R^(M x d_tau) - a sequence of M vectors. This is
             mapped into the UNet's intermediate layers via a cross-attention
             layer Attention(Q,K,V) = softmax(QK^T / sqrt(d)) V, where Q projects
             the UNet's flattened intermediate features phi_i(z_t) and K and V
             both project tau_theta(y). So the image side supplies the queries and
             the text side supplies keys and values.
Locators:    Sec. 3.3 "Conditioning Mechanisms." Title "High-Resolution Image
             Synthesis with Latent Diffusion Models," CVPR 2022.
Quote:       "By introducing cross-attention layers into the model architecture,
             we turn diffusion models into powerful and flexible generators for
             general conditioning inputs such as text." And: "we introduce a
             domain specific encoder tau_theta that projects y to an intermediate
             representation tau_theta(y)".
```

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. Radford et al. own the CLIP text encoder and its training
             objective.
Establishes: Why the text side arrives without firm adjective-to-noun structure:
             CLIP's text encoder is a Transformer trained by a contrastive
             objective that matches a whole image to a whole caption, rewarding a
             pooled representation of the caption rather than word-level syntax.
Paraphrase:  CLIP learns image representations by predicting which whole caption
             goes with which whole image, contrastively, over 400 million
             (image, text) pairs. The text encoder is a Transformer; the training
             signal aligns the whole-caption embedding with the whole-image
             embedding. There is no objective that preserves which adjective binds
             which noun, which is the structural information binding needs
             downstream.
Locators:    Abstract; method (contrastive objective, dataset size); text-encoder
             description. Title "Learning Transferable Visual Models From Natural
             Language Supervision," 2021.
Quote:       "predicting which caption goes with which image is an efficient and
             scalable way to learn SOTA image representations from scratch on a
             dataset of 400 million (image, text) pairs."
```

```text
URL:         https://arxiv.org/abs/2210.10606
Kind:        primary. Rassin, Ravfogel & Goldberg own the observed word-to-concept
             failures in DALL-E 2.
Establishes: Independent corroboration that attributes "leak" and words are
             reused for the wrong role - the same phenomenon the commission calls
             an attribute landing on the wrong object.
Paraphrase:  DALL-E 2 does not enforce that each word plays a single role: a
             single attribute word can modify two entities, a word can act as
             both object and modifier, and properties transfer improperly between
             entities (semantic leakage). Documented qualitatively across many
             prompts; the paper reports categories of failure rather than a single
             headline rate.
Locators:    Abstract; failure taxonomy (polysemy, dual-role words, leakage).
             "DALLE-2 is Seeing Double: Flaws in Word-to-Concept Mapping in
             Text2Image Models," BlackboxNLP @ EMNLP 2022.
Quote:       the model "does not follow the constraint that each word has a single
             role in the interpretation, and sometimes re-use[s] the same symbol
             for different purposes."
```

```text
URL:         https://arxiv.org/abs/2511.10136
Kind:        secondary. Vatsa, Bharati & Singh synthesize other groups' benchmarks
             and methods; they report on the field rather than owning a new
             measurement of binding.
Establishes: Context for the settled/open line, and a steelman of the strongest
             opposing view: that the cause is architectural, not merely encoder
             entanglement, so incremental fixes will not resolve it.
Paraphrase:  A 2025 review of compositional fidelity across benchmarks and
             methods. It reports that models accurate on single primitives fail
             sharply when the primitives are combined, and argues the shortfall
             needs "fundamental advances in representation and reasoning rather
             than incremental adjustments," attributing failure in part to
             continuous attention architectures being ill-suited to discrete
             constraints and to metrics that reward plausibility over constraint
             satisfaction. Its primitive focus is negation, counting, and spatial
             relations more than color/attribute binding.
Locators:    Abstract; failure-mode discussion. "Right Looks, Wrong Reasons:
             Compositional Fidelity in Text-to-Image Generation," 2025.
Quote:       models "that are accurate on single primitives fail precipitously
             when these are combined"; the field needs "fundamental advances in
             representation and reasoning rather than incremental adjustments."
```

## Contradictions

1. The split of blame is unsettled, and the two fix papers pull in opposite
   directions. StructureDiffusion intervenes on the encoding and reports only a
   small lift (correct two-object color 19.2% -> 22.7%, +3.5 points; two objects
   present 34.5% -> 38.0%). Attend-and-Excite intervenes only on cross-attention,
   never touching the encoder, and reports a large lift (minimum-object CLIP
   similarity 0.60-0.63 -> 0.69-0.72; user preference 78-91% vs baseline's
   3-14%). In Attend-and-Excite's own user study, StructureDiffusion is barely
   ahead of raw Stable Diffusion (6.98% / 6.75% / 7.31% preferred). Read together,
   the larger fixable share sits at cross-attention, not the encoder - which
   complicates, without refuting, the commission's "the encoder hands over a bag
   of concepts" framing. Caveat: each paper favors the part it intervenes on and
   uses different prompt sets and metrics, so this is competing-method evidence,
   not a controlled decomposition. This is the open question, and the evidence
   marks it as open rather than settling it.

2. Fixability is contested. The method papers frame binding as substantially
   recoverable downstream. The Vatsa 2025 survey argues the opposite for
   composition generally: that continuous attention architectures are
   fundamentally unsuited to discrete constraints and that incremental fixes will
   not close the gap. Even the fix papers' post-fix absolute numbers stay low
   (correct two-object color 22.7%), which is consistent with the survey's
   pessimism. Steelman both: the fixes do move the numbers, and the ceiling they
   reach is still far from reliable.

3. Nothing contradicts the settled claim itself. The systematic failure and the
   general location of the cause (text conditioning + cross-attention) reproduce
   across DALL-E 2 (Conwell & Ullman; Rassin et al.) and Stable Diffusion
   (T2I-CompBench; Attend-and-Excite; StructureDiffusion), different model
   families with different text encoders, so the angle's settled half holds.

## Numbers

```text
Figure: Color binding 0.3765 (SD v1.4), 0.5065 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  B-VQA (BLIP-VQA) score, 0-1, over the color-binding prompt subset
```
```text
Figure: Shape binding 0.3576 (SD v1.4), 0.4221 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  B-VQA score, 0-1, shape-binding subset
```
```text
Figure: Texture binding 0.4156 (SD v1.4), 0.4922 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  B-VQA score, 0-1, texture-binding subset
```
```text
Figure: Spatial relationships 0.1246 (SD v1.4), 0.1342 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  UniDet score, 0-1, 2D-spatial subset. This is the lowest category and
        the sharpest illustration that relations fail worse than attributes.
```
```text
Figure: Non-spatial relationships 0.3079 (SD v1.4), 0.3127 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  CLIP score, 0-1, non-spatial subset
```
```text
Figure: Complex compositions 0.3080 (SD v1.4), 0.3386 (SD v2)
Owner:  T2I-CompBench / ++ (Huang et al.)
Scope:  3-in-1 metric, 0-1
```
```text
Figure: ~22% overall relation-match rate; ~17% physical, ~28% agentic
Owner:  Conwell & Ullman 2022 (DALL-E 2)
Scope:  Fraction of 1,350 images (75 prompts x 18) judged by 169 humans to match
        the relation prompt. Only 3 of 15 relations exceeded 25%; none reached 50%.
```
```text
Figure: SD full-prompt CLIP similarity 0.83-0.84 vs minimum-object 0.60-0.63
Owner:  Chefer et al. 2023 (Attend-and-Excite), Fig. 8
Scope:  CLIP text-image cosine, 0-1, three two-object prompt sets, 64 seeds each.
        The gap is the "one object captured, the other neglected/mis-bound"
        signature. Attend-and-Excite raises minimum-object to 0.69-0.72.
```
```text
Figure: Two objects with correct colors 22.7% vs 19.2% baseline (CC-500)
Owner:  Feng et al. 2022 (StructureDiffusion)
Scope:  Human annotation of generated images; also two-objects-present 38.0% vs
        34.5%. Shows an encoder-side fix helps only marginally.
```
```text
Figure: CLIP training set 400 million (image, text) pairs
Owner:  Radford et al. 2021 (CLIP)
Scope:  Contrastive whole-image / whole-caption objective; no word-level
        binding objective.
```

## Source assets

```text
Asset: Attend-and-Excite (arxiv.org/abs/2301.13826), Figure 2, the "incorrect
       attribute binding" column - a two-object color prompt, the Stable
       Diffusion output that puts the color on the wrong object, and the
       corrected Attend-and-Excite output beside it. (The teaser also shows a
       catastrophic-neglect example in the adjacent column.)
Shows: The behavior itself in one frame: the prompt, the wrong image where the
       attribute landed on the wrong object, and that a targeted fix recovers it.
       This is the cleanest before/after of attribute binding in a cited primary.
Crop:  Must retain the exact prompt text label, the labeled Stable Diffusion
       (baseline) panel showing the mis-binding, and enough of the panel labels
       to attribute both images correctly; may omit the neglect column and other
       rows. Read the exact prompt string off the figure at capture time and
       caption it verbatim from the source - the specific wording of the example
       prompt was taken from a rendered summary and must be confirmed against the
       figure before it is quoted. Capture with `nb asset`; caption factually
       with the source. No external image URL.
```

An alternative if a color example is preferred is StructureDiffusion
(arxiv.org/abs/2212.05032), which carries labeled before/after grids on the
CC-500 concept-conjunction prompts; same crop discipline applies.

## Discarded

```text
https://arxiv.org/abs/2406.07844: a 2024 method paper ("Enhanced Text
  Embeddings") that also blames the CLIP text encoder. Corroborates but is
  redundant with StructureDiffusion for the encoder claim and postdates the
  settled record; not needed to meet the floor.
https://arxiv.org/pdf/2410.22775 (Diffusion Beats Autoregressive): relevant to
  compositional evaluation but its comparison is architecture-class, off the
  binding-mechanism angle; not cited to avoid padding.
https://arxiv.org/pdf/2410.20972 (Attention Overlap / entity missing): concerns
  the neglect failure more than attribute binding; Attend-and-Excite already
  covers neglect within a cited primary.
```

## Notes on gaps and verification

- No single cited primary reports a clean "single-object accuracy vs two-object
  accuracy" pair, which the commission's "red apple works, red cube on blue
  sphere fails" example implies. The closest quantified stand-in is
  Attend-and-Excite's full-prompt (0.83-0.84) vs minimum-object (0.60-0.63) CLIP
  gap, which shows one object is rendered well while the second is dropped or
  mis-bound. If the writer wants a direct single-vs-composite number, it is not
  in these sources; present the gap figure instead and describe it accurately.
- arXiv id 2307.06350 currently resolves to T2I-CompBench++ (the enhanced 2024
  version). The original T2I-CompBench is NeurIPS 2023 (proceedings hash
  f8ad010cdd9143dbb0e9308c093aff24). The SD v1.4/v2 per-category scores are the
  same across both; cite the version the writer links and keep the URL resolving
  to the paper's own arXiv/proceedings page, not a fetch route.
- The Conwell & Ullman physical (~17%) and agentic (~28%) split and the
  "3 relations > 25%, none > 50%" facts are the robust readings. Any single
  per-prompt figure (some individual prompts score high because that
  configuration is common in training data) should be verified against the
  paper's per-relation table before it is quoted.
- All URLs above are the documents' own arXiv abstract pages and resolve.
```
