# Draft handoff: when-ai-breaks/meta-ad-delivery-discrimination (writer 01)

## Original work

The article does what none of its four primary records do alone: it traces
one causal chain across them, study to charge to settlement to audit, to
isolate delivery-stage optimization as the mechanism (not advertiser
targeting) and then to show that the government-mandated fix Meta built in
response to that finding works only for the one ad category it was legally
required to cover, and that even there it works partly by showing the ad to
fewer people, a tradeoff the settlement's own compliance metric never counts.

## Proof result

`./nb stamp` then `./nb check .nb-work/when-ai-breaks/meta-ad-delivery-discrimination/library/when-ai-breaks/meta-ad-delivery-discrimination.html --series when-ai-breaks --library <scratchpad>/library`,
links included: **BLOCK: 0, WARN: 0, verdict: PUBLISHABLE**. Words: 2199
(band 1200-2200). Sources: 8 (6 primary, 2 secondary), all first-cited in
document order. `nb render-check` (with `CHROME_BIN` set to the locally
installed Chrome) passed: no overflow at 390px, styles attached, no page
errors. No warning was left intentionally; the initial `W-LENGTH-HIGH` and
several `W-SENTENCE-DENSITY` warnings from early drafts were resolved by
trimming and splitting, not suppressed.

One link fix during the final link-checked run: the evidence record's
primary HUD Charge of Discrimination URL
(`www.hud.gov/sites/dfiles/Main/documents/HUD_v_Facebook.pdf`) now 404s.
The record's own listed mirror, `archives.hud.gov/news/2019/HUD_v_Facebook.pdf`,
resolves (confirmed both by direct fetch and by the link-checked proof) and
is what source 2 cites now.

## Open questions

None blocking. Two decisions worth flagging for the editor:

- Per the brief, the 2019 civil-rights settlement's total dollar figure is
  never stated in the article (the evidence record could not reconcile the
  ACLU's ~$3M against the ~$5M figure in secondary reporting). The article
  describes what Facebook agreed to do, not what it paid, for that
  settlement.
- The DOJ's own complaint and consent-judgment text is still cited only
  through the Civil Rights Litigation Clearinghouse (secondary) and Meta's
  own whitepaper (primary, which quotes and links the DOJ compliance-metrics
  filing directly), per the brief's instruction, since justice.gov continued
  to return 401 on every path this session tried.
