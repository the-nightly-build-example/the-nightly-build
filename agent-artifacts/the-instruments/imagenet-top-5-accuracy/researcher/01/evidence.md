# Evidence record: the-instruments/imagenet-top-5-accuracy (01)

The evidence strongly supports the commission's label-noise-first angle, and every load-bearing number is verified against the primary that owns it. The metric's own definition, quoted from Russakovsky et al. (2015), shows top-5 was built to forgive the single-label/multiple-object mismatch: an image carries one ground-truth label, an algorithm returns five guesses, and it scores a hit if any of the five matches. Two independent relabelings then show how thin that single key is: Beyer et al. (2020) find roughly 29% of re-annotated validation images either hold multiple objects or map to several synonymous ImageNet classes, and Northcutt et al. (2021) find 2,916 outright wrong labels, about 6% of the 50,000-image validation set. The saturation point is primary and exact: winning top-5 error fell from 28.2% (2010) to 3.57% (ResNet, 2015), crossing the ~5.1% human figure and settling near the label-error floor. The human-baseline crack is documented in ImageNet's own record and, unusually, in the annotator's firsthand account: the 5.1% was one trained expert (Andrej Karpathy), while a second annotator scored ~12%.

The record is thin or contested in three places, all recorded below. First, the "label-error rate" is not one number: Russakovsky's own small-sample estimate is ~0.3%, Northcutt's human-validated figure is ~6%, and Beyer's ~29% counts multi-label ambiguity, not outright error, so the three measure different things. Second, correcting the labels does **not** flip the overall leaderboard: Northcutt find relative model rankings "unaffected" by correction, with the instability confined to near-top comparisons on the mislabeled subset. Third, the critique papers themselves affirm that ImageNet drove real progress and remains a useful benchmark, which the honest counter must carry. The GLUE finding is confirmed and distinct (see Contradictions and the closing note), so the writer can link it and stay off that ground.

## Sources

```text
URL:         https://arxiv.org/abs/1409.0575
Kind:        primary — Russakovsky et al., "ImageNet Large Scale Visual Recognition
             Challenge," IJCV 2015. Owns the task definition, the dataset, and the
             human-accuracy experiment firsthand.
Establishes: The exact top-5 and top-1 scoring rules; the single-label ground truth;
             the class and image counts; the explicit multi-object reason top-5 exists;
             the 5.1% / 12.0% human figures from two expert annotators; the authors'
             own estimate that ~0.3% of a 1,500-image sample was mislabeled in the
             ground truth.
Paraphrase:  Classification uses 1,000 object classes, ~1.2M training images, 50,000
             validation images, 100,000 test images. Each image has one ground-truth
             label. An algorithm returns up to five labels and is scored correct if any
             one matches; that is top-5 error. Top-1 error penalizes only the single
             highest-confidence label. The five-label allowance was introduced because
             only one category is labeled per image, which "creates ambiguity" for
             images holding more than one object. Human accuracy was measured by two
             trained expert annotators on test images: annotator A1 (trained on 500,
             labeled 1,500) reached 5.1% top-5 error against GoogLeNet's 6.8% on that
             sample; annotator A2 (trained on 100, labeled 258) reached ~12.0%. Both
             humans and GoogLeNet struggled most with images containing multiple ILSVRC
             classes, an error the authors say "is only present in the Classification
             setting, since every image is constrained to have exactly one correct
             label."
Locators:    Sec 2.1 (single label); Sec 3.1 (counts, Table 2: 1,281,167 train / 50,000
             val / 100,000 test); Sec 4.1 (top-5 rule Eq. 1, strawberry/apple ambiguity,
             top-1 rule); Sec 6.4 and 6.4.1 (human accuracy, Table 9); Sec 6.4.2
             (multiple-objects error type; 0.3% ground-truth errors).
Quote:       "each image i has a single class label Ci. An algorithm is allowed to
             return 5 labels ci1,...ci5, and is considered correct if cij = Ci for some
             j." / "an image might be labeled as a 'strawberry' but contain both a
             strawberry and an apple. Then an algorithm would not know which one of the
             two objects to name. For the image classification task we allowed an
             algorithm to identify multiple (up to 5) objects in an image and not be
             penalized as long as one of the objects indeed corresponded to the ground
             truth label." / "The human error was estimated to be 5.1%." / "the final
             classification error is significantly worse, at approximately 12.0% Top-5
             error." / "This error is only present in the Classification setting, since
             every image is constrained to have exactly one correct label."
```

