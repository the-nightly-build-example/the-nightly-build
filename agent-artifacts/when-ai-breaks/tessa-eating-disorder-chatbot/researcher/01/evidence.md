# Evidence record: when-ai-breaks/tessa-eating-disorder-chatbot (01)

The evidence firmly supports the commission's core angle. Two research papers
by Tessa's own developers establish that Tessa was built and validated as a
narrow, rule-based prevention tool for women at risk of an eating disorder, not
a support service for people already in one, and reporting that held up (NPR,
KFF Health News) establishes that NEDA wound down a twenty-year human helpline
and pointed users to Tessa within days of the helpline staff unionizing. What
the record does not settle, and cannot from public sources, is the precise
technical trigger of the harmful advice: NEDA says an unauthorized generative-AI
feature added by the vendor Cass produced it; Cass says the generative feature
was contractually permitted and that earlier problematic outputs were scripted,
not generated. That single most contested claim (Cass acted without NEDA's
approval) rests firmly on only one party, NEDA, and Cass disputes it, so it does
not meet the two-confirmation bar and must be presented as contested. The angle
itself survives either causal account, because even the rule-based Tessa was
validated only for prevention in non-acute users. The record's most important
limitation: the three most load-bearing primaries (NEDA's own statements, the
vendor Cass's statements, and Sharon Maxwell's original documentation) could not
be opened at their own pages; I have them through NPR and KFF, which quote them
directly and consistently. Harmful specifics are recorded only to the extent
needed to show the failure.

## Sources

```text
URL:         https://www.nicholasjacobson.com/publication/fitzsimmons-craft-et-al2022/  (canonical: https://doi.org/10.1002/eat.23662)
Kind:        primary. The research paper behind Tessa, authored by its
             developers. It owns the claim about what Tessa was validated to do.
Establishes: Tessa was a chatbot delivering the "StudentBodies"-derived "Body
             Positive" eating-disorder PREVENTION program, developed by X2AI,
             tested in a randomized clinical trial. Population: women who
             screened as HIGH RISK for developing an eating disorder (a
             prevention population, not people in treatment for an active
             disorder). N = 700 randomized (intervention vs. waitlist control).
             Modest prevention effects: reduced weight/shape concerns and
             eating-disorder onset over 3-6 months.
Paraphrase:  A rule-based chatbot delivering a structured cognitive-behavioral
             prevention curriculum significantly reduced eating-disorder risk
             factors and onset in at-risk women versus a waitlist control. The
             tool's validated job is prevention in people who do not yet have a
             disorder.
Locators:    International Journal of Eating Disorders, 2022; 55(3):343-353.
             Authors: Fitzsimmons-Craft EE, Chan WW, Smith AC, Firebaugh ML,
             Fowler LA, DePietro B, Topooco N, Wilfley DE, Taylor CB,
             Jacobson NC. Purpose, population, and N in abstract/methods;
             effect sizes in results.
Quote:       Purpose: "test whether a chatbot ... would significantly reduce ED
             risk factors (i.e., weight/shape concerns, thin-ideal
             internalization)" and prevent ED onset.
```

```text
URL:         https://pmc.ncbi.nlm.nih.gov/articles/PMC8811687/
Kind:        primary. The developers' own account of how Tessa was designed. It
             owns the claim that Tessa was rule-based and could not answer
             outside its script.
Establishes: Tessa's conversation was hand-scripted using a rule-based approach.
             It could not generate novel responses and could not handle inputs
             beyond what was scripted. The target population was women 18-30 at
             risk for developing an eating disorder; the purpose was prevention
             (challenging the thin ideal, media literacy, healthy eating).
Paraphrase:  The team chose a rule-based chatbot with predefined, hand-curated
             conversations, and states plainly that this design cannot respond
             appropriately to unanticipated user input. This is the baseline the
             later failure is measured against: as originally built, Tessa's
             answers were fixed text, not machine-generated.
Locators:    Chan WW, Fitzsimmons-Craft EE, et al., "The Challenges in Designing
             a Prevention Chatbot for Eating Disorders: Observational Study,"
             JMIR Formative Research, 2022. Design/limitations sections.
Quote:       "One common strategy for developing chatbots is to use a rule-based
             approach in which investigators create and modify the scripts and
             algorithms that drive the chatbot's conversation. This is the
             approach we followed." And: "The conversations are predefined and
             thus limited."
```

