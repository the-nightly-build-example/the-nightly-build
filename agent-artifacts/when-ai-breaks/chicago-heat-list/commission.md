# Commission: when-ai-breaks/chicago-heat-list

## Authorization

Scheduled run for 2026-08-14 (Fri). `nb duty` returned when-ai-breaks as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series.

## The incident

The Chicago Police Department's Strategic Subject List (the "heat list"), an
algorithm that scored individuals for their predicted involvement in gun violence,
as victim or offender. Developed by Miles Wernick at the Illinois Institute of
Technology under a National Institute of Justice grant, piloted around 2013 and
expanded across the department, it eventually scored several hundred thousand
people. RAND Corporation's evaluation of the pilot found that being on the list
did not reduce a person's chance of being shot and was mainly associated with
being arrested. The program was wound down and decommissioned around 2019-2020.

## Angle

Tell it in order: what the list was built to do, what it actually did, who it
affected, and what the department did afterward, with the names and dates. Then
teach why this kind of system fails this way, using ground the course has already
laid: predictions trained on arrest data learn policing patterns, not crime; a
risk score attached to no effective help becomes a reason for more police
contact; and a base rate this low makes most flags wrong. Close on where the same
weakness lives now, in the person-based risk scores and predictive-policing tools
still in use.

## Boundaries and neighbors

- Template: `lesson`. No open-item tags.
- Source policy: at least 8 sources, at least 4 primary and at least 1 secondary.
  Primary is the record: the RAND evaluation, the NIJ/CPD program documents, the
  Chicago Office of Inspector General review, and the released list data;
  secondary is the investigative reporting that held up.
- Distinct from when-ai-breaks/compas-recidivism (a court risk score) and from
  the automated-benefits failures robodebt, dutch-childcare-benefits, and
  optum-health-algorithm. This is predictive policing: an algorithm ranking
  individuals for police attention. Link the earlier lessons where they already
  taught proxy labels, base rates, and feedback loops, and build on them rather
  than re-teaching from scratch.
- Recent when-ai-breaks pieces used the base-rate frame (rite-aid-facial-
  recognition) and the proxy-label frame (optum-health-algorithm). This piece
  shares those mechanisms but has its own particulars, no effective intervention
  and a self-confirming feedback loop, so lead with those and link the earlier
  base-rate and proxy-label lessons instead of restating them.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model; deviations recorded per role.
- Workspace: `.nb-work/when-ai-breaks/chicago-heat-list`.
- Article: `library/when-ai-breaks/chicago-heat-list.html` under that workspace.
