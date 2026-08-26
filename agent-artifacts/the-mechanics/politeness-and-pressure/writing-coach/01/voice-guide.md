# Voice guide: the-mechanics/politeness-and-pressure (01)

## How this piece should sound

This is a Mechanics lesson. It starts from something the reader has done many
times, changing the tone of a prompt by adding a please, or telling the model
the answer matters, or warning that someone will be hurt if it gets this wrong,
and it walks back step by step to what inside the system makes wording and tone
move the output. The reader is smart and widely read, has never worked in a
codebase, and keeps meeting claims about AI they cannot check. Write for that
reader without talking down and without flattering the tone tricks they have
tried.

Hold the register plain and confident, the way Julia Evans opens by asking one
small, concrete question about a thing everyone has done at a terminal. The
answer to this lesson exists and can be stated directly, so the craft is in the
walk down to the mechanism, and the writing can be as plain as the answer allows.
Where the chain from tone to output runs through a step that is genuinely
unsettled among the people who build these models, say so as flatly as Ed Regis
reports that no one agrees on what generates lift. The series asks the lesson to
mark which steps are settled engineering and which are open, and an honestly
marked open step is a strength here as long as the settled steps are stated with
the same plainness.

Some steps in this chain are the writer's reasoning rather than something
measured, and Evans's "I believe the reason `cat` gets interrupted" shows how to
flag that boundary while still stating the chain in full. A lesson's body speaks
to no one and uses no "I," so that boundary gets marked in plain language that
tells the reader which link is inference and which is established. Where the
lesson meets a folk account of why politeness or pressure works, the tidy story
people pass around, Regis's handling of the equal transit time theory is the
model to study: name the claim exactly, then show the step it skips, rather than
waving it off. This belongs in the lesson only if the piece actually runs into
such an account.

When a step in the mechanism is abstract, the reader can be handed a comparison
they already hold, the way Regis uses lanes of traffic merging on a highway,
provided the comparison carries the real point and is dropped once it has done
its work. The reader also arrives with a naive picture of what a prompt does to a
model, and that picture is worth taking as seriously as Ciechanowski takes the
date ring a reader would wire straight to the hour wheel before he shows what it
would actually do. When the lesson reaches a figure the reader cannot scale on
their own, how far a phrasing shifts a probability, or how much of the training
text carries a given pattern, give the figure and where it comes from rather than
"a lot" or "tiny." Let the named parts of the system carry the explanation, and
stop the walk at the step below which nothing would change the answer.

## Julia Evans, "What happens when you press a key in your terminal?"

Source: https://jvns.ca/blog/2022/07/20/pseudoterminals/

> "I've been confused about what's going on with terminals for a long time.
>
> But this past week I was using xterm.js to display an interactive terminal in a
> browser and I finally thought to ask a pretty basic question: when you press a
> key on your keyboard in a terminal (like `Delete`, or `Escape`, or `a`), which
> bytes get sent?
>
> As usual we'll answer that question by doing some experiments and seeing what
> happens :)"

She opens by admitting she has been confused about the subject for years, then
narrows to one small, answerable question about something anyone using a terminal
has done. The confidence comes from how concrete and bounded the question is,
not from a claim of authority. Evans is visible in the choice to start from her
own confusion instead of hiding it.

> "I believe the reason `cat` gets interrupted when we press `Ctrl+C` is that the
> Linux kernel on the server side receives this `\x03` character, recognizes that
> it means "interrupt", and then sends a `SIGINT` to the process that owns the
> pseudoterminal's process group. So it's handled in the kernel and not in
> userspace."

She marks the edge of what she knows and keeps going: "I believe" flags that the
`SIGINT` chain is her reasoning rather than something she watched happen, and the
sentence then lays out that chain link by link down to the kernel. The honesty
and the precision sit together, and Evans is the kind of writer who says exactly
which part is inference.

> "Escape codes are why your terminal can get messed up if you `cat` a bunch of
> binary to your screen – usually you'll end up accidentally printing a bunch of
> random escape codes which will mess up your terminal – there's bound to be a
> `0x1b` byte in there somewhere if you `cat` enough binary to your terminal."

