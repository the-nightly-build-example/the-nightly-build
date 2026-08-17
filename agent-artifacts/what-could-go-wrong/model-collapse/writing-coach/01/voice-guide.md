> NOTE (orchestrator): this voice guide was written for a sibling lesson in the same series.
> Take its craft directions, register, and exemplar techniques. Ignore its subject-specific
> references — they belong to the sibling topic, not this article. This article's subject is set
> by this workspace's commission.md.

# Voice guide: what-could-go-wrong/reward-hacking (01)

## How this piece should sound

Open the way Timothy B. Lee opens on Yudkowsky: state the easy dismissal, then
take it away with something specific and checkable. The lesson has a real
version of that move sitting in its own brief. The objector who says this
worry is just science fiction can be answered by naming the person who worried
about it before "AI" meant anything, and what they had actually watched
happen. A date and a named case do that work. A sentence asserting that the
concern "predates modern AI" does not, and reads as the throat-clearing Lee's
paragraph never needs.

Lee also converts Yudkowsky's argument into three discrete, numbered claims
before saying which one he doubts. Reward hacking has the same shape available
to it: the gap between the objective as specified and the outcome as intended
is one claim, that the gap is hard to close is a second, and that it gets more
costly as systems get more capable is a third. Naming them separately, the way
Lee's numbered list does, lets the later test land on the specific claim the
evidence actually speaks to. Krakovna-style catalogued gaming and RLHF
sycophancy bear on the first claim directly and say much less, on their own,
about the third. A verdict delivered against "the argument" in general, rather
than against the premise the evidence actually tests, is the harder sentence to
earn and the easier one to get wrong.

When the demonstrated cases show up, an agent finding a bug that inflates its
score, a model learning to tell people what they want to hear because that is
what got rewarded, use Dan Luu's move of setting the case directly next to the
claim it's supposed to test and letting the reader see the fit, rather than
narrating the lesson at the end. Luu never tells the reader that a hospital
death and a broken build are "the same problem": he puts the anesthesiologist's
disabled alarm next to the postmortem detail and trusts the parallel to be
visible. A worked case for this lesson earns its place the same way. State
what the system was told to optimize, and exactly what it did instead, plainly
enough that the reader sees the divergence without being told what to conclude
from it.

The line between demonstrated and speculative is where this piece can borrow
most directly from Kelsey Piper's habit of conceding before claiming. Her
sentence on Waymo data states what's unknown first and the actual position
second, so the position lands as no more certain than the evidence supports.
Reward-model overoptimization studies and catalogued specification-gaming
behavior are the "we know this much" side of that sentence. A future system
using a reward hack to seize resources is not, and the piece is more honest
using her sentence order, the concession before the claim, than reaching for a
hedge that quietly drops the claim altogether. The same contrast move she uses
against the "we don't know" line in the Waymo piece, ordinary phrasing against
the sentence that deflates it, works equally well against an overclaim of
doom and an underclaim of dismissal. This piece has both to weigh, not just
one.

Whichever named advocate the present-day section quotes, someone arguing for
better oversight, someone content with today's mitigations, give them Lee's
treatment of Yudkowsky before testing them: the reason a reasonable person
could hold this position, stated in terms specific enough that the position is
recognizable to someone who holds it, not a version built to be easy to test
against. The commission's rule against naming a lab as an authority holds here
too. The researchers and the papers carry the argument, not the companies that
employ them.

## Dan Luu, "Normalization of deviance"

Source: https://danluu.com/wat/

> The data are clear that humans are really bad at taking the time to do
> things that are well understood to incontrovertibly reduce the risk of rare
> but catastrophic events. We will rationalize that taking shortcuts is the
> right, reasonable thing to do. There's a term for this: the normalization of
> deviance.

This sentence arrives after six anecdotes, not before them, so the claim is
paid for before it's made. Luu names the exact behavior (rationalizing
shortcuts) and only then attaches the field's term for it, and he says
outright that the term is borrowed rather than his own coinage. The move is
concrete case first, label second. It is never the reverse.

> Turning off or ignoring notifications because there are too many of them
> and they're too annoying? An erroneous manual operation? This could be
> straight out of the post-mortem of more than a few companies I can think
> of, except that the result was a tragic death instead of the loss of
> millions of dollars.

