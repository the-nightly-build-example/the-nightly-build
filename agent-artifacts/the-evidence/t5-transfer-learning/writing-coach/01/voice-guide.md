# Voice guide: the-evidence/t5-transfer-learning (01)

## How this piece should sound

This lesson teaches one document — Google's "Exploring the Limits of Transfer
Learning with a Unified Text-to-Text Transformer" — to a reader who is smart
and well-read but has never opened a training script. Nothing here should read
as though it assumes otherwise. The three exemplars below share one habit
worth taking whole: none of them lets an abstraction stand on its own
sentence. Wolfram doesn't assert that a model differs from a lookup table and
move on; he gives Galileo, the Tower of Pisa, and a specific table of drop
times before the general point ever needs stating. When this lesson has to
explain what an ablation study is, or why comparing setups by changing one
thing at a time is the paper's whole method, it can do the same: put a small,
literal case on the page first, the way the cannonball comes before the
theory of models.

Lee and Trott's habit of extending a single analogy in stages, rather than
dropping it on the page fully formed, applies directly to T5's text-to-text
framing. If an analogy is used to make "every task is the same kind of
problem" click, it can be built the way the shower-faucet analogy is built —
one addition at a time, so each new piece of the mechanism has somewhere to
land — rather than asked to carry the whole idea in one sentence. And
wherever the piece states a raw scale figure from the paper — the size of the
training corpus, the width of a parameter sweep, however many variants an
ablation compares — Wolfram's n-gram paragraph and Lee and Trott's
child-language-exposure line show the same fix: set the number beside one the
reader already has some feel for, and let the comparison carry the judgment
instead of an adjective.

Evans's rewrite of her own "header files are crucial tools" complaint is a
fair bar for this lesson's definitions. When a term of art enters — span
corruption, a denoising objective, whatever vocabulary the paper itself
uses — the sentence defining it should be checkable, the way her header-file
rewrite is checkable against an actual compiler error, rather than settling
for a plainer-sounding restatement of the same abstraction.

The paper's own results will sometimes support a weak why rather than a
clean one: an ablation that shows one setup did better without fully
explaining why, or a result the paper itself flags as preliminary. Evans's
point that a weak why beats no why, and Lee and Trott's willingness to say
outright that even a heavily studied case is "still far from" a full
explanation, describe the same discipline: report the evidence at the
strength it actually has rather than rounding it up to a tidier conclusion.
This is The Evidence, and the job is showing the reader what the document
supports — so that discipline matters more here than any single sentence
sounding more settled than the paper is.

## Timothy B. Lee and Sean Trott, "Large language models, explained with a minimum of math and jargon"

Source: https://www.understandingai.org/p/large-language-models-explained-with

> "Here's an analogy to illustrate how this works. Suppose you're going to
> take a shower, and you want the temperature to be just right: not too hot,
> and not too cold. You've never used this faucet before, so you point the
> knob to a random direction and feel the temperature of the water. If it's
> too hot, you turn it one way; if it's too cold, you turn it the other way.
> The closer you get to the right temperature, the smaller the adjustments
> you make.
>
> Now let's make a couple of changes to the analogy. First, imagine that
> there are 50,257 faucets instead of just one. Each faucet corresponds to a
> different word like the, cat, or bank. Your goal is to have water only come
> out of the faucet corresponding to the next word in a sequence."

The analogy doesn't arrive complete. It starts with one faucet and the plain
mechanics of finding a comfortable temperature, and only in the next
paragraph adds the detail — 50,257 faucets — that turns a shower metaphor
into a picture of training. The sentence "the closer you get to the right
temperature, the smaller the adjustments you make" is doing the actual
explanatory work (it describes what gradient descent does) without naming the
term at all.

> "We love this example because it illustrates just how difficult it will be
> to fully understand LLMs. The five-member Redwood team published a 25-page
> paper explaining how they identified and validated these attention heads.
> Yet even after they did all that work, we are still far from having a
> comprehensive explanation for why GPT-2 decided to predict Mary as the next
> word."

The judgment in the first sentence is earned by the specific numbers that
follow it — a five-member team, a 25-page paper — rather than asserted on its
own. The writers are visible in the willingness to say plainly that a
significant piece of published research still falls short of a full answer,
instead of describing the research as more conclusive than it was.

