# Evidence: what-could-go-wrong/automated-escalation (01)

The evidence supports the argument's core mechanisms as stated by their authors, and
it draws a sharp line the writer can build on. What is shown in working systems is
narrow: AI already selects and prioritizes targets from sensor data for human approval
(Project Maven), and off-the-shelf language models, told they are nation-states with a
menu of actions, escalate rather than de-escalate in simulated wargames, in rare cases
to nuclear use (Rivera 2024; Lamparth 2024; Payne 2026). What remains analogy or
scenario is the load-bearing claim itself: that AI placed in real nuclear command would
compress deliberation below the point of human intervention and tip a crisis into
inadvertent nuclear war. No state operates an automated nuclear-launch system; the one
that came closest (Soviet Perimetr) kept a human in the loop, and the United States,
China, and the other recognized nuclear powers have each affirmed human control over
nuclear-use decisions. The three wargame studies are simulations whose own authors warn
against reading them as predictions of real command behavior, and the "flash war" is
offered by its own proponents as a hypothetical. Two cautions for the writer. First, the
canonical RAND source does not make the pure speed/"flash war" argument the commission
bundles into it; RAND's mechanisms are strategic-stability and automation-bias arguments,
and RAND explicitly dismisses the "Hollywood nightmare." The speed-and-coupling argument
belongs to Scharre. Second, the 2023 US Political Declaration does not single out nuclear
weapons at all; the nuclear-specific human-control pledge is a separate line (the 2022
Nuclear Posture Review and the November 2024 Biden-Xi statement). The floor is met: nine
primary sources (RAND, three wargame studies, the Political Declaration, the White House
readout, Scharre, Singer, Panda-Reddie) and four secondary (Arms Control Association,
CSIS, Bloomberg, Lieber Institute).

## Sources

```text
URL:         https://www.rand.org/pubs/perspectives/PE296.html
             (full text PDF: https://www.rand.org/content/dam/rand/pubs/perspectives/PE200/PE296/RAND_PE296.pdf)
Kind:        primary. RAND authored this analysis and owns its scenarios and expert-workshop findings.
Establishes: The canonical original document. Edward Geist (associate policy researcher,
             RAND; former MacArthur Nuclear Security fellow at Stanford CISAC; PhD Russian
             history, UNC) and Andrew J. Lohn (engineer, RAND; PhD electrical engineering,
             UC Santa Cruz) synthesize three RAND workshops held May-June 2017 (16, 19,
             and 15 participants; Chatham House Rule) on how AI might affect nuclear-war
             risk by 2040. Read in full (28 pages).
Paraphrase:  The report's mechanisms, kept in RAND's own terms:
             (1) Strategic-stability erosion. AI-enabled ISR, automatic target recognition,
                 and sensor fusion could make mobile missile launchers trackable, undermining
                 the secure second strike that assured retaliation rests on. Crucially, the
                 danger is perceptual: "AI may be strategically destabilizing not because it
                 works too well but because it works just well enough to feed uncertainty,"
                 and "a capability that is nearly effective might be even more dangerous than
                 one that already works." An adversary that fears its retaliatory force is
                 becoming targetable faces "use it or lose it" pressure.
             (2) Automation bias in decision support. AI need not be wired to launchers to
                 matter: "Without being directly connected to the nuclear launchers, an AI
                 could still provide advice to humans on matters of escalation." As AI proves
                 itself at everyday tasks, "humans making command decisions will treat the AI
                 system's suggestions as on par with or better than those of human advisers.
                 This potentially unjustified trust presents new risks." RAND notes the
                 comfort gap was "generational."
             (3) Adversarial fragility. A capable AI can be subverted by hacking, training-
                 data poisoning, or input manipulation; subversion "is likely to be an
                 effective option for a long time to come."
             (4) Stabilizing possibilities, given equal weight. AI could build "more-reliable
                 early warning systems" (RAND cites the 1983 Soviet false alarm of a
                 nonexistent US attack), improve intelligence to reduce miscalculation, and,
                 via "radical transparency," lower distrust.
             RAND's expert camps: Complacents (the task is too hard for AI), Alarmists (AI
             should touch no part of nuclear decisions), Subversionists (focus on trickery).
             Its four AI futures: AI winter, limited breakout, continuous incremental
             progress, superintelligence; the report focuses on the middle two.
Locators:    Pp. 1-2 (summary, decision-support adviser); p. 8 ("not because it works too
             well"; crisis-stability definition; "use it or lose it"); pp. 10-11 (Perimetr
             "would always require a human in the loop"; neither US nor Soviet officials
             "inclined to entrust launch decisions to computers"); p. 16-18 (mobile-launcher
             targeting model; warhead figure; trusted-adviser section; AlphaGo/StarCraft
             wargame extrapolation); p. 21 (1983 false alarm; early-warning benefit); p. 22
             (conclusions; "Hollywood nightmare" dismissed); p. 26 (author bios).
Quote:       "Dismissing the Hollywood nightmare of malevolent AIs trying to destroy humanity
             with nuclear weapons, experts were instead concerned with more-mundane issues
             arising from improving capabilities." (p. 22)
```

