# Evidence record: what-could-go-wrong/automation-bias (01)

The record strongly supports the commissioned angle for the "already shown in a
working system" side. Bainbridge (1983) is read in full and states the origin
argument in her own words: automating the routine work leaves the human a
monitoring job that erodes exactly the manual and cognitive skills, and the
situational picture, needed to take over when the automation fails. The measured
consequence is documented firsthand in three settings I opened: a NASA
laboratory replication of "automation-induced complacency" (monitoring
sensitivity fell from A' = .84 to .70 when reliable automation was held
constant), a clinical decision-support experiment with 26 GPs (an incorrect
prescribing prompt flipped a correct decision to a wrong one in 5.2% of 520
cases), and an aviation/decision-support review that reports omission errors of
41% vs 3% and commission errors of 65%. The present-day AI side is thinner and I
have kept it separate: two recent primary lab studies (over-reliance on an LLM
adviser; less-secure code from an AI coding assistant) plus one secondary
perspective paper that itself concedes the broad "civilizational/deskilling"
claim outruns current measurement.

The record is thin in three specific places, all recorded below: (1) Parasuraman
and Riley (1997), a source the brief names, is behind a paywall and I could not
open its full text; its use/misuse/disuse/abuse taxonomy is present in the record
only through two sources that cite it firsthand. (2) The empirical
automation-bias study the brief names, Skitka, Mosier and Burdick (1999), I also
could not open directly; its headline figures reach the record only through
Cummings' (2004) retelling, so they are a single retelling, not verified against
the owning paper. (3) The AI-era figures come from crowdworker/student lab tasks
on 2022–2024 model versions and do not measure deployed behaviour.

The evidence does not undermine the commissioned angle. It refines it. See
Contradictions: aids help on net when reliable, the opposite failure (algorithm
aversion / under-reliance) is equally documented, and design and training measurably
change the size of the effect. So "a human in the loop is the fix" is neither
automatically true nor automatically false, which is the judgment the lesson asks
the reader to be able to make.

---

## Sources

```text
URL:         https://doi.org/10.1016/0005-1098(83)90046-8  (published home, Elsevier, resolves 200)
             https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf  (open full text I read, resolves 200)
Kind:        Primary. Bainbridge owns the origin argument; this is the paper that made it.
Establishes: The "ironies of automation" firsthand: automating routine control leaves the human
             a monitoring task that destroys the manual and cognitive skills, and the current
             mental picture of the process, needed to take over in the abnormal case.
Paraphrase:  The designer who removes the operator still leaves the operator the tasks that could
             not be automated, with no support designed for them. Manual take-over needs control
             skill that decays without practice, so a "formerly experienced operator who has been
             monitoring an automated process may now be an inexperienced one." Fault diagnosis
             needs cognitive skill and a live picture of process state that a monitor does not
             build. Monitoring itself is defeated by vigilance limits (after Mackworth 1950,
             ~half an hour). If the computer is better than the human, asking the human to judge
             whether the computer's decisions are acceptable is an impossible task. Most reliable
             automation, with the rarest need to intervene, needs the greatest investment in
             operator training.
Locators:    Automatica 19(6):775-779, 1983. Introduction and §1.1 (pp. 775-776); §1.1.1 Manual
             control skills; §1.1.2 Cognitive skills; §1.1.3 Monitoring; §2 Approaches; Conclusion.
Quote:       "physical skills deteriorate when they are not used, particularly the refinements of
             gain and timing. This means that a formerly experienced operator who has been
             monitoring an automated process may now be an inexperienced one." (p. 775)
             "the automatic control system has been put in because it can do the job better than
             the operator, but yet the operator is being asked to monitor that it is working
             effectively... The human monitor has been given an impossible task." (p. 776)
             "it is the most successful automated systems, with rare need for manual intervention,
             which may need the greatest investment in human operator training." (p. 777)
```

