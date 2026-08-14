# Voice guide: the-mechanics/formatting-defaults (01)

## How this piece should sound

This lesson begins from something the reader has watched a chatbot do many
times, answer a plain question in bulleted lists under bold headers, and works
backward one step at a time to what puts that habit there, ending in the
post-training stages that shaped it. The reader is sharp and widely read but has
never seen the inside of one of these systems, and there is no code, so the
words carry the whole explanation. The register the press already sets fits this
work: plain, closer to explaining something you understand well than to a
technical paper, and reaching for the plainest version of a sentence rather than
the most impressive one.

Working backward invites a wrong guess at almost every step, and those guesses
are worth using. The reader arrives with a folk theory about why the bullets
appear, and the later steps meet smaller guesses of the same kind. Where a
plausible simpler account of the formatting is available, the lesson can state
it in the reader's own terms and let it fail against what the system actually
does, the way Ciechanowski attaches the hand straight to the barrel and lets the
reader watch it spin uselessly, and the way Evans lets "you might think that
there's a system call like this" stand as reasonable before showing what really
happens. Naming the guess earns its place only when the piece can then show
where it stops accounting for the behavior.

Each step names a real part, a token, a training stage, a reward signal, and the
reader meets most of these for the first time. A part is explained when the
reader can say what it changes and what it leaves alone. Evans is precise about
this boundary with execve: almost everything survives, one thing is replaced,
and that line is the point. The lesson can hold each post-training stage to the
same test, saying what the stage alters in the model's behavior and what it
leaves untouched, rather than handing the reader a stage that vaguely shapes the
output.

Some of these parts have an everyday parallel the reader already handles, and
naming it can make a step concrete, as Ciechanowski's push on a swing makes the
escapement's small nudge land, or his credit card fixes a size the reader cannot
otherwise picture. A parallel like that works when it sits beside the real part
and confirms a mechanism the reader can already follow. It misleads when it
stands in for the part, and this desk asks for the part itself, so an image that
lets the reader skip the mechanism is worth less than the plain description.

More than one part can look responsible for the same behavior, and the
formatting habit is a case where the training text, the instruction tuning, and
the people who rated the outputs could each be blamed. When the lesson reaches a
step with competing candidates, it can name each and say what each would and
would not explain, the way Simler sets emotional inception beside cultural
imprinting and tests both, rather than settling on one and leaving the rest
unnamed. A candidate is easiest to weigh against a concrete case where the
behavior does or does not appear, which is the work Simler's bed sheets do.

This desk asks the lesson to mark which steps are settled engineering and which
are still open even to the people who build these systems. Where the mechanism
behind the formatting is understood, the lesson can say so plainly, and where it
is contested or unknown, it can say that too and mark its own reading as a
reading, the way Simler answers "Which is true? I don't know. But I suspect" at
the point a reader wants the answer. For this reader, saying plainly that the
cause is not fully settled is worth more than a confident answer the field does
not have.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "We've managed to make some parts rotate and one could naively think that we could just attach a watch hand to the barrel to make it track time. Unfortunately, that won't really work – you can witness this in the demonstration below."

Ciechanowski has just built a mechanism that visibly spins, and rather than move
on he stops to name the obvious next thought and lets it fail. He states the
naive move in the reader's own words, reports plainly that it will not work, and
only then shows why. The writer is visible in his willingness to spend a
paragraph on an approach he already knows is wrong, because watching it break
explains more than asserting the right answer would.

> "As the balance wheel swings, the jewel roller strikes the pallet fork, which unlocks the escape wheel. Once unlocked, the escape wheel powered by the mainspring pushes on the pallet fork which, through the jewel roller, pushes on the balance wheel itself. This causes the balance wheel to gain some energy, which prevents it from stopping after a while – it's equivalent to giving a push to a person swinging on a swing."

