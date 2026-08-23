# evidence: when-ai-breaks/michigan-midas (01)

The primary record strongly supports the commission's spine: from October 2013 to
August 2015 Michigan's MiDAS made unemployment-fraud determinations with no human
examiner, flagged claimants on data mismatches and an income-averaging formula,
notified them only through often-dormant online accounts, imposed a fraud penalty of
four times the benefits at issue (the state-law maximum), and collected by garnishing
wages and seizing tax refunds. Both federal opinions and the Michigan Supreme Court
recite this, and the mechanism is undisputed. The evidence is thin, and internally
inconsistent, on the two numbers a headline most wants. The famous "93% wrong" figure
belongs to the Unemployment Insurance Agency's own review reported in December 2016
(22,427 auto-adjudicated cases, 20,965 overturned) — not to the state Auditor General,
though two federal opinions say Auditor General. A second, fuller UIA review completed
in August 2017 found a different rate on a different denominator: 85% of the 40,195
purely computer-resolved fraud findings reversed, within 62,784 non-appealed penalty
cases representing 49,910 people. Any figure in the headline or dek must carry its own
denominator, period, and owner, or it will be wrong. The evidence also complicates the
litigation's ending: the Sixth Circuit in 2023 gave the agency supervisors qualified
immunity after discovery, recharacterizing the surviving claims as collection of
benefits actually paid — the state's strongest counter, which the piece must steelman.
I could not find the underlying case-level review data as a public document; the
state's own numbers live in a press release and in court recitations.

## Sources

```text
URL:         https://www.opn.ca6.uscourts.gov/opinions.pdf/19a0001p-06.pdf
Kind:        primary — the federal appellate opinion itself owns its factual recitation
             and holding. Cahoo v. SAS Analytics Inc., 912 F.3d 887 (6th Cir. 2019),
             Nos. 18-1295/1296, decided January 3, 2019, Clay, J.
Establishes: The mechanism, firsthand from the appellate record. MiDAS began October
             2013; searched claimant records against employer/state/federal data
             reaching back six years; flagged any discrepancy without checking for
             employer error or good-faith dispute; used an "income spreading" formula
             that averaged quarterly earnings across weeks so a claimant who reported
             no income for a week in a quarter where they earned income was
             automatically found to have committed fraud. On a flag MiDAS sent a
             multiple-choice questionnaire (verbatim in the opinion) to the claimant's
             online account only, gave ten days, and stated no basis for suspicion. A
             triggering answer or no response in ten days produced a "robo-adjudicated"
             fraud finding. "From October 2013 to August 2015, MiDAS exclusively
             determined whether claimants engaged in fraud — no human being took part
             in this process." Penalty = restitution plus four times benefits received
             or sought, "the maximum penalty permitted under state law," assessed even
             when no benefits were received; typical assessments $10,000-$50,000, some
             over $187,000. Collection by state and federal tax-refund interception,
             wage garnishment, and court action, available up to six years after a
             claimant stopped collecting. Holding: AFFIRMS denial of qualified immunity
             on the due-process claim; REVERSES on the equal-protection and Fourth
             Amendment claims.
Paraphrase:  A federal appeals court, taking the complaint as true at the pleading
             stage, described a system that decided fraud by computer alone for nearly
             two years, told claimants nothing of the basis, and punished at four times
             the amount; it let the due-process claim against individual agency
             officials proceed and dismissed the equal-protection and search claims.
Locators:    Statement of Facts, pp. 2-6; questionnaire text p. 4; four-times penalty
             p. 5; "no human being" p. 5; 93% recitation p. 6; holding p. 2.
Quote:       "From October 2013 to August 2015, MiDAS exclusively determined whether
             claimants engaged in fraud — no human being took part in this process."
             "the Michigan Auditor General reviewed over 22,000 of MiDAS' fraud
             determinations and found that 93% of them did not actually involve fraud.
             In other words, 93% of MiDAS' fraud adjudications were false-positives."
```

