# Editorial review: the-evidence/computing-machinery-and-intelligence (editor/01)

## Skeptic

Thesis: "passed the Turing test" is invoked as if it were one fixed bar, but
Turing set a narrow, numbered bet in 1950, and the 2025 result now cited as
meeting it keeps only one of his conditions and changes the rest, so the modern
claim borrows his name and quietly moves the test.

The piece stands on four claims, and each held after testing against the
evidence record and the two primaries.

- Turing's one prediction. The verbatim forecast (about fifty years, ~10^9
  storage, average interrogator, no more than 70 percent, five minutes) matches
  the primary word for word. The derived anchors check out: 10^9 is a billion,
  fifty years from 1950 is 2000, and the brain-storage range 10^10 to 10^15 is
  correctly rendered as ten billion to a thousand trillion. One break: the draft
  wrote "the bet has four parts" and then listed three (storage, questioner,
  five minutes), folding the 70 percent bar into the next sentence. The count
  was wrong against its own list. Fixed by calling the three setup items
  conditions, which the following sentence ("Under those conditions...") already
  assumed.

- The refusal and substitution. "Too meaningless to deserve discussion," the
  machine-takes-A question, and the three-party man/woman quote all match the
  primary.

- The arithmetic flip, the piece's original work. Turing's "interrogator right
  no more than 70 percent" is the complement of "machine fools at least 30
  percent," so the 30 percent floor is sound. GPT-4.5 with no persona was picked
  as human 36 percent of the time, which clears that floor; with the persona it
  reached 73 percent. In the three-party forced choice, "picked as human" is the
  same quantity as "interrogator wrong," so comparing the study's rate to
  Turing's bar is legitimate, and the article is careful to present the 30
  percent floor as its own derivation, not a sourced claim. The flip is honest.

- The conditions comparison. Time (five minutes) matches; judge (average
  interrogator vs. recruited undergraduates and paid Prolific workers), machine
  (unspecified vs. GPT-4.5 under a persona prompt), and the metric all differ,
  and the table and body report each accurately.

Display text, descriptor by descriptor. The forecast quote, the Lovelace quote
and Turing's reply, the "test of humanlikeness / ability to deceive" note, the
2024 two-party figures (54 percent GPT-4, 67 percent human, "the machine lost"),
and the Hayes & Ford quote all match the record. Three fixes. The draft put "a
computer" inside quotation marks around Turing's phrase; Turing wrote "programme
computers," so I pulled "a computer" outside the quotes and left only the
verbatim "with a storage capacity of about 10^9" inside them. The 73-to-36 drop
carried the locator "Figure 6," which the record assigns to the persona-prompt
text, not the win rates that live in Figure 2 and Table 1; I widened the locator
to name both. The dek called the interrogators "paid volunteers," but the record
supports payment only for the Prolific half, not the undergraduates, so I changed
it to "recruited participants," the honest span.

The headline sets 70 next to 73 as a near-tie, and the two figures sit on
opposite axes (interrogator-right vs. AI-picked-as-human). I kept it: the dek
names the changed conditions and the body works the inversion explicitly, so the
provocative pairing is a hook the piece immediately complicates, which is the
move the voice guide models. To keep the comparison honest where a reader might
screenshot the table alone, I added the interrogator's 27 percent right-rate
beside the 73 percent in the Bar cell.

The `data-nb-kind` labels are correct: five primaries (both Jones & Bergen
preprints, the PNAS version, Turing, Hayes & Ford) and two secondaries (Live
Science, Stanford Encyclopedia). The source floor is met. Every citation href
resolves under the proof's link check. Nothing broke that needs the researcher
or writer.

## Cut