```text
URL:         https://proceedings.neurips.cc/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
Kind:        primary — Krizhevsky, Sutskever, Hinton, "ImageNet Classification with Deep
             Convolutional Neural Networks," NIPS 2012 (AlexNet). Owns the 2012 metric
             value.
Establishes: AlexNet's winning ILSVRC-2012 top-5 error and the second-place margin; the
             single-model figure behind the ensemble result.
Paraphrase:  A single CNN reached 18.2% top-5 error; averaging five CNNs gave 16.4%; two
             CNNs pre-trained on the Fall-2011 release, averaged with the five, gave the
             winning 15.3%. The second-best ILSVRC-2012 entry scored 26.2%. (For
             ILSVRC-2010 the paper reports 37.5% top-1 / 17.0% top-5.) The ~11-point gap
             over the runner-up is the real-progress fact the honest counter needs.
Locators:    Abstract (15.3% vs 26.2%); Sec 7 Results (18.2% single model, 16.4% five,
             15.3% winning entry).
Quote:       "We also entered a variant of this model in the ILSVRC-2012 competition and
             achieved a winning top-5 test error rate of 15.3%, compared to 26.2%
             achieved by the second-best entry." / "The CNN described in this paper
             achieves a top-5 error rate of 18.2%. Averaging the predictions of five
             similar CNNs gives an error rate of 16.4%."
```

```text
URL:         https://arxiv.org/abs/1502.01852
Kind:        primary — He, Zhang, Ren, Sun, "Delving Deep into Rectifiers: Surpassing
             Human-Level Performance on ImageNet Classification," 2015 (PReLU-net). Owns
             the "superhuman" claim.
Establishes: The first published model result to pass the 5.1% human figure, and the
             authors' own caveat that this is not general machine-over-human vision.
Paraphrase:  PReLU-nets reached 4.94% top-5 test error on ImageNet 2012, a 26% relative
             improvement over GoogLeNet's 6.66%. The authors state this is, to their
             knowledge, the first result to surpass the 5.1% human-level figure they cite
             from Russakovsky et al. They immediately qualify it: beating the number on
             this dataset does not mean machine vision beats human vision on object
             recognition in general, and machines "still have obvious errors in cases
             that are trivial for humans."
Locators:    Abstract (4.94%, "first to surpass human-level performance (5.1%)");
             Sec 6 / Analysis of Results (the caveat).
Quote:       "To our knowledge, our result is the first to surpass human-level
             performance (5.1%, [22]) on this visual recognition challenge." / "While our
             algorithm produces a superior result on this particular dataset, this does
             not indicate that machine vision outperforms human vision on object
             recognition in general ... machines still have obvious errors in cases that
             are trivial for humans."
```

```text
URL:         https://arxiv.org/abs/1512.03385
Kind:        primary — He, Zhang, Ren, Sun, "Deep Residual Learning for Image
             Recognition," 2015 (ResNet). Owns the 2015 winning metric value.
Establishes: The 2015 endpoint of the saturation curve, 3.57% top-5, below the ~5.1%
             human figure and near the label-error floor.
Paraphrase:  An ensemble of residual nets up to 152 layers deep reached 3.57% top-5 error
             on the ImageNet test set and won first place in the ILSVRC-2015
             classification task.
Locators:    Abstract (3.57%, first place ILSVRC 2015).
Quote:       "An ensemble of these residual nets achieves 3.57% error on the ImageNet
             test set. This result won the 1st place on the ILSVRC 2015 classification
             task."
```

