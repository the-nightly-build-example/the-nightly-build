# Voice guide: the-instruments/squad

## How this piece should sound

This lesson teaches one reader — smart, widely read, with no time in a codebase and new to SQuAD — how a single benchmark number is built and where it stopped meaning what people took it to mean. Hold the paper's register: plain, concrete, skeptical, with no hype and no cynicism. Matt Yglesias explaining something he understands well is the touchstone. When a sentence could either sound good or be understood, be understood.

Luu, Shalizi, and Rogers all do one thing this piece can use: they build a number in front of the reader before they say what it means. Luu's contrived twenty-second latency case lets the reader compute the misleading percentile for themselves; Shalizi shows the abstract factor on real car data and lists the traits it sums. EM and F1 can be shown that way. One real passage, one real question, a crowdworker's answer, and the token overlap counted out gives the reader the arithmetic of an F1 score, and the definitions fall out of the worked case. The reader has not been told what precision and recall are, so the example is what carries them.

The human-performance line is a measured number too, and how it was measured — a set of crowdworkers answering a subset, scored the same way the models are — is what lets the reader see it as one estimate. Shalizi's move, once a number is built, is to say plainly what it does and does not tell you. That register fits the moment this lesson reaches what a token-overlap F1 actually rewards: agreement with the reference span, counted in shared tokens. Say plainly what a shared-token count captures, and be as plain about what it leaves out, where the section gets there.

Where the score misled, keep the turn earned and quiet. Rogers states the common reading of a leaderboard in one sentence and answers it in three words, with no gotcha; the early-2018 "superhuman" coverage and the distractor-sentence result can meet the same way, once the score has been built and the reader can see what it counts. Luu's paused-game AI shows that a vivid analogy is allowed when it matches the real mechanism — a system scoring a span it did not comprehend — and the piece has one available. An analogy that only works as a general moral is the kind to leave out.

Vividness comes from SQuAD's own nouns: spans copied out of the passage, exact-match, token overlap, the one appended distractor sentence, the crowd references. Rogers gets her force from "one Google model outperform another Google model," which is specific and checkable. This story has real drama, and the superhuman headlines and the collapse under a single added sentence carry it on their own when they are reported plainly and the figures are given.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "Chess is also relatively simple because you can directly measure whether or not you succeeded (won). Many real-world problems have the additional problem of not being able to measure your goal directly."

Luu states the whole idea of the piece in two plain sentences, using chess as the case where the goal can be checked directly. The second sentence names the harder problem exactly, that you often cannot measure the goal itself, and does not dress it up. Putting the checkable detail in the parenthesis — "whether or not you succeeded (won)" — rather than gesturing at it is a habit of his throughout.

> "It's like the video game solving AI that presses pause before its character is about to get killed, because pausing the game prevents its health from decreasing. If you have very narrow optimization goals, and your measurements don't give you any visibility into anything else, everything but your optimization goals is going to get thrown out the window."

The paused-game analogy is concrete and checkable: a specific AI, a specific move, a specific reason it works. Luu then states the general rule in the next sentence without any abstraction creeping in, and "thrown out the window" is a plain phrase carrying the point a fancier one would only decorate. The analogy is his own, and it fits the mechanism instead of sitting on top of it.

> "Consider a contrived case where you measure for 20 seconds. For the first 10 seconds, each response takes 1ms. For the 2nd 10 seconds, the system is stalled, so the last request takes 10 seconds, resulting in 10,000 measurements of 1ms and 1 measurement of 10s. With these measurements, the 99%-ile is 1ms, as is the 99.9%-ile, for the matter. Everything looks great!"

Luu walks the reader through an invented but exact case, second by second, with every number named, and lets them work out the 99th percentile themselves. "Everything looks great!" lands because the arithmetic just before it earned the irony. This is his characteristic move: build the misleading number in front of the reader rather than assert that it misleads.

## Cosma Shalizi, "g, a Statistical Myth"

Source: http://bactra.org/weblog/523.html

> "Factor analysis is handy for summarizing data, but can't tell us where the correlations came from; it always says that there is a general factor whenever there are only positive correlations. The appearance of g is a trivial reflection of that correlation structure."

Shalizi says in one sentence what the technique can do and, in the same sentence, what it cannot. "Handy for summarizing data, but can't tell us where the correlations came from" is the exact distinction the rest of the piece turns on, and he states it before any of the machinery. Calling the result "a trivial reflection of that correlation structure" is his plain verdict, given early and without hedging.

> "The leading factor, the automotive equivalent of g, is positively correlated with everything (price, engine size, passengers, length, wheelbase, weight, width, horsepower, turning radius) except gas mileage. It basically says whether the car is bigger or smaller than average. The second factor, which I picked to be uncorrelated with the first, is most positively correlated with price and horsepower, and negatively with the number of passengers — the sports-car/mini-van axis."

Shalizi takes an abstract statistical object and shows it on real car data, naming the actual variables it correlates with. "It basically says whether the car is bigger or smaller than average" translates the number into something a reader can hold. The parenthetical roll-call of traits and the offhand "the sports-car/mini-van axis" are him thinking out loud on the page, which is why the passage reads as a person working rather than a result being announced.

> "Mathematically, however, the first factor is just a weighted sum of the traits, with big positive weights on most variables and a negative weight on gas mileage. That we can make verbal sense of it is, to use a technical term, pure gravy. Really it's all just about redescribing the data."

Having built the factor, Shalizi says plainly what it is: a weighted sum of the traits he already listed. "Pure gravy" and "redescribing the data" are his flat way of saying the story we hang on the number is optional, and the number itself only restates what was measured. He offers this as a fact he has just shown, not as an opinion he is asserting.

## Anna Rogers, "How the Transformers broke NLP leaderboards"

Source: https://hackingsemantics.xyz/2019/leaderboards/

> "Leaderboards stimulate competitions between engineering teams, helping them to develop better and better models to tackle human language.
>
> Or do they?"

Rogers gives the received view in one clean sentence and answers it with a two-word paragraph on its own line. The turn is skeptical and light, and it commits the post to showing what is wrong rather than only doubting. She sets up the common view plainly and undercuts it in three words, and the rest of the piece pays that off.

> "The chief problem with the huge models is simply this:
>
> 'More data & compute = SOTA' is NOT research news."

After several paragraphs of setup, Rogers states the problem as a single blunt line set off by itself. The all-caps NOT and the shorthand "More data & compute = SOTA" are hers, and they read as a person talking, not a paper hedging. She has earned the bluntness by doing the argument first.

> "NLP leaderboards are in real danger of turning into something where we give up on reproducibility and just watch one Google model outperform another Google model every couple of months."

The danger is made concrete with specific nouns, one Google model beating another Google model every couple of months, rather than a general worry about progress. It is wry without being cynical: she is describing a real outcome she wants to avoid, not sneering at the field. The plainness is what gives it force; nothing in the sentence is inflated.
