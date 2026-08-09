# Commission: the-instruments/fid

## Authorized work

Scheduled run for 2026-08-09. `nb duty` returned `the-instruments` in open mode.
This slot replaces an earlier pick (`mmlu`) that collided with the already
published `the-instruments/mmlu`. One article; a genuinely unwritten measurement.

## The measurement

FID — the Fréchet Inception Distance (Martin Heusel et al., 2017, "GANs Trained by
a Two Time-Scale Update Rule Converge to a Local Nash Equilibrium," which
introduced it). This desk teaches how a public number is made and where it
misleads. FID is *the* number behind "state-of-the-art image generation": nearly
every GAN and diffusion paper reports it, and the reader meets "a new record FID
of X" claims constantly. The instruments desk has taken apart language and coding
benchmarks but has never measured an image-generation metric — a whole modality
missing from the reader's toolkit.

## What the lesson teaches (two or three ideas)

1. **How the number is built, step by step.** FID scores a set of generated images
   against a set of real ones. The procedure: run both sets through a fixed,
   pretrained image-recognition network (InceptionV3), read off the activations
   from one specific layer, treat each set's activations as a bell-curve cloud (a
   multivariate Gaussian summarized by a mean and a covariance), and compute the
   Fréchet distance between the two clouds. Lower means the generated cloud sits
   closer to the real one. Teach each step in plain words — the reader has met how
   models turn images into vectors on this desk (link it), so lean on that rather
   than re-teaching it.

2. **What the number can and cannot support.** FID measures distance in the
   features of an ImageNet classifier, so it sees what that network was trained to
   see and is blind to the rest. State plainly what a low FID does say (the
   generated set's statistics, through Inception's eyes, resemble the real set's)
   and what it does not (that any single image is good, or that quality improved
   in ways Inception ignores).

3. **At least one real case where the number misled, worked in full.** Choose the
   strongest documented failure and follow it through: options include the
   sample-size bias (FID is biased and shrinks with more samples, so two FIDs
   computed on different sample counts are not comparable — Chong & Forsyth 2020),
   the ImageNet lens (FID can be improved just by matching ImageNet class
   frequencies without better images — Kynkäänniemi et al. 2023), or resizing/
   implementation differences that make reported FIDs incomparable across papers
   and can flip rankings (Parmar et al. 2022, "Clean-FID"). Say what the confusion
   cost: incomparable leaderboard numbers, or a metric that moves without the
   images getting better.

The reader should finish able to read "SOTA FID of X" and ask the questions that
decide what it means: measured on which real set, with how many samples, through
whose resizing pipeline, and blind to what.

## Boundaries

- `the-evidence/gans` is published; do not re-teach what a GAN is. FID is the
  metric used to judge such models; link gans where useful.
- `the-mechanics/reading-images` is published (how a model turns an image into
  vectors); link it for the "Inception features" step rather than re-teaching
  image encoding.
- Do not teach diffusion models; FID is metric-agnostic to the generator.
- Claims about FID come from the papers that own each finding, read directly.

## Original contribution

Take the single number behind "best image generator" apart into its parts —
Inception features, two Gaussians, one distance — and show, worked in full, a
documented way it misleads (sample-size bias, the gameable ImageNet lens, or
resizing incomparability). The reader gets a metric they can interrogate the next
time a model is crowned on FID.

## Source policy (from `nb source-policy`)

Series and template agree: minimum 8 sources, primary ≥ 4, secondary ≥ 1.
Primaries: Heusel et al. 2017 (FID); Chong & Forsyth 2020 (sample-size bias);
Kynkäänniemi et al. 2023 (ImageNet-class manipulation); Parmar et al. 2022
(Clean-FID / resizing); optionally Salimans et al. 2016 (Inception Score, the
predecessor) and Kynkäänniemi et al. 2019 (precision/recall alternative). Give
every figure its denominator; contested figures resolve to the owning primary.

## Production policy (from `nb production-policy`, profile: balanced)

- writing-coach: capable (Sonnet), low effort
- researcher: capable (Opus), high effort
- writer: capable (Opus), medium effort
- editor: capable (Opus), high effort

None `required`; no deviation to record.

## This edition's neighbors

- `the-evidence/batch-normalization` (tonight) also involves an Inception network;
  keep distinct — FID is an evaluation metric, batch norm a training method — and
  cross-link at most. The other three lessons do not overlap.

## Recent habits not to inherit

- Instruments openers lean on "Every few months a lab announces…" and close the
  Why card on "By the end you can meet any … claim and say what it does and does
  not prove." Write the promise in FID's own terms, off that mold.
- The last two instruments pieces both hinged on "the score is confused for a
  harder skill." FID's shape is different: the anatomy of one number and the
  documented ways it lies. Keep that shape.
- Do not reuse "None of this makes the metric worthless"; write any fair-case beat
  fresh. Do not close on "read the claim precisely / now you know which one you
  are looking at." Vary any note label; do not default to "In plain language."

## Prior coverage to link, not re-teach

- `the-evidence/gans` — the generators FID judges.
- `the-mechanics/reading-images` — how a model turns an image into a vector.
- `the-instruments/bleu`, `the-instruments/perplexity` — earlier "one number that
  misleads" instruments, for the reader who wants the pattern (link, do not restage).
