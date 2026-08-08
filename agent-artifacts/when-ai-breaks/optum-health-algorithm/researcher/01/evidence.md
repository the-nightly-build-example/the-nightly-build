# Evidence record: when-ai-breaks/optum-health-algorithm (01)

The evidence firmly supports every load-bearing claim in the commission. The
Obermeyer et al. Science paper was read in full (author-hosted PDF), and every
headline figure the brief asks for is confirmed against the paper that owns it:
the ~49,618-patient analytic sample, the 4.8-vs-3.8 chronic-condition gap at the
97th percentile (26.3% more), the simulated 17.7%→46.5% jump in the Black share
of the auto-enrolled group, the ~200-million-people scale of the tool class, the
explicit exclusion of race as a feature, and the mechanism (the label is total
medical cost, so a health-need prediction is really a cost prediction). The
aftermath is anchored on a primary regulator document (the NY DFS/DoH joint
letter, read firsthand) and a primary vendor statement (via press). "Where it
lives now" rests on the authors' 2021 Algorithmic Bias Playbook and the paper's
own enumerated analogues. The record is thin in three honest places, all noted
below: (1) two of the most-repeated numbers are the *manufacturer's* replication
figure (48,772 excess conditions on 3.7M patients) and a *simulated*
counterfactual (17.7→46.5%), not observed real-world outcomes; (2) the paper
deliberately never names the vendor — "Optum / Impact Pro" comes from journalists
and regulators, a detail most retellings blur; (3) the vendor's own statement,
though primary in content, was read through secondary reporting. None of this
undermines the commissioned angle; it sharpens it.

## Sources

```text
URL:         https://sendhil.org/wp-content/uploads/2020/01/Publication-67.pdf
Kind:        primary — the study itself, authored by Obermeyer, Powers, Vogeli,
             Mullainathan; hosted on co-author Sendhil Mullainathan's own site
             (paper's own page: https://sendhil.org/dissecting-racial-bias-in-an-algorithm-used-to-manage-the-health-of-populations/).
             Science.org (https://www.science.org/doi/10.1126/science.aax2342) is
             gated (HTTP 403); the author copy is the full published article.
Establishes: The entire quantitative core — sample, risk-score health gap,
             counterfactual enrollment share, cost-as-label mechanism, race
             excluded, manufacturer replication and 84% fix.
Paraphrase:  Working with one large academic hospital, the authors studied all
             primary-care patients in risk-based contracts, 2013–2015. A widely
             used commercial risk-prediction algorithm scored patients to target
             a "high-risk care management" program; at any given score Black
             patients were substantially sicker than White patients. The bias
             arose because the algorithm's training label was next-year health-
             care cost, and less is spent on Black patients at equal need, so
             cost understated their illness. Race was not a feature. Retraining
             on a health-inclusive label cut the bias by 84%.
Locators:    Abstract; "Data and analytic strategy" (p.1–2, Table 1); "Health
             disparities conditional on risk score" (p.2–3, Fig.1); "Mechanism of
             bias" (p.3–4, Fig.3); "Problem formulation" / "Experiments on label
             choice" (p.5, Table 2); "Relation to human judgment" (p.6, Table 3);
             "Discussion" (p.7); competing-interests and data-availability notes
             (p.7); Editor's Summary "Racial bias in health algorithms" (p.8).
Quote:       "Notably, the algorithm specifically excludes race." / "the
             algorithm takes total medical expenditures ... in year t as the
             label. Thus, the algorithm's prediction on health needs is, in fact,
             a prediction on health costs." / "Remedying this disparity would
             increase the percentage of Black patients receiving additional help
             from 17.7 to 46.5%."
```