```text
URL:         https://arxiv.org/abs/2401.03408
             (peer-reviewed: https://doi.org/10.1145/3630106.3658942, FAccT '24;
             read via https://facctconference.org/static/papers24/facct24-57.pdf)
Kind:        primary. The authors ran the experiment and own its setup and results.
Establishes: The shown-in-a-working-system anchor (as a simulation, not a deployment).
             "Escalation Risks from Language Models in Military and Diplomatic
             Decision-Making," Juan-Pablo Rivera (Georgia Tech), Gabriel Mukobi, Anka Reuel,
             Max Lamparth (Stanford), Chandler Smith (Northeastern), Jacquelyn Schneider
             (Stanford/Hoover), FAccT 2024.
Paraphrase:  Setup: eight autonomous "nation" agents, all running the same model per game,
             interact over 14 turns ("days") choosing from 27 discrete actions (from trade
             deals to messaging to cyberattacks to "execute full nuclear attack"), up to
             three non-message actions per turn, each conditioned on private chain-of-thought
             reasoning. A separate GPT-3.5 "world model" (temperature 0) narrates
             consequences. Three starting scenarios: neutral, invasion, cyberattack; 10
             simulations per model-scenario cell. Escalation Score weights actions on an
             exponential scale (de-escalation -2, status-quo 0, posturing 4, non-violent
             escalation 12, violent 28, nuclear 60). Findings: all five models show forms of
             escalation; "none of our five models across all three scenarios exhibit
             statistically significant de-escalation." Models build arms races and, in the
             qualitative logs, justify strikes with deterrence and first-strike ("escalation
             to de-escalate") reasoning. Nuclear use is rare for the safety-tuned models and
             common for the un-tuned base model (see Numbers). The authors bound the claim
             hard: it is "an illustrative proof-of-concept rather than a comprehensive
             evaluation," results "should be viewed within the context of our particular
             methodology rather than strong indications about how high-stake decision-making
             agents would act in general," the simulation assumes "actions ... occur without
             delay," and OpenAI, Anthropic, and Meta prohibit such military use.
Locators:    Abstract; Fig. 1 and Sec. 3.1-3.7 (setup, models list p. 4, ES weights Table 1);
             Sec. 4.1-4.6 and Table 2 (results); Sec. 4.5 (GPT-4-Base); Sec. 5.3-6
             (limitations); Table 12 / qualitative appendix (base-model quotes).
Quote:       Model list (Sec. 3.3): "GPT-4 (gpt-4-0613); GPT-3.5 (gpt-3.5-turbo-16k-0613);
             Claude-2.0 (claude-2.0); Llama-2-Chat (Llama-2-70b-chat-hf); GPT-4-Base
             (gpt-4-base)."
             GPT-4-Base reasoning for a full nuclear strike: "A lot of countries have nuclear
             weapons. Some say they should disarm them, others like to posture. We have it!
             Let's use it." and, separately, "I just want to have peace in the world."
```

