# Voice guide: the-instruments/livecodebench (01)

## How this piece should sound

This is a lesson that takes a LiveCodeBench score apart: who makes the number,
from what problems, by what procedure, and where it stops meaning what a reader
assumes. The reader is sharp and reads widely but has never opened a codebase or
run a benchmark. Write for that reader in plain claims and concrete stakes. The
figures do the arguing; a grand word waits until the evidence has earned it.

Lead with worked cases, not descriptions of procedure. Dan Luu explains
open-loop measurement by inventing one service that gets one request a second and
answers in half a second, then asking what happens when a single request stalls.
When you walk the reader through pass@1 over held-out tests, or through a problem
tagged with a release date being scored against a model's training cutoff, do it
on one concrete problem moving through the steps, the way Luu does, rather than
narrating the mechanism in the abstract. Julia Evans does the same for a
mechanism that sounds forbidding: she shows the odometer stuck at 262144.0
because 262144.0 + 0.01 = 262144.0, an actual number the reader can hold. Where
a step of how the score is built could be stated as a rule or shown happening to
one number, show it happening.

When the score changes with the conditions it was measured under, put the two
numbers next to each other with their conditions attached. Luu's single latency
is 16ms measured at the server and 240ms measured at the client, and once both
numbers are on the page the reader sees that the gap lives in the measurement,
not the system. A LiveCodeBench figure carries its date window and its version
the same way. Let the reader see a figure and its conditions together, so the
thing that moved the number is visible rather than asserted.

Say plainly what the number supports and what it does not, and let "it depends"
be an honest answer where it is the true one. Evans, having fixed her odometer,
does not declare victory: she notes it is still off by about 17 centimeters, then
says that being off could be disastrous for a precision space maneuver and fine
for an odometer. A LiveCodeBench score can be trustworthy for one comparison and
worthless for another. Hold any verdict to what the evidence shows, and where a
figure is good enough for one use and not another, say which use.

When the piece reaches why two LiveCodeBench numbers resist comparison, reason it
out on the page rather than asserting it. Bergstrom and West spend several plain
sentences on why averaged restaurant ratings compare places within a city and
not across cities, stating what the ratings do tell you before what they do not.
The mechanics of a moving cutoff and a versioned problem set are the writer's to
establish, but establish them in that register: steps a reader can follow, not a
conclusion handed down. And a benchmark invites a long list of caveats; Bergstrom
and West name the single biggest issue and give it the room instead. Find the one
limitation that matters most for reading a LiveCodeBench figure and spend the
words there.

Use LiveCodeBench's own vocabulary and keep it exact. Luu writes "99%-ile" and
"netty"; Evans writes "32-bit floats" and "significand"; neither softens the term
to seem friendlier, and both stay readable because the example carries the word.
Pass@1, training cutoff, held-out tests, release date, scenario, contamination:
use them, and let the worked case make each one land. A plain explainer can still
have a person visibly behind it. Bergstrom and West live in Seattle and tell you
to order the salmon; the aside is dry, it costs one clause, and it is anchored in
the piece's own subject. A line like that is allowed here when the material
offers one, and never worth reaching for when it does not.

## Dan Luu, "Some latency measurement pitfalls"

Source: https://danluu.com/latency-pitfalls/

> "For example, if we look at 99%-ile latency, we can see that it's ~16ms when measured at the server and ~240ms when measured at the client, a factor of 15 difference. Alternately, if we look at a fixed latency, like 240ms, and look up the percentile, we see that's 99%-ile latency on the client, but well above 99.9%-ile latency on the server."

Luu takes one quantity and reports it two ways, and the two numbers are 15 times
apart. He does not tell the reader the measurement is tricky; he shows the same
latency being 16ms or 240ms depending on where the stopwatch sits, and lets the
size of the gap make the point. This is a writer who trusts a concrete pair of
numbers to do work that an adjective would only claim.

> "Below, the reported latency metrics for a single instance of cache-1 are the blue points and the measured (sampled) latency the client observed is the black line. Reported p99 latency is 0.37ms, but actual p99 latency is ~580ms, an over three order of magnitude difference."

Here the reported figure and the real one differ by more than a thousand times,
and Luu states both flatly and moves on. The plainness is the craft: he names the
reported number, names the true number, gives the ratio, and lets a reader feel
the distance without being told it is alarming. Luu is visible in the refusal to
editorialize over a number that could carry the paragraph on its own.

> "For a toy example of the problem, let's say that we have a service that, in production, receives exactly 1 request every second and that the service has a normal response time of 1/2 second. Under normal behavior, if we issue requests at 1 per second, we'll observe that the mean, median, and all percentile request times are 1/2 second."

To explain a measurement artifact, Luu builds the smallest possible case with
real rates and times rather than describing the artifact in general terms. One
request a second, a half-second response, and the reader has a concrete machine
to reason about before any complication arrives. His instinct is to make the
abstract thing walkable step by step.

## Julia Evans, "Examples of floating point problems"

Source: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/

> "The problem in this case is that, for 32-bit floats, 262144.0 + 0.01 = 262144.0. So it's not just that the number is inaccurate, it'll actually never increase at all! If we travelled another 10,000 kilometers, the odometer would still be stuck at 262144 meters (aka 262.144km)."

Evans explains a mechanism that intimidates people by showing it happen to one
number: add a centimeter to 262144.0 and you get 262144.0 back. The reader does
not need to hold the theory of floating point to see the odometer freeze, because
Evans has grounded the whole idea in an arithmetic fact they can check. She is the
kind of teacher who reaches for the smallest true example instead of the fullest
explanation.

> "There are still some small inaccuracies here – we're off about 17 centimeters. Whether this matters or not depends on the context: being slightly off could very well be disastrous if we were doing a precision space maneuver or something, but it's probably fine for an odometer."

Having offered a fix, Evans immediately says where it still fails and by how much,
then refuses to give a single verdict on whether that failure matters. Seventeen
centimeters is disastrous for one use and fine for another, and she says so
plainly rather than pretending the number is simply good or simply bad. The
honesty about what a figure can and cannot carry is where Evans is most herself.

## Carl Bergstrom and Jevin West, "Calling Bullshit case study: America's best barbecue?"

Source: https://callingbullshit.org/case_studies/case_study_barbecue.html

> "What went wrong? So many things. It's hard to even know where to start. But let's focus on the single biggest issue: the data collected are not appropriate to answer the question at hand."

Faced with a figure that is wrong in many ways at once, Bergstrom and West pick
one and set the rest aside. The move is the discipline: they admit the objections
could fill a page, then commit to the single failure that actually decides the
case. A reader learns more from one limitation explained fully than from ten
listed, and these writers know it.

> "So what these data tell us is that people in Seattle rate Seattle barbecue higher than people in Fort Worth rate Fort Worth barbecue places. We don't know how people in Seattle would rate Fort Worth barbecue, or how people in Fort Worth would rate Seattle barbecue."

This is a comparability problem argued in plain sentences a reader can follow one
at a time. They state exactly what the ratings do establish, then exactly what
they leave unknown, and the invalid comparison falls out of the two statements
rather than being asserted. Bergstrom and West are visible in the patience of it,
laying the reasoning end to end instead of announcing the conclusion.
