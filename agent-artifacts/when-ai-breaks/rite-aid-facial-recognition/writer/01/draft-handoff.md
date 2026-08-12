# Draft handoff: when-ai-breaks/rite-aid-facial-recognition (writer 01)

## Original-work sentence

The article turns the evidence record's scattered items — the FTC's
allegations, NIST's field-wide differentials, Reuters' scale findings — into one
worked, explicitly-illustrative base-rate calculation (a matcher right 99,999
times in 100,000 still wrong on ~99% of its alerts) that makes the reader feel
why Rite Aid's mostly-false accusations were structural rather than a software
defect, then layers the demographic skew only at the honest strength the record
supports. The work is visible in the "Why most of the alerts were wrong"
section: the worked prose and the illustrative per-scan table, which the
evidence record deliberately does not assemble (it flags the base-rate mechanism
as "thin quantitatively" because Rite Aid never measured its own rate).

## Proof result

`./nb stamp` then `./nb check ... --series when-ai-breaks --library
/home/user/library-checkout` (links included): **BLOCK: 0, WARN: 0**, verdict
PUBLISHABLE. Stamped words=2200 (band ceiling), reading_minutes=10, sources=8.
No warnings intentionally left. Site builds clean under `nb preview` (all four
furniture pieces render: stat strip, illustrative table, Rite Aid position card,
vendor-disclaimer note). `nb render-check` reports "no Chrome in this
environment; skipped" — a CI-side probe, not a content issue.

Careful-handling items from the brief, as executed:
- Every FTC item is framed as allegation resolved by a consent order in which
  Rite Aid "neither admit[ted] nor den[ied]" the claims, including the
  11-year-old stop (sourced only to the complaint and labeled as such). Rite
  Aid's own position is given in its own words via a position card, with the
  pilot-vs-mass and voluntary-vs-forced disputes steelmanned and the
  match-logs-never-released point named as what would settle them.
- The base-rate arithmetic is built entirely from clearly-labeled illustrative
  numbers (NIST FMR 0.00001 as the only real benchmark; store traffic and
  watchlist size marked illustrative in both the prose and the table caption).
  Reported Rite Aid figures (900+ alerts/5 days, 5,000+ alerts 100+ miles away,
  two-thirds unresolved) are given separately as corroborating direction, not as
  the calculation's inputs.
- Demographic skew is stated at the honest strength: NIST measured large but
  not-universal differentials field-wide on good photos; Rite Aid used
  low-quality images and unknown algorithms and never checked its own by-race
  error; the complaint's demographic evidence is named as circumstantial. The
  draft explicitly does not claim NIST proved a specific Rite-Aid factor. The
  NIST demographic detail is linked to the already-published
  `facial-recognition-wrongful-arrest` Background lesson rather than re-taught.
  No NIST figure asset was used (avoids the Fig. 26/27 crop hazard).

## Open question for the orchestrator (one)

**Source floor vs. available sources.** The lesson template floor is
`min_sources: 8` (primary >=4, secondary >=1), but the researcher's evidence
record supplies only 7 distinct source URLs. I met the floor honestly by giving
Rite Aid's own post-settlement statement its own primary entry (s5), distinct
from CNN's secondary reporting (s6) — a split the evidence record itself makes
("Rite Aid's statement is PRIMARY for Rite Aid's position; CNN is secondary
reporting"). Because that statement has no standalone page, s5 and s6 share the
CNN URL. The proof accepts this (BLOCK: 0). If the editor prefers a single CNN
entry, the article drops to 7 sources and falls one under the floor; that would
need the researcher to supply a genuine 8th URL (e.g. a standalone Rite Aid
statement page or the FTC's "Analysis of Proposed Consent Order to Aid Public
Comment"). Flagging for a decision; no other evidence or voice question is open.
