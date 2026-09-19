# Evidence: when-ai-breaks/amazon-rekognition-congress (01)

The primaries pin the incident cleanly. The ACLU's own post fixes the date, the
gallery of 25,000 arrest photos, the 535 probe faces, the default settings, the
28 false matches, the demographic skew, and the $12.33 cost. Amazon's two Matt
Wood blog posts and its June 2020 statement give its rebuttal and its
moratorium in the company's own words. The threshold mechanism (80% default vs.
99% recommended) and the gallery-size mechanism are firmly sourced. The
demographic mechanism is where the record needs care, and the writer must
respect one boundary. Two facts do the cutting. First, the ACLU's demographic
result is a description of 28 matches, not a measured per-group error rate.
Second, the audits Amazon disputes (Gender Shades, Raji/Buolamwini) measured
*gender classification*, guessing a binary gender from a face, which is a
different task from the face *matching* the ACLU test and real police use
involve. The one primary that measured demographic differentials in face
recognition itself, NIST's NISTIR 8280, did not test Rekognition, because Amazon
did not submit it. So the general mechanism is proven and the direction of the
error gap is measured; the specific claim that Rekognition's *matching* is
demographically biased rests on the ACLU demonstration plus inference from
related systems, not on a controlled test of Rekognition's matching. This does
not undermine the commissioned angle. It marks the line the writer draws between
what is measured and what is inferred.

## Sources

```text
URL:         https://www.aclu.org/news/privacy-technology/amazons-face-recognition-falsely-matched-28
Kind:        primary. The ACLU of Northern California ran the test and owns the result.
Establishes: The incident's facts firsthand: date, method, gallery, count, skew, cost.
Paraphrase:  In a test whose results were published July 26, 2018, the ACLU of
             Northern California used Amazon Rekognition to compare photos of
             every member of Congress against a database of 25,000 publicly
             available arrest photos, using the tool's default match settings.
             Rekognition returned 28 false matches. Nearly 40% of the false
             matches were people of color, though people of color make up only
             about 20% of Congress. Six members of the Congressional Black
             Caucus were among the 28, including the late Rep. John Lewis
             (D-Ga.). The scan cost $12.33.
Locators:    Body of the post; author line; the members-of-color and cost paragraphs.
Quote:       "These results demonstrate why Congress should join the ACLU in
             calling for a moratorium on law enforcement use of face
             surveillance." Author: Jacob Snow, Technology and Civil Liberties
             Attorney, ACLU Foundation of Northern California.
```

```text
URL:         https://aws.amazon.com/blogs/aws/thoughts-on-machine-learning-accuracy/
Kind:        primary. Amazon's own response to the ACLU test.
Establishes: Amazon's threshold defense, in its own words, dated July 27, 2018.
Paraphrase:  Amazon argues the ACLU used the wrong confidence threshold. The
             API default is 80%, which Amazon says suits general use but not
             public safety; for law enforcement it recommends 99%. Amazon says
             it re-ran a similar test at 99% and got zero misidentifications
             against a corpus 30x larger than the ACLU's. It stresses
             Rekognition is meant to narrow a field for human review, not to
             make an identification on its own. Author: Dr. Matt Wood, General
             Manager of Deep Learning and AI, AWS.
Locators:    Sections on confidence thresholds and on the ACLU test.
Quote:       "The default confidence threshold for facial recognition APIs in
             Rekognition is 80%, which is good for a broad set of general use
             cases (such as identifying celebrities on social media or family
             members who look alike in photos apps), but it's not the right
             setting for public safety use cases."
             "We recommend 99% for use cases where highly accurate face
             similarity matches are important (as indicated in our public
             documentation)."
             "When we set the confidence threshold at 99% (as we recommend in
             our documentation), our misidentification rate dropped to zero
             despite the fact that we are comparing against a larger corpus of
             faces (30x larger than the ACLU test)."
             "We should not throw away the oven because the temperature could be
             set wrong and burn the pizza."
```

```text
URL:         https://aws.amazon.com/blogs/machine-learning/thoughts-on-recent-research-paper-and-associated-article-on-amazon-rekognition/
Kind:        primary. Amazon's own response to the Raji/Buolamwini audit.
Establishes: Amazon's argument that the audits measured the wrong task, dated January 26, 2019.
Paraphrase:  Amazon argues facial analysis (finding generic attributes such as
             gender) and facial recognition (matching a face to an identity) are
             different technologies trained on different data, and that the
             research used facial analysis as a proxy for facial recognition.
             Amazon says its own gender-classification test on more than 12,000
             images found no significant accuracy difference across ethnicities,
             and that a Rekognition test against the 1-million-image MegaFace set
             produced zero false positives at the 99% threshold. Author: Dr.
             Matt Wood, General Manager of Artificial Intelligence, AWS.
Locators:    Sections distinguishing analysis from recognition and reporting Amazon's own tests.
Quote:       "Facial analysis and facial recognition are completely different in
             terms of the underlying technology and the data used to train
             them."
             "Using facial analysis to do facial recognition is an inaccurate
             and unadvised way to identify unique individuals."
             "Across all ethnicities, we found no significant difference in
             accuracy with respect to gender classification."
```

