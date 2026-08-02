# Voice guide: when-ai-breaks/microsoft-tay

## Directive

Register: a technically literate outside investigator, not the operator
explaining itself and not a newsroom recapping the operator's statement.
Write the way Leveson and Turner wrote up Therac-25 or Travis wrote up the
737 MAX: someone who has read the primary record closely enough to test the
company's own account against it, sentence by sentence, without theatrics.
The reader is smart and has no reason yet to trust or distrust Microsoft's
version; earn the reader's judgment for them by showing the record, not by
supplying adjectives.

Moves that change sentences in this draft:

- **Timeline first, in the corpus's own nouns.** Give named actors, exact
  times, and exact system names as the record actually documents them.
  Where the record is genuinely silent on a detail (why a specific
  safeguard was absent, what internal review preceded launch), say that
  plainly in one clause rather than filling the gap with a plausible-
  sounding guess. GitLab's postmortem and the AWS S3 write-up both keep a
  visible line between "this happened" and "we inferred this happened
  from later evidence" — hold that same line here, because the writer is
  outside the building and has less access than either of those authors
  had to their own systems.
- **Quote the offensive material like an investigator quotes evidence, not
  like a story quotes a scene.** A quoted tweet exists in the piece to
  support one specific claim (what the model output, what pattern it
  reveals) and stops the moment it has supported that claim. No quoted
  line should be followed by a sentence that reacts to it rather than
  using it. Therac-25's account of six radiation overdoses never leans on
  the injuries for effect; the clinical detail is the whole force. Do the
  same here: the fact pattern carries the weight, not the writer's tone
  toward it.
- **Keep three voices typographically distinct: the record, Microsoft's
  framing, and the writer's synthesis.** Attribute Microsoft's account
  with plain verbs ("Microsoft's post said," "Microsoft stated") and test
  it against the documented timeline in the next sentence rather than
  folding agreement or disagreement into the verb of attribution itself.
  Travis's 737 MAX piece is the model for testing an operator's account:
  he states Boeing's stated rationale in Boeing's terms, then holds it up
  against what the engineering record shows, in that order, without
  announcing that he is about to do so.
- **Carry the story straight into the mechanism using the same nouns, with
  no transition sentence that names the move.** Every exemplar below ends
  its narrative section and opens its explanatory section on the same
  actor or system it was just discussing — never on a sentence like
  "so what actually went wrong." The GitLab postmortem drops from what
  happened straight into the specific command that caused it; Cloudflare
  drops from the timestamped outage narrative straight into the
  regex engine's own behavior. Do the same at the story-to-mechanism
  seam here: the last sentence of the narrative and the first sentence of
  the mechanism section should share a noun.
