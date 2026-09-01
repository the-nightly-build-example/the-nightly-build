# Evidence record: the-evidence/segment-anything (01)

The evidence firmly supports the commissioned angle. The Segment Anything paper
and SA-1B's own dataset page agree that SAM produces masks with no class labels,
that its training set was built almost entirely by the model itself, and that
the scale claim rests on a data engine whose three stages did progressively less
human work. Every per-stage count in the brief is present in the paper and
internally consistent (4.3M + 5.9M assisted/semi-automatic masks; 1.1B total,
99.1% fully automatic). The paper draws its own boundary in plain terms: masks
carry no semantic meaning, instance segmentation only works when an external
detector supplies the boxes, and "it is unclear how to design simple prompts
that implement semantic and panoptic segmentation." The zero-shot claims are
real but smaller and more qualified than the popular reading. On the standard AP
metric, zero-shot SAM loses to the task-specific ViTDet-H on both COCO and LVIS,
a fact the paper reports itself. Independent medical-imaging studies extend that:
zero-shot SAM trails specialist models by wide Dice margins, and closing the gap
takes fine-tuning. The record is thin in one place: SA-1B's mask-quality claim
rests entirely on Meta's own 500-image internal study, with no independent audit
of the 1.1B masks. Nothing found undermines the commissioned angle; the
underperformance evidence undercuts the over-reading ("segmentation is solved"),
which is the reading the commission wants tested.

## Sources

```text
URL:         https://arxiv.org/abs/2304.02643
Kind:        primary — the paper owns the task, the model, the data engine, the
             SA-1B dataset, and every zero-shot number. Authored by the team
             (Kirillov et al., Meta AI Research / FAIR). Read in full via the
             ar5iv full-text mirror; the address above is the paper's own home.
Establishes: (a) the promptable segmentation task and its prompt types; (b) SAM's
             three-part architecture; (c) the three data-engine stages and their
             counts; (d) SA-1B totals; (e) the five zero-shot evaluations, their
             sizes and metrics, including where SAM loses to a task-specific model.
Paraphrase:  SAM is an image encoder (an MAE pre-trained ViT-H), a prompt encoder,
             and a lightweight mask decoder that returns a valid mask for any
             prompt — points, a box, a rough mask, or text. It predicts multiple
             masks per prompt to handle ambiguity and runs the prompt-to-mask step
             in ~50ms in a browser once the image embedding is computed. It was
             trained on SA-1B, a set of over 1B masks on 11M images, of which
             99.1% of masks were generated fully automatically by the model. Masks
             are class-agnostic: the annotation deliberately imposed no semantic
             labels. Zero-shot transfer is tested on five tasks; on the AP metric
             for instance segmentation SAM scores below the specialist ViTDet-H.
Locators:    Abstract; Sec. 3 (task and model); Sec. 4 (data engine); Sec. 5
             (SA-1B); Sec. 7.1–7.5 (zero-shot experiments); Sec. 8 (discussion,
             limitations). Numbers verified against these sections directly.
Quote:       "The promptable segmentation task ... is to return a valid
             segmentation mask given any prompt." / "we prompted the model with a
             32x32 regular grid of points ... producing a total of 1.1B
             high-quality masks." / "it is unclear how to design simple prompts
             that implement semantic and panoptic segmentation."
```

```text
URL:         https://ai.meta.com/datasets/segment-anything/
Kind:        primary — the dataset's own release page, owned by Meta, the party
             that built and licenses SA-1B. It owns the totals and the license.
Establishes: SA-1B's headline totals, that all released masks are automatic and
             class-agnostic, the release resolution, the privacy de-identification,
             and the research-only license.
Paraphrase:  SA-1B is 11M high-resolution, privacy-protecting images with 1.1B
             high-quality masks, roughly 100 masks per image, all generated fully
             automatically by SAM and stored as class-agnostic annotations in COCO
             run-length-encoding format. Faces and license plates are
             de-identified; the images were licensed from a large photo company.
             The dataset is released for research purposes only under a limited
             license.
Locators:    Dataset overview and license summary on the page.
Quote:       "Class agnostic mask annotations." / masks "generated fully
             automatically by the Segment Anything Model (SAM)." / license:
             "Research purposes only."
```

