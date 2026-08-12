# Evidence record: the-evidence/grokking (researcher/01)

The evidence firmly supports the commission's angle. The original grokking paper
(Power, Burda, Edwards, Babuschkin, Misra, 2022) is a deliberately minimal
setup: a 2-layer, ~400k-parameter transformer on binary-operation tables over 97
elements, with the headline curve run on division mod 97 at 50% training data.
Its own figures show training accuracy near-perfect below 10^3 steps and
validation accuracy reaching that level only near 10^6 steps. That much is
established firsthand and is not in dispute. The two later claims the lesson
leans on are also established firsthand: Nanda et al. (2023) reverse-engineered
the modular-addition circuit as a discrete-Fourier / rotation algorithm and
defined progress measures showing the generalizing circuit forms gradually
beneath a flat test-loss curve, and both the original paper and the follow-ups
identify weight decay as the intervention that drives the memorize-to-generalize
transition. Where the record is thin, or actively complicates the angle: a 2025
paper (Li, Fan, Zhou) reports "grokking" in one-pass pretraining of a 7B-parameter
LLM, which cuts against the flat claim that grokking is confined to toy scale.
Read closely, that paper reframes the effect as local, asynchronous, delayed
generalization detected through internal proxy metrics rather than a single
sudden test-accuracy jump, so it undercuts the popular "sudden unlock" usage even
as it extends the phenomenon's reach. I record it in full below so the editor can
test the angle against it. I could not extract a digitized accuracy-versus-steps
table from any paper; the full series lives inside the plots and would have to be
read off the figures, so the Numbers section carries the landmark points the
papers state in text, not a per-step series.

One commission-input correction: the commission names the second author "Yuri
Burns." The arXiv record and paper list "Yuri Burda." The full author line is
below.

## Sources

```text
URL:         https://arxiv.org/abs/2201.02177
Kind:        primary. The paper's own authors reporting their own experiment.
Establishes: What grokking is and the exact setup that produced it: the tasks,
             model, data fractions, optimizer, weight-decay setting, and the
             steps-to-generalization landmarks. Also the authors' own scope
             framing ("small algorithmically generated datasets").
Paraphrase:  The authors study generalization on small, algorithmically generated
             binary-operation datasets. On some operations the network "groks":
             validation performance climbs from chance to near-perfect well after
             the training set is already fit. They also study generalization as a
             function of dataset size and report that smaller training fractions
             require increasing amounts of optimization to generalize.
Locators:    Title, abstract, and experimental-details / hyperparameter section
             (read via the arXiv full text at ar5iv.labs.arxiv.org/abs/2201.02177).
             Figure 1 caption quoted below.
Quote:       Figure 1 (left) caption, verbatim: "Grokking: A dramatic example of
             generalization far after overfitting on an algorithmic dataset. We
             train on the binary operation of division mod 97 with 50% of the
             data in the training set. ... The red curves show training accuracy
             and the green ones show validation accuracy. Training accuracy
             becomes close to perfect at <10^3 optimization steps, but it takes
             close to 10^6 steps for validation accuracy to reach that level, and
             we see very little evidence of any generalization until 10^5 steps."
Detail:      Authors: Alethea Power, Yuri Burda, Harri Edwards, Igor Babuschkin,
             Vedant Misra (OpenAI). Submitted 6 Jan 2022 (arXiv v1). Presented at
             the ICLR 2022 workshop on mathematical reasoning (per commission;
             the arXiv abstract page itself does not print the venue).
             Tasks: binary operations a∘b=c with each element a distinct symbol.
             Modular arithmetic (addition, subtraction, multiplication, division
             mod p, with p=97); symmetric-group S5 compositions (x·y, x·y·x^-1,
             x·y·x); polynomials mod 97 (e.g. x^2+y^2, x^2+xy+y^2, x^3+xy); mixed
             conditional operations. Some operations (e.g. x^3+xy^2+y mod 97) did
             not generalize within the optimization budget at any fraction up to
             95%.
             Model: decoder-only transformer, 2 layers, width 128, 4 attention
             heads, ~4x10^5 non-embedding parameters; loss on the answer token.
             Optimizer: AdamW, learning rate 10^-3, weight decay 1, beta1=0.9,
             beta2=0.98, 10-update linear warmup, minibatch 512 (or half the
             training set), budget 10^5 updates (up to 10^6 for the headline run).
             Data efficiency: near 25-30% training data, a 1% decrease in training
             data raises median time-to-generalization by 40-50%.
             Weight decay: among interventions compared (full-batch GD, SGD,
             learning-rate changes, residual dropout, weight decay, gradient
             noise), weight decay improved data efficiency the most, "more than
             halving the amount of samples needed compared to most other
             interventions."
```

