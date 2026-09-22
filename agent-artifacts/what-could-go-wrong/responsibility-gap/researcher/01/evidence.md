# Evidence: what-could-go-wrong/responsibility-gap (01)

The evidence supports the commission's split cleanly. Matthias and Sparrow both
state the argument at full strength from the primary texts: responsibility needs
control and knowledge, learning systems remove them from the humans in the loop,
so no one qualifies. But in every real deployed case a human was held
responsible, through the ordinary control-and-knowledge test, and by design: the
Uber and Tesla systems were supervised systems that named a human operator as
the responsible party, so the gap Matthias imagined never opened. That is also
the record's sharpest limit on the angle. The deployed cases do not test
Matthias's scenario, because none involved a fully autonomous learning system
operating with no human assigned to supervise it; they involved SAE Level 2 or
developmental systems that required a human monitor. So "the stronger claim has
not held up" is well supported for legal and criminal responsibility and for
these systems, and unproven for the case Matthias and Sparrow actually described.
Two further findings cut against a tidy "law closed the gap" story: the EU's
dedicated AI Liability Directive was withdrawn in 2025, and the one instrument
that did pass (the revised Product Liability Directive) does not apply until
December 2026 and only to products. The primary "no gap" philosopher I read
(Tigard) concedes the moral gap is the hard one and that regulatory gaps are the
repairable kind, which is the opposite of the reassurance the angle reaches for.

## Sources

```text
URL:         https://link.springer.com/article/10.1007/s10676-004-3422-1
Kind:        primary. Matthias is the author who coined and owns the "responsibility gap" claim. (Read from an open copy hosted at eclass.uoa.gr; the article of record lives at the Springer DOI 10.1007/s10676-004-3422-1, Ethics and Information Technology 6(3):175-183, 2004.)
Establishes: The two classical conditions for responsibility (control and knowledge), and the argument that learning machines remove them from the operator and manufacturer, opening a gap traditional ascription cannot bridge.
Paraphrase:  A person can be held responsible only if she has control over her behaviour and its consequences "in a suitable sense," which means she knows the facts around her action and can freely choose among alternatives. We normally assign a machine's consequences to its operator as long as it runs to the manufacturer's specification, and to the manufacturer when it does not. Learning automata (neural nets, genetic algorithms, autonomous agents) change their own rules during operation from experience the maker never supplied, so neither operator nor manufacturer can predict or control the specific behaviour. Matthias defines the gap as the growing class of machine actions where "nobody has enough control over the machine's actions to be able to assume the responsibility for them," and closes by warning against "the injustice of holding men responsible for actions of machines over which they could not have sufficient control."
Locators:    Control/knowledge conditions, p.175 (PDF p.1). Neural nets as "black boxes," p.178. Gap defined, p.177 (PDF p.3). Conclusion, p.183.
Quote:       "the agent can be considered responsible only if he knows the particular facts surrounding his action, and if he is able to freely form a decision to act, and to select one of a suitable set of available alternative actions based on these facts" (p.175). "nobody has enough control over the machine's actions to be able to assume the responsibility for them. These cases constitute what we will call the responsibility gap" (p.177).
```

```text
URL:         https://robsparrow.com/wp-content/uploads/Killer-robots.pdf
Kind:        primary. Sparrow is the author of the trilemma; this is his own hosted copy of Journal of Applied Philosophy 24(1):62-77, 2007.
Establishes: The programmer / commander / machine trilemma for an autonomous weapon that commits an atrocity, and the jus in bello premise that someone must be justly holdable.
Paraphrase:  Sparrow stipulates an AI weapon that deliberately bombs surrendering soldiers with full knowledge, an act that would be a war crime if a human did it, and asks who to try. The programmer cannot fairly be held once the system is autonomous, because "the connection between the programmers/designers and the results of the system, which would ground the attribution of responsibility, is broken by the autonomy of the system." The commanding officer cannot fairly be held for actions of a machine "whose decisions they did not control." The machine cannot be held, because we cannot punish it: punishment requires that the object suffer, and we cannot imagine a machine suffering in a morally compelling way. Yet jus in bello requires that someone be holdable for each death, so deploying such systems is unethical. Sparrow himself believes machines will not meet the personhood conditions "for the foreseeable future."
Locators:    Trilemma set up, p.66-67. Programmer, p.69-70. Commanding Officer, p.70-71. Machine and punishment, p.71-73. Jus in bello condition, p.67-68. Impasse and conclusion, p.73-75.
Quote:       "the more these machines are held to be autonomous the less it seems that those who program or design them, or those who order them into action, should be held responsible for their actions" (p.66). "for the foreseeable future we will not be able to hold that machines are responsible for their actions" (p.73).
```

