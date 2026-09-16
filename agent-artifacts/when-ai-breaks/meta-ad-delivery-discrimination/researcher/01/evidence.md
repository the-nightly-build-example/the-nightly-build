purpose: evidence record for when-ai-breaks/meta-ad-delivery-discrimination, researcher invocation 01
brief: ../brief.md

The record supports every step the commission lays out: the mechanism (a peer-reviewed
controlled experiment isolating delivery from targeting, with exact skew figures by
job/property type, gender, and race), the harm and response chain (a federal housing charge,
an earlier civil-rights settlement that changed targeting, and a first-of-its-kind DOJ
settlement that required a new delivery system), and the operator's contested position,
attributed and in its strongest form. It is thin in one place the commission does not ask
about but the piece will need to handle carefully: the DOJ's own complaint and consent
judgment text could not be opened directly (justice.gov returned 401 Unauthorized on every
URL and subdomain tried, including via the settlement PDF, the OPA press release, the
archived version, and the CRT case page); the settlement's terms are reconstructed here from
a litigation-tracking secondary source, independent legal-industry secondary reporting that
agrees across outlets, and Meta's own primary account of the settlement (which quotes and
links the DOJ compliance-metrics filing directly). A second thing worth flagging to the
editor: an independent, peer-reviewed 2025 audit found that the delivery system Meta built in
response does reduce the measured skew for housing ads specifically, but does not extend that
result to employment or credit ads despite voluntary rollout there, and achieves the housing
reduction partly by showing the ad to fewer unique people per dollar. That complicates a tidy
resolution to the incident; it does not undermine the core, commissioned claim that delivery
optimization itself produced the disparity, which four independent, primary-sourced findings
(the study, the HUD charge, the earlier settlement, and the DOJ settlement) all converge on.

### Sources

