# evidence: the-mechanics/text-in-images (01)

The evidence strongly supports the commissioned chain and its required contribution: the character information a word carries is degraded before the diffusion model draws a single pixel, at the text encoder that hands the image model whole-word (subword-token) features rather than an ordered list of letters. Two model-owner documents make the diagnosis in their own words. Stable Diffusion's model card lists "The model cannot render legible text" as a known limitation and states it uses a frozen CLIP ViT-L/14 text encoder, which operates on lower-cased byte-pair-encoding tokens with a fixed 49,152 vocabulary (character-blind). OpenAI's DALL-E 3 paper blames its own text encoder outright: it "actually sees tokens that represent whole words and must map those to letters," and proposes character-level language models as the fix. The measured fix comes from "Character-Aware Models Improve Visual Text Rendering" (Google Research), which trades a character-blind encoder (T5) for a character-aware one (ByT5) on an otherwise identical image model and records 25-plus point spelling gains on common words and 30-plus on rare words. The evidence is thin in three specific places, and each is recorded in Contradictions: residual glyph-shaping failures the same paper attributes to the image-generation module, "outside the text encoder"; the finding that a character-blind model can recover near-perfect spelling at more than 100 billion parameters (PaLM 540B), so the information is expensive to reach, not strictly absent; and a lack of any published hard number for how long a string the current best systems can render before they fail, which stays an open question rather than a settled one.

