# Voice guide: what-could-go-wrong/self-replication

## Directive

Write like a risk analyst walking a smart reader through a case file, not like
someone building toward a verdict on whether to be scared. Register: calm,
declarative, technical where the subject demands it, never theatrical. Reader
relationship: the reader is capable of holding "this is a real threshold
someone chose for real reasons" and "this specific number is smaller than it
sounds" in the same paragraph without being told which one to feel. Do not
resolve that tension for them with tone.

The one move that will change sentences here: every time the piece reports
what a model did, name the harness in the same sentence or the one next to
it. Not "the model exfiltrated its weights" — say who had file access already
open, who wrote the retry loop, who supplied the hint when the model stalled.
That clause is not qualification tacked onto a claim; it is the claim. A
sentence that reports a capability result without it has reported the wrong
thing.

Second move: let confidence gradients show up as different verbs, not as
hedge-word garnish. "Formalized," "measured," and "achieved" describe
different epistemic states than "argues," "expects," or "would require."
Reach for the verb that is actually true of the claim rather than softening a
strong verb with a qualifier bolted on after.

Third move: when you steelman the alarm, steelman it all the way — give the
proponent's reasoning its own paragraphs, no double-voiced qualifier trailing
each sentence. The turn to evidence gets its own section, not a running
rebuttal woven sentence-by-sentence into the case being built. Undercutting
as you go reads as concession, not craft, and it costs the steelman its
strength.

## Licenses

```text
form: the deferred verdict
move: METR's threat-model writeup states what would have to be true for a
  scenario to matter, ranks it against competing threat models, and states
  outright that the org has deprioritized its own scenario — without ever
  telling the reader whether to worry. The ranking itself carries the
  judgment; no sentence announces it.
bar: a single instance, most naturally near the close, where the piece
  states what remains unresolved and stops there rather than resolving it
  for the reader. It must follow directly from evidence already laid out
  in the piece, and it may not restate the finding in softer words. If the
  sentence would work as a magazine pull-quote, cut it.

form: the named methodological caveat as its own clause
move: Bradford Saad's roundup never lets an eval result stand unaccompanied
  by the condition that made it possible — models with pre-loaded weight
  access, tasks scored on first-success-in-ten-tries, security settings
  looser than any real deployment. The caveat sits inside the same
  sentence as the result, not in a following "however."
bar: use only where the commission's own "how much did the harness hand
  the model" test applies — an eval number that would mislead without its
  condition attached. Never decorative; every use must change what the
  reader thinks the number means.

form: the ranked-disagreement structure
move: Kelsey Piper's Asterisk piece handles a contested claim by giving
  each camp's reasoning in full before comparing them, then marking her
  own confidence in pieces ("a weak form of this claim seems likely; the
  strong version is far less certain") instead of a single up-or-down
  verdict on the whole claim.
bar: use only for the piece's own central contested claim (does a
  scaffolded eval success predict autonomous replication). Splitting a
  claim into a likely part and an uncertain part is licensed only where
  the piece has shown, not asserted, the difference between them.
```

## Recently used, do not reuse