```text
URL:         https://arxiv.org/abs/2301.05217
Kind:        primary. Nanda and co-authors reporting their own interpretability
             analysis of grokking.
Establishes: The mechanistic account of the modular-addition case and the
             progress measures showing the generalizing circuit forms gradually
             beneath a flat test curve; weight decay's role in the final cleanup.
Paraphrase:  Training a one-layer transformer on a+b mod 113, the authors fully
             reverse-engineer the learned algorithm: the network maps inputs onto
             a circle via a small set of Fourier frequencies and adds by
             composing rotations with trig identities, reading out the answer by
             constructive interference. They define two progress measures
             (restricted loss, excluded loss) computed from the model's Fourier
             components, and use them to split training into three phases:
             memorization, circuit formation, and cleanup. The generalizing
             circuit is present and strengthening well before test loss moves.
Locators:    Abstract; algorithm/reverse-engineering section; progress-measures
             and three-phases section (read via ar5iv.labs.arxiv.org/abs/2301.05217).
Quote:       "grokking, rather than being a sudden shift, arises from the gradual
             amplification of structured mechanisms encoded in the weights,
             followed by the later removal of memorizing components."
Detail:      Authors: Neel Nanda, Lawrence Chan, Tom Lieberum, Jess Smith, Jacob
             Steinhardt. arXiv v1 12 Jan 2023, revised through Oct 2023; ICLR
             2023. Task a+b mod 113 (p=113 prime), 30% of pairs as training data;
             one-layer transformer, d=128, 4 heads, MLP width 512, no LayerNorm,
             untied embeddings; AdamW, lr 10^-3, weight decay 1. Five key
             frequencies k in {14, 35, 41, 42, 52}. Restricted loss ablates all
             but the key frequencies (tracks how well the generalizing algorithm
             is learned); excluded loss removes the key frequencies (tracks
             reliance on the circuit versus memorization). Phase boundaries read
             from their figures, approximate: memorization ~0-1.4k epochs, circuit
             formation ~1.4k-9.4k, cleanup ~9.4k-14k, with the visible test-loss
             drop in cleanup. Their text states weight decay drives the cleanup
             ("weight decay encourages the network to shed the memorized solution
             in favor of ... the Fourier multiplication circuit") and describes
             weight decay as necessary for grokking in their setup.
```

```text
URL:         https://arxiv.org/abs/2205.10343
Kind:        primary. Liu and co-authors reporting their own effective-theory
             analysis.
Establishes: A representation-learning account of grokking and a phase structure;
             situates delayed generalization as a "Goldilocks zone" effect. Named
             in the commission as a candidate weight-decay source; in fact its
             contribution is the representation/phase account, not weight decay
             directly (see Omnigrok below for the weight-norm/weight-decay
             mechanism from the same group).
Paraphrase:  Modeling grokking as representation learning, the authors identify
             four phases (comprehension, grokking, memorization, confusion) and
             argue good representations form only within a bounded "Goldilocks
             zone." On transformers the grokking regime sits nearer memorization
             than comprehension, which is why generalization is delayed. They use
             physics-style effective theories and phase diagrams.
Locators:    Abstract and phase-diagram sections.
Quote:       (none load-bearing beyond the abstract's phase list.)
Detail:      Authors: Ziming Liu, Ouail Kitouni, Niklas Nolte, Eric J. Michaud,
             Max Tegmark, Mike Williams. arXiv v1 20 May 2022; NeurIPS 2022.
```

