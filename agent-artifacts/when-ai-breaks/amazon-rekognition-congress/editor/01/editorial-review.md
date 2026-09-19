# Editorial review: when-ai-breaks/amazon-rekognition-congress (editor/01)

## Skeptic

Thesis: a face "match" is only a similarity score past an operator-chosen
cutoff, and once you search a large gallery the wrong scores clear that cutoff
and land unevenly across groups; the ACLU's $12.33 test showed the mechanism,
Amazon's threshold defense lowers the count without settling the demographic
question, and no one ever ran the test on Rekognition that would settle it.

The claims it stands on, and how each held:

- **The incident (July 2018, 535 members, 25,000 arrest photos, default
  settings, 28 false matches, ~40% people of color vs ~20% of Congress, six CBC
  members incl. John Lewis, $12.33).** Every figure matches the ACLU primary in
  the evidence record. The arithmetic the article adds, 535 x 25,000 = "more
  than thirteen million one-to-one comparisons," checks (13,375,000). July 2018
  is held throughout; the MIT Tech Review 2019 misdate is not followed. Holds.
- **A match is a score past a threshold; default 80%, Amazon recommends 99%.**
  Matches the AWS primary (s2), quotations verbatim substrings ("not the right
  setting for public safety use cases"). Holds.
- **Gallery size multiplies chances of a false match.** Base-rate framing,
  correctly linked to the ShotSpotter lesson. Holds.
- **Demographic gaps.** This is where I pushed hardest, per the brief. Every
  gender-classification figure (Gender Shades 34.7%/0.8%, tested MS/Face++/IBM
  not Amazon; Actionable Auditing 31.37%/0.0% for Rekognition) is stated as
  *classification*, and the draft says so twice ("misclassified," "mislabeled the
  gender," "Both figures measure gender classification, not face matching"). NIST
  carries the *matching* gap in general (10x-100x; U.S. mugshots highest for
  American Indians, elevated for African American/Asian, higher for women) and is
  correctly stated as never having tested Rekognition. No classification error
  rate is presented as Rekognition's face-match error rate. The ~40%/20% skew is
  stated as a description of the 28, not a per-group rate. Holds; this is the
  article's most careful passage and it is right.
- **Moratorium (June 10, 2020) and its narrowness.** Matches s8/s9. Holds.
- **data-nb-kind audit.** s1-s8 primary, s9 (MIT Tech Review) secondary; all
  correct against the primary/secondary test. Floor met: 9 sources, 8 primary, 1
  secondary. Links resolved in the writer's proof (BLOCK: 0).

Two breaks in display text and furniture, both fixable without new reporting, and
both fixed directly:

1. **Headline (and `<title>` and h1) omitted "falsely."** "Amazon's Rekognition
   matched 28 members of Congress to arrest photos" states the opposite of the
   article's own claim, which is that all 28 were *false* matches. A scanning
   reader who reads nothing else would take sitting members of Congress to have
   been correctly identified in arrest photos. This is a false label on a true
   story, and the largest one in the piece. Fixed: added "falsely" in all three
   places, aligning the display text with the body's own claim (no claim change).

2. **The 95% threshold-table row was labeled as an Amazon primary statement**
   ("Amazon, the day it disputed the test / its first answer to the ACLU"), but
   no Amazon primary in the record states 95%; the figure exists only in the
   ACLU's reply paraphrasing Amazon's shifting numbers (s3), and Amazon's own
   July 27 post (s2) recommends 99%. Presenting 95% as Amazon's direct word
   conflicts with the Amazon primary. This is sourcing note (1) from the brief.
   Settled by keeping the row (the shifting-number point is central and is
   sourced to the ACLU reply) and relabeling it honestly to the ACLU's account,
   plus trimming "Amazon named" out of the caption.

## Cut

Slop pass, every sentence including display text, bookends, and the table
caption. The prose is disciplined; the negative-parallelism instances all
correct real, named misconceptions and are earned, not reflex:

- "A match is not something the system discovers. It is a similarity score..."
  corrects the exact misconception the lesson exists to fix. Kept.
- "a false match does not require a bad algorithm. It requires a large gallery
  and a cutoff loose enough..." corrects the "the algorithm must be racist"
  reading the piece is arguing against. Kept.
- Takeaway opener "did not prove ... racist, and Amazon did not prove it is
  safe" names both real positions and refuses both. Kept.

One sentence failed on both accuracy and slop grounds and was recast: the
gallery-section closer "the ACLU had left one at its factory position while
turning the other all the way up." "All the way up" misstates the 25,000 gallery
as maximized when Amazon's own retest used a corpus 30x larger, and the clause
was a decorative closer more than a fact. Recast to two plain sentences that keep
the two-dials teaching and state the gallery's role accurately.

Edge sentences read against `spec/slop.md`: openers and closers of each section
carry facts or reasoning. The "today" close ("The next face search that returns
a name is running the same arithmetic the ACLU paid $12.33 to expose") lands the
present-tense point without a moral, in the Langewiesche register the voice guide
asks for. I considered the two three-part parallels (the "today" recap and the
takeaway) as a doubled construction, but they do different work in different
tenses (mechanisms are live now vs. what the test proved plus the three
questions), each carries the specific mechanisms rather than a fillable pattern,
and both survive the slop test; I left them rather than prolong the loop for
optional polish.

The takeaway's flagged 48-word density-warning sentence: judged by the slop
test, each of its three clauses carries a distinct taught mechanism in the
article's own nouns and reduces to nothing generic; it is a long sentence under
control that sets up the three closing questions. Kept.

Prompt-leakage and borrowed-phrasing checks against the commission, brief, and
voice-guide exemplars found none: the arithmetic-conversion move mirrors
Langewiesche's method (which the voice guide directs) without borrowing his
wording, and no brief framing survives as prose.

Furniture pass: the piece is one table. With the Verdict note removed (below),
that is the whole desk, which is the deliberate lean choice the commission asked
for and it breaks the recent nb-note/nb-figure/nb-stat stack. The table earns its
place (a comparison three-plus rows deep is exactly a table). No source asset:
the writer's reasoning is correct that a captured Gender Shades / NISTIR figure
would read as a match-rate visual, the exact classification/matching conflation
the brief forbids, so prose is the honest presentation here.

## Publication-blocking press rule

The body closed with a Verdict note (`nb-note nb-note-strong`). `press/editorial.md`
bans closing the body with a Verdict note or any block that restates the finding;
the takeaway bookend is where a lesson lands its judgment. Removed the note. Its
one piece of synthesis not already carried elsewhere, that raising the threshold
lowers the overall false-match rate (Amazon's point) but does not by itself even
out the gap across groups (NIST's), was folded into the body's NIST paragraph as
earned, cited analysis, so the argument still lands its judgment in prose. The
rest of the note was already carried by the body ("NIST never tested Rekognition,
because Amazon did not submit it") and the takeaway ("the test that would ... is
the one Amazon declined to hand over"). The "other developers submitted theirs"
phrasing, sourcing note (2), left with the note; no "99 developers" count was
introduced anywhere, so that note is settled too.

## Reader

Read straight through as the paper's reader: I come away able to say what a
"match" actually is (a score past a chosen cutoff), why a big gallery turns rare
errors into real ones, and, crucially, how to tell the measured
gender-classification gaps apart from the still-untested question of whether
Rekognition's *matching* is biased. That separation is the thing no single source
hands you, and it survives the edits. The draft-handoff's original-work sentence
(the >13M-comparison reframing and the measured-vs-inferred line) is delivered in
the gallery-size and uneven-errors sections; removing the Verdict note did not
cost it, because the measured-vs-inferred line lives in the body prose and the
takeaway. The prose sits with the voice-guide exemplars, not a median summary:
concrete, arithmetic shown, attribution kept distinct from judgment. The headline,
reread as the largest claim, now states the actual finding.

## Edits

- Added "falsely" to the `<title>` tag.
- Added "falsely" to nb-meta `title`.
- Added "falsely" to the h1 `nb-title`.
- Table caption: "The confidence threshold Amazon named for face matching" -> "The confidence threshold named for face matching".
- 95% table row: "Amazon, the day it disputed the test / its first answer to the ACLU" -> "the ACLU's account of Amazon's reply / the figure Amazon gave before settling on 99%".
- Gallery-section closer recast: "the ACLU had left one at its factory position while turning the other all the way up" -> "The ACLU left the threshold at its factory setting, and the gallery of 25,000 gave the wrong faces their chances."
- Removed the closing Verdict note (`nb-note nb-note-strong`) from the uneven-errors section.
- Folded its unique synthesis into the NIST paragraph: added "Raising the threshold lowers the overall false-match rate, which is Amazon's point, but does not by itself even out the gap between groups, which is NIST's." (cited s7), and kept the closing limitation as "NIST never tested Rekognition itself, though, because Amazon did not submit it."

## Required work

None routed. Every issue was mine to fix and is fixed directly; no evidence gap,
broken central claim, or reporting need remains for the researcher or writer.
The edits removed a furniture block and changed prose, so the article needs the
orchestrator's re-stamp (word count and reading time) and the standard proof
re-run before the PR; no source URLs, citations, or claims changed, so the proof
should hold at BLOCK: 0.

## Decision

approve. The publication-blocking Verdict note is removed with its judgment
preserved, both sourcing notes are settled, the display-text accuracy error is
corrected, and no gender-classification rate is presented as Rekognition's
match-error rate.
