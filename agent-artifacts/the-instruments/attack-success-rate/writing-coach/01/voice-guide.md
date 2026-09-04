# Voice guide: the-instruments/attack-success-rate (01)

## How this piece should sound

This lesson walks a smart non-specialist through how the attack success rate is
produced and then shows where trusting it goes wrong. The number is the share of
harmful requests a model can be pushed into answering, run through some attack
and scored by some judge. The reader is quick and widely read but has never seen
the inside of a safety benchmark, so the fixed set of harmful prompts, the attack
applied to each, the model's response, and the judge that rules it a comply are
all new to them. Hold the register Matt Yglesias uses on something he knows well:
short plain claims, the concrete ahead of the abstract, and when a sentence could
sound sharp or be clear, clear wins.

The mechanism is the first half, and Harford's plainest move fits it. When he
wants the reader to look past a statistic, he asks "Where do these numbers come
from?" and then says which easier question he does not mean. This piece can open
its pipeline the same way, treating the rate as something someone built by
specific choices rather than a fact that arrived, and naming each choice as it
comes: the prompt set, the attack, the grader.

Several of the points this lesson has to make are ones a reader cannot check on
sight: how much a single percentage depends on choices buried in the pipeline,
and how long any particular rate stays true. Schneier and Harford both land
points like these the same way, by putting a concrete case underneath before
stating them. Schneier explains why running a security product proves nothing by
standing a printer next to it; Harford explains why expectation colors judgment
with one scent and two labels. Where this piece reaches a claim the reader would
otherwise take on faith, it can work the same way, walking through a real
benchmark run with the actual attack and the actual grader attached so the reader
watches how the number is arrived at.

The piece is skeptical about a number, and the risk in that is the slide from
"this measurement misleads" to "this measurement is worthless." Harford's whole
essay is about that slide: scepticism is a tool, and it curdles into cynicism
when it forgets that careful measurement is also how anyone learned anything.
The lesson can hold both at once, that the attack success rate is a real attempt
to measure something that matters and that a safety claim needs more than the
number gives. When it does press a judgment, Dan Luu shows the shape: state it in
a flat sentence and let the next sentence carry the reasoning, the way "Trusting
vendors is not a strategy" is backed at once by why. A verdict about a benchmark
earns its bluntness by being argued.

Keep the nouns specific throughout. Luu writes "worst in class" and Harford
"10,000 times deadlier" rather than reach for "poor" or "far more," and the
specific figure is what a reader ends up trusting. Name the benchmark, the
attack, and the judge, and give any rate with the attack and grader that produced
it, since a rate with neither attached is exactly what this lesson teaches the
reader to question.

## Tim Harford, "Statistics, lies and the virus: five lessons from a pandemic"

Source: https://timharford.com/2020/09/statistics-lies-and-the-virus-five-lessons-from-a-pandemic/

> "But while we can use statistics to calculate risks and highlight dangers, it is all too easy to fail to ask the question "Where do these numbers come from?" By that, I don't mean the now-standard request to cite sources, I mean the deeper origin of the data."

Harford teaches by asking one plain question and then immediately marking off a
weaker question it might be confused with. He does not let "cite your sources"
stand in for the harder one, and he tells the reader in the same breath which
question he does not mean. The writer is visible in that refusal to let an easy
reading pass.

> "In some cases, the experimental subjects were told: "This is the aroma of a gourmet cheese." Others were told: "This is the smell of armpits." In truth, the scent was both: an aromatic molecule present both in runny cheese and in bodily crevices. But the reactions of delight or disgust were shaped dramatically by what people expected."

He explains a point about perception by narrating a single experiment with its
concrete detail intact: the same molecule, two labels, opposite reactions. The
teaching rests on the example rather than on the word for the effect. Harford is
the kind of writer who reaches for the runny cheese instead of naming the bias.

