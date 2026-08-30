# Voice guide: the-mechanics/random-numbers

## How this piece should sound

This lesson starts from one exact behavior: a chatbot asked for a random
number answers "7". The opening should be that specific, the way Julia
Evans narrows "what's going on with terminals" down to "when you press a key
... which bytes get sent?" before she does anything else. Naming the actual
number the reader has seen, not "a predictable answer" or "a suspicious
pattern," is what turns the opener into an investigation instead of a topic
sentence.

The piece has no code to lean on for concreteness, so the small example has
to carry weight the way Timothy B. Lee and Sean Trott's actual coordinates
carry the word-vector claim, or the way Bartosz Ciechanowski turns "runs about
two days" into 2,400 rotations before naming the part that produces that
number. Wherever this lesson touches a probability, a token, or a value a
sampling step actually used, the material may call for the real number
instead of a description of its size, kept next to the "7" example rather
than replacing it, since the series prompt asks the piece to keep the small
example in view at every step down.

Working backward asks the piece to spend at least one step on an answer that
looks right and isn't, the way Ciechanowski lets the reader watch the naive
watch-hand-on-the-barrel idea fail before the gear train shows up to fix it.
A reader might already hold a tempting explanation for "7": that the model
is just "randomly picking" the way a person would. Showing where that
explanation breaks is worth a step of its own, not a sentence dismissing it
in passing.

Each step should name the actual part doing the work and say plainly what it
does, the way Evans's Ctrl+C paragraph gets from a byte to a named kernel
mechanism and Ciechanowski's escape wheel and pallet fork act directly on
each other. Nothing in this piece should be described as a mechanism that
"ensures" or "produces" an outcome without naming the part and the action.

The series asks the piece to mark which steps are settled and which are
open, and Lee and Trott's paragraph on GPT-2 predicting "Mary" is a model for
where that goes: the finding stated plainly, then qualified by exactly what
the cited research still couldn't explain, in the same paragraph rather than
hedged separately at the end. Where this lesson's own trace bottoms out, at
the step where nothing further down would change the answer, the piece may
mark that the way it marks any other step: plainly, with what is and isn't
known about it, not with a sentence implying the subject is now closed.

Evans's closer is the model for stopping honestly: naming the specific
things being left out, then giving the real, unglamorous reason for stopping
there, rather than a sentence that sounds like a conclusion but restates
what the piece already showed. When this lesson hits its own ground, the
same move serves better than a summarizing last line: say what's being left
for a later lesson, plainly, and stop.

## Julia Evans, "What happens when you press a key in your terminal?"

Source: https://jvns.ca/blog/2022/07/20/pseudoterminals/

> "I've been confused about what's going on with terminals for a long time.
>
> But this past week I was using xterm.js to display an interactive terminal
> in a browser and I finally thought to ask a pretty basic question: when you
> press a key on your keyboard in a terminal (like `Delete`, or `Escape`, or
> `a`), which bytes get sent? As usual we'll answer that question by doing
> some experiments and seeing what happens :)"

She states her own confusion before she states the reader's, then narrows a
vague topic down to one exact, checkable question, naming the actual keys.
The stated plan isn't "we will explain how terminals work." It's "we'll
answer that question by doing some experiments." The method is concrete
from the first line, not just the subject.

> "I believe the reason `cat` gets interrupted when we press `Ctrl+C` is that
> the Linux kernel on the server side receives this `\x03` character,
> recognizes that it means "interrupt", and then sends a `SIGINT` to the
> process that owns the pseudoterminal's process group. So it's handled in
> the kernel and not in userspace."

"I believe" flags that this particular step is her inference about what's
happening inside the kernel, distinct from the bytes she watched cross the
wire a paragraph earlier. The piece keeps observed fact and reasoned-out
cause visibly separate. The last sentence names exactly where in the system
the behavior lives, kernel rather than userspace, instead of leaving it as
"somewhere under the hood."

