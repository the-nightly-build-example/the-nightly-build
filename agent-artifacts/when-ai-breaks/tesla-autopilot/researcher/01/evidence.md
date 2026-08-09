# Evidence: when-ai-breaks/tesla-autopilot (01)

This record supports a lesson built on two NTSB crash reports read in full, three
NHTSA investigation and recall documents read in full, the SAE J3016 taxonomy,
and Tesla's own public statements. The strongest ground is the two probable-cause
findings and the December 2023 recall of every Tesla equipped with Autosteer: the
government record consistently locates the failure in a mismatch between what the
system lets a driver do and what it can actually do, not only in driver
misbehavior. The record is thinnest on Tesla's verbatim 2016 and 2018 blog
statements: Tesla has removed both posts from its live blog, so their exact
wording is confirmed through contemporaneous reproductions rather than read on
tesla.com. The record's single most important line is a contradiction the
commission will want front and center: the "almost 40 percent" crash-reduction
figure that NHTSA published in 2017 and Tesla promoted for years was later
discredited, and NHTSA disowned it. Any sentence crediting Autopilot with a
crash-rate improvement must not rest on that figure.

Two proper-noun cautions carry into display text. The NTSB reports do not print
the drivers' names; they write "the car driver," "the Tesla driver," and "the
truck driver." The names Joshua Brown, Walter Huang, and Frank Baressi come from
the public record and reporting, not from the reports themselves. And the 2016
Tesla and 2015 Model S at Williston are a "car"; the 2018 vehicle is a Model X
"sport utility vehicle." Keep those exact.

## Sources

```text
URL:         https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1702.pdf
Kind:        primary — the NTSB owns the crash investigation and the probable-cause finding.
Establishes: The Williston, Florida crash of May 7, 2016 and its cause.
Paraphrase:  At 4:36 p.m. EDT on Saturday, May 7, 2016, a 2015 Tesla Model S 70D
             traveling east on US-27A near Williston, Florida struck a
             tractor-semitrailer making a left turn across its path. The car was
             operating on Autopilot (Traffic-Aware Cruise Control plus Autosteer).
             Its speed just before impact was 74 mph in a 65-mph zone; the driver
             had set the cruise speed to 74 mph. Over the 41-minute trip from
             Cedar Key, Autopilot was active 37 minutes; the system detected the
             driver's hands on the wheel on seven occasions totaling 25 seconds,
             with a longest gap of nearly 6 minutes. The Autopilot, forward
             collision warning, and automatic emergency braking did not react to
             the crossing truck, which they were not designed to detect. The NTSB
             adopted the report September 12, 2017; Robert L. Sumwalt III was
             Chairman.
Locators:    Abstract (p. i); Probable Cause (Executive Summary p. vi and §3.2, p. 42);
             Findings 1-13 (§3.1, pp. 41-42); trip data (pp. 14-15); speed (p. 5).
Quote:       "the truck driver's failure to yield the right of way to the car,
             combined with the car driver's inattention due to overreliance on
             vehicle automation... Contributing to the car driver's overreliance
             on the vehicle automation was its operational design, which permitted
             his prolonged disengagement from the driving task and his use of the
             automation in ways inconsistent with guidance and warnings from the
             manufacturer." (§3.2)
```

```text
URL:         https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR1702.pdf
Kind:        primary — same report; recorded separately for the recommendations it issued.
Establishes: The 2017 safety recommendations, including the one Tesla did not adopt.
Paraphrase:  The NTSB issued H-17-37 through H-17-43. Two went to six named Level 2
             manufacturers, Tesla among them: H-17-41, incorporate safeguards that
             limit automated control to the conditions it was designed for; H-17-42,
             develop applications that better sense driver engagement and alert when
             it is lacking. H-17-38 asked NHTSA to develop a method to verify such
             safeguards. Finding 6 states that monitoring steering-wheel torque is a
             poor surrogate for driver engagement, because a driver can touch the
             wheel without watching the road.
Locators:    §4.1, pp. 43-44 (H-17-37 to H-17-43); Findings 5-9, p. 41.
Quote:       "monitoring steering wheel torque provides a poor surrogate means of
             determining the automated vehicle driver's degree of engagement with
             the driving task." (Finding 6)
```