```text
URL:         https://www.ntsb.gov/investigations/accidentreports/reports/har1903.pdf
Kind:        primary. The NTSB is the investigating body and owns its probable-cause finding. Report NTSB/HAR-19/03, adopted November 19, 2019. Note: NTSB determines cause, not legal liability, and its report does not name the operator or the pedestrian.
Establishes: What the Uber ATG automated driving system did in the Tempe crash of March 18, 2018, and NTSB's assignment of cause to the human operator plus Uber ATG's safety culture.
Paraphrase:  A developmental Uber ATG automated driving system in a Volvo XC90 struck and killed a pedestrian crossing N. Mill Avenue outside a crosswalk. The system first detected the pedestrian 5.6 seconds before impact but never classified her as a pedestrian: it read her as a vehicle, then as "other" (unknown), then as a bicyclist, and did not predict her path or slow down. At 1.2 seconds before impact the system determined a collision was imminent, but its design "precluded emergency braking" and relied on the operator to take over; it also ran a 1-second "action suppression" period during which it withholds braking while it verifies the object and computes an alternative path. The operator was visually distracted, streaming a video on her phone, and looked up about 1 second before impact. NTSB's probable cause is the operator's failure to monitor because she was visually distracted, with contributing factors including Uber ATG's inadequate safety risk assessment, ineffective operator oversight, and inadequate safety culture, the pedestrian crossing outside a crosswalk while impaired, and Arizona DOT's insufficient oversight.
Locators:    Probable Cause and Findings, pp.v-viii (PDF pp.8-11). Detection, misclassification and braking timeline, pp.1-2 (PDF pp.13-14). Action suppression, section 1.5.5.3, p.~14 (PDF p.~24).
Quote:       "the system first detected the pedestrian 5.6 seconds before the crash. It initially classified the pedestrian as a vehicle, and subsequently also as an unknown object and a bicyclist" (p.1). "the design of the ATG ADS precluded emergency braking for crash mitigation alone" (p.1). Probable cause was "the failure of the vehicle operator to monitor the driving environment and the operation of the automated driving system because she was visually distracted throughout the trip by her personal cell phone" (p.v).
```

```text
URL:         https://maricopacountyattorney.org/m/newsflash/Home/Detail/751
Kind:        primary/official. The Maricopa County Attorney's Office is the charging authority; this is its own record of the indictment. (Companion record of the plea and sentence: https://maricopacountyattorney.org/m/newsflash/Home/Detail/1012)
Establishes: Who was criminally charged for the Tempe death, on what count, and the outcome, with dates. Confirms only the individual safety driver was charged, not Uber.
Paraphrase:  On August 27, 2020, a Maricopa County grand jury indicted the Uber safety driver, Rafael (aka Rafaela) Vasquez, on one count of negligent homicide (a felony) in the death of Elaine Herzberg on March 18, 2018. On July 28, 2023 Vasquez pleaded guilty to a reduced charge of endangerment, a class 6 undesignated offense, and was sentenced to three years of supervised probation; the office states the charge would be designated a misdemeanor on successful completion of probation.
Locators:    Indictment newsflash (Detail/751), dated August 27, 2020. Plea/sentence newsflash (Detail/1012), dated July 28, 2023.
Quote:       Plea record: "Endangerment, a Class 6 Undesignated Offense"; "Three years of supervised probation." Charging statement: "When a driver gets behind the wheel of a car, they have a responsibility to control and operate that vehicle safely and in a law-abiding manner" (County Attorney).
```

