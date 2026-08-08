# Editorial review: what-could-go-wrong/data-poisoning (editor/02)

This is a narrow confirmation read of writer/02 against the four round-01
required items. Round 01 settled the substance, spine, rates, and sourcing
labels; none of that is reopened here.

## Skeptic

The four round-01 required items all resolved cleanly:

1. Body-closing "Verdict" block gone. A search of the article for
   `nb-note-strong`, `nb-note`, and "Verdict" returns nothing. The
   why-they-dont-combine section now closes on its own argument, the
   "Neither easy story survives the evidence" paragraph that names the gap in
   both directions, and no summarizing or finding-restating block took the
   Verdict note's place. The takeaway bookend still lands the judgment
   ("A real, reproducible risk has been demonstrated in pieces; the assembled
   attack, in the wild, has not"). The press direction against closing the body
   with a finding-restating block is now honored.

2. s5 (OATML) title verbatim. The source line now reads "Poisoning Attacks on
   LLMs Require a Near-constant Number of Poison Samples," the real on-page H1
   I verified in round 01, disambiguated in the source line as the blog
   announcement of the s3 paper so it does not read as a duplicate of s3.

3. s8 (Fortune) title verbatim. Now "A small amount of bad data can 'poison'
   even the largest AI models, researchers warn," the real headline.

4. Mavroudis quote verbatim with honest elision. The article now prints a model
   that "when … it detects a specific sequence of words, it foregoes its safety
   training." Fortune's text is "when, for example, it detects a specific
   sequence of words, it foregoes its safety training." The second "it" is
   restored and the removed "for example," is marked by the ellipsis. The words
   inside the quote marks are now Fortune's own.

Does-not-compose discipline holds, unchanged. "Easy to install" stays attributed
only to Souly (never safety-tested, decayed under continued clean training);
"survives safety training" stays attributed only to Sleeper Agents (hand-written
SFT). The four-row table's columns still refuse to align: Souly's row reads "Not
tested; decayed under continued clean training" under *Survived safety training?*
and the only "Yes" is Sleeper Agents via "Wrote the triggers in directly." The
closing paragraph still names the gap in both directions. Nothing regressed.

## Cut

No cut needed. The removal of the Verdict block freed words without leaving a
seam; the section reads as one argument to its close. The changed source lines
and the repaired quote introduced no new prose beyond the verbatim strings.
Spot-checked the changed spots only, per the confirmation brief; the rest of the
piece is settled work I did not reopen.

## Reader

Unchanged from round 01 and still holding: the piece gives the reader an
assembled, side-by-side account of why the two scariest results cannot be
stacked, legible in a table arranged so the non-composition shows rather than
asserts, plus the honest both-directions gap. The prose still sits closer to the
Carlini/Schneier exemplars than a median summary. The confirmation did not
disturb that.

## Edits

- None. All four required items were writer-owned and correctly applied; no
  direct cut was warranted, so no `./nb stamp` was run.

## Required work

- None. The four round-01 items are resolved and nothing regressed.

## Decision

approve: the Verdict block is gone with no restating block in its place, both
source titles and the Mavroudis quote are now verbatim (elision honestly
marked), and the does-not-compose discipline and settled substance are intact.