```text
URL:         https://www.aclu.org/press-releases/aclu-comment-new-amazon-statement-responding-face-recognition-technology-test
Kind:        primary. The ACLU's reply to Amazon's rebuttal.
Establishes: The ACLU's counterargument and Amazon's shifting threshold numbers.
Paraphrase:  Responding to Amazon the same week, the ACLU says Amazon's numbers
             kept moving and that a recommended threshold does not fix an
             out-of-the-box default police can use. It notes Amazon's own June
             2017 instructional post with Washington County set the threshold at
             85%, not 95% or 99%. Author: Jacob Snow, ACLU Foundation of
             Northern California.
Locators:    Snow's quoted statement; the reference to the 2017 Washington County post.
Quote:       "Amazon has gone from its own system default of an 80 percent match
             rate to saying yesterday it should be 95 percent, and then saying
             today it should be 99 percent."
             "At no time has Amazon taken any responsibility for the very grave
             impact that their face surveillance product has on real people."
```

```text
URL:         https://www.aboutamazon.com/news/policy-news-views/we-are-implementing-a-one-year-moratorium-on-police-use-of-rekognition
Kind:        primary. Amazon's own moratorium statement.
Establishes: The June 10, 2020 one-year moratorium, in Amazon's words.
Paraphrase:  Amazon announces a one-year pause on police use of Rekognition and
             asks Congress to pass rules for the technology. It carves out
             continued access for Thorn, the International Center for Missing and
             Exploited Children, and Marinus Analytics, for anti-trafficking and
             missing-children work. The announcement came amid the protests
             following George Floyd's death and one day after IBM exited
             general-purpose face recognition.
Locators:    The full statement (four short paragraphs).
Quote:       "We're implementing a one-year moratorium on police use of Amazon's
             facial recognition technology."
             "We hope this one-year moratorium might give Congress enough time to
             implement appropriate rules, and we stand ready to help if
             requested."
```

```text
URL:         https://www.aies-conference.com/2019/wp-content/uploads/2019/01/AIES-19_paper_223.pdf
Kind:        primary. Raji & Buolamwini own these measurements.
Establishes: Rekognition's measured gender-classification error by subgroup, August 2018.
Paraphrase:  "Actionable Auditing" (AAAI/ACM Conference on AI, Ethics, and
             Society, 2019) extended the Gender Shades method to Amazon
             Rekognition and Kairos. On the Pilot Parliaments Benchmark as of
             August 2018, Rekognition's overall gender-classification error was
             8.66%. It made no errors on lighter-skinned males (0.0%) and erred
             on 31.37% of darker-skinned females, an error gap of 31.37
             percentage points, the worst of any company in the follow-up. This
             is gender classification, not face matching. Authors: Inioluwa
             Deborah Raji and Joy Buolamwini.
Locators:    Abstract; Table 1 (Overall Error on Pilot Parliaments Benchmark,
             August 2018); "Non-Target Corporation Key Findings."
Quote:       "Kairos (22.5% error) and Amazon (31.4% error) have the current
             worst performance for the darker female subgroup." "Amazon has an
             error gap of 31.37%."
```

```text
URL:         http://proceedings.mlr.press/v81/buolamwini18a/buolamwini18a.pdf
Kind:        primary. Buolamwini & Gebru own these measurements.
Establishes: The original audit's error gaps, and that it did not test Amazon.
Paraphrase:  "Gender Shades" (Proceedings of Machine Learning Research vol. 81,
             Conference on Fairness, Accountability and Transparency, 2018)
             audited three commercial gender-classification systems: Microsoft,
             Face++, and IBM. Amazon was not among them. Darker-skinned females
             were the most misclassified group, with error rates up to 34.7%,
             while the maximum error for lighter-skinned males was 0.8%. Authors:
             Joy Buolamwini and Timnit Gebru.
Locators:    Abstract; the intersectional results.
Quote:       "darker-skinned females are the most misclassified group (with error
             rates of up to 34.7%). The maximum error rate for lighter-skinned
             males is 0.8%."
```

