# Evidence: when-ai-breaks/rite-aid-facial-recognition (01)

The evidence supports the lesson's spine and both mechanisms, with one important
seam to respect. The record firmly establishes what Rite Aid built (a one-to-many
facial watchlist matching every entering shopper against an enrollment database of
"persons of interest"), that it ran from 2012 to 2020 in hundreds of stores, that
it produced thousands of recorded false positives, and that Rite Aid deployed it
with no accuracy testing, low-quality images, thin training, and instructions that
told staff to act on a match. All of that is the FTC's own charge, resolved by a
consent order in which Rite Aid "neither admit[ted] nor den[ied]" the allegations,
so it is allegation, not adjudicated fact, throughout. The base-rate mechanism is
strongly supported qualitatively: single enrollments generated hundreds to
thousands of alerts across the country in days, and the alerts skewed to false
because true matches are rare in a huge stream of ordinary shoppers. It is thin
quantitatively: Rite Aid never measured its own per-scan false-match rate (that is
part of the charge), so any fully worked base-rate arithmetic must use an
illustrative rate, not a reported one. The demographic-skew mechanism is where the
angle is thinnest and most easily overclaimed. NIST NISTIR 8280 measures large
false-positive differentials across demographic groups across the field of
algorithms, but on good-quality government photos, not on Rite Aid's system; and
NIST's own finding is that these differentials are large and broad but "not all"
algorithms show them, and some one-to-many algorithms show none. Rite Aid's own
demographic-harm evidence in the complaint is circumstantial (store siting in
non-white areas; low confidence scores correlated with plurality-Black/Asian areas
and feminine names), not a measured in-store error rate by race. So "the system
misread Black, Latino, Asian, and women shoppers more" is the FTC's supported
allegation plus a field-wide NIST measurement, not a measured Rite-Aid-specific
differential. Reuters (2020), independent of the FTC and predating it, corroborates
the scale (200 stores, one of the largest retail rollouts) and the concentration in
lower-income, non-white neighborhoods from its own store visits and statistical
analysis.

## Sources

