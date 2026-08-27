# Voice guide: the-mechanics/structured-output (01)

## How this piece should sound

This is a lesson on The Mechanics desk. It starts from something the reader has
done, asked a model to return only JSON or fill a fixed schema and watched the
answer come back worse, and walks backward one step at a time to what inside the
system produces that. The reader is quick and widely read and has never worked
in a codebase, so every part named earns a plain-words definition the moment it
appears, and nothing below the surface is assumed. There is no code.

The piece can open on the behavior itself, before any mechanism, the way Wenger
opens "What's in a Linux executable?" on renaming a file to `.exe` and back. The
reader already holds the experience: the request for strict JSON, the worse
answer. Beginning where they are lets the concrete puzzle lead them to the cause.

Reach each technical term through the everyday version of it first. Ciechanowski
gets to the watch's mainspring by starting from a spring anyone has squeezed, and
naming the ordinary coil spring, before the specialized one the mechanism uses.
The same path is open for the parts this lesson needs, the model choosing one
token at a time, a schema, the program that only admits format-valid tokens: name
the ordinary thing, then the exact one, and define it as it arrives.

The masking step is the one the reader most needs to watch happen rather than be
told about. Ciechanowski fixes real numbers, forty hours and 2400 turns of the
second hand, before he says the word gears, so the reader feels the problem
before its solution has a name. A single concrete next-token choice, showing
which tokens the format still allows and which one it blocks, is the kind of
worked example that carries constrained decoding further than a definition does.

Where the lesson reaches a move the reader would make on their own, just demand
the JSON and be done, it can put that move to work and let the reader see what it
does, the way Ciechanowski raises the obvious idea of tying the date ring
straight to the hour wheel and then shows it sliding under the window all day. A
cost the reader watches happen is more convincing than one the prose asserts.

Hold the line between what is settled and what is still argued. That a program
blocks the next tokens which would break the format, leaving the model to pick
among what remains, is mechanical and can be stated flatly. How much the
formatting alone costs is a live disagreement, and the prose can let it stay one,
the way Evans labels her "current theory" as a guess and Wenger ends by listing
the questions he still cannot answer. State the settled rung plainly and mark the
contested one as contested, without rounding either toward the other.

Keep the register plain and unhurried, and let the evidence carry the weight. The
reader keeps meeting claims about AI they cannot check, and this lesson earns
trust by staying checkable, in the plain declarative voice Ciechanowski and Evans
both hold even where the material is intricate. Where a figure would anchor
something the reader cannot scale on their own, give the figure.

## Julia Evans, "How the locate command works (and let's write a faster version in one minute!)"

Source: https://jvns.ca/blog/2015/03/05/how-the-locate-command-works-and-lets-rewrite-it-in-one-minute/

> I’ve known for a long time that locate is faster than find, and that it had some kind of database, and that you could update the database using updatedb.
>
> But I always somehow thought of the locate database as this Complicated Thing. Until today I started looking at it!

Evans names the exact thing that had put her off, "this Complicated Thing", and
then reports that she looked and found something ordinary. It works because she
states plainly what she used to believe and what changed, so the reader watches a
real reappraisal instead of being told the topic is simple. The "somehow" and the
capitalized "Complicated Thing" are Evans on the page, a little embarrassed to
have been intimidated for years.

> Whoa, our homegrown locate using grep is actually way faster! That is surprising to me. Our homegrown database takes about 3x as much space as locate’s database (45MB instead of 15MB), so that’s probably part of why.

She gives the measured result and her own reaction to it together: the homegrown
version is faster, it surprises her, and she offers the size difference as part of
the reason. The order is what is good, the number first and then the honest
"probably part of why", which keeps the guess separate from the finding. "That is
surprising to me" is a writer willing to be caught out by her own experiment.

> But I don’t really understand yet why locate is so much slower.
>
> My current theory is that grep is better optimized than locate and that it can do smarter stuff. But if you know the real answer, or if you get different results on your computer, please tell me!

After walking through how the command works, Evans marks the edge of what she
understands. She does not know why locate is slower, and "My current theory"
labels the sentence that follows as a guess rather than a result. The plain
admission, and the request for other people's numbers, are Evans treating the
reader as someone who might know more than she does.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> Purely mechanical devices have a few different ways to power themselves, but one of the simplest methods to store energy is to use a spring. Most springs we see in daily life are coil springs.

Ciechanowski reaches the watch's power source by starting from a spring anyone
has handled and naming the coil spring most people picture, before he introduces
the specialized spring the mechanism actually uses. The technical part arrives
only after the everyday version is in the reader's head. The patience is the
writer, unwilling to name a part before the reader can see it.

> If we wanted our watch to run continuously for around 40 hours on a single wind, we’d need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in.

He fixes the numbers first, forty hours and forty turns of the minute hand and
2400 turns of the second hand, and only once the gap is concrete does he say the
watch needs gears. The figures do the work, so the reader feels the size of the
problem before the part that solves it has a name. Choosing forty hours and
multiplying it out, rather than writing "many rotations", is Ciechanowski
insisting the reader hold a real quantity.

> You may wonder why we need this complicated mechanism in the first place. One could naively assume that we could directly tie the rotation of the date ring to the rotation of the hour wheel, similarly to how we rotated the hour wheel in sync with minutes, albeit at slower pace. Unfortunately, this would cause the current date to continuously rotate under the little window in the dial, making it hard to read.

He raises the simpler design a reader would think of, tying the date ring
straight to the hour wheel, and then shows the concrete thing that goes wrong,
the date sliding under the window all day instead of changing once. The
complicated mechanism is earned because the reader first wanted the simple one
and watched it fail. "You may wonder" is him answering the objection a careful
reader would already be forming.

## Amos Wenger, "What's in a Linux executable?"

Source: https://fasterthanli.me/series/making-our-own-executable-packer/part-1

> Executables have been fascinating to me ever since I discovered, as a kid, that they were just files. If you renamed a .exe to something else, you could open it in notepad! And if you renamed something else to a .exe, you’d get a neat error dialog.
>
> Clearly, something was different about these files. Seen from notepad, they were mostly gibberish, but there had to be order in that chaos. 12-year-old me knew that, although he didn’t quite know how or where to dig to make sense of it all.

Wenger opens on something he did as a child, renaming a file to `.exe` and back,
and lets that ordinary observation carry the question the whole series answers.
The writing stays specific: notepad, the error dialog, the gibberish that still
had order in it. The twelve-year-old who knew something was there but not how to
dig is the person the piece is written by and for.

> The bytes 05 and 00 - now, we’re dealing with a little-endian file, so that means 0x0005, which is just 5. So the fifth section header in the table contains section names.
>
> At this point we have no idea what sections are, but I think it’s safe to say that the file is divided into them and that their beginning and size is stored in those section headers.

He decodes two bytes in front of the reader, the value is five so it points at
the fifth section header, and then says plainly what he can and cannot yet
conclude. He does not know what a section is, but he can already tell the file is
divided into them, and he keeps the certain part and the inferred part apart. "I
think it’s safe to say" is Wenger reasoning out loud at the reader's pace.

> That doesn’t answer any of my questions. If anything, I have more questions now.
>
> Why is the entry point stored in an ELF file sometimes the same one we see in GDB and sometimes not? [...] Clearly, we have a lot more detective work to do…

At the end of the investigation Wenger reports that it raised more questions than
it settled, and he lists them exactly instead of smoothing them over. The honesty
is specific, three precise questions about the entry point in the source, each a
real loose end. Refusing to pretend the matter is closed, and staying cheerful
about the work left, is Wenger on the page.