## Sources

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. The paper that owns latent diffusion and its text-to-image
             conditioning mechanism (authored by the method's creators).
Establishes: How the text prompt reaches the image model in latent diffusion:
             a text encoder produces a code that conditions the denoising U-Net
             through cross-attention. Fixes the exact encoder the *paper* used
             for text-to-image (a BERT-tokenizer transformer), distinct from the
             CLIP encoder the released Stable Diffusion checkpoints later used.
Paraphrase:  For text-to-image, the authors tokenize the prompt with the BERT
             tokenizer and implement the conditioning encoder as a transformer,
             whose output is fed into the U-Net via multi-head cross-attention.
             The prompt never enters as pixels or glyphs; it enters as an encoded
             feature sequence the image model attends to.
Locators:    Section 3.3 (conditioning mechanism, cross-attention equation);
             Section 4.3.1 (text-to-image setup naming the BERT tokenizer).
Quote:       "We employ the BERT-tokenizer and implement tau_theta as a
             transformer to infer a latent code which is mapped into the UNet
             via (multi-head) cross-attention." (Sec 4.3.1)
```

```text
URL:         https://huggingface.co/CompVis/stable-diffusion-v1-4
Kind:        primary. The model card is authored by the model's makers about
             their own model; it owns the claim of what encoder Stable Diffusion
             uses and its own declared limitations.
Establishes: (1) Stable Diffusion v1 uses a frozen, pretrained CLIP ViT-L/14
             text encoder, whose (non-pooled) output conditions the U-Net via
             cross-attention. (2) The makers list illegible text as a known
             limitation. Together these put a character-blind CLIP encoder in
             the pipeline and record the failure the lesson explains.
Paraphrase:  The prompt is encoded by a fixed CLIP ViT-L/14 text encoder; that
             encoding drives the diffusion U-Net through cross-attention. Among
             listed limitations, the model cannot render legible text.
Locators:    "Model Details" / architecture description; "Limitations" list.
Quote:       "uses a fixed, pretrained text encoder (CLIP ViT-L/14)"
             "The non-pooled output of the text encoder is fed into the UNet
             backbone of the latent diffusion model via cross-attention."
             "The model cannot render legible text" (Limitations)
```

```text
URL:         https://arxiv.org/abs/2103.00020
Kind:        primary. The CLIP paper, authored by the method's creators; owns
             the description of CLIP's text encoder and its tokenizer.
Establishes: That CLIP's text encoder is character-blind: it reads a subword
             (byte-pair-encoding) representation, not characters. This is the
             tokenization link for any system that uses CLIP text features.
             Cite only to name the encoder as the character-blind step; do NOT
             re-teach what CLIP is (the-evidence/clip covers that tonight and is
             unpublished, so it must not be linked in Background).
Paraphrase:  CLIP's text encoder is a Transformer that operates on a lower-cased
             byte-pair-encoding representation of the text with a 49,152-token
             vocabulary. The unit it embeds is the subword token, not the letter.
Locators:    Section 2.4 (Text encoder architecture and tokenizer).
Quote:       "The transformer operates on a lower-cased byte pair encoding (BPE)
             representation of the text with a 49,152 vocab size" (Sec 2.4)
```

```text
URL:         https://arxiv.org/abs/2205.11487
Kind:        primary. The Imagen paper, authored by its creators; owns the
             encoder-vs-generator scaling finding and the DrawBench benchmark.
Establishes: (1) Imagen uses a frozen T5-XXL text encoder (4.6B parameters).
             (2) Its headline finding: scaling the frozen text encoder helps
             image-text alignment and fidelity much more than scaling the image
             diffusion U-Net. (3) T5-XXL text features beat CLIP text features on
             DrawBench. (4) DrawBench includes explicit "Text" and "Misspellings"
             prompt categories, and Imagen renders quoted text markedly better
             than DALL-E 2. This establishes that the encoder is the high-leverage
             component, while noting Imagen's T5 encoder is still character-blind
             (SentencePiece subwords), so this is an encoder-capacity result, not
             a character-awareness result.
Paraphrase:  A frozen T5-XXL (4.6B) encodes the prompt into embeddings that
             condition a cascade of diffusion models. Growing that encoder buys
             more alignment and fidelity than growing the diffusion model. T5-XXL
             text features are preferred over CLIP text features on the compositional
             DrawBench prompts. On DrawBench's quoted-text prompts Imagen beats
             DALL-E 2 clearly.
Locators:    Abstract; Sec 2 (contribution list, frozen T5-XXL); Sec 4.2 (encoder
             scaling, "T5-XXL (4.6B parameters)"); Sec 4.4 ("Scaling text encoder
             size is more important than U-Net size"); Appendix C / Table A.1
             (DrawBench categories incl. Text, Misspellings); Fig. A.21 (quoted-text).
Quote:       "increasing the size of the language model in Imagen boosts both
             sample fidelity and image-text alignment much more than increasing
             the size of the image diffusion model." (Abstract)
             "Scaling text encoder size is more important than U-Net size. While
             scaling the size of the diffusion model U-Net improves sample quality,
             we found scaling the text encoder size to be significantly more
             impactful than the U-Net size (Fig. 4b)." (Sec 4.4)
             "Imagen trained with our largest text encoder, T5-XXL (4.6B
             parameters), yields the best results" (Sec 4.2)
```

```text
URL:         https://arxiv.org/abs/2212.10562
Kind:        primary. "Character-Aware Models Improve Visual Text Rendering"
             (Liu, Garrette, Saharia, Chan, et al., Google Research). Owns the
             controlled experiment that isolates the text encoder as the cause
             and the character-aware encoder as the fix; introduces WikiSpell
             (text-only spelling) and DrawText (visual rendering) benchmarks.
Establishes: The central mechanism and the measured fix.
             (1) Why character-blind encoders cannot spell: subword tokenizers
             (BPE, SentencePiece) "compress common character sequences into
             unbreakable units by design," removing the signal about a token's
             internal letters. A single-token word carries no per-letter signal
             the encoder can pass on.
             (2) Text-only spelling (WikiSpell, held-out words, frozen encoder
             fine-tuned for spelling): T5-XXL reaches only 66% exact-match on the
             most common English words, while character-aware ByT5-XXL reaches
             ~98% and is nearly flat across word frequency. Character-blind models
             reach robust spelling only at PaLM 540B scale (>99%).
             (3) Visual rendering (DrawText Spelling, 2,000 images/model, OCR-scored):
             swapping T5 for ByT5 on the same data and training budget yields 25+
             point accuracy gains on the most frequent words and 30+ on the rarest;
             against Imagen-AR (trained 6.6x longer) the char-aware models gain 15+
             (frequent) and 30+ (rare). Gains hold for ByT5-XL, whose encoder is
             43% smaller than T5-XXL. A tiny character-aware add-on (Concat of
             T5-XXL with ByT5-Small, +4.8% encoder size) captures the benefit.
             (4) Error taxonomy pins which failures are the encoder's: semantic,
             homophone, and add-glyph errors appear only in character-blind T5,
             evidence the encoder lacks core spelling knowledge. Character-blind
             models even "regularize" irregular verbs (fought->fighted) in 11% of
             samples; character-aware models never do.
             (5) The honest limit (see Contradictions): dropped/repeated/merged/
             misshapen glyphs occur across ALL models, char-aware included, and
             are attributed to the image-generation module, not the encoder.
Paraphrase:  Popular text-to-image models feed the image generator subword-token
             features that hide a word's spelling. Give the generator a character-
             aware encoder instead and rendered spelling jumps sharply, at far
             smaller scale and far less training than brute scale or longer training
             buy a character-blind model. The remaining errors after the fix are
             mostly glyph-shaping and placement, which live in the image model.
Locators:    Abstract; Sec 1-2 (character-blind vs character-aware; Fig. 2 caption
             on tokenization); Sec 3 / Table 1 (WikiSpell, T5-XXL 66% vs ByT5-XXL
             ~98%; PaLM 540B >99%); Sec 5.1-5.2 (DrawText model list and results,
             the 15+/25+/30+ point gains, ByT5-XL 43% smaller, Concat +4.8%);
             Table 3 and Figs. 3, 5, 6 (error types, "the ff in coffee", irregular
             verbs).
Quote:       "most widely used language models are character-blind, relying on
             data-driven subword segmentation algorithms like Byte Pair Encoding
             (BPE)" (Sec 2)
             "They compress common character sequences into unbreakable units by
             design" (Sec 2)
             "Subword tokenization ... maps common character sequences onto IDs
             that are looked up in an embedding table before being passed to the
             model, removing any signal about token-internal composition."
             (Fig. 2 caption)
             "character-aware models (ByT5 and Concat) outperform the rest, with
             15+ point accuracy gains over Imagen-AR on the most frequent words,
             and 30+ point gains on the least frequent words." (Sec 5.2)
             "the gains are even larger: 25+ point gains on the most frequent words
             and 30+ point gains on the least frequent. Notably, these gains persist
             even for the smaller ByT5-XL model, whose encoder is 43% smaller than
             T5-XXL." (Sec 5.2)
             "for single-token words, fine-tuning provides no spelling signal since,
             by definition, that single token will not appear in the fine-tuning
             dataset." (Sec 3)
```

```text
URL:         https://stability.ai/news-updates/deepfloyd-if-text-to-image-model
Kind:        primary for the design fact (Stability AI's own announcement of its
             own model); its rendering claim is vendor marketing, flagged below.
Establishes: DeepFloyd IF uses a frozen large language model, T5-XXL-1.1, as its
             text encoder, and cross-attention layers to align text and image. The
             maker credits the T5 encoder for the model's text-in-image ability.
             This is a second production system built on a large frozen T5 encoder,
             corroborating the "encoder capacity governs text" throughline.
Paraphrase:  The generation pipeline uses the frozen T5-XXL-1.1 language model as
             the text encoder, plus many text-image cross-attention layers, and the
             maker attributes clear text-in-image to that deep text understanding.
Locators:    "Deep text prompt understanding" section of the announcement.
Quote:       "The generation pipeline utilizes the large language model T5-XXL-1.1
             as a text encoder."
             "Incorporating the intelligence of the T5 model, DeepFloyd IF generates
             coherent and clear text alongside objects..."
Note:        The "coherent and clear text" claim is the vendor's own, not an
             independent measurement. Treat the design fact (frozen T5-XXL-1.1) as
             solid and the rendering-quality claim as a marketing assertion; the
             Character-Aware paper independently shows T5-XXL-class (character-blind)
             encoders still misspell.
```

```text
URL:         https://cdn.openai.com/papers/dall-e-3.pdf
Kind:        primary. OpenAI's DALL-E 3 technical paper ("Improving Image Generation
             with Better Captions", Betker et al.). Owns DALL-E 3's own account of
             why its text rendering fails. This is the keystone corroboration from a
             current, widely used system.
Establishes: DALL-E 3 uses a T5 text encoder, and its makers attribute unreliable
             text rendering to that encoder specifically: the model sees whole-word
             tokens and must map them to letters. They name the character-level fix
             the Character-Aware paper measured. This is the commissioned angle stated
             by a model's own builders. (Note: the URL is a ~28 MB PDF; recorded to
             the document's own page. Section 5.2 "Text rendering" is the passage.)
Paraphrase:  DALL-E 3 can produce text but does so unreliably, with missing or extra
             characters. The authors suspect the T5 text encoder: it sees whole-word
             tokens, not letters, and must recover the letters when drawing. They want
             to try conditioning on character-level language models to improve this.
Locators:    Sec 5.2 "Text rendering" (Limitations & Risk). Encoder identity: the
             model uses a T5 text encoder (stated in the same section).
Quote:       "During testing, we have noticed that this capability is unreliable as
             words are have missing or extra characters. We suspect this may have to
             do with the T5 text encoder we used: when the model encounters text in a
             prompt, it actually sees tokens that represent whole words and must map
             those to letters in an image. In future work, we would like to explore
             conditioning on character-level language models to help improve this
             behavior." (Sec 5.2, quoted verbatim including the source's grammatical
             slip "words are have")