```text
URL:         https://ntrs.nasa.gov/citations/20020021642  (NASA NTRS record, open, resolves 200)
             PDF: https://ntrs.nasa.gov/api/citations/20020021642/downloads/20020021642.pdf
Kind:        Primary for its own experiment (a NASA-run complacency study). Secondary where it
             retells Parasuraman, Molloy and Singh (1993).
Establishes: A measured, controlled replication that holding automation reliable AND constant
             (not the reliability level itself) is what induces monitoring failure ("complacency").
Paraphrase:  NASA/TM-2001-211413, Prinzel, DeVries, Freeman and Mikulka. Forty undergraduates ran a
             multi-task flight simulation (tracking, fuel management, and a system-monitoring task
             whose automation caught 14/16 malfunctions at "high" reliability, 9/16 at "low").
             Monitoring sensitivity for the automation's own missed failures, A' (a signal-detection
             index where .5 = chance and 1 = perfect), was significantly higher under variable
             reliability (M = .84) than under constant reliability (M = .70), F(1,39) = 25.26,
             p < .0001. High "complacency-potential" participants did worse (M = .72) than low
             (M = .84). This confirms Parasuraman et al. (1993). The report's retelling of that 1993
             study: participants monitored across four 30-min sessions under constant low (56.25%),
             constant high (87.5%), or variable reliability; complacency appeared after ~20 minutes;
             consistency, not level, drove it.
Locators:    Title p.1; PMS-1993 retelling pp.9-10 (extracted lines ~1475-1510); method pp.13-17;
             A' result p.~24 (extracted lines 5400-5502); N=40 (extracted lines 2941, 4936).
Quote:       "Participants who performed the monitoring task under the variable reliability
             condition (M = .84) did significantly better than participants under the constant
             reliability condition (M = .70). This confirms the finding of Parasuraman et al.
             (1993) that constant reliability, even under high levels of reliability, significantly
             impairs the ability of the operator to monitor for infrequent automation failures."
Real-world:  Reports (citing Billings 1997) that the 1987 Detroit accident "was caused partly by
             the crew's complacent reliance on the airplane's automation to configure take-off"
             and failure to confirm via the taxi checklist. This is a retelling, not a primary
             accident record (that would be the NTSB report on Northwest Airlines Flight 255).
```

```text
URL:         https://openaccess.city.ac.uk/id/eprint/3005/  (open thesis, resolves 200)
Kind:        Primary. Goddard's own doctoral study; she owns the experiment and its data.
Establishes: Automation bias measured in a realistic clinical-prescribing decision-support task,
             WITH the counter-fact that the same aid improved decisions on net.
Paraphrase:  Kate Goddard, PhD thesis, City University London, April 2012, "Automation Bias and
             Prescribing Decision Support." 26 NHS General Practitioners each prescribed for 20
             validated scenarios (N = 520 prescribing cases). Advice was correct 70% of the time,
             incorrect 30%. Automation bias (a "commission" error) was operationalised as a
             clinician switching from a correct pre-advice prescription to an incorrect one after
             seeing the advice: 5.2% of all cases. Pre-advice accuracy was 50.4%, rising to 58.3%
             after advice; the aid improved decision accuracy in 13.1% of cases and worsened it in
             5.2%, a net improvement of ~8 percentage points. By participant, correct advice pulled
             decisions toward correct answers and incorrect advice pulled them toward wrong ones.
             Lower clinical experience was associated with more decision switching. Goddard flags
             that the low absolute number of bias instances makes the rate noisy and possibly an
             underestimate, and that a planned time-pressure arm was dropped for low response.
Locators:    Abstract (extracted lines 393-432); mitigators/accountability (extracted lines 650-651).
Quote:       "The rate of AB, as measured by decision switches from correct pre advice, to incorrect
             post advice was 5.2% of all cases at a CDSS accuracy rate of 70% - leading to a net
             improvement of 8%."
```

