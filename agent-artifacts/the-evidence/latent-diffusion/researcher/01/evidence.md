# Evidence: the-evidence/latent-diffusion (01)

The evidence strongly supports the commissioned angle: the Rombach et al. 2022 paper is a
method paper about moving diffusion out of pixel space into the latent space of a
pretrained autoencoder, and its reported gains are real but specific. The paper names the
cost problem (pixel-space diffusion takes "hundreds of GPU days"), describes the
two-stage fix (a once-trained autoencoder at downsampling factor f, then a diffusion UNet
in the latent space, with cross-attention for text and other conditioning), and reports
competitive-to-leading FID on LSUN, CelebA-HQ, FFHQ, class-conditional ImageNet, and
text-to-image MS-COCO. All of this is verifiable from the paper itself. The paper-versus-
product distinction holds cleanly and is the spine of the lesson: the academic LDM
text-to-image model was 1.45B parameters trained on LAION-400M, while the August 2022
Stable Diffusion product was a separate, larger training on LAION-2B/5B subsets with
aesthetic filtering, trained on 256 A100 GPUs, and it is the product's training set, not
the paper's experiments, that drew the copyright litigation and the Stanford CSAM finding.

The evidence is thin or needs care in three places. First, the paper's headline FID
figures were read from the arXiv text via the ar5iv HTML rendering because the CVPR
open-access PDF returned HTTP 403 (gated, not dead); the values match the paper's own
tables as rendered, but I could not cross-check each cell against the typeset PDF. Second,
the "efficiency" story is architectural and easy to overstate: the paper's own "hundreds
of GPU days" line is about pixel-space baselines, and the efficiency claim is relative,
not a statement that image diffusion became cheap. The product at scale still consumed
256 A100 GPUs. Third, the Getty copyright allegation is an accusation by one party, and
the one court to reach judgment (UK, Nov 2025) rejected the theory that the model weights
store or reproduce the training images. A lesson that treats the lawsuits as settled proof
of infringement would overreach the record.