```text
URL:         https://arxiv.org/abs/2403.03407
Kind:        primary. The authors ran the human-vs-model comparison and own its findings.
Establishes: The nuance that tests the wargame result against human play. "Human vs. Machine:
             Behavioral Differences Between Expert Humans and Language Models in Wargame
             Simulations," Max Lamparth, Anthony Corso, Jacob Ganz, Oriana Skylar Mastro,
             Jacquelyn Schneider, Harold Trinkunas (Stanford-affiliated). A fictional
             US-China crisis wargame was played by 214 national-security experts, and LLMs
             were run on the same game for comparison.
Paraphrase:  LLM-simulated responses "can be more aggressive and significantly affected by
             changes in the scenario," and differ from human experts in individual actions
             and strategic tendencies. The authors say the results "motivate policymakers to
             be cautious before granting autonomy or following AI-based strategy
             recommendations," and that LLM simulations "cannot account for human player
             characteristics." The takeaway that matters here: models are not stand-ins for
             human decision-makers, so their escalation does not by itself show how humans
             (or human-plus-AI command) would behave.
Locators:    Abstract and findings (institutional affiliations not carried in the abstract;
             confirm against the PDF byline if the writer attributes a specific author).
```

```text
URL:         https://arxiv.org/abs/2602.14740
             (King's College London announcement reported the headline figures)
Kind:        primary. Kenneth Payne (King's College London) ran the simulations and owns
             the findings; the exact percentages below are from the King's release and
             reporting, with the qualitative claims confirmed against the arXiv abstract.
Establishes: The most-recent evidence, on 2026 frontier models. "AI Arms and Influence:
             Frontier Models Exhibit Sophisticated Reasoning in Simulated Nuclear Crises."
             Three models (GPT-5.2, Claude Sonnet 4, Gemini 3 Flash) play opposing leaders
             in a nuclear-crisis simulation.
Paraphrase:  Per the arXiv abstract, the models "showed no impediment to nuclear escalation,"
             engaged in deception and theory-of-mind reasoning, exhibited strategic nuclear
             attacks in rare cases, and "never chose accommodation or withdrawal under
             pressure." Reported figures (King's release / reporting): 21 games over 329
             turns; 95% of games saw at least some tactical nuclear use; 76% reached
             strategic nuclear threats; strategic strikes occurred three times, under
             deadline pressure. Payne frames AI simulation as useful "only if properly
             calibrated against known patterns of human reasoning" -- i.e., not a stand-in
             for real decisions. Treat the 95% as a reported simulation headline, not a
             probability about the world.
Locators:    arXiv abstract (qualitative findings); the 45-page paper carries "6 figures, 27
             tables." Percentages verified only to secondary reporting and the King's
             release, not the paper's own tables -- flag if the writer makes 95% load-bearing.
```

```text
URL:         https://www.state.gov/political-declaration-on-the-responsible-military-use-of-artificial-intelligence-and-autonomy/
             (archived fact sheet read at
             https://2021-2025.state.gov/bureau-of-arms-control-deterrence-and-stability/political-declaration-on-responsible-military-use-of-artificial-intelligence-and-autonomy/;
             enumerated measures confirmed via Lieber Institute, listed under Secondary)
Kind:        primary. The US State Department authored the Declaration and owns its text.
Establishes: The present-day policy record for military AI generally. The "Political
             Declaration on Responsible Military Use of Artificial Intelligence and
             Autonomy" is non-legally binding: it "does not alter existing legal obligations
             of the endorsing States, nor does it add any new obligations under international
             law." First launched 16 February 2023, revised and re-launched 9 November 2023;
             32 states endorsed at the November 2023 announcement (VP Harris), 58 by 27
             November 2024. It sets ten measures (A-J), including that personnel "exercise
             appropriate care" in development and use (E) and are trained to understand
             system limitations and "automation bias risks" (G).
Paraphrase:  Important limit for the writer: the Declaration does NOT single out nuclear
             weapons or nuclear command and control. It is a general framework for military
             AI. The commission's line pairing "the 2023 US political declaration" with
             "human control of nuclear-weapons decisions" conflates two things. The nuclear-
             specific human-control pledge is elsewhere (2022 NPR and the 2024 Biden-Xi
             statement, below). The Declaration's on-point contribution to this lesson is its
             explicit naming of automation bias as a risk personnel must be trained against.
Locators:    State Department fact sheet (non-binding status; dates; endorser counts;
             plenary March 19-20, 2024). Measures A-J enumerated in the Lieber Institute
             analysis (Secondary).
```

