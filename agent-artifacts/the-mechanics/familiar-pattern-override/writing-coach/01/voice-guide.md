# Voice guide: the-mechanics/familiar-pattern-override

## How this piece should sound

This lesson is about a single trick almost every reader has already watched happen: take a famous riddle, change the one detail that flips the answer, and the model recites the textbook answer anyway. The piece should sound like someone walking a smart friend through why that happens, not like someone building a case for or against the model's intelligence. Plain claims, one mechanism at a time, and no more confidence than the evidence carries.

The trick itself can open the piece the way Dan Luu opens "Suspicious discontinuities": a plain, recognizable scene, stated flatly, that leaves the strangeness for the reader to notice on their own. Someone typing a lightly-altered Monty Hall or surgeon riddle into a chatbot and watching it recite the familiar answer is exactly that kind of scene, and the mechanism can wait a paragraph while the moment lands first.

The causal chain the commission already lays out — training prior, then template completion, then surface similarity — can be built the way Ciechanowski builds the watch: each part finished, shown failing to fully explain the behavior on its own, before the next part arrives to cover what's left. Once a term is set (next-token probability, training prior, template completion), it can stay fixed through every later step, the same way Ciechanowski keeps "escapement" and "pallet fork" exact once he's named them instead of trading them for a friendlier word later on.

Where the piece cites the AIW paper, a modified-riddle study, or a "the model can't reason" argument, Dan Luu's habit of stating exactly what a source shows and doesn't show is the right model for the gap this lesson has to hold open. He corrects the common misreading of the cocaine-sentencing data with a fact from the paper itself, not a hedge, and "models complete high-probability patterns" needs the same plain correction against "models can't reason": the two are not the same claim, and the distance between them is worth stating outright.

The open question about what this proves about reasoning calls for Julia Evans's habit, not a performance of caution about it. She never writes that the evidence is generally unsettled; she names the one specific thing she doesn't have a good answer for and stops there. This lesson's open question can work the same way: name the specific study, fix, or measurement that would move the reasoning debate, instead of a sentence that only rates how contested it is.

With no code and no shared terminal to point at, the worked example can do the job Evans's `dig` output does: show the puzzle's literal wording, the literal word that changed, and the model's literal answer before naming the general mechanism, the same way she shows the actual confusing output before explaining what's going on inside it. The reader sees the swap happen in the puzzle's own words before being told what caused it.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "But it took me YEARS to figure out how to confidently debug DNS issues, and I've seen a lot of other programmers struggle with debugging DNS problems as well. So what's going on?"

She states the puzzle through her own long struggle instead of an abstract claim that DNS is hard, then asks the plain question the rest of the post answers. The one capitalized word carries the exasperation; there's no separate sentence describing how frustrating it was.

> "It took me probably 5 years to realize that I shouldn't visit a domain that doesn't have a DNS record yet, because then the nonexistence of that record will be cached, and it gets cached for HOURS, and it's really annoying."

The claim is a specific, checkable mechanical fact — visiting a domain with no record caches its absence for hours — not a general statement that DNS caching is confusing. She reports her own five-year delay in learning it without dressing the delay up as anything more than annoying.

> "I don't have as good answers here as I would like to, but knowledge about weird gotchas is extremely hard won (again, it took me years to figure out negative caching!) and it feels very silly to me that people have to rediscover them for themselves over and over and over again."

She says plainly that she doesn't have a good answer instead of manufacturing one, and the sentence stops there instead of pivoting into a summary that pretends otherwise. The person is visible in the mild, self-directed exasperation of "it feels very silly to me," which is aimed at herself and the situation, not at the reader.

## Dan Luu, "Suspicious discontinuities"

Source: https://danluu.com/discontinuities/

> "If you read any personal finance forums late last year, there's a decent chance you ran across a question from someone who was desperately trying to lose money before the end of the year."

The opening sentence is a scene, not a thesis: a specific kind of forum, a specific season, a person doing something that sounds backwards. The counterintuitive behavior is stated flatly, and the reason for it waits for the next paragraph instead of getting folded into the same sentence.

> "I've seen this paper used as evidence of police malfeasance because the amount of cocaine seized jumped to 280g. This is the opposite of what's described in the paper, where the author notes that, based on drug seizure records, amounts seized do not appear to be the cause of this change."

He names the specific wrong reading before correcting it, and the correction is a fact drawn from the paper itself, not an appeal to his own authority. Nothing in the passage tells the reader he's being careful; the second sentence just states what the source says.

> "This post doesn't really have a goal or a point, it's just a collection of discontinuities that I find fun."

He undercuts any implied significance of the piece in his own closing note instead of closing on a claim that sums up what it all means. It reads as a person talking about something he finds interesting, not a report grading its own findings.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "Unlike their quartz and smart siblings, mechanical watches can run without using any batteries or other electronic components."

The one fact given here is the fact the rest of the piece depends on: no battery, so where does the motion come from. It's stated without an adjective inflating it, and it sets up the piece's whole question without announcing that it's doing so.

> "We clearly have some work to do – the hand spins way too fast, and it only does a few rotations before the mainspring inside the barrel runs out of the stored energy. Clearly, this contraption won't let us track time in any reliable way."

He builds a version of the mechanism, shows it visibly failing, and states plainly that it fails before moving to the part that fixes it. "Clearly" is doing real work both times: it points at something the reader just watched happen instead of asserting a conclusion the reader has to take on faith.

> "We need to find a way to control the rate of release of the energy stored in the mainspring – we'll do this with the escapement."

The sentence states the unsolved problem and names the exact part that solves it in the same breath, which is how each section hands off to the next one. The technical name isn't softened or pre-defined; the sentence trusts the next section to earn it.
