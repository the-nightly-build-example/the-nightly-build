# Voice guide: why a chess-playing chatbot makes illegal moves

## How this piece should sound

This lesson works backward from one behavior — a chatbot announcing a chess
move that isn't legal — down through the real parts of the system that
produce it, until the reader hits a mechanism nothing below it would change.
The reader has never opened a codebase and never will for this lesson, so no
step can lean on code to do its explaining; every step has to hold up in
plain English or it hasn't been explained.

Shirriff's bug-fix post is the clearest model for the spine of the piece: one
settled fact stated plainly, then the next, before the mechanism they add up
to is named. He doesn't summarize ahead to the punchline and doesn't let two
facts share a sentence until both have been earned separately. This lesson
should hold that discipline at the load-bearing step — whatever part of the
system is actually responsible for the illegal move — rather than compressing
it into a single tidy sentence once the reader's patience is expected to be
thin. His conclusion is also the model for the honesty the series direction
asks for: he says plainly which part of his story is confirmed and which part
is still a guess he'd like to check, in his own words, not a hedge bolted on
at the end. Wherever this lesson reaches a step the field itself hasn't
settled, say so the same way — as a specific unresolved question, not a
vague gesture at uncertainty.

Heaton's HTTPS piece shows two moves worth having available, not using by
default. One is dramatizing a step through a specific invented exchange
rather than a description of it — his "are you Google?" / "here's a piece of
paper with 'I am Google' written on it" skit makes an abstract verification
step concrete in a way a paragraph of description doesn't. If this lesson
reaches a step that's hard to picture in the abstract — what the system is
actually doing in the instant it produces the impossible move — a small
invented exchange like that can carry it, as long as it stays accurate to
the mechanism and isn't reached for out of habit. The other is his FAQ
device: posing the reader's actual doubt as a direct question in the
reader's own words, then answering it plainly before building the case. A
reader of this lesson is likely to be holding a specific wrong assumption —
that the system must be checking the rules and failing, or that it's simply
guessing at random — and that doubt is worth meeting head-on the way Heaton
meets "can a coffee shop read my traffic?" rather than being left to erode
trust in the explanation later.

Ciechanowski's watch essay is the model for two smaller habits. He lets a
technical term enter only once its part has started doing something in the
story, and defines it in that same sentence — the spring isn't called the
mainspring until the moment its job is established. And where an abstraction
needs to land, he reaches for one number that does the work rather than a
word like "vast" or "enormous" — a 343:1 gear ratio, not "a lot of speed
increase." Both habits matter here: whatever term of art this lesson needs
for the mechanism (a model's move representation, its training signal,
whatever the research points to) should arrive at the moment it's doing
something, not before, and if the piece can ground the scale of the problem —
how large the space of illegal-looking moves is, how the behavior compares
across models or positions — one real figure will do more work than a
qualifier.

None of this licenses padding a step to hit a quota of numbers or dialogue.
The chain only needs as many of these devices as the actual mechanism calls
for, and a step that's already clear in plain prose doesn't need a skit
built for it.

## Robert Heaton, "How does HTTPS actually work?"

Source: https://robertheaton.com/2014/03/27/how-does-https-actually-work/

> "HTTPS is simply your standard HTTP protocol slathered with a generous
> layer of delicious SSL/TLS encryption goodness. Unless something goes
> horribly wrong (and it can), it prevents people like the infamous Eve from
> viewing or modifying the requests that make up your browsing experience;
> it's what keeps your passwords, communications and credit card details
> safe on the wire between your computer and the servers you want to send
> this data to."

The joke in the first sentence ("delicious... goodness") costs nothing and
buys the plain, high-stakes claim that follows room to land without sounding
like a warning label. The parenthetical "(and it can)" is where the person
is visible: it's a specific, undefended admission dropped into a sentence
that could have stayed comfortably general.

> "If this were the whole story then SSL would be a joke; identity
> verification would essentially be the client asking the server "are you
> Google?", the server replying "er, yeah totally, here's a piece of paper
> with 'I am Google' written on it" and the client saying "OK great, here's
> all my data.""

