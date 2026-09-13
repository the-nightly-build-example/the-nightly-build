# Evidence: when-ai-breaks/retinopathy-field-study (01)

The evidence strongly supports the lesson's spine: a diabetic-retinopathy model with
ophthalmologist-level accuracy on curated image sets was deployed into real Thai
screening clinics and created friction that lab metrics never predicted. The
load-bearing field figure, that the system deemed 21% of images ungradable and refused
to score them (393 of 1,838 in the first six months at three clinics), comes from the
CHI 2020 study read in full, as do the connectivity delays, the referral-logistics
friction, the consent opt-outs, and every nurse quote. The lab pedigree (>90% sensitivity
and specificity) traces to Gulshan 2016 in JAMA, verified against that paper's own
operating points.

The evidence is thin in one place that matters, and it cuts against the commission's
loosest framing. The commission says bench accuracy "does not transfer to outcomes in
the room." The record shows something more precise and more interesting: the model's
diagnostic accuracy largely *did* transfer. A follow-up on the same prospective program
(Ruamviboonsuk 2022, Lancet Digital Health) reported 94.7% field accuracy for
vision-threatening disease, matching retina specialists. What failed was the workflow
around the model, driven by a conservative image-quality gate meeting messy real images
and slow clinic internet. The CHI study measured nurse and patient experience, not field
diagnostic accuracy, and its own authors name the tension as one of thresholds and
environment, not model error. Six of the seven CHI authors work for Google, so the
paper's framing carries the operator's stake; the independent secondaries corroborate the
facts and push back mainly on Google's optimistic tone. The writer should teach the
sociotechnical gap and must not claim the model's field accuracy collapsed. See
Contradictions for the full probe.

## Sources

```text
URL:         https://dl.acm.org/doi/10.1145/3313831.3376718
Kind:        primary. It is the field study itself, authored by the deploying team
             (six of seven authors at Google; one at Rajavithi Hospital). It owns every
             field observation, figure, and nurse quote firsthand.
Establishes: The deployment context, the 21% ungradable rate and its causes, connectivity
             delays, referral friction, consent opt-outs, the study scale, and the
             authors' own diagnosis of why the system faltered in the field.
Paraphrase:  From interviews and observation across eleven clinics in Thailand (five in
             Pathum Thani, six in Chiang Mai), the team studied a deep-learning DR
             screening system before and after deployment at three Pathum Thani clinics.
             The system "has stringent guidelines regarding the images it will assess" and
             "only assesses the highest-quality images"; if an image "has a bit of blur or
             a dark area" the system rejects it as ungradable "even if it could make a
             strong prediction." Of 1,838 images uploaded in the first six months, 393
             (21%) "didn't meet the system's high standards for grading." Low-quality
             images came from non-darkened rooms, cameras needing repair, and clinics not
             using dilation drops. Slow connections caused some images to take 60-90
             seconds to upload; one clinic's internet outage of two hours cut patients
             screened from 200 to 100. The authors conclude "ungradability had the largest
             impact on model performance and the patient experience," and reframe the core
             problem as "the tension between designing a threshold for the quality of
             images that the system will use... and the quality of images that arise from
             an imperfect, resource-constrained environment." As a result of the research
             they changed the protocol so an ophthalmologist overreader reviews an
             ungradable image before the patient is referred.
Locators:    Abstract; Sec 1 Introduction (lab-accuracy claim); Sec 4 "Context of use"
             (deployment, 7,600-patient prospective study, three initial clinics, Dec
             2018-May 2019); Sec 5 "Data Collection"/"Participants"/Table 1 (fieldwork
             Nov 2018, Apr 2019, Aug 2019; 1,838 image uploads); Sec 6 Findings, "Volume,"
             "Consenting patients," "Gradability," "Internet speed and connectivity,"
             "Workarounds"; Sec 7 Discussion; Sec 8 Limitations.
Quote:       "Out of 1838 images that were put through the system (in the first six months
             of usage), 393 (21%) didn't meet the system's high standards for grading."
Access note: The canonical ACM page gates automated fetches (returns 403 to bots) but
             resolves for a reader. Full text was read via the Internet Archive snapshot
             web.archive.org/web/20250307040559/https://dl.acm.org/doi/fullHtml/10.1145/3313831.3376718.
             An open author-hosted landing page is https://research.google/pubs/pub48768/.
```

