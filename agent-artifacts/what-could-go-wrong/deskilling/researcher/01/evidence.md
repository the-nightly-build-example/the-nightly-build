# Evidence: what-could-go-wrong/deskilling (01)

The argument's origin and its full-strength reasoning are documented firsthand:
Bainbridge (1983) states, in her own words, every load-bearing claim the
steelman needs, including the point that automation hands the operator the
hardest residue of the job after stripping the practice that built competence at
it. The "shown in a working system" side is strongest and oldest outside AI:
a controlled simulator study (Casner 2014) measured which piloting skills decay
and which do not, a government accident report (NTSB 2014) and FAA field
guidance (SAFO 13002) name automation reliance and the loss of manual practice
as factors, and a controlled navigation study with a three-year follow-up
(Dahmani and Bohbot 2020) measured spatial-memory decline that tracked GPS use.
The AI-specific "shown" side is thinner and newer: one retrospective
observational colonoscopy study (Budzyn 2025) measured a drop in unaided
detection after routine AI exposure, and one non-peer-reviewed preprint
(Kosmyna 2025) measured engagement proxies, not durable skill loss, in essay
writing. The present-day coding claim the commission names has no controlled
deskilling measurement; the closest recent number (METR 2025) is a productivity
and perception result, not skill decay. The evidence is thin in exactly one
place the commission leans on: measured, durable, AI-caused skill loss rests on
a single small observational study and a contested preprint, so the sharp line
between measured deskilling and forecast must be drawn hard.

## Sources

```text
URL:         https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf
Kind:        primary. Lisanne Bainbridge is the author of the argument; this is
             the full text of the paper that owns it (Automatica 19(6):775-779,
             1983). Read in full (5 pages).
Establishes: The "ironies of automation" argument at origin. The designer
             automates what can be automated and leaves the operator the rest;
             manual skills and cognitive knowledge deteriorate without practice;
             the operator asked to monitor and take over has lost the skill to
             do so; monitoring a rarely-failing automatic system is itself
             beyond sustained human attention.
Paraphrase:  Automating the easy parts of a task can make the remaining hard
             parts harder. A formerly skilled operator who only monitors becomes
             an unskilled one, because physical skills decay when unused and
             knowledge retrieval depends on frequency of use. The most reliable
             automation needs the most operator training, because manual
             intervention is rarest exactly where the process is most degraded.
Locators:    Manual control skills: p.775, sec. 1.1.1. Cognitive/long-term
             knowledge: p.775-776, sec. 1.1.2. Monitoring/vigilance: p.776,
             sec. 1.1.3. Deskilling and status: p.776, sec. 1.2. "Easy parts"
             framing: p.777, sec. 3. "Final irony": p.777, sec. 2.2.
Quote:       "Unfortunately, physical skills deteriorate when they are not used,
             particularly the refinements of gain and timing. This means that a
             formerly experienced operator who has been monitoring an automated
             process may now be an inexperienced one." (p.775)
             "There is some concern that the present generation of automated
             systems, which are monitored by former manual operators, are riding
             on their skills, which later generations of operators cannot be
             expected to have." (p.776)
             "By taking away the easy parts of his task, automation can make the
             difficult parts of the human operator's task more difficult."
             (p.777)
             Note: Bainbridge herself uses "deskilled" (p.776, sec. 1.2), for
             the job reduced to monitoring.
```

