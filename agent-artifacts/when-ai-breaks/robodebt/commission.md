# Commission: when-ai-breaks/robodebt

## The incident
Robodebt, Australia's Online Compliance Intervention (2015-2020). The federal government automated
welfare-overpayment recovery by averaging a person's annual tax-office income evenly across fortnights and
treating the result as proof of a debt, then shifting the burden onto recipients to disprove it. It raised
hundreds of thousands of unlawful debts, was found unlawful, was settled in a class action, and was the
subject of a Royal Commission that reported in 2023.

## Why this incident, tonight
The desk has taught government and institutional algorithmic failures (Dutch childcare benefits, UK
A-levels, COMPAS, Optum, NH Predict). Robodebt adds a distinct mechanism the course has not named: a coarse
statistical average substituted for individual fact, coupled with a reversed burden of proof, at national
scale with no human check. Its record is exceptionally strong, which lets the lesson teach from primary
findings.

## Tell it in order (the desk's structure)
- What it was built to do: recover welfare overpayments automatically by matching Centrelink records against
  annual Australian Taxation Office income data.
- What it actually did: averaged annual income evenly across fortnightly reporting periods (income
  averaging), producing debts for people whose real fortnightly income varied, and issued those debts with
  the onus on the recipient to prove them wrong.
- Who it affected: hundreds of thousands of welfare recipients; name the scale and the documented human harm
  the Royal Commission and court records establish, carefully and without overreach.
- What the operator did afterward: the scheme was found unlawful, debts were repaid or zeroed, a class action
  settled, and a Royal Commission investigated and reported.

## Why this kind of system fails this way (teach the missing piece)
- An average is not an individual fact. Spreading an annual figure evenly across fortnights invents a
  fortnightly income the person may never have earned; the artifact, not the person's actual pay, generated
  the debt.
- Automating an accusation with a reversed burden of proof turns a statistical guess into a demand the
  citizen must refute, often without the records to do so.
- Removing the human check that had previously verified these calculations scaled the error instead of a
  correct process.
Close, per the series prompt, with where the same weakness lives today: automated eligibility, tax, and
fraud systems that treat a model or a data-match as proof and put the burden of disproof on the individual.

## Disputed points, handled fairly
Where accounts differ (for example, how much the legal advice about lawfulness was known and when, or
attribution of specific harms), present the strongest version of each and say what the record settles versus
what remains contested. Prefer the Royal Commission's findings, the Federal Court judgment, and the
Ombudsman's report over reporting for contested facts.

## Template and form
Lesson template, body first, both bookends last. Background may link when-ai-breaks/dutch-childcare-benefits
and when-ai-breaks/uk-a-level-algorithm; the reader who opens neither must still follow.

## Reader and what to teach
Declared reader: smart, widely read, no codebase time. Assume algebra and probability. Teach here, each once:
income averaging and why an average across periods is not a per-period fact; the reversed burden of proof and
why it matters when a system is wrong; the difference between an automated calculation and a verified one.

## Sources
Series policy: min 8 sources, primary >= 4, secondary >= 1. Primary the researcher must open: the Royal
Commission into the Robodebt Scheme Final Report (2023); the Federal Court judgment (the Amato case and/or
the class-action approval); the Commonwealth Ombudsman's report; and a government or ANAO document on the
scheme's operation or the settlement. Secondary: the reporting that held up (for example the investigative
journalism that exposed it) for context. Verify every figure (debts raised, people affected, dollar totals,
the settlement) against the primary that owns it.

## Production record
Harness: claude-code-routine. Model for every role: Claude Opus 4.8 ("capable" tier; no role carries a
`required` directive). Efforts follow policy: writing-coach low, researcher high, writer medium, editor high.
Recommended nb-meta tags: government, automation, welfare.

## Recent habits not to inherit
From the recent when-ai-breaks and house record, break these:
- The anaphora heading run ("The car that... / The car that...", tesla). Do not build parallel headings.
- The where-it-lives-today heading phrasing "The same gap, in the cars on the road now" (tesla) and "When the
  label is a proxy" (optum). The section is required content; name it in Robodebt's own nouns.
- The headline molds "recalled X for letting Y" (tesla) and the comma-and reveal (optum). Find Robodebt's own
  surprise.
- The takeaway restated-definition opener and the "Two things are true" opener. Resolve the opener.

## This round's focus
Keep the income-averaging artifact and the reversed burden of proof central; that is the transferable lesson.
Handle harm claims with care and cite the record. Get the debt totals, the number of people affected, and the
settlement figure exactly right against the primary sources, and keep contested attributions labeled.
