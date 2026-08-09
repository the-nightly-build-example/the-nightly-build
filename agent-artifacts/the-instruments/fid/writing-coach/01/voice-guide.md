# Voice guide: FID (The Instruments)

## How this piece should sound

This lesson has two jobs in sequence, and the exemplars below were chosen
because each writer does both without letting the second one curdle into
cynicism. First the piece has to make FID's machinery legible: what gets
pulled out of an image, what gets fit to a distribution, what gets measured
as a distance between two distributions. Only once that construction is on
the page, plainly, does the piece get to turn on it.

Build the number the way Noah Smith builds GDP before he argues about it. He
writes out "GDP = Consumption + Investment + Government Purchases + Net
Exports" in plain symbols before he does anything else, so that when he later
says imports net out to zero he is pointing at a term the reader already has
in hand. FID has the same shape: features pulled from a network, a Gaussian
fit to the real images' features and another to the generated images'
features, a distance computed between the two fitted Gaussians. State that
sequence in the same unhurried, one-clause-at-a-time way before the piece
does anything with it. A reader who cannot repeat the sequence back cannot
follow what breaks it.

The hardest parts to picture are also the ones this lesson cannot skip:
fitting a Gaussian to a cloud of feature vectors, and a distance between two
distributions rather than two points. Smith's move for an abstraction this
stubborn is a comparison the reader already owns and can run in their own
head unassisted — his shoes-on-a-scale image for netting a quantity out of a
total does more work than another paragraph of accounting language would.
Reach for one comparison of that kind for the hardest step in FID's
construction, built from something this piece's own reader already knows,
not borrowed from either exemplar's subject.