```text
URL:         https://arxiv.org/abs/2210.01117
Kind:        primary. Liu, Michaud, Tegmark reporting their own analysis.
Establishes: The weight-norm / weight-decay mechanism, and the two-directional
             control result: grokking can be induced beyond algorithmic data and
             eliminated on algorithmic data. Directly relevant to both the cause
             claim (weight decay/regularization) and the counter-angle (is
             grokking only a toy artifact?).
Paraphrase:  The authors trace grokking to a mismatch between the training-loss
             and test-loss curves plotted against model weight norm (the "LU
             mechanism": train loss looks like an L, test loss like a U). This
             mechanism accounts for data-size dependence, weight-decay dependence,
             and the emergence of representations. Guided by it, they induce
             grokking on image, language, and molecule tasks, and eliminate it on
             algorithmic tasks, attributing the dramatic algorithmic case to
             representation learning. The lever throughout is the weight norm,
             which weight decay controls.
Locators:    Abstract; LU-mechanism section.
Quote:       "This simple mechanism can nicely explain many aspects of grokking:
             data size dependence, weight decay dependence, the emergence of
             representations, etc. ... we are able to induce grokking on tasks
             involving images, language and molecules. In the reverse direction,
             we are able to eliminate grokking for algorithmic datasets."
Detail:      Authors: Ziming Liu, Eric J. Michaud, Max Tegmark. arXiv v1 3 Oct
             2022, revised Mar 2023; ICLR 2023. Note: it induces grokking by
             controlling initialization scale / weight norm, not through natural
             large-scale training, and it can also switch grokking off. It is
             evidence that grokking is a tunable landscape phenomenon, not a
             scale-triggered unlock.
```

```text
URL:         https://arxiv.org/abs/2506.21551
Kind:        primary. Li, Fan, Zhou reporting their own pretraining measurements.
Establishes: The strongest available claim that a grokking-like effect appears at
             practical LLM scale. This is the source that most tests the
             commission's "toy-scale only" framing. Records both what it claims
             (delayed generalization at 7B) and how it redefines the effect.
Paraphrase:  Tracking checkpoints during one-pass pretraining of a 7B-parameter
             Mixture-of-Experts LLM (OLMoE), the authors compute per-sample
             training-loss convergence and compare it to downstream benchmark
             generalization across domains (math, code, commonsense, retrieval).
             They report that delayed generalization still occurs at this scale,
             but as a local, asynchronous, per-domain effect rather than one
             global synchronized jump: harder, later-memorized samples generalize
             with systematically longer delay. They propose pathway-based internal
             metrics (expert-routing edit distance, pathway consistency) to detect
             it without a held-out test set.
Locators:    Abstract and findings sections (read via ar5iv.labs.arxiv.org/html/2506.21551).
Quote:       "Grokking still occurs during the one-pass pretraining of
             practical-scale LLMs but it is local and asynchronous for different
             data groups/domains." And: "training loss stabilizes well before test
             accuracy begins to improve."
Detail:      Authors: Ziyue Li, Chenrui Fan, Tianyi Zhou (University of Maryland).
             arXiv 2025. The measured object is delayed generalization detected
             through convergence criteria and internal proxies, not a sudden
             test-accuracy spike; the paper explicitly contrasts its asynchronous,
             domain-staggered pattern with the global synchronized memorize-then-
             generalize pattern of the toy setting.
```

```text
URL:         https://www.quantamagazine.org/how-do-machines-grok-data-20240412/
Kind:        secondary. Science journalism reporting on grokking research from
             outside the authoring groups; quotes multiple researchers. Meets the
             commission's independent-secondary requirement (it is not a
             restatement of any single paper's own claim).
Establishes: How grokking is talked about in the wider argument, and the standing
             caution against over-extrapolation. Useful for the "how it is cited
             today" turn and for the sudden-versus-gradual framing.
Paraphrase:  The article presents grokking as apparent sudden understanding that
             is, underneath, a gradual internal shift from a memorizing algorithm
             to a generalizing one, with regularization moving resources between
             them. It reports the phenomenon has been studied in "only extremely
             small networks" and quotes Mikhail Belkin cautioning that modular
             arithmetic is "a drop in the ocean" compared with what today's
             networks do. Notably, it does not itself connect grokking to specific
             large-model or chatbot capability claims.
Locators:    Article body; author Anil Ananthaswamy; Quanta Magazine; 12 Apr 2024.
Quote:       "It's possible for things that seem sudden to actually be gradual
             under the surface." And, on scope: modular arithmetic is "a drop in
             the ocean."
```

## Contradictions

