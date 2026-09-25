# evidence: when-ai-breaks/babylon-health (01)

The record supports the commission's two-failure structure firmly. Failure one, the
oversold "beats doctors" claim, rests on documents I read in full: Babylon's own 2018
preprint (Razzaki et al.), which reports diagnostic accuracy "comparable to" doctors and
triage "safer on average," never "better," and which itself warns its results "cannot be
directly interpreted with respect to real-world accuracy and safety"; and the clinical
critique (Fraser, Coiera, Wong in The Lancet, and Coiera's contemporaneous line-by-line
review), which shows the headline depends on the curated test set and the comparison
protocol. Failure two, documented under-triage, rests on reproduced demonstrations by a
named NHS consultant, a gov.uk Field Safety Notice, and the MHRA's own letter conceding
his concerns. Where the record is thin: the under-triage failures are known through the
whistleblower's demonstrations and journalism that reproduced them, not through an
independent audited dataset with a denominator, so no rate of real-world under-triage can
be stated. The Lancet correspondence full text is paywalled and bot-gated; I confirmed its
citation through Crossref and its key objection through multiple reproductions plus
Coiera's own review. The single "81%" exam figure is Babylon's marketing composite, not a
number the study states; the paper reports separate component scores.

## Sources

```text
URL:         https://arxiv.org/abs/1806.10698  (PDF: https://arxiv.org/pdf/1806.10698)
Kind:        primary. This is the document Babylon's 2018 claim rests on, authored by
             Babylon staff and collaborators; it owns the accuracy and safety figures.
Establishes: The design and the exact figures of the "AI vs doctors" study.
             Title: "A comparative study of artificial intelligence and human doctors for
             the purpose of triage and diagnosis." Authors: Salman Razzaki, Adam Baker,
             Yura Perov, Katherine Middleton, Janie Baxter, Daniel Mullarkey, Davinder
             Sangar, Michael Taliercio, Mobasher Butt (all Babylon Health), Azeem Majeed
             (School of Public Health, Faculty of Medicine, Imperial College London),
             Arnold DoRosario (Northeast Medical Group, Yale New Haven Health), Megan
             Mahoney (Division of Primary Care and Population Health, School of Medicine,
             Stanford University), and corresponding author Saurabh Johri (Babylon Health).
             arXiv:1806.10698v1 [cs.AI], posted 27 June 2018. Later published in Frontiers
             in Artificial Intelligence (2020); the 2018 preprint is the document behind
             the RCP-event claim.
             Design: prospective validation using a "semi-naturalistic, role-play" OSCE
             format. 100 clinical vignettes written by independent medical practitioners,
             each modelling one condition in a patient aged >=16. Run over four rounds on
             consecutive days; in each round up to four "patients" (played by GPs) and four
             doctors. Seven locum GPs (Doctors A-G), none involved in building the model,
             gave a differential and triage per case. To keep the judge blinded, doctors
             had to pick diagnoses from the list of conditions the Babylon system models.
             A single independent judge (plus two in-house GPs on a subset) rated
             differentials and set the acceptable triage range. Separately, 30 vignettes
             from Semigran et al. 2015, 15 MRCGP Applied Knowledge Test vignettes, and 36
             MRCGP Clinical Skills Assessment vignettes were run against the system as
             external benchmarks.
Locators:    Abstract (p.1); "4 METHODS" and "4.2 Testing paradigm" (pp.3-4); Table 1 and
             surrounding text (p.4); Table 2 (p.6); Table 3 (p.7); sections 5.4.1-5.4.3
             (pp.6-7); "6 DISCUSSION" (pp.7-8).
Quote:       "the Babylon AI powered Triage and Diagnostic System was able to identify the
             condition modelled by a clinical vignette with accuracy comparable to human
             doctors (in terms of precision and recall). In addition, we found that the
             triage advice recommended by the AI System was, on average, safer than that of
             human doctors ... with only a minimal reduction in appropriateness." (Abstract)
             "our results cannot be directly interpreted with respect to real-world
             accuracy and safety." (Discussion, section 5.4.3 / p.7)
             "on the diagnostic component in isolation, it achieved accuracy rates above
             72%, the average pass mark for the past 5 years [RCGP] for the entire MRCGP
             exam." (Discussion, p.8) The paper adds the system's MRCGP performance
             "cannot be taken as a demonstration of an ability to pass the examination in
             full."
```

