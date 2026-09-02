# Editorial review: when-ai-breaks/bard-jwst-demo (editor/01)

## Skeptic

Thesis: Bard's launch demo shipped a confident, checkable falsehood because a
language model writes fluent text with no built-in truth check, so the
confidence of a sentence is no evidence of its truth, and the same failure now
runs in shipped products like AI Overviews.

The claims it stands on, and how each held:

1. Bard's promotional demo stated "JWST took the very first pictures of a planet
   outside of our own solar system," and that is false. Held. The verbatim
   sentence is at the cited source (Engadget, s2), which I opened; the exact
   wording matches.

2. The real first exoplanet image was 2M1207b, ESO VLT/NACO, detected 2004 and
   confirmed 2005; JWST's own first direct image was HIP 65426 b in 2022, which
   NASA calls explicitly not the first. Held against the primaries. I opened
   ESO eso0428 (2004 candidate, NACO on Yepun, the "if the candidate companion
   ... really a planet" quote), ESO eso0515 (the "first planet that has ever
   been imaged" quote, ~5 Jupiter masses), and NASA (the "not the first direct
   image of an exoplanet taken from space" quote). All three quotes and the
   dates match the article word for word.

3. Alphabet's stock fell about 8% (~$100B) that week, and no source pins the
   fall to the demo alone. Held on the numbers. Reuters via Al Jazeera (s6):
   8%, $8.59, $99.05, >$100bn; NPR (s7): as much as 9% intraday, Microsoft +3%.
   The article keeps the causation honest throughout ("No source ties the fall
   to Bard's error alone"), which is this round's central risk and it is handled.

4. The mechanism is ordinary LLM behavior, not a glitch, and it recurs in AI
   Overviews. Held. Hallucination and false-confidence are linked, not
   re-taught, in prose and in Background; both linked lessons exist in the
   library and their titles match the row text exactly. The AI Overviews close
   presents Google's "generally don't 'hallucinate'" line as Google's own
   account, matching the evidence's contradiction note. Reid's quote verifies
   at s8.

One break, and it is publication-blocking. The article prints a direct
quotation — Reuters "described the event as one that 'failed to dazzle'" — cited
to s6. I opened s6 three times. The word "dazzle" does not appear on the page.
The page's actual characterization is its lead: analysts said the AI search
event "lacked details on how it will answer Microsoft's ChatGPT challenge." So a
quotation reaches the reader that is not in its cited source. The evidence record
itself records "failed to dazzle" as living in the Al Jazeera reprint, so the
error originates upstream of the writer. Altering or requoting is not mine to do;
routed to researcher (fix the record) and writer (recast to the supported
wording). The dependent characterizations lean on the same unsupported phrase:
"a Google event that reporters called underwhelming" (vague attribution, s6) and
"a flat product event in Paris" (takeaway). Both must be reground to what s6
actually says once the quote is fixed.

Display text, descriptor by descriptor. Headline: "Bard's launch demo credited
the James Webb telescope with a discovery ESO made in 2004." The first image was
captured April 2004 (confirmed as a planet 2005); "2004" matches the commission
and the dek's "first photograph." Sound. Dek makes a claim about the world (the
first photograph was already eighteen years old when Google published the claim),
not a self-grade; "eighteen years old" is right for a 2004 image as of Feb 2023.
Subheads reconstruct the argument in the piece's own nouns and each verifies
(April 2004 candidate, 30 April 2005 confirmation, 1 September 2022 JWST). No
false label found in display text.

Every citation href opens to the source's own page: s1 blog.google (the Pichai
"An important next step" post, Feb 6 2023, LaMDA framing and JWST caption), s2
Engadget, s3 eso0428, s4 eso0515, s5 NASA science.nasa.gov, s6 Al Jazeera
(Reuters byline), s7 NPR, s8 blog.google AI Overviews (Reid). None is a fetch
endpoint; each lands on the document itself. The three originals the researcher
could not read firsthand (the Pichai tweet, Reuters and The Verge at their own
domains) are correctly not cited.

data-nb-kind audit against the researcher's authorship-and-stake test: primary
s1, s3, s4, s5, s8 (Google on its own launch and product; ESO and NASA on their
own observations); secondary s2, s6, s7 (outlets reporting from outside). Five
primary, three secondary, eight total — meets the floor (8 / 4 / 1). The
verbatim error and Google's statement sit on secondary sources by necessity, and
the record documents why; no label hides a missing independent source.

One uncited, unsupported claim cut on this read: "Bard itself launched to the
public two months later, in March 2023" is not in the evidence record, carries
no citation, and "two months" is wrong on its face (Feb to March). Removed as a
nonessential unsupported claim rather than routed.