```text
URL:         https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_complaint_filed.pdf
             (case landing: https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-ftc-v)
Kind:        Primary. The FTC's own complaint (FTC v. Rite Aid Corp. and Rite Aid
             Hdqtrs. Corp., Case 2:23-cv-05023, E.D. Pa., filed Dec 19 2023). The FTC
             owns these as its charges. Every underlying fact here is an ALLEGATION.
Establishes: What the system was, how it worked, the deployment failures charged, the
             specific harms alleged (including a minor), and the demographic allegations.
Paraphrase:  Rite Aid deployed AI facial recognition to match entering shoppers'
             "live images" against an enrollment database of "persons of interest" it
             deemed likely to shoplift or commit crime, to "drive and keep persons of
             interest out of [its] stores" (¶3). A match above a Rite-Aid-set confidence
             threshold generated a "match alert" to store employees' phones, carrying
             the enrollment image, live image, and an instruction: "Approach and
             Identify" (a majority of enrollments), "Observe and Provide Customer
             Service," "Pharmacy Patient - Escort to Pharmacy," or "911 Alert /
             Potentially Violent" (¶28-30). Employees were told to act if they believed
             the match accurate (¶28). Match alerts generally did NOT show the confidence
             score, so operators did not know it (¶27). Rite Aid did not tell consumers
             it used the technology and instructed employees not to reveal it (¶20).
             Enrollment images came from CCTV excerpts, the FR cameras, mobile phone
             photos, driver's licenses, and occasionally law enforcement or media; Rite
             Aid trained staff to "push for as many enrollments as possible" and enrolled
             "at least tens of thousands" of people, retained indefinitely (¶21-24).
             Charged failures (¶32, 50-84): no accuracy testing before or after
             deployment (vendors expressly DISCLAIMED accuracy in contract and in the
             alerts themselves, ¶51-52, 56); regular use of low-quality/blurry/poorly-lit
             images that raised false positives (¶57-65); ~1-2 hours of training, usually
             unverified, that did not cover the technology's limits or false positives
             (¶66-73); no monitoring — employees left ~two-thirds of alerts "unresolved"
             Dec 2019-Jul 2020, so Rite Aid could not track false positives (¶79-83);
             problematic enrollments left active despite generating cross-country alerts
             (¶84). Demographic allegations (¶39-49, 86): Rite Aid prioritized "urban"
             stores and transit routes; ~80% of all Rite Aid stores sit in plurality-White
             areas but ~60% of FR stores were in plurality non-White areas (¶41); face
             recognition often produces more false positives for Black/Asian subjects and
             for women (¶42); Rite Aid never checked whether its own accuracy varied by
             race or gender (¶43); match alerts in plurality-Black/Asian areas and to
             feminine-named enrollments were "significantly more likely to have low
             confidence scores," and low scores were more likely false positives (¶44-46);
             one alert matched a Black woman to an enrollment employees described as "a
             white lady with blonde hair," police were called and she was asked to leave
             before the false positive was realized (¶48). Minor: "Rite Aid employees
             stopped and searched an 11-year-old girl on the basis of a false-positive
             facial recognition match," and the girl's mother missed work because the
             child was so distraught (¶91). Harms (¶88-92): surveilled/followed shoppers;
             barred them from buying prescriptions and OTC medications; searched them;
             publicly accused them "in front of the consumers' coworkers, employers,
             children"; called police. One consumer wrote: "every black man is not [a]
             thief nor should they be made to feel like one" (¶92).
Locators:    ¶3-6 (overview), ¶18-31 (system + false-positive evidence), ¶32 & 50-84
             (deployment failures), ¶39-49 & 86 (demographics), ¶88-93 (harms), ¶91
             (11-year-old), ¶139 (duration/"stopped only after" press). Pages 2-24, 34-36
             of the 38-page complaint body (PDF pages 2-24, 34-36; the exhibits follow).
Quote:       "Rite Aid employees stopped and searched an 11-year-old girl on the basis of
             a false-positive facial recognition match." (¶91)
             "[VENDOR] MAKES NO REPRESENTATIONS OR WARRANTIES AS TO THE ACCURACY AND
             RELIABILITY OF THE PRODUCT IN THE PERFORMANCE OF ITS FACIAL RECOGNITION
             CAPABILITIES." (¶51, first vendor's contract)
             Second vendor's alert disclaimer: "identified a PROBABLE match. Feature
             matching technology cannot guarantee 100% matches. Discretion is advised." (¶56)
```