```text
URL:         https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf
Kind:        primary — the NTSB owns this investigation and probable cause.
Establishes: The Mountain View, California crash of March 23, 2018 and its cause.
Paraphrase:  On Friday, March 23, 2018 at 9:27 a.m., a 2017 Tesla Model X P100D
             traveling south on US-101 in Mountain View, Santa Clara County, moved
             left into the paved gore dividing US-101 from the SR-85 left-exit ramp
             and struck a crash attenuator at about 70.8 mph. Autopilot was engaged;
             TACC was set to 75 mph at the closest following distance. About 5.9
             seconds and 560 feet before impact Autosteer steered 5.6 degrees left
             into the gore with no driver torque detected; at 3.9 seconds and 375
             feet, having lost its lead vehicle, the car accelerated from 61.9 mph
             toward the 75-mph set speed. No driver torque was detected in the last
             6 seconds. The driver, an Apple engineer, had a cell-phone game running
             as the frontmost app. The attenuator had been crushed 11 days earlier
             (March 12, 2018) and not repaired. The NTSB adopted the report February
             25, 2020; Robert L. Sumwalt III was Chairman.
Locators:    Abstract (p. i); Probable Cause (§3.2, p. 58); Findings 1-23 (§3.1,
             pp. 55-57); last-10-seconds data (pp. 5-6); trip/engagement data (p. 20);
             prior gore incidents (pp. 20-21); attenuator damage (pp. 44, 62).
Quote:       "the Tesla Autopilot system steering the sport utility vehicle into a
             highway gore area due to system limitations, and the driver's lack of
             response due to distraction likely from a cell phone game application
             and overreliance on the Autopilot partial driving automation system.
             Contributing to the crash was the Tesla vehicle's ineffective
             monitoring of driver engagement, which facilitated the driver's
             complacency and inattentiveness." (§3.2)
```

```text
URL:         https://www.ntsb.gov/investigations/AccidentReports/Reports/HAR2001.pdf
Kind:        primary — same report; recorded separately for its accountability findings.
Establishes: That Tesla did not act on the 2017 recommendations, and the NTSB's
             judgment of both Tesla's design and NHTSA's oversight.
Paraphrase:  The report reiterated H-17-41 and H-17-42 to Tesla and reclassified
             both from "Open—Await Response" to "Open—Unacceptable Response." It
             found that by relying on the premise that drivers will always be
             attentive, Tesla "created a system designed to fail because of the
             foreseeable misuse of the system." It also faulted NHTSA: its approach
             "essentially relies on waiting for problems to occur rather than
             addressing safety issues proactively" (Finding 19), and its failure to
             ensure Level 2 safeguards "compromises safety" (Finding 17). New
             recommendation H-20-3 asks NHTSA to work with SAE on driver-monitoring
             performance standards that "prevent automation complacency."
Locators:    §2.3, pp. 47-48, 63-65 (reclassifications; "designed to fail," p. 48);
             Findings 16-21, pp. 56-57; §4.1 H-20-1 to H-20-4, p. 59.
Quote:       "Tesla has created a system designed to fail because of the
             foreseeable misuse of the system." (§2.3.2, p. 48)
```

