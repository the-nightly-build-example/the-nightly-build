# Evidence: when-ai-breaks/workday-hiring-screening (01)

The record strongly supports the commissioned angle and sharpens its proven-versus-alleged
line. What is **established** is legal, not factual: in *Mobley v. Workday, Inc.*, No.
3:23-cv-00770-RFL (N.D. Cal.), Judge Rita F. Lin held on a motion to dismiss that a software
vendor can be sued as an "agent" of the employers that use its tools, and later granted
preliminary certification of a nationwide ADEA collective. Both rulings accept Mobley's
allegations as true at their procedural stage and decide nothing about whether Workday's tools
actually discriminate. No court has found Workday's software discriminatory; the case is in
discovery and pre-notice as of the latest order I read (March 6, 2026). The evidence for the
mechanism (how automated screening produces disparate impact) and the doctrine (what disparate
impact means) is well-anchored in the EEOC's technical assistance and *Griggs v. Duke Power*.
Two things are thinner than the rest and flagged below: (1) the broad "how widespread" figure
for the closing turn rests best on Workday's own filing (1.1 billion applications), with survey
data as weaker secondary context; and (2) the federal-posture shift (EEOC pulled its AI guidance
in January 2025; a 2025 executive order de-prioritizes disparate-impact enforcement) is real and
I verified the guidance page is now gone, but the executive-order specifics come from secondary
reporting, not the order's own text. The angle is not undermined. The strongest counter-material
is that the "agent" theory is a pleading-stage, trial-court ruling, contested on the law and
untested on appeal, which the article must state rather than dress up as a verdict.

Distinguish throughout: **Workday is the vendor.** Its tools named in the record are Candidate
Skills Match (CSM) and the Workday Assessment Connector (WAC), plus the later-acquired HiredScore
features (Spotlight and Fetch). "pymetrics" is a third-party assessment product Workday's tools
are alleged to integrate. Where the alleged discrimination originates (Workday's own algorithms
versus employer-set preferences the tools implement) is a merits question the court expressly
left for later.

---

## Sources

```text
URL:         https://storage.courtlistener.com/recap/gov.uscourts.cand.408645/gov.uscourts.cand.408645.80.0_1.pdf
Kind:        Primary. The court's own order; the document that owns the "agent" holding.
             (Reported at 740 F. Supp. 3d 796. Not in the govinfo package, which begins at
             Doc 128; this is the filed PDF hosted by CourtListener/RECAP and it resolves.)
Establishes: Order Granting in Part and Denying in Part Motion to Dismiss, Doc 80, filed
             07/12/24, Judge Rita F. Lin. On a Rule 12(b)(6) motion (allegations taken as
             true), the court (a) DENIED dismissal of the Title VII/ADEA/ADA disparate-impact
             claims on an AGENT theory; (b) GRANTED dismissal, without leave, of the
             employment-agency theory; (c) GRANTED dismissal, without leave, of the
             intentional-discrimination claims (Title VII, ADEA, Section 1981); (d) GRANTED
             dismissal of the FEHA aiding-and-abetting claim with leave to amend. It did not
             reach the indirect-employer theory. It made NO finding that Workday discriminated.
Paraphrase:  Title VII, the ADA, and the ADEA define "employer" to include "any agent" of an
             employer, so an employer cannot escape liability by delegating a traditional
             function like hiring to a third party. A third-party agent is itself liable as an
             "employer" where it has been delegated a function "traditionally exercised by an
             employer." The FAC plausibly alleges Workday's customers delegated the traditional
             hiring function of rejecting applicants and advancing others to Workday's tools,
             which "participat[e] in the decision-making process" rather than implementing
             employer criteria "in a rote way." That the decision runs through AI rather than a
             human reviewer does not change the analysis; courts focus on the delegated
             function, not the manner of performance. By contrast, a spreadsheet or email
             vendor is not an agent because it does not participate in deciding whom to reject.
             Workday is NOT an "employment agency" because Mobley does not allege it "procures"
             employees or finds job opportunities for applicants. The disparate-impact claim
             survives: the FAC pleads a specific practice (algorithmic screening), a disparity
             (a zero-percent success rate across 100-plus qualified applications spanning many
             employers), and causation (the volume and timing of rejections plus alleged
             training-data bias). The intentional-discrimination claims fail for want of pleaded
             intent; awareness of adverse effects is not enough.
Locators:    Agent holding at pp. 5-11; employment-agency dismissal pp. 12-13; disparate impact
             pp. 13-16; intentional discrimination pp. 16-18; FEHA pp. 19-20; conclusion p. 20.
             ADEA-covers-applicants point at p. 16 n.4 (relying on Rabin v.
             PricewaterhouseCoopers, 236 F. Supp. 3d 1126 (N.D. Cal. 2017)).
Quote:       "Employers cannot escape liability for discrimination by delegating their
             traditional functions, like hiring, to a third party." (p. 5)
             "Workday's role in the hiring process is no less significant because it allegedly
             happens through artificial intelligence rather than a live human being who is
             sitting in an office going through resumes manually to decide which to reject." (p. 10)
             "Workday does qualify as an agent because its tools are alleged to perform a
             traditional hiring function of rejecting candidates at the screening stage and
             recommending who to advance to subsequent stages, through the use of artificial
             intelligence and machine learning." (p. 11)
             "The FAC adequately alleges that Workday is an agent of its client-employers, and
             thus falls within the definition of an 'employer' for purposes of Title VII, the
             ADEA, and the ADA." (p. 11)
```

