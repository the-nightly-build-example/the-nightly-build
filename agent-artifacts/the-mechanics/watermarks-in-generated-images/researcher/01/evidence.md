# Evidence record: the-mechanics/watermarks-in-generated-images (01)

The two mechanisms the commission needs are each pinned to a source that owns
it, and they hold up: the training-dataset paper documents a pervasive,
scored-but-not-removed watermark signal across the corpus Stable Diffusion
trained on, and a separate extraction paper documents verbatim memorization of
specific training images, with an explicit statement that the two are
different questions and that telling them apart for a single output is
unresolved. The litigation exhibit the commission wants as the concrete anchor
checks out as an anchor for the *behavior*, but not for the mechanism Getty's
own paragraph implies: the paired images in the complaint's central
watermark exhibit are two different photographs, not a matched original and
its copy, even though the surrounding paragraph cites memorization research
one sentence earlier. That gap is the most important finding in this record
and is detailed under Contradictions. The evidence is thin in one place the
commission asked about directly: neither the LAION-5B paper nor the Latent
Diffusion Models paper gives a dataset-wide watermark percentage; the actual
percentage figures come from LAION's own announcement blog, a primary source
but a different document than the peer-reviewed paper, and they are stated
there to be conservative undercounts. The deduplication-and-memorization
figure that exists is real but narrow: it was measured on CIFAR-10, not on
Stable Diffusion or LAION, and the paper says so.

## Sources

