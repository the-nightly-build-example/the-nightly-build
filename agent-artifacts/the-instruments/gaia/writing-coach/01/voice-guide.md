# Voice guide: the-instruments/gaia (01)

## How this piece should sound

This lesson takes the GAIA score apart for a reader who has never built a
benchmark and needs to know, by the end, exactly what that number is allowed
to tell them. Open the way Scott Alexander opens "The Mystery Of Internet
Survey IQs": with the number itself and the fact that makes it worth a second
look, before any framing about what benchmarks are for in general. The GAIA
score and the human baseline it gets compared against belong in the opening
sentences, with whatever makes that comparison strange (a gap the reader can
check against the question count or the scoring rule) sitting right next to
it, the way Alexander puts 1/200 and 1/50 next to his two IQ figures.

The lesson will need to keep at least two numbers straight that a scanning
reader could conflate: the validation-set score and the held-out test score,
or the overall score and a single level's score, or a leaderboard figure and
what the paper itself reports. Kevin Drum's cancer post exists almost
entirely to keep two numbers from blurring into one ("Not the death rate
from cancer... but the actual number of new cancers"). The GAIA lesson has
its own such pair to name and keep separate the moment either number first
appears.

When the lesson reaches the case where a GAIA figure misled people, state
the correction the way Alexander states his SAT-to-IQ fix: the wrong number,
the right number, and who or what produced the correction, in one sentence
if the material allows it. "Using Sebastian's updated tables, we find that
the average Less Wrong IQ... goes down from 140 → 132" credits the fix to a
named source instead of presenting it as the writer's own catch. If the
misleading case here turns on a specific submission, paper, or grading
dispute, name it the same way, at the moment the wrong number gets revised
downward or upward.

If the lesson's research turns up more than one plausible reason a GAIA
score can't be taken at face value (grading strictness, validation/test
mismatch, task selection, whatever the researcher finds), lay them out
side by side and say plainly that they point in different directions before
explaining each in turn, the way Alexander closes with three IQ estimates
that "contradict each other" and then works through why each might be the
wrong one. That is a shape for the analysis section to reach for only if the
research actually turns up competing explanations rather than one clean
one.

None of these three write in the register this lesson has to hold. All
three write in the first person, and the lesson's body never does. What
carries over is the precision and the willingness to put a number where a
summary would go; the pronoun stays behind. Where Julia Evans writes "I'd
like to make programs faster, and a great way to make your stuff WAY FASTER
is to make many small 5% improvements," the move worth keeping is that she
gives a concrete reason the mechanics matter to someone doing real work.
The GAIA lesson can do the same by tying a mechanical detail (how the
grader checks an answer, how a level is defined) to what it lets the reader
believe or doubt about an assistant, stated as a fact about the mechanism.

Drum's "Why?" standing alone as its own sentence, answered by the next one,
is worth having on hand for wherever the lesson explains why a GAIA number
moved or a score looked stranger than it should have. His closing line about
the cancer chart proposes a specific alternative reading of the exact chart
just shown; the lesson's analysis of what a high GAIA score does and doesn't
license can close the same way, naming the specific thing a reader should
stop believing about "AI assistants" once they've seen that one figure.

## Scott Alexander, "The Mystery Of Internet Survey IQs"

Source: https://www.astralcodexten.com/p/the-mystery-of-internet-survey-iqs

> "I have data from two big Internet surveys, Less Wrong 2014 and Clearer
> Thinking 2023. Both asked questions about IQ: The average LessWronger
> reported their IQ as 138. The average ClearerThinking user reported their
> IQ as 130. These are implausibly high. Only 1/200 people has an IQ of 138
> or higher. 1/50 people have IQ 130, but the ClearerThinking survey used
> crowdworkers (eg Mechanical Turk) who should be totally average."

The piece opens directly on the two numbers, ahead of any lead-in about why
online IQ claims matter. The next sentences supply the base rate that makes
"implausibly high" checkable: 1/200 and 1/50 let the reader do the
arithmetic themselves. Naming the ClearerThinking sample as
Mechanical Turk crowdworkers is doing real work, since that is the reason
the second number should have been unremarkable.

> "Using Sebastian's updated tables, we find that the average Less Wrong IQ
> as predicted by SATs goes down from 140 → 132, and the ClearerThinking IQ
> goes down from 134 → 124."

