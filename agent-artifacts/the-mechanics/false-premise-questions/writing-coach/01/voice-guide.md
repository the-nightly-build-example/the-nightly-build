# Voice guide: the-mechanics/false-premise-questions

## How this piece should sound

This lesson has one job: let a reader who has typed a leading question into a
chatbot and watched it answer fluently on a false premise understand exactly
why, one real step at a time, down to the point where nothing further would
change the story. The house register is Matt Yglesias explaining something he
understands well, plain claims, no fuss, and that has to hold for a piece whose
actual content is a chain: a presupposition sitting inside a prompt, a training
distribution, a training objective, and a layer of post-training that only
partly reaches the problem.

The series prompt already tells the writer that algebra and probability need no
introduction here. That changes what the exemplars' concrete-object move is for
in this piece. Wolfram and the Ars Technica writers spend real effort making
"probability" itself bearable for a reader who doesn't have it yet; this
reader already does. So the same move, shrinking an abstract object down to
something a reader can hold in one sentence, needs to go toward the objects
that are specific to this chain instead: what it means for a next-token
predictor to condition on something already in the prompt, what a "training
distribution that rarely corrects a premise" actually looks like as a fact
about real text.

Wolfram's cannonball passage is a model for introducing a term the lesson can't
avoid, whatever the writer ends up calling the presupposition-carrying part of
the chain: define it through one dated, physical case, rather than a sentence
of definition with an example tacked on afterward. The lesson has at least one
term like that, and it deserves the same treatment rather than a glossary-style
gloss.

The whole shape of this lesson is a descent, and the Redwood/GPT-2 "Mary"
passage in the Ars Technica piece shows a way to carry a reader down one
without signposting sentences like "now let's go deeper." Asking the same
question again, one level lower, each time a new part of the mechanism gets
named, can do that work instead, which suits a chain that's already built as a
series of nested "why" answers.

Two things in this lesson have to be marked as open rather than settled:
whether a model detects a false premise at all, and whether that detection
would be understanding or another pattern. Wolfram's cat passage and
Willison's alien-and-USB-stick line both handle a limit like that the same
way, by trying the claim on something concrete, a photograph, a file on a
laptop, and reporting plainly that the explanation runs out there, rather than
a sentence that announces its own carefulness. One clear image for the edge of
what's known, used once, does more work here than a hedge repeated at every
open point.

The lesson can likely afford one moment like Willison's Claude anecdote: a
real instance of the behavior itself, the actual false-premise question and
the actual answer, quoted rather than paraphrased, before the mechanism gets
explained. Whether that comes from a transcript the writer runs or from one of
the evaluation papers' own examples is for the evidence to decide.

Willison's own register pulls two ways at once for this piece. The "Twitter
influencer manual" joke works because its target is specific and checkable,
which is the kind of aside this lesson can use. The bigger gestures in the same
talk, "alien technology," "tame these bizarre new beasts," belong to a
conference room, not to a lesson bound by no hype and no doom. Take the
specificity Willison reaches for; leave the showmanship behind.

## Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?"

Source: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

> "Say you want to know (as Galileo did back in the late 1500s) how long it's
> going to take a cannon ball dropped from each floor of the Tower of Pisa to
> hit the ground. Well, you could just measure it in each case and make a
> table of the results. Or you could do what is the essence of theoretical
> science: make a model that gives some kind of procedure for computing the
> answer rather than just measuring and remembering each case."

Wolfram sets up the entire idea of a "model" with one dated, physical fact: a
cannonball, the Tower of Pisa, the late 1500s. He never states a definition of
"model" before the example runs; the example is the definition, and the two
options he offers, measure everything or build a procedure, are the actual
content of the term. Choosing a real, centuries-old piece of science instead
of an invented toy problem is his; it lets the passage carry weight without
needing invented drama.

> "Show yourself a picture of a cat, and ask 'Why is that a cat?'. Maybe you'd
> start saying 'Well, I see its pointy ears, etc.' But it's not very easy to
> explain how you recognized the image as a cat. It's just that somehow your
> brain figured that out. But for a brain there's no way (at least yet) to 'go
> inside' and see how it figured it out."

