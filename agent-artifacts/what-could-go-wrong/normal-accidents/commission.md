# Commission: what-could-go-wrong/normal-accidents

## Assignment
Teach normal-accident theory as an argument about how AI could go wrong: Charles
Perrow's claim that in systems with high interactive complexity and tight
coupling, catastrophic failures are a normal property of the system rather than
the fault of any one part. Present the argument at full strength, test it against
what AI systems actually do, and bring it to the present.

## The desk's shape, applied
- Open with the argument at full strength. Name Perrow and what he had seen:
  "Normal Accidents: Living with High-Risk Technologies" (1984), written in the
  aftermath of Three Mile Island (1979). Define his two axes in plain words:
  interactive complexity (parts interact in ways operators cannot foresee) and
  tight coupling (little slack, so a fault propagates before anyone intervenes).
  Lay out the reasoning its most careful defender would give.
- Then test it against real systems. Draw the sharp line the desk requires. What
  has already been shown in a working system: automated, tightly coupled
  failures that ran faster than human intervention. What is still analogy or
  guesswork: catastrophic "normal accidents" in future agentic-AI infrastructure
  that does not yet exist. Be honest that Perrow's theory has itself been
  contested (High Reliability Organization theorists argued some complex systems
  operate safely), and steelman that objection before weighing it.
- Bring it to the present. Say who applies this lens to AI now and what they want
  done (systemic-risk framings of AI in critical infrastructure, coupled model
  deployments, agentic systems acting without slack). Check the confidence
  against the proof. Where the systemic-catastrophe claim outruns the evidence,
  name the gap.

## Why this argument, why now
The what-could-go-wrong desk has covered the alignment canon thoroughly but never
the systems-safety lens: the argument that accidents can be structural, not
intentional or misaligned. It is a distinct way of reasoning about AI risk the
reader has not been given, and it reframes several pieces they have already read.

## Boundaries: link, do not re-teach
- what-could-go-wrong/flash-crash-risk is a demonstrated coupled-automation
  failure (the 2010 Flash Crash). Use it as a shown instance and link it; do not
  re-report it as this piece's center.
- what-could-go-wrong/algorithmic-monoculture is the correlated-failure-from-
  shared-models argument. Link it as a related mechanism; keep normal-accident
  theory (interactive complexity plus tight coupling) as the distinct subject.
- Do not drift into misalignment framings (instrumental-convergence, reward
  failures). The whole point is that this argument does not need a misaligned
  goal: well-behaved parts still produce system accidents.

## Neighbors this edition
Tonight also runs when-ai-breaks/character-ai-lawsuit, a single company's
product-safety failure. Keep this piece on the general systems-theory argument,
not on any one incident's blame.

## Sources
Lesson floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary: Perrow's book and papers, the primary record of any incident cited
firsthand (e.g., the official Flash Crash report), and the primary statements of
present-day proponents and critics. Secondary: outside analysis for context.
Read Perrow directly, not summaries of him; when his framing is dated, say how.
Name no company as an authority; cite arguments to their authors.

## Production record
- Profile: balanced. Roles run as isolated Claude subagents (capable tier).
- Effort by stage: writing-coach low, researcher high, writer medium, editor high.
- Writer records the actual writer model in nb-meta `model`, sets `harness` to
  `claude-code`. Article date: 2026-09-17.

## Recent habits to break
- Do not open with a heading of the form "What <Person> saw in <place>"
  (deskilling used "What Bainbridge saw in the control room"; suffering-risks
  used "What worried Brian Tomasik...").
- Do not build the dek as "the strongest evidence is a single <X> study"
  (deskilling) or "borrows its <thing> from <source> that never mentions <Y>"
  (suffering-risks), nor date the idea with a bare "dates to <year>" tail.
- Avoid the two-sentence terse-rebuttal headline mold and the comma-triad dek.
- The takeaway bookend lands the judgment; no Verdict block.
