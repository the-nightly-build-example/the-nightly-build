# Voice guide: the-evidence/dropout (01)

## How this piece should sound

This lesson explains one paper's mechanism and then tells the reader plainly
how much of the paper's reputation the evidence still supports. That's two
jobs that need the same register rather than a switch between them: plain and
concrete while it's teaching what dropout does, and just as plain and
concrete while it's saying where the paper's own framing has aged.

Open the mechanism the way Willison names the plain fact and lets the
correction to a bigger claim ride along in the same sentence (Willison,
"Ignore the 'AGI' hype..."). State what dropout does — units kept with
probability p, the rest zeroed, weights scaled at test time — in the same
breath as whatever inflated description of dropout the reader is likely
carrying in, rather than clearing the inflated version out of the way first
and teaching the mechanism as a separate, later step.

Where the paper gives its own justification — the co-adaptation story, the
exponentially-many-sub-networks analogy — Evans's floating-point paragraph is
the model for how much concreteness a mechanism needs (Evans, the 0.21
example). Don't describe the ensemble analogy in the abstract. Give the
reader something to hold: the paper's own numbers, or a worked instance of
the keep-and-scale arithmetic with an actual value of p.

Report the present-day narrowing of dropout's role — dropout set to zero or
applied sparingly in large transformers — the way Evans reports the benchmark
reversal (Evans, "This turned out to be wrong"): state what changed as
flatly as the original claim was stated, without turning the correction into
a verdict on the 2014 authors' judgment.

Recht's Markov Decision Process paragraph is the shape for the piece's
central honesty move: a technique's inflated reputation is usually a specific
case mistaken for the whole story (Recht, "professors torture you with in AI
classes"). Dropout's own version of that inflation is the "prevents
overfitting, full stop" reading of the paper. The corrective this lesson can
reach for is not that dropout doesn't work, but that its place in the
standard toolkit was one point in a landscape that kept changing underneath
it, and the two claims don't need to be pitted against each other any more
sharply than the evidence itself does.

Recht's closing paragraph is worth returning to for how the lesson states its
own scope: name exactly what the paper's numbers support and no more (Recht,
"captures every example I know of"), rather than reaching for a bigger
verdict about dropout in general than the paper's own list of benchmarks can
carry.

Where the interaction between dropout and batch normalization, or the exact
reason large-data models lean less on dropout, isn't fully settled by what's
cited, Evans's "I don't know which is better!" is the model for saying so
directly rather than picking a side to sound more finished than the evidence
is.

## Julia Evans, "Benchmarking correctly is hard (and techniques for doing it better)"

Source: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/

> "First: I didn't know that printing floating point numbers was a research
> problem! The core problem is that - there are a finite amount of 64 bit
> floating point numbers (about 2^64 of them!). So for any number, there are
> one or two closest floating point numbers to that number. 0.21 and
> 0.21000000000000002 are very close! So close that there's no floating point
> number between them."

This explains why printing a floating-point number is a real problem by
putting two actual numbers on the page rather than describing floating-point
precision as a concept. The parenthetical aside and the admission that she
didn't know this was a research problem keep a first-person presence inside
a paragraph that is otherwise doing pure mechanism.

> "This turned out to be wrong - it was actually 2x slower than the
> approximate algorithm (it's still an improvement on the state of the art
> in exact algorithms). They talk about what happened in their README.
>
> I don't point this out to make fun of the researchers for coming up with
> an incorrect result. I'm pretty sure they're way better at performance
> analysis than I am. Instead, I think this is a really good illustration
> that benchmarking programs and figuring out which one is faster is really
> hard - much much harder than you might think."

She reports a published claim and then reports that it was wrong, in the
same flat register she used for the original claim, without softening the
correction into ambiguity. The next paragraph explicitly declines to make
the reversal about the researchers' competence, which keeps the correction
about the finding rather than about anyone's error.

