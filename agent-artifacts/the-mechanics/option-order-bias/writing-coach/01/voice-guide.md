# Voice guide: option-order bias (The Mechanics)

## How this piece should sound

This lesson takes one behavior the reader may have run into, a model changing
which option it picks when the same options are listed in a different order, and
works back down to what produces it. The reader is quick and reads widely but
has never seen the inside of a transformer, so every part named on the way down
has to be built in plain words the first time it appears. Karpathy's four-letter
example is the model for how to open a step: reach for the smallest concrete
case that shows it, and let that case do the explaining while the sentences
around it stay short.

Option-order bias has more than one contributing cause. Among them: the options
arrive as one sequence of tokens, the model holds priors over the label tokens
themselves, position in the sequence carries its own effect, and how the answer
is scored shapes the choice. The failure this piece is most exposed to is naming
one of those and letting it account for the whole bias. Hold each part to the
standard of Olah's forget-gate paragraph: name it, say what it takes in and
gives back, and put its behavior in plain terms in the sentence that introduces
it, before the next step leans on it. When two causes could each explain the
same shift, Evans reading the two DNS responses shows what to do instead: say
what the observation does show and what it does not, and correct the wrong
reading before the reader adopts it.

Some steps here are settled engineering and some are open even to the people who
build these models, and the reader should finish able to tell which is which.
Karpathy's "likely due to" and his "is likely done with a different neuron" mark
a claim as inference without abandoning it, and Olah answers "which variant is
best?" only as far as named studies reach. Where the cause of a particular
reordering effect is genuinely unsettled, or where one case cannot be pinned to
a single contributing factor, that is the register the passage should hold:
state what is known, attribute it, and say plainly where certainty ends. State
an inference as an inference, and mark the point past which even the people who
build these models do not have an answer.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "As a working example, suppose we only had a vocabulary of four possible
> letters "helo", and wanted to train an RNN on the training sequence "hello".
> This training sequence is in fact a source of 4 separate training examples: 1.
> The probability of "e" should be likely given the context of "h", 2. "l"
> should be likely in the context of "he", 3. "l" should also be likely given
> the context of "hel", and finally 4. "o" should be likely given the context of
> "hell"."

Karpathy shrinks the problem to four letters and one short word before he
explains anything general, so the reader follows the process on a case small
enough to hold in mind. He then splits the single string "hello" into four
numbered predictions and states each one, which shows the step happening rather
than reporting that it happened. The example does the work while the sentences
around it stay plain and short.

> "This is an example of a problem we'd have to fix manually, and is likely due
> to the fact that the dependency is too long-term: By the time the model is
> done with the proof it has forgotten whether it was doing a proof or a lemma."

He begins from a specific mistake the reader has just seen, an environment opened
as a proof and closed as a lemma, and reasons back to a cause put in ordinary
words. "Likely due to" marks the explanation as his inference and not a settled
fact. The clause after the colon says what the model forgot and when, so the
cause is something the reader can picture and check.

> "The highlighted neuron here gets very excited when the RNN is inside the [[ ]]
> markdown environment and turns off outside of it. Interestingly, the neuron
> can't turn on right after it sees the character "[", it must wait for the
> second "[" and then activate. This task of counting whether the model has seen
> one or two "[" is likely done with a different neuron."

Karpathy reports exactly what the neuron does, then draws one inference from it
and stops. The detail that it waits for the second bracket before activating is
specific enough to check, and that is what makes the looser claim beside it
credible. "Is likely done with a different neuron" leaves an open question open
instead of filling it.

## Christopher Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "This decision is made by a sigmoid layer called the "forget gate layer." It
> looks at h_{t-1} and x_t, and outputs a number between 0 and 1 for each number
> in the cell state C_{t-1}. A 1 represents "completely keep this" while a 0
> represents "completely get rid of this.""

Olah names the part, says what it takes in and what it puts out, then translates
its two extreme values into plain English before he moves on. The reader learns
what a component does in the sentence that first uses it. Nothing is referred to
by a term he has not already defined.

> "Which of these variants is best? Do the differences matter? Greff, et al.
> (2015) do a nice comparison of popular variants, finding that they're all about
> the same. Jozefowicz, et al. (2015) tested more than ten thousand RNN
> architectures, finding some that worked better than LSTMs on certain tasks."

Olah asks the question the reader is starting to form and answers it only as far
as named studies let him. He ties each finding to who found it and how much they
tested, so the reader can weigh it. The honest answer is "about the same, with
exceptions," and he gives that rather than a cleaner claim the evidence would not
support.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "Here you can see we got a normal NOERROR response for google.com (which is in
> 8.8.8.8's cache) but a SERVFAIL for homestarrunner.com (which isn't). This
> doesn't mean there's no DNS record homestarrunner.com (there is!), it's just
> not cached)."

Evans reads a real command's output and says what the difference between the two
responses does and does not mean. The correction in the middle heads off the
wrong conclusion a reader would otherwise draw, that the SERVFAIL means the
domain has no record at all. She is exact about the limits of what one
observation shows.

> "Here I've requested a nonexistent domain, and I got the extended error EDE: 12
> (NSEC Missing): (Invalid denial of existence of xjwudh.com/a). I'm not sure
> what that means (it's some DNSSEC Thing), but it's cool to see an extra debug
> message like that."

Evans reaches the edge of what she knows and says so in the same plain voice she
uses for everything else. Admitting "I'm not sure what that means" costs her
nothing with the reader and keeps her from inventing an explanation. The
admission is specific: she names the exact error she cannot fully account for.