```text
URL:         https://www.ntsb.gov/Investigations/Accidentreports/Reports/Har1702.pdf
Kind:        primary. NTSB report NTSB/HAR-17/02 on the May 7, 2016 Williston, Florida Tesla Autopilot fatality, adopted September 12, 2017. Owns its probable-cause finding.
Establishes: NTSB's cause finding for the first known Tesla Autopilot death, and that it faulted the system's operational design for permitting driver disengagement, while assigning cause to human parties.
Paraphrase:  A Tesla Model S on Autopilot struck a tractor-semitrailer that turned across its path; neither the driver nor the system braked. NTSB's probable cause was the truck driver's failure to yield combined with the car driver's inattention due to overreliance on automation. It found a contributing factor in the car's operational design, which "permitted his prolonged disengagement from the driving task and his use of the automation in ways inconsistent with guidance and warnings from the manufacturer." Responsibility landed on the two drivers; the design was faulted but no party was found liable (NTSB makes no liability finding).
Locators:    Probable Cause, section 3.2, p.42. Operational design domain analysis, section 2.4, pp.32-33.
Quote:       "the truck driver's failure to yield the right of way to the car, combined with the car driver's inattention due to overreliance on vehicle automation" (p.42).
```

```text
URL:         https://static.nhtsa.gov/odi/inv/2022/INCLA-EA22002-14498.pdf
Kind:        primary/official. NHTSA Office of Defects Investigation closing resume for Engineering Analysis EA22-002, dated April 25, 2024. NHTSA is the safety regulator and owns the finding. (Related primary records: Tesla Recall 23V-838 Part 573 report, https://static.nhtsa.gov/odi/rcl/2023/RCLRPT-23V838-8276.PDF; Recall Query RQ24009, https://static.nhtsa.gov/odi/inv/2024/INIM-RQ24009-12199.pdf.)
Establishes: The regulator's recent, system-level finding on Tesla Autopilot: a "critical safety gap" between what drivers expected and what the system could do, and a recall of every Autopilot-equipped Tesla. This is the "who is held responsible today" evidence, and it lands on the manufacturer's controls rather than on an unlocatable gap.
Paraphrase:  ODI reviewed 467 crashes and found Autopilot's controls did not sufficiently ensure driver attention while the system's ease of engagement invited greater driver confidence. That mismatch of weak usage controls and high control authority "resulted in a critical safety gap between drivers' expectations of the L2 system's operating capabilities and the system's true capabilities," which "led to foreseeable misuse and avoidable crashes." ODI identified at least 13 crashes involving one or more fatalities in which foreseeable driver misuse played an apparent role. On December 12, 2023 Tesla filed a recall (23V-838) covering 2,031,220 vehicles, conceding "the prominence and scope of the system's controls may be insufficient to prevent driver misuse," with a software remedy. ODI closed EA22-002 and opened RQ24009 to test whether the remedy works. The Part 573 report states that when Autosteer is engaged "the driver is the operator of the vehicle" and is responsible for its movement.
Locators:    Close resume EA22-002: 467-crash breakdown and "critical safety gap," p.2 (PDF pp.2-3); at least 13 fatal crashes, p.3. Recall 23V-838: defect description and "driver is the operator," pp.2-3; population 2,031,220, p.1.
Quote:       "This mismatch resulted in a critical safety gap between drivers' expectations of the L2 system's operating capabilities and the system's true capabilities. This gap led to foreseeable misuse and avoidable crashes" (EA22-002 close resume, p.2). "the driver is the operator of the vehicle. As the vehicle operator, the driver is responsible for the vehicle's movement" (Recall 23V-838, p.2).
```

