# Evidence record: what-could-go-wrong/vulnerable-world-hypothesis (01)

The steelman side is fully sourced from Bostrom's own paper: the urn metaphor, the
"easy nukes" thought experiment, the Vulnerable World Hypothesis definition, the
three features of the semi-anarchic default condition, the four-type vulnerability
typology, and the "High-tech Panopticon" surveillance vignette all sit in the
primary text with exact locators and wording. The empirical anchor is where the
evidence is both strongest and most treacherous. The direct present-day
measurements exist and are primary: a 2024 RAND red-team study found no
statistically significant bioweapon-planning uplift from 2023-era models, and the
strongest cyber results (DARPA's AIxCC, Google's Big Sleep) are defensive
bug-finding, not attacker uplift. But the frontier picture moved after RAND: in
2025 Anthropic measured a rising bioweapons-acquisition uplift across model
generations (1.53x to 1.70x to 2.53x) and shipped Claude Opus 4 under precautionary
ASL-3, and OpenAI declared GPT-5 "High capability" in bio while stating it lacked
definitive evidence the model helps a novice. So "the measured uplift is limited" is
true of realized real-world capability and of the RAND null, but understates a
rising measured trend on text proxies and the labs' precautionary posture. The
objection side is well sourced from named critics (David Thorstad; Michael Nielsen)
plus a compilation post; the "unfalsifiability" objection is best documented as
something even sympathetic readers concede rather than as a knockdown from a hostile
one. The record's most important limitation is that the bio empirical claim is a
moving target: any flat "uplift is limited" reading risks reading as dated, while
the rising trend sits on proxies the labs themselves call weak and on plans that
every participant failed to complete.

## Sources

