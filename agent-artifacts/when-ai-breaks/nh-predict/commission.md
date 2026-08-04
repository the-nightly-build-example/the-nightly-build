# Commission: when-ai-breaks/nh-predict

## Authorized work
Scheduled duty for 2026-08-04 returned `when-ai-breaks` as an open section. This
commission fills it with one lesson on one incident. One article.

## The incident
UnitedHealth's use of the nH Predict algorithm (from its subsidiary NaviHealth)
to project how long Medicare Advantage patients need post-acute care — skilled
nursing and rehabilitation — and, per a November 2023 class action and a STAT
News investigation, to cut off coverage against treating physicians' judgment,
with a very high rate of denials reversed on appeal.

## Angle
Tell it in order, the desk's way: what the system was built to do, what it
actually did, who it affected (named, dated), what the operator did afterward.
Then explain why that kind of system fails that way, and close on where the same
weakness lives today. The mechanism to teach: a **length-of-stay predictor — a
population average with error bars — was converted into a per-patient coverage
cap**, and the ~90% appeal-reversal figure alleged in the complaint is the tell
that the conversion was invalid. Then generalize: a prediction used as a
decision, with automation bias and opacity turning a rough estimate into an
effectively unappealable rule.

## What the writer must establish (verify against primaries; guard attribution)
- What it was built to do: nH Predict, a NaviHealth tool, estimates expected
  recovery / length-of-stay for post-acute care by matching a patient to a
  database of "similar" patients and producing a target discharge date.
- What it did: UnitedHealth allegedly used those projections to deny or terminate
  coverage, with case managers reportedly pressured to keep patients within a
  narrow band of the tool's projected days (STAT News, Nov 2023). The complaint
  alleges roughly 90% of the algorithm-based denials that were appealed got
  reversed. **This is an allegation in active litigation — attribute it as such,
  not as established fact.**
- Who it affected: elderly Medicare Advantage patients; the named plaintiffs in
  Estate of Lokken et al. v. UnitedHealth Group (D. Minn., filed Nov 2023), both
  of whom died. Give dates and roles exactly.
- What the operator did: UnitedHealth's public response (that nH Predict is a
  guide, not a coverage-decision tool) and the litigation's status. The regulator
  side: the CMS Medicare Advantage guidance restricting algorithmic denial of
  individualized coverage, and the Senate Permanent Subcommittee on
  Investigations findings on post-acute prior-authorization denials.
- Why it fails that way: a model estimating a population average recovery is a
  category error when used as an individual entitlement cap (link
  distribution-shift reasoning); the number becomes a target and a shield
  (automation bias); opacity means only the few who appeal get relief, so a high
  reversal rate implies systematically wrong denials that mostly stood.
- Where it lives today: automated prior-authorization and claims denial across
  insurers (e.g., the Cigna PXDX batch-denial reporting), and any setting
  repurposing a population-level prediction as an individual decision rule.

## Boundaries
- Work from the record: the complaint, the investigative reporting, the CMS
  guidance, the Senate report. When the cause is disputed (UnitedHealth's "only a
  guide" versus the plaintiffs' "decisive in practice"), present the strongest
  version of each side and say what evidence would settle it (internal directives
  on adherence to the tool; the actual denial and appeal data).
- Keep reported fact, allegation, and the paper's synthesis strictly separate.
  This is a live suit and a named company; a mislabeled allegation is the costly
  error here.
- The reader has no clinical or insurance background; define Medicare Advantage,
  prior authorization, and post-acute care in plain words on first use.

## Sources plan
Series policy: min 8 sources, at least 4 primary and at least 1 secondary.
Target primaries: the class-action complaint (Estate of Lokken v. UnitedHealth)
for the specific allegations and the reversal figure; the STAT News investigation
(owns the internal-document reporting — classify with care: STAT is secondary,
the internal documents it quotes are the primary material); the Senate PSI report
on Medicare Advantage prior authorization; the relevant CMS guidance / final
rule; UnitedHealth's / Optum's public statement; a NaviHealth or CMS description
of what nH Predict is. At least one secondary for the present-day parallel (the
ProPublica Cigna PXDX reporting) and context. Researcher verifies every figure,
date, name, title, and the litigation status against the owning document, and
records exactly which claims are allegations.

## Neighboring articles this run (avoid overlap)
Tonight also publishes `the-evidence/alexnet`, `the-instruments/training-compute`,
`the-mechanics/retrieval`, `what-could-go-wrong/cyber-uplift`. The library holds
two other healthcare-AI failures (`epic-sepsis-model`, `ibm-watson-oncology`);
this incident's mechanism (a population predictor used as a coverage cap) is
distinct from theirs (a missed-detection alarm; unsafe recommendations from
synthetic training data). Keep the teaching on *this* mechanism and cite the
others only if a specific comparison earns it.

## Recent shapes to break
This desk's recent deks personify the system ("taught itself to penalize," "an
algorithm turned a passport into a fraud score"). The mechanism here invites the
same move; use it at most once and vary the rest. Avoid the comma-and-"and" dek
and heading molds. Coach supplies the do-not-reuse list from the recent library.

## Production record
- Profile: balanced. Model directive: `capable` for every stage (not required).
  Effort directives: writing-coach low, researcher high, writer medium, editor
  high.
- Actual harness: roles run as isolated subagents on model `claude-opus-4-8`.
  Per-stage effort inherited (not independently settable); recorded as a
  permitted deviation. Writer records the model string in `nb-meta`.