```text
URL:         https://www.dfs.ny.gov/reports-and-publications/comment-letters/dfs-doh-joint-letter-uhgi-20191025
Kind:        primary — the New York regulators' own joint letter (the document,
             not reporting on it). Read firsthand.
Establishes: The regulatory aftermath and the public naming of the vendor and
             product; the legal characterization under New York law.
Paraphrase:  On 25 October 2019 the NY Department of Financial Services and
             Department of Health jointly wrote to UnitedHealth Group's CEO,
             naming Optum's "Impact Pro," calling the racially disparate results
             unlawful in New York, and demanding the company either prove the
             algorithm is not discriminatory or stop using it.
Locators:    Full letter; addressee block; signature block; demand paragraph.
Quote:       "These discriminatory results, whether intentional or not, are
             unacceptable and are unlawful in New York." / "We call on you to
             immediately investigate these reports and demonstrate that this
             algorithm is not racially discriminatory or to cease using Impact
             Pro (or any other data analytics program) if you cannot demonstrate
             that it does not rely on racial biases or perpetuate racially
             disparate impacts."
```

```text
URL:         https://gitlab.com/labsysmed/dissecting-bias
Kind:        primary — the authors' own reproduction repository (README read via
             https://gitlab.com/labsysmed/dissecting-bias/-/raw/master/README.md).
Establishes: That the authors released a synthetic dataset (R package synthpop)
             plus R/Python code to reproduce the analysis, and that even here the
             manufacturer is never named ("our health system partner").
Paraphrase:  Provides synthetic master data, replication code, and the authors'
             own replicated results; contacts listed as Zoey (Zad) Li, Katie Lin,
             Ziad Obermeyer. Does not name the vendor anywhere.
Locators:    README.md (repo root); referenced in the paper's data-availability
             statement.
Quote:       (paper's data-availability note) "we provide instead a synthetic
             dataset ... and all code necessary to reproduce our analyses at
             https://gitlab.com/labsysmed/dissecting-bias."
```

```text
URL:         https://www.govtech.com/health/NY-Regulators-Probe-for-Racial-Bias-in-Health-Care-Algorithm.html
Kind:        secondary — Government Technology, reporting the DFS/DoH letter and
             the UnitedHealth response. Read firsthand.
Establishes: Confirms the letter's date, signatories, addressee, and product
             name; carries UnitedHealth's defense of the tool. Corroborates the
             primary DFS letter and relays the vendor statement.
Paraphrase:  Reports the 25 Oct 2019 letter from Superintendent Linda Lacewell
             (DFS) and Commissioner Howard Zucker (DoH) to CEO David Wichmann,
             names Optum/Impact Pro, and relays UnitedHealth's position that the
             tool was validated as "highly predictive of cost, which is what it
             was designed to do" and draws on 600+ clinical measures.
Locators:    Body paragraphs quoting the letter and the company.
Quote:       UnitedHealth: Impact Pro "was highly predictive of cost, which is
             what it was designed to do."
```

```text
URL:         https://www.sciencenews.org/article/bias-common-health-care-algorithm-hurts-black-patients
Kind:        secondary — Science News (AAAS), contemporaneous reporting. Read
             firsthand.
Establishes: That the vendor was identified as Optum/Impact Pro by journalists
             (the paper withheld it); the manufacturer's ~3.7M-patient
             replication; that the top-10 marketed algorithms use past cost as a
             predictor. Also relays Optum's statement.
Paraphrase:  Reports Obermeyer's team partnering with Optum, maker of Impact Pro,
             to fix the tool; notes the paper declined to name the hospital and
             that "the top 10 health care algorithms on the market" use past
             costs; carries Optum's statement on continual review and adding
             socioeconomic data.
Locators:    Body; vendor-response paragraph.
Quote:       Optum: "Predictive algorithms that power these tools should be
             continually reviewed and refined, and supplemented by information
             such as socio-economic data, to help clinicians make the best
             informed care decisions for each patient."
```

