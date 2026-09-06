# Editorial review: when-ai-breaks/shotspotter-wrongful-arrest (editor/01)

## Skeptic

Thesis: a ShotSpotter alert is a weak, base-rate-driven lead that cannot carry a
criminal charge, and Michael Williams spent eleven months in Cook County Jail
because a probabilistic flag, edited by hand, was treated as if it had located a
shooting; the same failure recurs wherever an automated signal enters a case as
though it were already confirmed.

The piece stands on four claims. I opened the cited sources and checked each
descriptor against its owning document.

1. **Williams's legal status.** Held pretrial about eleven months, charge
   dismissed July 2021 for insufficient evidence, never tried, never convicted.
   Confirmed against the AP investigation and the MacArthur case page. The draft
   states it exactly ("He was never tried and never convicted") and never
   inflates it to a conviction or a loose "arrest." His age is reported as 63,
   65, and 66 across sources; the draft uses "63 by his own account," which is
   the correct sourced handling of a genuinely conflicting figure. Held.

2. **The human edits to the alert.** The court-record quote (firecracker
   relabeled a gunshot) matches the AP verbatim. Walter Collier, a senior
   ShotSpotter engineer, moved the reported location about a mile to where
   Williams was driving; confirmed against the AP, which the company reframes as
   correction rather than denies. The headline ("began as a firecracker") and dek
   ("moved a mile to the street where he was driving") are both true to the
   record. Held. I checked the body clause "the intersection where the
   surveillance video showed Williams's car": the AP describes the evidence as
   "video of a car driving through an intersection," so the phrasing is
   supported, not an invention.

3. **The oversight figures, and what they measure.** OIG: 50,176 alerts
   confirmed and dispatched Jan 2020-May 2021; 41,830 with a disposition; 4,556
   found gun-crime evidence. Verified against the OIG report itself. Here the
   draft broke: it wrote "Of the 41,830 that ended with a recorded disposition,
   4,556 turned up evidence of a gun-related crime. That is 9.1 percent." But
   4,556/41,830 is 10.9 percent. The 9.1 percent is 4,556 of the 50,176 alerts
   police responded to, which is how OIG states it ("9.1% of CPD responses to
   ShotSpotter alerts"). The percentage was attached to the wrong denominator.
   Fixed in place without changing any figure: the sentence now reads "9.1
   percent of every alert police responded to," and the stat strip (which already
   paired 9.1% with 50,176) is now consistent with the prose. MacArthur's
   89%/86%/>40,000 over ~21 months verified against the study release. The
   downstream-outcome framing (these count whether police found a gun crime, not
   whether the sensors heard gunfire) is stated correctly. Held after the fix.

4. **The detection-accuracy crux is unsettled.** The company's 97% (2019-2021,
   customer-reported false-positive rate below 0.5%) verified against the FAQ; the
   claim that no independent controlled test distinguishing gunfire from
   firecrackers has been published verified against the MacArthur release. The
   draft's sentence "by its own definition, an alert counts as a false positive
   only when a police customer reports back" miscited the company's OIG rebuttal
   (s6), whose actual definition is objective (an alert sent when no gunfire
   occurred). The reporting-dependent point belongs to the FAQ's own phrase
   "customer-reported false positive rate" (s4) plus MacArthur's finding that such
   reports are rarely filed (s5). Reworked and re-cited to s4/s5; s6 now carries
   the argument it actually makes (missing physical evidence blamed on slow
   response or uncooperative witnesses, not detection error), which also removed a
   redundant restatement of the "an alert is itself evidence" position that the
   adjacent Position block already states from s7. Held after the fix.