```text
URL:         https://arxiv.org/abs/2210.08402
Kind:        primary — Schuhmann et al., "LAION-5B: An open large-scale
             dataset for training next generation image-text models"
             (NeurIPS 2022 Datasets and Benchmarks). The paper is the
             dataset's own technical documentation, written by the team that
             built it.
Establishes: The scale of the dataset Stable Diffusion trained on, the three
             released subsets, that every image carries a per-image
             watermark-probability score, that no dataset-wide watermark
             percentage is stated in the paper itself, and that the dataset
             was not deduplicated for near-duplicate images (that is named as
             future work).
Paraphrase:  LAION-5B is 5.85 billion CLIP-filtered image-text pairs, split
             into 2.32 billion English pairs (called LAION-2B-en), 2.26
             billion multilingual pairs, and 1.27 billion pairs whose
             language could not be classified (Sec. 1, Sec. 4). Two curated
             sub-datasets are named: LAION-High-Resolution, 170 million
             images for super-resolution work, and LAION-Aesthetic, 120
             million images selected by a linear aesthetic-score estimator
             built on CLIP (Sec. 5.1). Every released sample carries "the
             probability of the image containing a watermark" and "the
             probability of a sample being NSFW" as continuous 0-1 scores
             from the team's own classifiers (Sec. 4, "Dataset Composition");
             the paper states a headline figure only for NSFW ("3% of images
             were detected as NSFW," Sec. 4) and gives no equivalent
             dataset-wide watermark percentage anywhere in the main text or
             appendix. Appendix Q13 (datasheet, "Uses" section) states "there
             exist near duplicate images which makes possible a many to one
             embedding," and the Discussion section (Sec. 6) names
             deduplication against benchmark overlap as future work, not
             something already done to the released data. Appendix F.2,
             titled "Stable Diffusion," is the paper's own account of Stable
             Diffusion's training recipe: 237,000 steps at 256x256 on
             LAION-2B-en, 194,000 steps at 512x512 on laion-high-resolution,
             515,000 steps at 512x512 on laion-improved-aesthetics, and
             390,000 further steps at 512x512 on laion-improved-aesthetics
             with 10% text-conditioning dropout. The appendix does not state
             whether these training subsets were themselves watermark- or
             NSFW-filtered before use; it only cites the Stable Diffusion
             GitHub repository for further technical detail, which this
             record did not open (outside the four required primaries).
Locators:    Abstract; Sec. 1 (Introduction); Sec. 4 ("Dataset Composition");
             Sec. 5.1 ("Derived datasets"); Sec. 6 ("Discussion... Data
             Overlap"); Appendix, Datasheet Q13-Q14; Appendix F.2 ("Stable
             Diffusion").
Quote:       "a dataset consisting of 5.85 billion CLIP-filtered image-text
             pairs, of which 2.32B contain English language" (Abstract).
             "3% of images were detected as NSFW, which can be filtered out
             by a user with the NSFW tag." (Sec. 4). "There exist near
             duplicate images which makes possible a many to one embedding in
             certain scenarios." (Appendix, Q13).

URL:         https://laion.ai/blog/laion-5b/
Kind:        primary — LAION's own announcement post for the dataset (posted
             by Romain Beaumont, one of the paper's co-authors and the
             engineer who built the dataset-preparation pipeline, 31 Mar
             2022), published by the organization that owns the dataset and
             its watermark classifier.
Establishes: The only figure found anywhere in this research for what share
             of the dataset is watermarked, broken out by subset, with an
             explicit accuracy caveat from the source itself.
Paraphrase:  Under "Dataset Statistics," broken out per released subset, the
             post reports a watermark proportion of 6.1% for Laion2B-en,
             5.6% for Laion2B-multi, and 4% for Laion1B-nolang. The post
             describes these as conservative estimates: the watermark
             classifier was thresholded at a probability greater than 0.8
             before a sample was counted as watermarked, a strict cutoff
             that trades recall for precision, so the true watermarked share
             of each subset is more likely to be higher than the stated
             percentage than lower.
Locators:    "Dataset Statistics" section, per-subset breakdown (Laion2B-en,
             Laion2B-multi, Laion1B-nolang subsections).
Quote:       "Watermark proportion: 6.1%" (Laion2B-en); "Watermark
             proportion: 5.6%" (Laion2B-multi); "Watermark proportion: 4%"
             (Laion1B-nolang).

URL:         https://arxiv.org/abs/2112.10752
Kind:        primary — Rombach, Blattmann, Lorenz, Esser, and Ommer,
             "High-Resolution Image Synthesis with Latent Diffusion Models"
             (CVPR 2022). This is the paper that introduces the latent
             diffusion model architecture Stable Diffusion is built on,
             written by the team (with Stability AI compute support
             acknowledged) that trained it.
Establishes: The mechanism definition for distributional learning: what the
             training objective is and what it means for a diffusion model to
             be trained on a distribution rather than told to copy specific
             examples. Also: that the paper's own text-to-image experiments
             used LAION-400M, a different (smaller, earlier) LAION release
             than the LAION-5B subsets the released Stable Diffusion model
             was actually trained on per the LAION-5B paper's Appendix F.2.
Paraphrase:  Diffusion models are defined as "probabilistic models designed
             to learn a data distribution p(x) by gradually denoising a
             normally distributed variable" (Sec. 3.2); training minimizes a
             denoising loss (Eq. 2, the "LDM" objective) with no example-level
             copying step and no mechanism that targets a specific training
             image. For their own text-to-image experiments, the authors
             "train a 1.45B parameter KL-regularized LDM conditioned on
             language prompts on LAION-400M" (Sec. 4.3.1) — this is the
             academic paper's own model, not the separately released
             "Stable Diffusion" checkpoint, which the LAION-5B paper's
             Appendix F.2 documents as trained on LAION-2B-en and other
             LAION-5B subsets instead. The Limitations/societal-impact
             section states plainly that memorization was an open question
             at the time of writing: "Generative models can also reveal
             their training data [citations], which is of great concern when
             the data contain sensitive or personal information," without
             asserting that their own model does or does not do this.
Locators:    Sec. 3.2 ("Latent Diffusion Models"), Eq. 2; Sec. 4.3.1
             ("Text-to-Image Synthesis"); Sec. 5 / Limitations and Societal
             Impact.
Quote:       "Diffusion Models are probabilistic models designed to learn a
             data distribution p(x) by gradually denoising a normally
             distributed variable" (Sec. 3.2).

URL:         https://arxiv.org/abs/2301.13188
Kind:        primary — Carlini, Hayes, Nasr, Jagielski, Sehwag, Tramèr,
             Balle, Ippolito, and Wallace, "Extracting Training Data from
             Diffusion Models" (USENIX Security 2023). This is the
             extraction study itself, run by the researchers who designed
             and executed the attack.
Establishes: The verbatim-memorization mechanism, its formal definition, its
             extraction rate against Stable Diffusion specifically, that
             memorization concentrates on heavily duplicated training
             images, and the one deduplication-versus-memorization
             experiment this record could find — run on CIFAR-10, not on
             Stable Diffusion.
Paraphrase:  The paper defines "(k,l,delta)-Eidetic memorization": an image
             counts as extracted only if a generated image falls within an
             L2 pixel-distance threshold of a specific training image, with
             the primary threshold at 0.05-0.15 for "near pixel-perfect"
             matches (Sec. 4.1). This is explicitly a narrower, more
             conservative bar than "any recognizable resemblance" (Sec. 4.1,
             Fig. 2: a generated "Barack Obama" that is clearly recognizable
             but not a near-copy of any one training photo does not count).
             Against Stable Diffusion v1.4, described as "an 890 million
             parameter text-conditioned diffusion model trained on 160
             million images," the authors generated 500 candidate images
             each for the 350,000 most-duplicated training captions (175
             million generated images total) and identified 94 images
             meeting the strict (L2, 0.15) threshold, plus 13 more confirmed
             by manual visual inspection, for 109 total near-copies (Sec.
             4.2.2). Memorization concentrated heavily among training
             images duplicated at least k=100 times (Fig. 5); even at that
             level the duplicated examples are "just one in a million"
             training examples, so this is a study of the most-exposed
             tail of the dataset, not typical behavior. Against Imagen,
             a separate, non-public Google model, the rate was higher: 23
             of the 1,000 most-duplicated prompts were memorized (Sec. 4.3).
             The paper states plainly that duplication, not the training
             objective alone, is the load-bearing cause it identifies:
             "duplication is a major factor behind training data
             extraction" (Sec. 4.2.2), and separately that better (lower
             loss / lower FID) models memorize more (Sec. 5.2.3). On
             deduplication (Sec. 7.1), the authors deduplicated CIFAR-10
             using the imagededup tool at a similarity threshold above 0.85,
             removing 5,275 of 50,000 training images, retrained a diffusion
             model on the reduced set, and found the number of regenerated
             (memorized) images dropped from 1,280 to 986 — about a 23%
             relative reduction, which the paper itself calls "not a
             substantial drop." The paper explicitly states this experiment
             was not run on Stable Diffusion or any LAION-scale dataset; it
             only expects (does not measure) a larger effect there because
             the correlation between duplication and extraction was
             stronger for Stable Diffusion than for CIFAR-10 in the earlier
             sections. The paper never discusses watermarks: the word does
             not appear in the text, and the qualitative breakdown of the
             109 Stable Diffusion images extracted (58% recognizable-person
             photos, 17% products for sale, 14% logos/posters, Sec. 4.2.2)
             names no watermark category. The paper frames the open
             question explicitly: "Do large-scale models work by generating
             novel output, or do they just copy and interpolate between
             individual training examples? ... this question remains open"
             (Sec. 9).
Locators:    Abstract; Sec. 4.1 (Definitions, Fig. 2); Sec. 4.2 ("Extracting
             Data from Stable Diffusion"), 4.2.2 ("Extraction Results"), Fig.
             3, Fig. 5; Sec. 4.3 ("Extracting Data from Imagen"); Sec. 5.2.3
             ("Memorization Versus Utility"); Sec. 7.1 ("Deduplicating
             Training Data"); Sec. 9 ("Discussion and Conclusion").
Quote:       "we find 94 images are (l2,0.15)-extracted... a further 13 (for
             a total of 109 images) are near-copies of training examples"
             (Sec. 4.2.2). "The model trained on the deduplicated data
             regenerates 986 examples, as compared to 1280 for the original
             model. While not a substantial drop, these results show that
             deduplication can mitigate memorization." (Sec. 7.1). "Do
             large-scale models work by generating novel output, or do they
             just copy and interpolate between individual training
             examples? ... this question remains open." (Sec. 9).

URL:         https://www.courtlistener.com/docket/66788385/1/getty-images-us-inc-v-stability-ai-inc/
Kind:        primary — the Complaint itself, filed by Getty Images (US),
             Inc. against Stability AI, Inc. This is a litigant's own
             pleading: it establishes what Getty alleged and what its
             exhibit shows, not that the allegation is proven. Read from the
             court-stamped filing (Case 1:23-cv-00135-UNA, D. Del., Document
             1, filed 02/03/23), retrieved via the free CourtListener/RECAP
             mirror of the PACER record after the storage.courtlistener.com
             copy was checked against a second independent copy hosted by
             the Copyright Alliance and found identical.
Establishes: What Getty alleged about the watermark appearing in Stable
             Diffusion output, and — independently of the allegation — what
             the exhibit images themselves actually show, which is the
             concrete real-world anchor the commission asked for.
Paraphrase:  Getty alleges Stability AI copied "more than 12 million
             photographs" from Getty's sites to train Stable Diffusion (P1).
             Getty's central watermark allegation: "Often, the output
             generated by Stable Diffusion contains a modified version of a
             Getty Images watermark, creating confusion as to the source of
             the images and falsely implying an association with Getty
             Images" (P11). Paragraph 51 states that "independent
             researchers have observed that Stable Diffusion sometimes
             memorizes and regenerates specific images that were used to
             train the model," citing the Carlini extraction paper above
             and the Somepalli "Diffusion Art or Digital Forgery?" paper in
             footnote 6. The very next paragraph, 52, presents the
             complaint's main watermark exhibit and states it is "underscoring
             the clear link between the copyrighted images that Stability
             AI copied without permission and the output its model
             delivers," captioning a side-by-side pair as an "original,
             watermarked image copied by Stability AI and used to train its
             model" (left) against "the watermarked image... output
             delivered using the model" (right). As read directly (Page 18,
             PageID #18), the two images are two different photographs: the
             left is a real Getty stock photo of a Tottenham Hotspur player
             challenging a Southampton player, watermarked "gettyimages /
             Andrew Powell" with a visible stock-photo ID number; the right
             is a different scene — a Tottenham player (with a fictitious
             red "AA" chest crest, not any real sponsor mark) challenging a
             Liverpool player — carrying a smeared, illegible mark in the
             same corner position and typeface family as a Getty watermark,
             but not the same photograph, players, or pose as the left
             image. Paragraphs 58-60 present three further examples framed
             only as watermark distortion, not as matched original/output
             pairs: a red-carpet gown photo and a garden wedding photo, each
             carrying a blurred "gettyimages"-style mark (P58-59), and a
             synthetic-looking rugby image with a garbled watermark-like
             mark at bottom right (P59-60), which the complaint calls
             "distorted versions of Getty Images' watermark and other
             watermarks" (P60) without pairing it against any specific
             training photo. Paragraph 57-58 separately alleges Stability
             AI "knowingly removed Getty Images' watermarks from some images
             in the course of its copying," a distinct allegation from the
             watermark appearing in output.
Locators:    Complaint P1 (scale allegation), P11 (headline watermark
             allegation), P49-52 (cat-in-a-scarf example, memorization
             citation, and the soccer-photo exhibit), footnote 6 (citing
             Carlini and Somepalli), P57-61 (Section E, "Stability AI's
             Attempts to Circumvent Getty Images' Watermarks," wedding-photo
             and rugby-photo exhibits), Page 18/PageID 18 (the paragraph-52
             exhibit as printed).
Quote:       "In many cases, and as discussed further below, the output
             delivered by Stability AI includes a modified version of a
             Getty Images watermark, underscoring the clear link between the
             copyrighted images that Stability AI copied without permission
             and the output its model delivers." (P52). "Upon information
             and belief, Stability AI is well aware that Stable Diffusion
             generates images that include distorted versions of Getty
             Images' watermark and other watermarks, but it has not modified
             its model to prevent that from happening." (P60).

URL:         https://www.courtlistener.com/docket/66788385/getty-images-us-inc-v-stability-ai-inc/
Kind:        primary — the federal court's own docket for this case, used
             only to verify the case's identity and filing date, not for any
             substantive claim.
Establishes: Case number 1:23-cv-00135, filed in the U.S. District Court for
             the District of Delaware on Feb. 3, 2023 (docketed Feb. 6,
             2023), assigned to Judge Jennifer L. Hall, terminated Aug. 18,
             2025 (the docket shows this suit was later closed; this record
             did not research why, since the commission's use of the
             filing is about the exhibit and allegation at filing, not the
             case's outcome, and case disposition is outside this brief's
             questions).
Paraphrase:  Docket caption: "Getty Images (US), Inc. v. Stability AI, Inc.,
             1:23-cv-00135, (D. Del.)... Date Filed: Feb. 3, 2023... Cause:
             17:501 Copyright Infringement."
Locators:    Docket header/caption block.
Quote:       (none needed beyond the caption fields above)

URL:         https://arxiv.org/abs/2406.09548
Kind:        secondary — Black, Naidu, et al. (a large-scale survey/report,
             "Between Randomness and Arbitrariness: Some Lessons for
             Reliable Machine Learning at Scale"). The authors did not build
             LAION or its watermark classifier; they report and cite the
             dataset's own published statistic.
Establishes: Only that LAION's 6.1% figure is being cited and used by
             outside researchers as the dataset's watermark rate — this
             record used it solely to cross-check that the figure it found
             on LAION's blog is the same figure independent researchers rely
             on, not as the figure's origin.
Paraphrase:  "The LAION team estimates that the 6.1% of the dataset
             Laion2B-en contains watermarked images," citing "the website
             introducing the LAION dataset" and its "pwatermark" feature,
             in a section on data-licensing risk in large training sets.
Locators:    Section on dataset consent/licensing, footnote discussing
             LAION-5B's CC-BY release and watermark feature.
Quote:       "The LAION team estimates that the 6.1% of the dataset
             Laion2B-en contains watermarked images."
```

