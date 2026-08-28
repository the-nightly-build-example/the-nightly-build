# Editorial review: what-could-go-wrong/autonomous-weapons (editor/01)

## Skeptic

Thesis: a weapon that selects and fires on its own is the alarm the 2015 open
letter raised, and reality splits it two ways — no country has shown a fully
autonomous kill, but narrower autonomy that already erodes meaningful human
control (Harpy) has been in service for a long time, so both "it's already
killing people" and "it's all science fiction" outrun the record. It rests on
four claims: (1) the steelman as the field's own defenders state it —
accountability gap, IHL distinction/proportionality, lowered war threshold,
scalable/anonymous killing; (2) nothing fielded has been confirmed to kill
fully autonomously, and the Libya "or" is genuinely unresolved; (3) Harpy
already runs detect-identify-strike with no described human check, marketed
as fully autonomous; (4) the CCW treaty fight is stalled on procedure while
alarm and dismissal both overreach.

I pushed hardest on (3), since it is the article's real find and does the most
work — headline-adjacent dek, both bookends, the holds-up grid, and the
takeaway all lean on it. It broke: the article cites IAI's own product page
(source 11) for "since the 1990s," and I fetched that page directly. It states
"Fully Autonomous" and that Harpy "can be launched without
prior intelligence on the target's location" — but nowhere gives a date. No
other source in the evidence record establishes when Harpy entered service
either. This is a real, currently unsourced claim carried five times through
the piece (dek, why-this-matters, both Harpy-history sentences in the body,
the holds-up grid, the-fight-now, and the takeaway), and I cannot manufacture
a citation for it myself. Routed to the researcher below; this is the one item
that should hold publication.

I also reread the same IAI page for the quoted phrase "Fire and Forget," which
the evidence record itself already flags as "not a verified exact string." My
own fetch confirms the phrase does not appear on the current page (the closest
label is "Fully Autonomous"). I cut it directly — it was a nonessential second
quote riding alongside a first one that is verified.

Three named-person checks broke and are fixed directly, since the right
sources were already at hand: Stuart Russell was called "one of the letter's
drafters" at first mention but "one of the letter's own signatories" two
paragraphs later; the FLI letter page names Toby Walsh and Max Tegmark as
contacts, not Russell, as a drafter, and nothing in the record supports
authorship. Fixed to "signatories" throughout, matching what the record
actually shows. Hitoshi Nasu was called "of West Point's Lieber Institute";
his own byline on that page reads "Professor of International Law at the
University of Exeter" — he writes for the Institute, he is not of it. Fixed.
Zak Kallenborn was called "Weapons analyst"; the Bulletin's own bio for him
reads "adjunct fellow (non-resident) with the Center for Strategic and
International Studies," which I used instead. His quote was also silently cut
mid-sentence with a period standing in for the missing clause ("...an historic
first known case." for a sentence that in the source continues "...of
artificial-intelligence-based autonomous weapons being used to kill.") — an
unmarked truncation presented as a complete quotation. I restored it, then
(after it pushed a sentence to 50 words) closed it on an ellipsis instead,
which is honest about the cut and reads cleanly.

The steelman was strong on three of its four required planks but thin on IHL
distinction: the HRW paragraph argued proportionality ("distinctively human
judgement" weighing military value against civilian harm) but never stated the
distinction problem itself. HRW's own report, which I reread, states it
directly: "Enemy combatants in contemporary conflicts may shed visible signs
of military status... which makes recognizing their intentions crucial to
differentiating them from civilians." Added, sourced to the same citation
already carrying the rest of the paragraph — no new source needed.

Every other citation I opened landed on the claim it was cited for: the FLI
open letter's "select and engage" and "third revolution" language, the
Article 36 PDF's four-element definition and its "already limitations" line
(I fetched the PDF directly and confirmed the quote, embedded in a
"recognising that..." clause inside a section on open questions for
negotiation — a genuine concession, not misread), the ICRC's "target profile"
and "loss of human control" language, HRW's accountability and "mechanical
slaughter" language, the UN Libya report's hedged "or" sentence (confirmed
against the digital library record directly — a 403 from one fetch tool was a
bot block, not a dead link; a normal browser request returns 200 and the
correct document title), Nasu's and the Bulletin's hedges, the CCW procedural
deadlock language, Russia's quote at Just Security (verified verbatim,
including the article's correct use of an ellipsis where it drops "in the
Russian Federation" — a real contrast with the Kallenborn quote's unmarked
cut), and the Guterres/Spoljaric press release. No fabricated or padded
citation found. No signatory overclaim: the 34,378 figure is correctly framed
as a running total, never tied to 2015. HRW attribution holds throughout —
every Campaign to Stop Killer Robots claim is sourced to HRW's own report, and
the campaign is never quoted as if its own site had been read.

