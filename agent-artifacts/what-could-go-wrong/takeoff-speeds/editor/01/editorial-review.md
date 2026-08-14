# Editorial review: what-could-go-wrong/takeoff-speeds (editor/01)

## Skeptic

Thesis: the one thing anyone has actually measured about AI progress — METR's
six-year time-horizon line — is the shared property of both takeoff camps, so it
fuels the fast case and the slow case at once and decides neither, and the smooth
reading is not the safe reading.

The claims it stands on, and how each held:

1. There is a real, measured six-year exponential: METR's 50% task-completion
   time horizon doubling every 207 days (CI 166-240 days), from GPT-2 at ~2s to
   o3 at ~110 min. Checked against the METR abstract and Fig. 1 as cited: the
   three quoted lines are verbatim from the record's `Quote` items, the seven-
   month gloss and the "twelve frontier models, 2019 to 2025" span match, and the
   figure carries the fit. Holds.

2. The fast case rests on analogy (evolution, AlphaGo) and on projection about a
   system that does not exist (recursive self-improvement; AI-2027's 1.5x→3x→10x→
   25x multipliers). The article states this in the authors' own structure and
   then marks the line itself ("Natural selection is not gradient descent, and a
   program that mastered a closed board game is a bet, not a demonstration, about
   open-ended research"). Grounded in the record's Contradictions section. Holds.

3. The continuous case rests on observed smooth scaling (Kaplan's power law over
   "more than seven orders of magnitude"; Chinchilla's "double the data for every
   doubling of model size"; the METR trend). Both scaling quotes are verbatim
   `Quote` items, correctly attributed and cited. Holds.

4. The same line reads both ways and settles nothing: extended forward it reaches
   month-long autonomous work within a decade (AI-2027's runway); METR flags a
   possible recent acceleration (2023-2025 ~20% faster; o3 above trend, p=0.006)
   but rates its own confidence low (seven models). All figures match the record.
   The honest hinge — "fuel for both cases and a verdict for neither" — holds.

5. Continuity is not safety. The piece gives Christiano's own point that a slow
   takeoff may be harder to govern (many capable systems arrive together; aligned
   ones must compete), cited to s1, and explicitly refuses the reassuring reading.
   Holds, and is the round-focus requirement met squarely.

Quotation discipline (the sharpest risk): I checked every quotation mark in the
draft against the record's Quote/Reported labels. Every quoted string is a
verified `Quote` — Christiano's slow-takeoff operational definition, Good's
"intelligence explosion" sentence, the Kaplan power-law line, the Chinchilla
doubling rule, and the three METR lines (metric definition, "doubled every 207
days," GPT-2/o3 span). Every `Reported` item — Yudkowsky's discontinuity argument
and evolution analogy, the 2021 MIRI exchange (chimps/fission/AlphaGo, GDP-is-the-
wrong-meter, Christiano's forecast-discipline demand), Hanson, AI-2027's calendar
and multipliers, and Bostrom's minutes-to-days / decades timescales — is
paraphrased, outside quotation marks, and cited. No fabrication routed; the
constraint is met.

Display text, descriptor by descriptor: headline is the finding the piece
defends. Dek is accurate (207 days ≈ seven months; 2019-2025 ≈ six years; both-
readings claim is the thesis) and clears the negative-parallelism, semicolon-
reversal, suspended-question, and comma-triad dek molds. No person carries a
title/role/affiliation that could be wrong (names only; "and three colleagues"
correctly counts Larsen, Dean, Alexander). Good's date (1965), locator (Sec. 2,
p. 33), Chinchilla 70B-beats-larger, and the AI-2027 author credentials all match
the record.

`data-nb-kind` audit: nine primary (Christiano, Good, Yudkowsky, MIRI, AI-2027,
Hanson, Kaplan, Hoffmann, METR — each the document that owns its claim), one
secondary (s2, the LessWrong reading-group post reporting Bostrom's taxonomy).
Correct: Bostrom's timescales are cited to the secondary summary actually read,
not to the bot-blocked book, and Good's languagelog PDF is primary as the
document itself. Meets the 4-primary / 1-secondary floor with room to spare.

Citations: URLs match the documented sources. I verified the two structurally
notable ones by opening them — Hanson's oddly-formed `/p/30855html` slug does land
on "I Still Don't Get Foom" (2014) and matches the article's paraphrase, and
Good's languagelog PDF resolves as the served 4.1MB document the researcher read.
The figure's `data-nb-url` points to the arXiv PDF page 2 where Fig. 1 sits. The
writer's proof passed with links included (BLOCK: 0), consistent with this.

No break required routing: no central claim collapsed, no number conflicted with
its primary, no evidence was missing.

## Cut

Slop pass, every sentence including display text, furniture, and edges read out
of order. The prose is disciplined; three edges failed and I fixed them directly.

- Source-asset caption carried an interpretive second sentence ("The continuity
  camp reads it as a smooth curve; the fast camp extends the same line past the
  edge of the chart") that duplicated the body's "The same line, claimed by both"
  and violated the rule that a source-asset caption is a short factual cited
  label with interpretation left to prose. Cut it; moved the citation onto the
  factual label.

- "Here the fault line the whole desk cares about becomes concrete" narrated the
  newsroom (self-reference) and dangled for a reader arriving from a link.
  Recast to the piece's own terms: "Here the split between shown and projected
  becomes concrete."

- "Keep alarm and dismissal at the same distance" is lifted almost verbatim from
  the voice guide's instruction to the writer, and lands as a reader-directed
  imperative inside a body that speaks to no one. Prompt leakage plus body-
  address. The symmetry underneath is the article's own and is evidence-backed
  (both the 2027 extrapolation and the smooth-curve confidence are projections
  past measured data), so I rewrote it as reporting: "Alarm and dismissal sit at
  the same distance from the data: the extrapolation to superintelligence by 2027
  is a projection past it, and so is the confidence that the curve stays smooth."

Considered and kept: the section-close "Held at full strength, the fast case is
serious, specific, and honestly hedged" is a triad, but each adjective is earned
by the paragraph (dated multipliers; the stated prediction-not-demand and 5x
band) and the desk requires signalling that serious people hold the case before
the test. "The continuity camp is not answering with faith. It is answering with
a fit" reads as near-strawman but carries the piece's real spine (measured fit vs
unmeasured projection) and introduces the scaling evidence concretely. The table
caption's semicolon binds a tight, deliberate antithesis that is the article's
thesis-point; left as house-allowed rare use. None is publication-blocking.

Negative-parallelism instances ("a bet, not a demonstration"; "a known
quantitative rule, not a lucky architectural leap"; "not about the data ... about
what would count as data") each correct a misconception the piece actually names
(the jump framing, the fact/fact reading), so they stay.

Formula check against the recent-desk notes: the closer does not reuse the
"measured gap is small and the scary version is still an analogy/projection"
shape — it resolves the opener's "jump or curve?" in takeoff's own image (a curve
that may hide a cliff past the edge of the chart, climbed by a machine that does
not yet exist). Headings are built in the subject's nouns, reconstruct the
argument in order, and vary in construction. Dek clears the mold list.

Grammar and punctuation: clean; zero em-dashes; no banned terms; my edits
introduced none.

## Reader

Reading what survives straight through as the paper's declared reader, the one
thing I have that the five sources alone would not give me: the recognition that
the single line anyone has actually measured is the shared property of both
camps — the continuity side's proof of a smooth climb and the fast side's runway
to a self-improving machine — so the only measured evidence in the whole dispute
cannot decide it, and the smooth reading is not the safe one. The sources give
the fast case, the slow case, and the METR measurement separately; none stages
that measurement as the hinge both sides read and settles neither. The draft-
handoff's original-work sentence claims exactly this, and it survives the read:
the article turns the record's passing "cuts both ways" note into the spine of
the piece. The prose sits with the voice-guide exemplars — uncertainty stated in
both directions, the shown/projected line drawn on concrete cases, the reassuring
reading refused — not with a median summary. The headline is the largest claim
and the piece defends it.

## Edits

- Cut the interpretive second sentence from the METR Fig. 1 caption and moved the
  citation onto the remaining factual label.
- Recast "Here the fault line the whole desk cares about becomes concrete" to
  "Here the split between shown and projected becomes concrete" (removed newsroom
  self-reference / dangling referent).
- Recast "Keep alarm and dismissal at the same distance: ... a projection past
  the data ..." to "Alarm and dismissal sit at the same distance from the data:
  ... a projection past it ..." (removed voice-guide leakage and body-directed
  imperative; kept the evidenced symmetry).

## Required work

None. Quotation discipline, the honest hinge, cite-what-you-read labeling, the
source-asset crop, and the data-nb-kind audit all held; the three edges were
mine to fix and are fixed. No researcher or writer item outstanding.

## Decision

approve — the fast case is steelmanned at full strength, the shown-versus-
projected line is drawn in takeoff's own particulars, every quotation is a
verified verbatim item, the METR asset earns its place uncropped, and the three
prose faults were editor-fixable and are fixed.