```text
URL:         https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-cv-00770/pdf/USCOURTS-cand-3_23-cv-00770-1.pdf
Kind:        Primary. The court's own order (official government copy), owns the collective
             definition and the certification holding.
Establishes: Order Granting Preliminary Collective Certification, Doc 128, filed 05/16/25,
             Judge Lin. GRANTED preliminary (conditional) certification of a nationwide ADEA
             collective. This authorizes notice and opt-in; it is not a merits ruling and is
             expressly revisitable via decertification after discovery.
Paraphrase:  The collective is "[a]ll individuals aged 40 and over who, from September 24, 2020,
             through the present, applied for job opportunities using Workday's job application
             platform and were denied employment recommendations." Certification uses the Ninth
             Circuit's two-step process (Campbell v. City of Los Angeles): step one is "loosely
             akin to a plausibility standard," step two (decertification) is a harder look after
             discovery. Mobley met step one by substantially alleging a "unified policy" — use
             of Workday's AI recommendation system to "score, sort, rank, or screen" applicants
             — whose disparate impact on applicants over 40 is susceptible to common proof.
             Four other plaintiffs over 40 joined. The court rejected, for this stage, Workday's
             arguments that it makes no "recommendations," that employers' ability to toggle AI
             features defeats uniformity, and that variation in applicants' qualifications and
             rejection rates makes any collective impossible; each was preserved for stage two.
             Size is not a bar to notice: if the collective runs to "hundreds of millions,"
             that is because Workday is "plausibly accused of discriminating against a broad
             swath of applicants."
Locators:    Collective definition pp. 2-3 and p. 17; standard/two-step pp. 5-8; unified-policy
             analysis pp. 8-13; "recommend" dispute pp. 9-11; qualifications/standing pp. 13-17;
             size and 1.1 billion figure pp. 18-19.
Quote:       "The proposed collective is similarly situated because Mobley has substantially
             alleged the existence of a unified policy: the use of Workday's AI recommendation
             system to score, sort, rank, or screen applicants." (p. 1)
             "If the collective is in the 'hundreds of millions' of people, as Workday
             speculates, that is because Workday has been plausibly accused of discriminating
             against a broad swath of applicants. Allegedly widespread discrimination is not a
             basis for denying notice." (p. 2)
```

```text
URL:         https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-cv-00770/pdf/USCOURTS-cand-3_23-cv-00770-3.pdf
Kind:        Primary. The court's own order; owns the collective's scope as to HiredScore.
Establishes: Order re HiredScore Dispute, Doc 158, filed 07/29/25, Judge Lin. At the
             preliminary-certification stage, the collective INCLUDES applicants scored, sorted,
             ranked, or screened using the AI features in Workday's HiredScore product
             (Spotlight and Fetch), even though Workday acquired HiredScore after the operative
             complaint. Distinctions between HiredScore's algorithms and CSM are for the
             decertification stage.
Paraphrase:  Workday argued HiredScore is a separate product on a separate platform, acquired
             after the FAC, and different enough to require subclasses. The court held that the
             unified policy substantially alleged is Workday's AI recommendation system broadly,
             not just Workday Recruiting, and that later or expanded AI features fall within
             scope at this stage; algorithmic differences go to decertification, not now.
Locators:    Whole order, 2 pp. HiredScore products named at p. 1; scope holding at p. 2.
Quote:       "The scope of the collective, at the preliminary certification stage, includes
             individuals whose applications were scored, sorted, ranked, or screened using
             HiredScore AI features." (p. 2)
```

