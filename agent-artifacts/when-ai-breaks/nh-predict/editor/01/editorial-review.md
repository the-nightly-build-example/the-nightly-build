# Editorial review: when-ai-breaks/nh-predict (editor/01)

## Skeptic

**Thesis.** nH Predict, a length-of-stay predictor that produces a population-average
target discharge date, was — the class action alleges — used by UnitedHealth as a
per-patient coverage cap; the complaint's ~90% appeal-reversal figure is the tell that
converting a group average into an individual entitlement was invalid; the same
prediction-as-decision failure recurs across automated prior authorization.

**Claims it stands on, and how each held.**

1. *What the tool computes* (undisputed): matches a patient to a 6-million-case
   database and returns an estimated length of stay and a target discharge date.
   Verified against evidence ¶32 and STAT (03/13/2023). The $2.5B/2020 Optum
   acquisition, the six-million figure, and the per-patient outputs all match. Holds
   as fact and is labeled as such ("No one disputes what the tool produces").

2. *The harm allegation* (contested): UnitedHealth used the target dates to end
   coverage against treating physicians, with a 2023 internal target to hold stays
   within 1% of the projected days and discipline (up to termination) for deviation.
   Verified against complaint ¶7 and STAT (11/14/2023). The article welds it to its
   owner every time ("the complaint and STAT News reporting say"). Holds as
   allegation, correctly labeled.

3. *The hinge statistic* (contested): >90% of appealed denials reversed on internal
   appeal or before an ALJ. This is the round's pass/fail. Verified against ¶38
   ("upon information and belief"). The article carries it as an allegation, states
   the no-denominator / no-outside-source caveat in the same passage, and spells out
   the inference rather than asserting it — exactly the licensed single-statistic
   move. The writer also declined to use the stronger ¶1 "90% error rate"
   characterization; good instinct. I pressure-tested the writer's gloss "counting
   only the patients who appealed": ¶38 says denials "reversed through an internal
   appeal process or ALJ," which by mechanism means appealed denials, so the gloss is
   the charitable and more conservative reading, not an overreach. Holds.

4. *The 0.2% appeal rate*: carried once, immediately flagged that the complaint's own
   footnote traces it "to a study of a different insurance market" (the ACA
   Marketplace / Medicare Advantage denominator mismatch from ¶2 fn.1), with "lean on
   it lightly." The caveat the brief required is present. Holds.

5. *The regulator's position*: the CMS FAQ quote is verbatim against the evidence
   (Q2), attributed as "the regulator's stated position and not a ruling against
   UnitedHealth," and correctly dated February 2024 (after the conduct). This is the
   cleanest external, non-litigant confirmation of the category-error thesis, and the
   article treats it as position, not verdict. Holds.

6. *The Senate denial-rate data*: 10.9% → 16.3% → 22.7% (2020–2022) matches the PSI
   report exactly; framed as independent of the litigants; and the causation hedge is
   quoted verbatim ("linked in media reports," "not a proven cause"). Holds.

7. *Causation*: kept throughout as the plaintiffs' disputed claim and explicitly
   unresolved ("No court has yet ruled on whether nH Predict drove the denials");
   the Feb 13 2025 ruling breakdown is softly attributed to the LegalHIE secondary
   with the note that the opinion PDF could not be retrieved directly. Holds.

**Tried to break the premise.** The premise most worth keeping — that a population
average was wired to an individual cap — is the one UnitedHealth disputes. The
article does not assert it as adjudicated; it presents the plaintiffs' "decisive in
practice" case (1% target + discipline + policy language promising clinician
decisions) against the company's strongest "only a guide" form (a later appeal on a
fuller record can reverse without the first denial being wrong), and names the two
discovery items that would settle it. The premise survives *as a live dispute*, which
is the only form the record supports. No sentence in the evidence retires it; none
proves it either. Correctly handled.

**Display-text descriptors, checked one by one.**
- Headline "nH Predict sets one patient's discharge date from six million others":
  states only the tool's computation (it does output a target discharge date), and
  "from six million others" encodes the category error. It does not assert the
  disputed causal claim (that the date ended coverage) — that lives, attributed, in
  the dek. Cleared as litigation-safe.
- Dek: attributes the harm claim to "A class action against UnitedHealth says …";
  one lean sentence with a stance; not a comma-and chain. Compliant. (Note: the dek's
  "estimate became the deadline that ended nursing coverage" carries a second
  system-as-actor cadence after the headline's "sets," but it is inside the
  attributed allegation, not the paper's own voice; within "at most once" for the
  paper's personification, so not a required change. The handoff's claim that the
  license "was spent nowhere" is inaccurate — the headline spends it — but the result
  is compliant.)
- Subhead "How an average became a cap": stated the disputed usage as accomplished
  fact. Softened to present-tense "becomes" (see Edits) so it teaches the general
  mechanism rather than asserting the case outcome.
