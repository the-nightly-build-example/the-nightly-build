# Voice guide: the-mechanics/hands-in-generated-images

## How this piece should sound

This lesson starts from a picture almost everyone who has used an image generator
has seen: a hand with six fingers, or fingers that melt together. The reader is
quick, reads widely, and has never worked inside a model. Hold the register Julia
Evans holds when she finally troubleshoots DNS and finds it was not that hard. The
six-fingered hand is an ordinary result of an ordinary process, and the lesson
explains it as something that makes plain sense once the parts are on the table.
Evans reaches that register in the first person, telling the story of her own
learning. Take the matter-of-factness from her, and leave the first-person
telling: here the explanation stands on its own without a learner narrating it.

The reader arrives assuming the model must hold some notion that a hand has five
fingers, the way Ciechanowski's reader assumes the date ring could be tied
straight to the hour wheel. Ciechanowski names that assumption out loud before he
takes it apart, and gives the exact thing that goes wrong. The turn this lesson
rests on has the same shape. Nothing in the denoising process counts fingers or
stores a model of anatomy, and the reason is that the objective rewards a patch
that looks locally like real texture and an image that hangs together globally,
with no step anywhere that checks a hand for five fingers. Where the lesson can
name the assumption the reader brought before dismantling it, the dismantling
gives a concrete reason rather than a gesture at one.

Each step names a real part of the system and says what it does: the starting
noise, a denoising step, the training images a hand appears in, the objective
being optimized. Dan Luu, at the top of "Files are fraught with peril", lists the
layers he will descend through and attaches to each one the finding it will yield,
so the reader knows what each layer costs before he opens it. There is room to do
that here, saying at each step what that step explains about the six fingers
before going inside it, and to keep descending until a step where nothing below it
would change the answer. Luu also marks measured error rates against the numbers on
the datasheet, which is the same move the series asks for here: mark which parts
are settled and which are open even to the people who build these models. That
hands are small in the frame and turn up across a huge range of poses and grips is
reasonably understood. Whether the failure is solved is a moving target, and the
lesson can say which of its claims rest on the diffusion primaries and which rest
on softer practitioner explanation.

Some steps turn abstract: a diffuse spread of learned "hand" pixels, an
interpolation to something hand-shaped and plausible. Where one does, a concrete
anchor the reader already holds can carry it, the way Ciechanowski lets a push
given to someone on a swing carry a claim about how the balance wheel keeps its
energy without losing the mechanism underneath. The anchor earns its place only
when it is exact. Ciechanowski also states a design problem as arithmetic, 40
hours and 2400 rotations, and lets the figures show the size instead of calling
anything large or small. Where a real figure would make "small in the frame" or
"little signal" concrete, the figure carries more than the adjective would.

The six fingers are the expected output of this process, and the lesson can
present them that way rather than as a malfunction someone forgot to fix. Luu's
finding, that every program tested but one had a bug and that the experts who
wrote them still cannot write files safely, lands because the wrongness follows
from the system and not from anyone's mistake. The model producing a bad hand is
doing exactly what it was trained to do. And where the hand-specific claim rests
on thinner evidence than the mechanism does, the lesson can say so outright, the
way Evans says plainly that she does not have as good an answer as she would like.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "You may wonder why we need this complicated mechanism in the first place. One could naively assume that we could directly tie the rotation of the date ring to the rotation of the hour wheel, similarly to how we rotated the hour wheel in sync with minutes, albeit at slower pace. Unfortunately, this would cause the current date to continuously rotate under the little window in the dial, making it hard to read."

Ciechanowski states the simple design a reader would reach for, tying the date
ring straight to the hour wheel, and then gives the exact thing that goes wrong
with it: the date would slide continuously under the window instead of sitting
still. The reason is physical and checkable. The writer is visible in the decision
that the reader's own guess is worth naming before it is taken apart.

> "Once unlocked, the escape wheel powered by the mainspring pushes on the pallet fork which, through the jewel roller, pushes on the balance wheel itself. This causes the balance wheel to gain some energy, which prevents it from stopping after a while – it's equivalent to giving a push to a person swinging on a swing. When the balance wheel comes back, it performs the same action, just in the other direction."

The first sentence is a chain of real parts handing force to one another, each part
named. Then the effect gets anchored to something the reader has felt, a push
given to someone on a swing, and the comparison is exact rather than decorative.
Ciechanowski trusts a familiar motion to carry a claim about energy without
letting go of the mechanism that produces it.

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we'd need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands."

The design problem is stated as arithmetic the reader can follow, from 40 hours to
40 rotations to 2400. Nothing is called large or small; the numbers do that work.
Ciechanowski uses the figures to set up the next part by naming exactly what has
to be solved.

## Dan Luu, "Files are fraught with peril"

Source: https://danluu.com/deconstruct-files/

> "In this talk, we're going to look at how file systems differ from each other and other issues we might encounter when writing to files. We're going to look at the file "stack" starting at the top with the file API, which we'll see is nearly impossible to use correctly and that supporting multiple filesystems without corrupting data is much harder than supporting a single filesystem; move down to the filesystem, which we'll see has serious bugs that cause data loss and data corruption; and then we'll look at disks and see that disks can easily corrupt data at a rate five million times greater than claimed in vendor datasheets."

Luu lays out the three layers he will descend through and attaches to each one the
finding it will yield, so the reader knows where the piece is going and what each
layer costs. The sentence is long but stays under control because every clause
names a real layer and a concrete failure. The claims are specific enough to
check, down to the rate five million times greater than the datasheets say.

> "When they did this, they found that every single piece of software they tested except for SQLite in one particular mode had at least one bug. ... But they still can't use files safely every time!"

Luu gives the measured result flat: nearly every program tested had a bug, and the
authors still cannot use files safely. The judgment sits on the finding rather
than on adjectives, and the plainness is what registers the surprise. Luu trusts
the number to do the work an intensifier would otherwise be asked to do.

> "Something I find interesting is that, in these discussions, people will drop into a discussion where it's already been explained, often in great detail, why writing to files is harder than someone might naively think, ignore all warnings and explanations and still proceed with their explanation for why it's, in fact, really easy. Even when warned that files are harder than people think, people still think they're easy!"

Luu names a pattern he watched happen: people shown in detail why the thing is
hard, who conclude it is easy anyway. It is an observation about real behavior, so
it holds up on what it reports rather than on how it is phrased. The closing
exclamation is earned because the sentence before it did the work.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When I finally learned how to troubleshoot DNS problems, my reaction was "what, that was it???? that's not that hard!". I felt a little bit cheated! I could explain to you everything that I found confusing about DNS in a few hours."

Evans reports her own reaction to finally understanding something that had seemed
hard, including the flat letdown of it. The register is specific and unguarded,
from the four question marks to the feeling of being cheated, and it makes the
difficulty ordinary instead of mysterious. A person is on the page here, not a
narrator standing outside the material.

> "I don't have as good answers here as I would like to, but knowledge about weird gotchas is extremely hard won (again, it took me years to figure out negative caching!) and it feels very silly to me that people have to rediscover them for themselves over and over again."

Evans admits she does not have a good answer, then says plainly why the knowledge
is hard to come by, that it is won slowly and then rediscovered by the next person
from scratch. The honesty about the limits of her own advice is the thing worth
reading. She states what is unresolved instead of papering over it.