```text
URL:         https://arxiv.org/abs/1904.02095 (paper: "Discrimination through optimization:
             How Facebook's ad delivery can lead to skewed outcomes"; published version DOI
             10.1145/3359301, Proceedings of the ACM on Human-Computer Interaction, Vol. 3,
             No. CSCW, November 2019; this is version v5, Sep 12 2019, identical to the
             accepted CSCW text)
Kind:        Primary. Authored by the researchers who designed and ran the experiments
             (Muhammad Ali, Piotr Sapiezynski, Northeastern University; Miranda Bogen, Aaron
             Rieke, Upturn; Aleksandra Korolova, USC; Alan Mislove, Northeastern University).
             It owns every skew figure and every methodological claim about the experiment.
Establishes: That Facebook's ad-delivery system, not advertiser targeting, produces
             demographically skewed delivery of housing and employment ads even when
             targeting and budget are held identical across ad variants; that the skew begins
             before any user has clicked or interacted (shown via near-invisible test images);
             that it tracks the ad's content/image, not just market/budget effects.
Paraphrase:  The authors ran "dozens of ad campaigns, hundreds of ads with millions of
             impressions, spending over $8,500" on Facebook between (per campaign design)
             2018-2019, holding an ad's target audience and daily budget fixed while varying
             only the ad creative (headline, text, image) or, in one design, the budget alone.
             For race, because Facebook's ad-reporting tools do not break delivery down by
             race, the authors built a proxy: North Carolina voter records (7,560,885
             individuals; 93% self-report as Black or White) were partitioned by Designated
             Market Area (DMA) into race-matched custom audiences (Table 1: audiences A, B,
             disjoint, 400,000 White/0 Black and 0 White/400,000 Black respectively by DMA
             set; audience C, a larger combined 900,002 White/892,097 Black), uploaded to
             Facebook as Custom Audiences, and delivery was inferred by which DMA an
             impression landed in. For employment ads, 11 generic job types (AI developer,
             doctor, janitor, lawyer, lumberjack, nurse, preschool teacher, restaurant
             cashier, secretary, supermarket clerk, taxi driver) were each run with 5 image
             variants (white man, white woman, Black man, Black woman, no person), 55 ads
             total, all targeting the same audience (custom audience C), same budget, same
             24-hour run, Objective=Traffic. For housing, ads varied by tenure (rent/buy) and
             implied price (cheap/luxury), run 12 hours each on audiences A and B in rotation
             to cancel geography, against a non-housing baseline linking to google.com.
             Statistical significance used 99% Agresti-Coull confidence intervals and a
             difference-of-proportions Z-test, confirmed against Bonferroni correction for the
             55-way job comparison (Figure 10, appendix).
Locators:    Abstract; Introduction ("Contributions"); §3 Methodology (3.1-3.4); §4.1 (budget
             effects, Fig. 2); §4.2 (creative effects, Fig. 3-5); §4.3 (transparent-image test,
             Fig. 6, Table 2); §4.4 (employment ads, Fig. 7-8, and housing ads, Fig. 9); §5
             Concluding Discussion; Appendix (Fig. 10, multiple-hypothesis correction).
Quote:       "we run dozens of ad campaigns, hundreds of ads with millions of impressions,
             spending over $8,500 as part of our study" (Introduction). "In the most extreme
             cases, our ads for jobs in the lumber industry reach an audience that is 72% white
             and 90% male, our ads for cashier positions in supermarkets reach an 85% female
             audience, and our ads for positions in taxi companies reach a 75% Black audience,
             even though the targeted audience specified by us as an advertiser is identical
             for all three" (Introduction). "In fact, in response to the HUD lawsuit mentioned
             above, Facebook claimed that the agency had 'no evidence' of their ad delivery
             systems' role in creating discrimination" (Introduction, citing a ProPublica
             article the paper footnotes as its source for that claim, not a Facebook document
             the researchers themselves read).

URL:         https://www.hud.gov/sites/dfiles/Main/documents/HUD_v_Facebook.pdf
             (also mirrored at https://archives.hud.gov/news/2019/HUD_v_Facebook.pdf)
Kind:        Primary. This is HUD's own Charge of Discrimination, issued by HUD's Office of
             General Counsel and filed with HUD's Office of Administrative Law Judges. It
             owns HUD's findings and legal theory; it does not own the underlying facts about
             how Facebook's systems work, which it draws from Facebook's own public
             statements about its ad platform (quoted and footnoted in the charge itself).
Establishes: The formal federal housing charge: its docket number, filing date, filer,
             respondent, the specific two-phase (targeting/delivery) mechanism HUD alleges,
             and the relief HUD sought. Does not establish that a court or judge found
             liability -- a Charge of Discrimination is HUD's own reasonable-cause
             determination, not an adjudicated finding.
Paraphrase:  Case caption: The Secretary, HUD, on behalf of Complainant Assistant Secretary
             for Fair Housing and Equal Opportunity, Charging Party, v. Facebook, Inc.,
             Respondent. HUD ALJ No. [blank in filed copy]; FHEO No. 01-18-0323-8. The
             underlying complaint was filed by the Assistant Secretary for Fair Housing and
             Equal Opportunity on August 13, 2018. Following an investigation, HUD's Director
             of the Office of Systemic Investigations issued a Determination of Reasonable
             Cause, and this Charge of Discrimination was filed on March 28, 2019, alleging
             Facebook violated 42 U.S.C. §3604(a), (b), (c) and (f) (subsections 804(a),
             804(b), 804(c), 804(f) of the Fair Housing Act) by discriminating "because of
             race, color, religion, sex, familial status, national origin and disability." The
             charge describes Facebook's ad system as a two-phase process: an "ad targeting
             phase," where Facebook gives the advertiser tools to define an "eligible
             audience," and an "ad delivery phase," where "Respondent selects the ad's
             'actual audience'... Respondent alone, not the advertiser, determines which
             users will constitute the 'actual audience' for each ad" (para. 13, 17). The
             charge alleges this delivery-phase selection "considers sex and close proxies
             for the other protected classes" including "which pages a user visits, which
             apps a user has, where a user goes during the day, and the purchases a user makes
             on and offline" (para. 17, 18, 20), and that Facebook's use of machine learning
             to group users by shared attributes "inevitably recreates groupings defined by
             their protected class" (para. 20). It states Facebook is "the second largest
             online advertiser in the United States" responsible for "approximately twenty
             percent of all online advertising nationwide," with (as of the charge) roughly
             221 million active US Facebook users and 114 million active US Instagram users
             (para. 5-6). Relief sought: a declaration of violation, an injunction, mandatory
             fair-housing training for Facebook's agents/employees, damages to compensate
             aggrieved persons, "the maximum civil penalty against Respondent for each
             violation," and additional relief as appropriate (Conclusion, items 1-6). Signed
             by Jeanine Worden, Associate General Counsel for Fair Housing; Kathleen M.
             Pennington, Assistant General Counsel for Fair Housing Enforcement; and Ayelet R.
             Weiss, Trial Attorney, HUD Office of General Counsel.
Locators:    p.1 Jurisdiction; pp.2-6 Summary of Findings (paras. 4-20); p.6 Legal Allegations
             (paras. 21-26); pp.6-7 Conclusion; p.7 signature block, dated March 28, 2019.
Quote:       "Respondent's ad delivery system prevents advertisers who want to reach a broad
             audience of users from doing so. Even if an advertiser tries to target an
             audience that broadly spans protected class groups, Respondent's ad delivery
             system will not show the ad to a diverse audience if the system considers users
             with particular characteristics most likely to engage with the ad." (para. 19)

Note on titles/attribution: the charge itself was filed by career HUD attorneys on behalf of
the Assistant Secretary for Fair Housing and Equal Opportunity (the office, not named by
individual in the charge document). Contemporaneous secondary reporting (e.g. NPR, Bloomberg,
March 28 2019) attributes a public quote -- "Facebook is discriminating against people based
upon who they are and where they live" -- to then-HUD Secretary Ben Carson, the Department's
Senate-confirmed cabinet head, who is a distinct official from the Assistant Secretary for
FHEO who is the actual Charging Party. Keep these titles separate if either is named.

URL:         https://www.aclu.org/documents/summary-settlements-between-civil-rights-advocates-and-facebook
             (PDF: https://www.aclu.org/wp-content/uploads/document/3.18.2019_Joint_Statement_FINAL.pdf)
Kind:        Primary. A joint statement co-authored and released by Facebook together with
             the plaintiffs' counsel (ACLU, Outten & Golden LLP, Emery Celli Brinckerhoff &
             Abady LLP) and organizational plaintiffs (NFHA, CWA). It is the parties'
             description of their own settlement, not a court order -- there was no single
             consolidated court judgment; five separate legal actions were resolved.
Establishes: The exact terms Facebook agreed to for its ad platform, and which five legal
             actions (case names, courts, filing dates, plaintiffs, counsel) were resolved.
Paraphrase:  Released March 19, 2019 ("Today, civil rights organizations, labor groups, and
             Facebook announced historic settlements..."). Facebook agreed to: build a
             separate advertising portal for housing, employment, and credit ("HEC") ads on
             Facebook, Instagram, and Messenger with restricted targeting; remove gender, age,
             and "multicultural affinity" targeting for HEC ads; require a minimum 15-mile
             geographic radius for HEC ads and disallow zip-code targeting; remove targeting
             options describing or appearing to relate to protected characteristics from the
             HEC portal; stop using Lookalike Audiences' full feature set (gender, age,
             religious views, zip code, Facebook Group membership) for HEC ads; auto-detect
             and reroute HEC ads created outside the restricted portal; build a searchable
             public archive of all housing ads regardless of whether a given user was in the
             advertiser's intended audience; require advertiser self-certification of
             anti-discrimination compliance; provide educational materials; meet regularly
             with plaintiffs' counsel to report on implementation; let plaintiffs test the
             platform to confirm the reforms work; develop fair-housing/fair-lending training
             with NFHA; and "engage academics, researchers, experts, and civil rights and
             liberties advocates... to study the potential for unintended biases in the
             algorithmic modeling used by social media platforms." Five actions were resolved:
             Mobley et al. v. Facebook (N.D. Cal., filed Nov. 2016); National Fair Housing
             Alliance et al. v. Facebook (S.D.N.Y., filed March 2018, plaintiffs NFHA, Fair
             Housing Justice Center, Housing Opportunities Project for Excellence, Fair
             Housing Council of Greater San Antonio); Communications Workers of America et
             al. v. Facebook (EEOC charge, filed Jan. 2018, age discrimination in employment
             ads); Spees et al. v. Facebook (EEOC charge, filed Sept. 2018, sex discrimination
             in employment ads, CWA and ACLU); Riddick v. Facebook (N.D. Cal., filed Nov.
             2016).
Locators:    p.1 header and overview bullets; p.1-2 "Legal Actions Settled" case list; p.3
             "Plaintiffs challenged" summary of the three targeting mechanisms at issue
             (sex/age exclusion, narrow geography, Lookalike Audiences).
Quote:       "Facebook will engage academics, researchers, experts, and civil rights and
             liberties advocates, including the Plaintiffs, to study the potential for
             unintended biases in the algorithmic modeling used by social media platforms."

URL:         https://nationalfairhousing.org/national-fair-housing-alliance-settles-lawsuit-with-facebook-transforms-facebooks-ad-platform-impacting-millions-of-users/
Kind:        Primary. NFHA's own announcement of its own settlement (NFHA is the lead
             plaintiff in NFHA et al. v. Facebook).
Establishes: Confirms the March 19, 2019 date and the case name/court (NFHA v. Facebook,
             filed March 2018, S.D.N.Y.) independently of the joint statement; confirms the
             same specific platform changes from the plaintiff's own telling.
Paraphrase:  NFHA describes the same targeting restrictions as the joint statement (protected
             classes removed from HEC targeting, 15-mile minimum radius, Lookalike Audience
             restrictions) as the direct product of its lawsuit. Does not state a dollar
             figure for the settlement.
Locators:    Full text (short press release), dateline March 19, 2019.

URL:         https://www.aclu.org/press-releases/facebook-agrees-sweeping-reforms-curb-discriminatory-ad-targeting-practices
Kind:        Primary. The ACLU's own announcement of the settlement it was a party to
             (representing Spees/CWA plaintiffs and consumers).
Establishes: A monetary figure for at least part of the settlement, from the party that paid
             or received it.
Paraphrase:  States roughly $3 million in payments across the Spees/CWA, CWA/Bradley, and
             Mobley matters combined, covering legal fees/costs and compensation for named
             workers and consumers, plus non-monetary platform commitments matching the joint
             statement. Note: a separate figure of "$5 million" across ACLU/NFHA/CWA
             collectively also appears in contemporaneous secondary reporting (Axios,
             SiliconANGLE, March 19 2019); the two figures are not necessarily inconsistent
             (the larger figure may aggregate money not itemized in the ACLU's own release,
             e.g. any NFHA-specific relief), but the record could not fully reconcile them
             from primary sources within this invocation. Treat the exact total settlement
             dollar figure as unconfirmed to two decimal places; the commission does not ask
             the piece to state one, so this is a minor exposure, not a blocking gap.
Locators:    Full press release text, dateline March 19, 2019.

URL:         https://clearinghouse.net/case/43395/ (Civil Rights Litigation Clearinghouse,
             University of Michigan Law School, case page for United States v. Meta
             Platforms, Inc., 1:22-cv-05187, S.D.N.Y.)
Kind:        Secondary (a litigation-tracking database summarizing and citing the court
             filings; it did not author the complaint or the settlement). Recorded here
             because the primary filings themselves, hosted at justice.gov, returned HTTP 401
             Unauthorized on every attempt (direct fetch of the OPA press release, the USAO-
             SDNY press release, the CRT case page, the complaint PDF, the proposed-settlement
             PDF, and the final-judgment PDF; also attempted via the Wayback Machine, which
             this toolset cannot fetch at all). Corroborated below by two further independent
             secondary sources and, on the settlement's existence and the VRS/reviewer
             requirement specifically, by Meta's own primary whitepaper (next entry), which
             quotes and links the DOJ compliance-metrics filing directly.
Establishes: The DOJ's suit was filed June 21, 2022, in the U.S. District Court for the
             Southern District of New York; a settlement agreement was reached the same day
             and approved by the court on June 27, 2022; Meta was required to stop using the
             "Special Ad Audience" tool (the successor to "Lookalike Audience") for housing
             ads by December 31, 2022 (later reported elsewhere as extended to January 9,
             2023, coinciding with the VRS compliance-metrics announcement); Meta paid a
             $115,054 civil penalty, described as the maximum available under the Fair Housing
             Act at the time; Meta is subject to DOJ oversight and compliance review through
             June 27, 2026.
Paraphrase:  As above.
Locators:    Case summary and settlement-terms sections of the case page.

URL:         https://about.fb.com/wp-content/uploads/2023/01/Toward_fairness_in_personalized_ads.pdf
             ("Toward fairness in personalized ads," Meta, January 2023; authors listed:
             Miranda Bogen, Pushkar Tripathi, Aditya Srinivas Timmaraju, Mehdi Mashayekhi, Qi
             Zeng, Rabyd Roudani, Sean Gahagan, Andrew Howard, Isabella Leone)
Kind:        Primary. Meta's own technical and policy account of the delivery system it built,
             published under its own name.
Establishes: What Meta says it built (the Variance Reduction System, "VRS"), how it says VRS
             works mechanically, what data it says VRS does and does not use, and what
             compliance/verification process it describes.
Paraphrase:  VRS is described as "an offline reinforcement learning framework with the
             explicit goal of minimizing an ad's impression variance across... demographic
             subgroups" for housing, employment, and credit ("HEC") ads. It compares an
             "eligible ratio" (the demographic mix, by age, gender, and BISG-estimated race/
             ethnicity, of the audience the advertiser targeted, estimated from recent
             impressions) against a periodically-measured "delivery ratio" (the actual mix of
             who is being shown the ad), and uses a "controller" that adjusts a "pacing
             multiplier" in the ad auction (boosting or not boosting a given ad's chance of
             winning) to push delivery back toward the eligible ratio. It explicitly does not
             give the controller individual-level age, gender, or race/ethnicity -- only
             aggregate, differentially-private measurements and abstracted "user summary"
             features. Race/ethnicity is estimated via Meta's privacy-adapted implementation
             of Bayesian Improved Surname Geocoding (BISG), using US Census surname/geography
             data, itself further protected with differential privacy noise. The whitepaper
             states the VRS emerged from the June 2022 DOJ settlement, states Meta "designed
             a system we believe can help address the most acute concerns," and states a
             third-party reviewer will "review each Compliance Report and verify compliance
             with the VRS Compliance Metrics," footnoting the DOJ's own settlement-adjacent
             filing (justice.gov/opa/press-release/file/1514031/download) as the source of
             that requirement -- corroborating, from Meta's own account, that the DOJ
             settlement did create a reviewer/compliance-metrics regime, independent of
             whether this record could open the DOJ's text directly. It states race/gender/
             age targeting removals from the 2019 civil-rights settlement remain in place and
             were extended globally (Canada, EU). It separately describes a distinct, earlier
             mitigation, "Special Ad Audiences," as an alternative to Lookalike Audiences that
             Meta introduced and then discontinued for HEC ads "informed by concerns that
             these audiences might still be misused by advertisers attempting to circumvent
             our protections against discrimination" -- Meta's own account, in its own words,
             of why that intermediate tool did not hold up.
Locators:    Executive Summary (p.3); Introduction (p.4-5); "Ad targeting" section (p.8-10,
             Special Ad Audiences discontinuation); "Ad delivery outcomes: Reducing outcome
             variance" (p.12-23, full VRS mechanism, formulas, six-step process, privacy
             section, measurement/shuffle-distance section); "Technical challenges and open
             policy questions" (p.24-27, VRS's own stated limits: low-volume ads get fewer
             "episodes" to correct variance, snapshot measurements rely on estimates that can
             be wrong, multi-objective tradeoffs mean not all demographic dimensions can be
             optimized simultaneously without tension); footnote 12 citing the DOJ filing
             (p.34).
Quote:       "We note that while these privacy protections may slightly degrade the maximum
             performance of the system in reducing variance, we aimed to strike a reasonable
             balance between advancing fairness in an important context and honoring people's
             privacy." "Despite these constraints, we are confident that the Variance
             Reduction System will still lead to a substantial, albeit imperfect, reduction in
             variance." (p.21-23)

URL:         https://about.fb.com/news/2023/01/an-update-on-our-ads-fairness-efforts/
Kind:        Primary. Meta's own newsroom announcement.
Establishes: The public rollout announcement date and framing for VRS.
Paraphrase:  Dated January 9, 2023. Announces that Meta and DOJ reached agreement on VRS
             compliance metrics/targets, names the independent third-party reviewer role, and
             frames VRS as addressing housing ads first, with employment and credit ads to
             follow. Provides no numeric variance-reduction results itself -- it points to the
             whitepaper above for technical detail, which likewise reports no outcome
             percentages, only the mechanism and formulas.
Locators:    Full post text.

URL:         https://www.propublica.org/article/hud-sues-facebook-housing-discrimination-advertising-algorithms
Kind:        Secondary (ProPublica reporting that quotes Facebook's own contemporaneous
             statements; the statements themselves are primary utterances by Facebook, relayed
             here by a news outlet rather than a Facebook-authored document this record
             opened directly).
Establishes: Facebook's own contemporaneous public response to the HUD charge -- the
             strongest available primary-adjacent statement of the operator's contested
             position for this specific incident.
Paraphrase:  Dated March 28, 2019 (the day the charge was filed). A Facebook spokesperson is
             quoted disputing HUD's finding: "HUD had no evidence [supporting a] finding that
             our AI systems discriminate against people," and, separately, "We're surprised by
             HUD's decision, as we've been working with them to address their concerns and
             have taken significant steps to prevent" ad discrimination. The article also
             quotes an earlier (March 2018) Facebook statement responding to the NFHA lawsuit:
             "There is absolutely no place for discrimination on Facebook. We believe this
             lawsuit is without merit, and we will defend ourselves vigorously" (spokesman Joe
             Osborne). ProPublica separately reports Facebook declined to give HUD delivery
             data, citing privacy.
Locators:    Body of the article, statements attributed to a Facebook spokesperson and to Joe
             Osborne.
Quote:       "HUD had no evidence [supporting a] finding that our AI systems discriminate
             against people."

URL:         https://doi.org/10.1145/3715275.3732170 (Imana, Shen, Heidemann, Korolova,
             "External Evaluation of Discrimination Mitigation Efforts in Meta's Ad Delivery,"
             ACM Conference on Fairness, Accountability, and Transparency (FAccT '25), Athens,
             Greece, June 23-26, 2025; preprint mirror: arxiv.org/abs/2506.16560; PDF opened:
             ant.isi.edu/~johnh/PAPERS/Imana24a.pdf, an author's self-hosted copy of the same
             accepted text)
Kind:        Primary. A peer-reviewed, independently conducted audit by researchers unaffiliated
             with Meta or the DOJ, one of whom (Korolova) co-authored the original 2019 study
             above and one of whom (Heidemann) is cited in Meta's own whitepaper reference
             list -- giving continuity of method across both studies.
Establishes: Whether the delivery system Meta built in response to the 2022 settlement
             actually reduces the skew the 2019 study first measured, using a real-world,
             black-box replication that runs the same ad with and without VRS enabled.
Paraphrase:  Method: paired campaigns of the same ad creative, run simultaneously, identical
             in targeting/budget/creative except one copy is declared a housing/credit/
             employment special ad category (enabling VRS) and the other is not. 36 paired
             experiments across six ad creatives (a hair-product ad and a golfing ad
             constructed to be stereotypically skewed by race/gender; two education ads
             replicating known bias from prior work; an insurance and a financial ad), each
             run for a 24-hour, $20/day budget, replicated on three independent North Carolina
             voter-file audience partitions (same race-inference method as the 2019 study).
             Findings: for ads declared as housing, VRS does reduce measured variance against
             Meta's own compliance metric (variance below 10% in 15 of 18 race-comparison
             cases and 15 of 18 gender-comparison cases, versus fewer than 5 of 18 cases
             meeting that bar without VRS). For ads voluntarily declared as credit or
             employment (a category Meta began covering with VRS starting in January 2025),
             the same reduction was not observed: variance stayed above the 10% threshold in
             most cases, "comparable to the outcome without VRS." Across all 36 paired
             experiments, enabling VRS reduced the average number of unique people (reach)
             an ad reached by 9.82% for a fixed budget, and increased advertisers' cost per
             1,000 unique people reached in most paired comparisons -- meaning the measured
             fairness gain for housing ads is achieved partly by delivering the ad to fewer
             people overall, not only by redistributing the same number of impressions more
             evenly. The paper also identifies structural weaknesses in the settlement's own
             compliance design, independent of Meta's implementation: the agreed compliance
             metric is defined over ad impressions, not unique individuals reached, so an ad
             shown 100 times to one person can register as "balanced" while never reaching
             99 other eligible people; and "coverage" is defined as the percentage of
             qualifying ads that meet the variance threshold, counted per-ad rather than
             weighted by audience size, which the authors show (using a public sample of
             32,867 political ads' spend/impression distribution as a stand-in, since Meta
             does not publish this for opportunity ads) permits Meta to satisfy the coverage
             requirement while excluding a disproportionate share of total impressions from
             the largest campaigns. The third-party reviewer (Guidehouse) is "proposed and
             paid by Meta, subject to consent by the DoJ," has no privileged access to Meta's
             internal data, does not run its own test ads, and receives only Meta-aggregated,
             privacy-protected figures -- which the authors argue limits how independently the
             review can actually verify compliance, as distinct from recomputing the arithmetic
             Meta itself supplies.
Locators:    Abstract; §1 Introduction (settlement's two open questions); §2.1 (settlement
             terms, variance/coverage formulas, Table 1 coverage-requirement targets); §2.2
             (Meta's implementation, VRS multiplier mechanism); §2.3 (external verification,
             reviewer limits); §3 (three settlement-design gaps: impressions-not-individuals,
             selective coverage/leveling-down math with the political-ad sample, Fig. 2); §4
             (the 36-experiment audit, methodology in §4.1, housing results in §4.2.1 Fig. 4-5,
             employment/credit results in §4.2.2 Fig. 6, reach/cost results in §4.2.3).
Quote:       "While our work also operates without access to internal data, we suggest that
             our methods using test ads can strengthen an external audit and that such tests
             are critical to provide a more independent and broader scope verification of
             compliance that is not limited to verification of coverage computation formulas."
             (§2.3) "VRS thus 'passes the cost of decreasing variance to advertisers.'"
             (Abstract)
```