The first sentences track the parts in order, each one handing off to the next,
and only once the mechanism is fully laid out does he reach for the swing. The
everyday comparison arrives to confirm something the reader can already follow,
not to replace it. Ciechanowski is visible in the restraint: the analogy is a
single clause at the end, and the moving parts do the explaining.

> "That rounded rectangle surrounding the watch corresponds to the size of a credit card – if you have one handy you can put it on screen and drag the slider until the card fits in that outline. Hopefully, this really puts in perspective how small all the parts we've talked about are."

Every part in the article was drawn far larger than life, so at the end he fixes
the true size to an object the reader can hold against the screen. The
comparison does what a measurement would not: a few millimeters means little, a
credit card means something exact. He is visible in choosing a reference anyone
has in a wallet.

## Julia Evans, "What happens when you start a process on Linux?"

Source: https://jvns.ca/blog/2016/10/04/exec-will-eat-your-brain/

> "This is a reasonable thing to think and apparently it's how it works in DOS/Windows. I was going to say that this isn't how it works on Linux. But! I went and looked at the docs and apparently there is a posix_spawn system call that does basically this. Shows what I know."

Evans lets the reader's likely first guess stand as reasonable, corrects it,
then corrects herself when the guess turns out partly right, and reports her own
mistake without ceremony. The plain admission keeps the explanation honest about
where its tidy version frayed. She is visible in "Shows what I know", which
hands the reader a fallible person instead of an authority.

> "Instead of having children, what I do is you have a child that is a clone of myself, and then that child gets its brain eaten and turns into ls. Really."

A clone whose brain gets eaten and becomes ls is a concrete, almost physical
picture of an abstract operation, and it holds up because it is exact: a copy is
made, then overwritten. The framing is memorable without blurring the mechanism
underneath. Evans is visible in the plain, faintly absurd wording she is willing
to set beside a technical term.

> "When you run execve and have another program eat your brain, actually almost everything stays the same! You have the same environment variables and signal handlers and open files and more. The only thing that changes is, well, all of your memory and registers and the program that you're running. Which is a pretty big deal."

Evans separates what the operation leaves untouched from the one thing it
replaces, naming both plainly before she judges how large that one change is.
The reader finishes knowing the exact edge of the mechanism. "Which is a pretty
big deal" is her voice: a flat judgment that reports importance rather than
announcing it.

## Kevin Simler, "Ads Don't Work That Way"

Source: https://meltingasphalt.com/ads-dont-work-that-way/

> "Here we have a theory — a proposed mechanism — of how ads influence consumer behavior. Let's call it emotional inception or just inception, coined after the movie of the same name where specialists try to implant ideas in other people's minds, subconsciously, by manipulating their dreams."

Simler takes a loose popular belief and states it as a named, specific mechanism
before he argues against anything, so there is a definite claim on the table to
test. Naming it and saying exactly what it proposes gives the rest of the piece
something concrete to work against. He is visible in the care he takes to state
fairly an idea he means to reject.

> "On the other hand, if ads work by cultural imprinting, then we should expect almost no branded advertising for bed sheets, because their consumption is almost perfectly obscure (the opposite of conspicuous). It's unlikely that any of your peers will ever see or feel your bed sheets, nor even inquire about them. Bed sheets just aren't a social product, so cultural imprinting can't work to convince us to buy them."

Simler checks his mechanism against a product it predicts should get almost no
advertising, and the ordinary example does the testing: if the theory holds,
bed-sheet ads should be scarce, and they are. The concrete case carries the
point where a bare statement of the rule would not. He is visible in reaching
for the most everyday object available.

> "Which is true? I don't know. But I suspect — confounding factors notwithstanding — that we see a more-than-linear relationship between audience size and ad value, which might account for some of the network effects enjoyed by big national (and international) brands."

Simler sets out what each of the two mechanisms predicts about audience size,
and then, where the reader expects the answer, says plainly that he does not
have it and marks his own guess as a guess. Admitting the limit of the evidence
costs the argument nothing and makes the rest easier to trust. He is visible in
refusing to round a suspicion up to a finding.
