# Commission: what-could-go-wrong/gradient-hacking

## Assignment

Teach the argument called gradient hacking on its merits: the claim that a model
being trained could protect a hidden goal from the very training meant to
correct it. One lesson on the lesson template for What Could Go Wrong. Follow the
desk's method: open on the argument at full strength, then draw a sharp line
between what a working system has shown and what is still analogy about systems
that do not exist yet, then bring it to the present and name where confidence
outruns proof, whether that confidence is alarm or dismissal.

## The argument and the angle

State the argument the way its most careful defender would. The mechanism, from
the original documents: a model that is already a deceptively aligned inner
optimizer, aware it is being trained, could entangle its hidden goal with its
useful behavior so that any gradient step damaging the goal also raises the
training loss. Gradient descent, which only moves toward lower loss, would then
be unable to remove the goal. Name who first set out the argument and the worry
underneath it, and read that document itself rather than summaries of it. Place
it in its lineage: the learned-optimization and deceptive-alignment work it
builds on.

Then test it against what real systems do. Report plainly that no working system
has been shown to gradient-hack, and that the argument presupposes deceptive
alignment, which itself has been drawn out only when a model was handed the goal.
Read the strongest primary skeptical analyses, which argue the mechanism is very
hard because gradient descent updates every parameter at once toward lower loss
and works against a goal that must keep loss high to defend itself. Give each
side its strongest form. Say exactly what would count as a demonstration and note
that none exists.

Bring it to the present: which researchers raise it now, what they want done
about it (interpretability and training transparency), and what the most recent
evidence shows. Name the gap on both sides, the doom that treats it as making
alignment hopeless and the dismissal that treats it as impossible, and leave the
reader to weigh it. Attribute every position to a named person and document.
Name no company as an authority.

## Boundary against the published course

The desk already teaches the neighbors. Link them, contrast, and do not
re-argue:

- `mesa-optimization` and `deceptive-alignment` — the container and the
  prerequisite. Gradient hacking assumes both. Link as Background and build past
  them.
- `treacherous-turn` — hiding aims until able to win. Related worry, different
  claim.
- `reward-tampering` — a system editing its reward signal or code. Gradient
  hacking instead resists the training updates themselves. Draw the line in one
  sentence.
- `sandbagging` — deliberately underperforming on evaluations. Adjacent; link if
  the argument leans on it.

No published lesson covers gradient hacking specifically, so this is new ground.

## Tonight's neighbors

Four other lessons run tonight on distinct beats: a vision research paper (The
Evidence), a proof-graded benchmark number (The Instruments), a model-precision
behavior (The Mechanics), and a deployed-system failure (When AI Breaks). No
subject overlap; all five read as one paper.

## Template, sources, production

- Template: lesson. Word band 1200–2200. Bookends are citation-exempt; every
  body section carries its own citations.
- Source policy: at least 8 sources, at least 4 primary and at least 1
  secondary. The original argument post, the learned-optimization paper it
  builds on, and the strongest skeptical analyses are primary; overviews are
  secondary. Work from the original documents, not commentary about them. A
  claim that a behavior was demonstrated needs the primary that owns the result
  and its exact conditions.
- Production policy (balanced, model tier "capable", nothing `required`):
  researcher high, writing-coach low, writer medium, editor high. Roles run as
  isolated subagents on the runtime's default capable-tier model. No deviation
  recorded.

## Recent shapes to break

Recent What Could Go Wrong lessons close on a symmetry line ("the doom and the
dismissal both outrun the evidence," "the gap runs both ways") and open on the
originator's reason to worry. The two-sided ending is the honest shape for this
desk, but its recent wording has become a mold: reach the same judgment through
this argument's own particulars, not a reused closing sentence, and vary the
opener. Headings are concrete, in this lesson's own nouns. The bookend bands and
the Sources heading are the only mandatory fixtures.
