## How this piece should sound

This lesson has to do the same move at least four times: state a plain fact
about one part of a text-to-speech pipeline, then look at one small, real case
until the mechanism inside it is visible, then say plainly what that case
shows. Matthew Yglesias's account of the tariff mechanism does this by
refusing to describe the general economic principle first. He takes one named
company, works out exactly what it does when it can't raise prices, then does
the same for a second company, and the mechanism only becomes visible in the
gap between the two. Each step in the chain this lesson teaches, text
normalization, then grapheme-to-phoneme prediction, then homograph
disambiguation, can get the same treatment: not "the front end expands
abbreviations" as a general claim, but one specific written form walked
through to its specific, sometimes wrong, spoken output.

Bartosz Ciechanowski's GPS essay builds its explanation by starting from a
version of the system almost too simple to work, and then breaking it on
purpose before fixing it: the naive approach fails for a stated, specific
reason, and that failure is what motivates the next design choice, not a
transition sentence. The pipeline this lesson traces has the same shape. A
system that assigns a pronunciation to each written word in isolation is a
real, describable thing, and it fails for a nameable reason on a genuine
homograph. Stating what the isolated-word version can and cannot do, before
introducing what fixes it, is a stronger move here than describing the fix
first and the gap it closes second.

Timothy B. Lee and Sean Trott's explainer of how large language models work
builds an unfamiliar idea (a word represented as a list of numbers) out of one
small, everyday analogy walked through with real figures, latitude and
longitude for a city, before the technical term does any work on its own.
The lesson has at least two ideas that need exactly this kind of build-up
before they're named: what a phoneme is, and what it means for a system to
predict one from spelling. A small, concrete stand-in walked through first,
with the term arriving once the idea under it is already visible, will carry
more than defining the term and then illustrating it.

The same piece is also the clearest model for how to be honest about the edge
of what's settled. It states the limit and the state of knowledge in two flat
sentences back to back, one admitting what's not understood, one immediately
saying what is. The lesson's own account of modern neural and end-to-end TTS
needs this same two-part honesty: naturalness has improved sharply and
vendors patch specific failures with lexicons, and a genuinely ambiguous
sentence still has no reliable answer even for a careful human reader. Both
halves earn their place only if they're stated as separate, flat claims
rather than folded into a single hedge.

Lee and Trott's account of the Redwood Research study is the nearest model for
this lesson's own required contribution. It takes one real sentence, traces
the model's prediction backward through named, specific mechanisms one at a
time, and only afterward says what the traceback does and doesn't explain.
The reader's own remembered mispronunciation deserves that same backward walk:
not a mechanism described in general terms, but that one sentence traced back
to the exact step, named, that produced the wrong sound, followed by a plain
statement of what the traceback shows and what it leaves open.

One thing this lesson should leave behind rather than carry over: several of
these passages move between ideas with direct address or a first-person
aside: a "consider," a "we love this example," a narrator thinking out loud.
The lesson's body speaks to no one; that kind of address belongs to the two
bookends, not the chain of steps between them. What transfers from all three
writers is the sentence-level habit underneath the address: one plain claim,
one small real case, one honest statement of what a step does and doesn't
settle, not the voice that happens to carry it in the exemplar.

## Matthew Yglesias, "Tariffs only 'work' if they make prices higher"

Source: https://www.slowboring.com/p/tariffs-only-work-if-they-make-prices

> "So here I want to emphasize something: There are lots of different ways
> that tariffs could play out. Some of those ways could lead to large
> increases in consumer prices and some have smaller or near-zero price
> effects. But to the extent that tariffs successfully protect high-wage
> American jobs or drive new investment in creating such jobs, the mechanism
> through which they succeed is higher prices. If the prices don't go up,
> then the things that Trump is touting as the benefits of tariffs also don't
> happen. The high prices are the protection."

The paragraph states the mechanism as a claim, not a mood: tariffs work
through one specific channel, and everything downstream of that channel
depends on it. The short sentence that closes it restates nothing that came
before in different words; it compresses the paragraph's claim into six words
without softening it. That compression is where the writer's judgment is
visible. He is willing to say the harder, plainer version of the sentence
rather than the safer, longer one.

> "Consider the case of a company like Audi, which sells a lot of
> foreign-made SUVs in the United States. If they don't raise prices, then
> suddenly selling an Audi to an American customer becomes a lot less
> lucrative than selling the exact same car to a customer in some other
> country. The reasonable course of action would be to redirect some of the
> cars to foreign countries — cutting the price of Audis abroad somewhat (but
> by less than the tariff rate) — and ship fewer units to the United States.
> Then on the flip side, you have a company like Ford whose SUVs are all made
> in the United States. With fewer foreign-made vehicles available for sale
> in the United States, demand for their SUVs is going to be higher."

