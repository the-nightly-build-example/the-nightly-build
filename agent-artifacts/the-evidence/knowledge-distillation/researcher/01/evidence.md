# Evidence: the-evidence/knowledge-distillation (01)

The commissioned angle holds up against the documents, with two corrections the
writer must not skip. The soft-target-with-temperature method is exactly as the
commission describes it, and the three experiments are real, with figures I read
firsthand in the paper. But the paper the desk is reading never uses the phrase
"dark knowledge" the commission borrows for the idea, and its largest experiment
(the JFT specialists) does not actually complete a distillation: the authors say
in the paper that they did not distill the specialist ensemble back into one net.
The two experiments that demonstrate distillation end to end are MNIST and speech.
The drift claim is well sourced and precise, but it is narrower than "people
misuse the word": the broadening began in peer-reviewed work within a year
(Kim and Rush 2016 already used "knowledge distillation" for a hard-target,
generated-sequence method), and today's frontier usage (DeepSeek-R1) is a clean
case of training on a stronger model's generated text with none of the paper's
soft-target mechanism. DistilBERT, by contrast, is a faithful application that
does use temperature-softened soft targets, so it belongs on the "kept the method"
side of the line, not the "borrowed the name" side.

## Sources

```text
URL:         https://arxiv.org/abs/1503.02531
Kind:        primary. Owns the distillation method and every experiment number.
             Authors are the parties who ran the experiments and coined the usage.
Establishes: The soft-target-with-temperature method; the MNIST, speech, and JFT
             experiments and their scale; the paper's own framing of the idea.
Paraphrase:  A softmax raised to temperature T, q_i = exp(z_i/T) / sum_j exp(z_j/T),
             turns a model's outputs into a "softer" probability distribution over
             classes. The student trains on those softened outputs (soft targets)
             from the teacher at the same high T, then runs at T=1. The paper credits
             Caruana's earlier compression work and says it develops that approach
             "using a different compression technique." It frames the transferable
             knowledge as the relative probabilities the teacher assigns to wrong
             answers.
Locators:    Abstract; Section 1 (Introduction); Section 2 (Distillation); Section 3
             (MNIST); Section 4 (speech); Sections 5-6 (JFT specialists). NIPS 2014
             Deep Learning Workshop; submitted 9 March 2015.
Quote:       "The relative probabilities of incorrect answers tell us a lot about how
             the cumbersome model tends to generalize." / "An image of a BMW, for
             example, may only have a very small chance of being mistaken for a
             garbage truck, but that mistake is still many times more probable than
             mistaking it for a carrot." / "Using a higher value for T produces a
             softer probability distribution over classes." / "Since the magnitudes
             of the gradients produced by the soft targets scale as 1/T^2 it is
             important to multiply them by T^2 when using both hard and soft targets."
```

```text
URL:         https://www.cs.cornell.edu/~caruana/compression.kdd06.pdf
Kind:        primary. Owns the acknowledged predecessor. Authored by the researchers
             who ran the compression experiments (Bucila, Caruana, Niculescu-Mizil,
             Cornell), published at KDD 2006.
Establishes: The idea Hinton's paper builds on: compress a large ensemble into one
             small fast neural net by using the ensemble to LABEL a large data set,
             then training the net to mimic those labels. Introduces MUNGE for
             generating synthetic data when unlabeled data is scarce.
Paraphrase:  "Instead of training the neural net on the original (often small) training
             set used to train the ensemble, we use the ensemble to label a large
             unlabeled data set and then train the neural net on this much larger,
             ensemble labeled, data set." The mimic net matches the ensemble's own
             predictions, not the original 0/1 labels. It does NOT use a
             temperature-softened multi-class softmax or logits: that softening is
             Hinton's addition. Evaluated on eight binary classification problems
             (UCI ADULT, COVTYPE, LETTER, etc.), 4,000 real training points plus up
             to ~396k synthetic points.
Locators:    Abstract; Section 1; Section 2 (and 2.3 MUNGE); Section 3.2 (Results,
             Table 2); Section 6 (Conclusions).
Quote:       "On average, model compression with MUNGE is able to achieve 97% of the
             performance increase that could at best be expected." / "the mimic neural
             nets are 100-100,000 times smaller than the ensembles, and 100 to 10,000
             times faster to execute." / Conclusion: "the mimic neural nets are 1000
             times smaller and 1000 times faster."
```