She connects a familiar annoyance, a terminal turning to garbage after you dump a
binary to it, to its exact cause, a stray `0x1b` byte read as an escape
character. The explanation lands because it names the specific byte instead of
gesturing at "weird characters." The plain "there's bound to be" is Evans
trusting the reader to follow the mechanism on their own.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single
> wind, we'd need the minute hand to complete 40 rotations in that time.
> Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations
> in that time. We need to find a way to convert a small number of revolutions of
> the barrel into a large number of revolutions of the hands. This is where gears
> come in."

He sets the problem in real numbers before naming any solution, so the reader
feels the gap between a barrel that turns a few times and a second hand that must
turn 2400 times. Only once the arithmetic has made the problem concrete does he
say where gears come in. The plainness is deliberate, and Ciechanowski trusts the
figures to supply the motivation.

> "As the balance wheel swings, the jewel roller strikes the pallet fork, which
> unlocks the escape wheel. Once unlocked, the escape wheel powered by the
> mainspring pushes on the pallet fork which, through the jewel roller, pushes on
> the balance wheel itself. This causes the balance wheel to gain some energy,
> which prevents it from stopping after a while – it's equivalent to giving a push
> to a person swinging on a swing."

He traces one full cycle of the mechanism in order, each named part acting on the
next, and only then reaches for a familiar image to explain why the wheel does
not run down: a push given to someone on a swing. The named parts do the
explaining and the comparison arrives to answer one specific question. The chain
is easy to follow because he never skips a link in it.

> "You may wonder why we need this complicated mechanism in the first place. One
> could naively assume that we could directly tie the rotation of the date ring
> to the rotation of the hour wheel, similarly to how we rotated the hour wheel
> in sync with minutes, albeit at slower pace. Unfortunately, this would cause the
> current date to continuously rotate under the little window in the dial, making
> it hard to read."

He states the simpler design the reader would reach for, tying the date ring
straight to the hour wheel, then shows the concrete failure it produces: the date
creeping under the window all day instead of flipping over near midnight. He
takes the reader's likely guess seriously enough to name it and to refute it with
what it would actually do. That attention to the naive guess is where the teacher
is visible.

## Ed Regis, "No One Can Explain Why Planes Stay in the Air"

Source: https://www.scientificamerican.com/article/no-one-can-explain-why-planes-stay-in-the-air/

> "What Anderson said, however, is that there is actually no agreement on what
> generates the aerodynamic force known as lift. "There is no simple one-liner
> answer to this," he told the Times. People give different answers to the
> question, some with "religious fervor.""

He opens on a behavior no one doubts, planes staying up, and reports plainly that
the field has no agreed explanation for it, quoting a named curator rather than
"experts." He neither softens the surprise nor hurries to resolve it. Regis is
willing to let the puzzle stand and to pin it to a specific person the reader
could check.

> "There are plenty of bad explanations for the higher velocity. According to the
> most common one—the "equal transit time" theory—parcels of air that separate at
> the wing's leading edge must rejoin simultaneously at the trailing edge. Because
> the top parcel travels farther than the lower parcel in a given amount of time,
> it must go faster. The fallacy here is that there is no physical reason that the
> two parcels must reach the trailing edge simultaneously. And indeed, they do
> not: the empirical fact is that the air atop moves much faster than the equal
> transit time theory could account for."

He names the most common explanation exactly, states its claim in full, then says
where it breaks and gives the fact that contradicts it: the air on top moves
faster than the theory allows. He does not mock the wrong answer. He shows the
reader the physical step it assumes without warrant. The care is in refuting the
popular account on its own terms.

> "It might be natural to think that when a wing's curvature displaces air upward,
> that air is compressed, resulting in increased pressure atop the wing. This kind
> of "bottleneck" typically slows things down in ordinary life rather than
> speeding them up. On a highway, when two or more lanes of traffic merge into
> one, the cars involved do not go faster; there is instead a mass slowdown and
> possibly even a traffic jam. Air molecules flowing atop a wing do not behave
> like that, but Bernoulli's theorem does not say why not."

He takes an expectation the reader would form on their own, that squeezed air
should slow and press harder, and grounds it in merging highway lanes before
noting that air does not behave that way. The comparison does the work of
explaining, and then he is honest that the theorem still does not say why the air
differs. Regis anchors the idea in something the reader already knows and refuses
to claim more than the physics gives him.
