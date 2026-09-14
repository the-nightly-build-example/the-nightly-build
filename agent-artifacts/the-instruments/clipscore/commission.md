# Commission: the-instruments/clipscore

## Assignment

Teach CLIPScore: the automatic metric that grades how well an image matches a
text description by the cosine similarity CLIP assigns them. One measurement,
explained where it comes from, what it can and cannot support, and at least one
real case where it misled people and what that cost.

Template: lesson. Series: The Instruments (one public measurement per lesson).
Reader: smart, widely read, new to this subject. Publication date: 2026-09-14.

## The angle

CLIPScore is the reference-free number a lot of text-to-image work reports for
"prompt alignment." Its whole trust rests on CLIP: the score is only as good as
CLIP's own judgment of image-text fit. Teach the pipeline step by step (CLIP's
paired image and text encoders, cosine similarity, the rescaling in the original
CLIPScore paper), then show the specific failures that follow from grading with
a model rather than a rule: it inherits CLIP's blind spots, it is largely
insensitive to word order and attribute binding (so it cannot tell "a red cube
on a blue sphere" from the swap), and optimizing against it rewards CLIP's
preferences rather than human ones. Land at least one concrete case where a
system or paper looked good on CLIPScore while failing what it claimed to
measure, and what that error cost (misranked systems, or a follow-up metric
built to replace it).

## What to teach (short, complete)

1. Where the number comes from: what CLIP is (a model trained to pull matching
   image-text pairs together in one shared space) and how CLIPScore turns its
   cosine similarity into a 0-to-100-ish score. Give the exact construction from
   Hessel et al. (2021).
2. What it can support: a fast, reference-free, human-correlated check for
   gross image-caption fit, and why that made it standard. Give the reported
   correlation figures from the original paper.
3. Where it breaks and the real cost: insensitivity to composition/word order
   (tie to the attribute-binding problem, taught), inheritance of CLIP's biases,
   and the reward-hacking failure when CLIPScore is used as a training or
   selection objective. Anchor with a concrete measured case and the metric
   (VQAScore/TIFA-style faithfulness checks, PickScore, or a documented
   misranking) that was built in response.

## Boundaries and dedupe

- CLIP the model is taught in `the-evidence/clip`; link it, do not re-derive
  contrastive pretraining from scratch.
- Do not re-teach FID or Inception Score: `the-instruments/fid` and
  `the-instruments/inception-score` own image-realism metrics. CLIPScore grades
  image-text alignment, a different axis; name the distinction once and move on.
- Attribute binding as a model behavior is `the-mechanics/attribute-binding`;
  link it when composition-insensitivity enters.

## Neighbors in tonight's edition

`the-evidence/imagenet-database` also touches vision, in a different job
(dataset document, not metric). No forced cross-link.

## Sources

Floor: at least 8 sources, at least 4 primary, at least 1 secondary. URLs must
resolve. Primaries: Hessel et al., "CLIPScore" (2021); Radford et al., "Learning
Transferable Visual Models From Natural Language Supervision" (CLIP, 2021); at
least two primaries documenting a failure or a replacement metric (e.g. TIFA,
VQAScore, DALL-Eval, PickScore, or a compositional-benchmark paper). Read each
and cite the passage that supports the specific claim. Contested figures need a
primary.

## Production policy (balanced profile; none required)

- researcher: effort high, model claude-opus-4-8
- writing-coach: effort low, model claude-sonnet-4-5
- writer: effort medium, model claude-opus-4-8
- editor: effort high, model claude-opus-4-8

## Recent shapes to break (do not inherit)

The Instruments has leaned on the "a high X can hide Y" title mold (F1 hiding a
missed class) and on deks that expose a gamed number (a score that came from the
public set). The metric-misleads finding is the series' job, but find a title
and dek build this piece owns rather than reusing those molds. Vary heading
construction; avoid the comma-plus-"and" two-clause heading.
