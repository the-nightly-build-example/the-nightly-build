# Voice guide: the-evidence/wavenet

## How this piece should sound

This lesson explains what one document actually measured to a reader who has
probably met "WaveNet" only as shorthand for solved speech synthesis, never as
a number attached to a specific test. The register that fits is a teacher who
has read the paper closely and wants to show the reader exactly what it
established. Plain declaratives, real figures, and enough respect for the
reader to state a finding before building the case under it.

Monty Montgomery opens "24/192 Music Downloads are Very Silly Indeed" by
stating his conclusion in the first two sentences, before any of the
physiology that defends it. This lesson's own opening move, what the MOS
comparison actually measured and what it left out, can work the same way. Say
what the score was and what it excluded in the opening sentences, then spend
the paragraphs after earning it.

Where the lesson has to define a boundary, what a "raw audio sample" is, what
a dilated causal convolution reaches back to, what real-time synthesis
requires, Montgomery's habit of pinning a limit to the exact point where two
measured things meet (the hearing curve crossing the pain curve) is more
useful than a qualifier like "very high" or "quite slow." The paper and its
follow-ups supply real numbers for most of these, so the boundary can be
stated as an exact figure, per the house standard on numbers.

The autoregressive mechanism, one sample predicted from the ones before it,
is a case built for a Karpathy-style worked example: a tiny, made-up sequence
worked by hand before the piece scales to the paper's actual sample rate.
Karpathy grounds the whole idea of a character-level model in "hello" before
he ever shows Shakespeare. This lesson has the same shape available, a
two-or-three-sample toy case before the jump to thousands of samples a
second, if a small hand-worked case would make the mechanism concrete faster
than a general description of it.

Once dilated causal convolution is on the page, Olah's move of pairing a
structural fact with its plain-language paraphrase in the same breath, a
number and then what the number means in one clause, is the model for
keeping the mechanism legible without softening the vocabulary. The paper's
own terms (receptive field, stack of dilations, μ-law encoding) can stay
exact as long as each one gets that same one-clause unpacking at first use.

Both Karpathy and Olah write in direct address, "you," "let's," because their
form allows the writer to stand next to the reader. The lesson template
reserves that address for the two bookend cards and has the body speak to no
one, so the address itself has to stay out of the body. What can carry over
is the confidence underneath it. Olah's flat claim that long-term memory is
"practically their default behavior, not something they struggle to learn"
is a model for stating plainly what a mechanism does, once the evidence for
it is already on the page. The paper's honest limits, the generation speed
and the gap to a natural recording, call for the same directness: give the
figure and let it carry the weight, per the house standard on numbers.

The present-tense turn, what later work did to the original method, has its
model in Montgomery's Nyquist paragraph: a plain corrective sentence that
carries its own mechanism alongside the correction itself. When this lesson
says where the 2016 architecture stands against how "WaveNet" gets invoked
now, the correction can lean on the same shape. State what changed and why
in the same move.

## Monty Montgomery, "24/192 Music Downloads are Very Silly Indeed"

Source: https://people.xiph.org/~xiphmont/demo/neil-young.html

> "Unfortunately, there is no point to distributing music in 24-bit/192kHz
> format. Its playback fidelity is slightly inferior to 16/44.1 or 16/48, and
> it takes up 6 times the space."

This is the piece's whole argument, given away in the second sentence, before
a single supporting fact has appeared. The number (6 times the space) and the
comparison (16/44.1) are both concrete enough for a reader to go check for
themselves. That is where Montgomery's engineering background shows on the
page.

> "The upper limit of the human audio range is defined to be where the
> absolute threshold of hearing curve crosses the threshold of pain. To even
> faintly perceive the audio at that point (or beyond), it must
> simultaneously be unbearably loud."

Montgomery defines the edge of hearing as the exact point where two
independently measured curves intersect, then states the strange consequence
of standing at that edge: to hear it at all, it has to already hurt. The
precision is the personality here, a definition specific enough that a
reader could go find the two curves and check where they cross.

> "All signals with content entirely below the Nyquist frequency (half the
> sampling rate) are captured perfectly and completely by sampling; an
> infinite sampling rate is not required. Sampling doesn't affect frequency
> response or phase. The analog signal can be reconstructed losslessly,
> smoothly, and with the exact timing of the original analog signal."

This corrects the popular belief that sampling is inherently a rough
approximation, and it does that without the phrase "contrary to popular
belief" anywhere in it. Montgomery just states the actual mechanism, lossless,
exact timing, no effect on phase, at full confidence. Nothing here is hedged,
because he has already done the work earlier in the piece to be sure of it.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: http://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still
> remember when I trained my first recurrent network for Image Captioning.
> Within a few dozen minutes of training my first baby model (with rather
> arbitrarily-chosen hyperparameters) started to generate very nice looking
> descriptions of images that were on the edge of making sense."

Karpathy earns the word "magical" by immediately anchoring it to a specific,
checkable detail: a few dozen minutes, an arbitrarily-chosen setup, a result
better than the setup deserved. The claim of surprise is tied to a number and
a timeframe a reader could picture happening on their own machine, not left
to float on its own.

> "If training vanilla neural nets is optimization over functions, training
> recurrent nets is optimization over programs."

One sentence carries the entire distinction between two kinds of models. It
works because Karpathy has already spent several paragraphs establishing both
halves of the comparison before he compresses them into a single line. The
reader already has both terms loaded by the time the sentence lands.

> "As a working example, suppose we only had a vocabulary of four possible
> letters "helo", and wanted to train an RNN on the training sequence
> "hello". This training sequence is in fact a source of 4 separate training
> examples: 1. The probability of "e" should be likely given the context of
> "h", 2. "l" should be likely in the context of "he", 3. "l" should also be
> likely given the context of "hel", and finally 4. "o" should be likely
> given the context of "hell"."

Before showing a single result, Karpathy shrinks the entire mechanism down to
four letters and walks through what the model sees at each step. The four
training examples are named individually, one by one, which is what lets a
reader check the mechanism by hand.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Gates are a way to optionally let information through. They are composed
> out of a sigmoid neural net layer and a pointwise multiplication operation.
> The sigmoid layer outputs numbers between zero and one, describing how much
> of each component should be let through. A value of zero means "let nothing
> through," while a value of one means "let everything through!""

Olah gives the structural fact (a sigmoid layer, a multiplication) and its
plain-language meaning (zero blocks, one lets through) in the same short
space, so the reader never has to hold the mechanism unexplained for more
than a sentence. The exclamation point at the end is the one place personality
shows through a very dry mechanism, a small, controlled break in an
otherwise flat register.

> "Let's go back to our example of a language model trying to predict the
> next word based on all the previous ones. In such a problem, the cell state
> might include the gender of the present subject, so that the correct
> pronouns can be used. When we see a new subject, we want to forget the
> gender of the old subject."

Olah returns to the same worked example, a language model tracking a
subject's gender, every time he introduces a new gate. Reusing one case
across several mechanisms is what lets the reader watch the same concrete
thing pass through forget, input, and output in turn.

> "LSTMs are explicitly designed to avoid the long-term dependency problem.
> Remembering information for long periods of time is practically their
> default behavior, not something they struggle to learn!"

This is a strong claim stated without qualification, and it earns that
confidence because the surrounding paragraphs already showed why plain RNNs
fail at the same task. Olah is visible in the exclamation point, a plain
writer allowing himself one moment of enthusiasm once the technical case is
already made.
