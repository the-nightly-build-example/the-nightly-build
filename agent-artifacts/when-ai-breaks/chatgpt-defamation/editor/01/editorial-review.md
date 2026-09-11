# Editorial review: when-ai-breaks/chatgpt-defamation (editor/01)

## Skeptic

Thesis: a chatbot generates a false, defamatory statement about a named real
person exactly as readily as a true one, and civil liability for that is
unsettled and largely untested; the only U.S. suit to reach a merits ruling
cleared OpenAI on grounds tied to the facts of Walters's own case, not on
anything that settles the doctrine.

The claims it stands on, and how each held:

1. **ChatGPT fabricated an embezzlement accusation against Mark Walters,
   including a fully formatted, nonexistent complaint.** Held. The complaint
   (s1) owns the output: it quotes ChatGPT calling Walters SAF's "Treasurer and
   Chief Financial Officer" and alleging embezzlement "in excess of $5,000,000,"
   and states Walters held neither role and had no tie to SAF. The href returns
   the real PDF (verified by browser request; the fetch tool's 403 is a bot
   block, not a dead link). Headline, dek, and the "What ChatGPT generated" note
   all track the primary.

2. **The pattern of three others, and that they differ in kind.** Held. Turley
   (s3, his own account; s4 corroborating) — GWU professor, Alaska-trip
   fabrication, nonexistent March 21 2018 Washington Post article, Georgetown
   misattribution, surfaced by Volokh, never sued. Hood (s5) — Hepburn Shire
   mayor, whistleblower cast as convict, concerns notice 2023, dropped Feb 2024
   over cost, never filed. Holmen (s6) — 2025 noyb GDPR complaint, not
   defamation. Reopening each source, the load-bearing distinction survives:
   only Walters reached the merits, so the question is not merely unsettled but
   untested. This is the article's real contribution and it is stated cleanly.

3. **A chatbot libels as easily as it praises because the mechanism is
   indifferent to the difference.** Held. The piece links, and does not
   re-teach, the-mechanics/hallucination, then spends its own words on the
   distinct harm: a false statement of fact about a named person, delivered to
   one reader, is the injury itself. Grounded, not padded.

4. **The ruling decided less than its popular framing; liability is open.** This
   is the guardrail the brief flagged, and it holds throughout. The three
   grounds (defamatory meaning, fault, damages) are reported from the order (s2)
   with the verbs kept honest — the court "held," Walters "conceded," his
   lawyers "argued." The order's authorship ("drafted by OpenAI's own lawyers,"
   signed "as edited by the court") is stated. The steelman is present and
   real: the amicus position card (s9) and the Volokh / Andersen Jones scholars
   (s4). No sentence reads as "AI beats defamation." I tried to break this by
   reading the order's reasoning for a broader holding and found none the
   article overclaims.

Display text checked descriptor by descriptor. Headline: ChatGPT did allege
embezzlement of millions ($5,000,000) from a group (SAF) Walters never worked
for — accurate. Dek: adds the ruling and the untested question without
restating the headline; not a banned mold; its "such lawsuit" referent sits
directly under the headline, so it does not dangle. Subheads each name a
concrete step; the closing heading is built off "citations that do not exist,"
not the air-canada "same setup running right now" stamp.

Breaks found and handled:

- **"First Amendment scholar" for RonNell Andersen Jones was not supported by
  the owning source.** s4 (ABA Journal) identifies her as a University of Utah
  law professor. Fixed directly to that sourced descriptor.
- **"Colleague" for Volokh** implied a shared institution (he is UCLA, Turley
  GWU). Changed to "Another law professor," which the record supports.
- **"put an AI company on trial for defamation"** misdescribes a case that ended
  at summary judgment before any trial. Reworded to "the first defamation case
  in the United States against an AI company," preserving exactly what s8 is
  cited for (OpenAI counsel's first-of-its-kind framing).

Writer-flagged items resolved:

- **Riehl-date conflict (complaint May 4 vs order May 3).** The draft states no
  specific day ("early May 2023"), which is accurate for either and states no
  contested date, so there is nothing to correct. This is a primary-vs-primary
  conflict; the vague form is the honest resolution and I left it. No date was
  altered.
- **Scale figures (~200M weekly users, ~three-quarters share).** Attributed in
  prose as the amicus brief's own figures "drawn from outside reports," and the
  s9 note repeats the caveat. Not stated as independent fact. Correct.
- **No invented OpenAI voice.** Confirmed against s8: the Gibson Dunn page
  carries no direct OpenAI corporate quote, and the article attributes every
  such line to "OpenAI's counsel" / "OpenAI's own lawyers."

Citations and labels: all nine hrefs land on the source itself. Five are PDFs of
the primary documents (complaint, SJ order, MTD-denial order, noyb complaint,
amicus) and each resolved to a real PDF at its printed address; the HTML sources
(Turley, ABA, Canberra Times, Gibson Dunn) and the popehat Background link were
read and match what they are cited for. `data-nb-kind` audited: the amicus is
primary to its authors; the Gibson Dunn post and the ToU disclaimer are
primary-to-OpenAI and interested, and the article uses the firm post only for
the counsel's own characterization, which is disclosed. Source floor met (7
primary, 2 secondary, 9 total).

