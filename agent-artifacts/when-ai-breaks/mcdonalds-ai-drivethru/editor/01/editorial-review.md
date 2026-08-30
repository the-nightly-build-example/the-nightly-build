# Editorial review: when-ai-breaks/mcdonalds-ai-drivethru (editor/01)

## Skeptic

Thesis: McDonald's spent nearly five years and a sale to IBM building a
drive-thru voice order-taker, could not make it reliable enough to keep, and
never published the accuracy number that would say whether it worked; a
drive-thru is acoustically hostile to speech recognition, and much of today's
"AI" ordering is still a hidden human.

Claims it stands on, and how each held:

- **The chronology.** Apprente agreed acquired September 2019, folded into McD
  Tech Labs, sold to IBM by the joint statement of October 27 2021, tested at
  more than 100 US restaurants, switched off no later than July 26 2024 on the
  Mason Smoot memo. I opened every display date against its owning source. The
  PR Newswire wire copy of McDonald's release gives September 10 2019 and the
  McD Tech Labs charter; the IBM newsroom statement is dated October 27 2021 and
  carries the "substantial benefits to customers and the restaurant crew
  experience" line verbatim; Engadget gives the 10 Chicago restaurants in spring
  2021; Biometric Update confirms the ~two-year test, the accent/dialect
  trouble, franchisee cost, and the July 26 2024 shutdown; Al Jazeera and
  Restaurant Online carry the forward-looking quote and the "successes to date"
  memo line. Restaurant Business (s3, the memo source) 403s to automated fetch —
  a site bot block, not org policy, reachable in a browser — and its quote and
  Smoot's title are corroborated identically by s5, s7, and s8. The chronology
  holds exactly.

- **The two human-in-the-loop shapes stay apart.** This was the round's biggest
  risk and the draft handles it cleanly. The SEC finding (~70% of Presto orders
  entered by off-site agents in the Philippines and India) is labelled Presto
  throughout — prose, note attribution, and source note — and the article states
  in its own words that this is "a different arrangement from McDonald's, whose
  humans were the crew at the counter rather than remote agents," then draws the
  shared lesson without merging the two. The SEC PDF (s10) resolves and is the
  correct filing (Release 33-11352, settled January 2025). No merge.

- **The ~85% figure is attributed and flagged as never published.** The article
  says plainly the figure "comes from reporting rather than from McDonald's or
  IBM, and neither company released a measured number," repeats it in the dek as
  "reporting guessed about 85 percent," and steelmans both accounts around the
  missing number. Engadget (s4) confirms it presents 85% as its own
  characterization, not a company disclosure. The disputed cause is presented
  from both sides with the one figure that would settle it named.

- **The noise mechanism (Whisper Figure 5).** The SNR/WER collapse is sourced to
  the Whisper paper (s6), which resolves. Two breaks in the bridge from mechanism
  to case, both fixed directly:
  1. "A car idling at a menu board routinely sits in that range" asserted a
     measured drive-thru SNR (below ~10 dB) that no source in the record
     supplies — the Whisper curves measure LibriSpeech under controlled noise,
     not drive-thru acoustics. I recast it to the supported inference: the engine
     and traffic noise *push the ratio down toward* that range. The central claim
     (a drive-thru is hostile to ASR) is untouched; only the unsourced measured
     precision is gone.
  2. The draft glossed the accent/dialect trouble as "the noisy case the Whisper
     curves describe." Accent difficulty is a distinct failure mode from additive
     noise, and the figure is about noise; the apposition conflated two
     mechanisms the commission itself lists separately. I cut the false gloss.

