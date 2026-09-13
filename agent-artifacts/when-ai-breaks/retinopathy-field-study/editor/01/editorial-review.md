# Editorial review: when-ai-breaks/retinopathy-field-study (editor/01)

## Skeptic

Thesis: a diabetic-retinopathy model that scored like an ophthalmologist on
curated images kept that diagnostic accuracy in a Thai field program (94.7%,
matching the specialists who over-read the same images), and the deployment
still cost patients care, because a conservative image-quality gate refused a
fifth of the photographs nurses actually took and the surrounding workflow
(cloud upload over weak internet, an hour's drive to referral) was not the test
set. The lesson: a benchmark score is silent about how many real inputs a
system will accept and what the people around it must do when it says no.

The four claims it stands on, and how each held:

1. Lab pedigree. 90.3% sensitivity / 98.1% specificity for referable DR on the
   EyePACS-1 curated set; trained on 128,175 images graded 3-7 times by 54
   ophthalmologists and residents (Gulshan 2016, s2). Matches the evidence
   Numbers exactly; the article picks the high-specificity operating point and
   is consistent about it later. Held.

2. Field accuracy transferred. 94.7% field accuracy for vision-threatening
   disease vs 93.5% for the retina-specialist over-readers (Ruamviboonsuk 2022,
   Lancet, s7). This is the round's core correctness point, and the draft holds
   it: it never claims accuracy collapsed. Held.

3. The 21% ungradable rate. 393 of 1,838 images in the first six months across
   the three Pathum Thani clinics (CHI 2020, s1). The draft carries that scope
   in the sentence where the figure appears, and again in the chart caption.
   Held.

4. The failure was the quality gate and the workflow, not model error. Every
   primary agrees the model did not misread images; the gate was chosen "for
   patient safety" and refused blurry or dark images "even if it could make a
   strong prediction" (s1). Held.

I pushed hardest on the claim I most wanted to keep, the reconciliation in the
"Why a good model still failed" section, and found one break there. The draft
explained the refusals by asserting the quality gate was "calibrated during a
lab-grade validation study" and "set on clean data too." The evidence record
does not own that provenance; it frames the gate as a threshold set high for
patient safety colliding with field images, and if anything attributes its
stringency to the prospective safety study, not a lab validation. I did not have
the reporting to settle where the gate's threshold was calibrated, so rather
than route a non-central sub-claim I cut the unsupported provenance and rebuilt
the sentence from facts the record does own: the gate was set high for patient
safety, accuracy held on the images it did grade, so the same distribution shift
that might have shown up as wrong answers showed up instead as no answer at all.
The article's own claim survives on sourced ground.

Display text, descriptor by descriptor: headline actor (Google) matches the
corrected attribution (Google/Google Health with Rajavithi Hospital and the
MoPH, not Verily); "a fifth" tracks the 21% figure. The dek's "as accurately as
a retina specialist" is the 94.7% vs 93.5% result, and "tuned high for patient
safety" is sourced; the dek makes a claim about the world, not a grade of the
article's method. Every named person's role checks out against the owning
primary: Emma Beede (field study lead author, on Google's blog), Chinasa Okolo
(unaffiliated with Google), Michael Abramoff (eye doctor and computer scientist,
University of Iowa), Hamid Tizhoosh (University of Waterloo). Quotes are accurate;
ellipses in the Tizhoosh and Lancet quotes are honest truncations that do not
distort. Every figure carries its denominator and period: 393/1,838 first six
months; 60-90s uploads; 200-to-100 outage at one clinic; 40-50% opt-out by one
nurse's estimate at one clinic. Directions are correct (23% false-negative
reduction; a fifth refused). The specialist ratio (4.5M / 1,500 = 1:3,000) was
attributed to a loose "one specialist" after naming both ophthalmologists and
retinal specialists; I made it "one eye doctor" so the arithmetic reads against
the 1,500 it uses.

data-nb-kind audit: s1/s2/s3/s7 primary (the field study, the validation paper,
the 2019 grading comparison, the Lancet follow-up), s6 primary for what the
operator said (Beede on Google's blog), s4/s5/s8 secondary (MIT Tech Review,
TechCrunch, Okolo). All consistent with the evidence record and with the
primary/secondary test; the Google blog is correctly labeled primary for the
operator's own framing, not for the field facts, which are carried by s1/s7.
Source floor met: 8 sources, 5 primary / 3 secondary. The two internal cross
links (waymo-recall, epic-sepsis-model) resolve in the library checkout; source
hrefs match the evidence-record URLs. The ACM, JAMA, and Lancet links gate
automated bots (documented in the draft handoff) but resolve for a reader; the
writer's proof passed --check-links.

One sourcing gap remains and is routed below: the opening epidemiological claim
that diabetic retinopathy "is a leading cause of blindness in working-age
adults" carries no citation, and the evidence record does not record it. It is
almost certainly owned by the intro of s1 or s2, but I cannot attach a citation
to a passage I have not opened, and it is a specific, checkable claim rather than
a bare definition.

## Cut

The draft came in clean; the slop load was light. One sentence failed the test
outright: "The reasons were mundane and physical," an empty setup ("the X were Y
and Z") whose work the concrete list of causes right after it already does. I
cut it and let the darkened rooms, the broken camera, and the dropped dilation
drops carry the point, which is the voice guide's own discipline.

Edge pass, read out of order: the openers and closers hold. "The trouble began
at the camera," "Ungradable images were the most visible failure," and "The
clinics were the environment the system was for" each assert something the
paragraph then earns; "most visible failure" is the CHI authors' own ranking
("ungradability had the largest impact"). The article's last sentence resolves
the opener and states the conclusion the argument built, so it stays.

Borrowed phrasing: the sentence "The easy explanation is that the clinics and
the nurses were not ready for the technology" reproduced, almost word for word,
the voice guide's own coaching sentence ("The easy version here is that the
clinics or the nurses were not ready for the technology"). The Langewiesche move
underneath it (name the easy account, set it aside, spend the piece on the
harder one) is legitimate and the guide explicitly asked for it, and the point
is supported by Okolo, so I rewrote the line in the article's own terms ("The
comfortable reading is that the clinics simply could not keep up with the
technology") rather than cutting it. No phrasing was lifted from the exemplar
authors themselves.

Prompt leakage: none. The article teaches the "sociotechnical gap" without using
the brief's label, teaches distribution shift by linking waymo-recall rather
than re-teaching it, and states no claim that it fulfilled its assignment.

Negative parallelism: the takeaway's "the useful question is not whether the
number is real. It is whether anyone has watched the system work where it will
be used" is the earned kind. The misconception it corrects (that the live
question is whether the benchmark is honest) is the exact one the whole piece
dismantles, so it survives.

Two accuracy edits for precision: "how a system behaves" in the Why bookend
overclaimed against the piece's own correction (accuracy did transfer, so
behavior was partly predictable), so I changed it to "how a system will serve
the people it screens," which is the deployment outcome the lesson is actually
about and ties the opener to the takeaway. And the TechCrunch line attributed
its "sunny interpretation" verdict to "Google's own account of the work" when
TechCrunch was characterizing the blog post specifically; I tightened it to
"Google's own blog post about it."