```text
URL:         https://arxiv.org/abs/2412.15584  (open, resolves 200; also ACM CHI 2025)
Kind:        Primary. Bo, Wan and Anderson's own randomized experiment.
Establishes: Recent, direct measurement of over-reliance on an LLM adviser, and of a specific
             failure fluency raises: confidence rose after wrong reliance decisions (miscalibration).
Paraphrase:  Jessica Y. Bo, Sophia Wan, Ashton Anderson (University of Toronto), "To Rely or Not to
             Rely?", CHI 2025. Pre-registered online experiment, 400 Prolific crowdworkers in four
             conditions (Control n=99, Uncertainty Highlighting n=98, two others n=100), two tasks:
             LSAT logical reasoning and image-based numerical estimation. Each answered alone, saw
             GPT-4o advice (randomly good or bad, ~50% correct), then answered again. On LSAT,
             participants were initially correct on 36.0% of instances, and 46.1% after advice
             (advice helped on net); the best a perfectly-calibrated human-AI team could reach was
             62.1%, so much of the possible gain was lost to wrong reliance decisions. In the
             Control condition, when the LLM's advice was bad, self-reliance was only 0.44 (RSR),
             i.e. participants followed bad advice a majority of the time; relative reliance on good
             advice was 0.66 (RLR). Interventions reduced over-reliance but generally did not
             improve overall appropriate reliance, trading over-reliance for under-reliance.
             Participants reported HIGHER confidence gains when they made the wrong reliance choice.
Locators:    Abstract; §4.1 Participants; §4.2 Task performance (LSAT 36.0%/46.1%/62.1%); §4.3 and
             Table 1 (Control LSAT RLR .66, RSR .44, ARR 1.17). Numerical estimation: absolute error
             45.7% alone vs 47.0% with advice (no improvement).
Quote:       "while interventions reduce over-reliance, they generally fail to improve appropriate
             reliance. Furthermore, people became more confident after making incorrect reliance
             decisions in certain contexts, demonstrating poor calibration."
```

```text
URL:         https://arxiv.org/abs/2211.03622  (open, resolves 200; also ACM CCS 2023)
Kind:        Primary. Perry, Srivastava, Kumar and Boneh's own controlled user study.
Establishes: A second, independent modern over-reliance result on a different AI assistant type
             (code), including the same overconfidence signature.
Paraphrase:  "Do Users Write More Insecure Code with AI Assistants?" 47 participants after
             exclusions (33 with an AI assistant based on OpenAI's code-davinci-002; 14 control),
             five security-relevant programming tasks across Python, JavaScript and C. Participants
             with the assistant wrote significantly less secure code (insecure more often on four of
             five tasks, controlling for background) AND were more likely to believe their code was
             secure. The authors frame this as a "false sense of security" / overconfidence, not a
             claim that the assistant is useless.
Locators:    Abstract; §1 (RQ1 result); §3.2 (47 participants, 33/14 split); §3 (five tasks).
Quote:       "participants who had access to an AI assistant wrote significantly less secure code
             than those without access to an assistant. Participants with access to an AI assistant
             were also more likely to believe they wrote secure code."
```

```text
URL:         https://doi.org/10.2514/6.2004-6313  (AIAA published home; gated, returns 403/CAPTCHA)
             open copy I read: https://maritimesafetyinnovationlab.org/wp-content/uploads/2023/02/Automation-Bias-in-Intelligent-Time-Critical-Decision-Support-Systems.pdf (resolves 200)
Kind:        Primary for its definitions and framing (Cummings' own review/analysis). Secondary
             where it retells specific numbers from other studies (marked below).
Establishes: The standard definitions the lesson needs, plus documented deployed/high-fidelity
             cases, plus two clean "reliable-vs-erroneous" contrasts.
Paraphrase:  M. L. Cummings (MIT), "Automation Bias in Intelligent Time Critical Decision Support
             Systems," AIAA 2004-6313. Automation bias = the human "disregards or does not search
             for contradictory information in light of a computer-generated solution that is
             accepted as correct." Errors of omission = failing to notice a problem the automation
             did not flag; errors of commission = following an automated directive erroneously.
             RETELLING (of Skitka, Mosier and Burdick 1999): in an automated-monitoring-aid study,
             preprogrammed omission instances produced error rates of 41% (automated) vs 3%
             (non-automated), and intentional commission errors raised the error rate to 65%
             "despite the presence of 100% reliable secondary contraindications"; but when the aid
             was reliable it improved performance over no aid. RETELLING (Sarter and Schroeder 2001,
             in-flight icing): with erroneous computer advice, pilots WITHOUT the command display
             outperformed those with it, leading to the recommendation that status displays (LOA 2)
             be used instead of command displays (LOA 4) unless the aid is perfectly reliable.
             Cummings' own Tomahawk-redirection study: ranked recommendations (LOA 4) gave faster
             decisions with no accuracy cost WHEN correct, but induced automation bias when the
             recommendation was wrong.
Locators:    §Automation Bias (definitions, p.2); §III.B (41%/3%/65%, p.3, citing ref 19 = Skitka,
             Mosier & Burdick 1999; icing study, ref 20 = Sarter & Schroeder 2001); §III.C Patriot
             and Tomahawk (pp.4-5); references list p.5-6.
Quote:       "errors of omission occur when humans fail to notice problems because the automation
             does not alert them, while errors of commission occur when humans erroneously follow
             automated directives or recommendations."
Real-world:  Patriot missile fratricide, Operation Iraqi Freedom 2003: the system engaged in
             fratricide, shooting down a British Tornado and a US F/A-18, and "under the added
             stress of combat, Patriot operators did not veto the computer's solution" (citing the
             32nd Army Air and Missile Defense Command report). Eastern Air Lines L-1011, Florida
             Everglades, 1972 (citing NTSB AAR-73-14). Both are retellings; the primary records are
             the cited Army and NTSB reports.
```