```text
URL:         https://arxiv.org/abs/1910.01108
Kind:        primary. Owns the DistilBERT claims. Authored by the Hugging Face team
             that built and measured the model (Sanh, Debut, Chaumond, Wolf).
Establishes: A well-known faithful application of the soft-target method. Distills
             during pre-training with a triple loss: language modeling, distillation
             (soft targets on the teacher's output distribution, softmax temperature),
             and cosine distance. This is the paper's method, kept, not a loose usage.
Paraphrase:  DistilBERT is 40% smaller than BERT, 60% faster, and retains 97% of BERT's
             language-understanding performance (GLUE). It uses the teacher's softened
             output distribution as the distillation target, which is Hinton's soft
             targets, applied to a language model rather than an image or speech model.
Locators:    Abstract; the triple-loss description in the abstract and Section 3.
             Submitted 2 October 2019.
Quote:       "reduce the size of a BERT model by 40%, while retaining 97% of its
             language understanding capabilities and being 60% faster." / "we introduce
             a triple loss combining language modeling, distillation and cosine-distance
             losses."
```

```text
URL:         https://arxiv.org/abs/1606.07947
Kind:        primary. Owns the sequence-level distillation method. Authored by Kim and
             Rush (Harvard), EMNLP 2016.
Establishes: That the term "knowledge distillation" was extended within a year to a
             method that does NOT match softened distributions. It documents the
             standard (word-level) method and contrasts it with a sequence-level method
             that trains the student on the teacher's actual generated output.
Paraphrase:  Standard word-level distillation minimizes cross-entropy with the teacher's
             probability distribution at each position (the Hinton method, citing Hinton
             et al. 2015 and Bucila et al. 2006). Their sequence-level distillation
             instead runs beam search with the teacher over the training set and trains
             the student on the highest-scoring generated sequences as hard targets.
             The best student runs 10x faster than the teacher; sequence-level
             distillation beats a no-distillation baseline by 4.2/1.7 BLEU (greedy/beam).
Locators:    Abstract; Section 2.2 (word-level); Sections 3.2 and 4 (sequence-level).
Quote:       "Instead of minimizing cross-entropy with the observed data, we instead
             minimize the cross-entropy with the teacher's probability distribution."
             (word-level) / "train the student network with cross-entropy on this
             newly-generated dataset" produced by "running beam search and taking the
             highest-scoring sequence with the teacher model." (sequence-level)
```

```text
URL:         https://arxiv.org/abs/2501.12948
Kind:        primary. Owns the present-day frontier usage. Authored by DeepSeek-AI;
             also published in Nature 645:633-638 (2025).
Establishes: A clean case of "distillation" that has none of the paper's soft-target
             mechanism. Here distillation means supervised fine-tuning of smaller open
             models on text generated by a stronger model.
Paraphrase:  To give small models reasoning ability, they "directly fine-tuned
             open-source models like Qwen and Llama using the 800k samples curated with
             DeepSeek-R1." They "apply only SFT and do not include an RL stage" for the
             distilled models. There are no soft targets, no temperature, and no logit
             matching: the student trains on generated text as ordinary supervised data.
             Base models named include Qwen2.5 (1.5B to 32B) and Llama-3.1-8B /
             Llama-3.3-70B-Instruct.
Locators:    Section 2.4 ("Distillation: Empower Small Models with Reasoning
             Capability"). Submitted 22 January 2025.
Quote:       "we directly fine-tuned open-source models like Qwen and Llama using the
             800k samples curated with DeepSeek-R1." / "For distilled models, we apply
             only SFT and do not include an RL stage."
```

