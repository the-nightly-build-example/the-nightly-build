# Editorial review: the-instruments/hellaswag (editor/01)

## Skeptic

Thesis: a HellaSwag point is awarded for one narrow thing, recovering the real
next sentence out of three machine-written decoys, so a 2023 score near 95%
cited as "commonsense" is a saturated number graded against a partly broken
answer key, and two close scores no longer rank two models. The piece stands on
four claims: (1) a right answer is continuation-matching, not shown reasoning;
(2) the score climbed from 47.3% in 2019 to 95.3% in 2023 and is now level with
the 95.6% human line, not past it; (3) the answer key itself is unreliable, with
nearly 40% ungrammatical prompts and a hand audit finding 36% of a sample
broken; (4) the number is therefore saturated and no longer separates models.

I pushed hardest on claim (2), the one the round flags. The article holds the
line the orchestrator ruling requires. It writes "No checked model clearly
passes 95.6," fixes GPT-4's 95.3 as three-tenths under the human mark, frames the
cluster as noise, and quotes the retiring leaderboard's own verb, "reaching," not
"surpassing." Nowhere does it say models beat or passed the human number. The
figures verify against their owning primaries: 47.3% and 95.6% from the HellaSwag
paper (arXiv 1905.07830, opened and confirmed); 95.3% ten-shot from the GPT-4
report (arXiv 2303.08774, confirmed) and the author's own leaderboard
(rowanzellers.com/hellaswag, confirmed, listing "GPT4 base 10-shot 95.3" against a
stated "over 95%" / 95.6 human baseline). The item count verifies against the
released dataset (huggingface.co/datasets/Rowan/hellaswag, confirmed:
39,905 / 10,042 / 10,003 = 59,950), and the article states the released 59,950
with the split and notes the paper's rounder "70k," as the brief requires.

The two worked items are reproduced faithfully. The clean roof item matches the
released validation row 0 verbatim, gold index 3, and the caption's "roof
shingles" gloss matches the row's ActivityNet activity label. The flawed Surge AI
lacrosse item is verbatim, including the source's own typo "ield" in the
keyed-correct ending; I confirmed both against the Surge post (surgehq.ai,
opened), which carries the same 36% / 107-of-300 finding and the same quoted
item.

The error figures check against the validity paper (arXiv 2504.07825, opened;
abstract confirms the >65% Lorem-ipsum result and GoldenSwag, remaining figures
in the full text per the evidence locators): almost 40% ungrammatical prompts,
95.7% of the ActivityNet subset, 21.1% with a decoy as good as the key, key
correct in 96.3% of cases. I recomputed the article's derived figures: 100 − 96.3
= 3.7%, and 1/27 = 3.70%, so "roughly one item in twenty-seven is simply
mislabeled" is arithmetically right.

Two figure discrepancies surfaced against the primaries, both in the
commonsense-claim section, and both conflicting with the article's own
correctly-sourced statements elsewhere. The closing paragraph described the key
as "wrong about one item in twenty" (5%), where the mislabel rate the article
itself derives is one in twenty-seven (3.7%), and as "ungrammatical on nearly
half," where the sourced and elsewhere-stated figure is nearly 40%. The primary
governs; I corrected both to the article's own sourced values directly.

