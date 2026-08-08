# Voice guide: data-poisoning lesson (what-could-go-wrong)

## Directive

Write in a cool evidentiary register that does not change temperature between the
two halves of the piece. The lesson states a security argument at full strength and
then tests it against what has actually been shown. The default already gives you
plain claims, concrete stakes, and no hype or doom. What this piece needs on top of
that is a steadiness the default does not enforce: the prose must not lean in when it
describes the danger, and must not cool to relief or mockery when it finds the proof
thin. One hand holds the argument; the same hand weighs it. A reader should not be
able to tell from the sentence rhythm which side of the demonstrated/analogy line
they are standing on.

Two moves carry the whole lesson, and both are places the writer's temperature tends
to slip.

State the argument in the confidence its holders actually have. When you lay out why
a poisoned training set is dangerous, phrase the reasoning at the strength its careful
defenders would use, and attribute that strength to them, not to the paper. Do not
pre-soften it with hedges that no serious proponent would add. The argument earns its
force from being reported accurately, not from the writer performing worry.

Draw the demonstrated/analogy line as the spine of the piece, and make each crossing
carry new content. The distinction between what a lab has shown and what is still
analogy about deployed systems is the argument. It will recur. Guard it against
becoming a rhetorical seesaw: every time you mark the line, name the specific result
on the shown side and the specific missing condition on the not-yet side. A crossing
that only restates "proven here, unproven there" without a new fact is a tic; cut it.

Keep the attacker concrete. A backdoor, a trigger, a poisoned document are physical
things an attacker does; write them as actions with real mechanics, not as an abstract
"vulnerability." The reader understands a threat model by watching it operate once, at
the grain of what the attacker touches.

## Licenses

form: the worked attack, rendered in operational detail
move: Carlini walks the reader through the exact mechanism that breaks a system, at
  the level of the single change that does it; Schneier renders a threat as a specific
  scene before weighing it. The concrete rendering is what lets a general reader hold
  the threat model precisely enough to then judge it.
bar:  every mechanical detail traces to a demonstrated capability, not an invented one,
  and the passage returns to what was actually shown before the reader could mistake the
  scenario for the evidence. One scene that teaches the mechanism, not a montage.

form: the flat verdict at the evidentiary seam
move: Carlini states what a result forecloses in one short declarative ("the only cause
  is a mistake in the evaluation") and lets the surrounding evidence stand behind it,
  never raising his voice to land it.
bar:  the same passage shows what the verdict rests on, the sentence names what the proof
  does or does not establish rather than how alarming it is, and it reads at the same
  temperature as the sentences around it. If it needs emphasis to land, it has not been
  earned.

form: the repeated demonstrated-versus-analogy distinction as the organizing contrast
move: the house default caps earned "X, not Y" contrasts at one or two because they
  usually mark invented oppositions. Here the opposition is real, named, and load-bearing,
  and the lesson is built on returning to it.
bar:  both sides are real and specified at each use, never a strawman; each crossing adds
  a new result or a new missing condition the reader did not have; and the shapes vary, so
  the seam is not stamped by one repeated sentence mold.

## Nicholas Carlini, "Why I Attack" / "(yet another) Broken Adversarial Example Defense at IEEE S&P 2024"
Source: https://nicholas.carlini.com/writing/2024/why-i-attack.html , https://nicholas.carlini.com/writing/2024/yet-another-broken-defense.html
Craft:
- cadence: patient exposition that builds the mechanism step by step, then lands a short
  crisp verdict; the rhythm slows to teach and snaps shut to conclude.
- argument: establish the principle, then apply it to a specific system; the general claim
  is always cashed out in one concrete case the reader can inspect.
- evidence: separates what is mathematically forced (reproducible, universal) from what is
  a specific evaluation failure (shown by a code diff or a figure from the paper itself);
  uses the source's own numbers to refute the source's own claim.
- stance: an attacker's discipline about proof; a claim is interesting only once someone has
  actually broken or built the specific thing, not argued about it in general.
- notice: the exact seam where a defense's claim outruns its demonstration, and the single
  change that exposes it.
- diction: precise and unshowy, technical terms defined as used, occasional dry aside; never
  reaches for a big word to carry a point the evidence should carry.
- reader: treated as a fellow investigator who is being taught the standard of proof, then
  handed the tools to check the claim themselves.
- the move the axes miss: he refuses to let drama do the work of evidence. Even when
  exasperated, the verdict rests on a shown fact, not on the writer's certainty. Borrow the
  evidentiary discipline; leave the exasperation, which runs hotter than this lesson wants.

## Bruce Schneier, "Movie-Plot Threats"
Source: https://www.schneier.com/blog/archives/2005/09/movie-plot_thre.html
Craft:
- cadence: alternates short punchy observations with longer explanatory passages; the vivid
  scene is delivered fast, the analysis unspools slowly.
- argument: renders the frightening specific scenario in full, then steps back to ask whether
  it matches the actual distribution of risk; the vividness is the thing being examined.
- evidence: contrasts the memorability of a specific scenario against the breadth of what could
  actually happen; the specific detail is treated as a psychological fact, not a probability.
- stance: neither alarm nor mockery; a cool analytical distance held equally from panic and
  from complacency.
- notice: that a threat's vividness and its likelihood are different quantities, and the mind
  swaps one for the other.
- diction: plain, no jargon, general-audience; concrete nouns (crop dusters, scuba divers)
  carrying the argument.
- reader: addressed as an intelligent layperson whose fear is understandable and whose judgment
  is being trained, not corrected.
- the move the axes miss: he validates the psychology of the fear before scrutinizing the
  response to it, which is what lets the scrutiny stay sympathetic rather than dismissive. This
  is the one-temperature model for this lesson: take the worry seriously as you weigh it.

## Scott Alexander, "Beware The Man Of One Study"
Source: https://slatestarcodex.com/2014/12/12/beware-the-man-of-one-study/
Craft:
- cadence: builds a mental picture (the spread of results) before drawing its consequence;
  colloquial interjections keep a rigorous argument moving.
- argument: takes a single striking result seriously and grants it is well done, then shows
  where it sits in the fuller body of evidence and how much that placement changes the reading.
- evidence: concrete numbers and named cases rather than abstractions; the skepticism is
  structural, built from how evidence aggregates, not from doubting any one study.
- stance: cool distance from the outcome; models holding a finding at arm's length without
  either believing or dismissing it on sight.
- notice: the gap between one demonstration and the distribution it was drawn from, and how
  easily a reader mistakes the first for the second.
- diction: conversational while handling formal reasoning, which lowers the intimidation of the
  statistics without softening them.
- reader: taught a durable habit of mind, then trusted to apply it; not told what to conclude.
- the move the axes miss: he separates a result's validity from its usage. A demonstration can
  be entirely sound and still support far less than it appears to. That distinction is exactly
  the seam this lesson works, between a real lab result and what it licenses you to believe
  about deployed systems.

## Self-test

A writer following only the house default would already sound cool, plain, and evidentiary.
What this guide adds is the demand that the temperature hold flat across the steelman and the
test, that the demonstrated/analogy line be built as the piece's spine rather than mentioned
once, and that a concrete attack be rendered without letting the scene stand in for proof. A
draft that warms while describing the danger, or relaxes into relief when the proof turns out
thin, has missed the one thing this lesson needs that the default does not supply.