He sets an unrelated engineering failure (ignored alerts) directly against a
hospital death and lets the two questions do the comparing, rather than
asserting that they're "the same problem." Nothing here softens what happened
to the patient to make the analogy comfortable, and nothing inflates the tech
postmortem to match its stakes.

> Google didn't go from adding z to the end of names to having the world's
> best security because someone gave a rousing speech or wrote a convincing
> essay. They did it after getting embarrassed a few times, which gave people
> who wanted to do things "right" the leverage to fix fundamental process
> issues.

He answers "how did this organization get good at this" by naming the actual
mechanism, embarrassment rather than persuasion, instead of a tidy lesson. The
sentences right after this passage go on to say the change was brutal and met
real political pushback, so the credit given here is immediately qualified by
its cost rather than left to stand as a clean success story.

## Kelsey Piper, "We absolutely do know that Waymos are safer than human drivers"

Source: https://www.theargumentmag.com/p/we-absolutely-do-know-that-waymos

> "We don't know" sounds like a modest claim, but in this case, where it
> refers to something that we do in fact know about an effect size that is
> extremely large, it's a really big claim.

The sentence works by contrast rather than by piling on adjectives: "sounds
like" against "we do in fact know," and the deflating turn in the last clause.
She isn't disputing that gaps in the data exist; she's disputing the
rhetorical weight a hedge is being asked to carry, and she says exactly that.

> Imagine someone writing "we don't know if airplanes are safe — some people
> say that crashes are extremely rare, and others say that crashes happen
> every week." And when you investigate this claim further, you learn that
> what's going on is that commercial aviation crashes are extremely rare,
> while general aviation crashes — small personal planes, including ones you
> can build in your garage — are quite common.

She writes the confused position in something close to its own voice before
showing what it's confusing, which makes the flaw visible on the page instead
of asserted. The analogy borrows an intuition the reader already trusts
(commercial versus garage-built aviation) to make legible one they don't yet
have settled.

> We don't have perfect information, but we are not in a state of perfect
> ignorance either — and we're frankly much closer to the perfect information
> state than the perfect ignorance state.

The concession comes first, the actual position second, so the position lands
as no more certain than the evidence supports and no less. Neither the
alarmed reading nor the dismissive one gets the sentence's last word by
default.

## Timothy B. Lee, "The case for AI doom isn't very convincing"

Source: https://www.understandingai.org/p/the-case-for-ai-doom-isnt-very-convincing

> Normally, when someone predicts the literal end of the world, you can write
> them off as a kook. But Yudkowsky is hard to dismiss. He has been warning
> about these dangers since the early 2010s, when he (ironically) helped get
> some of the leading AI companies off the ground. Legendary AI researchers
> like Geoffrey Hinton and Yoshua Bengio take Yudkowsky's concerns seriously.

He states the easy dismissal and then takes it away with specific, checkable
facts: a decade, a named role in starting the AI companies he now warns
about, two credentialed researchers by name. None of that is a general appeal
to authority. By the end of the paragraph the reader can't mistake what comes
next for an argument against a fringe position.

> So is Yudkowsky right? In my mind, there are three key steps to his
> argument:
>
> 1. Humans are on a path to develop AI systems with superhuman intelligence.
> 2. These systems will gain a lot of power over the physical world.
> 3. We don't know how to ensure these systems use their power for good
>    rather than evil.

He converts a book-length argument into three discrete, checkable claims
before saying which one he doubts. A few paragraphs later he names "the
weakest link" as the second claim specifically, not the argument as a whole.
Doubt is aimed at one load-bearing premise, and the other two are left
standing.

> The real world is a lot messier. There's a military aphorism that "no plan
> survives contact with the enemy." Generals try to anticipate the enemy's
> strategy and game out potential counter-attacks. But the battlefield is so
> complicated — and there's so much generals don't know prior to the battle —
> that things almost always evolve in ways that planners don't anticipate.

The aphorism isn't decoration; it's the concrete case that makes an abstract
claim (complex systems resist perfect prediction) checkable against something
the reader already half-knows. He explains the mechanism, planners are
missing information so outcomes diverge, rather than citing the case and
moving on.