```text
URL:         https://arxiv.org/abs/2006.05525
Kind:        secondary. A survey reporting on the field from outside the original
             authoring parties (Gou, Yu, Maybank, Tao), IJCV 2021. It reports the
             taxonomy; it does not own the original method.
Establishes: That Hinton's soft-target method is now one category among several. The
             survey sorts distillation knowledge into response-based, feature-based, and
             relation-based, and places Hinton's logit/soft-target method in only the
             first. It records the lineage: Bucila 2006 first proposed the compression,
             Hinton 2015 popularized it as "knowledge distillation."
Paraphrase:  "response-based knowledge, feature-based knowledge, and relation-based
             knowledge" are the survey's three categories. Response-based knowledge is
             "the neural response of the last output layer of the teacher model," which
             is Hinton's soft targets. The survey attributes the term's popularization
             to Hinton et al. 2015 and the earlier idea to Bucila et al. 2006.
Locators:    Section 2 (knowledge categories); introduction (historical attribution).
Quote:       "The learning of a small model from a large model is later formally
             popularized as knowledge distillation (Hinton et al. 2015)." / "Bucilua et
             al. (2006) first proposed model compression to transfer the information from
             a large model or an ensemble of models into training a small model."
```

```text
URL:         https://www.ibm.com/think/topics/knowledge-distillation
Kind:        secondary. A vendor explainer (IBM; author Dave Bergmann) reporting the
             mainstream present-day definition. Useful for the drift claim as it shows
             the broadened, mechanism-agnostic definition in wide circulation.
Establishes: That the common definition today is teacher-to-student transfer in general,
             not soft targets specifically. It names Hinton et al. 2015 as the seminal
             paper and describes the goal broadly as matching the teacher's predictions,
             and even its reasoning steps.
Paraphrase:  Distillation "aims to transfer the learnings of a large pre-trained model,
             the 'teacher model,' to a smaller 'student model.'" The primary objective
             is "to train the student network to match the predictions made by the
             teacher network," and newer methods "train student models to mimic not just
             the teacher model's final output... but also the reasoning steps."
Locators:    Opening definition; the section citing the 2015 paper.
Quote:       "Knowledge distillation is a machine learning technique that aims to transfer
             the learnings of a large pre-trained model, the 'teacher model,' to a smaller
             'student model.'"
```

## Contradictions

- The commission calls the idea the paper's "dark knowledge." The phrase does not
  appear anywhere in the 2015 paper. I searched the full text. The paper's own
  words are "soft targets" and "the relative probabilities of incorrect answers."
  "Dark knowledge" comes from Hinton's later talks, not this document. The writer
  should teach the idea in the paper's words and must not put the phrase in the
  paper's mouth. If the lesson uses "dark knowledge" at all, it should attribute it
  as Hinton's later informal name, not a term from the paper.

