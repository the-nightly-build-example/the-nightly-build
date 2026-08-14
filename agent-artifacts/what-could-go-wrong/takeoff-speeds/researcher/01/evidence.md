# Evidence: what-could-go-wrong/takeoff-speeds (01)

The evidence lets the article do exactly what the commission asks: state the
fast-takeoff case in its authors' own words, then draw a hard line between the
part of it that rests on observed systems and the part that rests on analogy or
on systems that do not exist yet. The fast case has one clean primary origin
(Good 1965) and two live modern forms (Yudkowsky's discontinuity argument;
the AI-2027 scenario). Both modern forms lean on the same two analogies —
hominid evolution and AlphaGo — and on recursive self-improvement in a system
no one has built. The continuous case (Christiano, Hanson) is the one with
observed system behavior behind it: neural-scaling laws (Kaplan; Hoffmann) show
capability has been a smooth, forecastable function of compute and data, and
METR's time-horizon measurement is a real six-year trend on real models.

Where the record is thin, and the article must not paper over it: (1) the same
METR trend that grounds the continuous case is also the empirical engine of the
fast-takeoff scenario, because a steady exponential extrapolated forward reaches
"AI that does month-long projects" inside a decade, and METR itself flags a
possible recent acceleration. The observed data does not settle the argument; it
is read both ways. (2) "Continuous" does not mean "slow in wall-clock" and does
not mean "safe" — Christiano's own doubling metric describes a world reorganizing
in years, and he argues in his own essay that a slow takeoff may be the *more*
dangerous one to govern. Any framing that equates continuity with reassurance
misreads the primary. (3) Bostrom's takeoff definitions are load-bearing and I
could verify only the "slow" sentence verbatim from primary text; the "moderate"
and "fast" wordings are confirmed in substance across multiple readers but not
quoted from the book itself here (the hosting page is behind a bot-check).

Nothing in the record undermines the commissioned angle. It supports it: the
angle is to separate what a working system has shown from what is projection, and
the sources fall cleanly on that line.

A caution that binds every quotation below. The passages I pulled from PDFs
(Good, METR) and from the arXiv abstract pages (Kaplan, Hoffmann) are verbatim
and marked `Quote`. The passages from LessWrong / Overcoming Bias / MIRI / AI-2027
pages came through a page-summarizing fetch, so I record them as `Reported` — the
substance is reliable and attributed to the right person, but the writer must
reopen the source and confirm exact words before setting any of them in
quotation marks.

## Sources

```text
URL:         https://www.sciencedirect.com/science/chapter/bookseries/abs/pii/S0065245808604180
Kind:        primary. I. J. Good is the author making the intelligence-explosion
             claim; this is the paper that owns it. (Read in full from the PDF
             hosted at languagelog.ldc.upenn.edu/myl/Good1964.pdf; the citable
             home of the text is the ScienceDirect chapter, Advances in Computers
             vol. 6, 1965, pp. 31-88.)
Establishes: The original statement of the intelligence explosion, and its
             explicit built-in caveat about control.
Locators:    Section 2, "Ultraintelligent Machines and Their Value," opening
             paragraph (p. 33 of the published chapter).
Quote:       "Let an ultraintelligent machine be defined as a machine that can far
             surpass all the intellectual activities of any man however clever.
             Since the design of machines is one of these intellectual activities,
             an ultraintelligent machine could design even better machines; there
             would then unquestionably be an 'intelligence explosion,' and the
             intelligence of man would be left far behind."
Quote:       "Thus the first ultraintelligent machine is the last invention that
             man need ever make, provided that the machine is docile enough to
             tell us how to keep it under control."
Paraphrase:  Good defines the runaway by one mechanism only: machine design is an
             intellectual activity, so a machine that beats humans at all
             intellectual activities beats them at machine design, and iterates.
             The whole claim is one sentence of deduction, not evidence. The
             control problem is present from the first statement, hung on the word
             "provided."
```