## Contradictions

**The complaint's own exhibit undercuts the sentence introducing it.** Getty's
paragraph 51 cites memorization research (Carlini; Somepalli) immediately
before paragraph 52 presents its central watermark exhibit and says the
exhibit is "underscoring the clear link" between a specific copied training
image and Stable Diffusion's output. Read directly, the two images in that
exhibit are not the same photograph and not even the same players, pose, or
sponsor logo — they share only a corner position and general typeface family
of the distorted mark. The complaint frames the watermark as evidence of
copying *that* image; the image pair it prints is not evidence of that. It is
better evidence of the opposite mechanism: a mark reproduced as a learned
regularity of "stock sports photo" as a class, independent of any single
source photo. This is the specific pattern the brief asked this record to
flag — a source that frames the ghost watermark as copying one image — and it
comes from the litigant's own filing, not from a secondary retelling of it.
The complaint's later examples (paragraphs 58-60: the wedding photos, the
rugby image) do not even attempt a matched-pair framing; they present the
watermark as a recurring feature of output in general, which sits more
comfortably with the paper's own claims than paragraph 52's framing does.

**The paper the complaint cites for memorization never connects its findings
to watermarks.** Carlini et al. do not mention watermarks anywhere in the
paper, and their own breakdown of what kind of content the 109 memorized
Stable Diffusion images contained (recognizable people, products, logos/
posters) does not include a watermark category. The complaint's footnote 6
citation is accurate as far as it goes — Carlini's paper does establish that
Stable Diffusion memorizes some specific images — but nothing in that paper
supports extending that finding to the watermark phenomenon specifically.

