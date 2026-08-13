# Draft handoff: when-ai-breaks/tessa-eating-disorder-chatbot (writer 02)

Bounded second round to clear the sole round-01 blocker (`B-SOURCE-KIND`: fewer
than four primary sources). Round-01 prose, framing, sensitivity handling, and
the cause-dispute treatment stand unchanged; three new primaries from
`researcher/02/evidence.md` were worked into the prose where they genuinely
support a claim, and all citations were renumbered in first-citation order.

## Original-work sentence

The article fuses the two incompatible causal accounts (NEDA's "unauthorized
generative feature" and Cass's "it was the pre-written script") into one
scope-misuse mechanism that survives either resolution, showing the harm follows
from placing a prevention-validated tool in an acute-support role rather than
from any particular technical trigger, which no single source in the evidence
record does on its own. Still holds after this round: the new primaries deepen
the two poles of that fusion (the developers' own concession of "a technical
problem" that does not adjudicate, and the vendor's own broad framing of the
product) without shifting the spine.

## Changes this round (each new primary earns a claim, not a slot)

- **Fitzsimmons-Craft & Taylor, STAT op-ed (new primary, s1).** Now owns two
  first-party claims: the developers' stated purpose (Tessa built for prevention
  and to reach people "otherwise not likely to have access to other resources,"
  with fewer than one in five who develop an eating disorder ever getting care),
  in orientation; and their own "fair"/"related to a technical problem"
  concession, in the mechanism section. The concession is stated explicitly not
  to resolve the NEDA-vs-Cass cause dispute ("They did not say which operator's
  version of the cause was right").
- **Gullo et al. 2026, IJED (new primary, s5).** Now cited for the rule-based,
  prevention-scoped design point in orientation: the same developer group has
  since built more rule-based prevention chatbots for at-risk teenagers who do
  not yet have a disorder. Corroborates the round-01 rule-based claim from a
  second independent developer publication.
- **Cass / X2AI vendor product description (new primary, s7).** Now cited in the
  mechanism section for the vendor's own broad framing of the product (Tess as an
  always-available support chat "built by clinical psychologists," "similar to
  texting with a friend or coach"), sharpening the marketed-scope vs
  validated-scope gap. The vendor's advertised outcome figures are flagged as
  marketing, not validated results, and are not cited as fact or reproduced.
- **NEDA (Thompson) and Maxwell/Conason material stays secondary** via NPR (s6)
  and KFF (s4), unchanged in kind. No secondary was reclassified to game the
  floor.
- **Renumbering.** Sources renumbered in first-citation order: 1 STAT, 2 RCT,
  3 Chan JMIR, 4 KFF, 5 Gullo, 6 NPR, 7 Cass/X2AI, 8 NBC (Koko). All in-text
  `sup` citations and the source-list ids updated to match.

## Proof result

Command (run from `/home/user/the-nightly-build`), links included:
`./nb check .../library/when-ai-breaks/tessa-eating-disorder-chatbot.html --series when-ai-breaks --library /home/user/library-checkout`

Result: **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.** All eight source links
resolve, including the three added this round (STAT, the Gullo DOI
`10.1002/eat.70008`, and `x2ai.com/home`). `nb stamp`: words 2197,
reading_minutes 10, sources 8.

Final cited counts: **5 primary (s1 STAT, s2 RCT, s3 Chan, s5 Gullo, s7 Cass),
3 secondary (s4 KFF, s6 NPR, s8 NBC); 8 total.** Meets the commission floor
(minimum 8, at least 4 primary, at least 1 secondary) and clears
`B-SOURCE-KIND`.

## Warning intentionally left

None. The `W-LENGTH-HIGH` that appeared at first stamp (2242 words, band ceiling
2200) was cleared by tightening only this round's added sentences; no settled
round-01 prose was touched. Final length 2197 words is inside the band.

## Display-text pass

Re-run after edits. Headline, dek, and all subheads are unchanged from round 01
and still check out against the record; the dek in `nb-meta` and the rendered
dekline remain identical. No new display-text claims were introduced.

## Open items

- The single remaining first-party gap from the evidence record is unchanged and
  does not affect counts: NEDA's own dated Instagram statements (May 30 takedown;
  June 7 "separate decisions") and Maxwell's original post could not be opened
  first-party this round, so they remain attributed through NPR/KFF, which quote
  them directly. This is a researcher-side retrieval limitation, not a writer
  decision.
