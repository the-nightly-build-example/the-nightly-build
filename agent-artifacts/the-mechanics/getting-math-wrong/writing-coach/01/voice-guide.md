# Voice guide: the-mechanics/getting-math-wrong

## How this piece should sound

This lesson takes a thing the reader has watched happen, a chatbot returning a
confident wrong answer to a large multiplication, and walks backward to what
produces it. The register that fits is the one the press already asks for: plain
declaratives, concrete stakes, no display. Bartosz Ciechanowski explaining a
watch and Julia Evans explaining DNS both write this way, and neither ever
sounds like they are performing expertise. The house voice already settles the
tie the press names: understood over impressive.

The lesson is grounded in one real botched calculation with the true answer
beside it. Ciechanowski sets a mechanism up by first stating, in numbers a
reader can hold, exactly what it has to do (forty rotations of the minute hand,
twenty-four hundred of the second hand) before he names the gear that does it.
The worked multiplication can carry the explanation the same way: the digits of
the model's answer and the digits of the right answer, laid next to each other,
show the size of the miss more directly than any word for it. Where a figure
appears, doing the small arithmetic out loud, as he does with 40 × 60 = 2400,
reads better than asserting the total.

The chain from behavior to cause is a sequence of steps, and the joints between
them can do real work rather than fill space. Ciechanowski, having built the
gears, says the hand's speed is still untamed and that this is why the next part
exists. A step here can close the same way: name what has been explained, then
the specific thing it still leaves unaccounted for, so the next step answers a
question the last one raised. Within a step, Evans and Ciechanowski both keep to
plain cause and effect in short sentences, staying with the actual parts rather
than an abstraction over them.

Much of why this behavior is surprising is that the reader cannot see inside the
model. Evans names precisely what a person never gets to watch, the exchange
between resolver and nameservers, and says that this hiddenness is what makes
the trouble hard to reason about. The lesson can be as specific about what the
model receives when it reads a number, and about the place value and
right-to-left carrying a person uses without thinking, as Evans is about the
exchange she cannot see.

When the lesson reaches how a model actually represents and combines numbers, it
reaches ground that the people who build these systems have only partly mapped.
Karpathy, after several confident readings of what individual units seem to be
doing, says plainly that those readings are hand-wavy because the internal state
is large and spread out, and he marks that limit in the same voice he used for
the claims. Evans does the smaller version when she reads an error message,
explains what she can, and says she does not know what the rest means. The body
here speaks to no one and cannot say "I'm not sure," but it can state in the
third person, in plain words and without a heading announcing it, which parts
are established engineering and which remain open.

Reporting where the model goes wrong wants the same flatness. Karpathy gives a
generated program a plain overall verdict, then says it probably will not
compile, then points to the exact errors, with the praise and the fault side by
side and each tied to something on the page. Set the model's wrong product and
the true product down without drama and let their difference show the size of
the miss. The fixes the lesson points to, writing the steps out or handing the
sum to a calculator, can be named as plainly as the failure.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "But it took me YEARS to figure out how to confidently debug DNS issues, and I’ve seen a lot of other programmers struggle with debugging DNS problems as well. So what’s going on?"

She opens by admitting the thing took her years and that experienced people
around her struggled with it too, then asks a flat question and goes looking for
the answer. The voice is a person working something out in the open rather than
an authority delivering a result. Evans is visible in the capitalized "YEARS"
and in how ordinary "So what’s going on?" is.

> "I think a lot of DNS issues would be SO simple to understand if you could magically get a trace of exactly which authoritative nameservers were queried downstream during your request, and what they said."

She points at the exact part of the system a person never gets to see, the
conversation between the resolver and the nameservers, and says plainly that its
hiddenness is what makes the trouble hard. The judgment is specific to DNS's own
parts, not a general line about things being complex. Her wish for a tool that
would just show the hidden exchange is where she comes through.

> "Here I’ve requested a nonexistent domain, and I got the extended error EDE: 12 (NSEC Missing): (Invalid denial of existence of xjwudh.com/a). I’m not sure what that means (it’s some DNSSEC Thing), but it’s cool to see an extra debug message like that."

She shows a real command's output, reads off the part she understands, and then
says outright that she does not know what one piece means. Admitting the gap
costs her nothing and makes everything around it easier to trust. The person is
visible in "it’s some DNSSEC Thing" and in her willingness to stop at the edge
of what she knows.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in."

Before naming a single gear he states exactly what the mechanism has to
accomplish, in numbers the reader can hold. The problem is set concretely, so
the part that solves it arrives as the answer to something specific rather than
as the next topic. Ciechanowski is visible in his doing the multiplication out
loud, 40 × 60 = 2400, instead of just stating the total.

> "An important aspect of two matching gears is their number of teeth. Each tooth in one gear meets with a space between teeth in the other gear, so within a unit of time both gears rotate by the same number of teeth. If the number of teeth in two gears is different, those gears can take a different amount of time to complete a single rotation."

He explains why two meshed gears turn at different rates by walking one step of
cause and effect, a tooth meeting a space, in short plain sentences. Nothing is
asserted that the sentence before it has not earned. The writing stays with the
physical parts, teeth and spaces, rather than reaching for a general principle.

> "We’ve certainly achieved the goal of the second hand rotating many times on a single rotation of the barrel, but the speed of revolution of that hand is still completely untamed. We need to find a way to control the rate of release of the energy stored in the mainspring – we’ll do this with the escapement."

He marks what the mechanism has managed so far and names the one thing still
wrong with it, and that becomes the reason the next part exists. The transition
carries the argument forward instead of filling a gap between sections. The
plainness shows in "completely untamed" and in his stating the next problem
before he names the part that fixes it.

## Andrej Karpathy, "The Unreasonable Effectiveness of Recurrent Neural Networks"

Source: https://karpathy.github.io/2015/05/21/rnn-effectiveness/

> "The picture that emerges is that the model first discovers the general word-space structure and then rapidly starts to learn the words; First starting with the short words and then eventually the longer ones. Topics and themes that span multiple words (and in general longer-term dependencies) start to emerge only much later."

He describes what the model learns and in what order, the spaces first, then
short words, then longer-range structure much later, grounding each claim in
samples he actually watched print out. The sequence is reported as observation
and left undecorated. "The picture that emerges is" is Karpathy stating a result
without inflating it.

> "The code looks really quite great overall. Of course, I don’t think it compiles but when you scroll through the generate code it feels very much like a giant C code base."

He gives a flat overall verdict, then immediately says the thing probably does
not compile, and elsewhere points to the exact errors it makes. The praise and
the fault sit next to each other without drama, each tied to something concrete
on the page. His register is audible in "looks really quite great overall" set
right beside the admission.

> "Of course, a lot of these conclusions are slightly hand-wavy as the hidden state of the RNN is a huge, high-dimensional and largely distributed representation."

After several confident readings of what particular units in the network seem to
be doing, he says plainly that those readings are only partly reliable, and why.
He marks the limit of the interpretation in the same voice he used to offer it,
which keeps the earlier claims from overreaching. The candor is Karpathy's, and
it is doing real work rather than hedging for form.
