# Voice guide: how the model respects word order

## How this piece should sound

This lesson has one job that its exemplars all share: take a mechanism that
sounds like it shouldn't work, and walk the reader down to the part that
actually does the work. The reader already believes the behavior (a
transformer respects word order) and doesn't yet believe the mechanism
(the operation underneath is blind to order). That gap is the whole piece,
and it should be handled the way Bartosz Ciechanowski handles the watch hand
that spins uselessly on the bare barrel: state plainly what the naive setup
would produce, show that it doesn't produce the real behavior, and only then
bring in the part that fixes it. Don't announce the twist. Let the reader
watch it fail to work the naive way first.

Once a mechanism needs a real number to become concrete, use one, the way
Ciechanowski reaches for "40 hours on a single wind" and "2400 rotations"
the moment the gear ratio itself would otherwise stay abstract. This piece
has an obvious candidate for that treatment: a sentence and its scrambled
twin, run through the actual operation that reads them, with the reader able
to see for themselves that the two look identical to it. One concrete pass
through a genuinely small example is worth more than several sentences
gesturing at what "the model" does with order in general.

Define positional encoding, and whatever else the reader needs, in the
sentence that first needs it, the way the lesson template requires — but
don't let the definition sit there as a dictionary entry. Evans' habit of
naming the hidden layer and then immediately admitting what she still finds
strange about it ("I'm not sure what that means... but it's cool") is the
right model for the edge of this piece: state what positional encoding does,
plainly, and be equally plain about how much of why the field settled on
this particular way of supplying order, as opposed to any other, is
convention rather than proven necessity. The series brief asks for exactly
this line between settled engineering and open question, and Dan Luu's way
of holding it is to attach the uncertainty to one specific claim: "one
plausible guess is."

Keep the actors doing things. Ciechanowski writes his gear train verb after
verb — the barrel drives the wheel, the wheel drives the pinion — and the
self-attention operation in this piece can get the same treatment: it does
something to the tokens, on every pass, and the piece can say what, in
order, with a real verb carrying each step. When the piece reaches the place
where research hasn't fully settled why the field converged on the current
approach to supplying order, say so in one sentence and move on, the way Luu
closes his piece: admitting plainly that he doesn't know if latency will
keep improving, and naming exactly what's uncertain about it.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "We've managed to make some parts rotate and one could naively think that
> we could just attach a watch hand to the barrel to make it track time.
> Unfortunately, that won't really work"

This is the move the piece needs most: state the assumption a reader would
reasonably make, then flatly deny it, before explaining why. The sentence
reports the failure in the same plain voice as everything around it, with no
windup beforehand.

> "If we wanted our watch to run continuously for around 40 hours on a
> single wind, we'd need the minute hand to complete 40 rotations in that
> time. Moreover, the second hand should cover around 40 × 60 = 2400
> complete rotations in that time. We need to find a way to convert a small
> number of revolutions of the barrel into a large number of revolutions of
> the hands."

The abstract requirement — gear the barrel up to the hands — arrives only
after the concrete one: a real duration, a real rotation count, a piece of
arithmetic the reader can check by hand. The numbers come first, and the
abstraction follows from them.

> "Personally, I think this entire mechanism known as the keyless works is
> a real mechanical marvel. The intricate interactions are so well balanced
> and each part serves many different roles."

The judgment is there, but it's marked as his own opinion ("Personally, I
think") and placed after forty paragraphs of mechanism. The writer earns the
word "marvel" by having already shown the interlocking parts that make it
one.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When I finally learned how to troubleshoot DNS problems, my reaction was
> 'what, that was it???? that's not that hard!'. I felt a little bit
> cheated!"

The person is visible in the exact shape of her own surprise: four question
marks, an exclamation point, the specific memory of feeling cheated about
how easy the answer turned out to be.

> "Here I've requested a nonexistent domain, and I got the extended error
> EDE: 12 (NSEC Missing): (Invalid denial of existence of xjwudh.com/a).
> I'm not sure what that means (it's some DNSSEC Thing), but it's cool to
> see an extra debug message like that."

She ran the command, got output she couldn't fully explain, and says exactly
that. The admission is attached to one specific term ("that"), which keeps
the sentence honest without turning the whole paragraph vague.

> "Here you can see we got a normal NOERROR response for google.com (which
> is in 8.8.8.8's cache) but a SERVFAIL for homestarrunner.com (which
> isn't)."

A real pair of outputs, side by side, does the explaining that a paragraph
of description would otherwise need to do. The reader compares the two
results and reaches the conclusion directly.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "Although we don't have enough data to really tell why the blackberry q10
> is unusually quick for a non-Apple device, one plausible guess is that
> it's helped by having actual buttons, which are easier to implement with
> low latency than a touchscreen."

The uncertainty is scoped to one claim and named plainly as a guess. He says
what he doesn't know, then gives his best explanation anyway, labeled for
exactly what it is.

> "We get a 90 ms improvement from going from 24 Hz to 165 Hz. At 24 Hz each
> frame takes 41.67 ms and at 165 Hz each frame takes 6.061 ms... which is a
> difference of about 18ms. But the difference is actually 90 ms, implying
> we have latency equivalent to (90 - 18) / (41.67 - 6.061) = 2 buffered
> frames."

The arithmetic is shown in full: the expected number, the measured number,
and the gap between them. That gap is the proof that hidden buffering
exists, carried entirely by the numbers themselves.

> "I don't know that we'll see the same kind improvement with respect to
> latency, but one can hope. There are individual developers improving the
> experience for people who use certain, very carefully coded, applications,
> but it's not clear what force could cause a significant improvement in
> the default experience most users see."

A plain "I don't know" is followed immediately by the specific thing that
is known (individual developers, certain applications) and the specific
thing that remains open (what would move the default experience). The
uncertainty has real edges to it, drawn from what he actually measured.
