# Commission: the-evidence/vision-transformer

## The document

"An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale"
(Dosovitskiy, Beyer, Kolesnikov, Weissenborn, Zhai, Unterthiner, Dehghani,
Minderer, Heigold, Gelly, Uszkoreit, Houlsby; Google Research, Brain team).
Submitted to arXiv October 2020, published at ICLR 2021. This is the paper that
introduced the Vision Transformer (ViT): apply a near-standard Transformer
directly to a sequence of image patches, with the fewest possible image-specific
parts, and see how far scale carries it.

The Evidence reads one famous document per lesson so the reader knows what it
actually says. The famous shorthand this article tests is "Transformers replaced
CNNs in computer vision." The document is cited to settle that. Read the document
itself and show what it actually measured and, above all, what condition it
attached to the result.

## The angle

The paper's own finding is conditional, and the condition is the story. Trained
only on a mid-size labeled set (ImageNet-1k, ~1.3M images), ViT lands *below*
comparable convolutional networks: it lacks the built-in assumptions about images
(locality, translation equivariance) that a CNN gets for free, so with limited
data the CNN's assumptions win. The Transformer only pulls level with or ahead of
the best CNNs after pre-training on a much larger labeled set: ImageNet-21k
(~14M images) and especially Google's internal JFT-300M (~303M images). The
headline "ViT beats CNNs" is true only above a data threshold most people never
state when they cite it. The reader should finish able to see the size of the
foundation under the claim, and to say plainly when today's usage matches the
document and when it does not.

Bring it to the present honestly, both directions:
- The data condition was later softened. DeiT (Touvron et al., 2021) trained a
  competitive ViT on ImageNet-1k alone using strong augmentation and
  distillation, showing the "you need 300M images" reading was too strong as a
  hard law even if it held for the original recipe.
- The architecture claim was also pushed back. ConvNeXt (Liu et al., 2022)
  modernized a plain CNN and matched Transformers, showing much of ViT's win
  traced to training recipe and scale, not to attention as such.
Both corrections point the same way: the document showed a scale result, and the
field's shorthand dropped the scale.

## What this article must not do

- Do not re-teach the Transformer, self-attention, or how a word becomes a
  vector. Those are taught. Link `the-mechanics/word-order` (self-attention and
  order) and `the-evidence/attention-is-all-you-need` in prose at first use.
- Do not re-teach how a picture becomes tokens the model can compare. The
  patch-embedding mechanism (an image sliced into squares, each turned into a
  vector) is taught in `the-mechanics/reading-images`; link it rather than
  explaining it from scratch. Teach only the ViT-specific detail the argument
  needs (fixed 16x16 patches turned into a linear sequence, the added position
  embeddings, the class token).
- Adjacency alert. `the-evidence/clip` published 2026-08-25 and is directly
  next to this piece: CLIP's best model is a ViT (ViT-L/14), and the CLIP lesson
  already made the point that "the web-scale data, not the objective, did the
  work" for robustness. This article must stay on ViT's *own* territory:
  supervised image classification and the pre-training-data threshold for beating
  CNNs. Do not restate CLIP's contrastive-learning story or its robustness
  finding. A single link to `the-evidence/clip` (ViT as the backbone CLIP later
  used) is welcome; a second pass over CLIP's argument is repetition.
- The phrase "doing the work" has appeared in three of the last several
  Evidence/Mechanics pieces ("the data, not the objective, did the work"). It is
  now a house tic. Do not use it. Make the same point in this article's own
  words.

## Teach a short list completely

Candidate ideas, in dependency order (the writer finalizes and may cut):
1. What ViT is: patches as tokens, the smallest change to a Transformer that lets
   it read an image. One concrete worked example of the patch count (a 224x224
   image at 16x16 patches = 196 patches + 1 class token).
2. Inductive bias: what a CNN assumes about images for free, what ViT gives up,
   and why that trade only pays off with enough data. Define "inductive bias" in
   plain words at first use.
3. The scale ladder with real numbers: ImageNet-1k vs ImageNet-21k vs JFT-300M,
   and where ViT crosses from behind the CNN to ahead. Give the dataset sizes and
   at least one honest accuracy comparison from the paper (e.g. ViT-L/16 pre-trained
   on JFT vs a BiT ResNet baseline; state the exact numbers the researcher verifies).
4. The present: DeiT softens the data condition; ConvNeXt softens the
   architecture claim. What holds and what was oversold.

## Sources and production

- Source policy (lesson/the-evidence): at least 6 sources, at least 3 primary,
  at least 1 secondary. Primary here means the documents that own the claims: the
  ViT paper, the BiT paper (Kolesnikov et al., the CNN baseline ViT compares to),
  DeiT, ConvNeXt, and where possible the JFT-300M description (Sun et al.,
  "Revisiting Unreasonable Effectiveness of Data"). Verify every accuracy figure
  against the paper that owns it; ViT's tables report many configurations, so pin
  each number to its exact model, dataset, and resolution.
- Production policy: profile "balanced". Model tier "capable" for every role
  (recorded actual: claude-opus-4-8). Effort guidance: writing-coach low,
  researcher high, writer medium, editor high; none marked `required`. Effort is
  not independently dial-able through the run's child-agent interface, so each
  role runs at the session's default reasoning; no `required` directive is traded
  down, so there is no policy deviation to report.

## Original-work target

The article's own contribution: put the paper's conditional result back together
with the shorthand that dropped the condition, using the paper's own accuracy
numbers across the three data scales, and show with the later corrections
(DeiT, ConvNeXt) exactly which half of "Transformers beat CNNs" the evidence
supports and which half it does not.
