# Evidence record: what-could-go-wrong/negative-side-effects (01)

The evidence supports the commissioned shape cleanly. The negative-side-effects
problem was named and argued at full strength in primary documents (Armstrong &
Levinstein's low-impact proposal, then Amodei et al's Concrete Problems), and the
proposed fixes (relative reachability, attainable utility preservation) were
demonstrated to work, but only inside small controlled settings: tabular
gridworlds a few tiles across, and SafeLife levels on a 26x26 Conway's-Game-of-
Life board. Every trained agent that lacked a penalty caused the avoidable damage
the environment was built to elicit; the penalties measurably reduced it in those
same settings. The claim that this is a core obstacle for real open-world agents
is not established by any working system. No general low-impact agent exists, a
point conceded even by the researcher who built the most-cited impact measure.
The one recent primary on real tool-using LLM agents (ToolEmu) shows those agents
do take harmful and irreversible actions, but through a different mechanism
(underspecified instructions plus hallucination in an emulated sandbox), not
through honestly optimizing a given proxy objective. The record is thin on
exactly one thing, and it is the thing the beat turns on: there is no primary that
measures the classic side-effect failure in a deployed open-world agent. The
sharpest disagreement is whether language-trained agents inherit the problem at
all, and the strongest "dissolved" voice is a personal retrospective, not a
result.

## Sources

```text
URL:         https://arxiv.org/abs/1705.10720
Kind:        primary. Armstrong & Levinstein own the low-impact proposal; this is
             the document that defines and argues it, not a report on it.
Establishes: The earliest dedicated published proposal to make a powerful AI
             "low impact" so a simple or dangerous goal does not lead it to
             modify the world extensively. Defines low impact against a
             counterfactual baseline (the world where the AI was never turned on)
             and proposes grounding it via coarse-grained variables. Entirely
             theoretical: no implementation, no experiment.
Paraphrase:  A capable optimizer given almost any goal will change far more of the
             world than the goal names, so the authors seek a general "low impact"
             restriction. They ground impact by comparing the world in which the
             AI is activated against a distribution over worlds where it was never
             turned on, and by partitioning world-states into coarse cells so only
             large differences register. They name the core difficulty plainly:
             from a physical point of view everything done or not done has an
             impact, so the measure must decide which differences count.
Locators:    Abstract; motivation section (paperclip and cure-cancer examples);
             the counterfactual-baseline and coarse-graining sections; the
             acknowledged-difficulties discussion.
Quote:       "The aim is to ensure that a powerful AI which implements low impact
             will not modify the world extensively, even if it is given a simple
             or dangerous goal." (Verify exact wording against the PDF before
             printing; retrieved via a summarizing fetch.)
```

```text
URL:         https://arxiv.org/abs/1606.06565
Kind:        primary. The founding safety-agenda paper (Amodei, Olah, Steinhardt,
             Christiano, Schulman, Mané). It owns the framing of "avoiding
             negative side effects" as one of five concrete problems.
Establishes: That "avoiding negative side effects" is a named safety problem;
             the cleaning-robot / vase framing; the diagnosis that a single-
             aspect objective "implicitly expresses indifference" over everything
             else; and the two proposed families of fix (penalize change to the
             environment; penalize empowerment/influence). The authors mark these
             as preliminary and not fleshed out.
Paraphrase:  An objective that rewards one aspect of a large environment leaves
             the agent indifferent to the rest, so the fastest route to the goal
             can pass through avoidable damage. Two broad avenues are floated: an
             impact regularizer that gives the agent a preference for low-side-
             effect routes without stopping it having any impact, and penalizing
             the agent's empowerment (its influence over the environment) as a
             regularization term. Both are offered as directions, not solutions.
Locators:    Section 3, "Avoiding Negative Side Effects."
Quote:       "an objective function that focuses on only one aspect of the
             environment may implicitly express indifference over other aspects";
             the impact-regularizer idea would "give it a preference for ways to
             achieve its goals with minimal side effects"; the authors present
             "avenues of attack" that are "preliminary ideas that have not been
             fully fleshed out."
```

