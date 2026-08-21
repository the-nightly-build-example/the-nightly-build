# Voice guide: the-instruments/big-bench-hard (01)

## How this piece should sound

This lesson takes apart a single number — a model's score on BIG-Bench Hard — for a reader who has met "X% on BBH" in a model card and has no way to check what it means. The register is plain and unhurried, a good teacher explaining something they understand well. The reader is smart and reads widely, so nothing is talked down to, but they hold none of the machinery: what BIG-bench was, how the harder subset was picked, what an "average human rater" score is, or what chain-of-thought prompting does to the figure. Each of those gets built before it is used.

The core move is Dan Luu's in the tail-latency passage: state the procedure that produces the number before judging it, so that when the misleading version arrives it is already explained. BBH's headline rests on a construction with several steps — a benchmark assembled from many contributors' tasks, a subset kept because the strongest models of the day fell short of a human baseline, a prompting method that moves the score. If the material walks those steps in order, cause before effect, the way Luu walks a stalled system into a 99th-percentile that reads as fast, the reader can check each step against the one before it.

The "beats the average human rater" bar is where the barbecue case earns its place. Bergstrom and West show a ranking that looks like a comparison of cities but is really a comparison of raters, and they show it by naming exactly who did the rating and what those people never rated. The human baseline behind BBH invites the same plain accounting: who the raters were, how many, how their scores were collected, and therefore what "the model beat them" does and does not compare. Where that accounting is thin, or a figure is contested across the two papers, the piece can say so at the point the number appears rather than smoothing it over.

When the score misled, there is Willison's way of reporting a surprising benchmark: name what was measured, hand over the figures, then follow one concrete cause through to its effect. Whether chain-of-thought was used, and whether the tasks had already reached the training data, are the kinds of conditions that move a BBH percentage without appearing next to it. The lesson has room to show one documented case fully instead of listing every worry — the single biggest issue, chosen and worked through, as the barbecue piece does.

Short, single-purpose sentences suit this, with a figure carrying the weight instead of an adjective: the count of tasks, the size of the chain-of-thought gain, the distance between a saturated score and what it once told apart. Luu commits to the strong version of a claim rather than hedging it, and Willison hedges exactly as far as the evidence forces and no further; the piece can do both, taking the firm line where the sourcing supports it and stating plainly what is unknown where it does not. A flat aside in the writer's own voice is welcome where the numbers just before it have earned it, and empty where they have not. Chain-of-thought itself, and why prompting changes scores, are taught in other lessons; a link keeps this one on the number and how it was made.

## Dan Luu, "Goodhearting IQ, cholesterol, and tail latency"

Source: https://danluu.com/percentile-latency/

> "Consider a contrived case where you measure for 20 seconds. For the first 10 seconds, each response takes 1ms. For the 2nd 10 seconds, the system is stalled, so the last request takes 10 seconds, resulting in 10,000 measurements of 1ms and 1 measurement of 10s. With these measurements, the 99%-ile is 1ms, as is the 99.9%-ile, for the matter. Everything looks great!"

Luu builds the whole point out of one worked example with real numbers, and the reader can check every step: ten thousand fast measurements, one slow one, and a 99th-percentile that reports 1ms while the system sat stalled for ten seconds. He lays out the measuring procedure before he passes any judgment on it, so the misleading number arrives already explained. "Everything looks great!" is the writer's own dry aside, and it lands only because the figures right before it earned the irony.

> "If you specify goals in terms of 99%-ile, 99.9%-ile, and 99.99%-ile, you'll optimize your system to barely hit those goals. Those optimizations will often push other latencies around, resulting in a funny looking distribution that has kinks at those points, with latency that's often nearly as bad as possible everywhere else."

This is Luu explaining a mechanism in order, cause before effect, in sentences a non-engineer can follow. He names precisely what the tuning does — barely clears the three targets — and precisely what it costs — everything between them gets worse — so the claim is concrete rather than asserted. "Nearly as bad as possible everywhere else" is a person committing to the strong form of his point instead of softening it.

> "Some interventions that affected cholesterol levels also affected real health outcomes, prompting people to develop drugs that affect cholesterol. But it turns out that improving cholesterol isn't an inherent good, and like many intermediate targets, it's possible to improve without affecting the end goal."

Just above this, Luu has given the specific case: Pfizer's $800 million torcetrapib, a drug that improved cholesterol yet raised heart-attack risk. Here he draws the general lesson, and keeps the general sentence plain and short so nothing in it floats free of the case beneath it. It is the same writer in the same plain register across latency, medicine, and IQ, which is what lets a reader who knows none of those fields follow all three.

## Carl Bergstrom and Jevin West, "America's Best Barbecue?"

Source: https://callingbullshit.org/case_studies/case_study_barbecue.html

> "What went wrong? So many things. It's hard to even know where to start. But let's focus on the single biggest issue: the data collected are not appropriate to answer the question at hand."

They could have listed every flaw in the ranking; instead they grant that there are many and then pick the one that matters, which stops the piece from becoming a catalog. The short sentences read like a person thinking aloud before settling down to the work. The colon does real work: it promises the single issue and then delivers it in the same breath.

> "So what these data tell us is that people in Seattle rate Seattle barbecue higher than people in Fort Worth rate Fort Worth barbecue places. We don't know how people in Seattle would rate Fort Worth barbecue, or how people in Fort Worth would rate Seattle barbecue."

The entire flaw sits in two plain sentences: the number compares raters, not barbecue, and the comparison everyone assumes it makes was never in the data at all. They hold to the same two cities the whole way rather than reaching for synonyms, so the reader tracks the argument without effort. The writing exposes what a score rests on by naming exactly who did the rating and what those raters never rated.

> "In the end, Fort Worth has better barbecue but Seattle rates higher because the Seattle rater is more generous."

After building the mechanism, they collapse it into one sentence a reader can carry away and repeat, and it holds because the sentences before it did the work. The concreteness keeps it from flattening into a generic maxim about averages: a named place that is better yet scores lower, a named place that only looks like the winner.

## Simon Willison, "Open weight LLMs exhibit inconsistent performance across providers"

Source: https://simonwillison.net/2025/Aug/15/inconsistent-performance/

This piece is about benchmark scores, the article's own territory, so the passages below are here for how Willison writes, not for what he found.

> "Artificial Analysis published a new benchmark the other day, this time focusing on how an individual model—OpenAI's gpt-oss-120b—performs across different hosted providers. The results showed some surprising differences."

Willison opens by saying plainly what was measured and that it surprised him, then hands over the numbers. There is no throat-clearing and no announcement of importance ahead of the evidence. The plainness is the voice: a person telling you what he found in the order he found it.

> "There's a lot that can go wrong. Tool calling is particularly vulnerable to these differences—models have been trained on specific tool-calling conventions, and if a provider doesn't get these exactly right the results can be unpredictable but difficult to diagnose."

He names one concrete way the same model can post different scores rather than waving at "many factors," and he traces the cause through to its effect. The sentence keeps the exact terms a practitioner would use, "tool-calling conventions" and the rest, and still stays followable for a reader who has never called a tool. He does that by spelling out the consequence in plain words right after the technical clause, so the jargon never has to stand alone.

> "It looks like with hosted models even knowing the quantization they are using isn't necessarily enough information to be able to predict that model's performance."

Willison states plainly the limit of what the number can tell you, and hedges only as far as the evidence forces, with "isn't necessarily enough." He neither rounds the uncertainty up into a slogan nor down into false confidence. Being clear about what he cannot know from the data is part of why the reporting reads as trustworthy.