```

```text
URL:         https://huggingface.co/docs/diffusers/api/pipelines/deepfloyd_if
Kind:        secondary. Hugging Face's diffusers library documentation describes
             DeepFloyd IF from outside the authoring party; corroborates the design
             fact but does not own it.
Establishes: Independent corroboration that DeepFloyd IF's stages use a frozen
             T5-based text encoder feeding a U-Net with cross-attention and attention
             pooling, and that IF is positioned as strong at legible text. A
             repetition of the maker's design claim, not new proof of rendering quality.
Paraphrase:  IF's stages use a frozen T5 text encoder to produce embeddings for a
             U-Net; the library documents IF as able to place legible text in images.
Locators:    Pipeline overview / architecture description.
Quote:       (none load-bearing; used only to corroborate the frozen-T5 design)
```

## Contradictions

The evidence does not overturn the commissioned angle. It sharpens where the angle
stops. The claim that survives is the strong, most-skipped one: the failure is set at
the text encoder, before pixels, and character-aware encoders are the fix that follows.
Three findings bound how far that claim reaches, and the lesson should carry all three
as the settled-versus-open line the commission asks for.

- Some text failures are not the encoder's. In the Character-Aware paper's own error
  taxonomy, dropped, repeated, merged, and misshapen glyphs appear across every model
  tested, character-aware ones included. The authors attribute these to the image-
  generation module and write that "resolving these issues will require orthogonal
  improvements outside the text encoder" (Sec 5.2). So the encoder governs whether the
  model *knows* the spelling; the diffusion decoder still governs whether it can *shape
  and place* the glyphs. A lesson that says the encoder is the only cause overshoots.
  This is the cleanest map of "settled" (the encoder is the cause of not knowing the
  letters) versus "open" (glyph layout in the image model).

- Character-blindness is expensive, not absolute. The same paper documents that a
  character-blind model can reach robust spelling by brute scale: PaLM at 540B parameters
  spells at >99% from a 20-example prompt, and even a frozen T5-XXL reaches 66% on common
  English words after fine-tuning. The authors call the large-model result "miraculous"
  and show it needs scale "over 100B parameters" and does not generalize well beyond
  English. So the letters are not literally erased and unrecoverable; they are compressed
  out of easy reach and can be reconstructed statistically, but only at a scale most image
  systems will not pay for. The lesson should say the spelling is *degraded and hard to
  reach*, and should not claim the information is simply gone.

- The fix carries a cost. Pure character-only encoding decreased image-text alignment
  for prompts that do not involve visual text, which is why the authors propose the
  Concat approach (T5-XXL plus a small ByT5) rather than replacing the encoder outright
  (Abstract; Sec 5). Character-awareness is the fix for spelling, not a free upgrade to
  the whole encoder.

One framing tension worth flagging for the editor: Imagen's headline result is about
encoder *size* (a larger character-blind T5-XXL beats CLIP and DALL-E 2 on text), while
the Character-Aware result is about encoder *type* (character-aware beats character-blind
at equal or smaller size and less training). Both point at the encoder, but they are two
different levers. The lesson's argument is strongest if it keeps them distinct: scale
helped first, character-awareness helped more and cheaper.

No source contradicts the core diagnosis that the character signal is lost or degraded at
the encoder before the image model runs. DALL-E 3's own paper states it directly.

## Numbers

```text
Figure: 49,152 tokens
Owner:  CLIP paper (Radford et al.), Sec 2.4
Scope:  Size of CLIP's lower-cased byte-pair-encoding text vocabulary; the unit
        the text encoder embeds is a subword token from this set, not a character.