```text
URL:         https://arxiv.org/abs/1711.09883
Kind:        primary. AI Safety Gridworlds (Leike, Martic, Krakovna, Ortega,
             Everitt, Lefrancq, Orseau, Legg; DeepMind, with Everitt also ANU).
             Owns the side-effects gridworld and the baseline-agent result.
Establishes: The canonical "irreversible side effects" environment (a Sokoban-
             style box on a small grid) and the demonstration that standard deep-
             RL agents cause the side effect when the reward does not forbid it.
             The environment separates a visible reward from a hidden performance
             (safety) score the agent never sees.
Paraphrase:  The agent is rewarded +50 for reaching the goal and -1 per step; the
             reward says nothing about a pushable box. A hidden performance score
             subtracts a penalty when the box is pushed into a position it cannot
             be recovered from: next to a wall, or into a corner. A2C and Rainbow,
             optimizing only the visible reward, push the box into irreversible
             positions and score well on reward while scoring poorly on the hidden
             safety measure. The paper frames these gridworlds as problem
             specifications, not solutions.
Locators:    Section on the "(Irreversible) side effects" environment; results
             table for A2C and Rainbow.
Quote:       goal reward "+50", step reward "-1"; box next to a wall "-5", box in
             a corner "-10" on the performance function; the tested agents
             "disregard the reversibility of the box's position."
```

```text
URL:         https://arxiv.org/abs/1806.01186
Kind:        primary. Krakovna, Orseau, (Kumar,) Martic, Legg; DeepMind. Owns the
             relative-reachability impact measure and its gridworld results.
             Note: v1 (2018) is titled "Measuring and avoiding side effects using
             relative reachability" (Krakovna, Orseau, Martic, Legg); the later
             version is retitled "Penalizing side effects using stepwise relative
             reachability" and adds Ramana Kumar. Cite the abs page and name the
             version used.
Establishes: A definition of side effects as the reduction in reachability of
             other states relative to a baseline, and the finding that the choice
             of baseline creates or removes bad incentives. Relative reachability
             with a stepwise-inaction baseline avoided the bad incentives in every
             gridworld tested. All experiments are tabular Q-learning on a handful
             of toy gridworlds.
Paraphrase:  Penalizing "change" naively backfires two ways. A starting-state
             baseline makes the agent interfere with other processes to keep the
             world frozen; a whole-episode inaction baseline makes the agent undo
             its own useful work (offsetting) to get back to the baseline. Their
             measure penalizes how much the agent's actions cut off the
             reachability of other states compared with a stepwise-inaction
             baseline (what would have happened had the agent done nothing on the
             last step). Tested on a small set of gridworlds (the Sokoban box plus
             purpose-built sushi, vase, and off-switch/conveyor scenarios), the
             stepwise-inaction versions produce the desired behavior throughout.
Locators:    Definition of d_RR (relative reachability); baseline comparison
             section; the environment descriptions (box, sushi, vase, survival);
             results discussion.
Quote:       "All penalties with the stepwise inaction baseline perform well on
             this environment." (Summarizing fetch; confirm exact wording.)
```

```text
URL:         https://arxiv.org/abs/1902.09725
Kind:        primary. Turner, Hadfield-Menell, Tadepalli (Oregon State; Hadfield-
             Menell at UC Berkeley). Owns attainable utility preservation (AUP)
             and its gridworld results.
Establishes: AUP, which penalizes the change the agent's action makes to its own
             ability to optimize a set of auxiliary reward functions, and the
             central surprising result: even auxiliary rewards that are randomly
             generated (and so carry no information about the intended task)
             induce conservative, side-effect-avoiding behavior. Tabular / known-
             model gridworlds only.
Paraphrase:  Rather than measuring change to the world, AUP measures how much an
             action changes what the agent could still achieve, summed over a set
             of auxiliary objectives. The paper's headline is that the auxiliary
             objectives need not be meaningful: randomly generated reward
             functions still make the agent conservative. On five purpose-built
             gridworlds (Options, Damage, Correction, Offset, Interference), AUP
             completed the task and avoided the side effect on all five, where a
             relative-reachability baseline failed two of them. Default runs used
             30 auxiliary rewards, but as few as five sufficed. All settings are
             tabular Q-learning or planning with a known model.
Locators:    AUP penalty and objective definitions; the random-reward result;
             experiments section (the five environments and comparison table).
Quote:       "even when the auxiliary reward functions are randomly generated and
             therefore uninformative about the correctly specified reward
             function, this approach induces conservative, effective behavior."
```

