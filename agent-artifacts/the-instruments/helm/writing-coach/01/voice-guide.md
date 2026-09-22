# Voice guide: the-instruments/helm (01)

## How this piece should sound

This lesson explains how HELM turns many separate measurements into one
leaderboard rank, the mean win rate, and how that one number hides the places
where the underlying scores disagree. The reader is quick and widely read and
has never opened the HELM paper or the leaderboard. Write so that reader can
follow every step and, by the end, recompute the point without you.

Keep the register plain and exact. Dan Luu states a claim and says what is at
stake in the same sentence, with no throat-clearing and no words spent sounding
careful. Write the mechanics of HELM that way: name the scenarios, the seven
metrics, the standardized 5-shot run and the mean win rate in plain words the
first time each appears, use one word for each idea and keep using it, and
assume the reader already has few-shot prompting and accuracy from earlier
lessons.

Show the aggregation happening. Gladwell does not tell the reader that a ranking
is arbitrary. He prints the Car and Driver scores, changes the weights, and lets
the order change on the page. HELM's mean win rate is built from choices too:
which scenarios count, which of the seven metrics go into the average, whether
the efficiency and robustness axes stay in. Where the piece has a case in which
reweighting the scenarios or dropping an axis moves the order, the reader should
be able to watch the order move.

Tie the rank to the measurements under it. Shalizi's point about g is that a
single summary number can be a reflection of how the inputs were combined rather
than a fact discovered in the world. The mean win rate is computed from the
per-scenario results and cannot say more than they do. Keep the rank attached to
those results wherever the piece uses it, so a "#1 on HELM" claim reads as the
output of a procedure the reader has watched.

Be exact about what each metric measures and where it stops. Gladwell's suicide
ranking looks authoritative until he asks what a coroner actually records, and
the number that seemed objective turns out to rest on a judgment. HELM's
calibration, robustness, fairness, bias and toxicity numbers each count
something specific and narrow. Say what each one counts before the piece leans
on it, and say plainly where a model that scores well on one scores badly on
another.

Where the piece makes a claim about the ranking, show the check. Luu's stance is
that a benchmark number is worth only as much as the reader's ability to audit
it. When the lesson says the order changes under a different, equally defensible
choice, the arithmetic or the comparison that shows it belongs in the piece.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "The implication for the former is that measuring is less valuable than
> building and for the latter that measuring isn't valuable at all (perhaps
> other than for fame), but I don't see measuring as lesser let alone worthless.
> If anything, because measurement is, like writing, not generally valued, it's
> much easier to find high ROI measurement projects than high ROI building
> projects."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
Luu quotes the dismissive question he actually got, then answers it in a plain
declarative sentence with the stakes attached: measuring is undervalued, so the
high-return projects are easy to find. He states the claim straight and moves
on, spending no sentence reassuring the reader he is being fair. The "like
writing" aside is his own standing judgment showing through the argument.

> "One thing that both increases and decreases the impact of doing good
> measurements is that most measurements that are published aren't very good.
> This increases the personal value of understanding how to do good measurements
> and of doing good measurements, but it blunts the impact on other people,
> since people generally don't understand what makes measurements invalid and
> don't have a good algorithm for deciding which measurements to trust."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
This is Luu being skeptical about the thing his own readers rely on: most
published measurements are poor, and most people have no way to tell which to
trust. He gives the reason inside the sentence instead of asserting the
conclusion and leaving it there. The plainness is what lets the skepticism read
as a finding and not a complaint.

> "Trusting vendors is not a strategy. We know that vendors will lie and cheat
> to look better at benchmarks. Saying that it's a vendor's fault for lying or
> cheating can shift the blame, but it won't result in reviews being accurate or
> useful to consumers."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-22
Luu names the excuse, blame the vendor, and refuses it in short flat sentences.
The verdict comes first and the reason follows, and he does not soften "lie and
cheat" into anything more polite. You can hear a practitioner who has watched
this happen and stopped being surprised by it.

## Malcolm Gladwell, "The Order of Things"

Source: https://www.newyorker.com/magazine/2011/02/14/the-order-of-things

