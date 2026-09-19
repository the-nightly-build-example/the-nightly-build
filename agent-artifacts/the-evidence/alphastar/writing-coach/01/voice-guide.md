## How this piece should sound

This is a lesson for The Evidence, written for one reader: smart, widely read, and holding the headline that an AI reached Grandmaster at StarCraft II while holding nothing about how reinforcement learning works. The piece reads the paper behind that headline and shows what AlphaStar actually did and under what conditions. Write it the way Ben Brubaker writes complexity theory for people who do not have it: plain claims, terms defined in the sentence that first needs them, and the prior assumption laid out before the new result so the reader has something to compare it to. When league play, actions per minute, or imperfect information first appears, it can be defined in plain words right there, the way Brubaker defines "space" in the breath he introduces it.

Much of this lesson turns on the distance between what the paper showed and how the result is remembered. Dan Luu's opening on Ballmer is the plain form of that move: he states the common narrative in full, says what he is not disputing, and gives his own claim in one sentence, with no throat-clearing in front of it. The "AI crushed the pros" memory can be named as plainly, with the paper's actual result set beside it, and the contrast does not need the "not X, it's Y" construction to mark it. Brubaker does the same on scale when he separates what a result "may sound like" from the finer level at which it actually holds. Where AlphaStar's Grandmaster-on-the-ladder claim gets stretched into beating the world's best in a controlled series, the difference can be stated in ordinary words the same way.

The numbers carry this lesson, so handle them the way Luu handles Microsoft's revenue. He gives the figure together with the two possible starting points behind it instead of picking one and hiding the choice, and anchors a number the reader cannot scale to one they can hold. The actions-per-minute limits, the camera-interface constraints that changed between the January 2019 showcase and the Nature version, the count of human replays, and the ladder tier all invite that treatment: the figure and its honest range, the baseline named, and whatever is unknown said plainly.

A verdict on the "superhuman" framing is welcome once the reasoning that earns it is on the page. Luu reaches his judgment on Ballmer only after the venture-capital comparison is laid out where the reader can check it. The actions-per-minute and camera debate and the human-replay bootstrap are the reasoning this lesson has to show before it weighs that framing.

The machinery is the subject: the supervised imitation from human replays, the league of main agents and exploiters, and the interface the agent was given. Julia Evans treats a beginner's confusion as a fact about the system rather than about the beginner, and names the hidden parts one at a time. Naming each piece of AlphaStar's pipeline plainly, in the order the reader needs it, is most of the teaching here. Clarity does not mean leaving things out: Evans wants all the information and only wants it laid out well, and this lesson can keep the real conditions of the result while putting them in short, concrete sentences a first reader can follow.

## Ben Brubaker, "For Algorithms, a Little Memory Outweighs a Lot of Time"

Source: https://www.quantamagazine.org/for-algorithms-a-little-memory-outweighs-a-lot-of-time-20250521/

> "Time and memory (also called space) are the two most fundamental resources in computation: Every algorithm takes some time to run, and requires some space to store data while it’s running. Until now, the only known algorithms for accomplishing certain tasks required an amount of space roughly proportional to their runtime, and researchers had long assumed there’s no way to do better."

Brubaker defines "space" in the same clause that introduces it, and states the two resources in one plain sentence before making any claim about them. He is visible in the patience of giving the reader the old assumption first, so the new result has something to be compared with when it arrives.

> "This belief stems from the fact that algorithms can use the same small chunk of memory over and over, while time isn’t as forgiving — once it passes, you can’t get it back."

An abstract claim, that space is more powerful than time, is grounded in something physical the reader already knows: a chunk of memory can be reused, a passed second cannot. The plainness is Brubaker's, and the reasoning is one clause long and uses no term he has not already set.

> "Phrased in qualitative terms, Williams’ second result may sound like the long-sought solution to the P versus PSPACE problem. The difference is a matter of scale. P and PSPACE are very broad complexity classes, while Williams’ results work at a finer level. He established a quantitative gap between the power of space and the power of time, and to prove that PSPACE is larger than P, researchers will have to make that gap much, much wider."

Brubaker says what the result may sound like, then names the exact scale at which it actually holds, so the reader can tell the qualitative headline from the quantitative claim. The distinction is carried by ordinary words like "finer level" and "much, much wider," not by hedging.

## Dan Luu, "Steve Ballmer was an underrated CEO"

Source: https://danluu.com/ballmer/

> "There's a common narrative that Microsoft was moribund under Steve Ballmer and then later saved by the miraculous leadership of Satya Nadella. This is the dominant narrative in every online discussion about the topic I've seen and it's a commonly expressed belief "in real life" as well. While I don't have anything negative to say about Nadella's leadership in this post, this narrative underrates Ballmer's role in Microsoft's success."

Luu states the common narrative in full, credits what he is not disputing, then gives his own claim in one sentence. He is visible in how flatly he sets up the disagreement, with nothing between the narrative and the counter-claim.

> "When people point to a long list of failures like Bing, Zune, Windows Phone, and HoloLens as evidence that Ballmer was some kind of buffoon who was holding Microsoft back, this demonstrates a lack of understanding of the tech industry. This is like pointing to a list of failed companies a VC has funded as evidence the VC doesn't know what they're doing. But that's silly in a hits based industry like venture capital."

Luu answers a criticism by showing how the industry actually works, using a venture-capital comparison the reader can check, and reaches the word "silly" only after that reasoning is on the page. The verdict is his, and the sentences around it are what earn it.

> "Revenue increased from $14B or $22B to $83B, depending on whether you want to count from when Ballmer became President in July 1998 or when Ballmer became CEO in January 2000. The company was also quite profitable when Ballmer left, recording $27B in profit the previous four quarters, more than the revenue of the company he took over."

Luu gives the revenue figure with both possible starting points rather than choosing one and hiding the choice, and anchors the profit number to something the reader can scale it against, the revenue of the company Ballmer inherited. The care with the baseline is where Luu is visible.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "just teaching people what the hidden systems are makes a huge difference. For a long time I had no idea that my computer had many different DNS libraries that were used in different situations and I was confused about this for literally years. This is a big part of my approach."

Evans says that a large part of learning DNS is simply being told which parts of the system are hidden, and grounds it in her own years of not knowing her computer held several DNS libraries. She is visible in treating a beginner's confusion as a fact about the system rather than about the beginner.

> "And it’s not “dumbed down” or anything! It’s the exact same information, just formatted in a more structured way. My biggest frustration with alternative DNS tools that they often remove information in the name of clarity. And though there’s definitely a place for those tools, I want to see all the information! I just want it to be presented clearly."

Evans insists that presenting information clearly is not the same as removing it, and says plainly that she wants all of it and only wants it laid out well. She is visible in the flat refusal to trade completeness for readability.

> "For example, take DNS. We’ve been using DNS since the 80s (for more than 35 years!). It’s used in every website on the internet. And it’s pretty stable – in a lot of ways, it works the exact same way it did 30 years ago."

Short, concrete sentences carry the scale, more than 35 years and every website, with no adjective doing the work the numbers do. Evans is visible in how plainly she states how ordinary and stable the technology is before saying it was still hard to learn.