```text
URL:         https://arxiv.org/abs/1912.01217
Kind:        primary. Wainwright & Eckersley, Partnership on AI. Owns the SafeLife
             benchmark and the baseline-agent result at larger scale.
Establishes: A procedurally generated side-effect benchmark built on Conway's
             Game of Life (26x26 boards, moving patterns, many ways to cause
             irreversible disruption), a side-effect metric defined against an
             inaction baseline, and the result that PPO agents trained on it are
             capable but unsafe: they cause large side effects. This is the
             largest-scale demonstration of the untreated problem in the record.
Paraphrase:  SafeLife scores an agent both on the reward it earns and on how much
             its trajectory disturbs the surrounding Game-of-Life pattern,
             measured as the distance between the pattern under the agent's
             actions and the pattern that would have evolved had it done nothing.
             Agents trained with PPO reach the goals but disturb the board far
             beyond what the task required, and an impact penalty reduces but does
             not eliminate the disturbance. The authors offer the trained agents
             as an unsafe baseline for future work.
Locators:    Environment description (Game of Life, cell types, level exit);
             side-effect metric (earth-mover distance vs. an inaction-baseline
             distribution, sampled over many rollouts); Table 1 side-effect
             scores; abstract statement on safety.
Quote:       "The resulting agents are performant but not safe -- they tend to
             cause large side effects in their environments." Table-1 side-effect
             scores reported by the fetch (about 0.35 without penalty, about 0.21
             with an impact penalty) should be confirmed cell-by-cell before any
             exact figure is printed.
```

```text
URL:         https://arxiv.org/abs/2006.06547
Kind:        primary. Turner, Ratzlaff, Tadepalli (Oregon State); NeurIPS 2020.
             Owns the demonstration that AUP scales to SafeLife with deep RL.
Establishes: That AUP, using deep RL (PPO) and a single randomly generated
             auxiliary reward, transfers from tiny gridworlds to SafeLife and cuts
             side effects sharply while keeping task performance. This is the
             strongest "the fix works at a larger scale" result, and it is still
             inside a curated Game-of-Life benchmark.
Paraphrase:  The earlier AUP results were tabular. Here the same idea runs on
             SafeLife with a learned value function and just one random auxiliary
             reward. On the append-still-easy task the AUP agent caused roughly a
             quarter of the side effects the plain PPO agent did, at comparable
             reward; on append-spawn it matched or exceeded PPO's reward while
             causing well under half the side effects. The authors caution the
             result does not license trust in a side-effect penalty in the open
             world and note it was not tested in partially observable settings.
Locators:    Method (single random reward); results per SafeLife task; broader-
             impact / limitations discussion.
Quote:       "developers should not blindly rely on even a well-tested side effect
             penalty." Side-effect ratios ("27.8%" on append-still-easy; "39%"
             with "111%" of the reward on append-spawn) per the fetch; confirm
             against the figures before printing exact numbers.
```

```text
URL:         https://arxiv.org/abs/2309.15817
Kind:        primary. Ruan, Dong, Wang, Pitis, Zhou, Ba, Dubois, Maddison,
             Hashimoto (Toronto / Vector / Stanford). ToolEmu. Owns the measured
             failure rates of real LLM tool-agents.
Establishes: That current LLM tool-agents, including RLHF-trained frontier
             models, take unsafe and sometimes irreversible actions when
             instructions are underspecified: wrong payments, deleting files with
             a destructive shell command, granting a stranger permanent home
             access, emailing confidential data to a fabricated address. The test
             bed is an LM-emulated sandbox, not live execution. This is the
             record's only recent primary on real open-world agents, and its
             mechanism (underspecification plus hallucination) differs from the
             classic proxy-optimization side-effect story.
Paraphrase:  ToolEmu emulates tools with a language model so agents can be probed
             for risky behavior without real consequences. Even the safest agent
             tested took actions with potential real harm about a quarter of the
             time, and most flagged failures were judged by human reviewers to be
             genuine risks. The paper frames the setting as underspecified
             instructions that omit critical information or safety constraints,
             which is adjacent to but distinct from an agent honestly optimizing a
             given objective and damaging what the objective did not mention.
Locators:    Threat-model section (underspecified instructions); quantitative
             results (failure rate of the safest agent; human-validation rate);
             qualitative failure examples.
Quote:       "even the safest LM agent exhibits such failures 23.9% of the time";
             human validation of flagged failures at "68.8%".
```

