# evidence: when-ai-breaks/apple-card (01)

The evidence supports the commissioned angle closely and does not undermine it.
The spine, the March 2021 NY DFS *Report on Apple Card Investigation*, was read
in full (18 pages) and is unambiguous: after reviewing several thousand pages of
records and running regression analysis on underwriting data for nearly 400,000
New York applicants, DFS found no evidence of either deliberate (disparate
treatment) or disparate-impact discrimination, found the model did not use
gender or marital status as an input, yet documented real transparency and
customer-service failures. Both halves are firsthand in the report. The trigger
artifacts (David Heinemeier Hansson's and Steve Wozniak's November 2019 posts)
are the record's thinnest spot: the original tweets are now gated behind X's
login wall (HTTP 451), so their verbatim wording rests on cross-reproduction and
on the DFS report's own paraphrase, though the affected party's own published
account (Jamie Heinemeier Hansson, hosted on dhh.dk) was reached directly and is
primary. The mechanism (a model producing a disparate outcome through correlated
proxies without using the protected attribute) and the proof problem are
established by an expert critique of the DFS report and by the DFS report's own
section on how credit variables carry historical bias. The single most important
limitation: the public DFS report states its regression "did not bear out"
violations but does not show the proxy analysis, and a credentialed critic argues
DFS's method (comparing men and women with *similar credit characteristics*)
cannot by construction detect discrimination that operates *through* those
characteristics. So "no violation found" is faithful; "proven non-discriminatory"
is not, and the report itself says as much.

## Sources

```text
URL:         https://www.dfs.ny.gov/reports_and_publications/202103_report_apple_card_investigation
             (direct PDF: https://www.dfs.ny.gov/system/files/documents/2021/03/rpt_202103_apple_card_investigation.pdf)
Kind:        primary. The regulator's own investigation report; DFS owns the findings and the data analysis. This is the spine.
Establishes: Scope, method, and the load-bearing findings on both what was and was not found.
Paraphrase:  DFS investigated whether Goldman Sachs Bank USA unlawfully discriminated against women in Apple Card
             underwriting. It reviewed several thousand pages of records and written responses from the Bank and Apple,
             interviewed witnesses and complaining applicants, and analyzed underwriting data. Its Consumer Examinations
             Unit ran regression analysis on underwriting data for nearly 400,000 New York applicants covering launch
             through the initial complaints. Finding: no evidence of deliberate (disparate treatment) discrimination and
             no evidence of disparate-impact fair-lending violations; women and men with equivalent credit
             characteristics had similar outcomes. The Bank had a fair-lending program ensuring the model did not
             consider prohibited characteristics and would not produce disparate impacts. For every individual
             complainant, the Bank identified lawful factors (credit score, indebtedness, income, credit utilization,
             missed payments, other credit history) consistent with its credit policy. Separately, DFS documented a lack
             of transparency (the six-month wait to appeal, no explanation of granted terms since law requires
             explanation only on denial) and framed spouses' "shared finances" as a common misconception. It closes
             that its no-violation finding "does not prove otherwise" about systemic credit inequality and calls credit-
             scoring law "in need of strengthening and modernization."
Locators:    Summary (p.1); "did not produce evidence of deliberate or disparate impact discrimination but showed
             deficiencies in customer service and transparency" (p.3, Sec. I/II). Allegations, incl. Nov 7 2019 start and
             20x claim, and the Bank raising both wives' limits within days and dropping the six-month appeal wait
             (pp.4-5, Sec. II.c). Fair Lending Review, disparate treatment vs disparate impact definitions and the CEU
             regression on "nearly 400,000 New York applicants" (pp.5-6, Sec. III.a). Per-complainant lawful factors
             (pp.6-7). Transparency / six-month appeal / "black box" (pp.7-8, Sec. III.b.1). Path to Apple Card, June
             2020, >70,000 enrolled, ~5,000 approved (pp.8-9). Shared-finances misconception (pp.10-11, Sec. III.b.2).
             Historical bias baked into credit scores and "legacy bias" in model-training data (pp.14-16, Sec. IV.b).
             Second-look program, $2,500 max limit, terminated (pp.17-18, Sec. IV.c).
Quote:       "the Department's exhaustive review ... did not produce evidence of deliberate or disparate impact
             discrimination but showed deficiencies in customer service and transparency." (p.3)
             "DFS reviewed the Apple Card policies and practices for evidence of both disparate treatment and disparate
             impact and found that women and men with equivalent credit characteristics had similar Apple Card
             application outcomes." (p.5)
             "the Department found that the Bank had a fair lending program in place for ensuring its lending policy—and
             underlying statistical model—did not consider prohibited characteristics of applicants and would not produce
             disparate impacts." (p.6)
             "The use of credit scoring in its current form and laws and regulations barring discrimination in lending are
             in need of strengthening and modernization to improve access to credit." (p.13)
```