```text
URL:         https://www.lesswrong.com/posts/tjH8XPxAnr6JRbh7k/hard-takeoff
Kind:        primary. Eliezer Yudkowsky's own 2008 statement of the hard-takeoff
             view, from the Hanson-Yudkowsky AI-Foom debate.
Establishes: The strongest form of the discontinuity argument in its author's
             terms: recursive self-improvement need not be smooth, and evolution
             is offered as the precedent for a sharp capability jump.
Locators:    Post body, "Hard Takeoff" (Overcoming Bias / LessWrong, Dec 2008).
Reported:    Yudkowsky argues that folding optimization back on its own source
             ("dy/dt proportional to y") tends toward collapse or explosion, not a
             tidy linear middle, and that a smooth "soft takeoff" would require an
             improbably precise law of diminishing returns. He points to hominid
             evolution as a case where a slow, roughly-constant optimizer (natural
             selection) crossed some threshold in "general intelligence" and the
             result vastly outran the process that produced it. He locates the real
             "FOOM" at the point where the AI becomes able to do AI theory and
             "swallow its own optimization chain."
Note:        These are the fetch-summarizer's renderings, not verified verbatim.
             The load-bearing substance (RSI-need-not-be-smooth; the evolution
             threshold analogy) is his genuine position across the debate. Confirm
             wording before quoting.
```

```text
URL:         https://www.overcomingbias.com/p/30855html
Kind:        primary. Robin Hanson's own 2014 post "I Still Don't Get Foom,"
             restating his side of the debate against Bostrom's book.
Establishes: The continuous/broad case in its author's terms: capability is
             diffuse, gains come from many small pieces, and no single project
             leaps far ahead of the world.
Locators:    Post body, "I Still Don't Get Foom" (Overcoming Bias, Jul 2014).
Reported:    "For most big systems, overall architecture matters a lot less than
             getting lots of detail right." Hanson argues intelligence is "being
             better at many mental tasks by using many good mental modules," that a
             broadly better innovator "needs much better versions of that many
             modules," and that "if a project can't innovate faster than the world,
             it can't grow faster to take over the world." His analogy: industry
             "sits in thousands of places, must be wielded by thousands of people,
             and needed thousands of inventions," so "superintelligence just isn't
             the sort of thing that one project could invent."
Note:        Reported wording via page fetch. The architecture-vs-detail line and
             the "innovate faster than the world" line are characteristic Hanson
             and appear stable across retellings; confirm before quoting.
```

```text
URL:         https://sideways-view.com/2018/02/24/takeoff-speeds/
Kind:        primary. Paul Christiano's 2018 essay "Takeoff speeds," the canonical
             modern statement of the continuous case. (The sideways-view page
             returned 403 to the fetch; read via the author's LessWrong crosspost
             and the MIRI discussion that quotes it, both below. Record the essay's
             own address as the source's home.)
Establishes: The operational definition of slow vs fast takeoff, and the
             "incremental progress" argument.
Locators:    Essay body; definition in the opening section.
Quote:       Slow takeoff = "There will be a complete 4 year interval in which
             world output doubles, before the first 1 year interval in which world
             output doubles." (Confirmed identically across the LW crosspost and
             the MIRI transcript.)
Reported:    His mechanism: "it's easier to build a crappier version of something"
             and "a crappier AGI would have almost as big an impact," so weaker
             systems transform the world first and there is no clean discontinuity
             where one system jumps from irrelevant to decisive. He states, against
             intuition, that a slow takeoff may be a "worse scenario than fast
             takeoff in terms of AI risk," because many unaligned systems arrive
             together and aligned ones must compete rather than pre-empt. This last
             point is his own and matters for the article: continuous does not mean
             comforting.
```

```text
URL:         https://www.lesswrong.com/posts/AfGmsjGPXN97kNp57/arguments-about-fast-takeoff
Kind:        primary. Christiano's LessWrong crosspost of the same essay (title
             there: "Arguments about fast takeoff"). Used to read the essay's body
             after the sideways-view 403.
Establishes: Same as the essay above; this is the accessible copy.
Locators:    Post body.
Reported:    Confirms the "crappier version / almost as big an impact" argument
             and the "weaker AI systems will already have radically transformed the
             world" framing, plus the "slow takeoff may be worse for AI risk"
             conclusion.
```