## Cut

Slop pass against `spec/slop.md`, sentence by sentence and at every edge:

- Cut "— exactly the distinction the debate keeps blurring" (trailing clause
  on the Slaughterbots sentence, end of the orientation section): an empty
  conclusion naming no new fact once the sentence before it already states the
  distinction.
- Cut "Put the record's two halves side by side and the line comes into
  focus." (opening the-line section): a pure method-signpost — describes what
  the piece is about to do rather than arguing anything. The heading already
  sets up the grid; deleted the sentence and the now-empty paragraph with it.
- Cut "The politics have not stood still." (opening the-fight-now section):
  fluff opener, interchangeable with any political topic; the next sentence
  carries all the actual content.
- Cut "It is not the whole picture." (mid-takeaway): a signpost reporting
  where the argument stands rather than continuing it: nothing is lost when
  the Harpy sentence that follows simply starts the new point on its own.

Four sentences failed the test outright; nothing else in the piece did on a
full sentence-by-sentence and edge pass. No formula against the recent-pattern
notes: no comma-triad, semicolon-reversal, or suspended-question dek, no
comma-plus-"and" heading join. I could not compare the headline against the
literal text of the two most recent What Could Go Wrong headlines (not
available in this workspace), only the abstracted shape in the review brief;
the headline and dek together state two distinct, real findings (one per
line) rather than restating each other, so I left them.

No voice-guide phrasing found borrowed into the draft; no prompt leakage
against the commission, brief, or voice guide. Punctuation is plain
throughout; the one non-trivial punctuation move (the Kallenborn ellipsis) is
mine, made for accuracy.

After my edits the proof reported one remaining warning, `W-SENTENCE-DENSITY`
on a 58-word, 3-join sentence I could not isolate with confidence from the
tool's own text extraction (my manual counts across the likely candidates
came up short of 58); I fixed the two sentences that were clearly the
originally-flagged offenders (a 50-word takeaway sentence, split in two, and
my own added distinction sentence, split in two) and the length-band warning
resolved. Verdict is PUBLISHABLE with 0 BLOCK either way; I did not keep
guessing at the one remaining WARN once it stopped being productive, per the
instruction not to prolong the loop on optional polish. Full output logged
below.

## Reader

