# Voice guide: when-ai-breaks/galactica

## How this piece should sound

This lesson tells the story of Galactica, the science-writing model Meta
released to the public and pulled within days, and then explains why a system
built that way produces fluent falsehoods. The reader is smart, reads widely,
and is new to how these models work. Hold the plain, level register of Simon
Willison's "Hallucinations in code" from start to finish: the failure can be
reported at full seriousness without any alarm in the sentences themselves. The
authority comes from staying concrete, the way Timothy Lee spends three sentences
on adjusting a shower knob before he asks the reader to accept anything abstract.

The Galactica story invites a dramatic opening, and the material rarely needs
one. Dan Luu opens a decade of severe outages with a flat statement of what he
counted and nothing more, and the demo's first days can be told the same way,
letting what the model actually generated carry the weight that adjectives would
otherwise be asked to carry. When the piece reports what a fabricated citation or
a confident wrong answer looked like, a plain sentence lets the reader see it for
what it is, where a heightened one competes with it for attention.

The turn from what happened to why it happened is where the lesson lands, and it
can stay as unhurried as Willison naming the exact moment a hallucinated method
surfaces. The general mechanism belongs to the hallucination lesson this piece
links, so the explanation here has room to stay lean: enough for the reader to
see why a science-styled interface makes a guess read as a result, without
re-teaching the phenomenon the linked lesson owns. Where the cause is contested
or partly unknown, Lee's candor is the model, stating plainly what is not settled
rather than rounding it up to sound sure.

Name the people who built and promoted Galactica and the ones who criticized it.
Where the piece states a pattern about the model's behavior, it can pin that
pattern to what someone specifically showed or said, the way Luu attributes a
recurring cause to named analysis before he asserts it holds. A verdict on Meta's
choices is welcome once the record earns it, delivered level rather than
scolding. The short interval before Meta took the demo down is a fact; state it
and let it stand.

The lesson closes on where this weakness lives now, in the research-assistant and
answer models the reader already uses. That landing can report a present fact as
plainly as the rest of the piece reports the past, rather than widening into a
general warning about the technology.

## Simon Willison, "Hallucinations in code"

Source: https://simonwillison.net/2025/Mar/2/hallucinations-in-code/

> "A surprisingly common complaint I see from developers who have tried using LLMs for code is that they encountered a hallucination—usually the LLM inventing a method or even a full software library that doesn't exist—and it crashed their confidence in LLMs as a tool for writing code."

One measured sentence does a lot of work: it states the complaint, shows what the
hallucination looks like in practice, and reports its effect on the developer,
without speeding up or raising its voice. Willison is visible in the firsthand "I
see" and in his refusal to treat the failure as either a scandal or a dealbreaker.
He describes what happens and moves on.

> "The moment you run LLM generated code, any hallucinated methods will be instantly obvious: you'll get an error."

A short, flat sentence that explains why this failure is self-correcting by
pointing at the concrete moment it surfaces, the error, rather than grading it.
The plainness is doing the explaining. Willison trusts the fact to land on its
own instead of characterizing it for the reader.

> "A general rule for programming is that you should *never* trust any piece of code until you've seen it work with your own eye—or, even better, seen it fail and then fixed it."

He states a firm rule and then grounds it immediately in something physical,
watching the code run or fail. The voice is a working programmer's, direct and a
little impatient, and the single italicized "never" carries the emphasis with no
exclamation behind it. The standard he sets is concrete enough that a reader
could act on it.

## Timothy B. Lee, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Suppose you're going to take a shower, and you want the temperature to be just right: not too hot, and not too cold. You've never used this faucet before, so you point the knob to a random direction and feel the temperature of the water."

Lee explains an abstract idea by handing the reader a body they already have,
adjusting an unfamiliar shower knob by feel. The example is ordinary and exact,
and it does the explaining before any jargon arrives. He is visible in the
patience of it, willing to spend the sentences a faucet needs so the reader never
has to take the mechanism on trust.

> "At the moment, we don't have any real insight into how LLMs accomplish feats like this. Some people argue that examples like this demonstrate that the models are starting to truly understand the meanings of the words in their training set."

He states the limit of current knowledge in plain words, then lays out the live
disagreement instead of smoothing it over. Lee is visible in the honesty: he
would rather tell a general reader what is not known than sound more certain than
the field is. The candor makes the rest of his explaining more trustworthy, not
less.

## Dan Luu, "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "This is a collection of information on severe (`SEV-0` or `SEV-1`, the most severe incident classifications) incidents at Twitter that were at least partially attributed to cache from the time Twitter started using its current incident tracking JIRA (2012) to date (2022), with one bonus incident from before 2012."

Luu opens a piece about a decade of severe outages with a flat statement of what
he counted: the severity levels, the dates, the boundaries of the set. There is
no dramatic lede and no promise of lessons to come. The restraint is the voice,
and it lets the incidents that follow carry whatever weight they have.

> "Something else to look for is how frequently a major incident occured due to an incompletely applied fix for an earlier incident or because something that was considered a serious operational issue by an engineer wasn't prioritized. These were both common themes in the analysis Rebecca Isaacs and Dan Luu did on causes of failover test failures as well."

Here he points the reader at a recurring cause, a fix applied incompletely or a
known risk left unprioritized, and names the analysis that found the same thing
independently. The claim is strong, the delivery stays level, and he attributes
it rather than asserting it. Luu is visible in that habit of pinning a general
pattern to specific evidence before he will state that it holds.