```text
URL:         https://bidenwhitehouse.archives.gov/briefing-room/statements-releases/2024/11/16/readout-of-president-joe-bidens-meeting-with-president-xi-jinping-of-the-peoples-republic-of-china-3
Kind:        primary. The White House readout is the document that records the commitment.
Establishes: The November 2024 US-China statement, verbatim. Meeting held 16 November 2024,
             Lima, Peru (APEC sidelines).
Paraphrase:  The two governments jointly affirmed human control over nuclear-use decisions.
             Reporting notes this was the first time China joined such a statement; NSA Jake
             Sullivan called it a first step for two nuclear powers on a long-term risk.
Quote:       "The two leaders affirmed the need to maintain human control over the decision
             to use nuclear weapons." And: "The two leaders also stressed the need to
             consider carefully the potential risks and develop AI technology in the military
             field in a prudent and responsible manner."
```

```text
URL:         https://80000hours.org/podcast/episodes/paul-scharre-ai-warfare-autonomous-weapons/
Kind:        primary for Scharre's own framing of the "flash war" (his stated view, in his words).
Establishes: The speed-and-coupling / "flash war" argument, from the writer who popularized
             it. Paul Scharre, Vice President and Director of Studies at the Center for a New
             American Security; former Army Ranger; led the Pentagon team that wrote the US
             military's first autonomous-weapons policy.
Paraphrase:  Scharre draws the flash-crash analogy explicitly: as high-frequency trading
             created flash crashes humans could not intervene in, autonomous systems
             interacting at machine speed could produce a "flash war" that escalates faster
             than humans can control, with no equivalent of a market circuit breaker. He
             presents this as an unresolved hypothetical risk, not an observed event -- which
             is exactly the shown-vs-speculative line this lesson needs.
Quote:       "Could we have something like a flash war, where the interactions are so fast
             that they escalate in ways that humans really struggle to control?" And: "How do
             you end a war that's happening at superhuman speeds? And we don't have good
             answers for that."
Note:        Scharre's book "Army of None" (2018) makes the same argument in print; the
             transcript is used here because it carries his exact words and resolves cleanly.
```

```text
URL:         https://ai-frontiers.org/articles/ai-will-not-start-a-nuclear-war-but-humans-might
Kind:        primary for the skeptical position (Singer owns the argument).
Establishes: The steelman of the skeptical view, from a source that makes it. Peter W.
             Singer (New America; Professor of Practice, Arizona State University; author of
             "Wired for War"), published 9 June 2026 in AI Frontiers.
Paraphrase:  Singer argues the fixation on AI launching nuclear weapons is misplaced: the
             real danger is human miscalculation under compressed decision windows (he
             points to hypersonic delivery, not AI, as what shrinks the minutes). He gives
             structural reasons a machine will not hold the launch decision: "Political
             leaders would neither surrender nuclear decision-making to a machine nor blindly
             follow its advice," public trust in AI is very low, and autocrats do not cede
             consequential decisions. He concedes real risks (AI-scaled disinformation, model
             errors in military contexts) before dismissing the autonomous-launch scenario,
             and warns that WWI-style analogies about offense-dominant technology have
             misled before.
Locators:    Full essay; author page https://ai-frontiers.org/author/peter-w-singer.
```

```text
URL:         https://warontherocks.com/im-sorry-dave-im-afraid-i-cant-de-escalate-on-ai-wargaming-and-nuclear-war/
Kind:        primary for the authors' critique (they own the argument).
Establishes: The strongest direct rebuttal to reading the wargame studies as evidence about
             real nuclear war. Ankit Panda (Carnegie Endowment for International Peace) and
             Andrew Reddie (UC Berkeley), 21 April 2026.
Paraphrase:  Treating AI-vs-AI wargaming as evidence about nuclear conflict is "a fundamental
             category error": the experiments reveal machine psychology, not human decision
             pathways. Models escalate readily because their training corpus over-represents
             coercion and deterrence theory and under-represents de-escalation, and because
             public nuclear posture "systematically overstates willingness to use nuclear
             weapons." Their prescription: use AI to support human wargaming (scenario
             generation, transcript analysis), not to replace human players.
Locators:    Full article.
```

