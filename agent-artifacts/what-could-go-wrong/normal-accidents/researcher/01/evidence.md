# Evidence record: what-could-go-wrong/normal-accidents (01)

The evidence firmly supports the three moves the commission asks for. It carries
Charles Perrow's two axes and his classification in his own definitional wording
(complex versus linear interactions; tight versus loose coupling), the argument
that in a system with both properties a catastrophic accident is a normal
property rather than a fault; one incident that shows tightly coupled automated
failure running faster than any human could intervene, drawn from the regulators'
own reconstruction (the May 6, 2010 Flash Crash); the strongest primary statement
of the High Reliability Organization objection, from the Berkeley researchers who
built it, including two operational records of complex, tightly coupled systems
run with almost no catastrophic failure; and present-day authors who carry
Perrow's lens onto AI in their own words, with the specific interventions they
propose. It is thin, and honestly so, on the one thing the commission most wants
policed: no source shows a catastrophic "normal accident" in a deployed AI
system. The proponents themselves say the tight coupling is mostly potential, not
yet built, and that the catastrophe is inference. The record is also weakened by
one access failure worth stating plainly up front: Perrow's book itself
(*Normal Accidents*, 1984 / 1999) is gated behind lending and paywall on every
route tried, so his exact Chapter 3 wording and the placement chart were read
through his own 2011 article and through a peer-reviewed critique that quotes him
verbatim with page numbers, not off the book's own pages. Where that matters is
flagged in each entry.

A second finding cuts against a naive use of the theory and belongs in front of
the writer: Perrow drew the boundary of his own theory very tightly. He held that
most disasters are *not* system accidents, and named Bhopal, Chernobyl,
Challenger, and the Exxon Valdez as ordinary component-failure accidents outside
it. A piece that stretches "normal accident" to cover AI failure in general is
using the term more loosely than its author did.

## Sources

```text
URL:         https://www.sec.gov/news/studies/2010/marketevents-report.pdf
Kind:        Primary. The reconstruction is the regulators' own: staff of the
             CFTC and SEC assembled the trade-level record and interviewed the
             firms. It owns the account of what happened on May 6, 2010.
Establishes: The one incident the commission can show rather than assert: a
             tightly coupled, automated failure that ran faster than human
             intervention and cascaded across coupled markets, then recovered.
Paraphrase:  At 2:32 p.m. a single large fundamental trader (a mutual fund
             complex) began selling 75,000 E-Mini S&P 500 futures contracts,
             about $4.1 billion, as a hedge, using an automated Sell Algorithm
             set to target 9% of the trailing one-minute trading volume "without
             regard to price or time." On a prior occasion a comparable sale had
             taken more than five hours; on May 6, into an already stressed
             market, the volume-only algorithm executed in about 20 minutes.
             High-frequency traders first absorbed the sell orders, then, holding
             unwanted inventory, sold to each other, "generating a 'hot-potato'
             volume effect": between 2:45:13 and 2:45:27 HFTs traded over 27,000
             contracts, about 49% of volume, while buying only about 200 net.
             Buy-side depth in the E-Mini fell to about $58 million, under 1% of
             the morning's. The CME's Stop Logic Functionality paused E-Mini
             trading for five seconds at 2:45:28, after which prices recovered.
             The report's stated lesson: "the interaction between automated
             execution programs and algorithmic trading strategies can quickly
             erode liquidity and result in disorderly markets," and "high trading
             volume is not necessarily a reliable indicator of market liquidity."
             The staff response was to add slack to the coupling: single-stock
             circuit breakers (a five-minute pause on a 10% move within five
             minutes) and clearer trade-break rules.
Locators:    Executive Summary, pp. 1-8 (PDF pp. 4-11). Trigger and $4.1bn:
             p. 2. 20-minute execution: p. 2, and note 7. Hot-potato and $58m
             depth: p. 3. CME five-second pause: p. 3. Lessons and circuit
             breakers: pp. 6-7. Attribution caveat: cover page ("The Commissions
             have expressed no view regarding the analysis, findings or
             conclusions contained herein").
Quote:       "This large fundamental trader chose to execute this sell program
             via an automated execution algorithm ('Sell Algorithm') that was
             programmed to feed orders into the June 2010 E-Mini market to target
             an execution rate set to 9% of the trading volume calculated over
             the previous minute, but without regard to price or time." (p. 2)
```