```text
URL:         https://intelligence.org/2021/11/22/yudkowsky-and-christiano-discuss-takeoff-speeds/
Kind:        primary. A recorded 2021 discussion between the two principals; both
             men speak for themselves, so it owns each one's claims directly.
Establishes: The disagreement stated by each side in its sharpest current form,
             and the concrete test between them.
Locators:    Transcript body.
Reported:    Yudkowsky: the precedent set is discontinuity — "humans and chimps,"
             "fission weapons," "AlphaGo" — and GDP is the wrong meter because "the
             World-ending prototype had no prior prototype containing 90% of the
             technology which earned a trillion dollars"; capability can arrive
             before it shows up in output. Christiano: "the model gets better and
             more useful with each doubling ... in a pretty smooth way," and his
             challenge to the fast view is forecast discipline — "you've got to be
             able to say something in advance about what you expect to happen."
             Both concede real uncertainty (Christiano: "I have no idea what
             AlphaFold 2 is good for"; Yudkowsky treats hour-vs-month as secondary
             to the discontinuity itself).
Note:        Reported via page fetch; confirm exact words before quoting. The
             structure of the disagreement (precedent-of-jumps vs
             smoothness-plus-forecasts) is the article's spine and is solid.
```

```text
URL:         https://arxiv.org/abs/2001.08361
Kind:        primary. Kaplan et al., "Scaling Laws for Neural Language Models"
             (2020); the paper owns the scaling-law finding. Abstract read
             verbatim.
Establishes: That model loss is a smooth, predictable power-law function of
             scale — the observed-system backbone of the continuity claim.
Locators:    Abstract.
Quote:       "The loss scales as a power-law with model size, dataset size, and the
             amount of compute used for training, with some trends spanning more
             than seven orders of magnitude."
Paraphrase:  Architecture details (width, depth) matter little across wide ranges;
             the relationships are regular enough to predict optimal
             compute allocation. This is the "smooth function of compute and data"
             the brief asks for, from the paper that owns it. Caveat: the abstract
             does not claim the power law holds forever; it is an empirical fit over
             the observed range, not a law of nature.
```

```text
URL:         https://arxiv.org/abs/2203.15556
Kind:        primary. Hoffmann et al., "Training Compute-Optimal Large Language
             Models" (Chinchilla, 2022). Abstract read verbatim.
Establishes: That the smooth scaling relationship is precise enough to correct a
             field-wide mistake — prior models were undertrained — which is itself
             evidence of forecastability, not discontinuity.
Locators:    Abstract.
Quote:       "for every doubling of model size the number of training tokens should
             also be doubled."
Paraphrase:  Existing large models were "significantly undertrained." Chinchilla
             (70B parameters) trained on more data at the same compute as Gopher
             (280B) "uniformly and significantly outperforms" Gopher and GPT-3
             (175B), reaching 67.5% on MMLU (~7% over Gopher). A four-times-smaller
             model beating a larger one by fixing the data/parameter ratio is the
             continuity case's strongest single data point: capability tracked a
             known quantitative rule, not a lucky architectural jump.
```