```text
URL:         https://doi.org/10.1016/S0140-6736(18)32819-8
             (document home: https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(18)32819-8/fulltext)
Kind:        primary. Peer critique authored by the three clinicians who made it; it owns
             their objection. Full text is paywalled and bot-gated (the DOI resolves; the
             fulltext page returns 403 to automated requests).
Establishes: The formal clinical objection to the study. Citation confirmed via Crossref:
             Hamish Fraser, Enrico Coiera, David Wong, "Safety of patient-facing digital
             symptom checkers," The Lancet, 2018; vol. 392, issue 10161, pp. 2263-2264
             (November 2018), DOI 10.1016/S0140-6736(18)32819-8.
Locators:    Correspondence, pp. 2263-2264. Citation fields from the Crossref record for
             the DOI.
Quote:       Their central conclusion, reproduced identically across contemporaneous
             coverage: the study "does not offer convincing evidence that its Babylon
             Diagnostic and Triage System can perform better than doctors in any realistic
             situation, and there is a possibility that it might perform significantly
             worse." (See Limits on how this quote was verified given the paywall.)
```

```text
URL:         https://coiera.com/2018/06/29/paper-review-the-babylon-chatbot/
Kind:        primary. Firsthand technical review by Enrico Coiera, one of the three Lancet
             authors; it is his own analysis of the study, not reporting on it.
Establishes: The specific methodological objections behind the Lancet letter, dated
             29 June 2018 (two days after the preprint).
             - The test used artificial vignettes entered into the system, not real
               patients: "It doesn't test Babylon in front of real patients."
             - Selection bias: "any vignettes outside of the Babylon system's capability
               were excluded. They only tested Babylon on vignettes it had a chance to get
               right," while "the humans did not have a reciprocal right to exclude
               vignettes they were not good at."
             - Fragility to one doctor: "Removing B from the data set and recalculating
               results shows humans beating Babylon on every measure in Table 1."
             - No significance testing: "No statistical testing is done to check if the
               differences reported are likely due to chance variation."
             - A human operator translated each vignette into the system, an unquantified
               human contribution to the system's score.
             - Single assessor, "no inter-rater reliability measures."
             - On the one clean head-to-head external benchmark (30 cases), humans led on
               top-1 diagnosis.
Locators:    Blog post body, coiera.com, 29 June 2018.
Quote:       See Establishes; quotes are the review's own words.
```

```text
URL:         https://www.gov.uk/drug-device-alerts/field-safety-notice-11-to-15-february-2019
Kind:        primary. UK regulator (MHRA) public document; it owns the regulatory record.
Establishes: The MHRA logged a Field Safety Notice for the Babylon symptom checker.
             Entry: "Babylon Health: Chatbot Online Doctor," dated 13 February 2019,
             classification "Diagnostic / therapeutic software algorithm," MHRA reference
             2018/005/016/291/021.
Locators:    Field safety notices listing for 11-15 February 2019, gov.uk.
Quote:       "Babylon Health: Chatbot Online Doctor / 13 February 2019 / Diagnostic /
             therapeutic software algorithm / MHRA reference: 2018/005/016/291/021"
```

```text
URL:         https://www.sec.gov/Archives/edgar/data/1866390/000119312521304150/d231170dex991.htm
Kind:        primary. Babylon Holdings Ltd SEC filing (Form 6-K, exhibit 99.1 press
             release); it owns the listing facts. (Public on EDGAR; blocks generic
             automated user-agents but is a public filing.)
Establishes: Babylon completed its business combination with Alkuri Global Acquisition
             Corp on 21 October 2021 (shareholder approval 20 October 2021); Class A shares
             and warrants began trading on the NYSE on 22 October 2021 under tickers BBLN
             and BBLN.W.
Locators:    Exhibit 99.1 press release, Babylon Holdings Ltd, CIK 1866390.
Quote:       Founder/CEO Ali Parsa: "We founded Babylon on a fundamental belief, that it is
             possible to make quality healthcare accessible and affordable for every person
             on Earth."
```

