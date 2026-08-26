# Draft handoff: when-ai-breaks/saferent-tenant-screening (01)

## Original work

The article names, in one place the scattered filings never do, the single
design choice that turned the SafeRent Score into a denial: that it weighed the
credit records and non-tenancy debts a housing voucher exists to cover while
never counting the voucher itself, and it shows why that omission fell hardest
on the applicants least likely to miss rent. The move is visible in the
"What the SafeRent Score counted" section (the counted/not-counted table set
against the DOJ's "failing to consider... vouchers" framing) and is promoted as
the pull quote.

## Proof

`./nb check --series when-ai-breaks --library /home/user/library-checkout .nb-work/when-ai-breaks/saferent-tenant-screening/library/when-ai-breaks/saferent-tenant-screening.html`

Result: `BLOCK: 0`, `WARN: 0`, verdict PUBLISHABLE (links checked on). `nb stamp`
run before the final check: words 2190, reading 10 min, sources 8.

No warnings intentionally left standing.

Two W-warnings from an interim run were resolved rather than accepted:
- W-SOURCES-MIN (series floor is 8): added the National Consumer Law Center
  case page as source 5, cited for the state race-and-source-of-income claim it
  characterizes.
- W-CITE-ORDER: renumbered so sources run in first-citation order (the AP/Fortune
  position card now precedes the Clearinghouse settlement figures in the numbering).

## Evidence handling to flag for the editor

- Every claim about what the score *did* to Black and Hispanic applicants is
  written as a pleaded allegation that cleared a motion to dismiss (Judge Angel
  Kelley, D. Mass., July 26, 2023) and then settled with no admission of
  liability. The piece states plainly that the model internals are non-public
  and that no court tested the statistics. SafeRent's compliance position is
  given fairly, in Yazmin Lopez's own words, via a position card before the
  settlement is weighed.
- Voucher coverage uses the plaintiff-specific figures (Louis ~69%, Douglas ~57%);
  counsel's class-level "over 73%" is not attached to either individual and is
  not used.
- Settlement figure is the exact $2,275,000 total / up to $1,175,000 cash; the
  five-year injunctive term is stated as fact. The wire "$2.3M" rounding is not
  used.

## Open question

None blocking. One residual evidence limit, unchanged from the record: the exact
fee/service-award split inside the $2,275,000 was not confirmed from the fee
order itself (settlement PDFs were access-blocked for the researcher). The draft
does not assert any sub-split beyond "up to $1,175,000... cash to the class and
the rest to fees and administration," which the Clearinghouse and AP sources
support, so no claim in the article depends on the unverified split.
