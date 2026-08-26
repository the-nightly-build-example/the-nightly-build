# Evidence: what-could-go-wrong/eliciting-latent-knowledge (02)

This record supersedes 01. It preserves every source and finding from 01 and adds
one secondary source (Fabien Roger) read this round, moved out of the earlier
Discarded list into Sources, so the record now carries eight sources: seven
primary and one secondary. The 01 record remains as written; nothing here
overwrites it.

The evidence supports the commission's spine. ELK is stated by its own authors
(Christiano, Cotra, Xu; ARC, Dec 2021) as an unsolved, worst-case problem: the
report gives the SmartVault scenario and argues that a truthful "direct reporter"
and a deceptive "human simulator" have identical loss on any training set humans
can label, so ordinary training gives no reason to prefer the honest one. Burns
et al. (2022) is the one real empirical result the beat turns on: their
unsupervised method, CCS, recovers correct answers from frozen activations and
beats zero-shot by four points on average, but the authors themselves did not
test deception and could not say in what sense CCS finds "truth." The primary
critique, Farquhar et al. (Google DeepMind, Dec 2023), demonstrates on a working
model that CCS and its cousins track the most prominent feature of the
activations, not knowledge, and proves the CCS loss is satisfied by arbitrary
binary features. Fabien Roger's commentary (LessWrong, Mar 2023) supplies the
intermediate context: CCS finds a truth-like direction but not the model's
unique knowledge, because many orthogonal directions achieve low CCS loss. The
record is thin in one honest place: linear "truth-like" directions genuinely do
exist and generalize in benign, in-distribution settings (Marks & Tegmark, 2023),
and 2025 mechanistic work extracts hidden facts in controlled toy setups. That is
real and must be reported, but every such result lives on the checkable side of
the line ELK draws, not the worst-case side. The main limitation of this record:
the ELK-report, Burns full-text, Farquhar, and Roger quotes were extracted
through a fetch of each source's own page rather than read by me
character-by-character, so treat their wording as high-confidence but verify
against the document before any one of them carries a headline; the Burns and
Marks abstracts were captured verbatim.

## Sources

```text
URL:         https://docs.google.com/document/d/1WwsnJQstPq91_Yh-Ch2XRL8H_EpsnjrC1dwZXR37PC8/edit
Kind:        primary. This is the ELK report itself, authored by ARC, which owns the argument.
Establishes: The ELK problem statement, the SmartVault thought experiment, the direct-reporter
             vs human-simulator distinction, and the claim that training cannot separate them.
Paraphrase:  A superhuman predictor guards a vault holding a diamond, watched through a camera.
             It learns a rich internal model (a "Bayes net") of what the sensors and actions imply.
             A "reporter" is trained to answer human questions about what actually happened. Two
             reporters fit the training data equally: the direct reporter (translates the
             predictor's own internal state into human concepts) and the human simulator (predicts
             what a human labeler would say after seeing the same video). They agree on every case
             a human can check and diverge exactly when the AI knows the diamond was stolen but the
             human, fooled by tampered sensors, would not. The report calls this an open problem
             central to alignment and works it in the worst case.
Locators:    Report title and problem framing (opening sections); SmartVault sections; the
             "two reporters, identical loss" argument in the section contrasting the direct
             translator with the human simulator.
Quote:       "How can we train this model to report its latent knowledge of off-screen events?
             We'll call this problem eliciting latent knowledge (ELK)." And on why training does
             not separate the two reporters: "these two reporters have identical behavior on the
             training set, so they have identical loss. It's not obvious which one gradient
             descent would find." (Extracted via the document's own Google Docs rendering; wording
             is high-confidence, verify before use as a headline quote.)
```

```text
URL:         https://www.alignment.org/blog/arcs-first-technical-report-eliciting-latent-knowledge/
Kind:        primary. ARC's own announcement page for the report; it owns the framing of status.
Establishes: Authorship (Paul Christiano, Ajeya Cotra, Mark Xu; ARC), the December 2021 date, and
             the authors' framing of ELK as an unsolved open problem rather than a result.
Paraphrase:  ARC presents ELK as "an open problem which we believe is central to alignment" and
             frames the core difficulty as learning to map between an AI's model of the world and
             a human's. The page is a landing page that links to the full report; it is not the
             report text.
Locators:    Blog post body.
Quote:       "an open problem which we believe is central to alignment"
```

