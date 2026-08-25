# Voice guide: the-mechanics/text-in-images (01)

## How this piece should sound

Open on the behavior itself, stated as a plain observed fact, before naming
anything that causes it. Julia Evans's pipes post does this: the confusion
comes first, described as confusion, and only then does the piece go looking
for why. This lesson has the same shape available to it — a garbled word in
an AI-generated image, described exactly as a reader has seen it, ahead of
any mention of tokens, diffusion, or attention.

If the piece is going to correct a wrong assumption a reader is likely to
hold — that the model "doesn't know how to spell," or "just isn't good at
text" — name that assumption in the reader's own words before replacing it,
the way the physicist in the Quanta piece says "we usually think... that's
not what's happening here" before giving the real mechanism. A correction
stated without the wrong belief next to it reads as a lecture; stated
against the belief it replaces, it reads as an answer.

The series direction already asks for the chain to go down one real part at
a time until the reader hits ground. Cepelewicz's sentence about the cilia —
moving from a single one, to millions of them, to the whole animal, before
delivering the payoff that the animal "doesn't choose" anything — is what
that discipline looks like on the page: the climb comes before the
conclusion, never after it. Whatever the actual chain in this piece turns
out to be (a tokenizer, a text encoder, a latent space, a diffusion step,
whichever terms the real mechanism needs), each link should hand off to the
next by naming what acted and what it acted on, the way Ciechanowski's
escapement sentence does, rather than summarizing the chain in a sentence
afterward.

Every technical term this lesson needs earns its place the way "mainspring"
and "cilia" earn theirs in the exemplars: defined inside the sentence that
first uses it, through the plain thing that gave it its name, not glossed
over to the side. If a step in the chain has a genuinely apt everyday
comparison — the way a swinging watch balance is like pushing a child on a
swing — use it. Don't manufacture one where the mechanism doesn't actually
resemble anything ordinary; a strained comparison is worse than none.

Once the deepest cause is named, come back up and restate the original
behavior in terms of it, the way Ciechanowski's line about "the illusion of
a very smooth hand motion" closes the loop between the escapement's discrete
ticks and what the eye actually sees. This lesson's reader should finish
able to look at a garbled word in an image and see, in order, every step
between the cause at the bottom and the wrong letters on the screen — not
just the name of the cause.

## Julia Evans, "Why pipes sometimes get "stuck": buffering"

Source: https://jvns.ca/blog/2024/11/29/why-pipes-get-stuck-buffering/

> "If log lines are being added to the file relatively slowly, the result I'd see is… nothing! It doesn't matter if there were matches in the log file or not, there just wouldn't be any output."

This is the surprising behavior stated with nothing explained yet — the
writer reports what she saw, including her own confusion, instead of
skipping straight to the cause. That confusion is what gives the rest of
the piece something to resolve.

> "The reason why "pipes get stuck" sometimes is that it's VERY common for programs to buffer their output before writing it to a pipe or file. So the pipe is working fine, the problem is that the program never even wrote the data to the pipe!"

The cause is given once, then restated from the other side: not "the pipe is
broken" but "the pipe is fine, the data never arrived." Saying the same fact
twice from opposite angles is what turns an invisible mechanism into
something the reader can check against what they saw on their own screen.

> "When you press Ctrl-C, what happens? In a magical perfect world, what I would want to happen is for tcpdump to flush its buffer, grep would search for example.com, and I would see all the output I missed. But in the real world, what happens is that all the programs get killed and the output in tcpdump's buffer is lost."

The mechanism is delivered as the gap between what the writer wanted to
happen and what actually happens. Asking the question and voicing the wished
for answer before giving the real one makes the real answer land as a
correction to something the reader was already expecting, not a fact
dropped on them cold.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "In the world of modern portable devices, it may be hard to believe that merely a few decades ago the most convenient way to keep track of time was a mechanical watch. Unlike their quartz and smart siblings, mechanical watches can run without using any batteries or other electronic components."

The unfamiliar subject is introduced by naming the familiar thing sitting
right next to it — the quartz and smart watches the reader already owns —
before the piece says anything the reader has to take on faith. The very
next claim, about batteries, only lands because that comparison came first.

> "As the balance wheel swings, the jewel roller strikes the pallet fork, which unlocks the escape wheel. Once unlocked, the escape wheel powered by the mainspring pushes on the pallet fork which, through the jewel roller, pushes on the balance wheel itself. This causes the balance wheel to gain some energy, which prevents it from stopping after a while – it's equivalent to giving a push to a person swinging on a swing."

Each clause names what acted and what it acted on, then hands off to the
next clause the same way, so the chain of cause and effect is legible one
link at a time with no summarizing sentence needed at the end. The
comparison to pushing a child on a swing translates the whole mechanical
chain into something the reader has physically felt.

> "In this watch movement the balance wheel does a full back and forth swing four times per second, hitting the pallet fork twice during each cycle, for a total of 8 beats per second or 28,800 beats per hour. While different watches may have different rates, they all do a tiny turn of the second hand many times per second, which gives mechanical watches the illusion of a very smooth hand motion."

The surprising thing everyone has seen — a second hand that appears to
glide — is finally accounted for, in a specific count rather than a vague
"very fast," and the sentence says outright that what the reader sees is an
illusion built out of the mechanism just described. The loop from invisible
parts back to the visible behavior gets closed by name.

## Jordana Cepelewicz, "Before Brains, Mechanics May Have Ruled Animal Behavior"

Source: https://www.quantamagazine.org/before-brains-mechanics-may-have-ruled-animal-behavior-20220316/

> "The animal beneath the lenses wasn't much to look at, resembling an amoeba more than anything else: a flattened multicellular blob, only 20 microns thick and a few millimeters across, with neither head nor tail. It moved on thousands of cilia that blanketed its underside to form the "sticky hairy plate" that inspired its Latin name, Trichoplax adhaerens."

The technical name arrives already defined, because the plain phrase that
produced it — "sticky hairy plate" — is given in the same breath as the
Latin. A reader never has to hold an undefined term while waiting for a
definition that might come later.

> "Mechanical interactions that began at the level of a single cilium, and then multiplied over millions of cells and extended to higher levels of structure, fully explained the coordinated locomotion of the entire animal. The organism doesn't "choose" what to do. Instead, the horde of individual cilia simply moves — and the animal as a whole performs as though it is being directed by a nervous system."

The sentence climbs one level of scale at a time — one cilium, millions of
cells, the whole animal — before it delivers the surprising conclusion that
the animal isn't choosing anything. Putting the climb before the payoff is
what makes the payoff feel earned rather than announced.

> "We usually think, when we have something going on like that, that we have an internal clocklike signal that's saying, 'OK, go, now stop, now go, now stop,'" said Simon Sponberg... "That's not what's happening here. The cilia aren't getting paced. There's not some central thing that's saying 'Go, go, go.' It's the mechanical interactions that are setting up something that goes, goes, goes."

The scientist states the intuitive, wrong explanation first, in a plain
imagined voice ("go, now stop, now go"), then dismantles it with the real
one echoed in the same rhythm ("goes, goes, goes"). Quoting the correction
straight from the source, rather than paraphrasing it, lets the piece show a
misconception being named and knocked down rather than just asserting it's
wrong.