```text
URL:         https://www.cftc.gov/PressRoom/PressReleases/7156-15
Kind:        Primary. The CFTC is the charging party and owns the allegation.
Establishes: That the same regulator later attributed a contributing role in the
             Flash Crash to deliberate manipulation, which complicates using the
             day as a clean "well-behaved parts" accident with no bad actor.
Paraphrase:  On April 21, 2015 the CFTC charged Navinder Singh Sarao and Nav
             Sarao Futures Limited PLC with price manipulation and spoofing in
             the E-Mini S&P 500, alleging a "dynamic layering" scheme of large
             resting sell orders he did not intend to execute, and that his
             conduct on May 6, 2010 "contributed to" the order-book imbalance
             behind the Flash Crash. The verb is "contributed to," not "caused";
             it does not displace the 2010 report's account of the Sell
             Algorithm as trigger, but it adds an intentional actor to the day.
Locators:    CFTC Press Release PR7156-15, headline and body.
Quote:       Charges of "Price Manipulation and Spoofing"; conduct that
             "contributed to" the Flash Crash market conditions.
```

```text
URL:         https://press.princeton.edu/books/paperback/9780691004129/normal-accidents
Kind:        Primary, and the owner of the definitions and the classification.
             By Charles Perrow, sociologist, Yale University; first published by
             Basic Books in 1984, updated edition Princeton University Press 1999,
             written after the 1979 Three Mile Island accident.
             ACCESS-LIMITED: the book's full text could not be opened on any
             route tried (Internet Archive lending, De Gruyter, SAGE, Scribd,
             Google Books, HathiTrust all gated). The wording below was read
             through Hopkins 1999 (which quotes Perrow verbatim with page
             numbers) and cross-checked against the JAIR viewpoint's restatement
             and Perrow's own 2011 article. Cite the book as owner; treat the
             page numbers as Hopkins reports them.
Establishes: The two axes, the definition of a normal/system accident, and the
             placement of systems, in Perrow's own terms.
Paraphrase:  A normal (or system) accident is one involving the "unanticipated
             interaction of multiple failures" in a system running a high-risk
             technology (p. 70), as against a component-failure accident, where
             one part fails in a predictable way. Systems vary on two axes.
             Interactions are linear or complex; coupling is tight or loose. A
             system is tightly coupled when one thing follows rapidly and almost
             invariably from another, with little slack and little chance for a
             human to intervene before the fault propagates. Where a system is
             both complex and tightly coupled, and runs a high-risk technology,
             Perrow argues a catastrophic accident is inevitable over time.
             Perrow places systems in a four-cell space (p. 97, Figure 3.1):
             nuclear plants, chemical plants, aircraft/airways, space missions,
             and nuclear weapons systems in the complex-and-tight cell; dams and
             rail transport tightly coupled but linear; universities and R&D
             firms complex but loosely coupled; most manufacturing and the post
             office linear and loosely coupled.
Locators:    Ch. 3 "Complexity, Coupling, and Catastrophe." System-accident
             definition p. 70; complex/linear definition p. 78; four-cell chart
             p. 97 (Fig. 3.1); marine-collision fraction p. 175.
Quote:       "Linear interactions are those in expected and familiar production
             or maintenance sequence, and those that are quite visible even if
             unplanned. Complex interactions are those of unfamiliar sequences,
             or unplanned and unexpected sequences, and either not visible or not
             immediately comprehensible." (Perrow 1984, p. 78, as quoted in
             Hopkins 1999.)
```

```text
URL:         https://thebulletin.org/2011/12/fukushima-and-the-inevitability-of-accidents/
Kind:        Primary. Perrow is the author. Read via the free web excerpt
             (Stanford CISAC copy of the same text); the excerpt is the article's
             first section only, "Regulations." The full article ran in Bulletin
             of the Atomic Scientists 67(6):44-52.
Establishes: Perrow in his own late voice on how he reads catastrophe: as
             ordinary rather than exotic, and turning as much on power and
             captured regulation as on engineering.
Paraphrase:  Fukushima "replicates the bullet points of most recent industrial
             disasters" and is "prosaic, even." There will always be failures of
             design, components, procedures, operator error, and unexpected
             conditions; regulation, warnings, and preparedness reduce but cannot
             eliminate catastrophe. Because the possibility never leaves, "it is
             important to ask whether some industrial systems have such huge
             catastrophic potential that they should not be allowed to exist."
             He documents regulatory capture (the "nuclear power village" in
             Japan; the NRC cutting inspections after Senator Domenici's budget
             threat; OSHA clearing the Union Carbide plant at Institute, West
             Virginia, months before an accident there echoing Bhopal).
Locators:    "Fukushima and the inevitability of accidents," Bulletin of the
             Atomic Scientists, 1 December 2011 (web excerpt), section
             "Regulations."
Quote:       "it is important to ask whether some industrial systems have such
             huge catastrophic potential that they should not be allowed to
             exist."
```