```text
URL:         https://www.mied.uscourts.gov/PDFFIles/17-10657OPN.pdf
Kind:        primary — the federal district opinion. Cahoo v. SAS Institute Inc.,
             322 F.Supp.3d 772 (E.D. Mich. 2018), No. 17-10657, David M. Lawson, J.,
             opinion and order on motions to dismiss, dated March 2, 2018.
Establishes: The vendors and their contracts, firsthand from the pleadings the court
             recites. FAST Enterprises LLC (Centennial, CO) contracted about August
             2011 to "design, create, implement, configure, control and maintain the
             MiDAS software," including fraud investigation, overpayments, collections,
             and tax intercepts. SAS Institute Inc. (Cary, NC) contracted about
             December 2012 to build the Enterprise Fraud Detection Software (EFDS)
             "used by the Agency to make unemployment insurance fraud determinations,"
             integrated with MiDAS; that contract expired December 2017. CSG Government
             Solutions (Chicago) contracted about January 2010 to run the Project
             Control Office with "oversight responsibility for all aspects of MiDAS."
             Also: penalty "four times" the benefits (p.5); assessments "$10,000 and
             $50,000 and sometimes exceeded $187,000"; the "Michigan Auditor General
             eventually determined that of the 22,427 robo-adjudications reviewed, over
             93% did not involve fraud at all"; "Between October 2013 and August 2015,
             MiDAS made all fraud determinations," after which agency personnel added
             oversight but "exercised no more discretion than their MiDAS counterpart";
             the earlier Zynda v. Arwood, 175 F.Supp.3d 791 (E.D. Mich. 2016), settled
             February 2, 2017, with the state agreeing to suspend automated-system
             collection and Michigan barring fraud findings based solely on
             computer-identified discrepancies.
Paraphrase:  The court identifies three separate contractors with distinct roles —
             FAST built and ran the MiDAS platform, SAS built the fraud-detection
             engine that generated the fraud analysis, CSG oversaw the project — which
             matters for the "which vendor" question, since the fraud logic was not all
             one company's.
Locators:    Facts, pp. 3-9 (mechanism pp. 4-6; 22,427/93% p. 6; vendors pp. 7-9);
             Zynda p. 2; date and signature p. 55.
Quote:       "the Michigan Auditor General eventually determined that of the 22,427
             robo-adjudications reviewed, over 93% did not involve fraud at all."
```

```text
URL:         https://www.courts.michigan.gov/4a1c19/siteassets/case-documents/opinions-orders/msc-term-opinions-(manually-curated)/21-22/bauserman-op.pdf
Kind:        primary — the Michigan Supreme Court opinion. Bauserman v. Unemployment
             Ins. Agency, 509 Mich 673; 983 NW2d 855 (2022), Docket 160813, decided
             July 26, 2022.
Establishes: The state high court's holding and its account of the two named
             plaintiffs. Held that plaintiffs stated a cognizable constitutional-tort
             claim for money damages for the alleged violation of due process under
             Const 1963, art 1, sec 17, because enforcement of that right was not
             delegated to the Legislature and no other adequate remedy existed; affirmed
             denial of summary disposition. Grant Bauserman collected benefits Sept
             2013-March 2014, received December 3, 2014 redeterminations of ineligibility
             and intentional misrepresentation, was told he owed $19,910, protested,
             had his tax refund intercepted June 16, 2015, and was later cleared (the
             agency declared the redeterminations "null and void" on September 30, 2015)
             and repaid. Teddy Broe was assessed penalties and interest "totaling more
             than $8,000," had tax refunds intercepted May 2015, and was later cleared
             and repaid. The court recites the notice defect: questionnaires "sent only
             to the claimant's electronic account with the Agency, without any additional
             notice via United States mail or e-mail." Footnote 5: "It has been
             estimated that, between 2013 and 2015, approximately 40,000 people in
             Michigan were wrongfully accused" (citing Time, May 28, 2020), and "a study
             conducted by the Agency concluded that, during this same period,
             approximately 93% of the automated system's fraud determinations were
             incorrect" (citing The Guardian, Dec 18, 2016).
Paraphrase:  Michigan's highest court let wrongly accused claimants sue the state for
             damages, and — unlike the two federal opinions — credited the 93% figure to
             a study by the Agency itself, not the Auditor General.
Locators:    Syllabus and holding pp. 1-3; plaintiffs' facts pp. 2-4; questionnaire
             notice pp. 4-5; 40,000 and 93% at footnote 5, pp. 16-17.
Quote:       "a study conducted by the Agency concluded that, during this same period,
             approximately 93% of the automated system's fraud determinations were
             incorrect."
```