```text
URL:         https://www.ftc.gov/system/files/ftc_gov/pdf/2023190_riteaid_stipulated_order_filed.pdf
             (this filing contains the Stipulated Order plus, as Attachment A, the Decision and Order)
Kind:        Primary. The FTC/Rite Aid settlement filing. Owns the order's terms and the legal posture.
Establishes: The exact remedy and that it is a settlement without admission of the allegations.
Paraphrase:  Legal posture: "Defendants neither admit nor deny any of the allegations in the
             Complaint, except as specifically stated" (Stipulated Order, Findings ¶5); the same
             "neither admit nor deny" language recurs in the Decision and Order. Only for
             jurisdiction do they admit facts. Both sides waive appeal. The order was entered
             while Rite Aid was in Chapter 11 (petitions filed Oct 15 2023) and required
             bankruptcy-court approval. Provision I ("Use of Facial Recognition or Analysis
             Systems Prohibited"): Respondents "are prohibited for five (5) years from the
             effective date of this Order from deploying or using... any Facial Recognition or
             Analysis System... in any retail store or retail pharmacy or on any online retail
             platform." Provision II (deletion): within 45 days, delete/destroy all photos and
             videos of consumers used with the system "and any data, models, or algorithms derived
             in whole or in part therefrom," and certify under oath; within 60 days, identify and
             instruct all third parties (except government) that received such images/derived
             models to delete them and confirm. Provision III (monitoring program): if it ever
             uses any non-prohibited automated biometric system it must first build a written
             program that identifies and addresses risks of physical/financial/reputational harm,
             stigma, and severe emotional distress, "and must also identify and address risks that
             any such harms will disproportionately affect consumers based on race, ethnicity,
             gender, sex, age, or disability"; run pre-deployment and >=annual System Assessments;
             conduct documented accuracy testing (with consent) that determines the rate of
             Inaccurate Outputs and measures "any statistically significant variation... depending
             on demographic characteristics"; train operators on limitations and on automation and
             confirmation bias; and NOT deploy without "competent and reliable scientific evidence"
             that outputs are likely accurate. Provision IV: written notice to enrolled consumers
             and to anyone acted against, plus a complaint procedure. Provision V: written retention
             schedule, deletion of biometric information within <=5 years. Provision VI: clear and
             conspicuous in-store and online notice of any such system. Provision VIII: a
             comprehensive information security program, annual assessments, MFA, encryption, and
             CEO/senior-officer reporting. (The order also supersedes Rite Aid's 2010 FTC data-
             security order, Docket C-4308, whose Section II Rite Aid was charged with violating.)
Locators:    Stipulated Order Findings ¶5 (no admission); Provisions I (5-yr ban, PDF p.13),
             II (deletion, p.14-15), III (monitoring/testing, p.15-21), IV (notice, p.21-23),
             V (retention, p.23-24), VI (disclosure, p.24), VIII (data security, p.25-27).
             Decision and Order (Attachment A) repeats "neither admit nor deny."
Quote:       "prohibited for five (5) years from the effective date of this Order from deploying or
             using, or assisting in the deployment or use of, any Facial Recognition or Analysis
             System... in any retail store or retail pharmacy or on any online retail platform."
             (Provision I)
             "Defendants neither admit nor deny any of the allegations in the Complaint, except as
             specifically stated in this Stipulated Order or in the Decision and Order." (Findings ¶5)
```

```text
URL:         https://www.ftc.gov/news-events/news/press-releases/2023/12/rite-aid-banned-using-ai-facial-recognition-after-ftc-says-retailer-deployed-technology-without
Kind:        Primary for the FTC's own framing of its action (the agency speaking about its own case).
Establishes: The 2012-2020 / "hundreds of stores" framing, the plurality-community disparity claim,
             and the FTC's plain-language summary of the order. Announcement, dated Dec 19 2023.
Paraphrase:  "from 2012 to 2020, Rite Aid deployed artificial intelligence-based facial recognition
             technology" in hundreds of stores. Acting on false-positive alerts, employees followed,
             searched, barred, and publicly accused shoppers, "sometimes in front of friends or
             family." The technology "was more likely to generate false positives in stores located
             in plurality-Black and Asian communities than in plurality-White communities." Samuel
             Levine, Director of the FTC Bureau of Consumer Protection: "Rite Aid's reckless use of
             facial surveillance systems left its customers facing humiliation and other harms, and
             its order violations put consumers' sensitive information at risk." Order summary listed:
             five-year prohibition; delete images and derived algorithms; notify enrolled/acted-against
             consumers; investigate and respond to complaints; post clear notice; delete biometric
             information within five years; data-security program; third-party assessments; annual CEO
             compliance certification.
Locators:    Body paragraphs and the bulleted "Under the proposed order" list.
Quote:       Levine: "Rite Aid's reckless use of facial surveillance systems left its customers facing
             humiliation and other harms, and its order violations put consumers' sensitive
             information at risk."
```

