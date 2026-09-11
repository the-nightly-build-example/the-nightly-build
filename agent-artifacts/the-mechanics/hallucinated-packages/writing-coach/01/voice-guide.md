# Voice guide: the-mechanics/hallucinated-packages (01)

## How this piece should sound

This is a lesson for a reader who is smart and widely read and has never spent a
day in a codebase. They have watched an AI coding assistant confidently write an
import for a library that does not exist, and they want to know what in the
system produces that. The piece works backward from that behavior to its cause
and then to the slopsquatting risk that rides on it. The register is plain,
concrete, and sober: explain the mechanism at full resolution, give the security
problem its real size, and never reach for alarm or for a shrug.

Open on the behavior the reader already knows, named in its own particulars, the
way Dan Luu opens "Files are hard" on email clients that corrupted his inbox and
names Pine, Eudora, and Outlook rather than "some mail clients." The assistant
inventing a package, the registry it would have been installed from, the
specific invented name when the piece has one: the concrete case is what lets
the explanation land. Julia Evans sets the same kind of hook by stating how
ordinary and stable DNS is and then asking "So what's going on?" This piece can
pose the plain puzzle, a thing people see every day that turns out to have a
cause worth tracing, and then go get it.

Trace the cause down to ground one ordinary step at a time. Evans's note on
negative caching takes a behavior that feels mysterious and lands it on a single
plain fact about how the system works. Each step here should name a real part of
the system, what it does, and why it yields this behavior: how the model
produces a plausible-looking import, why a name that was never real recurs, why
the registry lets an attacker sit at that name. Where a step connects to
something the reader may half-know, a comparison can make it legible, the way Luu
tells the reader that file writes are the same reordering problem as
multithreaded code and then says plainly that files are harder. A judgment about
where the weakness lives today is welcome when the facts carry it; Luu states
his, and the Cloudflare report states its verdict about which piece of software
was actually at fault, without drama.

Explain at full strength without talking down. Evans insists her clearer output
is "not 'dumbed down'" and is "the exact same information, just formatted in a
more structured way," and that is the standard here: the reader with no codebase
time still gets the real mechanism, with the registry and the model's behavior
named exactly, not softened into generalities. Define each term of art, such as
the registry or slopsquatting, in the sentence it first appears, and then use it.

Be sober about the risk and exact about its size. The Cloudflare incident report
calls its bug serious in one plain clause, says it found no evidence of
exploitation, and then gives the rate as "1 in every 3,300,000 HTTP requests"
with the percentage beside it. When this piece reports how often assistants
hallucinate a package or how exposed the supply chain is, give the figure and
anchor it to something the reader already holds, and say plainly what is not
known. The same report separates how the bug happened from why it surfaced when
it did; this piece can likewise keep "why the model does this" apart from "why it
is dangerous now," resolving each in turn.

Mark the edges of what is settled. The Mechanics desk wants each step marked as
settled engineering or open question, and the exemplars do this honestly: Luu,
who is not a filesystem developer, writes that he would be surprised if there
were not at least one bug in his own post. Where the cause of the recurring fake
name or the fix for it is still unsettled even for the people who build these
systems, say so in plain words rather than papering over it.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "For example, take DNS. We've been using DNS since the 80s (for more than 35 years!). It's used in every website on the internet. And it's pretty stable – in a lot of ways, it works the exact same way it did 30 years ago.
>
> But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well. So what's going on?"

Evans builds the whole piece on a plain puzzle: an old, stable, everywhere thing
is still somehow hard, so why. She states the ordinary facts flatly, one per
short sentence, and lets the contradiction do the work of pulling the reader in.
Evans is visible in the bare "So what's going on?" that ends the setup and hands
the rest of the post its job.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

This is her standard for explaining: clarity is a matter of presentation, not of
throwing away detail. The passage separates making something readable from making
it simpler, and commits to keeping every bit of the real information. Evans is in
the insistence of it, the exclamation and the plain refusal to strip a mechanism
down to make it go easier.

> "It took me probably 5 years to realize that I shouldn't visit a domain that doesn't have a DNS record yet, because then the nonexistence of that record will be cached, and it gets cached for HOURS, and it's really annoying."

A behavior that feels inexplicable gets landed on one ordinary fact about how the
system works: the nonexistence is cached. She traces the surprise to a cause the
reader can hold and keep. Evans shows here how to take the mystery out of
something by naming the single plain mechanism under it.

## Dan Luu, "Files are hard"

Source: https://danluu.com/file-consistency/

> "I haven't used a desktop email client in years. None of them could handle the volume of email I get without at least occasionally corrupting my mailbox. Pine, Eudora, and outlook have all corrupted my inbox, forcing me to restore from backup."

Luu starts from a concrete thing that happened to him, with the real products
named, and the problem stated as plainly as a person would say it aloud. The
failure is specific and ordinary, and that is what makes the long technical
descent that follows feel earned. Luu is visible in the flat, unhurried report of
a genuine annoyance, with no effort to dress it up.

> "These are fundamentally the same issues people run into when doing multithreaded programming. Correctly reasoning about re-ordering behavior and inserting barriers correctly is hard. But even though shared memory concurrency is considered a hard problem that requires great care, writing to files isn't treated the same way, even though it's actually harder in a number of ways."

He ties an unfamiliar difficulty to one many of his readers already respect, then
states a judgment the piece has earned: files are actually harder. The comparison
does explanatory work, and the verdict is carried by the reasoning before it, not
asserted. Luu is in the willingness to rank the two problems plainly once he has
shown why.

> "I think this is understandable, given how much misinformation is out there. Not being a filesystem dev myself, I'd be a bit surprised if I don't have at least one bug in this post."

After pages of careful detail, he marks the limit of his own authority in plain
words. The admission is specific, about his own standing and this particular
post, not a ritual hedge. Luu is visible in treating his own possible error as
just another fact worth stating.

## John Graham-Cumming (Cloudflare), "Incident report on memory leak caused by Cloudflare parser bug"

Source: https://blog.cloudflare.com/incident-report-on-memory-leak-caused-by-cloudflare-parser-bug/

> "The bug was serious because the leaked memory could contain private information and because it had been cached by search engines. We have also not discovered any evidence of malicious exploits of the bug or other reports of its existence.
>
> The greatest period of impact was from February 13 and February 18 with around 1 in every 3,300,000 HTTP requests through Cloudflare potentially resulting in memory leakage (that's about 0.00003% of requests)."

This is how to state a security risk soberly. One clause says why it was serious,
the next says plainly what was not found, and the size is given as a rate with
the percentage set beside it so the reader can scale it. Graham-Cumming is
visible in the refusal to inflate or minimize: the facts are laid out at their
real size and left to carry the weight.

> "That explains how the pointer could run past the end of the buffer, but not why the problem suddenly manifested itself. After all, this code had been in production and stable for years."

He separates two questions that are easy to run together, the how and the
why-now, and tells the reader which one he has answered and which is still open.
It is the backward-working move made explicit, setting up the next step instead
of declaring victory. The writer is visible in the plain signposting of what is
still unexplained.

> "So, the bug had been dormant for years until the internal feng shui of the buffers passed between NGINX filter modules changed with the introduction of cf-html."

The payoff to the question above: a latent fault turned live only when something
nearby changed. The one vivid phrase sits inside an otherwise exact sentence and
names a concrete internal change rather than gesturing at one. Graham-Cumming is
in the single light touch allowed into prose that is otherwise kept precise.
