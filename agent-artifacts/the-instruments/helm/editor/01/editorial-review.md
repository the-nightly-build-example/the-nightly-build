# Editorial review: the-instruments/helm (editor/01)

## Correct

Thesis, read from the draft alone: a HELM leaderboard rank is a mean win rate
computed from a grid of per-scenario, per-metric scores, so it can say nothing
the grid does not, and the same grid yields a different order under other
defensible choices about which axis, which scenarios, and which models count.
The claims under it: (1) the seven metrics disagree, and the axes that reorder
the models are toxicity, bias, and calibration, not the accuracy-correlated
robustness and fairness; (2) the leader also moves with the comparison set, the
tie rule, and the sample size; (3) CRFM itself walked the number back twice and
dropped mean win rate in 2025 for exactly two of these failures.

I tried to break each. The one I most wanted to keep is the reorder case, and
it holds on the right axis: the piece states plainly that accuracy, robustness,
and fairness are "extremely strongly correlated," that dropping robustness or
fairness therefore does not scramble the order, and that this correlation is
CRFM's own reason for dropping them from HELM Lite. It builds the reorder on
toxicity, bias, and calibration, on the comparison set, and on HELM's two method
changes, not on dropping robustness. That is the correction the evidence record
flagged, and the draft got it right.

Checked every figure against the record: 30 models, 42 scenarios (16 core + 26
targeted), seven metrics measured "about seven times in eight" (87.5%), 5-shot
fixed across instances with 3 seeds, text-davinci-002 winning accuracy
comparisons more than nine times in ten, the OpenBookQA/HellaSwag calibration
reversal, HELM Lite at 30 models and 10 scenarios with one seed, the ties fix,
the +/-5 positions at 10 examples per scenario (x400 compute), and the March
2025 switch to mean score. All match. The two verbatim quotes carrying the
argument — the mean-win-rate definition (s3) and the two-reason abandonment
statement (s8) — match the record word for word, and the comparison-set quote,
the "extremely strongly correlated" phrase, the "reductive" / "useful practical
tools" pair, and the "contingent on how we chose to measure" caveat all check
out. Mean win rate is not overstated: the piece keeps it as CRFM's own primary
admission, not as a claim that the rank is worthless.

One break, and I fixed it. The accuracy-subfigure citation in the mean-win-rate
section pointed at `#page=50` while the figure caption, the axis-reorder
citation, the evidence record, and the writer's own capture all place Figure 26
on page 51. A reader clicking the first link would land on the wrong page. I
moved it to `#page=51` so both references to Figure 26 land on the figure.

Checked the headline, dek, and subheads against what they own. The headline
generalizes "HELM Capabilities dropped mean win rate" to "HELM's team stopped
ranking models by mean win rate"; the body is careful that HELM Classic still
ranks by it while Capabilities does not, so the headline is a defensible summary
of the team's decision and the body carries the nuance. Not a correctness fault.

Figure 26 asset: the crop shows the six per-metric rankings the prose names, with
model labels and the 0.0-1.0 scale intact. text-davinci-002 leads accuracy,
robustness, and fairness; T0pp (11B) tops the toxicity panel and sits near the
bottom of the bias panel; davinci (175B) is near the bottom of toxicity and high
on bias. Caption is a factual, cited label; alt text is accurate and useful. It
carries the model swap the prose describes.

The writer's open question (which metric set feeds the Classic headline column,
unread because the board is JS-rendered) is non-blocking, and the prose does not
assert which metrics enter that column. Confirmed.

## Reads well

Cut four things. "Here is the whole of the case that follows" opened the thesis
paragraph and narrates the piece's own structure ("what follows" is a
self-reference tell); the paragraph is plainly the thesis without it. "The rest
of this lesson is what that choice costs," "each time in the direction this
lesson has been tracing," and "the two failures this lesson has shown" each make
the body speak about the lesson, which the template reserves for the two
bookends; I rewrote the last two around the argument's own nouns ("moving away
from the single number," "both have already appeared above") and dropped the
first, since the section heading already carries the reader forward. "This is
worth saying plainly, because ..." advertised the writer's care rather than
saying anything checkable, so it went and the sentence now opens on the claim.

Nothing came in from the briefing or the exemplars: the register is the guide's
plain-and-exact Luu/Gladwell voice, and the worked-example second person ("take
another model ... give the point to whichever scored better") is the guide's own
"recompute the point without you," not slop. No formula echo of the recent
record: the piece frames HELM as aggregation hiding disagreement, not as another
"the number moves when the thing doesn't" instability piece, and the tie-fix and
sampling notes are subordinated as procedural choices rather than made the point.
The dek is one sentence with a stance and no number-then-reversal, no comma
triad, no semicolon reversal.

One heading, "Change the axis and the same models move," was a clause-and-clause
construction; I recast it as "Each axis reorders the same models," which keeps
the surprise (same models, different order) and reads as a step in the argument.

## The experience

Read top to bottom on the page, the lesson builds cleanly: grid, then the one
column laid over it, then the column moving as you change the axis, the
comparison set, and the method. Figure 26 is the right component and earns its
place — it lets the reader watch the same 30 models reorder across metrics
instead of taking it on the prose's word, and it is the piece's central
evidence. No component drags or is missing; a table would only restate what the
figure already shows.

What it gives beyond the sources: it reads HELM's scattered admissions — the Lite
correlation note, the seed cut, the Capabilities switch — as one continuous
retreat from a single choice-dependent number, and pins that retreat to the
paper's own Figure 26, so a reader leaves able to ask "which board, which metric,
which models" of any "#1 on HELM" claim and recompute why the answer changes.
That is more than the sources do apart, and it matches the writer's stated
original-work sentence.

## Edits

- Fig 26 accuracy-subfigure citation: `#page=50` -> `#page=51`, so the href lands on the figure.
- Cut "Here is the whole of the case that follows." (self-narration) from the mean-win-rate thesis paragraph.
- Cut "The rest of this lesson is what that choice costs." (body self-reference) from the same paragraph.
- Heading "Change the axis and the same models move" -> "Each axis reorders the same models" (clause-and-clause construction).
- Cut "This is worth saying plainly, because" (performed carefulness) in the axis-reorder section.
- "each time in the direction this lesson has been tracing" -> "each time moving away from the single number" (body self-reference).
- "they are the two failures this lesson has shown" -> "both have already appeared above" (body self-reference).

## Decision

approve — the argument is correct and rests on the right axis, and every
remaining issue was a fix I could make from the record and this checkout. Left
at BLOCK: 0, WARN: 0 (stamped words=1910). No writer round is owed.
