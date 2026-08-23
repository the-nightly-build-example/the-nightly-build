# Evidence: the-evidence/adam-optimizer (01)

The evidence firmly supports the commission's spine. The Adam paper (ICLR 2015)
is read firsthand: its update rule, its four default hyperparameters, its
Theorem 4.1 regret bound, and its complete experiment list are quoted from the
paper itself. Every experiment the paper ran is small by 2026 standards
(logistic regression on MNIST and a 10,000-word IMDB bag-of-words vector; a
two-hidden-layer MLP on MNIST; a small CNN on CIFAR-10; a VAE), with nothing
resembling a language model. The Reddi, Kale & Kumar counterexample (ICLR 2018)
is read firsthand: the exact linear-function sequence, the parameter settings
that make Adam diverge to the worst point in the domain, the named flaw in the
original proof (the sign of the quantity Gamma_t), and the AMSGrad fix. The
field's shrug is documented with two concrete artifacts: PyTorch ships AMSGrad
as an off-by-default flag, and the largest standardized optimizer benchmark
(Schmidt et al., ICML 2021) finds Adam a strong default that fifteen newer
methods, AMSGrad among them, fail to consistently beat. AdamW's decoupled weight
decay is read firsthand as the variant that did displace plain Adam.

Where it is thin, and the one place it complicates the commission: the flat
claim that "Adam's convergence proof was wrong" is true of the 2015 proof but is
not the end of the story. Later work (Zhang et al. 2022; Defossez et al. 2022)
proves Adam does converge under the large-beta2 regime practice actually uses,
and argues Reddi's counterexample depends on choosing the problem after fixing
the hyperparameters. The honest lesson is that the specific 2015 proof was
flawed and the method still has convergence guarantees under realistic settings,
not that Adam is a method that "does not converge." A writer must not overstate
the counterexample, exactly as the commission warns. The evidence does not
undermine the angle; it sharpens the correction it depends on.

## Sources

```text
URL:         https://arxiv.org/abs/1412.6980
Kind:        primary. The paper that owns Adam and every claim about it; Kingma
             & Ba are the authors. Read from the arXiv PDF (v9); the abstract
             page is the document's home and states the ICLR 2015 publication.
Establishes: What Adam is and what the 2015 paper demonstrated. Algorithm 1:
             maintain m_t = b1*m_{t-1} + (1-b1)*g_t (biased first moment) and
             v_t = b2*v_{t-1} + (1-b2)*g_t^2 (biased second raw moment), both
             initialized at 0; bias-correct m_hat_t = m_t/(1-b1^t) and
             v_hat_t = v_t/(1-b2^t); update theta_t = theta_{t-1} - alpha *
             m_hat_t/(sqrt(v_hat_t) + eps). The recommended defaults are alpha =
             0.001, b1 = 0.9, b2 = 0.999, eps = 1e-8. Theorem 4.1 gives an
             O(sqrt(T)) regret bound in the online convex framework; Corollary
             4.2 gives average regret R(T)/T = O(1/sqrt(T)). The experiments:
             (6.1) L2-regularized multiclass logistic regression on MNIST (784-d
             image vectors) and on IMDB movie reviews as 10,000-word
             bag-of-words vectors, minibatch 128, vs SGD-Nesterov, AdaGrad,
             RMSProp; (6.2) an MLP with two fully connected hidden layers of
             1000 ReLU units each on MNIST, minibatch 128, vs AdaGrad, RMSProp,
             SGD-Nesterov, AdaDelta, and SFO; (6.3) a CNN on CIFAR-10, three
             stages of 5x5 conv + 3x3 max pooling (c64-c64-c128-1000), minibatch
             128, 45 epochs; (6.4) a variational autoencoder (one 500-unit
             softplus hidden layer, 50-d Gaussian latent) testing bias
             correction. No language model and nothing near frontier scale.
Paraphrase:  Adam is a per-parameter adaptive step built from running averages
             of the gradient and its square, with bias correction, and the paper
             backs it with a convex regret bound and four small-scale
             experiments.
Locators:    Algorithm 1 and its caption (p. 2); defaults in the caption;
             update-rule discussion Section 2.1 (pp. 2-3); Theorem 4.1 and
             Corollary 4.2 Section 4 (p. 4); experiments Section 6 (pp. 5-7).
Quote:       "Good default settings for the tested machine learning problems are
             alpha = 0.001, beta1 = 0.9, beta2 = 0.999 and eps = 10^-8." Also,
             opening Section 6: "Using large models and datasets, we demonstrate
             Adam can efficiently solve practical deep learning problems." (The
             word "large" dates the paper: these are the models that were large
             in 2015.)
```

