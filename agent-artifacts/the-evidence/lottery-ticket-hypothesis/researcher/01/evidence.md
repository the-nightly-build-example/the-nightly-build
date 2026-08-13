# Evidence record: the-evidence/lottery-ticket-hypothesis (01)

The evidence supports the commissioned angle firmly. The primary paper (Frankle
& Carbin, ICLR 2019) states the hypothesis, the iterative-magnitude-pruning
procedure, and the reset-to-original-initialization step in language I verified
against the paper's own text, and it demonstrates the central result only on
small vision networks (LeNet on MNIST; Conv-2/4/6, VGG-19, and Resnet-18 on
CIFAR-10). The paper itself records that its plain procedure fails on the two
larger nets (VGG-19, Resnet-18) at the standard learning rate and needs a
warmup workaround, which is the seam the later work widened. Frankle's own 2020
follow-up replaces reset-to-initialization with rewinding to an early training
iteration to get matching subnetworks at ImageNet scale. The two critique papers
each complicate the "special initialization" reading: Liu et al. find the winning
-ticket initialization gives no gain over random at the standard learning rate,
and Zhou et al. find that only the sign of the initialization matters and that a
mask alone, with no training, already classifies well above chance. The "no
cheap up-front ticket" point is well supported: every method here finds the mask
by training and pruning, not before training. Where the record is thin: the
exact per-sparsity figures (the P_m percentages and speedups) were read from the
paper's HTML rendering of its figures and captions, not recomputed, so treat the
second decimal as the paper's own reported reading rather than an independently
checked one. There is also a live terminology hazard, recorded under
Contradictions: "P_m" in the 2019 paper is the percentage of weights *remaining*,
while later papers report "sparsity" as the percentage *pruned*, so 10% in one
frame is 90% in the other.

## Sources

```text
URL:         https://arxiv.org/abs/1803.03635
Kind:        primary. Frankle and Carbin authored the hypothesis, the method, and
             the experiments; the paper owns every claim about what was run and
             found. Published version: https://openreview.net/forum?id=rJl-b3RcF7
             (ICLR 2019). Read via the ar5iv HTML rendering of the full text.
Establishes: The Lottery Ticket Hypothesis; the iterative-magnitude-pruning (IMP)
             procedure and the reset-to-original-initialization step; that a
             randomly reinitialized winning ticket performs far worse; the scale
             of the demonstration (LeNet/MNIST, Conv-2/4/6 and VGG-19/Resnet-18 on
             CIFAR-10); that the plain procedure fails on the two larger nets at
             the standard learning rate and needs warmup.
Paraphrase:  A dense, randomly initialized network contains a much smaller
             subnetwork that, trained from the same initial weights, matches the
             full network's test accuracy in no more training iterations. You find
             that subnetwork by training the full net, pruning the smallest-
             magnitude weights, and resetting the survivors to the exact values
             they had at initialization, repeating the cycle. The mask alone is
             not enough: reset those same survivors to fresh random values and the
             subnetwork trains slower and tops out lower.
Locators:    Section 1 (hypothesis statement and the four-step procedure);
             Section 2 (LeNet/MNIST, random-reinit comparison); Section 3
             (Conv-2/4/6 on CIFAR-10); Section 4 (VGG-19 and Resnet-18, learning
             rate and warmup); Abstract (the "10-20%" summary claim).
Quote:       Hypothesis (Section 1): "A randomly-initialized, dense neural network
             contains a subnetwork that is initialized such that -- when trained in
             isolation -- it can match the test accuracy of the original network
             after training for at most the same number of iterations."
             Procedure step (Section 1): the surviving weights are reset to "its
             initialization from [the] original network before it was trained,"
             producing the winning ticket f(x; m . theta_0).
             Random reinit (Section 2): "When randomly reinitialized, winning
             tickets perform far worse," and reinitialized nets "learn increasingly
             slower than the original network and lose test accuracy after little
             pruning."
             Larger nets (Section 4): "At the higher learning rate [0.1], iterative
             pruning does not find winning tickets, and performance is no better
             than when the pruned networks are randomly reinitialized."
```