```text
URL:         https://nickbostrom.com/papers/vulnerable.pdf
Kind:        primary. Bostrom is the author; this paper owns the hypothesis,
             the urn metaphor, the typology, and every stabilization proposal
             the article attributes to him.
Establishes: The full argument at strength, in the author's own words. Citation:
             Nick Bostrom, "The Vulnerable World Hypothesis," Global Policy,
             Vol. 10, Issue 4 (November 2019), pp. 455-476,
             DOI 10.1111/1758-5899.12718. Author line: "Nick Bostrom is a
             Professor at Oxford University, where he directs the Future of
             Humanity Institute" (p. 476). Open-access under CC BY-NC.
Paraphrase:  Human creativity is like drawing balls from a giant urn: mostly
             white (beneficial), some gray (mixed or moderately harmful), and
             the hypothesis is that somewhere there may be a black ball, a
             technology that by default destroys the civilization that invents
             it. We have not drawn one, Bostrom says, not through wisdom but
             through luck. VWH holds that if development continues, capabilities
             will be reached that make civilizational devastation extremely
             likely unless civilization exits the "semi-anarchic default
             condition," a world with (1) limited preventive policing, (2)
             limited global governance, and (3) diverse human motivations
             including an "apocalyptic residual" who would destroy civilization
             even at cost to themselves. Vulnerabilities are sorted into four
             types. Stabilization would require, in the drastic cases, extremely
             effective preventive policing (illustrated by universal wearable
             surveillance) and/or effective global governance. Bostrom does not
             claim to show VWH is true; he calls its truth "an open question."
Locators:    Urn: p. 455, section "Is there a black ball in the urn of possible
             inventions?" Easy nukes: pp. 456-457, section "A thought
             experiment: easy nukes." VWH definition and the three features:
             p. 457. Typology: pp. 457-461 ("Typology of vulnerabilities,"
             Type-0/1/2a/2b). Stabilization list of four: p. 462 ("Achieving
             stabilization"). Panopticon: pp. 465-466 ("High-tech Panopticon").
             Devastation threshold: p. 457. "Open question": p. 457.
Quote:       Urn: "One way of looking at human creativity is as a process of
             pulling balls out of a giant urn. ... mostly white (beneficial) but
             also various shades of gray... What we haven't extracted, so far, is
             a black ball: a technology that invariably or by default destroys
             the civilization that invents it. The reason is not that we have
             been particularly careful or wise in our technology policy. We have
             just been lucky."
             VWH: "If technological development continues then a set of
             capabilities will at some point be attained that make the
             devastation of civilization extremely likely, unless civilization
             sufficiently exits the semi-anarchic default condition."
             Three features (p. 457): "1. Limited capacity for preventive
             policing. States do not have sufficiently reliable means of
             real-time surveillance and interception to make it virtually
             impossible for any individual or small group within their territory
             to carry out illegal actions... 2. Limited capacity for global
             governance. There is no reliable mechanism for solving global
             coordination problems and protecting global commons... 3. Diverse
             motivations. There is a wide and recognizably human distribution of
             motives... there are some actors ('the apocalyptic residual') who
             would act in ways that destroy civilization even at high cost to
             themselves."
             Easy nukes: "suppose it had turned out otherwise: that there had
             been some really easy way to unleash the energy of the atom - say,
             by sending an electric current through a metal object placed between
             two sheets of glass." Bostrom sets it against real history: "making
             an atomic weapon requires several kilograms of plutonium or highly
             enriched uranium, both of which are very difficult and expensive to
             produce."
             Type-1: "There is some technology which is so destructive and so
             easy to use that, given the semi-anarchic default condition, the
             actions of actors in the apocalyptic residual make civilizational
             devastation extremely likely." (Type-2a: powerful actors face
             incentives to use civilization-devastating ability, e.g. "safe first
             strike." Type-2b: many actors each take a slightly damaging action
             whose combined effect is devastation, e.g. "worse global warming."
             Type-0: a technology carries a hidden risk whose default outcome on
             discovery is inadvertent devastation, e.g. "surprising strangelets.")
             Panopticon: "Everybody is fitted with a 'freedom tag' ... worn
             around the neck and bedecked with multidirectional cameras and
             microphones. Encrypted video and audio is continuously uploaded from
             the device to the cloud and machine-interpreted in real time. AI
             algorithms classify the activities of the wearer... If suspicious
             activity is detected, the feed is relayed to one of several patriot
             monitoring stations." Bostrom prices it: if monitoring one person
             for a year fell "to around US$140... the entire world population
             could be continuously monitored at a cost of less than 1 per cent of
             world GDP." As a fallback he floats "a policy of preemptive
             incarceration, say whenever some set of unreliable indicators
             suggest a greater than 1 per cent probability that some individual
             will attempt a city-destroying act or worse."
```

```text
URL:         https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2900/RRA2977-2/RAND_RRA2977-2.pdf
Kind:        primary. RAND owns this measurement; the report is the study, not a
             description of one.
Establishes: The direct present-day bioweapon-uplift measurement the empirical
             anchor rests on. Christopher A. Mouton, Caleb Lucas, Ella Guest,
             "The Operational Risks of AI in Large-Scale Biological Attacks:
             Results of a Red-Team Study," RAND Corporation, RR-A2977-2 (2024).
Paraphrase:  A controlled red-team study: 12 "red cells" plus one "crimson cell,"
             across four attack vignettes, each drafting an operational plan
             (OPLAN) scored on a 9-point viability scale. Cells were randomized
             to internet-only, LLM A + internet, or LLM B + internet. The models
             tested were those available "as of summer 2023"; prompts are dated
             August-September 2023. Access to an LLM was associated with a
             0.22-point decrease in mean viability (p = 0.64); LLM A scored +0.12
             (p = 0.87) and LLM B scored -0.56 (p = 0.25) versus internet-only,
             none statistically significant. No plan scored as viable; all fell
             between "untenable" and "problematic." RAND frames this as
             biological-weapon attack planning lying "beyond" the current LLM
             capability frontier, and notes it did not measure how far beyond.
             Context figure: the Global Terrorism Database records 36 of 209,706
             attacks over 50 years (0.0001 percent) as using a biological weapon,
             killing 0.25 people on average, median death toll zero.
Locators:    Key Findings box, p. 1. Viability results and p-values, pp. 7-8
             ("Viability"). "Summer 2023" model scope, p. 2 and p. 11. GTD
             figure, p. 8.
Quote:       "We found no statistically significant difference in the viability
             of plans generated with or without LLM assistance." And: "access to
             an LLM was associated with a 0.22-point decrease in the assessed
             viability score on the 9-point scale... This estimate, however, had
             a p-value of 0.64, well above the commonly used threshold of 0.05."
             And: "these outputs generally mirror information readily available on
             the internet, suggesting that LLMs do not substantially increase the
             risks associated with biological weapon attack planning."
```