```text
URL:         https://arxiv.org/abs/2006.07159
Kind:        primary — Beyer, Hénaff, Kolesnikov, Zhai, van den Oord, "Are we done with
             ImageNet?," 2020. Owns the multi-label re-annotation (ReaL).
Establishes: The single-label assumption is wrong for a large share of images; corrected
             multi-label evaluation shrinks recent gains and re-ranks near-top models;
             remaining top-model error is dominated by label problems, not model error.
Paraphrase:  Many validation images hold several similarly prominent objects, so a single
             label under-describes them. Among re-annotated images, about 29% either hold
             multiple objects or map to several synonymous ImageNet classes. Beyer et al.
             collected Reassessed Labels (ReaL) for the whole validation set, ending with
             57,553 labels over 46,837 images. Under ReaL, gains of recent classifiers
             are "substantially smaller than those reported on the original labels," and
             the original ImageNet labels are "no longer the best predictors" of the
             re-collected set: several models already score higher on ReaL than the
             original labels themselves do. Even the best models still err ~11% by
             original labels and ~9% by ReaL, and their own follow-up study finds a large
             share of those "mistakes" are cases where the label, not the model, is wrong
             or incomplete. The authors nonetheless call ImageNet "a powerful benchmark
             for future research."
Locators:    Abstract; Sec 2 (single label per image); Sec 3.3 (57,553 labels / 46,837
             images); Sec 4 and Fig. 4 (slope 0.51; "no longer the best predictors";
             89.0% original vs 91.20% ReaL for the ensemble); Sec 5 and Fig. 7 (remaining
             mistakes, ~11% / ~9%).
Quote:       "many other images contain multiple, similarly prominent objects" /
             "approximately 29% either contain multiple objects or a category that
             corresponds to multiple synonym labels in ImageNet" / "we find the original
             ImageNet labels to no longer be the best predictors of this
             independently-collected set" / "Even the highest-performing models display
             an error rate of approximately 11% according to ImageNet labels, and 9%
             according to ReaL labels."
```

```text
URL:         https://arxiv.org/abs/2103.14749
Kind:        primary — Northcutt, Athalye, Mueller, "Pervasive Label Errors in Test Sets
             Destabilize Machine Learning Benchmarks," NeurIPS 2021. Owns the measured
             ImageNet validation error rate.
Establishes: The ~6% outright label-error rate in the ImageNet validation set, human-
             validated; and the precise, limited sense in which those errors move
             benchmark conclusions.
Paraphrase:  Using confident learning to flag candidates and crowd workers to check them,
             the authors find 2,916 label errors in the 50,000-image ImageNet validation
             set, which they round to 6% (the per-dataset table lists 5.83%). Across the
             ten datasets, 51% of algorithm-flagged candidates were confirmed wrong on
             average. Correcting or removing the errors leaves relative model rankings
             "unaffected" — confirming Recht et al. — but the results are "unstable":
             higher-capacity models track the systematic label errors more than smaller
             ones, so on the mislabeled slice the smaller model can win. On ImageNet with
             corrected labels, ResNet-18 outperforms ResNet-50 once the share of
             originally-mislabeled test examples rises by just 6%.
Locators:    Abstract (6% / 2,916; ResNet-18 vs ResNet-50); Table 1 (5.83% for ImageNet,
             ResNet-50 model); Sec 5 (rankings "unaffected" but "unstable," NASNet vs
             ResNet-18).
Quote:       "we identify ... 2916 (6%) errors in the ImageNet validation set (which is
             commonly used as a test set)" / "we find that relative rankings of models in
             benchmarks are unaffected after removing or correcting these label errors.
             However, we find that these benchmark results are unstable" / "on ImageNet
             with corrected labels: ResNet-18 outperforms ResNet-50 if the prevalence of
             originally mislabeled test examples increases by just 6%."
```

```text
URL:         http://karpathy.github.io/2014/09/02/what-i-learned-from-competing-against-a-convnet-on-imagenet/
Kind:        primary — Andrej Karpathy, firsthand account of being the human annotator
             behind the 5.1% figure. He owns the experience the human baseline is made
             of; this is not outside reporting on it.
Establishes: That "the human" in "5.1%" was one trained, motivated individual over many
             hours, that the number sits on a tradeoff curve rather than being a fixed
             human ceiling, and that a second annotator did far worse.
Paraphrase:  Karpathy built the labeling interface, trained himself on 500 validation
             images, then labeled 1,500 test images at roughly one per minute, admitting
             he "only enjoyed the first ~200, and the rest I only did #forscience." His
             top-5 error was 5.1% against GoogLeNet's 6.8% on that sample. A second
             annotator "only got up to about 12%." About 37% of his errors were
             fine-grained (dog breeds and the like). In a later note he stresses "human
             accuracy is not a point. It lives on a tradeoff curve," so more annotators
             or more effort would move it.
Locators:    Body (training, pace, 5.1% vs 6.8%, the ~12% second annotator, 37%
             fine-grained); the appended update ("tradeoff curve").
Quote:       "My own error in the end turned out to be 5.1%, approximately 1.7% better." /
             "I only enjoyed the first ~200, and the rest I only did #forscience." /
             "Human accuracy is not a point. It lives on a tradeoff curve."
```

