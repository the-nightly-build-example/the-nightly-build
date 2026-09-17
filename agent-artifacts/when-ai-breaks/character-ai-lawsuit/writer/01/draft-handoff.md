# Draft handoff: when-ai-breaks/character-ai-lawsuit (01)

## Original work
The article turns a scattered legal-and-safety record into a single teaching line
that separates what Garcia's complaint alleges from the one thing the court
actually held (that the app is a product and the claims could proceed, not that
it caused the death), and uses that alleged-versus-confirmed distinction to show
why an engagement-optimized companion fails a user in crisis and why the same
design is still shipping across the industry.

## Proof result
`nb check` (links included) against the branch library: **BLOCK: 0**, verdict
PUBLISHABLE.

One warning left intentionally:
- `W-SENTENCE-DENSITY` (40 words, 3 clause joins) on the sentence listing which
  claims survived the motion to dismiss ("Conway let most of the case go
  forward: ... unjust enrichment, and wrongful death."). It is a single
  enumeration of exactly which counts the court allowed to proceed, which the
  round's exactness requires stated precisely. Splitting it into multiple
  sentences would blur that one list; kept whole as a controlled sentence.

All other density warnings from earlier iterations were resolved by splitting.

## Care rules and the alleged/confirmed line
- No method or means of self-harm and no final messages appear; the first
  self-harm pop-up is named only as pointing to a suicide-prevention hotline.
- Headline and dek hold the line: the headline states only confirmed court
  actions ("let ... proceed," "treated its chatbot as a product"); the dek
  attributes the design/defect claim to "his mother's suit says." The body marks
  every complaint-sourced fact as alleged and states plainly that no court found
  the product caused the death and that the case settled with no admission of
  wrongdoing.
- Fixed corrections applied: De Freitas (not "Frietas"); death date February 28,
  2024 (not the order's "2025" typo).

## Open evidence / voice question
One open evidence item, already flagged in the researcher's "Unresolved access":
the settlement (source 8) rests on Reuters wire reporting, not on the
CourtListener stipulation of dismissal read firsthand. The article states the
settlement modestly (confidential terms, no admission of wrongdoing) and does not
lean further than that secondary supports. If the editor wants the settlement's
filing date/language confirmed from the primary docket entry, that document was
not opened for this round.
