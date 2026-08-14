# Voice guide: how the Humanity's Last Exam benchmark number is built

## How this piece should sound

This lesson explains how a Humanity's Last Exam score is produced and what such
a score is and is not evidence of, for a reader who is smart, reads widely, and
keeps meeting the number in headlines with no way to check it. The register is a
serious paper: plain claims, the figures where they matter, and no cynicism or
hype about a benchmark that has become a talking point. The three writers below
all take a number people quote and show the machinery under it, and they do it
without either debunking for sport or selling the result.

Most of what makes a benchmark number confusing is that the procedure behind it
is out of sight. Julia Evans treats naming the hidden parts of a system as most
of the teaching, and an HLE score has several hidden parts a reader has never
been shown: who wrote the questions, how they were chosen, what a model is
allowed to see, and how an answer is judged right or wrong. Where laying out one
of those steps plainly would remove the confusion, that is the lesson doing its
work. Evans also shows that a topic can turn out to be smaller than it looked
once it is laid open, and the piece can let the procedure be comprehensible
without inflating its difficulty or talking down to the reader who found it
opaque.

The score is a single figure built by combining many separate results, and that
construction is where readers go wrong. Hannah Ritchie's rhino passage carries
its point on real numbers: two populations, one collapsing and one growing,
average out to a figure that describes neither. Where the article can show the
same move on a concrete case, working the actual procedure on a small, real
example will teach more than a description of the method. When it comes to the
misreadings a reader has met in headlines, Ritchie names the wrong version
flatly and still takes the journalists' side, because she has made the slip
herself. Correcting how the number is commonly read, without scoring points off
the people who read it that way, fits a reader who is probably one of them.

Marking the limits of the score is half the lesson, and it can be done evenly.
Ritchie lists what her index leaves out and gives an ordinary reason for the
gap, without treating the omission as a scandal and without concluding the
number is worthless. The same steadiness lets the piece say what an HLE score
genuinely supports and what it cannot reach in one breath. Dan Luu sets the
standard for that judgment: ask what was actually measured, on what, rather than
trust the impression the headline figure gives. Where a claim about a model
rides on what the number seems to say, the article can separate what the score
advertises from what its procedure can bear, and let a plain figure sit there
when the mismatch is the finding.

Keep the sentences short and single-purpose for the most part, and let a longer
one run when it is under control, the way Luu's measurement sentence tracks a
whole move from doubt to instrument. Give figures as figures, and anchor any
number the reader cannot scale to something they already hold. A grand word
about what the benchmark proves waits until the procedure has earned it.

## Hannah Ritchie, "Living Planet Index: what does it really mean?"

Source: https://ourworldindata.org/living-planet-index-decline

> "These are just three of many headlines covering the Living Planet Index. But
> they are all wrong. They are based on a misunderstanding of what the Living
> Planet Index shows. I sympathize with the journalists. Interpreting this
> metric is hard."

Ritchie states the misconception flatly, quotes the headlines that got it wrong,
and then takes the journalists' side instead of scoring points off them. The
sympathy is hers: she says the metric is genuinely hard to read and admits
elsewhere that she has slipped the same way, which lets her correct the reader
without talking down. The short declaratives carry the correction with nothing
added on top.

> "By averaging these two populations we've ended up pretty clueless about the
> status of either of them. Either a 15% [or 74% using the geometric mean]
> decline would give a skewed understanding of the situation. The Black rhino in
> Tanzania has lost 96% of its rhinos and has become critically endangered. On
> the other hand, something is going right in Botswana because its numbers have
> increased."

This is the payoff of a worked example she built from two real rhino
populations, and the concrete numbers do the arguing: a 96% loss and a rising
population average into a figure that describes neither. Her care shows in the
bracketed "[or 74% using the geometric mean]", where she keeps the harder,
truer figure in view rather than quietly dropping it. The point is stated once
and left to stand.

> "Second, many taxonomic groups are not included at all - nothing on insects,
> fungi, coral or plants. This is largely due to data availability - it's easier
> to count bears than ants. Still, we should be wary of generalizing these
> results to all life on Earth."

She lists what the index leaves out and gives the plain, unglamorous reason for
the gap without treating it as an exposure. The closing caution is measured: be
wary of generalizing, not that the number is meaningless. Ritchie's evenness is
visible in how she credits the data's limit and its use in the same passage.

## Dan Luu, "Keyboard latency"

Source: https://danluu.com/keyboard-latency/

> "In general, my belief is that if someone makes performance claims without
> benchmarks, the claims probably aren't true, just like how code that isn't
> tested (or otherwise verified) should be assumed broken."

Luu sets a plain standard for believing a number and grounds it in something his
reader already accepts, that untested code is assumed broken. The comparison is
an engineer's instinct, and it makes the skepticism read as ordinary discipline
rather than a pose. One sentence, one standard, no hedging.

> "I never trust feelings like this because there's decades of research showing
> that users often have feelings that are the literal opposite of reality, so
> got a high-speed camera and started measuring actual keypress-to-screen-update
> latency as well as mouse-move-to-screen-update latency."

He distrusts his own impression, says why, and then goes and measures instead of
arguing about it. The single long sentence follows the whole move from doubt to
instrument to the exact quantities recorded, and the specificity of
"keypress-to-screen-update latency" is where the practitioner shows. He does not
dress the decision up; he reports it.

> "Most keyboards add enough latency to make the user experience noticeably
> worse, and keyboards that advertise speed aren't necessarily faster. The two
> gaming keyboards we measured weren't faster than non-gaming keyboards, and the
> fastest keyboard measured was a minimalist keyboard from Apple that's marketed
> more on design than speed."

The conclusion states what the measurements found in plain terms: the keyboards
sold on speed were not the quick ones, and the quickest was sold on looks. He
names the specific result and lets the gap between the marketing and the numbers
sit there without a flourish. The deflation is quiet, which is the Luu part.

## Julia Evans, "Why is DNS still hard to learn?"

Source: https://jvns.ca/blog/2023/07/28/why-is-dns-still-hard-to-learn/

> "When I finally learned how to troubleshoot DNS problems, my reaction was
> “what, that was it???? that's not that hard!”. I felt a little bit cheated! I
> could explain to you everything that I found confusing about DNS in a few
> hours."

Evans admits the subject turned out not to be hard once she saw it whole, and
that she felt cheated by how long it took. That admission is the person on the
page: she remembers being confused, and she traces the confusion to machinery
that was hidden from her instead of to the idea. The excitement and the
punctuation are her own register; the part that carries is the honesty that a
scary-seeming topic can be smaller than it looks.

> "just teaching people what the hidden systems are makes a huge difference. For
> a long time I had no idea that my computer had many different DNS libraries
> that were used in different situations and I was confused about this for
> literally years."

Her whole method sits in this line: naming the hidden parts of a system is most
of what makes it learnable. She backs the claim with her own case, years of
confusion because no one told her the machine had several DNS libraries, so it
rests on experience rather than assertion. The plainness and the confession are
both hers.