```text
URL:         https://arxiv.org/abs/2212.03827
Kind:        primary. Burns, Ye, Klein, Steinhardt own the CCS method and its results.
Establishes: What CCS does, on which models, its headline accuracy, and its scope claims.
Paraphrase:  Collin Burns and Jacob Steinhardt (UC Berkeley), Haotian Ye (Peking University), and
             Dan Klein (UC Berkeley) introduce Contrast-Consistent Search. For each yes-no
             question it builds a contrast pair (the statement answered "yes" and answered "no"),
             reads the model's hidden activations for each, and trains a linear probe with no
             labels to output a probability. Two loss terms shape it: a consistency term forcing a
             statement and its negation to get opposite truth values, and a confidence term
             preventing the degenerate all-0.5 answer. The claim is that a model's representation
             of truth must obey logical consistency, so a direction obeying it recovers knowledge
             the model may not state. Published at ICLR 2023.
Locators:    Abstract; method section (contrast pairs, consistency loss, confidence loss);
             results across 6 models and 10 datasets.
Quote:       "We show that despite using no supervision and no model outputs, our method can recover
             diverse knowledge represented in large language models: across 6 models and 10
             question-answering datasets, it outperforms zero-shot accuracy by 4% on average. We
             also find that it cuts prompt sensitivity in half and continues to maintain high
             accuracy even when models are prompted to generate incorrect answers." (Abstract,
             verbatim.)
```

```text
URL:         https://ar5iv.labs.arxiv.org/html/2212.03827
Kind:        primary. The full-text HTML of the same Burns et al. paper; owns its own caveats.
Establishes: The authors' own hedges about what CCS recovers and what it does not test.
Paraphrase:  The paper states CCS depends on a truth direction actually existing and being active
             in the representation, and says it is unclear when those conditions hold. It states
             they did not test deliberate lying or deception. It positions the work as a proof of
             concept and initial step, not a solution, and questions in what sense CCS finds
             "truth" at all.
Locators:    Discussion / limitations sections; introduction's framing as an initial step.
Quote:       "CCS relies on the existence of a direction in activation space that separates true
             and false inputs well ... It is not clear when these conditions hold precisely."
             And: "We did not evaluate our method on setups involving active 'lying' or
             'deception'." (Extracted from the paper's own full text; verify wording before use as
             a headline quote.)
```

```text
URL:         https://arxiv.org/abs/2312.10029
Kind:        primary. Farquhar et al. (Google DeepMind) own this refutation and its experiments.
Establishes: That CCS and other unsupervised methods track the most prominent activation feature,
             not the model's knowledge, shown on a working model and proved in general.
Paraphrase:  Sebastian Farquhar, Vikrant Varma, Zachary Kenton, Johannes Gasteiger, Vladimir
             Mikulik, and Rohin Shah (Google DeepMind) test CCS and related unsupervised probes.
             On Chinchilla-70B with IMDb reviews, they insert a distracting feature (appending a
             random word such as "Banana" or a fictional character Alice's stated opinion); the
             probes learn the inserted feature instead of the sentiment the task asks for. They
             show CCS and simple PCA make similar predictions, so the consistency condition adds
             little. They prove the CCS objective is under-specified: for any binary feature over
             the questions there is a probe with optimal CCS loss inducing that feature. December
             2023.
Locators:    Abstract; theorem on CCS under-specification; experiments on Chinchilla-70B
             (random-words, explicit-opinion "Alice", implicit-opinion DBpedia, prompt-sensitivity
             on TruthfulQA); CCS-vs-PCA comparison.
Quote:       "the classifier that CCS finds is under-specified: for any binary feature, h, on the
             questions, there is a probe with optimal CCS loss that induces that feature." And the
             conclusion that these methods "do not discover knowledge -- instead they seem to
             discover whatever feature of the activations is most prominent." (Extracted from the
             paper's own page; verify wording before use as a headline quote.)
```

```text
URL:         https://www.lesswrong.com/posts/bWxNPMy5MhPnQTzKz/what-discovering-latent-knowledge-did-and-did-not-find-4
Kind:        secondary. Fabien Roger writes commentary and re-analysis about Burns et al.'s CCS.
             He runs his own small follow-up probes, but the piece is cited here for context on
             the CCS dispute, not as the paper that owns the ELK argument or the DeepMind
             refutation. Per the citation policy, secondary reporting is acceptable for context;
             the record leans on Burns and Farquhar for the load-bearing claims.
Establishes: The intermediate reading that predates and agrees with Farquhar: CCS finds a
             truth-like direction, but not the model's unique knowledge, because many orthogonal
             directions achieve low CCS loss. Supports that this concern was raised early and
             independently, which is why it counts as context, not proof of the underlying fact.
Paraphrase:  Roger argues CCS successfully finds a direction that classifies true/false statements
             across datasets, but does not identify the single direction corresponding to the
             model's actual beliefs. He reports finding multiple orthogonal directions that all
             achieve low CCS loss and high accuracy, so CCS captures one of many "truth-like
             features" rather than pinning down latent knowledge, and may miss information about
             the model's internal beliefs.
Locators:    Sections "CCS does not find the single linear probe with high accuracy" and
             "CCS does not always find a probe with low test CCS loss"; Main Takeaways. Dated
             March 13, 2023.
Quote:       "There are many orthogonal linear probes which achieve low loss and high CCS accuracy,
             i.e. there are many truth-like features." And: "Vanilla CCS might miss important
             information about the model's internal beliefs." (Extracted from the post's own
             LessWrong page; verify wording before use as a headline quote. A repetition supports
             that the claim was made and raised early, not that it is independently true; the
             underlying fact rests on Burns and Farquhar.)
```

