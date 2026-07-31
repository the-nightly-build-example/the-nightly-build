# Voice guide — when-ai-breaks/gemini-image-generation

## Directive

Register: an engineer explaining a system to a smart colleague who wasn't in
the room, not a critic assigning blame and not a defender minimizing it. The
reader already knows this story had a culture-war fight attached to it; your
job is to be the calmer, more informed friend who tells them what actually
happened inside the software.

Reader relationship: report the mechanism, don't perform outrage or
sympathy about it. Never say what the reader should feel about the images.
State what the system did, what Google said it did, and let the gap between
intent and output do the work.

Moves that will change sentences here:

- **Sober timeline, dated and named, no scene-setting.** Open on the plain
  sequence — what the feature was for, what it produced, who said what, on
  which date — the way a postmortem opens with the timestamp, not the way a
  news feature opens with a scene. Skip any line that establishes drama
  before establishing fact. A date and a named title (not "a Google exec")
  carries more authority than an adjective ever will.
- **Move to mechanism through a specific worked case, not a general claim.**
  When you leave narration for engineering, don't announce the transition
  ("Here's why this happened") — pick one concrete prompt-to-output pair (a
  1943 soldier, a specific instruction the model silently added) and walk it
  step by step: what the user typed, what the system appended, what the
  model then had no way to know. The mechanism should be legible from that
  one worked trace before you generalize to the class of systems.
- **Defuse the charged framing by never naming it.** Do not write the
  sentence that summarizes "some called this woke, others called it biased"
  — that sentence exists only to then transcend it, and transcending a frame
  still imports it. Instead, describe only what the tuning was built to
  correct (a real, measured skew in training data) and only what it produced
  in this case (a wrong answer to a question with one correct answer). The
  reader recognizes the political fight without you naming its sides;
  naming the sides is what keeps a piece inside the fight instead of above
  it.
- **State Google's own account as Google's account, not as settled fact or
  as spin.** "Raghavan wrote that..." / "Google's post says..." — attribute
  the explanation to its source in the sentence that carries it, then let
  the engineering argument stand or fall on its own logic, not on how much
  you trust the speaker.
- **One clean tradeoff sentence, once.** The engineering point (a mitigation
  built for one failure mode creates a different one when applied without
  judgment) should appear once, stated plainly, not restated at the top and
  bottom as a thesis-and-echo. Earn it by the end of the mechanism section;
  don't announce it in advance.

Recently used, do not reuse:
- Opening on a sharp factual jolt (a dragged pedestrian, a 30-hour jail
  cell). This incident has no physical victim — do not manufacture false
  gravity to match that pattern.
