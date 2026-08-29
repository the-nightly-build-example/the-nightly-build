# Voice guide: the-mechanics/negation

## How this piece should sound

This lesson has two symptoms to open with (the sandwich that gets onions, the
image that gets an elephant) and one mechanism underneath them that the reader
has to see is the same mechanism twice. Willison's tokenizer post earns its
claims by putting a number in front of the reader before naming the cause: "The"
is 464, " the" is 262, so the point about capitalization and leading spaces is
made before it is stated. This lesson has the same option at every step:
a real prompt, its real output, and only then the sentence that explains it. A
described failure ("the model sometimes ignores negation") is not the same
sentence as a shown one, and the shown one is available here at every step
because the whole subject is reproducible in one try.

Luu's talk names all three layers he is about to walk through, and what each one
turns out to do wrong, before he explains any of them: file API, filesystem,
disk, in that order, each with its own concrete failure attached to its name in
the same sentence. This lesson's two systems, the language model and the
text-to-image model, want the same treatment: tell the reader up front that one
weakness is about to show up twice, in a token-prediction system and then in a
text-encoder system, so a reader who only skims the headings still knows there
are two stops on the way down and roughly what each one contributes. Without
that upfront naming, the image-generation half reads like a second, unrelated
lesson bolted onto the first.

Mark the settled floor the way both Evans and Luu mark theirs: by attribution
and hedge word, not by a stock disclaimer sentence at the end. Evans writes
"I'm not sure that the term 'DNS propagation' is why people like my friend end
up with an incorrect mental model" right where that particular claim gets
weaker than the ones around it, not in a closing caveat paragraph. Luu does the
same with a bare "IMO" dropped into an otherwise flat sentence. The open
question in this lesson, how much of language-model negation failure is
architecture and how much is data, is exactly this kind of claim: it belongs at
the sentence where it applies, marked as unresolved in the plainest available
words, and every step around it can still be stated flatly. Willison's glitch-
token passage does the harder version of this same move: he gives the likely
explanation, then hands the actual mechanism to a named source on Hacker News
rather than inventing a confident answer of his own. Where this lesson's chain
runs into a step nobody has fully explained, naming whose account it is (a
paper, a benchmark, a named uncertainty) does more work than a sentence that
just says the mechanism isn't fully understood.

Keep the register these three share: short declaratives, a number instead of an
adjective, and a joke only where the material earns it rather than one placed to
soften a hard sentence. None of the three writers announce that a section is
about to explain something before explaining it, and none of them close a
section by restating what it just showed. The lesson can afford the same trust:
end each step on the concrete thing it found, and let the next step's opening
line do the connecting.

## Julia Evans, "DNS 'propagation' is actually caches expiring"

Source: https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/

> "In fact, if you create a DNS record, it's possible that no DNS resolver will
> ever know about it! For example, I just created a record for a subdomain of
> jvns.ca that I will not tell you. Nobody will ever make a DNS query for that
> subdomain (I'm not going to make one, and you can't because I didn't tell you
> what it is!), so no resolver knows about it."

She proves the mechanism by doing it live in front of the reader instead of
asserting it. The parenthetical where she refuses to name the subdomain is a
small joke, but it is also the actual experiment: the joke and the proof are the
same sentence, so cutting one would cut the other.

> "One day recently I decided to actually find out why this was happening,
> found a Stack Overflow answer talking about it, and of course the answer is
> in a DNS RFC! The RFC for negative caching says that the TTL for negative
> caching is 'the minimum of the MINIMUM field of the SOA record and the TTL of
> the SOA itself'."

The sentence keeps the actual sequence of finding the answer, an annoyance, a
search, a forum post, a spec, instead of presenting the RFC's rule cold. Quoting
the RFC's own clause rather than paraphrasing it keeps the exact rule intact,
which matters here because a paraphrase would blur which field controls the
timing.

> "Of course, I'm not sure that the term 'DNS propagation' is why people like
> my friend end up with an incorrect mental model for how DNS works. That's a
> strong statement and I don't have a lot of evidence for it!"

She separates the mechanism she just demonstrated (caching) from a further claim
about why people get confused, and marks the second claim as unproven in her own
words, at the sentence where it applies, rather than softening it with a vaguer
qualifier somewhere else.

## Simon Willison, "Understanding GPT tokenizers"

Source: https://simonwillison.net/2023/Jun/8/gpt-tokenizers/

> "Note that capitalization is important here. 'The' with a capital T is token
> 464, but ' the' with both a leading space and a lowercase t is token 262."

The claim rests on two numbers a reader could look up themselves in the tool he
built. He states the mechanism, that case and a leading space each produce a
different token, through the specific integers rather than describing it in the
abstract first and illustrating it after.

> "The English bias is obvious here. ' man' gets a lower token ID of 582,
> because it's an English word. 'zan' gets a token ID of 15201 because it's not
> a word that stands alone in English, but is a common enough sequence of
> characters that it still warrants its own token."

He names the cause plainly instead of hedging it as a possibility, then backs it
immediately with the two token IDs that make the asymmetry checkable. The word
"obvious" is earned because the numbers were just shown, not asserted ahead of
them.

> "Why this happens is an intriguing puzzle. It looks likely that this token
> refers to user davidjl123 on Reddit, a keen member of the /r/counting
> subreddit. He's posted incremented numbers there well over 163,000 times.
> Presumably that subreddit ended up in the training data used to create the
> tokenizer used by GPT-2, and since that particular username showed up
> hundreds of thousands of times it ended up getting its own token. But why
> would that break things like this? The best theory I've seen so far came
> from londons_explore on Hacker News:"

He states the observation, offers the likely explanation for how the token came
to exist, and then hands the harder question, why a rare token breaks generation
the way it does, to someone else by name rather than inventing an answer of his
own. The line "why would that break things like this" marks the exact point
where his own explanation runs out.

## Dan Luu, "Files are fraught with peril"

Source: https://danluu.com/deconstruct-files/

> "In this talk, we're going to look at how file systems differ from each other
> and other issues we might encounter when writing to files. We're going to
> look at the file 'stack' starting at the top with the file API, which we'll
> see is nearly impossible to use correctly and that supporting multiple
> filesystems without corrupting data is much harder than supporting a single
> filesystem; move down to the filesystem, which we'll see has serious bugs
> that cause data loss and data corruption; and then we'll look at disks and
> see that disks can easily corrupt data at a rate five million times greater
> than claimed in vendor datasheets."

He names all three layers he is about to walk through, and what each one turns
out to do wrong, before explaining any of them. A reader always knows which
layer is currently being blamed and roughly what is still coming, because each
clause in the list ends on a concrete claim rather than a vague preview.

> "But they still can't use files safely every time! A natural follow-up to
> this is the question: why the file API so hard to use that even experts make
> mistakes?"

(Quoted exactly as published; this is an unedited talk transcript and the
sentence carries a small dropped word.) He earns the question by first showing
that experts, not just beginners, fail at this, so the "why" that follows is not
rhetorical filler asked before there is any reason to ask it.

> "In conclusion, computers don't work (but you probably already know this if
> you're here at Gary-conf). This talk happened to be about files, but there
> are many areas we could've looked into where we would've seen similar
> things. One thing I'd like to note before we finish is that, IMO, the
> underlying problem isn't technical."

The joke in the first sentence and the hedge "IMO" three sentences later come
from the same voice: he will overstate for effect, then immediately mark the
next claim as his own read rather than something the talk demonstrated. Putting
the two moves close together keeps the reader oriented on which claims were
shown and which are his opinion.