```text
URL:         https://arxiv.org/abs/2503.14499
Kind:        primary. Kwa, West, et al. (METR), "Measuring AI Ability to Complete
             Long Software Tasks." Read in full from the PDF (arXiv:2503.14499v4,
             dated 10 Jul 2026). METR owns the measurement.
Establishes: The best recent measured capability trend on real models — and the
             pivot point of the whole argument, because the same number grounds
             both sides.
Locators:    Abstract; Section 3.1; Figure 1; Section 4 and Appendix F/H (limits).
Quote:       "we propose a new metric: 50%-task-completion time horizon, the time
             humans typically take to complete tasks that AI models can complete
             with 50% success rate."
Quote:       "time horizon has doubled every 207 days with a 95% bootstrapped
             confidence interval 166-240 days (roughly plus/minus 19%)."
Quote:       "GPT-2 has a 50% time horizon of only 2 seconds, while o3 has a
             110-minute time horizon and succeeds at several tasks over 4 hours."
Paraphrase:  170 tasks (HCAST, RE-Bench, and the new SWAA short-task suite), 12
             frontier models spanning 2019 to 2025, with skilled human baseliners
             timing the tasks. The 2023-2025 growth rate is "about 20% faster than
             the 2019-2025 rate"; o3 sits above the long-run line (p = 0.006),
             which "may imply the trend in 2024 and early 2025 is faster." METR
             states its own caution: confidence in the 2024-2025-only trend is
             "low because there are only seven frontier models in this time span."
             It flags external validity directly — performance is "much lower on
             less structured, 'messier' tasks," scored against 16 messiness
             factors — so the clean exponential is measured on structured
             software/research tasks, not on the messy distribution of real work.
Note:        This is the article's key "observed system behavior." It supports
             continuity (a smooth six-year exponential) AND feeds the fast
             scenario (extrapolated, it reaches month-long autonomous projects
             within a decade; AI-2027 builds on exactly this). Present it as the
             hinge, not as a win for either side.
```

```text
URL:         https://ai-2027.com/
Kind:        primary. The AI-2027 scenario document; the authors own the forecast.
Establishes: The current, concrete fast-takeoff position — who holds it, what
             they claim, and what they want.
Locators:    Scenario body and "About" material.
Reported:    Authors: Daniel Kokotajlo (former OpenAI, whose Aug-2021 scenario is
             cited as having called chain-of-thought, inference scaling, and chip
             export controls before ChatGPT), Eli Lifland (ranked #1 on the RAND
             Forecasting Initiative leaderboard), Thomas Larsen, Romeo Dean, with
             Scott Alexander on the prose. Core claim: automated AI research drives
             an intelligence explosion — "superhuman coder" (~Mar 2027),
             "superhuman AI researcher" (~Aug 2027), superintelligence (late 2027),
             with an AI-R&D speedup rising ~1.5x -> 3x -> 10x -> 25x and, near the
             peak, "a year passes every week." Compute anchor: GPT-4 at ~2x10^25
             FLOP, a near-future training run at ~10^27 FLOP (~100x). Epistemic
             stance: "AI 2027 is not a recommendation or exhortation. Our goal is
             predictive accuracy," with two endings (a race and a slowdown), a
             stated ~5x-slower-or-faster band, and a Nov-2025 note that 2027 was
             their "modal" year while medians run "somewhat longer."
Note:        This is the modern descendant of Good's one-sentence deduction: the
             engine is still recursive self-improvement, now dated and quantified.
             Its multipliers describe a system that does not exist; its one
             empirical tether is the measured coding-capability trend (METR-style).
             Present the multipliers as the authors' projections, never as
             measurements.
```

```text
URL:         https://www.lesswrong.com/posts/GT8uvxBjidrmM3MCv/superintelligence-6-intelligence-explosion-kinetics
Kind:        secondary. A LessWrong reading-group post (Bostrom-chapter summary)
             used only to source the takeoff timescales and the crossover
             definition when the book's own hosting page was bot-blocked. It
             reports Bostrom; it does not own the claim.
Establishes: Bostrom's three-speed taxonomy and the optimization-power /
             recalcitrance framing, as reported by a reader.
Locators:    Post body (summary of Superintelligence ch. 4).
Reported:    Slow = decades or centuries; moderate = months or years; fast =
             minutes, hours, or days. Rate of intelligence gain = optimization
             power / recalcitrance. "The crossover" = "a point beyond which the
             system's further improvement is mainly driven by the system's own
             actions rather than by work performed upon it by others." A repetition
             of Bostrom, not Bostrom; see the verbatim "slow" definition below.
```

