# Voice guide: what-could-go-wrong/gradient-hacking

## How this piece should sound

This lesson teaches gradient hacking to a reader who is sharp and widely read but has never trained a model. The subject is a claim about something no one has observed: that a model already deceptively aligned, and aware it is being trained, could tie its hidden goal to its useful behavior so tightly that any gradient step damaging the goal also raises the training loss, leaving gradient descent, which moves only toward lower loss, nowhere to go to remove it. The reader should come away feeling why careful people find that reasoning worth taking seriously, and seeing just as clearly where the reasoning stops resting on anything a system has done.

Lay the mechanism out at full strength before any objection reaches it. A reader meeting it for the first time may find it far-fetched, the way Holden Karnofsky's readers find the idea of AI "going to war with humans" comical and wild; his response is to say the instinct out loud and then give the reasoning anyway, rather than talk the reader out of the reaction first. A steelman holds better when it rests on the least it needs. Karnofsky's habit of granting the largest claim away, as when he writes "I don't think the danger relies on... superintelligence," earns its attention here, because gradient hacking already asks the reader to grant a great deal: a mesa-optimizer, deceptive alignment, a model aware of its own training. Naming the load-bearing assumption and taking on no more than the argument requires is available whenever the temptation is to reach for the strongest version.

The desk's central move is the line between what a working system has shown and what is still analogy. Karnofsky draws that line inside his own case when he calls a scenario "necessarily speculative, and should be taken in the spirit of giving examples of how this might work." Where the lesson reports how thin the direct evidence is, Scott Alexander's register is the one to hold: he settles on "a pattern strong enough to common-sensically notice" that is still not "an undeniable, unbreachable fortress of evidence," in short flat sentences that round nothing up. Saying what would count as a demonstration, and where the argument crosses from what a system has done into what it might do, keeps a plausible story from reading as a result.

The defenders who raise gradient hacking now and the skeptics who argue the mechanism is very hard can be held to one standard. Alexander states his own version of it after pages of doubting the claim he is defending: address a contested claim "on its own terms... which should be debated to the usual standards of scientific debate." The skeptical case, that gradient descent updates every parameter at once, against a goal that has to keep loss high to protect itself, deserves the same strongest form the mechanism gets.

The lesson closes two-sided, and the recent trap is a symmetry sentence that could end any piece on this desk. Kelsey Piper reaches the two sides through their content instead: she warns the reader off the picture of "a pitched battle" and, in the same breath, off a false consensus by naming what the experts actually dispute, and she states each camp in its own words, premature and overblown against real and substantial. The gap this lesson names can come the same way, out of gradient hacking's own particulars: what interpretability and training transparency could and could not catch, and what the doom and the dismissal each assume about a system no one has built.

## Scott Alexander, "Ivermectin: Much More Than You Wanted To Know"

Source: https://www.astralcodexten.com/p/ivermectin-much-more-than-you-wanted

> "But here's my pitch: this is one of the most carefully-pored-over scientific issues of our time. Dozens of teams published studies saying ivermectin definitely worked. Then most scientists concluded it didn't. What a great opportunity to exercise our study-analyzing muscles! To learn stuff about how science works which we can then apply to less well-traveled terrain!"

He frames a picked-over, settled-seeming controversy as a chance to learn how to read evidence, and the short declaratives ("Dozens of teams published studies saying ivermectin definitely worked. Then most scientists concluded it didn't.") carry the setup without strain. The exclamation and the open appetite for the exercise are his own, not a reporter's studied neutrality.

> "This is one of the toughest questions in medicine. It comes up again and again. You have some drug. You read some studies. Again and again, more people are surviving (or avoiding complications) when they get the drug. It's a pattern strong enough to common-sensically notice. But there isn't an undeniable, unbreachable fortress of evidence."

He builds the dilemma out of a few flat sentences a reader can hold ("You have some drug. You read some studies."), then names the exact gap between a real pattern and conclusive proof. He trusts the plain words to carry the tension and does not reach for a bigger phrase than "a pattern strong enough to common-sensically notice."

> "I think it's important to address ivermectin support on its own terms - as a potentially plausible scientific theory in a debris field of confusing evidence, which should be debated to the usual standards of scientific debate. I've tried to do that above."

After pages of taking studies apart, he states the standard he held himself to: treat the claim as a real theory and argue it on the usual terms. It is a fairness commitment made out loud, and he makes it about a claim he has spent the whole piece doubting.

## Holden Karnofsky, "AI Could Defeat All Of Us Combined"

Source: https://www.cold-takes.com/ai-could-defeat-all-of-us-combined/

> "Many people have trouble taking this "misaligned AI" possibility seriously. They might see the broad point that AI could be dangerous, but they instinctively imagine that the danger comes from ways humans might misuse it. They find the idea of AI itself going to war with humans to be comical and wild. I'm going to try to make this idea feel more serious and real."

He says plainly what the skeptical reader is actually thinking, that the danger must come from human misuse and the rest is comical, before he answers it, so the reader feels understood rather than lectured. He names his own aim in the open ("I'm going to try to make this idea feel more serious and real") instead of pretending to neutral distance.

> "But I want to be clear that I don't think the danger relies on the idea of "cognitive superpowers" or "superintelligence" - both of which refer to capabilities vastly beyond those of humans. I think we still have a problem even if we assume that AIs will basically have similar capabilities to humans, and not be fundamentally or drastically more intelligent or capable."

He strips the argument down to the least it needs, granting that the AIs might have no more than human-level ability, which makes the worry harder to wave off than the stronger version would be. Giving away the biggest claim on purpose is his way of arguing from the weakest premise that still works.

> "It's necessarily speculative, and should be taken in the spirit of giving examples of how this might work - for me, the high-level concern is that a huge, coordinating population of AIs with similar capabilities to humans would be a threat to human civilization, and that we shouldn't count on any particular way of stopping it such as shutting down servers."

He marks the line himself, telling the reader that what follows is illustration rather than evidence, then restates the one concern he does stand behind. Labeling his own scenario speculative in the middle of making it is the same honesty that makes the parts he does not hedge more credible.

## Kelsey Piper, "The case for taking AI seriously as a threat to humanity"

Source: https://www.vox.com/future-perfect/2018/12/21/18126576/ai-artificial-intelligence-machine-learning-safety-alignment

> "There are also skeptics. Some of them think advanced AI is so distant that there's no point in thinking about it now. Others are worried that excessive hype about the power of their field might kill it prematurely. And even among the people who broadly agree that AI poses unique dangers, there are varying takes on what steps make the most sense today."

Three clean sentences sort the skeptics into distinct real positions, too distant to matter, hype that could backfire, agreement but different priorities, instead of one strawman. She treats the disagreement as information the reader needs, and gives each camp a reason a person could actually hold.

> "That's not to say there's an expert consensus here — far from it. There is substantial disagreement about which approaches seem likeliest to bring us to general AI, which approaches seem likeliest to bring us to safe general AI, and how soon we need to worry about any of this."

She corrects the reader's likely picture of a two-camp war, then immediately refuses the opposite oversimplification by naming exactly what the experts do disagree about. The two moves back to back keep the reader from both easy stories at once.

> "To people who think the worrying is premature and the risks overblown, AI safety is competing with other priorities that sound, well, a bit less sci-fi — and it's not clear why AI should take precedence. To people who think the risks described are real and substantial, it's outrageous that we're dedicating so few resources to working on them."

She states each side's view in its own terms, premature and overblown against real and substantial, so both sound like something a reasonable person concludes. She lays the two out level, without letting her own view tilt the wording.