```text
URL:         https://www-cdn.anthropic.com/6be99a52cb68eb70eb9572b4cafad13df32ed995.pdf
Kind:        primary. Anthropic owns the trial and the deployment decision it
             reports.
Establishes: A 2025 measured bioweapons-acquisition uplift figure, and that a
             frontier lab activated precautionary safeguards. "System Card: Claude
             Opus 4 & Claude Sonnet 4," Anthropic, May 2025.
Paraphrase:  A controlled uplift trial: groups of 8-10 participants had up to two
             days to draft a bioweapons-acquisition plan; the control group had
             basic internet, the treatment group additionally had Claude with
             safeguards removed. Outputs were graded by Deloitte against an
             acquisition-pathway rubric. Control scored 25% +/- 13%; Claude Opus 4
             63% +/- 13%; Claude Sonnet 4 42% +/- 11%, giving uplift multipliers
             of 2.53x and 1.70x. The prior generation, Claude Sonnet 3.7, scored
             1.53x. Anthropic's pre-set thresholds: total uplift >= 5x (or raw
             uplift >= 0.8) "would create significant additional risk," while
             uplift <= 2.8x "would keep risk at acceptable levels." All
             participants "hit critical failures." Anthropic calls text-based
             uplift trials "substantially weaker proxies for real-world
             scenarios." It concluded Sonnet 4 did not meet the ASL-3 bar but
             Opus 4's result was "sufficiently close that we are unable to rule
             out ASL-3," and deployed Opus 4 under the ASL-3 Standard. Expert
             red-teaming: for Opus 4 "substantially increased risk in certain
             parts of the bioweapons acquisition pathway," but "both models
             continued to make critical errors that would have prevented
             real-world success for many actors."
Locators:    Deployment decision and ASL-3, pp. 2 (abstract) and section 7 intro.
             Uplift trial (design, thresholds, scores), section 7.2.4.1,
             pp. 92-93. Expert red teaming, section 7.2.4.2, p. 94.
Quote:       "the uplift for Claude Opus 4 and Claude Sonnet 4 was 2.53x and
             1.70x, respectively. Furthermore, all participants hit critical
             failures. When we ran this trial for Claude Sonnet 3.7 during our
             previous round of testing, Deloitte's updated rubric placed Sonnet
             3.7's uplift at 1.53x... Claude Opus 4's result is sufficiently close
             that we are unable to rule out ASL-3." And: "Text-based uplift trials
             are substantially weaker proxies for real-world scenarios."
```

```text
URL:         https://cdn.openai.com/gpt-5-system-card.pdf
Kind:        primary. OpenAI owns the capability determination it reports.
Establishes: A second 2025 frontier lab treating a current model as high bio
             capability on precautionary grounds, while disclaiming definitive
             evidence of novice uplift. "GPT-5 System Card," OpenAI, 2025.
Paraphrase:  OpenAI decided to treat gpt-5-thinking as "High capability" in the
             Biological and Chemical domain under its Preparedness Framework and
             activated the associated safeguards, while stating it lacks
             definitive evidence the model could meaningfully help a novice create
             severe biological harm (its defined High-capability threshold). It
             frames the move as precautionary. The card also motivates a shift
             from hard refusals to "safe-completions," arguing dual-use bio and
             cyber prompts "can be completed safely at a high level, but may lead
             to malicious uplift if sufficiently detailed or actionable."
Locators:    Capability decision and precautionary framing, p. 4 (section
             preceding "Model Data and Training"). Safe-completions rationale,
             section 3.1. Preparedness/Bio section, section 5 (Biological and
             Chemical), p. 30ff.
Quote:       "we have decided to treat gpt-5-thinking as High capability in the
             Biological and Chemical domain under our Preparedness Framework,
             activating the associated safeguards. While we do not have definitive
             evidence that this model could meaningfully help a novice to create
             severe biological harm - our defined threshold for High capability -
             we have chosen to take a precautionary approach."
```

