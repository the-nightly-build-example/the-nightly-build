# Voice guide: the-evidence/flashattention

## How this piece should sound

This lesson explains a fact about a chip, not a fact about a paper: attention
is slow because a big table has to travel between two kinds of on-chip memory,
not because the arithmetic is hard. The house voice for the desk is plain
claims and concrete stakes, and nowhere does that matter more than the memory-
hierarchy section, where the whole teaching job is making "fast tier" and
"slow tier" mean something other than two adjectives the reader takes on
faith.

Take Dan Luu's move of putting the real number next to the claim instead of
asking the reader to trust the adjective: he doesn't say a modern machine is
much faster than an Apple 2e, he says 4,000x the speed, 500,000x the
transistors, and lets the absurdity of the gap do the work. This lesson has
the same job with SRAM and HBM: give the real capacity and bandwidth figures
side by side, the way the commission already asks for, so "fast and small"
versus "slow and large" is a pair of numbers the reader can hold, not a
metaphor.

Take his other habit too: when he explains why the Apple 2e is quick, he
doesn't just call the modern pipeline complicated, he walks the actual path
("there basically aren't handoffs, locks, or process boundaries. Some very
simple code runs and writes the result to the display memory") and lets the
absence of steps be the explanation. Idea 3 in this lesson is exactly that
kind of walk: tiling, a running softmax, recomputation in the backward pass.
Show what the naive version of attention does step by step and what
FlashAttention skips, the same concrete way, rather than summarizing the
result as "more efficient."

Julia Evans's instinct to report a flat or boring result and move on without
dressing it up is worth borrowing for the exact-vs-approximate correction this
piece owes. FlashAttention does not reduce FLOPs, and can add some. That is
not a caveat to soften or a concession to argue around; it is a plain fact,
stated the way she states a null result ("It took exactly the same amount of
time. NEXT.") and left to stand. The honest, undramatic delivery of "it does
the same multiplications, it just moves less data" is the whole correction in
idea 5, and it lands harder plain than argued.

Nelson Elhage's closing conviction, that a system built of layers has no
magic in it if you're willing to name the layer, is the register this piece
should hold about the memory hierarchy itself. The reader has never written a
kernel, but nothing here should read as an impression of complexity being
managed on their behalf. Name the tiers, name the sizes, name what moves
between them and why, the same directness with which he says a behavior "can
be understood by digging down through enough layers."

One direction the exemplars can't give, because it belongs to this lesson's
own shape: the worked example in idea 1 needs one real sequence length and the
resulting score-table size stated plainly before anything else is built on it,
since every later number (the memory scaling claim, the speedup claim) is a
comparison against that first concrete table. Get the reader holding one real
number early, and the rest of the lesson has something to measure against.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower
> than the computers I used as a kid. As a rule, I don't trust this kind of
> feeling because human perception has been shown to be unreliable in
> empirical studies, so I carried around a high-speed camera and measured the
> response latency of devices I've run into in the past few months."

The opening doesn't argue the reader into caring; it states a suspicion,
distrusts it on principle, and says exactly what was done to check it. The
person is visible in the choice to not trust his own perception and to go
build a measurement instead.

> "By comparison, on the Apple 2e, there basically aren't handoffs, locks, or
> process boundaries. Some very simple code runs and writes the result to the
> display memory, which causes the display to get updated on the next scan."

This is what a mechanism looks like written out instead of characterized. He
doesn't call the old machine's path "simpler," he says what isn't in it, and
the absence of steps is the argument.

> "It's a bit absurd that a modern gaming machine running at 4,000x the speed
> of an apple 2, with a CPU that has 500,000x as many transistors (with a GPU
> that has 2,000,000x as many transistors) can maybe manage the same latency
> as an apple 2 in very carefully coded applications if we have a monitor
> with nearly 3x the refresh rate."

The sentence stacks the real multiples instead of reaching for "far faster,"
and the multiples themselves supply the tone; nothing is added to tell the
reader to be surprised.

## Julia Evans, "Computers are *fast*!"

Source: https://jvns.ca/blog/2014/05/12/computers-are-fast/

> "So I have a computer. My computer contains hardware (like a CPU! RAM!
> L1/L2 caches!) But I don't understand very well how fast that hardware is,
> what tools I have to profile it, and how much of the time that my programs
> are running is split between RAM/the hard disk/the CPU."

She opens by naming exactly what she doesn't know, in the plainest possible
terms, before doing anything to find out. The not-knowing is stated, not
performed.

> "This is a pretty boring step. We made it use mmap instead (see
> bytesum_mmap.c), in the hopes that it would make it faster. It took exactly
> the same amount of time. NEXT."

A negative result gets exactly as many words as it earns. There's no hedge
around the fact that the change did nothing, and the one-word sentence that
ends the paragraph is her moving on, not a punchline.

> "I'm also kind of amazed by how fast C is. I'm used to writing in dynamic
> programming languages, which definitely do not process 1GB files in 0.25
> seconds. Fun!"

The closing anchors the abstraction ("fast") to a number she already built up
over the piece, and the surprise is stated as her own reaction, not asserted
as a fact about the world.

## Nelson Elhage, "Computers can be understood"

Source: https://blog.nelhage.com/post/computers-can-be-understood/

> "There is no magic. There is no layer beyond which we leave the realm of
> logic and executing instructions and encounter unknowable demons making
> arbitrary and capricious decisions. Most behaviors in one layer are
> comprehensible in terms of the concepts of the next layer, and all
> behaviors can be understood by digging down through enough layers."

Three short declaratives rule something out before the piece explains what is
true instead. The conviction is in the flat refusal of the "magic" framing,
not in any word that announces conviction.

> "With a rich mental model of the system and the code at hand, you can
> perform backwards reasoning in the form of deductions like 'Ah, if this
> field is set to NULL, someone must have set it … the only code that sets
> that field is {here}, {here}, and {here} … only the first and third could
> ever be called with a NULL argument …' and so on."

He drops into the actual internal monologue of the reasoning instead of
describing that reasoning from outside, which is what makes the mental model
concrete rather than asserted.

> "Computers are complex, but need not be mysteries. Any question we care to
> ask can, in principle and usually even in practice, be answered. Unknown
> systems can be approached with curiosity and determination, not fear."

The close restates the opening claim in the same plain terms it started with,
without reaching for a bigger word than the piece has earned.
