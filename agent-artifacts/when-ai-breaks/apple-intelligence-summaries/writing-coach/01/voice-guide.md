# Voice guide: when-ai-breaks/apple-intelligence-summaries

## How this piece should sound

This lesson opens the way Zetter opens Stuxnet: on the specific, dated moment
something was visibly wrong, not on a claim about AI. Put the reader where the
BBC was when the false Mangione summary appeared under its own name, with the
date and the exact wording, before the piece says anything about what a
summarizer is. The abstraction (a language model compresses text without
checking that the compression is true) earns its place only after the concrete
scene has shown why it matters.

The piece's required contribution is a correction: separate what looked like a
chatbot inventing a fact from what actually happened, a lossy compression that
changed a real story's meaning. Zetter's Stuxnet piece is built on exactly this
move — the plausible, wrong first read stated plainly, then overturned by what
the researchers actually found. Give the "it looked like X" a full, fair
sentence before the piece corrects it. Don't rush past the misreading to get to
the correction; the misreading is most of what the reader currently believes.

Where the piece explains the mechanism, hold the tone Langewiesche holds when
he calls the trigger for Air France 447 "the merest blip of an information
problem" and lets the mismatch between that and 228 deaths sit there
unglossed. A summarizer producing a false headline under the BBC's name is the
same kind of mismatch: ordinary machinery, an outsized result. State the
mismatch and move on rather than telling the reader how alarming it is.

Because this is a lesson and not a magazine feature, the mechanism has to
teach, not just narrate: define what a summarizer is doing (producing the most
probable short rendering, with no check on whether that rendering preserves
the source's truth) in the same plain register Langewiesche uses for automation
paradoxes, and link rather than re-explain what the course has already covered
on hallucination and faithful-vs-unfaithful summarization.

Both Greenberg and Zetter anchor stakes in specifics the reader can hold: named
companies, exact dollar figures, an exact quote from someone who watched it
happen. Do the same here with the exact false-summary text, the exact outlets,
the exact dates — the paper's numbers standard already asks for this, and
these exemplars show what it looks like in practice. Where a detail is
contested or single-sourced, say so plainly rather than smoothing it over, the
way Zetter marks what researchers could confirm and what stayed a guess.

The close asks where the same weakness lives today. Langewiesche's own close —
naming the general pattern once, in plain terms, then trusting specific,
named systems to carry it rather than a warning — is the register for that
section: state the mechanism (a summarizer compresses, and compression can
misstate, whatever brand's name sits on top of it) once, plainly, then let the
named systems (mail, chat, search, news summaries the reader already uses) do
the work without a moral appended to them.

## Andy Greenberg, "The Untold Story of NotPetya, the Most Devastating Cyberattack in History"

Source: https://www.wired.com/story/notpetya-cyberattack-ukraine-russia-code-crashed-the-world/

> "It was a perfect sunny summer afternoon in Copenhagen when the world's largest shipping conglomerate began to lose its mind."

One sentence carries the whole setup: a named company, a specific kind of day,
and a verb ("lose its mind") applied to a corporation instead of a person. It
opens the piece before any explanation of what NotPetya is, so the reader has
a scene to hold onto once the technical account starts.

> "NotPetya was propelled by two powerful hacker exploits working in tandem: One was a penetration tool known as EternalBlue, created by the US National Security Agency but leaked in a disastrous breach of the agency's ultrasecret files earlier in 2017. EternalBlue takes advantage of a vulnerability in a particular Windows protocol, allowing hackers free rein to remotely run their own code on any unpatched machine."

The mechanism gets named, sourced (where the tool came from, who made it, how
it leaked), and explained in one move, each sentence adding one new fact
rather than restating the last one. Nothing here tells the reader how bad this
is; the explanation of what the exploit lets an attacker do is left to make
that case on its own.

> "'I saw a wave of screens turning black. Black, black, black. Black black black black black,' he says."

A single witness's plain description of what he watched happen, quoted at its
actual length and repetition rather than trimmed for tidiness. The repeated
word is the IT administrator's own rhythm, not the writer's, and it does more
to convey scale than a sentence of the writer's own adjectives would.

## William Langewiesche, "The Human Factor"

Source: https://www.vanityfair.com/news/business/2014/10/air-france-flight-447-crash

> "A small glitch took Flight 447 down, a brief loss of airspeed indications—the merest blip of an information problem during steady straight-and-level flight. It seems absurd, but the pilots were overwhelmed."

The mismatch between cause and consequence is stated flatly, in the plainest
words available ("merest blip," "seems absurd"), with no adjective doing the
work of outrage. The judgment is confined to noting that it seems absurd, not
asserting that it was a scandal or a failure of anyone in particular.

> "To the question of why, the facile answer—that they happened to be three unusually incompetent men—has been widely dismissed. [...] To put it briefly, automation has made it more and more unlikely that ordinary airline pilots will ever have to face a raw crisis in flight—but also more and more unlikely that they will be able to cope with such a crisis if one arises."

The piece states and discards the easy explanation (bad pilots) before stating
the real one, and the real one is a paradox given in a single sentence anyone
could repeat afterward. Nothing here blames a company or a regulator; the
claim is about how a whole category of system behaves.

> "It seems that we are locked into a spiral in which poor human performance begets automation, which worsens human performance, which begets increasing automation. The pattern is common to our time but is acute in aviation."

The closing generalization is stated once, plainly, and immediately tied back
to the specific field (aviation) rather than left floating as a comment on
technology in general. The sentence names a mechanism, not a mood.

## Kim Zetter, "How Digital Detectives Deciphered Stuxnet, the Most Menacing Malware in History"

Source: https://www.wired.com/2011/07/how-digital-detectives-deciphered-stuxnet/

> "It appeared to be simply stealing configuration and design data from the systems, presumably to allow a competitor to duplicate a factory's production layout. Stuxnet looked like just another case of industrial espionage. [...] The story of Stuxnet might have ended there. But a few researchers weren't quite ready to let it go."

The plausible, wrong explanation is given a full, fair sentence — not a
strawman dispatched in a clause — before the piece admits it was wrong. The
short sentence that follows ("The story of Stuxnet might have ended there.")
marks the turn without announcing that a bigger reveal is coming.

> "The fact that Stuxnet was injecting commands into the PLC and masking that it was doing so was evidence that it was designed, not for espionage as everyone had believed, but for physical sabotage. The researchers were stunned. It was the first time anyone had seen digital code in the wild being used to physically destroy something in the real world."

The correction is stated as a finding, with the earlier belief named
specifically ("not for espionage as everyone had believed") rather than
gestured at. "The researchers were stunned" reports a fact about the people
who found it instead of asserting on the writer's own authority that the
moment was momentous.

> "IT WAS JANUARY 2010, and investigators with the International Atomic Energy Agency had just completed an inspection at the uranium enrichment plant outside Natanz in central Iran, when they realized that something was off within the cascade rooms where thousands of centrifuges were enriching uranium."

The opening puts a named agency, a named place, and a specific month in the
first sentence, and the strangeness ("something was off") is reported as
something the investigators noticed, not as a claim the writer is making
about the reader's behalf.