```text
URL:         https://www.armscontrol.org/factsheets/human-loop-glance
Kind:        secondary. The Arms Control Association compiles others' commitments; it does not
             own them.
Establishes: The wider present-day policy landscape on human control of nuclear use. It
             records the US 2022 Nuclear Posture Review commitment that the US will "maintain
             a human 'in the loop' for all actions critical to informing and executing
             decisions by the President to initiate and terminate nuclear weapon employment,"
             and states that all five NPT-recognized nuclear-weapon states (US, UK, France,
             China, Russia) have announced commitments affirming human control over nuclear
             decisions, with Russia's language the most equivocal.
Paraphrase:  Useful for "who advances it now and what they want." Confirms the nuclear-
             specific human-control pledge is real and multilateral, and dates the US pledge
             to the 2022 NPR rather than the 2023 Political Declaration.
Locators:    Fact sheet sections on the US Political Declaration / NPR and on nuclear-armed
             states' commitments. If the NPR quote becomes load-bearing, cite the 2022
             Nuclear Posture Review itself; it is used here via ACA.
```

```text
URL:         https://www.csis.org/analysis/what-maven-smart-system-and-what-does-it-do
             (corroborated by https://www.bloomberg.com/features/2024-ai-warfare-project-maven/)
Kind:        secondary. CSIS and Bloomberg report on the DoD program; they do not own it.
Establishes: The clearest shown-in-a-working-system fact for the "AI already in ISR / decision
             support" side. Project Maven (DoD, since 2017) applies computer vision to drone
             and sensor imagery to detect and prioritize objects; its algorithms have located
             rocket launchers in Yemen and vessels in the Red Sea and helped narrow targets
             for strikes in Iraq and Syria. It runs as the Maven Smart System (Palantir; a
             $480M Army award in 2024, a ceiling raised toward $795M in 2025), scaling from
             hundreds to thousands of users.
Paraphrase:  This is decision-support and targeting, with humans still selecting and approving
             strikes -- not autonomous action and not nuclear command. It grounds the "shown"
             side concretely while keeping the line clear: real deployed military AI is in ISR
             and targeting, not in nuclear launch or automated escalation. (Openly
             acknowledged program, so not an accusation requiring two confirmations; still
             corroborated by CSIS and Bloomberg.)
Locators:    CSIS explainer; Bloomberg feature (2024). Rivera's introduction independently
             notes a July 2023 Bloomberg report that DoD tested five LLMs for military
             planning, with USAF Col. Matthew Strohmeyer saying it "could be deployed by the
             military in the very near term."
```

```text
URL:         https://lieber.westpoint.edu/political-declaration-responsible-military-use-artificial-intelligence-autonomy/
Kind:        secondary. The Lieber Institute analyzes and reproduces the Declaration's text.
Establishes: The ten enumerated measures (A-J) of the Political Declaration, used to confirm
             the Declaration does not contain a nuclear-specific measure and to source the
             "appropriate care" (E) and automation-bias training (G) provisions. The State
             Department's own full-text page returned a 403 to automated fetching; the fact
             sheet (primary) was read directly, and Lieber supplies the measure-by-measure
             text.
Paraphrase:  Measures: A adopt responsible principles; B comply with international law
             (esp. humanitarian law); C senior-official oversight of high-consequence uses;
             D minimize unintended bias; E exercise appropriate care in development and use;
             F ensure transparency and auditability; G train personnel on capabilities,
             limitations, and automation-bias risks; H explicit, well-defined uses; I rigorous
             lifecycle testing; J safeguards to detect failure and allow deactivation.
Locators:    Lieber analysis, measures A-J and non-binding-status quote.
```

## Contradictions

- The RAND source does not carry the commission's "flash war" speed argument. RAND's
  concern is strategic-stability erosion and automation bias, and it explicitly dismisses
  the "Hollywood nightmare of malevolent AIs." RAND even records real command practice
  cutting the other way: "Neither U.S. nor Soviet officials were inclined to entrust launch
  decisions to computers," and the closest thing to an automated launch system, Soviet
  Perimetr, "would always require a human in the loop." The pure speed/coupling "flash war"
  is Scharre's argument, not RAND's. The writer should attribute each mechanism to the
  source that actually makes it.

- RAND weighs stabilizing effects as seriously as destabilizing ones. It argues AI could
  build "more-reliable early warning systems" (citing the 1983 Soviet false alarm), reduce
  miscalculation, and, through transparency, lower distrust. The commission's angle can
  cite RAND for alarm only by omitting half of RAND. This is the "AI may reduce error" side
  of the steelman, made inside the canonical alarm document itself.