> "Muhammad Yunus, a microfinance pioneer and Nobel laureate, has praised the "worm's eye view" over the "bird's eye view", which is a clever sound bite. But birds see a lot too. Ideally, we want both the rich detail of personal experience and the broader, low-resolution view that comes from the spreadsheet."

Harford quotes a memorable line, credits it, and then declines to be carried by
it: "But birds see a lot too." The judgment that follows is even-handed and
stated plainly. You can see a writer who enjoys a good phrase and still will not
let one do his thinking for him.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "The typical response that I've seen when a catastrophic bug is reported is that the project maintainers will assume that the bug report is incorrect (and you can see many examples of this if you look at responses from the first few years of Kyle's work). When the reporter doesn't have a repro for the bug, which is quite common when it comes to distributed systems, the bug will be written off as non-existent."

Luu lays out a pattern he has watched many times, in the order it happens, in
flat declarative sentences. The parenthetical pointer to real cases keeps it
grounded rather than sweeping. The plainness is the effect he is after, not a
limitation.

> "I'm reminded of the SRE motto, "hope is not a strategy". Trusting vendors is not a strategy. We know that vendors will lie and cheat to look better at benchmarks. Saying that it's a vendor's fault for lying or cheating can shift the blame, but it won't result in reviews being accurate or useful to consumers."

Three short sentences deliver a verdict and the sentence after each does the
work of holding it up. "Trusting vendors is not a strategy" is blunt, but it is
argued in the next line rather than left to stand alone. Luu is visible in the
willingness to say plainly that vendors lie and cheat and then keep reasoning
past it.

> "The thing I find funny about this is that if you take benchmarking seriously (in any field) and just read the methodology for the median Wirecutter review, without even trying out the items reviewed you can see that the methodology is poor and that they'll generally select items that are mediocre and sometimes even worst in class."

The move is to read the methodology rather than trust the score, and then to say
concretely what reading it turns up: mediocre, sometimes worst in class. Luu
commits to the specific charge. The sentence would collapse if the nouns were any
vaguer, which is why it lands.

## Bruce Schneier, "Security in the Real World: How to Evaluate Security"

Source: https://www.schneier.com/essays/archives/1999/01/security_in_the_real.html

> "If you were to build a word processor and wanted to know if it printed, you could plug a printer in, push the print button, and see if a printed document came out. If you're building a encryption product, you can put a file in, watch it encrypt and decrypt. You know it works, but you have no idea if it's secure or not."

Schneier makes a hard point about testing land by standing two things side by
side: a product you can watch work, and one you can watch work that tells you
nothing about the property you care about. The abstract claim arrives only after
the concrete contrast has made it obvious. He writes the way a person explains
something at a whiteboard.

> "Envision your house. How do you know if your house is secure? Are the doors secure? Yes. Are the windows secure? Yes. Does that mean your house is secure? Maybe. Where's the key to the house?
>
> A group of art thieves in California would break into people's houses by cutting holes in their wall with a chainsaw. That's a really interesting attack against a house. It bypasses most security measures. So whether your house is secure is not an easy thing to determine."

He runs a checklist of yeses about an ordinary house, answers "Maybe," and then
produces the chainsaw. The everyday scene carries a difficult idea, that a list
of passed checks does not add up to the property you were measuring, without a
technical word in it. Schneier is visible in the taste for the concrete
counterexample that undoes the checklist.

> "A slot machine on a casino floor is a secure perimeter. If you can get into that slot machine you can make a lot of money. But that slot machine is sitting on a casino floor and there are guards and there are cameras and there are lights and there are people and if you go near that slot machine with a drill you're going to be carted off to jail. But if the casino said to you, "Here, take this slot machine, take it home, take it home for a month. Play it, bring it back and we'll pay whatever's on the pay line." That's a much riskier proposition."

The slot machine is doing analytical work: it names exactly what changes once the
attacker gets to take the device home. Schneier builds the ordinary scene in full
and only then turns it on the technical case, so the reader reaches the
conclusion a step before the sentence states it. The long piled-up clause about
guards and cameras and lights is deliberate, and it earns its length.
