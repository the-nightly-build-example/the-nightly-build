# Voice guide: the-mechanics/clock-faces

## How this piece should sound

This lesson takes one odd thing an image generator does, and follows it down to
the parts that produce it. The odd thing carries the reader in, so the writing
does not have to sell it. Ask for a clock at 3:15 and get 10:10 back: that is
already strange enough to want an explanation. The register that fits is plain
and concrete, the register Simon Willison uses when he calls a language model "a
file" that is "just numbers" instead of something mysterious. When the piece
first says what a diffusion generator is doing as it "draws a clock," the flat,
demystifying description will do more for the reader than an impressive one.

The spine is the one Bartosz Ciechanowski uses on the watch: name the naive
expectation, show concretely why it fails, then name the real part responsible,
and go down a level. He does it with "one could naively think that we could just
attach a watch hand to the barrel," and then with the date wheel. The clock
piece has the same shape available to it. The reader expects the words "3:15" to
reach the hands somehow; the useful move is to say plainly which step would have
to exist for that to happen, and that it does not. Each step down should name a
real part of the system, the way the commission lays out the chain, until
nothing below the last step would change the answer.

Where an unfamiliar step can be anchored to something the reader already holds,
anchor it. Willison explains next-word prediction by pointing at the iPhone
keyboard suggesting "breakfast" after "I enjoy eating," and the reader is done
needing the concept explained. If a comparison genuinely fits the idea that a
generator renders the most likely appearance, one the reader already carries
will land it faster than a definition. Reach for the comparison only where it
holds; a forced one costs more than it saves.

Prefer the specific figure to the general word. Ciechanowski writes "40 hours"
and "40 × 60 = 2400 complete rotations," not "a lot"; Willison says "4.2
gigabyte," not "large." Where the research supports a number for how dominant the
near-10:10 arrangement is in clock and watch imagery, or for how a model reads an
arbitrary face, the number is worth more than "usually" or "often." Where it does
not, say what is actually known and stop there.

Mark the edge of what is known, plainly, and do not step past it. Julia Evans, in
the middle of a working example, writes "I'm not sure what that means (it's some
DNSSEC Thing)" rather than bluff, and Willison ends on "We still don't know what
LLMs can and can't do." This lesson has a settled part and an open part, and the
commission asks for the line between them to be visible: that diffusion models
reproduce dataset statistics and that clock imagery skews to one arrangement are
settled; how much targeted data or tooling closes the gap, and whether systems
that plan or call tools do better, are open. Name which is which in the piece's
own terms. The lesson body does this in the third person and addresses no reader,
so Evans's plainness carries but her "I" does not.

Commit to the concrete judgment when the evidence is in. Evans does not soften
her verdict on a tool; she says its output "has the feeling of a script someone
wrote in an adhoc way that grew organically over time." The angle here turns on a
distinction the piece can state outright: a real mechanism, a training prior plus
a missing step, against the hand-wave that "the AI is bad at clocks." Where the
reader can be equipped to tell one from the other, say it directly rather than
leave it implied.

## Simon Willison, "Catching up on the weird world of LLMs"

Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/

> "A more practical answer is that it's a file. This right here is a large
> language model, called Vicuna 7B. It's a 4.2 gigabyte file on my computer. If
> you open the file, it's just numbers. These things are giant binary blobs of
> numbers. Anything you do with them involves vast amounts of matrix
> multiplication, that's it."

Willison takes a thing people treat as uncanny and states what it physically is:
a file, a size in gigabytes, numbers. The short flat sentences do the
demystifying, and the exact figure ("4.2 gigabyte") keeps it from floating into
abstraction. He is visible in the refusal to make it sound more than it is.

> "How do they do all this? It really is as simple as guessing the next word in
> a sentence. If you've used an iPhone keyboard and type "I enjoy eating" it
> suggests words like "breakfast." That's what a language model is doing."

He explains a mechanism by pointing at a thing the reader has already used, so no
definition is needed. The comparison is exact, not decorative: the keyboard is
literally doing the smaller version of the same thing, which is why it teaches.
The plainness ("that's what a language model is doing") is Willison landing the
point without dressing it up.

> "We still don't know what LLMs can and can't do. There are new discoveries all
> the time, and new models are coming out every week."

This is how he marks an open frontier: he states the not-knowing as a fact, in
the same plain voice as everything he does know. There is no hedging and no
alarm. He is visible in treating "we don't know yet" as ordinary reporting rather
than a confession or a warning.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single
> wind, we'd need the minute hand to complete 40 rotations in that time.
> Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations
> in that time. We need to find a way to convert a small number of revolutions of
> the barrel into a large number of revolutions of the hands. This is where gears
> come in."

He sets the concrete goal in real numbers, states what stands in the way, and
only then names the next real part. The reader arrives at "gears" already
knowing what job the gears have to do, so the part is introduced by its purpose
rather than its name. Ciechanowski is visible in the patience: he earns each
component before he brings it on.

> "You may wonder why we need this complicated mechanism in the first place. One
> could naively assume that we could directly tie the rotation of the date ring
> to the rotation of the hour wheel, similarly to how we rotated the hour wheel
> in sync with minutes, albeit at slower pace. Unfortunately, this would cause
> the current date to continuously rotate under the little window in the dial,
> making it hard to read."

He voices the reader's own reasonable guess, then shows the specific thing that
goes wrong with it. The failure is concrete and visual (the date would smear
under the window), not a general "that wouldn't work." This is the move a
mechanism explainer lives on, and Ciechanowski is visible in taking the naive
guess seriously enough to answer it in full.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "In general `dig`'s output has the feeling of a script someone wrote in an
> adhoc way that grew organically over time and not something that was
> intentionally designed."

Evans commits to a specific characterization instead of hedging. The judgment is
concrete enough to picture ("grew organically over time") and it is hers,
plainly stated, not attributed to some vague consensus. She is visible in the
willingness to say what a thing is actually like.

> "I'm not sure what that means (it's some DNSSEC Thing), but it's cool to see an
> extra debug message like that."

In the middle of walking through a real example, she names the exact spot where
her own understanding runs out, and keeps going. The honesty is casual, not
apologetic, and it tells the reader precisely how far the explanation reaches.
Evans is visible in refusing to paper over the gap with confident-sounding
filler.