```text
URL:         https://caselaw.findlaw.com/court/us-6th-circuit/2285148.html
Kind:        primary — the 2023 federal appellate opinion (its own full text on this
             page; page is browser-gated, returns 403 to a bare request). Cahoo v. Fast
             Enterprises LLC, Nos. 21-1407/2672 (6th Cir. June 15, 2023).
Establishes: The litigation's endpoint against the individual agency officials and the
             state's strongest factual counter. After discovery, the court REVERSED the
             denial of qualified immunity to agency supervisors Sharon Moffet-Massey and
             Steven Geskey. It reasoned that discovery showed the process was more
             protective than the complaint alleged — claimants received notices of
             determination before any deprivation, with a 30-day appeal period and
             multi-level administrative review — and that what "was once a
             termination-of-benefits case has evolved into what is a collection-of-paid-
             benefits case," with no precedent putting these officials on notice that the
             procedures violated due process.
Paraphrase:  The same court that in 2019 let the due-process claim proceed later shielded
             the two remaining agency supervisors, on a fuller record that showed some
             notice and appeal existed and that most reversals concerned benefits the
             claimants had in fact been paid.
Locators:    Majority opinion, holding and "collection-of-paid-benefits" characterization.
Quote:       "We reverse the district court's denial of qualified immunity as to
             Moffett-Massey and Geskey."
```

```text
URL:         https://www.michigan.gov/leo/news/2017/08/11/michigans-unemployment-agency-completes-review-of-fraud-determination-cases-comprehensive-changes-u
Kind:        primary — the state agency's own statement of its 2017 review results
             (browser-gated; returns 403 to a bare request, loads in a browser). Talent
             Investment Agency - Unemployment Insurance, press release, August 11, 2017,
             Director Wanda M. Stokes. This is "the UIA's own 2017 review" the commission
             names.
Establishes: The fullest state-owned figures. The agency reviewed all cases between
             October 2013 and August 2015 where fraud was alleged; "These cases represent
             49,910 people." 4,955 cases were resolved through appeals. Of the 62,784
             cases "for which people were assessed a fraud penalty and did not seek an
             appeal," 40,195 "were originally resolved by way of computer program based on
             available information," and "85 percent of these original fraud findings were
             reversed." The other 22,589 were "initiated by computer program and then
             referred to an investigator," and "44 percent of these fraud findings were
             reversed." The agency was "refunding more than $20.8 million." Most reversals
             were cases where the claimant was overpaid but did not intend fraud. Confirms
             the automated system was no longer used for fraud determinations after this
             period.
Paraphrase:  The agency's own 2017 accounting reversed 85% of its purely computer-decided
             fraud findings and 44% of its computer-flagged-then-reviewed findings, across
             a population of 49,910 people, and refunded more than $20.8 million — figures
             larger and more granular than the 2016 "93% of 22,427" number.
Locators:    Body paragraphs on the 49,910 people, the 4,955 appeals, and the 62,784
             / 40,195 / 22,589 breakdown with the 85% and 44% reversal rates.
Quote:       "Of those cases, 40,195 were originally resolved by way of computer program
             based on available information. As part of the review, 85 percent of these
             original fraud findings were reversed."
```

```text
URL:         https://audgen.michigan.gov/finalpdfs/15_16/r641059315.pdf
Kind:        primary — Michigan Office of the Auditor General, Performance Audit Report,
             "Michigan Integrated Data Automated System (MiDAS)," report 641-0593-15,
             released February 2016.
Establishes: Context and one negative finding for the attribution question. Confirms
             MiDAS "was fully implemented in October 2013" and that in FY2014 UIA paid
             "$1 billion in unemployment insurance benefits for 611,503 claims." The
             audit is a security- and controls-focused performance audit (security
             management, access controls, claim-processing controls, appeals-process
             efficiency, additional-automation opportunities). It does NOT contain the
             "93%" fraud-error finding. This is the only OAG performance audit of MiDAS
             in the record, which is why crediting the "93%" to the Auditor General is
             imprecise.
Paraphrase:  The state auditor's actual MiDAS audit is about IT security and controls
             and does not produce the 93% figure the federal opinions attribute to it.
Locators:    Report Summary p. 1 (October 2013; $1 billion / 611,503 claims); findings
             list pp. 1-2.
Quote:       "MiDAS was fully implemented in October 2013."
```

