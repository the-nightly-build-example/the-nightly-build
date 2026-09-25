# Voice guide: the-instruments/mlperf

## How this piece should sound

This lesson explains a number that gets stripped from its box before it reaches
a headline. Write the way you would explain to a smart friend why "3x faster"
on a spec sheet can be true and still tell them nothing about the machine they
are about to buy: plain sentences, real figures, and the specific thing that
went missing between the results table and the press release.

State the incentive plainly and move on. Dan Luu's line on vendor benchmarks
below does not soften the claim with "some critics argue" or "it could be
argued that." MLPerf submitters are graded on their own numbers; say that
outright, the way you would say a runner is timed on their own watch, and then
go straight to showing it in a results table rather than asserting it twice.

When a vendor's headline figure and the underlying total pull apart, put both
numbers on the page and do the division that separates them, in the reader's
sight. Chips and Cheese does this with SPEC scores and physical-core counts:
show the total, show the count of chips each system used, and let the reader
watch the per-system number turn into the per-chip number. That is the move
this lesson needs for its "N times faster" case: the headline ratio and the
system-scale ratio, both on the page, so the reader sees where the multiplier
came from.

Go to the primary document before explaining what it conceals. Willison finds
the vendor's own press release and quotes its language before he tells you
what it leaves out. Do the same with a submission: give the division, the
category, the chip count, or the scenario name as MLCommons or the vendor
wrote it, then say what comparing across that boundary does and does not
support.

Where the reporting is generous rather than gotcha, let it be generous. Evans
does not accuse the paper she's describing of dishonesty when their own
benchmark result turned out backwards; she treats it as evidence that
benchmarking is harder than it looks, even for people who are good at it. The
misled "N times faster" case in this lesson has an MLPerf division and a
system scale sitting in the results table the whole time. The reader who got
misled did not do enough arithmetic, not something shadier, unless the record
shows otherwise.

Keep the hardware and the claim about the hardware as two separate verdicts,
and let the second one be the smaller of the two. Chips and Cheese closes on a
sentence that keeps its praise for the silicon intact while cutting the
marketing down to size. This lesson's MLPerf number is real, comparable
results are useful, and the "N times faster" headline can still be doing
something the number itself never claimed.

This is a lesson, so the two bookends carry the stance the body does not need
to announce for itself: the body stays in the results table and the rules
document, and lets the bookends say what a reader should now do with an MLPerf
claim the next time one crosses their feed.

## Dan Luu, "Measurement, benchmarking, and data analysis are underrated"

Source: https://danluu.com/why-benchmark/

> "Other than Volvo, car manufacturers generally design their cars to get the highest possible score on published crash tests; they'll add safety as necessary to score well on new tests when they're published, but not before"

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-25
The sentence states a mechanism, not a mood: manufacturers optimize for the test, and the semicolon clause gives the specific behavior that follows from it. There is no hedge in front of the claim and no adjective doing the work a fact should do. The writer is visible in the flat, declarative "but not before," which lands the point without dressing it up.

> "...after Consumer Reports and Car and Driver found that the Tesla Model 3 had extremely long braking distances (152 ft. from 60mph and 196 ft. from 70mph), Tesla updated the algorithms used to modulate the brakes, which improved braking distances enough that Tesla went from worst in class to better than average"

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-25
The exact distances in feet, at two named speeds, are what make this checkable instead of anecdotal; a reader could go find the same numbers. The writer trusts the figures to carry the sentence and does not add a sentence telling you how impressive they are.

> "We know that vendors will lie and cheat to look better at benchmarks. Saying that it's a vendor's fault for lying or cheating can shift the blame, but it won't result in reviews being accurate or useful to consumers."

Checked: https://danluu.com/why-benchmark/, retrieved 2026-09-25
Two short sentences state the incentive and then state why naming it isn't enough by itself. Nothing here is softened into "some might say" or "critics have argued"; the writer says who does what and why it matters to the reader, in that order.

## Simon Willison, "Open weight LLMs exhibit inconsistent performance across providers"

Source: https://simonwillison.net/2025/Aug/15/inconsistent-performance/

> "Artificial Analysis published a new benchmark the other day, this time focusing on how an individual model—OpenAI's gpt-oss-120b—performs across different hosted providers."

Checked: https://simonwillison.net/2025/Aug/15/inconsistent-performance/, retrieved 2026-09-25
The opening sentence names the organization, the exact model, and the axis being tested before any interpretation. A reader who has never heard of Artificial Analysis still knows what was measured and by whom from this one sentence.

> "I hadn't heard of CompactifAI before—I found this June 12th 2025 press release which says that "CompactifAI models are highly-compressed versions of leading open source LLMs that retain original accuracy, are 4x-12x faster and yield a 50%-80% reduction in inference costs" which helps explain their notably lower score!"