```text
URL:         https://static.nhtsa.gov/odi/inv/2016/INCLA-PE16007-7876.PDF
Kind:        primary — NHTSA's Office of Defects Investigation owns this closing report.
Establishes: NHTSA's first Autopilot investigation, its no-defect close, and the
             disputed 40% figure with the caveats NHTSA itself attached.
Paraphrase:  PE16-007 opened June 28, 2016 and closed January 19, 2017 (investigator
             Kareem Habib), covering 43,781 MY2014-2016 Model S and Model X. NHTSA
             found no defect in the AEB or Autopilot systems: AEB through MY2016 is a
             rear-end technology not designed to brake for crossing-path collisions,
             and Autopilot is an ADAS "that requires the continual and full attention
             of the driver." NHTSA classed Autopilot as SAE Level 1 with TACC alone
             and Level 2 with Autosteer added. The report's Figure 11 states the
             Tesla crash rate "dropped by almost 40 percent after Autosteer
             installation" — but its own footnotes limit the claim: the rates cover
             all miles before and after Autosteer, "not limited to actual Autopilot
             use," and only about one-third of the vehicles accumulated any
             pre-Autopilot mileage. The close "does not constitute a finding by
             NHTSA that no safety-related defect exists."
Locators:    Resume p. 1; §4.1, p. 5 (SAE levels); §5.4 and Fig. 11, pp. 10-11
             (40% and footnotes 21-22); Conclusion, pp. 11-12.
Quote:       "The data show that the Tesla vehicles crash rate dropped by almost 40
             percent after Autosteer installation." (§5.4) / footnote 22: "The crash
             rates are for all miles travelled before and after Autopilot installation
             and are not limited to actual Autopilot use."
```

```text
URL:         https://static.nhtsa.gov/odi/inv/2022/INCLA-EA22002-14498.pdf
Kind:        primary — NHTSA ODI owns this engineering-analysis closing report.
Establishes: The "critical safety gap" finding that produced the 2023 recall.
Paraphrase:  EA22-002 was upgraded from PE21-020 on June 8, 2022 and closed April 25,
             2024 (investigator Steven Posada), covering 2,031,220 Tesla vehicles.
             ODI reviewed 956 crashes reported through August 30, 2023; it set aside
             489 (insufficient data, other vehicle at fault, Autopilot not in use, or
             unrelated) and analyzed 467. It grouped them into frontal-plane impacts
             with time for an attentive driver to avoid (211), roadway departures
             where driver input inadvertently disengaged Autosteer (111), and
             roadway departures in low-traction conditions (145). ODI found
             Autopilot's controls "did not sufficiently ensure driver attention,"
             while its high control authority and ease of engagement "invited greater
             driver confidence." It identified at least 13 crashes with one or more
             fatalities in which foreseeable misuse played an apparent role. The close
             is concurrent with recall 23V-838; ODI opened Recall Query RQ24009 to
             judge whether the remedy works.
Locators:    Resume pp. 1-3; failure summary table (13 fatality incidents / 14
             fatalities); "critical safety gap," p. 3; RQ24009, p. 3.
Quote:       "This mismatch resulted in a critical safety gap between drivers'
             expectations of the L2 system's operating capabilities and the system's
             true capabilities. This gap led to foreseeable misuse and avoidable
             crashes."
```

```text
URL:         https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF
Kind:        primary — Tesla's own Part 573 Safety Recall Report filed with NHTSA.
Establishes: The December 2023 recall: the defect, the population, and the remedy.
Paraphrase:  Recall 23V-838 (Tesla reference SB-23-00-008), submitted December 12,
             2023, covers 2,031,220 vehicles — MY2012-2023 Model S, 2016-2023 Model X,
             2017-2023 Model 3, and 2020-2023 Model Y equipped with Autosteer, "100%"
             estimated to contain the defect. The defect: "the prominence and scope of
             the feature's controls may not be sufficient to prevent driver misuse of
             the SAE Level 2 advanced driver-assistance feature." The remedy is a free
             over-the-air update (version 2023.44.30) adding more prominent alerts,
             simpler engagement, extra checks off controlled-access highways and near
             traffic controls, and eventual suspension from Autosteer for drivers who
             repeatedly fail to show sustained responsibility. The chronology records
             that Tesla, "while not concurring with the agency's analysis," decided
             on December 5, 2023 to conduct the recall voluntarily.
Locators:    p. 1 (population); p. 3 (defect and safety-risk description); p. 4
             (chronology, non-concurrence); p. 5 (remedy, OTA version, dates).
Quote:       "While not concurring with the agency's analysis, in the interest of
             resolving EA22-002, Tesla determined on December 5, 2023, to voluntarily
             administer a recall." (p. 4)
```