```text
URL:         https://jamanetwork.com/journals/jama/fullarticle/2588763
Kind:        primary. Gulshan et al. 2016, JAMA. It owns the lab-accuracy claim the lesson
             opens on; the deployed model descends from this algorithm (the CHI paper cites
             it as reference [20] for its accuracy claim).
Establishes: The bench pedigree: ophthalmologist-level sensitivity and specificity for
             referable DR on curated, graded fundus-image sets.
Paraphrase:  A deep convolutional neural network was trained on a development set of
             128,175 fundus images, each graded 3-7 times by a panel of 54 US-licensed
             ophthalmologists and senior residents, with the reference standard set by
             majority decision. On the EyePACS-1 validation set (9,963 images from 4,997
             patients) the algorithm reached, at its high-specificity operating point,
             90.3% sensitivity and 98.1% specificity for referable DR, and at its
             high-sensitivity point 97.5% sensitivity and 93.4% specificity; AUC 0.991.
             On Messidor-2 (1,748 images from 874 patients) AUC was 0.990. The conclusion:
             "An algorithm based on deep machine learning had high sensitivity and
             specificity for detecting referable diabetic retinopathy." Every validation
             image here is a lab-curated, fully gradable photograph, which is the point of
             contrast with the field.
Locators:    Results (operating points, AUC, dataset sizes); Methods (development set,
             54 graders, majority-decision reference standard); Conclusions.
Quote:       "high sensitivity and specificity for detecting referable diabetic retinopathy"
Access note: jamanetwork gates automated curl (403) but returned full content to the
             fetch tool and resolves for a reader. DOI 10.1001/jama.2016.17216.
```

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC6550283/
Kind:        primary. Ruamviboonsuk et al. 2019, npj Digital Medicine. It owns the
             "23% false-negative reduction / 2% higher false positives" figure the CHI
             paper cites (as reference [33]) for the algorithm's edge over human graders.
Establishes: The algorithm's grading performance against the Thai national program's own
             human graders, on retrospective national-program images.
Paraphrase:  Using images from Thailand's national DR screening program (29,985 images,
             25,326 gradable, from 7,517 patients across 13 regions), the deep-learning
             system reached 0.968 sensitivity and 0.956 specificity for moderate NPDR or
             worse (AUC 0.987), versus regional human graders at 0.734 sensitivity and
             0.980 specificity. The system "significantly reduced the false negative rate
             (by 23%) at the cost of slightly higher false positive rates (2%)." Lead
             author Paisan Ruamviboonsuk is at the Department of Ophthalmology, Rajavithi
             Hospital, Bangkok; co-leads Jonathan Krause and Lily Peng are at Google.
Locators:    Abstract; Results (sensitivity/specificity, AUC); reported in CHI 2020 Sec 1.
Quote:       "significantly reduced the false negative rate (by 23%) at the cost of
             slightly higher false positive rates (2%)"
Access note: Open-access PMC page verified resolving (200). Publisher DOI
             10.1038/s41746-019-0099-8 (nature.com redirects bots through an auth cookie).
```

```text
URL:         https://www.thelancet.com/journals/landig/article/PIIS2589-7500(22)00017-6/fulltext
Kind:        primary. Ruamviboonsuk et al. 2022, Lancet Digital Health. This is the
             prospective interventional cohort that the CHI 2020 field study ran alongside,
             reported to completion. It owns the field diagnostic-accuracy result.
Establishes: How the same deployment performed on accuracy once run at scale. This is the
             evidence that the model's accuracy transferred to the field, which sharpens
             (and partly corrects) the commission's framing.