> "In other words, in trying to come up with a ranking that is
> heterogeneous—a methodology that is broad enough to cover all vehicles—Car and
> Driver ended up with a system that is absurdly ill-suited to some vehicles."

Checked: https://ialjs.org/wp-content/uploads/2017/01/Gladwell_TheOrderOfThings_NYer_14Feb2011r.pdf, retrieved 2026-09-22
Gladwell has just printed three different rankings of the same three cars,
produced by changing the weights, and this sentence says what that showed in one
plain clause. He names the cause, the one broad methodology stretched across
every vehicle, instead of calling the result arbitrary. The judgment "absurdly
ill-suited" is his, placed where the arithmetic has already earned it.

> "An algorithm takes a slate of statistics on each college and transforms them
> into a single score: it tells us that Penn State is a better school than
> Yeshiva by one point. It is easy to see why the U.S. News rankings are so
> popular. A single score allows us to judge between entities (like Yeshiva and
> Penn State) that otherwise would be impossible to compare. At no point,
> however, do the college guides acknowledge the extraordinary difficulty of the
> task they have set themselves."

Checked: https://ialjs.org/wp-content/uploads/2017/01/Gladwell_TheOrderOfThings_NYer_14Feb2011r.pdf, retrieved 2026-09-22
Here Gladwell describes the aggregation step itself: a slate of statistics
becomes a single score that puts one school above another by a point. He credits
why the single score is appealing before he turns on it, and the turn is a plain
observation about what the guides never admit. The prose stays exact about the
mechanism while making the skeptical point.

> "This list looks straightforward. Yet no self-respecting epidemiologist would
> look at it and conclude that Belarus has the worst suicide rate in the world,
> and that Hungary belongs in the top ten. Measuring suicide is just too tricky.
> It requires someone to make a surmise about the intentions of the deceased at
> the time of death."

Checked: https://ialjs.org/wp-content/uploads/2017/01/Gladwell_TheOrderOfThings_NYer_14Feb2011r.pdf, retrieved 2026-09-22
Gladwell takes a table that looks authoritative and asks what the number
actually records, which turns out to be a judgment about a dead person's intent.
He walks from the clean-looking list to the messy thing under it in plain steps,
with no technical vocabulary and no announced doubt. The skepticism is carried
by the example rather than stated.

## Cosma Shalizi, "g, a Statistical Myth"

Source: http://bactra.org/weblog/523.html

> "the case for g rests on a statistical technique, factor analysis, which works
> solely on correlations between tests. Factor analysis is handy for summarizing
> data, but can't tell us where the correlations came from; it always says that
> there is a general factor whenever there are only positive correlations. The
> appearance of g is a trivial reflection of that correlation structure."

Checked: http://bactra.org/weblog/523.html, retrieved 2026-09-22
Shalizi states his whole case in three plain sentences: the general factor is
what the method always produces from positively correlated tests, so its
appearance tells you nothing about where the correlations came from. He is
precise about what the technique does and blunt about what it cannot do, in the
same breath. The word "trivial" is his verdict, and the sentences around it hold
the reasoning that backs it.

> "The two-factor theory was a genuinely scientific theory of considerable scope
> and empirical content, which would have been very important if it was true.
> The way we can unambiguously tell that it had falsifiable empirical content is
> that it was, in fact, falsified."

Checked: http://bactra.org/weblog/523.html, retrieved 2026-09-22
Shalizi explains what made a theory scientific by pointing at what happened to
it: it could be tested, and the test failed. He treats the falsification as a
plain fact about the theory's history instead of an abstraction about method.
The short closing clause reads cleanly because the sentence before it set up
exactly what was falsified.

> "Thomson's ability-sampling model not only creates the illusion of a general
> factor of intelligence where none exists, it can also make this illusory
> factor look heritable."

Checked: http://bactra.org/weblog/523.html, retrieved 2026-09-22
This is Shalizi's one-sentence summary of a rival model that reproduces the
single factor out of many independent causes, put in words a non-specialist can
hold. He says plainly that the factor can be an illusion and that the illusion
can even look inherited. The clarity comes from naming the model and then saying
exactly what it does, with no cushioning.