- Other subheads ("What nH Predict was built to compute," "The days two patients did
  not get," "The dispute discovery would settle," "The same move at Cigna") assert no
  allegation as adjudicated fact and reconstruct the argument in order. None uses the
  banned comma-and heading mold or the flu-trends disputed-cause shape.
- Named-party facts (Lokken: 91, May 2022 fracture, ~19 covered days, appeal
  rejected, $12–14k/mo, died 07/17/2023; Tetzloff: 74, Oct 2022 stroke, 100-day
  referral, denied at 20, insurer's own physician agreed, denied again at 40, >$70k,
  died 10/11/2023) all match the complaint locators exactly.

**data-nb-kind audit.** s1/s3 STAT = secondary (correct; reports from outside).
s2 complaint = primary (owns its allegations, not their truth — correct). s4 CMS =
primary (correct). s6 Senate PSI = primary (correct). s7 LegalHIE, s8 Georgetown,
s9 ProPublica = secondary (correct). s5 CBS = primary-for-the-company's-position:
defensible — it carries naviHealth's verbatim statement, which the company owns — and
the evidence record makes that call deliberately. It is load-bearing (it is the 4th
primary; the series floor is 4), so I confirmed the kind is right rather than a padded
count. The steelman inferences that follow s5 in the position card ("On this
account …") are the paper's synthesis, signposted as such, not attributed to the
company; the citation correctly supports only the company's actual words.

**Citations opened as printed.** All nine hrefs resolve: complaint PDF (s2, 46-pp
Nov-2023 complaint), CMS FAQ PDF (s4), Senate PSI PDF (s6 — exceeds the fetch size
cap, i.e. it downloads, so it resolves), CBS (s5, naviHealth quote present),
ProPublica (s9, figures match), both STAT pieces (s1/s3), Georgetown tracker (s8,
case no. / 09-14-2026 class-cert date confirmed), and the LegalHIE secondary (s7,
survived/dismissed breakdown confirmed). The Feb-2025 opinion PDF is *not* cited — it
was the discarded 403 source — and the secondary that stands in its place resolves, so
the known gate is handled, not a dead-link failure.

## Cut

Four surgical cuts/fixes, no new prose past a clause:

- Removed the lecturing imperative "Set the doctor's number beside the plan's," which
  both violates the voice guide's *silent*-juxtaposition bar (no connective bridging
  the two halves) and echoes the coach's own instruction language. The three-sentence
  juxtaposition that remains (100 days ordered / insurer's own physician agreed /
  coverage ended at 40) is the licensed move, cleaner.
- Removed the section's closing locator "That gap is what this case is about," an
  editorializing frame that supplies the reaction the juxtaposition already carries;
  the section now ends on the punch, "Coverage ended at 40."
- Removed "Here the complaint puts down its most striking number," a signpost plus
  self-grading adjective ("most striking"), and repaired the following pronoun ("It
  alleges" → "The complaint alleges"). The statistic now lands at the pivot without
  being announced.
- Removed "Give that position its strongest form," a leaked steelman instruction from
  the brief narrating the writer's task; the position card does the steelmanning.

**Worst tell.** The leaked directive "Give that position its strongest form" — a
brief instruction surfacing as body prose. The self-grading "most striking number"
and the lecturing "Set … beside" openers are the same family. All removed.

**Consistency fix.** The cuts dropped reading time from 10 to 9 minutes; `nb stamp`
updated nb-meta, so I aligned the visible byline ("10 min read" → "9 min read") and
re-stamped.

**Furniture, earns-its-place.** The CMS quotation note earns it — a regulator's
verbatim position, the cleanest non-litigant confirmation of the thesis, set apart for
deliberate emphasis and not duplicated by the body. The naviHealth/UnitedHealth
position card earns it — the litigation balance requires the company's strongest form
given prominence. The three-row denial-rate table earns it as the independent numeric
counterweight to the contested 90%: honest (axes/years labeled, source cited, "as its
review was automated" is temporal not causal), and complementary to the prose's
"roughly doubled" rather than merely restating it. No block reads as furniture-for-its-
own-sake.

**Patterns.** No repeated heading shape; the "where it lives today" close names the
specific present-day system (automated prior authorization; Cigna PXDX) rather than
the worn "same weakness today." The do-not-reuse list is respected.

## Reader

What the piece gives beyond its sources: a transferable model none of the sources
hands over on its own — a population-average length-of-stay estimate converted into a
per-patient coverage cap, with the ~90% reversal figure's inference made explicit (a
high reversal rate among the few who appeal implies a much larger body of wrong
denials that were never challenged and stood), set against three separately labeled
registers (complaint allegation, CMS regulator position, Senate denial-rate data),
the company position steelmanned, and the mechanism generalized to automated prior
authorization. The draft-handoff's original-work sentence claims exactly this, and the
article delivers it; both answers survive, so the piece teaches rather than restates.
The prose sits closer to the voice-guide exemplars than to a median AI summary: it
welds each claim to its owner once and lets the verb carry the epistemic weight, shows
the mechanism through a visible gap (100 days vs 40) instead of naming it, and holds
editorial distance without smearing "allegedly" across every clause — the median
summary's move, which this piece avoids. Reread as the largest claim, the headline
commits to what the tool computes and encodes the category error without asserting the
disputed causation.

## Edits

- Cut "Set the doctor's number beside the plan's." from the two-patient juxtaposition.
- Cut "That gap is what this case is about." from the end of that section.
- Changed subhead "How an average became a cap" to "How an average becomes a cap."
- Cut "Here the complaint puts down its most striking number." and changed "It
  alleges" to "The complaint alleges."
- Cut "Give that position its strongest form." from the dispute section.
- Changed the visible byline "10 min read" to "9 min read" to match the re-stamped
  nb-meta.
- Ran `nb stamp` after the cuts (words 2170, reading 9, sources 9).

## Required work

None. No publication-blocking work remains for researcher, writer, or orchestrator.
Attribution discipline holds at every load-bearing claim and every display-text
descriptor; all figures reconcile with the owning primaries; every href resolves as
printed; the furniture earns its place.

## Decision

Approve, after direct cuts. Attribution is clean throughout, the display text carries
no allegation as adjudicated fact, and every citation resolves. Because I edited and
stamped the article, the orchestrator should run `nb stamp` + `nb check` (links
included) once more before delivery to confirm BLOCK: 0.
