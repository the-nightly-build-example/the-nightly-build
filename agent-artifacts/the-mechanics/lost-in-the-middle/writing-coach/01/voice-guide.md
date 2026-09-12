# Voice guide: the-mechanics/lost-in-the-middle

## How this piece should sound

This is a lesson that starts from something the reader has watched happen — a fact
buried in the middle of a long prompt gets used less reliably than the same fact
near the top or the bottom — and works back to what inside the model produces it.
Write it for a reader who is smart and reads widely but has never been shown how a
model takes in a long input. Keep the claims plain and the stakes concrete, down to
what breaks when the key sentence sits in the middle of a pasted document, and when
a sentence has to choose between sounding good and being understood, choose being
understood.

Build the explanation the way Bartosz Ciechanowski builds GPS. Start from a version
of "how a model reads a long input" simple enough to hold in one hand, then add only
the machinery each step needs: how a position in the sequence gets represented at
all, how attention divides its weight across many tokens at once, and what in the
training data would make the start and end of a long example behave differently from
its middle. A toy version of the input can be openly artificial, the way his drones
are, as long as the piece names the one idea worth carrying forward before it moves
to the next stage.

Where the behavior is a matter of degree, a small worked model with the measured
numbers in it does more than an adjective. Ciechanowski's drone example and Dan Luu's
"cartoon model" both work because the numbers are stated out loud and the reader can
check them. Accuracy that traces a U by position is the kind of claim that should
arrive with the figures the primaries actually recorded, at the sizes they measured.
The adjective on its own, "worse in the middle," leaves the reader nothing to check.

The register problem in this piece is the pull toward saying models ignore the
middle. Meet that claim the way Ciechanowski meets the myth about GPS and relativity:
grant the part of it that holds, then say exactly where it stops holding. Something
real is being reported, and it survives a bigger advertised context window. Both of
those are true and can be stated without stretching the effect past what was
measured.

The mechanism underneath is not fully settled, and the piece is stronger for saying
which parts are. Name the competing accounts the reader will meet — decay in the
positional encoding, dilution of attention across a long sequence, the shape of the
training distribution — and say which is established and which is still argued over.
Julia Evans admitting "I'm not sure what that means" about a line of DNS output is
the model for this: flagging the edge of what is known reads as trustworthy, and a
reader can tell a settled step from a live question when the writer marks it.

Keep the real vocabulary. This reader can be taught attention, positional encoding,
context window, and retrieval, each defined plainly the first time it is used, and is
better served by the actual terms than by softer stand-ins. Evans's line about output
that is reformatted but "not dumbed down" is the standard for the long-context and
retrieval sections: make the machinery legible without thinning what it says.

## Bartosz Ciechanowski, "GPS"

Source: https://ciechanow.ski/gps/

> We'll start by creating a positioning system that can tell us where we are. Our initial approach will be quite simple, but we'll step-by-step improve upon it to build an understanding of the positioning method used by GPS.

He tells the reader at the outset that the model will start crude and get better in
stages, and every later section adds one capability the previous one lacked. The
"we'll" keeps him constructing the system alongside the reader instead of unveiling a
finished one. The person shows in the patience: he is willing to spend a whole stage
on an idea he already knows he will replace.

> This method is less restrictive than the measuring tapes we've used, but having to fly drones to the landmarks to measure distances is still a bit ridiculous. However, the idea of using time of flight is very promising, we just need to come up with a faster and more convenient messenger.

He calls his own example ridiculous in the same breath that he keeps the single idea
worth keeping from it, using travel time as a stand-in for distance. Naming the
absurdity is where the voice is unguarded, and it lets him throw away the scaffolding
without ever having pretended it was the real answer.

> Those assertions are not true. If relativistic effects weren't accounted for and we let the clocks on satellites drift, the pseudoranges would indeed increase by that amount every day. However, as we've seen, an incorrect clock offset doesn't prevent us from calculating the correct position.

He takes a claim that circulates widely, grants the exact part of it that is true —
the drift really would happen — and then draws the precise line where it stops being
true. The correction is careful rather than triumphant. He does not mock the sources
he disagrees with, and he says what actually goes wrong instead of only that the
claim is false.

## Dan Luu, "Branch prediction"

Source: https://danluu.com/branch-prediction/

> One way you might design a CPU is to have the CPU do all of the work for one instruction, then move on to the next instruction, do all of the work for the next instruction, and so on. There's nothing wrong with this; a lot of older CPUs did this, and some modern very low-cost CPUs still do this. But if you want to make a faster CPU, you might make a CPU that works like an assembly line.

He introduces pipelining with an everyday image and, in the next breath, grounds it
in a fact about real chips: older and low-cost CPUs actually do the slow version. The
analogy carries the idea and the fact keeps it tied to the hardware. The plain
"There's nothing wrong with this" is the writer talking, unhurried, not selling.

> What's the performance impact of doing this? To make an estimate, we'll need a performance model and a workload. For the purposes of this talk, our cartoon model of a CPU will be a pipelined CPU where non-branches take an average of one instruction per clock, unpredicted or mispredicted branches take 20 cycles, and correctly predicted branches take one cycle.

Before he estimates anything he states the model he is estimating with, out loud,
including the number he assigns to each case. Calling it a "cartoon model" is honest
about how simplified it is, and it lets the reader follow the arithmetic that comes
next instead of taking the speedup on trust.

> There are a lot of things we didn't cover in this talk! As you might expect, the set of material that we didn't cover is much larger than what we did cover. I'll briefly describe a few things we didn't cover, with references, so you can look them up if you're interested in learning more.

At the end he lists what he left out and points to where the reader can find it,
without pretending the talk was complete. The exclamation and the direct "I'll
briefly describe" are the person on the page, and the move draws a clean border
between the part he explained and the part he is only naming.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> I'm not sure what that means (it's some DNSSEC Thing), but it's cool to see an extra debug message like that.

She hits a piece of output she cannot fully explain and says so plainly, then keeps
going. Admitting the gap costs her nothing, and it is part of why the rest is
believable, because the reader can see she marks what she does not know. "Some DNSSEC
Thing" is her voice, casual and exact at the same time.

> And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly.

She draws a hard line between making something clearer and stripping information out
of it, and she wants the first without the second. The plain, slightly indignant tone
of "I want to see all the information!" is the person, and the standard underneath it
is for explanation itself: reformat for the reader, do not thin the content.
