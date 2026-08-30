# Voice guide: The Instruments — SimpleQA

## How this piece should sound

This lesson takes apart one number: the SimpleQA score. The reader has never
built a benchmark and does not need to. What they need is to watch one get
built in front of them, in the order it actually happened, so that by the end
they can look at "SimpleQA: 62%" the way Nate Silver's readers learn to look
at a poll average — not as a fact handed down, but as the output of a
procedure with visible joints. Silver's swing-state piece never announces that
polls can mislead in the abstract. It opens on one afternoon's release from
one named firm, gives the actual numbers ("between 47 and 48 percent" in all
seven states), and only after the reader has felt how convenient that is does
it name the mechanism. The SimpleQA lesson can open the same way: on the
number as it is actually quoted somewhere, before backing up to explain how it
was made.

Spiegelhalter and Masters's habit of dating and sizing everything is worth
carrying over directly: not "deaths were reported unevenly" but "560 deaths
reported for England on Monday 18 January 2021, jumping to 1,507 the next
day." SimpleQA's own construction has this kind of joint somewhere — how the
questions were sourced, how the grader decides "correct" from "not attempted,"
what counts as a hallucination for scoring purposes — and each one can get the
same treatment: the actual mechanism, dated or counted, not summarized as
"the methodology has limitations."

When the piece needs to make a percentage mean something, Spiegelhalter's
schoolchildren-and-over-90s comparison is the model: he does not tell the
reader that risk varies enormously by age, he gives the two population counts
and the two death counts and lets "35,000 times" fall out of the arithmetic.
A SimpleQA figure that the reader cannot independently size — a score gap
between two models, a rate of confident wrong answers — can be pinned the same
way, against a quantity the reader already has some feel for.

The piece is allowed to say, plainly, where a careful reader still got the
number wrong, the way Spiegelhalter and Masters report their own early
mortality-displacement estimate and then that they were proved wrong by what
actually happened. That is not hedging. It is evidence that the number has
limits worth naming, offered without asking the reader to distrust the whole
enterprise. If the case the series direction asks for — a real instance where
the SimpleQA number misled someone, and what it cost — turns up a specific
misjudgment like that, it can be reported the same plain way: what was
claimed, what the number actually supported, and what followed.

Recht's lecture-blog voice is a reminder that explaining a benchmark's
mechanics does not require solemnity. When he narrates how train-test splits
actually got adopted, the sentences shorten to almost a checklist — "Gather
some data. Split the data in two. Release the data in public." — and the
piece can drop into that same flat rhythm when it walks through how SimpleQA's
own pipeline works, rather than smoothing the steps into a single dense
sentence. And when Recht wants to represent an objection to benchmarking, he
gives it to an invented but specific character, the grumpy statistician, in
that person's own words, rather than writing "critics argue" and paraphrasing.
If this lesson needs to voice a real objection to SimpleQA or to LLM
benchmarks generally, naming the objection's substance in its own terms will
carry more than attributing it to an unnamed chorus.

The lesson template's own rule stands over all of this: a term of art like
grader, calibration, or hallucination rate enters only when the lesson cannot
proceed without it, defined in plain words in the sentence that introduces it.
None of the exemplars above write for a technical reader, and neither does
this piece.

## Ben Recht, "Benchmarking our benchmarks"

Source: https://www.argmin.net/p/benchmarking-our-benchmarks

> "The AI Winters occur when there are no good benchmarks to fight over.
> 'Progress' happens when nerds have numbers to make go up, and entrepreneurs
> have benchmarks to sell as signifiers of sure bets."

This is a specific claim about who wants a benchmark number to move and why,
not a mood. "Nerds have numbers to make go up" and "entrepreneurs have
benchmarks to sell" name two different actors with two different incentives,
which is what keeps the sentence from being empty scene-setting. The person
behind it is visible in the register shift: "AI Winters" is a real term, "to
fight over" is not.

> "Since there were too many options, people just stuck with what was easy.
> Gather some data. Split the data in two. Release the data in public. Then
> it was a matter of trust within the community that what people published
> was honest benchmarking. This internal trust was key, and is key to all
> benchmarks."