When the piece turns skeptical, do it the way Spiegelhalter does: recompute
a piece of the claim by a different, plainer route and show the reader where
it stops agreeing with itself. He does not assert that the ONS's £5.3 billion
figure is too high; he multiplies the same assumptions a second way and
watches the number imply something absurd about ordinary men's behavior. FID
supports the same kind of second pass — take one input to the number
(sample size, which network's features, what counts as "real") and push it
through the calculation a different way to see where the ranking it produces
stops matching what the images actually look like. That recomputation is
what earns the doubt.

The commission asks for a documented case where FID misled someone. When the
piece reaches it, let the specific stakes carry the paragraph the way
Smith's tariff paragraph does. He names Navarro, names the tariffs, and
states plainly that they rest in part on the accounting error he just
walked through, without a separate sentence declaring that the error
matters. Whatever case this piece uses, the strongest version of that
paragraph names who relied on the number and what they did because of it,
in a sentence or two, and stops there.

Precise doubt can still be funny without turning cynical about the field.
Silver's "20 percent probabilities have an uncanny knack for doing 20
percent of the time" is a joke, and it is also exactly, unembarrassably
true. The humor comes from the number behaving exactly as advertised. If a
line in this piece about FID's own limits wants to be funny, it should work
the same way: correct on inspection, aimed at the arithmetic itself.

Once a term is set in this piece, it stays. Smith writes "netting out" every time
after the first. Spiegelhalter's "reality check" recurs exactly the same
way. FID's own vocabulary — Inception features, the Gaussian fit, the
Fréchet distance, sample size — should hold the same way once each is
defined for a reader who has not met them before, per the lesson template's
own rule.

## Nate Silver, "Don't let randomness make a fool of you"

Source: https://www.natesilver.net/p/dont-let-randomness-make-a-fool-of

> "And there was some reputational risk: if our forecast was 80/20 on
> Election Day and the 20 percent came up — as 20 percent probabilities have
> an uncanny knack for doing 20 percent of the time — it was going to
> negatively affect my life."

The joke and the statistics lesson are the same sentence. The tautology
does the work by itself, delivered flat with no signal that a joke is
coming. The person is visible in the timing: he waits until "20 percent of
the time" to land it.

> "And keep in mind that polls come with a margin of error. Let's say that
> if we had Nostradamus-like abilities, we knew that the true state of the
> race is that Kamala Harris would win Wisconsin by 1 percentage point in an
> election held today. A typical poll has about 800 respondents. Well, the
> margin of error in an 800-person poll is plus or minus 3.5 points. Except,
> that substantially understates the case because the margin of error
> pertains only to one candidate's vote share. [...] So the margin of error
> on the difference separating the candidates is roughly twice that: about 7
> points. That means if the true state of the race is Harris +1, you'll get
> some Trump +5s and Harris +7s just from sampling error alone."

This is construction made vivid without slowing down: an invented
omniscient narrator ("Nostradamus-like abilities") to fix a true value, then
arithmetic that runs on real numbers a reader can check step by step. Silver
is visible in the correction mid-paragraph — catching himself understating
the case and doubling the figure in front of the reader instead of just
supplying the corrected number.

> "People treat probabilistic predictions as deterministic ones, e.g. if
> Trump goes from a 48 percent chance of winning Wisconsin to a 52 percent
> chance, you'll get a lot of Nate Silver is calling Wisconsin for Trump!!!
> even though the forecast expresses a high degree of uncertainty and
> nothing in the model has really changed."

The skepticism here targets how the number gets read on Twitter, a specific
and named failure mode. Silver is visible in choosing his own name as the
punchline of the misreading: he is the one who gets blamed for a sentence
the model never said.

## Noah Smith, "Why do econ journalists keep making this basic mistake?"

Source: https://www.noahpinion.blog/p/why-do-econ-journalists-keep-making

> "Here's a simple analogy: Does putting on shoes make you lose weight? No,
> it doesn't. And yet when you weigh yourself with your shoes on at the
> doctor's office, and you want to know your actual body weight, you
> subtract the weight of your shoes afterwards. Imports are to GDP what
> shoes are to your weight on the scale at the doctor's office — just
> something superfluous that gets added in for the sake of measurement
> convenience, and which has to be netted out again later to get the true
> number."

The analogy carries the entire accounting identity without a single term
from it. Smith is visible in the two short sentences that open it — a
question and a flat answer — before he lets the comparison do the rest of
the explaining.

> "Back when IBM was the biggest, most important tech company, there was a
> saying in stock trading: 'Nobody ever gets fired for buying IBM.' Similarly,
> practically everyone in econ journalism writes 'Imports subtract from GDP,'
> so if you write that too, no one is going to give you grief about it.
> There's safety in numbers; you won't be singled out."

This explains why a wrong number survives without accusing anyone of
dishonesty. Smith is visible in reaching for a stock-trading cliché rather
than a statistics term to explain herd behavior among reporters — the
comparison comes from outside the subject, which is what makes it land.

> "If econ reporters hadn't continuously said that 'imports subtract from
> GDP' for decades on end, this mistaken idea might not have embedded itself
> so strongly in the MAGA people's heads. The tariffs are based, at least in
> part, on a simple accounting mistake."

The stakes arrive as a named, specific claim: Navarro, the tariffs, the
accounting mistake underneath them. Smith is visible in stopping right
there, at two flat sentences connecting the mistake to the tariffs, with no
line added about why a reader should care.

## David Spiegelhalter, "Is prostitution really worth £5.7 billion a year?"

Source: https://understandinguncertainty.org/prostitution-really-worth-%C2%A357-billion-year.html

> "To quote the ONS: Number of prostitutes in UK: 61,000. Average cost per
> visit: £67. Clients per prostitute per week: 25. Number of weeks worked
> per year: 52. Multiply these up and you get £5.3 billion at 2009 prices,
> around £5.7 billion now."

The construction is given as the source stated it, four plain assumptions
multiplied together, before any argument starts. Spiegelhalter is visible in
choosing to quote the inputs rather than summarize them — the reader gets to
watch the arithmetic happen instead of being told its result.

> "As always, it's best to do a simple reality check. The ONS assumptions
> come to around 75,000,000 visits a year. Let's say 60,000,000 are from
> locals rather than foreign visitors, which is more than a million a week.
> There are around 20,000,000 men between 18 and 65 in the UK (taking an
> arbitrary upper limit), so this would mean that on average each of them
> buys sex three times a year."

This is the skeptical turn done entirely as arithmetic: a second calculation
run against the first one, on the page, in the reader's view. Spiegelhalter
is visible in "as always" — the reality check reads as a standing habit of
his, applied here the same way he'd apply it to any number.

> "The assumptions also mean that the average person working in prostitution
> is turning over nearly £100,000 a year, which Jolyon from Tax Relief 4
> Escorts says is completely implausible, and he should know."

The doubt lands through a named source, someone with a specific and faintly
funny qualification for why he's the one to ask about escort pricing.
Spiegelhalter is visible in the dry "and he should know," judgment
delivered without raising his voice.
