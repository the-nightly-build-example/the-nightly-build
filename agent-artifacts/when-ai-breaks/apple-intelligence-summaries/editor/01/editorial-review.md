# Editorial review: when-ai-breaks/apple-intelligence-summaries (editor/01)

## Skeptic

The thesis: the Apple Intelligence notification failures were not a chatbot
inventing news from nothing but lossy compression of real published stories that
changed their meaning, and the damage came from each false line rendering under
the sending outlet's own name and icon. The claims it stands on:

1. Apple Intelligence notification summaries produced false lines under real
   outlets' names (Mangione "shot himself"; the Netanyahu, Littler, and Nadal
   cases). Held. Each traces to a cited BBC primary (s1, s4, s6). The Mangione
   line is given only in the BBC's own paraphrase, quoted and attributed; the
   Nadal ("Brazilian tennis player, Rafael Nadal, comes out as gay") and
   Netanyahu ("Netanyahu arrested") lines are the two quoted as literal
   notification text, exactly as the review focus requires; Littler is the BBC's
   paraphrase, attributed. The banned grouped "Luigi Mangione shoots himself; ..."
   screenshot string does not appear.
2. Each false line was a compression/misreading of a real story, not an
   invention. Held across all four cases and grounded in the source column of the
   table.
3. The harm is the outlet's name sitting atop a machine's sentence. Held; carried
   by the BBC's own statement (s6, "displaying the false headlines next to their
   logos") and CNN (s8, "under the publisher's banner"). The required
   contribution lands in the mechanism section and the takeaway.
4. Apple's response was narrower than the objectors' demand: a labeling promise
   (7 Jan, s5) then a pause only for News & Entertainment (16 Jan, s6). Held.

Breaks found and fixed:

- **Arithmetic.** "Apple had introduced the feature ten weeks earlier" is wrong.
  iOS 18.1 shipped 28 October 2024 and the Mangione report is 13 December 2024 —
  46 days, about seven weeks. Corrected to "seven weeks earlier" from dates
  already in the article. No new fact introduced.
- **Overstated attribution on the Netanyahu case.** The draft presented the
  21 November NYT "Netanyahu arrested" summary as flatly confirmed in the
  orientation, while later flagging NYT among the unverified social-media cases —
  internally inconsistent, and contrary to the record. The evidence record and
  the review focus are explicit: that case rests on a screenshot the BBC could
  not verify, flagged by a ProPublica journalist. Rewrote the sentence to
  attribute it as the BBC reported it (a screenshot it could not itself verify),
  using only verification context already in the cited source (s1). The mechanism
  section's use of the case as an "intrinsic misreading" now sits on an honestly
  scoped premise.

Verified and held without change: the Maynez 70%/90% figures are scoped to the
XSum research benchmark and explicitly disclaimed as not a measure of Apple's
feature (s7); the "also affected" outlets (Sky News, NYT, Washington Post) are
framed as unverified social-media reports (s6); Apple's side is single-origin to
the two brief statements and not overstated; the intrinsic/extrinsic mapping and
the named third failure mode (the Nadal cross-notification identity swap) read as
the writer's reasoning shown, not as the sources' labels. The eight `data-nb-kind`
labels match the evidence record's classifications; the source floor (8 sources,
6 primary, 2 secondary) is met. Display text checked descriptor by descriptor:
headline, dek, and all four subheads carry accurate, committed claims.
Distinctness holds — galactica and ai-overviews are named only to mark the
boundary (invention vs compression; junk read faithfully vs real news read
unfaithfully), and the two Background links are the-mechanics/hallucination and
the-instruments/hallucination-rate. Internal library link targets are not present
in this checkout (the library is protected state), which is expected; all four
correspond to lessons the evidence record confirms exist.

## Cut

No sentence was cut for slop: run against the placeholder test, the edges hold
because their nouns carry them, and the two negative-parallelism constructions
("not invention, compression"; "not X, but a far more ordinary process") sit on
the real, named misconception the whole piece exists to correct, which is the one
case the rule permits. The Zetter move (the plausible wrong read stated fairly,
then overturned) is executed in the mechanism section as the voice guide directs,
and the Langewiesche register (state the mismatch plainly, no appended alarm)
holds in "It compressed. It did not invent."

Two edges were repaired for writing, not slop:

- A broken sentence in the orientation — "it was not the only accurate one
  either," which reads as calling the false Mangione line accurate — was rewritten
  as part of the Netanyahu fix ("not the only line in its notification").
- The closing section heading "Your inbox runs the same compression" addressed
  the reader in the second person, which the lesson template allows only in its
  two bookends; every other reader-address in the body is a self-reference
  failure. Rewrote it in the incident's own nouns, "Mail, chat, and search run
  the same compression," and updated the section id and label to match. After the
  fix, the only second-person prose is inside the Why-this-matters and takeaway
  bookends, as the template requires.

One reflex semicolon ("The BBC complained to Apple in December; Apple declined to
comment") was set to the plainer period the punctuation standard defaults to. The
parallel semicolon in the closing section (Google's summaries do this; Apple's
did that) is a genuine tight parallel and was left. No recent-pattern formula:
the opener heading is the incident's own ("The Mangione summary"), not the
"What OpenAI shipped" mold; the close is built in this incident's nouns, not the
"Where the same X still lives" shape; the dek commits to the specific find with no
comma-triad or semicolon reversal. Furniture (one table, one position card, one
statement note, the two bookends) reads as a continuous article, each block
earning its place.

## Reader

Read straight through, the piece gives what the sources alone do not: the four
cases sorted against the intrinsic/extrinsic split, the Nadal case named as a
distinct cross-notification grouping error the single-document literature was not
built to measure, and the brand-attribution aggravator made explicit. The
original-work sentence in the draft handoff claims exactly this synthesis, and the
article delivers it. Both answers survive, so the piece is not a restatement of
its sources. The prose sits closer to the voice-guide exemplars than to a median
summary: it opens on the dated concrete scene, states the plausible-but-wrong read
before correcting it, and lets the mismatch stand unglossed. The headline, read as
the largest claim, is accurate and concrete.

## Edits

- Corrected "ten weeks earlier" to "seven weeks earlier" (28 Oct 2024 to 13 Dec
  2024 is 46 days).
- Rewrote the orientation's Netanyahu passage to attribute the 21 November NYT
  "Netanyahu arrested" case as a screenshot the BBC could not itself verify,
  flagged by a ProPublica journalist, and fixed the broken "not the only accurate
  one either" sentence in the same move.
- Renamed the closing section heading from "Your inbox runs the same compression"
  to "Mail, chat, and search run the same compression," and updated its
  `data-nb-section` and `id` to `mail-chat-and-search`, removing the only
  reader-address in the body.
- Changed the semicolon in "complained to Apple in December; Apple declined to
  comment" to a period.

## Required work

None outstanding. Every finding was resolved by direct edit using facts already
in the article and its cited sources; no break needed new reporting, a redraft, or
new evidence. The orchestrator re-stamps and runs the proof after these edits; the
one changed section `id` and the small wording changes refresh derived nb-meta
(word count, reading time) on that stamp.

## Decision

approve — the thesis and its four claims hold against the record, the attribution
is now honest descriptor by descriptor including the previously overstated
Netanyahu case, and the sole self-reference and the arithmetic error are fixed.