```text
URL:         https://academic.oup.com/jpart/article-abstract/1/1/19/978459
Kind:        Primary for the High Reliability Organization objection. Todd R. La
             Porte (Professor of Political Science, UC Berkeley) and Paula M.
             Consolini were core members of the Berkeley HRO Project; they report
             their own field research. Open copy read at polisci.berkeley.edu.
Establishes: The steelman: complex, tightly coupled, high-hazard systems that in
             fact run with almost no catastrophic failure, which is the direct
             empirical challenge to Perrow's inevitability claim.
Paraphrase:  The project studied the FAA air-traffic control system, two U.S.
             Navy nuclear aircraft carriers (USS Carl Vinson and Enterprise), and
             Pacific Gas and Electric's electric power system including its
             nuclear station. These "operate tightly coupled, complex, and highly
             interdependent technologies" yet attain very high reliability. Air
             traffic control handled "over 75 million instances per year in which
             a controller handled an aircraft across an air space" over the prior
             five years "with no instances of a midair collision when both
             aircraft were under positive radar control." A carrier's six-month
             deployment saw "over 16,000 arrested landings with no deck
             accidents," at a "crunch rate" (two aircraft touching) of about one
             in 7,000 moves. They cite Perrow (1984) directly as the perspective
             their data sit awkwardly against, and frame their finding "in the
             spirit of discovering anomalous data rather than theory
             disconfirmation." They attribute the reliability to features such as
             "nested authority structures" in which authority devolves to
             frontline operators at peak stress, which is the mechanism Perrow's
             centralize-versus-decentralize dilemma says cannot coexist.
Locators:    J-PART 1(1):19-48 (Jan. 1991). Systems studied and the ATC and
             carrier figures: pp. 20-22. High-hazard/low-risk and near-failure-
             free definition: p. 24. Nested authority: pp. 31-32 (per Hopkins).
             Note: the ATC figure is credited in the paper to La Porte 1988.
Quote:       "no instances of a midair collision when both aircraft were under
             positive radar control." (The qualifier "under positive radar
             control" bounds the claim and should be kept.)
```

```text
URL:         https://openresearch-repository.anu.edu.au/items/c9046717-d06d-4e99-8a77-d468c025df4f
Kind:        Secondary. Andrew Hopkins (sociologist, Australian National
             University) analyzes and criticizes Perrow. He is outside the
             authoring party, so this reports on the theory; but he quotes Perrow
             verbatim with page numbers, which is how the book's definitions were
             recovered here. Canonical: Safety Science 32(2-3):93-102 (1999),
             doi:10.1016/S0925-7535(99)00015-6.
Establishes: The contradiction the editor will push on: the theory covers a
             small, ill-defined class, its central terms lack an independent
             measure, and it may be wrong about inevitability.
Paraphrase:  Perrow's own scope is narrow: only 5-10% of the marine collisions in
             his longest chapter are system accidents (Perrow 1984, p. 175); the
             rest are component-failure accidents. Bhopal, Chernobyl, Challenger,
             and the Exxon Valdez are, in Perrow's later words, "component failure
             accidents," "alarmingly banal examples of organisational elites not
             trying very hard" (Perrow 1994, p. 218 and p. 28), not normal
             accidents. Complexity and coupling have no measure independent of the
             outcome they explain, which lets classification move to fit the
             result: Perrow calls the military early-warning system "moderately
             complex and coupled, but not disastrously so" (p. 291), and, against
             the HRO researchers, reclassifies air traffic control as "basically
             a linear system" and carrier flight operations as "basically linear"
             and "loosely coupled" (Perrow 1994, p. 216) rather than concede they
             are complex, tightly coupled systems run safely. Hopkins argues the
             HRO finding of "nested" centralized-and-decentralized authority, if
             real, removes the logical basis for inevitability.
Locators:    Hopkins 1999, throughout; Perrow page numbers as cited by Hopkins.
Quote:       "It is not a theory of disasters in general but only of a very
             small, and furthermore ill-defined subset of disasters or near
             disasters... it does not apply to many of the best-known disasters."
```

