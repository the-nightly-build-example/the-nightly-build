# Voice guide: the-mechanics/glitch-tokens (01)

## How this piece should sound

This lesson has one job: take a reader who has never thought about
tokenizers and get them to the point where they can explain, in their own
words, why a handful of specific tokens break a language model. The whole
piece can lean on a single running example, the article's own glitch
token, the way Julia Evans never leaves her one broken Docker container
and Atul Gawande never leaves M.'s scalp. Every step down toward the
tokenizer-versus-training-corpus mismatch should be a step taken with that
one token still in the room, not a general statement about tokenizers that
could have been written about any of them.

Evans's piece is built entirely from wrong turns stated exactly, not
gestured at: she doesn't say "permissions seemed like a possible cause,"
she says why permissions problems throw a different error and why the file
was already confirmed executable. This lesson will hit at least one
plausible-sounding wrong explanation for why a model can't handle a token
like this. Most readers' first guess will be something like "it's just a
rare word," and the piece is stronger if it states precisely why that
guess fails rather than waving it off. The body speaks to no reader the
way Evans's first-person voice does, so what carries over is her precision
about what a wrong hypothesis would predict and how the evidence
contradicts it, not her voice.

Travis's aside about the angle-of-attack sensor, sticking a hand out of a
car window, is doing real work: it hands the reader a physical sensation
they already own before the term "angle of attack" ever appears, and the
term only shows up once they have that sensation to hang it on. This
lesson has at least one moment like that available to it: how a
tokenizer's vocabulary gets built is not an experience most readers have
had, but the general shape has ordinary analogues worth reaching for, if
one fits the actual mechanism without distorting it. A list assembled from
what showed up often enough in one pass of text, handed off before anyone
checks it against what actually got learned, is not unlike a phrasebook
printed before the trip, or a seating chart drawn up before anyone RSVPs.

Travis also earns the right to a flat, declarative restatement of what a
system does, as in "Let's review what the MCAS does," only after he has
walked through the sensors and the trim system piece by piece. This lesson
can use that same move once, at the point where the reader has enough
parts named to hear a one-sentence statement of the mismatch and
understand every word of it. That sentence shouldn't arrive early, and it
shouldn't be dressed up; it should just be true and complete.