```text
URL:         https://www.ftc.gov/system/files/documents/public_events/1582978/algorithmic-bias-playbook.pdf
Kind:        primary — the authors' 2021 follow-up, "Algorithmic Bias Playbook"
             (Obermeyer, Nissan, Stern, Eaneff, Bembeneck, Mullainathan; Center
             for Applied AI, Chicago Booth), hosted by the FTC. Authorship, year,
             and framing confirmed; full body text could not be extracted (PDF
             would not decode via fetch — a transport failure, not a dead link;
             the URL resolves and downloads a 479 KB PDF).
Establishes: That cost/label-choice proxy bias is not a one-off but a general,
             still-deployed failure across live health algorithms — the present-
             day "where it lives now" anchor from a primary.
Paraphrase:  A guide by the Science paper's team for measuring and mitigating
             bias in live algorithms, built on their finding that convenient
             proxy labels reproduce structural bias; frames biased algorithms as
             deployed throughout the health-care system.
Locators:    Cover (authors/date); framing sections. Corroborated by the authors'
             university notice below.
Quote:       (per Berkeley Public Health, below) biased algorithms are "deployed
             throughout the health care system, influencing clinical care,
             operational workflows, and policy."
```

```text
URL:         https://publichealth.berkeley.edu/articles/spotlight/research/ziad-obermeyer-and-colleagues-at-the-booth-school-of-business-release-health-care-algorithmic-bias-playbook
Kind:        secondary — UC Berkeley School of Public Health notice (the lead
             author's own institution) reporting the Playbook's release. Read
             firsthand.
Establishes: Playbook authorship and 23 June 2021 date; that the bias is framed
             as widespread and present-day.
Paraphrase:  Reports Obermeyer and Chicago Booth colleagues releasing the
             Algorithmic Bias Playbook, describing biased algorithms as deployed
             throughout the health-care system and offering a four-step audit.
Locators:    Article body.
Quote:       "biased algorithms are deployed throughout the health care system,
             influencing clinical care, operational workflows, and policy."
```

```text
URL:         https://www.soa.org/resources/research-reports/2016/2016-accuracy-claims-based-risk-scoring-models/
Kind:        primary — Society of Actuaries report "Accuracy of Claims-Based Risk
             Scoring Models" (Hileman & Steele, 2016), the paper's reference (21)
             for the industry-wide cost-label practice. Landing page read; used
             as corroboration, not for new numbers.
Establishes: That the most predictive commercial risk-scoring models use prior
             cost to predict future cost, and that cost prediction was the
             accuracy metric across the widely used tools — the industry norm the
             paper's mechanism claim rests on.
Paraphrase:  A comparative evaluation of the leading claims-based risk-scoring
             models; the most accurate use prior cost as the predictor, and the
             study's accuracy metric is cost prediction.
Locators:    SOA report landing page / abstract; paper reference 21.
Quote:       (paper, p.5) "the Society of Actuaries's comprehensive evaluation of
             the 10 most widely used algorithms, including the particular
             algorithm we study, used cost prediction as its accuracy metric."
```

## Contradictions

- **Vendor framing vs. the finding.** UnitedHealth/Optum's response — that Impact
  Pro "was highly predictive of cost, which is what it was designed to do" — does
  not dispute the paper; it restates the paper's own mechanism. The disagreement
  is about what the tool *should* predict, not about whether cost-as-label
  produced the racial gap. The manufacturer then independently replicated the
  result on 3,695,943 patients and confirmed it (paper, p.7). So the closest thing
  to a counter-narrative actually corroborates the core claim.
- **Simulated vs. observed.** The signature 17.7%→46.5% figure is a *simulated*
  counterfactual: at each risk threshold the authors swap healthier White patients
  above the line for sicker Black patients below it until the marginal patient is
  equally sick (paper, Fig.1B, p.3). It is not a measured before/after of real
  enrollment. Real observed program enrollment was 19.2% Black (Table 3). A writer
  must not report 17.7→46.5 as an achieved change.
- **Which dataset owns "~50,000 more conditions."** The widely quoted "almost
  50,000 more chronic conditions" is 48,772, from the *manufacturer's* replication
  on 3.7M commercially insured patients (paper, p.7), not from the ~49,618-patient
  academic-hospital sample. Several retellings misattribute it to the study sample.
- No source contradicts the sample denominators, the 4.8-vs-3.8 gap, the race
  exclusion, or the cost-label mechanism.

## Numbers