> "One reason is scale. It's hard to overstate the sheer number of examples
> that a model like GPT-3 sees. GPT-3 was trained on a corpus of
> approximately 500 billion words. For comparison a typical human child
> encounters roughly 100 million words by age 10."

The 500-billion-word figure means little by itself, so the next sentence
supplies a number the reader already has some feel for — how much language a
child hears by age ten — and lets the size of the gap do the work. Nothing in
the passage is called massive or staggering; the comparison itself carries
that judgment.

## Stephen Wolfram, "What Is ChatGPT Doing … and Why Does It Work?"

Source: https://writings.stephenwolfram.com/2023/02/what-is-chatgpt-doing-and-why-does-it-work/

> "That ChatGPT can automatically generate something that reads even
> superficially like human-written text is remarkable, and unexpected. But
> how does it do it? And why does it work?"

The piece opens by naming the actual questions it intends to answer, in two
short sentences back to back, rather than easing in with context the reader
doesn't need yet. The pace is set immediately: short sentences doing the work
of framing the piece, not filling space before the real content starts.

> "But here's the problem: there just isn't even close to enough English text
> that's ever been written to be able to deduce those probabilities. In a
> crawl of the web there might be a few hundred billion words; in books that
> have been digitized there might be another hundred billion words. But with
> 40,000 common words, even the number of possible 2-grams is already 1.6
> billion — and the number of possible 3-grams is 60 trillion. So there's no
> way we can estimate the probabilities even for all of these from text
> that's out there. And by the time we get to "essay fragments" of 20 words,
> the number of possibilities is larger than the number of particles in the
> universe, so in a sense they could never all be written down."

Each sentence adds one more concrete number, and the numbers are chosen to
build toward a single comparison the reader can actually picture — more
possibilities than particles in the universe — rather than toward a general
claim about how large the number is. Once that comparison lands, the
paragraph stops; there's no follow-up sentence editorializing about how large
the number was.

> "Say you want to know (as Galileo did back in the late 1500s) how long it's
> going to take a cannon ball dropped from each floor of the Tower of Pisa to
> hit the ground. Well, you could just measure it in each case and make a
> table of the results. Or you could do what is the essence of theoretical
> science: make a model that gives some kind of procedure for computing the
> answer rather than just measuring and remembering each case."

An abstract methodological idea — what a model is, as distinct from a table
of measurements — is introduced through a specific historical case with a
name, a date, and a place attached, and the general definition only shows up
in the sentence after the concrete version is already on the page.

## Julia Evans, "Patterns in confusing explanations"

Source: https://jvns.ca/blog/confusing-explanations/

> "The outdated assumption here is that you (the reader) know how other
> version control systems implement branching, and that comparing other
> tools' implementation of branching to Git's implementation will help you
> understand branching. But if you're reading this and you've never used
> another version control system and never plan to, this explanation is
> useless! Who cares about how other version control systems implement
> branching? You just want to understand how Git works!"

The paragraph names exactly what background knowledge an earlier explanation
assumed, and why that assumption used to be reasonable, rather than just
labeling the explanation confusing. The complaint is falsifiable: a reader
can check, concretely, whether they actually hold the knowledge the sentence
assumed they had.

> "Almost every C program includes header files. For example, if you've ever
> written #include <stdio.h> at the beginning of a C program, stdio.h is a
> header file. #include basically tells the C preprocessor to paste the
> contents of stdio.h at the beginning of the program.
>
> One reason header files are important is that they define types and
> constants you need in your programs. For example, this code by itself will
> fail to compile with the error error: unknown type name 'FILE', because the
> FILE type is undefined."

This replaces a vaguer sentence from elsewhere ("header files are crucial
tools") with the literal error a reader would see on their own screen. The
claim about importance isn't asserted; it's demonstrated with a fact the
reader could go reproduce.

> "But as a reader, I find that a weak "why" is much better than no "why".
> I'd rather read "well, we use Kubernetes because it provides a decent basic
> deployment system and GKE means we don't have to think about servers" than
> an attempt at covering every single company's business reasons for using
> Kubernetes."

The judgment is stated as a comparison rather than a rule, and it's
immediately backed with an actual weak-but-real reason someone gave, instead
of a general claim about what a good explanation needs. The writer settles
for an honest partial answer instead of manufacturing a comprehensive one.