```text
URL:         https://doi.org/10.1145/3278721.3278766
Kind:        Primary for a present-day proponent's own argument. Matthijs M. Maas
             (then Faculty of Law, University of Copenhagen; Research Affiliate,
             Governance of AI Program, Future of Humanity Institute, Oxford).
             Read the author's hosted PDF and the ACM record.
Establishes: The clearest present-day application of Perrow to AI, and the
             specific interventions a proponent proposes, in his words.
Paraphrase:  "even narrow AI applications often involve networked (tightly
             coupled, opaque) systems operating in complex or competitive
             environments," so they are "prone to 'normal accident'-type failures
             which can cascade rapidly, and are hard to contain or even detect in
             time." Maas argues AI "may be even more susceptible to normal
             accidents than past 'textbook' case technologies such as nuclear
             power or aviation," and draws the direct bridge to the shown case: a
             military "'flash war'... analogous to the algorithmic flash crashes
             observed in the financial sector." His proposals target the "levers"
             of normal-accident risk: reduce opacity (explainable architectures),
             "promote heterogeneity in deployed AI architectures or cap
             unnecessary integration with networks (i.e. reduce 'coupling' &
             'complexity'), to insulate systems from flash crashes," restrict a
             system's autonomy and speed in competitive settings, and treat a
             human-in-the-loop not as a reliable fail-safe but as a possible
             "moral crumple zone." He marks his own uncertainty: "There are, as of
             yet, no clear-cut answers to the question of how to 'prevent' normal
             accidents. The following is therefore largely speculative."
Locators:    AIES'18 proceedings, pp. 223-228. Thesis: Abstract and section 1.
             "Flash war": section 3. Levers and recommendations: section 4.
             "largely speculative": section 4.
Quote:       "Like all tightly coupled, opaque systems, AIs will be prone to
             'normal accidents', ensuring that perfect safety may not be
             attainable."
```

```text
URL:         https://jair.org/index.php/jair/article/view/14263
Kind:        Primary for present-day proponents' own argument. Federico Bianchi
             (Stanford University), Amanda Cercas Curry and Dirk Hovy (Bocconi
             University). Open access; read in full.
Establishes: A second, more recent application, and, more usefully, proponents
             drawing the shown-versus-potential line themselves.
Paraphrase:  The authors "apply and extend Perrow's framework to AI" and argue
             "it is only a matter of time" before a normal accident occurs under
             the current paradigm. They restate the two axes and add two of their
             own (an "ACCI" scheme: Availability, Complexity, Coupling,
             Incompleteness). Crucially they concede the coupling is not yet
             built: "Currently, AI models are not tightly coupled: Few systems
             pipe models together," though "the potential for tighter coupling is
             high." They disclaim near-term catastrophe: "we do not assume any
             fatal risks in AI anytime soon," and "current AI systems are unlikely
             to cause severe destruction or death." Their worked examples of AI
             gone wrong are modest, not catastrophic (an automated ration-denial,
             UK exam-grading, a mistranslation, an Alexa mis-order). Their
             prescription mirrors Maas: keep coupling low, e.g. a confirmation
             screen between a language model and a car's controls.
Locators:    JAIR 76:193-199 (2023). Framework and Figure 1: section 2. "not
             tightly coupled": section 2.2. Disclaimers: section 1 and abstract.
Quote:       "Currently, AI models are not tightly coupled: Few systems pipe
             models together."
```

```text
URL:         https://arxiv.org/abs/2503.00237
Kind:        Primary for a present-day systems-safety framing, though not Perrow
             specifically. Position paper by an IBM Research group (Miehling,
             Natesan Ramamurthy, Varshney, Riemer, and others). Read in full.
Establishes: That the systems-lens argument is live for agentic AI now, phrased
             as emergence from interaction rather than from any single model.
Paraphrase:  Their position: "the current development of agentic AI requires a
             more holistic, systems-theoretic perspective in order to fully
             understand their capabilities and mitigate any emergent risks,"
             because development is "overly focused on individual model
             capabilities, often ignoring broader emergent behavior," which leads
             to underestimating risk. Advanced behavior "can emerge from
             (comparably simpler) agents simply due to their interaction with the
             environment and other agents." Useful as a datestamp on the present
             conversation, but it invokes systems theory in general, not normal-
             accident theory by name; use it to show the lens is current, not to
             carry a Perrow-specific claim.
Locators:    arXiv:2503.00237 (2025), Abstract and section 1.
Quote:       "a systems-level perspective is essential for better understanding,
             and purposefully shaping, agentic AI systems."
```