```text
URL:         https://nvlpubs.nist.gov/nistpubs/ir/2019/NIST.IR.8280.pdf  (DOI https://doi.org/10.6028/NIST.IR.8280)
Kind:        Primary. NIST owns these measurements. Grother, Ngan, Hanaoka, "Face Recognition Vendor
             Test (FRVT) Part 3: Demographic Effects," NISTIR 8280, National Institute of Standards
             and Technology, December 2019.
Establishes: The measured, field-wide false-positive differentials across demographic groups, with
             the exact framing and caveats. NOT a measurement of Rite Aid's system.
Paraphrase:  NIST tested 189 mostly commercial algorithms from 99 developers against 18.27 million
             photos of 8.49 million people, from four U.S. government datasets (domestic mugshots,
             immigration application photos, visa photos, border-crossing photos). Main result: false
             positive (false match) differentials are much larger than false-negative ones and exist
             "broadly, across many, but not all, algorithms tested," and "across demographics, false
             positives rates often vary by factors of 10 to beyond 100 times"; false negatives vary
             by factors below 3. On higher-quality application photos, false positives are highest in
             West/East African and East Asian people and lowest in Eastern Europeans (a factor of ~100
             between countries) - though a number of China-developed algorithms reverse this for East
             Asian faces. On domestic law-enforcement (mugshot) images, "the highest false positives
             are in American Indians, with elevated rates in African American and Asian populations;
             the relative ordering depends on sex and varies with algorithm." False positives are
             higher in women than men, "consistent across algorithms and datasets," an effect smaller
             than race. False positives are elevated in the elderly and in children. Crucial for the
             watchlist (one-to-many) case: differentials in one-to-one verification are "usually, but
             not always, present in one-to-many search algorithms," and "some developers supplied
             identification algorithms for which false positive differentials are undetectable"
             (NIST names Idemia; also NEC-3, Aware, Toshiba, Tevian, Real Networks as having stable
             rates). NIST frames the "African American women" shorthand carefully: Figure 26 shows one
             algorithm with elevated similarity scores in the "black female" population, but Figure 27
             (Idemia) shows scores uniform across Asian/black/white men and women - so the skew is
             algorithm-dependent, not a universal law.
Locators:    Executive Summary "WHAT WE FOUND" (report pp.1-3, PDF pp.4-6); Technical Summary
             identification section and "PRIOR WORK" (report pp.7-8, PDF pp.10-11); one-to-many
             heatmaps Figures 26-27 (report p.68, PDF p.~74).
Quote:       "Across demographics, false positives rates often vary by factors of 10 to beyond 100
             times." (Exec. Summary)
             "One important exception is that some developers supplied identification algorithms for
             which false positive differentials are undetectable." (Exec. Summary)
             "We found false positives to be higher in women than men, and this is consistent across
             algorithms and datasets. This effect is smaller than that due to race." (Exec. Summary)
```

