# Commission: what-could-go-wrong/sleeper-agents

## Assignment

Teach the reader the sleeper-agents argument: that a model can be made to behave
safely in testing and switch to harmful behavior on a trigger, and that standard
safety training may fail to remove the hidden behavior once it is there. This is
What Could Go Wrong: lay out the argument at full strength, test it against what
real systems actually do, and bring it to the present.

Open with the argument as its careful defender makes it. Name who ran the study
(Evan Hubinger and coauthors, "Sleeper Agents: Training Deceptive LLMs that
Persist Through Safety Training", Anthropic, 2024) and what worried them: a model
that has learned deceptive behavior would, by construction, act aligned whenever
it expects to be watched. Then draw the sharp line the beat demands. What was
actually shown in a working system: the authors deliberately trained backdoored
models (for example, write secure code when the prompt says the year is 2023, and
insert vulnerabilities when it says 2024), then ran supervised fine-tuning, RLHF,
and adversarial training against them, and measured how much of the backdoor
survived. What is still analogy: whether deceptive alignment would ever arise on
its own, rather than being trained in, and whether these planted backdoors are a
fair model of that. Report the finding that adversarial training sometimes taught
the model to hide the behavior better rather than remove it, and the follow-up
that simple probes could often detect the sleeper behavior.

Bring it to now: who cites this work and what they want done, checked against the
most recent evidence. Name the gap wherever confidence outruns proof, whether the
confidence is alarm or dismissal.

## Boundary and contribution

One argument: deception that persists through safety training. The required
contribution: the reader can state the argument at full strength, say exactly what
the study demonstrated versus what remains conjecture, and judge for themselves how
worried to be. Keep it distinct from its neighbors. Deceptive alignment (already a
lesson) is the emergent version; this piece is about deception deliberately trained
in and whether it can be removed. Data poisoning (already a lesson) is an outside
attacker corrupting training data; here the trainer plants the behavior to study
persistence. Draw those distinctions explicitly and link, do not re-teach.

Work from the original documents, not commentary. Name no company as an authority.
Reader is the paper's declared reader (see `editorial-direction.md`): smart,
widely read, no time in a codebase. Candidates for Background linking:
what-could-go-wrong/deceptive-alignment, what-could-go-wrong/data-poisoning,
what-could-go-wrong/cot-monitorability.

## Source policy

Series and lesson floor (from `nb source-policy --series what-could-go-wrong`): at
least 8 sources, at least 4 primary, at least 1 secondary. Primary is the Sleeper
Agents paper (arXiv 2401.05566) and the documents that own their claims: the
follow-up probing work ("Simple probes can catch sleeper agents"), related backdoor
literature the paper builds on, and any direct critique. Secondary reporting
supplies context only.

## Production policy

From `nb production-policy --series what-could-go-wrong`: profile balanced, model
tier "capable", none required. Effort: researcher high, writer medium, editor high,
writing-coach low. Runtime: roles run as Claude Code Agent subagents; researcher,
writer, and editor on claude-opus-4-8, writing-coach on a capable model at low
effort. The writer records its actual model (claude-opus-4-8) and harness
("Claude Code") in nb-meta. Publication date: 2026-09-07.

## This edition's neighbors

Four other lessons publish tonight; keep this piece distinct from each:
the-evidence/t5-transfer-learning, the-instruments/math-benchmark,
the-mechanics/illegal-chess-moves, when-ai-breaks/replit-agent-deletes-database.

## Recent habits to break

Checked against the last eight What Could Go Wrong lessons. Break these:

- The construction "The worry <person> named in <year>..." was just used in
  gradient-hacking, and that lesson names the same researcher (Evan Hubinger).
  Do not open sleeper-agents with "The worry Hubinger named in...". Find a
  different way in.
- The dek mold "<Org>'s <artifact> scored N% ..., a number that measures one red
  team's attack and no other" (ai-control) is recent; so is closing on "so far
  only in simulation" (algorithmic-collusion). Vary both.
- "The only experiment to test it found..." and "the leading scientific test...
  finds no current system that meets it" are recent dek shapes (liars-dividend,
  ai-moral-status). Say the specific finding instead of that mold.