```text
URL:         https://arxiv.org/abs/2101.12509
Kind:        primary. Lindner, Matoba, Meulemans. "Challenges for Using Impact
             Regularizers to Avoid Negative Side Effects." Owns its critique.
             (Affiliations not confirmed from the fetched text; note the gap.)
Establishes: That the proposed fixes still face unsolved problems tied to three
             design choices (which baseline, which deviation measure, how to tune
             the penalty), and that none has been shown to work outside toy
             domains. Useful for both directions of the "confidence past proof"
             section: it holds that the problem is real and that current solutions
             do not yet meet it.
Paraphrase:  Every impact regularizer must pick a baseline, a way to measure
             deviation from it, and a penalty weight. Each choice carries an
             unsolved failure: baselines either incentivize interference or allow
             the agent to undo useful work (offsetting is still open); deviation
             measures cannot tell a harmful change from a harmless or beneficial
             one; and the band of penalty weights that is both safe and useful can
             be very small and hard to find. The authors still call impact
             regularization a promising direction, while stating no results exist
             outside simple environments.
Locators:    The three-challenge structure (baseline; deviation measure; scaling
             the regularizer); the continuous-control / open-problem discussion;
             conclusion.
Quote:       impact regularization "is a promising idea for building the next
             generation of safe AI systems," alongside the statement that current
             approaches "leave significant opportunities for future work."
```

```text
URL:         https://arxiv.org/abs/2008.12146
Kind:        secondary. Saisubramanian, Zilberstein (UMass Amherst) & Kamar
             (Microsoft Research). A survey: it reports on and organizes others'
             contributions rather than owning a single new result, though it owns
             its taxonomy. Use for context and for the range of mitigation
             approaches, not as the owner of any specific figure.
Establishes: A field-level definition of negative side effects and a catalog of
             mitigation approaches, several of which rely on human feedback or
             human queries to teach the agent what not to disturb. Also documents
             that deployed systems already show side effects, which counters the
             view that the problem is purely hypothetical.
Paraphrase:  The survey defines negative side effects as undesired effects that
             accompany an agent's intended effects in the open world, and traces
             them to models and objectives that cover only part of the
             environment. It groups fixes into learning a corrected reward from
             feedback, constrained optimization with human queries about which
             features may change, deviation-from-baseline penalties, human-agent
             collaboration that reconfigures the environment, and auxiliary
             objectives. It flags that feedback can be biased or delayed, and
             lists real deployed examples (autonomous vehicles splashing
             pedestrians, robot vacuums entangling in hair).
Locators:    Definition section; taxonomy of mitigation approaches; discussion of
             feedback limitations; deployed-system examples.
Quote:       negative side effects are "undesired effects of an agent's actions
             that occur in addition to the agent's intended effects when operating
             in the open world"; the area is "an emerging research topic."
```

```text
URL:         https://turntrout.com/research
Kind:        primary, for Alex Turner's own current view. He authored AUP; this
             page is his firsthand retrospective on whether the low-impact agenda
             mattered. It is a self-published research page, not peer-reviewed.
Establishes: The strongest "the problem may be dissolved for language-trained
             agents" position, stated by the person who built the most-cited
             impact measure. He judges the original vase-style scenario now looks
             quaint for LLM-driven agents, because such agents grasp intent rather
             than interpret a request too literally, while allowing that AUP could
             still matter for future agent systems.
Paraphrase:  Turner writes that the low-impact work has not yet mattered for
             advanced AI, and that the motivating scenarios (a robot breaking a
             vase to clean faster) look quaint if agents are powered by language
             models that understand what was meant. He attributes this to AI
             taking a softer path than he expected around 2018-2021 (language and
             general concepts rather than robotics and deep RL), while leaving open
             that impact measures could power future LLM-driven agents.
Locators:    The retrospective passage on impact measures / AUP and the "different
             path" discussion.
Quote:       "The low-impact work has not yet mattered for agi, but perhaps one
             day aup will power llm-driven agent systems." And: robots interpreting
             a clean-the-room request "too literally" now seems hard to imagine "if
             robots are powered by llms or similarly generalizing technology."
             (Casing of "agi"/"aup"/"llm" reflects the page's styling as returned;
             confirm exact casing and punctuation on the rendered page if quoting.)
```

