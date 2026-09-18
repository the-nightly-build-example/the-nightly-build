# Voice guide: the-mechanics/typo-robustness

## How this piece should sound

The corrective this lesson opens with, that there is no spell-checker and the
model never runs a correction pass, can land as a flat, short claim the way
Yglesias states his own central correction: "This is all wrong, wrong,
wrong," backed by the same four-word answer repeated across four different
questions. The repetition is what makes his correction stick; qualifying it
("largely," "in most cases") would undo the job the sentence is doing. This
lesson has room for one sentence like that, at the point where the
misconception is actually named and cleared, rather than hedged throughout
the piece.

The step the whole explanation depends on, why a misspelling's pieces still
carry the intended meaning, is a mechanism claim, and it can hang on one
worked example the way Yglesias hangs an abstract price-and-amenity chain on
a single mobile-home factory: a real word, run through a real tokenizer,
showing the actual split into pieces, with the actual pieces named.
Describing tokenization only in the abstract ("text gets broken into subword
units") is exactly where a reader stops following. One real split, shown
once and named in full, can do teaching that a paragraph of description
cannot.

The piece ends at a boundary: everyday typos are handled robustly and this is
understood, while crafted, adversarial inputs are a live research question.
That boundary can be stated as plainly as Willison states the limits of
prompt-injection defenses, a flat claim about what is and is not known, with
no editorializing about how the reader should feel about the gap. Evans does
something similar at smaller scale, saying outright when a detail she read
did not fully make sense to her rather than smoothing over it. This lesson
can afford the same kind of honesty about where the settled engineering
stops and the open question starts, said once and left there rather than
hedged.

Willison's habit of showing the actual model output rather than describing
what a model would do fits the tokenizer example specifically: where the
lesson has a verified split from a real tokenizer, the split itself can carry
the point, rather than a sentence characterizing it.

## Matthew Yglesias, "The 'induced demand' case against YIMBYism is wrong"

Source: https://www.slowboring.com/p/induced-demand

> "This is all wrong, wrong, wrong. We simply cannot accept “make sure the
> neighborhood sucks” as our affordable housing strategy. How do you improve
> transportation access to a neighborhood without displacing people? You need
> to expand the housing supply. How do you improve schools without displacing
> people? You need to expand the housing supply. How do you reduce crime
> without displacing people? You need to expand the housing supply. How do you
> improve the retail amenities in Baltimore without displacing people? Well,
> you need to expand the housing supply!"

The verdict comes first, in three flat words repeated, before any of the
argument that earns it. Then the same question gets asked four times with
four different nouns, and the same six-word answer closes each one. The
repetition is the argument: by the fourth round the reader has done the
generalizing themselves, which is why the piece never has to state the
general rule directly.

> "The right model for thinking about this is industrial policy rather than
> housing. There are communities where people work in factories building
> mobile homes. Since the homes come off the assembly line and get shipped out
> of town, it's true that the mobile home factory doesn't increase local
> housing supply and improve affordability. Instead, it has all the normal
> benefits of any kind of factory whether it makes cars or jet engines or
> computer chips or refrigerators — it provides blue-collar jobs and tax
> revenue."

An abstract claim about jobs and tax revenue existing independently of local
housing supply gets replaced with one factory that ships its product
somewhere else. The reader can picture the trucks leaving town, and once they
can, the separation between "creates jobs" and "adds housing" stops being an
assertion and becomes a thing they just watched happen.

> "Poor people struggle to afford housing for the same reason they struggle to
> afford shoes and laptops and yoga classes — they don't have any money."

One clause states the finding the whole piece has been building toward, and
the comparison items are ordinary and slightly funny on purpose: shoes,
laptops, yoga classes. Naming three unrelated things poor people also cannot
afford does more to establish "this isn't a housing-specific problem" than a
sentence saying so would.

## Julia Evans, "Some possible reasons for 8-bit bytes"

Source: https://jvns.ca/blog/2023/03/06/possible-reasons-8-bit-bytes/

> "I'm not super into computer history (I like to use computers a lot more
> than I like reading about them), but I am always curious if there's an
> essential reason for why a computer thing is the way it is today, or
> whether it's mostly a historical accident."

The parenthetical admits a mild disinterest most technical writers would cut
to sound more invested in their own subject. Keeping it in does the opposite
of undermining the piece: it tells the reader exactly which question the
piece is chasing (essential reason versus historical accident) and why this
particular writer, who doesn't care about history for its own sake, is the
one asking it.

> "I don't understand this comment at all – why does the exponent have to be
> 8 bits if you use a 32-bit word size? Why couldn't you use 9 bits or 10 bits
> if you wanted? But it's all I could find in a quick search."

She quotes a primary source, then says plainly that she doesn't follow part
of it, and moves on without pretending otherwise. The confusion is specific
(named bit counts, a named alternative) rather than a general shrug, so the
reader can tell exactly where her understanding stops and can go check the
source themselves if they want to go further.

> "Overall this makes me feel like an 8-bit byte is a pretty natural choice if
> you're designing a binary computer in an English-speaking country."

The closing claim is deliberately narrower than "here is why computers use
8-bit bytes." "Feel like," "pretty natural," and the specific qualifier about
English-speaking countries all mark exactly how far the evidence in the piece
actually reaches, after forty-some paragraphs of research that could have
tempted a bigger conclusion.

## Simon Willison, "Prompt injection: What's the worst that can happen?"

Source: https://simonwillison.net/2023/Apr/14/worst-that-can-happen/

> "To date, I have not yet seen a robust defense against this vulnerability
> which is guaranteed to work 100% of the time. If you've found one,
> congratulations: you've made an impressive breakthrough in the field of LLM
> research and you will be widely celebrated for it when you share it with
> the world!"

The claim about the state of the field ("I have not yet seen") is stated
first, plainly, with its own limit built in ("to date"). The second sentence
is a joke, but it is a joke that only works because the first sentence is
true and specific: the exaggerated congratulations lands because the reader
already knows how hard the unsolved problem actually is.

> "There are plenty of 95% effective solutions, usually based around
> filtering the input and output from the models. That 5% is the problem
> though: in security terms, if you only have a tiny window for attacks that
> work an adversarial attacker will find them. And probably share them on
> Reddit."

The number does the work a vaguer word wouldn't: "95% effective" tells the
reader exactly how close current defenses get, and "that 5%" makes the
remaining gap sound small on paper and dangerous in practice within the same
sentence. The last line is one clause of deadpan humor tacked onto a
security claim, and it doesn't retract the claim or soften it.

> "More generally though, right now the best possible protection against
> prompt injection is making sure developers understand it. That's why I
> wrote this post."

The stated purpose of the piece arrives at the very end, after the
demonstrations have already done the persuading, so it reads as a
conclusion the evidence supports rather than a mission statement placed up
front. It is also the one moment the piece names itself, and it earns that
by being the actual reason the piece exists, not a gesture at the reader.