- **Toy-scale-only versus grokking at 7B (the main tension).** The commission's
  angle says the paper's setup "cannot carry" a claim about large systems, and
  that grokking has not been shown at frontier scale. Li, Fan, Zhou (2506.21551)
  report delayed generalization during real one-pass pretraining of a 7B MoE LLM.
  Two things keep this from overturning the angle, and both should be stated
  plainly rather than buried: first, it is a separate 2025 result, not something
  the 2022 paper showed; the original paper's own scale still cannot carry the
  large-model claim. Second, the 7B result is not the popular "sudden unlock." It
  is measured as local, asynchronous, per-domain delayed generalization detected
  through internal proxy metrics, and it explicitly contrasts itself with the toy
  setting's single global jump. So the paper simultaneously widens grokking's
  reach and undercuts the "sudden hidden phase change" reading the shorthand
  relies on. The editor should decide how much weight to give it; it is the one
  source that genuinely complicates a flat "toy only" statement.

- **How "sudden" is grokking?** No source I read defends grokking as a genuinely
  instantaneous jump once the metric is chosen well. Nanda et al. and the Quanta
  reporting both frame the externally sudden curve as a gradual internal
  transition. The 7B paper reinforces this (loss stabilizes well before test
  accuracy moves). This is agreement across sources, and it agrees with the
  angle. The remaining honest caveat: the surface test-accuracy curve in the
  original Figure 1 genuinely is abrupt on a log-step axis; "gradual" is a claim
  about internal progress measures, not about the watched metric. That
  distinction is the whole point and must survive into the draft.

- **Is weight decay necessary, or just most effective?** Slight disagreement in
  strength. The original paper frames weight decay as the single most effective
  data-efficiency intervention (more than halving samples needed), which implies
  grokking can occur without it, only worse. Nanda et al. describe weight decay
  as driving cleanup and (in their setup) necessary for grokking. Omnigrok recasts
  the lever as the weight norm, of which weight decay is one control. These are
  compatible if read as "weight decay is the dominant driver of the transition,"
  but do not let the draft flatten Nanda's "necessary" and the original paper's
  "most effective" into one claim; cite whichever paper owns the exact wording.

- **Does grokking generalize beyond arithmetic?** Omnigrok cuts both ways against
  a naive reading. It induces grokking on images, language, and molecules, so
  grokking is not unique to modular arithmetic; but it does so by tuning
  initialization/weight norm, not by scaling up natural training, and it can also
  switch grokking off on algorithmic data. The correct reading is that grokking
  is a controllable property of the loss landscape, which deflates the mystique
  rather than confirming a scale-unlock.

## Numbers

```text
Figure: p = 97 (prime modulus for the modular-arithmetic operations)
Owner:  Power et al. 2022 (2201.02177)
Scope:  Applies to mod-p operations; the full table has 97^2 = 9,409 equations.
```

```text
Figure: ~4 x 10^5 non-embedding parameters; 2 layers, width 128, 4 heads
Owner:  Power et al. 2022
Scope:  The transformer used across the paper's algorithmic experiments.
```

```text
Figure: 50% of the data in the training set (headline division-mod-97 run)
Owner:  Power et al. 2022, Figure 1 (left)
Scope:  Half of the 9,409-equation table; the rest is held out for validation.
```

```text
Figure: train accuracy near-perfect at <10^3 steps; validation reaches that
        level near 10^6 steps; "very little evidence of any generalization
        until 10^5 steps"
Owner:  Power et al. 2022, Figure 1 (left) caption
Scope:  Division mod 97, 50% train, single run; optimization-step (update) axis,
        log scale. This is the ~1000x gap between fitting and generalizing.
```

```text
Figure: near 25-30% training data, a 1% decrease raises median
        time-to-generalization by 40-50%
Owner:  Power et al. 2022 (data-efficiency result)
Scope:  Median over runs; steepness of the data-fraction-to-optimization curve.
```

```text
Figure: weight decay more than halves the number of samples needed for
        generalization versus other interventions
Owner:  Power et al. 2022 (intervention comparison)
Scope:  Compared against full-batch GD, SGD, learning-rate changes, residual
        dropout, gradient noise. Figure number not confirmed from text; recorded
        as the paper's intervention/data-efficiency comparison.
```

