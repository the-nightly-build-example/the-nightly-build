# Voice guide: the-evidence/batch-normalization (01)

## How this piece should sound

This lesson explains a mechanism practitioners have repeated for a decade —
internal covariate shift — and then reports the controlled experiment that
took it apart. The two Quanta passages below, from Philip Ball's piece on
cell signaling, are the model for that turn. Ball states the textbook
explanation in full first, in language that makes it sound reasonable, and
only then delivers the correction as one flat declarative sentence: "The only
problem with this story is that it is wrong." No hedge, no "not X but Y"
scaffolding, no drumroll. State what Ioffe and Szegedy proposed with the same
respect Ball gives the lock-and-key story, then correct it the same way: say
what the ablation actually showed, plainly, once.

The BMP passage gives this piece a specific move worth taking: a name that
outlived the mechanism it was coined for. "Bone morphogenetic protein" still
describes proteins that turn out to do far more than grow bone, because the
name froze at the moment of discovery while the science moved past it.
"Internal covariate shift" is the same kind of fossil — a phrase from the
2015 paper that the field still reaches for, years after the experiments that
should have retired it. The piece can use that parallel: the vocabulary
survived the explanation, and readers still hear "reduces internal covariate
shift" in talks and repos today. Naming that persistence is more useful than
just asserting the theory was wrong.

Generosity here means something specific: preserving what remains true after
the wrong mechanism is cut, the way Adam Mastroianni does with the 1974 car
crash study. He reports the failed replication in full — a re-run with ten
times the sample found no effect — and then holds onto the part that survived:
"I think the underlying point of this research is still correct: memory is
reconstructed, not simply recalled... But our memories are not so fragile
that a single word can overwrite them." Batch normalization is not the
mistake here. It works, reliably, at scale, and the lesson should say so as
plainly as it says the covariate-shift story doesn't hold. Cut the
explanation without cutting the technique's standing.

Adam Mann's account of the Mpemba effect supplies the other half of that
generosity: treat the original claim's plausibility as real, not as a
strawman to knock down. A physics teacher tells the boy who first reported
hot water freezing faster than cold, "You were confused. That cannot happen"
— and the teacher had ordinary intuition on his side, the same intuition that
made covariate shift sound right when Ioffe and Szegedy proposed it. The
piece earns its "not X, it's Y" contrast exactly once, on the mechanism
itself, because the misconception is real and specifically named in the
paper. It should not reach for that shape again in the takeaway or a section
header.

When the piece gets to the controlled experiment that actually overturned the
explanation, Mann's description of the thermometer-placement study is the
register to write it in: what varied, what was held fixed, and what the
measurement actually showed, in that order, with no editorializing folded
into the report of the result. The lesson template asks for a worked example
with real numbers; this is where it belongs, sized to what the ablation
actually measured rather than to how dramatic the reversal sounds.

Mastroianni's aside on sample size — "you need 46 men and 46 women just to
demonstrate the fact that men weigh more than women, on average" — is worth
imitating for a different reason: it gives the reader a number they can hold
against the study under discussion without a paragraph of statistical
throat-clearing. The paper's own experimental scale, and the scale of
whatever later work re-tested it, should get a comparison this concrete
somewhere in the piece.

None of this licenses a joke at Ioffe and Szegedy's expense. Every exemplar
here corrects a mechanism without diminishing the person who proposed it or
the technique that resulted. The piece can be direct about the theory being
wrong. It should never sound pleased about it.

## Philip Ball, "Biologists Rethink the Logic Behind Cells' Molecular Signals"

Source: https://www.quantamagazine.org/biologists-rethink-the-logic-behind-cells-molecular-signals-20210916/

> "The tidy, traditional explanation is that although the protein molecules
> that make up most of a cell's working parts are constantly bumping into one
> another, they treat nearly all of these encounters with indifference. Only
> when a protein meets another molecule that meshes exactly with an
> exquisitely sculpted part of its surface do the two lock together and
> interact."

