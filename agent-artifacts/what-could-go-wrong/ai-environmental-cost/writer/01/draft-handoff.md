# draft-handoff: what-could-go-wrong/ai-environmental-cost (writer/01)

## Original-work sentence

The article splits the per-unit question (what one query or one training run
costs) from the aggregate question (what the whole build-out adds to grids and
water systems), and shows from the primaries that every viral figure answers the
first badly while the real, measured risk lives in the second, which has a
counted 2024 base and a wide projected band. That split is made visible in the
`measured-aggregate` table, which puts the corrected per-unit estimates (0.3 Wh,
284 to 3.2 t, 552 t, 25/50.5 t) beside the aggregate (415 / 945 TWh) with each
one's accounting boundary and base year.

## Proof status

- `nb stamp`: words 1955, reading 8 min, sources 8.
- `nb check ... --no-check-links`: BLOCK 0, WARN 0.
- `nb check ...` (links included): BLOCK 0, WARN 0.

No warnings left standing. Seven initial W-SENTENCE-DENSITY notes were cleared by
splitting the long sentences (they were dense, not slop); none required keeping.

## How the required moves were handled

- "Five cars" is Strubell's neural-architecture-search row (626,155 lbs =
  284 tCO2e), stated as a search and set against the 126,000-lb car-lifetime row,
  not against training a Transformer (192 lbs); Patterson's 88-fold correction
  (to ~3.2 t, proxy-task + efficient datacentres, once per problem class) is in
  the same section.
- The viral ~3 Wh/query is traced to de Vries (2023) via the Feb-2023 A100 /
  2,000-output-token assumption, and revised ~10x down to ~0.3 Wh by Epoch AI,
  with the three reasons named. The metric itself is linked to
  the-instruments/energy-per-query at first use and not re-taught.
- Per-query water is treated as an acknowledged disclosure gap; no per-query
  water number is asserted.
- de Vries's projection figures (85-134 TWh/yr by 2027; Google-AI ~ Ireland) are
  attributed as reported from secondary coverage, with the bot-gate stated in the
  prose.
- IEA measured base (415 TWh, 2024) and the four-case projection bands
  (670-1,260 at 2030; 700-1,720 by 2035) are used; the earlier-edition 460 TWh
  (crypto-inclusive) is used only to make the boundary point.
- Both sides are given fairly before the gap is named; no company is named as an
  authority (Patterson et al. cited as the paper, not "Google says"). The worry
  is left to the reader.

## Open questions

None blocking. Note for the record: the commission asked for water figures, and
the evidence record confirms no primary owns a per-query or per-training water
number (the ~500 mL figure traces to Li et al., unverified). The piece therefore
carries water as a genuine blank rather than a corrected number, which is the
honest reading of the evidence. If the desk later wants a water figure stated, it
needs new evidence from the orchestrator, not invention here.
