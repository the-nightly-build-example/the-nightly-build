# Voice guide: the-instruments/clipscore (01)

## How this piece should sound

CLIPScore is produced by asking one model to grade another model's output. Before giving the construction — the two CLIP encoders, the cosine similarity, the rescaling into a 0-to-100-ish figure — name the actual decision the number gets used for: a paper ranking two text-to-image systems, a leaderboard entry, a training run selecting which sample to keep. Julia Evans opens the same way, with the real question someone is using a number to answer, before she shows the number itself. Attaching the score to a real decision early gives the construction that follows something concrete to be tested against.

When the lesson reaches what CLIPScore can support, state it as a comparison the reader can check: this score, set beside what a human rater said about the same image-caption pair, moved together this often. Evans does this with her own number — computing it once as a bare percentile and again as a range, then saying plainly which one she trusts and why. The reported correlation figures from Hessel et al. can do the same job here: give the figure next to what it covers.

The failure section is where a model-judging-model metric earns its place in this series, and the piece has room to give it real weight. When it reaches word-order and attribute binding, build one concrete pair early — a red cube on a blue sphere, its swap — so the failure can point back at something the reader already has, the way Evans' "be careful" turn names the exact scenario that breaks bootstrapping using the same flight-overbooking numbers built earlier in the post. Rachel Thomas's Wells Fargo sentence is worth the same attention for the reward-hacking half of the lesson: cause, mechanism, and outcome inside one sentence, closed on a specific count. Whatever the concrete misleading case turns out to be, give it that same shape: the pressure that produced the behavior, and the exact cost.

One naming habit is worth carrying over from Simon Willison: name what a thing is functioning as, at the moment the piece would otherwise reach for its official label. He names the Chatbot Arena leaderboard for what it functions as, a vibes-based evaluation, in the same sentence that gives a checkable fact about it. CLIPScore's official description is an automatic metric for image captioning; the piece can afford one sentence, once, that says what it functions as here — a model's opinion of another model's output, standing in for a person's opinion. After that sentence, use CLIPScore's own name and let the mechanism carry the point, the way Willison anchors DeepSeek's training-cost claim against Llama's own GPU-hour figure.

## Julia Evans, "Some easy statistics: Bootstrap confidence intervals"

Source: https://jvns.ca/blog/2015/07/04/bootstrap-confidence-intervals/

> "So, let's say I have some numbers like: 0, 1, 3, 2, 8, 2, 3, 4 describing the number of no-shows for flights from New York to Puerto Rico. And that I also have no idea what kind of distribution this number should have, but some Important Person is asking me how much it's okay to oversell the plane by."

Before any statistic appears, the reader already knows who wants the number and what they plan to do with it. The reader can measure every later step in the post against whether it actually answers the Important Person's question.

> "This is actually way more useful! It's telling me I can oversell by 0 - 2 people, and I don't have enough data to decide which one. I don't know if I'd take this graph to airline executives (though everyone loves graphs right?!?!), but it's for sure more useful than just a 0.35."

She computes the same quantity two ways — once as a single number, once as a range — and says directly which one she trusts, in terms of what each would let her tell a real person. The judgment sits on a comparison between two things she actually built.

> "If occasionally 100 people don't make the flight because they're all from the same group and that's important and not represented in your sample, bootstrapping can't save you."

The limitation is stated using the exact scenario the whole post was built around — the overbooked flight — with the same numbers, not as a general disclaimer about sampling. Naming the failure in the piece's own numbers is what makes it a real limit.

## Rachel Thomas, "The problem with metrics is a big problem for AI"

Source: https://www.fast.ai/posts/2019-09-24-metrics.html

> "Goodhart's Law states that “When a measure becomes a target, it ceases to be a good measure.” At their heart, what most current AI approaches do is to optimize metrics. The practice of optimizing metrics is not new nor unique to AI, yet AI can be particularly efficient (even too efficient!) at doing so."

She states the general law once, then narrows it in the next sentence to the one property that makes AI different: its efficiency at optimizing whatever it's given. The parenthetical adds a joke on top of that claim without weakening it.

> "The state-owned media outlet Russia Today was an extreme outlier in how much YouTube's algorithm had selected it to be recommended by a wide-variety of other YouTube channels. Such algorithmic selections, which begin autoplaying as soon as your current video is done, account for 70% of the time that users spend on YouTube. This chart strongly suggests that Russia Today has in some way gamed YouTube's algorithm."

The 70% figure turns "the algorithm was gamed" into something a reader can weigh, because it states how much of the platform's attention the mechanism actually controls. The verdict in the last sentence comes after the number that supports it.

> "After identifying cross-selling as a measure of long-term customer relationships, Wells Fargo went overboard emphasizing the cross-selling metric: intense pressure on employees combined with an unethical sales culture led to 3.5 million fraudulent deposit and credit card accounts being opened without customers' consent."

One sentence carries the whole chain: what the metric stood in for, the pressure it created, and what that pressure produced. It closes on a specific count, 3.5 million accounts, and the colon does one job — introducing the outcome the setup promised.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonw.substack.com/p/things-we-learned-about-llms-in-2024

> "If you browse the Chatbot Arena leaderboard today - still the most useful single place to get a vibes-based evaluation of models - you'll see that GPT-4-0314 has fallen to around 70th place."

He names the leaderboard by what it functions as — a vibes-based evaluation — and backs that label with a checkable fact about where a specific model landed. The naming and the evidence sit in the same sentence.

> "Training a GPT-4 beating model was a huge deal in 2023. In 2024 it's an achievement that isn't even particularly notable, though I personally still celebrate any time a new organization joins that list."

The claim is a change of degree, stated against a one-year-earlier baseline: what counted as a huge deal in 2023 is unremarkable in 2024. The aside that follows names one specific thing he still does — celebrating each new organization on the list.

> "The really impressive thing about DeepSeek v3 is the training cost. The model was trained on 2,788,000 H800 GPU hours at an estimated cost of $5,576,000. Llama 3.1 405B trained 30,840,000 GPU hours - 11x that used by DeepSeek v3, for a model that benchmarks slightly worse."

"Impressive" is backed by the exact hours and dollar figure in the very next sentence, then anchored against a named competitor's own number so the comparison is something the reader can verify.