### Contradictions

- **Whether the delivery system itself, or only advertiser targeting, causes the skew.**
  Facebook's public position (ProPublica, March 2019, and again in earlier NFHA-suit
  statements) is that its systems do not discriminate and that HUD had "no evidence" the
  delivery system's own operation was responsible. The 2019 CSCW study directly contradicts
  this by holding targeting and budget identical across ad variants and still measuring large,
  statistically significant skew (e.g. 90% male / 72% white for identical lumber-industry job
  ads versus 65% female / 75% Black for identically-targeted janitor ads). HUD's charge takes
  the same position as the study, independently, based on its own investigation of Facebook's
  own platform documentation (paras. 17-20). Two independently-arrived-at findings (an
  academic study and a federal agency's reasonable-cause determination) versus one denial from
  the party under investigation is not, on its own, proof the denial is wrong, but it is not an
  evenly balanced dispute either: the study's method (identical targeting, varied only
  creative) is designed precisely to rule out the "it's the targeting" explanation Facebook's
  statement implies.

- **Whether the fix works, and for whom.** Meta's own whitepaper states VRS will produce "a
  substantial, albeit imperfect, reduction in variance" without giving a number. The
  independent 2025 audit gives numbers, and they split: VRS meaningfully reduces measured
  variance for housing ads (its original, legally required scope) but not, in the same audit,
  for employment or credit ads despite Meta's voluntary claim to have extended VRS there
  starting January 2025. The audit further shows the housing-ad improvement co-occurs with a
  reduction in how many unique people the ad reaches per dollar -- a real, quantified tradeoff
  Meta's own whitepaper does not disclose a number for, though the whitepaper does acknowledge
  in general terms that privacy protections "may slightly degrade the maximum performance of
  the system."

