# Evidence record: when-ai-breaks/cigna-pxdx

Every source below was opened and read. Every URL returned HTTP 200 on
2026-09-09. Figures are quoted from the primary reporting and the court filing,
not from memory. github.com is not cited (egress blocked here; not relevant).

Floor check: 8 sources, 5 primary, 3 secondary.

## Sources

### S1 — PRIMARY. ProPublica / The Capitol Forum, "How Cigna Saves Millions by Having Its Doctors Reject Claims Without Reading Them" (Mar 25, 2023)
URL: https://www.propublica.org/article/cigna-pxdx-medical-health-insurance-rejection-claims
Authors: Patrick Rucker (The Capitol Forum), Maya Miller and David Armstrong (ProPublica).
Supports:
- The core figures, verbatim: "over a period of two months" in 2022, "Cigna
  doctors denied over 300,000 requests for payments using this method, spending
  an average of about 1.2 seconds on each case."
- The mechanism: Cigna built a "procedure-to-diagnosis" (PXDX) list that flags
  when a billed procedure does not match an accepted diagnosis; doctors "sign off
  on the denials in batches" without opening patient files.
- Named doctors and per-doctor volume (first two months of 2022): Dr. Cheryl
  Dopke reviewed 121,000 claims; Dr. Richard Capek about 80,000; Dr. Paul Rossi
  about 63,000.
- Quote, former Cigna doctor: "We literally click and submit. It takes all of 10
  seconds to do 50 at a time."
- Quote, Dr. Alan Muney (helped design the system): "the PXDX stuff is not
  reviewed by a doc or nurse or anything like that."
- Cigna's on-record framing: the system exists to speed payment for certain
  routine, low-cost claims.

### S2 — PRIMARY. Class Action Complaint, Kisting-Leung and Smiley v. Cigna Corporation et al., E.D. Cal., filed Jul 24, 2023 (Case 2:23-at-00698, later 2:23-cv-01477)
URL: https://litigationtracker.law.georgetown.edu/wp-content/uploads/2023/08/Kisting-Leung_20230724_COMPLAINT.pdf
Read via local text extraction of the filed PDF (18 pages).
Supports:
- Named plaintiffs Suzanne Kisting-Leung and Ayesha Smiley; Clarkson Law Firm.
- Para 1: the suit is about denying insureds "the thorough, individualized
  physician review of claims guaranteed to them by California law." Cigna has
  "approximately 2.1 million members in California."
- Para 2 repeats the ProPublica figure: "over a period of two months in 2022,
  Cigna doctors denied over 300,000 requests for payments using this method,
  spending an average of just 1.2 seconds 'reviewing' each request."
- Para 4: appeal rate alleged at "roughly .2%" of policyholders.
- Para 17: the legal duty. Under California Insurance Regulations, Cal. Code
  Regs. tit. 10, § 2695.7(d), Cigna must conduct a "thorough, fair, and
  objective" investigation of each bill; "Cigna's medical directors must examine
  patient records, review coverage policies, and use their expertise."
- Concrete case (paras 26-32): Kisting-Leung, enrolled since 2018, had a
  transvaginal ultrasound on Aug 19, 2022 after a referral for suspected ovarian
  cancer risk (found a dermoid cyst). On/around Oct 17, 2022 Cigna denied the
  claim as "not medically necessary," leaving her a $198 bill, even though
  Cigna's own Medical Coverage Policy calls the procedure "medically necessary
  for the evaluation of suspected pelvic pathology or for screening or
  surveillance of a woman at increased risk for ovarian or endometrial cancer."
- Four causes of action: breach of the implied covenant of good faith and fair
  dealing; California Unfair Competition Law (Bus. & Prof. Code § 17200);
  intentional interference with contractual relations; unjust enrichment.
NOTE on standing: figures 300,000 / 1.2s are the complaint's allegations
(quoting S1). Whether any individual named plaintiff's claim went through PxDx is
contested; see S5. Present the plaintiff cases as allegations, not settled fact.

### S3 — PRIMARY. Cigna Healthcare, "Cigna Healthcare Affirms its Approach to Expediting Physician Payments" (Jul 27, 2023)
URL: https://newsroom.cigna.com/2023-07-27-Cigna-Healthcare-Affirms-its-Approach-to-Expediting-Physician-Payments
Supports (Cigna's own words, the steelman):
- "The post-treatment review process works through software (not artificial
  intelligence or an algorithm) that matches the codes submitted by the physician
  with diagnosis codes."
- "Patients are not denied care through this review in any way -- it occurs after
  the patient has received treatment."
- "This process is used for approximately 50 low-cost tests and procedures."
- Cigna's claim that the reporting created confusion/misunderstanding about how
  PxDx works. Cigna calls the process a payment-acceleration tool, not a care
  denial.
This is the primary source for the precision point: Cigna itself denies AI/ML and
frames PxDx as post-service payment review.