```text
URL:         https://www.govinfo.gov/content/pkg/USCOURTS-cand-3_23-cv-00770/pdf/USCOURTS-cand-3_23-cv-00770-13.pdf
Kind:        Primary. The court's own order; the latest ruling I located, and the record's
             current-status anchor.
Establishes: Order Granting Motion for Leave to File Amicus Brief and Granting in Part and
             Denying in Part Motion to Dismiss and to Strike (the Second Amended Complaint),
             Doc 267, filed 03/06/26, Judge Lin. Confirms the case's posture after two prior
             MTD rounds and shows it is still in the pleadings/discovery phase, with no merits
             ruling. Three new named plaintiffs (Jill E. Hughes, Sheilah Johnson-Rocha,
             Faithlinh Rowe) were added, plus gender-based Title VII and FEHA claims.
Paraphrase:  The court again DENIED Workday's bid to dismiss the ADEA claim, rejecting Workday's
             argument that job applicants cannot bring ADEA disparate-impact claims; it reaffirmed
             Rabin and held the argument survives Loper Bright because Rabin does not depend on
             Chevron deference and is persuasive under Skidmore. It GRANTED, with leave to amend,
             dismissal of the new FEHA claims (no pleaded California nexus) and of Hughes's ADA
             claim (no allegations tying Workday's tools to physical disability as opposed to
             mental-health/cognitive conditions). It DENIED the motion to strike allegations
             about recruitment, promotion, and retention. AARP and AARP Foundation were granted
             leave to file an amicus brief supporting plaintiffs.
Locators:    Whole order, 6 pp. ADEA ruling pp. 2-3; FEHA pp. 3-4; Hughes ADA pp. 5; strike p. 5;
             conclusion p. 6. New plaintiffs named p. 1 and n.1.
Quote:       "[J]ob applicants may bring disparate impact claims under the ADEA for the reasons
             articulated in Rabin v. PricewaterhouseCoopers LLP." (p. 2, quoting 740 F. Supp. 3d
             at 811 n.4)
```

```text
URL:         https://www.eeoc.gov/sites/default/files/2024-04/Mobley%20v%20Workday%20NDCal%20am-brf%2004-24%20sjw.pdf
Kind:        Primary. The EEOC's own amicus brief (Office of General Counsel). Owns the agency's
             litigating position; it is the government's argument, not reporting about it.
Establishes: EEOC amicus curiae brief supporting Mobley and opposing dismissal, Doc 60-1, filed
             04/09/24. Argues Workday is a covered entity under Title VII, the ADA, and the ADEA
             on three theories: employment agency, indirect employer, and agent of employers.
             The court later adopted only the agent theory and rejected the employment-agency
             theory. The EEOC expressly takes no position on whether the allegations are true.
Paraphrase:  On the agent theory, the EEOC argues an employer's agent can bear direct liability
             where the employer delegated a function "traditionally exercised by an employer,"
             and that Mobley alleges employers delegated control of significant aspects of hiring
             to Workday, whose screening system can itself refer or reject candidates. The brief
             quotes the EEOC's own 2023 technical assistance that a software vendor acts as an
             agent "if the employer has given [the vendor] significant authority to act on the
             employer's behalf." On the employment-agency theory it drew an analogy to
             tax-preparation software counting as a "tax preparer" when it does more than
             mechanical assistance (Rev. Rul. 85-187; Morse, Do Tax Compliance Robots Follow the
             Law?). Signed by General Counsel Karla Gilbride and OGC attorneys.
Locators:    Statement of interest p. 1; introduction/three theories pp. 1-2; agent argument
             pp. 12-14 (Section IV.C); conclusion p. 14. Tax-software analogy in the
             employment-agency section, ~p. 9.
Quote:       "Mobley has plausibly alleged that Workday is an agent of employers because
             employers have purportedly delegated authority to Workday to make at least some
             hiring decisions." (Introduction, p. 2)
             "The EEOC's own technical assistance states that a software vendor acts as an
             employer's agent 'if the employer has given [the vendor] significant authority to
             act on the employer's behalf,' which 'may include situations where an employer
             relies on the results of a selection procedure that the agent administers on its
             behalf.'" (Section IV.C, p. 13)
```

