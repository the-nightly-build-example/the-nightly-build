# Editorial review: the-instruments/energy-per-query (round 01)

## Skeptic
Skeptic: thesis "energy per query has no fixed definition; the same query
prices out ten times apart because four stacked, nameable modeling choices
separate two honest estimates, and even one company's own number swings
2.4x on a fifth choice (the measurement boundary) with nothing else
changed"; tested 4 claims (Epoch 0.3 Wh vs de Vries 2.9 Wh reconciliation;
Google's 0.10/0.24 Wh boundary swing; the "10x a Google search" trace to
Hennessy 2023 x Google 2009; the Li et al. water range); broke: two factual
errors, both fixed in place rather than sent back —
- **Place/number mismatch.** "7.1 milliliters in Texas" paired the low-end
  figure with the wrong location. Evidence's own Table 1 detail (already at
  hand) gives Texas 7.590 mL and Ireland 7.107 mL, "lowest of all 18
  locations." The 7.1 figure is Ireland's. Fixed by changing "Texas" to
  "Ireland" (evidence.md's own summary lines 536 and 582 carry the same
  mislabel and should be corrected there for future pieces, but that does
  not block this article).
- **Date math.** "Sixteen years old" for the 2009 baseline undercounts by a
  year against this article's own 2026-08-02 dateline (2026 − 2009 = 17).
  Fixed both occurrences to "seventeen."
- Recomputed and confirmed: 1,050 Ws ÷ 3,600 = 0.29 Wh; 4x (tokens) × 1.75x
  (params) = 7x; 564,000,000 ÷ 195,000,000 = 2.9 Wh; Google's 0.10 vs 0.24 =
  2.4x; Hennessy 10x × 0.3 Wh = 3 Wh. All check out against the evidence and
  the primary sources it quotes.
- Confirmed the piece never lets Altman's 0.34 Wh or Google's 0.10/0.24 Wh
  read as corroboration of Epoch's 0.3 Wh; confirmed de Vries's "3 Wh" is
  kept as the Hennessy-derived figure, distinct from his own 2.9 Wh
  top-down number; confirmed the IEA/945 TWh figure is used only as scale,
  not leaned on for the unresolved ~1%/~1.5% discrepancy; confirmed
  `data-nb-kind` on all 9 sources matches the brief (Epoch, de Vries,
  SemiAnalysis, Li et al., Altman, Google 2025, Google 2009 = primary;
  Reuters, Carbon Brief = secondary).
- One tightened claim, not broken but loosely worded: "Google's own
  energy-per-prompt figure is already a tenth the size of the 4-watt-hour
  figure" understated the actual gap (0.24/4 = 0.06, under a sixteenth, not
  a tenth). Fixed to "well under a tenth."
- **Not fixed, returned to writer:** the house floor and the voice guide
  both require every energy/water figure to carry an everyday comparison at
  first use (voice guide move 1; "Numbers" section of the house floor). The
  0.3 Wh and 2.9 Wh headline figures get one (the LED-bulb comparison). The
  0.10/0.24 Wh Google figures, the 0.34 Wh Altman figure, the 945 TWh scale
  figure, and all four water figures (10-50 mL Li et al., 0.26 mL Google,
  0.32 mL Altman) do not. This is a real gap against a standard the paper
  cannot loosen, not optional polish, and closing it means writing new
  comparison sentences in several places, past what an editor cuts or
  tightens in place.

## Cut
Cut: 2 sentences; worst tell: a formulaic "X is not Y; it is Z" closer
manufactured as the article's very last line ("The next unfamiliar
per-query number is not a fact to accept or reject. It is five assumptions
waiting to be named.") — a generic moral that would fit any Instruments
piece verbatim, exactly what the template identity's "skip the generic
moral" line and the voice guide's "no closer built as a reusable formula"
note both rule out. The paragraph's real, earned ending was the sentence
just before it. Cut both trailing sentences; the takeaway now ends on the
specific finding. Also cut "The difference is not measurement error but a
boundary, drawn in a different place," a second instance of the same
hedged-contrast mold that only restated what the two preceding sentences
already established; cutting it brings the piece's earned "X is not Y"
contrasts down to two (the "not a rounding error or a scandal" line and the
"coincidence of magnitude is not... agreeing" line on false corroboration),
at the house ceiling instead of past it. No prompt leakage found: compared
the article's prose against the writer brief's internal labels
("denominator problem," "spine," "original work") and none appear verbatim
or lightly reworded. Opener is not "The number X published about itself";
headings and dek were checked against the five most recent the-instruments
library pieces (tokens-per-second, llm-as-a-judge, context-window,
perplexity, bar-exam-percentile) and match none of their molds or cadences.
Banned-term counts after cuts: em-dash 2 (≤4), leverage 0, load-bearing 0,
machinery 0 — all pass.