```text
URL:         https://doi.org/10.1037/xge0000033  (APA published home, resolves 200)
             open copy I read: https://marketing.wharton.upenn.edu/wp-content/uploads/2016/10/Dietvorst-Simmons-Massey-2014.pdf (resolves 200)
Kind:        Primary. Dietvorst, Simmons and Massey's own five-study paper.
Establishes: The opposite, equally documented failure: people UNDER-use good automation. This is
             the load-bearing contradiction for the desk's line.
Paraphrase:  Berkeley J. Dietvorst, Joseph P. Simmons, Cade Massey (University of Pennsylvania),
             "Algorithm Aversion: People Erroneously Avoid Algorithms After Seeing Them Err,"
             Journal of Experimental Psychology: General, 144(1):114-126, 2015. Across five
             incentivized studies, people who saw a statistical algorithm make forecasts became
             less willing to bet on it and chose an inferior human forecaster instead, even when
             they had seen the algorithm outperform the human, because they lost confidence in the
             algorithm faster after seeing it err. The failure runs opposite to automation bias.
Locators:    Abstract p.114; design (5 studies) pp.114-116; general discussion.
Quote:       "people are especially averse to algorithmic forecasters after seeing them perform,
             even when they see them outperform a human forecaster. This is because people more
             quickly lose confidence in algorithmic than human forecasters after seeing them make
             the same mistake."
```

```text
URL:         https://arxiv.org/abs/2509.08010  (open, resolves 200)
Kind:        Secondary. A present-day perspective/synthesis; it reports on and consolidates other
             people's work rather than owning a new experiment.
Establishes: Who makes the over-reliance argument now, what they want done, and (usefully) their
             own admission of where the evidence is still absent.
Paraphrase:  Lujain Ibrahim, Katherine M. Collins, Sunnie S. Y. Kim et al., "Measuring and
             mitigating overreliance to build human-compatible AI," arXiv:2509.08010v2 (2025, rev.
             2026). Argues that measuring and mitigating over-reliance "must become central to LLM
             research and deployment," naming three near-/long-term risks: high-stakes errors,
             governance challenges, and cognitive deskilling. It explicitly grounds the framing in
             Parasuraman and Riley's (1997) typology (misuse = over-reliance, disuse = under-
             reliance) and in Dietvorst's algorithm aversion. Crucially for the desk's line, it
             concedes the strong claim outruns present proof: "limited empirical evidence at this
             time is not indicative of no issue of overreliance," attributing the gap to the
             absence of good measurement rather than to a demonstrated harm.
Locators:    Abstract; §1; §2 (Parasuraman & Riley, Dietvorst); §deskilling/governance; §"a
             reasonable starting concern" (the empirical-evidence concession); Conclusion.
Quote:       "the risk of overreliance -- relying on LLMs beyond their capabilities -- grows... we
             argue that limited empirical evidence at this time is not indicative of no issue of
             overreliance."
```

---

## Contradictions

Searched specifically for evidence against the strong version of the angle. Found
four kinds, all recorded above and consolidated here because the editor will use
them to draw the shown/extrapolated line.

