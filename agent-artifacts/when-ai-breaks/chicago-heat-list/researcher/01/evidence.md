# Evidence: when-ai-breaks/chicago-heat-list (01)

The record strongly supports the commissioned narrative and its lesson. Chicago
built a person-level risk model (the Strategic Subject List, "heat list"), scored
hundreds of thousands of people who had ever been arrested, and attached police
attention to a high score. The one independent evaluation (RAND, Saunders/Hunt/
Hollywood, 2016) found the pilot did not change a listed person's chance of being
shot or killed, and did raise their chance of being arrested for a shooting. The
city's own Inspector General (2020) found the scores were unreliable, staff were
untrained, access was uncontrolled, and the interventions may have punished people
for arrests that never led to conviction. The released dataset and independent
analyses (Upturn, Chicago Sun-Times) show the list was overwhelmingly built from
arrest records, scored people with no violent history, and closely tracked the
demographics of who Chicago arrests. The mechanism the article teaches
(arrest data is a proxy for policing, not for crime, so a model trained on it
targets the already-policed) is documented as a primary legal-scholarly analysis
(Richardson/Schultz/Crawford, NYU Law Review) resting on the DOJ's 2017 finding
that CPD ran a pattern of unlawful force concentrated on Black and Latino
residents during the exact years the SSL data was generated. The present-day hook
is firm: the EU's AI Act (Reg. 2024/1689), in force since Feb 2, 2025, now
prohibits exactly this class of person-based crime-risk profiling.

