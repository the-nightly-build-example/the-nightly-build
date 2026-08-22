# Voice guide: the-evidence/whisper (01)

## How this piece should sound

This is a lesson in The Evidence: it takes one famous document about speech
recognition and tells a smart, widely read reader, who has no background in the
field, what the paper actually did and what it measured. The register is plain
and concrete, closer to how Matt Yglesias explains something he understands well
than to how a paper announces a result. Where a sentence could either sound
impressive or be understood, it should be understood.

Define each term the moment the lesson first needs it, in the same sentence, the
way Julia Evans names "resolver" and "authoritative nameservers" as she walks
through a single request. Word error rate, weak supervision, and zero-shot
evaluation are the terms a reader new to speech recognition will not already
hold; each can arrive attached to what it does, with the plain-words definition
beside its first use, so nothing rests on a term the reader was not yet given.

Explaining plainly does not mean thinning the material out. Evans wants all the
information and wants it presented clearly, and she refuses to let those be in
tension. The real vocabulary of the field belongs on the page, an error rate,
hours of transcribed audio, the difference between testing on held-out data and
testing on audio the model never trained on, made legible rather than removed.

The paper rests on numbers a reader cannot scale on their own: hours of audio,
the size of a training corpus, error rates across many datasets. Ed Yong's
handling of "15,305 participants" and "60 times as many volunteers as the studies
they were attempting to replicate" shows one way through it: give the figure,
then set it against a comparison the reader already holds, such as the scale of
the supervised sets that came before. When the figure is reported plainly it can
carry the stakes by itself; Yong gives "14 out of 28" first and his read on it
second, and never inflates it. This paper has no appetite for hype or doom, so a
well-placed figure, stated flat, is often where the weight should sit.

When a claim is abstract, a worked case under it does the teaching, the way Yong
grounds "failed to replicate half" in the particular effects that failed. A
single transcription, the words that were spoken, what the model wrote, where the
errors fall, can show what an error rate measures better than a definition
standing alone.

A reported number is worth examining rather than repeating. Dan Luu's flat
observation that most published measurements are not very good, and that readers
rarely have a way to tell a sound measurement from an invalid one, is the
disposition to bring when the lesson asks what a benchmark result actually
establishes and under what conditions it was collected. The analysis stays
earned: the data the paper used and the way it tested are the ground the reader
should be able to see under any judgment.

Say plainly where knowledge stops. Evans quotes an error message she cannot fully
explain and admits it rather than bluffing past it. The same honesty fits
wherever the document, or the work that came after it, leaves something
unresolved, and a lesson that marks the edge of what is known reads as more
trustworthy on everything inside it.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "A question I get asked with some frequency is: why bother measuring X, why not build something instead? More bluntly, in a recent conversation with a newsletter author, his comment on some future measurement projects I wanted to do (in the same vein as other projects like keyboard vs. mouse, keyboard, terminal and end-to-end latency measurements), delivered with a smug look and a bit contempt in the tone, was "so you just want to get to the top of Hacker News?""

Luu opens on a real exchange, a newsletter author asking with a smug look
whether he is just chasing internet points, instead of asserting up front that
measurement is undervalued. The reader meets a person and a tone before meeting
the argument, and the concrete scene carries a claim that a flat framing would
have drained. Luu's willingness to quote the dig against him, unflattering to
him, is part of why the voice reads as honest.

> "At the time, a common pattern in online discussions of distributed correctness was:
> Person A: Database X corrupted my data.
> Person B: It works for me. It's never corrupted my data.
> A: How do you know? Do you ever check for data corruption?
> B: What do you mean? I'd know if we had data corruption (alternate answer: sure, we sometimes have data corruption, but it's probably a hardware problem and therefore not our fault)"

He stages a common industry argument as a four-line dialogue, so a vague dispute
about whether databases silently lose data becomes something the reader can hear.
The move turns an abstraction into two people talking past each other. Luu's ear
for how engineers actually deflect a bug report shows in the parenthetical
alternate answer, which is the deflection he has heard many times.

