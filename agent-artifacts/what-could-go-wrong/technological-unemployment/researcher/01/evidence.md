# Evidence record: what-could-go-wrong/technological-unemployment (01)

Every headline number in this argument was checked against the study that owns
it, with its exact definition, denominator, and period. The evidence firmly
supports the commission's angle: the case does turn on tasks-versus-occupations
(Frey-Osborne's 47% versus the OECD/Arntz-Gregory-Zierahn 9% are the same
economy measured two ways) and on exposure-versus-displacement (Eloundou et al.
measure a capability, and say in the paper that it is not a displacement
forecast). The two things the argument most needs and does not have are both
recorded here: a measured count of jobs actually lost to AI does not exist in any
of these papers, and the real-system evidence that does exist is small, recent,
and setting-specific (one call-center firm; one freelancing platform; a short
post-ChatGPT window). The loudest present-day alarm figure, Amodei's, carries no
public study. The historical counter-argument (Autor) is recorded at full
strength, along with the specific reason Acemoglu gives for why this round's
early productivity gains may not extrapolate. Nothing below is repeated from
coverage: each number was read in the primary that produced it.

A "high-risk occupation" (Frey-Osborne) and a "high-exposure worker" (Eloundou)
are different objects and are kept distinct throughout. "At risk," "exposed,"
"productivity gain," and "displacement" are four different measurements and no
two of them are the same claim.

## Sources

```
URL:         https://www.marxists.org/reference/subject/economics/keynes/1930/our-grandchildren.htm
Kind:        primary — Keynes's own essay owns the coinage. (Public-domain full-text transcription; the text is the artifact, not the host.)
Establishes: The origin and original 1930 framing of "technological unemployment," and that Keynes framed it as temporary.
Paraphrase:  Keynes names a "new disease," technological unemployment, defined as unemployment caused when labour-saving discovery outruns the pace at which new uses for labour are found. He immediately calls this a temporary phase of maladjustment inside a longer story of the economic problem being solved, and forecasts a roughly fifteen-hour work week within a century.
Locators:    Section II ("technological unemployment" passage).
Quote:       "We are being afflicted with a new disease of which some readers may not yet have heard the name, but of which they will hear a great deal in the years to come — namely, technological unemployment. This means unemployment due to our discovery of means of economising the use of labour outrunning the pace at which we can find new uses for labour." Followed by: "But this is only a temporary phase of maladjustment."
```

```
URL:         https://www.oxfordmartin.ox.ac.uk/publications/the-future-of-employment   (PDF read: https://oms-www.files.svdcdn.com/production/downloads/academic/The_Future_of_Employment.pdf , Oxford Martin's own host)
Kind:        primary — the study that produced the 47% figure. Carl Benedikt Frey (Oxford Martin School) and Michael A. Osborne (Dept. of Engineering Science, Oxford).
Establishes: The 47% figure, its exact definition, denominator, method, and unit (whole occupations).
Paraphrase:  47% of total US employment is in the "high risk" category, defined as an estimated probability of computerisation above 0.7 (medium risk 0.3-0.7, low risk below 0.3). The unit is the whole occupation, not the task. Method: 702 occupations from the O*NET database; the authors, with a group of ML researchers at a workshop at the Oxford University Engineering Sciences Department, hand-labelled 70 of those occupations as automatable (1) or not (0) by asking whether all of an occupation's tasks could be specified for state-of-the-art computer-controlled equipment given big data; a Gaussian-process classifier trained on nine O*NET "level" variables (for perception/manipulation, creativity, social intelligence bottlenecks) then predicted probabilities for all 702. Employment weights are BLS 2010 occupational employment. Timeframe is deliberately vague: "some unspecified number of years, perhaps a decade or two." The authors explicitly make no attempt to estimate how many jobs will actually be automated.
Locators:    Sec. IV (method, hand-labelling), pp. ~30-31; Sec. V "Employment in the 21st Century" and Fig. III, p. 37 (the 47% statement, thresholds at 0.7/0.3); Conclusion, p. 44.
Quote:       "According to our estimate, 47 percent of total US employment is in the high risk category, meaning that associated occupations are potentially automatable over some unspecified number of years, perhaps a decade or two." And, on scope: "We make no attempt to estimate the number of jobs that will actually be automated, and focus on potential job automatability over some unspecified number of years."
```

