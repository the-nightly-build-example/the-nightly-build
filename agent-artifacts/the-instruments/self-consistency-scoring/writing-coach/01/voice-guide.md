# Voice guide: the-instruments/self-consistency-scoring (writing-coach 01)

## How this piece should sound

This lesson explains majority-vote scoring, the convention that turns k sampled
chain-of-thought attempts on one problem into a single reported number written
cons@k or maj@k, for a reader who has algebra and probability but has never
worked in machine learning. Write in plain claims with the stakes kept concrete,
in the register the press asks for: Matt Yglesias explaining something he knows
cold. A term the reader does not already hold, such as chain-of-thought, sampling
temperature, or plurality vote, gets a plain definition in the sentence that
first uses it, and nothing else leans on machine-learning background.

The procedure is easiest to see in whole numbers before any percentage. Steven
Strogatz reaches for "natural frequencies," simple counts of events, to make a
conditional probability legible, and the Our World in Data piece works out a rate
by counting the people inside each group. Where the lesson shows why answering
the same problem k times and taking the most common final answer yields a score,
it can lay out the actual answers and count them, then turn the count into a
rate, rather than opening with an accuracy figure the reader has to take on
trust.

Julia Evans explains a surprising numeric result by running one concrete case and
showing the arithmetic, what she expected set against what the machine actually
returned. When this lesson explains why sampling many times and voting moves a
score, and where the material shows what voting cannot move, one worked case with
real sampled answers and a real count of them will carry more than a general
statement about accuracy.

The distance between a cons@k number and a single-sample number is the lesson's
center. Strogatz's turn in the O.J. section, where he shows that both sides were
arguing from the probability of the wrong event and then states the question that
was actually at stake, is the move to study: name the exact quantity each number
reports, and say plainly what the cons@k number costs that the single-sample
number does not, so the reader sees why setting the two side by side misleads
rather than being told it is unfair. Where the piece needs to name the error in a
public comparison, the Our World in Data writers name theirs outright, "base rate
fallacy," and say in the same breath what it leaves out.

After the number is built and the comparison is taken apart, the lesson can land
its judgment on the reader without dressing it up. Strogatz sets a full paragraph
of wrong guesses against a six-word answer and lets the setup pay for the short
line; the register here tolerates a bare short sentence in that spot. Evans takes
care that a reader not close her piece believing the tool is broken. This lesson
can show exactly where majority-vote scoring misleads while keeping it clear that
the convention is real and has a job, so the reader does not leave thinking the
number is a trick.

## Steven Strogatz, "Chances Are"

Source: https://opinionator.blogs.nytimes.com/2010/04/25/chances-are/

> "What these resourceful students kept discovering, year after year, was a better way to think about conditional probability. Their way comports with human intuition instead of confounding it. The trick is to think in terms of "natural frequencies" — simple counts of events — rather than the more abstract notions of percentages, odds, or probabilities. As soon as you make this mental shift, the fog lifts."

Strogatz credits his students with the method before he adopts it, so the clearer
approach arrives as something people found rather than something he is selling.
He defines the term inside the sentence that uses it, and the reader picks up
"natural frequencies" without having to stop. The short payoff at the end lands
because the sentences before it set up the confusion it clears.

> "As for the American doctors, 95 out of 100 estimated the woman's probability of having breast cancer to be somewhere around 75 percent.
>
> The right answer is 9 percent."

The paragraph before this gives the doctors' wrong estimates in full; then a
single six-word sentence gives the answer. Strogatz trusts the setup to make the
short line land and adds no comment to it. The restraint is his: he has the
reader's attention at that moment and spends it on the number itself.

> "In effect, both sides were asking the jury to consider the probability that a man murdered his ex-wife, given that he previously battered her. But as the statistician I. J. Good pointed out, that's not the right number to look at.
>
> The real question is: What's the probability that a man murdered his ex-wife, given that he previously battered her and she was murdered by someone? That conditional probability turns out to be very far from 1 in 2,500."

Strogatz shows that both sides argued from one figure, that the figure answered
the wrong question, and then states the question that was actually at stake. He
does the correction by writing out both quantities in full, so the reader can see
that they differ instead of being told so. The plain verdict, "that's not the
right number to look at," rests on the sentences around it and needs no
underlining.

## Julia Evans, "Examples of floating point problems"

Source: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/

> "I don't want you to read this post and conclude that floating point is bad. It's an amazing tool for doing numerical calculations. So many smart people have done so much work to make numerical calculations on computers efficient and accurate!"

Evans stops to say what she does not want the reader to conclude, and says it
before the examples rather than after them. Her praise is specific: she points
at the work that went into making the calculations accurate, so it reads as her
actual view and not a hedge against the failures she is about to show. The voice
is at its plainest here: short sentences and an exclamation she means.

> "The problem in this case is that, for 32-bit floats, 262144.0 + 0.01 = 262144.0. So it's not just that the number is inaccurate, it'll actually never increase at all! If we travelled another 10,000 kilometers, the odometer would still be stuck at 262144 meters (aka 262.144km)."

She states the surprising fact flatly and puts the exact numbers where the reader
can check them. "It'll actually never increase at all" is the part that is hard
to believe, and she does not soften it or build to it. The explanation stays in
the same register as the rest of the post, so the reader is never handed a
harder sentence than the one before.

## Edouard Mathieu and Max Roser, "How do death rates from COVID-19 differ between people who are vaccinated and those who are not?"

Source: https://ourworldindata.org/covid-deaths-by-vaccination

> "Now we have all the information we need and can calculate the death rates:
>
> Of 10 unvaccinated people, 5 died → the death rate among the unvaccinated is 50%.
>
> Of 50 vaccinated people, 5 died → the death rate among the vaccinated is 10%.
>
> We, therefore, see that the death rate among the vaccinated is 5 times lower than among the unvaccinated."

The passage runs the whole calculation in small whole numbers the reader can
hold: how many died in each group, then the rate for each group, then the one
comparison. Each step is its own short line, and the comparison comes only once
both rates are in hand. Because the counts are shown, the line that draws the
conclusion needs no emphasis.

> "In the example, we invented numbers to simplify calculating the death rates. However, the same logic applies to the current COVID-19 pandemic. Comparisons of the absolute numbers, as some headlines do, make a mistake known in statistics as a 'base rate fallacy': it ignores that one group is much larger than the other."

The writers name the mistake and then say, in one clause, exactly what it
ignores, so the label is defined the moment it appears. They tie it back to the
reader's own situation by pointing out which group has grown larger, which is
what makes the named fallacy matter rather than stay abstract. The prose is
unhurried and assumes no statistics past counting.