```text
URL:         https://www.dfs.ny.gov/reports_and_publications/press_releases/pr202103231
Kind:        primary. DFS's own press release announcing the report; the regulator's summary statement of its finding.
Establishes: The headline finding and the ~400,000 figure in the regulator's own summary voice, plus the call for
             stronger, modernized fair-lending law.
Paraphrase:  DFS announced the investigation "did not produce evidence of unlawful discrimination against applicants
             under fair lending law," that women and men with similar credit characteristics generally had similar
             outcomes, that complainants' decisions were "explainable, lawful, and consistent with the Bank's credit
             policy," but that "deficiencies in customer service and a perceived lack of transparency undermined consumer
             trust." It notes ECOA is nearly 50 years old and that credit-scoring law needs strengthening; it credits
             Goldman/Apple for later transparency steps and the program to help denied applicants.
Locators:    Full release (single page).
Quote:       "did not produce evidence of unlawful discrimination against applicants under fair lending law."
             "deficiencies in customer service and a perceived lack of transparency undermined consumer trust in fair
             credit decisions."
```

```text
URL:         https://dhh.dk/2019/about-the-apple-card.html
Kind:        primary artifact. The affected applicant's own first-person published account (authored by Jamie Heinemeier
             Hansson, the wife whose limit was disputed), hosted on the family's own domain. Reached directly.
Establishes: The complainant side's firsthand claims: shared finances, her higher/older credit history, no explanation
             given, and the limit raised only after the tweets went viral.
Paraphrase:  Jamie Heinemeier Hansson states she and David share all financial accounts, that her credit score is higher
             than David's and her US credit history longer with no late payments, and that she is independently wealthy.
             She was given no explanation and no way to make her case; customer service attributed the outcome to "the
             algorithm" and to "your credit score." An Apple Card manager, aware of David's tweets, raised her limit to
             match his "without any real explanation." Dated November 11, 2019.
Locators:    Full post.
Quote:       "my very good credit score is higher than David's"; "I was given no explanation. No way to make my case.";
             "the AppleCard manager told me she was aware of David's tweets and that my credit limit would be raised to
             meet his, without any real explanation"; "It's just the algorithm."
```

```text
URL:         https://x.com/dhh/status/1192540900393705474
Kind:        primary artifact — GATED. David Heinemeier Hansson's original tweet. Could NOT be opened: twitter.com
             301-redirects to x.com, which returns HTTP 451 (login wall). Its substance was instead read in the DFS
             report (opened), which paraphrases it, and its verbatim wording is reproduced identically across multiple
             secondary outlets.
Establishes: The precise trigger of the episode and the "black box / 20x" framing. The 20x figure is independently
             confirmed by the DFS report (opened), which records the "Consumer" was "offered a credit limit ... 20 times
             higher than her offer" beginning November 7, 2019.
Paraphrase:  DHH publicly alleged the Apple Card gave him roughly 20 times his wife's credit limit despite joint tax
             returns, a community-property state, and long marriage, and attributed the outcome to an unexplainable
             "black box algorithm" with no working appeal.
Locators:    Tweet thread beginning Nov 7, 2019.
Quote:       (reproduced across outlets, not read on the source itself, so treated as reproduction) "The @AppleCard is
             such a [expletive] sexist program. My wife and I filed joint tax returns, live in a community-property
             state, and have been married for a long time. Yet Apple's black box algorithm thinks I deserve 20x the
             credit limit she does." — DFS report corroborates the 20x and the Nov 7 2019 date firsthand (p.4).
```