## Cut

A dedicated slop pass, then the edge pass, then the delete test. The prose was
already disciplined; the failures were signposts and self-grading at section
seams, plus one over-full takeaway. Sentences cut or rewritten for failing the
test:

- "This lesson works through the record and asks what that ruling did and did
  not decide." — method narration in the opener; the next sentence already says
  what the reader will understand. Cut.
- "What is worth adding here is narrower." — a signpost grading the article's
  own scope. Cut; the sentences on either side carry the point.
- "One feature of the order is worth stating plainly." — signpost. Cut; the
  sentence now leads with the fact (who drafted the order).
- "The reach is large." — empty conclusion ("the X is Y"); the figures that
  follow carry it. Cut.
- "Legal scholars have raised the same doubts." — near-vague-attribution
  lead-in; the named scholars follow immediately. Cut.
- "differ in a way that matters here" — folded away by merging the sentence into
  the concrete distinction it was announcing.
- "The same indifference that lets it invent a flattering detail lets it invent
  a felony." — an engineered line duplicating both neighbors; the concrete
  Walters/Holmen/birthday sentence makes the same point better. Cut, and the
  surrounding mechanism sentences compressed (the mechanism is linked, not this
  lesson's to re-teach).
- Takeaway: removed the four-case re-list and "Whether anyone can be made to pay
  for that is mostly unanswered," which restated the body and the closing
  sentence. The takeaway now lands the judgment without summarizing the body.
- Small tightenings: "None of it was true" (redundant), "and ended the case
  before trial" (the note already defines summary judgment that way), two
  bookend merges.

Grammar/syntax fix: "makes them clear a higher bar called" rewritten to
"requires them to clear a higher bar," which reads correctly.

Furniture: three components, each earning its place. The "What ChatGPT
generated" note shows the fabricated document verbatim (the artifact at the
center of the case). The "In plain language" note defines defamation, actual
malice, and summary judgment for a non-lawyer reader — required teaching. The
amicus position card carries the steelman cleanly. No stat strip, correctly; the
scale figures live in attributed prose. I considered requesting the Exhibit-1
image the evidence names, but the verbatim quotation note already carries that
evidence in text, and the piece is over-band, so an added asset would be
optional weight — declined.

No recurring formula against the recent-pattern notes: the dek avoids the
two-clause and comma-triad molds and the "when X did Y, a court did Z" shape,
and the closing heading breaks the "same setup running right now" stamp.

## Reader

Read straight through as the paper's declared reader: what I have that the
sources alone would not give me is the synthesis — that a chatbot states a false
crime about a real person with the same confidence it states a true fact, and
that the single ruling clearing OpenAI settled nothing about liability because it
turned on three facts peculiar to Walters in an order OpenAI's lawyers drafted,
so for almost everyone a chatbot names falsely the law has no answer yet. That
matches the draft-handoff's original-work statement, and neither the reader
answer nor that statement is a restatement of any one source; the piece assembles
scattered filings, a firm's victory post, an amicus, and news reports into one
argument. The prose sits closer to the voice-guide exemplars than to a median
summary: the fact/allegation/holding discipline is Howe's, the plain statement
of what the ruling does not establish is White's, and the harm is carried in
concrete facts, not heightened ones, in Somers's register. Headline reads true
as the largest claim.

## Edits

- Why bookend: cut the "works through the record" method sentence; merged two
  sentence pairs.
- Orientation: cut "None of it was true" (redundant).
- Pattern: "the same thing to other real people" tightened to "this to other
  people"; "A colleague, Eugene Volokh" changed to "Another law professor,
  Eugene Volokh."
- Pattern synthesis: merged the "differ in a way that matters here" signpost
  into the concrete distinction.
- Why-libel: cut "What is worth adding here is narrower"; compressed the
  mechanism paragraph and cut "The same indifference..." (cites s1/s6 retained).
- Ruling: "put an AI company on trial for defamation" -> "the first defamation
  case in the United States against an AI company"; cut "and ended the case
  before trial"; "One feature of the order is worth stating plainly" removed,
  sentence now leads with the fact; "makes them clear a higher bar called" ->
  "requires them to clear a higher bar,".
- Scholars: cut "Legal scholars have raised the same doubts"; "First Amendment
  scholar" -> "a University of Utah law professor" (sourced to s4).
- Today: cut "The reach is large."
- Takeaway: cut the four-case re-list and the "mostly unanswered" sentence.

## Required work

None is publication-blocking.

- **writer (non-blocking): fresh proof required.** The edits changed the word
  count and prose, so the article needs a re-stamp and re-check. My local
  estimate puts it near, and probably still modestly above, the 2200 ceiling
  (down from 2434). If it lands over, the W-LENGTH-HIGH warning may stand: the
  four commission-required cases, the full three-ground analysis the brief
  protects, and the required steelman leave no non-essential section to drop, so
  the residual overage is required substance, not slack. The orchestrator's
  fresh proof sets the authoritative number.

## Decision

approve — no publication-blocking issue remains; the skeptic breaks were fixable
in place, the liability guardrail holds, and the length was cut as far as the
required substance allows, with a recorded reason if the band warning stands.
