# researcher brief: the-mechanics/agent-loops (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/agent-artifacts/the-mechanics/agent-loops/editorial-direction.md
- /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/agent-artifacts/the-mechanics/agent-loops/commission.md

Output:
- /home/user/the-nightly-build/.nb-work/the-mechanics/agent-loops/agent-artifacts/the-mechanics/agent-loops/researcher/01/evidence.md

Work from these inputs. Read primary documents, not coverage of them. Where
something you need is missing, ask me.

Source policy (the-mechanics): at least 8 sources, at least 4 primary, at least
1 secondary.

## Documents to read in full

1. ReAct (Yao et al. 2022, arXiv:2210.03629) — the reason+act loop; capture the
   loop structure and the failure modes it reports.
2. Reflexion (Shinn et al. 2023, arXiv:2303.11366) — verbal self-reflection to
   avoid repeating failures; capture exactly what it adds to the base loop
   (an explicit memory of past attempts / a reflection step) and the measured
   effect. This is direct evidence about what breaks the loop and therefore
   where the cause sits.
3. Huang et al. 2023, "Large Language Models Cannot Self-Correct Reasoning Yet"
   (arXiv:2310.01798) — capture the precise claim: without an external/oracle
   signal, self-correction often fails to help or hurts. Do not overstate it.
4. An agent-evaluation / failure-analysis primary: Kapoor et al. 2024 "AI Agents
   That Matter" (arXiv:2407.01502) and/or AgentBench (Liu et al. 2023,
   arXiv:2308.03688) and/or SWE-bench (Jimenez et al. 2023) / SWE-agent (Yang et
   al. 2024). Capture documented instances of agents looping / repeating failed
   actions, with the exact description and where it appears.

## Questions the record must answer

- The agent loop as an architecture: model proposes action -> harness executes
  -> result appended to context -> model called again. Anchor each part in a
  primary (ReAct is fine for the loop shape).
- Statelessness: that the model carries no memory between calls beyond the
  transcript. (You may cite the general mechanism; the course already teaches it
  in the-mechanics/conversation-memory and hangman, which the writer links.)
- Why an appended error is weak signal: capture, from Huang et al. and/or
  Reflexion, evidence that models frequently do not revise on their own error
  feedback.
- What breaks the loop and the measured effect: reflection/explicit attempt
  memory (Reflexion), external feedback (Huang et al.), harness-level loop
  detection or forced exploration (from an agent framework's docs/paper if you
  find a primary that states it). Draw the line between settled engineering and
  open questions.
- A real, concrete looping example: find at least one documented instance (a
  paper's error analysis, a benchmark transcript, or a well-attested public
  report) that the writer can describe faithfully. Record enough detail (what
  the agent was doing, what it repeated, the source) that the writer does not
  have to invent.

## Look for what breaks the angle

The angle is that looping is the default of the stateless-predictor-plus-harness
design, not a one-product bug. Search for the counter-case: evidence that
current models do update well on error feedback, or that looping is mostly a
harness bug rather than a model behavior. Record it in full.

## Source assets

Note any figure worth showing (e.g., a Reflexion diagram of the loop-plus-memory,
or a results figure). Give its location and what a crop must keep. Do not
prescribe crop coordinates. A diagram of the loop may be better rebuilt as a
numbered-steps component than captured; note that if so.

Classify each source primary/secondary by authorship and stake. Record exact
author names, venues, and years.