- **The 2019 settlement's total dollar figure.** The ACLU's own release implies roughly $3
  million across the matters it names; contemporaneous secondary reporting elsewhere states
  $5 million across ACLU/NFHA/CWA combined. Not resolved from primary sources in this
  invocation; low-stakes for the commission, which does not ask for a dollar figure here, but
  the writer should not state a figure without re-verifying, or should state the range with
  both attributions if a figure is used at all.

### Numbers

```text
Figure: 90% male / 72% white, aggregate delivery of five lumber-industry job ads
Owner:  Ali et al. 2019 (arxiv.org/abs/1904.02095), Introduction and §4.4/Fig. 8
Scope:  5 ad variants (white man/woman, Black man/woman, no-person image) of one job ad,
        identical targeting (NC voter-file audience C: ~900k White, ~892k Black), identical
        $20/day budget, 24-hour run, aggregated across the 5 variants

Figure: 65% female / 75% Black, aggregate delivery of five janitor-job ads
Owner:  Ali et al. 2019, §4.4/Fig. 8
Scope:  Same design and audience as above, different job category

Figure: 85% female, aggregate delivery of five supermarket-cashier job ads
Owner:  Ali et al. 2019, Introduction
Scope:  Same design and audience as above

Figure: 75% Black, aggregate delivery of five taxi-driver job ads
Owner:  Ali et al. 2019, Introduction
Scope:  Same design and audience as above

Figure: Housing-ad racial delivery ranged from an estimated 27% white users (luxury rental)
        to 49% white users (cheap house purchase) -- i.e. roughly 51% to 73% Black -- across
        otherwise identically-targeted, identically-budgeted housing ads
Owner:  Ali et al. 2019, §4.4/Fig. 9
Scope:  4 housing ad variants (cheap/luxury x buy/rent) plus a non-housing baseline, run 12
        hours each on North Carolina voter-file audiences A and B in rotation (Table 1),
        99% confidence intervals per Agresti-Coull method

Figure: Fraction of men in the audience ranged from over 55% (at $1/day budget) to under 45%
        (at $50/day budget) for an identical ad, budget varied alone
Owner:  Ali et al. 2019, §4.1/Fig. 2
Scope:  Same ad creative and targeted audience; Pearson correlation rho = -0.88 (p<10^-5)
        targeting all US users, rho = -0.73 (p<10^-3) targeting custom phone-number audiences

Figure: Bodybuilding ad delivered to >75% men (91% male with full creative); cosmetics ad to
        >90% women (5% male with full creative), for identically-targeted, identically-budgeted
        ads differing only in creative
Owner:  Ali et al. 2019, §4.2/Fig. 3

Figure: Country-music-albums ad delivered to ~80% white users; hip-hop-albums ad to ~13% white
        users; neutral top-30-albums ad to ~45% white users -- identical targeting/budget
Owner:  Ali et al. 2019, §4.4/Fig. 7

Figure: HUD charge date: March 28, 2019 (charge); underlying complaint filed August 13, 2018
Owner:  HUD Charge of Discrimination, FHEO No. 01-18-0323-8 (hud.gov)
Scope:  Administrative charge, not a court judgment

Figure: 2019 civil-rights settlement date: March 19, 2019, resolving 5 legal actions filed
        between November 2016 and September 2018
Owner:  Joint statement (aclu.org), confirmed independently by NFHA's own release
Scope:  n/a (qualitative)

Figure: DOJ v. Meta filed June 21, 2022 (S.D.N.Y., 1:22-cv-05187); settlement approved June
        27, 2022; civil penalty $115,054; Special Ad Audience housing-ad deadline December 31,
        2022; VRS compliance metrics agreed January 9, 2023; DOJ compliance oversight through
        June 27, 2026
Owner:  Civil Rights Litigation Clearinghouse case page (secondary; DOJ's own primary filings
        were gated at source -- see Sources note above). VRS-metrics and reviewer-requirement
        elements corroborated by Meta's own whitepaper, which cites the DOJ filing directly.

Figure: In the independent 2025 audit, VRS held measured variance below the settlement's 10%
        threshold in 15 of 18 race-comparison cases and 15 of 18 gender-comparison cases for
        housing ads (vs. fewer than 5 of 18 without VRS); this improvement did not carry over
        to ads voluntarily declared as credit or employment, where variance mostly stayed
        above 10%, "comparable to... the no-vrs case"
Owner:  Imana, Shen, Heidemann, Korolova, FAccT 2025, §4.2.1-4.2.2
Scope:  36 paired VRS/no-VRS experiments, 6 ad creatives, 3 replicated North Carolina
        voter-file audience partitions per experiment, 24-hour/$20-day campaigns

Figure: Enabling VRS reduced mean ad reach (unique people reached) by 9.82% for the same
        fixed budget, across the 36 paired experiments; cost per 1,000 unique people reached
        rose in most paired comparisons when VRS was enabled
Owner:  Imana, Shen, Heidemann, Korolova, FAccT 2025, §4.2.3
Scope:  Same 36-experiment audit as above

Figure: Meta's own settlement-agreed coverage targets for housing ads receiving >=1,000
        impressions: variance below 10% required for 91.7% of such ads (gender) and 81.0%
        (estimated race); for >=300 impressions: 90.2% (gender, 10% threshold) and 80.1%
        (race, 10% threshold); stricter 5%-variance targets are lower (84.5% gender, 61.0%
        race at >=1,000 impressions)
Owner:  Settlement compliance-metrics terms, as reproduced in Imana et al. 2025, Table 1
        (citing the parties' agreed-upon metrics filing; this record did not open that DOJ
        filing directly -- see Sources note)
Scope:  Housing ads only; these targets are not shown to apply to the voluntary
        employment/credit expansion
```

