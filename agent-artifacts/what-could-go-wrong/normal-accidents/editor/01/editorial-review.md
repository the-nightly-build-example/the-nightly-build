# Editorial review: what-could-go-wrong/normal-accidents (editor/01)

## Skeptic

The thesis: normal-accident theory names a real failure mode, but only one working
system has actually shown it (the automated stock market), the AI application is
still inference by the proponents' own admission, and the theory resists testing
because its two axes can be reassigned after the fact; the earned verdict is
neither doom nor dismissal, only that keeping AI loosely coupled is cheap
insurance.

The claims it stands on, and how each held:

1. Perrow's mechanism (complex plus tightly coupled systems make catastrophe a
   normal property). Definitions, the four-cell placement table, and the marine
   5-to-10-percent figure all trace to the evidence record and carry their
   sourcing note. The verbatim linear/complex quotation, the placement table, and
   the marine fraction are each attributed through Hopkins 1999; the reclassification
   quotes cite Hopkins (s2). Held.

2. Perrow drew the theory narrowly. The 5-to-10-percent marine figure and the
   exclusion of Bhopal, Chernobyl, Challenger, and the Exxon Valdez as
   component-failure accidents are both on the record and correctly attributed,
   and the piece states plainly that stretching the term to AI failure in general
   claims more ground than Perrow did. This is the bound the brief asked me to
   protect, and the draft protects it. Held.

3. The Flash Crash is the shown case. Every figure (75,000 contracts / $4.1bn,
   9 percent of trailing volume "without regard to price or time," the 20-minute
   execution against a prior five-hour sale, the 27,000-contract hot-potato at
   ~49 percent of volume, sub-1-percent buy-side depth, the five-second CME pause,
   the 10-percent single-stock circuit breaker) matches the CFTC/SEC report as
   the evidence record carries it. The Sarao charge is kept in view honestly, and
   I verified against the CFTC release (s4) that Sarao was a London resident and
   that his conduct "contributed to" the order-book imbalance, so both descriptors
   stand. The mitigation (slack added by design) is kept, which correctly resists
   an inevitability reading. Held.

4. The present-day proponents concede the load-bearing fact. Maas 2018 and
   Bianchi/Cercas Curry/Hovy 2023 are quoted in their own words, including the
   JAIR authors' "AI models are not tightly coupled" and "we do not assume any
   fatal risks in AI anytime soon." The dek compresses this to "the researchers
   aiming it at AI today concede" the coupling is barely wired; Maas actually
   asserts present coupling while calling his own prescriptions "largely
   speculative," so the concession is strongest in Bianchi et al. The body carries
   both positions and the aggregate ("mostly potential") is fair. Held, with the
   Maas/Bianchi tension noted rather than papered over in the body.

5. The HRO steelman. The air-traffic and carrier figures and their hedges
   ("anomalous data, not disconfirmation"; "under positive radar control") are on
   the record. I found one real error here: the prose read "In the five years
   before their study... more than 75 million instances," which states 75 million
   across five years, whereas the primary (via the record) and the article's own
   stat strip both say 75 million per year. Fixed directly to "In each of the five
   years" so prose, furniture, and source agree.

6. The untestability gap. Perrow's post-hoc reclassification of air traffic
   control and carrier decks as "basically linear" and "loosely coupled" is
   attributed to Hopkins (s2) and drives the conclusion that the inevitability
   claim cannot easily be tested. This is the deepest objection and the piece
   lands it. Held.