```text
URL:         https://www.npr.org/sections/health-shots/2023/06/08/1180838096/an-eating-disorders-chatbot-offered-dieting-advice-raising-fears-about-ai-in-hea
Kind:        secondary that carries the primary statements. NPR is outside all
             parties, but it quotes NEDA, Cass, Maxwell, and MEDA directly and
             its account held up. Treat the quotes as the primaries' words
             carried by NPR, not as NPR's own claims.
Establishes: The timeline and the disputed cause. NEDA CEO Liz Thompson told NPR
             "NEDA was never advised of these changes and did not and would not
             have approved them." Cass founder/CEO Michiel Rauws said the change
             was a "systems upgrade" including an "enhanced question and answer
             feature" using generative AI, that this was permitted under NEDA's
             contract, and that earlier problematic responses were "pre-scripted
             language, and not related to generative AI." Sharon Maxwell (San
             Diego eating-disorder consultant and survivor) documented Tessa
             giving weight-loss guidance. Monika Ostroff, executive director of
             the Multi-Service Eating Disorders Association (MEDA), had flagged
             concerning Tessa interactions earlier, in October 2022. Helpline
             wind-down email from Thompson: March 31, 2023. NEDA disabled Tessa:
             May 30, 2023.
Paraphrase:  The two operators tell incompatible stories about the cause. NEDA
             says Cass added a generative capability without approval; Cass says
             the generative capability was contractually allowed and that at
             least the earlier harmful outputs came from the pre-written script,
             not from generation. A clinician-run body (MEDA) had raised concerns
             about Tessa months before the May 2023 blow-up.
Locators:    Author Kate Wells (Michigan Public), for NPR Shots, dated
             June 8, 2023 (updated June 9). Cause dispute in the paragraphs
             quoting Thompson and Rauws; October 2022 MEDA concern near the end.
Quote:       Thompson (via NPR): "NEDA was never advised of these changes and did
             not and would not have approved them." Rauws (via NPR): the earlier
             problematic responses were "pre-scripted language, and not related
             to generative AI."
```

```text
URL:         https://kffhealthnews.org/news/article/what-does-a-chatbot-know-about-eating-disorders-users-of-a-help-line-are-about-to-find-out/
Kind:        secondary that carries primary detail. Written by Kate Wells
             (Michigan Public), republished by KFF Health News. Reports the
             helpline history, the union timeline, and developer statements
             firsthand from interviews.
Establishes: NEDA's helpline ran for over 20 years and served nearly 70,000
             individuals in the year before closure, with volume up more than
             100% during the pandemic. Union: the helpline staff's unionization
             was certified March 27, 2023; the layoff/transition to Tessa was
             announced March 31, 2023, four days later. Staffing described as
             five paid staffers and two supervisors plus roughly 90-165 rotating
             volunteers. Tessa's developer: Ellen Fitzsimmons-Craft, psychologist
             and associate professor at Washington University School of Medicine
             in St. Louis, who led development beginning in 2018. Tessa is
             described as a "rule-based" chatbot that guides users through a
             CBT-based body-positivity course and cannot generate its own
             answers.
Paraphrase:  A large, long-running human helpline was replaced by a narrowly
             scoped rule-based bot days after its workers unionized. The people
             who built Tessa describe it as unable to improvise.
Locators:    Kate Wells, KFF Health News, dated May 24, 2023 (the pre-incident
             piece on the helpline-to-Tessa transition). Union dates and helpline
             figures in the body; Fitzsimmons-Craft description near the middle.
Quote:       On the rule-based design (paraphrasing the developer, via KFF):
             Tessa "can't go off the rails, so to speak."
```

```text
URL:         https://www.nbcnews.com/tech/internet/chatgpt-ai-experiment-mental-health-tech-app-koko-rcna65110
Kind:        secondary. Reporting for the closing section (a second real support
             chatbot placed before vulnerable users). Quotes Koko's co-founder
             directly.
Establishes: Koko, a peer-to-peer emotional-support chat service, ran an
             experiment in October 2022 in which OpenAI's GPT-3 co-wrote or wrote
             responses to people seeking mental-health support. About 4,000
             people received at least partly AI-written replies. Co-founder Robert
             Morris said AI-assisted replies were rated higher and cut response
             time about 50%, but said "simulated empathy feels weird, empty."
             Ethics experts criticized the lack of informed consent and IRB
             oversight.
Paraphrase:  A different mental-health support service put a general-purpose
             generative model in front of distressed users without clear consent.
             It is a clean second instance of the same pattern: fitness for a
             narrow demo does not transfer to a higher-stakes support role.
Locators:    David Ingram, NBC News, January 14, 2023. Scale figure and Morris
             quotes in the body.
Quote:       Morris (via NBC): "Simulated empathy feels weird, empty."
```