Do not build the dek on "the [subject] that needs [X] nobody has [held/
built/shown]" — that comma construction has run in this series' recent
neighbors and is now a stamp, not a sentence. Do not open with an
agent-noun construction ("an optimizer that," "an agent with a correct
reward") — same fatigue, different noun. Do not reach for a semicolon
reversal or a comma-triad dek; both are separately banned by the headline
standard and both have run recently in this desk. Build the headline and
dek from this piece's own finding — the size of the gap between what an
eval showed and what the headline claimed it showed — rather than from a
shape that already has a home in this series.

## Kelsey Piper, "A Field Guide to AI Safety"

Source: https://asteriskmag.com/issues/03/a-field-guide-to-ai-safety

Craft:
- cadence: short declaratives break up longer analytical runs; a
  one-line paragraph gets used as a hinge between sections, not as a
  stylistic tic repeated for rhythm's own sake.
- argument: opens by naming real disagreement among serious people
  before adjudicating any of it — each camp gets its reasoning stated at
  full strength on its own terms before the next camp's objection
  arrives.
- evidence: goes to primary sources across decades (I.J. Good 1965,
  Turing 1951) to show the concern predates the current hype cycle, then
  quotes contemporary claims directly rather than paraphrasing them into
  agreement or disagreement.
- stance: translator among camps, not advocate for one. States her own
  confidence in fractions of a claim rather than a verdict on the whole
  claim: strong version uncertain, weak version likely.
- notice: catches the difference between a claim about what current
  systems already do and a claim about what a future threshold would
  unlock, and never lets the two share a sentence unmarked.
- diction: technical terms (RLHF, recursive self-improvement) get
  defined in the sentence that first needs them; colloquial shorthand
  ("doomers") is used only after the position itself has been given a
  fair, undiminished statement.
- reader: treated as an intelligent skeptic who deserves to see why
  smart people land in different places, not as an audience to be moved
  from confusion to conviction.
- the move the other axes miss: she resists the pull to average the
  camps into a middle position. The piece ends with the disagreement
  still open and lets a concrete decision-analogy (grounding planes on
  uncertain evidence) carry the weight of "this matters regardless of who
  is right," instead of picking a side to close on.

## METR, "The Rogue Replication Threat Model"

Source: https://metr.org/blog/2024-11-12-rogue-replication-threat-model/

Craft:
- cadence: structured as discrete steps of a scenario (proliferation,
  compute acquisition, growth, evasion, damage), so the prose cadence
  tracks the causal chain instead of a rhetorical build toward alarm.
- argument: states what would have to be true, in order, for the
  scenario to occur, and flags at each step whether that condition is
  demonstrated, disputed among the authors, or unaddressed.
- evidence: anchors speculative steps to real analogues with numbers —
  botnet economics, cloud-compute pricing, known cybercrime patterns —
  so a conjectural step still has a measured comparison attached.
- stance: institutional and unhurried. States outright that the
  authors have deprioritized this exact threat model relative to others,
  which is a stronger form of calibration than hedging language could
  achieve on its own.
- notice: separates a capability's mere existence from its being the
  rate-limiting step; several capabilities in the chain are conceded as
  plausible and then set aside as not what makes the scenario likely or
  unlikely.
- diction: technical vocabulary (netwar actor, stealth compute cluster)
  paired with a plain concrete case each time, never left as an
  abstraction to do the scaring on its own.
- reader: addressed as a fellow evaluator of the scenario's plausibility,
  invited to check the specific task thresholds rather than accept a
  summary judgment.
- the move the other axes miss: the piece's authority comes from what it
  declines to claim. It is willing to rank its own scenario as less
  urgent than competitors, which no amount of hedging language would
  substitute for.

## Bradford Saad, "AI self-replication roundup"

Source: https://meditationsondigitalminds.substack.com/p/ai-self-replication-roundup
(cross-posted https://www.lesswrong.com/posts/Gxks46z8ecoSgfn4M/ai-self-replication-roundup)

Craft:
- cadence: taxonomic, moving from definitions through empirical results
  to governance implications — each section is a category, not a beat in
  a rising argument, which keeps the temperature flat even while
  surveying alarming claims.
- argument: takes each study on the table (the Fudan 2024/2025 papers,
  RepliBench) and states its headline result, then immediately states the
  condition that made the result achievable, in the same breath.
- evidence: quotes the paper's own framing precisely (">50% ... on
  15/20 task families") rather than a secondhand gloss, then names what
  the authors themselves flagged as a limitation of their own test.
- stance: synthesizer, not prosecutor of the overclaim. Credits a
  result as real before narrowing what it actually shows, so the caveat
  reads as precision rather than as a takedown.
- notice: catches that "the model succeeded" and "the model succeeded
  unaided" are different claims, and that most self-replication headlines
  quietly swap one for the other.
- diction: technical fluency without translation for a lay reader —
  appropriate for its original venue, not for this article's declared
  reader, but the discipline of pairing every result with its scope
  condition is the transferable part.
- reader: treated as capable of sitting with an unresolved question
  ("I don't know what to make of X") rather than needing it resolved
  before the piece can end.
- the move the other axes miss: the caveat is never a subordinate clause
  trailing behind the main claim — it sits inside the sentence that makes
  the claim, so a reader skimming for the result cannot skim past the
  condition that makes the result mean less than it sounds like.

## Self-test

A writer given only "steelman the argument, then test it against
evidence, calm register, no hype and no doom" would produce exactly the
house default this series already runs on every edition — that sentence
restates the desk's standing brief, not this article's craft problem.
What this guide adds beyond the default: the harness-naming rule makes
"how much did the harness hand the model" a sentence-level test, not a
section-level theme, so it governs individual capability claims the way a
citation rule would; the instruction to keep the steelman undercut-free
for its full length, saving the rebuttal for its own section, blocks the
default habit of hedging every strong claim as it's made; and the license
for stating confidence as a fraction of a claim (weak version likely,
strong version uncertain) gives the writer a concrete alternative to the
single up-or-down verdict the house default would otherwise reach for on
a contested claim like this one.