Paraphrase:  Between Dec 12, 2018 and March 29, 2020, 7,940 patients were screened and
             7,651 (96.3%) analyzed at nine primary-care sites under Thailand's national DR
             screening program, with regional retina specialists over-reading every image
             as a safety mechanism. For vision-threatening DR the deep-learning system had
             94.7% accuracy (95% CI 93.0-96.2), 91.4% sensitivity, and 95.4% specificity;
             the retina-specialist over-readers had 93.5% accuracy, 84.8% sensitivity, and
             95.5% specificity. 31.5% of patients were referred (for DR, DME, ungradable
             images, or low visual acuity). The interpretation states the system "can
             deliver real-time diabetic retinopathy detection capability similar to retina
             specialists in community-based screening settings," and that
             "socioenvironmental factors and workflows must be taken into consideration
             when implementing a deep-learning system." Funding: Google and Rajavithi
             Hospital. Registered TCTR20190902002.
Locators:    Abstract (Methods, Findings, Interpretation, Funding).
Quote:       "Socioenvironmental factors and workflows must be taken into consideration
             when implementing a deep-learning system within a large-scale screening
             programme in LMICs."
Access note: Lancet gates bots (403); abstract read in full via Europe PMC
             (EXT_ID:35272972). PMID 35272972; DOI 10.1016/S2589-7500(22)00017-6.
```

```text
URL:         https://blog.google/innovation-and-ai/technology/health/healthcare-ai-systems-put-people-center/
Kind:        primary, for what the operator said. Authored by Emma Beede, the field study's
             lead author, on Google's own blog, published April 25, 2020.
Establishes: Google's public framing of the field findings and the fix it made.
Paraphrase:  Google describes the work as "the first study of its kind that looks at how
             nurses use an AI system to screen patients," across "regular visits to 11
             clinics" over eight months. It acknowledges that "some images captured in
             screening might have issues like blurs or dark areas" and that "an AI system
             might conservatively call some of these images 'ungradable,'" and frames the
             friction as "disagreements between the system and the clinician" that "can
             lead to frustration." Its stated response: amend the protocol so eye
             specialists review ungradable images alongside medical records "instead of
             automatically referring patients," to "reduce unnecessary travel, missed work,
             and anxiety about receiving a possible false positive result." Emphasis falls
             on environmental differences like lighting.
Locators:    Body paragraphs on the study, ungradable images, and the protocol change.
Quote:       "an AI system might conservatively call some of these images 'ungradable'"
Access note: Verified resolving (200).
```

```text
URL:         https://www.technologyreview.com/2020/04/27/1000658/google-medical-ai-accurate-lab-real-life-clinic-covid-diabetes-retina-disease/
Kind:        secondary. MIT Technology Review, Will Douglas Heaven, April 27, 2020. Reports
             on the CHI study from outside the authoring party and adds independent voices.
Establishes: Independent framing of the lab-to-field gap and outside expert reaction.
Paraphrase:  The piece states the model "had been trained on high-quality scans" and "was
             designed to reject images that fell below a certain threshold of quality,"
             that nurses were "scanning dozens of patients an hour and often taking the
             photos in poor lighting conditions," and that "poor internet connections in
             several clinics also caused delays"; "more than a fifth of the images were
             rejected." It quotes Emma Beede, "a UX researcher at Google Health": "We have
             to understand how AI tools are going to work for people in context... before
             they're widely deployed." Independent experts: Hamid Tizhoosh, "at the
             University of Waterloo in Canada, who works on AI for medical imaging," calls
             it "a crucial study for anybody interested in getting their hands dirty and
             actually implementing AI solutions in real-world settings"; Michael Abramoff,
             "an eye doctor and computer scientist at the University of Iowa Hospitals and
             Clinics" and "CEO of a spinoff startup called IDx Technologies," says "I'm so
             glad that Google shows they're willing to look into the actual workflow in
             clinics."
Locators:    Body (cause description, rejection figure, Beede quote, Tizhoosh and Abramoff
             quotes with affiliations).
