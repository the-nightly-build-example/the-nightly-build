# Draft handoff: the-evidence/gpt-1 (writer 01)

## Original work
This lesson separates GPT-1's recipe into its two halves and traces each across
the later GPT reports, showing that the per-task fine-tuning and input
transformations the 2018 paper spends its longest section building are the half
its own descendants discarded, while the unsupervised pre-training it treats
almost in passing is the half every later model kept, a split the evidence
records contain but never draw.

## Proof result
`nb check` with links (exact brief command): **BLOCK: 0, WARN: 0** —
PUBLISHABLE. `nb stamp` written: words 2079, reading_minutes 9, sources 8 (six
primary, two secondary). No warnings left standing.

## Furniture
Three components, each load-bearing: an "In plain language" note defining
generative pre-training; a captured source asset (Fig. 1, the paper's own
four-task input-transformation diagram) in the task-shapes section; a rendered
chart (Fig. 2, `chart-1.py`) showing the per-dataset gains falling from 8.9 to
0.6, which carries the "report the scale honestly" beat. The descendant scaling
(117M -> 1.5B -> 175B) is left in prose rather than a fourth component.

## Exactness handled
- Parameter count: the paper states only the shape (12 layers, 768, 12 heads,
  FFN 3072); the 117M figure is attributed to the 2019 GPT-2 report ("equivalent
  to the original GPT"), not to the 2018 paper.
- Corpus stated as the paper states it ("over 7,000 unique unpublished books"),
  with the BooksCorpus origin's 11,038 flagged as an unexplained gap.
- Results reported honestly: 9 of 12, three losses (RTE, MRPC, SST-2), the
  spread of gains charted, GLUE given as the body's 72.8 vs 68.9 (not the intro's
  unreconcilable 5.5%), and the ablation showing pre-training worth ~14.8 points
  while the auxiliary objective was a wash (75.0 without vs 74.7 with).
- The "ImageNet moment" reception (Ruder, 2018) is presented as contemporaneous
  reception and explicitly held apart from the modest 2018 margins; the present
  arc is cited firsthand from GPT-2, GPT-3, GPT-4, with the Liu et al. survey
  naming the pre-train/prompt shift from outside OpenAI.
- Taught ground linked, not re-taught: attention-is-all-you-need (decoder), bert
  (Background), tokenization and embeddings (prose, first use). GLUE named only
  as what the 72.8 aggregate scores, no benchmark retelling (winogrande neighbor).

## Open evidence or voice question
None.