> "One thing that both increases and decreases the impact of doing good measurements is that most measurements that are published aren't very good. This increases the personal value of understanding how to do good measurements and of doing good measurements, but it blunts the impact on other people, since people generally don't understand what makes measurements invalid and don't have a good algorithm for deciding which measurements to trust."

Luu states flatly that most published measurements are not very good, then says
exactly why it matters: readers have no reliable way to tell an invalid
measurement from a sound one. The claim is strong and is immediately grounded in
a mechanism rather than left as an attitude. This is the sound of a writer who
treats a number as something to inspect before repeating it.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When you make a DNS request on your computer, the basic story is:
> your computer makes a request to a server called resolver
> the resolver checks its cache, and makes requests to some other servers called authoritative nameservers"

Evans introduces "resolver" and "authoritative nameservers" in the same lines as
the steps they name, so each term arrives already attached to what it does. She
gives the shape of the whole process in three short lines before any detail
arrives. Nothing here assumes a word she has not just defined, which is why a
newcomer can follow it on the first read.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. ... And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

Evans draws a line between explaining clearly and stripping information out, and
puts herself firmly on the side of keeping all of it while making it readable.
The passage states a working principle for explanatory writing without announcing
it as a principle. Her impatience, "I want to see all the information!", is where
the person is visible.

> "Here I've requested a nonexistent domain, and I got the extended error EDE: 12 (NSEC Missing): (Invalid denial of existence of xjwudh.com/a). I'm not sure what that means (it's some DNSSEC Thing), but it's cool to see an extra debug message like that."

Evans quotes a real error message, then admits she does not fully understand it
and calls it "some DNSSEC Thing" rather than bluffing past the gap. The admission
costs her nothing and earns the reader's trust, because it shows the rest of the
piece is not bluffing either. That offhand honesty about the limits of her own
knowledge is where the person shows.

## Ed Yong, "Psychology's Replication Crisis Is Running Out of Excuses"

Source: https://www.theatlantic.com/science/archive/2018/11/psychologys-replication-crisis-real/576223/

> "Over the past few years, an international team of almost 200 psychologists has been trying to repeat a set of previously published experiments from its field, to see if it can get the same results. Despite its best efforts, the project, called Many Labs 2, has only succeeded in 14 out of 28 cases. Six years ago, that might have been shocking. Now it comes as expected (if still somewhat disturbing) news."

Yong opens with the exact result, 14 of 28, and declines to oversell it, calling
it expected news that is only "somewhat disturbing." He gives the finding first
and his read on it second, so the number lands before any interpretation shapes
it. The restraint is the craft: the figure is left to do its own work.

> "The Many Labs 2 project was specifically designed to address these criticisms. With 15,305 participants in total, the new experiments had, on average, 60 times as many volunteers as the studies they were attempting to replicate. The researchers involved worked with the scientists behind the original studies to vet and check every detail of the experiments beforehand."

Yong reports the study's size as a raw count, 15,305 participants, then anchors it
to something the reader can feel, 60 times as many volunteers as the original
studies. The comparison does the work the bare number cannot, since few readers
can sense what 15,305 means until it is set against what came before. He also
notes what that scale bought, checking every detail with the original teams,
which pre-empts the obvious objection.

> "Despite the large sample sizes and the blessings of the original teams, the team failed to replicate half of the studies it focused on. It couldn't, for example, show that people subconsciously exposed to the concept of heat were more likely to believe in global warming, or that moral transgressions create a need for physical cleanliness in the style of Lady Macbeth, or that people who grow up with more siblings are more altruistic."

Rather than leave "failed to replicate half" as a statistic, Yong lists the
specific effects that failed, heat and belief in global warming, moral
transgressions and a need for cleanliness, siblings and altruism. The concrete
cases let the reader feel what did not hold up. The plain naming, with no
adjective doing the persuading, is Yong's hand.
