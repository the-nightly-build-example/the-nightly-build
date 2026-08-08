# Commission: when-ai-breaks/optum-health-algorithm

## Authorization
Scheduled run for 2026-08-08 (Sat). `nb duty` returned when-ai-breaks as an open
section: choose a topic within the beat, do not repeat a published slug. Verified
against the FULL published shelf (19 slugs); `optum-health-algorithm` is not among
them. It is distinct from the other bias/harm cases on the shelf (apple-card =
credit; compas-recidivism = criminal risk; amazon-hiring-tool = resumes;
nh-predict = discharge timing; epic-sepsis-model = clinical alerts;
dutch-childcare-benefits = welfare fraud): this incident's mechanism is a biased
LABEL (cost as a proxy for health need). One article only. Template `lesson`.

## Subject
The commercial health risk-prediction algorithm studied by Ziad Obermeyer, Brian
Powers, Christine Vogeli, and Sendhil Mullainathan in "Dissecting racial bias in an
algorithm used to manage the health of populations" (Science, Oct 25, 2019). A tool
of the kind sold by Optum and used across US health systems to flag patients for
extra care assigned Black patients lower risk scores than equally sick white
patients, because it predicted health-care COST rather than illness.

## Angle (the desk's shape: what happened in order, then why that kind of system fails that way, then where the weakness lives now)
- What happened, in order, with names and dates. The algorithm scored patients to
  select those for "high-risk care management." The researchers, with access to a
  large academic hospital's data (~50,000 patients in the primary analysis, drawn
  from a wider population the paper describes), found Black patients at a given risk
  score were substantially sicker than white patients at the same score. Report the
  paper's headline numbers exactly (e.g. the share of Black patients in the
  high-risk group and how it would change under an unbiased algorithm; the extra
  chronic conditions at equal score). Name the mechanism the vendor used: the label
  was predicted annual health-care cost. Because less money is spent on Black
  patients at equal sickness (access and other factors), cost understated their
  need. Note the aftermath: publication in Science, the New York State DFS/DoH
  inquiry, and the vendor's engagement with the researchers to reduce the bias.
- Why that kind of system fails that way. Teach the transferable lesson: a model
  learns the label it is given, and when a convenient proxy (cost) stands in for the
  target you actually care about (illness), the model faithfully reproduces every
  bias baked into the gap between proxy and target - "label bias" / proxy failure.
  This needs no malice and no protected attribute in the features; race was not an
  input. Ground it in the paper's own decomposition.
- Where the same weakness lives now. Proxy labels are everywhere in deployed scoring
  (engagement, cost, arrests, clicks). Name documented present-day analogues from
  the record and the fact that the ~200M-people scale figure the paper cites for
  such tools makes the proxy choice consequential.

## Required contribution
The reader can tell the incident accurately, explain why predicting cost produced
racial bias without race as a feature, and recognize proxy-label failure as a
general property of how such systems are built. Reported fact (the Science numbers,
the aftermath) stays distinct from the taught mechanism. Where a number is contested
or an estimate, say so.

## Sources and policy
Source policy (lesson/when-ai-breaks): min 8 sources; primary >= 4, secondary >= 1.
Primaries: the Obermeyer et al. Science paper (read the full text and the numbers,
including any published author summary / the Booth/Berkeley copy if Science is
gated); the authors' follow-up or the Science "Editor's Summary"; the New York
regulators' statements (DFS/DoH) if primary text is reachable; contemporaneous
primary vendor statement. Read the paper's methods for the exact denominators and
the cost-vs-illness decomposition. Secondary reporting only for context.

## Boundaries
Tell the record; keep the mechanism claim measured and sourced to the paper. Do not
conflate this with the other published bias cases - situate briefly and link rather
than re-tell them. No code. Do not moralize; teach the failure mode.

## Neighboring articles this edition
the-evidence/word2vec, the-instruments/needle-in-a-haystack,
the-mechanics/why-replies-stop, what-could-go-wrong/data-poisoning. This piece owns
proxy-label bias as a deployed-system failure.

## Habits not to inherit (recent when-ai-breaks shapes)
Recent pieces (apple-card, facebook-myanmar, gemini-image-generation) open on a
human moment, run a "How a model does X" mechanism heading, and close on "Where the
same weakness sits/lives today," using nb-figure and nb-note. Vary that closing-
heading mold and do not default to the figure+note pairing; a stat strip of the
before/after enrollment shares, or a small table, may serve. Name headings from this
incident's own steps.

## Harness and model
harness `claude-code-routine`; model `claude-opus-4-8` for every role. Balanced
production policy; per-role effort not independently settable in this harness
(mechanism deviation only, model unchanged).
