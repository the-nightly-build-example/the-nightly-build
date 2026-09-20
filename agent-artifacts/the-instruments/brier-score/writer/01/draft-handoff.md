# Draft handoff: the-instruments/brier-score (writer, round 01)

## Original-work sentence

The evidence record supplies the individual facts (Brier's own formula and
range, Murphy's three-term split, Good Judgment Open's two-term convention,
Halawi et al.'s numbers) as separate entries; the article's own work is to
run the same concrete case through each mechanism to make two of its claims
checkable rather than asserted — using Murphy's uncertainty term to show
mechanistically why the always-guess-the-base-rate trick pays off more as an
event gets rarer (rather than just stating that it does), and running Good
Judgment Open's own worked example (a 70-percent forecast that rains)
through the halved, one-term formula to show the two-scale trap as a single
before/after number (0.18 vs. 0.09) on one real forecast, instead of two
abstract conventions asserted to differ.

## Proof result

`./nb stamp` then `./nb check .nb-work/the-instruments/brier-score/library/the-instruments/brier-score.html --series the-instruments --library .nb-work/library` (links included):

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

Final stamp: words=2194 (band 1200–2200), reading_minutes=10, sources=8
(5 primary: Halawi et al. 2024, Brier 1950, Good Judgment Open FAQ,
ForecastBench/Karger et al. 2025, Lu 2025; 3 secondary: Wikipedia, Ferro &
Fricker 2012, the AI Alignment Forum critique). No warnings left outstanding
— the earlier em-dash-count and sentence-density warnings seen mid-draft
were fixed by rewriting, not suppressed.

Display-text self-test done before this handoff: headline, dek, and all four
subheads checked against the evidence's Numbers section (0.03, 0.179/0.149,
0.002, 0.238/0.240); nb-meta `dek` and the rendered dekline are identical;
headline and dek checked against `spec/headlines.md`'s banned molds (no
comma triad, no colon subtitle, no suspended question) and against the
commission's named recent habits (no "By the end..." opener, no two-part-
balance takeaway, no "Reading X as Y" closer, no "How a X becomes a Y"
heading — all four headings vary construction).

## Open questions

None outstanding for the researcher or editor. Two source substitutions the
researcher flagged (Murphy 1973 cited at one remove via Ferro & Fricker 2012;
Good Judgment Open's FAQ standing in for Metaculus's gated methodology page)
are used and cited exactly as the evidence record and brief specified. The
second, unplanned comparability trap (Good Judgment Open's two-term scale)
is used as directed, kept to one section and not expanded into a survey of
every platform's convention.