```text
URL:         https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial
             [This EEOC page now returns HTTP 404. The guidance was removed from EEOC.gov in
             January 2025 (see Contradictions). Recorded deliberately as the document's own
             address, because the removal is itself part of the story. A resolving archived copy
             is the Wayback capture of 2025-01-20 at
             https://web.archive.org/web/20250120231954/https://www.eeoc.gov/laws/guidance/select-issues-assessing-adverse-impact-software-algorithms-and-artificial
             (existence and 200 status confirmed via the Wayback availability API). I read the
             full text from an archived mirror; its four-fifths and vendor-agency language is
             also quoted verbatim inside the EEOC amicus brief above, which resolves.]
Kind:        Primary. The EEOC's own technical-assistance document. Owns the four-fifths rule as
             the agency applies it and the vendor-responsibility position.
Establishes: "Select Issues: Assessing Adverse Impact in Software, Algorithms, and Artificial
             Intelligence Used in Employment Selection Procedures Under Title VII" (short title
             "Title VII and AI: Assessing Adverse Impact"), OLC Control No. EEOC-NVTA-2023-2,
             issued 05-18-2023. Defines disparate/adverse impact, the selection-rate and
             four-fifths analysis, and when an employer is responsible for a vendor's tool.
Paraphrase:  Title VII bars neutral selection procedures that disproportionately exclude a
             protected group unless "job related for the position in question and consistent
             with business necessity"; this is "disparate impact" or "adverse impact." Selection
             rate is the share of a group selected. The four-fifths rule of thumb: one rate is
             "substantially" different from another if their ratio is less than 80%. Worked
             example: 48 of 80 white applicants (60%) and 12 of 40 Black applicants (30%)
             advance; the ratio 30/60 = 50% is below 80%, evidence of possible discrimination.
             The four-fifths rule is only a rule of thumb and may miss adverse impact where a
             procedure makes many selections. An employer may be responsible even when the tool
             is designed or administered by an outside vendor, including through agency: vendors
             "may include entities such as software vendors, if the employer has given them
             authority to act on the employer's behalf," which "may include situations where an
             employer relies on the results of a selection procedure that an agent administers
             on its behalf." The document ties disparate-impact method to Griggs.
Locators:    Definition of disparate impact and the three questions, "Title VII" section;
             vendor responsibility at Q3; selection rate at Q4; four-fifths rule and worked
             example at Q5; limits of the rule at Q6. Statutory/regulatory cites: 42 U.S.C.
             s 2000e-2(k); 29 C.F.R. Part 1607 (Uniform Guidelines); four-fifths at 29 C.F.R.
             ss 1607.4(D), 1607.16(B); Griggs cited at note 5.
Quote:       "Title VII also generally prohibits employers from using neutral tests or selection
             procedures that have the effect of disproportionately excluding persons based on
             race, color, religion, sex, or national origin, if the tests or selection
             procedures are not 'job related for the position in question and consistent with
             business necessity.'"
             "The rule states that one rate is substantially different than another if their
             ratio is less than four-fifths (or 80%)."
```

```text
URL:         https://www.law.cornell.edu/supremecourt/text/401/424
Kind:        Primary. The Supreme Court opinion; the doctrinal root of disparate impact.
             (Legal Information Institute hosts the U.S. Reports text; the opinion is the
             primary authority.)
Establishes: Griggs v. Duke Power Co., 401 U.S. 424 (1971), decided March 8, 1971, unanimous
             (Burger, C.J.; Brennan, J. took no part). Held that Title VII bars facially neutral
             employment practices (there, a high-school-diploma requirement and a general
             intelligence test) that exclude a protected group and are not shown to be related
             to job performance, regardless of the employer's intent. Source for what
             "disparate impact" means and the business-necessity defense the Workday claims turn
             on.
Paraphrase:  The Act reaches practices fair in form but discriminatory in operation; the
             touchstone is business necessity; a practice that excludes and is not related to
             job performance is prohibited even absent discriminatory intent. Congress aimed the
             statute at the consequences of practices, not just motivation, and placed on the
             employer the burden to show a job-related justification.
Locators:    Opinion of Burger, C.J., 401 U.S. at 429-433.
Quote:       "The Act proscribes not only overt discrimination but also practices that are fair
             in form, but discriminatory in operation. The touchstone is business necessity. If
             an employment practice which operates to exclude Negroes cannot be shown to be
             related to job performance, the practice is prohibited." (401 U.S. at 431)
             "good intent or absence of discriminatory intent does not redeem employment
             procedures or testing mechanisms that operate as 'built-in headwinds' for minority
             groups and are unrelated to measuring job capability." (401 U.S. at 432)
             "Congress directed the thrust of the Act to the consequences of employment
             practices, not simply the motivation." (401 U.S. at 432)
```

