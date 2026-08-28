# Voice guide: the-evidence/seq2seq

## How this piece should sound

This lesson reads one 2014 paper and tells the reader what it actually did, so
the register is Lee and Trott's, not Evans's and not Mitchell's own first-person
one: a smart stranger explaining a machine to someone who has never opened it,
never "I" and never a hedge dressed as a question. The seq2seq paper's whole
mechanism is one move — pack a sentence into a single fixed-length vector, then
unpack it — and that move has to be built the way Lee and Trott build a word
vector: with something the reader can already picture standing in for the
technical object, stated plainly, before the machine version of it appears. Do
this once, for the vector itself, not for every term after it; a second analogy
for the decoder would be the padding the exemplar shows how to avoid.

Sourced figures earn the same treatment Lee and Trott give GPT-3's 12,288
dimensions: a number the reader cannot picture on its own, paired with a
comparison that makes it legible, never left to sit alone as evidence of scale.
The series exists to show the size of the foundation under a claim, which is
this lesson's own mandate more than any exemplar's, and it means giving the
1997 LSTM and the 2014 training run their real numbers rather than gesturing at
"large" or "small." Mitchell's move before the o3 news — stating the prior
leaderboard's ceiling before reporting the jump over it — is the shape for
this: whatever the paper's translation system is measured against, give that
baseline before giving the paper's own number, so the reader can judge the
second figure instead of just receiving it.

The paper's one fatal limitation is where Mitchell's Breakout paragraph matters
most: she doesn't assert that a trained system failed to generalize, she gives
the one pixel-shift experiment that shows it. The fixed-length vector's
breakdown wants the same treatment — a specific case where the compression
failed, not a sentence that names "a limitation" and moves on. Where the
paper's own reception outran what it measured, that gap is worth stating as
plainly as Mitchell asks whether o3 is doing the reasoning ARC was built to
test, a direct question earned by the numbers just given, not a rhetorical one.

A term of art from the paper — the reversed source sentence, the fixed context
vector, whatever the paper calls its own trick — gets defined the way Evans
defines negative caching: the plain mechanics first, then the one concrete
consequence that makes the definition stick, in the same breath. That is also
where this piece can afford a real number delivered dryly, the way Mitchell
totals the cost of an evaluation run and lets the total speak instead of
flagging it as remarkable. No hype and no doom holds throughout: a grand claim
about what the paper started gets the argument under it before the word
appears, exactly the discipline Lee and Trott show when they say plainly that
nobody fully understands how these models work rather than smoothing past the
gap.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Why use such a baroque notation? Here's an analogy. Washington DC is located at 38.9 degrees North and 77 degrees West. We can represent this using a vector notation: […] This is useful for reasoning about spatial relationships. You can tell New York is close to Washington DC because 38.9 is close to 40.7 and 77 is close to 74. By the same token, Paris is close to London. But Paris is far from Washington DC."

Before the reader has to hold "a list of 300 numbers" as a mental object, the
piece hands them a map they already know how to read and lets the same logic
carry over. The move is visible in the order: the odd technical fact comes
first as a question the writer admits is odd ("why use such a baroque
notation?"), then the analogy answers it, rather than the analogy arriving to
soften something already stated in jargon.

> "For example, the most powerful version of GPT-3 uses word vectors with 12,288 dimensions—that is, each word is represented by a list of 12,288 numbers. That's 20 times larger than Google's 2013 word2vec scheme. You can think of all those extra dimensions as a kind of "scratch space" that GPT-3 can use to write notes to itself about the context of each word."

The number arrives twice, once as a raw figure and once as a ratio against a
number the reader met earlier in the same piece, and only after both is it
translated into what the extra room is for. Nothing here asks the reader to
just trust that "large" means large.

> "We love this example because it illustrates just how difficult it will be to fully understand LLMs. The five-member Redwood team published a 25-page paper explaining how they identified and validated these attention heads. Yet even after they did all that work, we are still far from having a comprehensive explanation for why GPT-2 decided to predict Mary as the next word."

The writers just spent several paragraphs building an impressive result, and
this is where they say plainly what it doesn't yet prove. The size of the
paper behind the finding (five researchers, twenty-five pages) is given as
part of the same sentence that says the finding still falls short, so the
admission carries its own evidence rather than reading as false modesty.

## Melanie Mitchell, "Did OpenAI Just Solve Abstract Reasoning?"

Source: https://aiguide.substack.com/p/did-openai-just-solve-abstract-reasoning

> "As of earlier this year, a few ARC competitions had been held, and the winning systems' performance was at most around 35% accuracy on the private test set. Average human performance had been estimated earlier (using parts of the training set) at about 85%."

This is the baseline, given before the news it exists to judge. By the time
the piece reports OpenAI's new score two sections later, the reader already
has both ends of the scale it should be measured against, supplied without
comment on which number is more impressive.

> "It's not necessarily the case. Machine learning methods are known to "overfit" to specific cases and often aren't able to generalize well. One very interesting example of this was from DeepMind's work on neural networks that learned to play Atari video games via reinforcement learning. A neural network trained on the video game "Breakout" […] was particularly successful, getting very high scores on the game. One set of researchers showed, however, that changing the game just by moving the paddle up a few pixels resulted in the original trained system performing dramatically worse."

The claim under test is abstract — does a system that solves a task actually
generalize the concept behind it — and instead of arguing the point in the
abstract, the piece hands over one experiment where the answer turned out to
be no. The specific detail that decides it is a few pixels, not a
redesigned game, which is what makes the failure a hard fact and not a
plausible-sounding worry.

> "To solve an ARC task, OpenAI gives o3 a number of "samples"—which I understand as independent queries with the same prompt—and then returns the solution with the most "votes" (the one that appears the most times) in those independent samples. The low-compute version was allowed six samples (at a cost of $20 per task), and the high-compute version was allowed 1,024 samples (at a cost estimated to be several thousands of dollars per task, and over $1M total for the whole evaluation…wow, this is a lot of money to solve 100 little puzzles!)"

The aside at the end is earned by the arithmetic just laid out in the same
sentence, not dropped in on its own. It reads as a person doing the math in
real time and reacting to what it adds up to, rather than a line written to
be quoted.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "negative caching! (which I talk about in this talk) It took me probably 5 years to realize that I shouldn't visit a domain that doesn't have a DNS record yet, because then the nonexistence of that record will be cached, and it gets cached for HOURS, and it's really annoying."

The term of art and its consequence arrive in the same breath: what negative
caching is, and what happens to you if you don't know about it. Nothing about
the definition is separated from the reason it matters, so there's no
glossary entry sitting apart from the stakes.

> "Here you can see we got a normal NOERROR response for google.com (which is in 8.8.8.8's cache) but a SERVFAIL for homestarrunner.com (which isn't). This doesn't mean there's no DNS record homestarrunner.com (there is!), it's just not cached)."

Right after showing two real command outputs side by side, the piece heads
off the exact misreading a newcomer would make from the second one. The
correction is folded into the sentence describing the result, not held for a
separate caveat later.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

This states outright the difference between simplifying a subject and just
organizing it better, which is a distinction the whole piece has been
demonstrating rather than announcing until this moment. The frustration named
here is specific to a real complaint about existing tools, not a general claim
about clarity.
