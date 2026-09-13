# Voice guide: the-mechanics/speech-to-text-hallucination

## How this piece should sound

This lesson works backward from one behavior, a transcription tool printing a
fluent sentence over silence or noise, to the reason it happens: the stage that
writes the words is an autoregressive language model, and a language model given
almost nothing to go on still produces well-formed text. The whole piece hangs
on whether that ending feels inevitable by the time the reader reaches it. Hold
a plain, level register the whole way, the kind Willison keeps even when a
result is surprising. The reader is sharp and has never read code. Define
encoder and decoder in plain words the first time each is used, and assume
nothing else about the architecture that the lesson has not already built.

The central craft to take is Ciechanowski's. He reaches each new part by first
saying plainly what the current arrangement cannot do, so the next part arrives
as the obvious answer to a gap the reader can already feel. His "This is where
gears come in" lands only because the sentences before it made the shortfall
concrete. When the reader has seen that the decoder is a language model whose
job is to emit probable text, an invented line over silence can be presented as
the expected output of that design rather than as a glitch. Contrast with an
older word-by-word recognizer, which had no such prior to fall back on, is one
place that gap can be made to bite.

Ground each step in something concrete, as all three writers do. Ciechanowski
uses real quantities, 40 hours and 2400 rotations, to show why a mechanism is
needed. Willison turns an abstract space into "germany" plus "paris" minus
"france" landing on "berlin," and Evans turns prefix codes into "010 00 1001
011 or baec." A single invented sentence, shown against the exact silence or
background sound that produced it, can carry the mechanism the way those small
cases carry theirs. Evans also shows the value of posing the puzzle before the
answer: she asks how you could possibly know where one character ends and the
next begins before she introduces Huffman codes. The confident sentence with
nothing behind it can be that puzzle here.

Hold the line between what is settled and what is open in plain statement, the
way Willison does when he writes that nobody fully understands what the numbers
mean while we do know the locations are useful. Some of this is settled: the
decoder is a generative language model, and empty input still yields output.
Some is not: which inputs set the invention off, how far better data or decoding
rules reduce it, how the rate differs by system. Say which is which without
letting the open part deflate the settled part or the settled part flatten the
open one. Where the account reaches something the field itself has not resolved,
name that plainly, the way Evans says outright when she does not know what a
piece of output means.

Keep the harm in proportion. A fabricated line in a medical scribe's transcript,
where the original audio may be gone, is serious on its own terms, and it reads
as more serious stated flatly than dressed up. Report what was found and let it
weigh what it weighs. If a vivid word helps, take it from the machine's own
parts, the way Ciechanowski lets the escape wheel "escape," a word that comes
straight from the name of the escapement. The encoder, the decoder, the silence,
the language prior are where this piece's images live.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "Embeddings are based around one trick: take a piece of content—in this case a blog entry—and turn that piece of content into an array of floating point numbers.
>
> The key thing about that array is that it will always be the same length, no matter how long the content is. The length is defined by the embedding model you are using—an array might be 300, or 1,000, or 1,536 numbers long.
>
> The best way to think about this array of numbers is to imagine it as co-ordinates in a very weird multi-dimensional space."

Willison starts from one plain claim and lets the next sentence add exactly one
thing, so a reader with no background is never carrying more than one new idea at
a time. Naming it "one trick" up front tells the reader the mechanism is small
before he sees it. The concrete counts, 300 or 1,000 or 1,536, do the work an
adjective like "large" would have left vague.

> "The location within the space represents the semantic meaning of the content, according to the embedding model’s weird, mostly incomprehensible understanding of the world. It might capture colors, shapes, concepts or all sorts of other characteristics of the content that has been embedded.
>
> Nobody fully understands what those individual numbers mean, but we know that their locations can be used to find out useful things about the content."

This is the settled-versus-open move done in two sentences. Willison states the
open part, that nobody fully understands the numbers, and the settled part, that
the locations are useful, in the same breath and lets neither cancel the other.
He is visible in his willingness to call the model's understanding "weird,
mostly incomprehensible" rather than reach for a term that would hide that he
finds it strange too.

> "Take the vector for “germany”, add “paris” and subtract “france”. The resulting vector is closest to “berlin”!
>
> Something about this model has captured the idea of nationalities and geography to the point that you can use arithmetic to explore additional facts about the world."

A claim that would be abstract, that the space encodes meaning, is made checkable
by one worked case a reader can hold in his head. The follow-up sentence is
carefully hedged: "Something about this model has captured" claims what the demo
shows and no more, which is how Willison keeps from overstating a mechanism he
has just called incomprehensible.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in."

Ciechanowski earns the next part by stating a requirement in real numbers first,
so gears arrive as the answer to a need the reader already feels rather than as
the next item on a list. The final short sentence introduces the mechanism only
after the gap it fills has been made concrete. He is visible in the patience of
it, laying out the arithmetic in full instead of asserting that a big speed-up is
needed.

> "The pallet fork prevents that motion, but as we pivot that pallet fork back and forth, we let the escape wheel briefly escape from that jail only to be stopped again."

The whole action is described in ordinary verbs, prevents, pivot, escape,
stopped, so the reader watches the parts move without any term of art in the
way. The one figure he allows himself, the "jail," is anchored to the real name
of the escapement, so the wordplay teaches the part's name instead of decorating
the sentence.

> "Once the pallet fork unlocks the escape wheel, that wheel has to start spinning very quickly. This is why gears in the gear train have holes in them – it reduces their moment of inertia so that the barrel can accelerate them more quickly."

Here he works from an observed detail, the holes in the gears, back to the reason
it has to be there, which is the same backward move this lesson makes from an
invented sentence to its cause. The explanation is one causal chain stated
plainly, with no step skipped between the holes and the acceleration they allow.

## Julia Evans, "How gzip uses Huffman coding"

Source: https://jvns.ca/blog/2015/02/22/how-gzip-uses-huffman-coding/

> "Those were totally made up 0s and 1s and do not mean anything. But, reading something like this, how can you know where the boundaries between characters are? Does 01 represent a character? 010? 0101? 01010?"

Evans sets up the problem before she offers the mechanism, so the reader feels
the difficulty that Huffman coding then resolves. The escalating questions, 01,
010, 0101, 01010, make an abstract ambiguity into something the reader can try
and fail to do himself. Her plainness is the point: she trusts a concrete puzzle
to motivate the idea more than a statement of importance would.

> "If you look at these carefully, you’ll notice something special! It’s that none of these codes is a prefix of any other code. So if we write down 010001001011 we can see that it’s 010 00 1001 011 or baec! There wasn’t any ambiguity, because 0 and 01 and 0100 don’t mean anything."

She states the rule and immediately runs it on a specific string, decoding
010001001011 into baec in front of the reader, so the mechanism is demonstrated
rather than described. Working the example by hand is what makes the property
believable. The exclamation marks and the delight belong to Evans's personal
blog. The move worth taking is the worked decode she does in front of the reader.
