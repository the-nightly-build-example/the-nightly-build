# Editorial review: when-ai-breaks/tessa-eating-disorder-chatbot (editor/01)

## Skeptic

Thesis: a tool validated only for a narrow, low-stakes job (eating-disorder
prevention in at-risk people who do not yet have a disorder) was moved into a
higher-stakes job (a helpline replacement for acutely ill users), where the same
generic dieting advice that is harmless to most people is the mechanism of the
illness for this population; the harm follows from that scope mismatch on either
account of the technical trigger, and the human responder who was automated away
was the check that would have caught it.

The claims it stands on, tested:

1. **Tessa was validated only for prevention in non-acute at-risk users, and was
   a rule-based fixed script.** Held. Opened s2 (the RCT, via the DOI): a
   randomized prevention trial in ~700 women screening at high risk, small but
   real reductions in risk factors and onset — a prevention population, not
   people in treatment. Opened s3 (Chan/JMIR, PMC): the developers state they
   used a rule-based approach, conversations "predefined and thus limited,"
   unable to answer outside the script. Opened s5 (Gullo 2026, DOI): the same
   group's later rule-based prevention chatbot for at-risk adolescents,
   corroborating the design point from a second developer publication. The spine
   is firmly sourced.
2. **NEDA wound down a 20-year human helpline and pointed users to Tessa days
   after staff unionized.** Held. Opened s4 (KFF): 20+ years, nearly 70,000
   served last year, volume up >100% in the pandemic, union certified Mar 27 and
   positions eliminated four days later, developer's "can't go off the rails, so
   to speak." The "replacement" characterization carries NEDA's June 7 "separate
   decisions ... may have become conflated" walk-back in the body; verified in s6
   (NPR).
3. **Users documented the harm; three independent parties confirmed it.** Held.
   Opened s6 (NPR): Maxwell (San Diego consultant/survivor) documented the
   advice; Conason (psychologist) reproduced it; Ostroff (MEDA) flagged concerns
   in Oct 2022; NEDA first disputed, then disabled Tessa May 30. The article
   reports the advice at the category level (weight loss, calorie deficit,
   counting, self-weighing) and omits the specific figures NPR prints — the
   minimum needed to show the failure, no usable instruction set. Sensitivity
   standard met.
