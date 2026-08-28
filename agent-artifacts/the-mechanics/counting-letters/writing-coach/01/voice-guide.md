# Voice guide: the-mechanics/counting-letters

## How this piece should sound

Open on the behavior itself, not on the machinery that explains it. Julia
Evans opens on the error message, confused and annoyed, before she has any
idea what is wrong. The reader of this lesson has watched a chatbot miss a
letter count on a word they could check on their fingers in two seconds, and
the piece earns the right to explain the tokenizer by first sitting in that
same small disbelief, the way Evans sits in "the file is RIGHT THERE."

Hold the one failure as the running example for the whole descent. Randall
Munroe never trades the AK-47 for a different gun partway through "Machine
Gun Jetpack"; every new fact, from thrust-to-weight ratio to ammunition
weight to hot gas and debris, lands on the same rifle, so the reader never
has to re-orient. The series prompt asks for the same discipline: work backward from one
behavior to its cause, step by step. If the piece needs a second word or a
second model to make a point, that is a sign the point is not yet earned on
the first one.

Name the real parts of the system the way Timothy Lee names the query
vector and the key vector: define each term in the sentence that first uses
it, in plain words, and then keep that exact word for the rest of the piece.
The tokenizer and byte-pair encoding are the two terms this lesson cannot
avoid; each gets its definition on first use and no synonym after.

Let one analogy carry the real weight. Lee's Washington-DC-as-coordinates
comparison appears exactly once, gets used to make an actual point about
distance, and is never brought back for color. If this
lesson reaches for a comparison to make chunking or splitting concrete, run
it once, get the payoff, and move past it.

Mark the edge between settled mechanism and open question in a plain
declarative sentence, not a hedge buried in a subordinate clause. Evans
writes "I still don't understand why it's using cgo here... I don't feel
like solving that mystery right now" and "for some reason it seems to
produce a slightly smaller binary?? I don't know why that is." Two flat
admissions, neither hedged with an apology. The series prompt asks this lesson to do the same
wherever the tokenizer's behavior genuinely runs out of settled explanation:
say what is known, say what is not, and do not dress up a guess as a
finding.

Let each step reframe into the next question the way Evans's fixed bug
opens onto a bigger one: "The problem was with the program's interpreter.
But I remembered that only dynamically linked programs have interpreters,
which is a bit weird... What's going on with that?" One answer becoming the
next question is how a piece keeps going down instead of stopping at the
first plausible-sounding cause.

None of the three exemplars below can be copied whole. Evans works in
terminal transcripts and Munroe works in an equation; this lesson runs no
code and no formula, so the same steps have to be carried in prose alone, in
plain sentences doing the work that a strace line or a thrust equation does
for them. And where Munroe closes on a joke built for his own site ("you
could jump mountains"), this lesson's close belongs to the takeaway bookend
instead, which lands the judgment on its own terms.

## Julia Evans, "Debugging a weird 'file not found' error"

Source: https://jvns.ca/blog/2021/11/17/debugging-a-weird--file-not-found--error/

> "Yesterday I ran into a weird error where I ran a program and got the
> error "file not found" even though the program I was running existed.
> It's something I've run into before, but every time I'm very surprised
> and confused by it (what do you MEAN file not found, the file is RIGHT
> THERE???!!??)"

This is the whole piece in miniature: a specific, checkable claim (the file
exists, the error says it doesn't) and a personal reaction that never
drifts into generic bafflement. The capital letters and stacked punctuation
are hers, earned by the actual contradiction sitting right in front of her.

> "The problem was with the program's interpreter. But I remembered that
> only dynamically linked programs have interpreters, which is a bit weird
> – I expected my Go binary to be statically linked! What's going on with
> that?"

She has just found the cause of the original bug, and instead of stopping,
she notices the cause itself is strange and asks why. The move is visible:
one answer becomes the next question, which is how the piece keeps
descending instead of settling for the first plausible stopping point.

> "And statically linking in this case doesn't even produce a bigger binary
> (for some reason it seems to produce a slightly smaller binary?? I don't
> know why that is) I still don't understand why it's using cgo here, I ran
> env | grep CGO and I definitely don't have CGO_ENABLED=1 set in my
> environment, but I don't feel like solving that mystery right now."

Two separate admissions of not knowing, back to back, each stated flatly
instead of hedged. Neither pretends to be answered. This is where the
writer is most visible: she names precisely what she checked (an
environment variable, a binary's size) before saying she can't explain it,
so the not-knowing reads as earned.

## Randall Munroe, "Machine Gun Jetpack"

Source: https://what-if.xkcd.com/21/

> "The principle here is pretty simple. If you fire a bullet forward, the
> recoil pushes you back. So if you fire downward, the recoil should push
> you up."

Three short sentences state the entire mechanism before any numbers arrive.
Nothing in the paragraph needs a term the reader doesn't already have. The
whole rest of the piece is this same idea getting bigger guns.

> "The amount of thrust created by a rocket (or firing machine gun) depends
> on (1) how much mass it's throwing out behind it, and (2) how fast it's
> throwing it."

He breaks the mechanism into exactly the two variables that matter and
names them in the plainest words available: mass and speed. The
parenthetical numbering is doing real work too. It tells the reader there
are exactly two things to track here, nothing hidden in a third.

> "In practice, the actual thrust turns out to be up to around 30% higher.
> The reason for this is that the gun isn't just spitting out bullets—it's
> also spitting out hot gas and explosive debris. The amount of extra force
> this adds varies by gun and cartridge."

Having just given a clean number, he immediately says the clean number is
wrong in practice and by how much, then says why, then says the correction
itself isn't fixed either. Three sentences, three different levels of
certainty, none of them blurred into the others.

## Timothy B. Lee, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Why use such a baroque notation? Here's an analogy. Washington DC is
> located at 38.9 degrees North and 77 degrees West. We can represent this
> using a vector notation... This is useful for reasoning about spatial
> relationships. You can tell New York is close to Washington DC because
> 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is
> close to London. But Paris is far from Washington DC."

The analogy is introduced, then immediately put to work on real numbers the
reader can check by eye, then dropped. Lee doesn't return to it later for
flavor. It exists to make one idea, proximity in a vector space, concrete
exactly once.

> "You can think of the attention mechanism as a matchmaking service for
> words. Each word makes a checklist (called a query vector) describing the
> characteristics of words it is looking for. Each word also makes a
> checklist (called a key vector) describing its own characteristics. The
> network compares each key vector to each query vector (by computing a dot
> product) to find the words that are the best match."

The metaphor (matchmaking) and the term of art (query vector, key vector)
arrive together, in the same breath, so the reader never holds an
undefined word for even a sentence. The parenthetical naming is doing the
defining; nothing is asserted about the term before it's given.

> "In short, these nine attention heads enabled GPT-2 to figure out that
> "John gave a drink to John" doesn't make sense and choose "John gave a
> drink to Mary" instead. We love this example because it illustrates just
> how difficult it will be to fully understand LLMs... Yet even after they
> did all that work, we are still far from having a comprehensive
> explanation for why GPT-2 decided to predict Mary as the next word."

The passage closes out a multi-step mechanical explanation, then states
plainly what is still not understood about it, from people who did the
underlying research. The uncertainty is specific: why this particular word,
after nine identified attention heads, and not language models in general.
