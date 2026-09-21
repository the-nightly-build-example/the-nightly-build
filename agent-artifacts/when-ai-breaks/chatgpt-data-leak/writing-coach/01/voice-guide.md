# Voice guide: when-ai-breaks/chatgpt-data-leak

## How this piece should sound

This lesson has one advantage the exemplars below did not always have. The
reader will already know what a shared cache and a connection pool are for,
because the piece will just have taught it. Once that's taught, write the
March 20, 2023 timeline the way Greenberg opens Maersk's: the date first,
then the specific thing people actually saw. A user who opened ChatGPT and
saw someone else's chat title in their own sidebar is the moment to render,
in the same literal way Greenberg renders the words that were actually
printed on Maersk's frozen screens.

When the mechanism itself is on the page, a cancelled request, a connection
returned to a pool, that connection handed to someone else's request under
load, take Luu's move on the tweet-service death spiral and write the causal
chain out inside the sentence, step to step. The reader has no backend code
to check an asserted cause against, so the chain has to be visible in the
prose itself. Redis, connection pooling, and request cancellation are this
lesson's terms of art. Each earns a plain-word definition in the sentence
where it first appears, the way Orosz defines "kernel level" the instant he
uses it: by saying what having that level of access lets a process do.

Where OpenAI's postmortem states a number, how many users, which fields, how
long the exposure window ran, use that number the way Yao Yue's 95 percent
success-rate figure is used: as the thing that carries the sentence, in place
of a word like "unreliable." Where the postmortem's account changed, or the
Garante's concern reached beyond this one incident, name what changed and
what stayed the same. A reader can hold that; a reader cannot hold "the
record is contested."

Keep the register the one paragraph in Orosz's recap already sets. The
businesses hit are airlines, banks, supermarkets, named as the kinds of
places they are, not folded into "critical infrastructure." Do the same for
who a shared, pooled backend serves today: name the kind of service, not the
category. A plain sentence that names the actual thing beats an atmospheric
one about the general danger of concurrency every time.

## Andy Greenberg, "The Untold Story of NotPetya, the Most Devastating Cyberattack in History"

Source: https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/

> "And on the afternoon of June 27, 2017, confused Maersk staffers began to
> gather at that help desk in twos and threes, almost all of them carrying
> laptops. On the machines' screens were messages in red and black
> lettering. Some read "repairing file system on C:" with a stark warning
> not to turn off the computer. Others, more surreally, read "oops, your
> important files are encrypted" and demanded a payment of $300 worth of
> bitcoin to decrypt them."

The date and the company arrive in the sentence's first clause, before
anything happens, so the reader is never made to wait for the who and when.
Greenberg then quotes what was actually printed on the screens: the exact
lines, the exact ransom figure. The reader sees the incident the way the
staffers first saw it.

> "NotPetya was propelled by two powerful hacker exploits working in tandem:
> One was a penetration tool known as EternalBlue, created by the US
> National Security Agency but leaked in a disastrous breach of the
> agency's ultrasecret files earlier in 2017. EternalBlue takes advantage
> of a vulnerability in a particular Windows protocol, allowing hackers
> free rein to remotely run their own code on any unpatched machine."

The tool is named once, then explained in a single sentence built from what
it let someone do: "free rein to remotely run their own code." Greenberg
gives the tool's origin, the NSA and the leak, before its function, so the
reader has a reason to care about the mechanism before the technical clause
arrives.

> "'I saw a wave of screens turning black. Black, black, black. Black black
> black black black,' he says. The PCs, Jensen and his neighbors quickly
> discovered, were irreversibly locked. Restarting only returned them to
> the same black screen."

The repetition is the source's own words. The sentence that follows states
the technical fact plainly: locked, unfixable by restarting, with no
adjective doing the work the quote already did. The person is visible in the
rhythm of his own sentence, in the counting of the black screens one by one.

## Dan Luu (with Yao Yue), "A decade of major cache incidents at Twitter"

Source: https://danluu.com/cache-incidents/

> "Every single incident so far has at least mentioned cache. In fact, for a
> long time, cache was probably the #1 source of bringing the site down for
> a while.
>
> In my first six months, every time I restarted a cache server, it was a
> `SEV-0` by today's standards. On a good day, you might have 95% Success
> Rate (SR) [for external requests to the site] if I restarted one cache
> ..."

The scale of the problem is carried by one concrete figure: a 95 percent
success rate on what the speaker calls a good day. The bracketed gloss is the
only place the writer steps into someone else's quote, and it does one job:
defining the one term the quote needed before moving on.

> "Cache failure modes are also interesting because, when cache is used to
> serve a significant fraction of requests or fraction of data, cache
> outages or even degradation can easily cause a total outage because an
> architecture designed with cache performance in mind will not (and should
> not) have backing DB store performance that's sufficient to keep the site
> up."

One sentence carries the whole reason a cache problem becomes a site-wide
problem: what the cache is there to do, and what the rest of the system was
never built to do without it. The cause and its effect are both stated, in
the same sentence, so neither has to be taken on faith.

> "Increased cache latency along with the design of tweet service using
> cache caused shards of the service using cache to enter a GC death spiral
> (more latency -> more outstanding requests -> more GC pressure -> more
> load on the shard -> more latency), which then caused increased load on
> remaining shards."

The feedback loop is spelled out as its own chain of arrows, inside the
sentence, step named after step. The parenthetical does the work a diagram
would, without leaving the sentence or the page.

## Gergely Orosz, "The biggest-ever global outage: lessons for software engineers"

Source: https://newsletter.pragmaticengineer.com/p/the-biggest-ever-global-outage-lessons

> "The instruction that crashed is the Assembly instruction "mov r9d,
> [r8]." This instructs to move the bytes in the r8 address to the r9d one.
> The problem is that r8 is an unmapped address (invalid), and so the
> process crashes!"

Orosz names the exact instruction, for the reader who can check it, then
immediately restates what it does in a sentence built from ordinary verbs:
move, is, crashes. The literal detail and the plain-language version sit
side by side, and each carries its own part of the sentence.

> "CrowdStrike's software operates at the kernel level in Windows, meaning
> its process is operating with the highest level of privileges and access
> in the OS. This means it can crash the whole system; for example, by
> corrupting part of the OS's memory. CrowdStrike operating at this level
> is necessary for it to oversee processes running across the OS, and to
> discover threats and vulnerabilities. But this also means that an update
> – even an innocent-looking content file! – can cause a crash."

The term "kernel level" is defined the moment it appears, by saying what that
level of access lets the software do. The passage then gives both the
danger and the reason the company needed that access in the first place,
holding both in view at once.

> "Millions of Windows 10 and 11 operating systems used by
> societally-critical businesses like airlines, banks, supermarkets, police
> departments, hospitals, TV channels, etc, suddenly crashed with the
> dreaded "Blue Screen of Death," and no obvious way to fix them."

The scale is a list of the actual kinds of businesses hit: airlines, banks,
supermarkets, named one after another. A reader can picture an airline
counter and a hospital admissions desk on their own, from the names alone.