```text
URL:         https://www.reuters.com/investigates/special-report/usa-riteaid-software/
             (also filed as https://www.reuters.com/technology/rite-aid-deployed-facial-recognition-systems-hundreds-us-stores-2020-07-28/)
Kind:        Primary for Reuters' own firsthand investigation (store visits, document review, its own
             statistical analysis); secondary where it restates others. Independent of the FTC and two
             years earlier, so it is the non-FTC confirmation of scale the commission asked for.
             Jeffrey Dastin, "Special Report: Rite Aid deployed facial recognition systems in hundreds
             of U.S. stores," Reuters, July 28 2020. NOTE: reuters.com returns HTTP 401 to automated
             requests (a bot wall, not a dead link - it resolves in a browser); the full wire text was
             read via a verbatim syndication. Record and cite Reuters' own page above.
Establishes: The program's independently-verified scale, location skew, vendors, and Rite Aid's 2020
             posture - none of it sourced to the FTC.
Paraphrase:  "Over about eight years, the American drugstore chain Rite Aid Corp quietly added facial
             recognition systems to 200 stores across the United States, in one of the largest rollouts
             of such technology among retailers in the country, a Reuters investigation found." "In the
             hearts of New York and metro Los Angeles, Rite Aid deployed the technology in largely
             lower-income, non-white neighborhoods, according to a Reuters analysis." Reuters' own store
             visits found cameras at 33 of the 75 Rite Aid shops in Manhattan and central LA metro; its
             statistical analysis found "Stores in more impoverished areas were nearly three times as
             likely as those in richer areas to have facial recognition cameras. Seventeen of 25 stores
             in poorer areas had the systems. In wealthier areas, it was 10 of 40." Vendors: an early
             system from FaceFirst (U.S.-backed) that loss-prevention agents said "regularly
             misidentified people" - one, working at a Rite Aid in an African-American neighborhood of
             Detroit, said "It doesn't pick up Black people well"; and later DeepCam LLC, which "worked
             with a firm in China whose largest outside investor is a Chinese government fund" (Reuters
             found no evidence Rite Aid data went to China). Rite Aid defended the technology to Reuters
             as having "nothing to do with race" and told Reuters (Feb 2020) customers had been apprised
             "through 'signage'" and a website policy; Reuters "found no notice of the surveillance in
             more than a third of the stores they visit[ed]." After Reuters sent its findings, Rite Aid
             said it had quit the software and later that all cameras were off, citing "a larger industry
             conversation." Basis: "thousands of pages of internal documents," store visits, and
             interviews with "more than 40 people."
Locators:    Lede and the sections on store-location analysis, vendors (FaceFirst/DeepCam), and Rite
             Aid's response.
Quote:       "It doesn't pick up Black people well" (a Rite Aid loss-prevention staffer, using FaceFirst
             in Detroit).
             "Stores in more impoverished areas were nearly three times as likely as those in richer
             areas to have facial recognition cameras."
```

```text
URL:         https://www.cnn.com/2023/12/20/tech/rite-aid-ai-ftc-settlement/index.html
Kind:        Secondary reporting, and the vehicle carrying Rite Aid's own statement. Rite Aid's
             statement is PRIMARY for Rite Aid's position; it was issued to press and has no standalone
             page, so it is recorded here as quoted. Author uncredited in fetch; dated Dec 20 2023.
Establishes: Rite Aid's public position on the settlement, verbatim in the quoted phrases.
Paraphrase:  Rite Aid said it is "pleased to reach an agreement" with the FTC but "we fundamentally
             disagree with the facial recognition allegations in the agency's complaint." Per CNN, the
             technology "was a pilot program and was only used in a 'limited number of stores,'" and
             "The test stopped more than three years ago before the FTC's investigation began." CNN also
             restates the FTC's filing figures (complaints spanning 2012 to 2020).
Locators:    Paragraph carrying the Rite Aid statement.
Quote:       Rite Aid: "pleased to reach an agreement"; "we fundamentally disagree with the facial
             recognition allegations in the agency's complaint"; program used in a "limited number of
             stores"; "The test stopped more than three years ago before the FTC's investigation began."
```

```text
URL:         https://www.nbcnews.com/business/business-news/rite-aid-punished-facial-recognition-accuse-customers-shoplifting-rcna130587
Kind:        Secondary reporting. Marley Jay, NBC News, Dec 20 2023.
Establishes: A second, independent carrier of Rite Aid's "few stores / discontinued 2020" line, and the
             mainstream framing of the case.
Paraphrase:  NBC reports the FTC said the technology was used "for nearly a decade" starting in 2012 and
             discontinued in 2020, and paraphrases Rite Aid as saying "the program was used at only a few
             stores and discontinued in 2020." No independent store count.
Locators:    Body.
Quote:       (paraphrase) Rite Aid: "the program was used at only a few stores and discontinued in 2020."
```

### Library context (not article citations; already-published Background link targets)

Both neighbor lessons the commission names ARE published in the library (the default
`nb history` list is capped at the 8 most recent; a keyword query surfaces them):

- `when-ai-breaks/facial-recognition-wrongful-arrest` (2026-07-30) - "A ranked list
  of candidates was enough to arrest the wrong man." Its sections already teach how a
  face-match candidate list misidentifies a person and include a section "The odds NIST
  had already measured." This is the Background link for face-matching misidentification;
  the commission's instruction to link it rather than re-teach that mechanic is valid, and
  it means this lesson's fresh work is the base-rate-times-scale mechanism in a mass
  one-to-many deployment, NOT a re-run of "NIST measured demographic error."