**LAION's watermark-prevalence figures are stated by LAION itself to be
undercounts.** The 6.1%/5.6%/4% figures came from a strict >0.8 classifier
threshold that the source explicitly frames as conservative. A writer citing
this figure as a ceiling on watermark prevalence would be citing it more
confidently than the source that owns it does.

**Two different figures exist for how much data Stable Diffusion trained
on, and no source reconciles them.** Carlini et al. describe the Stable
Diffusion v1.4 checkpoint they attacked as "trained on 160 million images."
The LAION-5B paper's own Appendix F.2 describes Stable Diffusion's training
recipe as a sequence of runs over LAION-2B-en (2.32 billion pairs),
laion-high-resolution (170 million), and laion-improved-aesthetics (size not
stated in either paper read for this record). These are not obviously the
same number, and this record found nothing in either primary source, or
searched for elsewhere, that explains what "160 million" refers to (a
specific filtered/deduplicated checkpoint stage, most likely, but unstated).
The writer should not present a single figure for "how many images Stable
Diffusion trained on" without naming which of these it means.

## Numbers

```text
Figure: 5.85 billion image-text pairs (LAION-5B total)
Owner:  LAION-5B paper (Schuhmann et al., arXiv:2210.08402), Sec. 1/Sec. 4
Scope:  The full released dataset as of the paper's 2022 publication; split
        2.32B English (LAION-2B-en), 2.26B multilingual, 1.27B
        unknown-language.

Figure: 170 million images (LAION-High-Resolution subset)
Owner:  LAION-5B paper, Sec. 5.1
Scope:  A curated subset of LAION-5B for super-resolution work; this is one
        of the four training stages Appendix F.2 lists for Stable
        Diffusion.

Figure: 120 million images (LAION-Aesthetic subset)
Owner:  LAION-5B paper, Sec. 5.1
Scope:  Aesthetic-score-filtered subset of LAION-5B (linear estimator on
        CLIP embeddings); "laion-improved-aesthetics," the subset used for
        two of Stable Diffusion's four training stages per Appendix F.2, is
        a further-filtered relative of this subset whose exact size is not
        given in the paper.

Figure: 3% of images flagged NSFW
Owner:  LAION-5B paper, Sec. 4
Scope:  Whole 5.85B corpus, at the paper's default NSFW-classifier
        threshold. Given only for contrast with the watermark figures,
        which the same paper does not provide at the same aggregate level.

Figure: Watermark proportion 6.1% (LAION-2B-en), 5.6% (LAION-2B-multi),
        4% (LAION-1B-nolang)
Owner:  LAION-5B announcement blog (laion.ai/blog/laion-5b/, Beaumont, 31
        Mar 2022) — a primary source, but not the peer-reviewed paper.
Scope:  Per named LAION-5B subset, at a >0.8 watermark-classifier
        probability threshold; the source calls these conservative
        (likely-undercounted) estimates.

Figure: "890 million parameter text-conditioned diffusion model trained on
        160 million images" (Stable Diffusion v1.4, as attacked)
Owner:  Carlini et al., arXiv:2301.13188, Sec. 4.2
Scope:  The specific Stable Diffusion v1.4 checkpoint the authors ran their
        extraction attack against; does not match, and is not reconciled
        with, any single subset-size figure in the LAION-5B paper's own
        Appendix F.2 description of Stable Diffusion's training recipe.

Figure: 109 near-identical training images extracted (94 by strict L2
        threshold + 13 by manual confirmation), out of 175,000,000 images
        generated
Owner:  Carlini et al., Sec. 4.2.2
Scope:  Stable Diffusion v1.4; attack targeted the 350,000 most-duplicated
        training captions specifically (500 generations each), so this is
        an upper-bound/worst-case rate for the most-exposed slice of the
        training set, not a random-output memorization rate.

Figure: Memorization concentrates at training-image duplicate count k >=
        100; at that level, duplicated images are still about "one in a
        million" of the full training set
Owner:  Carlini et al., Sec. 4.2.2, Fig. 5
Scope:  Stable Diffusion v1.4, same attack as above.

Figure: 23 of 1,000 most-duplicated prompts memorized
Owner:  Carlini et al., Sec. 4.3
Scope:  Imagen (Google's model), not Stable Diffusion; included only as a
        cross-model comparison point, not usable as a Stable Diffusion
        figure.

Figure: Deduplication (>0.85 similarity) removed 5,275 of 50,000 CIFAR-10
        training images; regenerated/memorized examples fell from 1,280 to
        986 (about a 23% relative reduction)
Owner:  Carlini et al., Sec. 7.1
Scope:  CIFAR-10 only, small unconditional diffusion models the authors
        trained themselves. Explicitly not measured on Stable Diffusion or
        any LAION-scale dataset; the paper states only an unmeasured
        expectation that the effect would be larger at that scale, and
        calls its own CIFAR-10 result "not a substantial drop."
```

