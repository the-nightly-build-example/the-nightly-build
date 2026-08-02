# Researcher brief: the-instruments/energy-per-query

## Inputs (begin here)
- This brief and `commission.md`.
- `editorial-direction.md` for standards.

## Output (write only this)
`.nb-work/the-instruments/energy-per-query/agent-artifacts/the-instruments/energy-per-query/researcher/01/evidence.md`
Follow the researcher SKILL sections exactly.

## Source policy
the-instruments lesson: **min 8 sources; primary ≥ 4, secondary ≥ 1.** A
provider's statement about its own footprint is a primary but interest-laden
source; classify it primary and flag the stake.

## Required primary documents (read first-hand)
1. **Epoch AI, "How much energy does ChatGPT use?"** (Josh You, 2025):
   https://epoch.ai/gradient-updates/how-much-energy-does-chatgpt-use — record
   the exact central estimate (~0.3 Wh for a typical GPT-4o query), the
   assumptions (active params, H100 throughput, output tokens, PUE), and how
   they explain the gap with older, higher estimates.
2. **Alex de Vries, "The growing energy footprint of artificial
   intelligence," *Joule* 3(10) or 7(10) 2023** — record his per-query / per-
   request figure, the method (top-down from hardware/servers, e.g. via
   SemiAnalysis and Google search-volume comparison), and his stated
   uncertainties. Confirm the exact number he gives and its denominator.
3. **Li, Yang, Islam, Ren, "Making AI Less Thirsty" (arXiv 2023, later
   revisions)** — record the water figure (e.g. ~500 ml per some number of
   queries), and crucially the definition: on-site cooling water vs off-site
   (electricity generation) water, WUE, and the datacenter-location dependence.
4. **A provider's own per-query figures**, if on record (e.g. a 2025 statement
   attributing ~0.34 Wh and a small water volume per query). Get the exact
   quote and source; label interest-laden.

## Also verify
- The origin of the **"Google search ≈ 0.3 Wh"** reference figure (find the
  Google source of record and its date; it is old — note the year). This is
  half of the "10x a Google search" comparison.
- Whether/where the "ChatGPT uses ~10x a Google search" claim was made and how
  its two inputs were chosen; and how Epoch's reanalysis undercuts it. Two
  independent confirmations for any accusation of a specific error.
- Definitions to teach: watt-hour (give an everyday equivalent), PUE (power
  usage effectiveness), WUE (water usage effectiveness), "inference" vs
  training energy. Capture a clean primary/authoritative definition for each.
- Context figure for scale: total datacenter or AI electricity load from a
  credible body (e.g. IEA), with year and denominator — for the reader's sense
  of scale only, clearly separated from per-query claims.

## Contradictions to hunt (this is the spine)
- The de Vries (~3 Wh) vs Epoch (~0.3 Wh) gap: pin the exact assumption(s) that
  produce the 10x difference (output-token count, chip generation, active
  params). Quote both.
- Provider self-report vs independent estimate: where they agree/differ and why.
- The water figure's framing disputes (which water counts).
Record all of these; the article's value is the reconciliation.

## Numbers section
Assemble a clean comparison series suitable for a chart: each published
per-query **energy** estimate with its value (Wh), what counts as a "query,"
the method, the chip/year assumed, and the owning source. Do the same for the
water figures. Flag which are directly comparable and which are not.

## Source assets
Consider one exact visual from a cited primary (e.g. a figure or table from
Epoch or de Vries showing the estimate breakdown) if it would let the reader
test the argument better than prose; else `None found`.

## Control
`DONE researcher <evidence-path>`; `BLOCKED researcher <reason>` if a required
primary cannot be opened after a real browser attempt.