- Colon-subtitle headline.
- The "not X but Y" hedged-contrast thesis mold.
- A heading cadence that joins two clauses with a comma and "and" ("The
  scale, and what it is compounding against").
- Culture-war vocabulary for the incident itself (woke, bias hysteria, DEI,
  anti-white, race-swapping) — describe the tuning and its failure in
  engineering terms only.

## Gregory Travis, "How the Boeing 737 Max Disaster Looks to a Software Developer"
Source: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer
Craft:
- cadence: Long, information-dense technical sentences alternate with short
  declaratives that land a judgment ("Big strike No. 1."). The short
  sentence never repeats what the long one said; it adds the verdict the
  long one earned.
- argument: Moves in one direction only — economic pressure (keep the plane
  certified as "the same 737") forces an aerodynamic compromise, which
  forces a software patch, which fails. Each step is the necessary
  consequence of the one before it, so the reader never has to backtrack.
- evidence: Uses his own two credentials (pilot, 40-year developer) once, at
  the top, to establish standing, then drops the first person and lets the
  airframe geometry and the software logic carry the rest.
- stance: Measured and damning at once — he never calls anyone a villain,
  he shows the chain of decisions and lets the reader arrive at "this was
  avoidable" on their own.
- notice: He notices that the software fix (MCAS) is invisible to the
  pilot — the same shape as an invisible instruction the reader of this
  piece needs to see. He makes the invisibility itself the finding, not a
  side detail.
- diction: Plain aviation and software nouns (angle of attack, trim, sensor,
  redundancy), each defined in the sentence that first needs it, never
  re-defined after.
- reader: Assumes intelligence, not domain knowledge — he teaches "angle of
  attack" the way he'd explain it to a sharp friend, once, briefly, and
  moves on.
- the move the axes miss: he treats the engineering explanation as the
  accountability. He does not need a closing paragraph assigning blame
  because the mechanism, correctly explained, already assigns it.
Calibration: "I have been a pilot for 30 years, a software developer for
more than 40."

## John Graham-Cumming, "Details of the Cloudflare outage on July 2, 2019"
Source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019
Craft:
- cadence: Time-stamped, UTC, minute by minute (13:42, 14:00, 14:07) — the
  clock itself supplies the sentence rhythm, so the writer never has to
  manufacture tension.
- argument: States the proximate cause in one line early (a bad regular
  expression), then spends the rest of the piece walking backward through
  the "11 things that had to go wrong" so the reader understands why one
  bad line of text took down a global network — proximate cause first,
  systemic cause built underneath it.
- evidence: Shows the actual failing pattern and walks a toy input through
  it step by step (3 characters, then 20) so the reader can verify the
  exponential blowup by hand rather than take the word "catastrophic" on
  faith.
- stance: A named executive owning a named outage in the first person
  plural ("we"), stating the impact in real numbers (a 27-minute outage,
  502 errors, traffic down) before any explanation, so the reader knows
  the stakes before the mechanism.
- notice: He notices that a single well-intentioned safety rule, deployed
  everywhere at once with no gradual rollout, is what turned one bad
  pattern into a global outage — the failure is in the deployment
  discipline, not just the one bad line.
- diction: Technical terms (backtracking, NFA, PCRE) are used, but each is
  earned by a plain-language sentence right before or after it that a
  non-specialist can hold onto.
- reader: Writes for someone who runs infrastructure but was not in the
  room — explains enough that a competent outsider could have caught the
  same bug, which is the actual point of a postmortem.
- the move the axes miss: apology and mechanism are kept in separate
  sentences. "We are ashamed it happened" does its emotional work once and
  briefly; the technical walkthrough that follows carries no apology tone
  at all, so the engineering stays legible.
Calibration: "The first `.*` in `.*.*=.*` acts in a greedy way and matches
the entire string 'x=x'."

## Richard Feynman, "Personal Observations on Reliability of Shuttle" (Rogers Commission Report, Appendix F)
Source: https://fisherp.mit.edu/appendix-f
Craft:
- cadence: Short declaratives that state a finding flatly, then a longer
  sentence that supplies the reasoning underneath it. "There was no safety
  factor at all" is one sentence, alone, doing the work three qualified
  sentences would blur.
- argument: Opens with the actual disputed number (engineers estimate 1 in
  100, management estimates 1 in 100,000) before any narrative, then asks
  the plain question the whole piece answers: what produces that gap.
  Structure follows the question, not the calendar.
- evidence: Grounds every general claim in one specific case — a turbine
  blade crack count, an erosion depth already observed twice before the
  disaster — rather than asserting a pattern and citing it after.
- stance: Never accuses a person by name of wrongdoing. Locates the failure
  in a process (a review that gets less strict each time nothing goes
  wrong) rather than in a villain, which is exactly how a reader keeps
  trusting the account on a subject people already have opinions about.
- notice: He notices that a defect surviving one flight gets silently
  reclassified as an acceptable risk for the next one — a process failure
  that repeats regardless of which specific defect it's applied to. That
  reusable pattern, not the O-ring itself, is the actual finding.
- diction: No jargon without immediate translation; a number is always
  followed by what it's being compared against (1 in 100,000 becomes "one
  shuttle a day for 300 years").
- reader: Assumes a reader capable of holding a probability estimate and
  comparing two institutions' numbers for the same event — never dumbs the
  math down, just states it plainly.
- the move the axes miss: he turns a single-incident postmortem into a
  transferable principle (organizations fool themselves about risk in a
  specific, describable way) without ever generalizing away from the
  concrete shuttle numbers that prove it.
Calibration: "It appears that there are enormous differences of opinion as
to the probability of a failure with loss of vehicle and of human life. The
estimates range from roughly 1 in 100 to 1 in 100,000."
