# Commission: the-evidence/alexnet

## Authorized work
Scheduled duty for 2026-08-04 returned `the-evidence` as an open section. This
commission fills it with one lesson reading the AlexNet paper. One article only.

## The document
Krizhevsky, Sutskever, and Hinton, "ImageNet Classification with Deep
Convolutional Neural Networks," NeurIPS (NIPS) 2012 — the paper universally
credited as the start of the deep-learning era. The reader keeps hearing "the
2012 ImageNet moment" and "AlexNet proved deep learning works." This lesson
shows what the paper actually reported, on what scale, and what of it held.

## Angle
Read the paper as The Evidence reads documents: state what it is and why it is
famous, walk the method and the numbers, show the scale honestly, then bring it
to the present. The through-line: AlexNet's leap was **one competition result
standing on three preconditions** — ImageNet's labeled scale, GPU compute, and a
stack of anti-overfitting tricks — and most of its specific techniques were
later discarded even as its thesis (depth + data + compute) became the field's
default assumption. Keep a sharp line between what the paper *proved* (a CNN
could win the 2012 ImageNet challenge by ~10 points) and what gets *attributed*
to it (that it invented or proved "deep learning").

## What the writer must establish (verify all against primaries)
- What it did: a deep convolutional network (5 conv + 3 fully-connected layers,
  ~60M parameters) trained to classify ImageNet images into 1000 categories.
- The result: top-5 error of 15.3% on ILSVRC-2012 versus 26.2% for the
  second-best entry; the ILSVRC-2010 top-1/top-5 figures the paper also reports.
- The scale: ~1.2M training images, 1000 classes; trained on two GTX 580 (3GB)
  GPUs over roughly five to six days.
- The engineering that made it work: ReLU (faster training than tanh), the
  two-GPU split forced by memory, local response normalization, overlapping
  pooling, and — the anti-overfitting pair — data augmentation and dropout.
- The precondition it rested on: ImageNet itself (Deng et al. 2009 / Russakovsky
  et al. 2015), the labeled dataset without which the result is impossible.
- What changed since: which specific techniques were superseded (LRN by
  batch normalization; ConvNets challenged for vision by the Vision Transformer)
  and which finding held (scale of data + compute + depth). ImageNet's own later
  audits (label-error / generalization studies) belong here as honest caveats.

## Boundaries
- Teach two or three ideas completely, per the lesson template. Do not attempt a
  full history of computer vision. The dataset (ImageNet) and the hardware story
  are context in service of reading *this paper*, not their own lessons.
- The reader has algebra and probability. Everything else about neural networks
  used here (what a convolution is, what "top-5 error" means, what overfitting
  is) gets taught in plain words on the spot or linked if a prior lesson holds
  it. The library has `the-mechanics/gradient-descent` and
  `the-mechanics/attention`; link, do not re-teach.
- No hype. "Revolution" and "big bang" are the reader's inherited shorthand; the
  lesson earns or qualifies any grand word with the evidence.

## Sources plan
Series policy: min 6 sources, at least 3 primary and at least 1 secondary.
Target primaries: the AlexNet paper itself; the ImageNet dataset paper
(Deng et al. 2009) and/or the ILSVRC challenge paper (Russakovsky et al. 2015)
for scale and margins; one primary documenting what changed (e.g., the
BatchNorm paper, the Vision Transformer paper, or an ImageNet label-error /
accuracy-generalization study). At least one strong secondary retrospective for
context. The researcher owns final source selection and must verify every
number against the primary that owns it.

## Neighboring articles this run (avoid overlap)
Tonight also publishes: `the-instruments/training-compute` (the FLOP number),
`the-mechanics/retrieval` (RAG), `what-could-go-wrong/cyber-uplift`, and
`when-ai-breaks/nh-predict`. This is the only vision/history piece; keep it in
its lane. Do not drift into general scaling-law argument — that is Kaplan/
Chinchilla territory the library already holds.

## Recent shapes to break
The Evidence desk's recent deks lean hard on a single negative-reveal mold
("X never mentions Y," "has four examples and zero citations"). This lesson may
land a genuine finding, but the coach and writer should vary the dek shape and
not reach for that stamped negative-reveal. Vary heading cadence; recent lessons
have used short declarative headings — fine, but avoid the comma-and-"and"
heading mold flagged in `spec/headlines.md`.

## Production record
- Profile: balanced. Model directive: `capable` for every stage (not required).
  Effort directives: writing-coach low, researcher high, writer medium, editor
  high.
- Actual harness: roles run as isolated subagents on model `claude-opus-4-8`
  (the available capable tier). Per-stage reasoning effort is not independently
  settable on these subagents, so effort is inherited; recorded as a deviation,
  permitted because no stage sets `required: true`. Writer records the actual
  model string in `nb-meta`.