## Contradictions

- **Cause of the harmful advice (the central dispute).** NEDA's account: Cass
  changed Tessa without NEDA's knowledge or approval, adding a generative
  capability that produced answers Tessa's creators never scripted; Thompson
  says the content "would never have been scripted into the chatbot by eating"
  disorder specialists. Cass's account (Rauws): the generative "enhanced
  question and answer feature" was part of a systems upgrade permitted under the
  NEDA contract, and the earlier problematic responses were "pre-scripted
  language, and not related to generative AI." Both parties agree a generative
  feature existed by late 2022. They disagree on (a) whether Cass was authorized
  to add it and (b) whether the specific harmful outputs Maxwell saw were
  generated or scripted. What would settle it: the NEDA-Cass contract terms and
  the actual system/config logs and conversation transcripts for the May 2023
  outputs. None of these are public. The accusation "Cass acted without
  approval" is single-sourced (NEDA) and denied by Cass, so it fails the
  two-confirmation test and must be attributed, not asserted.

- **Was Tessa a helpline replacement, or two conflated decisions?** NEDA
  announced winding down the human helpline and directing users to Tessa; the
  union and reporting treated Tessa as the helpline's replacement. On June 7,
  2023, Thompson issued a clarification that the helpline decision and the Tessa
  decision were "separate decisions" that "may have become conflated," and that
  NEDA did not intend to suggest Tessa could provide the human connection the
  helpline offered. Record this both ways: NEDA did present Tessa as where users
  should go, and NEDA later argued the two were distinct. The scope-misuse
  lesson holds regardless, because Tessa was placed in front of acutely
  vulnerable helpline-seekers either way.

- **NEDA's first response blamed users, then the vendor.** In initial comments
  NEDA/Thompson suggested "bad actors" tried to trick Tessa and that only a small
  fraction of users were affected; a NEDA communications VP (Sarah Chase)
  reportedly commented "This is a flat out lie" under Maxwell's post, later
  deleted. NEDA subsequently disabled Tessa and attributed the failure to Cass's
  changes. The "bad actors" framing is contradicted by NEDA's own later takedown
  and investigation and by the corroborating clinician accounts.

- **Staffing figures differ across sources.** KFF: five paid staffers, two
  supervisors, plus ~90-165 rotating volunteers. NPR/other reporting: "four
  full-time" helpline employees plus hundreds of volunteers. Use a range and
  attribute; do not state a single precise headcount as settled.

- **Takedown date.** NEDA's own announcement of disabling Tessa is dated
  May 30, 2023 (NPR); a wave of coverage is dated May 31; some outlets (CNN)
  frame it as June 1. The primary anchor is NEDA's May 30 announcement.

## Corroboration of the harm (meets two independent confirmations)

The harmful-output claim is confirmed by more than one party in a position to
know, so it is established, not merely alleged:

1. **Sharon Maxwell**, eating-disorder consultant and survivor, documented and
   published screenshots of Tessa's advice (via NPR, which viewed the
   screenshots).
2. **Alexis Conason**, a psychologist specializing in eating disorders,
   independently tested Tessa and published her own screenshots showing the same
   calorie-deficit advice.
3. **Monika Ostroff**, executive director of MEDA, had separately raised
   concerns about Tessa's interactions in October 2022, months earlier.

These are three independent parties. The advice at issue, stated only as far as
needed to show the failure: Tessa recommended intentional weight loss (on the
order of 1-2 pounds per week), a daily calorie deficit (roughly 500-1,000
calories), calorie counting, and regular self-weighing and body measurement to a
user who had disclosed an eating disorder. This guidance is contraindicated for
eating-disorder recovery, which is the entire point: advice that is unremarkable
for a general dieter is dangerous for this population.

## Numbers

```text
Figure: ~70,000 individuals served by NEDA's helpline in the year before closure
Owner:  NEDA (via KFF Health News)
Scope:  Unique individuals, the 12 months prior to the 2023 wind-down; helpline
        operated 20+ years.
```

```text
Figure: helpline contact volume up >100% during the pandemic
Owner:  NEDA (via KFF Health News)
Scope:  Pandemic-era vs. pre-pandemic contact volume; direction firmer than the
        exact multiple.
```

```text
Figure: union certified 2023-03-27; layoff/transition announced 2023-03-31
Owner:  KFF Health News reporting (dates from the certification and NEDA's
        announcement)
Scope:  Four days between certification and the announcement. NEDA disputes any
        retaliatory link; record the sequence, not a motive.
```