```

```text
Figure: 4.6 billion parameters
Owner:  Imagen paper, Sec 4.2
Scope:  Size of Imagen's frozen T5-XXL text encoder (its largest tested encoder,
        which gave the best results).
```

```text
Figure: text encoder scaling > U-Net scaling
Owner:  Imagen paper, Sec 4.4 / Fig. 4b (qualitative pareto comparison, no single
        scalar)
Scope:  Effect on image-text alignment and image fidelity of growing the frozen
        text encoder versus growing the image diffusion U-Net; encoder growth is
        "significantly more impactful."
```

```text
Figure: 66% (T5-XXL) vs ~98% (ByT5-XXL)
Owner:  Character-Aware paper, Table 1 (WikiSpell, English)
Scope:  Exact-match spelling accuracy on held-out most-common (Top 1%) English
        words, frozen encoder fine-tuned for spelling, text-only task. ByT5 is
        near-flat across all five frequency buckets; T5 is much lower and
        frequency-sensitive. This is text-only spelling, not image rendering.
```

```text
Figure: >99% at 540B parameters (PaLM); >100B needed
Owner:  Character-Aware paper, Sec 3 / Table 1 (few-shot)
Scope:  A character-blind model reaches near-perfect English spelling only at
        very large scale (PaLM 540B, 20-shot); robustness "only achieved at scales
        over 100B parameters" and weaker on other languages.