## Source assets

No number in this record forms a series worth an original chart: the
watermark proportions are three single percentages, not a trend, and the
deduplication result is one before/after pair on CIFAR-10 only. The real
visual evidence here is the exhibit images themselves.

```text
Asset: Getty complaint, Page 18 (PageID #18), paragraph-52 exhibit — a
       side-by-side pair of soccer photographs
Shows: A reader can see directly, without needing the surrounding legal
       argument, that the two images are different photographs (different
       players, pose, and a fictitious "AA" crest vs. a real sponsor
       arrangement) that share only a smeared, corner-positioned mark in the
       visual family of a Getty watermark. This is the single strongest
       piece of visual evidence in this record for the article's central
       teaching point: the watermark's presence does not mean the specific
       photo was copied.
Crop:  Both images must stay whole and side by side; cropping to just the
       watermark corners would remove the very comparison (different
       players/scene) that makes the point. Do not sharpen, enlarge, or
       otherwise "clean up" the distorted mark beyond how the exhibit
       renders it, since the illegibility is itself part of the evidence.

Asset: Getty complaint, Page 22 (PageID #22), paragraph-60 exhibit — a
       single generated image of two rugby players
Shows: What the ghost watermark itself looks like as a standalone texture on
       a generated image: a garbled, semi-legible "gettyimages"-style mark
       plus a second line of even-less-legible text beneath it, on an image
       with visibly distorted anatomy elsewhere in the frame. Useful for
       showing the reader the actual visual character the lesson opens
       with (a texture resembling a mark, not legible text) with a real,
       sourced example rather than a description.
Crop:  Can be cropped to the image itself (dropping the surrounding legal
       paragraph), but must keep the full frame so the mark's position and
       the rest of the image's visible distortion are both visible; do not
       crop to the watermark alone, which would misrepresent it as a
       clean logo rather than one figure among several odd regions of the
       generated image.

Asset: Carlini et al., Figure 1 (arXiv:2301.13188, page 1) — training-set
       photo of Ann Graham Lotz beside a Stable Diffusion generation of the
       same subject
Shows: A clean, sourced example of true verbatim memorization (L2 distance
       0.031, described by the authors as "nearly identical") — useful as
       the contrast case against the watermark exhibit, since this pair
       really is the same image reproduced, unlike the Getty exhibit.
Crop:  Keep both images and the caption's L2 distance figure together; the
       number is the evidence, not just the picture.

Asset: Carlini et al., Figure 5 (arXiv:2301.13188, page 6) — histogram of
       extracted-image counts against training-set duplicate count
Shows: The concrete threshold (~100 duplicates) at which memorization
       becomes detectable under their method; supports the "settled"
       half of the memorization mechanism with an actual distribution
       rather than only a prose claim.
Crop:  Keep both axes and their labels/scale; the duplicate-count axis is
       log-scaled and would mislead if relabeled or cropped to hide that.
```

