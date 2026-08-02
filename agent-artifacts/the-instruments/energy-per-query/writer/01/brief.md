# Writer brief: the-instruments/energy-per-query (round 01)

## Inputs (begin here; reread the voice guide before drafting)
- Commission: `../../commission.md`
- Editorial direction: `../../editorial-direction.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`  ← complete claim set (9 sources)
- Initialized article (edit in place):
  `/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`
- Template context: `.../energy-per-query/.nb-context/` (read `furniture/engine.md`)

## Output
- Fill the article HTML.
- Write `writer/01/draft-handoff.md`.

## What to write
An Instruments `lesson` teaching how the "energy per AI query" number is made
and why honest estimates for the same query differ ~10x. The reconciliation is
the spine and the original work. Teach three ideas completely:

1. **The denominator problem: "per query" has no fixed definition.** Energy per
   query ≈ (energy per output token) × (output tokens per query), and energy per
   token depends on active parameters, chip, and how hard the hardware is run.
   Name the four compounding choices that separate de Vries (~2.9–3 Wh) from
   Epoch (~0.3 Wh), from the evidence's Contradiction 1: output tokens (2,000 vs
   500, a 4x factor), dense 175B vs ~100B-active mixture-of-experts params (~1.75x),
   A100 vs H100 chip, and peak power vs a utilization-adjusted draw. Do the
   arithmetic in prose (voice guide): Epoch's 1,050 watt-seconds ÷ 3,600 = 0.29 Wh.
2. **Two ways to get the number, and a third axis nobody sees.** Bottom-up
   (Epoch: FLOPs/token × tokens ÷ chip throughput, with utilization discounts)
   vs top-down (de Vries: assumed fleet power ÷ assumed daily requests). State
   each method's blind spot. Then the sharp addition: Google's own Aug-2025
   measurement shows that changing only the *measurement boundary* (counting idle
   machines, CPU/DRAM, data-center overhead, or not) swings its own number 2.4x —
   0.10 Wh "narrow" vs 0.24 Wh "comprehensive". Same query, same company, same
   month. So "per query" hides a boundary choice as much as a token count.
3. **Where the number misled.** Trace "ChatGPT uses 10x a Google search": it is
   Alphabet chair John Hennessy's verbal "likely 10 times more than a standard
   keyword search" (Reuters, Feb 2023) multiplied by Google's **2009** figure of
   0.3 Wh per search — a 16-year-old number, not a measurement of today's ChatGPT
   or today's search. Epoch shows the 3 Wh side is likely ~10x too high. Then the
   water figure: Li et al.'s 10–50 mL per response sums on-site cooling water and
   off-site power-plant water and varies ~7x by location in their own table (7.1
   mL Texas to 47.5 mL Washington); provider self-reports (Altman ~0.32 mL;
   Google 0.26 mL) are far lower partly because their *energy* base is ~10x
   smaller, not from water efficiency alone — and Altman's blog discloses no
   method at all. Mark throughout: measured vs estimated vs extrapolated.

If space is tight, keep ideas 1–2 whole and compress the water case to one tight
paragraph.

## Decisions fixed for you (hold to the evidence)
- Every headline number carries an everyday comparison at first use (voice
  guide): 0.3 Wh ≈ an LED bulb for a few minutes; a US household ≈ 28,000 Wh/day.
- **Provider self-reports are primary but interest-laden — say so.** Altman's
  0.34 Wh sitting near Epoch's independent 0.3 Wh is very likely coincidence, not
  corroboration (no disclosed model, denominator, or boundary). Do not present it
  as confirmation.
- **De Vries did not assert a single "3 Wh" point estimate.** His paper gives two
  converging derivations and a five-bar chart (0.3 to 8.9 Wh); "de Vries's 3 Wh"
  is a secondary compression. You may note this as itself an instance of the
  denominator problem (which bar is "the" number?).
- IEA scale context is thin (researcher could not open IEA directly). Use only
  the verified Carbon Brief figure (data centres ~1% of global electricity;
  ~945 TWh projected by 2030), clearly as scale context, NOT a per-query number,
  and do not lean on the unresolved ~1%/~1.5% discrepancy.

## Source handling
- 9 sources, numbered in first-citation order. Kinds from the evidence: Epoch,
  de Vries, SemiAnalysis, Li et al., Altman blog, Google 2025, Google 2009 =
  **primary** (flag Altman + Google 2025 + Google 2009 as interest-laden in
  prose where they speak about their own product); Reuters, Carbon Brief =
  **secondary**. 7 primary + 2 secondary meets policy (min 8; primary ≥4;
  secondary ≥1). Set `data-nb-kind` accordingly; add `data-nb-locator` where the
  evidence supplies it.

## Furniture — the chart is encouraged here
- A single honest **bar chart** of the per-query energy estimates is the natural
  visual and delivers the reconciliation: use `nb chart` with the evidence's
  verified "Energy per query (Wh)" series. Requirements if you build it:
  - Only put figures on it that share a "single typical text query" denominator,
    OR clearly annotate each bar's denominator. Do NOT silently place
    non-comparable bars side by side.
  - Distinguish **estimated** vs **measured** figures (label or color), mirroring
    the honesty point.
  - Caption states what counts as "a query," names it as Wh per query, and cites
    the sources; note the bars are not all like-for-like.
  - Inspect the rendered PNG; commit the `chart-N.py` provenance.
- Alternatively (lower-risk), present the reconciliation as an `nb-table`. A
  `nb-stat-strip` (e.g. 0.3 Wh Epoch, 3 Wh de Vries, 2.4x boundary swing) can
  complement but not replace the reconciliation. Water numbers can be a short
  table or prose. Use only documented furniture; no external images.

## Bookends (write last)
- Background: link `the-instruments/tokens-per-second` (the sibling number about
  inference speed) and one useful outside item. Optionally
  `the-mechanics/autoregressive-generation` if you lean on "output length drives
  cost". Go deeper: beyond this paper. Relative links e.g.
  `../the-instruments/tokens-per-second.html`.

## Headline / dek / headings
- Headline: state the finding with actors/numbers named; no colon-subtitle, no
  comma-triad, no unanswered question. Candidate territory: the same query
  measured at 0.3 and 3 Wh, both honest; or the "10x a Google search" number
  resting on a 2009 figure.
- **Do NOT open with "The number X published about itself"** — used twice this
  week including the sibling piece tokens-per-second. Vary headings; avoid the
  tokens-per-second molds and comma-triads.
- Dek: adds what the headline omits; no banned dek molds; check recent deks.

## Constraints
- Word band 1200–2200. Banned (proof-enforced): em-dash ≤4, leverage ≤1,
  load-bearing 0, machinery 0, revolutionary/transformative/game-changing 0.
- nb-meta actual values: series the-instruments, slug energy-per-query, template
  lesson, mode open, order null, date 2026-08-02, harness "claude-code-routine",
  model "claude-sonnet-5",
  tags ["energy","water-footprint","inference-cost","datacenters"]. Measure
  sources/words/reading_minutes.

## Original work
In `draft-handoff.md`, name the one visible act of original work: the like-for-
like reconciliation that puts the major published per-query figures on one axis
and names the single assumption separating each pair (tokens, params, chip,
power-draw, measurement boundary). It must be visible in the article (the chart
or table plus the prose that reads it).

## Prove and hand off
Run to `BLOCK: 0`:
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-instruments \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html
```
If you build a chart, run `nb preview` and inspect the render. Treat warnings as
revision notes. Write `draft-handoff.md`. Return `DONE writer <draft-handoff-path>`
after BLOCK: 0, or a REQUEST line if evidence/voice is missing.