```text
URL:         https://eur-lex.europa.eu/eli/dir/2024/2853/oj/eng
Kind:        primary. Directive (EU) 2024/2853 (revised Product Liability Directive), the enacted EU legal instrument. Read from the authentic EUR-Lex text (CELEX 32024L2853); it lives at the EUR-Lex ELI address above.
Establishes: That EU no-fault product liability now expressly covers software and AI, keeps the maker liable for a product designed to develop unexpected behaviour, and lowers the claimant's burden with disclosure and rebuttable presumptions aimed at exactly the opacity/complexity the gap argument relies on.
Paraphrase:  Article 4 defines "product" to include software. Recital 44 says software, including AI systems, is a product for no-fault liability regardless of how it is supplied, and treats a software or AI developer as a manufacturer. Recital 82 states that "a manufacturer that designs a product with the ability to develop unexpected behaviour should remain liable for behaviour that causes harm," and that a maker keeps liability for machine-learning updates within its control (recital 118). Article 9 requires a defendant to disclose relevant evidence at its disposal to a claimant who has shown the claim is plausible. Article 10 presumes defectiveness where the defendant fails to disclose, breaches a mandatory safety requirement (including a requirement to log the product's operation), or where an obvious malfunction occurred; presumes the causal link where the damage is typical of the defect; and, under Article 10(4), presumes defectiveness or causation where the claimant faces "excessive difficulties, in particular due to technical or scientific complexity." Recital 114 names "machine learning" and "the inner workings of an AI system" as the complexity this is meant to address. The directive was adopted October 23, 2024 and applies to products placed on the market after December 9, 2026, the same date it repeals the 1985 directive.
Locators:    Definition of product, Article 4 (recital 44). Unexpected-behaviour liability, recital 82. Disclosure, Article 9(1). Presumptions, Article 10(2)-(4) (recital 114). Dates, Articles 17-18 and recital 144.
Quote:       "'product' means all movables ... it includes electricity, digital manufacturing files, raw materials and software" (Art. 4). "a manufacturer that designs a product with the ability to develop unexpected behaviour should remain liable for behaviour that causes harm" (recital 82). Article 10(4)(a): the presumption applies where "the claimant faces excessive difficulties, in particular due to technical or scientific complexity, in proving the defectiveness of the product or the causal link."
```

```text
URL:         https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:52022PC0496
Kind:        primary. The European Commission's proposal COM(2022) 496 final for an AI Liability Directive, September 28, 2022. Read from the authentic EUR-Lex text. This instrument was withdrawn; see the contradiction note.
Establishes: What the EU's dedicated AI-liability tool would have done, and that its central devices were disclosure and a rebuttable presumption of causation keyed to AI opacity, aimed straight at the gap.
Paraphrase:  The proposal eased the burden of proof for people harmed by AI in two ways. Article 3 let a court order a provider or user of a high-risk AI system to disclose or preserve relevant recorded evidence when a claimant showed a plausible claim, with a presumption of non-compliance if the order was ignored. Article 4 created a rebuttable "presumption of a causal link in the case of fault," so that once a claimant proved the defendant's fault and that the AI output (or failure to produce one) caused the damage, causation was presumed. For non-high-risk systems the presumption applied only where the court found it "excessively difficult" for the claimant to prove the link, difficulty assessed "in light of the characteristics of certain AI systems, such as autonomy and opacity." The defendant could rebut in each case.
Locators:    Disclosure, Article 3 and explanatory memorandum section 3. Presumption of causal link, Article 4 and explanatory memorandum section 4.
Quote:       Explanatory memorandum: "a targeted rebuttable presumption of causality has been laid down in Article 4(1) regarding this causal link." On non-high-risk systems: difficulties "assessed in light of the characteristics of certain AI systems, such as autonomy and opacity, which render the explanation of the inner functioning of the AI system very difficult in practice."
```