```text
URL:         https://arxiv.org/abs/1904.09237
Kind:        primary. Reddi, Kale & Kumar (Google, New York) own the
             counterexample and the AMSGrad algorithm. Published at ICLR 2018
             (best-paper award); the canonical venue page is
             https://openreview.net/forum?id=ryQu7f-RZ. Read from the arXiv PDF,
             which carries the "Published as a conference paper at ICLR 2018"
             header on every page.
Establishes: How the convergence claim was broken and what AMSGrad changes. The
             flaw is located in Gamma_{t+1} = sqrt(V_{t+1})/alpha_{t+1} -
             sqrt(V_t)/alpha_t, the change in the inverse learning rate over
             time. For SGD and AdaGrad Gamma_t is positive semidefinite (learning
             rates never rise); for Adam and RMSProp it can be negative, and "the
             proof in the original paper of ADAM erroneously assumes that Gamma_t
             is positive semi-definite and is hence, incorrect." Theorem 1 gives
             the concrete counterexample: on F = [-1, 1] with f_t(x) = C*x when
             t mod 3 = 1 and -x otherwise (C > 2), with b1 = 0 and
             b2 = 1/(1 + C^2), Adam converges to x = +1, the worst point in the
             domain, while the optimum is x = -1; its average regret does not go
             to 0. Theorem 2 extends this to any constant b1, b2 with
             b1 < sqrt(b2) (the same benign condition the 2015 proof assumes),
             and Theorem 6 (appendix) shows adding a constant eps does not save
             it. Theorem 3 gives a stochastic-convex version. AMSGrad (Algorithm
             2) changes one thing: v_hat_t = max(v_hat_{t-1}, v_t), and it
             normalizes by that running maximum instead of v_t, which forces
             Gamma_t >= 0 and a non-increasing step size. AMSGrad carries its own
             O(sqrt(T)) regret bound (Theorem 4).
Paraphrase:  Adam can converge to the single worst point of a simple convex
             problem; the 2015 proof failed because it assumed a quantity was
             always positive when Adam lets it go negative; AMSGrad fixes this by
             clamping the second-moment estimate to its historical maximum.
Locators:    Gamma_t definition and Theorems 1-2, Section 3 (p. 4); Theorem 3
             and AMSGrad Algorithm 2, top of Section 4 (p. 5); the "erroneously
             assumes" sentence, Section 4 (p. 5, pointing to Appendix D).
Quote:       "There is an online convex optimization problem where ADAM has
             non-zero average regret i.e., R_T/T does not converge to 0 as T ->
             infinity." (Theorem 1.) And: "The proof in the original paper of
             ADAM erroneously assumes that Gamma_t is positive semi-definite and
             is hence, incorrect."
```

```text
URL:         https://arxiv.org/abs/1711.05101
Kind:        primary. Loshchilov & Hutter own AdamW. Published as a conference
             paper at ICLR 2019. Read from the arXiv abstract page.
Establishes: Why plain Adam was displaced in transformer training. For SGD, L2
             regularization and weight decay are equivalent (up to a learning-
             rate rescaling); for adaptive methods like Adam they are not, and
             most implementations that call an L2 penalty "weight decay" are
             wrong to. AdamW decouples the weight-decay term from the gradient-
             based update, which the authors show decouples the best weight-decay
             value from the learning rate and "substantially improves Adam's
             generalization performance," letting Adam match SGD-with-momentum on
             image classification. This is the variant that became the default
             for transformers; it is worth one sentence in the lesson, not a
             section.
Paraphrase:  AdamW is Adam with weight decay applied separately from the
             adaptive gradient step, and that single change closed Adam's
             generalization gap and made it the standard transformer optimizer.
Locators:    Abstract; the equivalence-for-SGD-but-not-Adam claim and the
             decoupling proposal are both stated there.
Quote:       "L2 regularization and weight decay regularization are equivalent
             for standard stochastic gradient descent (when rescaled by the
             learning rate), but as we demonstrate this is not the case for
             adaptive gradient algorithms, such as Adam." And the fix
             "substantially improves Adam's generalization performance."
```