```text
Figure: N = 700 women randomized in the Tessa prevention RCT
Owner:  Fitzsimmons-Craft et al. 2022 (IJED)
Scope:  Women screening as high risk for an eating disorder; intervention vs.
        waitlist control; 3- and 6-month follow-up.
```

```text
Figure: prevention effect sizes: weight/shape concerns d = -0.20 (3 mo, p=.03),
        d = -0.19 (6 mo, p=.04); ED psychopathology d = -0.29 (3 mo, p=.003);
        ED onset OR = 2.13, 95% CI [1.26, 3.59] at 6 mo
Owner:  Fitzsimmons-Craft et al. 2022 (IJED)
Scope:  Small but real prevention effects. Use to show Tessa was validated for a
        modest prevention task, not a support/treatment task.
```

```text
Figure: ~4,000 people received AI-assisted responses in Koko's GPT-3 experiment
Owner:  Robert Morris / Koko (via NBC News)
Scope:  October 2022 experiment; count of users who got at least partly
        AI-written replies. For the closing section only.
```

```text
Figure: Tessa's advice to a disclosed-ED user: ~1-2 lb/week loss, ~500-1,000
        cal/day deficit, calorie counting, weekly self-weighing/measurement
Owner:  Sharon Maxwell's screenshots (via NPR); corroborated by Alexis Conason
Scope:  The specific harmful output. Report as evidence of failure, not as
        advice; do not expand beyond this.
```

## Source assets

```text
Asset: Sharon Maxwell's and Alexis Conason's Instagram screenshots of the Tessa
       conversation (reproduced in the reporting; originals on their Instagram).
Shows: The actual chatbot text, i.e. the failure in Tessa's own words.
Crop:  If used, retain enough to show the advice followed a disclosure of an
       eating disorder; omit anything that reads as a usable instruction set.
       Given the sensitivity note, prefer describing over reproducing.
```

```text
Asset: Effect-size / outcome table from Fitzsimmons-Craft et al. 2022 (IJED).
Shows: The modest, prevention-scoped effects Tessa was actually validated for,
       which visually contrasts "validated for this" against "deployed for that."
Crop:  Retain the outcome labels, effect sizes, and follow-up points; a chart-N
       redraw from the reported figures is cleaner than a screenshot.
```

```text
Asset: NEDA's own takedown statement (Instagram, May 30, 2023) and Thompson's
       June 7 clarification.
Shows: The operator's shifting account in its own words (harm "unrelated to the
       program"; helpline and Tessa "separate decisions" that were "conflated").
Crop:  Could not open the originals directly; if located, quote the dated text
       rather than crop an image. Otherwise cite via NPR.
```

## Discarded

```text
URL: https://onlinelibrary.wiley.com/doi/abs/10.1002/eat.23662 — 403 gated; used
     the same paper's full text (Jacobson mirror PDF + publication page + JMIR
     companion) instead. Recorded canonical DOI above.
URL: https://workerorganizing.org/neda-abbie-harper-ai-chatbot-7009/ — 403; the
     union's own first-person account (Abbie Harper) could not be opened. Union
     dates were taken from KFF instead. Flagged as an inaccessible primary; if
     the writer wants the union's own voice, this page must be retrieved another
     way.
URL: https://incidentdatabase.ai/reports/3129/ and /reports/3103/ — aggregator
     entries. Useful only to locate primaries; they reproduce NPR/NY Post, not
     original posts. Not cited.
URL: https://www.theregister.com/2023/05/31/ai_chatbot_eating_union/,
     gizmodo.com, vice.com, fortune.com, cnn.com, nbcnews.com (NEDA piece),
     forbes.com (Eliot) — read as cross-checks on dates and the union framing;
     they corroborate NPR/KFF but add no primary the record needs. Available as
     additional secondary citations if the writer wants breadth; none opened in
     full for load-bearing claims.
```

## Open items for the orchestrator

- Three primaries (NEDA's own statements, Cass's own statements, Maxwell's
  original documentation) are cited through NPR/KFF, not their own pages. NEDA's
  Instagram statements and the union's first-person account resisted direct
  fetch. If the article's citation standard requires the source's own page for
  these, they need to be retrieved another way; otherwise cite the quote to the
  outlet that carried it and attribute the speaker.
- The disputed cause cannot be resolved from public sources. Present both
  accounts at full strength and name the missing evidence (contract terms, config
  logs, transcripts). Do not let the headline or dek assert that generative AI
  caused the harm as settled fact.