```text
URL:         https://journals.sagepub.com/doi/10.1177/0018720814535628
Kind:        primary. Casner, Geven, Recker, and Schooler own the study data.
             Human Factors 56(8):1506-1516, 2014. Publisher page is gated (HTTP
             403); the full abstract was read verbatim via the Europe PMC record
             (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1177/0018720814535628&resultType=core,
             PMID 25509828). Abstract read; full text (figures, tables) not
             obtained.
Establishes: A controlled measurement of which manual-flying skills decay under
             automation. Manual control and instrument-scan skills were mostly
             retained even when rarely practiced; the cognitive tasks of manual
             flight (tracking position without a map display, sequencing
             navigation, recognizing failures) degraded more, and that
             degradation tracked how much the pilot's mind wandered while
             automation flew.
Paraphrase:  16 airline pilots flew routine and non-routine scenarios in a
             Boeing 747-400 simulator at systematically varied automation
             levels. Psychomotor skill held up; cognitive skill did not, and its
             retention depended on staying actively engaged in supervising the
             automation, not on stick-time alone.
Locators:    Abstract, Method and Results sentences (verbatim below).
Quote:       "We found pilots' instrument scanning and manual control skills to
             be mostly intact, even when pilots reported that they were
             infrequently practiced. However, when pilots were asked to manually
             perform the cognitive tasks needed for manual flight ... we observed
             more frequent and significant problems."
             This is the sharpest primary for the shown/forecast line: it says
             the popular claim ("automation ruins stick-and-rudder skill") is the
             weaker half; the measured loss is cognitive and engagement-linked.
```

```text
URL:         https://www.ntsb.gov/investigations/AccidentReports/Reports/AAR1401.pdf
Kind:        primary. The NTSB owns this accident report (AAR-14/01, adopted
             June 24, 2014) on Asiana Airlines Flight 214, San Francisco, July 6,
             2013. Downloaded and read in full (207 pages, text extracted).
Establishes: An accident where automation reliance and lost manual-flight
             practice are named factors, but not as the one-line cause. The
             probable cause is mismanaged descent, the pilot flying's unintended
             deactivation of automatic airspeed control, inadequate airspeed
             monitoring, and a delayed go-around. Contributing factors include
             autothrottle/autopilot complexity poorly described in Boeing and
             Asiana training. Finding 8 names automation reliance as a cause of
             the monitoring failure; Finding 15 and section 2.6.2 name Asiana's
             full-automation policy and scarce manual-flight practice.
Paraphrase:  The crew let the airplane get low and slow on a visual approach and
             did not catch it because they trusted the autothrottle to hold speed
             when it would not. The report ties the monitoring lapse partly to
             "automation reliance," and argues that regular manual flying would
             have helped the pilot flying feel and correct the decaying airspeed.
             Asiana policy discouraged hand-flying except below 1,000 ft; a
             contract instructor said pilots avoided manual flying for fear of
             error.
Locators:    Probable cause: p.129, sec. 3.2. Finding 8 (automation reliance)
             and Finding 15 (manual-flight practice): pp.129-130, sec. 3.1.
             Manual Flight analysis: pp.102-103, sec. 2.6.2. FAA actions: p.74,
             sec. 1.18.3. Board Member Weener's automation-overreliance emphasis:
             p.139 (individual statement).
Quote:       Probable cause: "the flight crew's mismanagement of the airplane's
             descent during the visual approach, the pilot flying's unintended
             deactivation of automatic airspeed control, the flight crew's
             inadequate monitoring of airspeed, and the flight crew's delayed
             execution of a go-around..." (p.129)
             Finding 8: "Insufficient flight crew monitoring of airspeed
             indications during the approach likely resulted from expectancy,
             increased workload, fatigue, and automation reliance." (sec. 3.1)
             Section 2.6.2: "Pilots must have both training and recent experience
             in manually manipulating the controls so as to have the skill and
             confidence to perform manual flight maneuvers safely."
```

```text
URL:         https://www.faa.gov/sites/faa.gov/files/other_visit/aviation_industry/airline_operators/airline_safety/SAFO13002.pdf
Kind:        primary. The FAA owns SAFO 13002, "Manual Flight Operations,"
             January 4, 2013. The faa.gov page returned HTTP 403 to automated
             fetch (gated, not dead); its exact wording was read verbatim as
             reproduced in the NTSB report, sec. 1.18.3, p.74.
Establishes: The aviation regulator, before the Asiana crash, warned in field
             guidance that continuous autoflight use degrades manual-recovery
             ability, citing an increase in manual-handling errors in operations
             data. This is a "shown side" field position, not a controlled
             measurement.
Paraphrase:  The FAA told operators to promote manual flight because flight-
             operations data showed rising manual-handling errors, and continuous
             autoflight use could erode a pilot's ability to recover the airplane
             from an undesired state. A November 2013 revision to 14 CFR Part 121
             added Extended Envelope Training (14 CFR 121.423) to build manual
             handling skills.
Locators:    Reproduced in NTSB AAR-14/01, p.74, sec. 1.18.3.
Quote:       As quoted by the NTSB: the SAFO "cautioned that continuous use of
             autoflight systems could lead to degradation of the pilot's ability
             to quickly recover the aircraft from an undesired state" and cited
             flight-operations data that "identified an increase in manual
             handling errors." (NTSB AAR-14/01, p.74)
```

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC7156656/
Kind:        primary. Dahmani and Bohbot own the study data. Scientific Reports
             10:6310, published April 14, 2020. Open-access full text read here;
             canonical publisher DOI: https://www.nature.com/articles/s41598-020-62877-0.