```text
URL:         https://nvlpubs.nist.gov/nistpubs/ir/2019/nist.ir.8280.pdf
Kind:        primary. NIST ran and owns this evaluation.
Establishes: Measured demographic differentials in face recognition (not classification).
Paraphrase:  NISTIR 8280, "Face Recognition Vendor Test (FRVT) Part 3:
             Demographic Effects" (December 2019), tested one-to-one and
             one-to-many algorithms from many developers on operational photo
             sets. Its main finding is that false-positive (false-match)
             differentials across demographic groups are large and broad, often
             a factor of 10 to beyond 100. On higher-quality application photos,
             false positives are highest for West and East African and East Asian
             faces and lowest for Eastern Europeans. On U.S. mugshots, the
             one-to-many case that matches the ACLU scenario, false positives are
             highest for American Indians, with elevated rates for African
             American and Asian faces. False positives are higher for women than
             men, and elevated for the elderly and for children. Authors: Patrick
             Grother, Mei Ngan, Kayee Hanaoka. Rekognition was not among the
             submitted algorithms; Amazon did not submit it.
Locators:    Executive summary (main-result paragraph and the false-positive bullets).
Quote:       "Across demographics, false positives rates often vary by factors of
             10 to beyond 100 times."
             "With domestic law enforcement images, the highest false positives
             are in American Indians, with elevated rates in African American and
             Asian populations."
             "We found false positives to be higher in women than men, and this
             is consistent across algorithms and datasets. This effect is smaller
             than that due to race."
```

```text
URL:         https://www.technologyreview.com/2020/06/12/1003482/amazon-stopped-selling-police-face-recognition-fight/
Kind:        secondary. Reports on the campaign from outside the parties.
Establishes: Context and the arc from the 2018 test and the audits to the moratorium; held up.
Paraphrase:  MIT Technology Review reports that the ACLU's Congress test and the
             Gender Shades / Raji-Buolamwini research drove a multi-year campaign,
             that Amazon first published blog posts calling the work misleading
             while internally hiring a fairness lead and improving the model, and
             that the June 10, 2020 moratorium was narrow: vague on non-police
             agencies such as ICE and DHS, and time-limited. It restates the
             Rekognition gap as 31.4 percentage points, matching the primary.
             Author: Karen Hao.
Locators:    Throughout; the timeline of Amazon's public and internal responses.
Quote:       (No unique quote needed; used for context and the response timeline.)
Caution:     The piece dates the ACLU Congress test to 2019. The primary dates it
             to July 2018; the primary governs.
```

## Contradictions

The central dispute is Amazon versus the ACLU and the auditors, and each side is
partly right.

Amazon's strongest case (Matt Wood, July 2018 and January 2019). The ACLU used
the 80% default, and Amazon recommends 99% for identification. Amazon's own
retest at 99% produced zero misidentifications against a corpus 30x larger, and
a separate Rekognition test against MegaFace's one million images produced zero
false positives at 99%. Amazon also argues the audits measured facial analysis,
gender guessing, not the face matching at issue, so the 31.37% figure is not a
matching error rate. NIST supports the narrow logic: the most accurate
algorithms produce fewer errors and smaller differentials, and a higher
threshold lowers false positives.

The ACLU and auditors' strongest case (Snow, July 2018; Raji/Buolamwini 2019;
NIST 2019). The default is what an operator gets out of the box, and Amazon does
not require 99% or gate the API on it; Amazon's own recommended number moved from
85% (its 2017 Washington County post) to 95% to 99% within days of the test.
NIST establishes, on face recognition proper, that false-match rates differ
sharply by group and that on U.S. mugshots the differential runs against
American Indian, African American, and Asian faces and against women. So the
uneven landing of false matches is a measured property of face recognition, not
an artifact of the ACLU's method.

What independent evidence settles it. Three quantities decide the case:
calibrated thresholds, the gallery size, and measured per-group error rates from
independent testing. On thresholds and gallery size the mechanism is settled: a
score cutoff tuned for one use is wrong for identification, and a one-to-many
search over 25,000 faces gives many chances for a false positive. On per-group
error the honest reading is split. Raising the threshold lowers the overall
false-positive rate, which is Amazon's point, but does not by itself equalize the
rate across groups, which is NIST's. The clean test that would settle
Rekognition's *own* matching bias, a NIST-style one-to-many demographic
evaluation of Rekognition at a stated threshold, does not exist, because Amazon
did not submit Rekognition to NIST. Amazon's stated reason is that a cloud
service cannot be downloaded and tested in isolation; 99 other developers did
submit. That gap is the record's most important limitation.

Contradiction against the commission: none that breaks the angle. The commission
already routes the cause through "calibrated thresholds, the gallery size, and
measured per-group error rates from independent testing," which is exactly where
the evidence lands. The only correction is precision: the 31.37% audit figure and
the 34.7% Gender Shades figure are gender-classification errors, not
face-matching errors, and Gender Shades did not test Amazon at all. The writer
should use them to establish that measured demographic gaps in facial systems
are real, and use NIST for the gap in matching, without implying either number
is the false-match rate behind the 28.

