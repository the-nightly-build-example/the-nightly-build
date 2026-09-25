# Voice guide: the-mechanics/hangman

## How this piece should sound

This is Matt Yglesias explaining something he understands, applied to a chatbot
that appears to cheat at hangman: plain claims, concrete stakes, no fuss. The
reader has played this game, watched the bot's answers contradict each other,
and wants the "oh, that's why" — not a tour of transformer internals. Everything
below is something to reach for only where the material at hand calls for it.

Name the surprise in the reader's own terms before naming the cause, the way
Evans gives 262 kilometers against an expected 10,000 instead of saying the
result was "way off." For hangman, that means showing the actual "yes," "yes,"
"no" that can't all be true of one word, or the revealed word that fails a clue
already given, before a single word of mechanism. Let the piece register its
own reaction to that the way Evans writes "This is VERY bad" — say plainly that
the answers can't all be true, and only then ask why.

The reader's wrong belief here isn't stupid; it's the same belief that makes
the trick work. They think the bot picked a word and is holding it in mind,
the way a real hangman opponent would. Willison's move for the parallel
mistake — granting the misreading real standing ("by no means an irrational
position") before showing what actually happens — is the shape for the "no,
it never wrote the word down" turn here. Where the piece needs the reader to
feel that a secret has to live somewhere to be a secret, a small human-scale
comparison does more than a technical one, the way Willison reaches for a
friend who was told to forget some gossip rather than for anything about
weights or parameters.

Where the transcript itself is the evidence, let it talk: quote the actual
contradictory answers the way Luu runs the actual broken outputs of his toy
write ("a boo," "a bor") instead of saying the operation "can produce
corruption." A joke earns its place only after the mechanism has done the
work, never in place of it — Luu's one-line "computers don't work" lands
because thirty minutes of proof came first, not because the line is funny on
its own. If nothing in the mechanism has earned a line like that by the end,
the piece doesn't owe one.

## Julia Evans, "Examples of floating point problems"

Source: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/

> "But I find all of this a little abstract on its own, and I really wanted
> some specific examples of floating point bugs in real-world programs. So I
> asked on Mastodon for examples of how floating point has gone wrong for them
> in real programs, and as always folks delivered!"

Checked: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/,
retrieved 2026-09-25

She names her own dissatisfaction with the abstract version of the claim
before she'll write about it, and goes and gets real cases instead of
inventing plausible ones. "As always folks delivered!" is a specific person
glad about a specific result, not a transition sentence.

> "This is VERY bad – it's not a small error, 262km is a LOT less than
> 10,000km. What went wrong? [...] Why is this happening? Well, floating
> point numbers get farther apart as they get bigger."

Checked: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/,
retrieved 2026-09-25

She states the size of the surprise in the reader's own units — 262 against
10,000 — instead of grading it as "significant," then asks the exact question
the number just raised and answers it in the next breath. The capitalized
"VERY" is her reacting, not hedging.

> "Real variance: 0.00029959105209321173
> Bad variance: -138.93632 <- OH NO
> This is extremely bad: not only is the bad variance way off, it's
> NEGATIVE!"

Checked: https://jvns.ca/blog/2023/01/13/examples-of-floating-point-problems/,
retrieved 2026-09-25

The comment "<- OH NO" sits right on the broken output, doing the reacting
where the reader is already looking, and "NEGATIVE" in caps names the specific
impossibility (a variance can never be negative) rather than saying the
number looks wrong.

## Simon Willison, "Training is not the same as chatting: ChatGPT and other LLMs don't remember everything you say"

Source: https://simonw.substack.com/p/training-is-not-the-same-as-chatting

This piece explains the general statelessness of chat models, adjacent to
this lesson's own subject. The passages below are quoted for how he argues,
not for the claim they carry; hangman's specific finding — that a plain chat
model can't hold a private commitment at all, not just that it forgets old
turns — is this lesson's own to make.

> "A common complaint I see about these tools is that people don't want to
> even try them out because they don't want to contribute to their training
> data. This is by no means an irrational position to take, but it does often
> correspond to an incorrect mental model about how these tools work."

Checked: https://simonw.substack.com/p/training-is-not-the-same-as-chatting,
retrieved 2026-09-25

He states the reader's actual position before touching it, and grants it
real standing — "by no means an irrational position" — instead of setting up
a weak version to knock down. He locates the error precisely, in the model
held in the reader's head, not in the reader's intelligence.

> "If your mental model is that LLMs remember and train on all input, it's
> much easier to assume that developers who claim they've disabled that
> ability may not be telling the truth. If you tell your human friend to
> disregard a juicy piece of gossip you've mistakenly passed on to them you
> know full well that they're not going to forget it!"

Checked: https://simonw.substack.com/p/training-is-not-the-same-as-chatting,
retrieved 2026-09-25

The comparison is a friend and gossip, not a technical stand-in, so a reader
who has never thought about model weights still feels exactly what's being
claimed. He commits to the comparison instead of qualifying it, which is why
the exclamation point reads as conviction and not decoration.

> "Does your company ban all use of LLMs because they don't want their
> private data leaked to the model providers? They're not 100% wrong - see
> reasons to worry anyway - but if they are acting based on the idea that
> everything said to a model is instantly memorized and could be used in
> responses to other users they're acting on faulty information."

Checked: https://simonw.substack.com/p/training-is-not-the-same-as-chatting,
retrieved 2026-09-25

He asks about a real decision (a company's policy) instead of a hypothetical
reader, and concedes the worry has a true part ("not 100% wrong") before
naming the specific faulty premise underneath the bad policy. The correction
lands on the belief, never on the person who held it.

## Dan Luu, "Files are fraught with peril"

Source: https://danluu.com/deconstruct-files/

> "If we just call pwrite like this, we might succeed and get a bar in the
> output, or we might end up doing nothing and getting a foo, or we might end
> up with something in between, like a boo, a bor, etc."

Checked: https://danluu.com/deconstruct-files/, retrieved 2026-09-25

He runs the actual broken outputs of his own toy example — "a boo," "a bor"
— instead of describing the failure mode abstractly as "partial writes." A
reader can picture the exact wrong string on the disk, which is what makes
the danger real instead of asserted.

> "But they still can't use files safely every time! A natural follow-up to
> this is the question: why the file API so hard to use that even experts
> make mistakes?"

Checked: https://danluu.com/deconstruct-files/, retrieved 2026-09-25

He defends the practitioners first — these are people who "know more about
filesystems than the vast majority of programmers" — before asking why they
still get it wrong, which turns what could be a gotcha into a real question
the rest of the talk goes on to answer.

> "In conclusion, computers don't work (but you probably already know this if
> you're here at Gary-conf)."

Checked: https://danluu.com/deconstruct-files/, retrieved 2026-09-25

The joke only works because of the thirty minutes of concrete evidence that
came before it — it claims nothing beyond what the audience just watched him
demonstrate, and the parenthetical aside to the room he's actually standing
in is a specific person talking to specific listeners, not a line built to
travel.