```text
URL:         https://link.springer.com/article/10.1007/s13347-020-00414-7
Kind:        primary. Daniel W. Tigard, "There Is No Techno-Responsibility Gap," Philosophy & Technology 34:589-607, 2021 (open access, CC-BY). Read the full paper from the German National Library CC-BY copy (d-nb.info/1217247998/34). This is the "no gap" rebuttal.
Establishes: A direct primary rebuttal of Matthias, arguing the gap does not exist because responsibility is plural, and, importantly, conceding that the legal/regulatory gap is the repairable kind while the moral gap is the hard one.
Paraphrase:  Tigard argues against both camps in the literature, the "techno-pessimists" who would halt AI and the "techno-optimists" who try to bridge the gap, holding instead that there is no techno-responsibility gap at all. He draws on pluralist theories of responsibility (Strawson's reactive attitudes; Watson's and Shoemaker's "faces" of responsibility) to distinguish attributability, answerability, and accountability. Matthias and the pessimists, he says, reduce responsibility to accountability, and the worry about blurred responsibility "is mostly about accountability"; but we can still attribute values to a technology and demand answers about it, so responsibility, "as a dynamic and flexible process, can effectively encompass emerging technological entities." He explicitly separates moral responsibility from legal liability and says the regulatory kind is fixable: "regulatory gaps can in principle be repaired with new regulation ... while potential gaps in moral responsibility are far less clear, and thereby less easily resolved."
Locators:    Thesis and the pessimist/optimist framing, pp.589-591 (PDF pp.1-3). Moral vs regulatory gap, pp.590-591. Pluralism and the three faces, pp.598-600 (PDF pp.10-11).
Quote:       "I will argue that there is no techno-responsibility gap" (p.591). "regulatory gaps can in principle be repaired with new regulation ... while potential gaps in moral responsibility are far less clear, and thereby less easily resolved" (p.590).
```

```text
URL:         https://www.npr.org/2019/03/06/700801945/uber-not-criminally-liable-in-death-of-woman-hit-by-self-driving-car-says-prosec
Kind:        secondary. NPR reporting on the Yavapai County Attorney's decision. Used only to establish that the decision was made; the primary is Yavapai County Attorney Sheila Polk's March 5, 2019 letter to the Maricopa County Attorney, which I could not obtain as a document.
Establishes: That the corporation, Uber, was found to have no basis for criminal liability, so no company was charged for the Tempe death; the matter was referred back for further review of the individual driver.
Paraphrase:  In March 2019 the Yavapai County Attorney's office, handling the case for conflict reasons, determined there was no basis for criminal liability for Uber and referred the question of the safety driver back to Tempe police for further investigation.
Locators:    NPR report, March 6, 2019.
Quote:       None; the wording that carries evidentiary weight is in Polk's letter, which I did not read directly.
```

```text
URL:         https://iapp.org/news/a/european-commission-withdraws-ai-liability-directive-from-consideration
Kind:        secondary. Reporting on the withdrawal of the AI Liability Directive. The primary is the Commission's 2025 Work Programme (COM(2025) 45, February 11, 2025), whose annex lists the proposal for withdrawal; I did not obtain that annex as a document.
Establishes: That the AI Liability Directive proposal (COM(2022) 496) was withdrawn by the Commission in 2025 for lack of foreseeable agreement, leaving the revised Product Liability Directive as the operative instrument.
Paraphrase:  On February 11, 2025 the European Commission listed the AI Liability Directive among proposals to be withdrawn, citing no foreseeable agreement among the co-legislators, and signalling it would assess whether a different approach was needed.
Locators:    IAPP report, February 2025.
Quote:       Commission annex, as reported: "No foreseeable agreement — the Commission will assess whether another proposal should be tabled or another type of approach should be chosen."
```

## Contradictions

- The deployed cases do not test the Matthias/Sparrow scenario, which weakens the
  angle where it is stated most strongly. Matthias's gap opens only when no human
  has the control and knowledge to be responsible. In both real cases a human did:
  the Uber system was developmental and the Tesla system is SAE Level 2, and both
  by design named a human operator as responsible and required them to supervise.
  NTSB (HAR-19/03) and NHTSA (Recall 23V-838) both state the human was the
  responsible monitor. So courts and regulators assigned responsibility partly
  because these were not autonomous-with-no-human systems. The record shows the
  stronger "no one can be held" claim failing in practice, but not in the case its
  authors built it for.

- Against the commission's "law dissolves the gap" leg: the EU's dedicated AI
  liability tool was withdrawn in 2025 (COM(2022) 496), and the instrument that
  passed (PLD 2024/2853) does not apply until December 9, 2026 and only to
  "products." Pure AI services, standalone algorithmic decisions that are not
  products, and harms outside product liability are not covered by it. The claim
  that liability law has closed the gap is true for a narrower slice, and later in
  time, than a confident statement would imply.