Roughly four sentences failed the slop or punctuation test and were cut or
tightened; none needed routing. "The game is a parlor trick before it is
anything else" reduced to a pattern any subject fits ("the X is a Y before it is
anything else") and also renamed the parlor game a trick a line after the heading
set the name, so I replaced it with a factual lead-in that keeps the name. "One
widely shared headline" claimed a reach the record does not establish, so
"widely shared" went. "The actual human sitting across from them" imported a
face-to-face image into a test the piece insists is text-only, so it became "the
real human in the same game." "Two baselines built to fail" overstated GPT-4o,
a capable model run without the persona prompt, not one engineered to lose, so
"built to fail" went.

Two semicolons splicing independent clauses were resolved to periods, per the
house punctuation default: the parlor-game description and the 2024 GPT-4 versus
human rates. No em-dashes in the body, and the one banned-term hit is the
document's own title.

Two headings against the recent-pattern notes. The closer "What the study's own
authors say it shows" used the flagged "What X..." mold and undersold a section
whose spine is that the test measures deception, so it became "Its own authors
call it a deception test," in the piece's own nouns. The opener "A parlor game,
played by teleprinter" and the other body headings avoid the "What X actually
built" mold. The dek avoids the banned comma-triad and semicolon-reversal molds
and commits to the specific find.

The takeaway's last sentence said the two questions to ask are "the ones Turing
actually specified," but one of them, the machine's instructions, is precisely
what Turing left open, so the sentence contradicted the article's own point. I
changed it to "the ones that decide what the score means." No prompt leakage
survived: the reader-facing "two questions" framing is the article's payoff, not
a lifted planning label, and the two bookends are the only self-addressing prose,
as the lesson template allows.

## Reader

What the piece gives beyond its sources: the two documents' exact numbers laid
side by side, plus the arithmetic that neither source performs, so a reader can
see that GPT-4.5 clears Turing's modest bar with no coaching while the 73 percent
headline is a separate, persona-dependent result. That matches the original-work
sentence in the draft handoff, and both answers survive the read. The prose sits
closer to the voice-guide exemplars than to a median summary: it states a figure
and its consequence back to back, ties each number to a named condition, and
finds the ordinary version of the imitation game before the vocabulary arrives.
The headline reads as the largest claim and the body defends it.

## Edits

- Orientation: "the actual human sitting across from them" changed to "the real
  human in the same game."
- Orientation: "one widely shared headline" changed to "one headline."
- Orientation: replaced "The game is a parlor trick before it is anything else"
  with "Turing borrowed the game from a parlor game about telling a man from a
  woman," and split the following semicolon into two sentences.
- The one number: "The bet has four parts" changed to "The bet has three
  conditions" to match the three items listed.
- The persona section: "two pre-registered rounds" changed to "two
  pre-registered studies."
- The persona section: "Two baselines built to fail" changed to "Two baselines."
- The persona section: moved "a computer" outside the quotation marks around
  Turing's "with a storage capacity of about 10^9."
- The persona section: widened the 73-to-36 locator from "Figure 6" to "Figure 6
  (persona prompt); Figure 2, Table 1."
- Dek: "paid volunteers" changed to "recruited participants."
- Comparison table, Bar row: added the interrogator's 27 percent right-rate
  beside the AI's 73 percent picked-as-human.
- Deception section: split the semicolon between the 54 percent and 67 percent
  2024 rates into two sentences.
- Deception section heading: "What the study's own authors say it shows" changed
  to "Its own authors call it a deception test" (and its `data-nb-section` label
  to `deception-test`).
- Takeaway: "the ones Turing actually specified" changed to "the ones that
  decide what the score means," with the two trailing clauses corrected to
  indirect-question order.

## Required work

None. No item routes to the researcher, the writer, or the orchestrator. The two
standing WARNs are correctly left: the 78-word forecast is Turing's verbatim
sentence, and the single 'machinery' use is the paper's own title.

## Decision

approve — the claims hold against the primaries, the original arithmetic is
sound, and the display-text, slop, and punctuation fixes were all within editing
reach, leaving a clean PUBLISHABLE proof.
