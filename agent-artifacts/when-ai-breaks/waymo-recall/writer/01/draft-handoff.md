# Draft handoff: when-ai-breaks/waymo-recall (01)

## Original work

The article turns Waymo's two separate NHTSA recall filings into one worked
lesson on the perceive-then-predict pipeline: it uses the towed truck (a
prediction failure) and the wooden utility pole (a perception-and-map failure)
as a matched pair that shows two different stages of the same stack breaking on
rare road configurations the training and the map never covered. The evidence
record notes that the two recalls fail different modules; the article is what
builds that distinction into a teaching sequence and pins it to the perception
vs prediction and distribution-shift concepts.

## Proof result

`./nb check ... --series when-ai-breaks --library <checkout>` with links:
**BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** `nb stamp` ran before the final
check (words=1695, reading_minutes=7, sources=8; 6 primary, 2 secondary, floor
met). All eight source links resolved. nb-meta dek is identical to the rendered
dekline; date 2026-09-08, harness claude-code, model claude-opus-4-8.

## Warnings intentionally left

None. The five W-SENTENCE-DENSITY warnings from the first pass were all cleared
by splitting the long sentences, and the two W-SELF-COUNT warnings cleared on
stamp.

## Notes for the editor (not warnings)

- Date discipline per the brief: incident dates and filing dates are kept
  distinct throughout (towed-truck collisions 12/11/2023 vs recall 24E-013 filed
  2/13/2024; pole collision 5/21/2024 vs recall 24E-049 filed 6/10/2024). The
  timeline in the orientation section makes the first gap visible on purpose.
- The two recalls are treated as different failing modules, not one recurring
  bug: towed truck = prediction; pole = perception + mapping (low damage score,
  no hard road edge). The pole remedy is described as software AND map, not
  software-only.
- The 8 mph pole speed and the Jaguar I-Pace model are attributed to reporting
  (TechCrunch), explicitly noting the filing does not give the speed.
- "wooden utility pole" uses the filing's term, not "telephone pole."
- The ODI investigation is used only as its opening resume supports (22
  incidents, 0 injuries at opening); the 2025 closure and the third recall were
  left out because no closing document was read firsthand.
- A few earned negative-contrast constructions were retained where they correct
  a misconception the piece names ("The pole was not a repeat of the towed-truck
  bug"; "not a body count"). The reflexive "not X but Y" opener in the Why
  bookend and the "X rather than Y" in the pole section were removed and
  rewritten positively.

## Open questions

None. The named inputs settled the piece.
