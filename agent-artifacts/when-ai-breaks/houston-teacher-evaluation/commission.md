# Commission: when-ai-breaks/houston-teacher-evaluation

## Assignment

When AI Breaks teaches one real incident: a deployed system that failed publicly
or did harm and left a record. Tonight's incident is Houston's use of the SAS
EVAAS value-added model to score, and in some cases fire, public-school teachers,
and the federal lawsuit that stopped it: Houston Federation of Teachers v.
Houston Independent School District (S.D. Tex., 2017). Tell it in order: what the
system was built to do (rank teachers by their students' test-score growth), what
it actually did (produced scores teachers could not verify or contest, on which
employment decisions were made), who it affected, and what the court and the
district did afterward. Name the people, the vendor, the district, and the dates.
Then explain why that kind of system fails that way. Close with where the same
weakness lives today.

The reader should leave able to say what a value-added score is, why teachers
could not audit theirs, what specifically the court found wrong, and what general
failure of unaccountable algorithmic scoring the case teaches.

## The record, and the sequence

The authoritative record is the court's ruling (the opinion denying summary
judgment on the teachers' due-process claim), the district's EVAAS policy, and
SAS's own description of the model. Recover the real findings, not a paraphrase:
what the court said about teachers' inability to verify their scores, the role of
the model being a proprietary "black box" whose computations the district itself
could not reproduce, the reported error or volatility in scores, and how the case
ended (the settlement and the district dropping EVAAS for stakes). Get the exact
holdings and figures from the record.

## Why that kind of system fails that way

The teaching is the mechanism: a value-added model estimates a teacher's effect
by predicting each student's expected growth and crediting the teacher with the
gap, an estimate built on noisy year-to-year test data and confounded by
everything about a classroom the model cannot see. Draw out why such scores are
volatile, why a proprietary model no one can inspect cannot be meaningfully
appealed, and why using an unverifiable estimate as the basis for firing is the
due-process failure the court reached. Keep the court's findings as findings.

## Where the weakness lives today

Close on where the reader meets the same failure now: opaque proprietary scoring
in hiring, performance management, and benefits, where a person is ranked by a
model they cannot see or contest. Use a sourced present-day example, not a
gesture.

## Boundaries

- The subject is this incident. Other algorithmic-scoring incidents the course
  has covered (a school-grades algorithm, a recidivism score, a tenant score, a
  benefits-fraud system) are different cases; link one only if the reader needs a
  concept it taught, and do not retell it. Concepts like proxy labels and base
  rates, if the reader needs them, are linked, not re-taught.
- Where responsibility or the model's validity is contested (SAS defends EVAAS as
  statistically sound; the plaintiffs and the court focused on verifiability and
  due process, not on declaring the model invalid), present each side's strongest
  account and say what the ruling did and did not decide.
- Define "value-added model" in plain words at first use.

## Sources to start from

Primary: the federal court's opinion in Houston Federation of Teachers v. HISD
(2017); the district's EVAAS policy or board records; SAS's own EVAAS
documentation; and the settlement record. Secondary reporting and peer-reviewed
work on value-added model volatility (for example the American Statistical
Association's statement on VAMs, and Amrein-Beardsley's research) provide the
mechanism and context. Series policy requires at least eight sources, at least
four primary. Every date, figure, and holding must come from the record that owns
it; accusations need two independent confirmations by parties in a position to
know.

## This edition's neighbors

Four other lessons tonight: the-evidence/deep-double-descent,
the-instruments/attack-success-rate, the-mechanics/irrelevant-context,
what-could-go-wrong/liars-dividend. No overlap; write for a reader who has not
read them.

## Recent coverage in this series, and habits not to inherit

The last five When AI Breaks lessons were clearview-ai, bard-jwst-demo,
galactica, ai-writing-detectors, mcdonalds-ai-drivethru. Break, do not reproduce:
- The where-it-lives-today closer shape "The failure moved from a demo to a
  search bar" / "Fluent citations still ship in research assistants". Write that
  section in this incident's own terms.
- Headings built as a bare reversal ("Found unlawful, rarely enforced"). Vary
  construction.
- Deks that pack a comma triad; write one lean sentence with the actor, the harm,
  and the one identifying detail.

Furniture rotates through the figure, the note, the table, the timeline, and the
stat strip. The volatility of a score across years, or the chain from score to
firing, may want a table or timeline; use only what the argument spends.

## Production record

Production policy (when-ai-breaks): profile balanced; every stage required:
false; model "capable"; effort high for researcher and editor, medium for
writer, low for writing-coach. Harness: claude-code-routine. Model resolved to
claude-opus-4-8 for every role. No required directive traded down. Writer records
model claude-opus-4-8, harness claude-code-routine, date 2026-09-04.

## Tags

Suggested: value-added-models, teacher-evaluation, due-process, algorithmic-
accountability, evaas. The writer may adjust.