```text
URL:         https://futurism.com/the-byte/steve-wozniak-apple-card-discriminated-against-wife
Kind:        secondary. Reporting that reproduces Wozniak's own public statement (his post itself is gated on X).
Establishes: The second, corroborating complaint from Apple co-founder Steve Wozniak, and his own 10x figure. Note the
             10x is Wozniak's claim; the DFS report does not state a Wozniak multiple (it says only "dramatically better"
             terms for the co-founder, p.4), so 10x is a repetition of his claim, not a DFS finding.
Paraphrase:  Wozniak reported the Apple Card gave him 10x the credit limit of his wife, Janet Hill, despite fully shared
             accounts and assets and equal limits on all their other cards including an AmEx Centurion. Nov 10, 2019.
Locators:    Article body; quoted tweet.
Quote:       "We have no separate bank accounts or credit cards or assets of any kind. We both have the same high limits
             on our cards, including our AmEx Centurion card. But 10x on the Apple Card."
```

```text
URL:         https://appleinsider.com/articles/19/11/11/goldman-sachs-denies-claims-of-apple-card-gender-bias
Kind:        secondary reporting that reproduces Goldman Sachs' own public statement (the @gsbanksupport statement is a
             primary artifact of the Bank's position; its original post is not directly reachable, so it is read here via
             reproduction). AppleInsider itself is secondary.
Establishes: The Bank's contemporaneous denial and its claim that gender/marital status are neither used nor known.
Paraphrase:  Goldman Sachs stated that two family members can receive significantly different credit decisions based on
             individual credit factors, and that "in all cases, we have not and will not make decisions based on factors
             like gender." (Elsewhere the Bank's retail-bank leadership stated it does not know an applicant's gender or
             marital status during the Apple Card application process.) November 11, 2019.
Locators:    Article body; quoted Goldman statement.
Quote:       "Based on these factors, it is possible for two family members to receive significantly different credit
             decisions. In all cases, we have not and will not make decisions based on factors like gender."
             (Repetition supports that Goldman made this claim, not that it is independently proven.)
```

```text
URL:         https://www.law.cornell.edu/uscode/text/15/1691
Kind:        primary. The Equal Credit Opportunity Act statutory text (15 U.S.C. 1691), Legal Information Institute.
Establishes: The legal frame: sex and marital status are prohibited bases for any aspect of a credit transaction. This
             is what makes "the model doesn't use gender" a necessary but not sufficient defense, since disparate impact
             is also actionable.
Paraphrase:  It is unlawful for any creditor to discriminate against any applicant, with respect to any aspect of a
             credit transaction, on the basis of race, color, religion, national origin, sex or marital status, or age
             (subject to capacity to contract), or because income derives from public assistance, or because the
             applicant exercised ECOA rights.
Locators:    Sec. 1691(a)(1)-(3).
Quote:       "on the basis of race, color, religion, national origin, sex or marital status, or age (provided the
             applicant has the capacity to contract)."
```

```text
URL:         https://www.consumerfinance.gov/compliance/circulars/circular-2022-03-adverse-action-notification-requirements-in-connection-with-credit-decisions-based-on-complex-algorithms/
Kind:        primary. CFPB's own interpretive circular (2022-03). The regulator owns this interpretation of ECOA.
Establishes: "Where it lives now": a federal regulator holding that black-box complexity is no excuse for failing to
             give applicants the specific reasons for an adverse credit decision. Directly ties the opacity lesson to
             current law.
Paraphrase:  The CFPB stated that creditors using complex algorithms, including machine-learning "black-box" models,
             are not exempt from ECOA/Regulation B's requirement to provide the specific and accurate principal reasons
             for an adverse action; not understanding one's own model is not a defense. Issued May 26, 2022 (published in
             the Federal Register June 14, 2022).
Locators:    Circular body (question-and-response format).
Quote:       "ECOA and Regulation B do not permit creditors to use complex algorithms when doing so means they cannot
             provide the specific and accurate reasons for adverse actions."
             "A creditor cannot justify noncompliance with ECOA and Regulation B's requirements based on the mere fact
             that the technology it employs to evaluate applications is too complicated or opaque to understand."
```

