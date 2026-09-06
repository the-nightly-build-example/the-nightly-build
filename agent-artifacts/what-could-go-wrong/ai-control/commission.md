# Commission: what-could-go-wrong/ai-control

## Authorized work

Scheduled run for 2026-09-06. `nb duty` returned `what-could-go-wrong` in open
mode. Selected after reading the full published library: the desk has covered the
threat arguments (deceptive-alignment, treacherous-turn, scheming) and several
safety agendas evaluated on their merits (scalable-oversight, cot-monitorability,
the-off-switch, eliciting-latent-knowledge, ai-boxing), but not AI control, the
agenda that assumes the model may be scheming and asks how to stay safe anyway.
It is a distinct, current argument with primary documents.

Argument: AI control (Redwood Research, Greenblatt et al. 2023, "AI Control:
Improving Safety Despite Intentional Subversion"). Template: lesson.

## The argument and the desk's method

What Could Go Wrong opens an argument at full strength, tests it against what real
systems show, and names where confidence outruns proof. Work from the original
documents. Name no company as an authority. Leave the reader to decide.

At full strength:
- The move that distinguishes control from alignment: instead of trying to make
  the model want the right thing (which we cannot yet verify), assume the model
  is a capable adversary that may deliberately subvert you, and design a
  deployment protocol so that even then you get useful work and catch or contain
  bad actions. Lay out the reasoning its careful defenders (Redwood) give: use a
  trusted weaker model plus limited human auditing to monitor and gate an
  untrusted stronger model; measure a protocol by a control evaluation, where a
  red team builds the untrusted model to subvert and you see whether the protocol
  still holds (safety) while getting work done (usefulness).
- Report the original experiment concretely: the APPS backdooring setting, the
  protocols compared (trusted monitoring, untrusted monitoring, trusted editing,
  defer-to-trusted), and the headline safety/usefulness numbers the paper
  reports.

Test against what real systems show, drawing the line:
- What has been demonstrated: control evaluations exist and work in a toy code-
  generation setting; follow-up work (Redwood/others, 2024-25) extends control
  protocols and studies whether models can subvert them. Report the concrete
  results and their exact setups.
- What is still projection: whether control scales to real deployments and to
  models much more capable than the trusted monitor and the human auditors is
  unproven; the agenda's own proponents state control fails once the untrusted
  model is sufficiently superhuman or the tasks are un-auditable. Say plainly
  where the confidence (in either direction) outruns the evidence.

Bring it to the present: who pursues control today and what they want done
(control evaluations as part of safety cases), checked against the most recent
evidence. Name the gaps honestly: the reassurance that "we can just catch it"
rests on the monitor and auditors staying competitive with the untrusted model.

## Boundaries

- Read Greenblatt et al. 2023 firsthand for the argument and numbers, and the
  follow-up control papers firsthand for the present. Not commentary.
- Distinguish from neighbors and link where useful: deceptive-alignment (the
  threat control assumes), cot-monitorability (a monitoring signal), scalable-
  oversight (a different agenda), ai-boxing (containment). Do not restate them.
- No hype, no doom. A grand word only after the argument earns it.

## Sources policy

Series floor: 8 sources, at least 4 primary and 1 secondary. Primaries:
Greenblatt et al. 2023 (arXiv 2312.06942) for the framework and APPS numbers; at
least two follow-up control primaries (e.g. Bhatt et al. "Ctrl-Z" / subversion
strategies; a control-evaluation or "control tax" paper; a safety-case paper
invoking control); and a primary stating control's limits (from the proponents
themselves). Record every safety/usefulness figure with its exact experimental
setup and denominator; a control number is meaningless without the red-team
setup that produced it.

## Model and effort

Harness: Claude Code (remote). Capable tier for every role. Effort per balanced
profile: writing-coach low, researcher high, writer medium, editor high. Writer
records harness "Claude Code" and its model in nb-meta.

## Habits not to inherit (recent what-could-go-wrong record)

- The desk's demonstrated-vs-projected framing is its substance; make the point,
  but do not copy the recurring dek phrasings ("None has yet", "feasible on paper
  and unshown", "so far only in simulation", "every X since 2023 has closed in
  months"). Find this piece's own words.
- Avoid comma-triad and negative-parallelism deks.
- Vary heading construction; do not reproduce the "full strength / the opposite
  mistake / what the studies can and cannot show" heading set neighbors used.

## Required contribution

The reader should finish able to state the control argument at its strongest
(safety from an untrusted model via protocols, measured by control evaluations),
name what the original experiment actually demonstrated (protocols holding in a
toy backdooring setting) and its numbers, and separate that from the unproven
projection that control scales to superhuman models and un-auditable tasks. They
should be able to judge both "we can just control it" and "control is useless."