```text
URL:         https://proceedings.mlr.press/v139/schmidt21a.html
Kind:        primary for its own benchmark result. Schmidt, Schneider & Hennig
             ran the study and own its finding; it is external commentary on
             Adam, so it is secondary evidence about Adam specifically. ICML
             2021, PMLR volume 139, pp. 9367-9376. Read from the PMLR PDF.
Establishes: How the field actually settled, and that AMSGrad did not displace
             Adam. They benchmarked fifteen optimizers (their set includes
             AMSBound, AMSGrad, AdaBelief, AdaBound, AdaDelta, AdaGrad, Adam,
             Lookahead variants, Momentum, NAG, NAdam, RAdam, RMSProp, SGD) over
             more than 50,000 individual runs across eight tasks. No single
             optimizer won across tasks; Adam was among the consistently
             competitive choices, and AMSGrad was flagged as having badly-
             performing default settings.
Paraphrase:  In the largest standardized optimizer comparison, Adam remained a
             strong default and the newer methods, AMSGrad included, did not
             consistently beat it.
Locators:    Abstract and the results heatmap (their Figure with the eight
             task columns); the "badly-performing default settings ... for
             AMSGRAD and ADADELTA" observation is in the results discussion.
Quote:       "ADAM remains a strong contender, with newer methods failing to
             significantly and consistently outperform it."
```

```text
URL:         https://docs.pytorch.org/docs/stable/generated/torch.optim.Adam.html
Kind:        primary artifact. The reference implementation most practitioners
             use; the default flags are a direct record of how the field uses
             Adam. Read from the PyTorch stable docs.
Establishes: That AMSGrad is available but off by default, and that the 2015
             defaults survived intact. The constructor is
             torch.optim.Adam(params, lr=0.001, betas=(0.9, 0.999), eps=1e-08,
             weight_decay=0, amsgrad=False, ...). The amsgrad option is described
             as "whether to use the AMSGrad variant of this algorithm from the
             paper On the Convergence of Adam and Beyond," and its default is
             False.
Paraphrase:  PyTorch's Adam ships the exact 2015 defaults and treats AMSGrad as
             an opt-in flag that is off unless a user turns it on.
Locators:    Constructor signature and the amsgrad argument description at the
             top of the page.
Quote:       "amsgrad ... whether to use the AMSGrad variant of this algorithm
             from the paper On the Convergence of Adam and Beyond" -- default
             False.
```

```text
URL:         https://arxiv.org/abs/2208.09632
Kind:        primary. Zhang, Chen, Shi, Sun & Luo own this convergence result.
             arXiv 2208.09632 (Aug 2022; the abstract page does not print a
             venue, though the work was presented in the NeurIPS 2022 cycle --
             treat the venue as unverified from this read). Read from the
             abstract page.
Establishes: The strongest challenge to reading Reddi's counterexample as
             damning. They prove Adam converges to a neighborhood of critical
             points when b2 is large and b1 < sqrt(b2) < 1, covering practical
             defaults such as b1 = 0.9 with a sufficiently large b2, and show a
             phase transition from divergence to convergence as b2 rises. They
             argue Reddi's protocol picks the problem after fixing the
             hyperparameters, whereas practice fixes the problem first and then
             tunes (b1, b2). This is context the writer needs to avoid
             overstating the counterexample.
Paraphrase:  Adam does converge without modification once b2 is large enough,
             which is the regime practice uses; the divergence example lives in
             the small-b2, adversarially-chosen corner.
Locators:    Abstract.
Quote:       Their central condition, paraphrased from the abstract: when b2 is
             large and b1 < sqrt(b2) < 1, Adam converges to the neighborhood of
             critical points, with a phase transition from divergence to
             convergence as b2 increases.
```

```text
URL:         https://arxiv.org/abs/2003.02395
Kind:        primary. Defossez, Bottou, Bach & Usunier own this proof.
             Published in TMLR (Transactions on Machine Learning Research). Read
             from the abstract page.
Establishes: A second corrected convergence result, giving Adam and AdaGrad an
             explicit bound on the trajectory-averaged squared gradient norm for
             smooth non-convex objectives with bounded gradients under proper
             hyperparameters, with an O(d ln(N)/sqrt(N)) rate. The abstract also
             notes the nuance that with the exact default parameters Adam's bound
             does not close, which is part of why the practical picture is
             subtle rather than settled.
Paraphrase:  Under smoothness and bounded gradients and suitable
             hyperparameters, Adam has a clean non-convex convergence bound; the
             literal defaults are the awkward case.
Locators:    Abstract.
Quote:       The averaged squared gradient norm has "an upper-bound which is
             explicit in the constants"; and, on defaults, that with the default
             parameters the guarantee does not hold in the same clean form.
```

