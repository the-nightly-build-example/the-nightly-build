# Voice guide: the-mechanics/overused-words

## How this piece should sound

This lesson takes a reader from something they have seen, chatbots reaching for
the same few words, back to what in the system produces it, stopping at each real
part along the way. The reader is quick and widely read but has never seen the
inside of one of these systems. Name every part in plain words the moment it is
used, the way Julia Evans names the resolver, its cache, and the authoritative
nameservers before she leans on any of them. A reader will follow a cause laid
out part by part and lose the thread at the step that is skipped, so keep the
chain unbroken and give each named part visible work to do.

The spine of the piece is measurement. Treat the frequency numbers the way Mark
Liberman treats his: give the figure, and say how it was obtained. When he calls
a trend "measured crudely by frequency in the Medline corpus," the reader learns
how much weight the graph can bear before being asked to stand on it. The words
readers point to are a real, counted thing in this lesson, so report them with
their numbers rather than as a general impression.

Most of the causal chain is settled and one link is not, and the reader should be
able to tell which is which. McCulloch shows the move: she lines up a
correlation, says plainly "It might be coincidence, but it might also be," then
states what the evidence does support and why. Where a step is established, say
so flatly. Where it is a leading guess, mark it as a guess in the same plain
voice, without setting it aside in a labeled box of its own. Evans does the
small-scale version when she admits she does not have as good an answer as she
would like, and that admission reads as more trustworthy than a filled-in one
would.

The subject is words, which tempts a piece into doing the thing it describes. Two
guards hold against it. The writing should not turn into a display of the words
it is about; bring one in where it is the evidence, then move on. And wit belongs
only where it cannot be pried loose from the subject. Liberman's usage mavens
"bidding the impact tide retreat" and McCulloch's "if all-caps was good enough
for the Romans, it would be good enough for telegrams" are funny because they
ride particular actors and particular nouns. A line that would still land with
the topic swapped out is decoration, and this topic will keep offering it.

When the piece reaches a verdict, about what the pattern is or about the tools
built to spot it, set it on a fact the reader can check, the way Liberman pins
his to an editor who used the discouraged word 347 words later. A judgment
resting on a specific number gives the reader something to check. A judgment
resting only on the writer's confidence does not.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> For example, take DNS. We've been using DNS since the 80s (for more than 35 years!). It's used in every website on the internet. And it's pretty stable – in a lot of ways, it works the exact same way it did 30 years ago.
>
> But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well. So what's going on?

She states the plain surprising fact with real figures, that the system is 35
years old and works the same as it did 30 years ago, and then the flat
contradiction that it still took her years. The person is visible in the blunt
"So what's going on?" and in the capitalized YEARS, an emphasis she trusts
instead of reaching for an adjective.

> When you make a DNS request on your computer, the basic story is:
> your computer makes a request to a server called resolver
> the resolver checks its cache, and makes requests to some other servers called authoritative nameservers

She names each real part in the order the request touches it, resolver, cache,
authoritative nameservers, in the plainest available words, and nothing is named
before it has been introduced. The teaching is in the sequencing: a reader with
no background can hold the chain because each link is set down before the next
one needs it.

> I don't have as good answers here as I would like to, but knowledge about weird gotchas is extremely hard won (again, it took me years to figure out negative caching!) and it feels very silly to me that people have to rediscover them for themselves over and over and over again.

She says outright that she does not have a good answer, and the frustration she
adds is about the specific thing she has been explaining rather than a general
mood. Admitting the gap plainly is what makes her trustworthy on the parts she
does explain.

## Mark Liberman, "Impact Effect" (Language Log)

Source: https://languagelog.ldc.upenn.edu/nll/?p=31229

> And most such word-oriented reactions reflect resistance to a historical usage shift on the scale of 50 years or so. Certainly this is the case for impact, as measured crudely by frequency in the Medline corpus of biomedical abstracts

He makes a claim about a word's rise and in the same breath says how he measured
it and how rough that measure is, "measured crudely by frequency in the Medline
corpus." The dry precision is the personality here: he tells the reader the
strength of the evidence before asking them to believe the trend.

> The graphs above suggest that the mid-60s usage mavens were bidding the impact tide retreat when it was merely swirling around their ankles.

The joke rides entirely on the specific actors, the mid-60s usage mavens, and on
the specific word, the impact tide. Take those out and no sentence is left, which
is why the wit does not read as ornament: it is doing the argument's work.

> Well, a journal is free to insist on any arbitrary style guide. Every paragraph must have a prime number of commas? Sure, if you say so. But the instruction to "try to avoid the word 'impact'" would be more persuasive if the same editorial message did not contain, 347 words later, the recommendation that in the Discussion section, "The focus should be on the impact of the findings on the field".

The verdict is delivered flatly and then fixed to a fact the reader can check: the
same editor used the word he banned, 347 words on. The "prime number of commas"
aside shows his humor, but the force of the paragraph comes from the counted
detail, not the joke.

## Gretchen McCulloch, "The Meaning of All Caps — in Texting and in Life" (Wired)

Source: https://www.wired.com/story/all-caps-because-internet-gretchen-mcculloch/

> Part of the blame may go to Morse code, that dashingly dotty system used for sending telegrams. Morse code represents every letter as a combination of dots and dashes, suitable for transmitting as long or short taps along an electrical line: A is dot-dash, B is dash-dot-dot-dot, and the rest of the 26 letters can all be represented as combinations of up to four dots and/or dashes. But if we wanted to include lowercase letters, we'd need a fifth and a sixth dot or dash, because we'd be representing 52 symbols, and telegraph operators would have to memorize twice as many codes. Unsurprisingly, people decided it wasn't worth it—if all-caps was good enough for the Romans, it would be good enough for telegrams.

She works backward from the behavior to a real mechanical cause and names its
parts, dots, dashes, 26 letters, 52 symbols, letting a number carry the
explanation of why lowercase was dropped. The closing line is funny because it
sits on the actual nouns, the Romans and the telegrams, not on a quip that could
be lifted out.

> The period when lengthening became popular lines up with the rise of recorded speech, such as phonographs, records, cassettes, and CDs. It might be coincidence, but it might also be that when we started being able to play and replay recorded speech, we started paying more attention to representing it precisely. At any rate, it's clear that the goal of repeated letters is to represent speech in writing, because the early examples show up in fictional dialog, especially in play scripts and novels.

She lines up a correlation, refuses to overclaim it with "It might be
coincidence, but it might also be," and then states the thing the evidence does
establish and the reason it does. Marking exactly where the proof stops is the
whole move, and she does it in the same plain voice she uses for everything else.

> I searched the Corpus of Historical American English for sequences of at least three of the same letter (to eliminate common English words like "book" and "keep"). The corpus contains texts from 1810 to 2009, but to my surprise, there were hardly any results in the first half of the corpus. The few earlier examples were mostly just typos, like "commmittee," or numerals, like "XXXIII."

She shows her method and the guardrail on it, excluding words like "book" and
"keep," then reports a result that ran against what she expected. Letting the
data correct her on the page, plainly, is where the person is visible.