```text
Figure: 49,618 patients in the main sample (6,079 Black + 43,539 White)
Owner:  Obermeyer et al. 2019, Table 1 and p.2
Scope:  Primary-care patients in risk-based contracts at one large academic
        hospital, 2013–2015; observed over 100,009 patient-years (11,929 Black +
        88,080 White). 71.2% commercially insured, 28.8% Medicare; mean age 50.9;
        63% female. ("~50,000" in popular summaries.)
```

```text
Figure: ~200 million people per year
Owner:  Obermeyer et al. 2019, p.1 (citing industry estimates)
Scope:  The whole class of commercial risk-prediction tools applied across the US
        each year — NOT the number affected by this one algorithm. This algorithm
        is described as "affecting millions of patients" (abstract).
```

```text
Figure: 4.8 vs 3.8 active chronic conditions at the 97th percentile = 26.3% more
Owner:  Obermeyer et al. 2019, p.2 (P < 0.001)
Scope:  Black vs White patients at the same algorithm risk score, at the auto-
        enrollment threshold (97th percentile). Comorbidity/"active chronic
        conditions" score.
```

```text
Figure: Black share of auto-identified group: 17.7% → 46.5%
Owner:  Obermeyer et al. 2019, abstract and Fig.1B (p.3)
Scope:  Simulated counterfactual at the 97th-percentile threshold, removing the
        health-vs-score gap. Not observed enrollment.
```

```text
Figure: Race excluded from the feature set
Owner:  Obermeyer et al. 2019, p.3 ("the algorithm specifically excludes race")
Scope:  The deployed algorithm and the authors' three experimental relabeled
        algorithms all exclude race; bias arises with no protected attribute as
        input.
```

```text
Figure: Cost wedge of $1,801 (or $1,144) per year
Owner:  Obermeyer et al. 2019, p.4
Scope:  At equal health, Black patients generate $1,801 less/year holding the
        number of chronic illnesses constant, or $1,144 less holding the specific
        illnesses constant. This wedge is why cost mispredicts need by race.
```

```text
Figure: Cost calibration (why cost looks "unbiased")
Owner:  Obermeyer et al. 2019, p.3
Scope:  At the median risk score, realized costs were $5,147 (Black) vs $4,995
        (White); in the top 5% of risk, $35,541 (Black) vs $34,059 (White). Cost
        is well-calibrated across race even as health is not.
```

```text
Figure: Label choice swings Black share 14.1% → 26.7%
Owner:  Obermeyer et al. 2019, Table 2 (p.6)
Scope:  Fraction Black in the highest-risk group when the training label is total
        cost (14.1%) vs number of active chronic conditions (26.7%) — nearly a
        twofold shift from label choice alone.
```

```text
Figure: Manufacturer replication — 48,772 excess conditions; 84% reduction
Owner:  Obermeyer et al. 2019, p.7
Scope:  Manufacturer's own replication on 3,695,943 commercially insured patients:
        Black patients had 48,772 more active chronic conditions than White at a
        given risk score. A health-plus-cost index label cut excess conditions to
        7,758, an 84% reduction in bias.
```

## Source assets

```text
Asset: Figure 1B — "Fraction of Black patients at or above a given risk score,"
       original vs simulated curves, p.3 of the paper.
Shows: The counterfactual jump. The "original" line sits near 0.18 at the 97th-
       percentile auto-enroll line (black dashed) while the "simulated" line rises
       to ~0.465 — the 17.7%→46.5% claim made visible in one panel.
Crop:  Must retain both curves, the y-axis (Fraction Black) with values through
       ~0.50, and the 97th-percentile (auto-identify) dashed line so the endpoint
       reads correctly. Must retain the "original"/"simulated" legend so the
       reader does not mistake the simulated curve for observed enrollment. May
       omit the 55th-percentile screening line.
```