Every citation href was opened as printed. All nine resolve to the source
itself: s1 dataset, s2 HellaSwag paper, s3 SWAG paper, s4 GPT-4 report, s5
rowanzellers leaderboard, s7 validity paper, s8 Surge, s9 Deepgram all render the
owning document. s6 (the Open LLM Leaderboard v2 announcement) is a HuggingFace
Space; it renders its own leaderboard shell with the v2 "let's make the
leaderboard steep again" tagline, which is specific to that announcement, so the
href lands on the correct source, and the saturation quote is held in the
evidence record. The `data-nb-kind` labels are sound: the two secondary tags (s6
leaderboard operator's interpretation, s9 Deepgram explainer) are correctly
secondary, and the primaries each own the figure cited to them.

The chart was inspected as visual evidence. chart-1.py and chart-1.png are
honest. Axes are labeled (Year; HellaSwag accuracy %), the y-axis runs 0–100, the
human baseline is a labeled dashed reference line at 95.6, and the model line runs
47.3 (2019) to 95.3 (2023), ending visibly below the human line, which is the
honest picture. The x-axis is categorical with only the two anchored years, and
the caption states "two anchored measurements," so the connecting segment implies
no intermediate-year precision the data lacks. Every plotted number matches the
provenance script, the evidence Numbers, and the cited primaries. No chart
correction routed to the writer.

## Cut

The dominant pattern was the body addressing the reader. The lesson template
confines reader-address and self-reference to the two bookends and requires the
body to speak to no one; four body passages broke that. "Hold onto that, because
it is the point the rest of the lesson turns on" (orientation) both addressed the
reader and narrated the lesson, so I cut it to the bare load-bearing claim.
"Read that carefully, because the easy version of it is wrong" (the-gap) was a
reader-address signpost previewing a correction the next sentences make plainly,
so I cut it. "Recall what a right answer is supposed to be... If you can blank
out the scene" (broken-items) I recast to the impersonal, keeping the check the
reader can follow, which the voice guide wants, without the second person.
"Here is what that costs a reader. See GPT-4 at 95.3... You are reading noise"
(commonsense-claim) I rewrote to the impersonal, keeping the concrete scenario
the commission asks for. One remaining "you could check yourself" in the
orientation count note was also reader-address plus a method aside; I recast it
to state which figure governs without addressing anyone.

One empty topic sentence went: "The design did what it was built to do" opened a
paragraph and stated an assessment the same paragraph then grounds and restates
as "adversarial filtering worked." It failed the placeholder test (any design
did what it was built to do) and was redundant, so I cut it and let the figures
lead.

One overstated descriptor: "the ActivityNet half of the test" asserts a
proportion the record does not establish (the ~40%-overall / 95.7%-ActivityNet
figures imply ActivityNet is under half). I changed "half" to "portion," which
the sources support and the sentence does not need the quantity to make its
point.

Edges, dek, and headings were checked against the recent-pattern notes. The "Why
this matters" opener does not use the "by the end you will be able to"
catchphrase; it opens on this test's own reason to read and closes on "the three
separate things it now hides," which the body resolves. The headline is a stated
finding in HellaSwag's nouns, not a comma-continuation or colon-subtitle mold.
The dek is a two-clause compound, not one of the flagged dek molds
(semicolon-reversal, comma-triad, suspended-question). The closing sections, "The
typo in the answer key" and "Why 95% still reads as commonsense," are fresh in
HellaSwag's nouns, not the flagged "What a high score would not prove" shape. No
borrowed phrasing from the voice-guide exemplars and no brief/commission leakage
found; the reader-situation language the commission supplies is used as reported
framing, not lifted. Furniture (the verbatim table, the misspelled-key note, the
chart) each does distinct evidentiary work; none is a decorative stack.

## Reader

What the piece gives beyond its sources: one shipped item carried the whole way,
so the reader sees for themselves that a HellaSwag point only ever means "picked
the real next caption," and then watches that same fact turn a 2023
"commonsense" score into three things at once, a continuation match, an unreliable
key, and a saturated ceiling, that no single source states together. That
synthesis is the article's own, and it matches the draft-handoff's original-work
claim. The prose, after the reader-address cuts, sits closer to the Roser/Luu
plain-and-concrete register the voice guide sets than to a median summary: worked
cases before verdicts, figures given plainly, the Lorem-ipsum check presented as
something the reader can follow. The headline reads true as the largest claim the
piece defends.

## Edits

- Cut reader-address/self-reference "Hold onto that, because it is the point the rest of the lesson turns on"; kept the continuation-vs-reasoning claim (orientation).
- Recast the item-count note off "one you could check yourself" to an impersonal statement of which figure governs (orientation).
- Cut the empty, redundant topic sentence "The design did what it was built to do" (how-answers-built).
- Cut reader-address signpost "Read that carefully, because the easy version of it is wrong" (the-gap).
- Recast "Recall what a right answer is supposed to be... If you can blank out the scene" to the impersonal, preserving the check (broken-items).
- Changed "the ActivityNet half of the test" to "the ActivityNet portion of the test" (unsupported proportion) (broken-items).
- Corrected "wrong about one item in twenty" to "one item in twenty-seven" to match the article's own 96.3%-derived figure and the primary (commonsense-claim).
- Corrected "ungrammatical on nearly half" to "nearly 40%" to match the sourced figure stated elsewhere in the article (commonsense-claim).
- Rewrote the reader-addressing cost paragraph ("Here is what that costs a reader. See GPT-4... You are reading noise") to the impersonal, keeping the concrete two-score scenario (commonsense-claim).

## Required work

None. All findings were fixable by direct edit from the evidence and the sources
opened in the first read. No missing evidence for the researcher; no broken
central claim, redraft, source asset, or chart correction for the writer. The
orchestrator stamps and re-proofs after these edits.

## Decision

approve — the load-bearing figures verify against their primaries and hold the
"level with, not past" line, every citation resolves to its source, and the
reader-address and figure-consistency defects were fixable in place.
