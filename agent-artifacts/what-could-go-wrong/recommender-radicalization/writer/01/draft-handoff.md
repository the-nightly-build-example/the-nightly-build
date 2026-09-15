# Draft handoff: what-could-go-wrong/recommender-radicalization (writer round 01)

## Original-work sentence

This piece holds Pariser's and Tufekci's engagement-optimization mechanism against
the four empirical tests built to detect it in real systems (Hosseinmardi 2021,
Chen 2023, Bakshy 2015, Guess 2023), and, in a synthesis table plus the closing
section, names the specific scope-limit that keeps each null from settling the
question — population-level data that cannot see an individual, a 2020 dataset
that arrives after YouTube rewired its recommender, and a Meta experiment run
inside a window Meta had already altered — so that both "the algorithm
radicalizes ordinary users" and "recommenders are harmless" are shown spending
confidence neither side's cited study actually measured. That comparative frame
is not in the evidence record; the evidence supplies the studies and their
individual caveats separately, in prose and in a Contradictions list.

## Proof result

- `./nb stamp .nb-work/what-could-go-wrong/recommender-radicalization/library/what-could-go-wrong/recommender-radicalization.html`
  → words=2200, reading_minutes=10, sources=9
- `./nb check ... --series what-could-go-wrong --no-check-links` → BLOCK: 0, WARN: 0
- `./nb check ... --series what-could-go-wrong` (links included) → BLOCK: 0, WARN: 0
- Iterated to resolve W-LENGTH-HIGH (started at 2727 words, trimmed to exactly
  2200, the top of the lesson band) and seven W-SENTENCE-DENSITY warnings
  (split or tightened the flagged sentences). No warning was left standing.
- `nb render-check` could not run (no Chrome in this environment); built a
  local preview with `engine/build_site.py --preview` instead and inspected the
  rendered HTML directly — bookends, the synthesis table, and the pull quote
  all render with the documented furniture classes.

## Self-test corrections made before handoff

- Caught and fixed two date errors during the display-text pass: Pariser's
  filter-bubble talk is dated 2011 in the evidence (not 2010, as an earlier
  draft sentence had it), and Bakshy et al. (2015) is four years after that
  talk, not three. Both are now correct in the orientation and
  whose-choices-shape-feed sections.
- Restored exact capitalization on the UMass Amherst quote ("Beginning around
  the start of November 2020...") to match the evidence record's verbatim
  transcription after an earlier compression pass had lowercased it.

## Notes for the editor

- No source asset or `nb chart` figure was built. The evidence record flagged
  three candidate source assets (Hosseinmardi Fig. 2, Chen Fig. 2, Bakshy Fig.
  3); instead, the piece renders the cross-study comparison as an `nb-table`
  built from the evidence record's own verified numbers (population/window,
  finding, and scope-limit per study), which carries the article's own
  synthesis more directly than any single source figure would. Open to
  revisiting if the editor wants a chart alongside it.
- The Guess et al. enrollment figure ("about 23,000 users per study") carries
  `data-nb-note` flagging it as sourced from Science's news coverage, not
  verified against the paywalled study body, per the evidence record's own
  flag. No per-platform figure was invented.
- No evidence or voice gap is open. The three "This round" bounds (population
  vs. individual, 2020-vs-2016 system, the altered Meta window) are carried in
  prose at first mention and again in the synthesis table.
