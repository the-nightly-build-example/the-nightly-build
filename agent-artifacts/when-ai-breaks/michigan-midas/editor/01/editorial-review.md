# Editorial review: when-ai-breaks/michigan-midas (editor/01)

## Skeptic

Thesis: Michigan's MiDAS auto-adjudicated unemployment fraud with no human
examiner from October 2013 to August 2015; removing that examiner, not the
data-matching itself, is what turned an irreducible false-positive rate into
mass harm, and a fourfold penalty plus dormant-account notice made each wrong
flag catastrophic. The state's own reviews later reversed the large majority of
the computer-alone findings.

The claims it stands on, and how each held:

- MiDAS decided fraud with no human, Oct 2013-Aug 2015. Verified against the
  Sixth Circuit opinion (s5, p.4-5: "From October 2013 to August 2015, MiDAS
  exclusively determined whether claimants engaged in fraud") and the district
  opinion (s4, p.7). Holds.
- Penalty was four times benefits, the state-law maximum, assessed even with no
  benefits received; assessments $10,000-$50,000, some over $187,000. Verified
  verbatim in s5, p.5. Holds.
- The two state reviews are distinct and must not be conflated: Dec-2016 = 93%
  of 22,427 (s4/s6); Aug-2017 = 85% of 40,195 computer-alone findings and 44% of
  22,589 investigated, within 62,784 non-appealed cases, 49,910 people, $20.8M
  refunded. Every figure in s7 confirmed exactly against the agency press
  release. The article holds them strictly apart and gives each its owner,
  period, and denominator. Holds.
- The "93%" mis-attribution: both federal opinions credit the Auditor General
  (confirmed in s4 p.6 and s5 p.6); the only OAG MiDAS audit (s2, Feb 2016) is an
  IT-security/controls performance audit with no fraud-error rate (confirmed on
  its objective/findings pages), and the Michigan Supreme Court credits "a study
  conducted by the Agency" (s1 fn5). The article states this correctly. Holds.
- Three vendors: FAST built/ran the MiDAS platform (~Aug 2011), SAS built the
  EFDS fraud engine (~Dec 2012), CSG ran oversight (~Jan 2010). Verified against
  s4 pp.7-9. The article's precision is right; I corrected the engine's name from
  "System" to "Software" to match the primary.
- Two opposite legal endings: MSC 2022 let claimants sue the state for damages
  (s1, verified) plus a $20M settlement (s8, verified); the Sixth Circuit 2023
  reversed qualified-immunity denial for Moffett-Massey and Geskey on a fuller
  record showing notice-before-deprivation, a 30-day appeal, and a
  collection-of-paid-benefits recharacterization (s9, verified). Both steelmanned
  at strength; the article correctly says neither court settled the count and
  names the missing evidence (unpublished case-level review data).

Breaks found and fixed. The article printed "20,965" as the count overturned in
the Dec-2016 review, cited to s4, but s4 states only "22,427" reviewed and "over
93%" — the exact 20,965 appears nowhere in the opened primary and is unsourced in
the evidence record. I cut the orphan number and kept "more than 93 percent of
22,427," which s4 fully supports. Separately, the "$5.4 million to 2,571 people"
clause cited s6, which supports the $5.4M and 53,633-flagged figures but not the
2,571 count on my read; I cut "to 2,571 people" and kept what s6 confirms.

Every citation href (s1-s9) and both Go-deeper links were opened and land on the
source itself. The four browser-gated URLs (s2, s7, s8, and the STPP explainer)
return 200 to a browser request and only 403 to an automated agent. All nine
data-nb-kind labels are correct: s1/s2/s4/s5/s7/s8/s9 are primary (court
opinions, a state audit, official agency and AG releases), s3/s6 secondary (news
outlets).

Headline judged as the largest claim. "Two years" overstated the ~22-month
automated window (Oct 1 2013-Aug 7 2015); the sources say "close to" and "nearly"
two years, and the body already reads "nearly two years." I changed the headline
to "nearly two years" for honesty and internal consistency, syncing the title
tag, nb-meta title, and h1.

No broken central claim requiring the researcher or a redraft.

## Cut

Press-file compliance, the round's first must-check: the body closed its last
section with a "Verdict" nb-note-strong block restating the finding. press/
editorial.md bans exactly this ("Do not close the body with a Verdict note, or
any block that restates the finding"), overriding the engine catalog's optional
Verdict furniture. I removed the block and recast its substance, the two rulings
answering different questions and the unpublished case-level data being what
would settle the count, as plain body prose ending the section. The lesson's
judgment now lives in body prose and the takeaway bookend, as the press file
directs.

Prompt leakage: the sentence ending "...every use of one has to carry its own
denominator, period, and owner" lifted the writer-brief's methodology instruction
into the article as if it were content; I cut that clause, leaving the
substantive non-conflation point intact. I also cut the lecturing opener "Notice
what these figures are not."

Signposts and self-direction cut: "One step deserves a close look, because..."
(led with the substance instead); "...and it is worth being exact about why";
"...and both are real"; and "The state's strongest counter is worth stating at
full strength" (folded into a substantive sentence naming the federal track).

Template self-reference: the body said "the number this lesson turns on." The
lesson template confines self-reference to the two bookends and says the body
never mentions the lesson; I changed it to "the number that matters most."

Roughly six edge/signpost sentences failed the slop or self-reference test, plus
the one leaked clause. The recurring pattern was self-directional throat-clearing
at section and paragraph openings ("worth a close look," "worth stating at full
strength"); each was replaced by leading with the reported substance, not by a
prettier signpost. No Robodebt echo: the opener is one claimant's determination
letter (not "a debt the recipient had to disprove"), the mechanism section is
"How a data mismatch became a fraud finding" (not the income-averaging spine),
and the closer names Michigan's own three parts (not "the same bargain still
runs"). The dek uses only the Aug-2017 85%/40,195 figure and matches no banned
dek mold. Furniture after edits: two bookends, one quotation note, one pull
quote, one table, no Verdict block, which reads as an article rather than a stack.

## Reader

Read straight through as the paper's declared reader, the piece gives what the
sources never assemble in one place: the causal isolation of examiner-removal
(not the matching, not the averaging alone) as the step that scaled an
irreducible false-positive rate into mass harm, plus the two amplifiers and a
rigorous separation of the two state reviews with the Auditor-General
mis-attribution corrected. That matches the draft-handoff's original-work
statement, and both survive. The prose sits closer to the voice-guide exemplars
than to a median summary: figures land plainly beside a scale the reader can hold
(four-times penalty, $10,000-$187,000 debts, 85% of 40,195), the human anchor is
built from Grant Bauserman's own particulars, and "fraud the accusation" is kept
distinct from actual fraud. The corrected headline is an accurate largest claim.

## Edits

- Headline "two years" to "nearly two years" in the title tag, nb-meta title, and h1 (honest to the ~22-month window; consistent with the body).
- "Enterprise Fraud Detection System" to "...Software" to match the primary (s4).
- Cut the unsourced "20,965" from the Dec-2016 sentence; kept "more than 93 percent of 22,427" (s4 supports this, not the exact count).
- Cut "to 2,571 people" from the $5.4M refund clause (s6 supports $5.4M and 53,633, not 2,571).
- Body self-reference "the number this lesson turns on" to "the number that matters most."
- Cut the lecturing opener "Notice what these figures are not."
- Cut the prompt-leak clause ", and every use of one has to carry its own denominator, period, and owner."
- "One step deserves a close look, because it manufactured fraud out of arithmetic" to "One step manufactured fraud out of arithmetic."
- Cut "and it is worth being exact about why" from "Removing the examiner is the change that scaled the harm."
- Cut "and both are real" from the two-endings section opener.
- "The state's strongest counter is worth stating at full strength." to "The state's strongest counter came in a separate federal track." (merged into the following sentence).
- Removed the "Verdict" nb-note-strong block and recast its content as plain body prose closing the two-endings section (press-file compliance).

## Required work

None blocking. All items were resolved by direct edit. The orchestrator's stamp
will refresh nb-meta word count and reading time after these cuts (the piece
stays inside the 1200-2200 band). Optional, researcher: if the "2,571 people"
early-refund count is wanted back, supply its owner and locator; it was cut
because s6 as opened did not carry it and the $20.8M/49,910 people figures (s7)
already give the authoritative counts.

## Decision

approve. Every publication-relevant issue, the banned Verdict block, the
headline overstatement, the vendor name, the two unsourced figures, the body
self-reference, and the prompt leak, was fixed directly; all central claims
verified against the opened primaries, the two reviews are held apart, and no
Robodebt echo remains.
