# Commission: the-evidence/latent-diffusion

## The document

"High-Resolution Image Synthesis with Latent Diffusion Models," Robin Rombach,
Andreas Blattmann, Dominik Lorenz, Patrick Esser, and Björn Ommer (CompVis,
LMU Munich), CVPR 2022. This is the paper whose method became Stable Diffusion
when CompVis, Stability AI, and Runway released trained weights in August 2022.
Teach the document itself, not the product that followed, though the release is
the reason the document is famous.

## What the lesson teaches

One idea, completely: diffusion image generation was too expensive to train or
run at high resolution because it denoised in pixel space, and this paper moved
the whole process into the compressed latent space of an autoencoder, cutting
the cost enough to put image generation on a single consumer GPU. Teach:

1. What the paper inherited. Diffusion models generate an image by starting from
   noise and removing a little at a time over many steps. Our reader met this in
   the denoising-diffusion lesson; link it, do not re-teach it. The cost problem:
   every denoising step ran over every pixel, so training took hundreds of GPU-
   days and sampling was slow.
2. The move the paper made. Train an autoencoder to compress an image into a
   small latent grid and back, then run the diffusion process in that latent
   space, and decode once at the end. Give the real compression factor and what
   it bought (the paper reports training and sampling cost reductions; get the
   exact figures).
3. How text gets in. Cross-attention on the denoiser conditions generation on a
   text embedding, which is how a prompt steers the picture. Keep this brief and
   concrete; the reader met attention already (link it).
4. The scale honestly. Training data (LAION subsets), model size, compute, and
   the benchmark numbers (FID on standard sets). Show how much, not "a lot."

Then bring it to the present: the August 2022 weight release and why open
weights mattered, what latent diffusion enabled and what broke (the LAION
dataset and the copyright and CSAM findings that followed), and what later work
kept or changed (latent diffusion is now standard; SDXL, SD3, and video models
build on it). Say plainly where the paper's claims still hold and where usage
outran them.

## Distinct value, and boundaries

The course covers denoising-diffusion (the DDPM mechanism), gans, clip, and
vision-transformer. None covers latent diffusion, the specific move that made
open image generation cheap. This lesson owns that move. Link denoising-diffusion
for the diffusion mechanism and attention/clip where the reader needs them,
rather than re-teaching. Do not retell the DDPM lesson; start from it.

## Source obligations

Series floor, from `nb source-policy --series the-evidence`: at least 6 sources,
with at least 3 primary and at least 1 secondary. Primary here is the Rombach et
al. paper (arXiv/CVPR), the CompVis/Stability weight-release materials, the LAION
dataset documentation, and any later primary (SDXL paper). The FID numbers and
cost figures are contested-prone; take each from the primary that owns it.

## Production policy

From `nb production-policy --series the-evidence` (profile: balanced). Models are
the "capable" tier (not a required pin); this run resolves "capable" to
claude-opus-4-8, matching the paper's published record. Efforts: writing-coach
low, researcher high, writer medium, editor high. Harness: claude-code. Record
the writer's actual served model in nb-meta.

## Recent patterns to break (for writer and editor)

Habits visible across the recent library; keep the required content but do not
inherit these shapes:

1. Dek: recent deks lean on a two-clause explanatory mold, a claim joined to its
   twist by "and/so/but/while" ("...and the $5.6 million price tag belongs to a
   different model"). Also the comma-triad and the "The [thing] that..." opener.
   Build this dek another way.
2. Closing body heading: recent pieces end on a terse verdict-of-limits heading
   ("A high GAIA score licenses less than the headline says," "Where the number
   keeps its word"). Keep the present/limits content; do not stamp its heading to
   that mold.
3. Avoid "The line the paper drew itself" as a heading (chain-of-thought used it).
4. The orientation heading is its own concrete step, not a paraphrase of the
   headline.
5. Furniture: nb-note and nb-stat-strip recur by reflex. Use only what the
   material calls for. A cost or FID comparison may genuinely want a table or a
   small stat strip; earn it.

## Original contribution target

The lesson should leave the reader able to explain why Stable Diffusion could run
on a gaming GPU when earlier diffusion models needed a cluster, and able to
separate what the paper proved from what the public release set loose.