```

```text
Figure: 25+ points (frequent), 30+ points (rare)
Owner:  Character-Aware paper, Sec 5.2 (DrawText Spelling)
Scope:  Full-string OCR spelling-accuracy gain from swapping the image model's
        text encoder T5 -> ByT5, same dataset and same training steps; measured
        over 2,000 images/model, no partial credit. Controlled comparison whose
        only variable is the encoder.
```

```text
Figure: 15+ points (frequent), 30+ points (rare)
Owner:  Character-Aware paper, Sec 5.2 (DrawText Spelling)
Scope:  Same benchmark, char-aware models vs Imagen-AR, a stronger character-blind
        baseline trained 6.6x longer. The char-aware model still wins.
```

```text
Figure: 43% smaller encoder, gains persist
Owner:  Character-Aware paper, Sec 5.2
Scope:  ByT5-XL's encoder is 43% smaller than T5-XXL yet still delivers the
        rendering gains: character-awareness, not size, is carrying this result.
```

```text
Figure: +4.8% encoder size (Concat)
Owner:  Character-Aware paper, Sec 5.1
Scope:  Adding a small ByT5-Small (220M) alongside T5-XXL raises encoder size by
        4.8% and makes an otherwise character-blind model character-aware.
```

```text
Figure: 11% of samples
Owner:  Character-Aware paper, Sec 5.2 / Fig. 6
Scope:  Rate at which character-blind T5-based image models wrongly add an -ed
        ending to 23 hand-chosen irregular past-tense verbs (fought -> fighted).
        Character-aware models never make this error. Evidence the encoder is
        guessing spelling from meaning and morphology.
```

## Source assets

```text
Asset: Character-Aware paper, Figure 1 (top vs bottom rows of generated postage
       stamps, same prompts, character-blind vs character-aware encoder).
Shows: The whole thesis in one image: identical prompts, one variable changed
       (the encoder), garbled text on top and clean text below. Prompts include
       short phrases like "California: All Dreams Welcome".
Crop:  A crop must keep at least one matched pair (same prompt, both rows) so the
       before/after is legible; must retain the row labels "Character-Blind" /
       "Character-Aware"; omit unrelated columns to keep the words readable.
```

```text
Asset: Character-Aware paper, Figure 2 (the tokenization diagram: input text ->
       tokenized text -> token IDs -> token embeddings, using the T5 SentencePiece
       tokenizer, e.g. "elephants" splitting into "elephant" + "s").