Wolfram tests a claim about the limits of explanation by trying it on the
reader directly: look at an actual cat, try to explain the recognition, watch
the explanation run out after one clause. He doesn't hedge the running-out with
a qualifier; he reports it as the finding itself, in the same plain sentences
he's been using all along.

> "As a straightforward analogy, let's say we have certain positions in the
> plane, indicated by dots (in a real-life setting they might be positions of
> coffee shops). Then we might imagine that starting from any point on the
> plane we'd always want to end up at the closest dot (i.e. we'd always go to
> the closest coffee shop)."

Wolfram translates "nearest point in an abstract space" into the most mundane
version of that idea available, a person picking the nearest coffee shop. He
gives it one sentence of setup and one sentence of payoff, then moves on rather
than extending the coffee-shop detail past what the point needs.

## Timothy B. Lee and Sean Trott, "A jargon-free explanation of how AI large language models work"

Source: https://arstechnica.com/science/2023/07/a-jargon-free-explanation-of-how-ai-large-language-models-work/

> "This is useful for reasoning about spatial relationships. You can tell New
> York is close to Washington, DC, because 38.9 is close to 40.7 and 77 is
> close to 74. By the same token, Paris is close to London. But Paris is far
> from Washington, DC."

Before asking the reader to picture a 300-number vector, Lee and Trott show the
same underlying idea, closeness as a number, at a size small enough to check by
hand: four cities and two coordinates each. The claim about "closeness" isn't
just asserted; the reader can verify it against a map they already carry in
their head.

> "Here's an analogy to illustrate how this works. Suppose you're going to
> take a shower, and you want the temperature to be just right: not too hot
> and not too cold. You've never used this faucet before, so you point the
> knob in a random direction and feel the temperature of the water. If it's
> too hot, you turn it one way; if it's too cold, you turn it the other way.
> The closer you get to the right temperature, the smaller the adjustments you
> make."

The analogy commits to one physical object, a single shower knob, rather than
staying general about "adjustment." Later in the piece the writers admit the
analogy "quickly gets silly if you take it too literally," which is a
different kind of honesty than a hedge: it names exactly where the comparison
stops holding instead of qualifying it in advance.

> "How did the network decide Mary was the right word to copy? Working
> backward through GPT-2's computational process, the scientists found a group
> of four attention heads they called Subject Inhibition Heads that marked the
> second John vector in a way that blocked the Name Mover Heads from copying
> the name John. How did the Subject Inhibition Heads know John shouldn't be
> copied? Working further backward, the team found two attention heads they
> called Duplicate Token Heads."

The passage is built out of one repeated question, "how did it decide X,"
asked again one level down each time a new mechanism gets named. The
structure itself carries the reader downward; the writers never need a
sentence announcing that they're going deeper, because the repeated question
already does that work.

## Simon Willison, "Catching up on the weird world of LLMs"

Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/

> "One way to think about it is that about 3 years ago, aliens landed on
> Earth. They handed over a USB stick and then disappeared. Since then we've
> been poking the thing they gave us with a stick, trying to figure out what
> it does and how it works."

Willison names what isn't understood before he names what is: the image admits
up front that nobody fully understands the object under discussion. The
bluntness of "poking the thing they gave us with a stick" is informal, but it
is also an exact description of the epistemic position he's in, not a
decoration on top of it.

> "A key challenge of these things is that they do not come with a manual!
> They come with a 'Twitter influencer manual' instead, where lots of people
> online loudly boast about the things they can do with a very low accuracy
> rate, which is really frustrating."

The joke lands on a specific, named target, people overstating what these
systems can reliably do, rather than a generic complaint. "Twitter influencer
manual" is a real noun standing in for a real problem, which is why the joke
still says something once you try to imagine it about a different subject.

> "Claude hallucinated at me while I was preparing this talk! I asked it: 'How
> influential was Large Language Models are Zero-Shot Reasoners?' ... It told
> me, very convincingly, that the paper was published in 2021 by researchers
> at Google DeepMind. This is not true, it's completely fabricated! The thing
> language models are best at is producing incredibly convincing text, whether
> or not it's actually true."

Willison doesn't describe the failure in the abstract. He gives the exact
question, the exact wrong answer, and the model and date involved, and only
after that specific, checkable exchange does he state the general claim. The
verdict arrives last, earned by the transcript in front of it, not first.