- **Let the 2016-vs-today comparison live inside the mechanism
  explanation, not in a separate closing section.** State what made the
  system update on live input then, and state what current deployments do
  instead, as two factual claims about architecture placed next to each
  other — not as a reassurance ("but don't worry, today's systems are
  different") and not as a warning. The reader should be able to derive
  the present-day relevance from the comparison itself.
- **Sentence-level diction.** Short declaratives carry the narrative
  sections; let a longer sentence appear only where a mechanism genuinely
  has that many moving parts and needs one continuous clause to hold
  together (Travis's autopilot-comparison sentences, GitLab's cascading
  cause sentences). Avoid any adjective that grades the incident
  ("shocking," "disastrous," "notorious") — name the specific fact that
  would justify the adjective and cut the adjective itself.

Recently used, do not reuse: the opener "The number X published about
itself"; comma-triad headings or deks; the heading mold "Two accounts, one
gap in the timeline"; any reusable closer formula or house catchphrase.

## Exemplars

## Amazon Web Services, "Summary of the Amazon S3 Service Disruption in the
Northern Virginia (US-EAST-1) Region"
Source: https://aws.amazon.com/message/41926/
Craft:
- cadence: Opens at the sentence level with a single grounding fact (time,
  region) before any causal claim appears; causal sentences stay short
  even when the underlying event was complex.
- argument: Moves from the triggering human action to the dependency graph
  it exposed — the essay's real subject is not the mistake but the blast
  radius the architecture allowed the mistake to have.
- evidence: Names the specific subsystems (index, placement, billing) and
  what each does, so the reader can trace the cascade system by system
  rather than take the summary on faith.
- stance: Institutional, first-person plural, addressed to customers as
  the audience of record.
- notice: Treats the operator error as a mechanical event ("one of the
  inputs was entered incorrectly") rather than narrating the person who
  made it — a self-postmortem convention.
- diction: Plain engineering vocabulary, no evaluative adjectives about the
  severity of the outage; the facts (duration, scope) carry that.
- reader: A customer who needs to know what broke and whether it will
  break the same way again, not a general audience needing the stakes
  explained.
- the axes miss the sequencing choice: technical justification is placed
  before the apology, not after — the piece earns the apology with the
  explanation rather than opening on contrition.
Calibration: "an authorized S3 team member using an established playbook
executed a command which was intended to remove a small number of servers
for one of the S3 subsystems... unfortunately, one of the inputs to the
command was entered incorrectly."

## GitLab, "Postmortem of database outage of January 31"
Source: https://about.gitlab.com/blog/2017/02/10/postmortem-of-database-outage-of-january-31/
Craft:
- cadence: Timestamped narrative section reads almost like a control-room
  log (±17:20 UTC, ±19:00 UTC); each entry is one clause of action, no
  editorializing inside the timeline itself.
- argument: The piece's spine is a "5 Whys" chain — each cause is shown to
  rest on a prior, more structural cause, so the single human error at the
  surface is revealed to sit on top of years of unmonitored backup
  failures.
- evidence: Specific version numbers, specific commands, specific error
  strings (pg_dump's exact failure) — nothing is described generically
  when the exact artifact is available.
- stance: Direct institutional accountability stated once, up front
  ("Losing production data is unacceptable"), then never repeated — the
  rest of the piece is technical, not contrite.
- notice: Keeps "Timeline," "Root Cause Analysis," and "Improving Recovery
  Procedures" as physically separate sections so fact, cause, and fix
  never blur into one paragraph.
- diction: Formal-technical throughout; human error is named without
  euphemism ("an engineer proceeds to wipe the PostgreSQL database
  directory, errantly thinking they were doing so on the secondary").
- reader: A practitioner audience that will judge the company by whether
  the postmortem is honest and specific, not by whether it is contrite.
- the axes miss the discipline of naming every contributing failure
  separately rather than letting one cause absorb the others: broken
  backups, silent cronjob failures, and disabled snapshots are each given
  their own accounting, so the piece never lets the proximate cause stand
  in for the whole story.
Calibration: "Trying to restore the replication process, an engineer
proceeds to wipe the PostgreSQL database directory, errantly thinking they
were doing so on the secondary. Unfortunately this process was executed on
the primary instead."

## John Graham-Cumming, "Details of the Cloudflare outage on July 2, 2019"
Source: https://blog.cloudflare.com/details-of-the-cloudflare-outage-on-july-2-2019/
Craft:
- cadence: Short declaratives state the mechanism plainly ("The CPU
  exhaustion was caused by a single WAF rule") before the piece allows
  itself a longer sentence to walk through the backtracking behavior step
  by step.
- argument: Structured as three widening rings — what happened, how the
  system normally operates, what went wrong — so the reader has the
  normal-operation context in hand before being asked to understand the
  failure.
- evidence: Builds the regex-backtracking explanation from a worked
  example (testing a short string against the actual problem pattern)
  rather than asserting the mechanism abstractly.
- stance: States the company's own responsibility in plain first person
  ("we are ashamed it happened") once, early, then spends the rest of the
  piece on the engineering account — accountability and explanation are
  sequenced, not blended sentence by sentence.
- notice: The failure list ("what went wrong") itemizes eleven distinct
  contributing conditions rather than compressing them into one root
  cause — precision over narrative tidiness.
- diction: Technical terms (backtracking, PCRE) are introduced inside a
  worked example rather than defined in isolation, so the definition and
  the demonstration are the same sentence.
- reader: A reader who does not already know regex internals but is
  willing to follow a worked example to get there — the piece teaches the
  mechanism rather than assuming it.
- the axes miss how the piece uses headings as the argument's actual
  spine ("What happened," "How Cloudflare operates," "What went wrong"):
  each heading names the next widening ring, not a scaffolding label.
Calibration: "The CPU exhaustion was caused by a single WAF rule that
contained a regular expression that caused catastrophic backtracking."

## Nancy Leveson and Clark Turner, "An Investigation of the Therac-25
Accidents"
Source: https://www.cs.columbia.edu/~junfeng/08fa-e6998/sched/readings/therac25.pdf
Craft:
- cadence: The opening states purpose before narrative — "our goal is to
  help others learn from this experience, not to criticize the equipment's
  manufacturer" — then the piece earns that stated fairness across forty
  pages rather than repeating the disclaimer.
- argument: Explicitly rejects single-cause explanation as a category
  error ("most accidents are system accidents... to attribute a single
  cause to an accident is usually a serious mistake") and structures the
  whole piece to demonstrate that claim, incident by incident.
- evidence: Built from sourced documents the authors identify as such
  (lawsuits, FDA memos, depositions) with the authors stating outright
  where documentation was unavailable and what they could not verify —
  visible epistemic honesty about the limits of an outside investigation.
- stance: External investigators writing about a manufacturer they have no
  institutional relationship with, holding the same evidentiary standard
  toward the manufacturer's claims as toward the plaintiffs' — this is the
  closest structural analog to writing about Microsoft's account from
  outside Microsoft.
- notice: A single timeline block lists every event across three years
  with dates in the left margin, so the reader can see the delay between
  first reported injury and manufacturer action laid out as bare fact
  before any interpretation begins.
- diction: Technical and legal terms are defined at first use in one
  clause each (fault tree, race condition) and reused exactly afterward;
  no variation for style.
- reader: An engineer or engineering student who needs to be able to
  reason about the failure mode afterward, not simply know that it
  happened.
- the axes miss the fairness technique itself: the authors quote the
  manufacturer's own justifications in full (its safety-analysis
  probabilities, its testing claims) before showing, with the documentary
  record, why each one did not hold — testing the account is done by
  juxtaposition, not by asserting disagreement.
Calibration: "Most accidents are system accidents; that is, they stem from
complex interactions between various components and activities. To
attribute a single cause to an accident is usually a serious mistake."

## Gregory Travis, "How the Boeing 737 Max Disaster Looks to a Software
Developer"
Source: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer
Craft:
- cadence: Alternates short, blunt sentences at moments of judgment ("Big
  strike No. 1. Big strike No. 2.") with long, clause-heavy sentences when
  walking through how an autopilot or trim system actually behaves —
  sentence length itself signals which mode the piece is in.
- argument: States the economic pressure behind Boeing's choice honestly
  before condemning the choice, so the criticism lands on the engineering
  decision specifically and not on the company's motive in general.
- evidence: Uses the author's own decades of flying and coding as a
  calibration instrument (his own Cessna's autopilot as the comparison
  case) rather than as an appeal to authority — the credential is spent on
  a specific comparison, not asserted and left idle.
- stance: An outsider to the company under scrutiny, openly opinionated,
  but every judgment is preceded by the specific technical fact that
  earns it — the anger is a conclusion, never a premise.
- notice: Names the single-sensor design decision as the crux and returns
  to it after every digression, so the piece never lets a secondary detail
  (certification process, pilot training) stand in for the central
  engineering fact.
- diction: Aviation and software terms are each defined once, briefly, in
  the sentence that first needs them, then used bare afterward.
- reader: A technically curious reader who is not a pilot or an aerospace
  engineer but will follow a careful comparison to a system they could
  picture (a smaller plane's autopilot).
- the axes miss the redundancy argument as a generalizable teaching move:
  the piece keeps returning to one plain engineering principle (a
  safety-critical system needs more than one sensor) and shows how its
  absence explains everything downstream, which is how a single mechanism
  can carry an entire piece instead of one paragraph of it.
Calibration: "I have been a pilot for 30 years, a software developer for
more than 40. I have written extensively about both aviation and software
engineering. Now it's time for me to write about both together."