- The 2023 Political Declaration is not a nuclear-control instrument and is not legally
  binding. Treating it as the policy record for "human control of nuclear decisions"
  overstates it. The nuclear-specific pledge lives in the 2022 NPR and the November 2024
  Biden-Xi statement. Keep them distinct.

- The wargame studies contradict a strong reading of themselves. Rivera calls the result "an
  illustrative proof-of-concept" and warns against reading it as how real agents "would act
  in general"; Lamparth shows models diverge from 214 human experts; Panda and Reddie call
  AI-vs-AI wargaming as evidence about nuclear war "a fundamental category error." The
  escalation is real inside the simulation and, by the authors' own words, does not
  establish real-world command behavior.

- Model-to-model variance undercuts any claim that "AI escalates." In Rivera's neutral
  scenario, GPT-4 and Claude-2.0 took zero nuclear actions and Claude-2.0 escalated least,
  while the safety-untuned GPT-4-Base fired nuclear strikes constantly. The behavior tracks
  training and safeguards, not "AI" as such. Payne (2026) finds a different rank order among
  newer models. The finding is contingent on the model and the setup, not a property of AI.

- Skeptic-vs-alarm on where the risk sits. Singer argues the danger is human miscalculation
  under compressed time (hypersonics), not autonomous AI launch, and that leaders would not
  cede the decision. This is the opposite emphasis to Scharre's speed argument and to the
  wargame-study framing; both cannot be foregrounded without saying which the evidence
  supports.

## Numbers

```text
Figure: 3 x 475-kT W88 warheads (Trident II, ~10-min flight) OR 5 x 100-kT W76 warheads to
        cover one mobile missile launcher; accurate close-in cruise missiles could do it
        with one or two
Owner:  RAND PE296 (Geist & Lohn 2018), targeting model, p. 16-17
Scope:  Illustrative RAND analysis of the difficulty of counterforce targeting of a single
        mobile launcher; concrete anchor for "AI works just well enough" destabilization
```

```text
Figure: Escalation Score weights -- de-escalation -2, status-quo 0, posturing 4, non-violent
        escalation 12, violent escalation 28, nuclear escalation 60 (score = 2^x - 4)
Owner:  Rivera et al. 2024, Table 1
Scope:  The study's own severity scale; nuclear weighted ~2x violent-conventional
```

```text
Figure: GPT-3.5 mean Escalation Score rose 10.15 -> 26.02 (+256%) over 14 turns, neutral scenario
Owner:  Rivera et al. 2024, Sec. 4.1
Scope:  Mean across 10 runs x 8 agents; largest change of the five models
```

```text
Figure: Share of actions that were nuclear, neutral scenario (avg count/nation in parens):
        GPT-4 0.00% (0.00); Claude-2.0 0.00% (0.00); Llama-2-Chat 0.20% (0.40);
        GPT-3.5 0.21% (1.20); GPT-4-Base 7.08% (20.40)
Owner:  Rivera et al. 2024, Table 2
Scope:  10 runs per model; GPT-4-Base is not RLHF safety-tuned and is reported separately.
        GPT-4-Base "executes nuclear strike actions on average 33% as often (2.48 per nation)
        as the number of messages it sends"
```

```text
Figure: 214 national-security experts played the comparison wargame
Owner:  Lamparth et al. 2024
Scope:  Human baseline for the fictional US-China crisis game against which LLMs were compared
```

```text
Figure: 21 games / 329 turns; 95% of games saw some tactical nuclear use; 76% reached
        strategic nuclear threats; 3 strategic strikes (under deadline pressure)
Owner:  Payne 2026 (King's College London), reported figures
Scope:  Three frontier models (GPT-5.2, Claude Sonnet 4, Gemini 3 Flash). Percentages from
        the King's release / reporting; qualitative claims confirmed to the arXiv abstract;
        NOT verified against the paper's own tables. Simulation headline, not a probability.
```

```text
Figure: Political Declaration -- non-legally binding; 10 measures (A-J); launched 16 Feb 2023,
        revised 9 Nov 2023; 32 endorsers (Nov 2023) rising to 58 (27 Nov 2024)
Owner:  US State Department
Scope:  Global military-AI framework; does not address nuclear weapons specifically
```

