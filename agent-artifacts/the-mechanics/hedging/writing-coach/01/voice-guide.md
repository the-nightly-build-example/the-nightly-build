# Voice guide: the-mechanics/hedging (01)

## How this piece should sound

Willison's contrast between a one-line claim and the paragraph of
self-corrections around it is the move to borrow, not the persona. This lesson
can open on a real hedge, drawn from an actual chatbot answer and quoted or
closely described, and name what it is doing in one plain sentence before
explaining why the model produced it. That single sentence gives the reader
something concrete to hold while the mechanism gets explained, the way
Willison's plain claim gives the reader something to measure his tangle of
qualifiers against.

Evans marks the exact point where her certainty runs out: "I can't figure
out," "I'm not sure," "my best guess," and the chain keeps moving past it
anyway. The hedging chain has the same shape. Base-rate completion and
reward-model optimization toward rater preferences are established mechanisms;
how much each stage contributes, and whether a given hedge is deliberate
policy or overshoot, is not. Marking that boundary belongs in the sentence
where the chain reaches it, and a step can stay open there instead of getting
rounded up to a finding the sources don't support.

Yong's "This account is what should happen... but what actually happens?" line
does something specific: it states the textbook mechanism plainly, then holds
the observed behavior up against it and shows where they part. The three-step
chain from next-token completion to reward-model shaping to explicit
safety-and-helpfulness tuning is exactly this kind of layered account, and each
layer can get its own version of that turn: here is what the mechanism should
produce, here is what a hedge in the wild actually looks like, here is where
they match and where they don't.

None of the three writers switch metaphors mid-explanation. Evans stays with
bytes and words; Yong stays with the lymph-node mercenaries once he's introduced
them. A single concrete example, reused rather than replaced, can carry a step
of the hedging chain the same way, whether that's one real hedged answer
followed all the way from prompt to output, or one plain restatement of the
same question a confident answer would have given.

The line this piece has to hold that none of the three exemplars had to: a
hedge withholds a stance the model could take regardless of what the user
wants to hear, while sycophancy reverses a stance because the user pushed.
Drawing that boundary is itself an act of naming precisely, in the reader's own
terms, and it can happen at the point in the chain where a reader would
otherwise conflate the two.

## Simon Willison, "We need to tell people ChatGPT will lie to them, not debate linguistics"

Source: https://simonwillison.net/2023/Apr/7/chatgpt-lies/

> "I completely agree that anthropomorphism is bad: these models are fancy
> matrix arithmetic, not entities with intent and opinions. But in this case, I
> think the visceral clarity of being able to say "ChatGPT will lie to you" is
> a worthwhile trade."

Willison states the objection to his own claim before he answers it, in the
same breath, rather than letting a reader raise it later. The concession costs
him nothing because he's already decided which claim he's defending. That
ordering, objection first and stated in its strongest form, then the plain
claim, is where the writer is visible: someone who has already had this
argument with himself.

> "Which of these two messages do you think is more effective? ChatGPT will
> lie to you. Or ChatGPT doesn't lie, lying is too human and implies intent. It
> hallucinates. Actually no, hallucination still implies human-like thought. It
> confabulates. That's a term used in psychiatry to describe when someone
> replaces a gap in one's memory by a falsification that one believes to be
> true—though of course these things don't have human minds so even
> confabulation is unnecessarily anthropomorphic. I hope you've enjoyed this
> linguistic detour! Let's go with the first one."

He doesn't tell the reader that hedged language is exhausting to read; he
writes four sentences of it, each one correcting the last, and lets the reader
feel the exhaustion directly. The plain sentence on either side of that
paragraph is what makes the demonstration legible as a demonstration and not
just a digression.

> "These are incredibly powerful tools. They are far harder to use effectively
> than they first appear. Invest the effort, but approach with caution: we
> accidentally invented computers that can lie to us and we can't figure out
> how to make them stop."

Three short sentences, each doing one job: what the tools are, why they're
hard, what to do about it. Nothing here oversells the danger or undersells the
usefulness in the same breath a lesser version of this paragraph would use to
hedge between them.

## Julia Evans, "Some possible reasons for 8-bit bytes"

Source: https://jvns.ca/blog/2023/03/06/possible-reasons-8-bit-bytes/

> "There aren't any definitive answers in this post, but I asked on Mastodon
> and here are some potential reasons I found for the 8-bit byte. I think the
> answer is some combination of these reasons."

This sentence sets the reader's expectations for the entire piece before the
mechanism starts: several partial causes, not one clean answer. Evans says this
once, near the top, instead of hedging every claim that follows it. The reader
knows from here what kind of answer they're getting.

> "I don't understand this comment at all – why does the exponent have to be 8
> bits if you use a 32-bit word size? Why couldn't you use 9 bits or 10 bits if
> you wanted? But it's all I could find in a quick search."

She reports the limit of her own research inside the paragraph where it
happened, in first person, rather than smoothing it into a general caveat
later. A reader can see exactly which claim she's not vouching for, because she
names it at the moment she hits it.

> "A bunch of people said it's important for a CPU's byte size to be a power of
> 2. I can't figure out whether this is true or not though, and I wasn't
> satisfied with the explanation that "computers use binary so powers of 2 are
> good". That seems very plausible but I wanted to dig deeper."

A plausible-sounding explanation doesn't get accepted just because it sounds
plausible. Evans names the explanation, says why it isn't enough, and keeps
going, which is a different thing from either rejecting it outright or
repeating it as settled.

## Ed Yong, "The Pandemic's Biggest Mystery Is Our Own Immune System"

Source: https://www.theatlantic.com/health/archive/2020/08/covid-19-immunity-is-the-pandemics-central-mystery/614956/

> "It works, roughly, like this. The first of three phases involves detecting a
> threat, summoning help, and launching the counterattack. It begins as soon as
> a virus drifts into your airways, and infiltrates the cells that line them."

"Roughly" is doing real work in that first sentence: it tells the reader a
simplified, ordered account is coming before it arrives, so the ordering itself
doesn't have to be defended later. Each sentence after it names one action and
moves to the next; nothing is explained twice.

> "This account is what should happen when the new coronavirus enters the
> body, based on general knowledge about the immune system and how it reacts
> to other respiratory viruses. But what actually happens? Well … sigh … the
> thing is, the immune system is very complicated."

Yong states the textbook model as a model, not as the finding, and then asks
the question that separates it from the observed reality. The sigh is the one
place he lets his own reaction show, and it lands precisely because everything
around it is measured.

> "'You can go pretty crazy pretty quickly with the speculations,' says Crotty,
> who co-led one of the studies that identified these cross-reactive cells. 'A
> lot of people have latched onto this and said it could explain everything.
> Yes, it could! Or it could explain nothing. It's a really frustrating
> situation to be in.'"

The uncertainty is attributed to the researcher who lived it, in his own
words, rather than delivered in Yong's narrating voice. That choice keeps the
open question honestly open: a source saying "it's frustrating" carries a
different weight than a writer saying "the answer is unclear."