```text
URL:         https://www.forbes.com/sites/michaelthomsen/2015/02/19/microsofts-deep-learning-project-outperforms-humans-in-image-recognition/
Kind:        secondary — Michael Thomsen, Forbes, 19 Feb 2015. Reports on the He et al.
             result from outside; owns no claim of its own.
Establishes: The contemporaneous misled framing: the headline states machines outperform
             humans, even though the body preserves the researchers' caveat. A clean case
             of the number's largest-type reading outrunning what it measured.
Paraphrase:  The article's headline reads "Microsoft's Deep Learning Project Outperforms
             Humans In Image Recognition," and the body says Microsoft Research
             "outperformed humans in a test to identify objects in digital images," then
             quotes the researchers' warning that this is not general proof that computer
             identification beats humans. No error figures are given in the text.
Locators:    Headline and opening paragraphs.
Quote:       "This week, Microsoft Research announced its newest deep learning project had
             outperformed humans in a test to identify objects in digital images." /
             "Researchers noted their scores shouldn't be taken as proof that computer
             image identification in general was better than humans."
```

```text
URL:         https://www.technologyreview.com/2015/05/13/168197/baidus-artificial-intelligence-supercomputer-beats-google-at-image-recognition/
Kind:        secondary — Tom Simonite, MIT Technology Review, 13 May 2015. Reports the
             2015 superhuman race and the Baidu rule-breaking from outside.
Establishes: How the "beats humans" figure propagated into a leaderboard race, and that
             one headline result was later invalidated for breaking the challenge rules —
             a concrete cost of over-trusting the number.
Paraphrase:  The article reports Baidu's system was wrong 4.58% of the time, against
             Google's 4.82% (March) and Microsoft's 4.94% (February), framing Microsoft's
             as "the first to better average human performance of 5.1 percent." A note
             added atop the piece records that on 1 June 2015 Baidu admitted breaking
             ImageNet Challenge rules, and the organizers said its results were not
             comparable to others'.
Locators:    Body (error figures; "first to better average human performance of 5.1
             percent"); top-of-page update (Baidu rule violation).
Quote:       "becoming the first to better average human performance of 5.1 percent" /
             "Baidu ... admit that it had broken rules governing the ImageNet Challenge."
```

## Contradictions

- **The honest counter the commission asked for: ImageNet-scale training drove real
  vision progress, and the label critiques do not erase that.** AlexNet's 15.3% beat the
  second-best 2012 entry's 26.2% by roughly 11 points (Krizhevsky et al.), a real jump
  that moved the field to deep networks; winning error then fell to 3.57% by 2015 (He et
  al., ResNet). Both critique papers say so plainly: Beyer et al. call ImageNet "a
  powerful benchmark for future research," and Northcutt et al. confirm Recht et al. that
  correcting labels leaves relative model rankings "unaffected." The lesson's point is
  about what the *single number* can support, not that the progress was fake.

- **The corrected key does not flip the leaderboard — a check on overreaching the label
  point.** Northcutt et al. find rankings "unaffected" by correction; the instability is
  confined to near-top comparisons, where a higher-capacity model that matches systematic
  label errors can lose to a smaller one on the mislabeled slice (ResNet-18 over ResNet-50
  once the mislabeled share rises 6%). The writer must not claim that fixing the labels
  reorders the whole leaderboard. It reorders the top of it, conditionally.

- **The "label-error rate" is genuinely disputed, because the three sources measure
  different things.** Russakovsky et al. estimate ~0.3% outright ground-truth errors in
  a 1,500-image sample. Northcutt et al. measure ~6% (2,916/50,000) outright wrong labels,
  human-validated. Beyer et al.'s ~29% counts multi-label or synonym ambiguity, not
  outright error. State which definition each number uses; do not blend them into one
  "error rate."