```text
URL:         https://www.darpa.mil/news/2025/aixcc-results
Kind:        primary. DARPA ran the competition and owns the reported results.
Establishes: The strongest present-day demonstrated cyber result is defensive
             (autonomous bug-finding and patching), not attacker uplift. DARPA,
             "AI Cyber Challenge Final Results" (2025).
Paraphrase:  In DARPA's AI Cyber Challenge (AIxCC) finals, autonomous cyber
             reasoning systems examined over 54 million lines of code, found 54 of
             63 synthetic vulnerabilities (86%) and patched 43 of them, and also
             surfaced 18 genuine, non-planted vulnerabilities and patched 11, at
             roughly $152 per task and about 45 minutes per patch. Winners: Team
             Atlanta ($4M), Trail of Bits ($3M), Theori ($1.5M). DARPA frames the
             result as AI securing open-source infrastructure, i.e. defense.
Locators:    Results figures and quotes in the DARPA news release body; winners
             at the foot.
Quote:       Program Manager Andrew Carney: "Quality patching is a crucial
             accomplishment that demonstrates the value of combining AI with other
             cyber defense techniques." Framed by DARPA around securing "the
             open-source software that underlies critical infrastructure."
```

```text
URL:         https://projectzero.google/2024/10/from-naptime-to-big-sleep.html
Kind:        primary. Google's Project Zero / DeepMind team reporting its own
             agent's find.
Establishes: A concrete, bounded example of an AI agent finding a real
             memory-safety bug in real software, on the defensive/research side.
Paraphrase:  The "Big Sleep" agent found a previously unknown exploitable stack
             buffer underflow in SQLite (a sentinel-value mishandling in
             seriesBestIndex), reproduced by a simple query, reported to
             developers and fixed the same day, before it reached an official
             release, so users were not affected. Traditional fuzzing had not
             found it despite 150+ CPU-hours of AFL. The team claims it as the
             first public case of an AI agent finding an unknown exploitable
             memory-safety issue in widely used real-world software.
Locators:    Post body ("The vulnerability," "the bug," "we believe this is the
             first...").
Quote:       "We believe this is the first public example of an AI agent finding
             a previously unknown exploitable memory-safety issue in widely used
             real-world software."
```

```text
URL:         https://reflectivealtruism.com/2024/05/17/harms-part-2-surveillance/
Kind:        primary for the objection. David Thorstad owns this critique of the
             surveillance remedy; secondary relative to Bostrom's paper, which it
             quotes and reads from outside.
Establishes: The strongest named objection that the surveillance remedy is
             worse than, or at least a grave cost against, the danger. Author:
             David Thorstad, Assistant Professor of Philosophy, Vanderbilt
             University (PhD Harvard 2020; postdoctoral fellow at the Global
             Priorities Institute, Oxford, 2020-2023), on his "Reflective
             Altruism" blog ("Harms, Part 2: Surveillance," 17 May 2024).
Paraphrase:  Thorstad reproduces the High-tech Panopticon and the preemptive-
             incarceration fallback verbatim and stresses these are "the actual
             proposal," not a caricature. His central moves: (1) Bostrom's own
             argument that the surveillance architecture must be built now,
             before a specific vulnerability appears, turns a speculative
             possibility into present advice, because "in an unfavorable scenario,
             the lead time could be as short as hours or days." (2) The costs of
             ubiquitous surveillance and preemptive incarceration are severe and
             Bostrom does not fully tally them. (3) The pressure toward
             surveillance is structural to longtermism, not incidental: he cites
             Zoe Cremer and Luke Kemp on "securitisation," the move of risk from
             normal politics into national security under emergency powers, and
             their warning that a worldview centered on existential risk can make
             "almost any action... justified." Thorstad does not argue VWH is
             unfalsifiable, and does not argue that no-black-ball-drawn is not
             evidence; his target is specifically the remedy.
Locators:    Sections 3-6 of the post. Panopticon quote, section 3. "hours or
             days" timing, section 4. Cremer/Kemp securitisation, section 5.
Quote:       "This is not a caricature of Bostrom's proposal. It is the actual
             proposal, or at least Bostrom's primary illustration of what he might
             be proposing." And, quoting Cremer and Kemp: "Any approach to
             understanding and mitigating existential risks runs the risk of
             becoming securitised... making it more likely to permit emergency
             powers and be placed under the control of unelected military and
             intelligence officials."
```