```text
URL:         https://techcrunch.com/2021/08/14/how-the-law-got-it-wrong-with-apple-card/
Kind:        secondary — credentialed expert critique. By Liz O'Sullivan (CEO of Parity, an algorithmic-governance
             company; adviser to S.T.O.P.), citing Patrick Hall of bnh.ai. This is the contradiction-hunt spine: it
             argues the DFS clearance was methodologically weak.
Establishes: Why "no violation found" is not "proven fair," the proxy mechanism, and the individual proof problem.
Paraphrase:  O'Sullivan argues DFS relied on an outdated "flip test" (would a female version of a male applicant be
             treated equally) and did not examine proxy variables, even though model features are known to proxy for
             protected classes (e.g., credit score is tightly correlated with race). Comparing applicants with similar
             credit characteristics can mask discrimination that operates through those very characteristics, and the
             differences on applicants' credit files "do not necessarily translate to true financial responsibility or
             creditworthiness." Without access to demographic data and the model, an individual applicant cannot
             demonstrate the statistical pattern needed to prove algorithmic bias.
Locators:    Article body.
Quote:       "we've known for years now that some model features can act as proxies for protected classes" (paraphrased
             from the piece); "a 1970s version of the flip test" (attributed to Patrick Hall); "these differences on the
             applicants' credit files do not necessarily translate to true financial responsibility or creditworthiness."
```

## Contradictions

- **"Proven bias" framing vs the record.** Much November 2019 coverage and the
  posts themselves called the Apple Card "sexist" and treated gender bias as
  established (DHH's own word was "sexist program"; headlines followed). The DFS
  report governs: it found *no evidence* of a fair-lending violation and found
  gender was not a model input. The honest reading is "accused, investigated, no
  violation found," not "proven discriminatory." The commission already takes
  this stance; the evidence backs it.

- **"No violation" vs "proven fair" — the live tension.** The DFS clearance and
  the O'Sullivan/TechCrunch critique disagree on what the clearance means. DFS
  says its regression "did not bear out" violations and that women and men with
  equivalent credit characteristics had similar outcomes. O'Sullivan argues that
  method cannot detect proxy discrimination and that DFS "failed to mention"
  whether it examined proxies. These are not fully reconcilable on the public
  record: DFS did not publish the proxy analysis, so a reader cannot verify
  whether proxies were tested. What would settle it: the underlying model
  features, the regression specification, and a proxy/mediation analysis — none
  of which is public, and none of which an individual applicant can obtain. This
  is the article's core teaching point and it is well supported.

- **Wozniak's 10x is his claim, not a DFS finding.** DFS records only that the
  co-founder was offered "dramatically better" terms (p.4); the 10x number comes
  from Wozniak's own post via secondary reproduction. DHH's 20x, by contrast, is
  confirmed firsthand by DFS. Keep the two on different evidentiary footings.

- **Goldman: "we don't know your gender."** Goldman's denial (gender/marital
  status not used or known) is consistent with the DFS finding that the model did
  not use prohibited characteristics. But "not a direct input" does not answer
  the disparate-impact / proxy question, which is exactly why ECOA reaches
  facially neutral policies (Source: DFS pp.5-6; ECOA 1691) and why the "we don't
  use gender" line does not by itself clear a lender.

## Numbers

```text
Figure: ~20x — DHH's Apple Card credit limit vs his wife's
Owner:  David Heinemeier Hansson's Nov 7 2019 post; confirmed firsthand by the DFS report ("20 times higher," p.4)
Scope:  Two individuals (one couple), initial Apple Card offers, November 2019
```

```text
Figure: 10x — Steve Wozniak's Apple Card credit limit vs his wife Janet Hill's
Owner:  Steve Wozniak's own statement (via Futurism reproduction). NOT stated in the DFS report.
Scope:  One couple, initial Apple Card offers, November 2019 (his claim)
```

```text
Figure: nearly 400,000 New York applicants analyzed
Owner:  NY DFS report (CEU regression), p.6
Scope:  Apple Card underwriting data, launch (Aug 2019) through the initial discrimination complaints (Nov 2019)
```

```text
Figure: >70,000 enrolled; ~5,000 approved; ~one-third on track to approval — "Path to Apple Card"
Owner:  NY DFS report, pp.8-9
Scope:  The remediation program for declined applicants, introduced June 2020, as of the report (March 2021)
```

```text
Figure: $2,500 maximum credit limit under the "second look" alternative-data program
Owner:  NY DFS report, p.18
Scope:  Applicants with limited/no credit history who opted to share Apple purchase data; program later terminated
```

```text
Figure: 5% of consumers' credit reports contained errors sufficient to raise their cost of borrowing
Owner:  2013 Federal Trade Commission report, cited in NY DFS report, p.14 (fn.8)
Scope:  US consumers; a 2004 State PIRGs study cited alongside found higher error rates
```