```
URL:         https://www.oecd.org/en/publications/the-risk-of-automation-for-jobs-in-oecd-countries_5jlz9h56dvq7-en.html   (PDF read on OECD's own host)
Kind:        primary — the study that produced the ~9% task-based figure. Melanie Arntz, Terry Gregory, Ulrich Zierahn. OECD Social, Employment and Migration Working Papers No. 189 (2016).
Establishes: The ~9% task-based figure, why the task framing lowers the answer, and that it is the same economy Frey-Osborne measured.
Paraphrase:  Applying a task-based approach, on average 9% of jobs across 21 OECD countries are "highly automatable," defined as an automatability of at least 70%. For the US specifically the figure is 9%, set directly against Frey-Osborne's 47% for the same country. The gap is driven by within-occupation task variation: even in occupations Frey-Osborne score as high-risk, workers perform tasks that are hard to automate, such as face-to-face interaction and group work. Data: the PIAAC Survey of Adult Skills (2012), which records task usage at the individual worker level (US task detail via the Princeton Data Improvement Initiative). Cross-country: highest in Germany and Austria (12%), lowest in Korea and Estonia (6%). The authors caution these numbers still should not be equated with actual expected employment losses.
Locators:    Abstract and executive summary (9% average, para. 6-7); Sec. B "Results for the US," p. 14 (US 9% vs FO 47%; bookkeeping-clerk and retail-salesperson worked examples); Sec. C, cross-country shares (Fig. 3).
Quote:       "As a result, only 9% of all individuals in the US face a high automatibility, i.e. an automatibility of at least 70%. This figure stands in contrast to FO, who argue that 47% of US jobs are at high risk of being automated." And on cause: "even in occupations that Frey and Osborne considered to be in the high risk category, workers at least to some extent also perform tasks that are difficult to automate such as tasks involving face-to-face interaction."
```

```
URL:         https://arxiv.org/abs/2303.10130   (working-paper PDF read: arxiv.org/pdf/2303.10130 ; published as Eloundou et al., Science 2024, doi:10.1126/science.adj0998)
Kind:        primary — the study that owns the LLM task-exposure shares. Tyna Eloundou, Sam Manning, Pamela Mishkin, Daniel Rock, "GPTs are GPTs" (2023).
Establishes: The LLM exposure shares, the exact definition of "exposure," and the explicit "exposure is not impact" caveat.
Paraphrase:  Exposure is a task-level measure: a task is "exposed" if access to an LLM (or LLM-powered software) could cut the time to do it, at equivalent quality, by at least 50%. The rubric has three levels: E0 no exposure; E1 direct (the LLM alone via a ChatGPT-style interface halves the time); E2 (software built on top of the LLM would halve the time). Aggregating to occupations, about 15% of a worker's tasks are directly exposed on average (the alpha measure, human and GPT-4 annotations both ~0.14-0.15); this rises above 30% including E2 software (beta) and above 50% for the widest measure (zeta). About 80% of workers are in an occupation with at least 10% of tasks exposed; about 19% of workers are in an occupation with over 50% of tasks exposed. Directly (human, E1 only) just 3% of workers have over half their tasks exposed, rising to up to 49% once complementary software and other generative models are counted. Source data: O*NET tasks/DWAs. The authors define exposure as a proxy that does not distinguish augmentation from displacement and make no adoption-timeline prediction.
Locators:    Sec. 3 exposure rubric (E0/E1/E2), pp. ~9-10 and Appendix A.1; Sec. 4 results and Table 3 (alpha ~0.15, beta >30%, 80%/19%); abstract and Sec. 4 (3% and up to 49% human estimates); Table 4 caption (not full automation).
Quote:       Definition/caveat: "We define exposure as a proxy for potential economic impact without distinguishing between labor-augmenting or labor-displacing effects." And: "We do not make predictions about the development or adoption timeline of such LLMs." And, on the highest-exposure occupations: "it does not necessarily suggest that their tasks can be fully automated by these technologies." And: "technical feasibility does not guarantee labor productivity or automation outcomes."
```

