# Voice guide: The Evidence — Denoising Diffusion Probabilistic Models

## How this piece should sound

This lesson has one paper to open, the 2020 "Denoising Diffusion Probabilistic
Models" paper, for a reader who has never trained a model but reads widely and
will notice if a claim is padded. The job is close to what Chris Olah does in
"Understanding LSTM Networks": build one unfamiliar mechanism, in order, for a
reader who has nothing to fall back on but what the essay just told them. Olah
never explains the forget gate before he has told the reader what a cell state
is, and he never names a gate before showing what it does. The forward and
reverse process in DDPM ask for the same discipline: state what noise is being
added or removed before naming the step that does it, and never let the word
"diffusion" carry weight the piece hasn't built yet.

Olah's opening move, grounding a technical need in something the reader already
does (a sentence understood in light of the one before it, before "recurrent" is
ever said) is available for this piece's own opening: the reader already knows
what a blurred photo looks like, or what happens to an audio signal buried in
static, before the paper's noising process has a name. Use that kind of run-up
once, at the point where the mechanism first needs it, not as a device to
resell later.

Where the piece has to render an equation or a schedule in prose, Andrej
Karpathy's move is the one to borrow: show the real thing, not a gesture at it.
Karpathy doesn't tell his reader that RNN-generated code "resembles" C; he shows
a snippet and then says plainly where it breaks, down to the exact undefined
variable. This paper has real numbers to offer in the same way, its number of
diffusion steps, its noise schedule, the specific benchmarks and scores it
reports, and the piece should reach for those over a paraphrase every time one
is available. Where the paper reports a strong result, name the figure the way
Karpathy names the variable that broke, specifically, not as a general
assessment. Where the 2020 paper's own tradeoffs sit (sample quality against
log-likelihood, for instance, is exactly this kind of mixed result), report
both sides with the same plainness, not a hedge that blurs them together.

The piece also has a second job past explaining the mechanism: correcting what
"diffusion model" has come to mean in the years since, against what the 2020
paper actually built and measured. Simon Willison's habit of marking the edge of
his own knowledge, "why this happens is an intriguing puzzle," "it looks
likely," "the best theory I've seen so far", is the register for that
correction. State what the paper showed as fact. State what later work added,
confirmed, or changed as exactly that, not as if it had always been part of the
original result. Where today's usage of "diffusion model" reaches past what
this paper demonstrated, say so as plainly as Willison says a glitch token's
cause is still a working theory, not a settled one.

This piece will meet more unfamiliar terms in one sitting than most lessons in
the course do, since the paper introduces several ideas at once: Gaussian
noise, a Markov chain, a variational bound, a U-Net. Decide, before drafting,
which of those the reverse-process explanation actually depends on, and build
only those in, the way Olah builds the LSTM's four gates one at a time and
never all at once. A term the walkthrough can survive without is one the
reader can survive without meeting.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read
> this essay, you understand each word based on your understanding of previous
> words. You don't throw everything away and start thinking from scratch
> again. Your thoughts have persistence."

This is the first paragraph of the essay, and it never says "recurrent neural
network." It states something the reader already knows about their own mind,
and only the next paragraph turns that into the gap a traditional network has.
The technical need arrives second, once the reader already feels why it
matters.

> "The cell state is kind of like a conveyor belt. It runs straight down the
> entire chain, with only some minor linear interactions. It's very easy for
> information to just flow along it unchanged." [...] "Gates are a way to
> optionally let information through. They are composed out of a sigmoid
> neural net layer and a pointwise multiplication operation. The sigmoid layer
> outputs numbers between zero and one, describing how much of each component
> should be let through. A value of zero means 'let nothing through,' while a
> value of one means 'let everything through!'"

Two mechanisms land back to back here, the cell state and the gate, and each
gets exactly one plain-language anchor: a conveyor belt for the first, "let
nothing through" and "let everything through" for the second. Olah doesn't
define "sigmoid" before he needs it and doesn't return to redefine the
conveyor belt once it's set. The reader is never asked to hold a term before
it has done anything.

