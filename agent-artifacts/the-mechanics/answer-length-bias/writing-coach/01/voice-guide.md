# Voice guide: the-mechanics/answer-length-bias

## How this piece should sound

This lesson takes something the reader has felt — ask a chatbot a question with a one-word answer and it comes back with a restated question, a preamble, three bullet points, and a caveat — and traces it to a measured place in how the model was trained. The reader is smart and reads widely, and has no time in a codebase. They keep meeting claims about AI they cannot check. Write so that by the end they can check this one: they can say why answers run long, and can tell a measured training artifact apart from a story about the model's personality.

Start from the behavior and distrust it until it is measured. Dan Luu opens "Computer latency" by admitting the feeling that his computers seem slower, then saying he does not trust that kind of feeling, and that he carried a camera around to measure it instead. The reader arrives with the same kind of impression about verbose answers. The lesson's work is to replace the impression with the length-reward relationship the reward model actually shows, not to restate the impression in steadier words.

Name the real part instead of the ready-made story. The reader may have heard that a model is "chatty" or "thorough by nature." Luu, on latency, grants that everyone knows complexity is bad and that there is always a conference talk saying so, then turns to what the complexity actually buys. Simon Willison, on the word "agents," says that if you tell him you are building agents you have told him almost nothing. Say what the reward model is and what optimizing a policy against it does to length, and set that beside the personality account the reader walked in with.

Carry the mechanism down to numbers the reader can hold. Willison works out in public what it would cost to caption 68,000 photos, lands on $1.68, and says he ran it three times because it seemed too low. Brian Potter, choosing between cost indexes, drops from the abstraction to ten hours of labor, a hundred pounds of steel, and a ton of cement. Give the measured length-reward correlation and the share of the RLHF win rate that length alone accounts for, and where a figure needs scale, put it next to one the reader already holds, the way Willison sets DeepSeek's training cost against Llama's as eleven times more.

Where a number might be catching something next to what it names, say so and leave it open. Potter, on rising construction costs, stops to note that a modern building may cost more per square foot because it is built to higher standards, which a cost index alone will not separate. This lesson has the same open question: whether raters rewarded length itself or the thoroughness that usually rides along with it, and the reward-model correlation does not by itself decide it. Mark what is settled engineering and what is open in this lesson's own terms, and resist closing the open part to make the lesson tidier.

Where the measurement is stark, a plain statement of it does more than an adjective. Luu closes by laying out in bare multiples that a machine thousands of times faster can barely match a forty-year-old one, and the numbers make the point with no grand word on top. If length turns out to account for a large part of what looked like quality, state that plainly and let the figure land; the strong word comes only after the measurement has earned it. And keep the explanation plain without thinning what it explains: Julia Evans says her friendlier tool output is not "dumbed down," it is the same information shown clearly, and that naming a hidden part of a system can dissolve years of confusion. Define the reward model, preference labeling, and the length correlation in plain words as each first appears, and trust the reader to follow the exact terms once they are named.

## Dan Luu, "Computer latency: 1977-2017"

Source: https://danluu.com/input-lag/

> "I've had this nagging feeling that the computers I use today feel slower than the computers I used as a kid. As a rule, I don't trust this kind of feeling because human perception has been shown to be unreliable in empirical studies, so I carried around a high-speed camera and measured the response latency of devices I've run into in the past few months."

Checked: https://danluu.com/input-lag/, retrieved 2026-09-22
Luu states the subjective impression in one plain sentence, then says he distrusts it and what he did instead, in the same breath. The measurement is the reason the piece exists, and he puts it ahead of any result. A specific person is visible: someone who carried a high-speed camera around for months rather than argue from memory.

> "Of course, we all know that complexity is bad. If you've been to a non-academic non-enterprise tech conference in the past decade, there's a good chance that there was at least one talk on how complexity is the root of all evil and we should aspire to reduce complexity. Unfortunately, it's a lot harder to remove complexity than to give a talk saying that we should remove complexity. A lot of the complexity buys us something, either directly or indirectly."

Checked: https://danluu.com/input-lag/, retrieved 2026-09-22
He grants the easy version — everyone agrees complexity is bad, there is always a talk about it — and then turns to what the complexity is actually doing. The move is to refuse the ready-made explanation without pretending it has no pull. The dry, slightly weary "Unfortunately" is his.

> "It's a bit absurd that a modern gaming machine running at 4,000x the speed of an apple 2, with a CPU that has 500,000x as many transistors (with a GPU that has 2,000,000x as many transistors) can maybe manage the same latency as an apple 2 in very carefully coded applications if we have a monitor with nearly 3x the refresh rate."

Checked: https://danluu.com/input-lag/, retrieved 2026-09-22
The judgment is carried entirely by multiples: thousands of times the speed, hundreds of thousands of times the transistors, to match a decades-old machine. He writes "a bit absurd" and then lets the figures be absurd on their own. Nothing is inflated, because the numbers are already extreme.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/