```text
Figure: ECOA nearly 50 years old (enacted 1974); prohibited bases include sex and marital status
Owner:  ECOA, 15 U.S.C. 1691(a); DFS press release notes the ~50-year span
Scope:  Federal fair-lending law in force throughout the episode
```

```text
Figure: Underwriting factors DFS confirmed as lawful bases for the complainants' decisions
Owner:  NY DFS report, pp.6-7
Scope:  credit score, indebtedness, income, credit utilization, missed payments, other credit-history elements
```

## Source assets

```text
Asset: "A wider window for approval" screenshot of the Apple Card website, reproduced in the DFS report, p.9
Shows: The categories of data Goldman Sachs draws on to set credit terms — TransUnion bureau data, disposable income
       after monthly debt obligations, utility payment history (telecom/gas/electric), history of paying down debt, and
       the annual income the applicant reports. A concrete, sourced picture of the inputs that stand in for the "black
       box," and the raw material for teaching how neutral-looking inputs can carry proxy effects.
Crop:  Keep the header and all five data-category labels legible; the decorative left panel can be trimmed. Caption must
       credit the DFS report p.9 (Apple's own site snapshot), not present it as the full model.
```

```text
Asset: "Good money habits lead to good credit" screenshot of the Apple Card website, reproduced in the DFS report, p.10
Shows: Goldman/Apple's post-incident guidance on improving approval odds (pay at least the minimum, keep disposable
       income, avoid many applications in a short span, check your report, build history). Useful only as an artifact of
       the transparency remediation, not as evidence about the underwriting itself.
Crop:  Retain the checklist items; omit if space is tight, as it is the weaker of the two.
```

```text
Asset: The DFS report's own statistical finding is NOT visualized — None found.
Shows: The report states the CEU regression "did not bear out violations" but publishes no chart, table, or specification
       of the ~400,000-applicant analysis. There is no owning visual for the central quantitative claim; do not fabricate
       one. This absence is itself the point for the "you can't verify it" section.
Crop:  n/a
```

## Discarded

```text
URL: https://twitter.com/dhh/status/1192540900393705474 / https://x.com/... : original tweet gated (HTTP 451, X login
     wall); not directly openable. Substance retained via the DFS report (opened) and cross-reproduction; recorded above
     as a gated primary, not dropped, but flagged because it is one of the "four primaries hard to reach."
URL: https://www.cnn.com/2019/11/10/business/goldman-sachs-apple-card-discrimination : returned HTTP 451; not opened,
     so not cited. Wozniak's statement was instead sourced from an openable outlet (Futurism).
URL: https://www.cnn.com/2019/11/12/business/apple-card-gender-bias : returned HTTP 451; not opened. The proxy-mechanism
     explanation was instead sourced from the TechCrunch/O'Sullivan critique (opened) and the DFS report's Sec. IV.b.
URL: https://thefinancialbrand.com/...-90253 : returned HTTP 403; not opened, so not cited.
URL: https://www.fastcompany.com/90429224/... (Jamie Heinemeier Hansson's byline) : returned HTTP 403; not opened. Her
     firsthand account was instead read directly at dhh.dk (opened, primary) which carries the same first-person
     material, so nothing is lost.
```

## Primary-reachability flag (per brief)

The brief named four candidate primaries and asked to flag if they are hard to
reach. Status:
- **DFS report** — reachable and read in full (PDF). PRIMARY, solid.
- **ECOA text** — reachable and read (LII). PRIMARY, solid.
- **The two viral posts (DHH, Wozniak)** — HARD TO REACH directly; both gated on
  X (451). DHH's substance and the 20x are corroborated firsthand by the DFS
  report; the affected party's own account (Jamie H. Hansson) was reached
  directly at dhh.dk as a primary substitute; Wozniak's 10x is via secondary
  reproduction (Futurism). Verbatim tweet text should be attributed as reproduced.
- **A Goldman statement** — the Bank's original post is not directly reachable;
  its statement is carried via secondary reproduction (AppleInsider). Treat as a
  primary artifact read through a repetition.

Source policy is met: 9 distinct sources recorded; 6 primary (DFS report, DFS
press release, Jamie H. Hansson's account, ECOA, CFPB circular 2022-03, and the
Goldman statement as a primary artifact reached via reproduction), plus the DHH
tweet as a gated primary; and 2 clear secondaries (Futurism, TechCrunch/
O'Sullivan). More than four primaries were reachable and read directly.