Quote:       "more than a fifth of the images were rejected"
Access note: Verified resolving (200).
```

```text
URL:         https://techcrunch.com/2020/04/27/google-medical-researchers-humbled-when-ai-screening-tool-falls-short-in-real-life-testing/
Kind:        secondary. TechCrunch, Devin Coldewey, April 27, 2020. Independent report that
             directly weighs Google's framing against the study's contents.
Establishes: The strongest independent challenge to the operator's tone, useful for the
             editor testing the angle.
Paraphrase:  The article attributes the field problems to the system's "stringent
             guidelines regarding the images it will assess," clinic-to-clinic workflow
             variation, and "slower and less reliable connections" causing 60-90 second
             uploads. It observes that Google's own blog "presents a rather sunny
             interpretation of events" despite documented failures including reduced
             screening throughput and nurses discouraging patient participation.
Locators:    Body (root-cause description; the "sunny interpretation" characterization).
Quote:       "the blog post presents a rather sunny interpretation of events"
Access note: Verified resolving (200).
```

```text
URL:         https://arxiv.org/abs/2012.01165
Kind:        secondary. Chinasa T. Okolo, "AI in the 'Real World'," NeurIPS 2020 workshop
             (Navigating the Broader Impacts of AI Research). Independent academic analysis;
             the author is not affiliated with Google.
Establishes: An outside scholar's diagnosis of the cause, locating it in a pre-deployment
             human-centered-design gap rather than in the model.
Paraphrase:  Okolo uses this deployment as a case study. The paper states the system "could
             not handle low-quality images taken in the Thai clinics, as the underlying
             algorithm had originally been trained on high-quality lab images," and that
             overburdened clinic workers "had to take more photos to produce a suitable
             image... lengthening the time spent per visit," compounded by "low internet
             speed/connectivity" and lack of proper screening rooms. Its judgment: "The
             lack of understanding around the existing workflows of analyzing diabetic
             retinopathy in the participating clinics led to the failures of this AI system
             once deployed," and human-centered methods "would have benefited the
             development of the system had they occurred pre-deployment." Note: Okolo says
             the algorithm was trained on scans "from patients in the United States and
             India," citing Gulshan et al. 2019 (JAMA Ophthalmology), a related India
             validation, not the 2016 JAMA paper the CHI study cites for its accuracy claim.
Locators:    Sec 3 "Case Study" (pp. 1-2); references [2] (Beede CHI 2020), [9] (Gulshan
             2019 India).
Quote:       "The lack of understanding around the existing workflows of analyzing diabetic
             retinopathy in the participating clinics led to the failures of this AI system
             once deployed."