Shows: Exactly where the letters disappear: the word becomes an ID looked up in a
       table, and the letters inside a token are no longer represented. This is the
       single most useful visual for the "spelling is gone before any pixel" step.
Crop:  Keep the four labeled stages and at least one word that is a single token
       plus one that splits; keep the caption clause about "removing any signal
       about token-internal composition".
```

```text
Asset: Character-Aware paper, Figure 4 (DrawText Spelling accuracy vs word-frequency
       bucket, 10 models, character-aware curves clearly above character-blind).
Shows: The measured fix as a chart: character-aware models sit above every
       character-blind baseline across all frequency buckets, and the gap widens on
       rare words.
Crop:  Keep the axis labels (word frequency; spelling accuracy) and a legend that
       distinguishes ByT5/Concat from T5/Imagen/SD/DALL-E 2/Parti. If reproduced,
       the paper's own script/data would be needed; per house rules a chart must be
       a committed chart-N.py, so this figure is a reference for what to plot, not a
       drop-in image.
```

```text
Asset: Character-Aware paper, Figure 5 (selected errors: T5-XXL consistently
       misspelling refers/similarly/stomach; ByT5-XXL making only sporadic dropped/
       merged/repeated-glyph errors).
Shows: The concrete texture of the two failure modes: a character-blind model
       reliably wrong on a word, a character-aware model mostly right with minor
       glyph slips. Good for the "short word renders now vs longer/rarer still
       garbles" example the brief asks for.
Crop:  Keep one clear consistent-misspelling example (top) and one sporadic-glyph
       example (bottom), with the target word noted.
```

```text
Asset: Imagen paper, Figure A.21 (Imagen vs DALL-E 2 on DrawBench "Text" prompts,
       e.g. a storefront with "Text to Image" written on it).
Shows: A larger character-blind encoder (T5-XXL) rendering quoted text better than
       an earlier system, illustrating the "scale helped first" half of the story.
Crop:  Keep a matched prompt pair so the comparison is legible; retain the quoted
       target string.
```

```text
Asset: DALL-E 3 paper, Figure 7 (common failure modes) and the Sec 5.2 passage.
Shows: A current, named production system stating in its own words that its text
       encoder is the suspected cause. The prose passage is the load-bearing asset
       here more than any single image.
Crop:  Prose, not image; quote Sec 5.2 as recorded above.
```

## Discarded

```text
URL: https://arxiv.org/abs/2103.00020 (partly) — CLIP is cited ONLY to name its
     text encoder as the character-blind step. The neighbor lesson the-evidence/clip
     covers the CLIP paper tonight and is unpublished, so no Background link to it and
     no re-teaching of what CLIP is. Kept as a narrow encoder-tokenizer citation only.
```

```text
URL: https://typedream.com/blogs/why-dall-e-cant-spell — popular explainer, not a
     primary or authoritative secondary; superseded by DALL-E 3's own Sec 5.2.
```

```text
URL: https://community.openai.com/... (forum threads on DALL-E 3 misspellings) —
     user anecdotes, not a source that owns or reliably measures the claim.
```

```text
URL: https://en.wikipedia.org/wiki/DALL-E — tertiary; every claim needed is
     available from the primary papers and model cards.
```

```text
URL: https://arxiv.org/abs/2403.09622 (Glyph-ByT5) and https://arxiv.org/abs/2503.19897
     (Scaling Down Text Encoders) — relevant and character-encoder-focused, but out of
     scope for this round's chain and would add newer systems the commission did not
     name. Noted as possible Go-deeper reading, not cited here. Scaling-Down's finding
     that text rendering is the capability most sensitive to shrinking the T5 encoder
     independently corroborates the encoder-governs-text throughline if the writer wants
     one more recent data point.
```

```text
URL: DALL-E 2 / unCLIP "struggles at producing coherent text" — used only as it is
     quoted inside the Character-Aware paper (Sec 1), i.e. a repetition, not opened
     firsthand this round. It supports that the claim was made about DALL-E 2, not an
     independent verification. Stable Diffusion's own "cannot render legible text" card
     is the primary statement of the behavior the lesson should lean on instead.
```