```text
URL:         https://www.sae.org/standards/content/j3016_202104/  (taxonomy read via
             SAE's own J3016 graphic article, https://saemobilus.sae.org/articles/sae-updates-j3016-automated-driving-graphic-19tofhp02_08)
Kind:        primary — SAE International authors the J3016 taxonomy these levels come from.
Establishes: What "Level 2" means, the term the whole lesson turns on.
Paraphrase:  SAE Recommended Practice J3016 defines six levels of driving automation,
             0 (No Automation) through 5 (Full Automation). At Level 2, "Partial
             Driving Automation," the system performs both the steering and the
             braking/acceleration of the driving task, but the human driver must
             monitor the driving environment at all times and be ready to take over.
             At Levels 0-2 the human, not the system, monitors the driving
             environment — the line that separates Level 2 from Level 3. NHTSA's
             PE16-007 report reproduces this SAE chart (its Figure 3) and applies it
             directly: TACC alone is Level 1, TACC plus Autosteer is Level 2.
Locators:    SAE J3016 levels table (0-5), Level 2 row; cross-checked against
             NHTSA PE16-007 §4.1 and Figure 3, p. 5.
Quote:       Level 2 — the system performs steering and acceleration/deceleration
             while "the human driver monitors the driving environment" and supervises.
```

```text
URL:         https://www.tesla.com/blog/tragic-loss
Kind:        primary — Tesla authored this statement and owns its position. Gated:
             Tesla has removed the post from its live blog; the wording below is
             confirmed through contemporaneous reproductions (Washington Post and
             others, June 30, 2016), not read on tesla.com.
Establishes: Tesla's public account of the Brown crash and its safety framing.
Paraphrase:  In "A Tragic Loss" (June 30, 2016), Tesla called the death "the first
             known fatality in just over 130 million miles where Autopilot was
             activated," set against a US fatality about every 94 million miles and a
             worldwide one about every 60 million miles. Tesla said neither Autopilot
             nor the driver noticed the white side of the tractor-trailer against a
             brightly lit sky, so the brake was not applied, and described Autopilot
             as disabled by default, requiring explicit acknowledgement, still
             improving, and requiring the driver to keep hands on the wheel and stay
             responsible for the vehicle. This is the interested party's account, not
             an authority; the mileage comparison shares the exposure-data weakness
             that later sank NHTSA's 40% figure (see Contradictions).
Locators:    "A Tragic Loss," Tesla blog, June 30, 2016.
Quote:       "This is the first known fatality in just over 130 million miles where
             Autopilot was activated. Among all vehicles in the US, there is a
             fatality every 94 million miles. Worldwide, there is a fatality
             approximately every 60 million miles."
```

```text
URL:         https://www.tesla.com/blog/update-last-week's-accident
Kind:        primary — Tesla authored this statement. Gated: removed from the live
             blog; wording confirmed via NBC News reproduction (March 31, 2018).
Establishes: Tesla's public account of the Mountain View crash — the driver-misuse
             side of the dispute at its strongest.
Paraphrase:  In "An Update on Last Week's Accident" (March 30, 2018), Tesla said the
             driver had received several visual and one audible hands-on warning
             earlier in the drive and that his hands were not detected on the wheel
             for six seconds before the collision. Tesla said he had about five
             seconds and 150 meters of unobstructed view of the concrete divider with
             its crushed attenuator but took no action, and pointed to the previously
             damaged attenuator as the reason the crash was so severe. Tesla also
             promoted an Autopilot safety claim (a Tesla with Autopilot hardware being
             several times less likely to be in a fatal crash) of the same
             exposure-controlled kind the QCS analysis disputes.
Locators:    "An Update on Last Week's Accident," Tesla blog, March 30, 2018.
Quote:       "The driver had received several visual and one audible hands-on warning
             earlier in the drive and the driver's hands were not detected on the
             wheel for six seconds prior to the collision." (as reproduced by NBC News)
```

