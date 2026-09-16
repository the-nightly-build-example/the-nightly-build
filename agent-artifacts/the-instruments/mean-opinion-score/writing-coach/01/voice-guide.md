# Voice guide: the-instruments/mean-opinion-score

## How this piece should sound

This lesson explains a number that looks like an absolute score — a MOS on a
fixed 1-to-5 scale — and has to leave the reader able to tell when two such
numbers are and aren't the same measurement. Hold to Fung's and Silver's
register below: plain declarative sentences carrying a specific figure, not an
adjective standing in for one. Where the piece has to state what a MOS is
worth (a within-test ranking) and what it isn't (a portable score), the shape
is the one Alexander reaches in the IQ piece — the number can be wrong while
the ranking underneath it stays right — worked out in MOS's own vocabulary
(listeners, category ratings, the confidence interval) rather than borrowed as
a line.

The step-by-step section — who is recruited, how samples are chosen, how
ratings are collected and averaged — has the most to gain from Silver's move
in the polling-average piece: name a mechanism, then run one concrete instance
of it in the same paragraph before moving to the next mechanism. A
crowdsourced listening test recruiting a handful of raters for one sample and
producing one mean is worth walking through the way Silver walks through 46
percent, 43 percent, and the average that should minimize error against
Thursday's poll.

For the section on the misleading comparison — a "human parity" or cross-paper
claim that treated two incompatible tests as one scale — Fung's GMAT piece is
the nearer model, because it stays inside one system's incentives rather than
diagnosing a discrepancy across several data sources the way Alexander does.
State each thing that made two MOS figures incomparable as its own clause: the
rater pool, the instructions, the other systems in the test, the audio
conditions. Fung's rules-of-the-game list states each mechanism and stops;
skip a sentence afterward telling the reader what to conclude from it.

The declared reader has never run a listening test, so naturalness, the
scale's labeled points, and the confidence interval each need the kind of
plain-word definition Silver gives house effects and Alexander gives norming:
at first use, and in this lesson's own terms rather than assumed from any of
the three passages below.

## Kaiser Fung, "Why are GMAT scores going up?"

Source: https://www.junkcharts.com/why-are-gmat-scores-going-up/

> "In the print edition, the article is printed on six columns. Not until the
> sixth column does the writer acknowledge that 'the test costs $250 for each
> attempt.' Allowing redos is an amazing business. So the stars are aligned:
> the college admissions people want to report higher GMAT averages; the
> applicants want to feel good about themselves; the test providers rake in
> the $$$; the test prep industry sucks even more of the $$$."

This paragraph works one joke through four clauses, each naming a different
party's incentive, and closes by repeating the dollar signs rather than
reaching for a bigger word. The parenthetical fact about the cost per attempt
sits inside the argument instead of decorating it. The aside about which
column of the newspaper buried that cost is Fung noticing what a source
downplayed, not editorializing about it.

> "The casualty is accurate measurement of whatever the GMAT test is supposed
> to measure. In an accompanying chart, we learn that the average score of all
> exams is consistently at least 20 points lower than the average scores sent
> to MBA programs. A 20-point gap for the average test-taker is a huge
> difference."

The first sentence states a conclusion; the next two give the number that
earns it. "A huge difference" is sized in plain words, by a 20-point gap
against the scale it sits on, rather than asserted with a stronger adjective.

> "Here are the rules of the game:
>
> College admissions staff only looks at the maximum score (why don't they
> look at the average or median?)
>
> The test providers allow test takers to strike low scores from their record
> within 72 hours, thus preventing these scores from being seen by schools"

Each rule is stated as a fact about the system, one to a line, and the one
aside — "why don't they look at the average or median?" — is Fung's judgment
sitting inside a parenthesis rather than claiming its own sentence. The list
carries the explanation; nothing summarizes it afterward.

## Scott Alexander, "The Mystery of Internet Survey IQs"

Source: https://www.astralcodexten.com/p/the-mystery-of-internet-survey-iqs

> "These are implausibly high. Only 1/200 people has an IQ of 138 or higher.
> 1/50 people have IQ 130, but the ClearerThinking survey used crowdworkers
> (eg Mechanical Turk) who should be totally average."

The claim that the averages are implausible is checkable in the same breath:
two population fractions sit right next to it. "Should be totally average" is
where his own expectation for the data shows through, stated as a fact about
the sample rather than a complaint about the number.

> "But there's still a problem here. Using an accurate SAT score → IQ
> calculator, we determined that the ClearerThinking average should be 124.
> But using real cognitive tests, it looks like it's 110. What went wrong?"

He states the same quantity two ways — should be 124, looks like it's 110 —
before asking what went wrong, and the gap between those two numbers is what
carries the paragraph forward, not a transition sentence announcing a puzzle.
Alexander is visible in leaving the contradiction sitting there unresolved
rather than smoothing past it.

> "The tested-IQ of this subgroup who report their scores is 114. So although
> they are a little smarter than the overall sample, most of the difference
> seems to be coming from some kind of falsehood/delusion. But it's a
> surprisingly well-behaved falsehood/delusion. Self-reported IQ test score
> correlates 0.54 with tested IQ. So people are getting their rank order
> mostly right, they're just wrong about the specific number."

One number (114) supports a qualified conclusion, then a second number (0.54)
revises what that conclusion means. The last sentence states exactly the
distinction the two numbers support — rank order versus specific value — no
further and no less.

## Nate Silver, "How Silver Bulletin calculates our polling averages"

Source: https://www.natesilver.net/p/silver-bulletin-polling-average-methodology

> "More precisely, the polling average on a given date is calculated using
> local polynomial regression. Technically speaking, we use a blend of more
> aggressive and more conservative settings. However, these settings are
> determined empirically based on what produces more stable averages that are
> free from autoregression. In other words, the current polling average should
> be the best predictor of forthcoming surveys. If Trump approval is 46
> percent on Tuesday and 43 percent on Wednesday, whatever average you
> calculate (i.e., 44 percent or 44.5 percent) should minimize error on what a
> new survey would say on Thursday."

The passage moves from the name of a method straight to a worked pair of
numbers — 46 percent, 43 percent, an average of 44 or 44.5 — so the definition
lands on a concrete case in the same paragraph it's introduced in. Silver
states his own standard for a "right" average, minimizing error against the
next survey, as a criterion rather than asserting it as self-evidently
correct.

> "House effects are persistent differences between a given firm's polls and
> those of other firms that survey the same race. For example, if a given
> firm's polls are on average 3 points more favorable to Democratic candidates
> than the average of other polls conducted at the same time, we back a
> proportion of that difference out (in this example, this would mean shifting
> the firm's surveys toward Republicans)."

He defines a term and runs one specific number through the definition in the
same sentence: three points, adjusted back out, with the direction of the
adjustment named. The parenthetical spelling out what the correction does in
practice is where the abstraction is made to actually land.

> "Too little smoothing can make the curve jut up and down unnecessarily and
> will result in overfitting of the data. If you smooth too much, however, the
> curve may be aesthetically pleasing but won't do all that good a job of
> describing the data and may be slow to catch up to new trends."

Two sentences hold both failure modes of the same setting, stated in plain
terms rather than technical ones: a curve that juts, a curve that looks good
but isn't. The word choice shows someone aware that a chart can look right
while being wrong.
