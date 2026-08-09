# Editorial review: when-ai-breaks/tesla-autopilot (editor/01)

## Skeptic

Thesis, stated from the draft alone: a Level 2 system steers and brakes but
cannot tell whether the human is still watching; two drivers stopped watching
and died; and the design-versus-misuse dispute over the cause was effectively
conceded by Tesla itself when, in December 2023, it recalled every Autosteer car
to strengthen the very driver-monitoring controls the NTSB had faulted. The
claims it stands on: (1) the two crash narratives, told in logged order; (2) the
NTSB's multi-causal probable causes, which name driver and design together; (3)
the recall as the point that settles the dispute; (4) the ~40% figure and the
miles-per-fatality comparison as discredited, appearing only to be taken apart.

I tried to break each and pushed hardest on the one I most wanted to keep, the
recall-as-concession spine. It holds. The recall's own defect language ("the
prominence and scope of the feature's controls may not be sufficient to prevent
driver misuse") is carried verbatim in the note and cited to Tesla's Part 573
filing (s9, primary); the article correctly preserves that Tesla filed "while not
concurring with the agency's analysis," so it does not overstate the concession
into a formal admission. The multi-causal discipline holds throughout: Williston
names the truck's failure to yield and the driver's overreliance beside the
operational-design finding; Mountain View names the phone game and overreliance
beside "system limitations" and "ineffective monitoring," and separately assigns
the injury severity to the crushed, unrepaired attenuator. Nothing reads as "the
software killed them."

Display text, checked descriptor by descriptor against the evidence: Joshua Brown,
US-27A near Williston, Florida, 4:36 p.m. Saturday 7 May 2016, 2015 Model S,
74 mph in a 65 zone, Autopilot 37 of 41 minutes, hands felt 7 times for 25
seconds, ~6-minute gap — all exact. Walter Huang, US-101 Mountain View,
California, 9:27 a.m. Friday 23 March 2018, 2017 Model X, TACC 75, 5.9 s/560 ft,
5.6 degrees into the gore, 3.9 s from 61.9 toward 75, no torque last 6 s, ~70.8
mph impact, attenuator crushed 11 days earlier — all exact. The vehicle-noun
caution is respected: the Model S is "the car," the Model X is "the sport utility
vehicle." Recall figure 2,031,220 and the "almost 40 percent" wording are exact.
The headline ("2 million cars," "for letting drivers stop watching the road") and
dek (steers and brakes, needs a human every second, the two named drivers, truck
and barrier) both commit to what the piece proves. The drivers' names are not in
the NTSB reports (the reports write "the car driver"); they come from the public
record, as the evidence flags, and are attached to citations that support the
surrounding facts — an accepted convention here, and the names and Huang's "Apple
engineer" role are correct.

The two disputed figures appear only to be dismantled. The 130-million-miles line
appears first inside Tesla's reported 2016 statement (attributed to Tesla, not
leaned on) and is later taken apart for the same missing-denominator flaw; the
~40% figure is introduced as Tesla's "headline evidence," called "hollow from the
start," and undone via NHTSA's own footnote and the FOIA-forced reanalysis. Neither
is used as support anywhere.

`data-nb-kind` audit: all eleven correct. The two NTSB reports, the three NHTSA
documents (PE16-007, EA22-002, the Part 573 recall), SAE J3016, and the Internet
Archive capture of Tesla's own "A Tragic Loss" page are primary; NBC News (both
the 2018 reproduction and the 2024 FSD report) and The Drive's QCS write-up are
secondary. The 2016 post is cited as an archive of Tesla's own page (kept primary,
correct); the 2018 post is routed through the NBC reproduction (secondary,
correct), exactly as the removed-source policy requires.

Link resolution: I opened every citation href as printed. The static.nhtsa.gov
PDFs (s1, s8, s9), both NBC pages (s6, s11), The Drive (s7), the NTSB PDFs (s3,
s5), SAE (s2), and the SGO page (s10) resolve. The web.archive.org capture (s4)
could not be fetched through the agent proxy (that host is blocked for this
session), so I confirmed it independently through the Wayback availability API,
which returns the exact capture (timestamp 20160722055534) with status 200 and
available:true; nb's own `--check-links` proof also passed BLOCK: 0. It resolves.

One break found. The Mountain View paragraph read "about five seconds and 150
meters of clear view of the divider," cited to s6 (NBC). NBC reproduces the
"five-second view" but not the "150 meters" — that figure lives only in Tesla's
removed 2018 blog, which the writer deliberately did not cite. The detail was
therefore unsupported by its citation and nonessential (the five seconds already
carries the point). I cut "and 150 meters" directly; the claim now matches the
cited secondary source.

