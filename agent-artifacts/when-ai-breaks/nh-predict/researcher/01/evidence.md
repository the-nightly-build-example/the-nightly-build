# Evidence record: when-ai-breaks/nh-predict (01)

The record strongly supports the commission's mechanism as *stated positions and
allegations*, not as adjudicated fact. Three findings are firm and firsthand: (1)
what nH Predict is and does, and the internal 1%-adherence target with discipline
attached, are established by the plaintiffs' complaint and STAT's internal-document
reporting; (2) the regulator's position that a length-of-stay prediction "alone
cannot be used as the basis to terminate post-acute care services" is established
directly by the CMS FAQ (a primary government document), which is the single
cleanest confirmation of the commission's category-error thesis; (3) the Senate
PSI report independently documents that UnitedHealthcare's post-acute
prior-authorization denial rate roughly doubled (10.9% → 22.7%, 2020–2022) while
it automated review. The record is **thin exactly where the commission's headline
number lives**: the ~90% appeal-reversal figure and the ~0.2% appeal rate both
originate inside the complaint, are pleaded "upon information and belief," carry no
independent source (the 0.2% is footnoted to a KFF study of *ACA Marketplace*
plans, not Medicare Advantage), and are not adjudicated. The causal claim — that
nH Predict *drove* the denials — is contested and unproven; even the Senate report
only calls nH Predict "linked in media reports" to denials. The angle survives, but
only with disciplined attribution: present 90% and 0.2% as complaint allegations,
and the causation as disputed and in discovery.

---

## Sources

```text
URL:         https://litigationtracker.law.georgetown.edu/wp-content/uploads/2023/11/Estate-of-Gene-B.-Lokken-et-al_20231114_COMPLAINT.pdf
Kind:        primary — the class-action complaint itself; owns the allegations (not their truth).
Establishes: The suit's caption, parties, plaintiff facts, and every core allegation.
             Case: Estate of Gene B. Lokken and Estate of Dale Henry Tetzloff v.
             UnitedHealth Group, Inc.; UnitedHealthcare, Inc.; naviHealth, Inc.; and
             Does 1-50. Case No. 0:23-cv-03514, U.S. District Court, District of
             Minnesota, filed 11/14/2023, jury demand. 25 causes of action; leads with
             breach of contract, breach of the implied covenant of good faith and fair
             dealing, unjust enrichment, and state insurance bad-faith / claim-settlement
             statutes across many states.
Paraphrase:  Defendants allegedly deployed the nH Predict AI model in place of clinicians
             to deny post-acute care to elderly Medicare Advantage members, overriding
             treating physicians, based on a model Defendants "know has a 90% error rate."
             nH Predict matches a patient's diagnosis, age, living situation, and physical
             function against a database of six million patients to output estimated length
             of stay and a target discharge date (¶32). naviHealth developed nH Predict
             after the 2010 ACA; UnitedHealth Group acquired naviHealth in 2020 for $2.5
             billion (¶22).
Locators:    ¶1 (90% error rate), ¶2 (0.2% appeal, footnote 1 = KFF ACA Marketplace study),
             ¶7 (1% target; discipline/termination for deviation), ¶32 (six-million database;
             length of stay; target discharge date), ¶33 (sample nH Predict Outcome sheet),
             ¶36 (up to 100 nursing-home days; denials often before day 14), ¶38 (>90%
             reversed on appeal/ALJ, "upon information and belief"), ¶¶42-57 (Lokken),
             ¶¶58-68 (Tetzloff), ¶¶80-... (causes of action).
Quote:       "over 90 percent of patient claim denials are reversed through either an
             internal appeal process or through federal Administrative Law Judge (ALJ)
             proceedings" (¶38).
```

```text
URL:         https://www.statnews.com/2023/11/14/unitedhealth-algorithm-medicare-advantage-investigation/
Kind:        secondary — STAT reports from outside; but it owns the reporting on the internal
             naviHealth documents, which are the primary material.
Establishes: The 1%-adherence-target claim and the case-manager discipline claim, sourced to
             internal documents and former employees. This is the pin for the commission's
             ~1% figure.
Paraphrase:  naviHealth "set a target for 2023 to keep rehab stays of patients in Medicare
             Advantage plans within 1% of the days projected by the algorithm." Missing the
             target "meant exposing themselves to discipline, including possible termination,
             regardless of whether the additional days were justified under Medicare coverage
             rules." Internally, managers' message was that the algorithm "was to be followed
             precisely so payment could be cut off by the date it predicted," contradicting
             the public "guidepost" line.
Locators:    "Denied by AI" series; investigation dated 11/14/2023, by Casey Ross and Bob
             Herman. STAT+ paywalled; the target and discipline passages above were retrieved.
Quote:       "within 1% of the days projected by the algorithm."
Note:        Search summaries indicate STAT reported the target tightened from 3% to under 1%;
             I confirmed only the "within 1%" figure firsthand. Treat the 3%→1% narrowing as
             STAT-reported detail, not independently confirmed here.
```

