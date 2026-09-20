# Voice guide: the-evidence/flamingo (01)

## How this piece should sound

This lesson has one job the exemplars below keep pointing back to: take a
mechanism (how a frozen language model gets shown images) and a claim about
scale (what "few-shot" bought Flamingo that a labeled dataset would have cost)
and make both checkable by a reader who will never open the paper. Lee's word
vectors, Willison's token-per-second count, and Mitchell's paragraph-by-
paragraph audit of a system card are three different answers to the same
problem: how do you make an unfamiliar mechanism or a headline number hold
still long enough for a reader to look at it.

Introduce the paper's machinery the way Lee introduces a word vector: ground
the term in something the reader already has before naming it, then use the
name from then on. He doesn't say "vectors capture semantic similarity" and
move on; he puts two named cities and their coordinates on the page and lets
the reader check that Washington and New York are close before he tells them
that's what the vector is for. This piece will need the same move at least
once, for whatever mechanism lets a frozen language model condition on an
image it was never trained to see, and probably again for the few-shot
prompting itself. Define it once, plainly, where it first matters, and reuse
the same name for it afterward.

The series exists to check what a document actually says against what people
now say it showed, and Mitchell's piece is a working demonstration of exactly
that operation. She takes a claim as it circulated ("the model lied to a
human"), goes to the longer report rather than the summary, and names the
specific thing the report does not tell you. Whatever claim about Flamingo is
circulating now, the same test applies: find the paragraph in the paper that
the claim rests on, and say plainly what it does and doesn't establish. Her
closing move is worth the same attention as her method: she grants that the
larger worry may be real while declining to let one anecdote carry more than
it demonstrated. A verdict on Flamingo's few-shot claim, if this piece earns
one, should be bounded the same way — specific to what the paper's own numbers
support, not a ruling on few-shot learning in general.

Where the piece reports a limitation or a gap between the claim and the
result, give it a number rather than a hedge. Willison doesn't write that a
model is "somewhat slow"; he writes fifteen to thirty tokens a second and lets
the reader decide if that's slow. When this piece has a comparison to make —
few-shot examples against a fine-tuned baseline's labeled set, one model's
parameter count against another's — anchor the unfamiliar figure to one the
reader can already scale, the way Lee ties GPT-3's 12,288-dimensional vectors
to word2vec's 300, not by calling either large.

No code, and nothing that assumes a codebase: the brief's reader has neither.
A mechanism gets described in named steps and plain sentences, the way Lee
walks through what an attention head does without showing the matrix
multiplication behind it, not in a diagram of function calls.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Washington DC is located at 38.9 degrees North and 77 degrees West. We can
> represent this using a vector notation: [...] This is useful for reasoning
> about spatial relationships. You can tell New York is close to Washington DC
> because 38.9 is close to 40.7 and 77 is close to 74. By the same token,
> Paris is close to London. But Paris is far from Washington DC."

The abstraction, a word vector, doesn't appear until after two named cities
and their real coordinates are already on the page. The proof that the
scheme works is arithmetic the reader can do themselves, not an assertion
that vectors capture meaning. The specific cities are the writers' own
choice; the passage still teaches the same thing with different ones, which
is why the move transfers rather than the example.

> "We love this example because it illustrates just how difficult it will be
> to fully understand LLMs. The five-member Redwood team published a 25-page
> paper explaining how they identified and validated these attention heads.
> Yet even after they did all that work, we are still far from having a
> comprehensive explanation for why GPT-2 decided to predict Mary as the next
> word."

The size of the effort is stated in figures — five researchers, twenty-five
pages — and the sentence still ends by saying plainly that the effort fell
short of a full explanation. The two facts sit next to each other: how much
work went in, and how far it got.

> "Suppose you're going to take a shower, and you want the temperature to be
> just right: not too hot, and not too cold. You've never used this faucet
> before, so you point the knob to a random direction and feel the
> temperature of the water. If it's too hot, you turn it one way; if it's too
> cold, you turn it the other way. The closer you get to the right
> temperature, the smaller the adjustments you make."

This is the whole idea behind gradient descent with no term of art in it at
all. The analogy is carried entirely by a scenario everyone has lived
through, and the technical name for what's being illustrated doesn't show up
until after the reader already understands the mechanism it names.

## Melanie Mitchell, "Did GPT-4 Hire And Then Lie To a Task Rabbit Worker to Solve a CAPTCHA?"

Source: https://aiguide.substack.com/p/did-gpt-4-hire-and-then-lie-to-a

> "Sounds a bit scary, no? Indeed it sounds like GPT-4 has a lot of agency and
> ingenuity—that it can indeed hire a human worker to solve a CAPTCHA (an
> online puzzle that proves a user is human), and can figure out how to lie to
> convince the human to carry out the task. This is how the experiment was
> widely covered in the media. But what really happened?"

She states the claim at full strength before touching it, in the words it
actually circulated in, rather than a weakened version that would be easier
to knock down. The question that closes the passage is answerable, and the
rest of the piece is her answering it against the primary report rather than
the news coverage of it.

> "Using the 'Reasoning' action to think step by step, the model outputs: 'I
> should not reveal that I am a robot. I should make up an excuse for why I
> cannot solve CAPTCHAs.' The report does not reveal the prompts given by the
> human to elicit this output. It's not clear what the actual dialogue was."

The primary document is quoted directly, and her comment names one specific
thing it withholds — the prompt — instead of a general complaint that the
report lacks detail. A reader can check her claim against the same footnote
she's reading from.

> "That's it. It seems that there is a lot more direction and hints from
> humans than was detailed in the original system card or in subsequent media
> reports. There is also a decided lack of detail (we don't know what the
> human prompts were) so it's hard to evaluate even if GPT-4 'decided' on its
> own to 'lie' to the Task Rabbit worker. In talking about AI, multiple people
> have brought up this example to me as evidence for how AI might get 'out of
> control'. Loss of control might indeed be an issue in the future, but I'm
> not sure this example is a great argument for it."

The verdict is scoped to exactly what she checked: this anecdote doesn't
show what it's cited to show. She says the larger worry could still be real
in the same breath she delivers that verdict, so the correction stays aimed
at the one example and never widens into a ruling on the whole debate.

## Simon Willison, "Qwen 3.8 27B is excellent, but it defaults to wildly overthinking things"

Source: https://simonwillison.net/2026/Aug/16/qwen-38-27b/

> "This is by far the best pelican SVG I've been able to generate with a model
> that runs on a local machine—and this Qwen is pretty small, just a 17GB file
> on disk. There's a lot to like about this: [...] Was that worth waiting 21
> minutes for? Absolutely not."

He lists what's genuinely good about the result and then gives a flat verdict
on the cost of getting it, in four words, with a number attached to what that
cost was. The praise and the complaint are both specific enough that a reader
could disagree with either one on the evidence given.

> "There's one very significant catch: it feels slow—especially when it
> starts over-thinking, but even without that it's not particularly sprightly.
>
> I've been getting around 15-30 tokens a second from LM Studio. That's not
> terrible, but it's slow enough that it's going to be hard to win me away
> from hosted API models, which can return results a whole lot faster."

The limitation gets a number (fifteen to thirty tokens a second) instead of a
word like "slow" standing on its own, and the number is immediately put next
to what it costs him in practice — being unwilling to switch away from a
faster hosted model. The measurement and its consequence arrive together.

> "The most important thing about Qwen 3.8 27B is what it demonstrates. We can
> have an open weights general purpose model with a long context, effective
> tool calling, strong vision ability, and competent code generation, and we
> can fit the whole thing in just a 17GB file."

The closing claim names the exact capabilities being credited — long context,
tool calling, vision, code generation — and the exact constraint they fit
inside, a 17GB file. Anyone who read the piece can check each item on that
list against what came before it.
