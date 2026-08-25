# Commission: when-ai-breaks/facebook-translation-arrest

## Assignment
Teach one real AI failure with a record: in October 2017, Facebook's machine
translation rendered a Palestinian construction worker's Arabic post — a
"good morning" greeting beside a photo — as "attack them" (Hebrew) and "hurt
them" (English), and Israeli police, acting on the machine translation with no
Arabic-speaking officer checking it, arrested him. Tell it in order: what the
system was built to do, what it actually did, who it affected, and what the
operator did afterward. Name the people, the companies, and the dates. Then
explain why this kind of system fails this way, teaching the missing piece on
the spot. Close on where the same weakness lives today, in systems the reader
actually meets.

## What happened (researcher verifies and dates every fact)
The worker posted in Arabic a word transliterated roughly "yusbihuhum" /
"يصبحهم", close in script to "good morning to them" ("sabah al-khair"
family), beside a photo of himself with a bulldozer at a West Bank
construction site. Facebook's Arabic->Hebrew/English neural translation output
a "hurt/attack them" reading. Police arrested him at the site, questioned him
for hours before anyone read the original Arabic, and released him once the
mistranslation was clear. Facebook apologized. Verify the exact wording of the
post and each translation, the location (reported as Beitar Illit), the date,
and Facebook's statement, from the primary reporting (Haaretz broke it; The
Guardian, Times of Israel, Gizmodo followed).

## Why it fails that way (the teaching)
- Machine translation guesses the most probable target text; it does not know
  what the source "really meant." Dialectal and colloquial Arabic — and short,
  context-free strings — are exactly where a system trained mostly on formal
  text guesses worst. The course has taught tokenization and the
  `multilingual-gap` (models see far less of most languages, and tokenizers
  split them worse); link it rather than re-teaching it.
- Automation bias is the second, decisive failure: a human acted on a machine
  output in a high-stakes setting without the cheap human check (one Arabic
  reader) that would have caught it. The translation error was ordinary; the
  harm came from trusting it unchecked.
- Distinguish the two so the reader sees that the fix is not only "better MT."

## Boundaries
- One incident. Do not fold in other translation stories except briefly as
  "where the same weakness lives today."
- Neighbor already published: `when-ai-breaks/facebook-myanmar` is a different
  Facebook failure (engagement-ranked feed, content moderation). Do not
  conflate. `the-mechanics/multilingual-gap` is the mechanism to link.
- Sensitivity: this involves a real, named private individual wrongfully
  detained, in a charged political setting. Report the record precisely and
  neutrally. Do not editorialize about the conflict; the lesson is about the
  system failure and automation bias, not the politics.

## Required contribution
Show the reader that the arrest turned on automation bias, not on an exotic
translation bug: an ordinary MT error in dialectal Arabic became a detention
only because a human treated an unchecked machine output as fact — and name
where that same unchecked-output pattern runs today (MT in policing, asylum
screening, and content moderation).

## Sources (researcher obligation)
Floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary here: the original reporting that holds the facts (Haaretz's account,
which is closest to the record; contemporaneous Guardian / Times of Israel /
Gizmodo pieces carrying Facebook's statement and the post's wording); any
Facebook/Meta statement quoted firsthand; and primary sources on the
mechanism (an NMT paper or documentation on dialectal-Arabic MT difficulty,
and the already-established multilingual/tokenization sources). Two retellings
of one origin count as one; corroborate the arrest facts across independent
reporting.

## Recent shapes to break (when-ai-breaks)
Verified against recent library structure and prose:
- Recent incident pieces open the why-bookend with a general principle ("A
  benefits agency does not need a robot to hurt people"). It is a good move
  but it recurs; vary it, or open on the concrete scene instead.
- The closing section "where the same weakness lives today" is series-
  mandated; keep it but avoid the recurring heading wording "Where the same
  <X> still runs / lives today."
- Avoid a takeaway that relitigates or moralizes; land on the automation-bias
  point in the article's own terms.
- Deks: no comma-triad, no semicolon reversal, no suspended question.

## Production record
Harness: Claude Code subagents, scheduled run. Balanced policy, no required
directives. Models/effort used:
- writing-coach: Claude Sonnet, low effort
- researcher: Claude Opus, high effort
- writer: Claude Opus, medium effort
- editor: Claude Opus, high effort