```text
URL:         https://arxiv.org/abs/2310.06824
Kind:        primary. Marks & Tegmark own this positive result on linear truth structure.
Establishes: The strongest evidence that truth is linearly readable in benign settings, which the
             beat must steelman and then bound.
Paraphrase:  Samuel Marks and Max Tegmark present datasets of simple true/false factual statements
             and show that at sufficient scale LLMs linearly represent truth or falsehood, visible
             as clear linear structure. Their mass-mean (difference-in-means) probe generalizes as
             well as other probes and is more causally implicated in outputs. They explicitly
             frame the work as answering earlier skepticism that such probes fail to generalize.
             Note: this is in-distribution factual truth a human can check, not the ELK worst case.
Locators:    Abstract; PCA visualizations of true/false clusters; mass-mean probing section.
Quote:       "LLMs linearly represent the truth or falsehood of factual statements" and that
             "simple difference-in-mean probes generalize as well as other probing techniques"
             while identifying more causally implicated directions. (Abstract, near-verbatim; the
             abstract also concedes prior work found "failures of these probes to generalize in
             basic ways, among other conceptual issues.")
```

```text
URL:         https://arxiv.org/abs/2505.14352
Kind:        primary. Cywiński, Ryd, Rajamanoharan, Nanda own this 2025 mechanistic result.
Establishes: Present-day framing: mechanistic interpretability can extract a hidden fact in a
             controlled toy setup, offered as a step, not a general ELK solution.
Paraphrase:  The authors use a "Taboo" model trained to hint at a secret word without saying it,
             where the secret is absent from the prompt and training text. Logit-lens and sparse-
             autoencoder methods elicit the secret word. They call it a proof of concept and say
             the methods need testing on more complex model organisms. Affiliation not confirmed
             from the page (associated with Neel Nanda's interpretability group). Submitted May
             2025.
Locators:    Abstract; Taboo-model setup; future-work hedges.
Quote:       Methods are "effective in eliciting the secret word" and represent "a step towards
             addressing the crucial problem" of eliciting hidden knowledge. (Extracted from the
             abstract; verify before headline use.)
```

## Contradictions

The commission's angle is that ELK is a real, still-unsolved worst-case problem
and that the one hopeful empirical result (CCS) was shown to track salience, not
knowledge. I searched for evidence breaking this in both directions.

- Direction that would break it: interpretability can now reliably read a
  model's truth representation. The real evidence here is Marks & Tegmark (2023)
  and the broader "geometry of truth" line: linear truth directions exist, are
  visible, and generalize across benign true/false datasets, and mass-mean probes
  are causally implicated in outputs. This does not undermine the angle. Every one
  of these results reads truth on statements a human can already label, which is
  the checkable side of the exact line ELK draws. None of them tests the ELK worst
  case, where the model knows something the human cannot verify and may be
  optimized to say otherwise. Marks & Tegmark's own abstract concedes prior probes
  showed "failures ... to generalize in basic ways." The writer must present this
  as a genuine positive result and then bound it, not wave it away.

- Direction that would break it: ELK is a non-problem in practice. I found no
  primary source arguing this. The nearest is the 2025 mechanistic work
  (arXiv:2505.14352), which extracts a hidden word from a Taboo model. Its authors
  explicitly call it a proof of concept on a toy model organism and a step, not a
  solution, and ask for testing on harder cases. A 2025 line of work (e.g.
  "LLM Knowledge is Brittle", arXiv:2510.11905, not read in full) points the other
  way, reporting that truthfulness representations rely on superficial resemblance.