```text
URL:         https://publicism.info/philosophy/superintelligence/5.html
Kind:        primary (Bostrom, Superintelligence ch. 4, "The kinetics of an
             intelligence explosion"). The page itself returned only a bot-check
             loader on repeated fetches, so I could NOT read the chapter body here.
Establishes: Intended source for the verbatim takeoff definitions and the
             decisive-strategic-advantage link.
Locators:    Ch. 4.
Quote:       Slow takeoff, confirmed verbatim via search index: "one that occurs
             over some long temporal interval, such as decades or centuries."
Note:        The "moderate" (months or years) and "fast" (minutes, hours, or days)
             wordings are confirmed in substance by two independent readers (the
             reading-group post above and the Alignment Forum "Distinguishing
             definitions of takeoff" post) but I did not read them verbatim from
             the book. Flag as a gap: if the article quotes moderate/fast, the
             writer must confirm against the book text, not a summary. Bostrom ties
             faster takeoff to a single project plausibly seizing a decisive
             strategic advantage; slow takeoff gives human institutions time to
             react.
```

## Contradictions

The disagreement is the subject, so each contradiction below is the article's
material, not a flaw to resolve.

- Fast vs continuous, at root. Yudkowsky/Good: capability crosses thresholds and
  jumps (evolution, AlphaGo, criticality); recursive self-improvement need not be
  smooth. Christiano/Hanson: capability has been a smooth, forecastable function
  of inputs (scaling laws), and gains are diffuse across many modules and firms,
  so no single project leaps the world. Both are stated here in their authors'
  own terms.

- Which measurement counts. Christiano makes world-output doubling the meter and
  demands advance predictions. Yudkowsky rejects GDP as the meter, arguing
  transformative capability can exist before it registers in output (regulatory
  and deployment lag). This is not a factual dispute they could settle with the
  same data; they disagree on what would even count as evidence. The article
  should name that.

- The METR trend cuts both ways. Read as a straight six-year exponential, it is
  the continuous case's best observed evidence. Extrapolated, and with METR's own
  note of possible recent acceleration, it is the empirical fuel for AI-2027's
  fast scenario. One number, two readings; the honest finding is that observed
  data has not resolved the argument.

- "Continuous" is not "safe," per the continuous camp's own author. Christiano
  argues a slow takeoff may be the harder one to govern. Any implication that the
  continuous case is the reassuring one contradicts its strongest proponent.

