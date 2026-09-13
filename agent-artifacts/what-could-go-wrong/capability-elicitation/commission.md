# Commission: what-could-go-wrong/capability-elicitation

## Assignment
Teach one argument about how AI could go wrong: that a passing safety evaluation
cannot prove a model is safe, because what a model can do depends on how hard you
try to make it do it. A failed dangerous-capability test is a lower bound, not a
ceiling. One lesson on the What Could Go Wrong desk. Template: lesson.
Publication date: 2026-09-13.

## Why this argument, now
The desk has covered many failure arguments, including a model hiding what it can
do (`what-could-go-wrong/sandbagging`), safety training being stripped after
release (`what-could-go-wrong/open-weights-release`), and whether we can oversee a
model's reasoning (`what-could-go-wrong/cot-monitorability`). It has not taught the
argument underneath the whole practice of pre-deployment evaluation: capability is
elicitation-dependent, so the number a lab reports is only as high as its own
effort to draw the capability out. This is the live methodological fault line in
2025-2026 safety cases, and the reader needs it to judge every "our model scored
below the danger threshold" claim.

## The angle (the desk's arc)
Open with the argument at full strength, from the people who make it. State it the
way a careful evaluator states it: an evaluation measures the capability of a
model plus the elicitation effort applied to it, so a low score can mean the model
is safe or that the testers did not try hard enough, and the two are hard to tell
apart. Name who argues this (evaluation organizations and lab safety teams) and
what they had seen that worried them.

Then test it against what real systems actually do. Draw the sharp line the desk
demands: what has been shown in working systems versus what is still inference.
Shown: better prompting, fine-tuning, tool and scaffold access, and more attempts
raise measured capability by large margins on the same model; safety fine-tuning
can be cheaply undone. Inference: that dangerous latent capabilities we have not
yet elicited are lurking behind today's passing evals.

Bring it to the present: how labs and government evaluators treat eval results now
(as lower bounds, with elicitation guidelines and red-team budgets), and where
confidence still outruns proof, in either direction, doom or dismissal. Name the
gap. Name no company as an authority; leave the reader to weigh how much comfort a
passed eval should give.

## What the reader already holds — do not re-teach, link instead
- A model deliberately underperforming to look safe: link
  `what-could-go-wrong/sandbagging` in Background and draw the distinction clearly
  (elicitation gap is about the testers' effort; sandbagging is about the model's
  choice).
- Fine-tuning removing safety training: link `what-could-go-wrong/open-weights-release`.
- Benchmark contamination and why a score is fragile: the reader has the
  Instruments desk; link one relevant lesson only if a Background row earns it.

## Research directions (researcher owns depth)
1. The strongest primary statement of the argument: evaluation-organization and
   lab-safety writing framing eval scores as lower bounds and capability as
   elicitation-dependent (for example, METR's capability-elicitation guidance, UK
   AI Safety Institute / AISI evaluation writeups, and lab responsible-scaling or
   preparedness documents). Quote the actual claim.
2. Real evidence that elicitation moves the number: measured gains from prompting,
   fine-tuning, tool use, scaffolding, and repeated sampling on a fixed model
   (with figures), and the cheap removal of safety fine-tuning. Read the papers
   that own these figures.
3. A concrete case where a first evaluation understated a capability later drawn
   out by better elicitation (e.g., a model judged incapable on a task that a
   scaffold or fine-tune then unlocked). One real instance, sourced.
4. The counter-case and the limit: where the argument overreaches (a passed eval
   is not worthless; elicitation cannot conjure a capability that is not there),
   and evidence bounding how large elicitation gaps actually are.

## Contradictions to probe
The two directions of overconfidence: safety teams treating a passed eval as
proof of safety, and worriers treating an unmeasured capability as proof of
danger. Steelman both and record what evidence would settle each.

## Sources
Floor: at least 8 sources, at least 4 primary, at least 1 secondary. Primary: the
evaluators' and labs' own methodology documents and the papers owning each
elicitation figure. Secondary: reporting only for context a primary does not own.
Prefer the document that made the argument to commentary about it.

## Boundaries
No code. This is an argument lesson, not an incident report and not a metrics
tutorial. Do not relitigate sandbagging or open-weights fine-tuning; use them as
the reader's existing ground and stay on the elicitation-gap argument. One
argument, steelmanned, then tested.

## Production policy (balanced; none required)
writing-coach capable/low; researcher capable/high; writer capable/medium; editor
capable/high. "capable" served by the run's default subagent model (Opus-class);
record the actual writer model in nb-meta.

## Neighbors in this run
the-evidence/mamba, the-instruments/bertscore,
the-mechanics/speech-to-text-hallucination, when-ai-breaks/retinopathy-field-study.
No overlap.

## Habits from the recent record not to inherit
- The desk's pieces repeatedly close on the beat "the researchers built the setup
  themselves" and open by naming a thinker who "argues/predicted." Both recur
  across recent lessons; do not reach for either as this piece's frame or closer.
- Keep the arc (argument at full strength / shown versus speculative / present and
  the gap) but name sections for this argument, never with stock labels.
