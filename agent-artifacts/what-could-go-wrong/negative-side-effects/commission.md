# Commission: what-could-go-wrong/negative-side-effects

## Assignment

Teach the argument that a capable agent optimizing almost any objective will
damage parts of the world it was never told to protect, because "change nothing
you were not asked to change" turns out to be very hard to specify. In the
safety literature this is the negative-side-effects or low-impact problem.

This is a lesson on What Could Go Wrong. Open with the argument at full strength:
name who first made it and what they had seen that worried them, and lay out the
reasoning the way its most careful defender would, so the reader sees why serious
people hold it before reading a word against it. Then test it against what real
systems actually do, drawing a sharp line between what has been shown in a working
system and what is still analogy about systems that do not exist yet. Then bring
it to the present: who argues it now, what they want done, and what the most
recent evidence says. Where confidence outruns proof — in either direction — name
the gap. Work from the original papers, not commentary. Name no company as an
authority. Leave the reader to decide how worried to be.

## The gap this closes

This desk has the neighboring arguments but not this one, and the reader must be
able to tell them apart. `what-could-go-wrong/reward-hacking` is about an agent
exploiting the *specification* of its objective; `instrumental-convergence` is
about an agent seeking power as a subgoal; `goal-misgeneralization` is about an
agent that learned the *wrong* goal. The side-effects argument is different: the
agent can pursue exactly the goal we gave it, honestly, and still wreck
everything the goal did not mention, because the objective is a thin slice of what
we care about. Link `reward-hacking` and `instrumental-convergence` at first use
to mark the boundary; do not re-teach them.

## Required contribution

Give the reader the exact shape of the argument and, above all, the sharp line
the beat demands:

- **Shown.** The demonstrations live in small, controlled settings — the safety
  gridworlds and side-effect benchmarks — where agents cause avoidable damage and
  proposed penalties (relative reachability, attainable-utility preservation, and
  the like) measurably reduce it. Report what those environments actually showed
  and at what scale.
- **Analogy.** The claim that this is a core obstacle for real, open-world agents
  is not established by a working system; no general low-impact agent exists.
- **The present.** Say who presses the argument now and what they want, and check
  it against recent work, including the live question of whether LLM tool-agents
  inherit the problem or whether human-feedback training papers over it. Name
  where the confidence — that it is a central danger, or that it is a non-issue —
  runs past the evidence.

Earn the piece by leaving the reader able to state the argument at its strongest,
locate the toy-versus-real boundary precisely, and judge the current confidence on
its merits rather than by who is voicing it.

## Sources

Floor (from `nb source-policy`): at least 8 sources, at least 4 primary, at least
1 secondary. Primary means the document that owns the claim: the founding
safety-agenda paper and the earlier low-impact proposals; the gridworld and
side-effect benchmark papers; the impact-measure papers; and any recent primary
bearing on agents in the open world. Read the papers and the exact results; a
reported effect must name the environment and method. Commentary and secondary
summaries are context only.

## Template and metadata

Template: `lesson`. `nb-meta` tags (writer sets, 4-6, lowercase hyphenated),
candidates: side-effects, low-impact-agents, ai-safety, reward-specification,
impact-measures. Date 2026-09-21. `harness` "claude-code"; `model` the writer's
actual served model.

## This run's neighbors

Four other lessons publish tonight: `the-evidence/backpropagation`,
`the-instruments/comet-score`, `the-mechanics/false-premise-questions`,
`when-ai-breaks/chatgpt-data-leak`. Distinct subjects; nothing to deconflict.

## Recent shapes to break (habits, not rules)

The beat itself fixes the argument's arc (full strength, then shown-versus-
analogy, then present and gap), so the sections will resemble other What Could Go
Wrong lessons by design. What must not carry over is the wording: recent pieces
lean on the dek mold "feasible on paper and unshown in any working system" and on
near-identical headings like "what a working system has been shown to hold" and
"how far the confidence runs past the proof," and close on "who makes the case
now." Write every heading and the dek in this piece's own nouns, and do not copy
those slots. Furniture such as `nb-holdsup` or `nb-table` is available where the
shown-versus-analogy split genuinely calls for it, not by reflex.

## Production policy (actual)

`nb production-policy`: profile `balanced`, tier `capable`, no `required`.
Resolved for this run's isolated subagents: researcher Opus 4.8 (high),
writing-coach Sonnet (low), writer Opus 4.8 (medium), editor Opus 4.8 (high).
Efforts advisory.