```text
URL:         https://michaelnotebook.com/vwh/index.html
Kind:        secondary. Michael Nielsen (physicist and writer) reading and
             assessing Bostrom's paper from outside; primary for his own stated
             view.
Establishes: That the unfalsifiability point is best framed as a concession by a
             sympathetic reader, not a hostile refutation, and that even a
             sympathetic reader recoils at the surveillance remedy.
Paraphrase:  Nielsen treats VWH as not empirically testable "in the usual sense"
             yet still judgeable as more or less plausible, so he does not present
             untestability as a defeater. He is uneasy about the remedy, invoking
             "the horrendous history of the Stasi, the KGB, the purges and the
             Gulag," and summarizes the bargain as: the good news is you need not
             worry about the world being destroyed, the bad news is you now live
             under Big Brother. He gestures at a possible alternative he calls
             "provably beneficial surveillance." He does not reject the hypothesis.
Locators:    Nielsen's "Notes on the Vulnerable World Hypothesis," sections on
             testability and on the surveillance remedy.
Quote:       "The good news is you don't need to worry about the world being
             destroyed; the bad news is you now live under Big Brother." On
             testability: the VWH is "not an empirically testable statement, not
             in the usual sense," but can still be judged "more or less plausible."
```

```text
URL:         https://forum.effectivealtruism.org/posts/Kj5jsfzb5JJgiofbw/on-the-vulnerable-world-hypothesis
Kind:        secondary. A published critique compilation, reading Bostrom from
             outside. Author is not named (posted as "[anonymous]"), which weakens
             its standing as an attributable objection.
Establishes: That the "surveillance remedy is worse than the danger" and
             "premises are not established" objections circulate as a stated
             critical position, useful as corroboration but not as a named
             authority.
Paraphrase:  The post argues several VWH premises are not clearly established
             (that many actors want global catastrophe; that continued
             technological development must be assumed), and that the remedy is
             self-defeating: "Surveillance is one example of an intervention to
             mitigate some kinds of existential risk which itself increases other
             kinds of existential risk," raising the risk of "totalitarian
             lock-in," unlikely to be "democratically consented to," and prone to
             giving "a false sense of security."
Locators:    Body of the EA Forum post.
Quote:       "Surveillance is one example of an intervention to mitigate some
             kinds of existential risk which itself increases other kinds of
             existential risk."
```

## Contradictions

The central contradiction is inside the empirical anchor, and it cuts against a
flat statement of the commission's line that "the measured uplift in current
evaluations is limited."

- The null result and the rising trend disagree, partly because they measure
  different model eras. RAND (2024) found no statistically significant bioweapon-
  planning uplift, but its models were "as of summer 2023." Anthropic (May 2025)
  measured a bioweapons-acquisition uplift that climbs across generations: Claude
  Sonnet 3.7 at 1.53x, Claude Sonnet 4 at 1.70x, Claude Opus 4 at 2.53x (control
  25%, Opus 63%). So "limited" is accurate for 2023-era models and for realized
  real-world capability, but a reader given only the RAND null would miss that the
  measured figure has been rising and that two frontier labs responded in 2025 with
  precautionary safeguards (Anthropic ASL-3; OpenAI "High capability").