```text
URL:         https://tech.eu/2021/06/03/add-one-to-the-spac-pile-londons-babylon-health-announces-4-2-billion-merger-with-alkuri-global-acquisition-corp/
Kind:        secondary. Trade reporting; used only for the deal's headline valuation, which
             the SEC F-4/424B4 registration documents own.
Establishes: The Babylon-Alkuri SPAC merger was announced 3 June 2021 at a $4.2 billion
             valuation. Author Dan Taylor, Tech.eu, 3 June 2021.
Quote:       "Babylon confirms its plan to go public via a $4.2 billion merger with Alkuri
             Global Acquisition Corp."
```

```text
URL:         https://techcrunch.com/2020/02/25/first-do-no-harm/
Kind:        secondary. Reputable reporting (Natasha Lomas, TechCrunch, 25 February 2020)
             reproducing Babylon's press release and the whistleblower's demonstration.
Establishes: David Watkins, an NHS consultant oncologist tweeting as @DrMurphy11,
             demonstrated the symptom checker giving a female profile with classic heart
             attack symptoms a diagnosis of panic attack or depression while giving the
             same symptoms in a male profile a possible heart attack. Babylon's response
             attacked him rather than the cases.
Locators:    Article body.
Quote:       Watkins: "Classic #HeartAttack symptoms in a FEMALE, results in a diagnosis of
             #PanicAttack or #Depression. The Chatbot ONLY suggests the possibility of a
             #HeartAttack in MEN!"
             Babylon press release: "our AI has been used millions of times, and not one
             single patient has reported any harm"; it described his work as "Twitter troll
             tests" and called him a "troll," and said his cases were "theoretical data
             (forming part of an accuracy test and experiment) rather than a genuine health
             concern from a patient."
```

```text
URL:         https://techcrunch.com/2021/03/05/uks-mhra-says-it-has-concerns-about-babylon-health-and-flags-legal-gap-around-triage-chatbots/
Kind:        secondary. Reputable reporting (Natasha Lomas, TechCrunch, 5 March 2021)
             reproducing the MHRA's letter to Watkins and Babylon's response.
Establishes: In May 2018 the MHRA had independently notified Babylon of two chatbot safety
             incidents (one missed heart attack, one missed DVT). On 4 December 2020 the
             MHRA wrote to Watkins conceding his concerns and flagging a regulatory gap
             around triage software.
Locators:    Article body.
Quote:       MHRA letter (4 Dec 2020): "Your concerns are all valid and ones that we share";
             "You have raised a complex set of issues and there are several aspects that
             fall outside of our existing remit."
             Babylon response: the letter's issues "relate to the regulation of 'symptom
             checkers' ... a very small part of Babylon's activities," and Babylon had "not
             received any notification by the MHRA of any regulatory action."
```

```text
URL:         https://undark.org/2019/12/09/babylon-health-artificial-intelligence-medical-advice/
             (read via authorized reprint: https://www.salon.com/2019/12/14/medical-advice-from-a-bot-the-unproven-promise-of-babylon-health_partner/)
Kind:        secondary. Investigative reporting (Jeremy Hsu, Undark, 9 December 2019;
             reprinted by Salon 14 December 2019).
Establishes: In a 2017 WIRED UK test, Fraser and Wong found Babylon's checker "performed
             worst in identifying common illnesses, including asthma and shingles." A
             September 2019 demonstration by Watkins showed the gender-split chest-pain
             result. Babylon defended the 2018 study rather than retracting it.
Locators:    Article body.
Quote:       Babylon on the 2018 study: "Some media outlets may have misinterpreted what
             was claimed but we stand by our original science and results."
```