```text
URL:         https://www.nbcnews.com/business/autos/tesla-says-autopilot-had-been-deadly-california-crash-n861676
Kind:        secondary — NBC News reporting on, and reproducing, Tesla's statement.
Establishes: That Tesla made the Mountain View statement above, and the public
             reaction. A repetition confirms the statement was made, not that its
             framing is correct.
Paraphrase:  NBC News (March 31, 2018) reproduced Tesla's blog language on the
             hands-off warnings, the six seconds, and the five-second view of the
             divider, and reported the NTSB's displeasure that Tesla released crash
             details while the investigation was open.
Locators:    Body paragraphs quoting Tesla's blog.
Quote:       "the driver's hands were not detected on the wheel for six seconds prior
             to the collision" (Tesla, as quoted by NBC News)
```

```text
URL:         https://www.thedrive.com/tech/26455/nhtsas-flawed-autopilot-safety-study-unmasked
Kind:        secondary — The Drive, reporting the Quality Control Systems reanalysis.
             (The underlying QCS report by Randy Whitfield is the primary; it is
             recorded here through this reproduction.)
Establishes: That NHTSA's 40% figure was discredited and how — the record's key line.
Paraphrase:  After NHTSA released the underlying data in November 2018 following a
             FOIA lawsuit by analyst Randy Whitfield, Quality Control Systems
             (February 2019) found only 5,714 of the 43,781 vehicles had the complete
             mileage data the calculation required; roughly 14,791 had no before/after
             mileage yet were still counted, some against zero exposure. On the subset
             with full data, the reanalysis pointed the other way, toward a large
             increase in airbag-deployment rate after Autosteer. NHTSA subsequently
             said its review had not assessed Autopilot's effectiveness.
Locators:    Sections on the discredited figure and the data problems.
Quote:       flaws "serious enough to completely discredit the 40 percent figure."
```

```text
URL:         https://www.nhtsa.gov/laws-regulations/standing-general-order-crash-reporting
Kind:        primary — NHTSA's Standing General Order 2021-01 and its crash-report data.
Establishes: Where Level 2 systems live today and how their crashes are counted —
             the lesson's "where this lives now" anchor.
Paraphrase:  Since June 2021, Standing General Order 2021-01 requires manufacturers
             to report a crash if a Level 2 ADAS was in use within 30 seconds of the
             crash and the crash killed someone, deployed an airbag, hurt a vulnerable
             road user, or sent anyone to the hospital or required a tow. Tesla files
             the large majority of the Level 2 reports collected under the order.
Locators:    SGO reporting thresholds and the ADAS Level 2 data releases on the page.
Quote:       reporting is triggered when Level 2 ADAS "was in use at any time within
             30 seconds of the crash" and it met the injury/tow/airbag threshold.
```

```text
URL:         https://www.nbcnews.com/tech/tech-news/tesla-faces-nhtsa-investigation-full-self-driving-fatal-collision-rcna176078
Kind:        secondary — reporting on NHTSA's October 2024 FSD investigation.
Establishes: That the same Level 2 supervision problem persists in Tesla's current
             "Full Self-Driving (Supervised)."
Paraphrase:  NHTSA opened a preliminary evaluation of Tesla "Full Self-Driving" in
             October 2024, covering about 2.4 million vehicles, after reports of
             crashes in reduced-visibility conditions including one pedestrian
             fatality. FSD remains an SAE Level 2 system for which Tesla says the
             driver must supervise and be ready to intervene; Tesla renamed it "Full
             Self-Driving (Supervised)" in 2024. This is context for the close, not a
             studied incident.
Locators:    Opening paragraphs on the probe scope and the fatal crash.
Quote:       FSD "requires drivers to pay attention and intervene if needed."
```

## Contradictions

- **Tesla's account vs the NTSB's, on both crashes — the central axis.** Tesla's
  strongest version: the drivers were warned, ignored warnings, took their hands
  off the wheel, and (at Mountain View) had seconds of clear view of the hazard
  and a game running; at Williston the truck was hard to see against a bright sky.
  The NTSB's strongest version: the drivers behaved exactly as a foreseeable
  Level 2 user does, and Tesla's design — steering-wheel torque as the only
  engagement check, and no restriction of Autopilot to the roads it was built for
  — permitted that behavior. What settles it is not opinion but the recall: in
  December 2023 Tesla itself recalled every Autosteer-equipped vehicle because
  "the prominence and scope of the feature's controls may not be sufficient to
  prevent driver misuse." The design point the NTSB pressed in 2017 and 2020 is
  the point the remedy addresses. Note that Tesla filed the recall "while not
  concurring with the agency's analysis," so the dispute over cause never formally
  closed even as the remedy shipped.