- The labs contradict themselves in a disciplined way, and the article must not
  flatten it. Anthropic's own 2.53x sits below its pre-set "significant additional
  risk" threshold of 5x, "all participants hit critical failures," and Anthropic
  calls the whole text-based method a "substantially weaker proxy for real-world
  scenarios." OpenAI activated High-capability safeguards while stating it does "not
  have definitive evidence that this model could meaningfully help a novice." Both
  the alarm reading (uplift is rising; labs are activating safeguards) and the
  dismissal reading (still below thresholds; every plan failed; proxies are weak)
  are supported by the same primary documents. This is the shown-versus-projected
  gap in the topic's own particulars.

- Cyber cuts against the hypothesis's fear more cleanly than bio. The strongest
  demonstrated results are defensive: DARPA's AIxCC (finding and patching real
  vulnerabilities) and Google's Big Sleep (finding a real SQLite bug, reported and
  fixed same day, before release). Neither is a measurement of attacker uplift
  lowering the cost of mass harm. A writer must not let a defensive bug-finding
  result stand in for the offensive-uplift mechanism the hypothesis actually fears.

- On the objections, the three named in the commission are not equally strong.
  "The surveillance remedy may be worse than the danger" is the best supported, from
  a named academic (Thorstad) and echoed by Nielsen and the anonymous post. "The
  hypothesis cannot be falsified" is real but is conceded by a sympathetic reader
  (Nielsen), not pressed as a refutation, and Bostrom pre-empts it by calling VWH's
  truth "an open question" he is not trying to prove. "Having drawn no black ball is
  not evidence one exists" is Bostrom's own framing ("we have just been lucky"), so
  it is less an external objection than a restatement of his premise; I found no
  strong named source pressing it as a distinct refutation, and the writer should
  either source it better or present it as an inference-symmetry point rather than
  attribute it to a critic.

## Numbers

```text
Figure: no statistically significant bioweapon-planning uplift; mean viability
        change from LLM access = -0.22 points on a 9-point scale, p = 0.64
Owner:  RAND RR-A2977-2 (2024), "Viability," pp. 7-8
Scope:  12 red cells, 4 vignettes, LLMs available as of summer 2023; planning
        phase only, execution phase not tested
```
```text
Figure: LLM A +0.12 points (p = 0.87); LLM B -0.56 points (p = 0.25) vs. internet-only
Owner:  RAND RR-A2977-2 (2024), p. 8
Scope:  Same study; two anonymized models
```
```text
Figure: bioweapons-acquisition uplift 2.53x (Claude Opus 4), 1.70x (Claude Sonnet 4),
        1.53x (Claude Sonnet 3.7, prior round); control 25% +/- 13%, Opus 63% +/- 13%,
        Sonnet 4 42% +/- 11%
Owner:  Anthropic, "System Card: Claude Opus 4 & Claude Sonnet 4" (May 2025),
        section 7.2.4.1
Scope:  Groups of 8-10 participants, up to 2 days, Claude with safeguards removed,
        graded by Deloitte; text-based proxy; all participants hit critical failures
```
```text
Figure: Anthropic thresholds: total uplift >= 5x (or raw uplift >= 0.8) = significant
        additional risk; uplift <= 2.8x = acceptable
Owner:  Anthropic system card (May 2025), section 7.2.4.1
Scope:  Pre-set decision thresholds for the ASL-3 rule-out
```
```text
Figure: GPT-5 treated as "High capability" (Biological/Chemical), safeguards
        activated, without definitive evidence of novice uplift
Owner:  OpenAI, "GPT-5 System Card" (2025), p. 4
Scope:  Precautionary determination under the Preparedness Framework
```
```text
Figure: AIxCC: 54M+ lines of code analyzed; 54/63 synthetic vulnerabilities found
        (86%), 43 patched; 18 real vulnerabilities found, 11 patched; ~$152/task;
        ~45 min/patch
Owner:  DARPA, "AI Cyber Challenge Final Results" (2025)
Scope:  Competition finals; defensive (find-and-patch), autonomous cyber reasoning
        systems
```
```text
Figure: Panopticon cost: ~US$140 per person per year would let the whole world be
        continuously monitored at < 1% of world GDP
Owner:  Bostrom (2019), p. 466
Scope:  Bostrom's own back-of-envelope for the surveillance vignette
```
```text
Figure: bioweapon use in terrorism: 36 of 209,706 attacks over 50 years (0.0001%),
        mean 0.25 deaths, median 0
Owner:  RAND RR-A2977-2 (2024), p. 8, citing the Global Terrorism Database
Scope:  Context for base-rate difficulty of executing a biological attack
```
```text
Figure: civilizational devastation threshold in VWH = at least the death of 15% of
        world population, or > 50% reduction of global GDP lasting more than a decade
Owner:  Bostrom (2019), p. 457
Scope:  Definitional; the bar VWH sets for "devastation"
```