The series demands marking what's settled against what's still guessed,
and both Travis and Gawande give models for doing that without breaking
stride. Travis keeps his certainty about the mechanism ("the antistall
system... consulted only the sensor on one side") entirely separate from
his admitted uncertainty about motive ("I don't know what toxic
combination... led to this mistake"). Gawande's "The theory — and a theory
is all it is right now —" does the same thing inside a single sentence,
flagging an explanation as the field's best current account without
stopping to apologize for it. This lesson has real material for both
moves: the tokenizer-training mismatch itself is settled and traceable,
but why this particular token and not some neighboring one breaks the
model the way it does may not be. Whichever parts of that turn out to be
contested rather than confirmed, say so the way Gawande does: inside the
sentence, not as a disclaimer bolted onto the end of a paragraph.

Gawande's other habit worth taking is following a named mechanism
immediately with what it's made of. He doesn't just hand the reader the
phrase "brain's best guess" and move on. The very next clause says what
the guess is assembled from. Every term this lesson introduces for the
tokenizer pipeline should get the same treatment: defined, then
immediately shown doing something with the article's own token.

One thing to leave behind rather than carry over: Evans's piece is a
transcript of terminal commands and their output, and this series runs no
code. Her rhythm, stating the puzzling result, trying an explanation,
showing exactly why it doesn't hold, then trying the next one, is the part
worth keeping. The commands themselves are not something this lesson has
room to imitate and shouldn't try to.

## Julia Evans, "Debugging a weird 'file not found' error"

Source: https://jvns.ca/blog/2021/11/17/debugging-a-weird--file-not-found--error/

> "Yesterday I ran into a weird error where I ran a program and got the
> error "file not found" even though the program I was running existed.
> It's something I've run into before, but every time I'm very surprised
> and confused by it (what do you MEAN file not found, the file is RIGHT
> THERE???!!??)"

The confusion comes first, stated as plainly as the symptom itself, before
any hypothesis. Nothing here oversells the weirdness with adjectives. The
all-caps question mid-sentence is doing the work a writer might
otherwise reach for a word like "bizarre" to do, and it's funnier and more
convincing for being the writer's actual reaction rather than a label
stuck on the event from outside.

> "At first I thought "hmm, maybe the permissions are wrong?". But this
> can't be the problem, because: permission problems don't result in a
> "no such file or directory" error / in any case when we ran ls -l, we
> saw that the file was executable / (I'm including this even though it's
> "obviously" wrong just because I have a lot of wrong thoughts when
> debugging, it's part of the process :) )"

This is a wrong guess killed with evidence, not with authority. Evans
doesn't say the guess was wrong; she gives the two specific facts that
rule it out, then adds a short aside admitting she's showing her work even
where the work led nowhere. That parenthetical is where the person is
most visible: she trusts the reader enough to walk them through a dead
end instead of only reporting the ones that paid off.

> "I still don't understand why it's using cgo here, I ran env | grep CGO
> and I definitely don't have CGO_ENABLED=1 set in my environment, but I
> don't feel like solving that mystery right now."

An open question stated in one plain sentence, with the specific thing she
checked named right there, and then set down without apology. She doesn't
pretend the loose end is fine or make it sound bigger than it is; she just
says what she knows, what she doesn't, and that she's stopping.

## Gregory Travis, "How the Boeing 737 Max Disaster Looks to a Software Developer"

Source: https://spectrum.ieee.org/how-the-boeing-737-max-disaster-looks-to-a-software-developer

> "The angle of attack is the angle between the wings and the airflow over
> the wings. Think of sticking your hand out of a car window on the
> highway. If your hand is level, you have a low angle of attack; if your
> hand is pitched up, you have a high angle of attack. When the angle of
> attack is great enough, the wing enters what's called an aerodynamic
> stall. You can feel the same thing with your hand out the window: As you
> rotate your hand, your arm wants to move up like a wing more and more
> until you stall your hand, at which point your arm wants to flop down on
> the car door."

The technical term arrives only after the sensation does. Travis hands the
reader something they've already felt, walks the analogy far enough to
recreate the stall itself in the reader's own arm, and only then does the
term "aerodynamic stall" get to mean something. Nothing about the analogy
is decorative: every part of it (level, pitched up, the flop) maps onto
the mechanism he's about to describe.

> "Let's review what the MCAS does: It pushes the nose of the plane down
> when the system thinks the plane might exceed its angle-of-attack
> limits; it does so to avoid an aerodynamic stall. Boeing put MCAS into
> the 737 Max because the larger engines and their placement make a stall
> more likely in a 737 Max than in previous 737 models."

This sentence only works because of everything built before it: engine
size, engine placement, angle of attack. It cashes all of that in at once,
flatly, with no flourish. It's the moment the piece stops accumulating
parts and states what they add up to.

> "I don't know what toxic combination of inexperience, hubris, or lack of
> cultural understanding led to this mistake. But I do know that it's
> indicative of a much deeper problem."

Two claims in two sentences, and Travis keeps them on opposite sides of a
clean line: he does not know the motive, he does know the mechanism is a
symptom of something larger. The admission of not-knowing isn't hedged or
softened. It's stated as flatly as the certainty next to it.

## Atul Gawande, "The Itch"

Source: https://www.newyorker.com/magazine/2008/06/30/the-itch

> "The account of perception that's starting to emerge is what we might
> call the "brain's best guess" theory of perception: perception is the
> brain's best guess about what is happening in the outside world. The
> mind integrates scattered, weak, rudimentary signals from a variety of
> sensory channels, information from past experiences, and hard-wired
> processes, and produces a sensory experience full of brain-provided
> color, sound, texture, and meaning."

The named mechanism doesn't sit alone as a label. The very next sentence
says what it's built from: which signals, which processes, combined how.
The phrase means something specific rather than standing in for an
explanation Gawande hasn't actually given yet.

> "The theory — and a theory is all it is right now — has begun to make
> sense of some bewildering phenomena."

A single dash-set clause does the whole job of marking this as unsettled,
without slowing the sentence down or turning into a disclaimer paragraph.
The confidence of "has begun to make sense of" and the caveat sit right
next to each other and neither one undercuts the other.

> "The new theory may also explain what was going on with M.'s itch. The
> shingles destroyed most of the nerves in her scalp. And, for whatever
> reason, her brain surmised from what little input it had that something
> horribly itchy was going on — that perhaps a whole army of ants were
> crawling back and forth over just that patch of skin. There wasn't any
> such thing, of course. But M.'s brain has received no contrary signals
> that would shift its assumptions. So she itches."

After pages of general science, the piece snaps back to the one named
case by name. The mechanism isn't left as an abstraction. It's run
through M.'s specific nerves and her specific scalp until it produces the
specific symptom the piece opened with, in a sentence four words long.