- **The 40% crash-reduction figure: NHTSA (2017) vs Quality Control Systems (2019),
  with NHTSA disowning its own number.** NHTSA's PE16-007 said the crash rate
  "dropped by almost 40 percent after Autosteer installation." Tesla promoted this
  for years. But NHTSA's own footnotes already conceded the rates covered all
  miles, not Autopilot miles, and that only about a third of vehicles had any
  pre-Autopilot mileage. After a FOIA lawsuit forced the data out in November 2018,
  Quality Control Systems found most vehicles lacked the mileage data the
  calculation needed and that the figure was, on the usable subset, unsupportable.
  Treat the 40% figure as discredited. Do not repeat it, and do not let any
  Tesla mileage-per-fatality comparison stand in for it — both share the same
  missing-denominator flaw.

- **Was the driver warned right before each crash? Yes and no, and the distinction
  is the lesson.** At Williston the system displayed the hands-on visual warning
  seven times across the 41-minute trip but never in the final approach, and never
  reached the last alert stage. At Mountain View the last hands-off alert came more
  than a minute before impact; in the final six seconds the system detected nothing
  and issued nothing. So Tesla's "the driver was warned" is true for the trip and
  misleading for the moment of the crash: the monitoring did not catch the
  disengagement when it mattered. Both reports read this the same way — torque
  monitoring is a poor proxy for attention.

- **Was Autopilot at fault, or the road? Both, and the report separates them.** At
  Mountain View the NTSB assigned the steering-into-the-gore and the failure to
  brake to Autopilot's limitations and the driver's distraction, and assigned the
  severity of the injuries to the crushed, unrepaired attenuator (a Caltrans and
  CHP failure). Do not let the infrastructure failure absorb the automation
  failure: the report is explicit that Autopilot steered the car into the gore.

## Numbers

```text
Figure: 74 mph at impact; cruise set to 74 mph; posted limit 65 mph
Owner:  NTSB HAR-17/02
Scope:  Williston crash, May 7, 2016; single vehicle
```
```text
Figure: Autopilot active 37 of 41 minutes; hands detected 25 seconds over 7 times;
        longest hands-off gap ~6 minutes; ~2 minutes total in a warning state
Owner:  NTSB HAR-17/02
Scope:  the crash trip from Cedar Key, May 7, 2016
```
```text
Figure: truck visible for at least ~7 seconds before impact (crash reconstruction)
Owner:  NHTSA PE16-007 (reconstruction); NTSB concurs on sight distance
Scope:  Williston crash approach
```
```text
Figure: impact speed ~70.8 mph; TACC set to 75 mph
Owner:  NTSB HAR-20/01
Scope:  Mountain View crash, March 23, 2018
```
```text
Figure: Autosteer steered left 5.9 s / 560 ft before impact with no driver torque;
        car accelerated from 61.9 mph toward 75 mph at 3.9 s / 375 ft; no torque in
        last 6 s
Owner:  NTSB HAR-20/01 (Tesla Carlog data)
Scope:  final 10 seconds of the Mountain View crash trip
```
```text
Figure: crash trip 28 min 33 s; Autopilot active >75% of it; driver torque not
        detected 34.4% of the time Autopilot was active
Owner:  NTSB HAR-20/01
Scope:  the Mountain View crash trip
```
```text
Figure: attenuator crushed 11 days earlier, on March 12, 2018, and not repaired
Owner:  NTSB HAR-20/01
Scope:  US-101 / SR-85 gore, Mountain View
```
```text
Figure: "almost 40 percent" crash-rate drop after Autosteer — DISCREDITED
Owner:  NHTSA PE16-007 (2017); disputed by Quality Control Systems (2019)
Scope:  43,781 MY2014-2016 Model S/X; airbag-deployment crashes per mile, all miles
        (not Autopilot miles); only ~5,714 vehicles had complete mileage data
```
```text
Figure: Tesla "first known fatality in just over 130 million miles" of Autopilot;
        US fatality ~every 94 million miles; worldwide ~every 60 million miles
Owner:  Tesla ("A Tragic Loss," 2016) — interested party; shares the exposure-data
        weakness of the 40% figure
Scope:  as of June 2016
```
```text
Figure: 2,031,220 vehicles recalled (23V-838), "100%" estimated to contain the defect
Owner:  Tesla Part 573 report, December 12, 2023
Scope:  all Autosteer-equipped MY2012-2023 S, 2016-2023 X, 2017-2023 3, 2020-2023 Y
```
```text
Figure: EA22-002 reviewed 956 crashes, analyzed 467; at least 13 fatal crashes tied
        to foreseeable misuse
Owner:  NHTSA EA22-002 (closed April 25, 2024)
Scope:  crashes reported through August 30, 2023
```
```text
Figure: six SAE J3016 levels, 0-5; Level 2 = "Partial Driving Automation"
Owner:  SAE International J3016
Scope:  taxonomy; at Levels 0-2 the human monitors the driving environment
```