```text
URL:         https://www.hrdive.com/news/workday-ai-bias-lawsuit-class-collective-action/748518/
Kind:        Secondary. Trade-press reporting (HR Dive, Ginger Christ, Editor, published
             05/19/25, updated 05/20/25). Reports on the ruling and carries Workday's public
             statement.
Establishes: Workday's public response to the certification ruling, and its public framing that
             it does not make hiring decisions. Confirms the court found Workday's website and
             discovery responses contradict its claim that it does not recommend applicants.
Paraphrase:  A Workday spokesperson said the ruling is preliminary and early and that the claims
             will be dismissed once facts are presented. The company's public position is that it
             does not offer employment recommendations. Useful for the timeline and for
             representing Workday's public voice; the load-bearing facts are drawn from the
             orders, not this article.
Locators:    Body; spokesperson quote and Workday position paragraph.
Quote:       "This is a preliminary ruling at an early stage of this case, and before the facts
             have been established. We're confident that once those facts are presented to the
             court, the plaintiff's claims will be dismissed." (Workday spokesperson, per HR Dive)
```

```text
URL:         https://www.shrm.org/about/press-room/fresh-shrm-research-explores-use-automation-ai-hr
Kind:        Primary for its own survey data; used as secondary context for the closing turn.
             SHRM (Society for Human Resource Management) authored and owns the survey figures.
Establishes: Prevalence context for automated hiring. From a SHRM recruitment survey fielded
             02/01-02/17/2022 to 1,688 HR professionals, presented at the SHRM Talent Conference
             (April 2022).
Paraphrase:  Nearly 1 in 4 organizations report using automation or AI to support HR activities
             including recruitment and hiring; use rises with size, from 16% of employers with
             fewer than 100 workers to 42% of those with 5,000 or more; and 64% of HR
             professionals say their organization's automation or AI tools automatically filter
             out unqualified applicants. Weaker than the case-owned figure below; the writer
             should prefer Workday's 1.1 billion for scale and use SHRM only for adoption
             breadth, with the 2022 date stated.
Locators:    Press release body (figures as summarized above; I read this via the page's own
             text through a fetch summary, not a downloaded copy — verify the 64% denominator
             against the release before printing).
Quote:       (none load-bearing beyond the figures in Numbers)
```

---

## Contradictions

**The rulings decide procedure, not the merits — this is the spine of the proven/alleged line.**
Both marquee rulings accept Mobley's allegations as true at their stage. The July 2024 order is a
Rule 12(b)(6) decision that "accept[s] factual allegations in the complaint as true" (Doc 80
p. 4). The May 2025 certification is step one of a two-step process, "loosely akin to a
plausibility standard," explicitly subject to later decertification (Doc 128 pp. 5-8). No court
has weighed evidence or found Workday's tools discriminatory. The article's claim that the
discrimination is unproven is not a hedge; it is what the court itself says.

**Workday's strongest rebuttals, in its own words (from its filings, quoted in the orders).**
Workday's position is that it "does not recommend, screen out, or otherwise assess or predict
applicants' likelihood of success in a role" (Dkt. 107, quoted Doc 128 p. 9), that customers can
"enable, disable, use, or ignore" its AI features (Doc 128 p. 4), and that any disparate impact
may be employer-driven rather than caused by Workday's algorithms (Doc 128 pp. 13-14). The court
did not reject these as false; it held they are merits questions for stage two and that, on the
current record, Workday's own website and discovery responses cut against its "we don't
recommend" claim (Doc 128 pp. 9-11). Publicly, Workday calls the case meritless and expects
dismissal once facts are presented (HR Dive). The article should present these as live defenses,
not as positions already defeated.