Establishes: A controlled study of tool dependence in navigation, with a rare
             three-year longitudinal arm that points at direction of cause.
             Greater lifetime GPS use correlated with worse hippocampal-dependent
             spatial memory when navigating unaided, and heavier GPS use over the
             three years tracked a steeper decline. Baseline sense of direction
             did not predict later GPS use, which argues the tool drove the
             decline rather than poor navigators reaching for the tool.
Paraphrase:  50 regular drivers were tested on virtual navigation and rated for
             lifetime GPS use; 13 were retested three years later. More GPS use
             went with weaker unaided spatial memory, and the follow-up showed
             decline steepening with more GPS use in between.
Locators:    Cross-sectional result and longitudinal result; reverse-causation
             discussion. Statistics below.
Quote:       "people with greater lifetime GPS experience have worse spatial
             memory during self-guided navigation" and "greater GPS use since
             initial testing was associated with a steeper decline in
             hippocampal-dependent spatial memory."
```

```text
URL:         https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00133-5/abstract
Kind:        primary. Budzyn and colleagues own the study data. The Lancet
             Gastroenterology & Hepatology, 2025. Publisher page is gated (HTTP
             403); the full abstract with all figures was read verbatim via the
             Europe PMC record (https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:40816301&resultType=core,
             PMID 40816301). Abstract read verbatim; full text not obtained.
Establishes: The single strongest AI-specific deskilling measurement found: after
             routine AI exposure, the same endoscopists detected fewer adenomas
             when working without AI. This measures unaided performance, which is
             the deskilling claim, not merely reliance on the aid.
Paraphrase:  At four Polish centers in the ACCEPT trial, adenoma detection rate
             in standard non-AI colonoscopy fell from 28.4% before AI was
             introduced to 22.4% after, an absolute drop of 6.0 percentage points
             (about 20% relative), with AI exposure an independent factor in
             regression. The study is retrospective and observational; the authors
             frame it as a possible negative effect on endoscopist behaviour, not
             a proven durable skill loss.
Locators:    Abstract: Methods, Findings, Interpretation. Numbers below.
Quote:       "The ADR of standard colonoscopy decreased significantly from 28.4%
             (226 of 795) before to 22.4% (145 of 648) after exposure to AI,
             corresponding with an absolute difference of -6.0% (95% CI -10.5 to
             -1.6; p=0.0089)." "Continuous exposure to AI might reduce the ADR of
             standard non-AI assisted colonoscopy, suggesting a negative effect
             on endoscopist behaviour."
```

```text
URL:         https://arxiv.org/abs/2506.08872
Kind:        primary. Kosmyna and seven co-authors (MIT Media Lab) own the study
             data. arXiv preprint 2506.08872, v1 June 10, 2025; v2 December 31,
             2025. Not peer-reviewed. Abstract read.
Establishes: A recent AI-assistant measurement on unaided cognition, with heavy
             caveats. Over four months, LLM users writing essays showed the
             weakest EEG connectivity of three groups, weaker memory of their own
             text, and lower reported ownership. This measures engagement and
             recall proxies, not a demonstrated durable loss of writing skill.
Paraphrase:  54 participants wrote essays across sessions in three arms (LLM,
             search engine, brain-only); 18 did a fourth switched session.
             Brain-only had the strongest, most distributed EEG networks; LLM the
             weakest. LLM users struggled to quote their own essays. When
             brain-only writers later used the LLM, recall and activation rose;
             when LLM users went unaided, engagement stayed low.
