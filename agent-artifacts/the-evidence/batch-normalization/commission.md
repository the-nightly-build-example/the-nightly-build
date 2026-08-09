# Commission: the-evidence/batch-normalization

## Authorized work

Scheduled run for 2026-08-09. `nb duty` returned `the-evidence` in open mode.
This slot replaces an earlier pick (`gpt-3`) that collided with the already
published `the-evidence/gpt-3-few-shot` (2026-07-19), which teaches that exact
paper. One article; a genuinely unwritten document.

## The document

Sergey Ioffe and Christian Szegedy, "Batch Normalization: Accelerating Deep
Network Training by Reducing Internal Covariate Shift" (2015). The desk reads a
famous AI document so the reader knows what it actually says. Batch normalization
is one of the most-used techniques in deep learning — it sits inside AlexNet-era
and ResNet-era vision networks and countless models since — and this paper is the
one everyone cites for it. It is also the desk's ideal specimen: a document whose
technique is indispensable and whose own stated explanation for *why* it works was
later shown, in controlled experiments, to be wrong. The paper puts that
explanation in its title.

Why now: the reader has met AlexNet and ResNet on this desk, both of which lean on
normalization, so the course has made this document readable. And "reduces
internal covariate shift" is still repeated as the reason batch norm works, a
claim the reader should be able to check.

## What the lesson teaches (two or three ideas)

1. **What batch normalization is and what it does.** In plain terms: a layer that
   takes each mini-batch of activations, rescales them to zero mean and unit
   variance using that batch's own statistics, then applies two learned parameters
   that let the network undo the normalization if it needs to. Mean and variance
   are basic statistics and need no introduction. Say what it bought: much faster
   training (the paper reaches the same ImageNet accuracy in far fewer steps),
   tolerance of higher learning rates, and a mild regularizing effect. Give the
   real numbers and scale from the paper (the step-count speedup; the ImageNet
   Inception result the paper reported as reaching and passing human-level top-5).

2. **The mechanism the paper claimed.** The paper's stated reason is "internal
   covariate shift": as an early layer's weights change during training, the
   distribution of inputs to later layers keeps shifting, and normalizing each
   layer's inputs is said to stabilize that. Teach this claim clearly and fairly —
   it is intuitive and it is the reason the technique is usually explained by.

3. **What later work found, and how to hold both.** Santurkar et al. 2018 ("How
   Does Batch Normalization Help Optimization?", MIT) tested the claim directly:
   they added noise *after* batch norm to deliberately increase internal covariate
   shift and the network still trained fast, and they measured that batch norm's
   real effect is smoothing the optimization landscape (making the loss and its
   gradients change more gently), not reducing distribution shift. Bring it to the
   present: the technique is right and everywhere; the paper's headline
   explanation for why is the part that did not survive a controlled test. Note
   honestly what is still debated (batch norm's regularization effect, its
   dependence on batch size, why it sometimes hurts) without overclaiming a
   settled replacement.

The reader should finish able to say what batch norm does, why the "internal
covariate shift" story is repeated, and why the evidence says that story is not
why it works.

## Boundaries

- `the-evidence/alexnet` and `the-evidence/resnet` are published and mention batch
  norm in passing; do not re-teach residual connections or AlexNet. Link where a
  claim needs them.
- `the-mechanics/gradient-descent` is published; do not re-teach gradient descent.
  Link it if the optimization-landscape idea needs grounding.
- Claims about what the paper did come from the paper itself; the correction comes
  from Santurkar et al. and peers, read directly. When the document's stated
  mechanism is wrong, say exactly how, per the desk's mandate.

## Original contribution

Separate the technique from its explanation: batch normalization the method is
indispensable and does what the paper showed, while "reducing internal covariate
shift," the reason the paper's own title gives, is contradicted by later
controlled experiments that isolate the cause. The reader gets a clean case of a
foundational document being right about what to do and wrong about why.

## Source policy (from `nb source-policy`)

Template floor governs: minimum 6 sources, primary ≥ 3, secondary ≥ 1. Primaries:
Ioffe & Szegedy 2015; Santurkar et al. 2018; a further primary on the mechanism
debate or batch-size dependence (e.g. Bjorck et al. 2018 "Understanding Batch
Normalization," or Wu & He 2018 "Group Normalization"). Contested figures resolve
to the owning primary.

## Production policy (from `nb production-policy`, profile: balanced)

- writing-coach: capable (Sonnet), low effort
- researcher: capable (Opus), high effort
- writer: capable (Opus), medium effort
- editor: capable (Opus), high effort

None `required`; no deviation to record.

## This edition's neighbors

- `the-instruments/fid` (tonight) also involves an Inception-network component;
  keep the two distinct — batch norm is a training method, FID is an evaluation
  metric — and cross-link at most. `the-mechanics/word-order`,
  `what-could-go-wrong/situational-awareness`, `when-ai-breaks/tesla-autopilot`:
  no overlap.

## Recent habits not to inherit

- Evidence openers lean on "You have almost certainly seen…" and close the Why
  card on "By the end you can say exactly…". Write the promise in this document's
  own terms, off that mold.
- The "method right, reason wrong" arc is a genuine, earned contrast; do not let
  it collapse into the negative-parallelism reflex ("not X, but Y") the slop
  standard flags. Two earned contrasts in a piece is already a lot.
- Do not close on the second-person "Now you know…" / "The next time you see…"
  mold, and do not reuse "None of this makes X fake." Vary any note label; do not
  default to "In plain language."

## Prior coverage to link, not re-teach

- `the-evidence/resnet`, `the-evidence/alexnet` — the vision nets that use batch norm.
- `the-mechanics/gradient-descent` — the optimization the smoothing claim is about.