**The "agent" theory is contested law and untested on appeal.** The July 2024 order acknowledges
the Ninth Circuit "did not address the question of liability of third-party agents of employers"
and distinguishes, rather than follows, Miller v. Maxwell's International (991 F.2d 583 (9th Cir.
1993)), which held individual supervisors are not liable as agents (Doc 80 pp. 7-8). Workday read
Miller to bar agency liability outright; the court disagreed and also treated some of Workday's
agency arguments as waived for being raised first at oral argument (Doc 80 p. 7). This is a
trial-court holding on a novel question; if it reaches the Ninth Circuit or another circuit
splits, it could be narrowed or reversed. The article must not imply appellate settlement.

**Whether ADEA disparate-impact claims even reach job applicants is itself disputed.** Judge Lin
twice held they do (Doc 80 p. 16 n.4; Doc 267 pp. 2-3), relying on Rabin (N.D. Cal. 2017) against
contrary en banc authority elsewhere — Kleber v. CareFusion (7th Cir.) and Villarreal v. R.J.
Reynolds (11th Cir.). The entire age-collective rests on a contested reading of the ADEA. This is
a real narrowing risk worth naming.

**Federal posture shifted against this enforcement theory after the rulings.** I confirmed the
EEOC's 2023 AI technical-assistance page now returns HTTP 404; it was removed from EEOC.gov in
January 2025. Secondary reporting (K&L Gates; National Law Review) ties this to the January 23,
2025 executive order "Removing Barriers to American Leadership in Artificial Intelligence" and
reports a later 2025 executive order directing agencies to de-prioritize disparate-impact
enforcement. Report factually: the guidance's removal does not change Title VII, and the EEOC's
amicus and the court's rulings remain in force in this case. Treat the executive-order specifics
as secondary until the primary order text is cited; the verified facts are the 404 and the
archived capture. This is context, not a change to the holding, and it cuts against, not for, the
plaintiff's tailwind.

**A distinction the record insists on: vendor versus third-party model.** Workday stated at oral
argument, without evidence, that its Assessment Connector "acts as a bridge" to "third-party" AI
features (Doc 128 p. 4), and pymetrics is a separate product its tools integrate. The court's
agent theory turns on the function delegated to Workday, not on who authored a given model. The
article should not blur Workday's own algorithms with third-party models it routes to; the
allocation of cause is unresolved.

No contradiction found in the core figures themselves (the 100-plus rejections, the collective
definition, the 1.1 billion): each traces to a single owning source and is not disputed across
sources, only characterized differently.

---

## Numbers

```text
Figure: 100+ job applications, all rejected, since 2017 (Mobley personally)
Owner:  Mobley's First Amended Complaint, as recited in Doc 80 (pp. 2-3, 14) and Doc 128 (p. 3)
Scope:  One applicant's own applications through Workday-using employers, 2017 onward; a
        "zero percent success rate" at initial screening. An allegation, not an audited count.
```

```text
Figure: 1.1 billion applications "rejected using Workday" during the period at issue
Owner:  Workday's own filing (Dkt. 107 at 24-25), quoted in Doc 128 p. 18
Scope:  Sept 24, 2020 to the date of briefing; Workday's figure, offered to argue the collective
        is unmanageably large. Best single anchor for the closing "how widespread" turn: it is
        primary, case-owned, and Workday's own number.
```

```text
Figure: "hundreds of millions" of potential collective members
Owner:  Workday's characterization (Dkt. 107), quoted/addressed in Doc 128 pp. 2, 18-19
Scope:  Workday's own estimate of the ceiling before the collective's qualifiers narrow it; the
        court declined to treat size as a bar to notice. Use as Workday's estimate, not a count.
```

```text
Figure: Collective = individuals aged 40+ who, from September 24, 2020 to present, applied via
        Workday's platform and were "denied employment recommendations"
Owner:  Doc 128 pp. 2-3, 17 (definition refined at p. 17: application scored/sorted/ranked/
        screened by Workday's AI; result not a hire recommendation; result conveyed to employer
        or an automatic rejection)
Scope:  Nationwide ADEA collective, conditionally certified; scope later held to include
        HiredScore AI features (Doc 158).
```

```text
Figure: Four-fifths (80%) rule; worked example 60% vs 30% selection rates, ratio 50%
Owner:  EEOC 2023 technical assistance, Q5; regulatory basis 29 C.F.R. ss 1607.4(D), 1607.16(B)
Scope:  Rule of thumb for a preliminary inference of adverse impact; the EEOC warns it can miss
        impact in large-volume selection. Good for teaching disparate impact concretely.
```