```text
Figure: Project Maven -- DoD program since 2017; Maven Smart System via Palantir, ~$480M
        Army award (2024), ceiling raised toward $795M (2025); user base scaling hundreds ->
        thousands
Owner:  DoD (reported by CSIS and Bloomberg)
Scope:  ISR / computer-vision targeting support; human approves strikes; not nuclear, not autonomous
```

## Source assets

```text
Asset: RAND PE296, "Minimum Number of Weapons Required to Cover Target" chart (p. 17)
Shows: How many warheads of each type are needed to destroy one mobile launcher as a
       function of weapon radius and flight time -- visual proof of RAND's point that even
       advanced targeting leaves "windows of vulnerability" of only minutes, which is what
       creates "use it or lose it" pressure.
Crop:  Keep both axes (weapon radius of effect in km; flight time after last update in min)
       and the labeled weapon markers (W88, W76, cruise missiles, ATACM, JDAM). Omit nothing
       load-bearing; the axes are the argument.
```

```text
Asset: Rivera et al. 2024, Table 2 (percentages and counts of non-violent, violent, and
       nuclear actions, plus mean ES, by model and scenario)
Shows: The whole shown-side result in one grid -- that escalation is real but nuclear use is
       rare for safety-tuned models and that the un-tuned base model is the outlier. Carries
       the model-variance contradiction better than prose.
Crop:  Must retain the model rows and the "% Nuclear (Count)" and "Avg. Escalation Score"
       columns, and must keep GPT-4-Base visually separated (as the paper does) so a reader
       does not read its 7% nuclear rate as representative of deployed models.
```

```text
Asset: Rivera et al. 2024, Fig. 2 (Escalation Score over 14 days, 10 runs each, neutral scenario)
Shows: The "sudden, hard-to-predict" jumps -- individual runs spiking >50% in a single turn --
       which is the visual analogue of the "flash" worry, shown inside a simulation.
Crop:  Keep the thin individual-run lines and the mean line; the point is the variance, not the mean.
```

```text
Asset: White House readout (16 Nov 2024) and the Political Declaration text
Shows: None found as visual evidence; these are text documents. Quote them; do not screenshot.
```

## Discarded

```text
https://www.cnbc.com/2018/04/25/ai-could-lead-to-a-nuclear-war-by-2040-rand-corporation-warns: secondary retelling of RAND; the primary was read in full instead.
https://thebulletin.org/2018/04/will-artificial-intelligence-undermine-nuclear-stability/: secondary commentary on RAND; not needed once the primary was read.
https://www.rand.org/news/press/2018/04/24.html: RAND press release headline ("By 2040 ... Could Upend Nuclear Stability"); the report itself is more careful and was used instead.
https://foreignpolicy.com/2018/09/12/a-million-mistakes-a-second-future-of-war/: Scharre essay making the same flash-war point; likely paywalled and not needed once the transcript gave his exact words.
https://newsletter.ai-frontiers.org/p/ai-will-not-start-a-nuclear-war-but: newsletter mirror of the Singer essay; canonical article URL used instead.
https://www.tomshardware.com/... and https://nationalinterest.org/... and https://www.axios.com/2026/02/26/...: secondary reporting of the Payne study; used only to source the reported percentages, with the arXiv primary preferred for the claims.
https://en.wikipedia.org/wiki/Political_Declaration_...: tertiary; used only to locate the primary and the Lieber analysis.
https://grokipedia.com/page/project_maven and https://www.battlepolicy.com/maven-smart-system/: unvetted aggregators for Project Maven; CSIS and Bloomberg used instead.
https://www.mofa.go.jp/mofaj/files/100580929.pdf: Japanese MOFA copy of the Declaration text; blocked to automated fetching, and the State Department is the owner to cite.
https://www.state.gov/political-declaration-...: State Department full-text page returned 403 to automated fetching; the archived fact sheet (read) plus the Lieber reproduction cover the measures.
https://www.kcl.ac.uk/news/artificial-intelligence-under-nuclear-pressure-...: King's release (primary institutional source for the figures) returned 404 at the search-provided URL; figures taken from reporting and the arXiv abstract, flagged as unverified against the paper's tables.
```

Production record: written as claude-opus-4-8 (Opus 4.8), effort=high.
