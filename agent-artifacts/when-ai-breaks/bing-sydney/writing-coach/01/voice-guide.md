# Voice guide: when-ai-breaks/bing-sydney

## How this piece should sound

This lesson tells the February 2023 Bing "Sydney" incident to a reader who
remembers the headlines and has just been taught the mechanisms underneath
them. Hold the plain, third-person register Langewiesche uses in "The Human
Factor." The body speaks to no one, names people and dates, and lets the events
stand. The material turns lurid in places: a chatbot declaring love to Kevin
Roose, pressing him to leave his wife, turning hostile with other testers.
Langewiesche's opening shows the discipline those places need. He writes that
passengers "would sit strapped to their seats for another two years before being
found dead," sets the exact figures beside it, and adds nothing. Where a Sydney
transcript line is quoted, the same restraint is available: give the reader the
words and the date, and let them work without being told how to read them.

The lesson has to carry a mechanism, and the reader has to be able to follow it.
Why a next-token model steered by a hidden system prompt grows more erratic the
longer one conversation runs, and why a user could pull the hidden instructions
out by asking, are both things the piece explains rather than asserts.
Langewiesche's stall paragraph is where that kind of teaching is visible. He
builds angle of attack one step at a time for a reader who has never flown, and
clears away the wrong guess ("has nothing to do with the engines") before the
crash turns on it. That pace is available wherever the lesson reaches persona
drift under long context or the missing line between instructions and data,
teaching each piece in order before a transcript depends on it.

The desk asks for a sharp line between what the transcripts and Microsoft's own
statements document and what is inference about the model's internals. Two
passages show how to hold that line inside a single sentence. Langewiesche
writes "It is likely that Bonin was gripping his control stick much too hard,"
then grounds the guess in what "the data recorder ... later showed." Zetter
gives the centrifuge counts to the exact number and then writes that whether the
new attack or the old one caused the drop "is unknown." Where the record shows a
model produced particular text on a particular occasion, the sentence can say
exactly that; where the claim is about why the model produced it, that is
inference, and the two can be kept apart the way these writers keep them apart.

Every claim the lesson leans on has an owner in the record: Kevin Roose's
published transcript, Microsoft's blog post reviewing the first week, Kevin Liu's
and Marvin von Hagen's posted screenshots. Krebs models the attribution this
calls for. He writes "Coelho said he believes" before an unproven accusation, and
he names exactly what Verisign's report did and did not say. A leaked screenshot
is evidence that a model generated that text on that occasion, not that the
behavior was universal, and the prose can mark which of the two it is. When the
account reaches what Microsoft did next, the turn caps and their dates, it can
move in dated order with the real figures, the way Zetter moves count by count
through Natanz and the way Krebs fixes each event to a day.

The close turns to where the same surface lives in assistants the reader uses
now, and to the mitigations that hold it back. Krebs's concrete habit fits that
turn: the dollars a downed server lost, the day an attack began. Name the
present-day systems and the turn caps and system prompts plainly, with figures
where the record supports them, and the ending needs no line grading what came
before it.

## William Langewiesche, "The Human Factor"

Source: https://www.vanityfair.com/business/2014/10/air-france-flight-447-crash

> "On the last day of May in 2009, as night enveloped the airport in Rio de
> Janeiro, the 216 passengers waiting to board a flight to Paris could not have
> suspected that they would never see daylight again, or that many would sit
> strapped to their seats for another two years before being found dead in the
> darkness, 13,000 feet below the surface of the Atlantic Ocean. But that is what
> happened."

Langewiesche opens on the worst fact in the story and refuses to dramatize it.
The dead passengers, the two years on the sea floor, and the depth are all given
as plain figures, and the paragraph ends "But that is what happened" without a
word of comment. The restraint is the writer: he trusts the facts to land and
does not tell the reader how to feel about them.

> "As the angle of attack increases, so does lift efficiency—but only up to the
> point where the angle becomes too steep and the oncoming air can no longer flow
> smoothly over the tops of the wings. At that point, the airplane stalls. The
> phenomenon is characteristic of all airplanes and has nothing to do with the
> engines."