```
URL:         https://www.nber.org/papers/w31161   (PDF read: nber.org/system/files/working_papers/w31161/w31161.pdf ; published Quarterly Journal of Economics)
Kind:        primary — the field study that owns the customer-support effect sizes. Erik Brynjolfsson, Danielle Li, Lindsey R. Raymond, "Generative AI at Work" (NBER WP 31161, 2023).
Establishes: The measured, real-system productivity effect of a generative-AI assistant, and its distribution across worker skill.
Paraphrase:  Using the staggered rollout of a generative-AI conversational assistant at a software firm's customer-support operation, data covering 5,179 agents and ~3 million chats: access to the tool raised productivity (issues resolved per hour) by 14% on average, against a baseline of about 2.6 resolutions per hour. The gain is concentrated among the least-experienced and lowest-skilled workers (34% for the lowest skill quintile) with minimal effect on the most experienced and highest-skilled. The tool spreads more-skilled workers' practices to newer ones. Access also improved customer sentiment and reduced attrition (driven by retention of newer workers). This is a productivity field study, not an employment-loss study; it measures output per worker, not headcount.
Locators:    Abstract; Sec. 1 (14% and 34% headline, p. ~4-6); Sec. results (baseline 2.6/hour, 0.29 log-point = 34% for lowest quintile); Sec. on customer sentiment and attrition.
Quote:       "Access to the tool increases productivity, as measured by issues resolved per hour, by 14% on average, including a 34% improvement for novice and low-skilled workers but with minimal impact on experienced and highly skilled workers."
```

```
URL:         https://www.ifo.de/DocDL/cesifo1_wp10601.pdf   (CESifo Working Paper 10601, 2023; published Hui, Reshef, Zhou, Organization Science 2024, doi:10.1287/orsc.2023.18441. SSRN copy at abstract_id=4527336 is gated.)
Kind:        primary — the labor-market study that owns the freelancer demand/earnings effects. Xiang Hui, Oren Reshef, Luofeng Zhou.
Establishes: An early measured demand-and-earnings drop for the most-exposed workers after ChatGPT, and that top freelancers were hit hardest.
Paraphrase:  On Upwork, a large online freelancing platform, a difference-in-differences design compares freelancers in occupations highly affected by generative AI (writing, coding) against less-affected occupations, around the November 2022 release of ChatGPT (and separately DALL-E 2 and Midjourney). After ChatGPT, more-affected freelancers saw their monthly number of jobs fall by 2% (s.e. 0.004) and monthly earnings fall by 5.2% (s.e. 0.016) relative to the comparison group. On the extensive margin, they were 1.2 percentage points less likely to get any job in a month (about a 10% drop from baseline employment). High past performance did not shield workers; top freelancers were disproportionately hurt. Denominator is freelancers in highly-affected occupations on one platform, not the whole labor market; the window is short-term.
Locators:    Abstract (2%, 5.2%); Sec. results (Table with 2% s.e.=0.004, 5.2% s.e.=0.016; 1.2 pp extensive margin; intensive-margin ~4.7% jobs / ~5.1% income); Sec. on top freelancers.
Quote:       "freelancers in more affected occupations experienced a decrease of 2% in the number of monthly jobs and a decrease of 5.2% in monthly earnings on the platform, following the release of ChatGPT, compared" [to less affected occupations].
```

```
URL:         https://economics.mit.edu/sites/default/files/2024-04/The%20Simple%20Macroeconomics%20of%20AI.pdf   (author's institution; also NBER WP 32487, nber.org/papers/w32487)
Kind:        primary — owns the macro TFP estimate. Daron Acemoglu (MIT), "The Simple Macroeconomics of AI" (April 2024).
Establishes: The modest ten-year macro estimate and the method behind it.
Paraphrase:  Using a task-based model and a version of Hulten's theorem (GDP/TFP gains equal the fraction of tasks impacted times average task-level cost savings), Acemoglu estimates that AI's total-factor-productivity effect over the next ten years is no more than 0.71% in total, roughly 0.07% per year. Inputs: about 19.9% of US labor tasks are exposed to AI (from Eloundou et al.); of exposed tasks, ~23% can currently be profitably automated (Svanberg et al., computer vision); average labor cost saving 27% (the average of Noy-Zhang 2023 and Brynjolfsson et al. 2023), which industry labor shares turn into ~15.4% total cost saving. GDP rises about 1.1% over ten years on his benchmark (upper bound 1.6-1.8% with heavier investment assumptions). A refined estimate that gives smaller gains on "hard-to-learn" tasks lowers the bounds to ~0.55% TFP and ~0.90% GDP over ten years. He notes new tasks could raise this, but that some new AI tasks (deepfakes, manipulative ads) carry negative social value.
Locators:    Abstract and Sec. 1 (0.71% TFP / 0.07% annual, ~1.1% GDP; hard-task refinement to 0.55%/0.90%); Sec. on Hulten's theorem; Sec. contrasting with Goldman Sachs's 7% GDP / 1.5%-p.a.-TFP figure.
Quote:       "This calculation implies that total factor productivity (TFP) effects within the next 10 years should be no more than 0.71% in total — or approximately a 0.07% increase in TFP growth annually." And: "GDP is also estimated to grow by around 1.1% over the next 10 years."
Note:        Some coverage and an earlier draft cite "0.66%." The version read here (MIT, April 2024) states 0.71% total TFP (refined 0.55%). Record the figure the study states and cite this version.
```

