# Voice guide: what-could-go-wrong/capability-elicitation

## How this piece should sound

This is a lesson that puts one argument about AI safety evaluation at full strength and then measures it against what real systems have actually done, written for a reader who is quick but has never run an evaluation. The argument is a subtle one about what a capability score does and does not establish, so the reader will only be able to weigh it once the mechanism underneath it has been made concrete. Scott Alexander spends three unhurried sentences on an invented drug and a spread of studies before he draws anything from them. This lesson has the same license to build its mechanism slowly, with a worked case and real quantities, before it asks the reader to accept any conclusion from it.

The desk's discipline is to take a worrying case seriously without tipping into doom, and to watch confidence in both directions at once. Alexander's minimum-wage section models the second half. He sets the conservative pile of studies beside the liberal pile, finds each convincing on its face, and trusts neither alone. This lesson can hold the reassuring reading of a passed evaluation and the alarmed reading of an unmeasured capability at the same distance, and can decline to settle a question the evidence leaves open. When it does reach a verdict, Alexander's "at least some evidence that the liberals are right on this one" shows the size to reach for: a claim scaled to what the evidence in hand can carry, and named as that size.

Holden Karnofsky, writing about a genuinely alarming scenario, separates the dramatic version of his claim from the smaller version he actually needs and keeps only the smaller one, and he marks the speculative parts of his story as speculative. Both moves belong here. The elicitation argument can be stated the way its most careful defenders state it, and the lesson can then hold only what working systems have demonstrated, drawing the line between a demonstrated result and an inference about systems that do not exist yet in the sentence where it crosses that line. Karnofsky also puts the case against his own worry plainly, with the concrete history behind it, and where this lesson owes the reader the reasons a passed evaluation still carries weight, it can give them with the same evenness.

Dan Luu sets the register. He writes about numbers produced by people with a stake in them, a vendor's benchmark or a reviewer's loaned unit, and refuses to take such a number on trust. To Luu it is something independent testing has to earn back. He states the incentive without heat and follows it to whoever ends up misinformed. A capability score is also a number someone had a reason to produce, and the lesson can explain why the effort behind it matters in that same flat, exact way, without reaching for alarm or relief. Luu and Alexander both mark the moment a single case is widened into a general rule, and this lesson can show that same seam when it moves from one instance to a claim about evaluations at large. Where the evidence bounds the argument but does not close it, Alexander's willingness to say "I don't have a good positive answer" is the honest option, better than a verdict rounded up to sound finished.

## Scott Alexander, "Beware The Man Of One Study"

Source: https://slatestarcodex.com/2014/12/12/beware-the-man-of-one-study/

> Suppose a certain drug is weakly effective against a certain disease. After a few years, a bunch of different research groups have gotten their hands on it and done all sorts of different studies. In the best case scenario the average study will find the true result – that it's weakly effective.

He builds the point from an invented drug and an ordinary sequence of events, using only quantities a reader already holds. The explaining is unhurried, one step per sentence, and Alexander is visible in the willingness to spend three sentences setting a mechanism up before he draws anything from it.

> This is more of a needle curve than a bell curve, but the point still stands. We see it's centered around 0, which means there's some evidence that's the real signal among all this noise. The bell skews more to left than to the right, which means more studies have found negative effects of the minimum wage than positive effects of the minimum wage. But since the bell curve is asymmetrical, we intepret that as probably publication bias. So all in all, I think there's at least some evidence that the liberals are right on this one.

Alexander reads the plot out, states what each feature means, and only then commits to a verdict, and he keeps the verdict small ("at least some evidence"). The confidence is sized to what one plot can bear, and you can see him declining to round "some evidence" up into a settled answer.

> I don't have a good positive answer. I do have several good negative answers.
>
> Decrease your confidence about most things if you're not sure that you've investigated every piece of evidence.

He states the plain limit of his own advice before he offers it, and what he offers is a downward adjustment to confidence rather than a rule that settles the question. The honesty about lacking a positive answer comes from Alexander in the first person, not from a hedged passive.

## Holden Karnofsky, "AI Could Defeat All Of Us Combined"

Source: https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/

> But I want to be clear that I don't think the danger relies on the idea of "cognitive superpowers" or "superintelligence" - both of which refer to capabilities vastly beyond those of humans. I think we still have a problem even if we assume that AIs will basically have similar capabilities to humans, and not be fundamentally or drastically more intelligent or capable.

Karnofsky separates the strongest version of his claim from the version he actually needs and keeps only the weaker one. The prose stays flat while he does it, which is where he shows: he would rather defend a smaller claim than assert a dramatic one.

> I believe civilization is pretty robust - we've had huge changes and challenges over the last century-plus (full-scale world wars, many dramatic changes in how we communicate with each other, dramatic changes in lifestyles and values) without seeming to have come very close to a collapse.

Writing about a catastrophic scenario, he still states the case against alarm plainly and gives the concrete history behind it. The parenthetical does real work, listing the shocks a civilization absorbed, so the reassurance reads as evidence rather than a gesture. His even-handedness toward his own worry is what shows here.

> It's necessarily speculative, and should be taken in the spirit of giving examples of how this might work - for me, the high-level concern is that a huge, coordinating population of AIs with similar capabilities to humans would be a threat to human civilization, and that we shouldn't count on any particular way of stopping it such as shutting down servers.

He labels the detailed story as speculative and then names the smaller thing he is actually confident about, so an illustration and the claim it supports do not get read as one. The care is in keeping what he asserts apart from what he only imagines, inside a sentence that could easily have blurred them.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> The typical response that I've seen when a catastrophic bug is reported is that the project maintainers will assume that the bug report is incorrect (and you can see many examples of this if you look at responses from the first few years of Kyle's work). When the reporter doesn't have a repro for the bug, which is quite common when it comes to distributed systems, the bug will be written off as non-existent.

Luu describes how a real problem gets waved away when no one can reproduce it on command, and he grounds the description in years of reading bug reports rather than in a general claim. The voice is an engineer reporting a pattern he has watched repeat, exact about the conditions under which the dismissal happens.

> That's one particular example, but I find that it's generally true that, in areas where no one is publishing measurements/benchmarks of products, the products are generally sub-optimal, often in ways that are relatively straightforward to fix once measured.

He widens one case into a plain rule and marks the move as he makes it ("I find that it's generally true"), so the reader sees a single example being turned into a claim. The register is unshowy and precise, which is characteristic of Luu.

> I'm reminded of the SRE motto, "hope is not a strategy". Trusting vendors is not a strategy. We know that vendors will lie and cheat to look better at benchmarks. Saying that it's a vendor's fault for lying or cheating can shift the blame, but it won't result in reviews being accurate or useful to consumers.

Luu treats a number from an interested party as something to be earned back through independent testing, not accepted on trust, and he states the incentive plainly before following it to who ends up misinformed. He is visible in caring less about assigning blame for a gamed number than about what the reader is left knowing.