```text
URL:         https://arxiv.org/abs/1912.05671
Kind:        primary. Frankle, Dziugaite, Roy, and Carbin authored this follow-up;
             it owns the rewinding method and the scale results. Published in ICML
             2020 (PMLR). Read via the ar5iv HTML rendering.
Establishes: That the original reset-to-initialization procedure does not yield
             matching subnetworks for larger networks; that rewinding the survivors
             to their values at a small early training iteration k (rather than to
             iteration 0) does; the linear-mode-connectivity / instability-analysis
             framing that explains why.
Paraphrase:  For small settings (MNIST) the matching subnetwork can be reset all
             the way to initialization, but for large settings (Resnet-50 and
             Inception-v3 on ImageNet, Resnet-20 on CIFAR-10) it only matches when
             reset to an early iteration a few percent into training. The paper
             ties this to when the network first becomes stable to the noise of
             stochastic gradient descent: two copies trained with different data
             orderings converge to the same linearly connected minimum only after
             that early point.
Locators:    Abstract and the IMP-with-rewinding sections; the ImageNet results
             tables for Resnet-50 and Inception-v3.
Quote:       "These subnetworks only reach full accuracy when they are stable to
             SGD noise, which either occurs at initialization for small-scale
             settings (MNIST) or early in training for large-scale settings
             (Resnet-50 and Inception-v3 on ImageNet)."
```

```text
URL:         https://arxiv.org/abs/1810.05270
Kind:        primary. Liu, Sun, Zhou, Huang, and Darrell authored this critique;
             it owns its own pruning-from-scratch experiments and its own test of
             the winning-ticket initialization. ICLR 2019. Read via ar5iv.
Establishes: That the winning-ticket initialization gives no advantage over random
             initialization at the standard (large) learning rate; that it helps
             only under a small learning rate with unstructured pruning, and that
             the small learning rate itself yields worse accuracy; and the broader
             thesis that a pruned architecture trained from scratch matches or
             beats one fine-tuned from inherited weights.
Paraphrase:  Retraining a pruned network from fresh random weights does as well as
             or better than keeping the large model's "important" weights, so the
             learned weight values are not what pruning is buying. Tested directly
             against the lottery-ticket claim, the winning-ticket initialization
             only outperformed random initialization when the learning rate was
             lowered to 0.01, and that lower rate produces lower final accuracy
             than the standard 0.1. The advantage also appeared only for
             unstructured (per-weight) pruning, not structured (whole-filter)
             pruning.
Locators:    Section 6 (comparison with the Lottery Ticket Hypothesis; Tables 8-9,
             Figure 7); Abstract and Section 1 (the from-scratch thesis).
Quote:       "with optimal learning rate, the 'winning ticket' initialization as
             used in Frankle & Carbin (2019) does not bring improvement over random
             initialization." And: "using the winning ticket as initialization only
             brings improvement when the learning rate is small (0.01), however such
             small learning rate ... [yields] a lower accuracy."
```

```text
URL:         https://arxiv.org/abs/1905.01067
Kind:        primary. Zhou, Lan, Liu, and Yosinski authored this analysis; it owns
             its own ablations, mask-criteria study, and the supermask result.
             NeurIPS 2019. Read via ar5iv.
Establishes: That preserving only the SIGN of the original initialization (not its
             magnitude) is enough for the ticket to train ("signs are all you
             need"); that setting pruned weights to zero specifically (not their
             init value) matters and the mask itself carries learned information;
             and the "supermask" -- a mask applied to an untrained, randomly
             initialized network that already classifies well above chance with no
             weight training at all.
Paraphrase:  The winning ticket's special initialization is less special than it
             looks. Keep the sign of each surviving weight and even set its
             magnitude to a constant, and the subnetwork still trains well, which
             says the useful region is the whole correct-sign quadrant. The pruning
             mask is doing part of the work of training: a mask alone, found by
             magnitude, applied to fresh random weights, reaches 86% on MNIST and
             41% on CIFAR-10 without any gradient steps on the weights.
Locators:    Sign-preservation and mask-criteria sections; the supermask section
             with the untrained-network accuracies.
Quote:       Supermask: masks applied to "an untrained, randomly initialized
             network" reach "86% on MNIST, 41% on CIFAR-10."
             Signs: the variants "work better when we ensure that the new values of
             the kept weights are of the same sign as their original initial
             values."
```