> "That's a total cost of $1.68 to process 68,000 images. That's so absurdly cheap I had to run the numbers three times to confirm I got it right."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-09-22
Willison has just done the arithmetic in front of the reader, reports the small total, and admits he re-ran it because it seemed too low. The self-check is the tell of someone who trusts the figure over the impression. It also keeps him from overclaiming: he shows the number instead of calling the result cheap and leaving it there.

> "If you tell me that you are building "agents", you've conveyed almost no information to me at all. Without reading your mind I have no way of telling which of the dozens of possible definitions you are talking about."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-09-22
He takes a word the field uses constantly and says plainly that it carries almost no information, then says why. The register is flat and unimpressed, which is the point: a vague term gets named as vague. This is Willison writing as someone who wants the specific thing meant, not the label.

> "The really impressive thing about DeepSeek v3 is the training cost. The model was trained on 2,788,000 H800 GPU hours at an estimated cost of $5,576,000. Llama 3.1 405B trained 30,840,000 GPU hours—11x that used by DeepSeek v3, for a model that benchmarks slightly worse."

Checked: https://simonwillison.net/2024/Dec/31/llms-in-2024/, retrieved 2026-09-22
He gives the raw figures, the GPU hours and the dollar cost, and immediately sets them beside Llama's as eleven times more for a slightly worse model, so the number has a scale. The comparison is doing the explaining. He commits to the exact figures rather than reaching for "cheap" or "efficient."

## Brian Potter, "Construction Costs Rarely Fall"

Source: https://www.construction-physics.com/p/construction-costs-rarely-fall

> "All else being equal, I prefer output indexes to input indexes, because they should more closely track what we actually care about (the cost of finished buildings), and should be less subject to distortion. For instance, the invention of some great cost-saving construction method might not be reflected in an input index that simply tallies up the cost of 10 hours of labor, 100 pounds of steel, and 1 ton of cement (which is how many input indexes are constructed)."

Checked: https://www.construction-physics.com/p/construction-costs-rarely-fall, retrieved 2026-09-22
Potter explains why he trusts one kind of index over another, then drops from the abstraction straight to ten hours of labor, a hundred pounds of steel, a ton of cement. The concrete list is how he keeps a measurement argument from floating free. A careful person is visible: one who has worked out what each index can and cannot capture.

> "In particular, it can be difficult to adjust cost indexes for quality; a modern building might cost more per square foot, but be built to higher standards or otherwise have higher performance than an older building, which looking only at changes in costs won't capture."

Checked: https://www.construction-physics.com/p/construction-costs-rarely-fall, retrieved 2026-09-22
He stops to name a way the number could mislead: a higher cost per square foot might be higher quality, which the index alone will not separate. He does not resolve it, he flags it and goes on. This is the habit of someone who would rather leave a question open than close it too neatly.

> "If we looked only at improvements in hand-made nails, we might conclude that nails on the market hadn't gotten any cheaper, even though what actually happened was that an older process had simply been replaced by a newer, better process."

Checked: https://www.construction-physics.com/p/construction-costs-rarely-fall, retrieved 2026-09-22
He uses a small history — hand-made nails giving way to cut nails and then wire nails — to show how a metric that tracks only the old process would miss the real change. The example is specific enough that the reader can follow the reasoning rather than take it on faith. The plainness is characteristic: no drama, just the case.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "For example, take DNS. We've been using DNS since the 80s (for more than 35 years!). It's used in every website on the internet. And it's pretty stable – in a lot of ways, it works the exact same way it did 30 years ago. But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
Evans sets up a genuine puzzle in short, concrete sentences: a thing used everywhere, stable for decades, and still hard to learn. She starts from the felt difficulty, not from the technology, and builds the puzzle out of plain facts anyone can check. The energy — the capitalized YEARS, the aside about 35 years — is hers, and the lesson's register is calmer than that.

> "just teaching people what the hidden systems are makes a huge difference. For a long time I had no idea that my computer had many different DNS libraries that were used in different situations and I was confused about this for literally years."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
She points to a plain remedy: naming the hidden pieces of a system does much of the work of un-confusing it, and she offers her own years of confusion as the case. The writing is unfussy and exact about what was hidden — which DNS libraries, used when. A person is visible in the admission that she was confused for years.

> "And it's not "dumbed down" or anything! It's the exact same information, just formatted in a more structured way. ... And though there's definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

Checked: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/, retrieved 2026-09-22
Evans draws a line between showing all of the information and showing it clearly, and insists these are not opposed. She wants the full thing, only legible. The exclamation is her register; the ethic under it is clarity without leaving things out. (The ellipsis drops one sentence between the two kept ones and does not change what she is saying.)
