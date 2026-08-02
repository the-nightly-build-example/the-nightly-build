# Editor review-brief: the-instruments/energy-per-query (round 01)

## Inputs (begin here; read the voice guide first)
- This brief.
- Editorial direction: `../../editorial-direction.md`
- The EXACT writer brief (leak detection): `../../writer/01/brief.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Evidence record: `../../researcher/01/evidence.md`
- Draft handoff (open original-work sentence at third read):
  `../../writer/01/draft-handoff.md`
- Article: `/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`
- Chart provenance + image:
  `.../library/the-instruments/energy-per-query/chart-1.py` and `chart-1.png`
- Template context: `.../energy-per-query/.nb-context/`

Three ordered reads (skeptic, cut, reader); surgical edits only.

## Points to test hardest (skeptic read)
- **The reconciliation (the spine and original work).** Verify each named gap
  factor against the evidence: output tokens 2,000 vs 500 (4x); dense 175B vs
  ~100B-active MoE (~1.75x); A100 vs H100; peak vs utilization-adjusted power;
  and Google's own measurement-boundary swing 0.10 vs 0.24 Wh (2.4x, same
  prompt). Recompute Epoch's 1,050 watt-seconds ÷ 3,600 = 0.29 Wh.
- **Provider self-reports are interest-laden — verify it's said.** Altman's
  0.34 Wh near Epoch's 0.3 must read as likely coincidence (no disclosed method),
  not corroboration; Google 2025 and Google 2009 also interest-laden.
- **De Vries "3 Wh"** must be presented as a secondary compression of two
  convergent derivations (2.9 Wh top-down; and the Hennessy "10x" × 2009 Google
  0.3 Wh), not his single point estimate.
- **The "10x a Google search" trace:** Hennessy's verbal "10x" (Reuters, 2023)
  × Google's **2009** 0.3 Wh figure — a 16-year-old number, not a measurement of
  today's ChatGPT or search. Confirm the age/staleness is stated.
- **Water case:** Li et al. 10–50 mL sums on-site + off-site water and varies
  ~7x by location (7.1 mL Texas to 47.5 mL Washington); provider low numbers
  partly follow from a ~10x smaller energy base, not water efficiency alone;
  Altman's water figure has no disclosed method. Verify measured vs estimated vs
  extrapolated is marked.
- **IEA context** used only as scale (data centres ~1% of electricity; ~945 TWh
  by 2030), not a per-query number; the ~1%/~1.5% discrepancy not leaned on.
- Give every headline number an everyday comparison at first use. Verify display
  text as claims and labels; audit `data-nb-kind` (Epoch, de Vries, SemiAnalysis,
  Li et al., Altman, Google 2025, Google 2009 = primary; Reuters, Carbon Brief =
  secondary).

## Chart (inspect as a reader)
Open `chart-1.png` and its `chart-1.py`. Critical honesty checks:
- Only same-denominator ("one typical text query") figures on the axis;
  confirm the 2009 Google-search figure and BLOOM/LLaMA (different query/model)
  are NOT on it (handled in prose).
- Measured vs estimated/self-reported visibly distinguished (color/legend).
- Axis labeled (Wh per query), caption states what "a query" means, notes bars
  are not all like-for-like, and cites sources. Numbers match the evidence.
Request corrections through the writer; never edit the asset yourself.

## Cut read
- Banned terms: em-dash ≤4, leverage ≤1, load-bearing 0, machinery 0 (verify).
- Cut self-grading, signposts, stock revelation frames, prompt leakage (compare
  against the writer brief). **Do NOT let a "The number X published about itself"
  opener stand** (used twice this week incl. the sibling tokens-per-second), nor
  the tokens-per-second heading molds, nor comma-triad headings/deks. Compare
  deks/headings against recent library.

## Reader read
One sentence on what the piece gives beyond its sources; compare with the
draft-handoff's original-work sentence (the one-axis reconciliation). Judge voice
against the exemplars. Retest the headline as the largest claim.

## Output
Write `../../editor/01/editorial-review.md` with the three required lines, direct
edits, required work by owner, and the decision. Return `DONE editor <path>` only
if no redraft is required; otherwise `REQUEST writer/researcher <need>`. Do not
run the proof; the writer reruns it on any revision.