```text
URL:         https://api.semanticscholar.org/graph/v1/paper/arXiv:1412.6980?fields=title,year,citationCount,influentialCitationCount,venue
Kind:        secondary. Semantic Scholar is an aggregator reporting a citation
             count it did not itself generate; useful for the scale claim, not a
             source of primary fact. The API endpoint is recorded deliberately:
             it is the artifact that returns the figure, and the human-readable
             semanticscholar.org page renders via JavaScript and comes back
             blank to a non-browser client. Retrieved 2026-08-23; the endpoint
             is rate-limited, so a reader may need to retry.
Establishes: The size of Adam's footprint. Semantic Scholar reports 170,154
             citations and 26,922 "influential" citations for the Adam paper.
             This confirms the commission's "well over a hundred thousand"
             without pinning a false precision; Google Scholar would give a
             different, larger number, so cite this as one platform's count as
             of the retrieval date, not as an absolute.
Paraphrase:  One major index counts over 170,000 citations of the Adam paper.
Locators:    Semantic Scholar record for the paper (API fields citationCount,
             influentialCitationCount).
Quote:       (none; a numeric field, recorded under Numbers.)
```

## Contradictions

- **Whether the counterexample is damning is disputed by later theory, not by
  the commission's own framing.** Reddi et al. (2018) prove the 2015 proof is
  wrong and Adam can diverge to the worst point of a convex problem. Zhang et al.
  (2022, arXiv 2208.09632) and Defossez et al. (TMLR, arXiv 2003.02395) then
  prove Adam does converge under realistic conditions (large b2, or smooth
  non-convex with bounded gradients and suitable hyperparameters). These do not
  contradict Reddi -- the divergence example still stands for its chosen
  parameters -- but they contradict any reading that "Adam has no convergence
  guarantee." Zhang et al. attack the protocol directly: Reddi picks the problem
  after the hyperparameters, practice does the reverse. The writer must state
  the flaw in the 2015 proof as fact and the "Adam still converges in practice"
  claim as later-proven, keeping the two separate.

- **Reddi's own empirical claim for AMSGrad conflicts with how the field
  settled.** Reddi et al. report AMSGrad "performs better than ADAM" on their
  experiments -- but those experiments are MNIST logistic regression, a
  one-hidden-layer 100-unit MNIST MLP, and a small CIFAR-10 CNN (CIFARNET), the
  same small scale as the 2015 Adam paper. The larger, later benchmark (Schmidt
  et al., ICML 2021) finds AMSGrad among the methods that do not consistently
  beat Adam, and PyTorch keeps it off by default. So "AMSGrad rarely helps in
  practice" is supported, and the reason the field could ignore a correct
  theoretical fix is that the fix rarely changed the outcome on real workloads.

- **The paper called its own models "large."** The 2015 paper opens Section 6
  with "Using large models and datasets." Read in 2026 this is the opposite of
  the reader's expectation, and the writer should use the paper's own word to
  make the scale gap concrete rather than editorializing about it.

No source disputes the update rule, the default hyperparameters, the content of
Theorem 4.1, or the mechanics of the counterexample and AMSGrad; those are
firsthand and uncontested.

## Numbers

```text
Figure: alpha = 0.001, beta1 = 0.9, beta2 = 0.999, eps = 1e-8 (Adam defaults)
Owner:  Kingma & Ba (2015), Algorithm 1 caption
Scope:  Recommended defaults "for the tested machine learning problems"
```

```text
Figure: 170,154 citations (26,922 "influential")
Owner:  Semantic Scholar aggregate for arXiv:1412.6980, retrieved 2026-08-23
Scope:  One index's lifetime count; other indexes report different totals
```

```text
Figure: MLP = 2 hidden layers x 1000 ReLU units; minibatch 128
Owner:  Kingma & Ba (2015), Section 6.2 (MNIST)
Scope:  The paper's largest fully connected experiment
```

```text
Figure: CNN = c64-c64-c128-1000, 5x5 conv, 3x3 max-pool stride 2, 45 epochs
Owner:  Kingma & Ba (2015), Section 6.3 (CIFAR-10), minibatch 128
Scope:  The paper's only convolutional experiment
```

```text
Figure: IMDB bag-of-words feature vector = 10,000 most frequent words
Owner:  Kingma & Ba (2015), Section 6.1
Scope:  The sparse-gradient logistic-regression experiment
```

