# Draft handoff: the-evidence/vision-transformer (01)

## Original-work sentence

This article turns the ViT paper's throwaway qualifier, "without strong
regularization," into the hinge of the whole story, using it to show that DeiT
did not overturn the paper so much as supply the exact ingredient its own
authors had named as missing.

The work is visible in the piece: the qualifier is quoted in its own note in
"The condition was the recipe, not the architecture," the slogan it corrects
("Vision Transformers need JFT-scale data") is named beside it and sourced to a
2022 survey that still repeats it, and the takeaway lands the two-facts-at-once
reading rather than the collapsed slogan.

## Proof result

`./nb check --series the-evidence --library /home/user/library-checkout <article>`
(links on, after `nb stamp`) returns **BLOCK: 0, WARN: 0, PUBLISHABLE**. Stamped
at 1957 words, 9 min read, 6 sources.

No warnings were left standing.

## Resolution of the round-01 source gap (now closed)

Round-01 draft was blocked by `B-SOURCE-KIND` / `W-SOURCES-MIN`: the researcher's
first evidence record supplied 5 primaries and no secondary, and the resolved
source policy requires 6 sources with at least 1 secondary. The researcher's
round-02 record
(`researcher/02/evidence.md`) added the secondary: Khan et al., "Transformers in
Vision: A Survey" (arXiv 2101.01169, ACM Computing Surveys 2022), Kind:
secondary.

It is cited once as **s4**, in the opening of "The condition was the recipe, not
the architecture," to document that the "ViT needs large-scale data" reading is
the received view in the survey literature. Adding it in first-citation position
there renumbered the two correctives: DeiT is now **s5**, ConvNeXt **s6**.

Per the researcher's caveat, the survey's "13% drop" restatement is NOT used: it
is recorded as an unverified secondary repetition. The article quotes only the
survey's qualitative claim ("pre-training ViT on a medium-range dataset would not
give competitive results") and attributes it to the survey as the circulating
view. Every hard accuracy figure in the piece is ViT's own (85.30 / 87.76 /
88.55) or its named baseline's (BiT-L 87.54).

## Notes for the editor

- Headline "The condition was the recipe, not the architecture" is a deliberate
  earned contrast, not a reflex negative-parallelism: the section names the real
  slogan it corrects and now sources it to the 2022 survey, then quotes the
  paper's own qualifier against it.
- JFT snapshots are kept separate per the record: 303M images / 18k classes cited
  to ViT (Sec 4.1); ~300M images / 375M labels cited to Sun et al. Never merged.
- 83.1% is used as the fair DeiT headline (no-distillation, ImageNet-1k only);
  85.2% is not quoted. The distilled-teacher-is-a-CNN point is acknowledged in
  one clause ("before any of the further gains they get by distilling from a
  convolutional teacher") rather than expanded.
- CLIP is linked once (its vision half is a ViT) with no second pass over its
  contrastive/robustness argument, per the adjacency alert.
- Furniture: one stat strip (the two data-scale poles, 1.3M vs 303M), one table
  (the accuracy crossover), one note (the paper's own qualifier, quoted). No
  chart or source asset: the crossover figures were reproduced as an honest
  table of pinned numbers rather than captured images, and the argument spends
  the numbers rather than a specific diagram.
</content>
