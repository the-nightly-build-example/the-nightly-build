# Voice guide: the-mechanics/agent-loops (01)

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When I finally learned how to troubleshoot DNS problems, my reaction was
> "what, that was it???? that's not that hard!". I felt a little bit cheated!
> I could explain to you everything that I found confusing about DNS in a
> few hours."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

The reaction is her own irritation, not a general claim about DNS: "I felt a
little bit cheated" names a specific feeling with a specific cause. She
commits to a real number, "a few hours," instead of a vaguer claim like "not
that long," which tells the reader exactly how large the gap between DNS's
reputation and the actual material turned out to be.

> "When you make a DNS request on your computer, the basic story is:
>
> 1. your computer makes a request to a server called resolver
> 2. the resolver checks its cache, and makes requests to some other servers
>    called authoritative nameservers"

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

A service most readers only meet through its symptoms gets reduced to two
named actors with one job apiece. Numbering it as a two-step story instead of
folding it into a paragraph makes each actor's job something the reader can
check on its own before the piece adds a third.

> "It took me probably 5 years to realize that I shouldn't visit a domain
> that doesn't have a DNS record yet, because then the nonexistence of that
> record will be cached, and it gets cached for HOURS, and it's really
> annoying."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-26

The number is exact and personal ("probably 5 years") rather than a round
complaint about DNS in general, and the consequence is stated in plain,
domestic terms ("cached for HOURS, and it's really annoying") instead of in
severity language. That combination is what makes a years-long confusion
read as a specific anecdote rather than a grievance against the field.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "Embeddings are based around one trick: take a piece of content—in this
> case a blog entry—and turn that piece of content into an array of floating
> point numbers. The key thing about that array is that it will always be
> the same length, no matter how long the content is."

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

The definition runs on a single verb, "turn... into," so there is exactly
one mechanism to track before anything else is added. The two claims that
follow, that the length never changes and that a model sets it, are stated
as facts a reader could go check, not as qualities the reader is being told
to be impressed by.

> "Nobody fully understands what those individual numbers mean, but we know
> that their locations can be used to find out useful things about the
> content."

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

He states a limit on what anyone knows in the same flat register as a fact
he's sure of, so the gap in understanding doesn't get dressed up as mystery.
Nothing in the sentence tells the reader how to feel about the not-knowing;
it just says what's established and what isn't, side by side.

> "Take the vector for "germany", add "paris" and subtract "france". The
> resulting vector is closest to "berlin"!"

Checked: https://simonwillison.net/2023/Oct/23/embeddings/, retrieved 2026-09-26

The demonstration is one arithmetic operation on three named things, and the
payoff arrives inside the same sentence as the operation instead of after a
build-up. The exclamation point is earned by an actual, checkable result,
not attached to the writer's own excitement about it.

## Bartosz Ciechanowski, "GPS"

Source: https://ciechanow.ski/gps/

> "We'll start by creating a positioning system that can tell us where we
> are. Our initial approach will be quite simple, but we'll step-by-step
> improve upon it to build an understanding of the positioning method used
> by GPS."

Checked: https://ciechanow.ski/gps/, retrieved 2026-09-26

He states the shape of the whole piece as a method before a single mechanism
has been introduced: build something simple, then improve it. That sentence
commits him to showing where the simple version breaks, and to treating the
breakage as the reason the next version exists.

> "With two distance measurements there are only two possible positions on
> the map where we could be located. Measuring distance to the third
> landmark narrows down that location to just a single choice."

Checked: https://ciechanow.ski/gps/, retrieved 2026-09-26

Each added measurement is given a precise effect on the number of possible
answers, two positions, then one, instead of a general claim about
increasing accuracy. The count does the work of showing why a third
landmark earns its place; nothing here has to call the method elegant.

> "Fortunately, we can solve this problem by flipping it on its head.
> Instead of the users sending audio signals to the landmarks, we'll have
> the landmarks emit the sounds and have the users listen to those sounds."

Checked: https://ciechanow.ski/gps/, retrieved 2026-09-26

The fix is stated as a single reversal of who does what, not a new
component bolted onto the old one. "Fortunately" is the only note of relief
in the passage, and it's attached to an actual redesign that the previous
paragraph already earned by naming the old design's specific flaw.

## How this piece should sound

Write plain, declarative sentences that each commit to exactly one
mechanism, the way Willison's "Embeddings are based around one trick"
commits to one verb before anything else gets added. When the piece names a
part of the system, give it a job in the same sentence and use only that
name for it afterward, the way Evans's two-step DNS story keeps "resolver"
and "authoritative nameserver" as the only two actors in that scene. A
reader should be able to point at a sentence and say which named part it is
about.

Ciechanowski's shape is a fair model for a piece that argues backward from a
familiar behavior to its mechanism: state the simplest version of why an
agent might repeat a failed step, let that version have a specific,
nameable flaw, and only then bring in the part of the system that the flaw
requires. A flaw earns the next layer; the next layer should not appear
because the piece has more to say. Where a fix or a limit is worth stating
plainly, a reversal like his "flipping it on its head" line, stated once
directly, may do more than a paragraph of qualification.

Numbers belong at the joints, not as texture. Ciechanowski's "two positions,
then one" and Evans's "cached for HOURS" both let a specific count or a
specific unit of time carry a claim that would otherwise need an adjective.
Where the piece can say how many retries, how much context, or how long a
cache or a window lasts, that number can replace words like "briefly" or
"a lot."

Willison's "nobody fully understands what those individual numbers mean"
is a plain way to mark a step as an open question without turning it into
suspense: state what's known and what isn't in the same sentence, in the
same tone. The series prompt asks that settled engineering and open
questions be told apart; this is one honest way to do it without a hedge
word doing the separating.

Personality can enter through a specific, dated reaction rather than a
general claim about how confusing or fascinating the subject is. Evans's
"I felt a little bit cheated" and her "probably 5 years" both locate the
feeling in one person's experience with one exact number attached. A
sentence that generalizes the reader's own probable frustration ("anyone
who's watched this happen knows how maddening it is") does less work than
one that states a specific reaction and lets the reader recognize it or
not.