A paragraph of methodology (why the standard SAT-to-IQ conversion is wrong)
lands in one sentence with two before-and-after figures and an arrow. The
writer credits Sebastian by name for the fix, and the arrow lets the size of
the correction register at a glance, sparing the reader from computing it
out of prose.

> "We have three ways of estimating IQ in these samples: demographic norming
> based on education levels, self-reports from past IQ tests, and
> self-reported SAT scores converted into IQ. All of these contradict each
> other."
>
> "The self-report numbers are probably wrong because some people use bad
> tests, and other people use good tests that can't measure above 135
> accurately."

The piece doesn't pick a winning estimate and stop. It lists all three,
states plainly that they disagree, and then works through why each one
might be the wrong one, one at a time. "Probably wrong because" commits to
an actual mechanism, bad tests here, a measurement ceiling there, so the
reader gets a specific, checkable reason for each doubt.

## Julia Evans, "Benchmarking correctly is hard (and techniques for doing it better)"

Source: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/

> "First: I didn't know that printing floating point numbers was a research
> problem! The core problem is that – there are a finite amount of 64 bit
> floating point numbers (about 2^64 of them!). So for any number, there are
> one or two closest floating point numbers to that number. 0.21 and
> 0.21000000000000002 are very close! So close that there's no floating
> point number between them."

The astonishment in "I didn't know that was a research problem!" comes
right before the sentence that earns it: a real figure (2^64) and a
concrete pair of numbers (0.21 versus 0.21000000000000002) the reader can
check the claim against.

> "I'm less interested in the question of academic rigor here and more
> interested in the idea of benchmarking correctly in practice – I'd like to
> make programs faster, and a great way to make your stuff WAY FASTER is to
> make many small 5% improvements. So you need to actually be able to detect
> a 5% improvement."

She states her own stake in the question directly rather than summarizing
someone else's paper from a neutral remove, and that stake is what turns an
abstract point about confidence intervals into a reason a working
programmer should care about them. The capitalized "WAY FASTER" carries the
emphasis without a qualifier hedging it.

> "I found this paper interesting because it didn't advocate using a Smart
> Benchmarking Framework which Solves All the Problems For You, and instead
> explains how you can understand the properties of the code that you're
> benchmarking and design a statistical analysis appropriately. I don't know
> which is better!"

Capitalizing "Smart Benchmarking Framework which Solves All the Problems
For You" mocks a category of product rather than one competitor by name,
and the next sentence admits she has no verdict between the two approaches.
Ending on stated uncertainty, instead of tidying disagreement into a
conclusion, matches what the open question in the piece actually looks
like.

## Kevin Drum, "Raw data: A cautionary tale"

Source: https://jabberwocking.com/raw-data-a-cautionary-tale/

> "How has the incidence of cancer risen over the past half century? Not the
> death rate from cancer, which has gone down because of better treatments,
> but the actual number of new cancers."

The second sentence exists only to rule out a different number the reader
might substitute for the one under discussion. Naming and setting aside the
death rate before saying anything about incidence keeps the two figures
from blurring together for a reader skimming past the distinction.

> "It's all about prostate cancer and it's all about detection. When PSA
> tests were approved and became widely used, prostate cancer diagnosis
> surged—but then dropped. Why? Too many harmless, asymptomatic cancers were
> being detected, so doctors became more rigorous about how high a PSA score
> needed to be before they suggested treatment."

"Why?" stands alone as its own sentence and gets answered directly by the
next one. The answer names the actual mechanism, a screening test whose use
changed and a threshold doctors later tightened, instead of describing the
swing in diagnoses as puzzling or significant.

> "This is apropos of nothing. It's just an example of how raw data can be
> misleading if you don't know the history behind the data collection.
> Cancer in men didn't really rise starting in the early '80s, we just got
> better at detecting one particular variety. Then we decided we were
> overdiagnosing and pulled back. Underneath it all, the actual incidence of
> cancer was about the same all along. You could draw a straight line from
> 1985 to 2015 and the chart would probably be more accurate."

The closing line proposes a specific, checkable alternative to the chart
just shown (a straight line from 1985 to 2015), rather than a general
statement about data being tricky. "This is apropos of nothing" is Drum
being honest that the post has no larger argument to sell, which is itself
the piece declining to manufacture stakes it hasn't earned.

---

Production record: written by claude-sonnet-5, effort=low.