```text
URL:         https://medcitynews.com/2020/02/babylon-physician-tussle-over-triage-chatbots-safety/
Kind:        secondary. Reputable reporting (Elise Reuter, MedCity News, 26 February 2020)
             reproducing the RCGP's rejection, another documented case, and Babylon's
             clinical-director defense. (Live page; blocks generic automated user-agents.)
Establishes: The Royal College of General Practitioners rejected Babylon's exam claim.
             Watkins showed a fictitious 67-year-old smoker with central chest pain being
             offered "gastritis or a sickle cell crisis." Babylon acknowledged correcting
             a bounded number of errors.
Locators:    Article body.
Quote:       RCGP: it "dismissed the company's claims as dubious, saying the exam prep
             materials the company used to test its algorithm didn't represent the full
             range of the test."
             Babylon: of the ~100 cases Watkins raised, "a panel of clinicians investigated
             them, correcting 20 errors in the company's AI"; the company "did not confirm
             which errors it had fixed."
             Clinical director Keith Grimes: "it's not giving out fake or false information.
             It's giving out safe information to patients to allow them to seek help in the
             right timing."
```

```text
URL:         https://techcrunch.com/2023/08/31/the-fall-of-babylon-failed-tele-health-startup-once-valued-at-nearly-2b-goes-bankrupt-and-sold-for-parts/
Kind:        secondary. Reputable reporting (Ingrid Lunden, TechCrunch, 31 August 2023) on
             the collapse; the underlying Chapter 7 petitions are court filings in Delaware.
Establishes: Babylon's US shares fell to a market capitalisation "just over $5,000"; the US
             operation became insolvent in August 2023; the UK subsidiary formally went into
             administration on 31 August 2023; UK assets were sold to eMed Healthcare UK,
             serving "some 700,000 people in the U.K." A 2019 round had valued Babylon at
             "nearly $2 billion."
Locators:    Article body.
Quote:       US-listed shares became "virtually worthless, with a market cap of just over
             $5,000."
```

## Contradictions

