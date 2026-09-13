# Voice guide: the-instruments/bertscore

## How this piece should sound

This is a lesson on the Instruments desk for a reader who follows ideas easily
and has never worked inside a machine-translation or summarization codebase. The
three writers below share the register this lesson wants: plain sentences, a
worked example carrying each idea, and a hard conclusion stated without
softening. Each of them keeps the exact technical words while explaining them,
and none writes up to the subject.

The spine of this lesson is a computation: turn each token into a vector, match
each candidate token to its closest reference token, average the similarities
into precision, recall, and F1. Olah computes a conditional probability on a
named pair, rain and a coat, with the two percentages written out, so the reader
watches the operation run rather than reads a definition of it. Where the piece
has a real candidate and reference to work with, the matching and averaging can
run the same way, on stated tokens and stated cosine numbers, so the reader
watches each candidate token find its partner.

Before the arithmetic, the reader needs to know what the number is asking.
Miller states the question his formula settles in one plain sentence before any
notation appears. At the point cosine similarity or the final average enters,
this lesson can say in words what quantity is being asked for, so the reader
carries the meaning into the math instead of decoding it back out afterward.

Where the lesson reaches a limit on what a BERTScore number supports, the
sentence that states it can be as flat as the reporting around it. Gregg tells
the reader inside his first four sentences that a number everyone trusts does
not measure what they assume, and he does not walk it back later. When this
piece establishes that two of these scores computed differently are not the same
measurement, or that a rescaled score reads on a different footing than a raw
one, a caveat hedged into "may sometimes" trains the reader to discount the
thing you most need them to keep.

Some of the machinery here is a convention rather than a law: a rescaling
baseline chosen for readability, a greedy matching rule picked among
alternatives, an encoder chosen from many. Gregg, asked where his own cutoff
came from, answers that he made it up and then shows how a reader could compute a
real one. Where a step in BERTScore is a choice, naming it as a choice is
available to you, and the reader trusts the steps you present as principled more
once you have marked the ones that are not.

A limitation is easiest to believe as a case. Miller does not describe the
weakness of average rating in the abstract; he shows two items with their exact
counts and lets the wrong ranking speak. Where this piece reaches a pair whose
surface meaning overlaps while a fact is flipped, or where word overlap and this
metric disagree, one worked pair with its numbers can carry the point that a
general statement of the weakness would only assert.

## Evan Miller, "How Not To Sort By Average Rating"

Source: https://www.evanmiller.org/how-not-to-sort-by-average-rating.html

> "Average rating works fine if you always have a ton of ratings, but suppose item 1 has 2 positive ratings and 0 negative ratings. Suppose item 2 has 100 positive ratings and 1 negative rating. This algorithm puts item two (tons of positive ratings) below item one (very few positive ratings). WRONG."

Miller shows why a scoring method fails by naming two items with their exact
counts and letting the arithmetic produce the wrong order, which the reader can
check against the numbers he gave. The bare "WRONG." is Miller declining to
soften a verdict the example has already earned.

> "We need to balance the proportion of positive ratings with the uncertainty of a small number of observations. Fortunately, the math for this was worked out in 1927 by Edwin B. Wilson. What we want to ask is: Given the ratings I have, there is a 95% chance that the “real” fraction of positive ratings is at least what? Wilson gives the answer."

He states what the formula is for, as a plain question, before any notation
arrives, so the reader meets the meaning first and the symbols second. The direct
address and the working-programmer framing are Miller talking to the person he
expects to be reading.

> "Many people who find something mediocre will not bother to rate it at all; the act of viewing or purchasing something and declining to rate it contains useful information about that item's quality."

Miller points at what the rating number cannot see, the people who declined to
rate, and treats their silence as data the score leaves on the floor. It shows a
writer thinking about what a measurement misses, not only about what it captures.

## Brendan Gregg, "CPU Utilization is Wrong"

Source: https://www.brendangregg.com/blog/2017-05-09/cpu-utilization-is-wrong.html

> "The metric we all use for CPU utilization is deeply misleading, and getting worse every year. What is CPU utilization? How busy your processors are? No, that's not what it measures."

Gregg opens by contradicting the reader's assumption head-on, in short questions
and a flat answer, and he spends no words easing into it. Being this direct that
a familiar number means something other than people think is the whole footing of
the piece, set in four sentences.

> "The metric we call CPU utilization is really “non-idle time”: the time the CPU was not running the idle thread. Your operating system kernel (whatever it is) usually tracks this during context switch. If a non-idle thread begins running, then stops 100 milliseconds later, the kernel considers that CPU utilized that entire time."

He replaces the familiar name with what the machine actually counts, then gives a
concrete case, a thread that runs and stops 100 milliseconds later, so the reader
can picture the definition. The plain relabeling is the move that lets the rest of
his argument stand.

> "For my above rules, I split on an IPC of 1.0. Where did I get that from? I made it up, based on my prior work with PMCs."

Asked where his own threshold came from, Gregg says he made it up, and then tells
the reader how to derive one that fits their system. Admitting the number is a
rule of thumb, instead of dressing it as derived, is the writer being exact about
how much the number is worth.

## Chris Olah, "Visual Information Theory"

Source: https://colah.github.io/posts/2015-09-Visual-Information/

> "There's a 25% chance that it's raining. If it is raining, there's a 75% chance that I'd wear a coat. So, the probability that it is raining and I'm wearing a coat is 25% times 75% which is approximately 19%."

Olah runs the actual arithmetic on a concrete pair, with each percentage named, so
the reader sees a conditional probability computed rather than defined. The homely
choice of example, the local weather and what he wears, is Olah reaching for
something the reader already holds to carry an unfamiliar operation.

> "There is simply a fundamental limit. Communicating what word was said, what event from this distribution occurred, requires us to communicate at least 1.75 bits on average. No matter how clever our code, it's impossible to get the average message length to be less."

After building one specific code, Olah names the limit it runs into and says
plainly that no cleverness beats it. Stating that a number is a floor, and that
the floor is what the quantity means, is precise about the measurement before its
formula appears.

> "One useful way to think about this is that every codeword requires a sacrifice from the space of possible codewords. If we take the codeword 01, we lose the ability to use any codewords it's a prefix of. We can't use 010 or 011010110 anymore because of ambiguity – they're lost to us."

Olah explains a constraint as a cost you pay: take one short codeword and you give
up others, shown with real strings a reader can read off. Attaching a concrete
price to each choice is how he makes an abstract rule something the reader can
hold onto.