Nothing here is described as a category. It's one named company doing one
specific, traceable thing, and then a second named company doing the mirror
version of that thing. The two together are what make the mechanism visible;
neither company's behavior alone would show it. The writer trusts a reader to
extract the general principle from the two specific cases rather than stating
the principle and using the cases as illustration.

> "Americans, of course, typically do not buy cars from the companies that
> make cars. We buy cars from car dealerships, which have these baffling
> geographically fragmented quasi-monopolies. When supply and demand for Ford
> SUVs is placed into disequilibrium, it's Ford dealerships, in the first
> instance, who will respond by raising prices. They might not even announce
> that prices are going up. They'll just become less willing to bargain down
> or give customers good deals."

This passage adds a layer of the mechanism the reader wasn't tracking (the
dealership, not the manufacturer) and names it plainly before explaining why
it matters. "Baffling geographically fragmented quasi-monopolies" is a real
description of a real market structure, not a flourish; the specificity of
the phrase is doing the same work as a citation would.

## Bartosz Ciechanowski, "GPS"

Source: https://ciechanow.ski/gps/

> "We'll start by creating a positioning system that can tell us where we
> are. Our initial approach will be quite simple, but we'll step-by-step
> improve upon it to build an understanding of the positioning method used by
> GPS."

This is the essay announcing its own method before using it: build a version
of the system too simple to be real GPS, then improve it one limitation at a
time. The sentence is not throat-clearing because it's making a specific,
checkable claim about how the piece is organized, and the piece then follows
through on exactly that structure for its full length.

> "The process of calculating a location of a point using measurement of
> distances is called trilateration – that procedure lies at the heart of a
> GPS receiver. However, being tied to two or three measuring tapes is
> certainly not how any GPS device functions, so let's keep on making our
> primitive positioning system better."

The technical term arrives only after four paragraphs of rope-and-landmark
description have already built the concept it names. The sentence right after
naming it immediately undercuts the toy version that just explained it
("certainly not how any GPS device functions"), which keeps the reader from
mistaking the simplified model for the real system.

> "The problem with this approach is that we've created an active system in
> which the landmarks have to actively respond to users' requests to provide
> the needed information. As the number of users increases, the complexity of
> the system grows significantly. Even if we came up with some clever way for
> the landmarks to distinguish the incoming signals and emit different
> responses, we're guaranteed to find some number of users that would
> overwhelm the infrastructure. Fortunately, we can solve this problem by
> flipping it on its head. Instead of the users sending audio signals to the
> landmarks, we'll have the landmarks emit the sounds and have the users
> listen to those sounds."

The failure is stated as a specific, structural fact about the design (an
active system that has to respond to every user doesn't scale), not as a
vague admission that the approach "has some issues." The fix is then framed
as the mirror image of the exact problem just named, so the reader can see
why this particular fix follows from this particular failure and not some
other one.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "As a result, no one on Earth fully understands the inner workings of LLMs.
> Researchers are working to gain a better understanding, but this is a slow
> process that will take years—perhaps decades—to complete. Still, there's a
> lot that experts do understand about how these systems work."

Two claims sit back to back without hedging into each other: a flat statement
of what isn't known, immediately followed by a flat statement of what is. The
second sentence doesn't walk back the first one, and the first doesn't get
buried under qualifiers meant to soften it. Both are allowed to stand as
separately true.

> "This is useful for reasoning about spatial relationships. You can tell New
> York is close to Washington DC because 38.9 is close to 40.7 and 77 is
> close to 74. By the same token, Paris is close to London. But Paris is far
> from Washington DC."

The analogy (cities as coordinates) is worked through with the actual
numbers rather than gestured at, and the last sentence does real work: after
three sentences showing the coordinates correctly group cities that are
close, the fourth shows they also correctly separate two that aren't. That's
what lets the reader carry the coordinate idea forward into the harder claim
about word vectors that follows it.

> "In the last two sections we presented a stylized version of how attention
> heads work. Now let's look at research on the inner workings of a real
> language model. Last year scientists at Redwood Research studied how GPT-2,
> a predecessor to ChatGPT, predicted the next word for the passage 'When
> Mary and John went to the store, John gave a drink to.'"

The piece marks its own transition from a simplified model to a documented,
real instance explicitly, rather than letting the reader assume the toy
version and the real finding are the same kind of claim. Naming the exact
sentence GPT-2 was asked to complete, in quotation marks, is what lets
everything that follows be checked against one fixed case instead of a
description of cases in general.