```text
Asset: Figure 1A — "Number of active chronic conditions vs algorithm risk score,
       by race," p.2–3.
Shows: The health gap at equal score: the Black curve sits above the White curve
       across the whole risk distribution, widening at the high-risk end (4.8 vs
       3.8 conditions at the 97th percentile).
Crop:  Must retain both race curves, the y-axis (number of chronic conditions),
       and at least the 97th-percentile line so the 4.8-vs-3.8 reading is anchored.
```

```text
Asset: Figure 3B — "Total medical expenditure vs number of chronic conditions, by
       race," p.5 (log y-axis).
Shows: The mechanism's root: at the same illness burden, the Black cost curve sits
       below the White curve — cost understates need for Black patients, so a cost
       label mislabels them. This is the single clearest picture of the proxy gap.
Crop:  Must retain both race curves and the log-scale y-axis label (Mean Total
       Medical Expenditure); note the log scale in any caption. Omitting either
       curve destroys the comparison.
```

```text
Asset: Table 3 — "Doctors' decisions versus algorithmic predictions," p.6.
Shows: Observed enrollment was 19.2% Black; relabeling to worst-predicted health
       would reach 29.2%. Useful to keep the simulated counterfactual honest next
       to a real observed number, or as a small stat strip instead of the figure.
Crop:  If rendered as a stat strip, retain the "Observed program enrollment"
       (0.192) and "Worst predicted health" (0.292) rows and the Fraction-Black
       column header.
```

## Discarded

```text
URL: https://www.science.org/doi/10.1126/science.aax2342 — gated (HTTP 403); the
     full text lives in the author-hosted PDF used above. Recorded as the paper's
     canonical DOI page but not the transport read.
URL: https://www.ruhabenjamin.com/blog/2019/10/25/assessing-risk-automating-racism
     and https://www.science.org/doi/10.1126/science.aaz3873 — Ruha Benjamin's
     companion Perspective, "Assessing risk, automating racism" (Science 366,
     421–422; Benjamin is Professor, Dept. of African American Studies, Princeton).
     Her blog page carries only a cover image and a download link, and the Science
     page is gated; full text not read, so not cited as evidence. Available if the
     writer wants a named expert framing and the citation can be verified.
URL: https://www.fiercehealthcare.com/payer/new-york-to-probe-algorithm-used-by-optum-for-racial-bias
     — HTTP 403; the same facts are held by the primary DFS letter and the govtech
     report already recorded.
URL: https://www.chicagobooth.edu/research/center-for-applied-artificial-intelligence/research/algorithmic-bias/playbook
     — Playbook landing page is form-gated; content confirmed via the FTC-hosted
     PDF URL and the Berkeley notice instead.
```

## Notes for the writer and editor (what retellings get wrong)

1. **The paper never names the vendor.** Obermeyer et al. studied a deidentified
   algorithm and stressed they had "no contact with the algorithm's manufacturer
   until after [the analysis] was complete" (p.7). "Optum / Impact Pro" was
   supplied by journalists (Wall Street Journal, 25 Oct 2019) and confirmed by the
   NY DFS/DoH letter — not by the study. A lesson that says "the paper studied
   Optum's Impact Pro" is wrong; the paper studied an unnamed tool later
   identified as Impact Pro.
2. **17.7→46.5% is a simulation, not an outcome** (see Contradictions).
3. **~200 million is the scale of the tool class per year, not victims of this
   tool** (see Numbers). This algorithm affected "millions"; the manufacturer's
   replication covered ~3.7M.
4. **48,772 (~"50,000 more conditions") is the manufacturer's 3.7M replication
   figure**, not the study-sample figure (whose equivalent is 4.8 vs 3.8 at the
   97th percentile).
5. **Bias without race as a feature** is the transferable point: race was
   explicitly excluded, yet a cost label reproduced the disparity because cost is
   correlated with race through unequal access. This is the paper's "label choice
   bias" / proxy-failure framing, and it is exactly the commissioned mechanism.

**Verdict on the angle:** The evidence supports the commissioned angle without
qualification. The three caveats (unnamed vendor, simulated counterfactual,
replication-vs-sample provenance) are precision corrections a careful lesson must
honor, not contradictions of the thesis.