Locators:    Abstract.
Quote:       "Brain-only participants exhibited the strongest, most distributed
             networks; Search Engine users showed moderate engagement; and LLM
             users displayed the weakest connectivity." Mark as measured proxy,
             not proven skill loss; see Contradictions for the published critique.
```

```text
URL:         https://arxiv.org/abs/2507.09089
Kind:        primary. METR owns the study data. "Measuring the Impact of Early-
             2025 AI on Experienced Open-Source Developer Productivity," 2025
             (also https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/).
             Read via the study's own reported results.
Establishes: The closest recent measured datapoint on the present-day coding
             claim, and a caution against confidence outrunning proof, in the
             direction of dismissal as much as doom. It measures speed and
             perception, not skill decay.
Paraphrase:  In a randomized trial, 16 experienced open-source developers took
             about 19% longer to complete tasks in their own repositories when
             allowed AI tools, yet estimated afterward that AI had sped them up by
             roughly 20%. The measured gap is between perception and productivity.
Locators:    Reported primary results (abstract and blog summary).
Quote:       Use only to mark the gap: there is no controlled measurement that AI
             coding assistants erode debugging or programming skill. This study
             shows a perception-reality gap in productivity, which is a different
             claim, and must not be presented as deskilling evidence.
```

```text
URL:         https://gi.org/journals-publications/ebgi/zhou_sep2025/
Kind:        secondary. Margaret J. Zhou, MD (Clinical Assistant Professor of
             Medicine, Stanford University Division of Gastroenterology &
             Hepatology), reviewing the Budzyn study from outside it for the
             American College of Gastroenterology's Evidence-Based GI. Read.
Establishes: An expert reading of the colonoscopy study's weight and its limits.
             Calls it the first study to assess AI-exposure effects on unaided
             colonoscopy performance, and flags observational confounding,
             selection bias, only 19 endoscopists with no per-endoscopist
             analysis, missing withdrawal-time data, and a low overall ADR
             (25.7%) against a US target near 35%.
Paraphrase:  Novel and important, but observational and confounded; the drop
             could reflect complacency rather than a proven durable skill loss,
             and the sample is small and specific.
Locators:    Strengths and Limitations sections.
Quote:       "this was an observational study susceptible to confounding and
             selection bias."
