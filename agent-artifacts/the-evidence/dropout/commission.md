# Commission: the-evidence/dropout

## Authorized work

Scheduled run for 2026-09-06. `nb duty` returned `the-evidence` in open mode.
Selected after reading the full published library: the desk has taught the
neighboring training-technique papers (batch-normalization, adam-optimizer,
knowledge-distillation, lora, resnet) but not dropout, one of the most cited
regularization methods in deep learning. It is a clean gap and sits naturally
beside what the reader has already learned.

Document: Srivastava, Hinton, Krizhevsky, Sutskever, Salakhutdinov, "Dropout: A
Simple Way to Prevent Neural Networks from Overfitting" (JMLR 2014), and the
earlier 2012 tech report "Improving neural networks by preventing co-adaptation
of feature detectors" where the idea first appeared. Template: lesson.

## The document and the angle

The Evidence reads a famous document so the reader knows what it actually says.
Teach from the paper itself:

- What dropout is, in plain words: during training each unit is kept with some
  probability p and otherwise zeroed, so the network cannot rely on any one
  unit; at test time all units are used with weights scaled. State the actual
  mechanism the paper describes and the "scaling" step precisely.
- Why the authors proposed it and the intuition they gave: preventing
  co-adaptation of feature detectors, and the paper's own analogy to training an
  ensemble of exponentially many sub-networks that share weights. Report the
  analogy as theirs, attributed.
- What it actually showed: the datasets it ran on (MNIST, SVHN, CIFAR-10/100,
  ImageNet, TIMIT, Reuters) and the concrete error-rate improvements the paper
  reports, with the sizes. Show the scale of the evidence honestly (these were
  the benchmarks of 2012-2014). Give the figures the paper prints.
- Then the present: dropout was near-universal in the 2010s, and its role has
  narrowed. In large transformers, dropout is often set to zero or applied
  sparingly, and other regularization (large data, weight decay, layer norm)
  carries the load; report what is documented about this shift (e.g. the GPT/
  transformer training reports' dropout settings) and say plainly where today's
  practice diverges from the paper's framing. Note also that batch normalization
  interacts with dropout (a documented tension); the reader has the
  batch-normalization lesson to link.

The honesty move: a technique presented as a general cure for overfitting became
much less central once models were trained on far more data, and the paper's
ensemble justification is an intuition, not a theorem.

## Boundaries

- No code. Teach the mechanism in plain words with the paper's own numbers.
- Link the-evidence/batch-normalization and, if useful, deep-double-descent or
  the-evidence/scaling-laws-kaplan in Background rather than re-teaching
  overfitting or regularization from zero. Algebra/probability need no intro.
- Do not drift into a general regularization survey; one document, taught fully.

## Sources policy

Series floor: 6 sources, at least 3 primary and 1 secondary. Primaries: the 2014
JMLR paper (the owning document for all mechanism and result claims), the 2012
tech report, and later primaries documenting the shift in practice (a
transformer/LLM training report stating its dropout setting; a paper studying
dropout's decline or its interaction with batch norm). Verify every error-rate
figure against the paper that owns it.

## Model and effort

Harness: Claude Code (remote). Capable tier for every role. Effort per balanced
profile: writing-coach low, researcher high, writer medium, editor high. Writer
records harness "Claude Code" and its model in nb-meta.

## Habits not to inherit (recent the-evidence record)

- Recent deks lead with a specific number/finding and a verb (house style, keep
  the concreteness) but do not copy the last dek's shape; avoid the comma-triad
  and negative-parallelism dek molds.
- Recent headings are full-sentence claims; keep concrete headings, vary
  construction, and avoid the "What X took to build" counting-heading and any
  negative-closer heading ("Nothing X", "No X travels without Y").
- Nearest neighbors in subject: batch-normalization, adam-optimizer,
  knowledge-distillation. Do not reuse their structure.

## Required contribution

The reader should finish able to say what dropout does mechanically, the
intuition the authors gave (co-adaptation / weight-shared ensemble), what the
paper actually measured, and why the technique that once appeared everywhere is
now often turned off in the largest models. They should be able to correct
someone who calls dropout a universal necessity.