## Contradictions

- The demonstrated case is not a clean "well-behaved parts, no bad actor"
  accident. The 2010 staff report attributes the trigger to an automated Sell
  Algorithm (structural), but in 2015 the CFTC charged Navinder Sarao with
  manipulation and spoofing that "contributed to" the same day. The commission's
  claim that normal-accident theory "does not need a misaligned goal" survives at
  the level of the mechanism (the cascade was structural), but the writer must
  not present the Flash Crash as free of intentional misconduct.

- The demonstrated case recovered and was mitigated. Prices reverted within about
  twenty minutes, a five-second CME pause halted the E-Mini cascade, and
  regulators then added single-stock circuit breakers and clearer trade-break
  rules. The same incident that shows tight coupling running faster than humans
  also shows a tightly coupled system being given slack by design afterward. This
  cuts toward the HRO side and against a reading of inevitability.

- Perrow limits his own theory more than most who invoke it. He classifies most
  disasters, including Bhopal, Chernobyl, Challenger, and the Exxon Valdez, as
  ordinary component-failure accidents outside normal-accident theory. A piece
  that treats "normal accident" as a general account of how AI could go wrong
  claims more territory than Perrow did.

- The central terms may not be independently measurable. Perrow reclassified air
  traffic control and carrier operations as "linear" and "loosely coupled" once
  HRO researchers pointed to them as complex, tightly coupled systems run safely.
  If complexity and coupling can be reassigned to fit the outcome, then "AI is
  complex and tightly coupled, therefore catastrophe is inevitable" is difficult
  to test. This is the deepest objection to the AI application and the editor's
  likely pressure point.

- Complex, tightly coupled systems demonstrably can be run with near-zero
  catastrophic failure: the HRO record (air traffic control with no midair
  collision under positive radar control across 75 million-plus handoffs a year;
  carrier decks at 16,000-plus arrested landings without a deck accident). The
  HRO authors themselves hedge (they call it "anomalous data," not
  disconfirmation), and the ATC claim is bounded by "under positive radar
  control." The evidence for safe operation is real and also qualified.

- The AI proponents concede the load-bearing fact. Both Maas and the JAIR authors
  say the tight coupling among AI systems is mostly potential, not yet built, and
  disclaim near-term catastrophe. The commissioned angle is not undermined by
  this; it is confirmed by it. The gap between demonstrated coupled-automation
  failure and catastrophic AI normal accidents is one the proponents draw
  themselves.

## Numbers

```text
Figure: 75,000 E-Mini S&P 500 contracts, about $4.1 billion, sold via automated algorithm
Owner:  CFTC/SEC staff, Findings Regarding the Market Events of May 6, 2010, p. 2
Scope:  One large fundamental trader's sell program beginning 2:32 p.m. on May 6, 2010
```
```text
Figure: Sell Algorithm targeted 9% of trailing one-minute volume, "without regard to price or time"
Owner:  CFTC/SEC staff report, p. 2
Scope:  The program's execution parameter on May 6, 2010
```
```text
Figure: about 20 minutes to execute, versus more than 5 hours for a comparable prior sale
Owner:  CFTC/SEC staff report, p. 2 and note 7
Scope:  Execution time of the May 6 sell program vs. an earlier one by the same trader
```
```text
Figure: HFTs traded over 27,000 contracts (about 49% of volume) in 14 seconds while buying only ~200 net
Owner:  CFTC/SEC staff report, p. 3
Scope:  The "hot-potato" effect, 2:45:13-2:45:27 p.m., May 6, 2010
```
```text
Figure: E-Mini buy-side depth fell to about $58 million, under 1% of the morning level
Owner:  CFTC/SEC staff report, p. 3
Scope:  Near the 2:45 p.m. low, May 6, 2010
```
```text
Figure: over 20,000 trades across more than 300 securities executed 60%+ away from 2:40 p.m. prices, then broken
Owner:  CFTC/SEC staff report, pp. 1 and 5-6
Scope:  2:40-3:00 p.m. window, May 6, 2010; trades later cancelled as clearly erroneous
```
```text
Figure: single-stock circuit breaker pauses trading 5 minutes on a 10% move within 5 minutes
Owner:  CFTC/SEC staff report, pp. 6-7
Scope:  The post-crash mitigation; S&P 500 names from June 10, 2010, Russell 1000 and some ETFs from Sept 10, 2010
```
```text
Figure: over 75 million controller-aircraft handoffs per year, no midair collision under positive radar control
Owner:  La Porte and Consolini 1991, p. 21 (ATC figure credited to La Porte 1988)
Scope:  U.S. air traffic control, the five years preceding the study
```
```text
Figure: over 16,000 arrested landings with no deck accidents; "crunch rate" ~1 in 7,000 moves
Owner:  La Porte and Consolini 1991, pp. 20-21
Scope:  A single U.S. Navy carrier's six-month deployment
```
```text
Figure: only 5-10% of the marine collisions Perrow studied were system accidents
Owner:  Perrow 1984, p. 175 (read via Hopkins 1999)
Scope:  Perrow's longest chapter, on marine accidents; the rest are component-failure accidents
```
```text
Figure: GPT-3 has 175 billion parameters, offered as evidence of AI's complexity/opacity
Owner:  Bianchi, Cercas Curry, and Hovy 2023, section 1 (citing Brown et al. 2020)
Scope:  Used illustratively by the proponents; the parameter count is owned by Brown et al. 2020
```