```text
URL:         https://ai.meta.com/blog/segment-anything-foundation-model-image-segmentation/
Kind:        primary — Meta's own release announcement. It owns the "foundation
             model" framing and the comparative scale claims made at launch.
Establishes: The launch framing ("first foundation model for image segmentation"),
             the scale-versus-prior-datasets claim, the annotation-speed claim, the
             prompt types, and the split licensing (model vs dataset).
Paraphrase:  Meta framed SAM as a step toward the first foundation model for image
             segmentation, with SA-1B holding more than 1.1B masks on ~11M images —
             400x more masks than any existing segmentation dataset. Building it
             was 6.5x faster than fully manual COCO polygon annotation and 2x
             faster than the previous largest annotation effort. SAM accepts
             foreground/background points, a rough box or mask, and free-form text.
             The model ships under Apache 2.0; the dataset is research-only.
Locators:    Announcement body (scale, speed, prompts, licensing paragraphs).
Quote:       "SA-1B has 400x more masks than any existing segmentation dataset." /
             "6.5x faster than COCO fully manual polygon-based mask annotation."
```

```text
URL:         https://arxiv.org/abs/2304.14660
Kind:        secondary (with respect to SAM) — an independent evaluation by Huang
             et al., published in Medical Image Analysis (2024, vol. 92, 103061).
             It is primary for its own COSMOS 1050K results but reports on SAM from
             outside the authoring party, which is what the brief asked for: an
             independent comparison where zero-shot SAM underperforms a
             task-specific model. Read via the arXiv HTML (v6).
Establishes: That zero-shot SAM is a weak medical segmenter relative to specialist
             models, measured on a large, standardized multi-modal benchmark.
Paraphrase:  The authors assembled COSMOS 1050K — 1,050,311 2D images/slices with
             6,033,198 masks across 18 modalities and 84 objects, drawn from 53
             open-source datasets — and ran zero-shot SAM on it. Original SAM
             reached a mean Dice of 58.52% and failed on many datasets. Box prompts
             beat point prompts; the automatic "everything" mode was weakest.
             Task-specific fine-tuning improved mean Dice by 4.39% (ViT-B) and
             6.68% (ViT-H). Their summary is that zero-shot SAM is decent but
             generally inferior to domain-specific models, lower by roughly 0.1–0.4
             Dice and by as much as 0.65 in the worst case.
Locators:    Abstract and results (COSMOS 1050K description; mean-Dice statement;
             prompt-mode and fine-tuning findings).
Quote:       "the original SAM may fail on lots of medical datasets with the mean
             DICE score of 58.52%." / "Finetuning the SAM on specific medical tasks
             could improve its average DICE performance by 4.39% and 6.68% for
             ViT-B and ViT-H, respectively."
```

```text
URL:         https://www.nature.com/articles/s41467-024-44824-z
Kind:        secondary (with respect to SAM) — MedSAM (Ma et al., Nature
             Communications 2024), the canonical fine-tune of SAM for medical
             imaging. Independent of the SAM authors. The Nature page is gated
             (a 303 redirect to an identity-provider login); its numbers were read
             from the authors' arXiv version (arxiv.org/abs/2304.12306). The
             address above is the source's own peer-reviewed home.
Establishes: The direction adaptation has actually taken — fine-tuning SAM on a
             large medical corpus to beat modality-specific specialists — and, by
             contrast, that unadapted SAM does not do this.
Paraphrase:  MedSAM is a foundation model for universal medical image segmentation,
             built by fine-tuning SAM on 1,570,263 image-mask pairs spanning 10
             imaging modalities and over 30 cancer types. The authors report it is
             more accurate and robust than modality-wise specialist models. The
             load-bearing distinction for this lesson: the winning system is the
             adapted MedSAM, not zero-shot SAM.
Locators:    Abstract (definition; training-set size; specialist comparison).
Quote:       "1,570,263 image-mask pairs, covering 10 imaging modalities and over
             30 cancer types." / "better accuracy and robustness than modality-wise
             specialist models."
```

```text
URL:         https://blog.roboflow.com/segment-anything-breakdown/
Kind:        secondary — independent contemporaneous coverage (Roboflow, published
             around the April 2023 release). Not the authoring party. Used only for
             present-day framing and one release detail, not for any core figure.
Establishes: How SAM was received and used in practice (a "foundation model,"
             an annotation first step) and that text prompting was not shipped.
Paraphrase:  Independent coverage described SAM as a foundation model for computer
             vision and "a GPT-esque moment," positioned it as a first step in
             annotation pipelines (its "Smart Polygon" one-click labeling), and
             noted that it outputs masks without class labels. It also records that
             text prompting was not released with the model — matching the paper's
             own framing of text-to-mask as a proof of concept.
Locators:    Article body (foundation-model framing; annotation use; the note that
             text prompting was not released).
Quote:       "text prompting is not released with the rest of the model."
```

## Contradictions