1. The aids help on net when they are reliable. Goddard's clinicians ended more
   accurate with the decision support than without it (50.4% -> 58.3%, net ~+8
   points) even though it also induced automation-bias errors in 5.2% of cases.
   Bo et al.'s participants scored higher on LSAT with the LLM than alone
   (36.0% -> 46.1%). Cummings reports that a reliable monitoring aid "led to
   improved human performance and fewer errors as opposed to not having an aid,"
   and her own Tomahawk study found ranked recommendations gave faster decisions
   with no accuracy loss when the automation was correct. So over-reliance is a
   cost that coexists with benefit; it is not evidence that the aid is bad.

2. The opposite failure is equally documented. Dietvorst et al. (2015) show
   people erroneously AVOID good algorithms after seeing them err, even ones they
   watched beat a human. Bo et al. observe under-reliance too, and find that
   interventions cutting over-reliance also cut useful reliance. "The human
   over-trusts the machine" is therefore not a universal law; distrust is a
   competing, measured failure mode.

3. Design and training move the effect. Goddard found accountability increases
   cross-verification and that less-experienced clinicians switched more.
   Cummings/Sarter & Schroeder found that when advice can be wrong, a plain
   status display beats a "do this" command display, and recommend status
   displays unless the aid is perfect. Bo et al. found a simple reliance
   disclaimer improved appropriate reliance on the LSAT task. This directly
   tests the proponents' original assumption that a human monitor is the fix: the
   fix is real but conditional on how the system is designed and how the human is
   held accountable, not automatic.

4. The present-day "civilizational" version outruns its proof. The strongest
   modern claims (broad cognitive deskilling, societal governance failure) are
   prospective. The secondary source that makes them (Ibrahim et al.) concedes
   the direct empirical evidence is currently limited. The measured AI studies I
   have (Bo et al.; Perry et al.) are single-session lab tasks with
   crowdworkers/students on specific 2022-2024 model versions (GPT-4o;
   code-davinci-002), not observations of deployed behaviour, and Perry's own
   authors note the model they tested is already a generation old. The symmetric
   dismissal — "a human in the loop fixes it" — is undercut by items 1-3.

No source I opened contradicts Bainbridge's core mechanism itself; the
disagreements are all about magnitude, direction, and remedy, which is the
territory the lesson is meant to map.

---

## Numbers

```text
Figure: Manual/monitoring skill decays; monitor vigilance fails after ~30 minutes
Owner:  Bainbridge 1983 (citing Mackworth 1950 for the 30-minute vigilance limit)
Scope:  Qualitative claim in process-control and flight-deck settings; no denominator.
```

```text
Figure: Monitoring sensitivity A' = .84 (variable reliability) vs .70 (constant), F(1,39)=25.26, p<.0001
Owner:  NASA/TM-2001-211413, Prinzel et al. 2001 (its own experiment)
Scope:  N = 40 undergraduates; A' is a signal-detection index (.5 chance, 1 perfect), not a raw
        detection percentage; automation caught 14/16 (87.5%) or 9/16 (56.25%) of malfunctions.
```

```text
Figure: Complacency appears after ~20 minutes; constant 87.5% vs 56.25%, four 30-min sessions
Owner:  Parasuraman, Molloy & Singh 1993 — REACHED ONLY VIA the NASA report's retelling
Scope:  Not verified against the owning 1993 paper (could not open it). Treat as retold.
```

```text
Figure: Automation bias (correct->incorrect switch after bad advice) = 5.2% of cases; aid net +8 points
Owner:  Goddard 2012 (its own experiment)
Scope:  26 GPs x 20 scenarios = 520 prescribing cases; advice correct 70% / incorrect 30%;
        pre-advice accuracy 50.4%, post 58.3%; aid helped 13.1%, hurt 5.2%.
```

```text
Figure: Omission error rate 41% (automated) vs 3% (non-automated); commission error rate 65%
Owner:  Skitka, Mosier & Burdick 1999 — REACHED ONLY VIA Cummings 2004's retelling
Scope:  Simulated en-route flight monitoring; 65% occurred "despite 100% reliable secondary
        contraindications." Single retelling; denominators/N not stated in the source I read.
```

