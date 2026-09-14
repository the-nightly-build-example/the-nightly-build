# Editorial review: what-could-go-wrong/deskilling (editor/01)

## Skeptic

Thesis: the deskilling argument is old and sound as reasoning, measured outside
AI in a form narrower than the slogan, but for AI itself the measured evidence is
almost nothing (one observational colonoscopy study plus a contested essay
preprint), and the version repeated most, coding assistants eroding programming
skill, has never been measured. The piece stands on four claims, and each held.

1. Bainbridge originates the argument and it is reasoning, not measurement. The
   paper (s1) resolves and downloads; the three quotes and the "residue" framing
   match the evidence record's locators and the article does not present the 1983
   paper as proof. Held.
2. Outside AI, the measured loss is cognitive, not stick-and-rudder. Casner (s2)
   is cited for exactly this, and the article states the finding cuts against the
   slogan. Asiana (s3) is handled as an accident where automation reliance was a
   named contributor to the monitoring failure, with the one-line probable cause
   quoted as in-the-moment mismanagement, not as proof that deskilling downs
   airliners. This matches the evidence record's Contradictions note. Dahmani &
   Bohbot (s4, was s5) carries the three-year longitudinal arm and the
   reverse-causation check. All confirmed against the sources. Held.
3. The strongest AI-specific measurement is the colonoscopy study. The numbers
   (28.4% to 22.4%, 6.0 points, CI 1.6-10.5, 19 endoscopists over 2,000 each,
   four Polish centers, US benchmark near 35%) all check against Budzyn (s5) and
   Zhou (s6) and the press release (s7), including "about a fifth" for the 21%
   relative drop. The article distinguishes this from automation bias correctly.
   Held. The headline claim ("the strongest evidence... is a single colonoscopy
   study") is the evidence record's own framing and is defended in the body.
4. The coding claim is unmeasured; METR is not deskilling evidence. METR (s10)
   is confirmed (16 developers, 246 tasks, expected ~24% speedup, believed sped
   up, actually ~19% slower) and is kept out of the deskilling column, labeled a
   productivity-and-perception result. Held.

Breaks and fixes:
- Kosmyna critique mislabeled. The article called Stankovic et al. "a published
  critique," which implies peer-reviewed standing the source does not have: it is
  an arXiv comment (submitted Dec 29, 2025), the same preprint status the article
  correctly notes disqualifies Kosmyna. I opened it and confirmed. Changed to "a
  separate critique," which the numbered citation to s9 already attributes. Fixed
  in place.
- Table caption carried an inline citation to the colonoscopy study on a line
  that is the article's own synthesis of the whole table, not a Budzyn claim, and
  every row is separately cited. Removed the stray superscript. Fixed in place.

data-nb-kind audit: all correct against the authorship-and-stake test. Eight
primary (Bainbridge, Casner, NTSB, Dahmani & Bohbot, Budzyn, Kosmyna, METR, plus
the dropped FAA alert) and three secondary (Zhou, EurekAlert, Stankovic). After
the length cut below the article carries seven primary and three secondary, ten
total, which clears the floors (>=4 primary, >=1 secondary, >=8 total). Every
href opened: the fetchable ones (s4 Dahmani, s6 Zhou, s7 EurekAlert, s8 Kosmyna,
s9 Stankovic, s10 METR) resolve and land on the source; Bainbridge (s1) and the
NTSB report (s3) return the real PDFs; the Sage (s2), FAA (now dropped), and
Lancet (s5) publisher pages are gated 403, which resolves-but-gated and does not
fail. The colonoscopy figures were confirmed against s6 and s7, which carry them.

Automation bias and technological unemployment are held apart and linked: the
former in the Why-this-matters Background row and again in the colonoscopy
section, the latter in Background and in the orientation section as "a different
argument."

## Cut

Roughly four sentences drew the slop pass; none were structural.

- "Her point was mechanical, not moral" invented the "moral" reading to contrast
  against, the negative-parallelism reflex the series is flagged for. The claim
  needs no foil, so cut to "Her point was mechanical."
- Dropped the Casner paragraph's closing sentence ("The skill most at risk was
  the attention and judgment Bainbridge called the residue; the physical touch
  everyone pictures losing held up well"). It restated the two findings the
  paragraph had just delivered and re-attached the "residue" label already set in
  orientation. A paragraph-edge sentence that reasons nothing new.
- "The version you are most likely to hear" addressed the reader inside the body,
  which the lesson template reserves for the two bookends. Recast to "The version
  repeated most often," which keeps the claim and drops the second person.
- Trimmed "a change in what they did on their own, which is the deskilling claim"
  to end at "on their own"; the next sentence already draws the deskilling/
  automation-bias boundary the clause was doubling.

The remaining edges hold. The takeaway's last sentence states the conclusion the
argument built (has anyone measured it in the case being argued, and for most the
answer is still no) and stays. The section headings are each a step in the
piece's own nouns and none uses the "X, not Y" or comma-plus-"and" builds the
recent record overuses. The dek commits to a stance and avoids the suspended
question. No prompt leakage or borrowed phrasing from the voice-guide exemplars.

## Length

The blocking task this round. The article was 2286 words against a 2200 ceiling.
I dropped the FAA field-position paragraph (source s4 in the old numbering), the
handoff's first-named candidate: it was explicitly the weakest link, "a field
position, not a controlled experiment" that "points the same way Casner did," so
its removal loses corroboration but no claim the piece rests on. That plus the
slop cuts above brought it under the band. `./nb check ... --no-check-links` now
returns BLOCK 0, WARN 0, PUBLISHABLE; the length warning is gone. I renumbered
the seven trailing sources into first-citation order and confirmed every inline
superscript, every list id, and the table cells point to a source that exists and
matches the claim.

## Reader

Read straight through, the piece leaves you able to run Bainbridge's reasoning
and, more than that, to sort any "AI is deskilling us" claim into measured-outside-
AI, measured-but-preliminary-for-AI, or unmeasured forecast, and to see that the
loudest case sits in the last bin. That is more than the sources give on their
own: they are scattered across aviation, navigation, endoscopy, essays, and
coding, and the article's work is the sort and the epistemic ranking, which the
draft-handoff's original-work sentence names as the intended contribution. Both
survive the read. The prose sits closer to the voice-guide exemplars than to a
median summary: plain claims with the figure attached, the turn from measured to
forecast carried in a sentence rather than a section break, and the uncertainty
stated as the specific study that does not exist yet.

## Edits

- Cut "not moral" from "Her point was mechanical, not moral"; changed "the less
  you use it" to "the less it is used."
- Deleted the Casner paragraph's closing "residue" sentence.
- Removed the FAA field-position paragraph and its source (old s4).
- Removed the stray colonoscopy citation from the synthesis-table caption.
- Recast "The version you are most likely to hear" to "The version repeated most
  often."
- Changed "a published critique" to "a separate critique" (Stankovic is an arXiv
  comment, not a peer-reviewed publication).
- Trimmed "on their own, which is the deskilling claim" to "on their own."
- Renumbered sources s5-s11 to s4-s10 in first-citation order across all inline
  citations, the table, and the source list.

## Required work

- orchestrator: run `nb stamp` before the final proof so nb-meta catches up with
  the edits (sources 11 to 10, and the lowered word count). This is the stated
  post-edit step; noted only so the source-count change is expected.

No researcher or writer work outstanding. No charts or source assets in this
article, so nothing for the writer's capture tooling.

## Decision

approve — the length overage is cleared without losing a claim, the three
evidence tiers are held apart and none is overstated, every citation resolves and
its kind is correct, and the two accuracy fixes (the critique's status, the
caption citation) were made in place.