- **"Superhuman" is contested at the source, not only in coverage.** The He et al. paper
  that first claimed to pass 5.1% also states in the same document that the result "does
  not indicate that machine vision outperforms human vision on object recognition in
  general." The overreach is in the reading, not the paper.

## Numbers

```text
Figure: 1,000 object classes; 1,281,167 training / 50,000 validation / 100,000 test images
Owner:  Russakovsky et al. 2015 (arXiv:1409.0575), Table 2 / Sec 3.1
Scope:  ILSVRC2012–2014 image classification dataset
```

```text
Figure: Human top-5 error 5.1% (annotator A1); ~12.0% (annotator A2)
Owner:  Russakovsky et al. 2015, Sec 6.4.1, Table 9 (A1 = Karpathy, per his own account)
Scope:  A1 trained on 500 images then labeled 1,500 test images; A2 trained on 100 then
        labeled 258; top-5 error
```

```text
Figure: GoogLeNet top-5 error 6.8% on the 1,500-image human-comparison sample; 6.66% full test
Owner:  Russakovsky et al. 2015, Sec 6.4.1 / Table 7 (99.9% CI 6.40–6.92)
Scope:  ILSVRC2014 winning classification model
```

```text
Figure: AlexNet winning top-5 error 15.3% vs 26.2% second best (single model 18.2%; five-model 16.4%)
Owner:  Krizhevsky et al. 2012 (NeurIPS)
Scope:  ILSVRC-2012 classification test set
```

```text
Figure: PReLU-net top-5 error 4.94%; "first to surpass human-level performance (5.1%)"
Owner:  He et al. 2015 (arXiv:1502.01852), Abstract
Scope:  ImageNet 2012 classification test set
```

```text
Figure: ResNet ensemble top-5 error 3.57%, 1st place ILSVRC 2015
Owner:  He et al. 2015 (arXiv:1512.03385), Abstract
Scope:  ImageNet 2015 classification test set
```

```text
Figure: Year-by-year winning top-5 error: 28.2% (2010, NEC) → 25.8% (2011, XRCE) → 16.4%
        val / 15.3% test (2012, SuperVision/AlexNet) → 11.7% (2013, Clarifai) → 6.66%
        (2014, GoogLeNet) → 3.57% (2015, ResNet)
Owner:  Russakovsky et al. 2015 (Tables 6–7) for 2010–2014; He et al. 2015 (ResNet) for 2015
Scope:  ILSVRC classification, best entry per year, top-5 error. The ~5.1% human figure
        sits between 2014 and 2015; by 2015 model error is below it and near the ~6%
        label-error floor. (2016 Trimps-Soushen ~2.99% and 2017 SENet ~2.25% exist but were
        not verified against their owning papers here; use only if separately sourced.)
```

```text
Figure: ImageNet validation label errors: 2,916 outright wrong (5.83%, rounded to 6%);
        ~29% of re-annotated images multi-label/ambiguous; ~0.3% authors' own small-sample estimate
Owner:  Northcutt et al. 2021 (2,916 / 6%); Beyer et al. 2020 (29%); Russakovsky et al. 2015 (0.3%)
Scope:  50,000-image ImageNet validation set. Three different definitions — do not merge.
```

```text
Figure: Best models still err ~11% (original labels) / ~9% (ReaL); ensemble 89.0% original vs 91.20% ReaL
Owner:  Beyer et al. 2020, Sec 4–5, Fig. 4 / Fig. 7
Scope:  ImageNet validation, top-model accuracy under original vs reassessed labels
```

## Source assets

```text
Asset: Russakovsky et al. 2015, Fig. 15 (Sec 6.4.2) — grid of representative error images,
       ground truth in blue and GoogLeNet's top-5 predictions beside each, with the
       leftmost column "images that contain multiple objects."
Shows: The single-label/multi-object problem directly: an image plainly holding several
       ILSVRC objects but carrying one label, which is exactly what top-5 was built to
       forgive. Lets the reader test the mismatch on a real case.
Crop:  A multiple-object example must keep both the several visible objects and the single
       blue ground-truth label; omit the unrelated error categories (closeups, filters,
       text) if cropping to make only the multi-object point.
```