Four short sentences narrate the actual sequence of a decision, not a
description of one. The plainness is doing work: each sentence is one action,
in the order it happened, so the reader can watch the standard get built
instead of being told a standard exists.

> "If you are a grumpy statistician, you'll always say stuff like 'The error
> bars on the test sets are too small to matter. You are double-dipping.
> There are too many experimenter degrees of freedom. Test set benchmarking
> is not a severe test of a hypothesis.'"

Rather than write "critics argue that test sets are statistically unsound,"
Recht puts the objection in a specific mouth and specific words, four
technical complaints in a row without translation. The joke is in "grumpy,"
but the content of the complaint is not softened or mocked — it is quoted
straight. That combination, a person's irritation named and the substance of
their point kept intact, is where the writer shows up.

## David Spiegelhalter and Anthony Masters, "Covid by numbers: 10 key lessons separating fact from fiction"

Source: https://www.theguardian.com/world/2021/oct/10/covid-by-numbers-10-key-lessons-separating-fact-from-fiction

> "The daily counts on the news of the '28-day' death figures do not
> represent deaths that happened in the last 24 hours, but those newly
> reported. There is a clear weekly cycle, with the numbers tending to be
> higher on Tuesdays and Wednesdays because of reporting delays over the
> weekend. That has led to some dramatic differences: there were 560 deaths
> reported for England on Monday 18 January 2021, jumping to 1,507 the next
> day."

The correction is not "these figures can be misleading" — it is the exact
mechanical reason (a reporting lag, not a death spike) and then the two real
numbers that show how large the artifact gets. A reader who only remembers
"560 to 1,507 overnight" has learned something they can check the next time a
Tuesday number jumps.

> "Out of over 7 million schoolchildren aged between five and 14, 11 died
> with Covid-19 mentioned on their death certificate over the year (one in
> 660,000). In the same period, 469 died from other causes. At the other end
> of the scale, out of more than 500,000 people aged over 90, nearly 30,000
> died with Covid-19 on their death certificate (around six in 100). That was
> 35,000 times the fatal risk experienced by schoolchildren."

The multiplier at the end is not asserted, it is built in front of the reader
from two population counts and two death counts they can independently check.
Giving the raw counts before the ratio is what makes "35,000 times" land as
arithmetic rather than a claim to take on faith.

> "At the start of the first wave, one of us (DS) was quoted as saying, 'many
> people who die of Covid would have died anyway within a short period',
> while others estimated that this proportion could be more than half. We
> were proved wrong by the limited deficit in deaths over the following
> year."

The writer names his own earlier estimate and states plainly that it was
wrong, without softening it into "estimates varied" or moving on quickly. The
person is visible in "one of us (DS)" and in the flat admission that follows
it — there is no defense mounted, just the correction.

## Nate Silver, "There's more herding in swing state polls than at a sheep farm in the Scottish Highlands"

Source: https://www.natesilver.net/p/theres-more-herding-in-swing-state

> "Take, for example, this afternoon's polling release from the British firm
> Redfield & Wilton. They polled all seven of the core battleground states.
> And in all seven, Kamala Harris and Donald Trump each received between 47
> and 48 percent of the vote."

The piece opens on one firm's one release, named, with the actual numbers,
rather than a general statement that some pollsters herd. A reader meets the
suspicious pattern before they meet the word for it, which is why the
definition that comes later has something to attach to.

> "Based on a binomial distribution — which assumes that all polls are
> independent of one another, which theoretically they should be — it's
> realllllllllllllly unlikely. Specifically, the odds are 1 in 9.5 trillion
> against at least this many polls showing such a close margin."

The math is real and stated precisely (a named distribution, an exact odds
figure), and the writer still lets himself stretch "really" across a dozen
extra letters. The precision is not undercut by the joke; the joke sits next
to it. That is a specific person finding a number genuinely startling, not a
generic emphasis device.

> "This is a clear-as-day example of what we call herding: the tendency of
> some polling firms to move with the flock by file-drawering (not
> publishing) results that don't match the consensus or torturing their
> turnout models until they do."

The term "herding" is defined in the same sentence that introduces it, in one
clause, using two concrete behaviors (not publishing outlier results,
adjusting turnout models) rather than an abstract description of the failure
mode.
