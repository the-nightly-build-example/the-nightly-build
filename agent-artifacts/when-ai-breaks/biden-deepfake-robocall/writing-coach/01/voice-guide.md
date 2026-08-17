> NOTE (orchestrator): this voice guide was written for a sibling lesson in the same series.
> Take its craft directions, register, and exemplar techniques. Ignore its subject-specific
> references — they belong to the sibling topic, not this article. This article's subject is set
> by this workspace's commission.md.

# Voice guide: when-ai-breaks/air-canada-chatbot (01)

## How this piece should sound

Tell the chatbot's answer and the tribunal's ruling the way Luu tells the
2011 cache incident: the date, the exact wrong claim, and what it cost the
customer, in that order, before a word about how a language model generates
text. A reader who stops after the first section should already know what
Air Canada's chatbot told the customer, what the airline's real policy said,
and what the tribunal decided — the same way a reader of Luu's incident can
stop after "their username reverted" and already have the whole opening
beat, dates and consequence, with no mechanism yet attached to it.

When the piece turns to why a chatbot like this produces a confident wrong
policy, build the chain the way Cloudberg builds the pitot tube passage:
what the system is supposed to do, what breaks, what comes out the other
end, each step hand-fed by the one before it in a plain sentence. The
mechanism here is retrieval against the airline's actual policy versus
generation that only has to sound right, and it earns the same three-step
treatment: what a grounded system does, what an ungrounded one does instead,
and what that difference produces when a customer asks about a refund.

Where the tribunal's own reasoning matters, quote it and then translate it
the way White translates the jury's two-theory verdict — "this means that"
is doing real work in her piece, turning a legal form into something a
non-lawyer can hold, and it can do the same for the tribunal's finding on
why Air Canada was liable for its own chatbot's words. Don't summarize
the ruling down to "the airline was found responsible"; the piece has room
for what the tribunal actually said about a company being answerable for a
tool it deployed.

When the piece names Air Canada's defense — that the chatbot was responsible
for its own words — report it the way White reports Bankman-Fried's face at
the verdict: externally, without editorializing about how absurd or
sympathetic the argument was. State what the airline argued and what the
tribunal did with it, and let the sequence of claim and rejection carry the
judgment.

The closing move, where this same weakness sits in systems the reader uses
today, needs a named system and a named gap the way White anchors one date
against another rather than gesturing at how common the problem supposedly
is. A customer-service, banking, or health chatbot that states a rule
without a citation to the rule is the same failure this lesson just spent a
section explaining; name one, name what it isn't grounded in, and stop
there rather than listing a genre of risk.

## Dan Luu (with Yao Yue), "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "There are a couple reasons we want to write this down. First, historical
> knowledge about what happens at tech companies is lost at a fairly high
> rate and we think it's nice to preserve some of it. Second, we think it
> can be useful to look at incidents and reliability from a specific angle,
> putting all of the information into one place, because that can sometimes
> make some patterns very obvious."

This states the piece's reason for existing in two flat, numbered claims
before a single incident is told. Neither claim asks the reader to take
importance on faith: one is about knowledge that would otherwise be lost,
the other about a pattern that juxtaposition makes visible. The writer says
what the piece is for, then the rest of the piece is exactly that and
nothing more.

> "On Nov 8, a user changed their name from [old name] to [new name]. One
> week later, their username reverted to [old name]."

Two short sentences carry an entire incident's opening beat: a date, an
action, and its reversal a week on. There's no scene-setting and no
adjective doing work — the dates and the reversal are the whole story at
this point, and the next several paragraphs earn the right to explain why
only because this sentence told the reader what happened first.

> "When we look at the incidents below, we'll see that most aren't really
> due to errors in the logic of cache, but rather, some kind of anomaly that
> causes an insufficiently mitigated positive feedback loop that becomes a
> runaway feedback loop."

This names the pattern across a dozen separately-told incidents before any
of them run, so the reader can carry it into each one. It's stated as a
finding, not tacked on as a moral once the incidents are done. "Insufficiently
mitigated positive feedback loop" is a specific enough phrase to rule out
other failure modes — a vaguer word like "unstable" would fit any of them
equally and explain none.