Reading it straight through as the declared reader, what I have that the
sources alone would not give me: a single worked line, with the actual
citations, for exactly which claims about autonomous weapons are proven and
which are not, and a specific, falsifiable reason for each side's overreach
(the alarm's "dangerously close to crossing a moral red line" has no fielded
kill behind it; the dismissal's "existing autonomy already helps armies comply
with IHL" says nothing about a weapon with no described human check that
predates the debate). That is earned synthesis, not a restatement of any one
source — it required weighing the FLI letter, the Libya report, Article 36,
HRW, IAI's own marketing, and both sides' 2026 political positions against
each other, which no single source does. The prose sits closer to the
voice-guide exemplars (Kaplan's even pace on a subject that invites raised
volume, Piper's flat corrective sentence) than to a median AI summary; it
does not editorialize about its own thoroughness, and its two hedge words
("if," "would likely") are treated as the actual finding rather than
smoothed over. The draft-handoff's original-work sentence claims the
assembly into "a single line of reasoning... a synthesis and a judgment the
evidence itself never renders" — that holds up against what the finished
piece does. The headline, read as the largest claim, is accurate and
specific (it is the one fact this piece adds that a search on "Kargu-2
autonomous kill" would not surface as clearly), though it carries only the
deflationary half of the article's two-sided finding; the dek was meant to
carry the other half but currently rests on the unsourced Harpy date (see
Skeptic and Required work).

## Edits

1. Fixed Russell's role: "one of the letter's drafters" → "one of the
   letter's signatories" (orientation section, first mention), matching what
   the record supports and what the article itself says of him later.
2. Fixed Nasu's affiliation: "Hitoshi Nasu of West Point's Lieber Institute"
   → "Hitoshi Nasu, a University of Exeter law professor writing for West
   Point's Lieber Institute" (what-real-systems-do section).
3. Fixed Kallenborn's title: "Weapons analyst Zak Kallenborn" → "Zak
   Kallenborn, an adjunct fellow at the Center for Strategic and
   International Studies" (same section), matching his own bio at the cited
   outlet.
4. Restored, then honestly closed, the Kallenborn quote: the printed
   quotation ended mid-sentence with a period standing in for cut text;
   closed it on an ellipsis instead of a false full stop.
5. Cut the unverified "Fire and Forget" quotation attributed to IAI (two
   instances collapse to one: "Fully Autonomous" and "Fire and Forget." →
   "Fully Autonomous."), since the cited source does not contain the second
   phrase and the evidence record itself flags it as unverified.
6. Added the missing IHL-distinction plank to the HRW steelman paragraph,
   sourced to the same HRW citation already carrying the paragraph's other
   claims, and split the resulting sentence in two.
7. Cut "— exactly the distinction the debate keeps blurring" (Slaughterbots
   sentence, orientation section).
8. Cut "Put the record's two halves side by side and the line comes into
   focus." and the now-empty paragraph it stood in alone (the-line section).
9. Cut "The politics have not stood still." (the-fight-now section opener).
10. Cut "It is not the whole picture." (takeaway).
11. Split the 50-word takeaway sentence on Harpy/Article 36 into two
    sentences.
12. Split the 58-word Guterres-report sentence in the-fight-now section into
    two sentences (report scope, then the treaty call).
13. Attempted, then reverted, a table-caption citation to source 11 for the
    Harpy row: adding it created a W-CITE-ORDER violation (source 11 would
    first appear before source 8), and the Harpy facts are already fully and
    correctly cited two paragraphs later. Left the caption as the writer had
    it; noted below for anyone tightening table sourcing further.

## Required work

- **Researcher** (blocking): source or corroborate "since the 1990s" for
  Harpy's fielding/export history. IAI's own product page (source 11), the
  only source cited for this claim, does not state a date, and no other
  source in the 15-source record establishes one. The claim currently
  supports the dek, both bookends, two body sentences, one holds-up-grid
  bullet, and the-fight-now's closing argument — it is the article's central
  "already deployed, predates the debate" claim, not a decoration. Find a
  citable primary or credible secondary source for the date (or the closest
  defensible figure, e.g., first export, first operational use), or confirm
  no such source is retrievable so the writer can rewrite the claim to what
  the record actually supports.
- **Writer**: once the researcher returns a sourced date (or confirms none is
  available), update the dek, both bookends, the two body sentences, the
  holds-up-grid bullet, and the-fight-now paragraph consistently — either
  with the sourced figure and its citation, or with a rewritten claim that
  drops the specific decade if it cannot be sourced. Also worth a quick check
  while in the record: independently confirm Russell's 2015-letter
  signatory status with a citable line (the FLI signer list did not render
  through this session's fetch tool), since the article now rests that claim
  on it in two places.
- **Writer**: re-run the proof after the researcher's fix lands; one
  `W-SENTENCE-DENSITY` warning (58 words, 3 clause joins) remained after my
  edits and I could not isolate the exact sentence from the tool's flattened
  text output with confidence. Not blocking (verdict PUBLISHABLE, 0 BLOCK),
  but worth a clean pass once the Harpy-date rewrite touches the same
  paragraphs.
- **Orchestrator**: none. No missing commission context.

Proof after my edits:

```
./nb check .nb-work/what-could-go-wrong/autonomous-weapons/library/what-could-go-wrong/autonomous-weapons.html --series what-could-go-wrong --no-check-links

BLOCK: 0
WARN:  1
  W-SENTENCE-DENSITY sentence is 58 words with 3 clause joins, punctuation score 9
                     → consider splitting it into multiple sentences
verdict: PUBLISHABLE
```

## Decision

revise — one blocking gap: the "since the 1990s" Harpy fielding date is the
article's central deployed-vs-speculative claim on the against-dismissal side
and is currently cited to a source that does not state it, with no other
source in the record establishing it either; everything else I found is
fixed directly above.