Checked: https://simonwillison.net/2025/Aug/15/inconsistent-performance/, retrieved 2026-09-25
He goes and finds the vendor's own words instead of guessing at a reason, then quotes them directly so the reader can judge the claim against the number for themselves. The exclamation point is the one place he lets his own reaction show, after the sourcing is already done.

> "As a customer of open weight model providers, this really isn't something I wanted to have to think about! It's not really a surprise though. When running models myself I inevitably have to make choices—about which serving framework to use (I'm usually picking between GGPF/llama.cpp and MLX on my own Mac laptop) and the quantization size to use."

Checked: https://simonwillison.net/2025/Aug/15/inconsistent-performance/, retrieved 2026-09-25
He states his own stake in the result plainly, then immediately grounds the complaint in his own concrete choices rather than a general grievance. Naming the specific tools he picks between is what keeps this from reading as a complaint about nothing in particular.

## Julia Evans, "Benchmarking correctly is hard (and techniques for doing it better)"

Source: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/

> "I don't point this out to make fun of the researchers for coming up with an incorrect result. I'm pretty sure they're way better at performance analysis than I am. Instead, I think this is a really good illustration that benchmarking programs and figuring out which one is faster is really hard – much much harder than you might think."

Checked: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/, retrieved 2026-09-25
She has just described a published paper's own headline result turning out backwards, and instead of using it to score a point, she says plainly that she rates the researchers above herself. The repetition in "much much harder" reads as someone thinking out loud, not a rhetorical flourish.

> "I'm less interested in the question of academic rigor here and more interested in the idea of benchmarking correctly in practice – I'd like to make programs faster, and a great way to make your stuff WAY FASTER is to make many small 5% improvements. So you need to actually be able to detect a 5% improvement."

Checked: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/, retrieved 2026-09-25
The number does the arguing: a 5% improvement is only worth chasing if your method can actually see 5%, and she says so directly instead of gesturing at "small gains add up." The capitalized "WAY FASTER" is the one place enthusiasm breaks through a sentence that is otherwise doing careful, quiet work.

> "But as a person who's done a lot of data analysis, the idea that you should look at the data that you're using to make an important decision (more than just calculating a single point estimate of the median / average) seems extremely reasonable to me."

Checked: https://jvns.ca/blog/2016/07/23/rigorous-benchmarking-in-reasonable-time/, retrieved 2026-09-25
She closes the post by naming her own qualification for the opinion before giving it, and the opinion itself is modest: look at the data, not just one summary number. "Seems extremely reasonable to me" undercuts any sense that she is delivering a verdict from on high.

## Chips and Cheese, "NVIDIA's Vera Whitepaper Has a Thread Loose"

Source: https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread

> "Unfortunately, NVIDIA also spends a good part of the paper trying to turn those interesting design choices into a morality play about x86. Traditional simultaneous multithreading is drawn as time-slicing, a configurable NUMA topology is presented as an unavoidable 32-node maze, four SPEC components become "agentic benchmarks," undefined performance-counter ratios are promoted as causal proof, and an unlabeled pictogram becomes a 1.8x reinforcement-learning result."

Checked: https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread, retrieved 2026-09-25
The second sentence lists five specific things the whitepaper does, each with the exact technical unit it happened to (SMT, NUMA nodes, SPEC components, counter ratios, a pictogram), so the list is doing five separate jobs and not padding one point five times. The single word "Unfortunately" is the only place the writer's own reaction appears before the evidence starts.

> "Then we reach Figure 24, "Vera drives 1.8x for RL training," with the figure being a row of little completed-task squares. There is no model, environment, CPU/GPU allocation, framework, batch size, power measurement, repetition count, or error bar. We do not even know whether the squares represent samples, steps, or some random layout of tiles at NVIDIA HQ."

Checked: https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread, retrieved 2026-09-25
The middle sentence is a plain list of every variable the chart is missing, in the vocabulary a reader of the field already has, which is what makes "there is no error bar" land instead of just sounding technical. The last sentence's guess about tiles at NVIDIA HQ is the one joke in the passage, and it only works because the list just before it earned it.

> "None of that makes Vera slow, it simply makes NVIDIA's proof smaller than NVIDIA Marketing's prose."

Checked: https://chipsandcheese.com/p/nvidias-vera-whitepaper-has-a-thread, retrieved 2026-09-25
The sentence keeps the hardware verdict and the marketing verdict apart in its own grammar, one clause each, so praising the chip and cutting down the whitepaper don't get to blur into each other. "NVIDIA's proof" against "NVIDIA Marketing's prose" is the whole argument of the piece compressed into two matched nouns, not a line built to be lifted.
