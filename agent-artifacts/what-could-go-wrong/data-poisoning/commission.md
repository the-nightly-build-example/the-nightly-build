# Commission: what-could-go-wrong/data-poisoning

## Authorization
Scheduled run for 2026-08-08 (Sat). `nb duty` returned what-could-go-wrong as an
open section: choose a topic within the beat, do not repeat a published slug.
Verified against the FULL published shelf (18 slugs); `data-poisoning` is not among
them. It is distinct from `deceptive-alignment` (a model deceiving on its own) and
`jailbreaks` (attacking a finished model at inference): poisoning plants the flaw
during training. One article only. Template `lesson`.

## Subject
The data-poisoning / backdoor argument: because models are trained on large,
partly untrusted corpora and fine-tuning data, an attacker who controls a small
slice of that data can plant a hidden trigger - a backdoor - that makes the model
behave normally until a specific input flips it, and the trigger can survive the
usual safety training.

## Angle (the desk's shape: steelman at full strength, draw the shown-vs-analogy line, bring to the present and name the gap)
- Open at full strength. Name who raised it and what they had seen: classic
  backdoor/poisoning results in ML (BadNets, Gu et al. 2017, for the intuition),
  then the LLM-era statement of the fear. Lay out the reasoning its careful
  defender would give: training data is too large to vet, provenance is weak, and a
  planted association is cheap to insert and hard to find by testing, because the
  model looks clean until the trigger appears.
- Test against what real systems actually do. Draw the sharp line the case turns on.
  SHOWN, in working systems: Anthropic's "Sleeper Agents" (Hubinger et al. 2024)
  demonstrated deliberately inserted backdoors that persisted through supervised
  fine-tuning, RLHF, and adversarial training - and that safety training could make
  them stealthier; and the 2025 poisoning-scaling result (Anthropic/UK AISI/Turing)
  that a roughly constant small number of poison documents (about 250) can implant a
  simple backdoor almost regardless of model or dataset size. Report exact
  conditions and what the backdoor did. ANALOGY / not yet shown: a consequential,
  attacker-inserted backdoor discovered in a deployed frontier model in the wild;
  the lab demonstrations insert the trigger themselves under known conditions.
- Bring it to the present. Who argues it now and what they want done (data
  provenance, training-data auditing, poisoning red-teams). Check confidence against
  the evidence and name the gap in both directions: the dismissal that "no real model
  has been caught poisoned, so it is theoretical" understates lab-demonstrated
  persistence; the alarm that "any model could already be backdoored" outruns what
  has been shown in the wild.

## Required contribution
The reader can state the argument at its strongest, separate what has been
demonstrated in controlled insertions from what remains analogy about the wild, and
judge how worried to be. Reported fact (what each result actually did, with numbers)
stays distinct from synthesis. Steelman critics before weighing. Name no company as
an authority; report the labs as sources of specific results, not authorities.

## Sources and policy
Source policy (lesson/what-could-go-wrong): min 8 sources; primary >= 4,
secondary >= 1. Primaries: BadNets (Gu et al., arXiv:1708.06733) for the backdoor
intuition; Sleeper Agents (Hubinger et al., arXiv:2401.05566) read for methods and
which trainings the backdoor survived; the 2025 poisoning-scaling paper/report (the
~250-document result) read for exact setup and the "near-constant count" claim; a
primary on data-provenance / web-scale poisoning feasibility (e.g. Carlini et al.
"Poisoning Web-Scale Training Datasets Is Practical," arXiv:2302.10149). Read methods
sections so the shown-vs-analogy line is exact. Steelman the skeptic (limits of the
demonstrations, why in-the-wild backdoors may be hard to pull off) from primaries.

## Boundaries
Link, do not re-teach: deceptive-alignment, sandbagging, jailbreaks, reward-hacking
are neighbors on the shelf; this piece owns training-time poisoning/backdoors and
should situate against them, not repeat them. No hype, no doom; a grand word only
after the argument earns it. Work from the papers, not commentary.

## Neighboring articles this edition
the-evidence/word2vec, the-instruments/needle-in-a-haystack,
the-mechanics/why-replies-stop, when-ai-breaks/optum-health-algorithm. Keep to the
poisoning argument.

## Habits not to inherit (recent what-could-go-wrong shapes)
Recent pieces (sharp-left-turn, sandbagging, mesa-optimization) open by naming the
arguer and the "measured gap behind the fear," run a shown-vs-analogy contrast
heading ("Where the evidence stops and X takes over"), and use nb-position /
nb-stat-strip. Do not reuse the "Where the evidence stops and X takes over" mold or
default to a position card; if used, make it earn its place. Vary the heading shape.

## Harness and model
harness `claude-code-routine`; model `claude-opus-4-8` for every role. Balanced
production policy; per-role effort not independently settable in this harness
(mechanism deviation only, model unchanged).