## Cut

I ran a dedicated slop pass over every sentence, including display text and the
Why/takeaway bookends and the note. The prose is genuinely tight and tied to its
subject: sentences like "the controls it recalled were the controls that had let
Brown and Huang stop watching the road" or "moving the catch into the product's
name" could not be moved to another article. No sentence failed the slop test, so
no slop cut was made. Candidate tells I weighed and cleared: "It was hollow from
the start" is immediately substantiated by the footnote concession, not an
unearned punchline; "This is not history" is the series-mandated pivot to where
the weakness lives now and is three words carrying a claim the paragraph proves;
"There was a second design point" and "The logs bear that out" are plain
transitions that carry the argument forward, not self-grading signposts. The
delete test removed nothing: every sentence carries a fact, a disputable claim,
or a reasoning step.

Negative parallelism is controlled — the earned contrasts ("the driver is the one
watching, not the car"; "steers and brakes but needs a human watching") name a
real misconception and stay within budget. Punctuation is plain: colons introduce
definitions or payoffs, there are no body em-dashes, and I found no comma splices
or run-ons. Grammar and syntax are clean throughout the prose and furniture.

Prompt-leakage check against the writer brief: the taught terms (automation
complacency, operational design domain, SAE Level 2) are legitimate terms of art
defined in place, not lifted instructions; the takeaway's two questions render the
brief's "what conditions can it not handle / what keeps the human watching"
teaching goal in the article's own concrete nouns (the turning truck, the
splitting exit, a torque sensor versus something that sees the eyes), not verbatim.
Voice-guide echo check against the Langewiesche, ProPublica, and Gladwell
passages: the piece takes their discipline (logged order, flat humane register,
each side stated in its own terms) without borrowing any distinctive clause.

Pattern comparison against the recent library (via `nb history`): the last two
when-ai-breaks lessons (optum, apple-card) resolved on "it did exactly what it was
built to do." This piece is the opposite shape and does not borrow that frame or
the "the tool was not broken" line; the takeaway lands on two carried questions,
not the "the first question is not A, it is B" mold, and avoids both "By the end
of this lesson you will be able to say…" and "Now you know which one you are
looking at." The headline avoids the comma-and construction the optum headline
uses. Section headings vary in build and reconstruct the argument; the two "The
car that…" headings are deliberate parallelism for the paired crashes, not a
cross-article formula. The note label "The defect, in Tesla's words" is honest
about its verbatim content and is not the recurring "In plain language" label.
nb-timeline is not used, and the Verdict block the press forbids is absent — the
body closes on the takeaway bookend.

Furniture: the single note is deliberate emphasis on the sentence the whole
dispute turns on, and earns its place. The writer's choice to narrate the gore
geometry in prose rather than add the NTSB diagram is sound — the argument is
documentary, and no included visual is needed to test it, so I request no asset.

## Reader

Read straight through as the paper's declared reader, what I have that the sources
alone would not give me: the understanding that a Level 2 system's fatal weakness
is not failing to drive but being unable to tell whether the human is still
watching, proven by aligning three documents the record keeps apart — the NTSB's
2017 design finding, the two crashes' final-seconds monitoring silence, and the
recall's own defect language. The original-work sentence in the handoff ("the
controls it recalled were the controls that had let Brown and Huang stop watching
the road") survives intact and is earned by the section that builds to it. Both
answers hold; this is synthesis, not a restatement of sources, and no redraft is
warranted. The prose sits with the voice-guide exemplars, not a median summary: it
narrates in logged order with the numbers doing the work, reports the two deaths
in plain flat sentences without telling the reader how to feel, and sets Tesla's
account beside the record without refereeing. The register stays reported and
humane throughout. The headline, reread as the largest claim, is exactly what the
piece defends.

## Edits

- Cut "and 150 meters" from the Mountain View paragraph: the figure was cited to
  NBC (s6), which reproduces only the "five-second view," so the detail was
  unsupported by its citation and nonessential.
- Ran `./nb stamp` after the cut: words 2199 to 2196, reading 10 min, sources 11.

## Required work

None. The single break found was resolved by a direct surgical cut within the
editor's authority; no item remains for the researcher, writer, or orchestrator.

## Decision

approve — every name, date, place, and quantity checks out against the evidence,
all eleven citations resolve and carry the kind they claim, the two discredited
figures appear only to be dismantled, the register stays reported and humane, and
the one unsupported detail was cut in place.