```text
Figure: Statutory coverage thresholds: 15 employees (Title VII, ADA), 20 (ADEA); "employer"
        includes "any agent"
Owner:  Doc 80 pp. 5-6, citing 42 U.S.C. ss 2000e(b), 12111(5)(A); 29 U.S.C. s 630(b)
Scope:  Defines who is a covered "employer"; the hook for agent liability.
```

```text
Figure: Adoption of automation/AI in HR: ~1 in 4 organizations overall; 16% (<100 workers) vs
        42% (5,000+ workers); 64% say tools auto-filter unqualified applicants
Owner:  SHRM survey, fielded Feb 2022 (n=1,688 HR professionals)
Scope:  U.S. employers, 2022; adoption breadth, not application volume. Secondary context; state
        the 2022 date and verify the 64% denominator before printing.
```

```text
Figure: Five plaintiffs total on the age claim (Mobley + four opt-in); three named plaintiffs
        added in the Second Amended Complaint (Hughes, Johnson-Rocha, Rowe)
Owner:  Doc 128 (four opt-in declarants, pp. 3-4); Doc 267 (three new named plaintiffs, p. 1 n.1)
Scope:  Named/opt-in plaintiffs, distinct from the far larger conditional collective.
```

---

## Source assets

```text
Asset: EEOC technical assistance, Q5 four-fifths worked example (80 white/40 Black applicants;
       60% vs 30%; ratio 50% < 80%). It is text/numbers in the source, not an image.
Shows: How a neutral screen produces a legally cognizable disparity, with real arithmetic the
       reader can follow. The one place a small table would teach disparate impact faster than
       prose.
Crop:  If rendered as a table, keep both selection rates and the 80% threshold; do not present
       the rule as a hard legal line — the source calls it a rule of thumb.
```

```text
Asset: Workday website language quoted in the orders ("reduce time to hire by automatically
       dispositioning or moving candidates forward"; "AI- and ML-driven job recommendations").
Shows: The vendor's own marketing describing the tools as making recommendations — the material
       the court said contradicts Workday's "we don't recommend" defense.
Crop:  Quote as text with the court's citation (Doc 80 p. 1; Doc 128 pp. 4, 10). No screenshot
       needed and none appears in the record.
```

```text
Asset: The court orders themselves (Docs 80, 128, 158, 267) and the EEOC amicus (Doc 60-1).
Shows: Nothing visual beyond standard filed-document formatting.
Crop:  None found. These are text opinions; no charts, figures, or images to carry an argument.
```

A timeline (Feb 2023 filing -> July 2024 agent ruling -> May 2025 conditional certification ->
July 2025 HiredScore scope -> March 2026 SAC ruling) is available from the dockets, but that is
furniture the writer would build, not a visual that lives in a source.

---

## Discarded

```text
URL: https://www.leagle.com/decision/740250197fsupp3d79642  — Reader-restricted (HTTP 403);
     superseded by the filed PDF of the same July 2024 order (Doc 80), which I read in full.
URL: https://www.cnn.com/2025/05/22/tech/workday-ai-hiring-discrimination-lawsuit  — Returned
     HTTP 451 (blocked); its Workday-statement content is covered by HR Dive, which resolved.
URL: https://supreme.justia.com/cases/federal/us/401/424/  — HTTP 403; replaced by the Cornell
     LII copy of the same Griggs opinion, read in full.
URL: https://www.courtlistener.com/docket/66831340/mobley-v-workday-inc/  — HTTP 403 to fetch and
     API rate-limited; used only to locate document numbers, which I confirmed against the
     govinfo and RECAP PDFs I actually read. Not cited.
URL: Aggregator ATS statistics ("99% of Fortune 500 use ATS," selectsoftwarereviews / jobscan /
     tracker-rms)  — Vendor-marketing blogs with no traceable methodology; rejected in favor of
     the SHRM survey and, for scale, Workday's own 1.1 billion filing figure.
URL: Law-firm client alerts (Seyfarth, Holland & Knight, Duane Morris, Davis Wright Tremaine)  —
     Read for orientation and to find primary documents; accurate but secondary, and everything
     they assert is available in the orders I read directly, so none is cited.
```
