# writer brief: when-ai-breaks/waymo-recall (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, paper voice, series prompt, citation standard.
- writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- researcher/01/evidence.md — the complete set of claims available to you; use the Numbers section exactly.
- commission.md (artifact root) — incident, teaching list, source floor, habits not to inherit.
- The initialized article: library/when-ai-breaks/waymo-recall.html (edit in place; keep chrome exact).
- .nb-context/ (template contract, furniture catalogs, runtime assets).

Output: writer/01/draft-handoff.md (plus the edited article).

Proof: ./nb check .nb-work/when-ai-breaks/waymo-recall/library/when-ai-breaks/waymo-recall.html --series when-ai-breaks --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout

This round's focus — the evidence corrects the commission's facts; follow the evidence, not the commission, where they differ:
- Dates: the towed-truck collisions were December 11, 2023 (Feb 13, 2024 is the recall FILING date). The pole collision was May 21, 2024 (June is the filing date). Use the incident dates for the events and the filing dates for the recalls, and keep them distinct.
- The two recalls are the same failure CLASS (rare tail configurations) but different failing MODULES: the towed truck was a prediction failure (the system incorrectly predicted the truck's future motion); the pole was a perception + mapping failure (perception assigned a low damage score; the map lacked a hard road edge). Do NOT imply the same prediction bug recurred at the pole. Used precisely, the two are a clean worked example of two stack stages failing separately.
- Precision: it was a "wooden utility pole" (the filing's words), not a telephone pole. The second recall's remedy was software AND map, not software-only. The 8 mph pole-collision speed is from press, not the filing — attribute it as reporting. Vehicle counts: recall 24E-013 = 444 vehicles; 24E-049 = 672 vehicles.
- Scope: the ODI investigation's later closure and the 2025 third recall are context from secondary reporting only — include only if needed and attribute as reporting, not as the filings. No one was injured in these two events; keep the register sober and do not reach for drama the record does not carry.

Teach perception vs prediction in plain words (pinned to the survey in the evidence) and distribution shift as why rare configurations break these modules; link ../ai-foundations/distribution-shift.html if it fits rather than re-teaching. Tell the incident in order with names, dates, places, counts, and recall numbers, then the failure class, then where the weakness lives now.

Habits not to inherit (from commission.md): find this piece's own opener and dek (avoid the one-line-harm opener and comma-and dek mold now familiar in the desk); vary heading construction; no colon-subtitle headline.
