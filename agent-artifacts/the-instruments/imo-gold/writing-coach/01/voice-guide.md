# Voice guide: the-instruments/imo-gold

## How this piece should sound

This lesson teaches how one number is made: the score under "an AI won a gold
medal at the International Math Olympiad." Its reader is quick and widely read
but has never sat with how an Olympiad proof is graded, so the writing carries
them from a problem to a medal without asking them to hold an unexplained term.
The register is the paper's: plain claims, concrete stakes, no fuss. When a
sentence could either sound impressive or be easy to follow, make it easy to
follow. A grand word like "gold" earns its weight from the conditions laid out
around it, not from the writing.

Walk the number in the reader's hands the way Timothy B. Lee walks task-length
scores, and ground the abstract scoring in one worked step the way he grounds
"how long humans take" in a single eight-hour task. The lesson turns on a kind
of measurement the reader may not have met: a coordinator reading a written
proof against a rubric and awarding partial credit, six problems at seven points
each. One problem, marked once, shows that more clearly than a description of the
whole system. Where the reader has to scale a figure they cannot picture, such
as a points total against a gold cutoff set by that year's human contestants,
anchor it to something they already hold.

The conditions are where this lesson lives, and the exemplars show how to state
them. Melanie Mitchell disqualifies a headline score by naming the two exact
rules it broke. Simon Willison refuses a leaderboard number without knowing how
many variants were tried behind it. When a medal depends on the time allowed,
the tools used, whether a human formalized the problem statements first, and who
did the grading, name each condition as a plain fact and not a caveat set to one
side. If one headline word turns out to cover scores produced by different
procedures, the material may call for holding those numbers apart rather than
letting a single story average them, the way Willison keeps a shipped model
distinct from the other variants a vendor tested privately.

Honesty about what a score does not settle is itself a finding. Lee reports the
impressive reading of a chart and then points at the confidence interval that
undercuts it, in the same level voice. This lesson can say plainly both what a
gold score certifies, which is particular problems solved under particular
conditions, and what it does not reach, without softening either half. A verdict
about the medal is welcome once the conditions are on the table. State it flat,
and let the facts already given carry it.

Keep the first person and any direct address for the two bookends, where the
template allows them. In the body the judgment sits in the conditions it states
plainly, and Mitchell and Willison show that a judgment delivered flat, on the
strength of the facts, reads as more certain than one dressed up.

## Timothy B. Lee, "Why it's getting harder to measure AI performance"

Source: https://www.understandingai.org/p/why-its-getting-harder-to-measure

> "But if you click on METR's task length page and hover over the dot for Claude Opus 4.6, you'll see something interesting: METR's confidence interval for Claude Opus 4.6 ranges from 5 hours to 66 hours. On Twitter, METR staff have urged people not to take the latest results as gospel."

Lee builds up the impressive reading of the chart and then sends the reader to
the tooltip where the caveat actually lives, so they can check it for
themselves. The plain "not to take the latest results as gospel" keeps his own
skepticism at a low, steady setting. You can see the reporter who went and
hovered over the dot.

> "In real workplaces, tasks are often connected to other tasks. They frequently require interacting with other people or the outside world. Sometimes it's not clear what task needs doing, and goals may evolve as people work on a project. Even after a task is completed, people might not agree on whether it was done well."

Four short sentences, each naming one concrete way real work differs from a
benchmark task. Nothing is dressed up, and the reader can picture each case. The
plainness is Lee's default setting, and it is what makes the abstract point
land.

> "METR didn't just guess how long humans would take on these tasks; it hired programmers and measured their actual completion times. For example, one problem in the METR test suite was to "speed up a Python backtesting tool for trade executions by implementing custom CUDA kernels while preserving all functionality." METR found that this takes human programmers about eight hours."

He grounds an abstract method, measuring how long humans take, in one real task
and one real number: eight hours. Quoting the task in full, CUDA kernels and
all, keeps the practitioner's exact words instead of smoothing them into "a hard
programming problem." The example does the explaining the claim alone could not.

## Melanie Mitchell, "On the "ARC-AGI" $1 Million Reasoning Challenge"

Source: https://aiguide.substack.com/p/on-the-arc-agi-1-million-reasoning

> "Oh yeah, they also rebranded ARC as "ARC-AGI", which I'm not a fan of, since I don't love the term "AGI," and I don't think that solving ARC is necessarily the golden ticket to achieving AGI, whatever AGI is. But no one is asking me for naming advice."

Mitchell states her objection to the rename and then undercuts her own standing
with "no one is asking me for naming advice." The joke rides on the actual
nouns, AGI and the golden ticket, so it carries a real point about the hype word
rather than decorating the paragraph. Her flat distrust of the term is visible
without any grand phrasing.

> "Greenblatt's method couldn't be run on the private evaluation set because it violated two rules of the competition: it required internet access (to use the GPT-4o API) and required more than the allotted 12 hours of run time."

She holds a headline score to the two exact rules it broke, internet access and
the 12-hour limit, stated as flat facts. The conditions do the judging; she
names them and lets that settle whether the score counts. This is how a number
gets measured against what actually produced it.

> "To me, this is reminiscent of the comparison between computer and human chess players. Computer players get a lot of their ability from the amount of look-ahead search they can do, applying their brute-force computational powers, whereas good human chess players actually don't do that much search, but rather use their capacity for abstraction to understand the kind of board position they're faced with and to plan what move to make."

She explains an abstract distinction, abstraction versus brute-force search,
through chess, which the reader already holds, and keeps both kinds of player
concrete. The long second sentence stays under control because each clause adds
one contrast and no more. You can see a researcher who cares about what the
number is supposed to measure, not only the number itself.

## Simon Willison, "Understanding the recent criticism of the Chatbot Arena"

Source: https://simonwillison.net/2025/Apr/30/criticism-of-the-chatbot-arena/

> "The Chatbot Arena has become the go-to place for vibes-based evaluation of LLMs over the past two years. The project, originating at UC Berkeley, is home to a large community of model enthusiasts who submit prompts to two randomly selected anonymous models and pick their favorite response. This produces an Elo score leaderboard of the "best" models, similar to how chess rankings work."

Three sentences take the reader from what the leaderboard is to exactly how its
number is produced: people pick a favorite of two anonymous answers, and those
votes become an Elo score. "Vibes-based" is doing honest work, naming the
softness of the input without sneering at it. The chess comparison lands the
mechanism for a reader who has never seen an Elo table.

> "If a model sits in top place, I'd like a footnote that resolves to additional information about how that vendor tested that model. I'm particularly interested in knowing how many variants of that model the vendor tested. If they ran 21 different models over a 2 month period before selecting the "winning" model, I'd like to know that—and know what the scores were for all of those others that they didn't ship."

Instead of calling for "transparency" in the abstract, Willison names the exact
thing he wants to see: a footnote, the count of variants, the scores of the ones
that were not shipped, with a concrete 21 models over two months. The
specificity is the argument. You can see the person who would actually read that
footnote.