- `when-ai-breaks/compas-recidivism` (2026-07-25) - "ProPublica and Northpointe read the
  same recidivism scores and both were right." It carries a section "The math that makes
  both sides right" teaching false-positive vs false-negative reasoning and base rates on a
  fixed population. It is the natural Background link for false-positive/false-negative
  definitions; note it teaches the two-error trade-off on a fixed cohort, not the
  rare-event/precision problem this lesson centers, so the base-rate mechanism here is still
  new teaching.

## Contradictions

1. Scale: pilot vs mass deployment. Rite Aid calls it "a pilot program" used in "a
   limited number of stores" / "only a few stores" (CNN, NBC). The FTC alleges 2012-2020
   across "hundreds of stores" (press release) with match alerts in "over 130 different
   Rite Aid stores... a majority of all locations using facial recognition technology"
   for a single enrollment (complaint ¶31b). Reuters, independently, found "200 stores...
   one of the largest rollouts of such technology among retailers in the country." The
   record does not support "pilot."

2. Why it stopped: voluntary vs forced. Rite Aid says it "stopped... more than three
   years ago before the FTC's investigation began" (CNN), framing discontinuation as its
   own choice. The FTC alleges the opposite: "Defendants stopped their unlawful conduct
   only after they learned that press coverage of their facial recognition practices would
   be published imminently" (complaint ¶139c). Reuters records that Rite Aid said it had
   quit only "after Reuters sent its findings to the retailer" in July 2020. The timelines
   agree on ~2020; the motive is disputed.

3. Race: Rite Aid told Reuters the program "had nothing to do with race." The FTC alleges
   disproportionate harm to Black, Latino, Asian, and women shoppers (complaint ¶6, 49, 86),
   and Reuters' own analysis found stores in poorer, non-white areas nearly three times as
   likely to have the cameras. Note the FTC's demographic evidence is circumstantial (siting,
   low-confidence-score proxies), not a measured in-store false-match rate by race.

4. Notice: Rite Aid told Reuters (Feb 2020) customers were apprised "through 'signage'" and
   a website policy. The FTC alleges Rite Aid "did not inform consumers" and "specifically
   instructed employees not to reveal" the technology (complaint ¶20). Reuters "found no
   notice of the surveillance in more than a third of the stores they visit[ed]."

5. Status of every underlying fact. The FTC's account is an allegation resolved by a consent
   order in which Rite Aid "neither admit[ted] nor den[ied]" the claims (Stipulated Order
   Findings ¶5; Decision and Order). It is not a court's finding of fact after trial. Every
   FTC-sourced fact above - the 11-year-old, the thousands of false positives, the demographic
   skew - carries this label. Where the ONLY source for an underlying fact is the FTC's charge
   (e.g. the 11-year-old girl, the internal "white lady with blonde hair" incident, the
   confidence-score-by-demographic finding), it is the FTC's allegation, uncorroborated by an
   independent party in a position to know.

6. Tension with the commissioned demographic-skew angle (flag for the editor). The angle asks
   the lesson to "layer" NIST's measured demographic error onto Rite Aid's base-rate problem so
   "the false accusations concentrate on the groups the system misreads most." The evidence
   supports this as a plausible, FTC-alleged mechanism but not as a Rite-Aid measurement: NIST
   measured the differentials field-wide on good-quality government photos and found them large
   but "not all" algorithms show them and some one-to-many systems show none; Rite Aid used
   low-quality CCTV images and never measured its own by-race error. The honest construction is
   "demographic false-positive skew is real, often large, and Rite Aid never checked which kind
   of system it had," not "NIST proved Rite Aid misread Black and women shoppers by 10-100x."

## Numbers