### Source assets

```text
Asset: Figure 8 in Ali et al. 2019 (arxiv.org/abs/1904.02095, §4.4) -- a two-panel dot plot
       showing, for each of 11 job categories (lumber, ai, taxi, lawyer, restaurant, doctor,
       nurse, secretary, preschool, janitor, supermarket), the fraction of men (left panel)
       and fraction of white users (right panel) the ad was delivered to, broken out by which
       stock-photo race/gender was pictured in that ad's image, plus an average marker per job.
Shows: The full spread of gender and racial skew across all 11 job categories at once, and
       that the skew tracks the image shown in the ad even though every job ad used identical
       targeting and budget -- the single clearest visual evidence for the commission's core
       mechanism claim (optimization, not targeting, produces the disparity).
Crop:  Keep both panels together (gender and race are the same 11 jobs, shown side by side);
       keep the job-category labels and the legend distinguishing Black man/Black woman/
       neutral/white man/white woman by image; omit nothing, the whole figure is the argument.

Asset: Figure 9 in Ali et al. 2019 (§4.4) -- a dot-and-error-bar plot of estimated fraction
       white in the delivered audience, one row per housing-ad variant (baseline, cheap-buy,
       cheap-rent, luxury-buy, luxury-rent), with 99% confidence intervals.
Shows: That housing ads for cheaper properties skewed toward Black audiences relative to
       otherwise identical luxury-property ads, holding targeting and budget fixed -- the
       housing-specific instance of the same mechanism, and the one closest to the federal
       housing charge's subject matter.
Crop:  Keep all five rows and the confidence-interval bars; the comparison across rows is the
       finding, not any single row's value.

Asset: Table 1 in the settlement's compliance metrics, as reproduced in Imana et al. 2025
       (§2.1, "Table 1: Coverage Requirements for Housing Ads") -- the agreed numeric variance/
       coverage thresholds Meta must meet, split by 5%/10% variance and by impression-volume
       tier.
Shows: The literal, government-agreed definition of "success" for VRS, in a domain where the
       settlement text itself was not directly accessible to this record -- useful as a
       primary-adjacent numeric anchor for what compliance means, and as a base for a possible
       chart comparing agreed targets against the 2025 audit's measured pass rates.
Crop:  Keep both the 5% and 10% rows and both impression-volume columns; the point is that
       the bar is lower than a reader might assume ("meets threshold" is not "zero skew").

Asset: Figure 5 (variance scatter, VRS vs no-VRS) and Figure 6 (delivery-ratio-to-Black-users
       comparison across housing/credit/employment) in Imana et al. 2025, §4.2.
Shows: A direct, real-world, post-fix measurement of whether the system Meta built actually
       moved delivery back toward the eligible audience, and that it did so for housing but
       not visibly for employment/credit -- the most current evidence available on "did the
       fix work."
Crop:  If used, crop to the housing-only panel for the main narrative point and hold the
       employment/credit panel in reserve for the "what's unresolved" beat; do not present
       the housing result without also surfacing that the same figure shows employment/credit
       not improving, or the crop would overstate the fix's scope.

A chart is supportable directly from the record's own numbers without needing the source
image: a bar chart of measured delivery skew by job category (Ali et al. 2019, Fig. 8's
underlying values -- lumber ~90% male/72% white, janitor ~65% female/75% Black, cashier ~85%
female, taxi ~75% Black, plus the housing figures 27%-49% white by property type) would carry
the mechanism argument cleanly, captioned to the study and dated 2019, with a caption noting
targeting and budget were held identical across every bar.
```