```text
Asset: Russakovsky et al. 2015, Fig. 7 (top row, Sec 4.1) — the strawberry/apple style
       example showing one image, one ground-truth label, and sample five-label outputs
       with their scores.
Shows: How top-5 scoring actually works and why five guesses were allowed — the worked
       example the commission asks for in "what to teach" item 1.
Crop:  Keep the ground-truth column and at least one scored multi-label output; the
       caption's scoring key must stay legible.
```

```text
Asset: Validated ImageNet label-error examples at https://labelerrors.com (Northcutt et al.
       2021, Fig. 1 is the paper's static version). The paper states the errors "can be
       viewed at https://labelerrors.com."
Shows: Browsable side-by-side of an ImageNet image, its given label, and the corrected
       label — the label problem made concrete for a reader. NOTE: the site is a
       JavaScript app and did not return static content on fetch, so cite it as the
       authors' companion artifact (named in the paper) and use the paper's Fig. 1 for any
       reproduced image, not a live scrape.
Crop:  Retain the image, the wrong given label, and the corrected label together; a crop
       that drops either label loses the point.
```

```text
Asset: A year-by-year top-5 error series (2010–2015) is a candidate for the single chart or
       small table the commission allows, built from the Numbers section above.
Shows: The fall from 28.2% to 3.57% crossing the ~5.1% human line and approaching the ~6%
       label-error floor — the saturation-against-noise point in one view.
Crop:  If drawn as a chart, mark the ~5.1% human line and the ~6% label-error band; label
       the axis as top-5 error and name the winning model per year. (Furniture note: the
       commission says a table OR a figure earns its place only if it changes
       understanding — do not stack both.)
```

## Discarded

```text
URL: https://arxiv.org/abs/2101.05022 (Yun et al., "Re-labeling ImageNet") — a third
     relabeling effort; real and on-topic, but Beyer and Northcutt already cover the
     multi-label and error-rate points the commission names, and adding it risks
     over-weighting the critique side. Held in reserve, not read in full.
URL: https://labelerrors.com — could not be read as a static page (JS app returned no
     content on fetch); recorded above via the Northcutt paper's own reference to it
     rather than cited as a page I opened.
URL: syncedreview.com / scmp.com / ibtimes.co.uk / forbes (Baidu Minwa) coverage —
     redundant secondary reporting of the same 2015 race already covered by the MIT
     Technology Review piece; two retellings of one origin count as one.
URL: en.wikipedia.org/wiki/AlexNet and assorted Medium summaries — used only to locate the
     primaries; not cited, since every figure was taken from the owning paper.
```

---

Note for the writer on non-overlap with the library (checked via `nb history`):

- **the-instruments/glue** teaches that a *language* benchmark's "human level" (87.1 on
  GLUE) was a hurried estimate from untrained crowd workers (Nangia & Bowman 2019), that
  the score is an unweighted average of nine tasks in four metric units, that a model can
  pass the average while sitting at chance on one task (WNLI), and that the tasks carry
  annotation-artifact shortcuts. Its one-line finding: "The line they crossed was a hurried
  crowd estimate, measured on tasks that leak their own answers." This lesson's primary
  finding is different in kind: a flawed single-label *key* (label noise plus the
  multi-object mismatch) scored against, with the human baseline a *secondary* crack told
  in ImageNet's own terms — one trained expert (Karpathy) over many hours, not a crowd
  estimate. Require a Background link to GLUE and lead with the labels, per the commission,
  so the two lessons do not re-argue the same "human baseline was thin" motif.

- The library already touches ImageNet elsewhere; link, do not re-teach: **the-evidence/
  alexnet** and **canon-papers/alexnet** (the 2012 result and paper), **ai-foundations/
  generalization** (Recht et al.'s fresh ImageNet test set, ResNet-152 78.3%→67.0% top-1,
  distribution shift — note this lesson already used ResNet-152's 78.3% top-1 and the
  11-point drop, and taught top-1 accuracy in passing), **the-instruments/fid** (uses an
  ImageNet-trained network), **the-evidence/batch-normalization** (defines ImageNet as the
  1,000-category, ~1.28M-image set), and **when-ai-breaks/google-photos-gorilla** (ImageNet
  geographic skew). The metric terms top-1/top-5 are not the explicit subject of any prior
  lesson, so this lesson owns defining them; generalization mentioned top-1 accuracy but
  did not define top-5.