Access note: PDF read in full (arxiv.org/pdf/2012.01165), verified resolving.
```

## Contradictions

The commission's central probe: was the failure the model, the images, the workflow, or
the deployment, and how does Google's framing differ from independent observers'? The
sources converge on the facts and split on emphasis and tone.

**The model was not inaccurate; it was conservative by design.** Every primary agrees
the model did not misread images. The CHI study says the system "only assesses the
highest-quality images" and rejects a blurry or dark image "even if it could make a
strong prediction," a threshold chosen "for patient safety reasons" (Sec 6, Gradability).
So the ungradable rate is not a model error. It is a deployment design choice, a
quality gate calibrated for a prospective safety study, colliding with images produced in
the field.

**The images and the environment are where the friction originated.** The CHI study
traces low-quality images to non-darkened rooms, a camera needing repair, and Pathum
Thani clinics not using dilation drops (Sec 6). The model was trained on curated, fully
gradable photographs (Gulshan 2016, Methods); the field supplied photographs taken under
fluorescent light with 90 seconds allotted per patient (CHI Sec 6, Volume). This is the
lab-versus-field distribution difference the lesson teaches.

**The workflow and infrastructure amplified it.** Ungradable results forced retakes
(2-4 minutes per patient, never a third try because of the flash; CHI Sec 6). Slow
uploads (60-90 seconds) and a two-hour outage that halved throughput (200 to 100) were
connectivity, not model, failures. Referral logistics, an hour's drive to Pathum Thani
Hospital, drove nurse workarounds and consent opt-outs (up to 50% at clinic 4).

**The frames diverge on tone and on where to lay the lesson.** The CHI authors, who are
Google's team, name the cause as a threshold-versus-environment tension and present the
protocol fix as a positive iteration (Sec 7). Google's blog is more optimistic still,
calling ungradable calls "conservative" and stressing lighting. TechCrunch flags this
directly: the blog "presents a rather sunny interpretation of events." Okolo, an outside
scholar, is sharpest, locating the failure in a *pre-deployment* human-centered-design gap
that should have surfaced the workflow realities earlier. MIT Technology Review sits
between: it reports the facts plainly and lets outside experts (Abramoff, Tizhoosh) credit
Google for studying the real workflow at all.

**The largest tension is with the commission's own wording.** The commission frames the
lesson as bench accuracy that "does not transfer to outcomes in the room." The Lancet 2022
follow-up on the same program shows the model's diagnostic accuracy *did* transfer: 94.7%
field accuracy, on par with retina specialists. What did not transfer was smooth
throughput and patient experience, because the image-quality gate rejected a fifth of real
images and the surrounding system (connectivity, referral distance, patient volume) was
not the test set. The honest lesson is the sociotechnical gap: a validated model can score
well and still degrade care if the deployment around it is not designed for the real
environment. The writer should not say field accuracy collapsed; it did not.

**One naming caution.** The primaries name the operator as "Google" (later "Google
Health") in partnership with Rajavithi Hospital under Thailand's Ministry of Public
Health; the Lancet 2022 funding line reads "Google and Rajavithi Hospital." Verily
(Alphabet's life-sciences company) appears in some 2016-era coverage of the broader
diabetic-eye-disease effort but is not named in the CHI or Lancet primaries for this Thai
clinic deployment. Attribute the deployment to Google / Google Health unless a source ties
Verily specifically to it.

## Numbers

```text
Figure: 21% ungradable (393 of 1,838 uploaded images)
Owner:  CHI 2020 (Beede et al.), Sec 6, Gradability
Scope:  First six months of usage, across the three Pathum Thani deployment clinics
        (Klong Luang, Nongsue, Lamlukka). System-log count, not a per-patient rate.
```

```text
Figure: >90% sensitivity and specificity (lab claim, as stated in the field study)
Owner:  Gulshan 2016 (JAMA); restated in CHI 2020 Sec 1
Scope:  Referable DR on curated validation sets. Exact EyePACS-1 operating points:
        90.3% sensitivity / 98.1% specificity (high-specificity), 97.5% / 93.4%
        (high-sensitivity); AUC 0.991.
```

```text
Figure: 128,175 images (development set), graded by 54 ophthalmologists/residents
Owner:  Gulshan 2016 (JAMA), Methods
Scope:  Training/development data; 3-7 grades per image, majority-decision reference.
```

```text
Figure: 60-90 seconds per image upload on slow connections
Owner:  CHI 2020, Sec 6, Internet speed and connectivity
Scope:  Observed at study clinics; a strong connection returned results in "a few seconds."
```

```text
Figure: 200 to 100 patients (single-clinic throughput drop during a two-hour outage)
Owner:  CHI 2020, Sec 6, Internet speed and connectivity
Scope:  One clinic, one internet-outage event.
```

```text
Figure: up to 50% opt-out (clinic 4); nurse P6 estimate "40-50% don't join"
Owner:  CHI 2020, Sec 6, Consenting patients
Scope:  Consent into the prospective study at specific clinics, driven by referral-travel
        fears, not a population screening rate.
```

```text
Figure: 23% relative reduction in false-negative rate, at 2% higher false positives
Owner:  Ruamviboonsuk 2019 (npj Digital Medicine); cited in CHI 2020 Sec 1
Scope:  Algorithm vs human graders, retrospective national-program images.
```

```text
Figure: Field accuracy 94.7% (95% CI 93.0-96.2), sensitivity 91.4%, specificity 95.4%
Owner:  Ruamviboonsuk 2022 (Lancet Digital Health)
Scope:  Vision-threatening DR; 7,651 analyzed patients, 9 sites, Dec 2018-Mar 2020;
        adjudicated reference standard. Over-readers: 93.5% / 84.8% / 95.5%.