- Tigard, the primary "no gap" rebuttal, contradicts the easy version of the angle
  from the other side. He grants that the regulatory gap is the repairable one and
  that the moral gap is "far less clear, and thereby less easily resolved." So the
  strongest scholarly denial of the gap concedes that pointing at liability law
  does not answer Matthias's core (moral) claim. The angle should keep legal and
  moral responsibility separate; the evidence closes the legal question much more
  firmly than the moral one.

- NTSB is not a court or a liability authority. Its "probable cause" for Uber and
  Tesla assigns causation and safety fault, not legal responsibility. Treating an
  NTSB finding as "who was held responsible" would overstate it. The actual
  responsibility outcomes are the criminal record (Vasquez charged and convicted of
  a reduced count; Uber not charged) and the regulatory recall (Tesla), not the
  NTSB reports.

- Diffuse responsibility is visible in the Uber case and supports the "design
  problem / many hands" half of the contribution. NTSB found Uber ATG's inadequate
  safety culture a contributing cause, yet the corporation faced no criminal
  charge, and the only person prosecuted was the individual monitor, who received
  probation. The party NTSB faulted most at the organizational level bore the least
  individual accountability.

## Numbers

```text
Figure: 5.6 seconds - time before impact the Uber ADS first detected the pedestrian
Owner:  NTSB/HAR-19/03
Scope:  single crash, Tempe, March 18, 2018; from first detection to impact
```
```text
Figure: never classified as a pedestrian (read as vehicle, then unknown/"other", then bicyclist)
Owner:  NTSB/HAR-19/03
Scope:  same crash; the ADS classification sequence over the 5.6 seconds
```
```text
Figure: 1.2 seconds - time before impact the ADS determined a collision was imminent, at which point its design precluded emergency braking and relied on the operator
Owner:  NTSB/HAR-19/03
Scope:  same crash
```
```text
Figure: 1 second - duration of the ADS "action suppression" period during which braking is withheld while the object is verified
Owner:  NTSB/HAR-19/03
Scope:  ATG ADS design behaviour, section 1.5.5.3
```
```text
Figure: 3 years of supervised probation (guilty plea to endangerment, class 6 undesignated), reduced from one count of negligent homicide
Owner:  Maricopa County Attorney's Office
Scope:  Rafaela Vasquez; indicted August 27, 2020; plea/sentence July 28, 2023
```
```text
Figure: 467 crashes reviewed; at least 13 involving one or more fatalities
Owner:  NHTSA ODI, EA22-002 close resume
Scope:  Tesla Autopilot investigation PE21-020/EA22-002, closed April 25, 2024
```
```text
Figure: 2,031,220 vehicles recalled
Owner:  NHTSA / Tesla Recall 23V-838
Scope:  all Autopilot-equipped Teslas, MY 2012-2023, filed December 12, 2023
```
```text
Figure: Tesla Autopilot crash speed 74 mph; hands detected on the wheel for 25 seconds of the 37 minutes on Autopilot
Owner:  NTSB/HAR-17/02
Scope:  Williston, Florida, May 7, 2016 (figures cited from the report's factual findings)
```
```text
Figure: applies to products placed on the market after 9 December 2026; adopted 23 October 2024
Owner:  Directive (EU) 2024/2853
Scope:  EU revised Product Liability Directive; transposition deadline and application date
```

## Limits

- I could not obtain the two underlying primary legal decisions as documents: the
  Yavapai County Attorney's March 5, 2019 letter declining to charge Uber, and the
  European Commission's 2025 Work Programme annex withdrawing the AI Liability
  Directive. Both facts are established through reputable secondary reporting and
  are not in dispute, but the writer should present them as decisions reported, not
  as documents I read, and the editor should treat the exact rationale wording as
  second-hand.
