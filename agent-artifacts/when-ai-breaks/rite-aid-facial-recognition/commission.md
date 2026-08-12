# Commission: when-ai-breaks/rite-aid-facial-recognition

## Authorized work

Scheduled duty for 2026-08-12 returned `when-ai-breaks` as an open section: choose
one incident within the beat, do not repeat a published slug. This commission
selects Rite Aid's facial-recognition surveillance program and the Federal Trade
Commission's 2023 enforcement action. It is one article, on the lesson template,
delivered as one Article PR.

## The incident and why it

Between roughly 2012 and 2020, the drugstore chain Rite Aid ran facial-recognition
surveillance in hundreds of its stores, matching shoppers as they entered against
a database of people the company had flagged as suspected shoplifters or troublemakers.
In December 2023 the Federal Trade Commission charged that the system generated
false matches that led employees to follow, stop, search, accuse, and eject
customers who had done nothing, and that the harm fell disproportionately on
Black, Latino, Asian, and women shoppers. Rite Aid settled: a five-year ban on
using facial recognition for surveillance, plus deletion of the images and models
and new safeguards. This desk teaches the incident so the reader can see why this
kind of system fails this way and where the same weakness sits today.

The beat's job here: tell what happened in order (what the system was built to do,
what it actually did, who it affected, what the operator did afterward), with the
people, companies, and dates named; then explain why that kind of system fails
that way, teaching the missing pieces on the spot; then close on where the same
weakness lives now, in systems the reader meets.

## The angle

Two mechanisms explain the failure, and the lesson should teach both plainly with
real numbers.

- The base-rate problem. Among the very large number of ordinary shoppers who
  enter a store, actual matches to a watchlist are rare. When the thing you are
  looking for is rare, even an accurate-sounding match rate produces mostly false
  accusations, because the few true matches are swamped by false ones drawn from a
  huge stream of innocent faces. Work this through with a concrete illustration so
  the reader can feel why "the system is usually right" and "most of its alerts are
  wrong" are both true at once.
- The demographic error skew. Face-matching systems have measured, uneven error
  rates: government testing found higher false-match rates for some groups than
  others across a broad set of algorithms. Layer that on a base-rate problem and
  the false accusations concentrate on the groups the system misreads most.

Then teach the deployment failures the record alleges: low-quality watchlist
images, no reasonable testing of accuracy, thin oversight, and instructions that
had staff act on a match. Keep reported fact, allegation, and analysis distinct.
The FTC's account is an allegation resolved by a consent order, not a court's
finding of fact, and Rite Aid did not admit the claims and has said the program
was limited and discontinued. Present the strongest version of each side and say
what evidence would settle what is disputed (the actual match logs and measured
error rates, largely not public). Close on where the same base-rate-times-bias
weakness lives today: live facial recognition in retail, venues, and policing.

## Sources

Source floor for this series: at least 8 sources, at least 4 primary, at least 1
secondary. Primary here is the party that owns the claim: the FTC for its charges
and order, the government testers for their measurements, Rite Aid for its own
position.

Direct the researcher to read, at minimum:
- The FTC's complaint against Rite Aid (December 2023). Read the specific
  allegations: the years and store counts, the examples of wrongful stops
  (including any involving minors), the demographic-harm allegations, and the
  deployment failures charged.
- The FTC's decision and order and its press release. Read the exact terms: the
  five-year prohibition, deletion requirements, and mandated safeguards, and the
  legal posture (settlement without admission).
- The National Institute of Standards and Technology face-recognition demographic
  study (Grother, Ngan, Hanaoka, "Face Recognition Vendor Test Part 3:
  Demographic Effects," NISTIR 8280, 2019), primary for the measured differences
  in false-match rates across demographic groups.
- Rite Aid's own public statement responding to the settlement, primary for its
  position and any factual claims it makes (store counts, discontinuation date).
- The independent reporting that first surfaced the program (Reuters, Jeffrey
  Dastin, "Rite Aid deployed facial recognition systems in hundreds of U.S.
  stores," 2020), as a secondary source for the program's scale and history. A
  restatement of the FTC's own allegation is not independent confirmation of the
  underlying facts.

Every figure (years, store counts, error-rate differentials, the order's terms)
is checked against the primary that owns it. Accusations of harm need the record
of a party in a position to know; where the only source is the FTC's own
allegation, label it as an allegation. Record Rite Aid's contradictions in full.

## Course placement and neighbors

The library already holds `when-ai-breaks/facial-recognition-wrongful-arrest`
(facial recognition misidentifying someone into a police arrest) and
`when-ai-breaks/compas-recidivism` (a scored-risk tool and disparate error). This
lesson is a distinct incident with a distinct mechanism emphasis: base rates times
demographic error in a private mass-surveillance deployment, resolved by a
regulator. Link the wrongful-arrest lesson in Background rather than re-teaching
how face matching can misidentify a person; if an earlier lesson already teaches
false-positive-versus-false-negative reasoning, link it instead of rebuilding it.
Tonight's other new articles are in unrelated desks (grokking, mmmu,
image-generation, reward-tampering); no cross-collision to manage. Link only
already-published library pages, never tonight's siblings.

## Production policy

Profile `balanced`; no role directive is `required`. Recorded plan: writing-coach
low effort, researcher high effort, writer medium effort, editor high effort;
model class `capable`. The runtime maps `capable` to the session's capable model
and runs each role at the session's effort; no `required` directive exists to
trade down. Actual harness: `claude-code-routine`. Actual model recorded in
nb-meta: `Claude Opus 4.8`.

## nb-meta

Date 2026-08-12. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Tags are
the writer's to set as descriptive keywords (this open series configures no tag
fragments); three concise topical tags.

Recent habits to break travel with the writer and editor briefs.
