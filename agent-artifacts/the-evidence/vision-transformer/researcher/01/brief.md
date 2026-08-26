# researcher brief: the-evidence/vision-transformer (01)

Inputs:
- `commission.md` (artifact root) — the angle, the required figures, and the boundaries.
- `editorial-direction.md` (artifact root) — citation standard, series territory, declared reader.

Output: `.nb-work/the-evidence/vision-transformer/agent-artifacts/the-evidence/vision-transformer/researcher/01/evidence.md`

This round's focus: nail the numbers the angle rests on, each against the document
that owns it.
- From the ViT paper: the patch setup (image size, patch size, resulting sequence
  length, class token, position embeddings); the exact statement that ViT trails
  CNNs when trained on mid-size data and matches or beats them only after
  large-scale pre-training; and at least one clean accuracy comparison pinned to
  its exact model, dataset (ImageNet-1k vs ImageNet-21k vs JFT-300M), and
  resolution.
- The dataset sizes: ImageNet-1k (~1.28M), ImageNet-21k (~14M), JFT-300M (~303M,
  from Sun et al. if reachable).
- The CNN baseline ViT compares against (BiT / ResNet, Kolesnikov et al.).
- The two present-day correctives: DeiT (competitive ViT on ImageNet-1k alone via
  augmentation + distillation) and ConvNeXt (a modernized CNN matching
  Transformers). Record what each actually claims, and any figure the article
  would cite.
- Search for what breaks the angle: places where ViT's advantage held at smaller
  scale, or where the "you need JFT" reading has been overstated. Record it under
  Contradictions.
Classify each source primary/secondary with the authorship-and-stake test. Confirm
every URL resolves to the document's own page.