> "There's definitely a lot more to know about terminals (we could talk more
> about colours, or raw vs cooked mode, or unicode support, or the Linux
> pseudoterminal interface) but I'll stop here because it's 10pm, this is
> getting kind of long, and I think my brain cannot handle more new
> information about terminals today."

She names three specific things she isn't covering rather than gesturing at
"more nuance," and gives an honest, ordinary reason for stopping instead of a
sentence dressed up to sound like a conclusion. The piece ends where her
knowledge and her energy actually ran out, and it says so.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Washington DC is located at 38.9 degrees North and 77 degrees West. We can
> represent this using a vector notation: Washington DC is at [38.9, 77] ...
> This is useful for reasoning about spatial relationships. You can tell New
> York is close to Washington DC because 38.9 is close to 40.7 and 77 is
> close to 74."

The analogy borrows a coordinate system the reader already owns (latitude
and longitude) and hands over the real numbers for four cities before
making the claim about closeness, so the reader can check "38.9 is close to
40.7" for themselves instead of taking the writer's word for it.

> "Suppose you're going to take a shower, and you want the temperature to be
> just right: not too hot, and not too cold. You've never used this faucet
> before, so you point the knob to a random direction and feel the
> temperature of the water. If it's too hot, you turn it one way; if it's too
> cold, you turn it the other way. The closer you get to the right
> temperature, the smaller the adjustments you make."

This is their analogy for how training adjusts a model's weights, not for
how a trained model picks its next word. That's a different mechanism than
the one this article traces, so the analogy itself doesn't transfer. What's
worth taking is the construction: one property (adjust toward a target by
trial and error) is established before the analogy is extended piece by
piece in the paragraphs that follow it.

> "We love this example because it illustrates just how difficult it will be
> to fully understand LLMs. The five-member Redwood team published a 25-page
> paper explaining how they identified and validated these attention heads.
> Yet even after they did all that work, we are still far from having a
> comprehensive explanation for why GPT-2 decided to predict Mary as the next
> word."

The finding is stated first: named attention heads did specific, identified
work. It's then immediately qualified by exactly what a 25-page paper and a
five-person research team still couldn't fully explain. Settled and open
sit in the same paragraph, not sorted into a confident half and a hedge
tacked on at the end.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "We've managed to make some parts rotate and one could naively think that
> we could just attach a watch hand to the barrel to make it track time.
> Unfortunately, that won't really work [...] We clearly have some work to
> do – the hand spins way too fast and it only does a few rotations before
> the mainspring inside the barrel runs out of the stored energy. Clearly,
> this contraption won't let us track time in any reliable way."

He states the naive-sounding idea plainly, in the reader's own likely words
("one could naively think"), then shows exactly how and why it fails before
introducing the part that fixes it. The reader watches the wrong answer fail
on its own terms, so the right one lands as something earned rather than
asserted.

> "If we wanted our watch to run continuously for around 40 hours on a single
> wind, we'd need the minute hand to complete 40 rotations in that time.
> Moreover, the second hand should cover around 40 × 60 = 2400 complete
> rotations in that time. We need to find a way to convert a small number of
> revolutions of the barrel into a large number of revolutions of the hands.
> This is where gears come in."

An abstract requirement (the watch should run about two days) becomes an
exact number of rotations before the part that satisfies it gets named. The
number is doing real work: it's checkable, and it's what makes "gears come
in" a conclusion instead of an announcement.

> "The escape wheel wants to rotate as indicated by the red arrow. The pallet
> fork prevents that motion, but as we pivot that pallet fork back and forth
> we let the escape wheel briefly escape from that jail only to be stopped
> again."

Every clause names an actual part and what it physically does to another
named part. Nothing here is described as a mechanism that "ensures" or
"regulates" anything. The one piece of color, "escape from that jail," isn't
decoration; it's the escape wheel doing the thing its own name says it does.

