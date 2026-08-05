# Evidence: the-mechanics/reading-images (01)

The core mechanism the commission wants taught is well-supported by primaries the
field treats as settled. The Vision Transformer paper owns the patchify step, the
trainable linear projection into a D-dimensional embedding, and the arithmetic
(224x224 at 16x16 = a 14x14 grid = 196 patches = 196 tokens). LLaVA owns the
"separate CLIP/ViT encoder, projected into the language model's word-embedding
space" arrangement; Flamingo owns a second arrangement (resample to a fixed 64
tokens, then let text attend through gated cross-attention); Fuyu owns the "native"
arrangement (patches linearly projected straight into a decoder, no separate
encoder). CLIP owns the shared image-text embedding space those encoders inherit.
A current vendor's own accounting (OpenAI's images/vision guide) owns the claim
that an image costs hundreds to thousands of tokens.

Where the record is thin is exactly the commission's causal punchline. No primary
states that miscounting and misread small text are *caused by* patch-grid
resolution. The GPT-4V system card documents those failures empirically ("miss text
or characters," "unreliable," "prone to hallucinations") but never attributes them
to patchification. The strongest bridge is indirect and points slightly against the
"never gets more detail than the patch grid captured" framing: the LLaVA-NeXT
authors report that raising input resolution and adding tiles measurably reduces
OCR errors and hallucination, which means the patch grid is a bounded design choice,
not a hard ceiling. Builders spend more tokens to capture more detail. And for the
actual closed models the reader uses (GPT-4V/4o, Claude, Gemini), the vision
mechanism is undisclosed; the mechanism in this record is reconstructed from the
open literature, not confirmed for any consumer chatbot.

## Sources

```text
URL:         https://arxiv.org/abs/2010.11929
Kind:        primary. Dosovitskiy et al. own the ViT method; this paper introduces
             patch-embedding as the patchify + linear-projection step the lesson teaches.
Establishes: An image is cut into fixed-size patches, each flattened and mapped by a
             trainable linear projection into the same D-dimensional embedding space the
             transformer uses; the number of patches equals the input sequence length.
Paraphrase:  The model reshapes an H x W x C image into N flattened 2D patches, where
             N = HW/P^2 is both the patch count and the effective sequence length. Each
             flattened patch is linearly projected to D dimensions ("patch embeddings").
             A learnable [class] token is prepended and position embeddings are added.
             Standard training resolution is 224x224; patch sizes are 16x16 (e.g. ViT-L/16)
             or 14x14 (ViT-H/14). 224/16 = 14, so a 14x14 grid = 196 patches.
Locators:    Section 3.1 "Vision Transformer (ViT)", Eq. 1; title "An Image is Worth
             16x16 Words".
Quote:       "we reshape the image x in R^{H x W x C} into a sequence of flattened 2D
             patches x_p in R^{N x (P^2 . C)}"; "N = HW/P^2 is the resulting number of
             patches, which also serves as the effective input sequence length"; "we
             flatten the patches and map to D dimensions with a trainable linear
             projection (Eq. 1). We refer to the output of this projection as the patch
             embeddings."
```

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. Radford et al. own CLIP; the paper introduces the contrastive
             image-text training that produces a shared embedding space.
Establishes: An image encoder and a text encoder can be trained jointly so that images
             and their captions land near each other in one shared vector space. This is
             the space vision-language models later project image patches into.
Paraphrase:  CLIP trains an image encoder and text encoder together with a contrastive
             objective on 400 million (image, text) pairs, matching each image to its
             caption. The result maps both modalities into a shared embedding space and
             transfers zero-shot to many vision tasks (matching ResNet-50 ImageNet
             accuracy with no labeled ImageNet examples).
Locators:    Abstract; title "Learning Transferable Visual Models From Natural Language
             Supervision".
Quote:       "predicting which caption goes with which image is an efficient and scalable
             way to learn SOTA image representations from scratch on a dataset of 400
             million (image, text) pairs collected from the internet."
```

```text
URL:         https://arxiv.org/abs/2304.08485
Kind:        primary. Liu et al. own LLaVA; the paper defines the encoder-plus-projector
             arrangement the commission names.
Establishes: The "separate vision encoder, projected in" arrangement: a pre-trained CLIP
             ViT encoder produces image features, and a single trainable projection matrix
             maps them into the language model's word-embedding space, where they sit
             alongside text tokens.
Paraphrase:  LLaVA uses the pre-trained CLIP visual encoder ViT-L/14 to produce visual
             features Zv, then applies a trainable projection matrix W to convert Zv into
             language embedding tokens Hv "which have the same dimensionality as the word
             embedding space in the language model" (Hv = W . Zv). The language model is
             Vicuna.
Locators:    Section 3 "Architecture" (Eq. 1-2, Figure 1).
Quote:       "we consider the pre-trained CLIP visual encoder ViT-L/14 [40], which provides
             the visual feature Zv = g(Xv)"; "We apply a trainable projection matrix W to
             convert Zv into language embedding tokens Hv, which have the same
             dimensionality as the word embedding space in the language model."
```

```text
URL:         https://arxiv.org/abs/2204.14198
Kind:        primary. Alayrac et al. own Flamingo; the paper defines the second
             arrangement (fixed resampled tokens + gated cross-attention).
Establishes: An alternative to concatenating projected patches: compress a variable number
             of vision features to a fixed small number of visual tokens, and let a frozen
             language model attend to them through inserted cross-attention layers. Both
             the vision encoder and the language model are frozen.
Paraphrase:  The Perceiver Resampler takes a variable number of image/video features from
             the frozen vision encoder and outputs a fixed 64 visual tokens. Gated
             cross-attention dense (GATED XATTN-DENSE) layers are inserted between the
             frozen language-model layers; their keys and values come from the visual
             features while queries come from the language tokens, so text attends to the
             image. Vision model and LM are pretrained and frozen.
Locators:    Section 2.1 "Visual processing and the Perceiver Resampler"; Section 2.2
             "Conditioning frozen LM on visual representations"; Figure 3.
Quote:       "It takes as input a variable number of image or video features from the vision
             encoder and produces a fixed number of visual outputs (64)"; "We freeze the
             pretrained LM blocks, and insert gated cross-attention dense blocks ... between
             the original layers, trained from scratch."
```

```text
URL:         https://cdn.openai.com/papers/GPTV_System_Card.pdf
Kind:        primary. OpenAI's own system card; owns the documented capabilities and
             failure modes of GPT-4V.
Establishes: The failure class the lesson explains, stated by the model's own maker: the
             model misses or merges text, overlooks symbols, cannot reliably place things
             spatially, and reports errors with confidence. It does not attribute these to
             patchification.
Paraphrase:  Training predicts the next word "using a large dataset of text and image data"
             (no vision-encoder architecture disclosed). Red-teaming in scientific domains
             found the model "would occasionally combine" two closely located text
             components (merging "multipotent hematopoietic stem cell (HSC)" and
             "self-renewing division"), was "prone to hallucinations," and "could make
             factual errors in an authoritative tone." A Be My Eyes beta tester: it "very
             confidently told me there was an item on a menu that was in fact not there."
             OpenAI concludes the model "is unreliable" for high-risk identification.
Locators:    Section 1 (training); Section 2.1.1 (Be My Eyes, confident menu error);
             Section 2.3.1 "Scientific proficiency" (text merging, missed symbols, spatial
             failure, "unreliable"); Figures 4, 6, 7, 15.
Quote:       "It could miss text or characters, overlook mathematical symbols, and be unable
             to recognize spatial locations and color mappings."; "the model was prone to
             hallucinations and sometimes could make factual errors in an authoritative
             tone."; "It very confidently told me there was an item on a menu that was in
             fact not there."
```

```text
URL:         https://developers.openai.com/api/docs/guides/images-vision
Kind:        primary. OpenAI's own developer documentation; owns its image-token accounting.
Establishes: An image costs hundreds to thousands of tokens, and the count is set by a
             tile or patch rule the vendor documents. This is where "an image costs
             hundreds of tokens" becomes concrete and checkable.
Paraphrase:  For tile-based models (GPT-4o, GPT-4.1, o-series) the image is scaled to fit a
             2048x2048 box, then so its shortest side is 768px, then divided into 512x512
             tiles. Cost = base + (tiles x per-tile). GPT-4o: 85 base + 170 per tile (a
             1024x1024 image = 4 tiles = 170*4 + 85 = 765 tokens). Low detail is a flat 85.
             GPT-4o-mini uses 2833 base + 5667 per tile. Newer small models
             (GPT-4.1-mini/nano) use 32x32-pixel patches with a per-model multiplier and a
             cap near 1536 patches (a 1024x1024 image = 1024 patches).
Locators:    "Calculating costs" section, per-model base/tile tables and worked examples.
Quote:       "85 base tokens" and "170 tokens" per tile (GPT-4o/GPT-4.1); patch models use
             "32px x 32px patches."
```

```text
URL:         https://huggingface.co/adept/fuyu-8b
Kind:        primary. Adept's own model card; owns Fuyu's architecture claim.
Establishes: The "native multimodal" arrangement the commission names: no separate vision
             encoder at all; image patches are linearly projected straight into the first
             decoder layer, exactly like the ViT projection but feeding one unified model.
Paraphrase:  Fuyu is a decoder-only transformer with no image encoder. Image patches are
             linearly projected into the first transformer layer, bypassing the text
             embedding lookup, which lets it accept arbitrary image resolutions. Image
             patches are treated like text tokens in raster order.
Locators:    Model card, "Architecture" / model details.
Quote:       "Architecturally, Fuyu is a vanilla decoder-only transformer - there is no
             image encoder."; "Image patches are instead linearly projected into the first
             layer of the transformer, bypassing the embedding lookup."; "This
             simplification allows us to support arbitrary image resolutions."
```

```text
URL:         https://llava-vl.github.io/blog/2024-01-30-llava-next/
Kind:        primary. LLaVA authors' own release page for LLaVA-NeXT (LLaVA-1.6).
Establishes: The counter-pressure to the commission's "never gets more detail" line:
             production systems split a high-res image into a grid of tiles, encode each,
             and concatenate, precisely to capture fine detail; and doing so reduces the
             OCR and hallucination failures the lesson attributes to coarse patches.
Paraphrase:  LLaVA-NeXT's "AnyRes" splits a high-resolution image into grid tiles
             (configurations like 2x2, 1x{2,3,4}, {2,3,4}x1), encodes each 336x336 tile
             with the CLIP ViT-L/14 encoder (576 tokens per tile), and concatenates them,
             supporting resolutions up to 672x672 / 336x1344 / 1344x336. The authors state
             that higher-resolution, detail-preserving representations significantly improve
             the model's ability to perceive intricate detail, reducing hallucination and
             improving OCR.
Locators:    "Dynamic High Resolution" section; blog dated 2024-01-30, Liu et al.
Quote:       "When provided with high-resolution images and representations that preserve
             these details, the model's capacity to perceive intricate details in an image
             is significantly improved."
```

```text
URL:         https://huggingface.co/blog/vlms
Kind:        secondary. A practitioner explainer (merve, Edward Beeching et al., Hugging
             Face, 2024-04-11). Reports on the arrangements above from outside the authoring
             labs; context only, not a claim owner.
Establishes: A plain taxonomy that matches the primaries: image encoder -> projector ->
             text decoder, with the LLaVA-style "project and concatenate" path versus other
             fusion strategies, and Fuyu's "patches straight into a projection layer."
Paraphrase:  VLMs pair an image encoder, a projector that aligns image features to the LM's
             input space, and a text decoder; a common recipe freezes the encoder and trains
             the projector first. It describes Fuyu as feeding image patches directly to a
             projection layer before the autoregressive decoder.
Locators:    Sections on architecture and Fuyu-8B.
Quote:       "image patches are directly fed to a projection layer and then the sequence
             goes through an auto-regressive decoder" (paraphrasing Fuyu).
```

## Contradictions

- **"It never gets more detail than the patch grid captured" is too absolute.**
  The commission frames the patch grid as a fixed ceiling that causes miscounting
  and misread text. The LLaVA-NeXT authors show the opposite lever exists: split
  the image into more tiles at higher resolution and the model perceives more
  detail, with measurably fewer OCR errors and hallucinations
  (https://llava-vl.github.io/blog/2024-01-30-llava-next/). OpenAI's own accounting
  makes the same point structurally: "high detail" mode spends 170 tokens per
  512px tile to see more, versus a flat 85 for "low detail"
  (https://developers.openai.com/api/docs/guides/images-vision). The honest framing:
  the grid is a bounded budget, not a physical ceiling. Detail is lost when the
  budget is small, and builders buy more detail with more tokens. The lesson's
  causal story survives, but "never" should become "only as fine as the chosen
  grid, and that grid is a cost tradeoff."

- **No primary attributes miscounting/misreading to patchification.** The GPT-4V
  system card documents the failures (miss text, merge nearby text, spatial errors,
  confident invention) but never says the patch grid caused them
  (https://cdn.openai.com/papers/GPTV_System_Card.pdf). The causal link the
  commission wants to teach is a reasonable synthesis, supported indirectly by the
  resolution-vs-accuracy result above, but it is an inference, not a documented
  finding. This is exactly the "open question" the series asks to mark.

- **The exact token count varies by an order of magnitude; 196 is illustrative.**
  ViT's 196 comes from 16x16 patches at 224x224. Real systems differ: LLaVA-1.5/NeXT
  use CLIP ViT-L/14 at 336x336 = 576 tokens per tile; Flamingo resamples to a fixed
  64; OpenAI tiles to 765+ tokens for a 1024x1024 image. "A few hundred" is a fair
  order of magnitude, but the specific 196 should be presented as the ViT worked
  example, not as what a chatbot actually uses.

- **The mechanism is undisclosed for the model the reader actually uses.** GPT-4V's
  card says only that it was trained to "predict the next word" over text and image
  data; it discloses no encoder, patch size, or token count. Which of the three
  arrangements (LLaVA-style projector, Flamingo-style cross-attention, Fuyu-style
  native) any consumer chatbot uses is not public. The lesson should teach the
  mechanism as the field's documented method, not assert it about GPT-4o/Claude/
  Gemini specifically.

## Numbers

```text
Figure: 196 patches (tokens) for a 224x224 image at 16x16 patches (14x14 grid)
Owner:  ViT (Dosovitskiy et al. 2020), Section 3.1, N = HW/P^2
Scope:  Standard ViT training config; illustrative, not a production chatbot count.
```

```text
Figure: 576 visual tokens per 336x336 tile (CLIP ViT-L/14, patch 14, 24x24 grid)
Owner:  LLaVA-1.5 / LLaVA-NeXT (Liu et al.), via CLIP ViT-L/14 encoder
Scope:  Per tile; LLaVA-NeXT concatenates up to ~5 tiles (~2880 tokens) via AnyRes.
```

```text
Figure: 64 visual tokens (fixed), regardless of input image/video size
Owner:  Flamingo (Alayrac et al. 2022), Perceiver Resampler, Section 2.1
Scope:  Output of the resampler feeding the frozen LM's cross-attention.
```

```text
Figure: 85 base tokens + 170 tokens per 512x512 tile (GPT-4o high detail);
        85 flat (low detail); 1024x1024 image = 765 tokens
Owner:  OpenAI images/vision guide (developers.openai.com)
Scope:  Per image, GPT-4o/GPT-4.1 tile accounting; other models differ (GPT-4o-mini
        2833 + 5667/tile; GPT-4.1-mini uses 32x32 patches, cap ~1536).
```

```text
Figure: 400 million (image, text) pairs
Owner:  CLIP (Radford et al. 2021), Abstract
Scope:  Contrastive pre-training dataset size.
```

## Source assets

```text
Asset: ViT Figure 1, the model-overview schematic (image split into a grid of patches,
       each flattened, linear projection, + position embeddings, into the transformer).
       https://arxiv.org/abs/2010.11929
Shows: The whole patchify-and-project step in one picture: pixels -> patch grid -> vectors.
Crop:  Keep the patch-grid-to-linear-projection portion. The classification-head tail is
       optional and can be omitted for a reading-focused lesson.
```

```text
Asset: GPT-4V system card Figure 4 (+ Figure 15, the clean source image), the hematopoiesis
       diagram where the model merges "multipotent hematopoietic stem cell (HSC)" and
       "self-renewing division." https://cdn.openai.com/papers/GPTV_System_Card.pdf
Shows: A concrete, vendor-documented instance of nearby text being merged and detail lost:
       the failure class the lesson explains, from the maker itself.
Crop:  Retain the prompt image and the portion of the model's response that invents the
       merged term. Must keep both to show the input and the specific error.
```

```text
Asset: GPT-4V system card Figure 6, misidentifying chemical structures / a Death Cap
       mushroom, labeled "Correct/Wrong Answer." Same PDF.
Shows: Confident wrong identification stated in an authoritative tone.
Crop:  Keep the "Wrong Answer" (xylazine/Thiamine) panel; it is the cleanest single
       example of confident invention.
```

```text
Asset: Flamingo Figure 3, the architecture diagram (Perceiver Resampler feeding gated
       cross-attention layers interleaved in the frozen LM). https://arxiv.org/abs/2204.14198
Shows: The second arrangement visually: fixed visual tokens on one side, text attending to
       them through inserted layers.
Crop:  Keep the resampler-to-cross-attention path; the per-block gating internals can be
       omitted for a no-architecture-survey lesson.
```

```text
Asset: OpenAI images/vision guide worked example / tile table (1024x1024 -> 765 tokens).
       https://developers.openai.com/api/docs/guides/images-vision
Shows: That "an image costs hundreds of tokens" is a documented, arithmetic fact, and that
       higher detail costs more tokens.
Crop:  The base+per-tile numbers and one worked example row suffice; no need for the full
       per-model matrix.
```

## Discarded

```text
URL: https://www.adept.ai/blog/fuyu-8b — returned HTTP 403 to the fetcher. The same claims
     are recorded from Adept's own model card (huggingface.co/adept/fuyu-8b), which is
     citable and resolves, so the blog is unnecessary.
```

```text
URL: https://getstream.io/blog/gpt-4o-vision-guide/ and various token-calculator sites
     (image-token-*.herokuapp.com, spurnow.com, stellaxon.com, spoold.com) — third-party
     restatements of OpenAI's token rule. Rejected in favor of OpenAI's own documentation,
     which owns the numbers.
```

```text
URL: https://arxiv.org/html/2403.11703 (LLaVA-UHD), arxiv 2408.03326 (LLaVA-OneVision),
     2412.13303 (FastVLM) — surfaced while confirming tiling/token counts. Real primaries,
     but they extend rather than change the mechanism, and the lesson is explicitly not a
     model survey. LLaVA-NeXT already carries the "tile for more detail" point. Not cited to
     avoid drifting into a comparison piece (commission boundary).
```