- What was claimed vs what the study says. Babylon publicised that its AI matched or beat
  doctors and passed the RCGP exam (MedCity: it "claimed its algorithm performed better
  than doctors on the Royal College of General Practitioners' official exam"). The study
  itself claims only accuracy "comparable to" doctors and triage "safer on average," and
  states its results "cannot be directly interpreted with respect to real-world accuracy
  and safety." Babylon's marketing outran its own paper. The paper also explicitly denies
  the exam scores demonstrate an ability to pass the MRCGP in full.
- Diagnostic accuracy, head to head. On the one external benchmark run against both the
  system and doctors (30 Semigran vignettes), doctors led on the top diagnosis (75.3% vs
  70.0%) while the system led on top-3 (96.7% vs 90.3%). On the main 100-vignette set the
  averages are close (recall 83.9% doctors vs 80.0% system), but Coiera shows the averages
  are fragile: removing the weakest doctor (Doctor B, recall 64.1%) flips Table 1 so
  humans beat the system on every measure. The study did no significance testing.
- Triage safety. The study reports the system safer than doctors against the judge's range
  (97.0% vs 93.1%). But against the stricter of the in-house GPs (GP-2) the system scored
  81.0% safety (Table 3), and documented real cases (a missed heart attack in a female
  profile, a missed DVT, chest pain routed to gastritis/sickle cell) show under-triage the
  vignette test did not surface. The MHRA logged two such incidents in May 2018.
- Whether the failures are real. Watkins and the MHRA treat the cases as valid safety
  concerns ("ones that we share"). Babylon calls them "theoretical data" and "troll tests,"
  says "not one single patient has reported any harm," and puts the number of genuine
  errors at 20 out of ~100 cases raised. The "no reported harm" figure is uncontrolled and
  self-reported, not a measured safety rate.

## Numbers

```text
Figure: 100 clinical vignettes
Owner:  Razzaki et al. 2018 (arXiv:1806.10698), Methods
Scope:  Test cases in the main study; each modelled one condition, patient aged >=16.

Figure: 7 doctors (Doctors A-G), locum GPs
Owner:  Razzaki et al. 2018, Table 1 / Methods
Scope:  Human comparators in the main study; each saw a subset (average 56.6 vignettes),
        not all 100. (Coiera's review refers to "6 doctors"; the paper's tables list seven.)

Figure: Babylon AI diagnostic recall 80.0%, precision 44.4%, F1 57.1% (n=100)
Owner:  Razzaki et al. 2018, Table 1
Scope:  Against the single disease modelled by each vignette.

Figure: Doctor-average recall 83.9% (range 64.1-93.8%), precision 43.6%, F1 57.0%
Owner:  Razzaki et al. 2018, Table 1
Scope:  Seven doctors, average 56.6 vignettes each.

Figure: Triage safety - Babylon AI 97.0% vs doctor average 93.1%; appropriateness 90.0%
        vs 90.5%
Owner:  Razzaki et al. 2018, Table 2
Scope:  Against one independent judge's range of acceptable triage; "safe" = equal or
        greater urgency than the judge's minimum.

Figure: Triage safety vs three in-house GPs - Babylon AI 90.0% / 81.0% / 90.0%
        (GP-1 / GP-2 / GP-3)
Owner:  Razzaki et al. 2018, Table 3
Scope:  Same cases scored against each GP's own acceptable range; GP-2 was the strictest.

Figure: Semigran-2015 benchmark (30 vignettes) - Babylon top-1 70.0% (21/30), top-3
        96.7% (29/30); doctors top-1 75.3%, top-3 90.3%
Owner:  Razzaki et al. 2018, section 5.4.1
Scope:  External vignette set; paediatric, dermatological and tetanus cases excluded.

Figure: MRCGP AKT 86.7% (13/15 top-3); MRCGP CSA 75.0% (27/36 top-3)
Owner:  Razzaki et al. 2018, sections 5.4.2-5.4.3
Scope:  Diagnostic component only, limited question sets; not the full MRCGP exam.

Figure: "above 72%" (MRCGP five-year average pass mark) as the bar the diagnostic
        component cleared
Owner:  Razzaki et al. 2018, Discussion (citing RCGP)
Scope:  The paper's own comparison; the single "81%" pass figure is Babylon's marketing
        composite, not stated in the paper (see Limits).

Figure: Two safety incidents (one missed heart attack, one missed DVT)
Owner:  MHRA, via TechCrunch (5 Mar 2021)
Scope:  Incidents the MHRA notified Babylon of, May 2018.

Figure: $4.2 billion SPAC valuation (Alkuri Global merger, announced 3 June 2021)
Owner:  Babylon Holdings SEC registration; figure via Tech.eu (3 Jun 2021)
Scope:  Implied post-combination equity value; NYSE ticker BBLN from 22 Oct 2021.

Figure: ~$2 billion (2019 private valuation); market cap "just over $5,000" by Aug 2023
Owner:  TechCrunch (31 Aug 2023)
Scope:  Peak private valuation vs collapsed US-listed value at wind-down.

Figure: UK assets sold to eMed Healthcare UK, serving ~700,000 UK patients; UK subsidiary
        into administration 31 Aug 2023
Owner:  TechCrunch (31 Aug 2023)
Scope:  UK business at collapse. (Chapter 7 petitions for the US entities were filed in
        Delaware in August 2023; the filing dates come from reporting, not a filing I read.)
```

## Limits

- No rate of real-world under-triage can be given. The safety failures are known through
  Watkins's own demonstrations and journalism that reproduced them (tweets and videos),
  the MHRA's count of two logged incidents, and the Field Safety Notice, none of which
  supplies a denominator over real usage. Babylon's "millions of uses, no reported harm"
  is uncontrolled and self-reported. The writer can show that specific serious
  presentations were reproducibly mis-triaged; the writer cannot state how often.
- The Lancet correspondence full text is paywalled and bot-gated. I confirmed the citation
  (authors, journal, volume 392, issue 10161, pp. 2263-2264, DOI) through the Crossref
  record, and its central objection through Coiera's own contemporaneous review (which I
  read in full) and multiple reputable reproductions of the same sentence. I did not read
  the correspondence's own page directly.
- The "81%" MRCGP figure that circulated in coverage is Babylon's marketing composite. The
  study reports component scores (86.7% AKT top-3, 75.0% CSA top-3, and the "above 72%"
  comparison), not a single 81%. Treat 81% as a publicised figure, not a study result.