## Admiral Cloudberg, "The Long Way Down: The crash of Air France flight 447"

Source: https://admiralcloudberg.medium.com/the-long-way-down-the-crash-of-air-france-flight-447-8a7678c37982

> "In the early hours of the first of June 2009, Air France flight 447 from
> Rio de Janeiro to Paris disappeared in a radar dead zone over the
> mid-Atlantic. The Airbus A330 with 228 people on board had vanished into
> the night without a distress call, leaving behind little to explain its
> sudden and dramatic end."

The scene is set with only what is dated and countable: the date, the
route, the number aboard, the fact of no distress call. Those bare facts
are doing the work that an inflating adjective would only claim to do. A
reader needs exactly this before anything about causes can mean anything.

> "Each pitot tube measures the pressure of the oncoming air, which is then
> compared to the static pressure to derive the plane's airspeed. This data
> in turn is used to calculate a number of other parameters, including Mach
> number, vertical speed, and altitude, which are all displayed
> instantaneously to the pilots. But if ice crystals clog the pitot tubes,
> air cannot enter them, causing the measured pressure to drop, which in
> turn causes a decrease in indicated airspeed."

Three sentences carry a full physical chain: what the sensor measures, what
that measurement becomes, and what breaks the chain. Each sentence supplies
the term the next one needs — "this data," "But if" — so a reader with no
aviation background follows the mechanism without a diagram standing in for
the explanation.

> "But such an accusation ignores the fact that Bonin was systematically
> underprepared for the situation in which he found himself. It is easy,
> from the vantage point of 2021, living in a world where Air France flight
> 447 has become one of the most studied accidents of all time, to say that
> he should have known better. And indeed he should have, but that's not
> the point: the point is that Bonin was only a symptom of a deeper
> problem."

Having spent pages establishing exactly what one pilot did, the piece turns
here to what let him do it — without withdrawing any of the specific facts
already on the record. "He should have, but that's not the point" holds
both things true instead of trading one for the other. This is the move
from one person's error to the system that produced it, made without
softening the person's actual responsibility to get there.

## Molly White, "Sam Bankman-Fried: guilty on all charges"

Source: https://www.citationneeded.news/sam-bankman-fried-guilty-on-all-charges/

> "It took almost as long for the judge to read the charges to the jury as
> it did for the jury to find Sam Bankman-Fried guilty on all seven counts.
> The verdict was delivered a year to the day from when CoinDesk published
> the leaked balance sheet that would ultimately lead to the collapse of
> FTX, exposing the crimes that had been happening just under the surface."

The opening sentence sets two durations against each other and lets the
comparison do the work, rather than stating that the deliberation was fast.
The second sentence adds one exact date matched against another. Neither
sentence tells the reader how to feel about the speed of the verdict; the
two numbers arrange that by themselves.

> "With the seventh charge, the jury was additionally asked to determine if
> he committed concealment money laundering, wire fraud proceeds money
> laundering, or both. They checked "both". This means that they found that
> Bankman-Fried had engaged in money laundering for the purposes of
> concealing the source, nature, ownership, or location of the funds and
> that he had committed money laundering for the purposes of concealing the
> proceeds of wire fraud."

The piece is explaining a genuinely technical distinction — two named legal
theories checked on one line of a verdict form — entirely in declarative
sentences, with no term left for the reader to guess at. "This means that"
is translation, not filler: it is the sentence that turns a jury's checked
box into something a reader without a law degree can hold onto. The piece
never collapses the two theories into one to make the sentence easier.

> "Bankman-Fried reportedly showed little visible emotion as the verdict was
> read, clasping his hands while he stood to hear the verdict and then
> sitting and looking at the table after it was finished. As he left the
> courtroom, he gave a nod to his parents."

The description stays entirely external — "reportedly," hands, standing,
sitting, a nod — and never claims to know what he felt. It sits at the
piece's most dramatic possible moment and stays flat there. That restraint
is what keeps an account of a verdict from turning into courtroom drama.
