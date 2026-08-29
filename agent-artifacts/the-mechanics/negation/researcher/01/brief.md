# researcher brief: the-mechanics/negation (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md) — citation standard, series territory, declared reader
- commission.md (../../commission.md) — behavior, causal chain, distinct contribution

Output: ./evidence.md

Read the primary research, not summaries of it. Target sources:

- Primary measurements that language models handle negation poorly. Candidates to
  read and verify firsthand: Kassner & Schütze, "Negated and Misprimed Probes for
  Pretrained Language Models" (2020); Ettinger, "What BERT is not: Lessons from a
  new suite of psycholinguistic diagnostics" (2020); Truong et al., "Language
  Models Are Not Naysayers: An Analysis of Language Models on Negation Benchmarks"
  (2023); García-Ferrero et al., "This is not a Dataset" (2023). Record the exact
  negation-versus-affirmation gap each measured, on which models, and the scope.
  Prefer results that cover recent instruction-tuned models where available.
- The vision-language "bag-of-words" evidence for the image case: Yuksekgonul et
  al., "When and Why Vision-Language Models Behave Like Bags-of-Words, and What to
  Do About It" (ARO benchmark, 2023), and any primary source measuring
  text-to-image failure on negated prompts. Establish that the text encoder's
  order/compositional insensitivity is measured, not asserted.
- Primary or authoritative documentation of the engineering patches: how negative
  prompts and classifier-free guidance work in diffusion image models (the
  classifier-free guidance paper, Ho & Salimans 2022, and reputable model docs).
  Establish what a "negative prompt" actually does.
- Enough on the training-data imbalance claim to source it: any primary analysis
  of how rare explicit negation is in text corpora, or state it as an estimate if
  only softer evidence exists. Do not assert a precise frequency without a source;
  mark it as estimate if needed.

Answer these questions for the writer:
1. How much worse, measured, is negation than affirmation, on what models and
   tasks? Give at least one concrete figure with scope.
2. What is the strongest evidence that a text-to-image model treats "no X" as "X"
   (the bag-of-words / compositionality finding), stated exactly?
3. What actually reduces the failure (scale, instruction tuning, negative prompts,
   classifier-free guidance), and what does the primary evidence say about how
   much?
4. What is genuinely still open about the internal mechanism of negation failure,
   sourced to people who build or study these systems?

Search for what breaks the angle: evidence that frontier instruction-tuned models
now handle simple text negation well (so the failure is mostly an image and
edge-case phenomenon), and record it in full. That contradiction sharpens the
lesson rather than sinking it. Confirm every URL resolves to the paper's own page.