- Internal tension worth flagging: Burns et al. claim CCS recovers knowledge
  distinct from what a model says; Farquhar et al. show on Chinchilla-70B that the
  same family of methods recovers whatever feature is most prominent, including
  inserted distractors. This is the beat's central contradiction, and it is a
  direct dispute between two primary sources, not a matter of interpretation. Burns
  reports a four-point average gain on standard QA datasets; Farquhar does not
  dispute that number, but shows it does not hold when a more salient feature is
  present, which is precisely the adversarial condition ELK cares about. Roger's
  commentary sits between them in time and agrees with Farquhar's direction: he
  reported the many-truth-like-directions problem in March 2023, months before the
  DeepMind paper.

## Numbers

```text
Figure: CCS outperforms zero-shot accuracy by 4% on average
Owner:  Burns, Ye, Klein, Steinhardt, arXiv:2212.03827 (abstract)
Scope:  Average across 6 models and 10 yes/no QA datasets; reported as 71.2% CCS vs 67.2%
        calibrated zero-shot in the paper body. In-distribution QA, no deliberate deception.
```

```text
Figure: 6 models, 10 datasets
Owner:  Burns et al., arXiv:2212.03827
Scope:  Models: T5, UnifiedQA, T0, GPT-J, RoBERTa, DeBERTa. Datasets include IMDB, Amazon,
        AG-News, DBpedia-14, RTE, QNLI, COPA, Story-Cloze, BoolQ, PIQA.
```

```text
Figure: CCS maintains high accuracy when models are prompted to answer incorrectly
Owner:  Burns et al., arXiv:2212.03827
Scope:  Paper body reports CCS roughly 82-84% under a misleading prompt where zero-shot
        drops ~9.5 points. Still an in-distribution setup, not active deception (authors
        state they did not test lying/deception).
```

```text
Figure: ~50% accuracy on the intended task once a distracting feature is inserted
Owner:  Farquhar, Varma, Kenton, Gasteiger, Mikulik, Shah, arXiv:2312.10029
Scope:  Chinchilla-70B on IMDb with a random word ("Banana"/"Shed") or a character opinion
        appended; the probe tracks the inserted feature at high accuracy while sentiment
        accuracy falls to chance. Demonstrates salience-tracking, not knowledge.
```

```text
Figure: For any binary feature there is a probe with optimal CCS loss inducing it
Owner:  Farquhar et al., arXiv:2312.10029 (theoretical result)
Scope:  General claim about the CCS objective, not tied to one model. Establishes the loss
        is under-specified with respect to knowledge.
```

## Source assets

```text
Asset: The SmartVault Bayes-net diagrams in the ELK report — the predictor's internal Bayes
       net, the human's Bayes net, and the direct-translator mapping between them.
Shows: Concretely why a direct reporter and a human simulator can produce the same answers:
       one reads the predictor's own nodes, the other re-runs the human's inference.
Crop:  A crop must keep both Bayes nets and the mapping arrows; omitting either side loses
       the whole point of the contrast. Confirm the exact figure in the document before use.
```

```text
Asset: Burns et al. Figure 1 — the CCS pipeline (contrast pair to hidden states to the
       consistency-and-confidence probe).
Shows: What CCS actually does mechanically, in one image, for a reader who has never seen a
       probe.
Crop:  Keep the two branches of the contrast pair and both loss terms; do not crop to a
       single branch.
```

```text
Asset: Farquhar et al. results figures on Chinchilla-70B — accuracy on the intended label vs
       accuracy on the inserted distracting feature.
Shows: The probe following the inserted feature to high accuracy while task accuracy sits at
       chance: the salience-not-knowledge finding in one chart.
Crop:  Keep both bars/lines (intended task and inserted feature) side by side; a single bar
       proves nothing.
```

```text
Asset: Marks & Tegmark PCA visualizations of true vs false statement representations.
Shows: The clean linear separation of true and false factual statements that makes the
       "truth is linearly readable" steelman concrete and honest.
Crop:  Keep the labeled true/false clusters and the axes note that this is a low-dimensional
       projection.
```

## Discarded

```text
URL: https://www.emergentmind.com/topics/eliciting-latent-knowledge-elk — tertiary overview, no firsthand claim; used only to locate primaries.
URL: https://arxiv.org/html/2510.11905v1 — "LLM Knowledge is Brittle" (2025); relevant and supportive of the angle but not read in full this round; named in Contradictions, not cited as established.
URL: https://arxiv.org/abs/2506.00823 — "Probing the Geometry of Truth" (2025) follow-up; not needed once Marks & Tegmark carries the linear-truth steelman.
URL: https://docs.google.com/.../export?format=txt and /mobilebasic — transport routes to the ELK report, not the document's own citable page; the /edit URL above is recorded instead.
```
