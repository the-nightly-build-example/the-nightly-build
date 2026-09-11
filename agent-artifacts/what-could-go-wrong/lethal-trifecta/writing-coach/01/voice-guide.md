# Voice guide: what-could-go-wrong/lethal-trifecta (01)

## How this piece should sound

This lesson takes a security argument seriously enough to test it. The reader is
smart and widely read but has never had to reason about an attacker, so the
writing has to carry two jobs at once: make the lethal-trifecta argument legible,
and say how much of it the 2025 evidence actually supports. The register that
does both is plain and unhurried, the register of someone who has thought about
the threat and is neither frightened of it nor bored by it. The exemplars below
are security writers who explain a threat model to a general audience and are
trusted to say how worried to be. None of them raises their voice to do it.

Open with the argument at its strongest, and state it fairly before testing it.
Bruce Schneier, arguing that the country cannot defend every target,
first lays out which targets an attacker would genuinely prefer and why each one
(S3). The reader believes his conclusion because the case against it was real.
An agent that can read private data, read untrusted content, and reach the
outside world is worth the reader's worry for concrete reasons; give those
reasons their full weight before any test is applied to them.

The argument will arrive carrying strong words: that such an agent *will* leak, that
exfiltration is *inevitable*, that the combination is *unsafe by design*. Weigh those
words the way Matthew Green weighs "impossible" when it appears on his own side
of a debate (G1): he asks what assumptions the word rests on and treats a claim
that outruns its conditions as a weakness to probe, not a tool to borrow. The
calibration this piece needs lives in that move. Say which parts of the trifecta
hold in general and which hold only when particular conditions are met.

Keep the demonstrated apart from the hypothetical, and handle each with the same
precision. Green distills an elaborate proposal down to the one thing it actually
requires (G3), and he reads a government's need for a new law as an admission of
what voluntary cooperation could not do, without ever saying the government
"implied" it (G2). A prompt injection shown working against a real system in 2025
and an attack still described only on paper are different kinds of claim, and the
line between them is where this argument usually turns. Draw it in the open.

Teach the mechanism through a case the reader can picture. Thomas Ptacek explains
why encrypted email fails by pointing at the one event every user of it has
watched happen, the plaintext reply with the whole thread quoted underneath (T2);
Maciej Cegłowski shows a safety control being defeated by walking through exactly
how a trucker beats a once-a-minute logging device (M2). A single worked instance
of an agent reading attacker-controlled text and then acting on it will do more
for this reader than the three-part definition stated in the abstract.

Where the evidence earns a verdict, state it plainly. Ptacek's opening commits in
five flat sentences with no hedge (T1), and it works because the argument under it
holds the weight; Schneier's "we can't defend everything" carries for the same
reason (S2). And when the piece tells the reader how worried to be, it can be as
direct as Cegłowski sorting an entire industry into what is silly, what is useful,
and what is harmful in a single sentence (M1). That directness is what keeps a
calibrated verdict from reading as either alarm or dismissal.

## Bruce Schneier, "Terrorists Don't Do Movie Plots"

Source: https://www.schneier.com/essays/archives/2005/09/terrorists_dont_do_m.html

> "We all do it. Our imaginations run wild with detailed and specific threats. We imagine anthrax spread from crop dusters. Or a contaminated milk supply. Or terrorist scuba divers armed with almanacs. Before long, we're envisioning an entire movie plot, without Bruce Willis saving the day. And we're scared."

The passage names specific imagined scenarios rather than saying people imagine
frightening things, so the reader watches the exact habit being described instead
of being told about it. Schneier puts himself inside it with "We all do it,"
which keeps the observation from landing as an accusation against other people.
The short flat sentences carry the list without inflating any item in it.

> "The problem with movie plot security is that it only works if we guess right. If we spend billions defending our subways, and the terrorists bomb a bus, we've wasted our money. To be sure, defending the subways makes commuting safer. But focusing on subways also has the effect of shifting attacks toward less-defended targets, and the result is that we're no safer overall."

Schneier states a concrete cost, then concedes the real point on the other side,
that defending subways does make commuting safer, before he draws his conclusion.
The concession is specific rather than a throat-clearing gesture, and the verdict
arrives only once it has been made. The reasoning is shown step by step, so the
reader can check each move.

