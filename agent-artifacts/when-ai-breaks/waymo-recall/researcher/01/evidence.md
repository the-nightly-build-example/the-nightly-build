# Evidence: when-ai-breaks/waymo-recall (01)

The record fully supports the spine of the commission and forces two factual
corrections to how the brief dates it. Both recalls are on the record as Waymo's
own Part 573 filings with NHTSA, and I read both filings in full: the towed-truck
recall (NHTSA 24E-013, 444 vehicles) and the pole recall (NHTSA 24E-049, 672
vehicles). The exact recall numbers, filing dates, vehicle counts, defect
descriptions, chronologies, and remedies below are quoted from those primaries.
The correction: the two towed-truck collisions happened on **December 11, 2023**
in Phoenix, not in February 2024; February 13, 2024 is the *filing* date. The
pole collision happened on **May 21, 2024**; June 10, 2024 is that filing's date.
Waymo's own Feb 13, 2024 blog post confirms the towed-truck account and cause in
the company's own words. The perception-vs-prediction distinction and
distribution shift are each pinned to an external authoritative source.

The evidence also refines the angle in one important way the editor must weigh:
the two recalls are **not** the same stage of the stack failing. The towed truck
was a **prediction** failure (the filing says the ADS "incorrectly predicted the
future motion"). The pole was a **perception-plus-mapping** failure (the filing
says the "perception system assigned a low damage score to the object" and the
map lacked a "hard road edge"). They share a class — rare configurations outside
what the system was built to expect — but not a failing module. That refines,
and does not break, the distribution-shift thesis; see Contradictions.

The floor is met: 8 sources, 6 primary, 2 secondary.

## Sources

```text
URL:         https://static.nhtsa.gov/odi/rcl/2024/RCLRPT-24E013-4528.PDF
Kind:        primary — Waymo's own Part 573 Safety Recall Report, the filing that owns the recall's numbers, defect, chronology, and remedy. Filed by the manufacturer under 49 CFR 573.
Establishes: The first recall. NHTSA Recall No. 24E-013; Manufacturer Recall No. "NR" (none assigned); Submission Date FEB 13, 2024; Manufacturer Waymo LLC (1600 Amphitheatre Parkway, Mountain View CA). Number potentially involved 444; estimated 100% with defect. Recalled equipment: "5th Generation Automated Driving System (ADS) prior to the 12/20/2023 driverless software release." Production dates MAR 17, 2022 - DEC 20, 2023. This is an EQUIPMENT recall (the "E" in 24E-013): the recalled item is the ADS software, not a vehicle model.
Paraphrase:  Defect: before the remedy, if a Waymo ADS encountered a vehicle being towed ahead of it where the towed vehicle's rearmost axle had a significant steer angle — so the towed vehicle sat at a persistent angle to the tow vehicle and did not track behind it — the ADS "may have incorrectly predicted the future motion of the towed vehicle," and if that towed vehicle was in the Waymo's path a collision could occur. Safety risk: "Incorrect prediction of the future motion of another vehicle may result in an increased risk of a collision." Chronology: on 12/11/2023 a Waymo AV operating in Phoenix, Arizona made contact with a pickup truck being towed backwards and at an angle; the tow truck was traveling straight in the middle shared turn lane while the towed pickup partially occupied the travel lane to its right; the Waymo's front left contacted the pickup; the tow truck did not stop; several minutes later a second Waymo AV contacted the same off-angle towed pickup, still occupying multiple lanes. Both were same-direction, low-relative-speed contacts; neither caused injuries. Waymo discussed the events with NHTSA on 12/15/2023, 12/20/2023, 1/17/2024, 2/5/2024, and 2/7/2024; the Safety Board decided to file on 2/7/2024. Remedy: between December 20, 2023 and January 12, 2024 Waymo updated the ADS in all affected vehicles via a new software release; Waymo owns all affected vehicles and has never sold them, so no owner/dealer notification was required.
Locators:    p.1 (header, population, equipment, defect); p.2 (safety risk, chronology start); p.3 (chronology end, remedy, recall schedule).
Quote:       "the Waymo ADS may have incorrectly predicted the future motion of the towed vehicle." / "On 12/11/2023 a Waymo AV operating in Phoenix, Arizona made contact with a pickup truck being towed backwards and at an angle relative to the towing vehicle." / "Several minutes later, a second Waymo AV made contact with the same off-angle towed pickup truck... Neither collision resulted in injuries."
```