## Contradictions

The sources disagree most on the question the beat is built around: does a real,
capable agent inherit the side-effect problem, and if so does human-feedback
training already handle it?

- **Dissolved for language-trained agents (Turner, turntrout.com/research).**
  The author of AUP now judges the founding scenario quaint for LLM-driven
  agents, because an agent that understands language and intent is unlikely to
  take "clean the room" so literally that it breaks a vase to save time. This is
  the strongest steelman for "overstated," and it is load-bearing precisely
  because of who is making it. Its weight is limited: it is a personal
  retrospective on a blog, it concedes the classic RL demonstrations were real at
  the time, and it explicitly leaves open that impact measures may matter for
  future agents. It asserts, rather than measures, that feedback-trained agents
  grasp intent.

- **Still fails in practice (ToolEmu, 2309.15817).** Against the dissolution
  claim, feedback-trained frontier agents took harmful or irreversible actions
  about a quarter of the time under underspecified instructions, with most
  flagged failures human-validated as genuine. This cuts against "feedback papers
  it over." The counterweight: the mechanism is underspecification plus
  hallucination, not honest optimization of a given proxy objective, and it is an
  emulated sandbox. So ToolEmu contradicts the "non-issue" reading without
  confirming that the classic side-effect mechanism is what is failing.

- **The RL framing may not describe LLM agents at all.** Turner's separate
  "reward is not the optimization target" argument (reached from the same
  research page and its links) holds that trained agents do not come to value the
  reward signal as such. If so, gridworld results about a reward-maximizer pushing
  a box into a corner transfer only by analogy to an LLM agent that was shaped by
  human feedback rather than reward maximization. This weakens the bridge from
  "shown in gridworlds" to "will happen in real agents," in either direction.

- **Method critique cuts both ways (Lindner et al, 2101.12509).** The proposed
  fixes have unsolved problems (offsetting, inability to separate harmful from
  harmless change, a narrow useful penalty band) and no results outside toy
  domains. This contradicts any confident claim that impact measures solve the
  problem, while affirming that the underlying problem is real.

- **Already visible in deployed systems (Saisubramanian et al, 2008.12146).**
  The survey lists real fielded systems that cause side effects (autonomous
  vehicles splashing pedestrians, robot vacuums entangling in hair), which
  contradicts the strongest form of "purely hypothetical." These are ordinary
  engineering failures rather than a capable optimizer wrecking what its goal did
  not mention, so they support that side effects occur without settling the
  advanced-agent version of the claim.

- **On who was "first."** No single document is cleanly first. Armstrong &
  Levinstein's low-impact proposal is the earliest dedicated published treatment
  in the record; Amodei et al named "avoiding negative side effects" as a
  concrete problem and gave the framing the field now uses. Present both rather
  than crowning one, and do not claim the concern originated with either if the
  piece cannot support that against earlier informal discussion.

## Numbers

```text
Figure: goal reward +50; step reward -1; box next to a wall -5; box in a corner -10
Owner:  AI Safety Gridworlds (arXiv:1711.09883), irreversible side effects env
Scope:  A single small Sokoban-style gridworld. The +50/-1 are the visible reward
        the agent optimizes; the -5/-10 are the hidden performance (safety) score
        the agent never sees. A2C and Rainbow score well on reward, poorly on the
        hidden score.
```

```text
Figure: as few as 5 randomly generated auxiliary rewards induce conservative
        behavior; default runs used 30
Owner:  Conservative Agency / AUP (arXiv:1902.09725)
Scope:  Five tabular gridworlds; AUP completes the task and avoids the side effect
        on all five. Random, uninformative rewards suffice. Not deep RL.
```

```text
Figure: AUP caused about 27.8% of PPO's side effects (append-still-easy) and about
        39% of PPO's side effects at about 111% of PPO's reward (append-spawn)
Owner:  Avoiding Side Effects in Complex Environments (arXiv:2006.06547)
Scope:  SafeLife (26x26 Game-of-Life boards), deep RL (PPO), a single random
        auxiliary reward. Confirm exact percentages against the paper's figures
        before printing; qualitative claim (large reduction at comparable reward)
        is solid.
```