Ball states the old model in its strongest, most reasonable form before
touching it. There is no signal here that a correction is coming; the sentence
reads like something a textbook would say without apology. That restraint is
what makes the next line land.

> "The only problem with this story is that it is wrong. Although many
> proteins do exhibit selective molecular recognition, some of the ones most
> central to the workings of our eukaryotic cells are far less picky."

The correction is one short declarative sentence, not a build-up. Ball doesn't
soften it with "turns out" or "surprisingly" — he just says the story is
wrong and moves immediately to what's actually true. The writer is visible in
the refusal to dramatize a moment that doesn't need it.

> "Their name comes from 'bone morphogenetic protein,' because the
> first-known gene for one was originally thought to encode a protein
> involved in bone formation. But although it is indeed involved in that...
> the idea that bone growth is the function of BMP proteins has long since
> proved illusory."

This passage, from a different part of the piece, shows Ball tracking how a
name survives the theory that produced it. He doesn't just report that the
old function was wrong; he shows the naming fossil that still misleads people
today, which is a more useful fact than the correction alone.

## Adam Mann, "Controversy Continues Over Whether Hot Water Freezes Faster Than Cold"

Source: https://www.quantamagazine.org/does-hot-water-freeze-faster-than-cold-physicists-keep-asking-20220629/

> "When Mpemba asked his physics teacher why this occurred, he was told, 'You
> were confused. That cannot happen.'"

One line of reported dialogue does the work of a paragraph of throat-clearing
about why the mechanism was believed. Mann doesn't explain that the belief
was reasonable — he shows a teacher being confident and wrong, and lets the
reader supply the judgment.

> "They found that the readings depended on where they placed the
> thermometer. If they compared the temperatures between hot and cold cups at
> the same height, the Mpemba effect didn't appear. But if measurements were
> off by even a centimeter, they could produce false evidence of the Mpemba
> effect."

This is the mechanics of the controlled experiment itself, told as a sequence
of what the researchers did and what they saw, with the finding stated as a
plain conditional rather than a verdict. Nothing here tells the reader how to
feel about the result; the centimeter is doing all the persuading.

> "Osborne... took a lesson from the initial skepticism and dismissal that
> the schoolboy's counterintuitive claim had faced: 'It points to the danger
> of an authoritarian physics.'"

Mann closes by quoting someone from inside the story rather than summarizing
the moral himself. The generosity toward the original, dismissed claim is
still present in the very last line — the piece never pivots to mocking the
people who got it wrong.

## Adam Mastroianni, "I swear the UFO is coming any minute"

Source: https://www.experimental-history.com/p/i-swear-the-ufo-is-coming-any-minute

> "You show people a video of a car crash, and then you ask them to estimate
> how fast the cars were going, and their answer depends on what verb you
> use... This study has been cited nearly 4,000 times, and its first author
> became a much sought-after expert witness who testifies about the
> faultiness of memory."

Mastroianni establishes the stakes of the original claim with a concrete
number — 4,000 citations, an actual expert-witness career — instead of
calling it "influential" or "famous." The reader can check the claim because
it's a citation count, not an adjective.

> "A blogger named Croissanthology re-ran the study with nearly 10x as many
> participants (446 vs. 45 in the original). The effect did not replicate...
> I think the underlying point of this research is still correct: memory is
> reconstructed, not simply recalled, so what we remember is not exactly what
> we saw. But our memories are not so fragile that a single word can
> overwrite them."

This is the passage to study for generosity under correction. Mastroianni
reports the failed replication flatly, then draws a line between what the
original study got wrong (a single word changing an estimate) and what it
was gesturing at correctly (memory is reconstructed). He keeps both truths
in the same paragraph instead of letting the correction erase the insight.

> "I think 'choice overload' is like many effects we discover in psychology:
> can it happen? Yes. Can the opposite also happen? Also yes."

A short, plain admission that a debunking doesn't always produce a clean
opposite. The two-question rhythm is Mastroianni's own voice showing through
— it reads like someone thinking out loud, not like a thesis statement.