```text
URL:         https://static.nhtsa.gov/odi/rcl/2024/RCLRPT-24E049-1733.PDF
Kind:        primary — Waymo's own Part 573 Safety Recall Report for the second recall.
Establishes: The second recall. NHTSA Recall No. 24E-049; Manufacturer Recall No. R24-002; Submission Date JUN 10, 2024; Manufacturer Waymo LLC. Number potentially involved 672; estimated 100% with defect. Recalled equipment: "5th Generation Automated Driving System (ADS) software prior to the 5/29/2024 driverless software release and map prior to the 6/4/2024 map update." Production dates MAR 17, 2022 - JUN 04, 2024. Two components named: 5th Gen ADS software and 5th Gen ADS map.
Paraphrase:  Defect: a collision could occur if the ADS met a pole or pole-like permanent object and all four held — (1) the object was within the road boundaries and the map lacked a hard road edge between the object and the drivable surface; (2) the perception system "assigned a low damage score to the object"; (3) the object was in the ADS's intended path (e.g., during a pullover near it); (4) no other nearby objects prompted the ADS to react and avoid. Safety risk: "Insufficient ability to avoid pole or pole-like permanent objects within the drivable surface may result in an increased risk of a collision." Chronology: on May 21, 2024 a Waymo AV operating in Phoenix, Arizona collided with a wooden utility pole in an alleyway while executing a low-speed pullover; no passengers, no other road users, no injuries, "some damage to the Waymo AV." Field Safety Committee began analysis May 22, 2024; developed two mitigations — a software update to improve response to pole-like objects, and mapping updates adding a hard road edge near such objects. Safety Board decided to file on June 5, 2024. Remedy: ADS software updated in all affected vehicles between 5/29/2024 and 6/3/2024; map updated so that by 6/6/2024 all affected vehicles ran the 6/4/2024-or-later map.
Locators:    p.1 (header, population, equipment); p.2 (defect four conditions, safety risk, components); p.3 (chronology, remedy).
Quote:       "the Waymo ADS's perception system assigned a low damage score to the object" / "the map did not include a hard road edge between the object and the driveable surface" / "On May 21, 2024, a Waymo AV operating in Phoenix, Arizona collided with a wooden utility pole located in an alleyway while executing a low-speed pullover maneuver. There were no passengers, other road users, or injuries associated with the event, and some damage to the Waymo AV."
```

```text
URL:         https://waymo.com/blog/2024/02/voluntary-recall-of-our-previous-software/
Kind:        primary — Waymo's own public account of the towed-truck events and the fix. Owns Waymo's framing ("voluntary recall") and its plain-language cause.
Establishes: Post dated February 13, 2024. Confirms: collisions on December 11, 2023 in Phoenix; two Waymo vehicles struck the same improperly towed, backwards-facing pickup truck that was "persistently angled across a center turn lane"; "no injuries and minor vehicle damage." Waymo's stated cause in plain words: "the Waymo AV incorrectly predicted the future motion of the towed vehicle." Waymo says it voluntarily filed the recall report with NHTSA and began deploying a software update to its fleet, completed by January 12, 2024.
Paraphrase:  Waymo frames the filing as voluntary and stresses the rarity of the towed-vehicle configuration. The company's own description of the failure matches the filing: a wrong prediction of where the towed truck would go.
Locators:    Blog post body (single page).
Quote:       "backwards-facing pickup truck being improperly towed ahead of the Waymo vehicle such that the pickup truck was persistently angled across a center turn lane" / "resulted in no injuries and minor vehicle damage."
```

