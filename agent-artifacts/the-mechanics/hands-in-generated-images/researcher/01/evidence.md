# Evidence: the-mechanics/hands-in-generated-images (01)

The evidence supports the full causal chain the commission draws, with one honest
seam. Steps 1 and 2 rest on the diffusion primaries: DDPM and the latent-diffusion
paper describe a model trained by a denoising reconstruction objective, with no term
in the objective that models anatomy, parts, or finger count. That the objective
"rewards local texture and global coherence" is a fair reading of what the trained
model does, not a phrase the primaries use, so it is framing built on the objective
they state. Step 3 is the best-grounded link on the hand-specific side: three
independent hand papers (HandRefiner, HanDiffuser, FoundHand) and the model builder
itself (a Stability AI spokesperson) name the same two causes firsthand: hands
occupy few pixels in the frame, and they are highly articulated and appear in a wide
range of poses, occlusions, and grips. The one claim that stays soft is the last
half-step: that the model "interpolates to something hand-shaped and plausible,
which lands on the wrong finger count often." No primary I found measures a base-rate
of malformed hands, and no primary states the interpolation mechanism in those words.
The prevalence is attested only qualitatively and by the existence of a whole
subfield of fixes. Step 4 (open, not solved; a moving target improved by scale,
data, and hand-specific pose or mesh guidance) is well supported by the dates and
methods of that same subfield.

## Sources

```text
URL:         https://arxiv.org/abs/2006.11239
Kind:        primary. Ho, Jain, and Abbeel own the DDPM training objective they define.
Establishes: What a diffusion model is trained to do. The model is trained on a
             weighted variational bound connected to denoising score matching; in
             practice it learns to predict the noise added to an image at each step.
             The objective is stated over reconstruction of the noised signal. There
             is no term in it for object parts, anatomy, counting, or semantics.
Paraphrase:  A diffusion model generates by starting from noise and removing it step
             by step. Its training target is a denoising reconstruction bound, not
             any structural or semantic supervision. The absence of an anatomy or
             counting term is read from the objective as stated, an argument the
             primary makes by construction rather than by asserting the negative.
Locators:    Abstract; objective definition (the paper's L_simple noise-prediction loss).
Quote:       "Our best results are obtained by training on a weighted variational
             bound designed according to a novel connection between diffusion
             probabilistic models and denoising score matching with Langevin
             dynamics."
```

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. Rombach and coauthors own the latent-diffusion method that
             Stable Diffusion, the model the hand papers test against, is built on.
Establishes: That the same denoising objective runs in the latent space of a
             pretrained autoencoder, with text or other conditioning added through
             cross-attention. Confirms the generator in question is a denoising model
             with no explicit parts or counting stage. Names the base model the
             hand-failure evidence is measured on.
Paraphrase:  Stable Diffusion decomposes image generation into a sequence of
             denoising steps run in a compressed latent space, conditioned on text by
             cross-attention. Nothing in the described formulation models hand
             structure or finger count.
Locators:    Abstract; method (latent-space denoising, cross-attention conditioning).
Quote:       "By decomposing the image formation process into a sequential
             application of denoising autoencoders, diffusion models (DMs) achieve
             state-of-the-art synthesis results on image data and beyond."
