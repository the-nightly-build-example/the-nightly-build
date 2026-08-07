# researcher brief: the-evidence/resnet (01)

Inputs:
- editorial-direction.md — citation standard, series territory, declared reader
- commission.md — subject, angle, boundaries, source policy

Output: researcher/01/evidence.md

Research questions (answer each against the owning primary):
- Read arXiv:1512.03385 in full. Record exactly: the degradation problem (that
  deeper plain nets had higher TRAINING error, Fig 1, not overfitting); the
  residual/skip-connection formulation; the depths tested (34/50/101/152 and the
  1202-layer CIFAR probe); ImageNet top-5 error (single model and the 3.57%
  ensemble); the ILSVRC/COCO 2015 sweep; parameter counts vs VGG. Locators.
- What the paper claimed and did not: it is image recognition; it did not claim
  the residual trick would generalize to other architectures. Confirm from text.
- How the record held up: open primaries analyzing WHY residuals help —
  identity-mappings follow-up (He et al. 2016); the 'ensemble of relatively
  shallow networks' view (Veit et al. 2016); loss-landscape work (Li et al.
  2018) if accessible. Establish that residual connections are reused inside the
  Transformer (the 'Add & Norm' residual path) from the attention paper itself.
- 'Why famous': a dated citation count from a primary index.
Contradiction hunt: claims that ResNet 'just added layers' or that depth alone
drove the gain; whether the 1202-layer net actually did better (it did worse on
CIFAR — record that honestly).

Verify every number against the primary that owns it. Record each source's own
resolvable URL (not the fetch route). Classify primary vs secondary with a
reason. Fill the Contradictions section only after a real search for what breaks
the angle. Meet the source policy in the commission. Report the evidence path,
the record's most important limitation, and whether the evidence undermines the
commissioned angle.
