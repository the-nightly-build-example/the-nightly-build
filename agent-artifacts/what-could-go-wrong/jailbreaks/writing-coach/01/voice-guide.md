# Voice guide — what-could-go-wrong/jailbreaks

Register: adversarial-ML field register, not general-audience AI commentary.
Write the way a careful red-teamer briefs a smart colleague who wasn't in the
room: plain sentences, exact numbers, no persuasion beyond the evidence shown.
Reader relationship: treat the reader as capable of weighing the argument
themselves once the facts and the gaps are both on the table. Never reassure
them and never alarm them; report the finding and let its weight do the work.

Moves that will change sentences in this piece:

- Open by conceding the defender's argument at full mechanism, not just at
  tone. State the actual reasoning step (fine-tuning is a thin layer over
  weights that already hold the capability; worst-case robustness has decades
  of adversarial-ML evidence against it) before any qualifier appears. A
  concession that only softens tone while withholding the mechanism reads as
  a hedge, not a steelman.
- Reverse the default burden of proof when reporting a defense. Treat "this
  attack still works, in some form, against the newest defense" as the base
  rate to disprove, not "the defense holds" as the default. When a defense
  looks like it's winning, name the exact attack that was tried against it
  and what specifically failed, not just the headline success-rate drop.
- Define contested terms by mechanism, not by the behavior they produce.
  "Refusal is a learned pattern over token sequences, not an enforced
  boundary between instruction and data" identifies by what physically
  happens; "refusal sometimes fails" identifies only by outcome and invites
  the reader to conflate two different failure modes. This is the same
  discipline the mechanism link (instructions-are-data) already established;
  extend it rather than re-derive it.
- Put each hedge word on the specific clause it covers, never as a blanket
  qualifier over a paragraph. "Probably," "not yet shown," "empirically
  unsolved but theoretically suspected hard" belong immediately next to the
  claim they weaken. A reader should be able to point at the single word that
  marks a claim as conjecture rather than fact.
- Give every number its method: which model, which attack, how many
  attempts, whose count. A success rate without the attack that produced it
  is not evidence, it's a headline.
- When a gap in a defense needs an explanation, attribute it to a structural
  or systemic cause (what the training objective can and can't reach, what
  an evaluation covers and doesn't) rather than to any actor's diligence or
  motive. This keeps the piece from naming a company as an authority while
  still explaining why the gap exists.

Recently used, do not reuse: the desk's "the record runs out before the
catastrophe" / "X has never once been logged" closer or its cadence; a
scenario-triad open; a colon-subtitle headline; a hedged-contrast dek (the
"X is not Y; it is Z" mold or its softer cousins, in the dek specifically).

## Nicholas Carlini, "Are Adversarial Example Defenses Improving?"
Source: https://nicholas.carlini.com/writing/2020/are-adversarial-exampe-defenses-improving.html
Craft:
- cadence: short declarative sentences that report a result and stop; a
  caveat gets its own short sentence rather than a subordinate clause.
- argument: empirical and comparative. A controlled sweep of many defenses
  against adaptive attacks carries the claim; there is no rhetorical build to
  a thesis, the tally is the thesis.
- evidence: names each defense, names the specific adaptive attack used
  against it, gives the resulting success rate. Never a bare percentage.
- stance: unsparing about what broke, sympathetic about why (evaluation
  incentives, time pressure), and explicit that this is a systemic problem,
  not a case of any author acting in bad faith.
- notice: separates "evaluation methodology got more rigorous" (real,
  demonstrated progress) from "defenses got stronger" (not yet shown) —
  two claims a less careful writer would collapse into one.
- diction: plain, unhedged verbs for what happened ("broke," "failed"), held
  apart from clearly marked hedges for what's still open.
- reader: someone who wants the honest tally over reassurance, and will
  check the method behind any number that surprises them.
- the move the axes miss: he treats a defense that survives as the surprise
  needing extra scrutiny, not the default expectation. That reversed burden
  of proof is exactly the posture needed when weighing whether current
  defenses are "winning."
Calibration: "We could break all of the defenses we selected. And worse,
defenses are failing in just the same way as before."

## Simon Willison, "Prompt injection and jailbreaking are not the same thing"
Source: https://simonwillison.net/2024/Mar/5/prompt-injection-jailbreaking/
Craft:
- cadence: short paragraphs, each doing exactly one job; a key claim often
  gets its own one-sentence paragraph so it can't be missed or diluted.
- argument: isolates two things practitioners conflate, defines each by what
  physically happens rather than by what the attack achieves, then shows why
  the conflation leads to the wrong defense being built.
- evidence: a concrete worked scenario (a digital assistant reading a
  calendar invite) stands in for citations, making an abstract mechanism
  distinction tangible without needing a study.
- stance: corrective without scolding; owns his share of the confusion
  ("I clearly haven't done a good enough job of maintaining the term")
  rather than blaming the reader for missing the distinction.
- notice: catches that two attacks can look identical from the outside — the
  model does something unwanted either way — while needing different fixes,
  because the mechanism that produced them differs.
- diction: everyday words standing in for technical operations; a term like
  "concatenation" is explained at first use, not assumed.
- reader: an engineer who will build something this week and needs the
  distinction to choose the right defense, not to win an argument.
- the move the axes miss: he defines by mechanism first and lets the
  consequence follow, rather than defining by consequence and working
  backward. A mechanism-first definition stays stable even when two
  mechanisms produce the same visible failure, which is the exact trap this
  article's central term (robust refusal) sits in.
Calibration: "Crucially: if there's no concatenation of trusted and
untrusted strings, it's not prompt injection."

## Buck Shlegeris, "Why imperfect adversarial robustness doesn't doom AI control"
Source: https://www.lesswrong.com/posts/ewfGpHMXHhiwCA7se/why-imperfect-adversarial-robustness-doesn-t-doom-ai-control
Craft:
- cadence: a structured rebuttal, one point per short paragraph, no
  rhetorical questions and no dramatic beats — the structure itself is the
  pacing.
- argument: concedes the opposing premise in full before showing the
  conclusion doesn't follow from it; separates "this would help" from "this
  is necessary," which is where the doom argument actually breaks.
- evidence: builds a concrete mechanism scenario (what a trusted-model check
  can and can't detect) instead of citing a benchmark, because the claim
  under test is structural and hasn't been measured yet.
- stance: charitable to the position he's arguing against; explicit that
  parts of his own rebuttal are probabilistic rather than settled.
- notice: catches that "adversarial robustness is imperfect" and "imperfect
  robustness is fatal to this plan" are two different claims routinely
  merged into one.
- diction: plain working-paper register, no drama words, no verdict language
  ahead of the argument that would earn it.
- reader: an informed peer who already holds the opposing view and needs to
  be walked through why it doesn't fully follow, not persuaded by tone.
- the move the axes miss: he places the hedge word directly on the specific
  unproven clause inside his own argument ("probably," "maybe a bad design
  choice"), so the reader can see exactly which links in his own chain are
  solid and which are his best guess. The hedge placement is the argument's
  honesty mechanism, not a stylistic softener.
Calibration: "I agree that better adversarial robustness would definitely
help with control, but I think this argument misses several important
points."
