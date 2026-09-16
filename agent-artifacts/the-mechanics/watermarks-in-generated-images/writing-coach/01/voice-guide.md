## How this piece should sound

This lesson works backward from one behavior — the ghost watermark smeared
across a generated image — through the training data, to two mechanisms
underneath it, and it has to keep saying honestly which of those steps is
settled and which is still open. That is the exact move Timothy Lee and Sean
Trott make in the passage below: two short sentences that state plainly what
nobody yet understands, right before the sentence that says what is
understood, with no hedge stretched across the whole paragraph. This piece
needs that same clean cut at its own hardest step, where a learned watermark
and a memorized training image are both real and only "which one produced
this particular output" stays open. Say which is which in a sentence or two,
not a paragraph of qualification.

Each step up the chain — watermark, training set, training objective,
memorization — is a real mechanism, and the piece has real cases ready for
each one: a stock-photo mark co-occurring with a whole class of training
images, an extracted training image from the memorization literature, the
litigation exhibit itself. Olah's paragraph on predicting "sky" after "the
clouds are in the" commits to one specific sentence before it generalizes to
"in such cases." Reach for one of this piece's own cases the same way, before
the general claim about distributional learning or about memorization, not
after it as decoration.

Where a mechanism is abstract enough to need a comparison, this piece can
use one the way Olah's conveyor belt carries an entire paragraph about the
cell state, or the way Lee and Trott's faucets-and-squirrels analogy makes
backpropagation picturable instead of asserted. A distribution learned
across millions of watermarked photos, or a training pass nudging weights
toward reproducing a mark, is the kind of mechanism one physical image can
carry for a paragraph or two — stated once, then reused, rather than three
different partial comparisons competing for the same idea.

Where the field's own term is the right word — distributional learning,
memorization, deduplication, the training objective — keep it and define it
in place, the way Evans keeps "Gram matrix" and says exactly what operation
produces it instead of softening it into "some math." A reader who has never
trained a model still needs the term that will let them recognize the next
piece of AI coverage that uses it loosely.

The lesson template keeps the body from addressing the reader directly; that
belongs to the two bookends alone. Evans's "I still don't completely
understand this inner product thing" is a first-person aside that this piece
can't borrow directly, but the honesty behind it can survive in the body's
own voice: naming, in plain declarative sentences, exactly which claim in the
chain is established and which one is an open question even for people who
build these systems, rather than either overclaiming certainty or hedging
everything equally.

This is a short chain with five named steps, not a survey of everything
known about diffusion models and watermarks. Let one or two worked cases per
step do the work, the way each of the passages below stays inside a single
example before moving on, and give the space that frees up to explaining the
mechanism itself rather than piling on more instances of it.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "As a result, no one on Earth fully understands the inner workings of
> LLMs. Researchers are working to gain a better understanding, but this is
> a slow process that will take years—perhaps decades—to complete."

This sits right before the paragraph that says what experts do understand,
so the reader gets the honest limit and the promise of what follows in
back-to-back sentences. Neither sentence hedges the other; the first states
the limit flatly, the second states the scope of what's coming, and the
piece moves on.

> "This is useful for reasoning about spatial relationships. You can tell
> New York is close to Washington DC because 38.9 is close to 40.7 and 77 is
> close to 74. By the same token, Paris is close to London. But Paris is far
> from Washington DC."

The comparison uses coordinates the writers had already put on the page two
sentences earlier, not a fresh example invented to illustrate the point. The
reader checks the claim against numbers already in front of them instead of
taking the analogy on faith.

> "Second, there's a maze of interconnected pipes behind the faucets, and
> these pipes have a bunch of valves on them as well. So if water comes out
> of the wrong faucet, you don't just adjust the knob at the faucet. You
> dispatch an army of intelligent squirrels to trace each pipe backwards and
> adjust each valve they find along the way."

The image is deliberately silly — an army of squirrels — and the writers
let it stay silly rather than smoothing it into something more dignified. It
does the job of making backpropagation something a reader can picture,
where a correct but abstract description of gradient updates would not.

## Julia Evans, "How do these 'neural network style transfer' tools work?"

Source: https://jvns.ca/blog/2017/02/12/neural-style/

> "When we put an image into the network, it starts out as a vector of
> numbers (the red/green/blue values for each pixel). At each layer of the
> network we get another intermediate vector of numbers. There's no
> inherent meaning to any of these vectors."

Three short sentences, each building directly on the one before it, and the
qualifying claim — that the numbers have no inherent meaning — is stated on
its own rather than buried in a subordinate clause. Nothing here decorates;
every sentence is doing definitional work the next paragraph depends on.

> "Defining 'style' is a bit more complicated. If I understand correctly,
> the definition 'style' is actually the major innovation of this paper –
> they don't just pick a layer and say 'this is the style layer'. Instead,
> they take all the 'feature maps' at a layer (basically there are actually
> a whole bunch of vectors at the layer, one for each 'feature'), and define
> the 'Gram matrix' of all the pairwise inner products between those
> vectors. This Gram matrix is the style."

She keeps the paper's own term, "Gram matrix," instead of reaching for a
friendlier synonym, and says exactly what operation produces it — pairwise
inner products of feature maps — rather than gesturing at "some math." The
precision is where her authority is visible, not the enthusiasm around it.

> "I still don't completely understand this inner product thing. Someone
> tried to explain this to me on twitter a bit but I still don't really get
> it."

She names the specific thing she doesn't understand, in the middle of an
otherwise confident explanation, instead of smoothing over the gap or
avoiding the topic. The parts she does explain read as more trustworthy
because of the part she flags as unclear.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "Humans don't start their thinking from scratch every second. As you read
> this essay, you understand each word based on your understanding of
> previous words. You don't throw everything away and start thinking from
> scratch again. Your thoughts have persistence."

The essay's opening move is a claim about the reader's own mind, checkable
without any technical background, before a single term of art appears. The
abstraction the essay is about to name — memory carried across a sequence —
only shows up once the concrete case has made obvious what it refers to.

> "Sometimes, we only need to look at recent information to perform the
> present task. For example, consider a language model trying to predict
> the next word based on the previous ones. If we are trying to predict the
> last word in 'the clouds are in the sky,' we don't need any further
> context – it's pretty obvious the next word is going to be sky."

The example commits to one specific sentence and one specific predicted word
before the essay generalizes to "such cases." The general claim, when it
comes in the next sentence, only has to point back at something the reader
already worked out themselves.

> "The cell state is kind of like a conveyor belt. It runs straight down the
> entire chain, with only some minor linear interactions. It's very easy for
> information to just flow along it unchanged."

One physical image — a conveyor belt — carries the whole paragraph, and
every sentence after it stays inside that image instead of switching to a
new comparison. The plainness of the comparison, not a technical
description of the mechanism, is what makes an otherwise abstract piece of
architecture feel concrete.
