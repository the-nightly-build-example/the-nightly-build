# Draft handoff: the-instruments/energy-per-query (round 02 — required repair)

## What this round did
Closed the one required-change gap from the round-01 editorial review: added
an everyday comparison at first use for every figure the review named, using
only comparisons already present in the evidence record's own quotes. No new
research, no reopened settled work. The original-work sentence from round 01
still holds unchanged: the article puts five published per-query energy
figures on one watt-hour axis and, for each adjacent gap, names the single
stacked assumption that produces it — the article's visible contribution
(Fig. 1 / `chart-1.py` + the reconciliation prose) is untouched this round.

## Comparisons added, and where
All edits are in one file:
`/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`
No chart file touched.

1. **Google 0.24 Wh (comprehensive figure), first use in the Fig. 1 caption:**
   "Google's own May 2025 production telemetry puts a Gemini prompt at 0.10 to
   0.24 Wh, the higher figure under nine seconds of television, depending
   only on what gets counted." — Google's own framing ("less energy than
   watching nine seconds of television"), cited to source 5 (already cited in
   that sentence). Per the brief, only the comprehensive (0.24 Wh) figure got
   the comparison; the 0.10/0.24 pair is the boundary-swing point and one
   comparison suffices.
2. **Altman 0.34 Wh, first use in the same Fig. 1 caption:** "Sam Altman's
   undisclosed self-report puts it at 0.34, about an oven's draw for just
   over a second." — Altman's own framing, cited to source 6. Per the brief's
   note to vary the concrete object, I used only the oven half of Altman's
   quote ("about what an oven would use in a little over one second") and
   left out the lightbulb half, since the LED-bulb comparison is already used
   for Epoch's 0.3 Wh figure earlier in the piece; using both would have made
   the two comparisons read as the same formula.
3. **945 TWh (2030 data-centre projection):** no edit made. The article
   already states, in the sentence that carries this figure, the exact
   fallback framing the brief specifies for when no sourced country
   equivalence exists: "Data centers draw just over 1% of the world's
   electricity, a share the International Energy Agency expects to more than
   double by 2030, to about 945 terawatt-hours a year." This is the "~1% of
   global electricity, on track to roughly double by 2030" scale framing the
   brief names as sufficient in the absence of a sourced country comparison,
   and the evidence record supplies no such country equivalence — inventing
   one was correctly ruled out. Flagging this explicitly rather than editing
   for its own sake, per "do not re-open settled work."
4. **Li et al. 10–50 mL, first use in the water paragraph:** "Li and
   coauthors' figure, that a GPT-3-era reply costs 10 to 50 milliliters, or
   10–50 such replies per 500-milliliter bottle, sums water evaporated
   on-site..." — Li et al.'s own bottle-count framing, cited to source 9
   (already cited at the end of that sentence's clause chain). This also
   pays off the opener's "half a bottle of water" line, as the brief noted.
5. **Google 0.26 mL, same paragraph:** "Google's comprehensive figure is 0.26
   milliliters, about five drops of water," cited to source 5 — Google's own
   framing ("five drops of water").
6. **Altman ~0.32 mL, same sentence:** "and Altman's undisclosed figure is
   about 0.32, roughly a fifteenth of a teaspoon," cited to source 6 —
   Altman's own framing ("roughly one fifteenth of a teaspoon"), trimmed
   "one" for one clean clause.

Each addition is one clause at first use, per voice guide move 4 (no stacked
comparisons on one figure), and none touches a figure that already had a
comparison (0.3 Wh Epoch's LED-bulb comparison and 2.9 Wh de Vries's bulb
comparison are unchanged).

## Round-01 editor edits preserved (verified by direct grep after editing)
- "Ireland" (not Texas) for the 7.1 mL figure — present, no "Texas" anywhere.
- "seventeen years" / "seventeen-year-old baseline" (not sixteen) — both
  occurrences present.
- "already well under a tenth the size" — present.
- "roughly ten times too high" — present.
- Both cut sentences ("The difference is not measurement error but a
  boundary..." and the "five assumptions waiting to be named" closer) —
  confirmed absent, not reintroduced.

## Word count
Recounted honestly with the engine's own `Article.word_count` (same property
`nb check` uses) after all additions: **2200** words, exactly at the top of
the 1200–2200 band. Updated `nb-meta.words` from 2163 to 2200. No content was
cut to make room; the additions were kept to one tight clause each and two
were folded into existing sentences rather than given their own sentence, to
stay inside the band without touching any settled prose.

## Proof result
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-instruments \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html
```
`BLOCK: 0`, `WARN: 0`, verdict `PUBLISHABLE`. Em-dash count unchanged at 2
(≤4 ceiling); no new em-dashes were introduced (the Li et al. range uses an
en dash, "10–50," matching the brief's own notation, not counted against the
em-dash ceiling). Banned terms (leverage, load-bearing, machinery,
revolutionary/transformative/game-changing) untouched by this round's edits.

## Remaining questions
None. All six required comparisons were available verbatim or as a direct
paraphrase inside the evidence record; no researcher follow-up needed.