## Numbers

```text
Figure: 535 members of Congress (probe faces)
Owner:  ACLU (aclu.org post)
Scope:  All sitting members, run as probes against the gallery, July 2018.
```

```text
Figure: 25,000 publicly available arrest photos (gallery size)
Owner:  ACLU (aclu.org post)
Scope:  The enrollment gallery searched, July 2018.
```

```text
Figure: 80% (default confidence threshold); 99% (Amazon's recommended threshold for law enforcement)
Owner:  Amazon (Matt Wood, "Thoughts on Machine Learning Accuracy")
Scope:  Rekognition API default vs. Amazon's documented recommendation.
```

```text
Figure: 28 false matches
Owner:  ACLU (aclu.org post)
Scope:  Rekognition candidate matches at default settings, 535 probes against 25,000 photos.
```

```text
Figure: ~40% of false matches were people of color; people of color ~20% of Congress
Owner:  ACLU (aclu.org post)
Scope:  Descriptive breakdown of the 28 matches. Small sample, not a per-group error rate.
```

```text
Figure: 6 members of the Congressional Black Caucus among the 28 (incl. Rep. John Lewis, D-Ga.)
Owner:  ACLU (aclu.org post)
Scope:  Named subset of the 28 false matches.
```

```text
Figure: $12.33 (cost of the test)
Owner:  ACLU (aclu.org post)
Scope:  Total AWS charge for the July 2018 scan.
```

```text
Figure: Rekognition gender classification: 8.66% overall; 0.0% lighter male; 31.37% darker female; 31.37 pp gap
Owner:  Raji & Buolamwini, "Actionable Auditing" (AIES 2019), Table 1
Scope:  Pilot Parliaments Benchmark, Rekognition version as of August 2018. Gender classification, not matching.
```

```text
Figure: Gender Shades: darker-female error up to 34.7%; lighter-male max error 0.8%
Owner:  Buolamwini & Gebru, "Gender Shades" (PMLR v81, 2018)
Scope:  Microsoft, Face++, IBM gender classifiers, 2017-2018. Amazon not tested.
```

```text
Figure: Face-recognition false-positive differentials often 10x to >100x across groups
Owner:  NIST, NISTIR 8280 (Dec 2019)
Scope:  One-to-one and one-to-many algorithms from many developers; Rekognition not among them.
```

```text
Figure: Amazon retest at 99%: zero misidentifications on a corpus 30x the ACLU test; zero false positives against MegaFace (1M images) at 99%
Owner:  Amazon (Matt Wood, July 2018 and January 2019 posts)
Scope:  Amazon's own unaudited internal tests.
```

## Source assets

```text
Asset: Table 1, "Overall Error on Pilot Parliaments Benchmark, August 2018 (%)," in the Actionable Auditing paper.
Shows: Every company's error by subgroup side by side; Rekognition's 0.0% lighter-male vs 31.37% darker-female contrast in one row.
Crop:  Must retain the Amazon row and the column headers (All, Females, Males, Darker, Lighter, DF, DM, LF, LM). Omit nothing that identifies which figure is which subgroup.
```

```text
Asset: The false-positive-by-demographic figures in NISTIR 8280 (the demographic false-match plots referenced in the executive summary).
Shows: How far false-match rates diverge across groups, the visual form of the "10x to 100x" claim.
Crop:  Must retain the axis labels and the demographic legend; a crop that drops the scale misstates the size of the gap.
```

```text
Asset: The composite of the 28 falsely matched members' official photos on the ACLU post.
Shows: The scale and the human specifics of the false matches, including named members.
Crop:  Confirm the exact form on the live page before use; do not assert a layout the writer has not opened.
```

## Discarded

```text
URL: https://en.wikipedia.org/wiki/Amazon_Rekognition — encyclopedia summary; used only to locate primaries, cited none.
URL: https://www.geekwire.com/2018/amazon-challenges-aclu-study-facial-recognition-tech-police/ — secondary retelling of Amazon's rebuttal; the AWS posts own those quotes directly.
URL: https://www.fastcompany.com/90209609/amazon-fires-back-on-aclu-congressional-face-recognition-finding — secondary; superseded by the primary AWS post.
URL: https://www.npr.org/2020/06/10/874418013/amazon-halts-police-use-of-its-facial-recognition-technology — returned HTTP 503; the moratorium primary and MIT Technology Review cover the same ground.
URL: https://www.theverge.com/2020/6/10/21287101/... — fetch blocked; not needed once the primary statement and MIT Technology Review were read.
URL: https://privacysos.org/blog/five-fast-facts-from-the-federal-study-of-demographic-bias-in-facial-recognition/ — secondary; NISTIR 8280 owns the findings directly.
```
