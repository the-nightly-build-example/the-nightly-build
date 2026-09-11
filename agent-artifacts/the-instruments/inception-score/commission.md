# Commission: the-instruments/inception-score

## The measurement

The Inception Score (IS), the number that for several years stood in for "this
generator makes better images." Introduced by Tim Salimans, Ian Goodfellow, and
colleagues in "Improved Techniques for Training GANs" (2016), it scores a set of
generated images using a pretrained Inception v3 ImageNet classifier, with no
reference to real images at all.

## What the lesson teaches

How the number is made, step by step, then what it can and cannot support, with
at least one real case where it misled people.

1. Where the number comes from. Run each generated image through an Inception
   classifier trained on ImageNet. IS rewards two things at once: each image
   should be confidently classified as one thing (sharp, recognizable), and the
   set as a whole should spread across many classes (diverse). State the
   construction plainly, defining the one probability idea it needs (the gap
   between the label distribution for a single image and the average label
   distribution over all images). The reader holds probability already; do not
   re-teach it.
2. What a number built that way can support, and what it cannot. It never looks
   at a single real image, so it cannot tell you the generated images resemble
   the target distribution; it is blind to within-class diversity and to
   memorizing the training set; and the score depends on the exact classifier and
   preprocessing. Give the real case: Barratt and Sharma (2018) showed a model
   optimized directly against the Inception network reaches a near-maximal score
   while producing nothing meaningful, and IS cannot see mode collapse. This is
   why FID replaced it (the reader has the FID lesson; link it).
3. What it cost. Years of GAN papers ranked progress on a number that could be
   gamed and could not detect the failure GAN researchers most cared about
   (mode collapse). Be concrete about how it was reported and compared.

## Distinct value, and boundaries

The course covers fid (the successor metric) and gans and image generation.
None teaches the Inception Score itself: its construction, its specific failure
modes, and why it was retired. This lesson owns that. The FID lesson is the
natural Background link and the contrast, but do not retell FID; this is the
number that came before it and why it fell.

## Source obligations

Series floor, from `nb source-policy --series the-instruments`: at least 8
sources, at least 4 primary and at least 1 secondary. Primary: Salimans et al.
2016 (the paper that introduced IS), Barratt & Sharma 2018 ("A Note on the
Inception Score"), the FID paper (Heusel et al. 2017) for the replacement claim,
and further primary critiques of IS. Take every figure from its owning primary.

## Production policy

From `nb production-policy --series the-instruments` (profile: balanced). Models
are the "capable" tier (not required); this run resolves "capable" to
claude-opus-4-8. Efforts: writing-coach low, researcher high, writer medium,
editor high. Harness: claude-code. Record the writer's actual model in nb-meta.

## Recent patterns to break (for writer and editor)

1. Dek: avoid the two-clause "claim, and/so the twist" explanatory mold, the
   comma-triad, and the "The [number] that..." opener that recent instruments
   deks reached for.
2. The Instruments desk in particular keeps closing on a verdict-of-limits
   heading ("A high GAIA score licenses less than the headline says," "What a
   utilization number cannot see," "Where the number keeps its word"). Keep the
   "what it cannot support" content the beat requires, but do not build the
   closing heading to that stamp.
3. Orientation heading is its own step, not a paraphrase of the headline.
4. Furniture: nb-note, nb-stat-strip, and nb-table recur by reflex. A metric with
   an equation may genuinely want an nb-math block; a before/after comparison may
   want a table. Earn each.

## Original contribution target

The reader should finish able to say exactly what a high Inception Score does and
does not prove about a generator, and able to recognize the general trap of a
single distributional score standing in for image quality.
