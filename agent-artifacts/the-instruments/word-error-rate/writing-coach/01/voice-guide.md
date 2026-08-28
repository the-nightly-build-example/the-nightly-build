# Voice guide: the-instruments/word-error-rate (01)

## How this piece should sound

Word Error Rate reaches the reader as a single settled percentage, but it
starts life as a count of edits against a reference transcript, and the
piece should let the reader see that gap between the two before it argues
anything else about the number. Open on one instance of the number doing
real work in the world, the way Angwin, Larson, Mattu, and Kirchner open
"Machine Bias" on Borden and Prater rather than on Northpointe's scoring
procedure: a person, a specific figure attached to a specific claim, and
only then the machinery that produced it. The "human parity" claim this
piece is built around can arrive the same way, as something that happened
to someone or something someone said in public, ahead of any definition of
the metric behind it.

WER is a fraction, and every fraction the piece states needs both halves
named the first time it appears, not just the resulting percentage. Angwin et
al. do this reflexively: "Only 20 percent of the people predicted to commit
violent crimes actually went on to do so" tells the reader what's on top and
what's on bottom in one clause. Silver and George do it too, with "assigned
approximately 6 percent of AV — when, in fact, they are responsible for
roughly 30 percent of total marginal value." A WER figure is edits over
reference words, and the piece should say so in those terms the first time a
number is used to argue something, not just report the percentage and move
on.

The place readers guess wrong about WER is the counting step itself: which
kinds of mistakes get counted, how they're weighted against each other, and
what the reference transcript's own choices contribute to the count before
any system has spoken a word. Silver and George have a model for correcting a
reader's guess at exactly this kind of moment, in the passage on how ELWAY's
rating changes don't zero out the way Elo's do: state the version the reader
already assumes, say plainly that it isn't true, then say what happens
instead. That three-step move, not a list of rules, is what should carry the
piece through wherever WER's arithmetic diverges from what "count the
errors" sounds like it means.

Where the piece needs the reader to feel, rather than just be told, that a
number everyone treats as objective actually rests on a judgment call,
Gladwell's aside on measuring suicide rates is worth studying for the move
itself: a short excursion into a different domain establishes that this kind
of hidden judgment call is common to measurement generally, then the piece
returns to its own subject having earned the claim rather than asserted it.
Use the device sparingly and bring it back to WER quickly; the digression
works for Gladwell because it's brief and because the essay has the room of
a magazine feature, and this piece does not have that room to spend touring
other measurements for their own sake. One clean case and one fully worked
mechanism, not several examples for texture, is the right scope for a daily
lesson.

The reader has no time in a codebase, so the alignment step — turning a
transcript comparison into a count of edits — should read as a procedure a
person could actually carry out, in full sentences, the way Silver and
George keep the QB-adjustment and pace-factor logic in prose long after a
bulleted spec sheet would have been the easier way to write it, and the way
Angwin et al. describe Northpointe's 137 questions as things asked of
defendants rather than as a formula. Reach for a table only where the reader
needs to compare several named quantities side by side, per the house
literal-strings rule; don't let the procedure collapse into pseudocode
along the way.

## Julia Angwin, Jeff Larson, Surya Mattu, and Lauren Kirchner, "Machine Bias"

Source: https://www.propublica.org/article/machine-bias-risk-assessments-in-criminal-sentencing

> "Yet something odd happened when Borden and Prater were booked into jail: A
> computer program spat out a score predicting the likelihood of each
> committing a future crime. Borden — who is black — was rated a high risk.
> Prater — who is white — was rated a low risk. Two years later, we know the
> computer algorithm got it exactly backward. Borden has not been charged
> with any new crimes. Prater is serving an eight-year prison term for
> subsequently breaking into a warehouse and stealing thousands of dollars'
> worth of electronics."

This is the second paragraph of the piece, and the score hasn't been
explained yet — the reader meets it only as a verdict attached to two named
people, one of whom it got right and one of whom it got backward. The
writers withhold the mechanism on purpose: "we know the computer algorithm
got it exactly backward" is the kind of flat, declarative sentence a report
can make because the two outcomes just given support it word for word.

> "We obtained the risk scores assigned to more than 7,000 people arrested in
> Broward County, Florida, in 2013 and 2014 and checked to see how many were
> charged with new crimes over the next two years, the same benchmark used by
> the creators of the algorithm. The score proved remarkably unreliable in
> forecasting violent crime: Only 20 percent of the people predicted to
> commit violent crimes actually went on to do so."