```text
Figure: LSAT accuracy 36.0% alone -> 46.1% with LLM; best possible team 62.1%; bad-advice self-reliance 0.44
Owner:  Bo, Wan & Anderson 2025 (its own experiment)
Scope:  N = 400 (Control n=99); per-instance rates over LSAT question instances; GPT-4o adviser
        set to ~50% accuracy. Numerical-estimation task: absolute error 45.7% alone vs 47.0% with advice.
```

```text
Figure: AI-assisted participants wrote significantly less secure code (worse on 4 of 5 tasks) and
        were more likely to believe their code was secure
Owner:  Perry et al. 2023 (its own experiment)
Scope:  47 participants (33 AI / 14 control); OpenAI code-davinci-002; Python/JavaScript/C.
```

```text
Figure: Algorithm aversion across 5 studies: seeing an algorithm err lowers willingness to use it
        even when it outperforms a human
Owner:  Dietvorst, Simmons & Massey 2015 (its own studies)
Scope:  Five incentivized forecasting experiments; effect is directional (choice/confidence), not
        a single headline percentage.
```

---

## Source assets

```text
Asset: NASA/TM-2001-211413, the A' bar comparison (variable M=.84 vs constant M=.70), Results section
Shows: The whole "complacency" claim in one image — reliable-but-constant automation lowers the
       human's ability to catch the automation's own failures.
Crop:  Must keep both condition labels and the A' axis with its range; a crop that drops the axis
       hides that A' is a sensitivity index, not "percent detected."
```

```text
Asset: Bo et al. 2025, Figure 4 transition matrices (first- vs second-stage LSAT outcomes) and
       Table 1 (RLR/RSR/ARR by condition)
Shows: Over-reliance and under-reliance side by side — how many correct answers were talked out of,
       and how many wrong answers were adopted, after LLM advice.
Crop:  Table 1 must retain the RSR row and the condition labels; the over-reliance reading is
       1 minus RSR, so dropping the metric definition would mislead.
```

```text
Asset: Goddard 2012, the pre/post advice accuracy figures (50.4% -> 58.3%, with the 13.1% helped /
       5.2% harmed split), abstract and Table 6.2
Shows: The net-benefit-with-embedded-bias picture in one place — the single most useful counter to a
       one-sided "automation bias is pure harm" framing.
Crop:  Keep both the helped and harmed figures together; showing only 5.2% would invert the meaning.
```

```text
Asset: Bainbridge 1983 — no chart in the paper. None found (it is an argument, not a dataset).
```

---

## Discarded

```text
URL: https://journals.sagepub.com/doi/10.1518/001872097778543886 — Parasuraman & Riley 1997, the
     brief's named taxonomy source. Full text is paywalled (SAGE returns 403; Semantic Scholar,
     ResearchGate, the author's GMU lab page, and the Internet Archive all failed or were blocked
     in this session). NOT read, so NOT cited as read. Its use/misuse/disuse/abuse taxonomy is in
     the record only through sources that cite it firsthand (Cummings 2004; Ibrahim et al. 2025).
     Canonical page recorded here for the writer; if the taxonomy is quoted, quote it from Cummings
     or Ibrahim, not from this paywalled paper.
```

```text
URL: https://www.sciencedirect.com/science/article/abs/pii/S1071581999902525 — Skitka, Mosier &
     Burdick 1999, the brief's named empirical study. Abstract only; full text paywalled and the
     author's own hosting (lskitka.people.uic.edu) reset every connection this session. Its figures
     enter the record only via Cummings' (2004) retelling and are flagged as such in Numbers.
```

```text
URL: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5356416/ — Lyell et al., "Automation bias in
     electronic prescribing" (120 students). NCBI served a CAPTCHA/anti-bot page, not the article.
     Not needed: Goddard 2012 covers the clinical decision-support result with a cleaner denominator.
```

```text
URL: Blog/commentary summaries of Bainbridge (acolyer.org "the morning paper"; Human Factors 101;
     various Medium posts). Rejected: commentary, not the original document, which the brief and the
     series direction both forbid. Bainbridge is read directly instead.
```