```text
URL:         https://www.michigan.gov/ag/news/press-releases/2022/10/20/som-settlement-of-civil-rights-class-action-alleging-false-accusations-of-unemployment-fraud
Kind:        primary — Michigan Department of Attorney General press release, October
             20, 2022 (browser-gated). Announces the Bauserman settlement.
Establishes: The Bauserman resolution. A $20 million settlement in Bauserman v.
             Unemployment Insurance Agency, filed in the Michigan Court of Claims in
             2015, for a class alleging MiDAS "falsely accuse[d] thousands of
             Michiganders of unemployment fraud, resulting in the wrongful seizure of
             their paychecks, income tax refunds, and other assets without due process."
             Eligibility runs to claimants who had money collected for the first time on
             or after March 9, 2015 (the class was narrowed by the earlier accrual
             ruling). The Court of Claims approved the settlement in late January 2024.
Paraphrase:  The state agreed to pay $20 million to a class of wrongly accused claimants;
             the limitations ruling cut the eligible group to first-collection dates on
             or after March 9, 2015.
Locators:    Release body: settlement amount, case name/court, class scope.
Quote:       "$20 million."
```

```text
URL:         https://www.michiganpublic.org/politics-government/2016-12-16/state-review-93-of-state-unemployment-fraud-findings-were-wrong
Kind:        secondary — Michigan Radio (Michigan Public) news report, December 16,
             2016. Reports on the state's review from outside the agency.
Establishes: Independent corroboration that the 93% finding came from "a new state
             review" (the UIA), not the Auditor General; that MiDAS "flagged 53,633
             cases of fraud" between late 2013 and mid-2015; and that the state had
             "already repaid $5.4 million to those wrongly found guilty of fraud." The
             93% and late-2013-to-mid-2015 period match the primary record.
Paraphrase:  Contemporaneous state-press reporting attributes the 93% to a state (UIA)
             review and adds a distinct "53,633 flagged" figure and an early $5.4 million
             refund total.
Locators:    Lede and body (state review; 93%; 53,633 flagged; $5.4 million).
Quote:       "a new state review."
```

```text
URL:         https://www.govtech.com/data/Michigan-Integrated-Data-Automated-System-Experiences-93-Percent-Error-Rate-During-Nearly-Two-Years-of-Operation.html
Kind:        secondary — Government Technology news report (republishing local
             reporting), July 31, 2017.
Establishes: Independent corroboration of the contract value and the operating window.
             Describes a "$47-million computer system," a "93% error rate during the
             close to two years it operated without active human oversight," "at least
             20,000 Michigan residents" falsely accused, an operating window of "October
             1, 2013 to August 7, 2015," "Michigan's highest-in-the-nation quadruple
             penalties," and collection by "wage garnishes and seizure of income tax
             refunds." Notes administrative law judges surfaced the problem through
             appeal decisions.
Paraphrase:  Trade-press reporting supplies the $47 million contract figure and the
             exact operating dates, and frames the penalty as the nation's highest.
Locators:    Body (contract value; dates; 20,000; quadruple penalty; collection).
Quote:       "93% error rate during the close to two years it operated without active
             human oversight."
```

## Contradictions

- Owner of the "93%" figure. The two federal opinions attribute "over 22,000 / 93%"
  to "the Michigan Auditor General" (Cahoo, 322 F.Supp.3d 772, p.6; Cahoo, 912 F.3d
  887, p.6). The Michigan Supreme Court attributes it to "a study conducted by the
  Agency" (Bauserman, footnote 5). Michigan Radio calls it "a new state review." The
  only OAG performance audit of MiDAS in the record (report 641-0593-15, Feb 2016) is
  an IT-controls audit that does not contain the 93% finding. Resolution: the 93%
  belongs to the UIA's own review reported in December 2016; the federal opinions'
  "Auditor General" label traces to the plaintiffs' complaint paragraphs those opinions
  cite and is imprecise. A headline crediting the state auditor with the 93% would be
  wrong.

- Which rate, which denominator. "93% of 22,427" (auto-adjudicated cases, reported
  December 2016, with 20,965 overturned) versus "85% of 40,195" purely computer-resolved
  findings and "44% of 22,589" computer-flagged-then-investigated findings (the UIA's
  August 2017 review, within 62,784 non-appealed penalty cases). Same October 2013-August
  2015 window, different populations and review dates. Both are the UIA's own figures.
  These are not interchangeable, and neither is "the" error rate without its denominator.

