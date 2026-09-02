# Voice guide: when-ai-breaks/bard-jwst-demo

## How this piece should sound

This lesson tells one dated sequence — Google published a promotional answer,
the answer was false, astronomers and reporters said so, Alphabet's stock
moved — and then explains one mechanism. Both halves want the same discipline:
state what happened, in order, and let the facts carry the weight they already
have. Nothing here needs a bigger word than the record supports, because the
record is already enough.

Tell the Bard/JWST sequence the way Dan Luu and Yao Yue tell each Twitter
cache incident: date every beat and name who did what, one fact at a time,
without building toward the failure as a reveal. "On Nov 8, a user changed
their name... One week later, their username reverted" does its job because
each sentence stops at the fact it's carrying. The promotional post, the
astronomers' correction, Google's statement, and the market move can be laid
down the same way: dated, attributed, and left alone.

When the piece explains why a fluent model produced a false sentence, compress
it the way Feynman compresses years of O-ring certification history into a
page, rather than re-deriving the mechanism from nothing. The brief already
points to hallucination and false confidence as taught ground to link, not
reteach; the craft move is the same one Feynman uses on the reader who does
not know turbopumps — state the operative fact once, in words that reader
already has, and move to what it means.

Let the reported market-value figure do its own work, the way Doug Seven lets
"$460 million loss in 45-minutes" do its own work in the Knight Capital story:
say the number, say it is reported, and do not stand an adjective next to it
to tell the reader how to feel about it.

Hold off assigning the failure to any one person at Google. Doug Seven's own
move — "the engineer(s) who deployed SMARS are not solely to blame here" —
locates the fault in what let a piece of dead code run unchecked, not in
whoever touched it last. The same question is available here: what let an
unverified sentence ship in a launch demo, not who typed it.

If the piece reaches for a comparison to make "sounds right is not is right"
concrete, earn it the way Feynman earns the Russian-roulette line: only after
the mechanism has already been shown, and only the once. A comparison that
arrives before the reader has the mechanism is doing the mechanism's job for
it.

Prefer the boring explanation to the dramatic-sounding one, in the spirit of
Dan Luu and Yao Yue's observation that viral tech stories are usually wrong
"for banal reasons." Where the record supports a duller account of why the
error reached a launch demo unchecked, that account is worth more than a
livelier one the record doesn't quite support.

The series prompt asks this lesson to close on where the same weakness lives
today, in tools the reader actually uses. That close is this article's own to
earn — no exemplar here supplies it — but it can hold the same register as the
opening: dated where it can be, plain about what is reported versus what is
inferred, and no larger than the paragraph in front of it.

## Dan Luu and Yao Yue, "A Decade of Major Cache Incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "On knowledge loss, when we've seen viral Twitter threads or other viral
> stories about what happened at some tech company, when we look into what
> happened, the most widely spread stories are usually quite wrong, generally
> for banal reasons. One reason is that outrageously exaggerated stories are
> more likely to go viral, so those are the ones that tend to be remembered."

This is the essay's reason for existing, stated as a plain claim rather than a
complaint: sensational versions of an incident spread faster than accurate
ones, so the accurate version has to be written down on purpose. The writers
are visible in the choice to name the mechanism (virality selects for
exaggeration) instead of just asserting that people get it wrong.

> "On Nov 8, a user changed their name from [old name] to [new name]. One
> week later, their username reverted to [old name]. Between Nov 8th and
> early December, tens of these tickets were filed by support agents. Twitter
> didn't have the instrumentation to tell where things were going wrong, so
> the first two weeks of investigation was mostly getting metrics into the
> rails app to understand where the issue was coming from."

Every sentence here adds one dated fact and stops. There's no foreshadowing of
how bad it gets and no editorializing about the delay; the writers trust the
timeline itself to convey how hard the bug was to see. The restraint is
visible in what's left out — no adjective describes the two weeks of blind
investigation, the two weeks itself does.

> "The trigger for this incident was power loss in two rows of racks. In
> terms of the impact on cache, 48 hosts lost power and were restarted when
> power came back up, one hour later. 37 of those hosts had their caches fail
> to come back up because a directory that a script expected to exist wasn't
> mounted on those hosts."

This explains a cascading failure in three sentences, each one handing off a
number to the next: 48 hosts, one hour, 37 of them. The writers are visible in
the choice to keep counting instead of summarizing — the specificity is the
explanation.

## Doug Seven, "Knightmare: A DevOps Cautionary Tale"

Source: https://dougseven.com/2014/04/17/knightmare-a-devops-cautionary-tale/

> "This story is true – this really happened. This is my telling of the story
> based on what I have read (I was not involved in this). This is the story
> of how a company with nearly $400 million in assets went bankrupt in
> 45-minutes because of a failed deployment."

The opening states the stakes once, flatly, and immediately discloses the
limits of the writer's own knowledge of it. Seven is visible in that
disclosure: he is telling a story he wasn't present for, and says so before
telling it, rather than writing it as if he had watched it happen.

> "At 9:30 AM Eastern Time on August 1, 2012 the markets opened and Knight
> began processing orders from broker-dealers on behalf of their customers
> for the new Retail Liquidity Program. The seven (7) servers that had the
> correct SMARS deployment began processing these orders correctly. Orders
> sent to the eighth server triggered the supposable repurposed flag and
> brought back from the dead the old Power Peg code."

Three sentences move from the market opening to the specific server
misbehaving, each one narrower than the last. The one bit of personality —
"brought back from the dead" — lands because everything around it is so
plain; a single loose phrase reads as wit surrounded by precision instead of
as reaching for effect.

> "The engineer(s) who deployed SMARS are not solely to blame here – the
> process Knight had set up was not appropriate for the risk they were
> exposed to."

After forty-five minutes of a company's near-collapse, this sentence
declines to name a person responsible and instead names a process. Seven is
visible in the choice of subject: not "someone made a mistake" but "the
process was not appropriate," which is a harder and less satisfying sentence
to write than the blame it declines to assign.

## Richard Feynman, "Personal Observations on Reliability of Shuttle"

Source: https://www.nasa.gov/history/rogersrep/v2appf.htm

> "The fact that this danger did not lead to a catastrophe before is no
> guarantee that it will not the next time, unless it is completely
> understood. When playing Russian roulette the fact that the first shot got
> off safely is little comfort for the next."

The comparison arrives only after several paragraphs establishing exactly what
wasn't understood about O-ring erosion; it isn't decoration, it's the payoff
of an argument already made. Feynman is visible in choosing the plainest
possible image for a repeated near-miss rather than a technical description
of probability.

> "Official management, on the other hand, claims to believe the probability
> of failure is a thousand times less. One reason for this may be an attempt
> to assure the government of NASA perfection and success in order to ensure
> the supply of funds. The other may be that they sincerely believed it to be
> true, demonstrating an almost incredible lack of communication between
> themselves and their working engineers."

Feynman gives management's confidence two possible explanations, one closer
to bad faith and one closer to honest self-deception, and does not choose
between them for the reader. He's visible in offering the more charitable
explanation at all, in a report that could have simply accused.

> "For a successful technology, reality must take precedence over public
> relations, for nature cannot be fooled."

The report's last sentence carries weight because nothing before it has used
language this flat and final; every other page is qualified, sourced, and
hedged the way engineering writing has to be. Feynman is visible in saving the
one unqualified sentence in the whole document for the very end.
