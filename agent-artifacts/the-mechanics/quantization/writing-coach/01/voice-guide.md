# Voice guide: the-mechanics/quantization (01)

## How this piece should sound

This lesson starts from something the reader has run into: the cheaper, faster, or on-device version of a model answers noticeably worse than the full one, though it goes by the same name. The word for what was done to it is quantization, and the lesson works back to what that does to the model's weights and why it sometimes barely shows and sometimes shows a lot. The reader is quick and widely read and has never opened a model's weights. Assume they can follow a number and a small worked case, and assume nothing else: not what a weight is, not how many bits hold one, not what it means to round a number to a coarser set of allowed values. Hold the register plain and serious, the way Matt Yglesias explains something he understands cold. State the claim flat, make the stakes concrete, and when a choice comes down to sounding good or being understood, be understood.

The core difficulty is teaching a mechanism made of numbers with no code and no diagram to point at. Fabien Sanglard's window-and-offset passage is the one to study for it. He sets the standard formula aside and hands the reader two ordinary words to picture instead, and the substitution does the teaching the notation could not. Where this lesson needs the reader to see what storing a weight in fewer bits actually does, that it lands on one value out of a smaller allowed set, a plain everyday picture the reader already holds may carry it further than the arithmetic would. Sanglard also keeps naming each part the same way once he has named it, and this lesson has many parts that each need one fixed name: the weights, the bits, the allowed values, the rounding, the large-magnitude values.

Much of the lesson is measured results: how much the answers change as the bits drop from sixteen to eight to four, and how much a careful scheme buys back. Dan Luu's latency piece shows how to carry numbers like these without hype. He begins from a feeling the reader shares, declines to trust it, and measures, and when he lands a verdict the multipliers he has already laid out are what earn it. The figures can reach the judgment on their own here too. And when the tidy version of the story does not survive the evidence, there is Luu's handling of "complexity is bad" to borrow from: say the neat version plainly, then show the exact place it breaks.

The lesson lives on a contrast the reader will want settled, that the same rounding is usually harmless and occasionally severe. Julia Evans holds that kind of contrast without raising her voice. She reports a leftover error as a real figure, seventeen centimeters, and then decides whether it matters by naming where it would be a disaster and where it would be fine, rather than grading it. Her "whether this matters or not depends on the context" is close to the temperature this lesson wants wherever it explains why the same loss of precision costs almost nothing in one place and a great deal in another. And where the lesson marks what the field has not settled, Evans's plain "I can kind of see" is one honest way to say the builders themselves do not fully know, without softening it into fog.

## Julia Evans, "Examples of floating point problems"

Source: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/

> "I don't want you to read this post and conclude that floating point is bad. It's an amazing tool for doing numerical calculations. So many smart people have done so much work to make numerical calculations on computers efficient and accurate!"

Before she shows a single failure she heads off the wrong lesson the failures might teach, and she does it with plain enthusiasm rather than a hedge. The person is visible in the direct "I don't want you to" and in deciding, out loud, what the reader should not walk away believing.

> "There are still some small inaccuracies here – we're off about 17 centimeters. Whether this matters or not depends on the context: being slightly off could very well be disastrous if we were doing a precision space maneuver or something, but it's probably fine for an odometer."

She gives the leftover error as a real quantity, seventeen centimeters, and then rules on whether it matters by naming two concrete situations instead of assigning it a grade. The "or something" and the swing from disastrous to probably fine are a person weighing it in front of you.

> "This is a very basic example but I can kind of see how this would create all kinds of problems if I was doing page layout with floating point numbers, or doing CAD drawings."

She admits the example is small and then reaches to where the same bug would actually bite, which keeps a toy case honest about what it does and does not prove. "I can kind of see" is her own uncertainty left in rather than smoothed over.

## Fabien Sanglard, "Floating Point Visually Explained"

Source: https://fabiensanglard.net/floating_point_visually_explained/

> "This is usually where I flip the table. Maybe I am allergic to mathematic notation but something just doesn't click when I read it."

He names that the standard explanation fails a real reader, and puts the failure on himself rather than on the reader who did not follow it. The first-person "I am allergic to mathematic notation" is him owning the difficulty instead of asserting it in general.

> "Although correct, this way of explaining floating point will leaves some of us completely clueless. Fortunately, there is a different way to explain it. Instead of Exponent, think of a Window between two consecutive power of two integers. Instead of a Mantissa, think of an Offset within that window."

This is the move: he swaps two jargon words for two everyday spatial words and tells the reader exactly what to picture in their place, and the swap itself carries the lesson. What is on the page is Sanglard handing over his own mental image rather than describing one.

> "The window must start at 4 and span to next power of two, 8. The offset is about half way down the window."

Having built the picture, he runs a real number through it in plain words, so the reader watches the metaphor do actual work rather than admire it. "About half way down the window" is him reading the value off his own picture the way he wants the reader to.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower than the computers I used as a kid. As a rule, I don't trust this kind of feeling because human perception has been shown to be unreliable in empirical studies, so I carried around a high-speed camera and measured the response latency of devices I've run into in the past few months."

He opens from an ordinary feeling the reader has had, then refuses to trust it and goes and measures, so the piece earns its numbers before it uses them. "As a rule, I don't trust this kind of feeling" is a stated habit of mind, not a pose.

> "Unfortunately, it's a lot harder to remove complexity than to give a talk saying that we should remove complexity. A lot of the complexity buys us something, either directly or indirectly."

He takes the tidy explanation everyone reaches for and declines it, then shows that the thing being blamed is paying for something. The dry contrast between removing complexity and giving a talk about removing it is his skepticism of easy answers, doing the work in one sentence.

> "It's a bit absurd that a modern gaming machine running at 4,000x the speed of an apple 2, with a CPU that has 500,000x as many transistors (with a GPU that has 2,000,000x as many transistors) can maybe manage the same latency as an apple 2 in very carefully coded applications if we have a monitor with nearly 3x the refresh rate."

The verdict is three plain words, "a bit absurd," and every bit of its force comes from the multipliers he lines up ahead of it. He lets the numbers reach the judgment and only puts a label on the result.