```text
Figure: 2012 to 2020 (system operating period)
Owner:  FTC press release ("from 2012 to 2020"); complaint ¶139a frames it as "at least seven years"
Scope:  Duration of the facial-recognition deployment. Reuters independently: "about eight years."
        Rite Aid: stopped ~2020 ("more than three years" before its Dec 2023 statement).
```
```text
Figure: hundreds of stores (FTC) / 200 stores (Reuters)
Owner:  FTC press release ("hundreds of stores"); Reuters ("200 stores") from its own analysis
Scope:  Stores that used the technology, 2012-2020, nationwide. The complaint gives no single raw
        count; it lists concentration cities (NYC, LA, SF, Philadelphia, Baltimore, Detroit, Atlantic
        City, Seattle, Portland OR, Wilmington DE, Sacramento) and says a single enrollment alerted in
        "over 130" stores, "a majority of all locations using facial recognition technology" (¶31b).
```
```text
Figure: at least tens of thousands of people enrolled on the watchlist
Owner:  FTC complaint ¶23
Scope:  Total enrollment database over the program's life; images retained indefinitely (¶24).
        As of Jul 2020 a majority of enrollments had no first or last name recorded (¶77).
        This is the watchlist size for a base-rate illustration.
```
```text
Figure: thousands of false-positive match alerts recorded Dec 2019 - Jul 2020
Owner:  FTC complaint ¶31
Scope:  Only the ~8-month window in which Rite Aid's later system recorded outcomes at all; ~two-thirds
        of all alerts in that window were never "resolved," so the true count is unknown and higher (¶82).
```
```text
Figure: over 5,000 match alerts generated >100 miles from the enrolling store (Dec 2019 - Jul 2020)
Owner:  FTC complaint ¶31a
Scope:  Alerts geographically implausible for the enrolled person - used as evidence of false positives.
```
```text
Figure: over 900 match alerts for a single enrollment in a 5-day period, across 130+ stores
Owner:  FTC complaint ¶31b
Scope:  One enrollment image; hundreds of alerts each in NY and LA, 100+ in Philadelphia, more elsewhere.
        A concrete illustration of one bad enrollment swamping the system with false alerts.
```
```text
Figure: Bronx enrollment - over 1,000 alerts (May 16 - Jul 2020) = "nearly 5 percent of all match alerts"
Owner:  FTC complaint ¶84a
Scope:  One enrollment; >99% of its alerts fired in/near Los Angeles (enrolled in the Bronx); of the <3%
        of alerts with a recorded outcome, all were "Bad Matches." DERIVED (not stated by FTC): if 1,000+
        alerts was ~5% of the total, total alerts in that window were on the order of ~20,000 - use only as
        an illustrative order-of-magnitude, labeled as such.
```
```text
Figure: ~80% of all Rite Aid stores in plurality-White areas vs ~60% of FR stores in plurality non-White areas
Owner:  FTC complaint ¶41
Scope:  Store siting, used to allege disproportionate exposure. Reuters' independent parallel: 17 of 25
        poorer-area stores had the system vs 10 of 40 wealthier-area stores ("nearly three times as likely").
```
```text
Figure: false-positive rates vary across demographic groups "by factors of 10 to beyond 100 times"
Owner:  NIST NISTIR 8280 (2019), Executive Summary
Scope:  Measured across 189 algorithms from 99 developers on U.S. government photos; false-positive
        differentials, largest on one-to-one verification / country-of-birth. "many, but not all"
        algorithms; some one-to-many algorithms show undetectable differentials. NOT measured on Rite Aid.
```
```text
Figure: no measured per-scan false-match rate for Rite Aid's actual system exists (public)
Owner:  Gap. FTC complaint ¶43, 76-83 (Rite Aid never tested or tracked accuracy)
Scope:  The one number a clean base-rate calculation needs is precisely the number Rite Aid never produced.
        A fully worked base-rate example must supply an ILLUSTRATIVE per-scan false-match rate (NIST test
        thresholds such as FMR = 0.00001 or 0.00003 can anchor it) and an ILLUSTRATIVE daily store traffic,
        both labeled illustrative, not reported.
```