- Affected-count figures measure different things. 53,633 "flagged for fraud" (Michigan
  Radio); ~40,000 "wrongfully accused" (Time estimate, via Bauserman fn 5); 62,784
  non-appealed penalty cases and 49,910 people in the reviewed universe (UIA Aug 2017);
  ~20,000-20,965 overturned (Dec 2016 review); 40,195 reversed among the purely
  computer-resolved cases (Aug 2017). Flagged is not accused is not penalized is not
  reversed is not people. Resolution: for a state-owned "people affected," use the
  49,910 from the August 2017 review, and label 40,000 an estimate.

- The two headline "outcomes" point opposite ways. The Michigan Supreme Court (2022)
  let claimants sue the state for damages; the Sixth Circuit (2023) granted the agency
  supervisors qualified immunity. These are different courts, defendants, and legal
  theories (a Michigan constitutional-tort claim against the Agency versus federal
  Section 1983 claims against individual officials), not a direct conflict — but a piece
  must state each precisely rather than pick the convenient one.

- Human review after August 2015. The complaint alleged roughly 50% of determinations
  were still invalid once humans were added (912 F.3d 887, p.6); the UIA's August 2017
  review found 44% of the computer-flagged-then-investigated cases reversed. Roughly
  consistent; both indicate adding a human on top of the same flags did not fix it.