## Source assets

```text
Asset: HAR-17/02, Figure 11 — timeline of the 41-minute Williston trip marking when
       the driver's hands were detected and where the visual/auditory warnings fired.
Shows: how little of the drive the driver touched the wheel (25 s of 37 min) and that
       no warning fired in the final approach.
Crop:  keep the time axis, the hands-detected bands, and the warning markers; keep the
       "approximate and relative" note so the timing is not read as exact.
```
```text
Asset: HAR-20/01, Figure 2 — diagram of the US-101 / SR-85 gore, travel lanes, and
       the attenuator the Model X struck.
Shows: how a lane-keeping system could follow the widening gore's left line straight
       into the barrier.
Crop:  retain the gore's neutral area, the diverging lane lines, and the attenuator
       position; the geometry is the point.
```
```text
Asset: HAR-20/01, Figure 12 — the last Autopilot segment with the two hands-off
       visual alerts and the escalation to an audible alert.
Shows: that the last alert came well before impact and nothing fired in the final
       seconds — torque monitoring missing the disengagement that mattered.
Crop:  keep both alert markers and the gap to impact.
```
```text
Asset: NHTSA PE16-007, Figure 3 — SAE's levels-of-automation chart, and Figure 11 —
       the before/after-Autosteer crash-rate bars behind the 40% claim.
Shows: Figure 3 grounds "Level 2"; Figure 11 is the image that launched a figure now
       discredited — usable only if captioned as disputed.
Crop:  Figure 11 must not be shown as a standing fact; pair it with the QCS rebuttal
       or omit it.
```
```text
Asset: Tesla Part 573 recall report 23V-838 — the defect and remedy text.
Shows: Tesla, in its own filing, conceding the controls "may not be sufficient to
       prevent driver misuse" across every Autosteer car.
Crop:  the defect sentence and the population line carry the argument in Tesla's words.
```

## Discarded

```text
URL: https://static.nhtsa.gov/odi/inv/2016/INOA-PE16007-7080.PDF — the PE16-007
     opening resume; superseded by the closing report already recorded.
URL: https://www.bloomberg.com/news/articles/2019-02-13/... — Bloomberg on the disputed
     40% figure; paywalled and redundant to The Drive's fuller account.
URL: https://spectrum.ieee.org/feds-call-teslas-autopilot-safe — IEEE Spectrum's
     January 2017 write-up of the 40% figure as fact; predates the rebuttal, so it
     documents the claim's launch but not its collapse. Not cited to avoid implying
     the figure stands.
URL: https://www.washingtonpost.com/.../ntsb-says-driver-in-fatal-tesla-crash... —
     WaPo on the 2017 finding; solid but redundant to the NTSB report read directly.
URL: https://saemobilus.sae.org/articles/level-2-taking-high-value-adas-mainstream-21avep01_03
     — SAE trade piece on "Level 2+"; marketing framing, not the J3016 definition.
URL: https://www.researchgate.net/publication/348447872_... — third-party discussion
     of the Mountain View findings; the primary report supersedes it.
```
