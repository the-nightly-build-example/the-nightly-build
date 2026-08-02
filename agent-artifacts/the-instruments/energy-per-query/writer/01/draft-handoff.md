# Draft handoff: the-instruments/energy-per-query (round 01)

## Original work
The article puts every major published per-query energy figure (Google's
2025 narrow and comprehensive telemetry, Epoch's bottom-up estimate,
Altman's undisclosed self-report, de Vries's top-down estimate) on one
watt-hour axis in a single chart and reconciliation prose, and for each gap
between adjacent figures names the one specific assumption that separates
them: output-token count (4x), active-parameter count (~1.75x), chip
generation, peak-vs-utilization power draw, and — the sharp addition —
measurement boundary (Google's own 2.4x swing on the identical prompt). No
source performs this side-by-side, like-for-like reconciliation itself; the
article's visible contribution is the axis (Fig. 1 / `chart-1.py`) plus the
paragraphs that read each gap back to its named cause.

## Files changed
- Article: `/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`
- Chart script + PNG: `/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query/chart-1.py` and `chart-1.png` (rendered with `nb chart`, inspected the PNG twice — once to fix a legend/title overlap).

## Proof result
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-instruments \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html
```
`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE` (link check on, all 9 source
URLs resolve). Word count settled at exactly 2200 (band 1200–2200) after
several rounds of splitting dense sentences and trimming connective tissue;
no idea's explanation was shortened to make room — all three commissioned
ideas (denominator problem with real arithmetic, bottom-up vs top-down
methods plus the boundary swing, and the 10x-claim/water misleading case)
are taught in full. `nb preview` built cleanly; render-check reported no
Chrome available in this environment, so the chart PNG was inspected
directly instead (twice, including the legend-overlap fix).

## Editorial decisions held from the brief
- Provider self-reports (Altman, Google) marked interest-laden in prose at
  first use; Altman's proximity to Epoch's number is explicitly called
  likely coincidence, not corroboration, quoting Google's own critique.
- De Vries's "3 Wh" is presented as a secondary compression of two
  convergent derivations, not his own point estimate (his 2.9 Wh top-down
  figure is the one carried through the reconciliation).
- IEA scale context uses only the Carbon Brief figure (~1% today, ~945 TWh
  by 2030) as background, not a per-query number, and the ~1%/~1.5%
  discrepancy is not leaned on.
- Chart holds only same-denominator ("one typical text query") figures and
  marks measured vs. estimated/self-reported by color and legend; the 2009
  Google-search figure and BLOOM/LLaMA figures were deliberately left off
  the chart (different query type / different models) and handled in prose
  instead.

## Remaining questions
None outstanding. All three ideas were fully sourced from the evidence
record with no gaps requiring a researcher follow-up.