## Cut

Slop pass, every sentence including display text and furniture. Three sentences
cut or repaired for slop, one heading rebuilt.

- Cut the empty-frame opener "The correction is not a matter of interpretation."
  It reduces to "the X is not a matter of Y" and the two ESO primary quotes that
  follow prove the point; deleting it loses no fact or reasoning step.
- Removed the decorating "sharply" from "Alphabet's stock fell sharply that same
  week." The voice guide is explicit that the market figure carries its own
  weight and takes no adjective telling the reader how to feel; the takeaway
  already writes "did fall that week" plainly, so this aligns the opener.
- Repaired a body self-reference the lesson template forbids outside its
  bookends: "The lesson for the reader is not that AI answers are usually wrong"
  named the lesson and addressed the reader in the body. Recast to "The problem
  is not that AI answers are usually wrong," keeping the earned contrast.

The negative-parallelism reflex appears several times and I checked each against
a named misconception: "did not just misdate an obscure fact," "This was not a
rare malfunction. It is the ordinary behavior," "Bard's demo did not glitch,"
and the recast "The problem is not that AI answers are usually wrong." Each
corrects a real underestimation the piece names (a minor date slip, a rare
glitch, that fluency signals truth), so each is earned and stays. No empty
punchlines survived: "Correct is not part of the specification" lands the
mechanism after it has been shown, which the voice guide permits.

Formula check against the recent-pattern notes. The dek is a single "when"-clause
sentence, not the flagged ", and"-twist or comma triad, and it does not echo
galactica. The headline is one clause with no trailing ", and" reveal. The
closing heading is "The failure moved from a demo to a search bar," not the
recurring "Where X still Y." One heading did carry the desk's flagged comma-and
mold — "What Google did next, and what the market did" — so I rebuilt it as "A
stock drop the reporting won't pin on the demo," which states that section's own
argument step. The four furniture components (two bookends, the quotation note,
the stat strip, the timeline) are all catalog-documented; the stat strip's three
figures are each cited in the prose beneath it and read honestly (close, market
value, intraday low). No prompt leakage survived the compare: the "ordinary
behavior, not a rare glitch" thesis tracks the commission's angle but is earned
in the body through the mechanism, not lifted as a planning label, and its
clauses are reordered.

## Reader

Read straight through as this paper's reader — smart, no time in a codebase,
forever meeting AI claims they cannot check — the piece hands over what the
sources alone would not: the exact false sentence set against the real
2004/2005/2022 record, the reason a fluent model writes a false sentence as
surely as a true one, and a test they can carry to the AI summaries they use
daily. The draft-handoff's original-work claim (a single dated argument that
converts the causation caveat into reasoned prose and carries the mechanism
forward into AI Overviews) survives comparison with the article; the piece does
that. The prose sits closer to the voice-guide exemplars than to a median
summary: dated beats with named actors, the market number left largely
unadorned, the mechanism compressed and linked rather than re-derived. The
headline, read as the largest claim, is true and supported.

## Edits

- Cut "The correction is not a matter of interpretation." (empty-frame opener).
- Removed "sharply" from "Alphabet's stock fell sharply that same week."
- Rebuilt the heading "What Google did next, and what the market did" as "A
  stock drop the reporting won't pin on the demo" (broke the comma-and mold).
- Recast "The lesson for the reader is not that AI answers are usually wrong" to
  "The problem is not that AI answers are usually wrong" (body self-reference the
  lesson template bans outside its bookends).
- Cut "Bard itself launched to the public two months later, in March 2023."
  (uncited, unsupported by the record, and factually loose on "two months").

## Required work

- researcher: The direct quotation "failed to dazzle" attributed to Reuters (s6)
  is not on the cited page. Correct the evidence record: the phrase does not
  appear in the Al Jazeera/Reuters reprint. The supported characterization on
  that page is the lead — analysts said the event "lacked details on how it will
  answer Microsoft's ChatGPT challenge." Confirm the exact wording and the
  readable source that carries it so the writer has ground to stand on.
- writer: Replace the misattributed "failed to dazzle" quotation with the
  supported characterization the record confirms, and reground the two phrasings
  that lean on it — "a Google event that reporters called underwhelming" (also a
  vague "reporters" attribution) and the takeaway's "a flat product event in
  Paris" — to what the sources actually say. While there, the em-dash-free
  sentence that carried the quote joins its clauses with a semicolon where a
  period would do; recast it as a period when you rewrite.

## Decision

revise — a direct quotation ("failed to dazzle") reaches the reader that is not
in its cited source, and correcting it needs the researcher's record and the
writer's re-reporting; everything else editable is fixed in place.
