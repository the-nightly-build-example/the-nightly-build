# Evidence: the-evidence/adversarial-examples (01)

The record supports the commission on every load-bearing number. The panda figure,
the Fast Gradient Sign Method equation, the MNIST results, and the linear-explanation
claim are all verified word-for-word against the 2015 paper (arXiv:1412.6572). The
predecessor primary (Szegedy et al. 2013) confirms exactly what the 2015 paper added:
Szegedy's group discovered adversarial examples and their transfer across models but
offered only "blind spots"; Goodfellow's paper added an explanation, a cheap attack,
and adversarial training. Three later primaries (Madry 2018, Athalye 2018, Ilyas 2019)
plus a 2024 state-of-the-art result (Bartoldson) and one secondary survey establish
that the problem endured.

Where the record is thin, or where it pushes back on the commission: the "still
unsolved" framing is true but must be stated precisely, because the evidence also shows
real, measured progress. Robust training (Madry's PGD) works to a meaningful degree,
and the best CIFAR-10 robust accuracy climbed from ~46% in 2018 to ~74% in 2024. So the
honest claim is "no cheap, general defense and a large remaining gap," not "nothing
works." Two further corrections to the paper itself: the paper's own proposed defense,
single-step FGSM adversarial training, was later shown to confer little real robustness
(gradient masking), and its central linear explanation is contested from at least two
directions (Tanay & Griffin's boundary-tilting geometry; Ilyas et al.'s non-robust
features). The commission already anticipates the contested explanation, so the evidence
confirms the angle rather than breaking it.

## Sources

```text
URL:         https://arxiv.org/abs/1412.6572
Kind:        primary — this is the paper under examination; Goodfellow, Shlens, and
             Szegedy own every claim and number in it. ICLR 2015; v1 submitted
             2014-12-20, v3 (final) 2015-03-20.
Establishes: What the paper claims and did firsthand. The linear explanation, the
             FGSM attack, the panda/GoogLeNet demonstration, the MNIST results, and
             adversarial training.
Paraphrase:  The paper argues the primary cause of neural networks' vulnerability to
             adversarial perturbation is that the networks are too linear, not too
             nonlinear. Linear behavior in high-dimensional input spaces is enough to
             produce adversarial examples: many tiny per-pixel changes, each aligned
             with the sign of the model's gradient, sum to one large change in the
             pre-activation. This view predicts why one model's adversarial example
             fools other models trained differently. It also yields a one-step attack,
             the Fast Gradient Sign Method, and a defense, training on FGSM examples.
Locators:    Abstract; Sec. 3 (linear explanation); Sec. 4 (FGSM); Sec. 5 (MNIST /
             adversarial training); Fig. 1 (panda).
Quote:       "We argue instead that the primary cause of neural networks' vulnerability
             to adversarial perturbation is their linear nature." (Abstract)
             "Linear behavior in high-dimensional spaces is sufficient to cause
             adversarial examples." (Sec. 3)
```

```text
URL:         https://arxiv.org/abs/1312.6199
Kind:        primary — Szegedy, Zaremba, Sutskever, Bruna, Erhan, Goodfellow, Fergus
             own the discovery of adversarial examples. ICLR 2014; submitted
             2013-12-21. (This is the predecessor the commission requires.)
Establishes: What existed before the 2015 paper: the phenomenon itself and its
             transfer across models, found by optimization, with no working
             explanation.
Paraphrase:  This paper first exhibited adversarial examples. It found them by
             box-constrained L-BFGS optimization, searching for the smallest additive
             perturbation that flips a network's label. The perturbations are barely
             perceptible. Crucially, an adversarial example built against one network
             is often still misclassified by a different network trained with different
             hyperparameters or on a different training subset — transfer. The authors
             offered no mechanism, describing adversarial examples as low-probability
             "pockets" or "blind spots" in the input space. Datasets and models: MNIST
             (fully connected nets and an autoencoder), ImageNet (AlexNet), and a
             ~1-billion-parameter net trained on YouTube frames (QuocNet).
Locators:    Sec. 4 (framework / L-BFGS); Sec. 4.3 (cross-model generalization);
             Fig. 5 (magnified perturbations).
Quote:       "if we use one neural net to generate a set of adversarial examples, we
             find that these examples are still statistically hard for another neural
             network even when it was trained with different hyperparameters."
```

```text
URL:         https://arxiv.org/abs/1706.06083
Kind:        primary — Madry, Makelov, Schmidt, Tsipras, Vladu (MIT) own the PGD
             attack and the robust-optimization result. ICLR 2018; submitted 2017-06-19.
Establishes: That the problem endured, that single-step FGSM training is not a real
             defense, and that a stronger multi-step attack (PGD) plus robust training
             is the durable partial answer.
Paraphrase:  The paper casts robustness as a min-max (saddle-point) problem: minimize
             the worst-case loss over perturbations inside a bounded set. Its attack,
             projected gradient descent, is FGSM run for many small steps with
             projection back into the epsilon-ball — the authors call it the multi-step
             variant of FGSM. Training against PGD adversaries yields models that
             retain meaningful accuracy under strong attack. Single-step FGSM training,
             by contrast, overfits to the one-step attack and gives little robustness
             against PGD.
Locators:    Sec. 2 (saddle-point formulation); Sec. 3 (PGD as multi-step FGSM);
             Sec. 4 (MNIST/CIFAR-10 results and the FGSM-training failure).
Quote:       "A more powerful adversary is the multi-step variant, which is essentially
             projected gradient descent (PGD) on the negative loss function."
             On single-step training: FGSM-trained networks "have poor performance on
             natural examples and don't exhibit any kind of robustness against PGD
             adversaries."
```

```text
URL:         https://arxiv.org/abs/1802.00420
Kind:        primary — Athalye, Carlini, Wagner own the result that a class of 2018
             defenses was illusory. ICML 2018; submitted 2018-02-01.
Establishes: That the defenses published after the paper were mostly broken, and why —
             they hid gradients rather than removing the vulnerability.
Paraphrase:  The authors identify "obfuscated gradients," a form of gradient masking
             that makes standard attacks fail while leaving the model just as
             vulnerable to attacks built to route around the masking. Of nine defenses
             accepted at ICLR 2018, seven relied on obfuscated gradients. New attacks
             broke six of those completely and one partially, in each paper's own
             threat model.
Locators:    Abstract; Sec. 1 (headline result); per-defense sections.
Quote:       "We identify obfuscated gradients, a kind of gradient masking, as a
             phenomenon that leads to a false sense of security in defenses against
             adversarial examples." "Of the 9 defenses accepted at ICLR 2018 [that we
             study], 7 rely on obfuscated gradients ... our new attacks successfully
             circumvent 6 completely, and 1 partially."
```

```text
URL:         https://arxiv.org/abs/1905.02175
Kind:        primary — Ilyas, Santurkar, Tsipras, Engstrom, Tran, Madry own the
             non-robust-features account. NeurIPS 2019; submitted 2019-05-06.
Establishes: A firsthand later diagnosis that competes with the 2015 paper's "linear
             flaw" reading: adversarial examples come from real, predictive features,
             not from a model defect.
Paraphrase:  The paper argues adversarial vulnerability is a consequence of models
             latching onto "non-robust features" — patterns in the data that genuinely
             predict the label and generalize, but that a human cannot perceive and
             that flip under a small perturbation. In the key experiment, the authors
             relabel a training set so that its imperceptible non-robust features point
             to the wrong class, train on it, and the resulting model still generalizes
             to the ordinary, clean test set. That only works if those imperceptible
             features carry real signal. This reframes the phenomenon as a property of
             the data, not a design mistake — a different account from the paper's
             linearity story.
Locators:    Abstract; Sec. 3 (disentangling robust/non-robust features); the
             non-robust-features generalization experiment.
Quote:       "adversarial vulnerability is a direct result of our models' sensitivity to
             well-generalizing features in the data." Training on the relabeled set
             "results in a well-generalizing classifier" on the standard test set
             (~43.7% CIFAR-10 test accuracy from features alone).
```

```text
URL:         https://arxiv.org/abs/1608.07690
Kind:        primary — Tanay and Griffin (UCL) own this critique. arXiv 2016, not
             formally published; submitted 2016-08-27.
Establishes: A direct, firsthand challenge to the paper's central explanation.
Paraphrase:  The authors argue the linear explanation is neither necessary nor
             sufficient. They build a toy image class on which a linear classifier is
             perfect and has no adversarial examples at all, so linearity does not by
             itself force the phenomenon. They also argue the dimensionality intuition
             does not hold as stated: enlarging MNIST images does not worsen adversarial
             vulnerability in proportion to the added dimensions. Their alternative,
             "boundary tilting," is geometric: adversarial examples appear when the
             decision boundary is tilted to lie close to the data along low-variance
             directions, which can happen without hurting clean accuracy and which
             produces the imperceptible, high-frequency perturbations seen in deep nets.
Locators:    Secs. 3-4 (critique of the linear explanation); Sec. 5 (boundary tilting).
Quote:       "we can find classes of images for which adversarial examples do not exist
             at all." "adversarial examples exist when the classification boundary lies
             close to the submanifold of sampled data."
```

```text
URL:         https://arxiv.org/abs/1707.08945
Kind:        primary — Eykholt, Evtimov, Fernandes, Li, Rahmati, Xiao, Prakash, Kohno,
             Song own the physical-attack result. CVPR 2018; submitted 2017-07-27.
             (Published page https://openaccess.thecvf.com/content_cvpr_2018/html/
             Eykholt_Robust_Physical-World_Attacks_CVPR_2018_paper.html returned 403 to
             an automated fetch; the arXiv page above is the source's own page and
             resolves.)
Establishes: That real-world adversarial attacks exist, and that they are a different
             threat model from the paper's imperceptible pixel perturbation.
Paraphrase:  The attack is physical: black-and-white stickers, designed to look like
             graffiti, placed on a real stop sign. This is not an imperceptible digital
             perturbation. A road-sign classifier read the stickered stop sign as a
             speed-limit sign in 100% of stationary lab images and in 84.8% of video
             frames captured from a moving vehicle. The visible, human-noticeable nature
             of the perturbation is the point of contrast: the 2015 paper's threat model
             is a change too small to see, and that is a specific setting, not the only
             way attacks reach the physical world.
Locators:    Abstract; Sec. 5 (drive-by and stationary evaluations).
Quote:       "100% of the images obtained in lab settings, and in 84.8% of the captured
             video frames obtained on a moving vehicle (field test)" — stop sign read
             as "Speed Limit 45."
```

```text
URL:         https://arxiv.org/abs/2404.09349
Kind:        primary — Bartoldson, Diffenderfer, Parasyris, Kailkhura own this
             state-of-the-art robustness result. ICML 2024; submitted 2024-04-14.
Establishes: The current size of the gap, ten years on. This is the "still unsolved,
             but not stagnant" anchor.
Paraphrase:  The paper reports the strongest CIFAR-10 robustness on the standard
             threat model (AutoAttack, L-infinity, epsilon = 8/255): about 74% robust
             accuracy, a new best, against clean accuracy near 94%. The authors state
             plainly how far short of solved this is, and they use scaling laws to argue
             the ceiling is real: robustness grows slowly and plateaus, so brute-force
             scale will not close the gap, and perfect robustness is not attainable.
             The progression matters: Madry's 2018 CIFAR-10 model held ~46% under
             20-step PGD; the 2024 best holds ~74% under the stronger AutoAttack. Real
             gain, still a large gap.
Locators:    Abstract; scaling-law section; results tables.
Quote:       "Taking CIFAR10 as an example, SOTA clean accuracy is about 100%, but SOTA
             robustness to l-infinity-norm bounded perturbations barely exceeds 70%."
             "our scaling laws also predict robustness slowly grows then plateaus at
             90%: ... perfect robustness is impossible."
```

```text
URL:         https://arxiv.org/abs/1801.00553
Kind:        secondary — Akhtar and Mian (Univ. of Western Australia) survey and report
             on others' work; they do not own the primary claims. Published in IEEE
             Access, 2018; submitted 2018-01-02.
Establishes: That, from outside any authoring party, the field itself recorded no
             consensus on why adversarial examples exist — direct support for calling
             the linear explanation contested rather than settled.
Paraphrase:  The survey catalogs attacks, explanations, and defenses. It presents the
             linear/"linearity" reading of Goodfellow et al. as one hypothesis among
             several that "do not perfectly align with each other," alongside flatness
             of decision boundaries, large local curvature, and low network flexibility.
             It states outright that the literature lacks consensus on the cause.
Locators:    Sec. III-A2 (FGSM and linearity); Sec. V (existence of adversarial
             examples).
Quote:       "current literature seems to lack consensus on the reasons for the
             existence of the adversarial examples." "Flatness of decision boundaries,
             large local curvature of the decision boundaries and low flexibility of
             the networks are some more examples of the viewpoints ... that do not
             perfectly align with each other."
```

## Contradictions

- **"Still unsolved" is true but risks reading as "no progress."** Athalye 2018 broke
  the cheap defenses, and Bartoldson 2024 confirms a large remaining gap and argues a
  hard ceiling. But Madry's PGD training is a real, durable partial defense, and the
  best CIFAR-10 robust accuracy rose from ~46% (Madry, 2018) to ~74% (Bartoldson, 2024)
  under a stronger attack. Certified defenses (randomized smoothing) also exist. The
  writer should say "no cheap, general defense and a wide gap," not "nothing works."
  This qualifies the commission's framing; it does not break it.

- **The paper's own defense was later downgraded.** The 2015 paper proposes FGSM
  adversarial training as a fix. Madry 2018 found single-step FGSM training gives little
  real robustness against a multi-step (PGD) attacker — a case of gradient masking. So
  the "harnessing" half of the paper held up only in weakened form: adversarial training
  is the right idea, but it needs a strong multi-step attack in the loop, not FGSM.

- **The linear explanation is contested, from two directions.** Tanay & Griffin 2016
  argue linearity is neither necessary nor sufficient and propose boundary tilting
  instead. Ilyas et al. 2019 recast the phenomenon as non-robust but genuinely
  predictive features in the data — a diagnosis unlike "the model is too linear." The
  Akhtar & Mian survey confirms no field consensus. None of this contradicts that FGSM
  works or that the paper's linear intuition usefully predicted transfer; it contradicts
  the stronger reading that linearity is the settled, complete cause.

- **Provenance note, not a disagreement.** The predecessor's author list includes Ian
  Goodfellow and Christian Szegedy, two of the three authors of the 2015 paper. The
  "what this paper added over the last one" story is the same people advancing their own
  prior work, not one group correcting another. Worth stating plainly so the article
  does not frame it as a rivalry.

## Numbers

```text
Figure: epsilon = 0.007 (panda perturbation), the magnitude of the smallest bit of an
        8-bit pixel encoding
Owner:  Goodfellow, Shlens, Szegedy 2015 (arXiv:1412.6572), Fig. 1
Scope:  GoogLeNet on ImageNet; single demonstration image

Figure: panda 57.7% -> nematode 8.2% -> gibbon 99.3% (class and confidence before and
        after the perturbation; nematode is the network's read of the perturbation
        image alone)
Owner:  Goodfellow, Shlens, Szegedy 2015, Fig. 1
Scope:  GoogLeNet on ImageNet; single image

Figure: FGSM perturbation:  eta = epsilon * sign( grad_x J(theta, x, y) )
Owner:  Goodfellow, Shlens, Szegedy 2015, Sec. 4
Scope:  Definition; theta = model params, x = input, y = label, J = cost

Figure: MNIST maxout network, error on FGSM examples (epsilon = 0.25): 89.4%, average
        confidence 97.6%
Owner:  Goodfellow, Shlens, Szegedy 2015, Sec. 5
Scope:  MNIST test set; pixel values in [0,1]

Figure: MNIST maxout clean test error 0.94% -> 0.84% with adversarial training; error on
        adversarial examples 89.4% -> 17.9% with adversarial training
Owner:  Goodfellow, Shlens, Szegedy 2015, Sec. 5
Scope:  MNIST test set

Figure: shallow softmax regression, error on FGSM examples (epsilon = 0.25): 99.9%,
        average confidence 79.3%
Owner:  Goodfellow, Shlens, Szegedy 2015, Sec. 5
Scope:  MNIST test set

Figure: Madry robust accuracy — MNIST ~89%+ under strongest test-suite attack
        (epsilon = 0.3); CIFAR-10 ~46% under 20-step PGD (epsilon = 8/255)
Owner:  Madry et al. 2018 (arXiv:1706.06083), Sec. 4
Scope:  MNIST and CIFAR-10 test sets; adversarially trained models

Figure: 7 of 9 ICLR-2018 defenses relied on obfuscated gradients; 6 broken fully, 1
        partially
Owner:  Athalye, Carlini, Wagner 2018 (arXiv:1802.00420)
Scope:  The nine defenses accepted at ICLR 2018 that they studied

Figure: ~43.7% CIFAR-10 standard-test accuracy from a model trained only on non-robust
        features (relabeled dataset)
Owner:  Ilyas et al. 2019 (arXiv:1905.02175)
Scope:  CIFAR-10; the D_det construction

Figure: CIFAR-10 SOTA robust accuracy ~74% (AutoAttack, L-inf, epsilon = 8/255) at
        ~94% clean; "barely exceeds 70%"; scaling-law plateau ~90%
Owner:  Bartoldson et al. 2024 (arXiv:2404.09349)
Scope:  CIFAR-10; best WideResNet-94-16 and the paper's scaling analysis

Figure: physical stop-sign attack: 100% misclassification in lab images, 84.8% of
        drive-by video frames; stop -> Speed Limit 45
Owner:  Eykholt et al. 2018 (arXiv:1707.08945)
Scope:  Road-sign classifier (LISA-CNN); physical sticker perturbation
```

## Source assets

```text
Asset: Figure 1, the panda + perturbation + gibbon triptych, in Goodfellow, Shlens,
       Szegedy 2015 (arXiv:1412.6572).
Shows: The whole argument in one image — an almost invisible perturbation, added at
       epsilon = 0.007, turns a 57.7%-confidence panda into a 99.3%-confidence gibbon.
       The three panels with their labels and confidences carry more than any prose
       restatement.
Crop:  Must retain all three panels and their captions (the "+", the ".007 x sign(...)"
       middle panel, and the class/confidence labels). Cropping to two panels loses the
       point that the middle image is itself the additive perturbation.
```

```text
Asset: The FGSM equation, eta = epsilon * sign(grad_x J(theta, x, y)), Sec. 4 of the
       2015 paper.
Shows: How cheap the attack is — one gradient sign, one step. This is the "harnessing"
       the title promises, and it fits on one line.
Crop:  Reproduce as text/typeset, not as a photographed equation.
```

```text
Asset: Eykholt et al. 2018 stop-sign photographs (the stickered real sign as
       photographed in the field), arXiv:1707.08945.
Shows: That an adversarial attack can be a physical, visible object in the world, not
       only a digital pixel edit — the concrete contrast with the panda's invisible
       change.
Crop:  Keep the full sign so the stickers read as graffiti-like patches on a real
       octagonal stop sign.
```

## Discarded

```text
https://robustbench.github.io/ : the live leaderboard is JavaScript-rendered and
  returned only placeholder text to an automated fetch. The current-SOTA figure it
  hosts is owned and stated directly by Bartoldson et al. 2024 (arXiv:2404.09349),
  which is cited above, so the leaderboard adds no verifiable number of its own here.
https://dl.acm.org/doi/10.1145/3594869 ("Interpreting Adversarial Examples in Deep
  Learning: A Review", ACM Computing Surveys 2023): returned HTTP 403; could not read
  the passage firsthand, so not cited. The Akhtar & Mian survey (arXiv, open) covers the
  same "no consensus on the cause" point and is readable, so it stands in as the
  secondary.
https://www.kdnuggets.com/2018/10/adversarial-examples-explained.html : a popular
  explainer; superseded by the primaries it summarizes. Not needed.
```
