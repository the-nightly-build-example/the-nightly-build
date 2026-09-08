# Voice guide: the-evidence/alphazero (01)

## How this piece should sound

This is a lesson for a reader who is comfortable with ideas and short on time, meeting the AlphaZero paper for the first time. Keep the register plain and concrete, in the manner of Simon Willison or Melanie Mitchell explaining a result they understand well: one claim to a sentence, the concrete thing before the abstraction, and no grand word before the argument has earned it. When a term the paper cannot be read without has to enter, such as self-play, reinforcement learning, or an evaluation function, it can be defined in the sentence where it lands, the way Mitchell defines "out of distribution" as she uses it.

The lesson's work is to hold what the paper actually reported against how it gets cited. Mitchell's "Why does this matter?" passage sets out what the evidence would mean under the strong reading and under the strict one before she chooses, and this piece has the same choice to set up: what the result shows if the loose citation is right, and what it shows read strictly. Dan Luu states the received narrative in full, and marks off what he is not disputing, before he argues against it. Where the lesson describes how AlphaZero gets invoked in arguments today, it can put that citation in the citers' own terms first and give the strong reading its due, so the correction has something real to push against.

When the paper reports a match against an engine, such as Stockfish at chess or the shogi and Go programs it was tested against, the conditions decide how much the score shows: the hardware each side ran on, the time each was given per move, the version and settings of the opponent. Willison's o3 sentence puts the impressive benchmark result and the cost that qualifies it in the same breath, joined by "albeit." A match result and its fine print can arrive together here in the same way, rather than the score first and the conditions a paragraph later or not at all.

Keep the numbers honest the way Willison and Luu do. Give the figure the paper gives, give a range where the paper supports only a range, as Luu does with two start dates for the same revenue, and anchor any figure the reader cannot scale on their own, such as training compute, hours of self-play, or positions searched per move, to one they already hold. Where the number people cite differs from the number the paper reported, both can appear.

The judgment at the end is earned, plain, and clear of both sneering and mush. Luu's "True, but not much of a criticism" concedes the fact and still lands, without mocking the people who hold the common view. Willison keeps genuine value and real criticism in the same paragraph without letting either cancel the other. Mitchell closes on a verdict, that the capacity "still needs to be systematically demonstrated," which neither inflates the result nor waves it away. Where AlphaZero's result is genuinely impressive, the lesson can say so directly; where a common citation runs past what the paper showed, it can say how far, and stop there.

## Melanie Mitchell, "Can Large Language Models Reason?"

Source: https://aiguide.substack.com/p/can-large-language-models-reason

> "Why does this matter? If robust general-purpose reasoning abilities have emerged in LLMs, this bolsters the claim that such systems are an important step on the way to trustworthy general intelligence. On the other hand, if LLMs rely primarily on memorization and pattern-matching rather than true reasoning, then they will not be generalizable—we can't trust them to perform well on "out of distribution" tasks, those that are not sufficiently similar to tasks they've seen in the training data."

Mitchell lays out both readings of the same evidence and gives each its due before she has taken a side, so the reader can see what is at stake rather than be told it matters. She is a researcher stating plainly what would follow if the strong claim held and what would follow if it did not. The technical phrase "out of distribution" is defined in the same sentence it appears.

> "As a stark example of this, Horace He, an undergraduate researcher at Cornell, posted on Twitter that on a dataset of programming challenges, GPT-4 solved 10 out of 10 problems that had been published before 2021 (GPT-4's pre-training cutoff date) and zero out of 10 problems that had been published after 2021. GPT-4's success on the pre-2021 challenges thus seems to be due to memorizing problems seen in its training data rather than reasoning about the problems from scratch."

Two numbers carry this, ten out of ten against zero out of ten, split by a single date. Mitchell reports the impressive-sounding score and the detail that reframes it in one move, and she names the person and where he posted it instead of writing that researchers found something. The reader is left able to follow the inference and check it.