Display text checked descriptor by descriptor. The headline ("Automated markets
already break the way Perrow warned reactors would") is the piece's most
aggressive line, but it claims the mechanism was demonstrated in markets, not that
markets suffered a reactor-scale catastrophe, and the dek and body keep it honest;
it is the bounded shown-versus-analogy center, not a maximalist reach. Subheads
each name a real step. The `data-nb-kind` labels are defensible: Hopkins is the one
secondary, the two proponents and the HRO paper are primary for their own
arguments, the two regulator documents are primary for the incident. No sentence
implies the Perrow book was read firsthand.

One factual divergence from the evidence record: the draft's illustrative "an
automated benefits denial" where the record established "ration-denial." The JAIR
server was unreachable (repeated 502s) so I could not confirm the source's exact
framing, but the evidence record is the binding claim set, so I aligned the text
to it ("an automated ration denial"). It is one item in a three-example list of
modest harms and load-bearing to nothing; if the writer's source reading framed it
differently, that is a one-word restoration.

## Cut

Three sentences failed the slop and template tests and came out or came down.

- A signpost opened the shown-versus-analogy paragraph: "Here is the line the whole
  argument turns on." It graded the argument's structure rather than continuing it,
  and the two sentences after it carry the line on their own. Cut; the paragraph is
  stronger as a plain two-beat statement, which is exactly the register the voice
  guide's Schneier and Luu passages model for marking a limit.

- The untestability paragraph opened "There is a deeper problem, the one that
  should temper anyone's confidence." The trailing clause is an empty assessment
  naming nothing checkable, and the paragraph's own closing sentence delivers the
  same point more precisely ("the gap where confidence outruns proof"). Trimmed to
  "There is a deeper problem," which keeps the real work the opener does, ranking
  this objection beneath the empirical HRO one.

- The body addressed the reader once, "The nearest related worry the reader has
  met is algorithmic monoculture." The lesson template confines addressing the
  reader to the two bookends; the body speaks to no one. Removed "the reader has
  met"; the in-prose link still carries that it is a prior lesson.

No em-dashes (count already zero). Punctuation is clean: the colons all introduce
a promised payoff or list, and I found no comma splice. No borrowed phrasing from
the voice-guide quotations. No prompt leakage: the "confidence outruns proof" and
"neither doom nor dismissal" framings echo the series prompt in words but the piece
earns both from the reclassification evidence, so they are the article's own, not
lifted instructions. On the recent-pattern notes: no "What <Person> saw in <place>"
opener, no colon-subtitle or terse-rebuttal headline, no comma-triad dek, and no
banned dek mold. One heading joins two clauses with "and" ("The systems that run
safely, and the measure the theory lacks"); it is the only one, the section
genuinely makes two moves, and it does not echo a flagged recent pattern, so I left
it.

## Reader

Read straight through, the piece gives what no single source does: the explicit
line between the coupled-automation cascade that is on the record and the AI
catastrophe that is not, the diagnosis that Perrow's terms have no measure
independent of the outcomes they explain, and a verdict (keep AI loosely coupled as
cheap insurance, distrust both inevitability and dismissal) that the evidence
record itself never states. The draft-handoff's original-work sentence claims
exactly this synthesis, and it survives. The prose sits closer to the voice-guide
exemplars than to a median AI summary: it states each abstraction plainly and
grounds it in a worked case, and it marks its own limits in the same level voice it
uses for the evidence. The headline, read last as the largest claim, is defended by
the body.

## Edits

- "In the five years before their study... 75 million instances" changed to "In
  each of the five years before their study" so the air-traffic figure's period
  matches the primary and the article's own stat strip.
- Cut the signpost sentence "Here is the line the whole argument turns on."
- Trimmed "There is a deeper problem, the one that should temper anyone's
  confidence." to "There is a deeper problem."
- Removed the reader-gesture: "The nearest related worry the reader has met is" to
  "The nearest related worry is".
- Aligned the illustrative example "an automated benefits denial" to the evidence
  record's wording, "an automated ration denial".

## Required work

None blocking. Two notes for the orchestrator, neither a routed item:

- Re-stamp and re-prove after these prose cuts (net roughly eighteen words removed;
  still inside the length band).
- The "ration denial" example is now faithful to the evidence record but was not
  confirmable against the JAIR source during this pass (server 502). If the writer
  reads the source and it frames that example differently, it is a one-word
  restoration, not a re-report.

## Decision

approve. The sourcing caveat holds, the argument stays bounded, and the one real
error (the air-traffic figure's period) plus the slop and template lapses were all
fixable directly.