## Discarded

```text
URL: https://arxiv.org/abs/2212.03860 (Somepalli et al., "Diffusion Art or
     Digital Forgery? Investigating Data Replication in Diffusion Models")
     — only the abstract was reviewed (via a fetched summary), not the full
     paper, so this record does not treat it as read to the standard the
     other sources meet. It is the second paper Getty's footnote 6 cites
     for memorization, alongside Carlini. Carlini et al. themselves
     characterize Somepalli's method as measuring semantic/style similarity
     to the training set rather than Carlini's stricter near-pixel-identical
     standard (Carlini Sec. 2, "Background"), which is a relevant
     distinction if the writer wants to cite Somepalli directly — but doing
     so would require a fresh, full read, which is outside this brief's
     four required primaries and was not attempted here.

URL: an unverified figure encountered only in an initial web-search summary
     — "1,308 random samples from LAION-5B, 176 watermarked (13.45%),
     precision 34.09%, recall 51.13%" — could not be located in either the
     LAION-5B paper or the LAION-5B blog post after checking both directly
     for a watermark test-set section (LAION-5B paper Appendix C.7,
     "Watermark and safety inference," describes a manually annotated test
     set but states no such percentages). Not used anywhere in this record
     because its source was never opened and confirmed.

URL: https://fingfx.thomsonreuters.com/gfx/legaldocs/byvrlkmwnve/GETTY%20IMAGES%20AI%20LAWSUIT%20complaint.pdf
     and https://docs.justia.com/cases/federal/district-courts/delaware/dedce/1:2023cv00135/81407/1
     — alternate mirrors of the same complaint found while locating a
     canonical source; superseded once the court-stamped copy was retrieved
     directly from CourtListener/RECAP (storage.courtlistener.com), which
     this record cites instead as the document's own stable page.

URL: https://copyrightalliance.org/wp-content/uploads/2023/02/Getty-Images-v.-Stability-AI-Complaint.pdf
     — read in full first (used to locate the watermark paragraphs and
     exhibits before the canonical court copy was found) and confirmed
     text-identical to the official filing; not cited in the Sources
     section above because the CourtListener/RECAP copy is the document's
     own canonical page, but recorded here since it was genuinely read and
     shaped this record's early findings.
```
