# writer brief: the-mechanics/false-premise-questions (01)

Inputs:
- ../../editorial-direction.md — house standard, voice, series prompt, template identity
- ../../commission.md — subject, angle, required contribution, source floor, recent shapes to break
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../../../library/the-mechanics/false-premise-questions.html — the initialized article to edit in place
- ../../../../.nb-context/ — effective template contract and furniture catalogs
Output: ./draft-handoff.md
Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-mechanics/false-premise-questions/library/the-mechanics/false-premise-questions.html --series the-mechanics --repo /home/user/the-nightly-build

This round's focus, from the researcher's cautions in the record:
- Keep two steps distinct in the causal chain: *noticing* the presupposition and *verifying* the premise is actually false. CREPE and Kim 2021 place much of the residual difficulty in verification, not detection. Do not collapse them.
- The "premise-corrections are rare in the training distribution" step is supported indirectly (models hold the knowledge yet default to answering; forum questions are followed by answers), not by a corpus count. State it at exactly that strength.
- Do not close on "just train it to reject premises." The 2026 tradeoff result shows that pushing a model to reject false premises harder makes it wrongly reject true ones, degrading ordinary QA. That tension belongs in the open section.
- Use the generation-over-generation correction rates (e.g. the medical false-presupposition study's GPT-4o to GPT-5 climb, none exceeding roughly 43%) in the open section, attributed to the study that measured them.
- Concrete examples flagged for exact-wording confirmation before printing: "When did Marie Curie discover Uranium?" and "How many eyes does the sun have?" Confirm wording against the owning source or attribute it as reported.

The commission's "Recent shapes to break" applies: no "the fix doesn't work" penultimate section by reflex, and no "training presses X into its probabilities" dek echo.
