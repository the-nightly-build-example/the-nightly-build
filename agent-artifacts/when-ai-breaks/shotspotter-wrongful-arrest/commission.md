# Commission: when-ai-breaks/shotspotter-wrongful-arrest

## Authorized work

Scheduled run for 2026-09-06. `nb duty` returned `when-ai-breaks` in open mode.
Selected after reading the full published library: the desk has covered face
recognition, predictive policing (person-based heat list), and benefits-fraud
algorithms, but not acoustic gunshot detection, a distinct deployed system with a
clean, well-recorded incident. It teaches a different failure mode (a machine
alert becoming evidence) in a domain the course has not yet touched.

Incident: the ShotSpotter (now SoundThinking) gunshot-detection system and the
case of Michael Williams, held about eleven months in Cook County jail on a
prosecution that leaned on a ShotSpotter alert, until prosecutors withdrew the
case in 2021 for insufficient evidence. Template: lesson.

## The incident and the desk's method

When AI Breaks tells one incident in order, names people, companies, and dates,
explains why that kind of system fails that way, and closes on where the same
weakness lives now. Work from the record.

Tell it in order:
- What the system is: microphone sensors across a city that detect loud impulsive
  sounds and classify them as gunfire, with human "acoustic experts" reviewing
  and sometimes reclassifying/relocating alerts. Name the company (ShotSpotter/
  SoundThinking) and how police buy and use it.
- What happened to Michael Williams: the May 2020 shooting of Safarian Herring in
  Williams's car, the ShotSpotter evidence used, the ~11 months in jail, and the
  2021 dismissal. Name the people, the jurisdiction (Cook County / Chicago), the
  dates, and what the record shows about how the alert was used and about the
  human reclassification of alerts documented in this and related cases.
- The oversight record: the Chicago Office of Inspector General's 2021 report and
  the MacArthur Justice Center study on how rarely alerts led to evidence of a
  gun crime; and Chicago's later decision to end the contract (2024). Report the
  figures each source states.

Then why that kind of system fails that way: a detector tuned to flag possible
gunfire produces many alerts, most not gun crimes; base rates and the
human-review step mean an alert is a weak signal, and the failure is treating a
probabilistic alert as if it located a crime. Teach the base-rate point plainly.

Close on where the weakness lives now: acoustic and other alert systems that feed
police discretion, and the general pattern of a machine flag hardening into
evidence.

## Boundaries

- Work from the record: the AP investigation that held up, the Cook County court
  filings, the Chicago OIG report, the MacArthur Justice Center study, and
  ShotSpotter/SoundThinking's own statements (the company disputes critics'
  characterizations; present its position fairly from its own words). When the
  cause is disputed, give the strongest account of each side and say what
  evidence would settle it.
- Name people, companies, dates exactly. Get Williams's legal status precise: he
  was detained/held pretrial and the case was dismissed, not convicted; do not
  overstate.
- Teach only the mechanism the incident needs (detection + base rates + human
  review), not a general ML course.

## Sources policy

Series floor: 8 sources, at least 4 primary and 1 secondary. Primaries: the Cook
County court record for People v. Williams if reachable, the Chicago OIG 2021
report, the MacArthur Justice Center report, and ShotSpotter/SoundThinking's own
published statements/methodology. Secondary: the AP investigation (2021) and
other reporting that held up. Verify every figure (jail duration, alert counts,
percentages) against its owning source; the company contests several, so
attribute carefully.

## Model and effort

Harness: Claude Code (remote). Capable tier for every role. Effort per balanced
profile: writing-coach low, researcher high, writer medium, editor high. Writer
records harness "Claude Code" and its model in nb-meta.

## Habits not to inherit (recent when-ai-breaks record)

- Keep the concrete actor-named dek but do not copy the "Company did X, and Y
  happened" clause rhythm or the comma-and closing shape; avoid comma-triad and
  negative-parallelism molds.
- Vary heading construction; name headings for this incident, do not reproduce
  neighbors' phrasings.
- Nearest neighbors in theme: chicago-heat-list, facial-recognition-wrongful-
  arrest, compas-recidivism. Distinct incident and mechanism; make the structure
  this piece's own and do not re-argue theirs.

## Required contribution

The reader should finish able to recount the Williams case and the oversight
findings, explain why a gunshot-detection alert is a weak, base-rate-driven
signal that should not carry a prosecution, and see the general pattern of a
machine alert hardening into evidence in systems still in use.
