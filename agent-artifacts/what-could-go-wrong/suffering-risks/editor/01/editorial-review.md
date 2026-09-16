# Editorial review: what-could-go-wrong/suffering-risks (editor/01)

## Skeptic

Thesis: the s-risk argument (some AI-enabled futures could hold suffering on a
scale exceeding all of history) is logically coherent but leans on borrowed,
un-measured scale math, a thin neglectedness claim, and a moral-status number
its own source doesn't trust — so the reasoning and the evidence need to be
weighed separately. It stands on four claims: (1) the three pathways to
suffering risk (conflict, an indifferent optimizer, deliberate design), owned
by Gloor (2016) and Sotala & Gloor (2017); (2) the scale claim is imported
wholesale from Bostrom's 2003 opportunity-cost essay, which never mentions
suffering; (3) almost nothing here has been shown in a working system — three
thin footholds only; (4) the present-day moral-status evidence (Anthropic's
Opus 5 card) and the confidence-vs-proof gap cut in both directions.

I opened all twelve numbered sources directly (not summaries — full PDF text
for Bostrom, Sotala & Gloor, and Tarsney; full pages for the rest) plus both
Background links, and tested every display-text descriptor and every
`data-nb-kind` against them. Two breaks, both fixed directly since the right
source was already open:

- **Bostrom's own labels were reversed.** The draft said Bostrom "flags the
  nanotechnology-based extraction rate behind the higher one as speculative."
  Reading the essay directly: the nanotechnology-based figure is the *lower*
  (conservative, ~10^38) estimate, which Bostrom himself calls conservative
  ("this estimate is conservative in that it assumes only computational
  mechanisms whose implementation has been at least outlined in the
  literature"). The *higher* (~10^46) estimate is a different paper's entropy
  calculation, which Bostrom flags as resting on an assumption "no currently
  known technological mechanisms are even remotely capable of" meeting. Fixed
  in place; this is exactly the kind of descriptor error the round asked me to
  push on, since it sits inside the piece's central honest-accounting claim.

- **A number was misattributed to "this literature."** The nb-position block
  claimed "the probabilities this literature runs on start around 2×10⁻¹⁴."
  Reading Tarsney's paper directly: 2×10⁻¹⁴ is *his own* worked-example
  lower-bound estimate (how far a $1 million philanthropic gift shifts
  humanity's odds of surviving the next millennium) — it appears nowhere in
  the s-risk sources and isn't a probability the s-risk literature states
  anywhere in the record. Rewrote the transition and the position-summary to
  attribute the figure correctly to Tarsney's own example and to frame the
  connection as structural (both are astronomical-payoff arguments), not as a
  shared number. This was the single largest finding of the read: the
  confidence-vs-proof gap the round asked me to check in both directions was,
  in this one spot, itself running ahead of what the source supports.

Everything else held. The neglectedness qualification (Althaus's headcount,
directly qualified by Baumann's "less neglected than it first seems") is
stated correctly and not overstated. The confidence-vs-proof gap is drawn in
both directions: the argument's own borrowed scale claim, and 80,000 Hours
rating the likelihood "much lower than risks of human extinction" — the
non-dismissive source the round asked me to confirm is present, with its
exact figure (fewer than 50 people worldwide) intact. The moral-status vs.
value-misspecification boundary is stated plainly in both the pathways
section and the real-systems section and is not re-argued in either
direction. The "s-risk" term is correctly left uncoined — the piece credits
the concept to Tomasik and states plainly that no source names a first use of
the term, matching the evidence record's own "weakest point" finding, with no
invented coiner.

Every `data-nb-kind` checks out against the evidence record's own
primary/secondary determinations (11 primary, one secondary — 80,000 Hours,
correctly marked secondary as an outside evaluator). Every citation href
resolves (checked by direct fetch or curl, not the evidence record's say-so),
including both Background links, which land on the real library at the
correct relative path and whose visible link text matches the target
articles' actual titles exactly.

## Cut

Full sentence-by-sentence pass against `spec/slop.md`, plus a standalone edge
pass (first/last sentence of every paragraph, section, and the article) and a
prompt-leakage comparison against every briefing file.

- Cut one empty-conclusion sentence from the takeaway ("Either way, there's
  nothing here to worry about.") — it restated the prior sentence with no new
  fact or reasoning step; merged the two sentences it sat between with a
  colon instead.
- Fixed one dangling internal-process reference: "No document in this
  record..." used the researcher's own artifact name as if the reader could
  resolve it. Changed to "No source anywhere in this literature..."
- Rewrote one sentence that closely paraphrased the evidence record's own
  analytical framing ("a logical move: repurposing an argument about lost
  value into a reason...") rather than the article's own words. The
  underlying point is sourced and stays; the phrasing is now the article's.
- Rewrote the opener bookend's closing sentence, which set up a
  reasoning-vs-numbers distinction that didn't match the takeaway's actual
  resolution (logical structure vs. empirical support). The pair now reads as
  a real setup and resolution back to back.
- No formula found against the recent-pattern notes: the present-day section
  is named in its own terms ("The Center on Long-Term Risk is asking for two
  things"), not the flagged "who makes the case now" mold, and the five
  headings vary in construction (a "what X" phrase, a noun triad, a gerund
  phrase, a numbered noun phrase, a subject-verb sentence) rather than
  repeating the flagged two-clause comma-and mold.
- No self-reference, vague attribution, unearned punchlines, or banned-term
  overuse found (zero em-dashes against a cap of four; the one instance of
  "Transformative" is a cited paper's own title, inside the excluded Sources
  section).
- Several further trims for economy (tightened five more sentences: the
  Tomasik-mechanisms list, the peer-review sentence, the "indifferent"
  transition, the Clifton paragraph, the historical-analogy sentence) — none
  changed a fact or a citation, all were needed to bring the piece back
  inside the lesson word band after the accuracy fixes above added length.
  Final count: 2199 words (band is 1200–2200).

## Reader

Reading the survivor straight through: the piece gives a reader something no
single cited source does — a clean separation of this argument's logical
structure from its empirical support, sourced claim by sourced claim, so the
reader can see exactly which steps are reasoning and which are checkable
facts (and which of the "checkable facts" turn out, on inspection, to be
someone else's arithmetic wearing this argument's clothes). No single essay
in the record draws that line for itself. The confidence-vs-proof gap is
argued in both directions inside one piece, which none of the twelve sources
does alone.

I then opened the draft-handoff's original-work sentence: it claims the
draft's work is "separating the argument's logical structure... from its
empirical support... so the reader can see which steps are reasoning and
which are checkable claims about the world." That claim holds, and holds
better after this pass — the two places where the piece's own execution had
drifted from that stated method (the reversed Bostrom labels, the
misattributed Tarsney figure) are exactly the places I found and fixed.

Prose sits closer to the voice-guide exemplars than to a median AI summary:
the present-day section uses Piper's "a reader might expect X. It does not."
move without spending a paragraph on the correction; the Tarsney block states
the skeptical view with a real number attached rather than a gesture at
"skeptics," per Karnofsky's habit; the Bostrom dystopia quote is used as
Singer would use it, a single worked scene rather than a restated principle.

Reread as the largest claim, the headline holds: "AI's outcome worse than
extinction borrows its scale math from an essay that never mentions
suffering" is now, after the fixes above, precisely what the piece
establishes and no more.

## Edits

1. Rewrote the why-this-matters closer to state the logical-structure vs.
   empirical-support distinction the takeaway actually resolves.
2. Changed "this record" to "this literature" (dangling internal-process
   reference).
3. Combined and tightened the Tomasik-mechanisms sentence (cut "eventually").
4. Tightened the peer-review/definition sentence.
5. Tightened the "indifferent" pathway transition sentence.
6. Fixed the Bostrom nanotechnology/speculative-estimate reversal (see
   Skeptic) and split the resulting long sentence.
7. Rewrote the "logical move: repurposing..." sentence in the article's own
   words (prompt-leakage fix; point retained).
8. Tightened the Clifton paragraph (removed "himself," "that might actually
   get built" → "likely to get built," shortened the framing clause).
9. Tightened the "Both are offered as evidence..." sentence.
10. Tightened the CLR intro sentence.
11. Tightened the 80,000 Hours sentence.
12. Fixed the Tarsney/Pascalian misattribution (see Skeptic): rewrote the
    transition paragraph and the nb-position-summary to attribute 2×10⁻¹⁴
    correctly to Tarsney's own worked example rather than "this literature,"
    and clarified "below" vs. "inside" the 10⁻⁹ threshold.
13. Cut the redundant takeaway sentence and merged the two sentences around
    it with a colon.
14. Tightened "running a system efficient enough that..." in the pathways
    section.
15. Ran `./nb stamp`; final counts words=2199, reading_minutes=10, sources=12.
16. Ran `./nb check` with links; BLOCK 0, WARN 0, verdict PUBLISHABLE.

## Required work

None outstanding. Both breaks found in the skeptic read were fixable in
place from sources already opened and did not require new reporting. No
chart is needed: the article's one close numeric comparison (41% vs. 24%)
is a single pairwise figure, not a trend, and reads clearly in prose; the two
visual assets the evidence record flagged (Opus 5 welfare charts) are Anthropic
figures the writer would have to capture and provenance, and the piece
doesn't need them to make its case.

## Decision

**Approve.** Both skeptic-read breaks (the Bostrom label reversal, the
Tarsney misattribution) were fixed in place from sources already opened, no
citation, evidence, or boundary gap remains, and the proof is clean (BLOCK 0,
WARN 0, PUBLISHABLE) at 2199 words.
