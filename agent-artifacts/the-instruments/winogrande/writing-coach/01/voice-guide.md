# Voice guide: the-instruments/winogrande

## How this piece should sound

This is a lesson for a reader who is smart and widely read but has never taken
apart a benchmark. Hold the register plain and precise, the way Dan Luu writes
about latency: say what a WinoGrande accuracy figure is a measurement of before
you report one, and when a term like an annotation artifact or adversarial
filtering has to enter, define it in the sentence where it first appears, the
way Julia Evans introduces catastrophic cancellation only at the point her
example forces the word. Explain each step of the construction in ordinary
words. The reader should be able to follow how the number is made without
already knowing the field.

The construction becomes real when it runs on a case with numbers, as the
odometer does for Evans. Where the material gives you figures the reader can
hold, the human-performance figure, a machine baseline, the size of the set
before and after filtering, work through them rather than describe them from
above. Luu rounds his measurements to avoid claiming a precision his method
cannot support, and states exactly what the timer captured; a WinoGrande figure
can be reported the same way, as a number attached to a specific procedure and
a specific filtered set, not a fixed property of the task.

Be skeptical of a tidy score without turning sour. Shalizi asks plainly why a
discredited summary number keeps getting used, and pins the doubt to concrete
evidence rather than to a raised voice. When you press what a high WinoGrande
score does and does not license a reader to conclude, pair the doubt with the
evidence the way Luu answers a bad argument with the flight comparison, so the
skepticism is earned and not merely a mood. Before the piece shows where the
score misled people, it can grant what the benchmark did well, the scale and the
filtering that closed shortcuts already known, the way Evans credits floating
point before cataloguing its failures. That is what keeps the later criticism
fair.

For the misled case, the plainest shape is the one Shalizi uses for
falsification: what the number was taken to show, the harder test it met, and
what that test found. Report it in that order and let the cost of being wrong
sit in figures. The reader should finish able to look at a WinoGrande number on
a model card and say what it was built to measure, what the filtering bought,
and where the gap between the score and the reasoning it was meant to require
can still open up.

## Dan Luu, "Keyboard latency"

Source: https://danluu.com/keyboard-latency/

> "I can only find one person who's publicly benchmarked keyboard latency and they only tested two keyboards. In general, my belief is that if someone makes performance claims without benchmarks, the claims probably aren't true, just like how code that isn't tested (or otherwise verified) should be assumed broken."

Luu refuses to accept a performance claim without the measurement under it, and
he states the rule flatly, with a comparison the reader already understands.
The plain first-person "my belief is" is where he is visible: he is telling you
his standard for believing a number, not performing certainty.

> "The latency measurements are the time from when the key starts moving to the time when the USB packet associated with the key makes it out onto the USB bus. Numbers are rounded to the nearest 5 ms in order to avoid giving a false sense of precision."

He says exactly what the number is a measurement of, start point and end point,
before he lets any figure stand. Then he caps the precision so the number does
not claim more than the method earned. The care not to oversell the measurement
is the writer showing his own honesty about what he can and cannot see.

> "This doesn't actually make sense because there are independent quantities. This line of argument is like saying that you wouldn't notice a flight being delayed by an hour because the duration of the flight is six hours."

Luu takes apart a common bad argument with an everyday comparison, keeping the
two quantities separate so the reader can see why the argument fails. No jargon
carries the point; the plain analogy does. This is his habit of answering a
weak claim with a concrete case rather than an assertion.

## Julia Evans, "Examples of floating point problems"

Source: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/

> "To make this concrete, let's say that we're adding numbers to the odometer 1cm at a time. What does it look like after 10,000 kilometers?"

Evans turns an abstract hazard into a specific case with real quantities, and
poses the question the reader now wants answered. The move from a general
warning to "let's say" and a number is where she is visible: she teaches by
building the smallest example that will actually show the problem.

> "There are still some small inaccuracies here – we're off about 17 centimeters. Whether this matters or not depends on the context: being slightly off could very well be disastrous if we were doing a precision space maneuver or something, but it's probably fine for an odometer."

She reports the leftover error as a figure, then says plainly that whether it
matters depends on what the number is for. The judgment is visible in her
willingness to say "probably fine" and, in the same breath, to name the use
where the same error would not be fine.

> "I don't want you to read this post and conclude that floating point is bad. It's an amazing tool for doing numerical calculations. So many smart people have done so much work to make numerical calculations on computers efficient and accurate!"

Before she catalogues the failures, Evans credits the tool and the people who
built it, so the criticism that follows reads as fair rather than as a takedown.
The direct "I don't want you to read this post and conclude" is the writer
telling you how to hold what she is about to show you.

## Cosma Shalizi, "g, a Statistical Myth"

Source: https://www.bactra.org/weblog/523.html

> "Since Spearman's theory of g is about as refuted as a statistical hypothesis gets, why does g still feature in arguments about social policy and education? Isn't this as though some parties in the global warming debate had climate models involving phlogiston and caloric?"

Shalizi asks, directly, why a summary number that failed its own test keeps
getting used, and he anchors the skepticism in a comparison from another field
the reader can weigh. The wry, unhedged question is where he is on the page: he
states his doubt as a question the argument then has to answer.

> "The way we can unambiguously tell that it had falsifiable empirical content is that it was, in fact, falsified. Looking at larger and more diverse data sets, it became clear that the partial correlations among scores on mental ability tests were not zero, or even close enough to attribute the difference to chance. Put to reasonably severe tests, it failed."

He shows how a claim about a number met more data and broke, in plain sequence:
what the claim predicted, the test, the result. The short closing sentence lands
the outcome without decoration. The precision about what the evidence showed is
the writer refusing to let a result sound softer than it was.

> "in turning factor analysis into a better tool for describing correlations, Thurstone et al. made it into a next-to-useless tool for explaining correlations, and most users of the tool then and since have never really grasped the problem."

Shalizi draws a clean line between a method that describes a pattern well and the
same method used to explain where the pattern comes from, and he names who
carried the confusion forward. The exactness about what the tool can and cannot
do is where he is visible: he is careful in the same place his opponents are
loose.
