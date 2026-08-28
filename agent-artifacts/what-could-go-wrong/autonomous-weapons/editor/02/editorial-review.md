# Editorial review: what-could-go-wrong/autonomous-weapons (editor/02)

## Skeptic

This is a revision read against two required repairs from editor/01 and
researcher/02: the unsourced Harpy "since the 1990s" fielding claim, and
Russell's mislabeled role. I did not re-litigate the four claims the thesis
rests on, already tested in editor/01 — I pushed only on the changed
sentences.

**Harpy date.** Grepped every "1990s"/"1980s"/"1999"/"decades" occurrence in
the printed HTML (ten hits) and checked each against researcher/02's
Jamestown/Shichor finding (source 13): dek, dekline, the why-this-matters
bookend, both body sentences in what-real-systems-do, the holds-up-grid
bullet, the-fight-now's closing paragraph, and the takeaway. Every instance
now reads as an export/sale claim tied to the mid-1990s Sino-Israeli Harpy
deal, never a bare fielding-year claim. No instance of "since the 1990s"
standing alone survives, and no "late 1980s"/"1989"/"first tested" origin
claim survives either — the article dropped that thread entirely rather than
capping it, which the brief allowed. I opened the Jamestown page directly
(https://jamestown.org/program/the-u-s-factor-in-israels-military-relations-with-china/)
and confirmed both load-bearing quotes verbatim: "the Sino-Israeli Harpy UAV
deal, negotiated in the mid-1990s" and "by 1999, Israel had reportedly sold
China about one hundred Harpy UAVs." The one imprecise-sounding phrase, "two
decades before the 2015 letter" (what-real-systems-do), holds up: mid-1990s
(~1995) to 2015 is 20 years on the negotiation date, squarely inside the
16-to-26-year range the evidence record itself computes. Not an overclaim,
left alone.

**Russell's role.** Grepped for "drafter" — zero hits. First mention now
reads "who helped present the letter," cited to source 2 (FLI's own 2015
year-in-review newsletter). I opened that URL directly and confirmed the
exact sentence the citation rests on: "Stuart Russell and Toby Walsh
presented the autonomous weapons open letter at the International Joint
Conference on Artificial Intelligence in Buenos Aires, Argentina" — the page
does not call him a drafter. The second mention ("some of the letter's own
signatories, Russell among them," Slaughterbots paragraph) is unchanged from
editor/01's approved fix and still reads "signatories," consistent with the
record.

**New sources.** Opened both new citation hrefs directly (not just checked
the evidence record's paraphrase) and confirmed each lands on the source
itself and supports the claim it's cited for. `data-nb-kind` is correct on
both: source 2 (FLI's own newsletter) is `primary`; source 13 (Jamestown/
Shichor, an independent think-tank publication) is `secondary` — matching
researcher/02's own classification for each.

**Renumbering.** Extracted every `sup`/`href` pair programmatically (41
citations total): every displayed number matches its `href` target id with
zero mismatches, and the first-appearance order across the article is
strictly sequential 1 through 17 — clean `W-CITE-ORDER`. The two new sources
land exactly where the writer's handoff said they would (2 right after 1;
13 right after 12).

**dek/dekline.** Extracted the `nb-meta` JSON dek and the rendered
`.nb-dekline` text programmatically and diffed them: byte-identical.

Nothing broke on this pass. I found no new fact to route.

## Cut

Slop and edge pass on the changed material only (bookend Harpy clause, the
Russell first-mention sentence, the full Harpy paragraph, the holds-up
bullet, the-fight-now's closing paragraph, the takeaway's Harpy sentence, and
the two sentences touched by the density fix):

- No sentence in the changed material failed the delete test — each carries
  either a new sourced fact (the export timeline, Russell's presenter role)
  or a reasoning step (the-fight-now's "Calling a ban premature and calling
  deployed autonomy well governed are not the same claim" survives; it's the
  paragraph's actual argument, not a signpost).
- No self-reference, method-signpost, or prompt leakage found in the changed
  sentences.
- Grepped for the four sentences editor/01 cut ("exactly the distinction the
  debate keeps blurring," "Put the record's two halves side by side...,"
  "The politics have not stood still," "It is not the whole picture.") and
  for the previously-cut "Fire and Forget" quote and "Weapons analyst"
  title — none reintroduced.
- Checked the density fix directly: the Kallenborn quote now closes on a
  literal `...` rather than the `&hellip;` entity that was fusing it with
  the next sentence past the proof's sentence-boundary regex, and "offers
  the closest thing to a positive claim, hedged twice" is now its own
  sentence, followed by "He hedges it twice: ..." Both read cleanly and the
  proof confirms zero density warnings.
- Ran a punctuation-artifact grep (double spaces, stray commas, doubled
  periods) across the full file: nothing found.
- Word count: `nb-meta` and the rendered content agree at 2200 words, at the
  top of the lesson band's 1200–2200 ceiling but not over it.

No sentence failed the slop test on this pass. Nothing to cut.

## Reader

I did not re-open the original-work sentence question generally — editor/01
already answered it and this round's changes don't touch the article's
synthesis, only one factual anchor and one attribution. Reading the changed
passages in place: the Harpy paragraph and the-fight-now's closing argument
read stronger than round 1, not weaker — "two decades before the 2015
letter" and "decades of Harpy sales against it" are more concrete and more
defensible than the round-1 "since the 1990s" claim they replace, and the
piece loses nothing in specificity for having narrowed to what the record
actually supports. The prose in the changed sentences sits at the same
register as the rest of the piece — plain, load-bearing, no borrowed
phrasing. Reread the headline as the largest claim: it is unchanged from
editor/01's approved version and still accurate.

## Edits

None. Every item in review-brief.md item-by-item checked out on direct
verification (opened both new source hrefs live, extracted and diffed the
dek/dekline programmatically, extracted every sup/href pair and confirmed
sequential 1–17 with zero mismatches, grepped every remaining
1990s/1980s/1999/decades/drafter instance) with nothing left to fix.

## Required work

None. All items in review-brief.md resolved: Harpy date reframed
consistently everywhere with no surviving unsourced fielding-year claim,
Russell no longer called drafter and his "helped present" wording is cited
to the record, both new sources carry correct `data-nb-kind` and open
correctly, citation renumbering is clean 1–17, and the dek/dekline are
byte-identical.

Proof after this review:

```
./nb check .nb-work/what-could-go-wrong/autonomous-weapons/library/what-could-go-wrong/autonomous-weapons.html --series what-could-go-wrong --no-check-links

BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

## Decision

approve — every required repair from editor/01 and researcher/02 landed
correctly and verifiably (both new sources opened and confirmed live, dek/
dekline byte-identical, citations sequential with no mismatches, no
surviving unsourced Harpy date, no "drafter" label), the fresh skeptic and
cut pass on the changed material found nothing to break or cut, and the
proof is clean at 0 BLOCK / 0 WARN.
