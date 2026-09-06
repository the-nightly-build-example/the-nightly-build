# Voice guide: the-instruments/calibration-error (01)

## How this piece should sound

This lesson has one job: show how a reliability number is actually computed,
and then show where the computation stops meaning what people take it to
mean. Both halves need the same treatment Spiegelhalter and Pearson give the
micromort: state which number was used and what was assumed, one step at a
time, so a reader could find the exact place to disagree. Whatever bucketing
or averaging step turns raw predictions into the published figure, walk it
the way they walk 135,000 hospital beds down to 75 micromorts a day, in full
sentences, no notation the reader has to first learn to read.

Evans' eight flight numbers are the model for the worked example: small
enough to write out completely, given a job before any statistic touches
them, so the reader knows what the numbers are for before being asked to
trust anything built from them. A calculation run on a handful of made-up
predictions the reader can hold in their head will teach the mechanism
better than a calculation described over a real model's thousands.

Once the number exists, hold it to a specific account of what it can and
cannot certify, the way Fung closes on the mismatch between what passkey
success rate measures and what a reader assumes it measures, or the way
Spiegelhalter and Pearson name the two things an average risk does not
represent before saying what it is still good for. The account should name
the particular thing the reliability number is silent on, not gesture at
uncertainty in general. Where a comparison would make the number's size
legible, Fung's door lock and Spiegelhalter's motorbike miles both convert an
abstract rate into an object with an obvious job; the calibration figure
wants a comparison of that kind rather than a restatement in different units.

The series wants a real case where the number misled someone and what that
cost. Evans' habit of listing the exact reasons her own computed figure does
not deserve confidence, the fractional person, the sample size, the unknown
distribution, is the register for that case: specific, checkable reasons the
number failed, not a general note that summary statistics can be misleading.

## Kaiser Fung, "Metrics for Evaluating Passkeys"

Source: https://www.junkcharts.com/metrics-for-evaluating-passkeys/

> "In my experience, most people don't log out after they log in. They think
> it's more convenient. Developers also think it's more convenient, and thus
> many application interfaces actively hide the log-out buttons. These users
> will only attempt log-ins if they unexpectedly got kicked off. They are
> unlikely to remember any password."

Fung doesn't just call the reported failure rate implausible. He narrates the
exact mechanism that would produce it, one sentence handing off to the next,
until the number's origin is visible rather than asserted. The reasoning is
worked out in front of the reader, not delivered as a conclusion.

> "If the door lock salesperson boasts that their lock lets in 98% of entry
> attempts, do you feel convenienced or insecure? I feel insecure, because I
> believe all services face a healthy amount of malicious activities so I
> expect a lower success rate."

He turns an abstract success rate into a physical object with an obvious
purpose, then answers his own question in the first person instead of
leaving it rhetorical. His judgment sits in the plain "I feel insecure," not
in the analogy that set it up.

> "The point is that it's important to define the right metrics. Passwords
> and passkeys are security measures, and the highlighted metric concerns
> convenience, which may be negatively correlated with security."

The piece closes on a distinction between what the reported number measures
and what a reader assumes it measures. He states the mismatch as a fact about
the metric's own definition, not as suspicion of the company that published
it.

## David Spiegelhalter and Mike Pearson, "Understanding uncertainty: Small but lethal"

Source: https://plus.maths.org/content/os/issue55/features/risk/index

> "For example, the risk of death from a general anaesthetic (not the
> accompanying operation), is quoted as 1 in 100,000, meaning that in every
> 100,000 operations we would expect one death. This corresponds to 10
> micromorts per operation."

One fact is stated three times at three levels of concreteness: a quoted
risk, a count out of a round number, a figure in the new unit. By the end of
the sentence the ratio and the unit are visibly the same thing, with no step
skipped between them.

> "Each day in England around 135,000 people occupy a hospital bed and
> inevitably some of these die of their illness. But not all these deaths are
> unavoidable: in the year up to June 2009, 3,735 deaths due to lapses in
> safety were reported to the National Patient Safety Agency, and the true
> number is suspected to be substantially higher. This is about 10 a day,
> which means an average risk of around 1 in 14,000, assuming few of these
> avoidable deaths happened to out-patients. So staying in hospital for a day
> exposes people, on average, to at least 75 micromorts."

Four sentences, four steps: an annual count, a caveat on that count, a daily
rate, a converted figure. Each step names the number it used and the
assumption it made, so a reader can locate the exact point where they might
disagree with the total.

> "Of course, we can only quote average risks over a population, which
> neither represent your personal risks, nor those of a random person drawn
> from the population. Nevertheless they provide useful ballpark figures from
> which reasonable odds for specific situations might be assessed."

He names two specific things the average risk does not represent before
saying what it is still useful for. Both the concession and the defense are
particular claims about the number, not a general hedge tacked on for
balance.

## Julia Evans, "Some easy statistics: Bootstrap confidence intervals"

Source: https://jvns.ca/blog/2015/07/04/bootstrap-confidence-intervals/

> "So, let's say I have some numbers like: 0, 1, 3, 2, 8, 2, 3, 4 describing
> the number of no-shows for flights from New York to Puerto Rico. And that I
> also have no idea what kind of distribution this number should have, but
> some Important Person is asking me how much it's okay to oversell the plane
> by."

The made-up numbers are small enough to read in one glance, and the scenario
gives them a job before any statistic is computed on them. The reader knows
what the eight numbers are for before being asked to trust anything derived
from them.

> "Uh, great. the 5th percentile is there will be 0.35 people who don't make
> the plane. This is a) not really something I can take to management, and b)
> I have no idea how much confidence I should have in that estimate, given
> that I only have 8 data points. And I have no distribution to use to reason
> about it."

She produces the exact number the calculation was built to produce, then
immediately lists the specific reasons it doesn't deserve confidence: the
absurd fractional person, the small sample, the unknown distribution. Nothing
about the number's limits is left for the reader to infer.

> "The way you bootstrap is to sample with replacement from your data a lot
> of times (like 10000). So if you start with [1,2,3], you'd sample [1,2,2],
> [1,3,3], [3,3,1], [1,3,2], etc. Then you compute your target statistic on
> your new datasets. So if you were taking the maximum, you'd get 2,3,3,3,
> etc. This is great because you can use any statistic you want!"

The procedure is walked on a three-number example small enough to write out
every resample by hand, before the general statistic it produces is named.
Nothing here requires the reader to already know the word for what she's
doing.