```

```text
Figure: 31.5% of patients referred
Owner:  Ruamviboonsuk 2022 (Lancet Digital Health)
Scope:  Referred for DR, DME, ungradable images, or low visual acuity, in the field cohort.
```

```text
Figure: Thailand specialist shortage: ~1,500 ophthalmologists, 200 retinal specialists,
        ~4.5 million diabetic patients (ratio ~1:3000)
Owner:  CHI 2020, Sec 1 (citing Thai national survey data, ref [23])
Scope:  National context motivating the screening program; MoPH target 60% screened,
        actual under 50% annually since 2013.
```

```text
Figure: 9.6% of Thailand's population living with diabetes (2016)
Owner:  CHI 2020, Sec 1 (citing WHO country profile, ref [40]); comparison anchor:
        9.1% in the United States (ref [41])
Scope:  National prevalence, 2016.
```

## Source assets

```text
Asset: CHI 2020 Figure 2, "Eye screening process before and after deployment of the deep
       learning system" (workflow diagram).
Shows: The exact step the tool added, an upload-to-cloud-for-real-time-assessment stage
       inserted into the nurse's existing photograph-and-refer flow. This is the clearest
       single visual of where the sociotechnical friction enters.
Crop:  Must retain both the before and after lanes so the added upload/return step reads;
       omit nothing that distinguishes pre- from post-deployment.
```

```text
Asset: CHI 2020 Figure 5, a nurse forming a composite of one eye from two ungradable
       photos taken with varied lighting.
Shows: The concrete workaround the quality gate forced, and why it failed: the system
       needs one high-quality image per eye and cannot assemble a composite. Grounds the
       ungradability finding in a real act at the camera.
Crop:  Retain both half-images and enough of the retinal field to see they are top and
       bottom of the same eye; a caption must state the system could not use the composite.
```

```text
Asset: CHI 2020 Figure 3, the web application showing the model's DR and DME predictions
       beside the fundus photos.
Shows: What the nurse actually saw, the interface where an "ungradable" verdict or a
       referral recommendation appeared in real time.
Crop:  Retain the prediction labels alongside the image; omit only if patient-identifying
       detail is present (the study used case numbers, so likely none).
```

```text
Asset: A lab-versus-field accuracy comparison the writer could build as a committed chart
       (spec/charts.md), not a source image: lab operating points (Gulshan 2016) beside
       the 2022 field accuracy and the 21% ungradable share.
Shows: That accuracy transferred while a fifth of images never reached scoring. Honest
       framing requires labeling the ungradable share as a separate bar, not folded into
       accuracy.
Crop:  N/A (rendered chart). Cite Gulshan 2016, CHI 2020, and Ruamviboonsuk 2022 in the
       caption; note the two operating points are distinct thresholds.
```

## Discarded

```text
URL: https://vibegraveyard.ai/story/google-diabetic-retinopathy-thailand/ — unverifiable
     aggregator with no byline or sourcing; every figure it carries is available in the
     primaries. Not cited.
URL: https://www.newsweek.com/... and https://www.engadget.com/... — same-day April 2020
     rewrites of the CHI study and Reuters/AP wire; redundant with MIT and TechCrunch and
     add no independent reporting or framing.
URL: https://www.nature.com/articles/s41746-019-0146-5 — the Author Correction to the 2019
     npj paper, not the paper itself; the substantive figures live in PMC6550283.
URL: https://hlth.com/... and https://www.mobihealthnews.com/... (2024 model-licensing
     news) — a later commercial development, outside this incident's boundary.
URL: https://blog.google/.../arda-diabetic-retinopathy-india-thailand/ — Google promotional
     retrospective; the operator's account is better carried by the 2020 Beede blog written
     at the time of the study.
```