```text
URL:         https://arxiv.org/abs/2007.12223
Kind:        primary. Chen, Frankle, Chang, Liu, Zhang, Wang, and Carbin authored
             this extension; it owns the BERT subnetwork results. NeurIPS 2020.
             Read via the arXiv abstract page.
Establishes: A concrete present-day usage of the winning-ticket idea on a widely
             used pre-trained model (BERT), and the boundary the shorthand hides:
             the masks are still found by iterative magnitude pruning, i.e. by
             training and pruning, not read off cheaply before training.
Paraphrase:  The lottery-ticket phenomenon carries to pre-trained BERT: for a range
             of GLUE/SQuAD-style downstream tasks there are matching subnetworks at
             40% to 90% sparsity. Unlike earlier NLP work these can be found "at
             (pre-trained) initialization" -- meaning the pre-trained weights serve
             as theta_0 with no rewinding -- but identifying the mask still requires
             iterative magnitude pruning on the task, so the ticket is still found
             in retrospect, not up front.
Locators:    Abstract.
Quote:       "For a range of downstream tasks, we indeed find matching subnetworks
             at 40% to 90% sparsity. We find these subnetworks at (pre-trained)
             initialization, a deviation from prior NLP research where they emerge
             only after some amount of training."
```

```text
URL:         https://iclr.cc/Conferences/2019/Awards
Kind:        primary for the award fact -- ICLR is the body that granted it. Names
             the Lottery Ticket paper as an ICLR 2019 Best Paper Award winner.
Establishes: The "best-paper award" claim in the commission, and that it was one of
             two co-equal Best Paper Awards (not a sole "best paper").
Paraphrase:  ICLR 2019 gave two Best Paper Awards. One went to "The Lottery Ticket
             Hypothesis: Finding Sparse, Trainable Neural Networks" by Jonathan
             Frankle and Michael Carbin.
Locators:    Awards page listing.
Quote:       (Award listing) "Best Paper Award ... The Lottery Ticket Hypothesis:
             Finding Sparse, Trainable Neural Networks."
```

```text
URL:         https://medium.com/syncedreview/iclr-2019-mila-microsoft-and-mit-share-best-paper-honours-440675d5773e
Kind:        secondary. SyncedReview reporting on the ICLR 2019 awards from outside
             the authoring party; provides reception context, not firsthand claims.
Establishes: Context that the award was shared between two papers and that the
             Lottery Ticket paper's headline result was reported as its "10-20% of
             the size" claim; useful only as evidence the paper drew notice, not as
             a source for any technical figure.
Paraphrase:  Reporting from May 6, 2019 that ICLR 2019 split its Best Paper honours
             between "Ordered Neurons" (MILA/Microsoft) and "The Lottery Ticket
             Hypothesis" (MIT), summarizing the latter by its 10-20%-of-size result.
Locators:    Article body.
Quote:       (Repeating the paper) "We consistently find winning tickets that are
             less than 10-20% of the size of several fully-connected and
             convolutional feed-forward architectures for MNIST and CIFAR10."
```

## Contradictions

- **Terminology, a real reader-facing trap.** Frankle & Carbin 2019 report P_m as
  the percentage of weights *remaining* (smaller P_m = sparser). Liu et al., Chen
  et al., and most later work report "sparsity" as the percentage *pruned*. So
  "P_m = 10%" (2019) and "90% sparsity" (later) can describe the same network. Any
  figure the article quotes must state which frame it is in, or it will read as
  ten times denser or sparser than intended.