## Source assets

```text
Asset: Figure 3.1, the interaction/coupling chart, in Perrow 1984 (Ch. 3, p. 97)
Shows: Perrow's own placement of systems in the four-cell space, with nuclear
       plants, chemical plants, aircraft, space missions, and nuclear weapons in
       the complex-and-tightly-coupled corner. The single clearest picture of the
       theory's classification.
Crop:  Reproduction is rights-restricted and the original could not be opened
       here; do not lift the scanned figure. If a chart is wanted, the honest
       route is an original redraw of the two axes with a few labeled systems,
       cited to Perrow 1984 p. 97, not a copy of his figure.
```
```text
Asset: Figure 1 in Bianchi, Cercas Curry, and Hovy 2023 (JAIR, section 2)
Shows: The proponents' redrawn coupling/interaction diagram with "Current AI"
       placed low on coupling and "Future AI Models" pushed toward the complex,
       tightly coupled corner. It visualizes the shown-versus-potential line the
       commission wants, and the arrow is the proponents' own inference.
Crop:  Open-access figure; if used, keep the distinction between the plotted
       existing technologies and the authors' added AI points, since the AI
       placement is argued, not measured.
```
```text
Asset: The E-Mini price-and-liquidity reconstructions in the CFTC/SEC report
       (Section I and the order-book charts, Section IV)
Shows: Price collapsing as buy-side depth vanishes within seconds, which is the
       coupling-runs-faster-than-humans point in one image.
Crop:  A single security's order-book panel carries it; retain the timestamp axis
       and the depth scale, and cite the report and page.
```

## Discarded

```text
URL: https://people.ohio.edu/piccard/entropy/perrow.html — a course review that paraphrases Perrow's chart; secondary to a secondary, superseded by Hopkins' verbatim quotation with page numbers.
URL: https://en.wikipedia.org/wiki/Normal_Accidents and /wiki/System_accident — tertiary; useful only to confirm the definitional wording found in primaries, not citable.
URL: https://medium.com/@qhsestandard/... — blog restatement; no independent authority.
URL: https://www.degruyterbrill.com/document/doi/10.1515/9781400828494-005/pdf — Perrow's Ch. 3 itself, but paywalled (HTTP 403/405); recorded as the access failure, not as a read source.
URL: https://journals.sagepub.com/doi/full/10.1177/0096340211426395 — full Perrow Fukushima article, paywalled (403); only the free excerpt was read.
URL: https://archive.org/details/normalaccidentsl00perr — the book, lending-restricted; OCR text marked private, search-inside gated. The access failure, not a source.
URL: https://arxiv.org/abs/2606.13474 (systems-thinking approaches to loss-of-control risk) and https://arxiv.org/abs/2512.17600 (STAMP/STPA and AI loss of control) — read enough to see they apply systems-safety, not Perrow's normal-accident theory specifically; the two proponent sources above cover the commissioned lens more directly. Available if the writer wants the very latest systems-safety framing.
```
