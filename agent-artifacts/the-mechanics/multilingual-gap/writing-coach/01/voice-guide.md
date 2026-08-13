# Voice guide: the-mechanics/multilingual-gap (01)

## How this piece should sound

This lesson works backward from something the reader has felt: an assistant that is sharp in English turns vaguer, more error-prone, and oddly dearer in another language, and worst of all in languages written in a non-Latin script. The register that fits is plain and unhurried, a serious explanation for a reader who is smart and widely read but has never seen the inside of one of these systems and has no reason to be talked down to. Each step names a real part of the system in words that reader can already hold.

Fix what the model and the tokenizer actually operate on before explaining why the gap appears, the way Amit Patel pins down what A* can see ("It only sees the graph!") before any path is found. A reader cannot reason about why one language comes out worse until they hold what the training text was mostly made of, and what the tokenizer does to a sentence when it splits it.

Where the mechanism turns on a number, commit to the number. Ciechanowski does not say a watch needs a great many turns; he says forty hours, 2400 rotations, a ratio near 343 to 1, and the figure is what forces the next part into the design. The multilingual gap turns on real quantities too, a share of the training text and a count of tokens for the same sentence in two languages, and the writing can carry the same refusal to round: the figure the evidence supports, not "far more."

The reader arrives with a plausible story for the gap. Hold that story up and take it apart on a concrete case, as Ciechanowski raises the obvious way to drive the date ring and then shows in one sentence exactly what goes wrong with it. Where a familiar phrase carries the wrong picture, the writing can do what Julia Evans does with "DNS propagation": replace the phrase with the parts that are really moving, plainly enough that the wrong picture falls away on its own.

How much each cause contributes is partly unsettled, and the commission asks the piece to say which parts are settled engineering and which are open. Rate the claims in the writer's own voice, the way Evans marks her own line ("That's a strong statement and I don't have a lot of evidence for it") and Patel grants a reader's shortcut and then bounds it ("Yes, but only in this specific case"). The reader should be able to tell, from the sentence itself, whether they are holding a settled result or a guess.

When the piece sets the two causes beside each other, let the comparison rest on parts it has already shown at work, the way Patel's account of A* names two algorithms the reader has just watched fall short. A contrast drawn before its parts are built asks the reader to take it on faith; drawn after, it restates what they have already seen.

## Bartosz Ciechanowski, "Mechanical Watch"

Source: https://ciechanow.ski/mechanical-watch/

> "If we wanted our watch to run continuously for around 40 hours on a single wind, we'd need the minute hand to complete 40 rotations in that time. Moreover, the second hand should cover around 40 × 60 = 2400 complete rotations in that time. We need to find a way to convert a small number of revolutions of the barrel into a large number of revolutions of the hands. This is where gears come in."

The writing sets an exact requirement and only then names the next part. Forty hours, forty rotations, 2400 rotations: the count is the explanation, because it is the count that rules out attaching a hand straight to the barrel and so calls for gears. Ciechanowski is visible in the refusal to round; he gives the figure the mechanism actually needs rather than a word for how big it is.

> "One could naively assume that we could directly tie the rotation of the date ring to the rotation of the hour wheel, similarly to how we rotated the hour wheel in sync with minutes, albeit at slower pace. Unfortunately, this would cause the current date to continuously rotate under the little window in the dial, making it hard to read."

He raises the design a reader would reach for first, then disproves it with the specific thing that would go wrong: the date would creep under the window and be unreadable. The honesty is in taking the wrong guess seriously enough to test it, instead of waving it away. This is a teacher who has anticipated the reader's question before the reader asks it.

> "Notice that each big gear drives a smaller gear called a pinion. A pinion is mounted on the same shaft as the next big gear so we're able to keep increasing the speed on each axis."

A part is named and defined in the same breath, in plain words, and then put to work in the next clause. Nothing technical is left standing without its meaning attached to it. The definition costs one short sentence and the explanation moves on.

## Julia Evans, "DNS 'propagation' is actually caches expiring"

Source: https://jvns.ca/blog/2021/12/06/dns-doesn-t-propagate/

> "In fact, if you create a DNS record, it's possible that no DNS resolver will ever know about it! For example, I just created a record for a subdomain of jvns.ca that I will not tell you. Nobody will ever make a DNS query for that subdomain (I'm not going to make one, and you can't because I didn't tell you what it is!), so no resolver knows about it."

She proves an abstract claim, that records are pulled and not pushed, with a small concrete stunt: a subdomain she made and won't reveal, which therefore no resolver will ever learn. The example is carrying the argument, not decorating it. Evans is visible in the mischief of the instance and the exclamation she lets herself keep.

> "And if those cached records are still valid, they'll never request a new record! So a DNS update doesn't fully take effect until all cached versions of that record have expired. When people say 'we're waiting for DNS to propagate', what they actually mean is 'we're waiting for cached records to expire'."

One sentence swaps a misleading phrase for the parts that are really at work: what people call propagation is cached records expiring. The reframing is done by naming the actual mechanism plainly, so the wrong picture has nothing left to stand on. This is the same move the article makes on the gap the reader has felt.

> "Of course, I'm not sure that the term 'DNS propagation' is why people like my friend end up with an incorrect mental model for how DNS works. That's a strong statement and I don't have a lot of evidence for it!"

She states a claim and then rates her own confidence in it out loud: it is a strong statement, she does not have much evidence, and she says so plainly. The reader is never left unsure whether they are holding a finding or a guess. Evans is visible in the willingness to undercut her own line the moment it outruns what she can support.

## Amit Patel, "Introduction to the A* Algorithm"

Source: https://www.redblobgames.com/pathfinding/a-star/introduction.html

> "A* doesn't see anything else. It only sees the graph. It doesn't know whether something is indoors or outdoors, or if it's a room or a doorway, or how big an area is. It only sees the graph! It doesn't know the difference between this map and this other one."

Before any behavior is explained, the writing fixes exactly what the algorithm perceives by listing what it does not: not rooms, not doorways, not size. Pinning the input down first is what makes the later behavior follow instead of feeling like a rule handed down. The repeated "It only sees the graph!" is Patel's, and the repetition is what makes it land.

> "Dijkstra's Algorithm works well to find the shortest path, but it wastes time exploring in directions that aren't promising. Greedy Best First Search explores in promising directions but it may not find the shortest path. The A* algorithm uses both the actual distance from the start and the estimated distance to the goal."

The final part is introduced as the sum of two earlier ones, each named with the exact shortfall the piece has already shown: one wastes effort, the other can miss the shortest path. The contrast earns itself because the reader watched both algorithms run and fall short before this sentence arrived. Nothing here is asserted that was not first demonstrated.

> "Wouldn't it be faster to stop when adding the node to the queue? Yes, but only in this specific case. It doesn't work correctly when combining with other features, such as movement costs. I prefer to check when removing the node, so that the same technique works in general."

He voices the reader's natural shortcut as a question, grants it, then says precisely where it breaks and why he chooses the other way. The claim is bounded to the case where it holds rather than stated flat. The "I prefer" puts a person in the room making a judgment, which is different from a rule descending onto the page.