This is a mechanism explained by staging it as a specific, badly-run
conversation rather than describing it. The exact words he puts in the
server's mouth ("er, yeah totally") are doing the explaining — they show
exactly what's missing from the naive version of the protocol, which is why
the sentence after this one, about the real fix, has something concrete to
correct.

> "Can a coffee shop monitor my HTTPS traffic over their network? Nope. The
> magic of public-key cryptography means that an attacker can watch every
> single byte of data exchanged between your client and the server and still
> have no idea what you are saying to each other beyond roughly how much
> data you are exchanging."

He asks the question a reader with real doubt would actually ask, in exactly
those words, and answers it in one word before spending a sentence earning
that answer. The directness of "Nope" is only possible because the piece has
already built the mechanism that makes it true.

## Ken Shirriff, "A bug fix in the 8086 microprocessor, revealed in the die's silicon"

Source: http://www.righto.com/2022/11/a-bug-fix-in-8086-microprocessor.html

> "The 8086 microprocessor was a groundbreaking processor introduced by
> Intel in 1978. It led to the x86 architecture that still dominates desktop
> and server computing. While reverse-engineering the 8086 from die photos,
> a particular circuit caught my eye because its physical layout on the die
> didn't match the surrounding circuitry."

The opening states the stakes of the chip in two flat sentences and then
pivots on an observed anomaly, not a claim. "Didn't match the surrounding
circuitry" is a specific, checkable thing he noticed, which is why the whole
piece can be a chain of causes leading back to it instead of an assertion
the reader has to take on faith.

> "A complication is that the 8086 uses "segmented memory", where memory is
> divided into chunks (segments) with different purposes. On the 8086, there
> are four segments: the Code Segment, Data Segment, Stack Segment, and
> Extra Segment. Each segment has an associated segment register that holds
> the starting memory address for that segment."

Each sentence here adds exactly one fact and stops. He doesn't reach ahead to
say why segments matter to the bug until the reader has all three
sentences in hand — the discipline of finishing one idea before touching the
next is visible in how little each sentence is asked to carry.

> "A problem arises if the processor receives an interrupt after the Stack
> Segment register has been changed, but before the Stack Pointer register
> has been changed. The processor will store information on the stack using
> the old stack pointer address but in the new segment. Thus, the
> information is stored into essentially a random location in memory, which
> is bad."

This is the cause, stated only once every piece it depends on has already
been named separately in the two paragraphs before it. "Which is bad" is
almost a joke, and it's earned rather than empty because the sentence just
before it has already shown exactly why: a location that's random is
somewhere real data can get overwritten by accident.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "In the world of modern portable devices, it may be hard to believe that
> merely a few decades ago the most convenient way to keep track of time was
> a mechanical watch. Unlike their quartz and smart siblings, mechanical
> watches can run without using any batteries or other electronic
> components."

The second sentence states the one fact that makes the whole subject worth
forty more paragraphs: no batteries, no electronics. Naming the modern
devices ("quartz and smart siblings") the reader already understands is what
lets the watch's total absence of anything electronic register as strange
rather than as trivia.

> "Let's consider how much of a speed increase we have to do here. The
> barrel can rotate close to 7 times on a single wind, but we want the
> second hand to complete around 2400 revolutions in the same time. We need
> the ratio of teeth, or the ratio of radii, to be around 343:1."

The claim "we need a lot of speed increase" would have been true and said
nothing. Naming the actual figures — 7 rotations, 2400 revolutions, a
343:1 ratio — is what turns "the gears do a lot of work" into a specific,
checkable fact the next paragraph can then show is physically absurd to
build directly.

> "The escape wheel wants to rotate as indicated by the red arrow. The
> pallet fork prevents that motion, but as we pivot that pallet fork back
> and forth, we let the escape wheel briefly escape from that jail only to
> be stopped again."

Giving the wheel a "want" is doing real work, not decoration: it lets him
describe a mechanical constraint (the fork blocking rotation) in a sentence
short enough to read at the pace the actual back-and-forth happens. The word
"jail" is the one moment of personality in an otherwise literal sentence,
and it survives because the mechanics underneath it are exactly right.
