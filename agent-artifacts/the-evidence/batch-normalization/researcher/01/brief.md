# researcher brief: the-evidence/batch-normalization (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and boundaries
  (residuals, AlexNet, and gradient descent are taught elsewhere; link them).
- `../../editorial-direction.md` — citation standard, series territory, declared reader.

Output: `evidence.md` (this directory)

Focus and known risk surface (decisions the inputs do not settle):

- The paper (Ioffe & Szegedy 2015, "Batch Normalization: Accelerating Deep Network
  Training by Reducing Internal Covariate Shift," arXiv 1502.03167) is the primary
  that owns what batch norm is and what it claimed. Read it. Record precisely: the
  normalization procedure (per-mini-batch mean/variance, the learned scale/shift
  parameters, how inference differs from training), the exact speedup claim on
  ImageNet (the step-count reduction), and the ensemble top-5 result the paper
  reported (the figure it gave for reaching/surpassing human-level, with its
  denominator and test set). Record the paper's own definition of "internal
  covariate shift" in its own words.
- The correction: Santurkar et al. 2018 ("How Does Batch Normalization Help
  Optimization?", NeurIPS) is the primary that contradicts the stated mechanism.
  Record exactly what they did (the experiment adding noise after batch norm to
  increase internal covariate shift while training stayed fast; the
  landscape-smoothing / Lipschitz measurements) and how strong the claim is.
- A third primary on the ongoing debate strengthens the "still argued" note: e.g.
  Bjorck et al. 2018 ("Understanding Batch Normalization") on higher learning
  rates, or Wu & He 2018 ("Group Normalization") on batch-size dependence. Record
  what each establishes firsthand.
- Search for what cuts against the angle in both directions: any defense of the
  internal-covariate-shift account, or evidence the Santurkar result is contested
  or bounded. Contradictory evidence is the most valuable line; record it.
- Give every figure its denominator and owning primary. Classify each source
  primary/secondary with a reason. A source asset candidate: note whether any
  paper carries a clean figure a reader could learn from (a training-curve
  comparison, or the ICS-noise experiment plot), or write None found.

Run-environment caveat: record each source's own resolving page (arXiv,
NeurIPS/publisher), never a fetch-proxy URL.
