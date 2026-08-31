# Voice guide: the-instruments/toxicity-score

## How this piece should sound

This lesson teaches how a toxicity score is produced and where it fails, for a
reader who is fluent and widely read but has never trained a classifier. Hold
the register plain and level, the way Narayanan and Kapoor hold theirs while
taking a benchmark apart: state what is known, mark what is not, and keep the
volume the same when the subject turns charged. The number rests on a chain the
reader has not seen. Human labelers judge comments. A classifier learns from
those labels. It outputs a probability. A threshold turns that probability into
"toxic." An average over many prompts turns many such calls into one score used
to rank models. When the piece walks that chain, it can do what Evans does with
a DNS request and name the hidden parts one at a time, so the score arrives as a
procedure rather than a fact.

When the lesson reaches how the number misleads, Luu's account of a latency
target tuned until it turned on its own goal shows a way to explain that without
assigning motive. The people optimizing improved the number they watched and did
not see what else moved. A toxicity score tuned into a model, or used to rank
models, can be described the same way: the classifier scores what it was trained
to score, and a system that chases a lower score chases the classifier, wherever
the classifier is wrong. Report the mechanism in the classifier's own terms and
let the mechanism carry the cost.

The threshold, and the labelers' judgments the classifier learned, are the
subjective choices sitting inside a number that looks objective. Narayanan and
Kapoor's question about contamination, how similar is too similar and who
decides, is the kind of question this piece can put to the threshold and to the
label: at what probability does a comment become toxic, and whose sense of
"toxic" did the labels encode. The word is narrower here than in ordinary use,
and the reader cannot weigh the score without the definition the classifier
actually runs on, so that definition belongs where the score first appears.

The hardest place in the piece is where it reports that text naming an identity,
or written in African-American English, scores more toxic. Give it as the cited
evidence gives it, with the figures the sources support, and stop where the
evidence stops. Luu's habit of committing to the named drug and the exact dollar
figure instead of a general lesson about proxies is the model: report the
finding and its cost, and skip the adjective for how bad it is. The judgment
belongs in the takeaway bookend. The body shows the finding and the chain that
produced it.

The piece can hold two true things at once, the way Narayanan and Kapoor hold
that a tool is neither useless nor trustworthy on its own. A toxicity score
measures something real about what a model emits, and it carries its labelers'
biases into every ranking built on it. Keep the criticism to what the evidence
supports, and let the number keep whatever it has actually earned.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "And chess is really simple compared to a lot of real world problems. 64
> squares. 32 pieces. Pretty much any analog problem you can think of contains
> more state than chess, and so do a lot of discrete problems. Chess is also
> relatively simple because you can directly measure whether or not you
> succeeded (won). Many real-world problems have the additional problem of not
> being able to measure your goal directly."

Luu sets the claim down flat and then narrows it twice: chess is simple, but
even in chess you can measure the goal directly, and most problems you cannot.
The two-word sentences stop as soon as they have said their fact, so the longer
sentences around them carry the point. He is visible in the instinct to count
the thing, 64 squares and 32 pieces, rather than characterize it.

> "If you try a series of optimizations while doing nothing but looking at three
> numbers, you'll choose optimizations that improve those three numbers, even if
> they make the rest of the distribution much worse. In this case, latency
> rapidly degrades above the 99.99%-ile because the people optimizing literally
> had no idea how much worse they were making the 99.991%-ile when making
> changes."

This explains why a metric gets gamed without blaming the people who game it.
They watched three numbers, improved them, and "literally had no idea" what they
were doing to everything else. The judgment stays on what the optimizers could
see, which is why the failure reads as built into the setup, and Luu's care to
keep it there is where he shows.

> "Given that narrative, it certainly sounds reasonable to try to develop new
> drugs that improve cholesterol levels, but when Pfizer spent $800 million
> doing exactly that, developing torcetrapib, they found that they created a
> drug which substantially increased heart attack risk despite improving
> cholesterol levels."

One sentence holds the whole case: a plausible plan, a named company, a dollar
figure, a drug, and a result that ran the wrong way. The figures do the work,
and the sentence commits to what happened without calling it surprising. Luu
reaches for the specific drug and the specific number where a general remark
about proxies would have been easier.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "just teaching people what the hidden systems are makes a huge difference. For
> a long time I had no idea that my computer had many different DNS libraries
> that were used in different situations and I was confused about this for
> literally years. This is a big part of my approach."

Evans names the fix in plain words: tell people what the hidden parts are. She
grounds it in her own confusion, that she did not know her computer held several
DNS libraries and stayed stuck on it for years, so the advice rests on a case
rather than a principle. She is visible in treating her past ignorance as
ordinary and worth reporting.

> "And it's not "dumbed down" or anything! It's the exact same information, just
> formatted in a more structured way. My biggest frustration with alternative
> DNS tools that they often remove information in the name of clarity. And though
> there's definitely a place for those tools, I want to see all the information!
> I just want it to be presented clearly."

Evans holds that making something clear and stripping information out of it are
different things: the friendlier version removes nothing and only lays the same
fields out. The passage carries her conviction that a reader can be shown all of
it and only needs it arranged well. The register here is loud, and the
exclamation points are hers rather than the genre's, but the value under them is
that clarity is arrangement.

## Arvind Narayanan and Sayash Kapoor, "GPT-4 and professional benchmarks: the wrong answer to the wrong question"

Source: https://www.aisnakeoil.com/p/gpt-4-and-professional-benchmarks

> "We don't know the answer, but we hope to inject some reality into the
> conversation. OpenAI may have violated the cardinal rule of machine learning:
> don't test on your training data. Setting that aside, there's a bigger
> problem. The manner in which language models solve problems is different from
> how people do it, so these results tell us very little about how a bot will do
> when confronted with the real-life problems that professionals face. It's not
> like a lawyer's job is to answer bar exam questions all day."

The pair say what they do not know before what they do, then lay out two
separate problems in order and never raise their voice. The last sentence brings
the abstraction down to something a reader can check: whatever a bar exam
measures, it is not the job. They commit to one plain claim, don't test on your
training data, and let it stand.

> "If OpenAI were to use a distance-based method, how similar is too similar?
> There is no objective answer to this question. So even something as seemingly
> straightforward as performance on a multiple-choice standardized test is
> fraught with subjective decisions."

This surfaces a choice buried inside a number that looks objective: deciding how
similar two questions must be before one counts as contamination has no right
answer, so the score inherits a judgment call. The two short questions do the
exposing and the longer sentence states the consequence. Narayanan and Kapoor
are visible in going straight to the step where the subjectivity enters instead
of arguing with the score.

> "To be clear, we're not saying that Copilot is useless, just that metrics are
> meaningless without a qualitative understanding of how professionals use AI."

The verdict is bounded on both sides: the tool is not useless, and the number
does not mean much on its own. Saying plainly what they are not claiming keeps
the criticism precise and hard to wave off as hype. The writers hold to the
narrow point the evidence supports.
