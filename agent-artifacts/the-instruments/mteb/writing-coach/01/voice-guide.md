# Voice guide: the-instruments/mteb (01)

## How this piece should sound

This lesson explains how one number on the MTEB leaderboard is assembled: a
per-dataset score in whatever metric that task happens to use, those datasets
gathered into task types, and a plain average laid over the whole pile. The
reader is quick and widely read but has never worked in a codebase, and is
meeting this number the way every team building retrieval meets it, as the thing
that sorts the leaderboard they are about to trust. Write for someone deciding
what to rely on, not for someone who already knows embedding models inside out.

Hold the register Harford reaches for when he warns that scepticism can curdle
into cynicism. The piece is going to show the reader specific places where the
average misleads, and the pull at that point is to leave them thinking the
leaderboard is a con. It is not. The average is a real, usable summary that was
built for reasons and breaks down in particular spots, and the piece can give
the usable half its due as squarely as Harford gives statistics theirs before he
turns to how they deceive. The aim is a reader who understands where this
average bends, not one who leaves distrusting every number they meet.

Where the piece puts a figure on how far apart two models sit, the top of the
leaderboard against the middle of it, or one model against the next, Silver's
move with batting averages is available: give the number, then set it beside a
difference the reader can already feel, and say plainly when a gap that looks
decisive on a ranked table is small next to the error the score itself carries.
A general reader has no feel for what a fraction of an average MTEB point is
worth, and a comparison they already hold is what gives it one.

When the piece reaches the point where topping the overall mean and being the
right model for a given reader's job come apart, Luu's separation of relative
rank from real proficiency is the plainest way to hold the two ideas apart. He
does it by naming a concrete thing a highly ranked player still gets wrong, so
the reader can check the distance rather than take it on his word. The
counterpart here is a specific task or use the average buries, made concrete
enough to see, rather than a general reminder that averages hide things.

The construction itself, different metrics on different datasets folded into task
types and folded again into one mean, is where Luu's point about a measure with
no single dimension applies. Naming plainly what each fold gives up, at the
moment the piece performs that fold, keeps the construction legible. And Silver's
habit of exposing his own method and inviting the reader to disagree with it fits
a lesson whose whole purpose is to let the reader judge the number themselves:
show where the choices were made, and where a step rests on a decision someone
could have made differently, say so.

Some of what the piece shows will correct an obvious reading, that the model at
the top of the table is simply the best model. Where it does, Silver's way of
earning a correction is available: he names the intuitive measure, then works a
concrete case where that measure fails, instead of asserting the intuition
wrong. A worked case the reader can follow does more than a flat contradiction.

## Nate Silver, "How FiveThirtyEight Calculates Pollster Ratings"

Source: http://web.archive.org/web/20260426063250/https://fivethirtyeight.com/features/how-fivethirtyeight-calculates-pollster-ratings/ (archived; the original fivethirtyeight.com URL now redirects away from the piece)

> "In baseball, there isn't much difference in an absolute sense between a .300 hitter and a .260 hitter — it amounts to getting about one extra hit during each week of the baseball season. Likewise, the differences in poll accuracy aren't that large. We estimate that the very best pollsters might be about 1 percentage point more accurate than the average pollster over the long run. However, the average poll in our database missed the final election outcome by 5.3 percentage points. That means even the best poll would still be off by 4.3 points."

Silver gives the ranking its due and then deflates it with arithmetic: the best
pollster beats the average by about a point, the average poll is already off by
more than five, so the distance between best and typical is small next to the
error they all carry. He ties an unfamiliar quantity, a percentage point of poll
accuracy, to one a general reader can feel, the difference between a .300 and a
.260 hitter. The honesty is in refusing to let his own ranking sound more
decisive than the numbers support.

> "The database also includes a column indicating whether a poll "called" the winner of the race correctly. But we think this is generally a poor measure of poll accuracy. In a race that the Democrat won by 1 percentage point, a poll that had the Republican winning by 1 point did a pretty good job, whereas one that had the Democrat winning by 13 was wildly off the mark."

He takes the most intuitive way to judge a poll, did it call the winner, and
shows with one worked pair of numbers why it is a bad measure. He does not just
assert that the intuitive reading is wrong; he builds a case where calling the
winner and being accurate come apart. The worked example is how he earns the
correction instead of asking the reader to take it on faith.

> "Test everything out for yourself — probably you'll agree with some elements of our approach and disagree with others. Better yet, maybe you'll discover a bunch of cool things that we hadn't thought to look for. We think there should be more pollster ratings — FiveThirtyEight shouldn't have the last word on them."

Silver hands the reader the raw data and invites disagreement with his own
method. It is the posture of someone confident enough in the work to show the
choices it rests on, and it treats the reader as a checker rather than an
audience. His plain admission that his own outfit "shouldn't have the last word"
is the opposite of a writer defending a number he needs you to accept.

## Dan Luu, "95%-ile isn't that good"

Source: https://danluu.com/p95-skill/

> "People will argue that players at this rank should be good because they're better than 95% of other players, which makes them relatively good. But non-relatively, it's hard to argue that someone who doesn't realize that you should step on the objective to probably win the game instead of not touching the objective for a sure loss is good."

Luu pulls apart two claims that a percentile invites you to run together: that
someone is better than 95 percent of others, and that they are actually good. He
settles it with a concrete, checkable example, not stepping onto the objective
to win, so the judgment rests on something the reader can see rather than on his
say-so. The blunt "is good" at the end is his habit of committing to a plain
verdict once the example has earned it.

> "One complication is that real life activities tend not to have a single, one-dimensional, objective to optimize for. Another is that what makes someone good at a real life activity tends to be poorly understood (by comparison to games and sports) even in relation to a specific, well defined, goal."

Luu marks exactly where a clean ranking stops being possible: when the thing
being measured has more than one dimension and no agreed definition of good. He
states the two complications plainly and separately rather than gesturing at
"it's complicated." The care to keep a well-defined goal distinct from a poorly
understood one is the empiricist in him, declining to average over a distinction
that matters.

## Tim Harford, "How to Truth with Statistics"

Source: https://timharford.com/2022/01/how-to-truth-with-statistics/

> "That weakness is Huff's tendency to make statistics seem like a game, a stage magician's trick, all good fun but never to be trusted. I worry that we're starting to trust nobody; we're starting to believe that lying with statistics is all anyone ever does. Huff does not help."

Harford is diagnosing a failure mode in the reader, not scoring a point against
Huff. He names the specific over-correction he worries about, deciding that lying
with statistics is all anyone ever does, and then assigns blame for it in a
three-word sentence. The flatness of "Huff does not help" is where you hear him:
he has a clear view and states it without hedging or heat.

> "Scepticism is all very well, but not if it curdles into cynicism. Statistics can be used to deceive but they are also a vital tool in our quest to understand the world around us, like a telescope for an astronomer."

Harford holds two positions at once without softening either: numbers can be
used to deceive, and they are still among the best instruments we have. He gives
the pro-statistics half real weight rather than a token nod, which is what keeps
the skepticism from reading as an attack. The comparison to a telescope does
concrete work, naming what statistics are for instead of decorating the
sentence.