```

```text
URL:         https://arxiv.org/abs/2311.17957
Kind:        primary. Lu, Xu, Zhang, Wang, and Tao own the diagnosis and the
             measurements in HandRefiner (ar5iv full text at
             https://ar5iv.labs.arxiv.org/html/2311.17957).
Establishes: The strongest firsthand statement of why hands are hard, with numbers.
             The paper attributes malformed hands to the difficulty of learning hand
             structure and pose from training images "which involves extensive
             deformations and occlusions." It states a hand kinematic model has 16
             joints and 27 degrees of freedom, that finger-finger occlusions occur
             when a 3D hand projects to 2D, and that hand generation "has little
             tolerance for error." It measures its own fix: image-level FID on HAGRID
             77.60 to 74.12, hand-level FID on FreiHAND 158.34 to 147.52, and in a
             survey of 100 malformed generated images, 97 depth maps still recovered
             the correct five-finger topology.
Paraphrase:  Hands are hard because the model must infer a 16-joint, 27-degree-of-
             freedom articulated 3D object from 2D training images full of occlusion,
             and small errors read as wrong. HandRefiner does not fix generation
             itself; it inpaints the hand region afterward using a hand-mesh model and
             ControlNet, and improves FID and keypoint confidence when it does.
Locators:    Abstract; Introduction, Section 1 (joints, DOF, occlusion); Section 4.2
             User Study (97 of 100 depth maps); Tables 1 and 2 (FID).
Quote:       "A kinematic model of hand contains 16 joints and 27 degrees of freedom."
             "This difficulty arises from the complex task of learning the physical
             structure and pose of hands from training images, which involves
             extensive deformations and occlusions."
```

```text
URL:         https://arxiv.org/abs/2403.01693
Kind:        primary. Narasimhaswamy and coauthors (CVPR 2024) own the diagnosis and
             the user study in HanDiffuser (full text at
             https://arxiv.org/html/2403.01693v1).
Establishes: A second independent firsthand account of the cause, and numbers on how
             often the base model reads as wrong to people. The paper states hands
             "often take up a small part of the image, but are highly articulate,"
             with "high degrees of freedom" and fingers that "bend to various degrees
             relatively independently," plus diverse shapes, orientations, occlusion,
             and hand-object interaction. Its user study rated Stable Diffusion hands
             "Good or better" for plausibility only 27% of the time, against 55% for
             its own method; hand-region FID (FID-Hand) 31.219 for fine-tuned Stable
             Diffusion against 27.550 for HanDiffuser.
Paraphrase:  Hands are small in the frame yet carry many independent degrees of
             freedom, so the base model gets them plausible-looking only a minority of
             the time by human judgment. The fix injects explicit 3D hand parameters
             (SMPL body, MANO hand) into generation.
Locators:    Abstract; Introduction (small part of the image, highly articulate);
             experiments (user study percentages, FID and FID-Hand).
Quote:       "hands often take up a small part of the image, but are highly
             articulate. They have high degrees of freedom, with a wide variety of
             flexibility where fingers can bend to various degrees relatively
             independently."
```

```text
URL:         https://arxiv.org/abs/2412.02690
Kind:        primary. Chen and coauthors (CVPR 2025) own the FoundHand diagnosis and
             dataset (full text at https://arxiv.org/html/2412.02690v1).
Establishes: The cleanest firsthand statement of the two-part cause the commission's
             step 3 needs, in one sentence: hands are under-sampled in training data
             because they occupy very few pixels or their complex articulations go
             uncaptured. Confirms the problem persists across major systems, and that
             the current fix is scale plus a dedicated representation: FoundHand-10M,
             a 10-million-image hand dataset with 2D keypoints and masks.
Paraphrase:  Both halves of "hands are the worst case" trace to one primary sentence:
             hands are small (few pixels) and high-variance (articulations not
             captured), so the learned distribution over hand pixels is thin. FoundHand
             answers it with data scale and a keypoint representation, evidence the
             problem is being pushed back by data rather than declared solved.
Locators:    Introduction (few pixels / articulations not captured; models
             consistently struggle); dataset description (FoundHand-10M, 10M images).
Quote:       "hands are not well-sampled in these datasets - they either occupy very
             few pixels, or complex articulations are not captured."
```

```text
URL:         https://arxiv.org/abs/2312.04236
Kind:        primary. Zhang, Qin, Liu, and Campbell (Australian National University)
             own the detection-and-restoration pipeline (full text at
             https://ar5iv.labs.arxiv.org/html/2312.04236).
Establishes: That malformed hands in Stable Diffusion output are common enough to
             build a detector and a repair model around, and corroborates the failure
             as real and recurring. It defines the target as "non-standard hands" and
             builds its data by redrawing hand regions in 30,000 HAGRID images with
             Stable Diffusion, then manually keeping the malformed ones (9,623 training
             pairs). It does not report a prevalence rate.
Paraphrase:  A third independent group treats malformed Stable Diffusion hands as a
             standing problem worth a dedicated detector, but like the others it does
             not measure how often hands come out wrong. It supports "the failure is
             real and frequent," not "the failure rate is X."
Locators:    Abstract and method (definition of non-standard hands; 30,000 HAGRID
             redraws; 9,623 pairs).
Quote:       "Stable Diffusion occasionally generates images with atypical hands,
             defined as non-standard hands."
```

```text
URL:         https://www.buzzfeednews.com/article/pranavdixit/ai-generated-art-hands-fingers-messed-up
Kind:        secondary. BuzzFeed News reporting by Pranav Dixit, January 31, 2023.
             Its value is that it carries a first-party statement: the closest thing to
             the model builder's own explanation, quoted directly.
Establishes: The model builder's own account. A Stability AI spokesperson states that
             in AI datasets human images "display hands less visibly than they do
             faces" and that hands "tend to be much smaller in the source images, as
             they are relatively rarely visible in large form." An AI-and-arts
             professor, Amelia Winger-Bearskin, adds that the system learns statistical
             appearance, not anatomy: it is "just looking at how hands are represented
             in the images that it has been trained on." Treat the Stability AI line as
             a firsthand claim about the training data, reported here at one remove.
Paraphrase:  Stable Diffusion's maker attributes the failure to hands being small and
             infrequently prominent in training images. A named outside expert frames
             the model as learning appearance statistics rather than structure. The
             professor's point is expert opinion, not a measurement.
Locators:    Body, Stability AI spokesperson statement; body, Winger-Bearskin quotes.
Quote:       "within AI datasets, human images display hands less visibly than they do
             faces. Hands also tend to be much smaller in the source images, as they
             are relatively rarely visible in large form."
```

```text
URL:         https://www.britannica.com/topic/Why-does-AI-art-screw-up-hands-and-fingers-2230501
Kind:        secondary. Britannica explainer by Meg Matthias, synthesizing existing
             expert commentary (it cites the same BuzzFeed interview and New Yorker
             coverage). No original reporting.
Establishes: That the two-cause account (training data shows hands less than faces;
             the model learns 2D appearance across poses, not 3D anatomy) is the
             settled popular-explanation consensus, useful only as a marker of what the
             general reader has likely already been told.
Paraphrase:  A reference-work restatement of the training-data and no-3D-understanding
             explanation. It repeats the Stability AI line rather than adding
             independent evidence, so it supports "this is the accepted explanation,"
             not the explanation's truth.
Locators:    Body (two reasons: data prominence; 2D appearance across varied poses).
Quote:       "within AI datasets, human images display hands less visibly than they do
             faces" (quoting the Stability AI spokesperson).
```

## Contradictions

- **Two emphases for step 3, both from primaries.** The model builder and Britannica
  frame the cause as training-data scarcity (hands shown less than faces, smaller in
  frame). FoundHand and HanDiffuser frame it as distributional diffuseness (few pixels
  plus high, independent articulation). These are complementary, not opposed, but they
  are distinct claims, and the commission's step 3 leans on the second. Both are cited
  so the writer can hold them apart rather than blur them into one cause.

- **"No counting / no anatomy step" is a framing, not a measured finding.** The
  diffusion primaries establish the objective and what it optimizes; they do not
  assert "there is no anatomy step" as a result. That the objective contains no such
  term is true by reading its definition, but it is an argument from the construction
  of the objective, not an experiment. Steelman: one could argue a large enough model
  implicitly learns an anatomy prior from data, which is exactly what scale-and-data
  fixes like FoundHand exploit. The honest line is that no explicit anatomy or counting
  computation exists, while an implicit statistical one is learned imperfectly.

- **Scale is closing the gap, which cuts against calling this a hard limit.** The fix
  papers run 2023 to 2025 and report real gains from more and better hand data
  (FoundHand-10M) and explicit pose or mesh guidance (HandRefiner, HanDiffuser). That
  the failure recedes with data and dedicated representation is itself evidence the
  cause is statistical coverage, not an in-principle barrier. This supports step 4's
  "moving target," and it warns against writing the failure as permanent or as proof
  the model "cannot" do hands.

- **No measured base-rate anywhere in the read set.** The commission's "lands on the
  wrong finger count often" is not backed by a prevalence figure from any primary.
  HandRefiner's "97 of 100" is the inverse measurement (how often a correct topology
  is still recoverable from malformed images), not how often hands are malformed. The
  frequency is attested only by qualitative statements and by the existence of the
  fix subfield. Flagged again under the record's limitation.

## Numbers

```text
Figure: 16 joints and 27 degrees of freedom (per hand kinematic model)
Owner:  ElKoura and Singh 2003, "Handrix: animating the human hand." HandRefiner
        (arxiv 2311.17957) repeats it with that citation, so HandRefiner is a
        retelling, not the owner. Cite the figure to ElKoura and Singh if the article
        leans on it, or attribute it as "the count HandRefiner cites."
Scope:  A biomechanical model of a single human hand.
```

```text
Figure: Stable Diffusion hands rated "Good or better" for plausibility 27% of the time
Owner:  HanDiffuser (arxiv 2403.01693), user study.
Scope:  Human raters on a 5-point plausibility scale; HanDiffuser scored 55% on the
        same scale. Judgment data, not an anatomical error count.
```

```text
Figure: FID-Hand 31.219 (fine-tuned Stable Diffusion) vs 27.550 (HanDiffuser)
Owner:  HanDiffuser (arxiv 2403.01693), experiments.
Scope:  Frechet Inception Distance on hand regions; lower is closer to real. A quality
        distance, not a finger-count rate.
```

```text
Figure: FID 77.60 -> 74.12 (HAGRID, image level); 158.34 -> 147.52 (FreiHAND, hand level)
Owner:  HandRefiner (arxiv 2311.17957), Tables 1 and 2.
Scope:  Before and after HandRefiner's inpainting fix; measures the fix's effect, not
        the base failure frequency.
```

```text
Figure: 97 of 100 malformed survey images yielded a correct five-finger topology depth map
Owner:  HandRefiner (arxiv 2311.17957), Section 4.2 User Study.
Scope:  Of 100 images already selected as malformed, a hand-mesh reconstruction still
        recovered five-finger structure in 97. This measures the fix's foothold, not
        how often generation fails. Do not read it as a 97% correct-hand rate.
```

```text
Figure: FoundHand-10M, 10 million hand images with 2D keypoints and masks
Owner:  FoundHand (arxiv 2412.02690).
Scope:  Training dataset size for the dedicated hand model; evidence of the scale of
        data being thrown at the problem.
```

## Source assets

```text
Asset: HandRefiner (arxiv 2311.17957), teaser figure in Section 1 showing malformed
       generated hands beside the same images after refinement.
Shows: The failure and its correction side by side: extra or fused fingers in the raw
       Stable Diffusion output, resolved after inpainting. The clearest single visual
       of what "wrong hands" means.
Crop:  Keep a raw malformed hand at readable size; a before/after pair carries more
       than either alone. It is a paper figure, so usage and licensing are the
       writer's and editor's call, and the caption must credit the source.
```

```text
Asset: HanDiffuser (arxiv 2403.01693), qualitative comparison grid of Stable Diffusion
       vs HanDiffuser on the same prompts.
Shows: Independent examples of the same failure modes (finger count, fused fingers,
       implausible orientation) from a second group, useful if the article wants a
       source other than HandRefiner.
Crop:  A single Stable Diffusion failure cell is enough; retain the finger region.
       Same licensing caveat.
```

```text
Asset: FoundHand (arxiv 2412.02690), examples of malformed hands from popular models.
Shows: The failure across multiple named systems, supporting "this is general, not one
       model." Only needed if the article argues the point is not Stable-Diffusion-
       specific.
Crop:  Retain the hand; omit surrounding UI or model labels unless the article names
       the models. Same licensing caveat.
```

DDPM and the latent-diffusion paper carry sample galleries, but none is hand-specific,
so: None found that carries the hand argument better than prose.

## Discarded

```text
URL: https://www.alibaba.com/product-insights/why-do-ai-art-generators-still-struggle-with-hands-and-will-that-ever-truly-be-solved.html
     SEO product-insight page, no author or sourcing, commercial. Repeats the common
     explanation without owning any claim.
URL: (companion Alibaba product-insights variants on the same query) Same reason.
URL: https://futurism.com/the-byte/ai-awful-generating-pictures-human-hands
     Aggregation of the BuzzFeed interview; use the BuzzFeed original instead.
URL: https://dev.to/evanmarie/the-ai-hand-conundrum-why-generative-models-struggle-with-human-hands-21ib
     Personal blog, no primary standing; secondhand explanation.
URL: https://knowyourmeme.com/memes/ai-drawing-hands
     Meme catalog; documents the phenomenon culturally, adds no mechanism evidence.
URL: https://citizen.digital/article/the-curious-case-of-why-ai-is-so-bad-at-drawing-hands-n335349
     General-press retelling of the same two causes; superseded by the primaries.
URL: https://supreethn.github.io/research/handiffuser/index.html
     HanDiffuser project page. Read for numbers, carries none; the arxiv full text does.
URL: https://openaccess.thecvf.com/content/CVPR2024/papers/Narasimhaswamy_HanDiffuser_...pdf
     Same paper as arxiv 2403.01693, returned HTTP 403; read via the arxiv HTML instead.
URL: https://medium.com/@EleventhHourEnthusiast/denoising-diffusion-probabilistic-models-...
     Third-party DDPM explainer; the DDPM primary itself is the source used.
```