- **The special-initialization reading vs. Liu et al.** The popular shorthand says
  the winning ticket's *specific initial weights* are what make it trainable. Liu
  et al. find no advantage of those weights over fresh random weights at the
  standard learning rate; the advantage appears only at a small learning rate that
  itself costs accuracy, and only for unstructured pruning. This does not overturn
  the existence result. It undercuts the practical "these exact weights are magic"
  reading. Steelman for the original: Frankle & Carbin's own Section 4 already
  reported that the plain procedure fails on VGG-19/Resnet-18 at learning rate 0.1,
  so the two papers agree on the fact and differ on how much it matters.

- **The special-initialization reading vs. Zhou et al.** Zhou et al. push further:
  only the *sign* of the initialization is needed, and a mask with no weight
  training (the supermask) already works far above chance. This complicates "the
  weights are special" by relocating much of the signal into the mask and the sign.

- **"At initialization" vs. the need for rewinding.** The 2019 paper resets to
  iteration 0. Frankle et al. 2020 shows that for larger networks a matching
  subnetwork is found only when reset to an early iteration k > 0, not iteration 0.
  So the clean "a subnetwork trainable from its original random initialization"
  statement is a small-network result; at scale the object is "trainable from an
  early-training checkpoint." The BERT paper is the partial exception (pre-trained
  weights act as theta_0), but its mask still comes from iterative pruning.

- **What strengthens the original method.** The core phenomenon replicated and
  extended. Sparse matching subnetworks are real, are found repeatedly by IMP, and
  carry to ImageNet-scale vision (2020) and to pre-trained BERT (2020). The 2019
  existence claim, read narrowly, has held; it is the practical and "special
  weights" readings that later work trimmed.

- **No source found claiming a cheap up-front ticket that works.** The search for
  a method that identifies a winning ticket *before* training, at general scale,
  turned up the pruning-at-initialization line of work (SNIP, GraSP, and similar)
  as the aspiration, but every matching-subnetwork result in this record is found
  by training and pruning. This supports, rather than breaks, the commission's
  "found in retrospect" point.

## Numbers

```text
Figure: winning tickets are "less than 10-20% of the size" of the original
Owner:  Frankle & Carbin 2019, Abstract
Scope:  weights remaining (not pruned) across the small MNIST/CIFAR-10 nets tested;
        a qualitative summary claim, not a single measured value
```

```text
Figure: LeNet-300-100 on MNIST, architecture: two hidden layers, 300 and 100 units
Owner:  Frankle & Carbin 2019, Section 2
Scope:  MNIST classification; roughly 266K weights before pruning
```

```text
Figure: LeNet winning ticket still matches original accuracy down to about
        P_m = 3.6% of weights remaining; learns fastest around P_m = 13.5%-21.1%
Owner:  Frankle & Carbin 2019, Section 2 (read from the paper's figures/captions)
Scope:  weights remaining; "matches" = within/above original mean test accuracy.
        Read from the HTML rendering of the figures, not recomputed
```

```text
Figure: Conv-2 / Conv-4 / Conv-6 on CIFAR-10 remain above original mean test
        accuracy while P_m > 2%; each converges roughly 2.5x-3.5x faster near its
        best sparsity (e.g. Conv-6 ~2.5x at P_m = 15.1%)
Owner:  Frankle & Carbin 2019, Section 3 (read from figures/captions)
Scope:  weights remaining; CIFAR-10 test accuracy. Second-decimal P_m values are
        the paper's reported readings, not independently checked
```

```text
Figure: VGG-19 on CIFAR-10 -- no winning tickets at learning rate 0.1; with linear
        LR warmup (k = 10000) at 0.1, winning tickets exceed original accuracy
        while P_m >= 1.5%
Owner:  Frankle & Carbin 2019, Section 4
Scope:  weights remaining; CIFAR-10. The warmup workaround is the key qualifier
```

