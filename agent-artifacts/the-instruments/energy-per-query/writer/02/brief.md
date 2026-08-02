# Writer brief: the-instruments/energy-per-query (round 02 — required repair)

## Why this round
The round-01 editor approved the piece's substance, chart, and sourcing but
returned ONE required change against a standard the paper cannot loosen (house
floor "Numbers"; voice guide move 1): several figures lack an everyday
comparison at first use. Close exactly that gap. Do not re-open settled work.

## Inputs (begin here)
- The round-01 editorial review (your required-change list):
  `../../editor/01/editorial-review.md` (see "Required work by owner")
- Your round-01 handoff: `../../writer/01/draft-handoff.md`
- Evidence record (carries the ready sourced comparisons): `../../researcher/01/evidence.md`
- Voice guide: `../../writing-coach/01/voice-guide.md`
- Editorial direction: `../../editorial-direction.md`
- Article (edit in place; it ALREADY contains the editor's round-01 direct edits —
  preserve them): `/home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html`

## The required change (and only this, plus what it logically touches)
Add a concrete everyday comparison at FIRST use for each figure below. The
evidence record already supplies sourced comparisons — use those, cite as
already cited, invent no new numbers:
- **Google 0.10 / 0.24 Wh** (median Gemini text prompt): Google's own framing —
  "less energy than watching nine seconds of television" (Source 6). Use it for
  the 0.24 Wh figure at first use; the 0.10 vs 0.24 pair is the boundary-swing
  point, so a comparison on the comprehensive (0.24) figure suffices.
- **Altman 0.34 Wh**: Altman's own framing — "about what an oven would use in a
  little over one second, or a high-efficiency lightbulb would use in a couple
  of minutes" (Source 5). (Keep the LED-bulb comparison distinct from Epoch's if
  both appear near each other; vary the concrete object so they don't read as a
  formula.)
- **945 TWh (2030 data-centre projection)**: give a scale comparison a reader
  holds. The evidence frames data centres at ~1% of global electricity today
  rising toward this figure; express 945 TWh in a way the reader can picture
  (e.g. relative to a country's annual electricity use ONLY if the evidence
  supports the specific comparison — otherwise keep it to the "~1% of global
  electricity, on track to roughly double by 2030" scale framing already
  sourced to Carbon Brief). Do not invent an unsourced country equivalence.
- **Water figures at first use**: Li et al. 10–50 mL → its own bottle framing
  ("10–50 medium responses per 500 mL bottle," Source 4), which also pays off
  the opener's "half a bottle" line; Google 0.26 mL → "about five drops of
  water" (Source 6); Altman ~0.32 mL → "roughly one fifteenth of a teaspoon"
  (Source 5).

Keep each comparison to one clause at first use (voice guide move 4). Do not
stack multiple comparisons on one figure. Do not add comparisons to figures that
already have one (0.3 Wh Epoch, 2.9 Wh de Vries keep the LED-bulb comparison).

## Preserve (do not undo the editor's round-01 edits)
The article already contains the editor's fixes: "Ireland" (not Texas) for
7.1 mL; "seventeen years" (not sixteen); "well under a tenth"; "roughly ten
times too high"; two cut sentences; nb-meta words 2163. Keep all of these. Your
additions will raise the word count — recount and update `nb-meta.words`
honestly; stay within 1200–2200 (you have headroom).

## Constraints
- Banned (proof-enforced): em-dash ≤4 (currently 2 — do not add net em-dashes
  past 4), leverage ≤1, load-bearing 0, machinery 0,
  revolutionary/transformative/game-changing 0.
- Do not touch the chart (`chart-1.py`/`chart-1.png`) — the editor passed it.

## Prove and hand off
Reread the voice guide, apply the additions, then run to `BLOCK: 0`:
```
export PATH="$HOME/.local/bin:$PATH"
/home/user/the-nightly-build/nb check --series the-instruments \
  --repo /home/user/the-nightly-build --library /home/user/library-checkout \
  /home/user/the-nightly-build/.nb-work/the-instruments/energy-per-query/library/the-instruments/energy-per-query.html
```
Write `writer/02/draft-handoff.md` (never overwrite 01): list each comparison
added and where, confirm the editor's edits preserved, the new word count, proof
result, and any warnings left. Return `DONE writer <writer/02/draft-handoff-path>`
after BLOCK: 0, or a REQUEST line if a needed comparison is not in the evidence.