```
URL:         https://www.aeaweb.org/articles?id=10.1257/jep.29.3.3   (Journal of Economic Perspectives 29(3):3-30, 2015; text read via course mirror jenni.uchicago.edu/econ341/readings/Autor_2015_JEP_v29_n3.pdf)
Kind:        primary — owns the task-complementarity / historical counter-argument. David H. Autor (MIT), "Why Are There Still So Many Jobs? The History and Future of Workplace Automation."
Establishes: The historical counter-argument at full strength, with the ATM/bank-teller worked case and the conditions under which complementarity does or does not protect workers.
Paraphrase:  Autor's thesis: commentary overstates machine substitution and ignores complementarity — automating some tasks raises the value of the tasks that remain, and tasks that cannot be automated are generally complemented by the ones that are, which can raise labor demand. Worked case (from Bessen 2015): ATMs, introduced in the 1970s, roughly quadrupled from ~100,000 to ~400,000 in the US between 1995 and 2010; US bank-teller employment nonetheless rose modestly from ~500,000 to ~550,000 between 1980 and 2010 (though it fell as a share of total employment). Tellers per branch fell by more than a third between 1988 and 2004, but cheaper branches let banks open more than 40% more urban branches, and tellers shifted toward "relationship banking." Autor's Polanyi's-paradox point: the hardest tasks to automate are those requiring flexibility, judgment, and common sense, which people understand only tacitly ("we know more than we can tell"). He states two conditions that limit the wage benefit of complementarity: an elastic supply of the complementary skill, and whether the remaining tasks are ones only some workers can supply.
Locators:    Opening thesis, pp. 3-5; ATM/teller case, pp. 6-7; Polanyi's paradox, pp. ~11-12; complementarity/demand-elasticity/labor-supply conditions.
Quote:       On the thesis: "Automation does indeed substitute for labor — as it is typically intended to do. However, automation also complements labor, raises output in ways that lead to higher demand for labor, and interacts with adjustments in labor supply." On the case: "US bank teller employment actually rose modestly from 500,000 to approximately 550,000 over the 30-year period from 1980 to 2010." On Polanyi: "the tasks that have proved most vexing to automate are those demanding flexibility, judgment, and common sense — skills that we understand only tacitly."
```

```
URL:         https://www.yahoo.com/news/anthropic-ceo-warns-ai-could-152758674.html   (Fortune, Chris Morris, May 28 2025; reports the origin interview at Axios, axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic — the Axios page returns 403 to automated fetch and is the gated origin.)
Kind:        secondary — reporting, from outside Anthropic, on how the alarm is deployed now. Fetched firsthand at the Fortune/Yahoo page; the Axios interview is the origin.
Establishes: The present-day, high-profile version of the alarm and that it rests on no public study.
Paraphrase:  Anthropic CEO Dario Amodei told Axios that AI could eliminate about half of all entry-level white-collar jobs within roughly one to five years and push unemployment to 10-20%, across technology, finance, law, and consulting. He framed it as a duty to warn and a call for preparation, not a modeled forecast; no dataset or study is cited behind the numbers. This is the "confidence outruns proof" datapoint on the alarm side: a specific, large figure from a party with a stake, unaccompanied by a public method.
Locators:    Headline and body; direct-quote paragraph.
Quote:       Amodei: "Most of them are unaware that this is about to happen. It sounds crazy, and people just don't believe it… We, as the producers of this technology, have a duty and an obligation to be honest about what is coming."
```

