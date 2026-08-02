# Editorial review: the-evidence/alphago (round 01)

## Skeptic

Skeptic: thesis "AlphaGo's Nature paper never mentions Lee Sedol, and the system
it does report on beat a European champion trained first on human games, not a
world champion or a system that learned from nothing"; tested naming discipline
(AlphaGo Fan/Lee/Zero), the two retired myths, the DeepSeek-R1 present-day note,
every headline figure (29.4M/160,000; 99.8% = 494/495; Fan Hui 5-0, Oct 2015;
Lee Sedol 4-1, Mar 2016; Zero 100-0 vs AlphaGo Lee; the Elo ladder 3,144/3,739/
4,858/5,185), and all six `data-nb-kind` labels; broke: none of the central
claims. Found three small, fixable defects: (1) the dek's "Its one reported
result is a 5-0 win over Fan Hui" is literally false — the 2016 paper also
reports a 99.8% tournament win rate against other Go programs — so "result"
overclaimed uniqueness the paper doesn't have; fixed to "Its one human match."
(2) A citation for source 4 (Google's announcement blog) was attached to "Go
crowns no single world champion," a claim that source doesn't establish (it
only avoids the term); reattached the citation to the quoted phrase the source
actually supports ("the top Go player of the past decade") and left the
world-champion aside uncited as incidental context, not an argument-bearing
claim. (3) "The lab that cites AlphaGo most explicitly in 2025" claimed a
superlative across all 2025 discourse that the evidence record explicitly
disclaims ("I did not attempt an exhaustive census of all such citations");
cut "most explicitly." Recomputed every arithmetic aside in the piece (160,000
games ÷ 365 ≈ 440 years; 4.9M self-play games over 72 hours ≈ 19/second) and
both check out. The naming discipline the brief worried about — AlphaGo Fan vs.
AlphaGo Lee vs. AlphaGo Zero, and which one played which 100-0/5-0/4-1 match —
holds in every sentence, the stat strip, the chart, and the ledger table.

## Cut

Cut: 1 sentence-internal fix (semicolon spliced two independent clauses in the
Background reading row for the Bitter Lesson link; split into two sentences,
since they weren't tightly enough bound to earn a rare semicolon over a
period); worst tell: the unmoored citation on "Go crowns no single world
champion" (a real miscitation, not just a style note — described above). No
stock revelation frames, no signposting, no prompt leakage against the writer
brief, no banned terms, no em-dashes, and no repeated dek/headline/heading
mold from the voice guide's "do not reuse" list turned up. Furniture (stat
strip, table, chart figure, bookends) all have a clear communicative purpose
and none reads as filler.

## Reader

Reader: this gives me a working ledger for a fact I already half-knew — which
of the "AlphaGo beat the world champion" and "AlphaGo learned from nothing"
claims each specific document (2016 paper, Lee Sedol match record, 2017 Zero
paper) actually supports, built by cross-reading two Nature papers against
three independent match accounts, a synthesis that exists nowhere in any one
cited source. That matches the draft-handoff's stated original-work sentence
(the ledger table plus its resolution in the takeaway) and it is visibly the
spine of the article, not a decoration. Prose reads close to the voice-guide
exemplars (Karpathy, Olah): concrete case before term (MCTS staged from one
board position before the name arrives), arithmetic done inline, one "not X,
it is Y" reserved for the takeaway as instructed. The headline retested as the
largest claim holds: the 2016 Nature paper's text, read start to finish, does
not contain "Lee Sedol."

## Chart

`chart-1.png` inspected as a rendered image and against its committed
`chart-1.py` provenance. Numbers match Silver et al. 2017 p. 12 exactly:
AlphaGo Fan 3,144, AlphaGo Lee 3,739, AlphaGo Master 4,858, AlphaGo Zero 5,185,
same tournament, same 2-hour time controls — no cherry-picking across
different conditions. The line-chart choice (over a bar chart) is honest: the
y-axis is explicitly labeled "interval scale, no true zero," the axis starts
at 3,000 rather than 0, and the four systems are ordered chronologically
(Fan → Lee → Master → Zero), matching the prose's own sequence. The caption
states only facts the chart shows (each version rated higher than the last;
the last used no human data) with no unsupported interpretation, and it
carries the citation per the furniture spec. No recrop or correction needed.

## Edits made directly in the article

1. Dek (both the `nb-meta` JSON and the `<p class="nb-dekline">`): "Its one
   reported result is a 5-0 win over Fan Hui" → "Its one human match is a 5-0
   win over Fan Hui" (the paper reports other results too; only the human
   match is singular).
2. Orientation section: moved the citation for source 4 off "Go crowns no
   single world champion" and onto the quoted phrase it actually supports
   ("the top Go player of the past decade").
3. AlphaGo Zero section, closing sentence of the DeepSeek-R1 paragraph: cut
   "most explicitly" (unsupported superlative against an evidence record that
   disclaims an exhaustive census).
4. Background reading row (Bitter Lesson link): semicolon splice → period.
5. `nb-meta`: `words` 2174 → 2172 to reflect the two-word cut above;
   `reading_minutes` unchanged (10, no rounding change at this word count).

## Required work by owner

None. No claim, source, asset, or structural issue survived that needs the
writer or researcher — all four defects found were citation-attachment or
word-choice precision, fixed surgically in place.

## Decision

Publishable as edited. No redraft required.