- **Zero-shot SAM vs. a task-specific model, inside the paper itself.** The
  commission asked specifically for any independent comparison where zero-shot
  SAM underperforms a task-specific segmentation model. The paper reports one on
  itself. On instance segmentation by mask AP, SAM loses to the specialist
  ViTDet-H on both benchmarks: COCO 46.5 vs 51.0, LVIS 44.7 vs 46.6. The paper
  argues the AP gap partly reflects low COCO ground-truth quality ("on COCO,
  where the mask AP gap is larger and the ground truth quality is relatively low
  ... ViTDet learns the specific biases of COCO masks") and that human raters
  prefer SAM's masks despite the lower AP. Both framings should reach the reader:
  the number favors the specialist; the paper contests the number's metric. This
  does not contradict the commissioned angle — it supports the "not a recognizer,
  and not segmentation-solved" reading.

- **On object proposals, "does remarkably well" is not "wins."** The paper's
  prose says SAM "outperforms ViTDet-H on medium and large objects, as well as
  rare and common objects," which is true per-slice, but on the headline
  all-objects average recall SAM trails: AR 59.3 vs 63.0. A writer who takes the
  sentence without the table would overstate the result. Both numbers are below.

- **"Foundation model for segmentation" (Meta, launch) vs. independent medical
  results.** Meta's framing and later popular usage call SAM a foundation model
  that generalizes. The independent medical evaluations show zero-shot SAM
  generalizes poorly to out-of-distribution domains (mean Dice 58.52% on COSMOS
  1050K; specialists better by up to ~0.65 Dice). The reconciliation is that the
  wins come after adaptation (MedSAM), not zero-shot. No source disputes the
  paper's natural-image numbers; the disagreement is about how far "anything"
  reaches.

- **MedSAM says it beats specialists; Huang says zero-shot SAM does not.** These
  are not in conflict: MedSAM is fine-tuned, Huang's underperformer is unadapted
  SAM. Keep the two apart in any sentence that cites them together — the
  difference is the whole point of the adaptation story.

## Numbers

```text
Figure: 4.3M masks from 120k images (assisted-manual stage)
Owner:  SAM paper (Sec. 4, data engine)
Scope:  First data-engine stage; model retrained 6 times; annotation time per
        mask fell 34s -> 14s; masks per image rose 20 -> 44.
```

```text
Figure: 5.9M additional masks in 180k images; 10.2M cumulative (semi-automatic)
Owner:  SAM paper (Sec. 4)
Scope:  Second stage; model retrained 5 times; masks per image rose 44 -> 72
        (including automatically generated masks).
```

```text
Figure: 1.1B masks from 11M images (fully automatic stage)
Owner:  SAM paper (Sec. 4/5); SA-1B dataset page; Meta blog
Scope:  Third stage applied to all 11M images via a 32x32 point grid; these masks
        are the released SA-1B set.
```

```text
Figure: 99.1% of released masks generated fully automatically
Owner:  SAM paper (Sec. 5)
Scope:  Share of SA-1B's ~1.1B masks; the human-drawn/human-checked masks
        (~10.2M across the first two stages) are the remaining ~0.9%.
```

```text
Figure: ~100 masks per image; images ~3300x4950 px, released at shortest side 1500 px
Owner:  SAM paper (Sec. 5); SA-1B dataset page (page states ~1500x2250 released)
Scope:  Per-image average and image resolution for SA-1B. Faces and license
        plates de-identified; images licensed from a photo provider.
```

```text
Figure: 94% of sampled mask pairs have >90% IoU
Owner:  SAM paper (Sec. 5, mask-quality study)
Scope:  Internal study on 500 sampled images comparing automatic masks to expert
        corrections. This is Meta's own audit; no independent audit of the full
        1.1B masks exists in the record.
```

```text
Figure: 400x more masks than any prior segmentation dataset; annotation 6.5x
        faster than manual COCO polygons
Owner:  Meta release blog (comparative claims)
Scope:  Launch-time comparison against existing public segmentation datasets and
        the COCO annotation workflow. Meta's own framing.
```

```text
Figure: single-point mIoU — SAM higher than RITM on 16 of 23 datasets, by up to ~47 IoU
Owner:  SAM paper (Sec. 7.1)
Scope:  Zero-shot single-point valid-mask task over a 23-dataset suite. Human
        study on a 1-10 quality scale placed SAM's mean ratings between 7 and 9,
        above RITM.
```

```text
Figure: zero-shot edge detection on BSDS500 — SAM ODS .768, OIS .786, AP .794, R50 .928
Owner:  SAM paper (Sec. 7.2)
Scope:  BSDS500 test set. Below the task-specific EDETR (ODS .840) and roughly at
        the level of the older HED (ODS .788). Reported as an emergent ability,
        not state of the art.
```

```text
Figure: object proposals on LVIS v1 — SAM AR@1000 59.3 (all) vs ViTDet-H 63.0 (all)
Owner:  SAM paper (Sec. 7.3, object-proposal table)
Scope:  Average recall at 1000 proposals. SAM higher on medium (81.6 vs 80.8),
        large (86.9 vs 87.0 — essentially tied), common (63.9 vs 63.3), rare
        (65.8 vs 58.3); lower on all, small (45.5 vs 51.7), frequent (59.1 vs 63.1).
```

```text
Figure: zero-shot instance segmentation — SAM mask AP below ViTDet-H on both sets
Owner:  SAM paper (Sec. 7.4, instance-segmentation table)
Scope:  COCO: SAM 46.5 vs ViTDet-H 51.0 (AP_S 30.8/32.0, AP_M 51.0/54.3, AP_L
        61.7/68.9). LVIS: SAM 44.7 vs ViTDet-H 46.6 (AP_S 32.5/35.0, AP_M
        57.6/58.0, AP_L 65.5/66.3). SAM is prompted with ViTDet's boxes; the
        detector, not SAM, supplies the object locations and classes.
```

```text
Figure: zero-shot medical segmentation — original SAM mean Dice 58.52% on COSMOS 1050K
Owner:  Huang et al. 2024 (independent; owns this result)
Scope:  1,050,311 images / 6,033,198 masks / 18 modalities / 84 objects / 53
        datasets. Zero-shot SAM inferior to specialist models by ~0.1-0.4 Dice,
        up to ~0.65 worst case. Fine-tuning improved mean Dice by 4.39%/6.68%.
```

```text
Figure: MedSAM trained on 1,570,263 image-mask pairs, 10 modalities, >30 cancer types
Owner:  Ma et al. 2024 (MedSAM; owns this result)
Scope:  The adaptation that beats modality-wise specialists — a fine-tune, not
        zero-shot SAM. Establishes the "where adaptation went" thread.
```

## Source assets

```text
Asset: The paper's opening overview figure (the task / model / data-engine
       triptych near the front of the SAM paper).
Shows: The whole contribution at a glance — that a prompt goes in and a mask
       comes out, that the model has three parts, and that the dataset was built
       by a model-in-the-loop loop. It carries the "three things at once" the
       commission wants kept distinct.
Crop:  Must keep all three panels legible together; a crop to one panel loses the
       point that these are one system. Omit nothing that labels a panel.
```

```text
Asset: The data-engine "masks per image" progression reported in Sec. 4 (20 -> 44
       -> 72), and the stage-by-stage counts.
Shows: The scale story as a curve of decreasing human effort — the number a
       human touched shrinks while the total explodes. Better as a small chart
       than as three sentences of numbers.
Crop:  If rendered as the paper's own figure, keep the axis labels and the stage
       boundaries. If rebuilt as a chart-N.py per house rules, cite the paper as
       the data source in the caption.
```

```text
Asset: The instance-segmentation comparison table (Sec. 7.4): SAM vs ViTDet-H mask
       AP on COCO and LVIS, with the size breakdown.
Shows: The single cleanest in-paper piece of "not segmentation-solved" evidence —
       the specialist wins on the standard metric. It grounds the boundary claim
       in the paper's own numbers.
Crop:  Keep both rows and both dataset columns; dropping either the COCO or LVIS
       column would let a reader treat one loss as a fluke.
```

```text
Asset: SA-1B example-image grid on the dataset page / in the paper (images with
       their ~100 automatic masks overlaid).
Shows: What "class-agnostic masks" looks like — every region segmented, none
       named. The visual makes the labels-vs-masks distinction concrete.
Crop:  Keep at least one full image with its dense mask overlay; a tight crop to
       one mask hides the density that is the point.
```

## Discarded

```text
URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC11788268/ (nnSAM) — a hybrid method that
     combines SAM features with nnU-Net; about a new architecture, not a clean
     zero-shot-SAM-vs-specialist comparison. Huang et al. covers the underperformance
     point with a larger, standardized benchmark.
```

```text
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12196577/ (lumbar-spine MRI SAM/MedSAM) —
     real finding (MedSAM Dice 0.79/0.88 vs nnU-Net 0.99) but a single small
     anatomical study; Huang et al. and MedSAM already carry the medical thread
     with broader evidence. Held in reserve, not cited.
```

```text
URL: https://viso.ai/deep-learning/segment-anything-model-sam-explained/ — a vendor
     explainer; overlaps the Roboflow piece for present-day framing and adds no
     independently sourced figure. One secondary framing source is enough.
```

```text
URL: https://arxiv.org/pdf/2408.06305 (From SAM to SAM 2) and other SAM 2 / SAM 3 material —
     the commission scopes this lesson to the original document. SAM 2 (video,
     2024) is context only; not read into the record beyond noting it exists.
```
