# Voice guide: the-mechanics/poetic-meter

## How this piece should sound

This is a lesson on The Mechanics desk that starts from something the reader has
met firsthand, a chatbot that rhymes a poem passably but botches the meter, and
walks back to why. Write for a reader who is smart and reads widely but has
never looked inside a language model. Hold a plain, concrete register the whole
way, the register Julia Evans keeps when she lists what happens on a DNS request
and then says "here are some things you don't see." The lesson has to move
between two vocabularies without strain: the sound of English, meaning syllables,
stress, a limerick's beat, a haiku's 5-7-5, and the way a model takes in text,
meaning tokens and the decoder and what the representation does and does not
carry. Name each real part and say what it does in plain words, the way Evans
names the resolver and the authoritative nameservers before she explains them.

Evans's line that a clearer format is "not 'dumbed down' or anything" but "the
exact same information, just formatted in a more structured way" is the standard
for handling the technical words here. Keep the load-bearing terms, token,
stress, scansion, phonology, and define each in plain words the first time it
appears. A vaguer near-synonym reached for variety would only blur the thing the
reader is trying to hold. Gretchen McCulloch introduces haplology only once she
has shown the thing it names, and defines it in the same sentence; a term this
lesson cannot proceed without can arrive the same way. A joke that depends on the
subject's own nouns is welcome where it fits, as McCulloch's aside about
shortening haplology to haplogy is.

The sound side becomes teachable through a small example the reader can say
aloud. McCulloch writes "we say PRO-bab-ly, not pro-BAB-ly or pro-bab-LY" and the
reader hears where the stress lands. Where this lesson needs the reader to feel a
syllable count or a stress pattern, a line that scans set against one that does
not, a respelling or a marked line does work that an abstract description of
meter cannot.

When the lesson reaches a settled point about what a model does or does not have,
state it flatly. Evans gives her verdict on dig's output without softening it:
it "has the feeling of a script someone wrote in an adhoc way that grew
organically over time and not something that was intentionally designed." The
countable constraints in fixed-form poems are numbers, and numbers can carry a
sentence on their own; Somers lets "26 years," "70,000 words," and "28 languages"
do the work, and a haiku's 5-7-5 or a pentameter line's ten syllables can do the
same here.

The lesson turns on a real difference between what a person does to hold meter
and what the model has to go on. Somers draws one clean contrast, a dictionary
"built by a large team" against one where "a person labored at his desk," and it
holds because the two things genuinely differ. Where this lesson sets counting
syllables and placing stress beside whatever the model actually works from, the
contrast earns its place only if the two are truly unlike, and it stays out
wherever it would only decorate.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "I write a lot about technologies that I found hard to learn about. A while back my friend Sumana asked me an interesting question – why are these things so hard to learn about? Why do they seem so mysterious?"

Evans opens on a technology the reader already uses and treats the difficulty of
learning it as a fair question rather than a failing. The voice is plainly hers:
she names her friend, quotes the actual question she was asked, and lets her own
long confusion stand in the open. It sets up an explanation by admitting the
thing looked mysterious first.

> "In general dig's output has the feeling of a script someone wrote in an adhoc way that grew organically over time and not something that was intentionally designed."

This is a flat judgment about a tool, stated with no hedging and no inflation.
Evans says exactly what dig's output feels like, and the specific image of a
script that grew organically carries the point. Her impatience with careless
design is visible without her announcing it.

> "And it's not 'dumbed down' or anything! It's the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

Evans draws the line between clear and dumbed-down and comes down hard for
keeping all the information while presenting it well. The passage shows her core
value as an explainer, and the exclamation marks and the blunt "I want to see all
the information" are recognizably her. The plain restatement, same information
and better structure, is what makes the distinction concrete.

## James Somers, "You're probably using the wrong dictionary"

Source: https://jsomers.net/blog/dictionary

> "Dictionaries today are not written this way. In fact it'd be strange even to say that they're written. They are built by a large team, less a work of art than of engineering. When you read an entry you don't get the sense that a person labored at his desk, alone, trying to put the essence of that word into words. That is, you don't get a sense, the way you do from a good novel, that there was another mind as alive as yours on the other side of the page."

Somers marks a real difference between two kinds of thing, and the contrast holds
because the things truly differ: a dictionary built by a team against one written
by a single mind. The judgment is concrete and earned; he builds it from "labored
at his desk, alone," not from an abstract claim about quality. His attachment to
a person being present on the page is the writer showing through.

> "Webster's dictionary took him 26 years to finish. It ended up having 70,000 words. He wrote it all himself, including the etymologies, which required that he learn 28 languages, including Old English, Gothic, German, Greek, Latin, Italian, Spanish, Dutch, Welsh, Russian, Aramaic, Persian, Arabic, and Sanskrit. He was plagued by debt to fund the project; he had to mortgage his home."

Here the facts carry the paragraph with almost no adjectives: twenty-six years,
seventy thousand words, twenty-eight languages, a mortgaged home. Somers trusts
the numbers to convey the scale of one man's labor, and the short declaratives
around one long middle sentence keep the passage from flattening. The awe is in
what he chose to report, not in how he described it.

## Gretchen McCulloch, "Do You Ever Say Probly Instead of Probably? Here's Why."

Source: https://slate.com/human-interest/2014/04/haplology-the-erosion-of-an-unstressed-syllable-so-that-probably-becomes-probly-and-library-becomes-libry.html

> "It's really a question of efficiency. English words tend to have one or two syllables that are stressed. In this case, we say PRO-bab-ly, not pro-BAB-ly or pro-bab-LY. This naturally also means that the stressed syllables are more interesting and important to your production and understanding of the word than the unstressed ones."

McCulloch teaches stress with a word the reader can say aloud, marking the
stressed syllable in capitals so the pattern is audible on the page. The
explanation stays plain and moves in small steps, and the example does work that
a definition of stress alone would not. Her ease with the mechanics of speech
shows in how lightly she handles them.

> "In fact, the omission of one of two consecutive identical syllables is so common in English and other languages that it has its own name: haplology (which is sometimes shortened to haplogy if you want to get self-referential about it)."

McCulloch names the term only after she has shown the thing it describes, and she
defines it in the same sentence. The parenthetical joke about shortening
haplology to haplogy depends entirely on what the word means, so it lands without
slowing the explanation. The light touch is hers, and it never costs her the
point.