```text
URL:         https://static.nhtsa.gov/odi/inv/2024/INOA-PE24016-12382.pdf
Kind:        primary — NHTSA Office of Defects Investigation opening resume (ODI RESUME) for Preliminary Evaluation PE24016. Owns the regulator's account of what it opened and why.
Establishes: Investigation PE24016 opened 05/13/2024; investigator Neil Dold, reviewer Scott Simmons, approver Tanya Topka. Subject: "Unexpected ADS behavior." Manufacturer Waymo LLC; product "Waymo 5th Generation automated driving system (ADS)"; population 444 (estimated). 22 incidents (17 crashes, 0 injuries, 0 fatalities at opening), reported under Standing General Order 2021-01 plus public-source non-crash reports. Problem: "ADS behavior causing single-party crashes and potential traffic safety law violations."
Paraphrase:  ODI opened a Preliminary Evaluation into the 5th-gen ADS covering collisions with stationary and semi-stationary objects (gates, chains, parked vehicles) and apparent violations of traffic control devices, and into similar scenarios. The estimated population (444) matches the driverless 5th-gen fleet size in the first recall. This is the same generation of ADS the recalls concern, but the investigation's scope is broader than the two recalled defects. NOTE: I read the OPENING resume only; the investigation's later status is from secondary reporting (see the Yahoo/Reuters entry) — it was CLOSED in 2025 after Waymo's recalls, with no further action.
Locators:    p.1 (header, population, failure summary, action); p.2 (scope, SGO reference); pp.2-3 (SGO report IDs).
Quote:       "ODI has received reports of 22 incidents involving Waymo vehicles equipped with Waymo's 5th generation automated driving system (ADS) wherein the ADS-equipped vehicle was the sole vehicle operated during a collision or wherein the ADS-equipped vehicle exhibited driving behavior that potentially violated traffic safety laws."
```

```text
URL:         https://arxiv.org/abs/2107.07455
Kind:        primary — the "Shifts" dataset paper (Malinin et al., arXiv:2107.07455, v1 Jul 2021, final Feb 2022; presented at NeurIPS 2021 Datasets & Benchmarks). It owns its claims about distributional shift and includes a self-driving-car vehicle motion prediction task built on real Yandex fleet data.
Establishes: An authoritative statement that distribution shift is not an edge case in autonomous driving but the normal condition, and a clean definition of the motion prediction task. Supports the commission's "distribution shift as why rare configurations break prediction" without re-teaching it (the library's distribution-shift lesson is the internal link; this is the external primary).
Paraphrase:  The paper presents benchmarks for robustness to distributional shift, including "self-driving car (SDC) vehicle motion prediction" affected by real distributional shifts. It states distributional shift is ubiquitous in the autonomous driving domain, arising for example when fleets begin operating in new locations, and that uncertainty quantification has life-critical application there because a vehicle can slow or hand off to a remote operator when confidence is low. It frames motion prediction as predicting the distribution over possible future states of the agents around the self-driving car.
Locators:    Abstract; Introduction / SDC task section.
Quote:       "distributional shift is ubiquitous in the autonomous driving domain" / "predicting the distribution over possible future states of agents around the self-driving car" / "Uncertainty quantification therefore has potentially life-critical application in this domain."
```

```text
URL:         https://arxiv.org/abs/2412.14088
Kind:        primary/authoritative — "Joint Perception and Prediction for Autonomous Driving: A Survey," Dal'Col, Oliveira & Santos (IEEE, arXiv:2412.14088, 2024). A peer-oriented survey that owns a clean, standard definition of the two modules and where they sit in the pipeline.
Establishes: The plain-words definitions the lesson needs for perception vs prediction, and the fact that they are traditionally separate, sequential modules whose errors propagate forward. Directly supports "define perception vs prediction; the towed truck broke the prediction step."
Paraphrase:  Perception perceives the environment (static and dynamic objects); prediction forecasts the future behavior of those objects; the work is typically split into object detection, object tracking, and motion prediction, developed independently with outputs passed sequentially from one to the next. The survey notes that in this sequential arrangement errors can amplify as they propagate through the pipeline — useful for explaining how a right detection can still yield a wrong outcome when prediction fails.
Locators:    Abstract; introduction.
Quote:       "The perception module is responsible for perceiving the environment, including static and dynamic objects, while the prediction module is responsible for predicting the future behavior of these objects. These modules are typically divided into three tasks: object detection, object tracking, and motion prediction. Traditionally, these tasks are developed and optimized independently, with outputs passed sequentially from one to the next."
```

```text
URL:         https://www.insurancejournal.com/news/national/2024/02/16/761144.htm
Kind:        secondary — Reuters wire report (David Shepardson), Feb 16, 2024, carried by Insurance Journal. Reports on the first recall from outside Waymo.
Establishes: Independent confirmation of the first recall's headline facts: 444 vehicles; two vehicles hit the same towed pickup within minutes in December 2023 in Phoenix; cause given as inaccurate prediction of the towed vehicle's movement; remedy already deployed Dec 20, 2023 - Jan 12, 2024. Confirms the media framing that would reach a general reader.
Paraphrase:  A repetition of the filing's facts by an established outlet. Supports that the recall was reported, and reported accurately, in the mainstream press. Does not add facts beyond the filing.
Locators:    Article body.
Quote:       (facts, not wording, are the evidence here) — count 444; cause "inaccurate prediction of towed vehicle movement."
```

