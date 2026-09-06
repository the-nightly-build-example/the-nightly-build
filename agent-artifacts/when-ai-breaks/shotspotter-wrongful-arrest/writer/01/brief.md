# writer brief: when-ai-breaks/shotspotter-wrongful-arrest (01)

Inputs:
- .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/agent-artifacts/when-ai-breaks/shotspotter-wrongful-arrest/editorial-direction.md
- .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/agent-artifacts/when-ai-breaks/shotspotter-wrongful-arrest/commission.md
- .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/agent-artifacts/when-ai-breaks/shotspotter-wrongful-arrest/writing-coach/01/voice-guide.md
- .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/agent-artifacts/when-ai-breaks/shotspotter-wrongful-arrest/researcher/01/evidence.md
- Article to edit: .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/library/when-ai-breaks/shotspotter-wrongful-arrest.html
- Template context dir: .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/.nb-context/

Output:
- .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/agent-artifacts/when-ai-breaks/shotspotter-wrongful-arrest/writer/01/draft-handoff.md

Proof:
- ./nb stamp .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/library/when-ai-breaks/shotspotter-wrongful-arrest.html
- ./nb check .nb-work/when-ai-breaks/shotspotter-wrongful-arrest/library/when-ai-breaks/shotspotter-wrongful-arrest.html --series when-ai-breaks --library /home/user/library-checkout
  (iterate --no-check-links; final proof with links, to BLOCK: 0)

nb-meta: harness="Claude Code", model="claude-opus-4-8". Tags e.g. shotspotter, soundthinking, gunshot-detection, chicago, wrongful-detention, base-rates.

This round's focus: tell the Williams incident in order, teach why an acoustic alert is a weak base-rate-driven signal, and close on where a machine alert hardening into evidence still lives.

Accuracy cautions from the evidence record (respect exactly):
- Williams's legal status: detained about 11 months, case dismissed July 2021 for insufficient evidence, NEVER convicted. Do not call it a conviction or an "arrest" loosely; the record supports pretrial detention and dismissal.
- Attribute every figure to its owner: the Chicago OIG (50,176 alerts; the 9.1% and 2.1% figures; Jan 2020-May 2021 window) and the MacArthur Justice Center (89%/86%; >40,000 alerts; ~21 months) measure DOWNSTREAM OUTCOMES (whether police found a gun crime), not detection accuracy. The company's 97% "accuracy" is self-reported and counts an alert wrong only on a rare voluntary police complaint. State plainly that no independent, controlled test of whether the sensors distinguish gunfire from firecrackers/backfires exists in the record — that crux is unsettled.
- SoundThinking's March 2026 statement claims its own later analysis (that ShotSpotter cannot detect gunfire inside an enclosed vehicle) is what freed Williams. Present the company's framing fairly, in its own words, but do not let it stand as the last word; both its account and the "alert hardened into evidence" reading can be true. Include the alert-modification record (the firecracker relabel and ~one-mile relocation; the 2016 Rochester testimony) attributed to its source.
- Include Chicago's 2024 end of the contract with dates.
- Name company as ShotSpotter, renamed SoundThinking (2023); use the name that fits the period.

Teach the base-rate point plainly (many alerts, few gun crimes → an alert is a weak signal), the mechanism the incident needs, no general ML course.

Habits not to inherit (from commission): keep the concrete actor-named dek but avoid the "Company did X, and Y happened" clause rhythm and comma-and closer; avoid comma-triad and negative-parallelism deks; vary heading construction; nearest neighbors chicago-heat-list, facial-recognition-wrongful-arrest, compas-recidivism (all in the library — link one in Background if useful, do not re-argue them).