I also audited the 2026 turn the brief flagged. SoundThinking's settlement
statement (not a party to the suit; ShotSpotter "not designed to detect gunfire
within an enclosed vehicle"; "responsible for Mr. Williams's release" through its
"unprecedented step" of contacting prosecutors; arrest came "nearly three months
after the alert") is present in the company's own words and does not stand as the
last word: the draft holds both the "helped charge him in 2020" and "helped free
him in 2021" accounts as compatible and closes that neither shows the alert
earning a murder charge's certainty. This is the correct handling.

Citations: all ten hrefs point at the source they name. apnews.com (s1),
macarthurjustice.org (s2, s5), chicago.gov (s8), and wttw.com (s9) return an
anti-bot 403 to automated fetch but resolve for a human reader and were confirmed
live and on-topic; the rest I read directly. The data-nb-kind labels hold: AP and
WTTW are the two independent secondaries, the company statements are primary for
the company's own positions, and no "primary" label hides a missing independent
source (the Williams narrative rests on the AP and the court record, not on a
company page).

One figure I tightened toward its primary: the 68-county study (Doucette et al.,
in the OIG report and the AP) measured firearm homicides and arrests, so "no
measurable drop in gun violence" overstated its scope. Changed to "gun
homicides."

## Cut

Six sentences failed the slop test or the punctuation standard; I cut or trimmed
each.

- The section opener "The critics and the company are not measuring the same
  thing, and that gap is the whole dispute" carried the "X is the whole Y"
  punchline the slop file names. Cut the tail; the first clause states the point.
- "The numbers from Chicago show the gap plainly" was a signpost that graded the
  evidence ("plainly") without doing any reasoning; the OIG figures that follow
  make the point themselves. Deleted.
- "worth carrying forward" (before the police-behavior finding) telegraphed the
  closer and editorialized about relevance. Trimmed.
- "But that is exactly why" softened toward the "that's the whole point" family.
  Dropped "exactly"; the sentence still carries the base-rate step.

Edge test: I read the first and last sentence of every paragraph, section, and
the whole piece out of order. The surviving edges each carry a fact or a
reasoning step. The closer the writer flagged for me ("The same shape recurs
wherever an automated signal ... enters a case as though someone had already
confirmed what it claims") is earned, not a reach: the piece taught the mechanism
(probabilistic flag, treated as fact, entered as evidence), and the three example
systems it names are ones the course has already covered and links here. It makes
no current-deployment factual claim that would need the 2021 footprint figure to
prop it up, so it needs no new source and no softening.

Prompt-leakage check against the commission, brief, and voice guide: none. The
desk's "machine flag hardening into evidence" framing is re-expressed in the
piece's own concrete mechanism rather than lifted. The bookends' reader address
is the one self-reference the lesson template allows, and each bookend sentence
says something specific to this incident.

Formula check against the recent-pattern notes: the dek is a concrete
actor-named sentence with no comma-triad, semicolon-reversal, or suspended
question, and no "Company did X, and Y happened" rhythm. The five headings are
built differently from one another and from the named neighbors, each in this
incident's nouns. No decorative "underscoring/highlighting" verbs and no
elaborate copula. The takeaway lands its judgment as prose, not as a Verdict
block, and the body addresses no one.

Furniture: the court-record note, the stat strip, and the SoundThinking Position
block each do work the prose would carry less well, and none makes the piece read
as a stack of blocks. I left them.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not give me: the two questions the record quietly conflates,
pulled apart and named. Whether an alert leads police to gun-crime evidence
(9.1%, 89%) and whether the sensors can tell a gunshot from a firecracker (never
independently tested) are different measurements, and the piece shows why neither
number could carry Williams's charge. That is also the original-work sentence's
claim, and it survives. The prose sits closer to the voice-guide exemplars than
to a median summary: the opening reconstructs the sequence from nouns, the base
rate is worked through the actual Chicago counts rather than asserted, and the
company and its critics are set side by side without the narrator refereeing
first. The headline, reread as the largest claim, is one the piece defends.

## Edits

- Cut "silent" and "police" from "a silent police surveillance video": neither
  descriptor is in the sources, which say only "video of a car driving through an
  intersection." Now "a surveillance video that showed Williams's car."
- Fixed the 9.1% denominator: "Of the 41,830 that ended with a recorded
  disposition, 4,556 ... That is 9.1 percent" changed to "Of those, 41,830 ended
  with a recorded disposition, and 4,556 ... That is 9.1 percent of every alert
  police responded to." No figure altered; 4,556 is 9.1% of the 50,176, not of
  the 41,830.
- Deleted the signpost "The numbers from Chicago show the gap plainly."
- Trimmed "But that is exactly why a single alert says so little" to "But that is
  why a single alert says so little."
- Cut the "X is the whole Y" tail: "not measuring the same thing, and that gap is
  the whole dispute" is now "not measuring the same thing."
- Reworked the false-positive sentence from "by its own definition, an alert
  counts as a false positive only when a police customer reports back ..." to "But
  that rate depends on who reports back: an alert counts as a false positive only
  when a police customer says no gunfire occurred ...," and moved its citation
  from s6 to s4+s5 (the FAQ's "customer-reported" phrase and MacArthur's
  rarely-filed finding).
- Replaced the redundant "the company argues the outcome studies miss the point:
  an alert, it says, is itself evidence that gunfire happened" (which restated the
  Position block) with the argument s6 actually makes: "The company also rejects
  the outcome measures themselves, saying that when an alert turns up no physical
  evidence, the cause is a slow response or an uncooperative witness rather than a
  detection error," cited to s6.
- Added s4 to the Position block's summary, where the human-review clause needed a
  source that carries it (s7 supplies the location/timestamp/audio).
- Trimmed "one more effect worth carrying forward" to "one more effect."
- Changed "no measurable drop in gun violence or arrests" to "gun homicides,"
  matching the study's actual scope.

## Required work

None. All items above were within editor scope (prose, framing, citation
placement) and are fixed in place; no figure, name, date, or quotation was
altered, and no claim needed reporting I do not hold.

## Decision

approve — the four load-bearing claims hold against their primaries after the
denominator and citation fixes, the piece teaches the base-rate mechanism in its
own concrete terms, and no publication-blocking work remains.