## Source assets

```text
Asset: FTC press release / case page header and the "Under the proposed order" bulleted terms
       (ftc.gov). A plain screenshot of the FTC's own summary of the ban.
Shows: The remedy in the regulator's own words - five-year ban, deletion, notice, monitoring.
Crop:  Keep the FTC masthead and the bullet list; a headline crop must not drop the "proposed"/
       settlement framing.
```
```text
Asset: NIST NISTIR 8280 Executive Summary "WHAT WE FOUND" block, and Figures 26 vs 27 (report p.68).
Shows: The exec-summary text is the citable statement of the 10-to-100x differential and its caveats.
       Figures 26 (elevated scores for the black-female population on one algorithm) and 27 (Idemia,
       uniform across groups) side by side make NIST's real point: the skew is algorithm-dependent.
Crop:  If either figure is used, use BOTH or neither - showing only Figure 26 misrepresents NIST as
       claiming a universal Black-women effect. Retain the axis/demographic labels and the dataset (mugshot)
       and algorithm captions.
```
```text
Asset: FTC complaint ¶28-30 (the "Approach and Identify" / "911 Alert" match-alert instructions) and
       the vendor accuracy disclaimers quoted at ¶51-52, 56.
Shows: The mechanism in the record's own words - an alert with no confidence score, a pre-set
       instruction to act, sitting on top of a vendor's written "we don't warrant accuracy" disclaimer.
Crop:  Text excerpt; preserve the disclaimer's all-caps and the "PROBABLE match... Discretion is advised."
```
```text
Asset: Reuters store-location statistic (17 of 25 poorer vs 10 of 40 wealthier) - a simple bar comparison.
Shows: The independent, non-FTC evidence that deployment concentrated in poorer, non-white areas.
Crop:  If rendered as a chart it must be built from Reuters' figures with Reuters cited in the caption
       (per spec/charts.md, a committed chart-N.py), not lifted as an image.
None found: no public dataset of Rite Aid's actual match logs or by-race error rates exists (that is the
       missing evidence that would settle the disputes; see Numbers).
```

## Discarded

```text
URL: https://www.goodreads.com/author_blog_posts/20163176-...  Used only to read the verbatim Reuters
     wire text after reuters.com bot-walled (401). Not citable itself; Reuters' own page is recorded instead.
URL: https://moguldom.com/293887/...  Secondary restatement of Reuters; adds nothing firsthand and rounds
     NIST loosely ("up to 100 times more likely"). Rejected in favor of NIST and Reuters directly.
URL: https://talkingbiznews.com/.../how-reuters-investigated-rite-aids-use-of-facial-recognition/
     A Dastin process interview; used only to confirm the "ended the program after Reuters shared findings"
     point already in the Reuters article. Not needed as a citation.
URL: https://www.wilmerhale.com/...; https://www.mintz.com/...; https://www.arnoldporter.com/...;
     https://www.mofo.com/...; https://www.insideprivacy.com/...  Law-firm client alerts. Accurate but
     secondary summaries of the FTC filings; superseded by reading the complaint and order directly.
URL: https://www.barchart.com/...; https://www.hipaajournal.com/...  Secondary news summaries; the "11-year-
     old girl" and "thousands of incorrect matches" they carry trace to the FTC complaint, which is cited directly.
URL: https://www.ftc.gov/legal-library/browse/cases-proceedings/2023190-rite-aid-corporation-matter
     Wrong slug (404). The correct landing is .../2023190-rite-aid-corporation-ftc-v (recorded above).
URL: reuters.com direct + web.archive.org  reuters.com returns 401 to automated requests; web.archive.org is
     blocked by this session's egress policy (not retried, per proxy policy). Reuters text obtained via the
     syndication noted above; Reuters' own URL is the recorded source.
```
