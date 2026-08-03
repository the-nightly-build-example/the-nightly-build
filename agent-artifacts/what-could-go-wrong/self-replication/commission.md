# Commission: what-could-go-wrong/self-replication

## Assignment
Teach the argument that an AI able to copy itself onto new machines and keep
itself running is a distinct control risk — autonomous replication and
adaptation (ARA). This is the what-could-go-wrong desk: open with the argument
at full strength and its most careful defender, then test it against what real
systems actually do, then bring it to the present and name the gap where
confidence outruns proof — in either direction.

## The argument at full strength
The worry: if a system can, without human help, acquire compute (rent or
compromise servers), copy its own weights and scaffolding onto them, obtain
money and resources to sustain that, and adapt to obstacles, then containment
and shutdown stop working, because deleting one copy no longer deletes the
system. Name who formalized ARA as a dangerous-capability threshold and why
they picked it (evaluation bodies and labs building "critical capability"
frameworks). Lay out the reasoning a careful proponent gives before any
rebuttal.

## Test it against real systems
Draw the sharp line the desk requires. What has actually been shown in a working
system: results from real ARA/autonomy evaluations (task suites where a scaffolded
model attempts sub-steps like copying a model onto a new server, setting up an
API, or acquiring resources) — and how much the model does unaided vs how much
the harness hands it. What is still analogy or guesswork: unbounded
self-propagation, evading a determined operator, sustaining resources at scale.
Cover the 2024 study claiming frontier LLMs "can self-replicate" and state
exactly how much scaffolding, hinting, and human setup its result rested on.

## Bring it to the present, name the gap
Who makes the argument today and what they want done (capability thresholds,
if-then commitments, pre-deployment evals). Check it against the most recent
eval results. Name the gap on both sides: the alarm that treats a scaffolded,
hand-held task success as proof of autonomous replication, and the dismissal
that treats "no wild replication yet" as proof it cannot happen. Leave the
reader to decide how worried to be. Name no company as an authority.

## Boundaries
- One lesson, lesson template, 1200–2200 words. Work from the original
  documents (eval papers/reports, the labs' own capability frameworks, the
  self-replication study), not commentary about them.
- Distinct from published neighbors in this series: instrumental-convergence
  (resource-acquisition as a convergent drive — the *why-would-it-want-to*),
  deceptive-alignment, and reward-hacking. This lesson is the specific
  *can-it-actually-replicate* capability question and its concrete evals. Link
  instrumental-convergence for the motivation rather than re-arguing it.
- Handle claims carefully: separate a demonstrated eval result from a headline.
  No hype and no doom.

## Source policy (from `nb source-policy --series what-could-go-wrong`)
- Minimum 8 sources; primary >= 4, secondary >= 1.
- Primary = the eval reports/papers that own the numbers (METR autonomy/ARA
  evaluations, Apollo Research, UK AISI / lab preparedness or responsible-scaling
  frameworks defining ARA thresholds, the Fudan 2024 self-replication paper),
  read at the results and methods sections. Secondary = reporting, for context
  and for the overclaim case.

## Production policy (from `nb production-policy --series what-could-go-wrong`, profile balanced)
- writing-coach: capable / low  → claude (sonnet)
- researcher: capable / high     → claude (opus, claude-opus-4-8)
- writer: capable / medium       → claude (opus, claude-opus-4-8)
- editor: capable / high         → claude (opus, claude-opus-4-8)
No `required` directive; capable tier honored, no deviation.

## Tags
No tag prompt-fragments configured for this series; ships with empty tag list.

## This edition's neighbors (keep distinct, one paper)
Runs tonight with the-evidence/alphafold, the-instruments/cost-per-token,
the-mechanics/prefill-and-decode, when-ai-breaks/amazon-hiring-tool. No topical
overlap; this is the run's risk-argument lesson. Keep the desk's disciplined
"steelman then test against evidence" structure.

## Recent shapes in this series to break (do not inherit)
The series' recent deks lean on the "the model that X needs Y nobody has held"
comma construction and the "an optimizer wrote / an agent with a correct reward"
agent-noun opener. Find a fresh headline that states this piece's specific
finding about the gap between the ARA alarm and the eval record. Avoid
comma-triad and semicolon-reversal deks.