- Vendor identity. Common shorthand (and the commission's framing) says "Fast
  Enterprises built MiDAS." True for the MiDAS platform, but the district opinion shows
  the fraud-detection engine that produced the fraud analysis was SAS's EFDS, integrated
  into MiDAS, and CSG ran project oversight. "The vendor" is three companies with
  different roles; the fraud logic was not solely FAST's.

## Numbers

```text
Figure: MiDAS made all fraud determinations with no human examiner, October 2013-August 2015
Owner:  Cahoo, 912 F.3d 887 (6th Cir. 2019), p.5; Cahoo, 322 F.Supp.3d 772 (E.D. Mich. 2018), p.6
Scope:  The fully automated period; both opinions state it plainly
```

```text
Figure: 93% of auto-adjudicated fraud determinations did not involve fraud; 22,427 reviewed; 20,965 overturned
Owner:  UIA's own review reported December 2016 (corroborated: Michigan Radio, Dec 16, 2016; recited in both federal opinions and in Bauserman fn 5). 22,427 and "over 93%": Cahoo, 322 F.Supp.3d 772, p.6
Scope:  Auto-adjudicated fraud cases, October 2013-August 2015; initial refunds $5.4 million to 2,571 people (Michigan Radio)
```

```text
Figure: 85% of purely computer-resolved fraud findings reversed; 40,195 such cases
Owner:  Talent Investment Agency-UI press release, August 11, 2017
Scope:  Within the 62,784 penalty cases that were not appealed, October 2013-August 2015
```

```text
Figure: 44% of computer-flagged-then-investigated fraud findings reversed; 22,589 such cases
Owner:  Talent Investment Agency-UI press release, August 11, 2017
Scope:  The remainder of the 62,784 non-appealed penalty cases, same period
```

```text
Figure: 49,910 people in the reviewed universe; 4,955 cases resolved through appeals; more than $20.8 million refunded
Owner:  Talent Investment Agency-UI press release, August 11, 2017
Scope:  All October 2013-August 2015 cases where fraud was alleged
```

```text
Figure: Approximately 40,000 people wrongfully accused, 2013-2015
Owner:  Estimate; Time Magazine (May 28, 2020), cited in Bauserman fn 5 — secondary, an estimate not a state count
Scope:  The full fully-automated period
```

```text
Figure: 53,633 cases flagged for fraud
Owner:  Michigan Radio (Michigan Public), Dec 16, 2016 — secondary
Scope:  Late 2013 to mid-2015
```

```text
Figure: Fraud penalty = four times benefits received or sought, the state-law maximum; assessed even if no benefits received
Owner:  Cahoo, 912 F.3d 887, p.5; Cahoo, 322 F.Supp.3d 772, p.5
Scope:  Per fraud determination; typical assessments $10,000-$50,000, some over $187,000
```

```text
Figure: $19,910 assessed against Grant Bauserman; over $8,000 against Teddy Broe
Owner:  Bauserman, 509 Mich 673 (2022), pp.2-3
Scope:  The two named plaintiffs; both later cleared and repaid
```

```text
Figure: $47 million MiDAS contract; operating window October 1, 2013-August 7, 2015
Owner:  Government Technology, July 31, 2017 — secondary (contract value not found in a primary I read)
Scope:  System cost and exact automated-operation dates
```

```text
Figure: $1 billion in UI benefits paid for 611,503 claims, FY2014
Owner:  Michigan Office of the Auditor General, report 641-0593-15 (Feb 2016), p.1
Scope:  Fiscal year 2014, program scale context
```

```text
Figure: Bauserman settlement $20 million; eligibility to first collection on/after March 9, 2015; approved late January 2024
Owner:  Michigan Attorney General press release, October 20, 2022; approval reported January 2024
Scope:  The Court of Claims class action against the UIA
```

```text
Figure: Vendor contracts — FAST (~Aug 2011, MiDAS platform), SAS (~Dec 2012, EFDS fraud engine, expired Dec 2017), CSG (~Jan 2010, project oversight)
Owner:  Cahoo, 322 F.Supp.3d 772 (E.D. Mich. 2018), pp.7-9
Scope:  Roles and approximate contract dates
```

## Source assets

```text
Asset: The multiple-choice fraud questionnaire, quoted in full in Cahoo, 912 F.3d 887, p.4
Shows: The actual instrument that triggered a "fraud" finding — the yes/no intent
       question and the eight canned reasons — which lets a reader see how thin the
       "adjudication" was.
Crop:  Reproduce as a text block, not an image; retain the "Did you intentionally
       provide false information..." line and the numbered options verbatim. Omit
       nothing that changes the logic.
```

```text
Asset: The 62,784 / 40,195 (85% reversed) / 22,589 (44% reversed) breakdown in the
       August 11, 2017 TIA-UI press release
Shows: The state's own tally, which supports a small honest table separating purely
       computer-decided cases from computer-flagged-then-reviewed cases and their
       different reversal rates.
Crop:  If built into a chart, label each bar with its denominator and reversal rate and
       cite the press release and date in the caption; do not merge the two buckets into
       one "error rate."
```

```text
Asset: Michigan Office of the Auditor General report 641-0593-15 (Feb 2016), Report
       Summary page with the audit-objective conclusions
Shows: That the auditor's MiDAS audit concerned security and controls — useful if the
       piece needs to show visually why "the auditor found 93%" is wrong.
Crop:  Retain the objective/conclusion labels; this is documentary evidence for the
       attribution point, not decoration.
```

```text
Asset: None found for a single canonical "affected people" figure — the state never
       published one clean number, and the review data lives in a press release and
       court recitations rather than a chartable public dataset.
Shows: n/a
Crop:  n/a
```

## Discarded

```text
URL: https://www.opn.ca6.uscourts.gov/opinions.pdf/19a0209p-06.pdf — wrong case (Ermold v. Davis, the Kim Davis marriage-license matter); it only cites Cahoo in passing.
URL: https://www.opn.ca6.uscourts.gov/opinions.pdf/21a0007p-06.pdf and 23a0128p-06.pdf — not Cahoo; they cite Cahoo's qualified-immunity standard but are other cases (the 23a file is Sterling Hotels v. McKay).
URL: https://audgen.michigan.gov/wp-content/uploads/2022/03/r186031021-7565.pdf — OAG audit 186-0310-21 (March 2022) is about UIA personnel management during COVID-19, unrelated to MiDAS fraud.
URL: https://www.theguardian.com/us-news/2016/dec/18/michigan-unemployment-agency-fraud-accusations — the secondary the Michigan Supreme Court cites for the 93%; not independently retrievable here (blocked). Recorded as cited-by-the-court, not read; Michigan Radio (read) serves the same corroboration.
URL: https://bridgemi.com/michigan-government/broken-human-toll-michigans-unemployment-fraud-saga/ — relevant human-toll secondary, but returned 403 and was not read; not relied on.
URL: https://stpp.fordschool.umich.edu/sites/stpp/files/2024-08/stpp-midas-explainer.pdf — a University of Michigan policy explainer (useful synthesis) but its compressed PDF did not extract cleanly; not relied on for any figure.
URL: law.justia.com/cases/federal/appellate-courts/ca6/18-1296/... — reprint of the 2019 opinion; blocked (403). The official ca6 PDF (19a0001p-06.pdf) was used instead.
```
