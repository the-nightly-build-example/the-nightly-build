# Voice guide: the-evidence/long-short-term-memory (01)

Domain and genre: reading one old machine-learning paper, the 1997 Long
Short-Term Memory paper, and telling a smart non-specialist what it actually
says and how small its experiments were. The exemplars below are writers the
field rates for explaining hard technical material in plain, exact prose. Each
passage was retrieved from the raw page and checked word for word. Quote
characters and line-wrap spacing were normalized; words, word order and the
punctuation inside each sentence match the source.

## How this piece should sound

This lesson reads the 1997 LSTM paper and tells the reader what is in it. The
reader is quick and reads widely but has never traced a gradient through a
recurrent network, and keeps meeting claims about LSTM they cannot check. Write
to be understood by that reader, the way Nielsen writes about handwriting
recognition: the constant error carousel and the gate units can be carried in
plain sentences without the sentences going vague to stay easy. When a term like
the constant error carousel has to enter, it can be deflated the way Nielsen
deflates "hidden." Say what it does and drop the aura, so the exact term stays
and only the mystery around it goes.

The evidence in the paper is small: synthetic sequence tasks run on tiny
networks. Nielsen's MNIST description and Luu's measurement writing show one way
to be honest about that without editorializing. Give the reader the composition
and the counts, how many memory cells, how long the sequences, how many tasks,
and let the size register on its own, instead of reaching for a word like
"limited" or "impressive." Where the writer's own reading enters, it can be
marked the way Luu marks "by my standards," so the reader can tell which claims
come from the paper's numbers and which are the writer weighing them.

The gap between what the 1997 model demonstrated and the LSTM people invoke today
is the lesson's own find, and the writer reaches it from the evidence. Luu's
refusal to accept a reputation without the measurement behind it suits a paper
whose reputation now runs well ahead of its synthetic experiments. Where today's
citations claim more than those tasks showed, the piece can say so in a flat
sentence and let the gap stand, as Luu states that most published measurements
are not very good and moves straight to what follows from it.

The direct, spoken register in Evans's "what, that was it????" fits the lesson's
opening and closing cards rather than the walk-through: a reader who has been
told LSTM is hard can be shown there how small the protected-value idea is once
it is laid out. Evans's line between clear and dumbed-down applies to the gate
units and to the forget gate that was added after 1997. Keep the real mechanism
and the real terms and improve only how they are arranged, rather than trading
the mechanism for a picture of it.

## Michael Nielsen, "Neural Networks and Deep Learning," Chapter 1

Source: http://neuralnetworksanddeeplearning.com/chap1.html

> "Most people effortlessly recognize those digits as 504192. That ease is deceptive. In each hemisphere of our brain, humans have a primary visual cortex, also known as V1, containing 140 million neurons, with tens of billions of connections between them."

Checked: http://neuralnetworksanddeeplearning.com/chap1.html, retrieved 2026-09-22
Nielsen makes difficulty felt by handing the reader a number to hold, 140 million
neurons in one visual area and tens of billions of connections, instead of
calling the visual system complex. "That ease is deceptive" is his own read of
something everyone does without thinking, and he states it flatly rather than
selling it. The person shows in that plain verdict placed next to the figures.

> "The term "hidden" perhaps sounds a little mysterious - the first time I heard the term I thought it must have some deep philosophical or mathematical significance - but it really means nothing more than "not an input or an output"."

Checked: http://neuralnetworksanddeeplearning.com/chap1.html, retrieved 2026-09-22
Nielsen takes a term a beginner finds forbidding and tells the reader it means
nothing more than "not an input or an output." He reaches the reader by owning
his own first reaction, that he thought "hidden" carried some deep significance,
before letting the air out of it. The technical word stays in place; only the
aura around it is removed.

> "The first part contains 60,000 images to be used as training data. These images are scanned handwriting samples from 250 people, half of whom were US Census Bureau employees, and half of whom were high school students. The images are greyscale and 28 by 28 pixels in size."

Checked: http://neuralnetworksanddeeplearning.com/chap1.html, retrieved 2026-09-22
Nielsen reports the exact makeup of the data he is about to rely on: 60,000
training images, 28 by 28 pixels, from 250 people split between census workers
and high-school students. He gives the composition rather than an adjective like
"large," so the reader can judge how much the later accuracy figures rest on. The
plain listing is the writer trusting the reader with the real counts.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "My go-to example for this is Kyle Kingsbury's work with Jepsen. Before Jepsen, a handful of huge companies (the now $1T+ companies that people are calling "hyperscalers") had decently tested distributed systems. They mostly didn't talk about testing methods in a way that really caused the knowledge to spread to the broader industry. Outside of those companies, most distributed systems were, by my standards, not particularly well tested."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
Luu backs a broad claim about the state of tested software with one named case,
Kyle Kingsbury's Jepsen, instead of leaving the claim general. He flags his own
judgment where it is a judgment, "by my standards, not particularly well tested,"
so the reader knows which part is his call. The specific name and the marked
opinion are both the writer refusing to hide behind "it is widely known."

> "The typical response that I've seen when a catastrophic bug is reported is that the project maintainers will assume that the bug report is incorrect (and you can see many examples of this if you look at responses from the first few years of Kyle's work). When the reporter doesn't have a repro for the bug, which is quite common when it comes to distributed systems, the bug will be written off as non-existent."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
Luu describes a pattern he has watched many times by walking through its steps in
order: the report is assumed wrong, then, with no reproduction, written off as
non-existent. He states what happens without naming it a syndrome or dressing it
up, and the ordered steps carry the point. "That I've seen" keeps it his own
observation and not a stated law.

> "One thing that both increases and decreases the impact of doing good measurements is that most measurements that are published aren't very good. This increases the personal value of understanding how to do good measurements and of doing good measurements, but it blunts the impact on other people, since people generally don't understand what makes measurements invalid and don't have a good algorithm for deciding which measurements to trust."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
Luu states plainly that most published measurements are not very good, then says
what follows from it for a reader trying to decide which ones to trust. He does
not soften the claim, and he explains the consequence in the same flat register.
The work is in the reasoning set out step by step, and the writer is visible in
choosing to reason it out rather than assert it.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "For example, take DNS. We've been using DNS since the 80s (for more than 35 years!). It's used in every website on the internet."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
Evans sets the stakes for a technology with facts a reader can check: in use
since the 80s, more than 35 years, on every website. She states each one and
claims no importance for it beyond what it is. She is present in the choice to
lead with how old and ordinary the thing is.

> "When I finally learned how to troubleshoot DNS problems, my reaction was "what, that was it???? that's not that hard!". I felt a little bit cheated!"

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
Evans lets the reader hear her own reaction on first solving the problem, "what,
that was it????", and then "I felt a little bit cheated." The voice is a person
talking, and it earns trust by admitting the thing had looked mysterious to her
too. This first-person, direct-to-the-reader register belongs in a lesson's
opening and closing cards, not the walk-through, which addresses no one.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
Evans draws the line between clear and simplified: the clearer version is not
dumbed down, it is the exact same information with the presentation improved. She
wants everything shown and only the arrangement changed. The insistence on
keeping all the information is hers, stated in her own plain words.
