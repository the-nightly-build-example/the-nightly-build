# Evidence: the-evidence/imagenet-database (01)

The evidence firmly supports the commission's core factual claims. The 2009 CVPR
paper is a database paper: it builds a hierarchy on WordNet, fills it with images
from web search, and verifies labels with Amazon Mechanical Turk workers under a
per-category voting scheme. Every headline figure for the 2009 artifact is taken
from that paper directly: 12 subtrees, 5,247 synsets, 3.2 million images, an
average of over 600 images per synset, and 99.7% labeling precision on 80 sampled
synsets. The competition people usually mean by "ImageNet," and the 2012 accuracy
result, are documented by two separate later primaries (the 2015 ILSVRC paper and
the 2012 AlexNet paper), which confirm the commission's claim that the famous jump
was a later, separate thing. Two later primary audits (a 2020 bias audit by the
dataset's own creators, and a 2021 label-error audit) give the "what later work
corrected" material.

The evidence is thin in one place that matters, and it complicates the angle in
two. It is thin on the popular construction figures the reader will have seen
(49,000 workers, 167 countries, 160 million candidate images): those are not in
the 2009 paper and reach us only through secondary retrospectives, so they cannot
be attributed to the document. The angle is complicated by two findings recorded
under Contradictions: the 2009 paper already argues, with its own experiments,
that more and cleaner data improves recognition, so the "data mattered" thesis is
seeded in the document rather than absent from it; and the 2021 label-error figure
is measured on the ILSVRC-2012 validation set, a different and later construct
from the 2009 presence-verification the 99.7% number describes, so it corrects the
popular assumption of pristine labels without refuting the 2009 measurement.

## Sources

```text
URL:         https://www.image-net.org/static_files/papers/imagenet_cvpr09.pdf
Kind:        primary, and controlling. Jia Deng, Wei Dong, Richard Socher,
             Li-Jia Li, Kai Li, and Li Fei-Fei (Dept. of Computer Science,
             Princeton University), "ImageNet: A Large-Scale Hierarchical Image
             Database," CVPR 2009, pp. 248-255. This is the document the lesson
             reads. It owns every claim about what ImageNet was and did in 2009.
Establishes: What the 2009 database contained and at what scale; the WordNet
             backbone and the synset unit; the web-search candidate collection;
             the Amazon Mechanical Turk verification scheme and its dynamic
             per-category voting threshold; the 99.7% precision claim; the
             projected full scale; three demonstration experiments. It says
             nothing about deep learning, ILSVRC, AlexNet, or top-5 accuracy;
             those words do not appear.
Paraphrase:  ImageNet is built on the hierarchical structure of WordNet, where
             each concept is a "synset." At the time of writing it holds 12
             subtrees (mammal, bird, fish, reptile, amphibian, vehicle,
             furniture, musical instrument, geological formation, tool, flower,
             fruit) with 5,247 synsets and 3.2 million images, averaging over 600
             images per synset, and it aims eventually for roughly 50 million
             images over about 50,000 synsets. Candidate images are collected by
             querying image search engines with WordNet synonyms (queries also
             expanded with parent terms and translated into Chinese, Spanish,
             Dutch, and Italian); raw search accuracy is around 10%, so each
             synset starts with over 10,000 candidates. Humans on AMT then verify
             whether each candidate image contains the target concept. Because
             users disagree, an image is kept only on a convincing majority, and
             a simple algorithm sets how many agreeing votes a category needs: for
             each synset an initial sampled subset is voted on by at least 10
             users to build a confidence-score table, and remaining candidates are
             labeled until a per-category confidence threshold is reached.
Locators:    Abstract; Sec. 1 (synset definition, "around 80,000 noun synsets");
             Sec. 2 "Scale"/"Accuracy" and Fig. 2 (subtree table); Fig. 4 (99.7%
             precision); Sec. 3.1 (candidate collection, 10% search accuracy,
             >10K candidates, query languages); Sec. 3.2 and Fig. 7 (AMT
             verification, majority vote, >=10 users on initial subset,
             confidence table); Sec. 5.1 (~50M images/~50K synsets goal, "~10% of
             the WordNet synsets").
Quote:       "This paper offers a detailed analysis of ImageNet in its current
             state: 12 subtrees with 5247 synsets and 3.2 million images in
             total." (Abstract)
             "An image is considered positive only if it gets a convincing
             majority of the votes... we first randomly sample an initial subset
             of images. At least 10 users are asked to vote on each of these
             images. We then obtain a confidence score table... we proceed with
             the AMT user labeling until a pre-determined confidence score
             threshold is reached." (Sec. 3.2)
```

```text
URL:         https://arxiv.org/abs/1409.0575
Kind:        primary, for the competition. Olga Russakovsky and Jia Deng (equal
             first authors), Hao Su, Jonathan Krause, Sanjeev Satheesh, Sean Ma,
             Zhiheng Huang, Andrej Karpathy, Aditya Khosla, Michael Bernstein,
             Alexander C. Berg, and Li Fei-Fei, "ImageNet Large Scale Visual
             Recognition Challenge," International Journal of Computer Vision,
             2015 (DOI 10.1007/s11263-015-0816-y). It owns the facts about ILSVRC:
             the creators describe the challenge firsthand.
Establishes: That ILSVRC is a separate, later thing from the 2009 database: an
             annual competition run since 2010 on a 1,000-category subset, and
             that 2012 was the paper's own named "turning point" when a deep CNN
             (the SuperVision team, Krizhevsky et al.) won.
Paraphrase:  The challenge has run annually from 2010. The classification task
             uses 1,000 object classes with roughly 1.2 million training images.
             For ILSVRC2012-2014 the split is 1,281,167 training, 50,000
             validation, and 100,000 test images. The 2012 competition was "a
             turning point," when the SuperVision team's deep convolutional
             network won both classification and localization; its influence
             dominated 2013 and 2014 entries.
Locators:    Abstract; Sec. 1 (annual since 2010); Sec. 3.1 and Table 2 (1,000
             classes; 1,281,167 / 50,000 / 100,000 for 2012-14); Sec. 5.1,
             "ILSVRC2012" (turning point, SuperVision/Krizhevsky).
Quote:       "We see a turning point in 2012 with the development of large-scale
             convolutional neural networks." (Sec. 5.1)
```

```text
URL:         https://proceedings.neurips.cc/paper_files/paper/2012/hash/c399862d3b9d6b76c8436e924a68c45b-Abstract.html
Kind:        primary, for the 2012 result. Alex Krizhevsky, Ilya Sutskever, and
             Geoffrey E. Hinton (University of Toronto), "ImageNet Classification
             with Deep Convolutional Neural Networks," NIPS 2012. It owns the
             accuracy figure people attribute to "ImageNet."
Establishes: The exact figure the popular shorthand points at, and that it is a
             2012 ILSVRC result on the 1,000-class subset, not a 2009 database
             measurement. (Cited here only for the figure; the architecture is
             taught by the-evidence/alexnet.)
Paraphrase:  The network was trained on the 1.2 million high-resolution ImageNet
             LSVRC-2010 images across 1,000 classes. Entered in the ILSVRC-2012
             competition, it achieved a winning top-5 test error rate of 15.3%,
             against 26.2% for the second-best entry.
Locators:    Abstract; Sec. 1 and Sec. 6 (ILSVRC-2012 results).
Quote:       "We also entered a variant of this model in the ILSVRC-2012
             competition and achieved a winning top-5 test error rate of 15.3%,
             compared to 26.2% achieved by the second-best entry." (Abstract)
```

```text
URL:         https://wordnet.princeton.edu/
Kind:        primary, for the taxonomy. Princeton University's WordNet project
             ("About WordNet"; the reference work is Christiane Fellbaum, ed.,
             WordNet: An Electronic Lexical Database, MIT Press, 1998, which the
             2009 paper cites as [9]). It owns the definition of a synset and the
             structure ImageNet borrowed.
Establishes: What a synset is and what the "IS-A" hierarchy is, independent of the
             ImageNet paper's summary of it.
Paraphrase:  WordNet is a large lexical database of English. Nouns, verbs,
             adjectives, and adverbs are grouped into sets of cognitive synonyms
             ("synsets"), each expressing a distinct concept, and synsets are
             interlinked by conceptual-semantic and lexical relations. The most
             frequent relation among synsets is the super-subordinate relation
             (hypernymy/hyponymy, the "IS-A" relation), which links a general
             synset such as {furniture} to more specific ones such as {bed} and
             {bunkbed}; all noun hierarchies rise to the root node {entity}.
             WordNet contains 117,000 synsets across all parts of speech; the 2009
             ImageNet paper works from its roughly 80,000 noun synsets.
Locators:    "About WordNet" section (definition; 117,000 synsets); "The most
             frequently encoded relation..." (super-subordinate / IS-A, root
             {entity}).
Quote:       "Nouns, verbs, adjectives and adverbs are grouped into sets of
             cognitive synonyms (synsets), each expressing a distinct concept.
             Synsets are interlinked by means of conceptual-semantic and lexical
             relations."
Access note: The live page returns HTTP 403 to automated agents (Cloudflare
             human-check gating, not a dead link); it resolves normally in a
             browser. Content above was read from the Internet Archive capture of
             this same page dated 2019-12-24
             (https://web.archive.org/web/20191224064921/https://wordnet.princeton.edu/).
             The recorded URL is the source's own page.
```

```text
URL:         https://arxiv.org/abs/1912.07726
Kind:        primary, a dataset-bias audit by the dataset's own creators. Kaiyu
             Yang, Klint Qinami (Princeton), Li Fei-Fei (Stanford), Jia Deng, and
             Olga Russakovsky (Princeton), "Towards Fairer Datasets: Filtering and
             Balancing the Distribution of the People Subtree in the ImageNet
             Hierarchy," FAccT 2020 (DOI 10.1145/3351095.3375709). It owns its
             own audit findings firsthand.
Establishes: A concrete, quantified problem later found in ImageNet's construction
             that the 2009 paper did not anticipate: because ImageNet tried to
             illustrate every WordNet noun synset with images, the person subtree
             imported WordNet's offensive and non-visual categories.
Paraphrase:  The full ImageNet person subtree holds 2,832 people categories,
             about 8.3% of all images. The authors identify 1,593 of these as
             potentially offensive labels that should not be used. Of the
             remaining 1,239, they find only 158 are visual (can be inferred from
             appearance), and recommend filtering the subtree down to those 158.
             The named root causes are WordNet's stagnant concept vocabulary, the
             attempt to illustrate every category with images, and unequal
             representation within concepts.
Locators:    Abstract; Sec. 1 (2,832 categories, ~8.3% of images; 1,593 offensive;
             1,239 remaining; 158 visual); Sec. 4.2 ("out of 2,832 synsets... we
             have identified 1,593 unsafe synsets. The remaining 1,239 synsets are
             temporarily deemed safe").
Quote:       "out of 2,832 synsets within the person subtree, we have identified
             1,593 unsafe synsets."
```

```text
URL:         https://arxiv.org/abs/2103.14749
Kind:        primary, a label-quality audit. Curtis G. Northcutt (MIT / ChipBrain
             / Cleanlab), Anish Athalye (MIT / Cleanlab), and Jonas Mueller (AWS),
             "Pervasive Label Errors in Test Sets Destabilize Machine Learning
             Benchmarks," NeurIPS Datasets and Benchmarks 2021. It owns its
             error-rate measurement firsthand.
Establishes: That the labels in the ILSVRC-2012 subset people benchmark on are not
             error-free, correcting the popular assumption of pristine ImageNet
             labels. Note the measured object is the ILSVRC-2012 validation set,
             not the 2009 12-subtree database, and single-label errors are a
             different construct from the 2009 presence-verification precision.
Paraphrase:  Across 10 widely used test sets the authors estimate an average of at
             least 3.3% label errors, and for the ImageNet validation set at least
             6%. Candidate errors were flagged by confident-learning algorithms
             and then human-checked; on average 51% of flagged candidates were
             confirmed as genuinely mislabeled.
Locators:    Abstract (average >=3.3%; ImageNet >=6%; 51% confirmed).
Quote:       "we estimate an average of at least 3.3% errors across the 10
             datasets, where for example label errors comprise at least 6% of the
             ImageNet validation set."
```

```text
URL:         https://en.wikipedia.org/wiki/ImageNet
Kind:        secondary, for how "ImageNet" is invoked today. A tertiary/secondary
             encyclopedia entry reporting on ImageNet from outside the authoring
             team. Used only for context on the popular framing and for figures it
             attributes to others; not used for any primary figure.
Establishes: That the popular story credits ImageNet (via the 2012 AlexNet result)
             with catalyzing the deep learning boom, and that widely repeated
             construction figures (worker and candidate-image counts) circulate
             through secondary coverage rather than the 2009 paper.
Paraphrase:  The article dates the original paper to CVPR 2009 and frames the 2012
             AlexNet result (top-5 error 15.3%) on the ILSVRC challenge as the
             moment industry attention shifted, quoting The Economist: "Suddenly
             people started to pay attention, not just within the AI community but
             across the technology industry as a whole." It states the eventual
             full ImageNet (ImageNet-21K) holds 14,197,122 images across 21,841
             categories, and relays construction figures it attributes to
             secondary sources: about 49,000 Mechanical Turk workers from 167
             countries filtering over 160 million candidate images between July
             2008 and April 2010, each of the 14 million images labeled three
             times. These construction figures are not in the 2009 paper.
Locators:    Lead and "History"/"Significance" sections; "Dataset" section
             (14,197,122 images / 21,841 categories); construction-figures
             sentence with its citations.
Quote:       "Suddenly people started to pay attention, not just within the AI
             community but across the technology industry as a whole." (The
             Economist, as quoted by the article)
```

## Contradictions

- **The 2009 paper is not silent on the "data mattered" thesis; it argues it.**
  The commission frames the document as "not that story" (the story that data,
  not just algorithms, drove deep learning). That is right about deep learning and
  about the famous 2012 jump. It is too strong about the thesis itself. Section 4
  of the 2009 paper runs experiments showing that cleaning the labels improves
  nearest-neighbor recognition and that more images per category improves it
  further ("NN-voting + clean ImageNet" beats noisy; "NBNN" with full-resolution
  images beats both; enlarging the dataset "can be significantly improved by
  enlarging the dataset"). The paper explicitly proposes ImageNet as "a training
  resource" and "a benchmark dataset." So the data-centric argument is seeded in
  the document; what arrived in 2012 was the deep-learning method that exploited
  data at that scale, not the idea that data helps. The lesson should separate
  "the paper made no data argument" (false) from "the paper did not show the 2012
  accuracy jump" (true).

- **The 99.7% (2009) and the ~6% error (2021) measure different objects.** The
  99.7% precision is a presence-verification measurement on 80 synsets sampled
  across the mammal and vehicle subtrees of the 2009 database, verified by an
  independent group of subjects (Deng 2009, Fig. 4). The ~6% figure is a
  single-label error rate on the ILSVRC-2012 validation set (Northcutt 2021), a
  later 1,000-class subset with one label per image, where multi-object images and
  fine-grained confusions drive much of the error. The later audit corrects the
  popular belief that ImageNet labels are pristine; it does not directly refute
  the 2009 number, and the writer must not present it as "the 99.7% was wrong."

- **The projected full scale was not reached as projected.** The 2009 paper's goal
  was roughly 50 million images over about 50,000 synsets "in the next two years"
  (Sec. 5.1). The database as it actually became (ImageNet-21K) is about 14.2
  million images over 21,841 synsets (relayed by the Wikipedia entry from
  image-net.org statistics; not a 2009 figure). The document's stated ambition and
  the eventual artifact diverge, and the difference is worth stating plainly.

- **The famous worker figures are not in the document.** "49,000 workers," "167
  countries," "160 million candidate images," and "July 2008 to April 2010" appear
  throughout popular coverage and in the Wikipedia entry, attributed to later
  retrospectives. The 2009 paper gives no worker count and no total-candidate
  count; its only crowd-size figure is "at least 10 users" voting on each image of
  a per-synset initial sample (Sec. 3.2). Any worker or country figure must be
  attributed to the secondary retrospective, never to the 2009 document.

## Numbers

```text
Figure: 12 subtrees; 5,247 synsets; 3.2 million images
Owner:  Deng et al. 2009 (Abstract; Sec. 2)
Scope:  ImageNet at the time the CVPR 2009 paper was written; the 12 named
        subtrees only, not the full projected database.
```

```text
Figure: average of over 600 images per synset (target 500-1000 per synset)
Owner:  Deng et al. 2009 (Sec. 2 "Scale"; Sec. 1)
Scope:  Current (2009) 12-subtree database; target is the stated design goal.
```

```text
Figure: 99.7% average labeling precision
Owner:  Deng et al. 2009 (Fig. 4)
Scope:  80 synsets randomly sampled across tree depths of the mammal and vehicle
        subtrees; correctness of each image verified by an independent group of
        subjects. A presence-verification precision, not a single-label accuracy.
```

```text
Figure: at least 10 users vote per image on the initial sampled subset; image
        kept only on a convincing majority; per-synset confidence threshold
Owner:  Deng et al. 2009 (Sec. 3.2, Fig. 7)
Scope:  The AMT quality-control procedure; the vote count needed varies by
        category difficulty (e.g., "Burmese cat" needs more agreement than "cat").
```

```text
Figure: ~10% raw image-search accuracy; over 10,000 candidate images per synset
        after intra-synset duplicate removal
Owner:  Deng et al. 2009 (Sec. 3.1)
Scope:  Candidate-collection stage, before human verification.
```

```text
Figure: ~80,000 noun synsets in WordNet (paper); 117,000 synsets total in WordNet
Owner:  Deng et al. 2009 (Sec. 1) for the 80,000 nouns; WordNet/Princeton for
        the 117,000 total (all parts of speech).
Scope:  80,000 is noun synsets, the space ImageNet draws from; 117,000 is all
        parts of speech in the WordNet release described.
```

```text
Figure: projected ~50 million images over ~50,000 synsets; current build ~10% of
        WordNet synsets
Owner:  Deng et al. 2009 (Sec. 5.1; Sec. 2)
Scope:  Stated completion goal "in the next two years," not an achieved figure.
```

```text
Figure: ILSVRC classification subset: 1,000 categories; ILSVRC2012-14 split
        1,281,167 train / 50,000 validation / 100,000 test images; run annually
        since 2010
Owner:  Russakovsky et al. 2015 (Table 2; Sec. 3.1; Sec. 1)
Scope:  The competition subset and its splits, distinct from the 2009 database.
```

```text
Figure: AlexNet ILSVRC-2012 winning top-5 test error 15.3%, vs 26.2% second-best
Owner:  Krizhevsky, Sutskever, Hinton 2012 (Abstract)
Scope:  ILSVRC-2012 classification test set, 1,000-class subset. This is the
        figure the popular "ImageNet" shorthand points at.
```

```text
Figure: person subtree: 2,832 categories (~8.3% of images); 1,593 flagged unsafe;
        1,239 remaining, of which only 158 visual
Owner:  Yang et al. 2020 (Abstract; Sec. 1; Sec. 4.2)
Scope:  The person subtree of the full ImageNet hierarchy, audited in 2019-2020.
```

```text
Figure: >=6% label errors in ImageNet validation set; >=3.3% average across 10
        test sets; 51% of algorithmically flagged candidates confirmed erroneous
Owner:  Northcutt, Athalye, Mueller 2021 (Abstract)
Scope:  ILSVRC-2012 validation set (single-label), not the 2009 database.
```

```text
Figure: eventual full ImageNet (ImageNet-21K): 14,197,122 images; 21,841 categories
Owner:  image-net.org statistics, relayed by the Wikipedia entry (secondary)
Scope:  The database as it grew after 2009; not a figure from the 2009 paper, and
        short of the paper's own ~50M/~50K projection.
```

## Source assets

```text
Asset: Deng et al. 2009, Figure 2 (page 2): red histogram of number of images per
       synset, beside a table summarizing selected subtrees (Mammal 1,170 synsets
       / 862K images; Vehicle 520 / 317K; Bird 872 / 705K; Furniture 197 / 157K;
       GeoForm 176 / 77K; MusicInstr 164 / 110K).
Shows: The real, uneven scale of the 2009 database: over half of synsets exceed
       500 images while about 20% have very few. It lets the reader see the
       foundation's true size rather than the "3.2 million" headline alone.
Crop:  Keep the subtree table's synset and image counts legible; the histogram
       axis labels ("# images per synset", percentage) must survive any crop.
```

```text
Asset: Deng et al. 2009, Figure 7 (page 5): the "Burmese cat" example. Left, six
       sampled users giving conflicting yes/no answers on the same images; right,
       the confidence-score table contrasting "Cat" and "Burmese cat" (e.g., 2
       yes / 0 no gives confidence 0.97 for cat but 0.83 for Burmese cat).
Shows: The paper's actual methodological contribution: how disagreement is turned
       into a per-category vote threshold. This is the single best visual for
       teaching how crowd labels were made trustworthy.
Crop:  Retain both the user-vote panel and the confidence table together; the
       contrast between the two categories is the point and neither half stands
       alone.
```

```text
Asset: Deng et al. 2009, Figure 4 (page 3): precision plotted against tree depth
       (1 through 9), with the 99.7% average annotated.
Shows: That the accuracy claim is measured across depth levels, and that deeper
       (more fine-grained) synsets are the hard case the voting scheme has to hold
       precision on.
Crop:  Keep the y-axis precision scale (0.9-1.0) and the depth axis; omitting the
       scale would overstate how flat the curve is.
```

```text
Asset: Russakovsky et al. 2015, Table 2 (top): image-classification dataset size
       by year (ILSVRC2010 1,261,406 train; ILSVRC2011 1,229,413; ILSVRC2012-14
       1,281,167; each with 50,000 validation).
Shows: The competition subset's scale and its stability across the years, making
       concrete that "ImageNet" the benchmark is a fixed 1,000-class slice, not
       the full 2009 database.
Crop:  Keep the year rows and the train/val/test columns; the per-class ranges in
       parentheses can be dropped without losing the point.
```

```text
Asset: Yang et al. 2020, Table 1 (person-subtree filtering summary).
Shows: The quantified scale of the person-subtree problem (unsafe vs. remaining vs.
       visual categories) in one view.
Crop:  Retain the category counts; the paper deliberately obscures the offensive
       synset names, and any use must preserve that omission.
```

## Discarded

```text
URL: https://qz.com/1034972/the-data-that-transformed-ai-research-and-possibly-the-world (Dave Gershgorn, Quartz, 2017): the canonical popular retrospective and the origin of the "49,000 workers / 167 countries" figures, but the live page and its Internet Archive captures render the article body only through client-side JavaScript, so the passages could not be read. Not cited. The same framing and figures are available, attributed, through the Wikipedia entry that is cited above.
```

```text
URL: https://viso.ai/deep-learning/imagenet/ : secondary explainer that repeats the 3.2-million and 99.7% figures already owned by the 2009 primary; adds no interpretation, so not cited.
```

```text
URL: https://www.sfu.ca/~kabhishe/posts/posts/summary_cvpr_imagenet_2009/ : a personal blog summary of the 2009 paper; a retelling of the primary, not an independent source, so not cited.
```

```text
URL: https://www.semanticscholar.org/paper/ImageNet:-A-large-scale-hierarchical-image-database-Deng-Dong/... : indexing/landing page for the 2009 paper, useful only to locate the PDF, which is cited directly.
```
