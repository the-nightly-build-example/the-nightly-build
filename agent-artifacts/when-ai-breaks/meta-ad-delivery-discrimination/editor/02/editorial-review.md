# Editorial review: when-ai-breaks/meta-ad-delivery-discrimination (editor/02)

## Skeptic

Focused confirmation read of the one item round 01 routed: the VRS-audit stat
strip and the "36 paired campaigns" sentence, checked directly against the
primary, Imana, Shen, Heidemann, and Korolova, "External Evaluation of
Discrimination Mitigation Efforts in Meta's Ad Delivery" (FAccT '25,
arXiv:2506.16560), §4.1.1, §4.2.1, and Figure 3, rather than the evidence
record's paraphrase (which itself states the wrong figures — "15 of 18" for
both race and gender at 10%, the same error round 01 caught in the draft).

Reread the paper's own text directly. On the race result at Meta's 10%
compliance threshold: "In the right figure for race, we see variance is more
than 10% without VRS in all 18 cases. VRS reduces variance to less than 10%
in all cases, bringing it down to less than 5% in 15 of the 18 cases." That
is 0/18 passing without VRS and 18/18 passing with VRS at the 10% threshold;
15/18 is the paper's own stricter 5%-threshold figure for race with VRS on,
not a separate pass count the article needs.

The stat strip now reads "18/18 · Race comparisons under Meta's 10%
compliance threshold, system on" and "0/18 · The same race comparisons,
system off." Both numbers, the threshold, and the race-only labeling (no
conflation with the gender comparisons, which the paper reports separately:
15/18 already under 5% variance even *without* VRS) match the primary
exactly. Held.

On the "36 paired campaigns" sentence: the primary's §4.1.1 states the
design as six ad creatives × two demographic attributes × three replicated
audiences = 36 experiments, "the same ad twice: once with and once without
VRS," each pair declared as a housing ad to enable VRS ("all initial
experiments declared ads as housing... employment and credit are evaluated
separately in section 4.2.2"). The article's sentence — "one copy declared a
housing ad (turning VRS on) and one not, across three separately built
audiences" — matches this exactly; it no longer claims the 36 split across
housing, employment, and credit declarations, which the paper does not
support. Held.

Checked the ending's "worked for housing, not yet for employment/credit, at
a reach cost the compliance metric doesn't count" nuance against the same
primary: "while VRS reduces variance according to the legal compliance
metrics for housing ads compared to a case without VRS intervention, fewer
unique users are reached... and the cost of compliance is passed on to
advertisers." The takeaway bookend's "the correction working for housing ads
and not yet working for the employment and credit ads... came at a cost the
compliance metric never counted: it worked partly by showing the ad to fewer
people" states that nuance correctly and un-softened. Holds, and reads as
the article's own sentence, not a lift from the primary's wording.

No other claim was reopened. Round 01's mechanism, timeline, HUD-independence,
author-count, and heading-formula fixes are unchanged in the current file and
were not retested here per the brief's scope.

## Cut

Reread the two changed sentences and their immediate paragraphs (the stat
strip's three labels, the sentence introducing the 36 paired campaigns, and
the following paragraph on employment/credit, which the writer left
untouched) against `spec/slop.md`. No new slop: no empty conclusion,
negative parallelism, unearned punchline, or vague attribution introduced by
either edit. The stat-strip labels are fixed-form furniture fragments,
consistent with the component's use elsewhere in the library. No grammar or
syntax break in either changed sentence; both read as clean, single-purpose
sentences carrying a fact with its denominator and period, matching the
voice guide's instruction to give the delivery study's and settlement's
figures "named denominator, named period, stated once plainly."

No repeated pattern, formula, or edge-sentence problem introduced. Nothing
else in the file changed, so no further cut pass was run.

## Reader

This is a confirmation read, not a fresh Reader pass. The corrected numbers
now support exactly what the ending claims: the fix worked for housing (0/18
to 18/18 at the compliance threshold Meta itself must meet) and not for
employment/credit, and it did so partly by narrowing reach. That is the
"reduced, not fixed" nuance the brief asked me to confirm, and it survives
the correction intact — if anything the corrected 0/18-to-18/18 figure is a
cleaner, more checkable number for the reader than the draft's wrong
"<5/18 to 15/18" was. Round 01's Reader finding — that the piece gives a
causal chain none of the four primaries states alone, and that the prose
sits closer to the voice guide's exemplars than a median summary — stood on
this item resolving correctly, and it now does.

## Edits

None. The correction was sound as delivered; no direct fix was needed in my
remit.

## Required work

None outstanding. No item is routed to the researcher, writer, or
orchestrator.

## Decision

**Approve.** The corrected stat strip and the "36 paired campaigns" sentence
match the Imana et al. (FAccT '25) primary exactly — threshold, the
0/18-to-18/18 with/without-VRS counts, and the race-only labeling — and the
"reduced, not fixed" ending still holds under the corrected figures. Neither
changed sentence introduced new slop or a grammar break. Nothing in my remit
needed a fix, and nothing new needs routing.