> "One might argue that humans also rely on memorization and pattern-matching when performing reasoning tasks. Many psychological studies have shown that people are better at reasoning about familiar than unfamiliar situations; one group of AI researchers argued that the same patterns of "content effects" affect both humans and LLMs. However, it is also known that humans are (at least in some cases) capable of abstract, content-independent reasoning, if given the time and incentive to do so, and moreover we are able to adapt our understanding of what we have learned to wholly new situations. Whether LLMs have such general abstract-reasoning capacities, elicited through prompting tricks, scratchpads, or other external enhancements, still needs to be systematically demonstrated."

Mitchell states the strongest version of the opposing view, that people lean on memory too, and grants the studies behind it, before she says where it stops short. The closing sentence is a verdict that neither dismisses the models nor overstates them: the capacity has not yet been shown. She commits to that judgment in plain words instead of softening it.

## Simon Willison, "Things we learned about LLMs in 2024"

Source: https://simonwillison.net/2024/Dec/31/llms-in-2024/

> "The really impressive thing about DeepSeek v3 is the training cost. The model was trained on 2,788,000 H800 GPU hours at an estimated cost of $5,576,000. Llama 3.1 405B trained 30,840,000 GPU hours—11x that used by DeepSeek v3, for a model that benchmarks slightly worse."

Willison gives the exact hours and dollars rather than calling the cost low, then sets one figure against another so the reader can size it: eleven times the compute for a slightly worse result. The comparison is what makes the number mean anything. He is a practitioner who reaches for the real numbers first.

> "The sequel to o1, o3 (they skipped "o2" for European trademark reasons) was announced on 20th December with an impressive result against the ARC-AGI benchmark, albeit one that likely involved more than $1,000,000 of compute time expense!"

The impressive benchmark result and the cost that qualifies it sit in one sentence, joined by "albeit," so the reader meets the achievement and its price at once. Willison withholds neither the praise nor the caveat. The parenthetical on the naming shows a writer at ease being himself on the page without breaking the report.

> "I think telling people that this whole field is environmentally catastrophic plagiarism machines that constantly make things up is doing those people a disservice, no matter how much truth that represents. There is genuine value to be had here, but getting to that value is unintuitive and needs guidance."

Willison concedes the force of the criticism in its own harsh words, then says plainly that value remains and that reaching it is hard. He holds the two together without letting either one cancel the other. The judgment is his own, and he signs it with "I think" rather than handing it to unnamed others.

## Dan Luu, "Steve Ballmer was an underrated CEO"

Source: https://danluu.com/ballmer/

> "There's a common narrative that Microsoft was moribund under Steve Ballmer and then later saved by the miraculous leadership of Satya Nadella. This is the dominant narrative in every online discussion about the topic I've seen and it's a commonly expressed belief "in real life" as well. While I don't have anything negative to say about Nadella's leadership in this post, this narrative underrates Ballmer's role in Microsoft's success."

Luu states the received story fully and fairly before he argues against it, so the reader knows exactly which claim is in dispute. The third sentence fences off what he is not saying, which keeps the correction from reading as an attack on Nadella. He names the gap he is about to work in, between the common belief and the record, in these first three sentences.

> "Ballmer's critics can't point to a poor total return because Microsoft's total return was very good under his tenure. Revenue increased from $14B or $22B to $83B, depending on whether you want to count from when Ballmer became President in July 1998 or when Ballmer became CEO in January 2000. The company was also quite profitable when Ballmer left, recording $27B in profit the previous four quarters, more than the revenue of the company he took over."

Luu gives two starting figures, not one, and says out loud why the number is ambiguous, which start date you choose. He then anchors the profit to something the reader already has in hand: it was larger than the whole company's revenue when Ballmer began. He commits to the numbers and shows their limits at the same time.

> "Of course it would be better if Ballmer was prescient and all of his bets succeeded, making Microsoft worth something like $10T instead of the lowly $3T market cap it has today, but the criticism of Ballmer that says that he had some failures and some $1T successes is a criticism that he wasn't the greatest CEO of all time by a gigantic margin. True, but not much of a criticism."

Luu grants the criticism in full, then measures exactly how much it comes to. "True, but not much of a criticism" is a verdict that concedes the fact and still lands, with no sarcasm aimed at the critics. He has restated the opposing point accurately enough that granting it costs him nothing.