Display text checked descriptor by descriptor: headline ("nearly five years" =
Sep 2019 to Jul 2024, accurate), dek, every subhead, Mason Smoot's title (chief
restaurant officer, McDonald's USA), the SEC release number and date, the
White Castle/SoundHound 90% claim (s9). All held. `data-nb-kind` audit: four
primaries (McDonald's release via wire, IBM statement, Whisper paper, SEC order),
six secondaries; meets policy, and no secondary is dressed as an independent
primary.

The failure clips are handled at exactly the right evidentiary weight: the two
mainstream-carried clips are described, the origin-unverified "260 nuggets"
number is wisely absent from the body, and the provenance limit ("they show the
behavior was filmed... they do not measure how often it happened") is stated.

## Cut

Slop pass, every sentence including display text and furniture prose. Four
sentences failed and were fixed:

- The opener's third sentence led with "The reasons are specific and worth
  holding onto:" — empty self-grading (the "X is specific and worth Y" reduction)
  fronting a preview of the body's three arcs, exactly the syllabus/preview tell
  the brief and the recent-pattern notes flagged. The three arcs themselves carry
  real content and are each resolved in the takeaway, and the lesson template
  sanctions posing the lesson's questions in the opener and answering them in the
  takeaway. So I kept the three arcs and replaced the empty lead-in with "Three
  questions run through it:", which frames them as genuine questions rather than
  self-grading and drops the formula.
- "So two accounts sit next to each other." — a pure signpost reporting where the
  argument stands; deletion loses no fact. Cut; the paragraph now opens on the
  first account.
- The two mechanism-bridge sentences above (SNR overclaim, accent apposition)
  also read as reaching past the evidence; handled under Skeptic.

One logic repair: "One figure would separate the accounts: ... a measured
accuracy rate ... and the stated reason for stopping. McDonald's released
neither" named one thing but listed two and then said "neither." Changed to "Two
things would separate the accounts ... McDonald's gave neither," which the
commission and evidence back (both a measured figure and the reason for ending
are what would settle it).

Held to the standard and kept: "A voice order-taker is not one program. It is a
chain of three" is an earned contrast — it corrects the real monolith intuition
and is the section's actual teaching spine. "The plainest documentation of that
comes not from McDonald's but from a competitor" earns its "not/but" by warning
the reader the best evidence is about a different company, the section's crux.
The comma-triad in "The menu is fixed, the same items repeat all day, and the
customer is trying to be understood" is body prose carrying three real reasons
and passes the reduction test. No em-dashes in the prose; colons all introduce
what their clause promises; en-dashes only in date ranges.

Furniture (timeline, three-step pipeline, position card, SEC note, the Whisper
figure) each does distinct work and none reads as a stacked block or a repeated
formula; no missed component. Edges, dek, and headings checked against the
recent-pattern notes: the dek is two plain sentences (no two-clause contrast, no
comma-triad, no atmospheric colon subtitle); headings are in the story's own
nouns ("back off the menu", "between the speaker and the fryer", "The same order
still routes to a person") and vary in construction; the closer names specific
current systems (White Castle/SoundHound, Presto) rather than a generic
where-it-lives heading. No leakage from the commission or briefs: the "260
McNuggets" punchline and the required-contribution framing are not lifted.

## Reader

Read straight through as the paper's reader, the answer to "what do I have that
the sources alone would not" survives: I can now say why a drive-thru defeats
speech recognition (the three-stage pipeline and the SNR/WER collapse), why the
success-or-failure question is unanswerable (the accuracy number was never
published), and that "AI" ordering hides a human in two different shapes. No
single source offers that — the Whisper paper never mentions McDonald's, the SEC
order is about Presto, and the trade reporting does not teach the mechanism. The
draft-handoff's original-work claim (the reframing around the one unpublished
figure, plus the two-shapes distinction) matches what the article delivers. The
prose sits closer to the voice-guide exemplars than a median summary: Seven-style
plain-stakes openings, Travis-style bare facts left to close paragraphs, and the
pipeline vocabulary (ASR, SNR, WER, the three stages) named once and reused. The
headline reads true as the largest claim.

## Edits

- Opener: replaced "The reasons are specific and worth holding onto:" with "Three
  questions run through it:", keeping the three arcs.
- Pipeline: "A car idling at a menu board routinely sits in that range" → "...
  with traffic behind it, pushes the ratio down toward that range" (removed the
  unsourced measured-SNR claim).
- Pipeline: cut the false apposition "the noisy case the Whisper curves describe"
  after "different accents and dialects" (accents are not the noise case).
- No-number section: cut the signpost "So two accounts sit next to each other."
- No-number section: "One figure would separate the accounts ... McDonald's
  released neither" → "Two things would separate the accounts ... McDonald's gave
  neither" (one/neither logic).

## Required work

None blocking.

- orchestrator: re-stamp after these edits (word count and reading time shift
  slightly; I did not run `nb stamp`).
- writer: no blocking item. Optional only — if a stronger claim that the
  drive-thru itself measures in the sub-10 dB failure range is wanted, it needs a
  sourced drive-thru SNR measurement (a new researcher artifact); the piece does
  not need it, and the softened inference is honest as it stands. The closing
  section's peer scope (White Castle/SoundHound and Presto rather than a broader
  Wendy's/Yum roster) is non-blocking per the brief and the draft handoff;
  broadening it would require a readable source the researcher could not open, so
  I did not add unread coverage.

## Decision

approve — the spine (chronology, the two human-in-the-loop shapes, the attributed
and flagged 85%, the noise mechanism, the honest figure asset) holds under
scrutiny, and the slop, signpost, and evidence-reach faults I found were all
fixable directly.