This is the moment the piece states its own method, and it states the
denominator along with the number: not "the score is unreliable" but a
population size, a time window, and the fraction that follows from them. The
sentence "the same benchmark used by the creators of the algorithm" is doing
quiet, specific work — it forecloses the objection that the reporters graded
the tool by a standard the tool wasn't built to meet.

> "Overall, Northpointe's assessment tool correctly predicts recidivism 61
> percent of the time. But blacks are almost twice as likely as whites to be
> labeled a higher risk but not actually re-offend. It makes the opposite
> mistake among whites: They are much more likely than blacks to be labeled
> lower risk but go on to commit other crimes."

Three sentences carry three different facts about the same score — an
overall accuracy figure, then one direction of the error broken out by group,
then the mirror-image error in the other group — and none of the three
substitutes for the others. A single "the tool is biased" would have cost
the piece exactly this structure, which is what lets a reader hold both
failure modes at once instead of one vague impression.

## Malcolm Gladwell, "The Order of Things," The New Yorker

Source: https://www.newyorker.com/magazine/2011/02/14/the-order-of-things

> "Car and Driver is one of the most influential editorial voices in the
> automotive world. When it says that it likes one car better than another,
> consumers and carmakers take notice. Yet when you inspect the magazine's
> tabulations it is hard to figure out why Car and Driver was so sure that
> the Cayman is better than the Corvette and the Evora."

This comes right after the piece has shown the reader the actual scoring
table, so "it is hard to figure out why" isn't an opinion dropped on the
reader — it's an invitation to go check the arithmetic the paragraph just
displayed. The authority of the ranking (consumers and carmakers take
notice) is stated before it's undercut, which is why the undercutting lands.

> "This list looks straightforward. Yet no self-respecting epidemiologist
> would look at it and conclude that Belarus has the worst suicide rate in
> the world, and that Hungary belongs in the top ten. Measuring suicide is
> just too tricky. It requires someone to make a surmise about the
> intentions of the deceased at the time of death. In some cases, that's
> easy. Maybe the victim jumped off the Golden Gate Bridge, or left a note.
> In most cases, though, there's ambiguity, and different coroners and
> different cultures vary widely in the way they choose to interpret that
> ambiguity."

Gladwell reaches outside the piece's own subject (college rankings) to make
a general point about measurement, and the borrowed case is allowed to run
for several sentences before he brings it back. What keeps it from reading
as padding is that every sentence adds a new reason the count is softer than
it looks — the coroner, the culture, the ambiguous cause of death — rather
than restating the first one.

> "A school like Penn State, then, can do little to improve its position. To
> go higher than forty-seventh, it needs a better reputation score, and to
> get a better reputation score it needs to be higher than forty-seventh.
> The U.S. News ratings are a self-fulfilling prophecy."

The circularity is stated twice, once as a plain description of what Penn
State would have to do and once as the general name for it, and the second
sentence is only earned because the first one just demonstrated it with a
real school. Cut the first sentence and "self-fulfilling prophecy" would be
an assertion; left in, it's a description.

## Nate Silver and Joseph George, "How our ELWAY forecasts work," Silver Bulletin

Source: https://www.natesilver.net/p/how-our-elway-forecasts-work-methodology

> "Most NFL power ratings are based on the margin of victory or points
> scored and allowed in previous games. However, some statistics are more
> predictive of future performance than plain ol' points."

This is the sentence that justifies the entire rating system that follows,
and it does it by naming what a reader already assumes ratings are built
from before saying ELWAY departs from it. "Plain ol' points" is a small,
deliberately informal touch inside an otherwise exact sentence, and it marks
the authors' own voice without costing the sentence any precision.

> "One tricky factor in football is that offense bleeds over into defense
> and vice versa because a better offense creates improved field position
> and only one team possesses the ball at a time. The notion that 'the best
> defense is a good offense' is true; if you have the ball, the opposition
> is less likely to score on you than against the 1985 Bears. ELWAY accounts
> for this."

The 1985 Bears reference is a single, specific, named case standing in for
an entire class of teams (historically dominant defenses), and it does more
work than a general claim about defense would, because a reader who follows
football can picture the exact team being compared against.

> "In traditional Elo ratings, changes in team ratings always net out to
> zero for a given game. For example, if the Chargers gain 15 Elo rating
> points in defeating the Broncos, the Broncos lose 15 points. This is not
> true for ELWAY. Instead, both teams may wind up with net-positive or
> net-negative ratings for the game."

This is the passage the summary above points to directly: state what the
reader already believes about how the system must work, give one concrete
number to pin the belief down (15 points, one team, one game), say flatly
that it's wrong for this system, then say what replaces it. Nothing here
tells the reader the mechanism is surprising or counterintuitive — the
four-sentence structure demonstrates that on its own.
