# Voice guide: the-evidence/mixture-of-experts

## How this piece should sound

This lesson reads one 2017 paper on sparse mixture-of-experts and shows a reader
who is smart, widely read, and new to neural-network architecture two things:
what routing a token to a few experts actually does, and why a model's
advertised parameter count is larger than the number of parameters that run for
any single token. Hold the register plain and unhurried. Claims are stated
straight, the concrete is reached for before the abstract, and no term of the
field is used before the lesson has built it.

Routing is the hardest thing in the piece to picture, and the Willison and Olah
passages below show two ways to keep it followable. Willison introduces
embeddings by handing the reader the smallest concrete instance and one property
of it, with real numbers, before any talk of scale. When the gate first appears
here, the reader may be best served by the same smallest version: one token
arriving, the gate scoring the experts, a few of them chosen to run. Olah keeps
the meaning of the numbers fastened to the picture, so his gate that passes some
signal and holds the rest says what a zero and a one mean as it describes them.
The gating step in this paper decides which experts a token visits, and it can
be shown the same way, as a plain choosing with the numbers still attached.

An abstract point lands faster after a concrete case the reader can hold, the way
Olah's France sentence creates the need for long-term memory before the machinery
has a name. Why route at all, why not run every expert on every token, is the
kind of question a concrete instance can raise a beat before the answer arrives.

The correction at the center of the lesson is a question of which quantity a
number counts, and Luu's opening is the closest model for it. He spends a
paragraph fixing which population a percentile is measured against, because the
figure is honest only once its denominator is named. The advertised parameter
count and the parameters active for one token are different quantities, and the
lesson can pin down exactly which one a headline number is reporting. The larger
number is accurately measured; it counts something other than what runs per
token, and the piece can say that in plain words.

Keep the correction even. Luu includes himself in the mistake he is describing,
and the honest number here can be set straight without any contempt for the
people and companies that quote the larger one. A figure the reader cannot scale
on their own needs a comparison they already hold. A parameter count in the
billions, or the compute a token actually spends, means little until it sits
beside something the reader can measure it against.

Willison says outright that nobody fully understands what the individual numbers
mean. Where this paper's mechanism resists that kind of plain reading, where why
a token routes to a given expert cannot be stated cleanly, the lesson loses
nothing by admitting it in the same voice it uses for everything else.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "Embeddings are based around one trick: take a piece of content—in this case a blog entry—and turn that piece of content into an array of floating point numbers.
>
> The key thing about that array is that it will always be the same length, no matter how long the content is. The length is defined by the embedding model you are using—an array might be 300, or 1,000, or 1,536 numbers long."

Willison names the mechanism as "one trick" and immediately gives a concrete
case, a blog entry, then the single property that matters: the array is always
the same length, and he supplies the real lengths. He explains by handing over
the object and one fact about it, not a definition. The plainness is a choice,
and you can hear him deciding the reader is owed the actual thing.

> "Why place content in this space? Because we can learn interesting things about that content based on its location—in particular, based on what else is nearby.
>
> The location within the space represents the semantic meaning of the content, according to the embedding model's weird, mostly incomprehensible understanding of the world. It might capture colors, shapes, concepts or all sorts of other characteristics of the content that has been embedded.
>
> Nobody fully understands what those individual numbers mean, but we know that their locations can be used to find out useful things about the content."

He asks the plain question the reader would ask and answers it before reaching
for any vocabulary. Then he states outright that nobody fully understands what
the numbers mean. Naming the limit in the same breath as the use is what keeps
the explanation trustworthy, and telling you where his own understanding stops is
a habit of Willison's.

> "Take the vector for "germany", add "paris" and subtract "france". The resulting vector is closest to "berlin"!
>
> Something about this model has captured the idea of nationalities and geography to the point that you can use arithmetic to explore additional facts about the world."

The example is fully worked and checkable: germany plus paris minus france lands
near berlin. He states the result flatly, then draws the modest, exact
conclusion and stops. The restraint after a surprising result is Willison being
careful not to oversell what it proves.

## Chris Olah, "Understanding LSTM Networks"

Source: https://colah.github.io/posts/2015-08-Understanding-LSTMs/

> "The key to LSTMs is the cell state, the horizontal line running through the top of the diagram.
>
> The cell state is kind of like a conveyor belt. It runs straight down the entire chain, with only some minor linear interactions. It's very easy for information to just flow along it unchanged."

Olah gives the cell state a physical image, a conveyor belt, and then states the
plain consequence: information can flow along it unchanged. The image is doing
real explanatory work, because the sentences that follow depend on it. He picks
the one picture that makes the rest of the mechanism followable.

> "Gates are a way to optionally let information through. They are composed out of a sigmoid neural net layer and a pointwise multiplication operation.
>
> The sigmoid layer outputs numbers between zero and one, describing how much of each component should be let through. A value of zero means "let nothing through," while a value of one means "let everything through!""

He describes the gate as a way to let information through, then keeps the meaning
of the numbers attached to it: zero lets nothing through, one lets everything.
The math, a sigmoid and a multiplication, is named in plain words and then
grounded at once in what the numbers do. Olah never lets the notation float free
of its meaning.

> "But there are also cases where we need more context. Consider trying to predict the last word in the text "I grew up in France… I speak fluent French." Recent information suggests that the next word is probably the name of a language, but if we want to narrow down which language, we need the context of France, from further back."

Before naming any machinery, Olah gives a sentence the reader can finish
themselves: the last word of "I grew up in France... I speak fluent French." The
concrete case creates the need for the mechanism, so the mechanism then arrives
as the answer to a question the reader already feels. He motivates before he
defines.

## Dan Luu, "95%-ile isn't that good"

Source: https://danluu.com/p95-skill/

> "Note that when I say 95%-ile, I mean 95%-ile among people who participate, not all people (for many activities, just doing it at all makes you 99%-ile or above across all people). I'm also not referring to 95%-ile among people who practice regularly. The "one weird trick" is that, for a lot of activities, being something like 10%-ile among people who practice can make you something like 90%-ile or 99%-ile among people who participate."

Luu spends a whole paragraph pinning down which population the percentile is
measured against, because the same number means different things depending on
the denominator. He gets the quantity exact before he argues about it. That
carefulness is why his later claims are hard to wave away.

> "At 90%-ile and 95%-ile ranks in Overwatch, the vast majority of players will pretty much constantly make basic game losing mistakes. These are simple mistakes like standing next to the objective instead of on top of the objective while the match timer runs out, turning a probable victory into a certain defeat."

The claim rests on a concrete, checkable case: at these ranks players stand next
to the objective instead of on it and lose a match they would have won. He gives
the specific mistake and its specific cost rather than asserting that the players
are bad. The argument is built from something a reader could go and watch.

> "The answer is, of course, that the person asking the question is also doing obviously stupid game-losing things all the time because anyone who doesn't constantly make major blunders wins too much to stay at 95%-ile. This also applies to me."

Luu corrects a widely held belief and puts himself inside the correction: the
player complaining about bad teammates is making the same mistakes, and so is
Luu. The evenness is what makes the correction land, because he is not scoring a
point against the people who are wrong. He states the fact and takes his own
share of it.
</content>