Where it is thin, and where it cuts against a flat "this whole class of system
cannot work": RAND itself declines to say whether the pilot failed because the
theory is wrong or because the intervention was never built ("theory failure vs.
implementation failure"), notes no violent "backfire," allows the pilot "may have
improved justice by identifying more perpetrators," and reports the algorithm
improved in later versions. The OIG's findings are about reliability and process,
not a formal finding of racial bias; the racial-disparity claim is owned by the
released data and by outside analysis, not by the OIG. The famous "56% of Black
men" figure has a small provenance wrinkle (see Contradictions). Total federal
spend is best cited from OIG's $3.8M; the individual NIJ awards I could confirm
sum to less because a DOJ Bureau of Justice Assistance grant also funded the tool.

---

## Sources

```text
URL:         https://link.springer.com/article/10.1007/s11292-016-9272-0
Kind:        primary. Owns the only independent evaluation of the SSL pilot; the
             authors designed and ran the quasi-experiment. (Read in full via the
             openly posted copy at
             https://www.nacdl.org/getattachment/9d276b57-0d3f-477a-90fb-5a00c003edff/rand-ssl-study.pdf ;
             also hosted by RAND at https://www.rand.org/pubs/external_publications/EP67204.html
             and NIJ at https://nij.ojp.gov/library/publications/predictions-put-practice-quasi-experimental-evaluation-chicagos-predictive )
Establishes: What the SSL pilot did to a listed person's risk of violence and of
             arrest. The pilot's design, sample, period, and the intervention
             actually attached to a high score.
Paraphrase:  Jessica Saunders, Priscillia Hunt, and John S. Hollywood, all of the
             RAND Corporation (Santa Monica), evaluated the Chicago Police
             Department's 2013 predictive-policing pilot. It used version 1.0 of
             the model. 426 people judged highest-risk were placed on the SSL on
             March 26, 2013. Using propensity-score matching, the treated group
             was no more or less likely than matched controls to be a shooting or
             homicide victim, but was 2.88 times more likely to be arrested for a
             shooting. City-level ARIMA analysis found the homicide decline
             predated the SSL and was not caused by it. The only formal "treatment"
             (a commander visit offering services) ran in one district and reached
             under 5% of listed people. The authors could not resolve whether the
             null victimization result reflects theory failure or implementation
             failure. Published J. Exp. Criminol. (2016) 12:347-371,
             DOI 10.1007/s11292-016-9272-0.
Locators:    Abstract p.347; intervention pp.355-356, 360-361; Table 3 "Doubly
             robust treatment estimates" p.364; discussion pp.363-366;
             conclusions pp.366-368.
Quote:       "Individuals on the SSL are not more or less likely to become a
             victim of a homicide or shooting than the comparison group, and this
             is further supported by city-level analysis. The treated group is
             more likely to be arrested for a shooting." (Abstract)
             "those placed on the SSL were 2.88 times more likely than their
             matched counterparts to be arrested for a shooting, although this is
             based on of a small absolute number of shootings - only 9 individuals
             from the SSL were arrested for a shooting in the year after being
             placed on the list, against 5 from the matched control group"
             "This was the only place where a formal [treatment] was offered as a
             way to prevent gun crime ... As only one district participated, less
             than 5 % the SSLs were subject to this intervention"
             "the pilot version 1.0 of the model identified less than 1 % of
             homicide victims (3 out of 405)"
```

```text
URL:         https://igchicago.org/publications/advisory-concerning-the-chicago-police-departments-predictive-risk-models/
Kind:        primary. The City of Chicago Office of Inspector General's own audit
             of CPD's risk models; it owns these findings. (PDF read in full at
             https://igchicago.org/wp-content/uploads/2020/01/OIG-Advisory-Concerning-CPDs-Predictive-Risk-Models-.pdf )
Establishes: The program's full scope and lifecycle, how many people were scored,
             who got scored, why the scores were unreliable, the decommissioning
             date and reason, and the total federal grant spend.
Paraphrase:  OIG File #18-0106, "Advisory Concerning the Chicago Police
             Department's Predictive Risk Models," issued January 23, 2020 over
             Inspector General Joseph M. Ferguson, addressed to Interim
             Superintendent Charlie Beck. CPD received $3.8 million in federal
             grants to build models predicting who would become a "party to
             violence" (PTV), i.e. victim or offender in a shooting. There were
             six versions: five iterations of the SSL (risk "scores"), then the
             Crime and Victimization Risk Model, CVRM (risk "tiers"). Illinois
             Institute of Technology built them; RAND evaluated versions 1, 5, and
             6. Every person arrested at least once in the four years before a
             calculation got a score, regardless of any violent history; victims
             never arrested got none. As of July 2018, 399,412 people had an SSL
             score; as of March 2019, 313,513 had a CVRM tier. SSL scores were not
             updated from August 2016 until CVRM launched Jan 9, 2019 - static for
             ~2.5 years. Six areas of concern: (1) scores/tiers were unreliable;
             (2) sworn personnel were not properly trained; (3) no controls on
             internal/external access; (4) interventions may have attached
             negative consequences to arrests that did not result in convictions;
             (5) versions 2-5 were never evaluated; (6) no sustainability plan.
             CPD told OIG in August 2019 it would decommission the program and did
             so November 1, 2019 (grant period ended September 30, 2019).
Locators:    Cover letter p.1; background/attributes p.1; "Individuals Who
             Received a Risk Score or Tier" p.2; "General Areas of Concern"
             p.3-4; data-staleness finding pp.4-5 ("Clean and Vet Data").
Quote:       "CPD received $3.8 million in federal grants to develop these models"
             "Every individual arrested at least once within a four-year time
             period prior to IIT's calculation - regardless of whether they had a
             history of violence - received a risk score or risk tier."
             "an individual arrested for a non-violent misdemeanor (for example,
             certain instances of driving over the speed limit), might have been
             assigned a risk score or tier while a victim of a gunshot wound (who
             was never arrested) would not have been included in the model."
             "Interventions influenced by CPD's PTV risk models may have attached
             negative consequences to arrests which did not result in
             convictions."
```

```text
URL:         https://data.cityofchicago.org/d/4aki-r3np
Kind:        primary. The released list itself - the artifact the article examines.
             (Catalog record confirmed at
             https://catalog.data.gov/dataset/strategic-subject-list-historical )
Establishes: The list exists as a public, de-identified dataset; its score range,
             its input attributes, and that it carried race/sex fields.
Paraphrase:  "Strategic Subject List - Historical," published by the City of
             Chicago on its Data Portal. Covers August 1, 2012 to July 31, 2016.
             SSL score runs 0 (extremely low risk) to 500 (extremely high risk).
             Eight ranking attributes: times a shooting victim; age at latest
             arrest; times a victim of aggravated battery/assault; prior arrests
             for violent offenses; gang affiliation; prior narcotics arrests;
             trend in recent criminal activity; prior unlawful-use-of-weapon
             arrests. The dataset includes race and sex fields; CPD states these
             were not used in the algorithm.
Locators:    Dataset landing page (About / Columns).
Quote:       (dataset field descriptions; no single load-bearing sentence)
```

```text
URL:         https://www.upturn.org/work/how-strategic-is-chicagos-strategic-subjects-list/
Kind:        secondary. Upturn analyzes the released dataset from outside CPD; it
             owns its computed figures but reports on CPD's data. (Companion
             write-up: https://medium.com/equal-future/how-strategic-is-chicagos-strategic-subjects-list-upturn-investigates-9e5b4b235a7c )
Establishes: How many listed people had scores above the scrutiny threshold, how
             many had no arrest or shooting-victim record, and that score is
             driven mostly by age.
Paraphrase:  By Brianna Posadas, published June 22, 2017, analyzing the dataset
             released after the Sun-Times FOIA fight. Of 398,684 people on the
             list, 287,404 had scores above 250 (the level CPD says draws
             heightened scrutiny) - over two-thirds. 127,513 had never been
             arrested and had never been a shooting victim; roughly 90,000 of
             those were still rated high risk. Upturn reports age explains roughly
             89% of the variance in SSL scores.
Locators:    Body of the post; summary figures.
Quote:       "127,513 [people] have never been arrested or been the victim of a
             shooting, yet the model deemed them worthy of a risk score" (as
             reported); "age accounts for roughly 89% of variance in SSL scores"
```

```text
URL:         https://chicago.suntimes.com/2017/5/18/18386116/a-look-inside-the-watch-list-chicago-police-fought-to-keep-secret
Kind:        secondary. Investigative reporting that pried the data loose via
             FOIA litigation and analyzed it; reports on CPD's records.
Establishes: How the data became public, the top-of-list composition, the score
             range, and the racial skew at the top.
Paraphrase:  By Mick Dumke and Frank Main, May 18, 2017. The Sun-Times obtained
             the data through an Illinois FOIA lawsuit after CPD refused even a
             names-removed version; the Attorney General's office found CPD in
             violation. The database held more than 398,000 entries - everyone
             arrested and fingerprinted in Chicago since 2013. Scores ran 10 to
             500. 153 people had the maximum 500; 3,568 scored 400-499. Nearly
             half of the people at the top had never been arrested for illegal gun
             possession; about 13% had never been charged with any violent crime;
             20 of the 153 highest-scored had never been arrested for guns or
             violence. 85% of those with the highest score were African-American
             men.
Locators:    Article body (data findings and racial breakdown).
Quote:       "Nearly half of the people at the top of the list have never been
             arrested for illegal gun possession"
             "20 of the 153 people deemed most at risk to be involved in violent
             crime, as victim or shooter, have never been arrested either for guns
             or violence"
             "the vast majority of people with the highest score - 85 percent -
             were African-American men"
```

```text
URL:         https://www.nyulawreview.org/wp-content/uploads/2019/04/NYULawReview-94-Richardson-Schultz-Crawford.pdf
Kind:        primary (for its own analysis and argument). Rashida Richardson,
             Jason M. Schultz, and Kate Crawford originate the "dirty data" thesis
             and the multi-jurisdiction study; it is the primary analysis of the
             feedback-loop/proxy-label problem the brief asks for. Also a scholarly
             secondary on SSL facts it restates.
Establishes: The mechanism: arrest-based data generated during documented unlawful,
             racially biased policing trains a model that then targets the same
             already-policed population - and Chicago is the lead case study.
Paraphrase:  "Dirty Data, Bad Predictions: How Civil Rights Violations Impact
             Police Data, Predictive Policing Systems, and Justice," 94 N.Y.U. L.
             Rev. 192 (May 2019). "Dirty policing" (flawed, racially biased,
             sometimes unlawful practices) shapes how data is created, producing
             "dirty data"; systems trained on it "cannot escape the legacies of
             the unlawful or biased policing practices that they are built on."
             Chicago is Case Study 1. The SSL was built by IIT and funded through
             the DOJ Bureau of Justice Assistance grant program; a majority of its
             variables are arrest records, not convictions, so people who
             committed no crime can land on the list and the list "likely reflects
             CPD's unlawful and biased practices." The authors report that more
             than one-third of listed people had never been arrested or been a
             crime victim and almost 70% of that cohort got a high score, and that
             56% of Black men under thirty in Chicago had an SSL score - the same
             group the DOJ and ACLU found CPD unlawfully targeted. Footnote 68
             notes SSL enforcement overlaps spatially with the heavily-patrolled,
             predominantly non-white South and West sides.
Locators:    Abstract p.192; "dirty data/dirty policing" definitions pp.192-193,
             199-201; Case Study 1: Chicago pp.205-210; SSL variables and findings
             pp.208-209; footnotes 64, 68-71.
Quote:       "If predictive policing systems are informed by such data, they cannot
             escape the legacies of the unlawful or biased policing practices that
             they are built on."
             "a majority of these variables are based on arrest records, rather
             than convictions, which not only means that people who have not
             committed crimes may end up on the list but also that the list likely
             reflects CPD's unlawful and biased practices"
             "fifty-six percent of Black men under the age of thirty in Chicago
             have a risk score on the SSL, and this is the same demographic that
             has been disproportionately affected by CPD's unlawful and biased
             practices"
```

```text
URL:         https://www.justice.gov/d9/chicago_police_department_findings.pdf
Kind:        primary. The U.S. Department of Justice's own pattern-or-practice
             findings on CPD; it owns this finding.
Establishes: The underlying fact that makes the "dirty data" mechanism concrete:
             during the years the SSL data was generated, CPD's policing was
             found unlawful and concentrated on Black and Latino residents.
Paraphrase:  "Investigation of the Chicago Police Department," Civil Rights
             Division, U.S. DOJ and U.S. Attorney's Office for the Northern
             District of Illinois, released January 13, 2017. Found CPD engaged in
             a pattern or practice of unreasonable force in violation of the Fourth
             Amendment, tied to systemic training and accountability failures, and
             documented that CPD's practices fell disproportionately on Black and
             Latino Chicagoans and young men of color.
Locators:    Summary of findings pp.4-5; disproportionate impact on communities of
             color pp.68, 143-150 (as cited by Richardson et al. n.70).
Quote:       "CPD engages in a pattern or practice of using force, including deadly
             force, in violation of the Fourth Amendment"
```

```text
URL:         https://nij.ojp.gov/funding/awards/2011-ij-cx-k014
Kind:        primary. The federal award record.
Establishes: The main NIJ grant that funded the SSL demonstration and evaluation.
Paraphrase:  "Chicago Police Predictive Policing Demonstration and Evaluation
             Project: Phase 2," awarded to the Chicago Police Department, NIJ award
             2011-IJ-CX-K014. Total $2,999,984 including the original award and
             2012 and 2014 supplements. Status: Closed.
Locators:    Award detail page (amount, recipient, number).
Quote:       (award metadata)
```

```text
URL:         https://nij.ojp.gov/funding/awards/2009-de-bx-k223
Kind:        primary. The federal award record.
Establishes: The earlier NIJ planning grant for the program.
Paraphrase:  "Chicago Police Department's Predictive Policing Demonstration and
             Evaluation Planning Program," awarded to the Chicago Police
             Department, NIJ award 2009-DE-BX-K223, $196,406.
Locators:    Award detail page.
Quote:       (award metadata)
```

```text
URL:         https://www.iit.edu/directory/people/miles-wernick
Kind:        primary. IIT's own description of its faculty member and his role.
Establishes: The algorithm's designer, his exact title and institution, and the
             NIJ/CPD relationship.
Paraphrase:  Miles N. Wernick, Professor Emeritus of Biomedical Engineering and
             former Motorola Endowed Chair Professor of Electrical and Computer
             Engineering at the Illinois Institute of Technology, was technical
             lead on the NIJ-sponsored predictive-policing research program with
             the Chicago Police Department, applying machine learning, social
             network analysis, and image-processing methods to crime data.
Locators:    Faculty bio page.
Quote:       "technical lead on a research program in 'predictive policing' in
             collaboration with the Chicago Police Department, sponsored by the
             National Institute of Justice (NIJ)"
```

```text
URL:         https://artificialintelligenceact.eu/article/5/
Kind:        primary. The consolidated text of the EU AI Act (Regulation (EU)
             2024/1689) reproduced with article navigation; the law itself.
Establishes: The present-day treatment of exactly this class of system:
             person-based crime-risk profiling is now prohibited in the EU.
Paraphrase:  Regulation (EU) 2024/1689 (AI Act). Article 5's prohibitions became
             applicable February 2, 2025. Article 5(1)(d) bans placing on the
             market or using an AI system to assess or predict the risk of a
             natural person committing a criminal offence based solely on profiling
             or on assessing personality traits and characteristics. A carve-out
             allows AI that supports a human assessment already grounded in
             objective, verifiable facts directly linked to criminal activity.
Locators:    Article 5(1)(d) and its exception.
Quote:       "making risk assessments of natural persons in order to assess or
             predict the risk of a natural person committing a criminal offence,
             based solely on the profiling of a natural person or on assessing
             their personality traits and characteristics"
```

```text
URL:         https://www.chicagomag.com/city-life/august-2017/chicago-police-strategic-subject-list/
Kind:        secondary. Chicago Magazine reporting analyzing the released data.
             (Note: this domain now 301-redirects to a chicagotribune.com reprint
             that the fetcher could not reach; the article's own home is the
             chicagomag.com URL recorded here and it is the citation Richardson et
             al. use at n.67/n.70.)
Establishes: A cited home for the "56% of Black men" figure and the age-driven
             nature of the score.
Paraphrase:  "The Contradictions of Chicago Police's Secretive List," by Yana
             Kunichoff and Patrick Sier, August 21, 2017. Reports on the SSL data,
             including the finding that a large majority of high scores track age
             and that a majority of young Black men in Chicago carried a score.
Locators:    Article body.
Quote:       (figure verified via Richardson et al. n.70; see Contradictions on
             "under thirty" vs "20 to 29")
```

```text
URL:         https://chicago.suntimes.com/city-hall/2020/1/27/21084030/chicago-police-strategic-subject-list-party-to-violence-inspector-general-joe-ferguson
Kind:        secondary. Reporting on the program's end.
Establishes: The public account of decommissioning and CPD's framing.
Paraphrase:  By Sam Charles, January 27, 2020. Reports CPD retired the SSL in
             November 2019 after the OIG advisory; nearly 400,000 people were
             scored between August 2012 and June 2018 regardless of conviction
             status; the program ran largely in secret until the Sun-Times pried a
             version loose in 2017. CPD offered no on-record defense in the piece;
             IG Joe Ferguson framed the lesson as careful data handling and
             purpose-driven policy.
Locators:    Article body.
Quote:       (as paraphrased)
```

---

## Contradictions

- **CPD's stated purpose vs. what the list did.** CPD framed the SSL as a way to
  identify at-risk people and connect them to social services (the Custom
  Notification Program). RAND found the only formal "treatment" reached under 5%
  of listed people and that the measurable effect was on arrests, not
  victimization. The OIG found the same CPD directive urged "the highest possible
  charges" for listed people who were later arrested, and flagged that
  interventions "may have attached negative consequences to arrests which did not
  result in convictions." Richardson et al. (n.72-74) note most districts did not
  focus SSL enforcement on services. The prevention framing and the enforcement
  reality diverge sharply. This supports, not undermines, the angle.

- **Did the pilot fail because the idea is wrong, or because it was never built
  out? (Steelman the program.)** RAND explicitly does not settle this: "it is not
  clear if this is due to the absence of a defined prevention strategy or a lack
  of impact because this sort of approach cannot work (e.g., theory failure vs.
  implementation failure)." RAND also found no violent "backfire," said the pilot
  "may have improved justice by identifying more perpetrators," and reported the
  algorithm improved in later versions (per IIT/Lewin & Wernick 2015, a newer
  iteration accurately predicted gun-violence involvement for 29% of the top 400
  over 18 months). A lesson claiming "this class of system fails" must engage
  this: the record supports that the deployment failed and that the class carries
  structural flaws (proxy labels, feedback loops, near-impossible low-base-rate
  prediction, no defined intervention), but RAND does not declare the class
  impossible.

- **What the OIG did and did not find.** The OIG's concerns are reliability,
  training, access controls, sustainability, and interventions punishing
  non-convictions. The OIG did not issue a formal finding of racial bias in the
  model. The racial-disparity claim is owned by the released dataset (primary) and
  by outside analysis (Sun-Times, Upturn, Richardson et al.), which the writer
  should attribute accordingly rather than to the OIG.

- **The "no violent record" figure has two owners with two denominators.** The
  Sun-Times reports the finding at the top of the list (e.g., 20 of the 153
  highest-scored never arrested for guns or violence; ~13% of top-scored never
  charged with any violent crime). Upturn reports it across the whole list
  (127,513 never arrested or shot, ~90,000 of them still high-risk). Richardson et
  al. state "more than one third ... have never been arrested or a victim of a
  crime, and almost seventy percent of that cohort received a high risk score."
  These are consistent but not interchangeable; cite the figure with its
  denominator.

- **"56% of Black men" - age band and provenance.** Richardson et al. (n.70) state
  "fifty-six percent of Black men under the age of thirty," attributing it to the
  SSL data and to Kunichoff & Sier (Chicago Magazine). Other secondary summaries
  render it as "ages 20 to 29." The underlying figure lives in the released data /
  the Chicago Magazine analysis, not in a government primary I could open directly;
  the cleanest citation is Richardson et al. ("under thirty"). Do not present the
  "20 to 29" phrasing as if a primary owns it.

- **Population counts are snapshots, not one number.** 426 = the 2013 pilot list
  (RAND, model v1.0). 398,684 = the dataset released in 2017 (Upturn/Sun-Times).
  399,412 with an SSL score as of July 2018 and 313,513 with a CVRM tier as of
  March 2019 (OIG). "Nearly 400,000 between Aug 2012 and June 2018" (Sun-Times
  2020). Each belongs to its own model version and date; do not blend them.

- **Federal spend.** OIG: $3.8 million total federal grants. The two NIJ awards I
  confirmed sum to $3,196,390 (2011-IJ-CX-K014 $2,999,984 + 2009-DE-BX-K223
  $196,406); Richardson et al. attribute tool funding to the DOJ Bureau of Justice
  Assistance. Cite $3.8M to the OIG as the authoritative total; treat the NIJ award
  figures as the identifiable components, not the whole.

---

## Numbers

```text
Figure: 426 people placed on the SSL (pilot, model version 1.0)
Owner:  RAND / Saunders, Hunt, Hollywood (2016)
Scope:  The March 26, 2013 pilot list; each district's top 20 plus all scoring 500+
```

```text
Figure: Shooting-victim effect Exp(b) = 0.802, t = -0.558, p = 0.58 (not significant)
Owner:  RAND, Table 3 "Doubly robust treatment estimates", p.364
Scope:  Treated (n=426) vs. matched controls, ~12 months post-listing
```

```text
Figure: Murder-victim effect Exp(b) = 1.04, p = 0.96 (not significant)
Owner:  RAND, Table 3, p.364
Scope:  Same
```

```text
Figure: Shooting-arrest effect Exp(b) = 2.88, t = 2.46, p = 0.01 (significant)
Owner:  RAND, Table 3, p.364
Scope:  Same. Absolute counts: 9 SSL vs. 5 matched controls arrested for a shooting
```

```text
Figure: Murder-arrest effect Exp(b) = 1.57, p = 0.33 (not significant)
Owner:  RAND, Table 3, p.364
Scope:  Same
```

```text
Figure: Model identified <1% of homicide victims (3 of 405)
Owner:  RAND (2016), discussion p.363
Scope:  405 Chicago homicides, March 2013-March 2014; pilot model v1.0 recall
```

```text
Figure: Listed people's 12-month homicide rate = 0.7% (vs 0.036% for prior-arrest
        non-listed; 0.003% for residents without records)
Owner:  RAND (2016), p.365
Scope:  Year after the pilot list; illustrates low-base-rate prediction difficulty
```

```text
Figure: SSL score range 0-500 (max multiplier capped at "500+")
Owner:  City of Chicago Data Portal (dataset); RAND p.356; Sun-Times reports 10-500 observed
Scope:  Score assigned to each arrestee
```

```text
Figure: $3.8 million federal grants (total program)
Owner:  Chicago OIG (2020), p.1
Scope:  Full PTV risk-model program, ~2009-2019
```

```text
Figure: NIJ award 2011-IJ-CX-K014 = $2,999,984; NIJ award 2009-DE-BX-K223 = $196,406
Owner:  NIJ award records
Scope:  Identifiable NIJ components of the federal funding
```

```text
Figure: 399,412 with an SSL score (July 2018); 313,513 with a CVRM tier (March 2019)
Owner:  Chicago OIG (2020), p.2
Scope:  Everyone arrested at least once in the prior four years, regardless of violent history
```

```text
Figure: 398,684 on the released list; 287,404 scored above 250; 127,513 never
        arrested or shot (~90,000 of them high-risk); age ~89% of score variance
Owner:  Upturn / Brianna Posadas (2017), from the released dataset
Scope:  The 2017 FOIA-released SSL dataset
```

```text
Figure: 153 people at max score 500; 3,568 scored 400-499; 85% of highest-scored
        were African-American men; 20 of top 153 never arrested for guns or violence
Owner:  Chicago Sun-Times / Dumke & Main (2017)
Scope:  Same released dataset, top of the list
```

```text
Figure: >1/3 of listed people never arrested or a crime victim, ~70% of them
        high-scored; 56% of Black men under 30 in Chicago had a score
Owner:  Richardson, Schultz, Crawford (2019), pp.208-209
Scope:  Released SSL dataset (their reading of Upturn/NYT and SSL data)
```

```text
Figure: SSL scores static from August 2016 until CVRM launch January 9, 2019 (~2.5 years)
Owner:  Chicago OIG (2020), pp.4-5
Scope:  Data-staleness finding
```

```text
Figure: EU AI Act (Reg. 2024/1689) Article 5 prohibitions applicable February 2, 2025
Owner:  Regulation (EU) 2024/1689, Article 5(1)(d)
Scope:  Present-day legal status of person-based crime-risk profiling in the EU
```

---

## Source assets

```text
Asset: RAND Table 3, "Doubly robust treatment estimates" (p.364) - the five
       outcome rows (shooting victim, shooting arrest, murder victim, murder
       arrest, any weapon) with Exp(b) and p-values.
Shows: In one frame, the entire finding: no effect on victimization, a large
       effect only on shooting arrests. This is the load-bearing evidence and
       reads better as the table's five rows than as prose.
Crop:  Retain the outcome labels, Exp(b) column, and p-values. A rebuilt clean
       table (per spec/charts.md, not a screenshot) is the honest form; keep the
       exact numbers and note non-significance.
```

```text
Asset: The released "Strategic Subject List - Historical" dataset itself
       (data.cityofchicago.org/d/4aki-r3np) - the columns showing score, race,
       sex, arrest counts, and victimization counts per de-identified person.
Shows: That the list is a real, browsable roster with race/sex attached and that
       score is computed from arrest-heavy inputs. The artifact's existence is
       part of the story.
Crop:  If any view is shown, it must be the public de-identified dataset only;
       omit anything resembling an identifiable individual.
```

```text
Asset: A distribution of SSL score against age from the released data (the basis
       of Upturn's "~89% of variance is age").
Shows: That the "risk" score largely re-encodes age - the cleanest single
       demonstration that the model is not measuring what it claims.
Crop:  Would need to be rebuilt as an honest chart from the primary dataset per
       spec/charts.md; label axes and cite the City Data Portal. Only build if the
       writer uses the age point.
```

```text
Asset: None found beyond the above for the OIG, NIJ, DOJ, and EU sources - their
       evidence is textual (findings, award figures, statutory language) and is
       better carried as quotation than as a document image.
```

---

## Discarded

```text
URL: https://www.researchgate.net/publication/306071857 - repost of the RAND
     article; cite the journal's own DOI page instead.
URL: https://cebcp.org/.../individuals-saunders-et-al-2016/ - secondary summary of
     the RAND study; the primary was read directly, so this adds nothing.
URL: https://www.activistpost.com/2013/08/... - advocacy blog, not a reliable
     record.
URL: https://www.smithhanley.com/2017/02/14/predictive-policing-in-chicago/ -
     staffing-firm blog; unsourced restatement.
URL: https://worldmetrics.org/predictive-policing-statistics/ and
     https://wifitalents.com/predictive-policing-statistics/ - aggregated "stat"
     pages with no traceable primary; unusable for figures.
URL: https://policypoliticalreview.com/2025/05/08/... - opinion blog; used none of
     its claims.
URL: https://www.scribd.com/doc/552868478 - re-host of the OIG advisory; the
     official igchicago.org PDF was read instead.
URL: https://www.thenation.com/article/archive/what-amazon-taught-cops/ - relevant
     context on predictive policing generally but not needed; primary sources cover
     the claims.
URL: https://arxiv.org/pdf/2405.07715 ("Evidence of What, for Whom?") - a 2024
     retrospective on the SSL; interesting but secondary and not required once the
     primary record (RAND, OIG, released data, Dirty Data) is in hand. Available if
     the writer wants a recent scholarly read for Go deeper.
```
