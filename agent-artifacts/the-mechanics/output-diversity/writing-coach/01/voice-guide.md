# Voice guide: the-mechanics/output-diversity

## How this piece should sound

This is a lesson for The Mechanics. It starts from something the reader has
watched a chatbot do — ask it for a story, a character name, or a "random" idea
a few times and the same few keep coming back — and works backward, one step at
a time, to the part of the system that produces the sameness. The reader is
quick and widely read and has never seen the inside of one of these systems.
Write for that reader in plain claims, and treat the everyday behavior as the
thing the lesson has to explain. Dan Luu opens on a
feeling anyone has had about slow computers and then, instead of arguing from
it, describes carrying a high-speed camera around for months to measure whether
it was real. The reader should come to believe the sameness is real because the
piece has shown it.

The desk's method is to name a real part of the system and say what it does
before the argument leans on it. Ciechanowski does this part by part: he
introduces the pinion, the escape wheel, the pallet fork, each with its job
stated plainly, and when he reaches the escapement he closes the causal chain on
pushing a person on a swing. This lesson moves through real parts of the model
the same way. A term from the field can enter carrying its plain-language job,
and where an everyday comparison makes a step concrete the way the swing does,
it earns its place.

Where a step turns on a quantity, the figure can do the work. Ciechanowski fixes
the requirement in numbers — 2400 rotations of the second hand on a single wind
— before the gears arrive to meet it, and Dan Luu attaches each stretch of delay
to a named component with the milliseconds shown. The commission also asks the
lesson to mark which steps are settled engineering and which are still open even
for the people who build these systems. Both can be said in the same level
voice: Dan Luu states his flat finding about latency without dressing it up, and
declines the easy line that complexity is simply bad by showing what the
complexity buys. State what is settled plainly, and say as plainly where the
builders themselves do not yet agree.

The restraint does not have to be humorless. Gawande's aside about house movers,
wedding planners, and tax accountants carries his argument about how ordinary
the fix is while it also amuses. A dry line is welcome where the subject earns
it and where it does not stand in for the explanation.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower than
> the computers I used as a kid. As a rule, I don't trust this kind of feeling
> because human perception has been shown to be unreliable in empirical studies,
> so I carried around a high-speed camera and measured the response latency of
> devices I've run into in the past few months."

The opening takes a feeling everyone has and refuses to trust it, then says the
concrete thing Luu did instead. He is visible in the decision to measure rather
than argue, and in naming his own unreliability before anyone else can.

> "At 144 Hz, each frame takes 7 ms. A change to the screen will have 0 ms to
> 7 ms of extra latency as it waits for the next frame boundary before getting
> rendered … On top of that, even though my display at home advertises a 1 ms
> switching time, it actually appears to take 10 ms to fully change color once
> the display has started changing color."

Each figure is attached to a named part of the pipeline — the frame boundary,
the display's color change — so the reader can see where the delay comes from.
Luu is the kind of writer who distrusts a spec sheet and reports what the part
actually does when he watches it.

> "Unfortunately, it's a lot harder to remove complexity than to give a talk
> saying that we should remove complexity. A lot of the complexity buys us
> something, either directly or indirectly. When we looked at the input of a
> fancy modern keyboard vs. the apple 2 keyboard, we saw that using a relatively
> powerful and expensive general purpose processor to handle keyboard inputs can
> be slower than dedicated logic for the keyboard, which would both be simpler
> and cheaper."

He declines the crowd-pleasing verdict that complexity is the villain and works
out what it actually buys, grounding the claim in the keyboard he already
measured. The passage shows a writer who would rather show a tradeoff than land
a clean line.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single
> wind, we'd need the minute hand to complete 40 rotations in that time.
> Moreover, the second hand should cover around 40 × 60 = 2400 complete
> rotations in that time. We need to find a way to convert a small number of
> revolutions of the barrel into a large number of revolutions of the hands.
> This is where gears come in."

He states what the mechanism has to achieve in plain figures before he names the
part that achieves it, so the gears arrive as the answer to a number the reader
is already holding. Ciechanowski is visible in the patience of setting the
requirement first.

> "As the balance wheel swings, the jewel roller strikes the pallet fork, which
> unlocks the escape wheel. Once unlocked, the escape wheel, powered by the
> mainspring, pushes on the pallet fork, which, through the jewel roller, pushes
> on the balance wheel itself. This causes the balance wheel to gain some
> energy, which prevents it from stopping after a while – it's equivalent to
> giving a push to a person swinging on a swing."

The causal chain is followable one link at a time, each part named and each
handoff shown, and it lands on a physical thing the reader has done. He ends an
abstract loop on the swing so the reader has a familiar motion to hold onto.

> "You may wonder why we need this complicated mechanism in the first place. One
> could naively assume that we could directly tie the rotation of the date ring
> to the rotation of the hour wheel, similarly to how we rotated the hour wheel
> in sync with minutes, albeit at a slower pace. Unfortunately, this would cause
> the current date to continuously rotate under the little window in the dial,
> making it hard to read."

He raises the simpler design the reader is already imagining, then gives the
concrete reason it fails before showing the real one. Ciechanowski is the sort
of explainer who answers the "why not just…" a step before the reader asks it.

## Atul Gawande, "The Checklist"

Source: https://www.newyorker.com/magazine/2007/12/10/the-checklist

> "An investigation revealed that nothing mechanical had gone wrong. The crash
> had been due to 'pilot error,' the report said. Substantially more complex
> than previous aircraft, the new plane required the pilot to attend to the four
> engines, a retractable landing gear, new wing flaps, electric trim tabs that
> needed adjustment to maintain control at different airspeeds, and
> constant-speed propellers whose pitch had to be regulated with hydraulic
> controls, among other features. While doing all this, Hill had forgotten to
> release a new locking mechanism on the elevator and rudder controls. The
> Boeing model was deemed, as a newspaper put it, 'too much airplane for one man
> to fly.'"

He explains a failure by listing the actual controls one person had to manage
and then naming the single step that was missed, so the cause is something the
reader can see rather than take on faith. Gawande counts the parts the way a
surgeon counts steps.

> "These steps are no-brainers; they have been known and taught for years. So it
> seemed silly to make a checklist just for them. Still, Pronovost asked the
> nurses in his I.C.U. to observe the doctors for a month as they put lines into
> patients, and record how often they completed each step. In more than a third
> of patients, they skipped at least one."

He calls the steps obvious and then reports the measured gap flatly, and the
number does the surprising. The restraint is his: he lets the finding land
without telling the reader how to feel about it.

> "These are, of course, ridiculously primitive insights. Pronovost is routinely
> described by colleagues as 'brilliant,' 'inspiring,' a 'genius.' He has an M.D.
> and a Ph.D. in public health from Johns Hopkins, and is trained in emergency
> medicine, anesthesiology, and critical-care medicine. But, really, does it
> take all that to figure out what house movers, wedding planners, and tax
> accountants figured out ages ago?"

The dry closing question carries the argument that the fix was humble, and it
earns the laugh because the comparison is a fair one. Gawande is visible in the
willingness to puncture the mystique of his own profession while keeping the
real person in view.
