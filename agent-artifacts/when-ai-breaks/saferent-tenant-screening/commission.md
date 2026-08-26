# Commission: when-ai-breaks/saferent-tenant-screening

## The incident

Louis v. SafeRent Solutions. Mary Louis, a Black rental applicant who used a
federal housing voucher (Section 8), was denied an apartment in the Boston area
after SafeRent's tenant-screening algorithm gave her a low score, despite a
landlord reference and a guaranteed-payment voucher. She and other voucher holders,
with the Community Action Agency of Somerville and represented in part by the
National Consumer Law Center and Cohen Milstein, sued SafeRent Solutions in 2022
under the federal Fair Housing Act and Massachusetts law, alleging the score
discriminated against Black and Hispanic applicants and voucher holders. The case
settled in November 2024: SafeRent agreed to pay about $2.3 million and, for five
years, to stop using its score (or offering a score with an accept/decline
recommendation) for voucher-holding applicants in the covered region. When AI
Breaks teaches one deployed system that failed publicly or did harm and left a
record.

## Tell it in order

- What the system was built to do: SafeRent (formerly CoreLogic Rental Property
  Solutions) sells landlords a tenant-screening score that ranks applicants on
  predicted tenancy risk, folding in credit history, debts, and non-rental financial
  data. Landlords set a threshold and auto-decline below it.
- What it actually did: scored applicants in a way the plaintiffs' analysis said
  systematically disadvantaged Black and Hispanic applicants and, critically,
  penalized the very financial signals (credit/debt) that a housing voucher is
  designed to make irrelevant — the voucher guarantees a large share of rent, yet
  the score did not credit it.
- Who it affected: named plaintiffs (Mary Louis; Monica Douglas) and a class of
  voucher holders; establish the harm concretely (denied housing).
- What the operator did afterward: the litigation, the DOJ/HUD statement of
  interest on how disparate-impact liability applies to screening algorithms, and
  the settlement terms and date.

## Then explain why this kind of system fails this way

Teach the mechanism the record needs, on the spot:
- Proxy discrimination / disparate impact: a model trained on data shaped by past
  inequities can reproduce them through correlated proxies (credit, debt) without
  using race as an input. Where this was taught before, link rather than re-teach:
  `when-ai-breaks/optum-health-algorithm` (a score that used a cost proxy and rated
  sicker Black patients lower) and `when-ai-breaks/amazon-hiring-tool` (a screener
  that learned a protected-trait proxy) are the neighbors; reference the shared
  mechanism and keep this piece on tenant screening's specifics (the voucher blind
  spot, the accept/decline threshold, the opacity to the applicant).
- Why the voucher makes it sharp: the score down-weights exactly the risk a voucher
  removes, so the tool is worst precisely for the applicants public policy is trying
  to house.

## Close with where the same weakness lives today

Tenant-screening scores are ubiquitous and largely unregulated; the same
accept/decline-on-a-black-box-score pattern runs across housing (and the CFPB/FTC
attention it has drawn). Keep it concrete and sourced, not a general moral.

## What this article must not do

- Work from the record: the complaint, the DOJ/HUD statement of interest, the
  settlement agreement, and reporting that held up (name outlets and dates). Where
  the cause is characterized differently by the parties, present the strongest
  version of each and say what evidence would settle it (the algorithm's internals
  were not fully public; note what the settlement did and did not admit — SafeRent
  denied wrongdoing).
- Do not re-teach disparate impact from scratch if the neighbor lessons cover it;
  link and extend.
- Handle a real, living plaintiff soberly: names and facts from the record only, no
  dramatization.
- Vary the closers and openers. The last When AI Breaks piece (facebook-translation-
  arrest) opened by "taking the incident apart into its two separate failures" and
  used "It is tempting to file the whole episode under X"; its takeaway ran "The X
  was the ordinary part... That is the failure to watch for... The safeguard it
  needed cost almost nothing." Do not reuse those shapes. Avoid "By the end you will
  be able to..." and the phrase "doing the work."

## Sources and production

- Source policy (lesson/when-ai-breaks): at least 8 sources, at least 4 primary,
  at least 1 secondary. Primary = the court complaint, the DOJ/HUD statement of
  interest, the settlement agreement or the court/DOJ press release, and any
  SafeRent statement. Secondary = reporting that held up. Verify every figure
  ($2.3M, the five-year term, dates, the score range) against the document that
  owns it. Accusations need two independent confirmations by parties in a position
  to know; two retellings of one origin count as one.
- Production policy: profile "balanced", model tier "capable" (recorded actual:
  claude-opus-4-8). Effort guidance coach low / researcher high / writer medium /
  editor high; none `required`; effort not independently settable via the run's
  child interface, so roles run at session default reasoning; no deviation to report.

## Original-work target

Show that the screening score failed not by a bug but by design — it scored the
financial signals a housing voucher exists to neutralize — and use the settlement's
specific remedy (stop scoring voucher applicants) to make plain what the tool was
actually getting wrong, then locate the same pattern in the tenant-screening tools
still in use.
