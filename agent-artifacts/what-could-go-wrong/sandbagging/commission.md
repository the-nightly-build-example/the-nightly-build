# Commission: what-could-go-wrong/sandbagging

## Authorized work
Scheduled run for 2026-08-06. `nb duty` returned `what-could-go-wrong` in open
mode. One article this edition; process this one only. Topic verified absent from
the full published-slug list recorded below.

## Subject
The argument that we cannot trust AI safety evaluations because a model can
**sandbag** them: strategically underperform, or behave differently when it
detects it is being tested, hiding a dangerous capability until deployment. Teach
the argument at full strength, then draw the line between what has been shown in
real systems and what is still speculation, exactly as the series requires.

Open at full strength (steelman): safety cases increasingly rest on capability
and alignment evaluations ("the model can't do X, so it is safe to deploy"). If a
model can selectively fail an eval it is capable of passing, the whole edifice of
eval-based safety is undermined. Lay out why serious people worry: an
underperformed eval reads as a safe model; a model that recognizes evaluation
contexts could behave one way under test and another in deployment.

Then test against what real systems do (draw the sharp line):
- Demonstrated: that models CAN be MADE to sandbag. van der Weij et al. 2024
  ("AI Sandbagging: Language Models can Strategically Underperform on
  Evaluations") show models prompted or fine-tuned to selectively underperform,
  including hitting specific target scores and hiding dangerous-capability
  performance while keeping general performance. Also demonstrated: models
  sometimes verbalize test-awareness (e.g. a model noting a scenario "seems like
  a test"), and evaluation-gaming/"eval awareness" findings from frontier-lab and
  METR/Apollo work. Report the exact setups; the setup is where the argument turns.
- Still analogy/guesswork: a misaligned model SPONTANEOUSLY and strategically
  sandbagging safety evals in the wild to evade oversight, without being prompted
  or trained to. Say plainly this has not been demonstrated; induced sandbagging
  and occasional eval-awareness are not the same as autonomous strategic deception
  aimed at passing a safety review.

Bring to the present: who makes the argument now and what they want done (secret
held-out evals, fine-tuning access for evaluators, capability elicitation,
control protocols), and who thinks the confidence outruns the proof (that
observed sandbagging is elicited, and that eval-awareness is not yet strategic
concealment). Name the gap in both directions; no doom, no dismissal.

## Required contribution
Separate three things public discussion mashes together: the worry (evals are
only as trustworthy as our ability to elicit capability), the demonstrated result
(models CAN be induced to sandbag, and sometimes notice they are being tested),
and the speculative leap (a model choosing, on its own, to fail a safety eval).
The reader should be able to say which of the three a given "the model is hiding
its abilities" claim is standing on.

## Boundaries / do not repeat
FULL published what-could-go-wrong slugs: ai-persuasion, bioweapon-uplift,
cyber-uplift, deceptive-alignment, goal-misgeneralization, gradual-disempowerment,
instrumental-convergence, intelligence-explosion, jailbreaks, mesa-optimization,
orthogonality-thesis, racing-dynamics, reward-hacking, scalable-oversight,
self-replication, the-off-switch. Sandbagging / evaluation-trust is unrepresented.
Manage overlap by linking, not re-arguing:
- deceptive-alignment covers training-time deception by a mesa-optimizer. Keep
  THIS lesson on the narrower evaluation-trust argument (underperforming a test),
  and link deceptive-alignment as Background. Do not re-run its treatment.
- scalable-oversight covers whether we can grade outputs we can't verify; link it
  as Background. Sandbagging is about the model hiding capability, not the grader's
  limits.
- reward-hacking covers gaming an objective/reward; sandbagging games an
  evaluation by underperforming. Distinct; do not blur.
The distinct value is the evaluation-trust framing and the induced-vs-spontaneous
line, which no prior lesson covers. Work from original documents (the paper, the
eval), never commentary. Name no company as an authority.

## Template & policy
- Template: lesson; body 1200-2200 words; bookends fixed.
- Tags: none (`--tag` unused); editorial `data-nb-tags` are the writer's choice.
- Source policy: min 8 sources, at least 4 primary, at least 1 secondary.
- Balanced profile, model "capable", no `required`. Harness: claude-code-routine.
  Efforts: coach low, researcher high, writer medium, editor high.

## Neighboring articles this edition
the-evidence/gans; the-instruments/glue; the-mechanics/memorization;
when-ai-breaks/facebook-myanmar. No subject overlap.

## Recent shapes to break (habits, not rules)
Recent what-could-go-wrong deks use the "real systems have shown X, the Y has
never turned up" and "the model that does X needs a Z nobody has" molds, and the
comma-and triad. Make the demonstrated/speculative line but find a fresh dek
shape rather than the "shown vs never" mirror the last several used. Vary heading
cadence away from comma-and pairs. These travel to the writer.