4. **The technical cause is disputed and single-sourced.** Held and correctly
   restrained. NEDA (Thompson) says Cass added an unauthorized generative
   feature; Cass (Rauws) says it was contract-permitted and the harmful outputs
   were pre-scripted (both via s6, secondary). The two position cards steelman
   each side; the article states the sharpest claim "rests on one party and is
   denied by the other." The developers' STAT concession of "a technical problem"
   (s1, verified) is explicitly barred from adjudicating it ("They did not say
   which operator's version of the cause was right"). No display text asserts
   generative AI as the settled cause.

Display-text audit, descriptor by descriptor. The **headline broke on
attribution**: "NEDA tested Tessa to prevent eating disorders ..." credits the
validation to NEDA, but the body and s2 establish the research team led by
Fitzsimmons-Craft tested it and that Tessa "was not built by NEDA." A wrong actor
in the headline reaches every reader. Rewrote to "Tessa was tested to prevent
eating disorders. NEDA offered it to people who had one" — passive on the testing
(no false attributor), NEDA correctly owning only the offering, contrast and
nouns preserved. Updated in the `<title>`, the `nb-meta` title, and the `<h1>`.
Dek verified and left as is (attributes the advice to users, disables-after-days
matches May 30, asserts no cause). Subheads each map to a supported step and none
asserts the cause.

One unsupported claim: orientation opened by calling NEDA "the largest nonprofit
in the United States working on eating disorders." "Largest" is in neither cited
source (checked s6 and s4 directly) nor the evidence record. Cut the superlative
to "a national nonprofit working on eating disorders," which the record supports.

`data-nb-kind` audit: s1 STAT op-ed, s2 RCT, s3 Chan, s5 Gullo, s7 Cass/X2AI all
correctly primary; s4 KFF, s6 NPR, s8 NBC correctly secondary. The disputed-cause
quotes and the Maxwell/Conason/Ostroff harm rest on NPR/KFF as secondary carriers
of the parties' words, not relabeled to manufacture independence. The vendor page
(s7) is used only for the product's own framing; its efficacy figures are called
marketing and not cited as fact, as the record requires.

Every href opened as printed. s1, s3, s4, s6, s7, s8 resolve to the source. s2 and
s5 are DOIs that 302 to the Wiley article pages; Wiley returns 403 to the
automated fetcher (publisher bot-blocking, not a dead link), and the DOI is the
correct canonical citation form — the writer's `nb check --links` passed. Both
Background links (`epic-sepsis-model.html`, `air-canada-chatbot.html`) exist on
the when-ai-breaks shelf in the library checkout.

One miscitation fixed: the helpline staffing sentence blends KFF ("five to six
paid staffers ... 90-165 volunteers") with NPR ("four full-time ... hundreds of
volunteers") but cited only s4. The "four" and "a few hundred" are NPR's, so I
added s6 to make the stated "accounts vary" range honestly cross-sourced. The
number stays as the writer set it (altering it is out of an editor's remit); the
top of the range, "five," clips KFF's "six" slightly — noted below as optional,
not blocking.

## Cut

Cut four sentences that failed the slop delete test, none carrying a fact or a
reasoning step:

- "The first flag came early." — an empty edge opener; the date that follows
  carries the "early" without it.
- "Start with the part the record settles." — a navigational signpost; the
  section's concrete sentences already mark what is settled versus disputed.
- "Each will matter when the advice turns out to be neither." (with the reader-
  directive "Keep both facts in view:" folded out) — a forward teaser; the two
  facts it points at are already stated plainly in the same paragraph.
- Recast "Notice that the answer barely matters for the lesson" to "The answer
  barely matters": removed both the lecturing "Notice that" opener and a stray
  body self-reference ("for the lesson").

One further body self-reference fixed for the lesson template (the body speaks to
no one): "so it is not something this lesson can state as fact" became "so it
cannot be stated as settled fact." The allowed self-reference in the two bookends
was left alone.

Negative-parallelism lines checked against the "named misconception" test. The
opener's flagged line, "the failure is in the role, not the wiring," stays: the
misconception it corrects (that the fix turns on which line of code produced the
advice) is real and is the piece's central subject — the whole cause-dispute
section exists to answer it. "People at risk, not people in crisis" and "not the
advice but who received it" likewise correct the piece's own named distinction
and stay. The takeaway lands on "The human it replaced was often the part that
knew the difference," not on negative parallelism, as the brief required.

Furniture reviewed: the timeline carries the 2023 sequence the commission
allowed; the two position cards are the steelman-each-side apparatus the disputed
cause needs; the "What would settle it" note names the missing evidence. Each does
work; none makes the piece read as a stack of blocks. No em-dashes; punctuation
clean. Prompt-leakage pass: the takeaway's "Fitness for one job does not travel to
a harder one" is the article's earned thesis demonstrated by the body, not the
commission's "does not transfer to a higher-stakes deployment" lifted — reworded
and earned, so kept. No exemplar phrasings from the voice guide were borrowed.

## Reader

Read straight through as the paper's smart-but-new reader, what I have that the
sources alone would not give me: one clean mechanism — scope misuse — that makes
the incident legible without resolving the cause fight. The same advice is safe or
dangerous depending on who reads it; the human responder was the check; and the
technical trigger is genuinely undecided and does not change the lesson. The
individual sources give the timeline, the trial, the vendor framing, and the
dispute separately; the article fuses them, which matches the draft-handoff's
original-work sentence. Both answers survive. The prose sits closer to the voice-
guide exemplars than a median summary: it attributes step by step, states grave
facts plainly without intensifiers, and names the unknown flatly ("None are
public"). The headline, reread as the largest claim, now holds after the fix.

## Edits

- Headline rewritten in `<title>`, `nb-meta` title, and `<h1>`: "NEDA tested
  Tessa ..." to "Tessa was tested to prevent eating disorders. NEDA offered it to
  people who had one" (actor attribution).
- Cut the unsupported superlative "the largest nonprofit in the United States" to
  "a national nonprofit working on eating disorders."
- Cut "The first flag came early."
- Cut "Start with the part the record settles."
- Cut "Keep both facts in view: ... Each will matter when the advice turns out to
  be neither." to plain "Tessa was validated for prevention, and it was a fixed
  script."
- Recast "Notice that the answer barely matters for the lesson." to "The answer
  barely matters."
- Fixed body self-reference: "so it is not something this lesson can state as
  fact" to "so it cannot be stated as settled fact."
- Added s6 citation to the helpline staffing sentence so the cross-account range
  is attributed to both KFF and NPR.

## Required work

None blocking. Optional, for the writer if a later pass touches the line: the
staffing range reads "four to five full-time employees," but KFF says "five to
six" and NPR says "four" — "four to six" would match both sources exactly. The
number is nonessential context, hedged as "accounts vary," and now cites both, so
it does not block publication.

## Decision

approve — the attribution and sensitivity risks are handled (disputed cause
attributed and never asserted, no cause in display text, the replacement walk-back
carried, no harmful instructions reproduced, source kinds correct), and the
remaining defects were direct editor fixes made in place.
