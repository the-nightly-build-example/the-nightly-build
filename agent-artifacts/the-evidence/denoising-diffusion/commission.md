# Commission: the-evidence/denoising-diffusion

## Assignment
Read the founding document of modern diffusion image generators: Jonathan Ho,
Ajay Jain, and Pieter Abbeel, "Denoising Diffusion Probabilistic Models" (UC
Berkeley, June 2020; NeurIPS 2020; arXiv:2006.11239). One lesson, one document.

The reader keeps hearing "diffusion model" as the thing behind Stable Diffusion,
DALL-E, Midjourney, and Sora. This lesson teaches what the 2020 paper actually
introduced, then separates that from everything later papers added before the
technology reached those products.

## Why this document, why now
The library already teaches image generation as a mechanic (the-mechanics/
image-generation) and the earlier generative approach (the-evidence/gans), but
never the primary paper the whole area rests on. Naming what DDPM did and did
not do closes the biggest gap under a class of products the reader meets daily,
and gives later lessons on latent diffusion, guidance, and text conditioning
something to build on.

## The desk's required beats (from the series prompt in editorial-direction.md)
- State what the document is, who wrote it, why it became famous.
- Walk what it actually did: the forward noising process, the reverse network
  trained to predict the noise, the training objective, the datasets, the
  numbers (image sizes, sampling steps, the reported FID/Inception scores).
- Show the scale honestly: pixel space, small unconditional or class-conditional
  images, ~1000 sequential sampling steps, the specific datasets and their size.
- Bring it to the present: what later work added on top (latent space, text
  conditioning, guidance, fast samplers) and what the 2020 paper itself did NOT
  do. Where today's "diffusion model" usage does not match what this paper
  showed, say so plainly.

## Boundaries
- Do not re-teach how an image generator denoises step by step, or GANs. Both
  are published lessons; link them in Background at first use, never as numbered
  sources, and never cover them as new (see press/editorial.md in the direction).
- One document is the subject. Later papers (score matching, DDIM, latent
  diffusion, classifier-free guidance, text-to-image systems) are context for
  the present-day section and for honest attribution of what DDPM did not do.
  They are not co-subjects.
- This is a teaching desk with no opinion column: verdicts are welcome only when
  earned from the cited evidence.

## Required contribution (the original work the writer must name)
The article does something the sources do not: it draws the exact line between
what the 2020 DDPM paper measured and what the reader's mental image of "a
diffusion model" (text-to-image, fast, photorealistic) actually owes to later
work. A reader who has heard "diffusion" a hundred times should finish able to
say which one idea is Ho et al.'s and which capabilities arrived afterward.

## Neighbors in tonight's edition (keep this piece distinct)
- the-instruments/simpleqa (a factuality benchmark) — no overlap; different desk.
- the-mechanics/random-numbers, what-could-go-wrong/ai-moral-status,
  when-ai-breaks/mcdonalds-ai-drivethru — no overlap.
No shared claims, figures, or framings with any of these.

## Template and policy
- Template: lesson (word band 1200-2200).
- Source policy: at least 6 sources; at least 3 primary, at least 1 secondary.
  The DDPM paper and the later papers it is measured against are primaries; the
  test is authorship and stake, not document type.
- Production policy (profile balanced): researcher effort high / model capable;
  writer effort medium / model capable; editor effort high / model capable;
  writing-coach effort low / model capable. No stage carries a required model or
  effort directive, so no directive is being traded down. Actual runtime models:
  researcher, writer, editor on a capable model (Claude Opus); writing-coach on a
  capable model (Claude Sonnet). Efforts as above.

## Candidate Background links (writer decides; link, do not re-teach)
the-mechanics/image-generation (the denoising process, taught from scratch);
the-evidence/gans (the generative approach diffusion displaced).
