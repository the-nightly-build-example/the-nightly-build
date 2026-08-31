# Voice guide: the-evidence/adversarial-examples

## How this piece should sound

The reader arrives knowing that a photo of a panda can be nudged into a
confident "gibbon" by a change they cannot see, and knowing nothing about why.
The lesson's job is to make the mechanism behind that image ordinary. Dan Luu's
branch-prediction piece shows the move: he starts from the simplest thing a CPU
could do, shows why it is too slow, and only then introduces the real design.
The panda example can carry the same weight when the piece earns the mechanism
the same way, building up to it so the reader is ready before it is named. The
Fast Gradient Sign Method reads as the obvious thing to try once the reader can
already see why a tiny, carefully chosen change to the pixels would move the
model so far.

Keep the abstractions anchored to something the reader already holds, the way
Simon Willison drops a claim about billion-parameter models onto an iPhone
keyboard suggesting the next word. Terms the reader does not have, perturbation,
the linear explanation, the model's decision boundary, land better attached to
the panda's pixels than defined in the open air. Willison also shows how to be
honest about a limit without raising your voice: he makes the model fabricate an
answer, names the fabricated detail, and states the limit in one plain sentence.
When the piece weighs the imperceptible-perturbation threat model against the
real-world attacks that exist, that same order is available, the concrete case
first and the sober line after it.

The paper's confidence is part of the story, and so is what a decade did to it.
Scott Aaronson's FAQ holds a firm judgment about a famous result while keeping
every word of it tied to the numbers, the chip size and the size of the speedup.
The paper's own claims can be given their real scale the same way, the size of
the perturbation and the confidence the model reported, before they are weighed.
Aaronson also pins a slippery term to one exact meaning and sets aside the larger
thing people hear in it. "Adversarial examples are solved" and "the linear
explanation is right" are the kind of claims that reward that discipline: say
which version the evidence supports and which it does not. A measured verdict is
welcome here, and it reads as measured only when the reader has already seen the
evidence it rests on.

None of this needs a grand word to carry it. The image of a panda read as a
gibbon is already striking, and the register that fits is the plain one all three
writers use when they explain: short true sentences, the real numbers, and a
verdict on whether the problem was solved only where the evidence for it is on
the page.

## Dan Luu, "Branch prediction"

Source: https://danluu.com/branch-prediction/

> "One way you might design a CPU is to have the CPU do all of the work for one instruction, then move on to the next instruction, do all of the work for the next instruction, and so on. There's nothing wrong with this; a lot of older CPUs did this, and some modern very low-cost CPUs still do this. But if you want to make a faster CPU, you might make a CPU that works like an assembly line."

He builds the idea from its plainest version first, shows why that version is
slow, and only then reaches for the assembly line, so the reader meets pipelining
already holding the problem it solves. Luu is visible in the patience of it: he
will not introduce the real mechanism until the reader would ask for it
themselves.

> "I think that a lot of people have an idea that CPUs are mysterious and hard to understand, but I think that CPUs are actually easier to understand than software. I might be biased because I used to work on CPUs, but I think that this is not a result of my bias but something fundamental."

The verdict is stated flatly, then checked against his own possible bias, which
he leaves in the reader's view. This is where Luu the former hardware engineer
shows: he gives a plain opinion and hands the reader the exact reason it might be
wrong.

## Simon Willison, "Catching up on the weird world of LLMs"

Source: https://simonwillison.net/2023/Aug/3/weird-world-of-llms/

> "How do they do all this? It really is as simple as guessing the next word in a sentence. If you've used an iPhone keyboard and type "I enjoy eating" it suggests words like "breakfast." That's what a language model is doing."

Willison takes the reader's own phone as the worked example, so a claim about
billion-parameter models lands on something the reader has done with their thumb.
He is visible in the refusal to make it sound harder than it is: the simplest
true account of the mechanism, set down without hedging.

> "It told me, very convincingly, that the paper was published in 2021 by researchers at Google DeepMind. This is not true, it's completely fabricated! The thing language models are best at is producing incredibly convincing text, whether or not it's actually true."

He shows the model failing on a specific question he actually asked, names the
fabricated detail, and only then states the limit in one plain sentence. Willison
earns the general claim by demonstrating it first, which is how he stays honest
about what the technology cannot do without tipping into alarm.

## Scott Aaronson, "Scott's Supreme Quantum Supremacy FAQ!"

Source: https://scottaaronson.blog/?p=4317

> "With a 53-qubit chip, it's perfectly feasible to see a speedup by a factor of many millions, in a regime where you can still directly verify the outputs, and also to see that the speedup is growing exponentially with the number of qubits, exactly as asymptotic analysis would predict. This isn't marginal."

He gives the numbers that matter first, the chip size and the size of the
speedup, and the plain verdict follows them and rests on them. Aaronson is
visible in the confidence, but it is confidence a reader can check, because every
word of it is tied to the figure just stated.

> "This is purely a confusion over words. Those other experiments demonstrated other forms of "quantum supremacy": for example, in the case of Bell inequality violations, what you could call "quantum correlational supremacy." They did not demonstrate quantum computational supremacy, meaning doing something that's infeasible to simulate using a classical computer (where the classical simulation has no restrictions of spatial locality or anything else of that kind)."

He pins a slippery term to one exact meaning, then names the near-synonym it gets
confused with and sets it aside. Aaronson the complexity theorist shows here in
the insistence that the claim means one specific thing and not the larger thing
people hear in the phrase.
