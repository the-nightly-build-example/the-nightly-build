# Commission: when-ai-breaks/tesla-autopilot

## Authorized work

Scheduled run for 2026-08-09. `nb duty` returned `when-ai-breaks` in open mode,
reason: "open section — choose a topic within the beat; do not repeat a
published slug." One article.

## The incident

Tesla Autopilot's fatal crashes, told through the two with the fullest public
record: Joshua Brown (Williston, Florida, 7 May 2016) and Walter Huang (Mountain
View, California, 23 March 2018). Both were investigated end-to-end by the
National Transportation Safety Board, giving the desk exactly what it wants: a
deployed system, a public failure that did harm, and a documentary record
(NTSB reports, NHTSA investigations, the 2023 recall). The failure mode is
distinct from the two autonomous-vehicle incidents this desk has covered, and the
weakness it teaches still lives in every car with lane-centering today.

## What the lesson teaches (the desk's shape: what happened, why it fails that
## way, where it lives now)

1. **What the system was built to do, and what it did.** Autopilot is a Level 2
   driver-assistance system — adaptive cruise plus lane-centering (Autosteer) —
   that requires the human to supervise and be ready to take over at any moment.
   Teach the SAE levels only as far as needed to place Autopilot at Level 2 and
   say what that means: the car steers and brakes in its lane, and the driver is
   still the driver. Then the two crashes, in order, with names and dates: in
   2016 a Model S on Autopilot drove under a crossing tractor-trailer it never
   braked for; in 2018 a Model X on Autopilot steered into a highway barrier. Say
   who was affected and what the operator (Tesla) and regulators did afterward.

2. **Why this kind of system fails this way.** Two joined causes, taught on the
   spot: automation complacency (when a system handles the driving almost all the
   time, the supervising human stops supervising — the exact vigilance the design
   depends on is the thing it erodes) and the operational design domain (a Level 2
   system operates in conditions it cannot itself reliably bound and does not
   refuse to enter, so it will confidently steer in a situation it cannot handle).
   Layer in the naming gap: a system marketed as "Autopilot," and later "Full
   Self-Driving," invites trust its Level-2 reality does not earn. Draw the sharp
   line the desk asks for where cause is disputed: Tesla's account (the drivers
   misused a system they were warned to supervise) against NTSB's (the system's
   design predictably produced that misuse, its driver-monitoring was ineffective,
   and its domain was unbounded), and say what evidence settles it.

3. **Where the same weakness lives today.** Automation complacency and unbounded
   ODD are not Tesla-specific; they are properties of every consumer Level-2 ADAS
   (lane-centering plus adaptive cruise) the reader can buy now, and of Tesla's
   ongoing "FSD (Supervised)." Close on that, grounded in the regulatory record
   (NHTSA's Autopilot investigation and the December 2023 recall), not on a moral.

## Boundaries

- `when-ai-breaks/uber-self-driving-fatality` (a Level-4 test vehicle whose
  perception failed and whose emergency braking was disabled, with an inattentive
  safety operator) and `when-ai-breaks/cruise-robotaxi` (a driverless robotaxi
  that dragged a pedestrian and whose operator misled regulators) are covered.
  This lesson is a *consumer Level-2* system with a supervising driver, and the
  failure is the supervision loop itself. Link both; do not restage them. The
  contrast (who was supposed to be watching) is the cleanest way to place this one.
- Teach SAE levels only to the depth the argument needs; do not turn the lesson
  into a taxonomy.
- Work from the record — NTSB reports, NHTSA investigations and the recall, Tesla's
  own statements — not from secondary retellings. Numbers and findings to the
  owning primary.

## Original contribution

Show that Autopilot's fatal failures were not the system failing to work but the
system working as a Level-2 aid while being used as if it were more — and that the
design (naming, unbounded domain, weak driver-monitoring) is what turned an
ordinary human tendency, automation complacency, into a fatal one. The reader
should finish able to look at any "hands-free"/"self-driving" feature and ask the
two questions that decide its safety: what conditions can it not handle, and what
keeps the human watching for them.

## Source policy (from `nb source-policy`)

Series and template agree: minimum 8 sources, primary ≥ 4, secondary ≥ 1.
Primaries: NTSB's Brown report (HAR-17/02) and Huang report (HAR-20/01); NHTSA's
2016-2017 Autopilot investigation (ODI PE16-007) closing report; NHTSA's later
investigation and the December 2023 recall (Part 573 / closing report); Tesla's
own public statement(s); SAE J3016 for the levels. Coverage that held up is
secondary context. Where cause is disputed, the primary that owns the finding
governs; an accusation needs two independent confirmations.

## Production policy (from `nb production-policy`, profile: balanced)

- writing-coach: capable (Sonnet), low effort
- researcher: capable (Opus), high effort
- writer: capable (Opus), medium effort
- editor: capable (Opus), high effort

None `required`; no deviation to record.

## This edition's neighbors

- The other four lessons tonight (`the-evidence/gpt-3`, `the-instruments/mmlu`,
  `the-mechanics/word-order`, `what-could-go-wrong/situational-awareness`) do not
  overlap. This is the only incident lesson; keep it reported and concrete, no
  benchmark scores or risk-theory framing.

## Recent habits not to inherit

- This desk's recent openers open on a scene-setting generalization ("Hospitals,
  insurers, and clinics rank patients by a computed risk score…") and close the
  Why-this-matters card on "By the end of this lesson you will be able to say
  exactly how…". Write the promise in this incident's own terms and off that mold.
- The last two incident lessons (optum, apple-card) both resolve on a "the tool
  was not broken; it did exactly what it was built to do" turn. This incident has
  a genuinely different shape — a system used outside what it was built for — so do
  not borrow the "working as designed" frame or the takeaway line
  "The tool was not broken." Land the takeaway on the two questions the reader
  should carry, in fresh words, not the recurring "So when you meet X, the first
  question is not A, it is B" mold.
- Avoid the second-person "Now you know which one you are looking at" closer.
- "In plain language" note recurs across the shelf; label any note for its move.
- A timeline of events is natural here; if used, keep the furniture earning its
  place (the desk uses nb-timeline rarely — check it is the right primitive, not a
  default).

## Prior coverage to link, not re-teach

- `when-ai-breaks/uber-self-driving-fatality` — the Level-4 test-vehicle fatality.
- `when-ai-breaks/cruise-robotaxi` — the driverless-robotaxi failure and cover-up.
- If a claim needs distribution-shift or automation-bias framing already taught
  elsewhere in the desk, link rather than re-teach.