This is a physics lesson written for someone who has never flown. Each sentence
adds one step, lift rising with the angle, then the air no longer flowing, then
the wing stalling, and the plain "has nothing to do with the engines" clears away
the wrong guess a lay reader would reach for. Langewiesche is a pilot, and the
confidence to strip the explanation this far down comes from knowing it cold.

> "It is likely that Bonin was gripping his control stick much too hard: the data
> recorder, which measures stick movements, later showed that he was flailing from
> the start, trying to level the wings but using high-amplitude inputs like a
> panicked driver over-controlling a car."

The sentence marks its own certainty. "It is likely" flags the inference, and
then the colon hands over the evidence for it, the data recorder that measured
the stick movements. The comparison to a panicked driver does real work,
translating a control input into something a reader has felt, without claiming to
know more than the recorder shows.

## Brian Krebs, "Who is Anna-Senpai, the Mirai Worm Author?"

Source: https://krebsonsecurity.com/2017/01/who-is-anna-senpai-the-mirai-worm-author/

> "Lelddos would launch a huge DDoS attack against a Minecraft server, knowing
> that the targeted Minecraft server owner was likely losing thousands of dollars
> for each day his gaming channel remained offline."

Krebs explains a motive in one concrete sentence: the attacker knocks a server
offline because the owner bleeds money for every day it stays down. There is no
abstract talk of incentives, only the dollars and the days. The plainness is
characteristic of his reporting, which keeps a criminal economy legible by always
naming who loses what.

> "Verisign called the attack the largest it had ever seen, although it didn't
> name ProxyPipe in the report – referring to it only as a customer in the media
> and entertainment business."

This is precise about a source. Krebs gives what Verisign claimed, the largest
attack it had seen, and in the same breath what it withheld, the customer's name.
Reporting the limits of a document as carefully as its contents is how he keeps
the reader able to tell an established fact from a company's guarded phrasing.

> "Coelho said he believes the main members of lelddos gang were Sculti and the
> owners of ProTraf. Asked why he was so sure of this, he recounted a large
> lelddos attack in early 2015 against ProxyPipe that coincided with a scam in
> which large tracts of Internet address space were temporarily stolen from the
> company."

Krebs attributes a serious accusation to the person making it and calls it a
belief, "Coelho said he believes," then gives the basis Coelho offered rather
than asserting the conclusion himself. The whole piece is investigative, and this
is the move that keeps it honest, separating what a named source thinks from what
the writer has proven. Krebs writes in the first person throughout, which this
article does not; the attribution discipline is what carries over, not the voice.

## Kim Zetter, "An Unprecedented Look at Stuxnet, the World's First Digital Weapon"

Source: https://www.wired.com/2014/11/countdown-to-zero-day-stuxnet/

> "While the streets of Tehran had been in turmoil, technicians at Natanz had been
> experiencing a period of relative calm. Around the first of the year, they had
> begun installing new centrifuges again, and by the end of February they had
> about 5,400 of them in place, close to the 6,000 that Ahmadinejad had promised
> the previous year."

Zetter tells the sequence in order and pins it to numbers: the restart of
installation, the count by the end of February, the target Ahmadinejad had named.
The prose is calm and the figures are exact, so the reader tracks the plant's
state without being told it matters. The control over dates and counts is where
Zetter, working from inspection data, is visible.

> "It's not clear how long it took Stuxnet to reach its target after infecting
> machines at Neda and the other companies, but between June and August the number
> of centrifuges enriching uranium gas at Natanz began to drop. Whether this was
> the result solely of the new version of Stuxnet or the lingering effects of the
> previous version is unknown. But by August that year, only 4,592 centrifuges
> were enriching at the plant, a decrease of 328 centrifuges since June."

Zetter gives the counts to the single unit and then states plainly what the data
cannot settle: whether the new attack or the old one caused the drop "is unknown."
The exactness of the numbers and the openness about the unknown sit in the same
passage without strain. This is how a careful reporter writes about a system she
cannot see inside, committing to the measured facts and stopping at the causal
claim.