> "Written down as a set of equations, LSTMs look pretty intimidating.
> Hopefully, walking through them step by step in this essay has made them a
> bit more approachable."

The essay's own closing admission: the underlying math is genuinely hard to
read cold, and the walkthrough exists because of that, not despite it. Nothing
larger is claimed for the essay than getting the reader from "intimidating" to
"a bit more approachable."

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "There's something magical about Recurrent Neural Networks (RNNs). I still
> remember when I trained my first recurrent network for Image Captioning.
> Within a few dozen minutes of training my first baby model (with rather
> arbitrarily-chosen hyperparameters) started to generate very nice looking
> descriptions of images that were on the edge of making sense. Sometimes the
> ratio of how simple your model is to the quality of the results you get out
> of it blows past your expectations, and this was one of those times."

The claim of surprise is grounded in a specific, checkable detail, a few dozen
minutes, a first model, arbitrary hyperparameters, before the essay allows
itself the word "magical." The excitement is earned by the particulars sitting
right next to it, not asserted on its own.

> "The code looks really quite great overall. Of course, I don't think it
> compiles but when you scroll through the generate code it feels very much
> like a giant C code base. [...] A common error is that it can't keep track
> of variable names: It often uses undefined variables (e.g. rw above),
> declares variables it never uses (e.g. int error), or returns non-existing
> variables."

Karpathy names what worked and then names exactly what failed, down to the
specific undefined variable, in the same paragraph and at the same level of
detail. Neither side is softened to protect the other. The failure is reported
with a real example, not summarized as "occasional mistakes."

> "Again, what is beautiful about this is that we didn't have to hardcode at
> any point that if you're trying to predict the next character it might, for
> example, be useful to keep track of whether or not you are currently inside
> or outside of quote. We just trained the LSTM on raw data and it decided
> that this is a useful quantitity to keep track of. In other words one of its
> cells gradually tuned itself during training to become a quote detection
> cell, since this helps it better perform the final task."

The observation here is precise about what happened (one cell, trained on raw
data, ended up tracking quote state) rather than reaching for a grander claim
about what it means. The finding is left to be exactly the size it is.

## Simon Willison, "Understanding GPT tokenizers"

Source: https://simonwillison.net/2023/Jun/8/gpt-tokenizers/

> "Large language models such as GPT-3/4, LLaMA and PaLM work in terms of
> tokens. They take text, convert it into tokens (integers), then predict
> which tokens should come next. Playing around with these tokens is an
> interesting way to get a better idea for how this stuff actually works
> under the hood."

Four short sentences state the entire mechanism before any example arrives.
Nothing here is hedged or dressed up; each sentence does one piece of work and
stops.

> "The English bias is obvious here. ' man' gets a lower token ID of 582,
> because it's an English word. 'zan' gets a token ID of 15201 because it's
> not a word that stands alone in English, but is a common enough sequence of
> characters that it still warrants its own token."

The claim ("English bias") is made and then immediately paid for with the
actual token IDs behind it, not a general description of tokenization
inefficiency. A reader can check 582 and 15201 against the notebook the post
links; nothing here asks to be taken on faith.

> "Why this happens is an intriguing puzzle. It looks likely that this token
> refers to user davidjl123 on Reddit, a keen member of the /r/counting
> subreddit. He's posted incremented numbers there well over 163,000 times.
> Presumably that subreddit ended up in the training data used to create the
> tokenizer used by GPT-2, and since that particular username showed up
> hundreds of thousands of times it ended up getting its own token."

Every claim in this passage is marked for how sure it is: "intriguing puzzle,"
"looks likely," "presumably." Willison isn't refusing to explain the glitch
token, he's explaining it while being exact about which parts are established
and which are his best read of the evidence.