```
URL:         https://itif.org/publications/2022/09/30/oops-the-predicted-47-percent-of-job-loss-from-ai-didnt-happen/
Kind:        secondary — opinion/analysis, from a technology-industry-aligned think tank (Information Technology and Innovation Foundation), on how the 47% figure is deployed. Author Robert D. Atkinson.
Establishes: The dismissal-side deployment, and (usefully) a misreading of Frey-Osborne worth flagging.
Paraphrase:  ITIF argues the predicted mass job loss did not materialize: nine years after 2013 the US had added ~16 million jobs with unemployment around 3.7%, and specific "high-risk" occupations (insurance underwriters, +16.4%) grew while a "low-risk" one (recreational therapists, -8.9%) shrank. Note for the writer: the piece characterizes Frey-Osborne as having predicted that 47% of jobs "would likely be eliminated," which the original explicitly disclaims (Frey-Osborne measured occupations "at risk," not a job-loss forecast). The dismissal here partly rebuts a stronger claim than Frey-Osborne made.
Locators:    Opening and jobs-data paragraphs.
Quote:       "Well, it's been nine years since their dystopian forecast came out, so it's worth looking at what happened to U.S. jobs." And the misstatement to flag: it describes the forecast as "47 percent of U.S. jobs would likely be eliminated by technology over the next 20 years."
```

## Contradictions

- **47% versus 9% is the central disagreement, and it is methodological, not
  empirical.** Frey-Osborne and Arntz-Gregory-Zierahn measure the same US economy
  and disagree by a factor of five because one scores whole occupations (a
  high-risk occupation) and the other scores tasks within occupations weighted to
  individual workers (a high-automatability worker). AGZ state the gap is caused
  entirely by within-occupation task variation and give worked examples
  (bookkeeping clerks: 98% under Frey-Osborne, but only 24% of them work without
  group work or face-to-face interaction; retail salespersons: 92%, but only 4%).
  Neither is a count of jobs lost.

- **Exposure versus displacement.** Eloundou et al.'s 80%/19% exposure shares are
  routinely deployed as if they were displacement figures. The authors contradict
  that reading in the paper: exposure "does not distinguish between
  labor-augmenting or labor-displacing effects," and high exposure "does not
  necessarily suggest that their tasks can be fully automated." An exposed task
  can become a productivity gain (Brynjolfsson-Li-Raymond) rather than a lost job.

- **Productivity gain versus employment loss point in opposite directions in the
  real-system evidence.** Brynjolfsson-Li-Raymond find AI made customer-support
  workers 14% more productive and cut attrition (a complement, keeping people in
  work). Hui-Reshef-Zhou find the most-exposed freelancers lost 2% of jobs and
  5.2% of earnings (a substitute, reducing demand). Both are real and measured;
  they differ because one studies output per worker inside a firm and the other
  studies demand for workers on an open platform. Neither generalizes to the whole
  economy.

- **Who is hit hardest reverses between two field studies.** Brynjolfsson-Li-
  Raymond: gains concentrate on the least-skilled, compressing the gap (34% for
  the bottom quintile, minimal at the top). Hui-Reshef-Zhou: top freelancers are
  disproportionately hurt and past performance gives no protection. The alarm and
  dismissal both cite "AI helps/hurts workers" without noticing the two studies
  measure different things (skill within a task versus demand across a market).

- **Macro modesty versus micro alarm.** Acemoglu's ten-year TFP estimate (≤0.71%,
  ~0.07%/year) is roughly an order of magnitude below the Goldman Sachs figure he
  contrasts with (7% GDP, 1.5%/year TFP), and far below Amodei's implied
  disruption. Acemoglu's own caveat cuts against extrapolating the field studies:
  measured gains sit in "easy-to-learn" tasks, and future effects fall on
  "hard-to-learn" tasks where gains should be smaller.

- **The dismissal partly attacks a claim Frey-Osborne did not make.** ITIF treats
  47% as a prediction that jobs "would likely be eliminated." Frey-Osborne
  explicitly make "no attempt to estimate the number of jobs that will actually be
  automated." The "it didn't happen" rebuttal lands on a stronger forecast than the
  study issued — which is itself evidence of how the number travels stripped of its
  definition.