> "Terrorists don't care if they blow up subways, buses, stadiums, theaters, restaurants, nightclubs, schools, churches, crowded markets or busy intersections. Reasonable arguments can be made that some targets are more attractive than others: airplanes because a small bomb can result in the death of everyone aboard, monuments because of their national significance, national events because of television coverage, and transportation because most people commute daily. But the United States is a big country; we can't defend everything."

Before concluding that everything cannot be defended, Schneier builds the
strongest version of the opposing view: which targets an attacker would actually
prefer, with a reason attached to each. The steelman is real because the reasons
are real, and the plain closing line works because the argument before it is fair.

## Matthew Green, "Thinking about 'traceability'"

Source: https://blog.cryptographyengineering.com/2021/08/01/thinking-about-traceability/

> "But difficult is not the same thing as impossible. A recent post by WhatsApp makes the case that tracing is fundamentally impossible to implement securely in an end-to-end encrypted system. While this claim seems intuitively correct, it's also kind of unsatisfying. After all, 'impossible' is a strong word, and it's highly dependent on which assumptions you're making."

Green is arguing against traceability, and the overclaim sits on his own side, yet
he refuses it and says why: whether "impossible" is true depends on the
assumptions behind it. He separates what feels correct from what is precise, and
treats a vague claim as a liability even when it favors his position.

> "It's now time to say a stupid and obvious thing: what's being proposed in India is not cooperative tracing.
>
> Let's be clear: if detective work and cooperation was sufficient to trace the originators of harmful content, the police wouldn't be asking for new encryption laws, and WhatsApp wouldn't be suing the Indian government."

Green works out what the law's backers must be conceding from the single fact that
they need a law at all: that voluntary cooperation was not enough. He reads the
action rather than the stated motive, and he states the inference plainly instead
of writing that anyone hinted or implied it, which keeps the reported fact and his
reading of it distinct.

> "This brings us to the central challenge of all content tracing proposals so far: to make tracing possible, a tracing system needs to turn every WhatsApp user (including the originator) into a cooperative green circle — regardless of whether users actually want to cooperate with police."

Green reduces an elaborate cryptographic proposal to the one demand it cannot
avoid making: that every user be turned into a source of tracing data whether or
not they consent. The sentence carries what the mechanism actually requires rather
than how it is described. ("Green circle" points back to a diagram earlier in the
post where cooperating users are drawn that way.)

## Thomas Ptacek (Latacora), "Stop using encrypted email"

Source: https://www.latacora.com/blog/2020/02/19/stop-using-encrypted-email/

> "Email is unsafe and cannot be made safe. The tools we have today to encrypt email are badly flawed. Even if those flaws were fixed, email would remain unsafe. Its problems cannot plausibly be mitigated. Avoid encrypted email."

Five short declarative sentences, each its own claim, building to the instruction
at the end. Ptacek commits all the way, with "cannot be made safe" and "Avoid
encrypted email" carrying no hedge, and the word "unsafe" repeats across the
sentences instead of giving way to softer synonyms.

> "The clearest example of this problem is something every user of encrypted email has seen: the inevitable unencrypted reply. In any group of people exchanging encrypted emails, someone will eventually manage to reply in plaintext, usually with a quoted copy of the entire chain of email attached."

Rather than describe the failure in the abstract, Ptacek points at the one thing
every user of the system has watched happen. The event is ordinary and easy to
recognize, and the reader's recognition of it is what supports the general claim
about why the system cannot hold a secret.

## Maciej Cegłowski, "Haunted By Data"

Source: https://idlewords.com/talks/haunted_by_data.htm

> "We're very much in the 'radium underpants' stage of the surveillance economy. A lot of the hype is silly, some of what we're doing is useful, and some of it is downright harmful."

After a long argument, Cegłowski sorts the whole field into three plain buckets in
a single sentence: some of the hype silly, some of the work useful, some of it
harmful. He neither condemns the industry wholesale nor excuses it, and he states
the split flatly instead of hedging it. (The "radium underpants" phrase is a
callback to the running nuclear analogy he uses through the talk, and belongs to
that format rather than to an explanatory piece.)

> "The device logs only once a minute, so if you accelerate to 45 mph, and then make sure to slow down under the 10 mph threshold right at the minute mark, you can go as far as you want.
>
> So we have these tired truckers staring at their phones, bunny-hopping down the freeway late at night."

Cegłowski walks through exactly how a driver defeats a device that checks position
once a minute: get above the speed, then drop under the threshold right at the
mark. The example is concrete enough to see, and it shows a control being beaten
by the very person it was built to measure, rather than asserting that controls
get beaten.
