# Voice guide: the-mechanics/irrelevant-context

## How this piece should sound

This lesson explains why a model that solves a math word problem correctly can
get it wrong once you rename the people, swap the numbers, or add one true but
irrelevant sentence. The logic of the problem did not move; only its surface
did. The reader is smart and reads widely and is new to how these systems work.
The job is to take them from the behavior down to what produces it, and the
register that carries that is plain, unhurried, and unexcited. Dan Luu and Simon
Willison both write this way about hard technical material: they state the thing
and its stakes and move on, without dramatizing a striking result. Hold that
register here, where an accuracy drop from a cosmetic change is genuinely
surprising and does not need help sounding so.

Open on the behavior itself, the way Luu opens "Files are hard" on the email
clients that kept corrupting his inbox: a concrete case the reader has met,
named specifically, and then the plain question the rest of the piece answers.
The behavior for this lesson is a model whose answer to a word problem gets worse
when the surface changes and the reasoning does not. Let the reader see it before
any mechanism.

When the piece reports how large the effect is, how far accuracy moved under a
surface change, how far it fell with an added irrelevant clause, across how many
models, give the numbers the way Luu gives disk-error rates: as sourced ranges
with the qualifying detail beside them, not rounded down to a single dramatic
figure. Reporting the range and the qualifier is what keeps the finding from
flattening into a slogan.

Working backward means naming a real part of the system and saying what it does.
Willison pins an abstract thing, a fixed-length array of numbers, to the actual
lengths so the reader has something to hold. Do the same when the lesson reaches
what the model receives, a prompt that is a sequence of tokens it conditions on
at once, and why an added sentence or a changed name shifts the output: keep each
step attached to a small concrete case rather than left as a general statement.
Terms the reader does not already have, taught earlier or not, can be settled in
the sentence they appear in without stopping the piece, the way Luu folds the
definition of a term into the clause that introduces it.

The lesson runs down to a point where the field is settled and a point where it
is not. Mark which is which plainly. Willison, describing what the numbers in an
embedding mean, says outright that nobody fully understands them and that they
are useful anyway, and holds both halves in one sentence without resolving the
tension or hyping past it. Where this piece reaches the contested question of
what the behavior implies about reasoning, that steadiness is the model: state
the strongest form of each side, and where the people who build these systems do
not agree, say so rather than smoothing the disagreement into a verdict the
evidence has not earned.

Plain does not mean thin. Julia Evans insists that presenting information clearly
is not the same as removing it, and that she wants all of it. Explain why surface
form moves the answer at the level of what the model actually does, rather than
reaching for a reassuring simplification that leaves the reader unable to tell
when someone else's explanation has skipped a step.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "I haven't used a desktop email client in years. None of them could handle the volume of email I get without at least occasionally corrupting my mailbox. Pine, Eudora, and outlook have all corrupted my inbox, forcing me to restore from backup. […] Why has my experience with desktop applications been so bad?"

The piece opens on a problem the writer actually lived with and names the
specific clients rather than "some email programs." The closing question is the
real one the rest of the piece answers, not a rhetorical warm-up. Luu is visible
in the flat, unhurried tone: he states the annoyance and the puzzle without
dramatizing either.

> "Well, what sort of failures can occur? Crash consistency (maintaining consistent state even if there's a crash) is probably the easiest property to consider, since we can assume that everything, from the filesystem to the disk, works correctly; let's consider that first."

He defines the term of art in the same breath he introduces it, inside the
parentheses, so a reader who has never heard "crash consistency" is not left
behind. He also announces that he is taking the easiest piece first and says why,
which lets the reader see the plan. "Let's consider that first" narrates the
order of the explanation without ceremony.

> "The Bairavasundaram et al. SIGMETRICS '07 paper found that, depending on the exact model, between 5% and 20% of disks would have at least one error over a two year period. Interestingly, many of these were isolated errors -- 38% of disks with errors had only a single error, and 80% had fewer than 50 errors."

The numbers arrive as ranges tied to the study they come from, and he adds the
second-order detail (most disks with errors had only one) instead of stopping at
a single alarming figure. That is how he keeps a measured claim measured. His
habit of citing the specific paper by name and year is on display.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well. So what's going on?"

One sentence carries an admission, that it took her years, and turns it into the
question the post exists to answer. The plain "So what's going on?" hands the
reader the thread to follow, and she does not pretend the thing was easy for her.
The capitalized "YEARS" is her personal-blog register showing through, louder
than a serious paper would go; the transferable part is the honesty and the plain
question, not the shout.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

Her stance on clarity is stated outright: presenting information clearly is not
the same as removing it, and she wants all of it. The emphatic "I want to see all
the information!" shows her insistence that plain does not mean thin. The slight
looseness of the phrasing ("alternative DNS tools that they often remove") is the
sound of someone talking directly rather than composing a sentence.

## Simon Willison, "Embeddings: What they are and why they matter"

Source: https://simonwillison.net/2023/Oct/23/embeddings/

> "The key thing about that array is that it will always be the same length, no matter how long the content is. The length is defined by the embedding model you are using—an array might be 300, or 1,000, or 1,536 numbers long."

He states the one property that matters, same length regardless of input, before
any detail, then fixes the abstraction with the actual lengths so the reader
holds something concrete. Willison's calm, matter-of-fact register is visible;
nothing is oversold, and the concrete figures do the work.

> "The location within the space represents the semantic meaning of the content, according to the embedding model's weird, mostly incomprehensible understanding of the world. It might capture colors, shapes, concepts or all sorts of other characteristics of the content that has been embedded."

He states plainly what the numbers are meant to represent, then in the same
sentence concedes how little is understood about them. The short concrete list,
colors, shapes, concepts, keeps an abstract claim tangible. He is visible in the
willingness to call the thing weird rather than smoothing it over.

> "Nobody fully understands what those individual numbers mean, but we know that their locations can be used to find out useful things about the content."

A single sentence holds both halves of an honest position: the individual numbers
are not understood, and the thing works and is useful anyway. He does not resolve
the tension or hype past it. This is his steady, unexcited way of marking the
edge of what is known.