```text
URL:         https://techcrunch.com/2024/06/12/waymo-second-robotaxi-recall-autonomous-vehicle/
Kind:        secondary — TechCrunch, June 12, 2024. Reports on the second recall and adds the vehicle model and a Waymo spokesperson quote.
Establishes: Independent confirmation of the second recall: 672 vehicles, described as "Jaguar I-Pace robotaxis"; pole collision on May 21 in Phoenix during a low-speed pullover; collision speed reported as 8 mph; explicitly Waymo's second recall, referencing the February 444-vehicle recall; Waymo remedy was a mapping and software update. Direct quote from Waymo spokesperson Katherine Barna.
Paraphrase:  Adds the vehicle model (Jaguar I-Pace) that the equipment filing does not name, and the reported 8 mph speed (not in the filing). Confirms the "second recall" framing and Waymo's plain-language account of insufficient ability to avoid narrow, permanent on-road objects.
Locators:    Article body.
Quote:       "We went to work immediately and determined that, in certain situations, our vehicles had insufficient ability to avoid collisions with on-road narrow, permanent objects" (Katherine Barna, Waymo spokesperson).
```

## Contradictions

- **Date framing (correction to the brief/commission).** The brief calls these
  "February 2024 towed-truck collisions" and the June recall "June 2024 pole
  collision." The filings are explicit: the towed-truck collisions were on
  **12/11/2023** (24E-013, p.2) and the pole collision was on **5/21/2024**
  (24E-049, p.3). February 13, 2024 and June 10, 2024 are the *filing/submission*
  dates. Waymo's own blog (Feb 13, 2024) also dates the collisions to Dec 11,
  2023. The writer must not write that the crashes happened in February or June.

- **The two recalls are different failing stages, not one recurring prediction
  bug.** The commission frames the pole recall as "a different rare object, same
  class of gap." The filings show the *class* is shared (rare configuration
  outside the trained distribution) but the *failing module* differs: 24E-013 is
  a **prediction** failure ("incorrectly predicted the future motion"), while
  24E-049 is a **perception + mapping** failure (perception "assigned a low
  damage score to the object"; the map lacked a "hard road edge"). This does not
  undercut the distribution-shift / long-tail thesis — both are tail cases the
  system was not built to expect — but it does contradict any sentence implying
  the same prediction weakness recurred at the pole. Handled honestly, it
  strengthens the perception-vs-prediction teaching: the two recalls are a
  natural worked example of the two stages failing separately. This is the
  record's most important nuance for the editor.

- **"Telephone pole" vs "utility pole."** The commission and much coverage
  (Gizmodo, TechCrunch) say "telephone pole." The primary filing says "wooden
  utility pole" (24E-049, p.3), and AZPM/CNBC say "pole." Use the filing's term.

- **Second-recall remedy is software AND map.** The commission's "issued a
  software update" is right for the first recall but incomplete for the second:
  24E-049 names two components (ADS software and ADS map) and two mitigations. Do
  not describe the pole fix as software-only.

- **No injuries in the two recalled events; a later, broader tally is not zero.**
  Both filings state no injuries, and the ODI opening resume shows 0 injuries at
  opening (22 incidents, 17 crashes). Secondary reporting on the *closure* of
  PE24016 in 2025 (Yahoo/Reuters; Self Drive News) says the investigation
  ultimately reviewed a much larger set — reported as 367 incidents including 109
  crashes and one injury — before closing with no action. Keep the register
  precise: the two recalled incidents caused no injuries; the one reported injury
  belongs to the wider investigation scope, not to the towed-truck or pole
  events. I did not read a closing ODI document firsthand; treat the closure
  figures as secondary.

- **Filing typo, do not propagate.** 24E-013 p.3 reads "On 2/7/2023, Waymo's
  Safety Board determined..." — a clear typo for 2/7/2024 (every other date in
  the chronology is late 2023 / early 2024, and the filing was submitted Feb 13,
  2024). If citing the Safety Board decision date, use 2/7/2024 and note the
  filing's slip if precision is challenged.

- No source contradicts Waymo's factual account of either event; no party
  disputes the vehicle counts or recall numbers. The disagreements above are of
  framing and precision, not of contested fact.

## Numbers

