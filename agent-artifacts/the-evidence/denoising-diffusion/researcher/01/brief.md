# researcher brief: the-evidence/denoising-diffusion (01)

Inputs:
- editorial-direction.md (this article's standing directions: house standard,
  slop standard, citation rule, the reader, and The Evidence series prompt)
- this brief

Output: researcher/01/evidence.md

## Subject
Jonathan Ho, Ajay Jain, Pieter Abbeel, "Denoising Diffusion Probabilistic
Models," UC Berkeley, June 2020 (NeurIPS 2020), arXiv:2006.11239. This is the
document the lesson teaches. Read the paper itself first, in full, including the
algorithm boxes and the experiments section.

## Questions the evidence record must answer
1. What the document is: exact authors, affiliation, venue, date. Why it became
   the reference point for diffusion image generation.
2. The method, precisely enough for a lesson to teach it: the forward process
   (adding Gaussian noise over T steps), the reverse process (a U-Net trained to
   predict the noise added), and the simplified training objective the paper
   settled on (predicting the noise term). What each piece does in plain terms.
3. The exact numbers: number of diffusion steps T; the datasets used and their
   image resolutions and sizes; the reported quality scores (CIFAR-10 Inception
   Score and FID, and any 256x256 results). Give each figure with its owner and
   scope.
4. The honest scale and limits of the 2020 result: pixel space (not latent), the
   image sizes actually generated, unconditional / class-conditional (no text
   prompts), and sampling cost (~1000 sequential network evaluations).
5. What came before: Sohl-Dickstein et al. 2015 (the original diffusion idea)
   and score-based models (Song & Ermon 2019). State what DDPM added over these,
   in the paper's own framing.
6. What came after, for the present-day section: latent diffusion / Stable
   Diffusion (Rombach et al. 2022), classifier-free guidance (Ho & Salimans
   2022), fast samplers (DDIM, Song et al. 2021), and text-to-image systems
   (DALL-E 2, Imagen). For each, one precise line on the specific capability it
   added that DDPM itself did not have. This is how the article separates the
   2020 paper from today's "diffusion model."
7. Contradictions / what breaks the angle: was DDPM actually first? What does the
   paper itself credit to prior work? Record this fully so the editor can test
   the "founding document" framing.

## Source policy for this article
At least 6 sources; at least 3 primary and at least 1 secondary. The DDPM paper,
its predecessors, and the later papers are all primaries (authorship-and-stake
test). Classify each and say why. Secondary reporting is acceptable for context
on the products.

## Source assets
Name any exact visual from the DDPM paper that could carry an argument better
than prose (e.g. an algorithm box, the forward/reverse schematic, a sample grid
with its reported score), following the evidence-record asset shape. Do not
prescribe crop coordinates.

## Focus / risk
The article's whole value is the line between what the 2020 paper measured and
what later papers added. Verify the "did not do" claims (no text conditioning, no
latent space, slow sampling) against the paper directly, not against later
summaries that fold everything into "diffusion models."