Term consistency: the body twice said "sight-threatening" while the primary
(s7) and the committed chart say "vision-threatening." I aligned the 94.7%
sentence to "vision-threatening" (its own source), and changed the earlier
"sight-threatening cases" to "referable cases," which is what the 2019 grading
comparison (s3, moderate NPDR or worse) actually measured and is the term the
orientation section already established.

Punctuation and grammar: clean. No em-dashes, no semicolons, colons used to
introduce what the clause promises. No grammatical breaks in body or display
text.

Recent-pattern check against the When AI Breaks record: the headline keeps the
desk's named-actor + hard-number discipline (Google, a fifth) without copying a
recent piece's distinctive shape; it reads as the house style, not an echo of
one article. The two-sentence dek avoids the recent one-sentence molds and the
three banned dek forms (its closing "undarkened rooms, slow clinic internet, and
photographs..." is a list of collision points, not the clause-triad the standard
warns against). The five section headings are this incident's own steps, no stock
labels.

## Reader

Read straight through, the piece gives the reader something no single source
does: the model's lab pedigree, its 94.7% field accuracy (Lancet 2022), and the
21% ungradable rate (CHI 2020) set in one frame so the failure reads as a
quality-gate-and-workflow gap rather than an accuracy collapse. Those two field
numbers live in two different papers; putting them together and reading
distribution shift off the gap is the article's own work, and it matches the
original-work sentence in the handoff. The prose sits closer to the voice-guide
exemplars than to a median summary: the arithmetic is worked on the page
(1:3,000; 393 of 1,838; 200 to 100), the nurses and patients stay on the page as
people through what they did rather than adjectives, and the verdict on the
deployment arrives spare, through Okolo's plain words. The headline, read last as
the largest claim, is defended by the body.

## Edits

- Why bookend: "how a system behaves once real people, cameras, and clinics are
  in the loop" -> "how a system will serve the people it screens once real
  cameras, clinics, and connections are in the loop" (accuracy: the benchmark did
  predict field accuracy; the gap is deployment outcome).
- Orientation: "one specialist for every three thousand" -> "one eye doctor for
  every three thousand" (removes referent ambiguity; the 1:3,000 ratio uses the
  1,500 ophthalmologists).
- Orientation: "missing fewer sight-threatening cases" -> "missing fewer
  referable cases" (matches what s3 measured and the section's own term).
- The-images: cut "The reasons were mundane and physical." (slop; concrete list
  carries it).
- The-room: "Google's own account of the work" -> "Google's own blog post about
  it" (matches what TechCrunch actually characterized).
- Why-it-failed: "field accuracy for sight-threatening disease" -> "for
  vision-threatening disease" (term matches s7 and the chart).
- Why-it-failed: rewrote the quality-gate sentence to drop the unsupported
  "calibrated during a lab-grade validation study" / "set on clean data"
  provenance; rebuilt from sourced facts (gate set high for patient safety;
  accuracy held on graded images; the shift showed up as no answer, not a wrong
  one).
- Why-it-failed: "The easy explanation is that the clinics and the nurses were
  not ready for the technology" -> "The comfortable reading is that the clinics
  simply could not keep up with the technology" (de-echo the voice guide's own
  coaching sentence).

## Required work

- writer: Source the opening epidemiological claim that diabetic retinopathy
  "is a leading cause of blindness in working-age adults" (and the paired "caught
  early it can be treated before sight is lost"). It carries no citation and is
  not in the evidence record. If the intro of s1 (CHI 2020) or s2 (Gulshan 2016)
  owns it, extend that citation to the clause; if no held source owns it, cut the
  clause. This is the only publication-blocking item.

Chart: inspected and correct, no work required. The provenance in chart-1.py
(94.7% Ruamviboonsuk 2022; 93.5% over-readers; 21% CHI 2020) matches the evidence
record and cited primaries. Read as a reader, the image is honest: 0-100 percent
axis, the ungradable share in a distinct color and its own legend series so it is
never folded into an accuracy number, data labels present, and a caption that
states the third bar is the share never graded while the first two measure
grading on accepted images.

## Decision

revise: the article is sound and its corrected thesis holds after my edits; one
uncited, checkable epidemiological claim needs the writer to attach a source or
cut it before it can publish.