```

```text
URL:         https://www.eurekalert.org/news-releases/1094223
Kind:        secondary. Journal-issued press release reporting the Budzyn study
             and outside comment. Read. (Relays primary detail and an independent
             expert; the underlying claims trace to the primary and to Omer
             Ahmad's Lancet comment.)
Establishes: Study scale and the authors' own caveats: 19 experienced
             endoscopists, each having done over 2,000 colonoscopies; 1,443 non-AI
             colonoscopies (795 before, 648 after); authors state the observational
             design means factors other than AI may have influenced the result and
             call for studies in less-experienced operators. Independent commentator
             Dr Omer Ahmad (UCL) warns of "the quiet erosion of fundamental skills"
             while noting AI's promise.
Paraphrase:  Confirms endoscopist and colonoscopy counts and the authors'
             observational caveat, and carries Ahmad's outside caution.
Locators:    Body of release.
Quote:       Authors: "the observational nature of the study means that factors
             other than the implementation of AI use may have influenced the
             findings." Ahmad: caution against "the quiet erosion of fundamental
             skills required for high-quality endoscopy."
```

```text
URL:         https://arxiv.org/abs/2601.00856
Kind:        secondary. Stankovic, Hirche, Kollatzsch, and Doetsch critique the
             Kosmyna preprint from outside it. arXiv comment, December 2025. Read.
Establishes: That the Kosmyna essay-writing result is contested on method, and
             that reduced EEG connectivity does not by itself prove skill loss.
             Grounds the instruction to mark the AI-writing evidence as a proxy,
             not a demonstration.
Paraphrase:  Names limited sample size, EEG-analysis and reproducibility
             problems, inconsistent reporting, and limited transparency, and says
             the results should be read more conservatively.
Locators:    Abstract of the comment.
Quote:       "some results by Kosmyna et al. (2025) could be interpreted more
             conservatively."
```

## Contradictions

- The Asiana probable cause does not name deskilling. Framing the crash as
  "automation deskilled the pilot, and that caused the crash" overstates the
  NTSB record. The one-sentence probable cause is about in-the-moment
  mismanagement and inadequate airspeed monitoring plus autothrottle-mode
  complexity (NTSB p.129). Automation reliance appears as one contributor to the
  monitoring lapse (Finding 8), and lost manual practice as a would-have-helped
  factor (Finding 15, sec. 2.6.2), not as the cause. Board Member Weener's
  stronger "automation overreliance" language is an individual statement (p.139),
  not the Board's cause. Use Asiana as an accident where automation dependence
  was a named factor, not as proof that deskilling downs airliners.

- Casner (2014) cuts against the popular version of the aviation claim. Manual
  stick-and-rudder control was "mostly intact" even when rarely practiced; the
  measured loss was in cognitive tasks, and it tracked disengagement
  (mind-wandering) more than raw practice loss. The slogan "use it or lose it,
  for hand-flying" is the weaker, less-supported half of the finding.

- The colonoscopy result may be complacency or in-the-moment automation bias
  rather than durable skill erosion. It is one retrospective, observational study
  with residual confounding, 19 experienced endoscopists, no per-endoscopist
  analysis, and a low baseline ADR (Zhou/ACG). A three-month unaided ADR drop is
  a behavior-change signal, not proof of lost underlying capability. This is the
  single most important caveat on the AI-specific "shown" claim. Note also the
  boundary with the automation-bias article: deskilling is loss of the underlying
  capability over time; this study measures unaided performance, which is why it
  belongs here, but its mechanism is not yet pinned to skill loss.

- The Kosmyna preprint is contested (Stankovic et al.) and non-peer-reviewed.
  Reduced EEG connectivity is an engagement proxy; it does not demonstrate that
  the writers lost writing skill. Popular "ChatGPT makes you dumber" framing is
  not supported by the paper. Effects may reflect reduced effort under assistance,
  which can reverse when the assistance is removed.

- The present-day coding claim runs ahead of its evidence. No controlled study
  found here measures erosion of debugging or programming skill from AI
  assistants. METR (2025) measured a productivity slowdown and a perception gap
  in 16 experienced developers, which is not deskilling. This gap runs in both
  directions the series warns about: doom (asserted skill collapse) and dismissal
  (assumed harmlessness) each outrun the measurement.

- Bainbridge is a forecast that has aged well in some domains, not a measurement.
  Her 1983 paper reasons from process-control and flight-deck experience; it is
  the argument's origin and its most careful statement, not primary quantitative
  proof. Treat its claims as the steelman to be tested, and cite the later
  measurements (Casner, Dahmani/Bohbot, Budzyn) for anything asserted as shown.

## Numbers

```text
Figure: adenoma detection rate 28.4% (226 of 795) before AI exposure
Owner:  Budzyn et al., Lancet Gastroenterology & Hepatology, 2025
Scope:  standard non-AI colonoscopy, 4 Polish ACCEPT centers, 3-month pre-AI
        window (Sept 2021 onward), 19 experienced endoscopists
```
```text
Figure: adenoma detection rate 22.4% (145 of 648) after AI exposure
Owner:  Budzyn et al., 2025
Scope:  standard non-AI colonoscopy, same centers, 3-month post-AI window (to
        March 2022)
```
```text
Figure: absolute ADR change -6.0 percentage points (95% CI -10.5 to -1.6;
        p=0.0089); about 20% relative; AI-exposure odds ratio 0.69 (95% CI
        0.53-0.89)
Owner:  Budzyn et al., 2025
Scope:  primary outcome; regression adjusted for patient sex and age
```
```text
Figure: 1,443 non-AI colonoscopies (795 before, 648 after); 19 endoscopists,
        each having performed over 2,000 colonoscopies
Owner:  Budzyn et al., 2025 (counts confirmed via journal press release)
Scope:  denominator for the ADR comparison
```
```text
Figure: 16 airline pilots; Boeing 747-400 simulator; automation level varied
Owner:  Casner et al., Human Factors, 2014
Scope:  psychomotor skills mostly retained; cognitive skills degraded more
```
```text
Figure: 50 drivers cross-sectional; 13 retested after 3 years
Owner:  Dahmani and Bohbot, Scientific Reports, 2020
Scope:  lifetime GPS use vs unaided spatial memory. Reported associations:
        cross-sectional r = -0.22 (95% CI -0.41 to -0.01); 3-year probe decline
        r = -0.68 (95% CI -0.91 to -0.10); cognitive-map decline r = -0.52 (95%
        CI -0.79 to -0.21). Baseline sense of direction did not predict later GPS
        use (r = 0.07). Small longitudinal n; treat coefficients as directional.
```
```text
Figure: 54 participants (18 in a 4th switched session); ~83% of LLM users could
        not quote their just-written essay
Owner:  Kosmyna et al., arXiv preprint, 2025 (the 83% figure is widely reported
        from the paper; the abstract states LLM users "struggled to accurately
        quote"; verify the exact 83% in the full text before printing it)
Scope:  essay-writing task over 4 months; EEG connectivity weakest in LLM group.
        Preprint, contested; proxy measures
```
```text
Figure: experienced developers 19% slower with AI; expected a 24% speedup
        beforehand and still believed AI sped them up 20% afterward
Owner:  METR, 2025
Scope:  16 experienced open-source developers, 246 issues, own repositories.
        Productivity and perception, not skill decay. Read firsthand at
        https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/
```
```text
Figure: mid-1930s origin and reach of the argument: Bainbridge 1983, Automatica
        19(6):775-779
Owner:  Bainbridge, 1983
Scope:  process control and flight-deck automation; the argument's canonical
        statement, not a measurement
```

## Source assets

```text
Asset: NTSB AAR-14/01 figures of the final approach (airspeed and altitude
       versus time to impact), ch. 1
Shows: airspeed decaying well below the target with the crew not correcting,
       which is the concrete image of a monitoring failure under automation
Crop:  keep the airspeed trace, the target-speed reference line, and the time-to-
       impact axis; not visually inspected in this pass, so the writer/editor
       should open the figure before relying on it
```
```text
Asset: Dahmani and Bohbot (2020) figures plotting lifetime GPS use against
       unaided spatial-memory scores, and the 3-year change
Shows: the negative association and its steepening over time in one picture
Crop:  keep both axes labeled and the sample size; not visually inspected this
       pass, confirm before use
```
```text
Asset: Kosmyna et al. (2025) EEG brain-connectivity network diagrams by group
Shows: the visual contrast of "weakest connectivity" in the LLM group that the
       popular coverage leaned on
Crop:  must keep all three group panels together and the caption's caveats, or it
       misleads; not visually inspected this pass. Given the contested status,
       prefer prose over this image
```
```text
Asset: Bainbridge (1983); Casner (2014) abstract; Budzyn (2025) abstract
Shows: None found suitable. Bainbridge is prose with no figures; Casner and
       Budzyn full-text figures were not obtained (gated), only abstracts read
```

## Discarded

```text
URL: https://journals.sagepub.com/doi/10.1177/0272989X12465490 (Povyakalo et al.,
     2013, CAD mammography) — a controlled reanalysis showing computer aids hurt
     the most discriminating readers on hard cases. Strong, but it measures a
     within-session effect of the aid on the decision (automation bias), not
     erosion of the underlying skill over time. It belongs to the neighboring
     automation-bias article the commission fences off; using it here would blur
     the boundary. Note it only to distinguish the two.
```
```text
URL: https://www.thelancet.com/journals/langas/article/PIIS2468-1253(25)00164-5/abstract
     (Ahmad, "Endoscopist deskilling: an unintended consequence...", Lancet
     comment) — the primary of Ahmad's caution, but gated (403) and not read
     firsthand. His view is captured through the journal press release instead;
     recorded here so the writer can cite the comment's own page if quoting him.
```
```text
URL: https://www.diva-portal.org/smash/get/diva2:1901956/FULLTEXT01.pdf — a later
     paper applying Bainbridge to public-service automation, not the 1983 source.
     Not needed; the original was read directly.
```
