# researcher brief: the-evidence/latent-diffusion (01)

Inputs:
- editorial-direction.md (citation standard, The Evidence territory, declared reader)

Output: researcher/01/evidence.md

Source floor (from nb source-policy --series the-evidence): at least 6 sources,
at least 3 primary and at least 1 secondary. Exceed it where a source changes the
interpretation.

Research questions to answer from primary documents:

1. The paper's claim and method. From Rombach et al. 2022 (arXiv 2112.10752 /
   CVPR): what problem it names with pixel-space diffusion, the latent-space move
   (autoencoder + diffusion in latent space + decode), the compression/
   downsampling factors studied (f=4,8,16...), and the cross-attention
   conditioning. Read the method and experiments sections, not the abstract only.
2. The scale and the numbers. Exact training/sampling cost claims (GPU-days,
   speedups) and the headline FID/other scores on the datasets used (e.g.,
   LSUN, ImageNet, COCO text-to-image), with the dataset sizes. Record each
   figure with the primary that owns it, its denominator, and its scope.
3. The release. The August 2022 Stable Diffusion weight release (CompVis /
   Stability AI / Runway): what was released, the training set (LAION-2B/
   LAION-5B subsets, aesthetics filtering), and the model size. Distinguish the
   paper (CompVis academic) from the product (Stable Diffusion).
4. How it holds up / usage vs findings. Later primary work that kept latent
   diffusion (SDXL paper, SD3/rectified-flow if relevant) and the documented
   problems that followed the dataset and release: the LAION copyright disputes
   and the Stanford Internet Observatory finding of CSAM in LAION-5B (Dec 2023),
   with the primary report. Where do people cite this paper for more than it
   showed?

Hunt for what breaks the framing: e.g., whether the cost reduction is as clean as
the headline, whether latent diffusion trades away any quality vs pixel-space
diffusion, and disputes over LAION. Record contradictions in full.

The reader already met the diffusion mechanism (denoising-diffusion), attention,
and CLIP in this library; note where a Background link would replace re-teaching,
but do not browse the archive for background beyond confirming those lessons exist
by slug (the-evidence/denoising-diffusion, the-mechanics/attention or
the-evidence/attention-is-all-you-need, the-evidence/clip).
