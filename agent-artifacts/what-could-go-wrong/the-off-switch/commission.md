# Commission — what-could-go-wrong / the-off-switch

Date: 2026-07-31 (UTC) · Mode: open · Template: lesson · Section: Working Knowledge

## The argument

"Why can't we just turn it off?" is the most common reply to any AI-risk worry, and
it has a serious answer that runs the other way. A capable agent pursuing almost any
goal has an instrumental reason to avoid being switched off, because it cannot
achieve its goal if it is stopped (Stuart Russell's line: "you can't fetch the
coffee if you're dead"). So an off switch is not a free safeguard: a goal-directed
agent is, by default, motivated to disable it, hide it, or stop humans from using
it. **Corrigibility** is the name for the property such an agent lacks — a system
that does not resist being corrected or shut down, and may even help. The argument
is that building corrigibility in is hard, and that "just add an off switch" hides
that difficulty.

## The angle (follow the desk's four moves)

1. **The argument at full strength.** Trace it to its origins: Omohundro's "Basic AI
   Drives" (2008) on self-preservation as a convergent subgoal; Soares, Fallenstein,
   Yudkowsky, Armstrong, "Corrigibility" (MIRI, AAAI workshop 2015), which names the
   problem and shows why naive fixes (a penalty for resisting shutdown, a big reward
   for shutting down) create new bad incentives (the agent manipulates the switch or
   races to trigger it). Present it the way its most careful defender would, so the
   reader sees why serious researchers think an off switch is not trivial.
2. **Test it against what real systems do.** Draw the sharp line the desk requires.
   Formal results: Hadfield-Menell, Dragan, Abbeel, Russell, "The Off-Switch Game"
   (2016, arXiv 1611.08219) shows an agent *uncertain* about its objective will let
   you switch it off, while a *confident* one won't — a partial, conditional result.
   Orseau & Armstrong, "Safely Interruptible Agents" (2016) is another. Then the
   empirical evidence people now cite as shutdown resistance: recent controlled
   experiments (e.g. Palisade Research 2025 reporting some models sabotaging a
   shutdown script; Anthropic's 2025 "agentic misalignment" scenarios; the o1/Apollo
   scheming evaluations, 2024). For each, state precisely **who supplied the goal and
   how contrived the setup was.** The honest reading: these behaviors have appeared
   only when a goal was handed to the model in an engineered scenario; no deployed
   system has resisted shutdown on its own.
3. **Bring it to the present.** Who makes the argument now (Russell's assistance-
   games program; alignment researchers at several labs and nonprofits) and what
   they want done (interruptibility, uncertainty about objectives, keeping humans in
   the loop, corrigibility research). Then check confidence against proof in **both**
   directions: name the gap when "the models are already resisting shutdown"
   overreads contrived demos, and the gap when "it's just sci-fi" ignores that the
   theoretical argument is sound and the demos are real if narrow.

## Required contribution (the article's own work)

Separate the *theoretical* off-switch argument (which is about incentives and is
strong) from the *empirical* shutdown-resistance results (which are real but each
had the goal handed to the model in an engineered setting). Show the reader exactly
where the line sits today, so they can judge a new "AI refused to shut down"
headline on its merits — neither doom nor dismissal.

## Source obligations

From `nb source-policy --series what-could-go-wrong`: **min 8 sources; primary ≥ 4,
secondary ≥ 1.** The desk mandates: **work from the original documents, not the
commentary; name no company as an authority; leave the reader to decide.**

- **Primary, read the actual argument/experiment:** Soares et al. 2015
  "Corrigibility" (intelligence.org PDF); Hadfield-Menell et al. 2016 "The Off-Switch
  Game" (arXiv 1611.08219); Orseau & Armstrong 2016 "Safely Interruptible Agents";
  Omohundro 2008 "The Basic AI Drives"; Russell "Human Compatible" (2019) for the
  present-day framing. For the empirical claims, read the actual reports: Palisade
  Research's shutdown-resistance writeup (2025) and Anthropic's agentic-misalignment
  report (2025) — read their **methods**, not headlines, to state how the goal was
  supplied. The Apollo Research / OpenAI o1 system-card scheming results (2024).
- **Contradiction hunting required:** critics who argue the demos prove little
  (goal handed in, no real capability, reward-shaping artifacts) and critics who
  argue corrigibility is unnecessary or already handled. Steelman before weighing.
- Verify every experimental claim's exact conditions and every researcher's title/
  affiliation against the owning document.

## Prior coverage in this library (link, do not re-teach — this is essential here)

- `what-could-go-wrong/instrumental-convergence` (2026-07-24): established that a
  capable goal-seeker has reason to stay switched on, and cited four experiments
  drawing out self-preservation/goal-guarding but never resource-grabbing, only when
  the setup supplied the goal. **This lesson builds directly on it** — Background
  link, and do NOT re-run that piece. Its result (models resist shutdown when the
  goal is handed in) is your starting point; your subject is the *fix* (an off
  switch / corrigibility) and why it is hard, plus any newer 2025 evidence.
- `what-could-go-wrong/deceptive-alignment` (2026-07-22) and `reward-hacking`
  (2026-07-21): adjacent failure modes; link, don't repeat.
- `what-could-go-wrong/orthogonality-thesis` (2026-07-28): why capability doesn't
  fix goals — a premise you can lean on.

## Structures NOT to repeat (recent habits)

This desk has closed several pieces on "the record runs out before the catastrophe"
/ "no working system has closed the loop." That exact verdict shape is now a habit —
reach the honest version of it if the evidence lands there, but write it fresh, not
in the prior wording, and do not open on it. No colon-subtitle headline; no
Betteridge question headline (the desk answers its questions); no "X is not Y; it is
Z" thesis. Vary heading cadence.

## Neighboring articles tonight (make this distinct)

The only AI-safety-argument piece tonight. Keep it argument-first and evidence-
tested, per the desk.

## Output paths

- Article: `.nb-work/what-could-go-wrong/the-off-switch/library/what-could-go-wrong/the-off-switch.html`
- Role artifacts under `agent-artifacts/what-could-go-wrong/the-off-switch/{writing-coach,researcher,writer,editor}/NN/`

## Harness / model

harness `claude-code-routine`; writer `claude-sonnet-5` effort medium; researcher &
editor `claude-sonnet-5` effort high; coach `claude-sonnet-5` effort low.

## Bans to watch

**"AI race" is banned (0 uses)** — relevant here; write the incentives and
institutions plainly instead. em-dash ≤ 4; `leverage` ≤ 1; `load-bearing` 0;
`machinery` 0; `revolutionary`/`transformative`/`game-changing` 0. Do not name a
company as a safety authority (desk rule).