- The Tesla Williston speed and hands-on-wheel figures are cited here from the NTSB
  report's factual narrative; I read the probable-cause and operational-design
  sections in full but did not transcribe the factual-section page for each figure.
  If the article leans on the 25-seconds-of-37-minutes figure, the writer should
  land it on the specific factual paragraph before publishing.
- I did not pursue the civil settlements (Uber reportedly settled with Herzberg's
  family in 2018; multiple Tesla wrongful-death suits are ongoing). The commission
  asked about who was "held responsible," and civil liability is part of that
  picture; I have criminal and regulatory outcomes firmly and civil outcomes not at
  all. If the article wants to claim liability law actually delivered compensation,
  that leg is unsupported in this record.
- The commission's "strict or vicarious liability regardless of a blameworthy mind"
  point is supported at the level of the EU instruments (no-fault product liability
  extended to software) but I did not read a US strict-liability case or a
  common-law vicarious-liability authority applied to an autonomous system. The
  doctrine claim is grounded in the EU primary sources; a US doctrinal claim would
  need its own source.
- Everything the commission named as a must-open primary was opened and read in
  full: Matthias, Sparrow, both NTSB reports, the Maricopa charging and plea
  records, the NHTSA Autopilot findings, the PLD and the withdrawn AILD, and a
  primary "no gap" rebuttal (Tigard). The source minimums are met (nine primary
  sources read, two secondary).

## Source assets

```text
Asset: NTSB/HAR-19/03, Figure 1 (p.2, PDF p.14) - aerial view of the crash site with the pedestrian's path from first detection to impact and the SUV's position and speed at three points before impact.
Shows: The whole failure in one image - the system had 5.6 seconds and a clear line, and neither the machine nor the distracted monitor acted. Carries the "there was time" point better than prose.
Crop:  Must retain the pedestrian path, the three SUV positions with times/speeds, and the "no crosswalk" location. Omit nothing load-bearing; do not crop to just the impact point, which loses the time margin.
```
```text
Asset: NTSB/HAR-19/03, the object-classification timeline table (section 1.6, PDF pp.16-17) listing times before impact against classification (vehicle / other / bicyclist) and predicted path.
Shows: In the system's own logged labels, that it never saw a pedestrian. Concrete evidence for the "opacity / misclassification" design-problem half of the contribution.
Crop:  Keep the time column and the classification column together; a crop that drops the times makes the sequence unreadable.
```
```text
Asset: NHTSA EA22-002 close resume (p.2), the 467-crash breakdown into three categories (211 frontal-plane strikes with time to respond; 111 inadvertent Autosteer disengagements; 145 low-traction roadway departures).
Shows: The regulator's own decomposition of how Autopilot crashes happened, and that most involved a driver who could have responded. Supports the "controls, not an unlocatable gap" reading.
Crop:  A three-part bar or the raw counts beside the "critical safety gap" sentence; retain the category labels, which carry the meaning.
```
```text
Asset: Directive (EU) 2024/2853 and COM(2022) 496 - text instruments only.
Shows: None found. No visual carries these better than a short quotation of the article text.
Crop:  n/a
```

## Discarded

```text
URL: https://link.springer.com/content/pdf/10.1007/s10676-004-3422-1.pdf - Springer's Matthias PDF is bot-blocked and returns a challenge page; read the same article from the open eclass.uoa.gr copy instead.
URL: https://www.academia.edu/47804984/ - academia.edu returns 403 and requires login; not a readable source route.
URL: https://www.proquest.com/openview/6e2182a373e2b0b9bab1a63c08d6e131/1.pdf - ProQuest openview redirects to a login lander; not the document.
URL: https://www.cnbc.com/2024/04/26/tesla-autopilot-... - CNBC coverage of the NHTSA "critical safety gap" finding; read the primary EA22-002 close resume instead, so this adds nothing.
URL: https://en.wikipedia.org/wiki/Death_of_Elaine_Herzberg - useful for orientation and dates, but every fact it carries is available from the NTSB report and the Maricopa County records, which own the claims.
URL: https://www.twobirds.com/... and other law-firm client alerts on PLD 2024/2853 - accurate summaries, but the directive text itself is the primary and was readable, so the alerts are not cited.
```