```text
Figure: 444 vehicles potentially involved (first recall)
Owner:  NHTSA Part 573 Report 24E-013, p.1 ("Number of potentially involved : 444")
Scope:  All 5th-gen ADS driverless-capable vehicles on software prior to the 12/20/2023 release; estimated 100% with defect. Waymo owns all of them; none sold.
```

```text
Figure: 672 vehicles potentially involved (second recall)
Owner:  NHTSA Part 573 Report 24E-049, p.1 ("Number of potentially involved : 672")
Scope:  All 5th-gen ADS driverless-capable vehicles on software prior to 5/29/2024 and map prior to 6/4/2024; estimated 100% with defect. Reported as Jaguar I-Pace (TechCrunch).
```

```text
Figure: 2 collisions with the same towed truck, minutes apart
Owner:  NHTSA 24E-013, p.2 chronology ("Several minutes later, a second Waymo AV made contact with the same off-angle towed pickup truck")
Scope:  Single event chain, Phoenix AZ, 12/11/2023; both same-direction, low relative speed; 0 injuries.
```

```text
Figure: ~8 mph pole collision speed
Owner:  Secondary only (TechCrunch / CNBC report 8 mph). NOT in the filing.
Scope:  The 5/21/2024 pole event; the filing says only "low-speed pullover" and "some damage to the Waymo AV." Attribute to reporting, not the filing.
```

```text
Figure: NHTSA recall numbers — 24E-013 (first), 24E-049 (second); manufacturer no. R24-002 for the second, none ("NR") for the first
Owner:  The two filings, p.1 each.
Scope:  Equipment recalls ("E") of the ADS, filed 2/13/2024 and 6/10/2024 respectively.
```

```text
Figure: PE24016 — 22 incidents, 17 crashes, 0 injuries at opening; population 444
Owner:  NHTSA ODI opening resume INOA-PE24016-12382, p.1
Scope:  5th-gen ADS, at investigation opening 5/13/2024. Later scope grew (secondary reporting) before closure in 2025 with no action.
```

```text
Figure: Third recall for context — 25E-034, ~1,212 vehicles (roadway barriers: chains, gates)
Owner:  Secondary (CNBC / TechCrunch, May 14, 2025); primary filing exists at https://static.nhtsa.gov/odi/rcl/2025/RCLRPT-25E034-2471.PDF (not read firsthand)
Scope:  Software prior to the 11/7/2024 release; 16 barrier collisions 2022-late 2024, no injuries; fix deployed by late Dec 2024. Use only as "where the weakness lives now," clearly marked as a separate, later recall.
```

## Source assets

```text
Asset: None found — the Part 573 filings are text-only forms with no diagrams, photos, or charts.
Shows: n/a
Crop:  n/a
```

The primary filings carry no visual evidence. If the lesson wants a diagram, it
would be an original explanatory graphic (perception -> prediction -> planning
pipeline, or the towed-truck geometry) built to the paper's chart/figure rules,
not a crop from a source. No public photo of either specific event is in the
primary record read here.

## Discarded

```text
URL: https://static.nhtsa.gov/odi/rcl/2024/RCLRPT-24E013-2218.PDF — alternate NHTSA-hosted copy of the same 24E-013 filing; I read and cite the -4528 copy instead. Same content.
URL: https://www.cnn.com/2024/06/13/business/waymo-recalls-driverless-cars-poles/index.html — returned HTTP 451 (geo-blocked); could not read firsthand, so not cited. Facts covered by TechCrunch/CNBC/AZPM.
URL: https://www.cnbc.com/2024/06/13/waymo-recalls-672-self-driving-vehicles-after-arizona-collision.html — returned HTTP 403; not read firsthand. TechCrunch used instead for the second recall.
URL: https://interestingengineering.com/... , https://gizmodo.com/... , https://www.wardsauto.com/... , https://news.azpm.org/... — redundant secondary coverage of the same recalls; not needed beyond Reuters and TechCrunch, which are sufficient and higher-confidence.
URL: https://arxiv.org/... (SAIL, AMD, CDKFormer, RiskNet, meta-learning long-tail papers) — recent, narrow method papers on long-tail trajectory prediction; the Shifts paper and the Dal'Col survey cover the concept authoritatively without over-citing niche methods.
URL: https://selfdrivenews.com/nhtsa-ends-waymo-ads-safety-probe/ and Yahoo/Reuters closure report — used only to note PE24016 closed in 2025 with no action and the later incident tally; the closing ODI document itself was not read firsthand, so the closure figures are recorded as secondary, not as verified primary numbers.
```