- **Keynes framed technological unemployment as temporary; the present alarm
  frames it as possibly permanent.** Keynes coined the term inside an optimistic
  long-run story (the economic problem solved, a 15-hour week). Today's alarmists
  keep the term and drop the optimism. The disagreement is about whether new work
  appears as fast as old work is automated — the exact hinge Autor's complementarity
  argument turns on.

## Numbers

```
Figure: 47% of total US employment in the "high risk" category (probability of computerisation > 0.7)
Owner:  Frey & Osborne (2013)
Scope:  Denominator = total US employment weighted by BLS 2010 occupational employment across 702 O*NET occupations. Unit = whole occupations. Period = "some unspecified number of years, perhaps a decade or two." Not a forecast of jobs actually lost.
```
```
Figure: Medium risk 0.3-0.7 probability; low risk < 0.3 probability
Owner:  Frey & Osborne (2013)
Scope:  Same 702 occupations; the thresholds that define the three risk bands.
```
```
Figure: 9% of US jobs "highly automatable" (task-based); 9% average across 21 OECD countries
Owner:  Arntz, Gregory, Zierahn / OECD (2016)
Scope:  Denominator = individual workers (US via Princeton Data Improvement Initiative; OECD via PIAAC 2012). "Highly automatable" = automatability of at least 70%. Task-based. Directly comparable to Frey-Osborne's 47% for the US.
```
```
Figure: Cross-country high-risk share: Germany & Austria 12% (high); Korea & Estonia 6% (low); OECD average 9%
Owner:  Arntz, Gregory, Zierahn / OECD (2016)
Scope:  Share of workers with automatability >= 70%, 21 OECD countries, PIAAC 2012. (Chart-ready series.)
```
```
Figure: ~15% of a worker's tasks directly exposed (alpha ~0.14-0.15); >30% including LLM-powered software (beta); >50% widest measure (zeta)
Owner:  Eloundou, Manning, Mishkin, Rock (2023)
Scope:  Task-level, O*NET tasks/DWAs, US. "Exposed" = time to complete cut >=50% at equal quality. Human and GPT-4 annotations agree. Capability measure, not displacement.
```
```
Figure: 80% of workers in an occupation with >=10% of tasks exposed; 19% of workers with >50% of tasks exposed
Owner:  Eloundou, Manning, Mishkin, Rock (2023)
Scope:  Beta measure (LLM + software), share of US workforce. Exposure, not impact.
```
```
Figure: 3% of workers with >50% of tasks exposed (direct human, E1 only); up to 49% with complementary software and other generative models
Owner:  Eloundou, Manning, Mishkin, Rock (2023)
Scope:  Human-annotated bounds on the share of US workers, low end (LLM alone) to high end (with tooling).
```
```
Figure: +14% average productivity (issues resolved per hour); +34% for lowest-skill quintile; minimal for highest-skilled
Owner:  Brynjolfsson, Li, Raymond (2023)
Scope:  5,179 customer-support agents at one software firm, ~3 million chats, staggered AI-assistant rollout. Baseline ~2.6 resolutions/hour. Output per worker, not headcount.
```
```
Figure: -2% monthly jobs (s.e. 0.004); -5.2% monthly earnings (s.e. 0.016); -1.2 pp probability of any job in a month (~10% of baseline)
Owner:  Hui, Reshef, Zhou (2023)
Scope:  Freelancers in highly-affected occupations on Upwork, difference-in-differences vs less-affected occupations, around ChatGPT's Nov 2022 release. One platform; short-term.
```
```
Figure: <=0.71% total TFP over 10 years (~0.07%/year); GDP ~1.1% over 10 years; refined bounds 0.55% TFP / 0.90% GDP
Owner:  Acemoglu (2024, MIT April version)
Scope:  US economy, next 10 years. Inputs: 19.9% of tasks exposed, 23% of exposed profitably automatable, 27% average labor cost saving (~15.4% total). Contrast: Goldman Sachs 7% GDP / 1.5%-per-year TFP.
```
```
Figure: ATMs ~100,000 -> ~400,000 (1995-2010); US bank tellers ~500,000 -> ~550,000 (1980-2010); tellers/branch -1/3 (1988-2004); urban branches +40%
Owner:  Autor (2015), citing Bessen (2015)
Scope:  US banking. The historical complementarity case: automation of a task coincided with modestly rising employment in the same occupation, though tellers fell as a share of total US employment.
```
```
Figure: ~50% of entry-level white-collar jobs eliminated in 1-5 years; unemployment 10-20%
Owner:  Dario Amodei (claim, reported by Axios/Fortune, May 2025) — NOT a study
Scope:  Tech, finance, law, consulting; entry-level roles. A warning with no public dataset or method. Record as a deployment of the argument, not as a measured figure.
```