- The commission lists the JFT specialists experiment as one of the three that
  "show it works" for distillation. The paper does not distill the specialists in
  that experiment. The authors write: "We have not yet shown that we can distill the
  knowledge in the specialists back into the single large net." What JFT shows is
  that adding 61 specialist models to the baseline raises accuracy and that
  specialists train fast (a few days versus the baseline's ~six months). It is a
  motivation-and-ensemble result at large scale, not a completed distillation. The
  two experiments that demonstrate distillation end to end are MNIST and speech.
  This matters directly for the "show the scale honestly" instruction: the largest
  experiment is the one where the distillation step was not run.

- The drift is real but narrower than "the word is misused." The extension to
  non-soft-target methods happened in peer-reviewed research within a year (Kim and
  Rush 2016, a hard-target generated-sequence method still called "knowledge
  distillation"). The survey (Gou 2021) treats Hinton's method as one of three
  knowledge categories, not the definition. So the honest framing is that the term
  now names a family of teacher-to-student methods, of which Hinton's soft-target
  logit matching is the original and one member. DeepSeek-R1 is the clean case where
  the modern usage keeps none of the paper's mechanism (no soft targets, no
  temperature, just SFT on generated text). DistilBERT is the counter-case that keeps
  the mechanism. The gap the desk wants is best drawn between those two, not as a
  blanket claim that everyone gets the word wrong.

- Minor: an earlier web search snippet claimed DeepSeek-R1 distilled into "DeepSeek-V3."
  That is wrong and I did not use it. The paper's own Section 2.4 names Qwen and Llama
  as the distilled students; V3 is a base model, not a distilled student. I trusted the
  primary.

## Numbers

```text
Figure: 67 test errors (of 10,000) - large MNIST net, two hidden layers of 1200 ReLU units,
        trained with dropout, weight constraints, and jittered images
Owner:  Hinton, Vinyals, Dean 2015, Section 3
Scope:  MNIST test set, 10,000 cases
```

```text
Figure: 146 test errors - small net (two hidden layers of 800 units) with no regularization
Owner:  Hinton, Vinyals, Dean 2015, Section 3
Scope:  MNIST test set, 10,000 cases
```

```text
Figure: 74 test errors - same small net, distilled on the large net's soft targets at
        temperature 20 (no jitter). Closes most of the 146-to-67 gap.
Owner:  Hinton, Vinyals, Dean 2015, Section 3
Scope:  MNIST test set, 10,000 cases
```

```text
Figure: transfer set with NO 3s: 206 total test errors, 133 of them on the 1010 test 3s
        (877/1010 = 86.8% of 3s right); after raising the 3's bias by 3.5, 109 total errors,
        14 on 3s (996/1010 = 98.6% of test 3s right)
Owner:  Hinton, Vinyals, Dean 2015, Section 3 (the "omit the 3" transfer experiment)
Scope:  MNIST test set. Note the 98.6% headline figure required a manual bias adjustment
        to the 3 output unit; before the adjustment the model already got 86.8% of 3s right
        despite never seeing a labeled 3.
```

```text
Figure: transfer set with only 7s and 8s: 47.3% test errors; after lowering the biases by
        7.6, 13.2% test errors
Owner:  Hinton, Vinyals, Dean 2015, Section 3
Scope:  MNIST test set, two-class transfer variant
```

```text
Figure: Speech net: 8 hidden layers of 2560 ReLU units, 14,000 output labels (HMM states);
        ~2000 hours of English, ~700M training examples; ensemble of 10 models
Owner:  Hinton, Vinyals, Dean 2015, Section 4
Scope:  Google's production acoustic model at the time
```

```text
Figure: Speech results - baseline single net: 58.9% frame accuracy, 10.9% WER;
        10x ensemble: 61.1% accuracy, 10.7% WER; distilled single net: 60.8% accuracy, 10.7% WER
Owner:  Hinton, Vinyals, Dean 2015, Section 4 (results table)
Scope:  Test frame accuracy and Word Error Rate. Distillation recovers most of the ensemble's
        frame-accuracy gain (58.9 to 60.8 of 61.1) and matches the ensemble WER. The WER gain
        over baseline is small in absolute terms: 0.2 points (10.9 to 10.7).
```

```text
Figure: JFT dataset - 100 million labeled images, 15,000 labels; baseline deep CNN trained
        ~6 months by distributed SGD; 61 specialist models (300 classes each + a dustbin
        class), each trained in "a few days"
Owner:  Hinton, Vinyals, Dean 2015, Sections 5-6
Scope:  Google internal image dataset
```

```text
Figure: JFT results - baseline: 25.0% test accuracy, 43.1% conditional test accuracy;
        + 61 specialists: 26.1% test accuracy, 45.9% conditional; 4.4% relative improvement overall
Owner:  Hinton, Vinyals, Dean 2015, Table 3
Scope:  JFT test set. Low absolute accuracy reflects 15,000 classes. This is the specialist
        ENSEMBLE's accuracy; the specialists were not distilled back into one net.
```

```text
Figure: JFT breakdown (Table 4), relative accuracy change by number of specialists covering a class:
        0 specialists -> 0.0% (350,037 test examples); 1 -> +3.4%; 2 -> +7.4%; 3 -> +8.8%;
        4 -> +10.5%; 5 -> +11.1%; 6 -> +11.3%; 7 -> +12.8%; 8 -> +13.6%; 9 -> +16.6%; 10+ -> +14.1%
Owner:  Hinton, Vinyals, Dean 2015, Table 4
Scope:  JFT test set, grouped by how many specialists cover each class
```

```text
Figure: Model Compression - mimic nets achieve 97% of the best-possible performance increase;
        ~1000x smaller and ~1000x faster than the ensembles (paper's headline); range across
        problems 100-100,000x smaller, 100-10,000x faster
Owner:  Bucila, Caruana, Niculescu-Mizil 2006, Section 3.2 (Table 2, Table 3, Table 4) and Conclusion
Scope:  Eight binary classification problems, 4,000 real training points + up to ~396k synthetic
        (MUNGE) points. Table 4: average ensemble size ~550 MB vs mimic net ~0.33 MB.
```

```text
Figure: DistilBERT - 40% smaller than BERT, 60% faster, retains 97% of language-understanding
        performance
Owner:  Sanh, Debut, Chaumond, Wolf 2019, Abstract
Scope:  GLUE language-understanding benchmark; on-device inference for the speed figure
```

```text
Figure: DeepSeek-R1 distillation - 800k curated samples generated with DeepSeek-R1; students are
        open models (Qwen 1.5B-32B, Llama-3.1-8B, Llama-3.3-70B); SFT only, no RL, no soft targets
Owner:  DeepSeek-AI 2025, Section 2.4
Scope:  Supervised fine-tuning on generated text
```

```text
Figure: Sequence-level distillation (Kim and Rush) - best student 10x faster than teacher;
        +4.2/1.7 BLEU over a no-distillation baseline (greedy/beam); with weight pruning,
        13x fewer parameters than the teacher at -0.4 BLEU
Owner:  Kim and Rush 2016, Abstract
Scope:  Neural machine translation
```

## Source assets

```text
Asset: Speech results table (Hinton 2015, Section 4): three rows, baseline / 10x ensemble /
       distilled single net, columns for frame accuracy and WER
Shows: That one distilled net recovers almost all of a 10-model ensemble's frame-accuracy gain
       and matches its WER. The clearest single-view proof the method transfers ensemble knowledge.
Crop:  Keep all three rows and both columns. Do not crop to the accuracy column alone: the small
       WER gain (0.2 points over baseline) is part of the honest picture.
```

```text
Asset: JFT specialist tables (Hinton 2015, Table 3 and Table 4). Table 3 is baseline vs +61
       specialists; Table 4 is the relative gain by number of covering specialists.
Shows: Scale (15,000 labels, low absolute accuracy) and where specialists help most (classes
       covered by more specialists gain more). Table 4 is the honest scale picture.
Crop:  If used, the caption must state these are ensemble results, not a completed distillation.
```

```text
Asset: Model Compression Figure 2 (Bucila 2006): average RMSE across eight problems vs training-set
       size, with lines for RANDOM, NBE, MUNGE, ensemble selection, best single model, best neural net
Shows: The mimic net trained on MUNGE data descending toward the ensemble's error line as synthetic
       data grows, while a plain neural net stays well above it. The predecessor's core result in one chart.
Crop:  Keep the ensemble-selection line (bottom) and the best-neural-net line (top) as reference bounds.
```

```text
Asset: Model Compression Table 4 (Bucila 2006): model size in MB, mimic net vs ensemble, per problem
Shows: Average ensemble ~550 MB against average mimic net ~0.33 MB, the concrete "~1000x smaller"
       claim made checkable.
Crop:  The MUNGE and ENSEMBLE columns plus the average row carry the point.
```

```text
Asset: Distillation paper (Hinton 2015) - no informative figures. The paper is table- and prose-based.
Shows: Nothing further; noted so the writer does not go looking for a diagram the paper does not have.
Crop:  None found.
```

## Discarded

```text
URL: https://www.forbes.com/sites/siladityaray/2025/01/29/openai-believes-deepseek-distilled-its-data-for-training-heres-what-to-know-about-the-technique/
     Returns HTTP 403 (gated) and is a contributor piece; the IBM explainer and the DeepSeek-R1
     primary cover the same present-day usage with sources that resolve.
URL: https://www.technologyreview.com/2025/02/12/1111382/a-quick-guide-to-the-most-important-ai-law-youve-never-heard-of/
     Returns HTTP 404. Not cited; a URL that does not resolve cannot back a claim.
```
