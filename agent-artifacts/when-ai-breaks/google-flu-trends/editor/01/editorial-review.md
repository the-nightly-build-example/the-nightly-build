# Editorial review 01 — when-ai-breaks/google-flu-trends

Skeptic: thesis "Google Flu Trends failed not from a bug but because the
fitted relationship between search terms and flu drifted while media
behavior and Google's own search algorithm kept moving underneath it";
tested 4 claims (the ~2x/"100 of 108 weeks" overestimation, the 2009
swine-flu underestimation, the writer's own reconciliation of Google's
spike-detector account with Lazer's algorithm-dynamics account, and the
ARGO comparison in the "defenders" paragraph); broke: the ARGO sentence
mischaracterized whose search data was low-quality.

Cut: 6 sentences/clauses; worst tell: "Lazer, Kennedy, King, and
Vespignani produced the field's definitive post-mortem" — "definitive
post-mortem" is lifted near-verbatim from `commission.md`'s instruction to
the writer ("is the definitive post-mortem; use it as the analytical
spine"), not a description any source makes of itself.

Reader: this gives me a reconciliation neither primary states on its own —
that Google's media-spike account and Lazer's algorithm-dynamics account
describe different stretches of one timeline rather than a dispute the
record can't settle — built from dates and figures each primary supplies
independently. Prose reads close to the voice-guide exemplars (concrete,
stacked, comparable numbers; causal chains one link per sentence); not a
median AI summary.

## Source verification (reopened as opponent, not just checked against evidence.md)

Fetched and grep'd the actual PDFs/pages directly, not just the evidence
record:
- Lazer et al. 2014 (Science, via the dhi.ac.uk mirror cited in
  evidence.md): confirmed verbatim — "more than double the proportion of
  doctor visits," "has missed high for 100 out of 108 weeks starting with
  August 2011," the figure caption's "21 August 2011 to 1 September 2013,"
  "more than 50%" 2011-2012 overshoot, MAE 0.486/0.311/0.232, "86 changes
  in June and July 2012," the June 2011/February 2012 search-feature
  changes, and the media-panic rejection quote. All match the article
  exactly.
- Cook et al. 2011 (PLoS ONE, fetched directly): confirmed the pH1N1 Wave
  1 correlation collapse (0.29 vs. updated 0.95), the ~40->~160 query
  count, the 48%->17% / 8%->69% category-share shift, and the September
  24, 2009 revision date.
- Copeland et al. 2013 (Google's own paper, fetched and grep'd): confirmed
  the exact Jan. 13, 2013 week numbers (CDC 4.52%, GFT 10.56%, "more than
  twice"), the 6.04-point peak, the 1.13-point/0.30-point 2008-2012
  baseline-error figures, the spike-detector "3 to 7 days" quote — and
  incidentally, this Google paper itself cites "Nature 2/13/13, When
  Google got Flu Wrong," independently corroborating the article's Butler
  citation beyond what evidence.md alone captured.
- Google's 2015 shutdown post (fetched directly): confirmed the August 20,
  2015 date, the three named data recipients, and the absence of the
  words "overestimate," "error," or "wrong."

No overestimation or swine-flu figure needed correction. The commission's
core ~2x / "100 of 108 weeks" / swine-flu-underestimation claims all trace
cleanly to their owning primaries with the exact denominators and periods
the article states.

## Direct edits made

1. **Miscitation fixed.** The September 24, 2009 revision sentence (query
   count 40->160, symptom-share 8%->69%) was cited to source 2 (Ginsberg
   2009, published seven months *before* that revision existed). Both
   facts belong to Cook 2011 (source 3), already cited correctly one
   sentence earlier and in the table caption. Changed `href="#s2">2` to
   `href="#s3">3`.
2. **Factual correction.** The ARGO paragraph claimed ARGO was built
   "using the same low-quality public search data Google Flu Trends had
   relied on." This inverts the record: GFT's original model was built on
   Google's own internal search logs (Ginsberg 2009's "50 million of the
   most common search queries," mined from Google's raw logs); ARGO used
   the *public* Google Trends/Correlate interface, which the evidence
   record notes explicitly as *lower*-quality than what GFT's own team had
   access to. Rewrote to "using lower-quality public search data than
   Google Flu Trends had ever needed," which correctly makes the
   "defenders" point *stronger* (worse data, still won), not the reverse.
3. **Prompt leakage cut.** "Lazer, Kennedy, King, and Vespignani produced
   the field's definitive post-mortem" echoed `commission.md`'s exact
   framing for the writer ("is the definitive post-mortem... the
   analytical spine"), an internal editorial judgment about the source's
   role in this assignment, not a reported fact. Cut to "published their
   critique in Science."
4. **Hedged-contrast trim (three cuts, one piece).** The floor caps earned
   "not X, but Y" constructions at one or two per piece; this draft had
   four, two of them stacked in the same takeaway paragraph. Kept the two
   that carry real information found nowhere else (the underestimate ->
   overestimate direction flip; the takeaway's "not 'is the fit still
   correlated' but 'does this input still mean what it meant'," which is
   the article's stated required contribution). Cut: "not because they
   are sick" (redundant — the next sentence already makes the same point:
   "counted that concern as new cases"); "not one lasting an entire
   season" (converted to a plain second sentence, "An entire season was a
   different problem"); and "not to distrust search data, or big data
   generally. It is" (redundant with the ARGO paragraph's "not inherently
   hopeless," already established).

Ran `./nb check ... --no-check-links` after each round of edits:
`BLOCK: 0`, `verdict: PUBLISHABLE`, same single warning throughout.

## Source-count warning (7 vs. floor of 8) — left standing, not escalated

Checked every central claim against the commission's per-kind floors
(primary >=4, secondary >=1) and against whether any claim depends on a
source that isn't independently strong. Primary count is 6, secondary is
1; both clear their floors. The ~2x overestimation is double-sourced
(Google's own Copeland et al. and the outside Lazer paper, independently).
The swine-flu miss is likewise corroborated by both Cook (Google) and
Lazer (outside). The one source with a thin footing — Declan Butler's
paywalled Nature News piece — is cited only for its confirmed title and
date, a fact independently confirmed a second way: Copeland et al.'s own
paper cites the identical Nature piece by name and date. No central claim
rests on a single fragile source. Per the review brief's instruction, I am
not requesting an 8th source to clear a count that reflects no actual
evidentiary gap.

## Visual evidence

Considered requesting the Lazer two-panel chart or Ginsberg's Figure 1
(evidence.md flags both, with crop guidance already worked out) as a
source asset. Declined to request one: every central figure the charts
would show (the 10.56%/4.52% comparison, the 100-of-108-weeks duration,
the MAE comparison) is already delivered in prose with an exact number and
an anchoring comparison, meeting the house Numbers standard on its own.
Nothing in the piece is harder to follow without a chart. This is a
missed opportunity worth a future writer's discretion, not a publication
blocker.

## Minor housekeeping (non-blocking)

The cuts above are net negative by roughly 15-20 words; the declared
`"words": 2199` in `nb-meta` (and the sources-section byline) is now
slightly stale. This does not move the article out of its 1200-2200 band,
does not change the displayed "10 min read," and the proof's own recount
did not flag a mismatch. Not requesting a rewrite for this; whoever next
touches this file in a writer invocation should let `./nb check` retrue
`words` in the normal course of re-running the proof.

## Required work by owner

None outstanding. No REQUEST to researcher (no central claim lacks
independent support) or writer (no missing prose, structure, markup,
asset, or proof failure) is needed.

## Final decision

Publishable as edited. No redraft required.