```text
URL:         https://www.statnews.com/2023/03/13/medicare-advantage-plans-denial-artificial-intelligence/
Kind:        secondary — the foundational "Denied by AI" investigation; owns the first
             description of nH Predict from sources and internal material.
Establishes: What nH Predict is and does, firsthand from naviHealth material and interviews;
             the six-million-patient database; the per-patient outputs (mobility/cognition
             assessment, estimated length of stay, target discharge date). This is the source
             the complaint itself repeatedly cites for its nH Predict description.
Paraphrase:  nH Predict "uses details such as a person's diagnosis, age, living situation, and
             physical function to find similar individuals in a database of 6 million patients,"
             then produces "a down-to-the-minute prediction of their medical needs, estimated
             length of stay, and target discharge date." naviHealth's public line: the tool
             "is not used to make coverage determinations" and is "a guide."
Locators:    Investigation dated 03/13/2023, by Casey Ross and Bob Herman. STAT+ paywalled;
             the description and the naviHealth statement were retrieved.
Quote:       "The NaviHealth predict tool is not used to make coverage determinations. The tool
             is used as a guide to help us inform providers, families and other caregivers."
```

```text
URL:         https://www.hsgac.senate.gov/wp-content/uploads/2024.10.17-PSI-Majority-Staff-Report-on-Medicare-Advantage.pdf
Kind:        primary — U.S. Senate Permanent Subcommittee on Investigations majority staff
             report; owns its findings and quotes the internal documents PSI obtained.
Establishes: Independent (non-litigant) documentation that post-acute prior-authorization
             denials rose sharply as insurers automated review, and that nH Predict figured in
             UnitedHealthcare's post-acute workflow. Does NOT independently confirm the 90%
             figure or that nH Predict caused specific denials.
Paraphrase:  Title: "Refusal of Recovery: How Medicare Advantage Insurers Have Denied Patients
             Access to Post-Acute Care," Majority Staff Report, Sen. Richard Blumenthal
             (Chairman), 10/17/2024, 54 pp., based on 280,000+ pages from UnitedHealthcare,
             Humana, and CVS (inquiry launched 05/17/2023). UnitedHealthcare's post-acute
             prior-auth denial rate rose 10.9% (2020) → 16.3% (2021) → 22.7% (2022). Its
             skilled-nursing-facility denial rate in 2019 was "nine times lower than it was in
             2022." In 2022, UnitedHealthcare and CVS denied post-acute prior-auth requests at
             ~3x their overall denial rate; Humana's post-acute rate was >16x its overall rate.
             A January 2022 UnitedHealthcare presentation shows a "naviHealth Care Coordinator
             completes nH Predict … to determine optimal [post-acute care] placement." In
             December 2022 a UnitedHealthcare working group explored using AI/machine learning
             to predict which post-acute denials were likely to be appealed and overturned.
Locators:    Executive Summary (pp. 4-6); UnitedHealthcare findings (pp. 4-5); Appendix Table 1
             (denial rates by facility type, p. 54).
Quote:       "an algorithm linked in media reports to denials of care" (describing nH Predict —
             note the report's own hedge on causation).
```

```text
URL:         https://www.cms.gov/files/document/hpms-memo-faq-coverage-criteria-and-utilization-management-020604pdf.pdf
Kind:        primary — CMS (the regulator) FAQ memo on the CY2024 MA final rule (CMS-4201-F).
Establishes: The regulator's position, directly on point: a length-of-stay prediction cannot,
             by itself, justify terminating post-acute coverage; the individual patient must be
             reassessed. This is the cleanest external confirmation of the commission's
             category-error thesis, independent of the litigation.
Paraphrase:  MA organizations may use algorithms/AI to assist coverage determinations, but must
             comply with 42 CFR § 422.101(c), which requires basing decisions on the individual
             patient's circumstances. "An algorithm that determines coverage based on a larger
             data set instead of the individual patient's medical history, the physician's
             recommendations, or clinical notes would not be compliant." Issued 02/06/2024
             (HPMS memo); rule effective for coverage from 01/01/2024.
Locators:    Question 2 (pp. 2-3, algorithms/AI); Question 8 (post-acute termination).
Quote:       "an algorithm or software tool can be used to assist providers or MA plans in
             predicting a potential length of stay, but that prediction alone cannot be used as
             the basis to terminate post-acute care services." (Q2)
```

