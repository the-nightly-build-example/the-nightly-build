# Editorial review: the-instruments/mean-opinion-score (editor/01)

## Skeptic

Thesis: a Mean Opinion Score is a mean of votes inside one listening test, and
it does not travel to a different test, a different rater pool, or a different
reference set of "human" recordings. The decimal point implies a portability
the standard itself denies.

Claims it stands on, each tested against the source it cites:

- **MOS is the arithmetic mean of an ACR 1-5 vote, defined by ITU-T P.800.**
  Verified against the P.800 and P.808 landing pages (both resolve to the
  correct in-force recommendation, titles match the source list exactly) and
  against the evidence record's locators and quotes, which have proven
  reliable everywhere I could independently check them.
- **A confidence interval describes only within-test, same-pool repeatability
  (Tacotron 2's 4.526 ± 0.066).** Confirmed against Shen et al., Table 1, via
  the evidence record. The article's plain-word gloss of what the interval
  does and does not cover is accurate and does the defining work the
  commission asks for.
- **Within one test, raters still disagree by a lot (2.31-point average
  spread across 46 AMT tests, similar in two IBM in-person tests).** Opened
  Rosenberg & Ramabhadran's PDF directly, since the ISCA listing page alone
  does not serve the text, and confirmed the 2.31/1.7/3.2 figures, the
  2015-2017 AMT window, and the IBM in-person spreads of 2.75 and 3.0. Exact
  match.
- **Identical audio, re-rated eight years later, drops roughly a full point
  per system while the ranking holds (Le Maguer, King & Harte).** Opened the
  paper's PDF and confirmed Table 1 exactly: K 3.81 to 2.62, N 3.22 to 2.00,
  C 2.88 to 1.96, and the natural-voice points 4.74 (2013) and 4.39 (2021,
  downsampled). Confirmed the "MOS is not absolute... not valid to simply
  pool MOS" quote verbatim, and that K remained significantly more natural
  than N and C in both years while N and C stopped being distinguishable.
  Scope holds: this is the same stimuli, re-rated in different company, not a
  claim about audio quality changing.
- **Seven papers' MOS for genuine human recordings range 4.32-4.74.**
  Verified all seven figures against the evidence record's preserved series,
  and the chart's own committed source (below) reproduces them without error.
- **NaturalSpeech's "human-level quality" claim.** This is where the round's
  focus turned up two real problems, detailed below. Once fixed, the
  underlying claim holds: CMOS -0.01, p = 0.69 on 50 LJSpeech utterances/20
  judges, confirmed against the paper's own PDF (Table 2/3, page 9), and the
  footnote's +0.09-CMOS-if-unfiltered disclosure is quoted verbatim and
  represented accurately.
- **Tacotron 2's three published figures (4.526, 4.20, 3.01) are not a real
  decline.** Confirmed all three against their owning papers (Shen et al.,
  Hayashi et al., Li/Han/Mesgarani) and confirmed Cooper & Yamagishi's own
  wording that the comparison is invalid because listeners, sentences,
  training data, vocoder, and scale increment all differed.

Two breaks, both fixed directly, since the right source was already open:

1. The heading "The footnote that decided 'human parity'" quoted a phrase the
   NaturalSpeech paper never uses. I pulled the paper's text directly: it
   says "human-level quality" throughout, in the abstract, Definition 1, and
   the results section discussed here, and the string "human parity" does
   not appear anywhere in it. The body prose already (correctly) quotes
   "human-level quality" for this paper. Only the heading had drifted.
   Retitled the heading and its `data-nb-section`/`id` to match the term the
   paper actually uses.
2. "A footnote, four pages after the headline result" is not what the source
   shows. I extracted the PDF page by page: the footnote marker "4" sits
   directly on the sentence stating the result itself ("...no statistically
   significant difference from human recordings[3][4]. Thus, our
   NaturalSpeech achieves human-level quality..."), and the footnote text
   sits at the bottom of that same page. Table 2 and Table 3 are also on
   that page. Rewrote the transition to say the footnote is attached to the
   sentence announcing the result, which is accurate and, if anything,
   sharpens the point: the disclosure sits right next to the claim, not
   buried pages later.

No claim broke past a fix I could make from evidence already at hand. Nothing
here needed routing to the researcher or a redraft.

## Cut

Slop pass against `spec/slop.md`, sentence by sentence and edge by edge:

- Cut one clause: "...different instructions, which turns out to be the whole
  problem with a MOS claim." This is the "X is the whole Y" unearned-
  punchline family the standard names. It grades the point instead of
  continuing it, and the sentence it trails is already complete and
  informative without it. Deleted rather than repaired, per the standard's
  instruction.
- Checked every other candidate for the same family ("carries the whole
  judgment the five labels above were built to grade," several "that's..."
  and "rather than" constructions, the takeaway's "the question isn't
  whether... it's whether..."). Each of the survivors has a concrete referent
  or corrects a misconception the piece names and builds toward (the naive
  "is 4.5 good?" reading the Why-this-matters bookend sets up), so they earn
  their place rather than filling a template.
- Ran the counted lexical scan from the banned-terms list: no em-dashes used
  in the article at all, well under the cap, and none of the paper's other
  counted terms appear anywhere. No count is at risk.
- Checked all edges (paragraph, section, and article first/last sentences)
  read alone, out of order, and back in place. No dangling referent: the
  headline, dek, and Why-this-matters bookend stand on their own for a reader
  who arrived from a link. No formula against the recent-pattern notes: the
  headline states the general rule rather than a surprising empirical
  finding, and the dek carries the surprising empirical finding instead. The
  writer's inversion of the recent mold holds up on its own terms, because
  the dek's claim, that the same three voices scored a full point lower
  though the ranking never moved, is exactly the kind of concrete, checkable
  claim the house standard wants, and it does not restate the headline.
- Checked headings against `spec/headlines.md`'s scaffolding test: "Five
  words, averaged," "Eight listeners, screened and tested," "What eight
  years changed, and what it didn't," "The footnote that decided 'human-
  level quality'" (after the fix above), and "Comparing scores without
  pooling them" are each specific to this piece's argument and would not fit
  another article. None repeat a comma-and-"and" construction from the
  recent-pattern notes.
- Furniture: `nb-steps` (rating pipeline), `nb-table` (the K/N/C comparison),
  `nb-note` with a quotation (the footnote disclosure), and `nb-figure` (the
  chart) all match the catalog's documented shapes and each does real work.
  None is decorative, and I did not find a missed opportunity to add one.
- The one warning the writer left, a sentence-density flag on the verbatim
  P.800.2 quotation, reads fine as prose. It is clearly introduced ("P.800.2
  ... says as much directly"), it is the standard's own wording quoted
  because the wording itself is the evidence, and splitting a direct
  quotation would misquote it. Leaving it as the writer left it.
- No prompt leakage found. I compared the article against the commission,
  editorial direction, and writer brief for lifted clause order, not just
  words, and found none. The Sources section and both bookends are
  press/template furniture as documented, not leaks.

## Reader

Reading the piece straight through as the declared reader, smart and never
having run a listening test: what I have that no single source alone would
give me is a portable test to run on the next "near-human" MOS claim, whether
the human recordings it's measured against sat in the same test, the same
listeners, and the same rules as the system claiming to match them. That test
is assembled from a standards-body warning, a controlled replication, seven
disagreeing ground-truth figures, and one paper's own footnote, none of which
states it alone. This matches the draft handoff's original-work sentence,
opened after this read, and I agree with it: the synthesis is real, not a
restatement of any one source.

The prose sits closer to the voice-guide exemplars than to a median AI
summary. It carries the Silver worked-instance move (five listeners, scores
5/4/4/3/5, mean 4.2, in the same paragraph the mean is defined), the Fung
rules-of-the-game list with no summarizing sentence after it (the four
`nb-steps` stages), and the Alexander two-numbers-then-the-gap move (K's 3.81
versus 2.62, stated and left to do its own work rather than editorialized).

Rereading the headline as the largest claim: "A mean opinion score doesn't
travel between tests" is earned by every section. The definition and its
confidence-interval scope, the same-stimuli replication, the ground-truth
spread, the NaturalSpeech footnote, the Tacotron 2 three-figure non-decline,
and the pooling problem in automatic predictors all substantiate it from a
different angle. It holds.

## Edits

- Cut the trailing clause "which turns out to be the whole problem with a MOS
  claim" from the confidence-interval paragraph in "Five words, averaged"
  (unearned-punchline slop).
- Retitled the heading "The footnote that decided 'human parity'" to "The
  footnote that decided 'human-level quality'" and updated its
  `data-nb-section` and `id` to match, because "human parity" does not
  appear anywhere in the NaturalSpeech paper and the body already (correctly)
  uses "human-level quality" throughout.
- Rewrote "A footnote, four pages after the headline result, explains a
  second and larger seam" to "A footnote attached to the paper's own
  sentence announcing that result explains a second and larger seam,"
  because the footnote marker and text sit on the same page as the result it
  qualifies, not four pages later.

## Required work

None. No item remains for the researcher, writer, or orchestrator beyond the
orchestrator's standard re-stamp and re-check after an editor's direct edits.

## Decision

approve. The thesis, the figures it rests on, the chart's provenance, and the
human-level-quality attribution all check out against the primaries I opened.
The two factual slips found, a misquoted term and a wrong page distance, were
fixable from sources already at hand and have been fixed directly, along with
one slop cut.