- What is shown vs what is analogy (the commission's central question). Shown in
  working systems: smooth neural-scaling (Kaplan; Hoffmann); a measured
  capability trend on 12 real models (METR). Not shown, resting on analogy:
  evolution and AlphaGo as precedents for a discontinuous jump. Not shown,
  resting on a system that does not exist: recursive self-improvement, the
  "superhuman AI researcher," AI-2027's 10x-25x R&D multipliers. The two modern
  fast-takeoff statements (Yudkowsky 2021; AI-2027) both draw their force from
  the analogy-and-projection column, not the observed column.

## Numbers

```text
Figure: 50% task-completion time horizon doubles every 207 days (~7 months)
Owner:  METR, arXiv:2503.14499
Scope:  12 frontier models, 2019-2025; 95% CI 166-240 days (+/-19%)
```

```text
Figure: GPT-2 = 2 seconds; o3 = 110 minutes (50% time horizon), with some tasks over 4 hours
Owner:  METR, arXiv:2503.14499 (v4, 10 Jul 2026)
Scope:  170-task suite (HCAST, RE-Bench, SWAA); human-baselined durations
```

```text
Figure: 2023-2025 horizon growth ~20% faster than the 2019-2025 rate; o3 above trend, p=0.006
Owner:  METR, arXiv:2503.14499
Scope:  Possible acceleration; METR rates its confidence "low" (only 7 models in 2024-2025)
```

```text
Figure: Model loss scales as a power law over "more than seven orders of magnitude"
Owner:  Kaplan et al., arXiv:2001.08361
Scope:  Language-model loss vs model size, dataset size, compute (2020)
```

```text
Figure: Compute-optimal scaling — double the data for every doubling of model size
Owner:  Hoffmann et al., arXiv:2203.15556
Scope:  Chinchilla 70B beats Gopher 280B / GPT-3 175B at equal compute; MMLU 67.5% (~+7% vs Gopher)
```

```text
Figure: AI training compute doubled ~every 3.4 months, 2012-2018
Owner:  Amodei & Hernandez (OpenAI, "AI and Compute"), as cited in METR arXiv:2503.14499
Scope:  Reported secondhand via METR; not independently verified here. Use as context only.
```

```text
Figure: AI-2027 projected AI-R&D speedup ~1.5x -> 3x -> 10x -> 25x; compute GPT-4 ~2e25 FLOP -> ~1e27 FLOP
Owner:  ai-2027.com (Kokotajlo, Lifland, Larsen, Dean, Alexander)
Scope:  Authors' scenario projection, not a measurement; stated ~5x slower-or-faster band
```

```text
Figure: Bostrom takeoff timescales — slow: decades/centuries; moderate: months/years; fast: minutes/hours/days
Owner:  Bostrom, Superintelligence ch. 4
Scope:  Clock time from roughly human-level to strong superintelligence; only "slow" verified verbatim here
```

## Source assets

```text
Asset: METR Figure 1 — 50% time horizon (log scale, minutes/seconds/hours) plotted
       against model release date, 2019-2025, with the fitted exponential and a
       95% CI band, individual models labeled (GPT-2 at ~2s up to o3 at ~110min).
Shows: The single clearest picture in the whole debate: a straight line on a log
       axis over six years. A reader sees at once why the continuity camp points
       to it, and — because the line is climbing steeply — why the fast camp
       extrapolates it to month-long autonomous work within a decade.
Crop:  Keep both axes labeled (log scale must be marked) and keep the model labels
       so the reader can place GPT-2 and o3. Keep the CI band. Do not crop to only
       the recent steep segment; the whole six-year span is the point.
```

```text
Asset: Kaplan et al. Figure 1 — test loss falling as a straight line against
       compute, dataset size, and parameters on log-log axes.
Shows: What "smooth power-law scaling" actually looks like — three panels of
       near-straight lines over many orders of magnitude. Concrete backing for the
       otherwise-abstract "capability is a smooth function of compute" claim.
Crop:  Retain the log-log axis labels and the multi-order-of-magnitude span; the
       straightness over that span is the entire message.
```

```text
Asset: AI-2027 scenario timeline (the site's own milestone chart: superhuman coder
       -> superhuman AI researcher -> superintelligence across 2025-2027).
Shows: How the modern fast case is dated and staged. Useful only if the article
       explicitly frames it as the authors' projection, set beside the METR chart
       so the reader sees projection next to measurement.
Crop:  Must retain any on-figure label identifying it as a forecast/scenario, so it
       is never mistaken for observed data.
```

Good 1965: None found (text-only paper; its evidence is the wording itself,
already quoted).

## Discarded

```text
URL: https://www.overcomingbias.com/p/ai-go-foomhtml — This 2008 post is Hanson
     restating Yudkowsky's pro-foom position to check he understood it, not
     Hanson's own counter-argument. Replaced by "I Still Don't Get Foom" (2014),
     which carries Hanson's actual case.
URL: https://www.overcomingbias.com/p/i-still-dont-get-foomhtml — 404 (wrong slug).
     Correct address is /p/30855html, used above.
URL: https://sideways-view.com/2018/02/24/takeoff-speeds/ — Returned HTTP 403 to
     the fetch (gated, not dead). Recorded as the essay's home; body read via the
     LessWrong crosspost and the MIRI transcript. No content lost.
URL: publicism.info/.../5.html (Bostrom ch. 4) — Served only a bot-check loader on
     repeated fetches. Not discarded as a source (it is the book chapter); recorded
     with the one verbatim definition I could confirm and an explicit gap flag for
     the moderate/fast wordings.
```