```text
Figure: Counterexample constants: F = [-1,1]; f_t(x)=C*x if t mod 3=1 else -x,
        C>2; beta1=0, beta2=1/(1+C^2); Adam iterate -> +1, optimum -> -1
Owner:  Reddi, Kale & Kumar (2018), Theorem 1 / Section 3
Scope:  One-dimensional online convex problem; the minimal divergence example
```

```text
Figure: AMSGrad change: v_hat_t = max(v_hat_{t-1}, v_t); regret O(sqrt(T))
Owner:  Reddi, Kale & Kumar (2018), Algorithm 2 and Theorem 4
Scope:  The single modification and its guarantee
```

```text
Figure: CIFAR-10 = 60,000 labeled 32x32 images
Owner:  Reddi et al. (2018) restatement; standard dataset size
Scope:  Anchors "CIFAR-10" for a reader who cannot scale it
```

```text
Figure: 15 optimizers, >50,000 runs, 8 tasks; no single winner
Owner:  Schmidt, Schneider & Hennig (2021), ICML / PMLR 139
Scope:  Standardized cross-task benchmark
```

```text
Figure: PyTorch Adam defaults lr=1e-3, betas=(0.9,0.999), eps=1e-8, amsgrad=False
Owner:  PyTorch torch.optim.Adam documentation
Scope:  The reference implementation's constructor defaults
```

## Source assets

```text
Asset: Algorithm 1 pseudocode box, Kingma & Ba (2015), p. 2
Shows: The full Adam update in eight lines, including the two moment updates,
       the two bias corrections, and the final step. The defaults sit in the
       caption directly beneath it.
Crop:  Keep the four update lines and the two bias-correction lines; keep the
       caption line with the defaults. Omit the "Require" preamble if space is
       tight, but not the epsilon in the final line.
```

```text
Asset: Figures 1-3 training-cost curves, Kingma & Ba (2015), pp. 5-6
Shows: Adam converging as fast as or faster than AdaGrad, RMSProp, and SGD-
       Nesterov on the small tasks. Figure 3 (CIFAR-10 CNN) is the one where
       Adam's margin over SGD is only marginal, which the paper itself concedes.
Crop:  A single curve panel (e.g. MNIST logistic regression, Figure 1 left) is
       enough to show the empirical claim; do not stack all six. Keep axis
       labels (training cost vs iterations over dataset).
```

```text
Asset: Figure 1 synthetic-divergence plots, Reddi et al. (2018), p. 5
Shows: Adam's average regret failing to reach 0 and its iterate x_t walking to
       +1 while AMSGrad's reaches the optimum at -1. This is the counterexample
       made visible and is the strongest single image for the lesson's turn.
Crop:  Keep the iterate-value panel (x_t vs iterations) with both Adam and
       AMSGrad traces and the y-axis showing -1 and +1; that panel carries the
       argument alone.
```

```text
Asset: Algorithm 2 AMSGrad pseudocode, Reddi et al. (2018), p. 5
Shows: That the fix is one line: v_hat_t = max(v_hat_{t-1}, v_t). Placing it
       beside Adam's Algorithm 1 makes the size of the correction concrete.
Crop:  Keep the two lines that differ from Adam (the max line and the update
       that divides by sqrt(v_hat_t)); the rest matches Algorithm 1.
```

```text
Asset: None found for the "field kept using Adam" point beyond prose.
Shows: The Schmidt et al. results heatmap exists but is dense and task-by-task;
       it does not crop to a single legible claim for this reader. Better told
       in a sentence with the PyTorch default as the concrete artifact.
Crop:  n/a
```

## Discarded

```text
URL: https://openreview.net/forum?id=ryQu7f-RZ -- the ICLR 2018 venue page for
     the Reddi paper is behind a browser-verification wall to WebFetch. Recorded
     as the canonical venue inside the Reddi entry; the readable primary is the
     arXiv page, which carries the identical "Published as a conference paper at
     ICLR 2018" text. Not a separate source.
```

```text
URL: Duchi, Hazan & Singer (AdaGrad, JMLR 2011) and Tieleman & Hinton (RMSProp,
     Coursera 2012) -- not independently opened. Their update rules are read
     secondhand inside the Adam paper (Section 5) and the Reddi paper (Section
     2), which is enough for the one-sentence "what Adam changed" the commission
     allows. If the writer needs to state either update rule as fact, cite it to
     the primary that describes it here, or open the original first. Do not list
     them as sources read.
```
