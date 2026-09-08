# Commission: when-ai-breaks/waymo-recall

## The incident

Waymo's first software recall. In February 2024, two Waymo driverless vehicles in
Phoenix struck the same backwards-facing pickup truck being towed at an angle,
minutes apart. Waymo traced it to how its system predicted the towed truck's
future path, issued a software update, and filed its first recall with NHTSA
(covering 444 vehicles). A second recall followed in June 2024 after a Waymo
vehicle hit a wooden telephone pole in an alley (672 vehicles). No one was
injured in either, but both are on the record as safety recalls with NHTSA
filings. The lesson teaches one incident in order: the towed-truck collisions are
the spine; the pole recall is where the same class of weakness recurs.

## Why this incident now

Waymo is the driverless service held up as the one that works, the safety-first
counterexample to Cruise (`../when-ai-breaks/cruise-robotaxi.html`) and to the
fatal Uber test (`../when-ai-breaks/uber-self-driving-fatality.html`). That makes
its recalls the clearest available lesson in why even a careful,
heavily-validated perception-and-prediction system fails on road situations that
sit outside what it was built to expect, and why the correction arrived only
after the vehicles had already hit something.

## The angle

Tell it in order, then explain the failure class. What the system is built to do:
perceive the scene and predict where other road users will go, then plan around
them. What actually happened: a truck towed backwards and crab-angled did not
match the shapes and motions the system reliably handles, so its prediction of
the truck's path was wrong, twice, the same way. Why that kind of system fails
that way: perception-and-prediction models are trained on distributions of scenes
and behave unreliably on rare configurations (distribution shift), and a
self-certified recall is the mechanism by which a company both fixes such a fault
and admits it existed. Where the same weakness lives today: the pole collision is
a different rare object, same class of gap; and every deployed AV, Waymo included,
carries the residual of situations too rare to have trained on. Keep the register
sober: no injuries here, and the honest lesson is about the failure mode and the
recall process, not a body count.

## What to teach (short list, in order)

1. What happened, in order, with names, dates, places, and the exact vehicle
   counts and NHTSA recall numbers. The two February collisions with the towed
   truck; Waymo's account; the recall filing.
2. What a driverless system must do that failed here: perceive and, crucially,
   predict the path of another road user, then plan. Define perception vs
   prediction in plain words. The towed truck broke the prediction step.
3. Why prediction fails on rare configurations: a model learns from the
   distribution of scenes it was shown; a backwards-towed truck at an angle is
   far out on the tail. Link `../ai-foundations/distribution-shift.html` rather
   than re-teaching it if it fits; teach the missing piece on the spot otherwise.
4. The recall as mechanism, and where the weakness lives now: what a software
   safety recall is for an AV, the June pole recall as the same class of gap, and
   the honest generalization to every deployed AV including Waymo. Do not overclaim
   danger; state what the record supports.

## Template, bands, sources

- Template: lesson. Word band 1200-2200. Sections: why, orientation, 0-4 flex,
  takeaway, sources.
- Source floor (when-ai-breaks/lesson): at least 8 sources, at least 4 primary and
  at least 1 secondary. Primary: the record itself — the NHTSA Part 573 Safety
  Recall Reports for both recalls (get the recall numbers, dates, vehicle counts,
  and Waymo's stated cause), Waymo's own blog/safety posts describing the events
  and the fix, and any NHTSA ODI documents. Reporting that held up (e.g.,
  established outlets covering the recalls) is secondary context. Verify every
  number against the primary that owns it.

## Production policy (resolved)

Profile balanced. writing-coach low/capable, researcher high/capable, writer
medium/capable, editor high/capable. None required. Writer records actual harness
and model in nb-meta.

## Background links available (verify and link, do not re-teach)

`../when-ai-breaks/cruise-robotaxi.html`,
`../when-ai-breaks/uber-self-driving-fatality.html`,
`../when-ai-breaks/tesla-autopilot.html`,
`../ai-foundations/distribution-shift.html`. Use only those the reader needs.

## This run's neighbors (for coherence, not overlap)

Publishing tonight: the-evidence/alphazero, the-instruments/auroc,
the-mechanics/attribute-binding, what-could-go-wrong/encoded-reasoning. No
overlap; keep the shared voice.

## Habits not to inherit (voice and shape)

Recent when-ai-breaks pieces open on the harm in one line and lean on the
comma-and dek mold; the shape is familiar, so find this piece's own opener and
dek. Headings run to full-sentence claims; vary construction. No colon-subtitle
headline. Because no one was hurt, resist any reach for drama the record does not
carry; the teaching is the failure class and the recall, stated plainly.