```text
URL:         https://www.cbsnews.com/news/unitedhealth-lawsuit-ai-deny-claims-medicare-advantage-health-insurance-denials/
Kind:        primary for the company's stated position (UnitedHealth/naviHealth's own words),
             retrieved via secondary reporting (CBS News, Elizabeth Napolitano, 11/20/2023).
             Same origin as the naviHealth statement in STAT; counts as one origin.
Establishes: The operator's on-record "only a guide" defense — the material for Contradictions.
Paraphrase:  naviHealth spokesperson Aaron Albright: the predict tool "is not used to make
             coverage determinations"; it is "a guide to help [UnitedHealth] inform providers …
             about what sort of assistance and care the patient may need"; coverage decisions
             are based on "CMS coverage criteria and the terms of the member's plan."
Locators:    Statement quoted in body; article dated 11/20/2023.
Quote:       "not used to make coverage determinations … a guide to help [UnitedHealth] inform
             providers."
```

```text
URL:         https://litigationtracker.law.georgetown.edu/litigation/estate-of-gene-b-lokken-the-et-al-v-unitedhealth-group-inc-et-al/
Kind:        secondary — Georgetown Health Care Litigation Tracker; a docket compilation.
Establishes: Litigation status. Case 0:23-cv-03514, D. Minn. (Fourth Division), filed
             11/14/2023, Judge John R. Tunheim. Amended complaint 04/05/2024; second motion to
             dismiss 05/20/2024; ruling 02/13/2025 ("granted in part"); class-certification
             declarations due 09/14/2026. Case is live and ongoing as of this record.
Locators:    Case summary and docket timeline.
```

```text
URL:         https://www.legalhie.com/judge-decides-class-action-lawsuit-can-proceed-against-unitedhealth-for-use-of-ai/
Kind:        secondary — legal-industry summary of the 02/13/2025 ruling (used because the
             court's opinion PDF at courthousenews.com returned HTTP 403; see Discarded).
Establishes: What survived the second motion to dismiss and why.
Paraphrase:  Judge Tunheim let breach of contract and breach of the implied covenant of good
             faith and fair dealing proceed (tied to policy language that coverage decisions
             would be made by clinical staff, not an algorithm). He dismissed most other
             state-law claims — including unjust enrichment, insurance bad faith, and state
             consumer-protection claims — as barred by the Medicare Act's broad preemption, and
             waived the usual requirement to exhaust Medicare administrative appeals (irreparable
             harm and likely futility).
Locators:    Article body.
Note:        Secondary; the specific survived/dismissed breakdown should ideally be confirmed
             against the docketed order before publication if the piece leans on it.
```

```text
URL:         https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims
Kind:        secondary — ProPublica / The Capitol Forum investigation (present-day parallel).
Establishes: A second insurer converting review into an automated batch process — the
             "where it lives today" beat.
Paraphrase:  "How Cigna Saves Millions by Having Its Doctors Reject Claims Without Reading Them,"
             by Patrick Rucker, Maya Miller, and David Armstrong, 03/25/2023. Over a two-month
             span in 2022, Cigna's PXDX system was used to deny more than 300,000 payment
             requests, averaging about 1.2 seconds per case; one medical director denied
             roughly 60,000 in a single month. A former Cigna doctor: "We literally click and
             submit. It takes all of 10 seconds to do 50 at a time." Cigna called the reporting
             "biased and incomplete" and said the tool "accelerate[s] payment of claims for
             certain routine screenings."
Locators:    Article body.
Quote:       "We literally click and submit. It takes all of 10 seconds to do 50 at a time."
```

---

## Contradictions