## Source assets

```
Asset: Frey & Osborne (2013), Figure III, p. 37 — distribution of BLS 2010 occupational employment over probability of computerisation, shaded into low/medium/high bands.
Shows: How the 47% is constructed — the bi-polar pile-up of employment at high and low probability, and exactly which mass falls above 0.7. Makes the "whole occupations" method visible.
Crop:  Keep the full x-axis (0 to 1), the 0.3 and 0.7 threshold lines, and the shaded high-risk area with its label. Do not crop out the low/medium bands, which are the point of comparison.
```
```
Asset: Arntz, Gregory, Zierahn (2016), Figure 2, p. 14 — Distribution of Automatibility in the US, task-based versus occupation-based, on one axis.
Shows: The two methods on the same economy: the occupation-based curve is bi-polar (resembling Frey-Osborne), the task-based curve pulls toward the middle, which is why 47% becomes 9%. The single clearest picture of the tasks-versus-occupations crux.
Crop:  Retain both curves and the legend distinguishing them, and the 70% threshold. Omitting either curve destroys the comparison.
```
```
Asset: Arntz, Gregory, Zierahn (2016), Figure 3 — share of workers at high risk by OECD country.
Shows: The cross-country spread (6% Korea to 12% Germany/Austria), useful if the writer wants to show the task-based number is stable and low across rich countries.
Crop:  Keep all country bars and the axis; the range is the message.
```
```
Asset: Frey & Osborne (2013), the ranked occupation table / appendix — occupations by probability of computerisation (telemarketers, title examiners, hand sewers near 0.99).
Shows: The concrete end of the method: which named occupations the model scores as almost certain to be computerised. Good for grounding "high risk" in real jobs.
Crop:  Keep occupation names and probabilities together; a probability without its occupation label is meaningless.
```
```
Asset: Brynjolfsson, Li, Raymond (2023) — the figure showing productivity effect by worker skill quintile (largest at the bottom, near zero at the top).
Shows: That the measured real-system gain compresses the skill gap rather than falling evenly, the finding that distinguishes this study from the freelancer study.
Crop:  Keep all skill quintiles on the x-axis; the shape (declining left to right) is the finding.
```
A comparison chart the writer could build from committed figures: Frey-Osborne
47% (occupation-based, US) beside Arntz-Gregory-Zierahn 9% (task-based, US), each
labeled with its definition and denominator. All four numbers are recorded above
with exact scope, so a `chart-N.py` could plot them honestly.

## Discarded

```
URL: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4527336 — Hui-Reshef-Zhou on SSRN; returned 403 (gated). Read the identical CESifo WP 10601 PDF instead; recorded that resolving URL.
URL: https://www.axios.com/2025/05/28/ai-jobs-white-collar-unemployment-anthropic — origin of the Amodei claim; returns 403 to automated fetch. Kept as the named origin; fetched the same claim firsthand at Fortune/Yahoo and recorded that.
URL: https://www.cnn.com/2025/05/29/tech/ai-anthropic-ceo-dario-amodei-unemployment and https://www.kron4.com/... — further retellings of the Amodei claim; 451/403 and, being the same origin, count as one source. Not separately recorded.
URL: https://journalistsresource.org/economics/computerization-future-research-technologys-effects/ — a research roundup; useful orientation but a tertiary summary, superseded by reading each study firsthand.
URL: https://melbourneinstitute.unimelb.edu.au/.../result?paper=3197111 (Coelli & Borland, "Behind the Headline Number") — an independent critique of Frey-Osborne; not read in full, and the tasks-versus-occupations critique it makes is already owned firsthand by the OECD/AGZ paper, so it would be a second retelling of that point rather than a new source.
URL: https://arxiv.org/pdf/2104.13747 (Lindner et al., model-selection critique of Frey-Osborne) — a methodological reanalysis; not needed for the headline numbers and would overweight one contested detail.
```