### S4 — PRIMARY. U.S. House Committee on Energy and Commerce, "E&C Republicans Press Cigna for Clarification After Investigative Report Accuses Insurance Company of Denying Claims Without Reading Them" (May 16, 2023)
URL: https://energycommerce.house.gov/posts/e-and-c-republicans-press-cigna-for-clarification-after-investigative-report-accuses-insurance-company-of-denying-claims-without-reading-them
Signatories: Chair Cathy McMorris Rodgers (R-WA), Health Subcommittee Chair Brett
Guthrie (R-KY), Oversight Subcommittee Chair Morgan Griffith (R-VA). Response
demanded by May 30, 2023.
Supports:
- Oversight/regulator attention is real and documented (primary government
  record), not just press.
- The committee's framing: "The PXDX review process automatically categorizes
  certain claims as 'unnecessary' using an algorithm in place of a clinician's
  judgement."
- Reversal-rate anchor: the letter notes about "80 percent of Medicare Advantage
  coverage denials were overturned" on appeal and that "nearly one-in-five" such
  denials were appealed; roughly "five percent of policy-holders appeal denials."
  Use these as the committee's cited figures (Medicare Advantage context), not as
  PxDx-specific rates.

### S5 — PRIMARY. Georgetown Health Care Litigation Tracker, "Kisting-Leung et al. v. Cigna Corporation et al." case record (order on motion to dismiss, Mar 31, 2025)
URL: https://litigationtracker.law.georgetown.edu/litigation/kisting-leung-et-al-v-cigna-corporation-et-al/
Supports:
- Case No. 2:23-cv-01477, E.D. Cal., Judge Dale A. Drozd. Status: proceeding;
  discovery deadline Sep 30, 2026.
- A Mar 31, 2025 order on the motion to dismiss let core claims proceed. Cross-
  referenced with S8: the court allowed an ERISA fiduciary-breach theory (finding
  Cigna's use of PxDx to read plan terms "was an abuse of discretion") and a
  California Unfair Competition Law claim to go forward.
- Plaintiff Abdulhussein Abbas was dismissed. Some named plaintiffs were found to
  lack standing because their claims were not shown to have been denied through
  PxDx review. This is the evidence for the "individual denials are contested"
  caveat.

### S6 — SECONDARY. STAT News, "Lawsuit says Cigna illegally denies claims in bulk, sticking patients with unexpected bills" (Jul 24, 2023)
URL: https://www.statnews.com/2023/07/24/cigna-lawsuit-claim-denials/
Supports: independent contemporaneous report of the suit; repeats the 300,000 /
1.2-seconds figures; states California law requires each claim get a "thorough,
fair, and objective investigation." Corroborates S1 and S2.

### S7 — SECONDARY. ProPublica / The Capitol Forum, "Cigna Faces Congressional Investigation..." follow-up (May 16, 2023)
URL: https://www.propublica.org/article/cigna-health-insurance-denials-pxdx-congress-investigation
Supports (follow-up reporting that held up):
- State insurance departments in Washington, California, and Delaware opened
  inquiries; the U.S. Department of Labor expressed concern.
- Cigna's dispute, direct quote: it welcomes "the opportunity to fully explain
  our PxDx process to regulators and correct the many mischaracterizations and
  misleading perceptions ProPublica's article created."
- Cigna's four points of dispute: denials of payment vs. denials of care, and
  whether doctors were incentivized to deny.

### S8 — SECONDARY. NFP, "Court Allows Lawsuit Over AI Use in Benefit Denials to Proceed" (2025 analysis of the Mar 31, 2025 ruling)
URL: https://www.nfp.com/insights/court-allows-lawsuit-over-ai-use-in-benefit-denials-to-proceed/
Supports: the ruling let an ERISA fiduciary-breach claim proceed on a finding
that Cigna's interpretation of plan terms to use PxDx "was an abuse of
discretion," plus a California UCL claim. Corroborates S5 on the outcome.

## Figures verified against primary reporting
- 300,000+ denials in two months of 2022 — S1 (reporting), S2 para 2 (complaint).
- ~1.2 seconds average per case — S1, S2 para 2.
- Per-doctor counts (Dopke 121,000; Capek ~80,000; Rossi ~63,000) — S1.
- "10 seconds to do 50 at a time" — S1 (former doctor).
- ~0.2% appeal rate alleged — S2 para 4. (Distinct from the Medicare Advantage
  appeal/reversal figures in S4; keep them separate.)
- ~50 low-cost procedures; "software (not AI or an algorithm)"; post-treatment
  review — S3 (Cigna).
- $198 bill, transvaginal ultrasound, Aug/Oct 2022 — S2 paras 27-30.
- Cal. Code Regs. tit. 10, § 2695.7(d) "thorough, fair, and objective" — S2 para 17.
- 2.1 million California members — S2 para 1.

## Handling notes for the writer
- Do not write "AI" or "machine learning" as a description of PxDx. It is code-
  matching software. Cigna denies AI on the record (S3); the reporting describes
  a list-match, not a learned model (S1).
- The 300,000 / 1.2s figures are Cigna's own internal data as reported by S1 and
  repeated in the sworn complaint S2. Attribute to the reporting.
- Present Cigna's steelman (S3, S7) and say what the court has and has not
  settled (S5, S8): core claims proceed; individual denials still contested.