```text
Figure: Resnet-18 on CIFAR-10 -- no winning tickets at 0.1; with warmup (k = 20000)
        at LR 0.03, reaches ~90.5% test accuracy at P_m = 27.1%
Owner:  Frankle & Carbin 2019, Section 4
Scope:  weights remaining; CIFAR-10 top-1 test accuracy
```

```text
Figure: rewinding recovers matching subnetworks at scale -- e.g. Resnet-50 on
        ImageNet at ~30% sparsity when rewound to roughly epoch 5 (a few percent
        into training), where reset-to-iteration-0 fails
Owner:  Frankle et al. 2020
Scope:  ImageNet; "sparsity" here is percentage pruned. Epoch/sparsity values read
        from the paper's tables via HTML rendering, not recomputed
```

```text
Figure: BERT matching subnetworks at 40% to 90% sparsity across downstream tasks
Owner:  Chen et al. 2020, Abstract
Scope:  sparsity = percentage of weights pruned; GLUE/SQuAD-style downstream tasks;
        masks found by iterative magnitude pruning
```

```text
Figure: supermask (mask only, weights untrained) reaches 86% on MNIST, 41% on
        CIFAR-10
Owner:  Zhou et al. 2019
Scope:  test accuracy with no gradient training of the weights; contrast against
        ~10% chance baselines (both are 10-class problems)
```

## Source assets

```text
Asset: Frankle & Carbin 2019, the early-stopping-iteration and test-accuracy vs.
       P_m curves for LeNet (Section 2) and Conv-2/4/6 (Section 3), each with the
       randomly-reinitialized control plotted alongside the winning ticket
Shows: the whole argument in one image -- the winning-ticket curve holds flat as
       weights are removed and turns down only at extreme sparsity, while the
       random-reinit curve degrades early. This is the reset-vs-random comparison
       the lesson centers on
Crop:  must retain both the winning-ticket line and the random-reinit line and the
       x-axis label (percent of weights remaining); do not crop to a single line,
       which would hide the comparison that is the point
```

```text
Asset: Frankle & Carbin 2019, Section 4 VGG-19/Resnet-18 curves showing the
       standard-learning-rate run failing (tracking the random-reinit line) and the
       warmup run succeeding
Shows: concretely that the plain procedure did not scale, the seam the 2020 paper
       widened
Crop:  keep the failing and warmup curves together and the learning-rate labels
```

```text
Asset: Zhou et al. 2019, the supermask result (untrained masked-network accuracy
       bar/'table')
Shows: that a mask alone already carries much of the signal -- the strongest single
       visual for the "the weights are less special than the shorthand says" point
Crop:  retain the accuracy value and the "no training" labeling so it is not
       mistaken for a trained result
```

```text
Asset: Frankle et al. 2020, the sparsity-vs-accuracy curves comparing rewind-to-0
       against rewind-to-early-k at ImageNet scale
Shows: the failure of reset-to-init and the recovery from rewinding, side by side
Crop:  keep both the k=0 and k>0 curves and the sparsity axis
```

## Discarded

```text
URL: https://blockchain.news/ainews/mit-s-lottery-ticket-hypothesis-90-neural-network-pruning-without-accuracy-loss-transforms-ai-inference-costs-in-2024 : promotional blog, no primary figures, conflates the hypothesis with unrelated production-pruning claims; not citable
URL: https://www.authorea.com/doi/full/10.22541/au.176168540.05810555/v1 : unrefereed preprint on GPT-2 lottery tickets; not needed given Chen et al. 2020 covers the pre-trained-model usage from a primary, refereed source
URL: https://arxiv.org/pdf/2403.04861 (A Survey of Lottery Ticket Hypothesis, 2024) : useful as evidence the line is still active, but a survey is secondary and adds no figure the primaries do not already own; left out to avoid padding
```
