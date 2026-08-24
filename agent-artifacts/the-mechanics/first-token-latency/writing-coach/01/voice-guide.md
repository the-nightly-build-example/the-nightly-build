# Voice guide: the-mechanics/first-token-latency

## How this piece should sound

The lesson works backward from a felt pause — the moment between a reader
sending a message and the first word appearing — to the machinery that produces
it. Write for a smart adult who uses AI chatbots and has never seen the inside
of one.

Somers opens his piece on the concrete event that made an invisible mechanism
worth reading about: a date, a place, a busy signal, a specific number of
attempted calls. The article has its own felt event to hand — a sent message,
the wait before the first word — and the opening worked example can commit to
one such event in the same specific way, before the words "prefill" and
"decode" arrive. Somers's foot-on-the-pedal passage shows the same move applied
to a mechanism the reader cannot see: he starts from something the reader has
physically done. Ground each step of the chain the same way. A worked case
belongs at every step the commission names.

Luu is direct about which claim he holds and where he thinks a common belief is
wrong. Where the article has room to correct a common intuition about chatbot
latency — that the pause is the model "thinking harder", say, or that a slower
model must be a smarter one — Luu's move is the one to reach for: name the
belief, say what you think is true, and give the evidence in the same
paragraph. If no such misconception is at stake at a given step, skip it. Luu
also commits to the strength of a claim ("only weakly related", "roughly 5ms
unloaded"). On steps the commission marks as settled engineering (attention
cost grows with input length; the KV cache is what makes decode cheap), the
language can be that flat. On steps it marks as open (how far a particular
serving stack has moved the balance with speculative decoding, paged attention,
or continuous batching), commit at whatever precision the sources actually
support and no further.

Evans is a teacher whose past confusion is her main evidence for what needs
explaining. The body of a lesson does not speak in the first person, so her
voice does not transfer to it as-is. What transfers is her stance toward the
reader: she explains the thing that would have unstuck her a year ago, without
flattering the reader and without talking down to them. Where a term of art
enters this lesson, treat the reader the way she does — as someone who has just
not been shown it yet.

The subject invites comparison to systems where a fixed one-time cost is
followed by a cheap steady stream. An analogy from outside the machine can help
a lay reader once, but each one carries a claim that must be true of the
mechanism it stands in for, and a second one usually dulls the first. Reach
for one that earns a step.

Read the drafted piece with the analogies and the specifics stripped out. What
should remain is a lesson only about first-token latency in a chatbot: a pause
a reader has felt, worked down through prefill, attention, and the KV cache to
the point where the answer stops changing. If the same paragraph could sit
inside a lesson on backpropagation or on RLHF, rewrite it around this lesson's
mechanism.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When I finally learned how to troubleshoot DNS problems, my reaction was
> "what, that was it???? that's not that hard!". I felt a little bit cheated!
> I could explain to you everything that I found confusing about DNS in a few
> hours."

Evans arrives on the page as someone who was recently confused about her own
subject. The four question marks and the exclamation carry the reaction. Her
authority as a teacher comes from remembering exactly what she used to not
understand, and the sentence that follows commits to a specific offer she can
keep.

> "In general dig's output has the feeling of a script someone wrote in an
> adhoc way that grew organically over time and not something that was
> intentionally designed."

She names a concrete part of the system (dig's output) and gives a plain
verdict on it. "Adhoc" and "grew organically over time" describe what a reader
who has used the tool already recognizes, so she does not have to list the
flaws before giving her verdict.

> "I don't have as good answers here as I would like to, but knowledge about
> weird gotchas is extremely hard won (again, it took me years to figure out
> negative caching!) and it feels very silly to me that people have to
> rediscover them for themselves over and over and over again."

She admits what she does not have a good answer for and then says plainly what
she does think. The personal feeling ("it feels very silly to me") sits in the
sentence as evidence about the state of the field. The repeated "over and over
and over again" is the one bit of rhythm the sentence takes, and it earns it by
naming a specific frustration.

## Dan Luu, "Terminal latency"

Source: https://danluu.com/term-latency/

> "Curiously, I rarely hear complaints about keyboard and mouse input being
> slow. One reason might be that keyboard and mouse input are quick and that
> inputs are reflected nearly instantaneously, but I don't think that's true.
> People often tell me that's true, but I think it's just the opposite. The
> idea that computers respond quickly to input, so quickly that humans can't
> notice the latency, is the most common performance-related fallacy I hear
> from professional programmers."

Luu names a common belief, says he thinks the opposite, and reports what he has
heard from working programmers. A reader who disagrees can see exactly which
sentence to disagree with. Nothing in the paragraph is hedging.

> "Why don't people complain about keyboard-to-display latency the way they
> complain stylus-to-display latency or VR latency? My theory is that, for
> both VR and tablets, people have a lot of experience with a much lower
> latency application. For tablets, the "application" is pen-and-paper, and
> for VR, the "application" is turning your head without a VR headset on. But
> input-to-display latency is so bad for every application that most people
> just expect terrible latency."

He asks a question a reader might already have asked themselves, and answers
it by comparing the machine to two things the reader knows firsthand: pen and
paper, and turning your head. The quotation marks around "application" mark
that he is stretching the word; the sentence would still work if they were
gone.

> "The closest thing that I care about is the speed at which I can ^C a
> command when I've accidentally output too much to stdout, but as we'll see
> when we look at actual measurements, a terminal's ability to absorb a lot of
> input to stdout is only weakly related to its responsiveness to ^C."

He grounds an abstract measurement in something a terminal user has actually
done (hitting ^C on a runaway command). "Only weakly related" is a specific
strength of claim: not "unrelated" and not "correlated", and a reader can check
it against the numbers he shows later.

## James Somers, "The Coming Software Apocalypse"

Source: https://www.theatlantic.com/technology/archive/2017/09/saving-the-world-from-code/540393/

> "There were six hours during the night of April 10, 2014, when the entire
> population of Washington State had no 911 service. People who called for
> help got a busy signal. One Seattle woman dialed 911 at least 37 times while
> a stranger was trying to break into her house. When he finally crawled into
> her living room through a window, she picked up a kitchen knife. The man
> fled."

The subject of the piece is invisible (software), but the opening is entirely
concrete: a date, a place, a busy signal, one specific caller, a specific count
of attempts, a kitchen knife. Somers uses five sentences on the observable
event before the word "software" arrives. The reader reaches the mechanism
already believing something is at stake.

> "But software doesn't break. Intrado's faulty threshold is not like the
> faulty rivet that leads to the crash of an airliner. The software did
> exactly what it was told to do. In fact it did it perfectly. The reason it
> failed is that it was told to do the wrong thing. Software failures are
> failures of understanding, and of imagination."

Six short sentences take a familiar analogy (rivet, airliner) and turn it into
a claim the reader had not started the paragraph believing. Each sentence adds
one step, none of them long. The last sentence states plainly what the previous
five have earned.

> "Technological progress used to change the way the world looked—you could
> watch the roads getting paved; you could see the skylines rise. Today you
> can hardly tell when something is remade, because so often it is remade by
> code. When you press your foot down on your car's accelerator, for instance,
> you're no longer controlling anything directly; there's no mechanical link
> from the pedal to the throttle. Instead, you're issuing a command to a piece
> of software that decides how much air to give the engine. The car is a
> computer you can sit inside of."

Somers names an invisible mechanism (drive-by-wire) by starting from something
the reader has physically done (pressing an accelerator). The concrete step —
the missing mechanical link — is described before the summary sentence at the
end, so that summary lands on ground the paragraph has already built.
