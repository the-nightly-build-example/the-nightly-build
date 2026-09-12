# draft-handoff: the-mechanics/lost-in-the-middle (writer 01)

## Original-work statement

The article turns the evidence record's separate primaries into one backward
chain from the behavior to its candidate causes, adjudicating the mechanism
claims against each other so the reader sees why RoPE decay alone cannot be the
cause (Su's decay predicts recency, and Liu found the U across position schemes
including ALiBi) and why the effect size is model-dependent, and it renders Liu's
tabular GPT-3.5-Turbo and Claude-1.3 numbers as a single chart that puts the U
and its near-flat counterexample side by side.

## Proof result

`nb stamp` then `nb check ... --series the-mechanics --library <checkout>` with
links: **BLOCK: 0, WARN: 0** (PUBLISHABLE). words=2196 (within the 1200-2200
band), sources=9 (8 primary, 1 secondary), reading 10 min. No warnings left
standing.

Chart provenance committed: `lost-in-the-middle/chart-1.py` (+ rendered
`chart-1.png`), data from Liu et al. Appendix G Table 6. Chart image inspected;
GPT-3.5-Turbo traces the U, Claude-1.3 is nearly flat.

## Open evidence / voice questions

- **Persistence in current frontier models is unreplicated in the record.** No
  source reruns Liu's position-of-answer QA curve on a 2024-2025 model, so the
  draft hedges the persistence claim to what the proxies support (RULER effective
  vs claimed context, NoLiMa length falloff with GPT-4o 99.3%->69.7% at 32K, Levy
  length isolation) and states plainly that the specific U by position in a 2025
  model is unmeasured here. If a later round needs the specific U asserted in a
  named current model, that evidence must be commissioned. Owner: researcher /
  orchestrator (flagged as unresolved in the evidence record).
- **Hsieh et al. calibration gains not quoted.** Only the load-bearing claim from
  Hsieh (U-shaped, content-independent attention bias, shuffle-invariant) is used;
  the specific mitigation percentage gains were read from text, not re-derived, so
  the draft does not cite any of them. No open question, recorded so a reviewer
  does not expect a gain figure.