## Reader
Reader: this gives me a like-for-like axis no single source builds — five
published per-query figures (two of Google's own boundaries, Epoch's
bottom-up model, Altman's self-report, de Vries's top-down model) placed on
one watt-hour scale, with the specific assumption that separates each
adjacent pair named and, where the sources allow it, quantified (tokens 4x,
params 1.75x, boundary 2.4x), rather than a debate recap that ends in a
verdict. This matches the draft-handoff's original-work claim, and it holds
up: no cited source performs this specific side-by-side reconciliation
itself. The prose reads closer to the voice-guide exemplars (Epoch's
audit-style term-then-number pairing, Ritchie's status-marking of
measured/estimated/self-reported) than a median AI summary — it shows its
arithmetic inline rather than asserting a corrected number. The headline,
retested as the largest claim, holds: 0.3 Wh (Epoch) and 2.9 Wh (de Vries)
are both real, sourced, "honest" figures for the same rough action, and the
piece defends both halves in full.

## Direct edits made
1. "7.1 milliliters in Texas" → "7.1 milliliters in Ireland" (place/number
   mismatch; Ireland is the location the evidence's Table 1 actually pairs
   with 7.1 mL).
2. "already a tenth the size" → "already well under a tenth the size"
   (0.24 Wh ÷ 4 Wh = 0.06, under a sixteenth, not a tenth).
3. "sixteen years old" → "seventeen years old"; "a sixteen-year-old
   baseline" → "a seventeen-year-old baseline" (2026 − 2009 = 17).
4. "closer to ten times too high than too low" → "roughly ten times too
   high" (the piece already computed the ratio as exactly 10x two
   paragraphs earlier; the hedge added confusion, not precision).
5. Cut: "The difference is not measurement error but a boundary, drawn in a
   different place."
6. Cut: "The next unfamiliar per-query number is not a fact to accept or
   reject. It is five assumptions waiting to be named."
7. `nb-meta` "words": 2200 → 2163, recounted with the engine's own
   `Article.word_count` after the cuts above (still inside the 1200–2200
   band).

## Chart (inspected as a reader)
`chart-1.png` and `chart-1.py` pass the honesty checks. Only same-
denominator ("one typical text query") figures are on the axis — the 2009
Google-search figure and the BLOOM/LLaMA figures are correctly left out and
handled in prose, as the script's own docstring notes. Measured (Google's
two boundaries, gold) and estimated/self-reported (Epoch, Altman, de Vries,
blue) are visibly distinguished by color and a legend, and Epoch's own
0.29 Wh is correctly grouped as estimated rather than measured. Axis is
labeled "Watt-hours per query"; the x-axis subtitle states the shared
denominator; the caption states what "a query" means, names the units,
cites all five sources, and says the bars are not all like-for-like. All
five plotted values (0.10, 0.24, 0.29, 0.34, 2.90) match the evidence
record's Numbers table exactly. No correction requested.

## Required work by owner
**Writer:** add an everyday comparison at first use for the Google
0.10/0.24 Wh figures, the Altman 0.34 Wh figure, the 945 TWh scale figure,
and the water figures (10-50 mL Li et al., 0.26 mL Google, 0.32 mL Altman).
The evidence record already carries ready sourced comparisons for most of
these — Google's own "less energy than watching nine seconds of
television" and "five drops of water" (source 5/6), Altman's own "about
what an oven would use in a little over one second" and "roughly one
fifteenth of a teaspoon" (source 6), and Li et al.'s own bottle-count
framing (10-50 responses per 500 mL bottle, which would also pay off the
opener's "half a bottle of water" line) — so this is restoring cut or
never-drafted material against the writer's own brief and the voice
guide's move 1, not new research.
**Researcher:** none. No sourcing or evidence gap found; the two factual
errors caught above were fixable from evidence already on hand and were
fixed directly.

## Decision
REQUEST writer: close the missing-everyday-comparison gap listed above
(Google 0.10/0.24 Wh, Altman 0.34 Wh, the 945 TWh figure, and the four
water figures), then rerun the proof.
