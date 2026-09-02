# Voice guide: the-instruments/superglue

## How this piece should sound

This lesson takes a leaderboard number apart in front of a reader who has never
built one and has no reason to trust anyone who says "trust me." The register
that earns that trust is the one the paper voice already names: plain claims,
concrete stakes, no fuss. Below that general instruction, three moves from the
exemplars below fit this particular lesson's shape.

State the construction before you defend the objection to it, the way O'Neil's
opening two sentences name the verdict and the mechanism in the same breath. The
SuperGLUE score can be named plainly early — what it is an average of, what the
human row is — before the lesson spends any words on why that construction
misleads. Nothing here is a discovery to withhold; withholding it only makes the
reader do arithmetic on their own before they have the pieces.

Assign no blame before the reporting has earned it, the way Fung's four
questions about the US News ranking refuse to pick a villain until each party's
actual role is on the page. This lesson has several candidates for who is
responsible for "AI beats humans at reading comprehension" entering public
argument — the paper's own authors, the press covering the DeBERTa crossing, the
leaderboard format itself — and each can get its actual role stated before the
lesson decides how much blame it carries, rather than the piece deciding first
and reporting second.

Build one small worked example of the averaging problem, invented but honest
about being invented, the way Fung's hundred-student school runs the same
formula twice to produce two different numbers from the same twenty classes.
SuperGLUE's "one number hides a weighting choice" is a claim a reader can be
shown rather than told: two invented tasks with two different metrics, averaged,
against the same two tasks weighted differently, is the kind of small
demonstration this lesson has room for before it turns to the real eight.

Stay skeptical of your own reconstruction, not only of the number you are
correcting. Fung says plainly where his scraped-data workaround might be wrong
even as he uses it to catch Columbia; when this lesson explains what the human
baseline actually measures and what the crossing actually meant, the same
honesty applies to the lesson's own account of "what the annotators' protocol
actually captured" and "what saturation actually shows." A correction presented
as the new fixed truth teaches the wrong lesson about measurement.

Where the lesson reaches a verdict — what the DeBERTa crossing did and did not
mean, what a reader should now ask of any "beats human baseline" headline — earn
it with a specific figure the lesson produced, the way O'Neil's "more than a
third" follows arithmetic just shown and Alexander's "about half the gap" reports
a partial resolution as partial rather than a settled answer. The takeaway this
lesson leaves the reader with is a question they can now ask, not a mood; state
what fraction of the original claim survives and what doesn't, rather than
declaring the whole thing debunked or vindicated.

## Cathy O'Neil, "The arbitrary punishment of New York teacher evaluations"

Source: https://mathbabe.org/2015/04/02/the-arbitrary-punishment-of-new-york-teacher-evaluations/

> "The Value-Added Model for teachers (VAM), currently in use all over the
> country, is a terrible scoring system, as I've described before. It is
> approximately a random number generator."

The verdict and the comparison that makes it checkable arrive in the same two
sentences, with no qualifier stacked in front of either. A reader can hold "a
random number generator" against whatever the piece does next and see if it
holds up, because the claim is concrete enough to fail.

> "Let's think through the math of how likely it is that you'd be denied
> tenure based only on this random number generator. We will assume only that
> you otherwise get good ratings from your principal and outside observations.
> Indeed, Cuomo's big complaint is that 98% of teachers get good ratings, so
> this is a safe assumption."

Before running any arithmetic, she states exactly what is being held constant
and cites the specific figure that makes holding it constant reasonable. The
reader knows what is being tested and what has been set aside before a single
number gets multiplied.

> "This is the political power of a terrible scoring system. More than a third
> of teachers are being arbitrarily chosen to be punished by this opaque and
> unaccountable test."

The verdict sentence only appears after the coin-flip arithmetic just above it
produces the 35% figure that earns it. The judgment names the specific
mechanism — opaque, unaccountable — rather than resting on the adjective by
itself.

## Kaiser Fung, "Manufacturing statistics, US News style"

Source: https://www.junkcharts.com/manufacturing-statistics-us-news-style/

> "Is it the school administrators' fault that they one-up each other gaming
> the ranking to the nth degree? Or is it the people's fault for selecting one
> school over another because it's ranked higher on US News? Should US News
> have fact-checked submitted data? Can we blame US News for providing a
> product that apparently is deemed highly valuable?"

Four questions, four different parties, and none of them answered yet. The
piece spreads the possible blame across everyone with a hand in the number
before it reports what actually happened, so no party is convicted ahead of the
evidence.

> "Let's say a school with 100 students offers 20 undergraduate classes. Each
> student takes 4 classes, resulting in 400 total enrollments. Two of these
> classes are compulsory so the enrollment is 100 each. The other 200
> enrollments are split between 18 classes, so each of the smaller classes
> enrolls 11 students. Each student therefore has the same schedule, 2 large
> classes (n=100) and 2 small classes (n=11). Therefore, the average class size
> experienced for each student is (100+11)/2 = 56."

The example is invented, not the real Columbia data, but it runs the same two
counting rules against each other on the same twenty classes. The gap between
56 and 20 isn't asserted afterward — it's produced by the numbers in the
passage itself.

> "Undeterred by the lack of disclosure, Prof. Thaddeus does the prototypical
> data science thing - scrape the web, in particular, Columbia's Directory of
> Classes, for information on every class and its maximum enrollment size."
>
> "While analyzing scraped data provides a good approximation, this method
> (like most web scraping exercises) cannot claim to be accurate. One problem
> is that capacity is not the same as actual enrollment."

The correction gets the same scrutiny as the number it's correcting. Having
just caught US News overstating a figure, the piece immediately says where its
own workaround could be wrong too, instead of presenting the fix as the new
settled number.

## Scott Alexander, "The Mystery Of Internet Survey IQs"

Source: https://www.astralcodexten.com/p/the-mystery-of-internet-survey-iqs

> "These are implausibly high. Only 1/200 people has an IQ of 138 or higher.
> 1/50 people have IQ 130, but the ClearerThinking survey used crowdworkers (eg
> Mechanical Turk) who should be totally average."

"Implausibly high" isn't left to stand on its own; the next two sentences give
the exact ratios a reader can check it against, plus the one detail (who the
respondents actually were) that makes the number suspicious in the first place.

> "The self-report numbers are probably wrong because some people use bad
> tests, and other people use good tests that can't measure above 135
> accurately. The SAT numbers are probably wrong because of selection: smarter
> people are more likely to take the SAT and remember their score. This
> probably becomes less important in overall smarter samples, where most
> people have taken the SAT and nobody has a score which is truly
> embarrassing."

Three competing numbers were in play through the piece, and the close doesn't
average them into one answer or crown a winner — it gives each one its own,
different reason for being wrong. "Probably" appears twice: the writer names
his own remaining uncertainty instead of resolving it for effect.

> "Since the only reported SAT scores come from people who remember them, this
> means that SAT scores overestimate the full-sample IQ, at least in this
> case. We previously had a gap between the 124 IQ from SAT conversion and the
> 110 observed IQ. This resolves about half of the gap, bringing it down to
> 124 predicted vs. 116 observed."

The finding is reported as a fraction of the original problem, not the whole
answer: "about half the gap." The running discrepancy gets an updated number
attached to it rather than being declared closed, so the reader always knows
how much is still unexplained.
