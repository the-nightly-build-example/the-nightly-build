# Voice guide: the-instruments/rouge (01)

## How this piece should sound

This lesson explains how one ROUGE number is produced and what it can be trusted
to mean, for a reader who is quick but has never seen the metric. The register
that fits is plain and teacherly, closer to working through an arithmetic problem
than to arguing about benchmarks. The reader is owed the actual counting, not a
report of the result.

Where the lesson first names a ROUGE score, it can say what the number is before
any formula, the way Kalid Azad states that an average is whatever single value
could replace the whole set. ROUGE-N and ROUGE-L each measure overlap between a
candidate summary and a human reference, recall-oriented against that reference.
Stating that in plain words first gives the formulas something to land on.

The worked ROUGE calculation is the center of the piece, and the exemplars show
what a good one looks like. Alex Reinhart's mammogram case counts concrete units
in front of the reader, a thousand women down to seventy false positives, and
Azad shows the median of a four-item list with bare integers. A ROUGE example can
run the same way: a short candidate and a short reference chosen so the reader can
count the overlapping n-grams by hand and carry the division to the score, instead
of being handed the number. Reinhart's habit of laying out every figure first,
with each term defined where it is used, suits a reader meeting recall, n-gram,
and reference summary for the first time.

Even-handedness is where this piece is hardest, and two exemplars model it without
tipping. Azad weighs the mean against the median by saying what each is for, and
Max Roser weighs the advantage of a concrete measure against its downside, neither
one calling a number wrong. Where the lesson separates what string overlap can
establish from the quality and faithfulness it is often taken to prove, it can
hold the same even hand: name what a ROUGE score is good for and where it goes
blind, each on its own terms, keeping the verdict until the counting has earned
it.

Roser also has the frame for the blind spot. He keeps a measure distinct from the
thing it stands for, a measure of population health that is not a definition of
health, and he states plainly that any number compressing a great deal of
information into one figure will carry shortcomings. A string-overlap score that
never reads meaning is such a number, and the lesson can present the faithfulness
gap as a property of the measure rather than as an accusation against it.

One more move from Roser is available where the construction section needs it. He
shows a design choice changing a figure by building a stripped-down case, two
identical countries that differ in one decision. If the lesson shows how a choice
inside ROUGE moves the score, which n, recall against an F-measure, one reference
or several, stemming or none, it can make that concrete on the small example
rather than asserting it.

## Kalid Azad, "How To Analyze Data Using the Average"

Source: https://betterexplained.com/articles/how-to-analyze-data-using-the-average/

> "The average is the value that can replace every existing item, and have the same result. If I could throw away my data and replace it with one “average” value, what would it be?"

Azad names the thing before he computes it: the average is whatever single value
could stand in for the whole set. The definition is concrete and comes before any
formula. Azad is visible in the habit of restating a familiar quantity as a plain
question the reader can answer.

> "The median solves this problem by taking the number in the middle of a sorted list. If there’s two middle numbers (even number of items), just take their average. Outliers like 100 only tug the median along one item in the sorted list, instead of making a drastic change: the median of 1 2 3 4 is 2.5."

The rule and its worked case sit in the same breath, and the case uses bare
integers small enough to check by eye. Nothing is asserted that the reader cannot
verify against "1 2 3 4". Azad is visible in how the mechanics and the tiny
example are never separated.

> "Figures like housing prices and incomes are often given in terms of the median, since we want an idea of the middle of the pack. Bill Gates earning a few billion extra one year might bump up the average income, but it isn’t relevant to how a regular person’s wage changed. We aren’t interested in “adding” incomes or house prices together — we just want to find the middle one."

Azad weighs one measure against another by saying what each is for, and grounds it
in a case the reader already holds, Bill Gates against a regular wage. Neither
number is called wrong; each is placed where it fits. Azad is visible in the even
hand and the everyday example that carries it.

## Alex Reinhart, "The p value and the base rate fallacy" (from *Statistics Done Wrong*)

Source: https://www.statisticsdonewrong.com/p-value.html

> "There has been some controversy over the use of mammograms in screening breast cancer. Some argue that the dangers of false positive results, such as unnecessary biopsies, surgery and chemotherapy, outweigh the benefits of early cancer detection. This is a statistical question. Let’s evaluate it."

Reinhart states the dispute, then narrows it to something a calculation can
settle, and says so plainly. The two short sentences at the end set up the work
without dramatizing it. Reinhart is visible in the low, matter-of-fact register
that treats a charged topic as arithmetic.

> "Suppose 0.8% of women who get mammograms have breast cancer. In 90% of women with breast cancer, the mammogram will correctly detect it. (That’s the statistical power of the test. This is an estimate, since it’s hard to tell how many cancers are missed if we don’t know they’re there.) However, among women with no breast cancer at all, about 7% will get a positive reading on the mammogram, leading to further tests and biopsies and so on. If you get a positive mammogram result, what are the chances you have breast cancer?"

Every number the calculation will need is laid out first, each with its
plain-language meaning attached, and the passage ends on the question the reader
now wants answered. The aside defines statistical power in the place it is used.
Reinhart is visible in the patience of loading the facts before drawing any
conclusion.

> "Imagine 1,000 randomly selected women who choose to get mammograms. Eight of them (0.8%) have breast cancer. The mammogram correctly detects 90% of breast cancer cases, so about seven of the eight women will have their cancer discovered. However, there are 992 women without breast cancer, and 7% will get a false positive reading on their mammograms, giving us 70 women incorrectly told they have cancer."

Reinhart runs the base rate as a count rather than a formula: a thousand women,
eight with cancer, seven detected, seventy false positives. The reader can follow
each step and check it. Reinhart is visible in the flat, unhurried tally that lets
the surprising result arrive on its own.

## Max Roser, "What is economic growth? And why is it so important?"

Source: https://ourworldindata.org/what-is-economic-growth

> "Growth is often measured as an increase in income or inflation-adjusted GDP per capita. But these measures are not the definition of it — just like life expectancy is a measure of population health but is certainly not the definition of population health."

Roser separates a number from the thing it stands for, and pins the distinction
with a second case the reader already accepts, life expectancy against health. The
sentence keeps the measure and the reality it points to apart without dismissing
the measure. Roser is visible in the care to say what a figure is, and is not, a
definition of.

> "Finding a measure means that you have to find a way to express a huge amount of relevant information in a single metric. As the sketch shows, you have to first measure the quantity and quality of all the many, many goods and services that get produced and then find a way to aggregate all of these measurements into one summarizing metric. No matter what measure you propose for such a difficult task, there will always be problems and shortcomings in any proposal you might make."

Roser describes what any single summarizing number is doing, compressing a great
deal into one figure, and states the consequence evenly: every such measure will
have shortcomings. It neither defends nor attacks a particular metric. Roser is
visible in the calm, general statement of the trade-off that any aggregate number
makes.

> "Imagine two countries that are identical except for one aspect: home ownership. In Country A, everyone rents their homes, and the total sum of annual rent amounts to €2 billion per year. In Country B, everyone owns their own home, and no one pays rent. To provide housing is certainly an economic service, but if we only counted monetary transactions, then we would get the false impression that the value of goods and services in Country A is €2 billion higher than in Country B."

Roser shows a construction choice changing a figure by building two identical
countries that differ in one decision, with the rent named in round numbers. The
reader sees how a boundary drawn one way or another moves the total. Roser is
visible in the invented, stripped-down case used to make a measurement rule
concrete.