> "I found this paper interesting because it didn't advocate using a Smart
> Benchmarking Framework which Solves All the Problems For You, and instead
> explains how you can understand the properties of the code that you're
> benchmarking and design a statistical analysis appropriately. I don't know
> which is better!
>
> But as a person who's done a lot of data analysis, the idea that you
> should look at the data that you're using to make an important decision
> (more than just calculating a single point estimate of the median /
> average) seems extremely reasonable to me."

She states a real uncertainty instead of picking a side to sound decisive,
then gives the one thing she is sure of and why. The two sentences separate
what she's confident about from what she isn't, in the same paragraph, and
neither one is dressed up to hide which is which.

## Simon Willison, "Here's how I use LLMs to help me write code"

Source: https://simonwillison.net/2025/Mar/11/using-llms-for-code/

> "Ignore the 'AGI' hype—LLMs are still fancy autocomplete. All they do is
> predict a sequence of tokens—but it turns out writing code is mostly about
> stringing tokens together in the right order, so they can be extremely
> useful for this provided you point them in the right direction."

The sentence corrects a specific piece of hype with a specific mechanism in
the same breath, so the correction and the plain description of what the
thing does arrive together rather than one after the other. Nothing in the
sentence apologizes for the correction or oversells what's left standing
after it.

> "Most of the craft of getting good results out of an LLM comes down to
> managing its context—the text that is part of your current conversation.
>
> This context isn't just the prompt that you have fed it: successful LLM
> interactions usually take the form of conversations, and the context
> consists of every message from you and every reply from the LLM that
> exist in the current conversation thread."

The mechanism is stated once, plainly, and the next sentence adds exactly
one more fact about it — what counts toward it — instead of restating the
same definition with more adjectives. The two sentences build on each other
rather than circling the same point twice.

> "I wrote about this at length last week: the one thing you absolutely
> cannot outsource to the machine is testing that the code actually works.
>
> Your responsibility as a software developer is to deliver working
> systems. If you haven't seen it run, it's not a working system. You need
> to invest in strengthening those manual QA habits."

The claim about responsibility is stated as a flat rule and then defended in
one more sentence, with no hedge and no exception carved out for
convenience. The voice here is a practitioner naming a job's obligation, not
a general observation floated above the work.

## Ben Recht, "Defining Reinforcement Learning Down"

Source: https://www.argmin.net/p/defining-reinforcement-learning-down

> "We have a computer program in feedback with an evaluation environment.
> The computer produces responses to a series of tests. An external agent
> then numerically scores these responses. The computer program is fed
> these scores and internally updates its software for the subsequent
> evaluation. The process repeats. The goal of the iteration is to produce a
> program that achieves the highest possible average score when interacting
> with the evaluation environment."

Each short sentence adds one step of the mechanism, in order, and no
sentence does more than one job. The plainness of the vocabulary — "a
computer program," "an external agent" — is itself the explanation; there's
no jargon left over to translate afterward.

> "Now you might ask, what about all of those Markov Decision Processes that
> professors torture you with in AI classes? Though it has historically
> been the other way around in classical artificial intelligence, Reformist
> RL, like behaviorist psychology, views MDPs as secondary rather than
> primary."

The question names the exact assumption a reader trained on the standard
version of the subject would be carrying in, then states plainly that the
standard version is the narrower case, not the general one. The wry "torture
you" phrase is the one place personality shows, and it doesn't soften the
actual claim being made about what's primary and what isn't.

> "This characterization of reinforcement learning and Reformist
> Reinforcement Learning captures every example I know of. It connects
> nicely to the rest of machine learning. You can teach it in a single
> class. My survey of reinforcement learning goes from 27 pages to 809
> words. I have learned from experience."

The final paragraph states the scope of what was just shown instead of a
bigger claim the piece didn't earn, and stays that specific about a
definition that took him most of a page to reach. The dry aside about page
counts, right at the end, is the one place the writer's own workmanship
becomes visible.