**The operator's "only a guide" position (strongest version).** nH Predict is
clinical decision-support and care-coordination software: it estimates a likely
length of stay and anticipated post-acute needs to help providers and families
plan. UnitedHealth's stated process is that coverage determinations are made by
clinicians against CMS criteria and the member's plan terms — not by the algorithm
(naviHealth statement; CBS/STAT). On this account a high appeal-reversal rate is
not proof of a wrong original denial: appeals are decided on a fuller, later record,
often with new clinical information, so reversals can reflect changed facts rather
than initial error. And the 90% figure is self-reported in a complaint, "upon
information and belief," with no external citation.

**The plaintiffs' "decisive in practice" position.** The public "guide" line is
contradicted by internal messaging that the algorithm "was to be followed precisely
so payment could be cut off by the date it predicted" (STAT), a 2023 target to keep
stays within 1% of the projection, and discipline (up to termination) for
deviation. If clinicians are punished for departing from the model's date, the
model is functionally the decision.

**What would settle it.** Two things, both in discovery (the court ordered broad
discovery into UnitedHealth's use of the tool in 2025): (1) the internal adherence
directives — whether deviation from nH Predict was actually disciplined, and how
tightly the 1% target bound reviewers; and (2) the underlying denial and appeal
data with denominators — how many post-acute denials, how many appealed, the
reversal rate broken out by reason, and whether reversals cite *new* evidence or
correct the *original* record. The complaint's 90% and 0.2% are exactly the numbers
that dataset would confirm or refute.

**Regulator vs. operator.** The CMS FAQ sides with the mechanism the plaintiffs
describe without ruling on this case: a predicted length of stay "alone cannot be
used as the basis to terminate post-acute care services," and coverage driven by a
"larger data set instead of the individual patient's" record is non-compliant. CMS
issued this in February 2024, after the conduct at issue; it is regulatory position,
not a finding against UnitedHealth.

**Causation gap.** The Senate PSI report documents the denial-rate surge and nH
Predict's presence in the workflow, but explicitly frames nH Predict as "linked in
media reports" to denials — it does not itself establish that the algorithm caused
the denials. No source I read adjudicates the causal claim.

---

## Numbers

```text
Figure: ~90% (">90 percent") of appealed nH Predict denials reversed on internal appeal or ALJ review
Owner:  Lokken complaint, ¶38 (and "90% error rate," ¶1)
Scope:  ALLEGATION, pleaded "upon information and belief"; no denominator, period, or external
        source given. Not adjudicated. Must be attributed to the complaint, never stated as fact.
```

```text
Figure: ~0.2% of policyholders appeal denied claims
Owner:  Lokken complaint, ¶2
Scope:  ALLEGATION; footnote 1 sources it to a KFF study of ACA MARKETPLACE plans (Feb 9, 2023),
        not Medicare Advantage. Denominator mismatch — weak. Attribute to the complaint and flag.
```

```text
Figure: within 1% — the 2023 target for keeping rehab stays to the algorithm's projected days
Owner:  STAT, 11/14/2023 (internal documents / former employees)
Scope:  Reported internal target for Medicare Advantage rehab stays in 2023; deviation risked
        discipline up to termination. Also pleaded at complaint ¶7.
```

```text
Figure: 6 million patients in the nH Predict comparison database
Owner:  Lokken complaint ¶32; STAT 03/13/2023
Scope:  naviHealth's historical patient database used to match "similar" patients and produce
        estimated length of stay and target discharge date.
```

```text
Figure: UnitedHealthcare post-acute prior-authorization denial rate: 10.9% (2020) → 16.3% (2021) → 22.7% (2022)
Owner:  Senate PSI report, Executive Summary (p. 5)
Scope:  Share of UnitedHealthcare post-acute-care prior-authorization requests denied, by year,
        during automation rollout. Primary, non-litigant.
```

```text
Figure: UnitedHealthcare skilled-nursing-facility denial rate in 2019 was nine times lower than in 2022
Owner:  Senate PSI report, Executive Summary (p. 5)
Scope:  SNF-specific denial rate, 2019 vs. 2022.
```

```text
Figure: 2022 post-acute prior-auth denial rate ≈ 3x overall (UnitedHealthcare, CVS); >16x overall (Humana)
Owner:  Senate PSI report, Executive Summary (p. 4)
Scope:  Ratio of each insurer's post-acute denial rate to its overall prior-auth denial rate, 2022.
```

```text
Figure: naviHealth acquired by UnitedHealth Group in 2020 for $2.5 billion
Owner:  Lokken complaint ¶22
Scope:  Acquisition price and year (naviHealth sits under Optum within UnitedHealth Group).
```

```text
Figure: UnitedHealthcare insures 52.9 million Americans; Medicare Advantage covers 30.8 million (51% of eligible Medicare, $454B / 54% of federal Medicare spending)
Owner:  Lokken complaint ¶4 (52.9M) and ¶25 (MA figures, citing KFF, Aug 2023)
Scope:  Scale context. MA figures are as of 2023.
```

```text
Figure: Cigna PXDX — 300,000+ denials over two months (2022); ~1.2 seconds average per case; ~60,000 by one director in one month
Owner:  ProPublica / The Capitol Forum, 03/25/2023
Scope:  Present-day parallel. Cigna's own review volume, disputed by Cigna as mischaracterized.
```

Named-party facts (verify exactly as written):
- **Gene B. Lokken**, 91, Wisconsin (Lincoln County). Fell 05/05/2022, fractured leg and
  ankle; admitted Aspirus Tomahawk Hospital; admitted to Tomahawk Health Services 05/11/2022.
  Coverage paid 07/01–07/20/2022, terminated ~07/20/2022; appeal rejected ~08/01/2022. Family
  paid $12,000–$14,000/month out of pocket, July 2022–July 2023. **Died 07/17/2023.** Estate is
  a named plaintiff. (Complaint ¶¶42-57.)
- **Dale Henry Tetzloff**, 74, Wisconsin (Portage County). Stroke 10/04/2022; doctor referred to
  SNF for at least 100 days; denied ~November 2022 after 20 days; on a second appeal a
  UnitedHealth doctor agreed he needed more time; denied again after 40 days. Out-of-pocket
  >$70,000 over ~10 months; discharged June 2023 to assisted living. **Died 10/11/2023.** Estate
  is a named plaintiff. (Complaint ¶¶58-68.)

---

## Source assets

```text
Asset: Sample nH Predict "Outcome" sheet reproduced in the complaint (¶33, p. 12),
       taken from a naviHealth presentation.
Shows: The tool's actual per-patient output — the numeric mobility/cognitive scores,
       estimated length of stay, and target discharge date. It makes the abstract
       "population average turned into a per-patient date" concrete: the reader sees a
       single elderly patient reduced to a discharge date on a form.
Crop:  Retain the length-of-stay / target-discharge fields and the patient-scoring rows.
       Omit nothing that identifies it as naviHealth's own document; it carries no real
       patient PII (it is a sample). Reproduce as a document image, not a redrawing.
```

```text
Asset: Senate PSI report, Appendix Table 1 — "Number of requests and denial rates by
       facility" / adverse-determination rates by type of post-acute care facility (p. 54).
Shows: The denial-rate rise across post-acute settings, insurer by insurer — the
       independent, non-litigant numbers behind the 10.9% → 22.7% figure.
Crop:  If charted, preserve axis labels and the year range; cite the PSI report in the
       caption. Do not compress multiple insurers into one bar without labeling.
```

```text
Asset (CMS FAQ): None found — the operative passage is text (Q2/Q8); quote it, do not image it.
```

---

## Discarded

```text
URL: https://www.courthousenews.com/wp-content/uploads/2025/02/UHG-judge-dissmisses-counts-opinion.pdf
     — The actual 02/13/2025 opinion, but returned HTTP 403 on fetch; could not read it
     firsthand. Ruling details are recorded from the legalhie summary and Georgetown tracker
     instead; if the article relies on the survived/dismissed breakdown, confirm against the
     docketed order.
```

```text
URL: https://en.wikipedia.org/wiki/NH_Predict
     — Tertiary; useful only as an index to primaries. Not cited.
```

```text
URL: https://sites.suffolk.edu/jhtl/2025/11/11/the-lokken-lawsuit-... (Suffolk JHTL)
     — Law-student commentary; secondary analysis, adds no primary fact the complaint/ruling
     do not already own. Not cited.
```

```text
URL: https://kffhealthnews.org/news/article/biden-administration-software-algorithms-medicare-advantage/
     — Solid secondary on the CMS guidance, but the CMS FAQ (primary) is read directly, so this
     is redundant. Available as reader-facing context if the writer wants a plain-language
     secondary on the rule.
```

```text
Figure discarded: "post-acute denial rate rose from 8.7% to 22.7%" (seen in search summaries)
     — The 22.7% (2022) is confirmed by the PSI report, but the 8.7% starting point does not
     match the PSI series (10.9% in 2020). Use the PSI figures (10.9% → 16.3% → 22.7%); drop
     the unverified 8.7%.
```
