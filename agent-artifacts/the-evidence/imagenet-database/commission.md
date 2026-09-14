# Commission: the-evidence/imagenet-database

## Assignment

Read the document that introduced ImageNet: Deng, Dong, Socher, Li, Li, and
Fei-Fei, "ImageNet: A Large-Scale Hierarchical Image Database," CVPR 2009. The
lesson teaches what that paper actually built and claimed, at honest scale, and
separates it from the thing "ImageNet" now stands in for in arguments about deep
learning.

Template: lesson. Series: The Evidence (reads one famous AI document per
lesson). Reader: the paper's declared reader, smart and widely read, new to this
subject. Publication date: 2026-09-14.

## The angle

People cite "ImageNet" to settle the argument that data, not just algorithms,
drove the deep learning era. The 2009 paper is not that story. It is a database
paper: a taxonomy borrowed from WordNet, images gathered from web search, and
labels bought from Amazon Mechanical Turk workers, with a quality-control scheme
to make crowd labels trustworthy. The famous accuracy jump people mean by
"ImageNet" came in 2012 (AlexNet on the ILSVRC subset), three years and a
separate competition later. Teach what the 2009 document contains, at its real
scale, then show plainly where today's shorthand diverges from it.

## What to teach (short, complete)

1. What the 2009 paper actually delivered: a hierarchy of concepts drawn from
   WordNet, populated with web images and human-verified labels. Give the real
   figures the paper reports for the database at publication and its intended
   full scale, and the labeling method and its verification step. Distinguish
   the database (2009) from ILSVRC, the annual competition on a 1,000-category
   subset that started in 2010.
2. How crowd labels were made reliable: the sampling/agreement procedure the
   paper describes for accepting a label, and what accuracy it claimed for the
   result. This is the paper's real methodological contribution and the reader
   should see it.
3. The gap between document and shorthand: the 2012 result people attribute to
   "ImageNet" is AlexNet on the ILSVRC-2012 subset, a later and separate thing.
   Say plainly what the 2009 paper did and did not show, and what later work
   (the competition, and the label-quality and dataset-bias audits) confirmed or
   corrected about it.

Keep the list to these. If the label-bias critique cannot be taught at real
depth within the band, state it briefly and cite it rather than padding.

## Boundaries and dedupe

- Do not re-teach the AlexNet architecture: `the-evidence/alexnet` owns it. Link
  it where the 2012 result enters; treat it as taught ground.
- Do not teach top-5 accuracy as a metric from scratch: `the-instruments/
  imagenet-top-5-accuracy` owns that. Link at first use.
- This is a database/document lesson, not a benchmark-metric lesson and not a
  model lesson. Its distinct value is the honest scale of the 2009 artifact and
  the document-vs-shorthand correction.

## Neighbors in tonight's edition

Tonight also runs `the-instruments/clipscore` (an image-text metric). Both touch
vision; they do not overlap in job. No cross-link is required unless the
evidence naturally supplies one.

## Sources

Floor: at least 6 sources, at least 3 primary, at least 1 secondary. Every
source URL must resolve. The controlling primary is the 2009 CVPR paper itself;
read it and take every figure from it, not from coverage. Additional primaries
available: the ILSVRC paper (Russakovsky et al., 2015, IJCV) for the competition
and its scale; the WordNet reference for the taxonomy; later primary audits of
label quality or dataset bias. Secondary reporting may supply context on how
"ImageNet" is invoked today. Contested or widely-misquoted figures need a
primary.

## Production policy (balanced profile; none required)

Actual assignments for this run:
- researcher: effort high, model claude-opus-4-8
- writing-coach: effort low, model claude-sonnet-4-5
- writer: effort medium, model claude-opus-4-8
- editor: effort high, model claude-opus-4-8

## Recent shapes to break (do not inherit)

Recent The Evidence openers lead with named authors plus a surprising verb
(Kingma and Welling made random sampling differentiable) and deks that pair a
specific number with a reversal (matches a transformer twice its size, and loses
to a far smaller one). Both are house habits now. Find this piece's own opening
and dek build. Vary heading construction from the recent run; do not join two
clauses with a comma and "and."