CLIP has no published lesson in this library (nb history returns "No matching published
coverage" for a CLIP query), so the writer cannot Background-link CLIP and must define the
CLIP text encoder in-line where Stable Diffusion's conditioning is introduced. The
denoising-diffusion mechanism (slug `the-evidence/denoising-diffusion`), attention
(`the-evidence/attention-is-all-you-need`), and the GAN baseline (`the-evidence/gans`) do
exist and can be linked instead of re-taught.

## Sources

```text
URL:         https://arxiv.org/abs/2112.10752
Kind:        primary. Rombach, Blattmann, Lorenz, Esser, and Ommer own every method and
             result claim in it; it is the document the lesson teaches.
Establishes: The title "High-Resolution Image Synthesis with Latent Diffusion Models";
             authors Robin Rombach, Andreas Blattmann, Dominik Lorenz, Patrick Esser,
             Björn Ommer; submitted to arXiv 2021-12-20 (v1), revised 2022-04-13 (v2);
             published at CVPR 2022. The problem named, the two-stage method, the
             downsampling factors, the cross-attention conditioning, and the reported
             scores (read in full below from the paper body).
Paraphrase:  The paper decomposes image synthesis into a perceptual-compression stage (an
             autoencoder trained with a perceptual loss plus a patch-based adversarial
             objective, in either a KL-regularized or a VQ-regularized variant) and a
             generative stage (a time-conditional denoising UNet trained in the
             autoencoder's latent space). Conditioning on text, layout, or other inputs is
             done by a domain-specific encoder whose output enters the UNet through
             cross-attention layers.
Locators:    Abstract; Sec. 1 (Introduction); Sec. 3.1 (perceptual compression); Sec. 3.2
             (latent diffusion); Sec. 3.3 (conditioning / cross-attention); Sec. 4
             (experiments).
Quote:       "training the most powerful DMs often takes hundreds of GPU days (e.g. 150 -
             1000 V100 days ...)" (Sec. 1). "we need to train the universal autoencoding
             stage only once and can therefore reuse it for multiple DM trainings or to
             explore possibly completely different tasks" (Sec. 1).
```

```text
URL:         https://ar5iv.labs.arxiv.org/html/2112.10752
Kind:        primary (same paper). This is an HTML rendering of arXiv:2112.10752 used to
             read the method, the f-factor analysis, the tables, and the limitations
             section because the CVPR PDF was gated. The canonical address of the source
             is the arXiv abstract page above; this row records the transport actually
             read. Do not cite this URL in the article; cite the arXiv page.
Establishes: The downsampling factors studied, the optimal range, the text-to-image model
             size and training set, the scores, and the paper's own stated limitations.
Paraphrase:  The encoder downsamples by a factor f = H/h = W/w. The paper studies
             f in {1,2,4,8,16,32}; f=1 is pixel-space diffusion. It finds LDM-{4-16}
             "strike a good balance between efficiency and perceptually faithful results,"
             that overly large f causes "stagnating fidelity after comparably few training
             steps" from "too strong first stage compression resulting in information
             loss," and reports a roughly 38-point FID gap between pixel-based LDM-1 and
             LDM-8 after 2M steps. The text-to-image model is "a 1.45B parameter
             KL-regularized LDM conditioned on language prompts on LAION-400M" (Sec.
             4.3.1). The paper states LDMs' "sequential sampling process is still slower
             than that of GANs" and that their use "can be questionable when high precision
             is required" because autoencoder reconstruction "can become a bottleneck for
             tasks that require fine-grained accuracy in pixel space."
Locators:    Sec. 3.1; Sec. 4.1 (f-factor analysis, Fig. 6-7); Sec. 4.3.1 (text-to-image);
             Tables 1-3; Limitations paragraph (Sec. 5 / conclusion area).
Quote:       "their reconstruction capability can become a bottleneck for tasks that
             require fine-grained accuracy in pixel space"; "overly large values of f cause
             stagnating fidelity after comparably few training steps."
```

```text
URL:         https://huggingface.co/CompVis/stable-diffusion-v1-4
Kind:        primary. The model card authored by the model's developers (Robin Rombach,
             Patrick Esser). It owns the product's architecture, training data, and
             training procedure claims.
Establishes: That Stable Diffusion is a latent diffusion model, with a CLIP ViT-L/14 text
             encoder and downsampling factor 8; the LAION training subsets and the
             aesthetic/watermark filtering thresholds; the training hardware and steps;
             the CreativeML OpenRAIL-M license; the v1-1 to v1-4 lineage. This is the
             primary for distinguishing the product from the paper.
Paraphrase:  The model uses "a fixed, pretrained text encoder (CLIP ViT-L/14)" and encodes
             images at "a relative downsampling factor of 8." It was trained on subsets of
             LAION: "LAION-2B (en)," "laion-high-resolution" (170M examples from LAION-5B
             at resolution >=1024x1024), and "laion-improved-aesthetics" / "laion-aesthetics
             v2 5+," filtered to original size >=512x512, aesthetics score >5.0, and
             estimated watermark probability <0.5. v1-4 was trained on "32 x 8 x A100 GPUs"
             with 225,000 steps at 512x512, batch size 2048, and 10% text-conditioning
             dropout for classifier-free guidance. Stated model size "0.9B params."
Locators:    Model card sections: Model Details; Training (Training Data, Training
             Procedure); License.
Quote:       "a fixed, pretrained text encoder (CLIP ViT-L/14)"; training data filtered to
             "aesthetics score >5.0, and ... watermark probability <0.5."
```

```text
URL:         https://stability.ai/news-updates/stable-diffusion-public-release
Kind:        primary. Stability AI's own announcement of the public release. Owns the
             release event, the license framing, and the safety-classifier claim.
Establishes: The public release date of August 22 (2022); that weights (v1.4), code, and a
             model card were published via HuggingFace; the CreativeML OpenRAIL-M license;
             the inclusion of an AI-based safety classifier by default.
Paraphrase:  Stability AI announced the public release of Stable Diffusion, with model
             weights and code available on HuggingFace under the CreativeML OpenRAIL-M
             license, described as permitting commercial and non-commercial use. The
             package included a default AI-based safety classifier intended to remove
             undesired outputs. The page credits HuggingFace and CoreWeave for the release;
             the broader CompVis/LMU, Runway, EleutherAI, and LAION collaboration is
             documented in the model card and secondary coverage rather than this page.
Locators:    Announcement body; license paragraph; safety-classifier paragraph.
Quote:       "We have developed an AI-based Safety Classifier included by default in the
             overall software package."
```

```text
URL:         https://arxiv.org/abs/2307.01952
Kind:        primary. The SDXL paper by the Stability AI team. Owns the claim that the
             production line stayed on the latent-diffusion architecture.
Establishes: That SDXL is a latent diffusion model, released July 2023, with a roughly
             three-times-larger UNet and a second text encoder. Confirms the paper's method
             persisted into later products.
Paraphrase:  "SDXL: Improving Latent Diffusion Models for High-Resolution Image Synthesis,"
             Podell, English, Lacey, Blattmann, Dockhorn, Mueller, Penna, Rombach (Stability
             AI), arXiv 2307.01952, submitted 2023-07-04. The paper states "We present
             SDXL, a latent diffusion model for text-to-image synthesis," built on "a three
             times larger UNet backbone," with more attention blocks, a larger
             cross-attention context, and a second text encoder.
Locators:    Title; abstract; Sec. 2 (architecture / comparison to prior SD).
Quote:       "We present SDXL, a latent diffusion model for text-to-image synthesis."
```

```text
URL:         https://purl.stanford.edu/kh752sm9123
Kind:        primary. The Stanford Internet Observatory report. SIO performed the detection
             firsthand, validated by third parties, so it owns the CSAM finding. (PDF:
             https://stacks.stanford.edu/file/druid:kh752sm9123/ml_training_data_csam_report-2023-12-23.pdf)
Establishes: That known CSAM was present in the LAION-5B dataset that trained Stable
             Diffusion; the counts, the method, and the recommendation regarding SD 1.5.
Paraphrase:  David Thiel, Stanford Internet Observatory, "Identifying and Eliminating CSAM
             in Generative ML Training Data and Models," initial release 2023-12-20 (the
             read version is dated 2023-12-23). Using perceptual-hash (PhotoDNA), MD5
             cryptographic-hash, and k-nearest-neighbor embedding detection, the authors
             "identified 3,226 dataset entries of suspected CSAM, much of which was
             confirmed as CSAM by third parties" (NCMEC, the Canadian Centre for Child
             Protection, and Thorn's classifier). The report states the most popular
             resultant model, Stable Diffusion 1.5, "were ultimately trained on a wide
             array of content, both explicit and otherwise," and recommends that models
             based on SD 1.5 without safety measures "should be deprecated and distribution
             ceased where feasible." LAION took the 5B dataset down following the report.
Locators:    Title page; Sec. 1 (Introduction, 3,226 figure); Sec. 1.3 (Use by subsequent
             models); Sec. 4 (Summary of results); Sec. 5.1 (Removing material).
Quote:       "we identified 3,226 dataset entries of suspected CSAM, much of which was
             confirmed as CSAM by third parties." "Models based on Stable Diffusion 1.5
             that have not had safety measures applied to them should be deprecated and
             distribution ceased where feasible."
```

```text
URL:         https://copyrightalliance.org/wp-content/uploads/2023/02/Getty-Images-v.-Stability-AI-Complaint.pdf
Kind:        primary (legal document), but an accusation: it owns the fact that Getty made
             the claim, not that the claim is true. Getty is a party with a direct stake.
Establishes: The existence, forum, and content of Getty's US copyright action, and that it
             names LAION as the training-data source. Useful for the dispute's framing, not
             as proof of infringement.
Paraphrase:  "Getty Images (US), Inc. v. Stability AI, Inc.," filed in the US District
             Court for the District of Delaware (February 2023; the document's case number
             field is blank in this copy and the filing stamp is not in the extracted
             text). Getty alleges "Stability AI has copied more than 12 million photographs
             from Getty Images' collection, along with the associated captions and
             metadata, without permission," and that "Stable Diffusion was trained on 5
             billion image-text pairs from datasets prepared by non-party LAION." Claims
             arise under the Copyright Act of 1976, the Lanham Act, and DMCA Section 1202
             (copyright management information), plus Delaware trademark and unfair
             competition law.
Locators:    Caption (court, parties); Nature of Action paras. 1-3; LAION description
             (training-data paragraph); Section 1202 paragraphs.
Quote:       "Stability AI has copied more than 12 million photographs from Getty Images'
             collection ... without permission from or compensation."
```

```text
URL:         https://www.lw.com/en/insights/getty-images-v-stability-ai-english-high-court-rejects-secondary-copyright-claim
Kind:        secondary. A Latham & Watkins analysis reporting the UK High Court judgment.
             The primary is the judgment itself (Getty Images v Stability AI, England and
             Wales High Court, 4 November 2025, Mrs Justice Smith), which I did not open;
             this row records the reporting I read. Treat the ruling's holdings as attributed
             to this secondary until the judgment is read directly.
Establishes: That the one court to reach judgment rejected the core copying/storage theory.
             This is the evidence that most constrains the angle against overclaiming the
             lawsuits.
Paraphrase:  Per the analysis, at trial Getty dropped its primary copyright-infringement
             claim (web scraping and model training) and its database-right claim, having
             accepted there was no evidence the training occurred in the UK. The court
             rejected the remaining secondary-infringement claim, finding "the Model itself
             does not store any of those Copyright Works; the model weights are not
             themselves an infringing copy" (reported at judgment para. 600). The court
             found only limited, narrow trademark infringement tied to Getty watermarks
             appearing in some outputs, not widespread or continuing past SD v2.x.
Locators:    L&W insight body: claims abandoned; secondary-infringement holding; trademark
             holding.
Quote:       "the model weights are not themselves an infringing copy" (quoting judgment
             para. 600, as reported).
```

## Contradictions

- **The cost-reduction headline is relative, not absolute.** The paper's "hundreds of GPU
  days (150 - 1000 V100 days)" figure describes pixel-space baselines, and the efficiency
  claim is that latent diffusion needs less compute for comparable quality, plus a reusable
  autoencoder (arXiv:2112.10752, Sec. 1). It is not a claim that image diffusion became
  cheap in absolute terms. The product built on the method, Stable Diffusion v1-4, was
  trained on "32 x 8 x A100 GPUs" (256 A100s) per its model card. A lesson that presents
  the paper as making image generation cheap would misread the paper; present the gain as
  per-unit-quality and architectural.

- **Latent diffusion trades away pixel-level precision, by the authors' own admission.**
  The paper states reconstruction by the autoencoder "can become a bottleneck for tasks
  that require fine-grained accuracy in pixel space" and that sampling "is still slower than
  that of GANs" (arXiv:2112.10752, limitations). The method is not uniformly dominant over
  pixel-space diffusion; it is a favorable trade.

- **The lawsuits are not settled proof of infringement.** Getty's US complaint alleges
  more than 12 million images were copied via LAION (Delaware complaint). But the first
  court to reach judgment, the English High Court in November 2025, found the model weights
  do not store or reproduce the training images and rejected the secondary-infringement
  claim, after Getty had already dropped its primary copyright and database claims (Latham
  & Watkins analysis of the judgment). The honest framing is an unresolved and partly
  adverse legal record, not a vindicated accusation.

- **The paper is not the product, and the CSAM finding attaches to the product's data.**
  The academic text-to-image LDM was 1.45B parameters trained on LAION-400M
  (arXiv:2112.10752, Sec. 4.3.1). The Stanford CSAM finding concerns LAION-5B, the larger
  dataset used for Stable Diffusion, and SIO names Stable Diffusion 1.5 specifically
  (Thiel, 2023). Do not let the finding bleed onto the CVPR paper's own experiments, which
  used a different (though related) LAION subset.

## Numbers

```text
Figure: downsampling factors studied: f in {1, 2, 4, 8, 16, 32}
Owner:  arXiv:2112.10752, Sec. 3.1 / Sec. 4.1
Scope:  f=1 is pixel-space diffusion; LDM-{4-16} reported as the efficient/faithful range.
```

```text
Figure: ~38-point FID gap between pixel-based LDM-1 and LDM-8 after 2M training steps
Owner:  arXiv:2112.10752, Sec. 4.1 (Fig. 6-7 analysis)
Scope:  Same UNet budget comparison; illustrates the benefit of moving off pixel space.
```

```text
Figure: class-conditional ImageNet 256x256 FID 3.60, Inception Score 247.67 (LDM-4-G,
        classifier-free guidance s=1.5); LDM-4 without guidance FID 10.56, IS 103.49
Owner:  arXiv:2112.10752, Table 3
Scope:  ImageNet (1000 classes); headline class-conditional result; with vs without guidance.
```

```text
Figure: text-to-image MS-COCO 256x256 FID 12.63, IS 30.29 (LDM-KL-8-G, guidance s=1.5);
        LDM-KL-8 without guidance FID 23.31, IS 20.03
Owner:  arXiv:2112.10752, Table 2
Scope:  MS-COCO validation captions; the 1.45B-parameter model trained on LAION-400M.
```

```text
Figure: unconditional FID: CelebA-HQ 256 = 5.11; FFHQ 256 = 4.98; LSUN-Churches = 4.02;
        LSUN-Bedrooms = 2.95
Owner:  arXiv:2112.10752, Table 1
Scope:  Single-domain unconditional generation; lower FID is better.
Note:   Read via the ar5iv rendering; not cross-checked against the CVPR PDF (403 gated).
```

```text
Figure: academic text-to-image LDM = 1.45 billion parameters, trained on LAION-400M
Owner:  arXiv:2112.10752, Sec. 4.3.1
Scope:  The paper's own model, distinct from the later Stable Diffusion product.
```

```text
Figure: Stable Diffusion v1-4 trained on 32 x 8 = 256 A100 GPUs; 225,000 steps at 512x512,
        batch size 2048; text encoder CLIP ViT-L/14; downsampling factor 8; ~0.9B params
Owner:  CompVis/stable-diffusion-v1-4 model card (HuggingFace)
Scope:  The product, not the paper. Training-data filtering: original size >=512x512,
        aesthetics score >5.0, watermark probability <0.5.
```

```text
Figure: LAION-5B CSAM finding: 3,226 suspected entries; 1,679 PhotoDNA matches (746
        classified CSAM or possible CSAM by C3P among those still live); 495 MD5 matches
        (229 unique to that method); 78 of 432 Thorn high-probability candidates confirmed
Owner:  Thiel, Stanford Internet Observatory (2023), Sec. 4 (Summary of results)
Scope:  Evaluated 32,138,129 items above the chosen safety cutoff across the LAION datasets;
        ~30% of PhotoDNA-checked URLs were already offline. LAION-2B-en = 2.32B entries.
```

```text
Figure: Getty alleges "more than 12 million" Getty photographs copied; Stable Diffusion
        trained on "5 billion image-text pairs" from LAION
Owner:  Getty Images (US) v. Stability AI, US complaint (D. Del., Feb. 2023)
Scope:  Alleged figures in a complaint, not adjudicated facts. The UK court (Nov. 2025)
        rejected the copying/storage theory.
```

## Source assets

```text
Asset: arXiv:2112.10752, Figure 3 - the LDM architecture diagram (encoder E / decoder D
       around the pixel space, the diffusion/denoising UNet in latent space, and the
       conditioning path entering via cross-attention).
Shows: The entire method in one picture: where compression happens, where diffusion
       happens, and how text conditioning is injected. This is the figure a lesson teaching
       "diffusion moved into latent space" most needs.
Crop:  Must retain the E -> latent -> UNet -> D path and the cross-attention/conditioning
       block labelled with the domain encoder. Omit nothing that breaks the left-to-right
       flow; do not crop away the conditioning arm.
```

```text
Asset: arXiv:2112.10752, Figure 6/7 - FID (or sample quality) versus training steps across
       downsampling factors f.
Shows: Why f=1 (pixel space) and very large f both lose, and why LDM-{4-8} win: the
       empirical basis for the whole "sweet spot" claim. Carries the trade-off better than
       prose.
Crop:  Keep the axis labels (FID and training steps/throughput) and the curves for f=1, 8,
       and 16/32 so both failure modes are visible. A chart rebuilt from the paper's data
       per spec/charts.md would be cleaner than a screenshot if the underlying numbers are
       recoverable.
```

```text
Asset: Getty Images v. Stability AI complaint - the exhibit images showing a distorted
       Getty Images watermark reproduced in Stable Diffusion outputs.
Shows: The concrete basis for the trademark part of the claim, and a vivid illustration of
       training-data memorization. Use with care: it sits inside adversarial legal framing,
       and the UK court limited the trademark finding.
Crop:  If used, retain the watermark artifact and label it as a plaintiff's exhibit, not a
       neutral finding. Omit any surrounding imagery that is not the point.
```

```text
Asset: Stanford Internet Observatory CSAM report - Table 2 (summary of detection results).
Shows: The counts behind the finding in one place (PhotoDNA, MD5, Thorn columns). For an
       article, present the figures as a small table rather than reproducing anything from
       the dataset.
Crop:  Table only. None of the underlying imagery exists or should ever be shown; this is
       the one source where visual evidence beyond a results table is out of bounds.
```

## Discarded

```text
URL: https://openaccess.thecvf.com/content/CVPR2022/papers/Rombach_High-Resolution_Image_Synthesis_With_Latent_Diffusion_Models_CVPR_2022_paper.pdf
     Returned HTTP 403 (gated). The canonical peer-reviewed PDF; not unreachable, just
     blocked to this fetcher. The arXiv version (same paper, cited above) was read instead.
     The writer may still link the CVPR page as the venue of record.
```

```text
URL: https://www.twobirds.com/en/insights/2025/uk/stability-ai-defeats-getty-images-copyright-claims-in-first-of-its-kind-dispute-before-the-high-cour
     Returned HTTP 402. Would have been a second independent reading of the UK ruling; the
     Latham & Watkins analysis (cited) covered the same judgment.
```

```text
URL: petapixel.com / simonwillison.net / Wikipedia coverage of the August 2022 release
     Read to locate the release date and collaborators, then set aside. Secondary color
     with nothing the Stability AI page and the model card do not own firsthand.
```