```text
Figure: p = 113 (prime modulus); training on 30% of input pairs
Owner:  Nanda et al. 2023 (2301.05217)
Scope:  Modular addition a+b mod 113; one-layer transformer, d=128, 4 heads,
        MLP width 512; AdamW lr 10^-3, weight decay 1.
```

```text
Figure: five key Fourier frequencies, k in {14, 35, 41, 42, 52}
Owner:  Nanda et al. 2023
Scope:  The frequencies the trained network uses to implement modular addition
        as rotation; ablating these collapses the generalizing solution.
```

```text
Figure: three phases (approx. epochs): memorization 0-1.4k, circuit formation
        1.4k-9.4k, cleanup 9.4k-14k
Owner:  Nanda et al. 2023
Scope:  Read from their progress-measure figures; boundaries approximate. Test
        loss drops in cleanup while the circuit was already forming earlier.
```

```text
Figure: 7 x 10^9 parameters (7B MoE, OLMoE)
Owner:  Li, Fan, Zhou 2025 (2506.21551)
Scope:  One-pass pretraining; delayed generalization measured per domain and via
        internal pathway proxies, not a single global test-accuracy jump.
```

Full accuracy-versus-steps series: not available as a numeric table. The papers
state landmark points in text (above); the continuous curves live only in the
figures. A chart reproducing the grokking curve would need the series digitized
from Power et al. Figure 1 (left) or, better, regenerated from the described
setup rather than lifted from the paper image.

## Source assets

```text
Asset: Power et al. 2022, Figure 1 (left) — the grokking curve for division
       mod 97 at 50% train: red training-accuracy curve reaching ~100% below
       10^3 steps, green validation-accuracy curve flat near chance until ~10^5
       steps and rising to ~100% near 10^6 steps, on a log optimization-step axis.
Shows: The entire phenomenon in one image: fast memorization, a long flat
       validation plateau, then the late rise. The ~1000x gap is legible directly.
Crop:  Must retain both curves, the log x-axis with its 10^3 / 10^5 / 10^6
       gridlines, and the y-axis showing accuracy from chance to 100%. Do not crop
       away the flat plateau — the plateau is the point. (House rule: charts are
       regenerated from a committed chart script, not lifted; this is the shape to
       reproduce, not an image to embed.)
```

```text
Asset: Power et al. 2022, Figure 1 (center) — median steps-to-generalization
       versus training-data fraction (log y-axis), for the S5 product.
Shows: How sharply required optimization rises as training data shrinks; the
       quantitative basis for the 25-30% / 40-50% data-efficiency claim.
Crop:  Retain the log y-axis and the data-fraction x-axis; the curve's steepness
       is the content.
```

```text
Asset: Nanda et al. 2023 — the progress-measures figure: restricted loss and
       excluded loss (and the three-phase shading) plotted against training
       epochs beside the flat-then-dropping test loss.
Shows: That the generalizing circuit strengthens during circuit formation while
       test loss is still flat — the direct visual case that "sudden" is only
       sudden in the watched metric.
Crop:  Must keep the flat test-loss segment aligned with the already-moving
       progress measures; the alignment is the argument. Omitting the test-loss
       trace destroys the point.
```

```text
Asset: Nanda et al. 2023 — the Fourier-spectrum plot of the embedding / neuron
       activations showing energy concentrated at a few frequencies.
Shows: The learned solution is sparse and structured (a handful of frequencies),
       not a memorization lookup — the concrete face of "it learned an algorithm."
Crop:  Retain the frequency axis and the isolated peaks; the sparsity is the
       evidence.
```

```text
Asset: Google PAIR interactive explorable, "Do Machine Learning Models Memorize
       or Generalize?" (pair.withgoogle.com/explorables/grokking/).
Shows: An animated memorize-to-generalize transition; useful only as a Go-deeper
       pointer, not as source evidence. Secondary and not cited for any claim.
Crop:  N/A (interactive).
```

## Discarded

```text
None rejected after a full read. Several candidates surfaced in search and were
not opened, so they are not recorded as sources or assets: "Grokking as the
Transition from Lazy to Rich Training Dynamics" (2310.06110), "Critical Data Size
of Language Models from a Grokking Perspective" (2401.10463), and the Wikipedia
"Grokking (machine learning)" entry. If the writer needs the lazy-to-rich framing
or a second at-scale data point, those are the next reads; I did not open them, so
nothing from them appears above.
```