- The Chapter 7 filing dates and the specific liabilities range ($100M-$500M) come from
  reporting of the Delaware petitions, not from a court document I opened. The valuation
  trajectory ($4.2B SPAC, ~$2B private, ~$5,000 market cap) is solid across reporting and
  the SEC filing but the $4.2B figure itself is cited from trade reporting, not extracted
  from the registration statement.
- I did not confirm the name of the RCGP official who voiced the caution from a document I
  opened. MedCity News attributes the rejection to "the college" without naming a person;
  a chair's name appeared only in search summaries, so it is not recorded here.
- Everything the commission asked for is otherwise established: the study and its design,
  the clinical critique, documented under-triage cases with dates, regulator involvement,
  Babylon's defenses in its own words, and the collapse.

## Source assets

```text
Asset: Table 1, Razzaki et al. 2018 (p.4) - recall, precision and F1 for each of the seven
       doctors and the Babylon AI against the vignette-modelled disease.
Shows: The head-to-head diagnostic numbers the "comparable to doctors" claim rests on, and
       how close and how variable they are (Doctor B's 64.1% recall against Babylon's 80.0%).
Crop:  Keep the Doctor A-G rows, the Doctor Average row and the Babylon AI row with the
       column headers and the Number-of-Vignettes column. Do not drop the vignette-count
       column: it shows doctors saw far fewer cases each than the system's 100.

Asset: Table 2, Razzaki et al. 2018 (p.6) - triage safety and appropriateness per doctor
       and for Babylon AI against the judge's acceptable range.
Shows: The 97.0% vs 93.1% safety claim in full, with the appropriateness trade-off
       (90.0% vs 90.5%) beside it.
Crop:  Retain the Safety and Appropriateness columns and the Babylon AI and Doctor Average
       rows; the per-doctor rows give the spread.

Asset: Figure 1, Razzaki et al. 2018 (p.5) - recall-vs-precision plot for the doctors and
       the Babylon AI at different thresholds.
Shows: Where the system sits relative to individual doctors, and that tuning moves the
       system's operating point toward different doctors.
Crop:  Keep both axes labelled (Average Recall, precision) and the Babylon AI series
       distinguishable from the doctor points.

Asset: The gender-split chest-pain demonstration (@DrMurphy11 / Watkins), described in
       TechCrunch (25 Feb 2020) and Undark (9 Dec 2019); the original is Watkins's own
       tweet/video.
Shows: The clearest single illustration of under-triage: identical serious symptoms routed
       to A&E for a male profile and to a panic-attack/GP outcome for a female profile.
Crop:  If the original tweet or video frames are used, retain both the male and female
       results side by side so the divergence is visible; retain the symptom entry. Record
       it as a demonstration reproduced by named reporting, not as a Babylon document.
```

## Discarded

```text
URL: https://www.digitalhealth.net/2018/07/babylon-ai-abilities-on-par-human-doctors/ - Cloudflare-blocked (403) to every request; live for a human browser but I could not open it, and its content (RCP event, Babylon PR wording) is covered by sources I did read (MedCity, the study). Gated, not cited.
URL: https://pubmed.ncbi.nlm.nih.gov/... - reCAPTCHA wall; citation confirmed via Crossref instead.
URL: https://qz.com/1766418/how-using-babylon-healths-ai-symptom-checker-could-go-wrong - 403 to every request; its material (Watkins's title, cases) is covered by TechCrunch and MedCity, which I did open.
URL: https://www.mobihealthnews.com/news/emea/researchers-question-babylon-claims-its-system-beat-doctors-rcgp-exam - 403; RCGP rejection covered by MedCity instead.
URL: https://theweek.com/health/babylon-health-the-failed-ai-wonder-app-that-dazzled-politicians - body truncated to navigation only; no citable text extracted.
URL: https://www.frontiersin.org/journals/artificial-intelligence/articles/10.3389/frai.2020.543405/full - the 2020 journal version; I cited the 2018 preprint that Babylon's original claim rested on, to match the incident's timeline.
```