### Discarded

```text
URL: https://www.justice.gov/opa/pr/justice-department-secures-groundbreaking-settlement-agreement-meta-platforms-formerly-known -- gated, returned HTTP 401 Unauthorized on every attempt (direct fetch, alternate justice.gov subdomains/paths, and via archive.org, which this toolset cannot fetch at all). Same result for every other justice.gov and archives.opa URL tried, including the complaint PDF, the proposed-settlement PDF, the final-judgment PDF, the CRT case page, and the USAO-SDNY press release. Not treated as dead -- just inaccessible to this record; flagged to the orchestrator.
URL: https://www.courtlistener.com/docket/63398625/united-states-v-meta-platforms-inc/ -- returned HTTP 403 Forbidden; would have been a useful route to the underlying PDFs (RECAP-hosted) had it loaded.
URL: https://www.alphaxiv.org/abs/1904.02095 -- thin mirror of the same CSCW paper's abstract with no independent content beyond what the primary arXiv page and PDF already gave; not needed once the full paper was read directly.
URL: https://ccs.neu.edu/~mali/papers/facebook-delivery-cscw.pdf -- same paper as the arXiv copy used above (an author's self-hosted mirror); read via the arxiv.org/pdf/1904.02095 copy instead once the direct WebFetch summarizer failed on both and the file had to be opened directly as a PDF -- kept the arXiv copy as canonical since it is versioned and dated.
```