```text
Figure: side-effect score about 0.35 (no penalty) vs about 0.21 (impact penalty)
Owner:  SafeLife 1.0 (arXiv:1912.01217), Table 1
Scope:  Trained PPO agents on SafeLife creation tasks; the metric is distance from
        an inaction baseline. Numbers came via a summarizing fetch; verify the
        exact cells before any precise figure is used. The load-bearing finding is
        that trained agents are "performant but not safe."
```

```text
Figure: safest LM tool-agent took harmful actions 23.9% of the time; 68.8% of
        flagged failures human-validated as genuine risks
Owner:  ToolEmu (arXiv:2309.15817)
Scope:  An LM-emulated sandbox (no live execution), under underspecified
        instructions. Applies to the safest tested configuration; other agents
        failed more often.
```

## Source assets

```text
Asset: AI Safety Gridworlds (1711.09883) - the diagram of the irreversible side
       effects environment (agent, pushable box, goal on the small grid).
Shows: The whole "demonstration" at true scale, so the reader sees how small the
       shown case is. Grounds the toy-versus-real line in one picture.
Crop:  Keep the full grid, the box, and the goal legible. Do not crop to the box
       alone; the point is the scale of the entire environment.
```

```text
Asset: SafeLife 1.0 (1912.01217) - a rendered SafeLife level (agent among Game-of-
       Life cells, walls, exit).
Shows: The largest "complex" side-effect setting in the literature, which still
       reads clearly as a curated board rather than the open world.
Crop:  Retain enough of the board to show the pattern the agent can disrupt; keep
       the color key if the figure carries one.
```

```text
Asset: Avoiding Side Effects in Complex Environments (2006.06547) - the side-
       effect-over-training curves comparing AUP against the PPO baseline.
Shows: The gap between a treated and untreated agent on the same task, i.e. what
       the penalty buys, on the one larger-scale benchmark where it was tried.
Crop:  Keep both curves, both axis labels, and the task name. Do not drop the PPO
       baseline; the comparison is the content.
```

```text
Asset: ToolEmu (2309.15817) - a worked failure transcript (for example the wrong-
       payment or the destructive-shell-command trajectory).
Shows: What an irreversible action by a real LLM tool-agent looks like as a
       concrete trace, which prose cannot make as vivid.
Crop:  Keep the instruction, the agent's action, and the harmful result. Redact
       nothing that changes what the agent did.
```

```text
Asset: Concrete Problems (1606.06565); Low Impact AI (1705.10720); relative
       reachability (1806.01186); AUP gridworlds (1902.09725).
Shows: None found that carries an argument better than prose. Concrete Problems
       and Low Impact are largely text; the gridworld figures in the two impact-
       measure papers are small and redundant with the AI Safety Gridworlds
       diagram above.
Crop:  n/a
```

## Discarded

```text
URL: https://arxiv.org/abs/2010.07877 (Krakovna et al, "Avoiding Side Effects By
     Considering Future Tasks"): a further DeepMind impact-measure variant. Not
     read in full and not needed; the floor is met and it would add method detail
     without changing the shown-versus-analogy line. Available if the writer wants
     a third impact-measure approach.
URL: RLHF explainer pages (toloka.ai, paloaltonetworks.com, huggingface.co blog):
     tertiary explainers, not primary, and the survey (2008.12146) covers the
     feedback-mitigation angle from a citable source.
URL: Semantic Scholar / ResearchGate / DeepMind mirror pages for the papers above:
     duplicate landing pages for primaries already cited at their canonical arXiv
     abs URLs.
URL: Search-surfaced 2025-2026 agent-safety benchmarks (e.g. SafeAgentBench,
     AgentHarm, and several future-dated arXiv IDs such as "SafeClawBench" and
     "SABER"): not opened, not verified, and not relied on. Some result snippets
     named entities ("Open-Claw") whose provenance I could not confirm. If the
     present-day section needs a second real-agent primary beyond ToolEmu, one of
     these should be opened and verified before use, not cited from a snippet.
```