## Source assets

```text
Asset: Bostrom (2019), the "High-tech Panopticon" / "freedom tag" vignette, pp. 465-466
Shows: The surveillance remedy in the author's own concrete words, which lets a
       reader feel the cost the argument accepts before any critic speaks. It reads
       as a set-piece and is the single most quotable primary passage.
Crop:  If excerpted, keep the freedom-tag description and the "patriot monitoring
       stations" through the arrest step; the privacy-protection sentences can be
       trimmed but the abuse-oversight caveat should stay so the excerpt is not
       stacked against Bostrom.
```
```text
Asset: Anthropic system card (May 2025), Figure 7.2.4.1.A, "Bioweapons acquisition
       uplift trial results" (left: raw scores; right: critical failures)
Shows: The measured uplift by model alongside the fact that every participant hit a
       critical failure, i.e. both the rising trend and its current ceiling in one
       figure. This is the strongest single visual for the shown-versus-projected
       point.
Crop:  A crop must retain the critical-failures panel; showing only the rising raw
       scores would misrepresent the finding as unbounded capability.
```
```text
Asset: RAND RR-A2977-2 (2024), Table 3 (and Tables 4-5), viability scores by
       condition and vignette
Shows: The null result concretely: near-identical viability with and without an LLM,
       and no systematic per-vignette trend.
Crop:  Keep the internet-only vs. LLM columns and the p-values; do not crop to a
       single vignette where one model happened to score higher.
```
```text
Asset: DARPA AIxCC final-results figures (vulnerabilities found/patched; cost/time)
Shows: The scale and the defensive nature of the strongest cyber demonstration.
Crop:  Keep the "found vs. patched" pairing; a "found" count alone overstates what
       was actually remediated.
```

## Discarded

```text
URL: https://onlinelibrary.wiley.com/doi/full/10.1111/1758-5899.12718 — the Wiley
     version of Bostrom's paper; same text as nickbostrom.com/papers/vulnerable.pdf,
     used only to confirm the Global Policy 10(4):455-476 citation. Cite the paper
     once, via the author's open-access copy.
```
```text
URL: https://en.wikipedia.org/wiki/Vulnerable_world_hypothesis — tertiary summary;
     useful orientation only, owns no claim.
```
```text
URL: https://forum.effectivealtruism.org/posts/wZzMvwi55cqGhsvSE/... and
     rharling.medium.com/summary-... — third-party summaries of Bostrom's paper; the
     primary is open, so these add nothing citable.
```
```text
URL: Cremer & Kemp, "Democratising Risk" (Futures, 2022) — a named secondary on
     securitisation, but I read it only as quoted inside Thorstad, not in the
     original. Cite the securitisation point via Thorstad, or open Cremer & Kemp
     directly before attributing to them.
```
```text
URL: https://www.ncsc.gov.uk/report/impact-of-ai-on-cyber-threat and
     nicholas.carlini.com/writing/2025/are-llms-worth-it.html — cyber-uplift context
     already carried by the linked what-could-go-wrong/cyber-uplift lesson; not
     re-sourced here, per the commission's instruction to spend that lesson rather
     than redo it.
```
