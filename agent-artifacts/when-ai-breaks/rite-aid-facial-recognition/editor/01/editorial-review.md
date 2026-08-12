# Editorial review: when-ai-breaks/rite-aid-facial-recognition (editor/01)

## Skeptic

Thesis: a facial-recognition watchlist that scans a whole crowd to find a few
rare targets produces mostly false accusations however accurate the matcher is
(the base-rate problem), those false accusations fall hardest on the groups a
skewed matcher misreads most, and Rite Aid is the clearest recorded case, shut
down by a 2023 FTC consent order.

The claims it stands on, and how each held:

- **Rite Aid ran a facial-recognition watchlist on entering shoppers, 2012 to
  2020, in hundreds of stores.** Held. The existence and scale are not FTC-only:
  Reuters independently documented ~200 stores from its own store visits and
  document review, and the article attributes the "hundreds" to the FTC and the
  "~200" to Reuters separately. The mechanism detail (enrollment database,
  confidence threshold, "Approach and Identify" alert) is correctly fenced with
  "Here is how the FTC says it worked" and the blanket "Treat the specifics that
  follow as the agency's charges, not a court's findings."

- **The false matches led employees to follow, stop, search, accuse, and eject
  innocent shoppers.** Held as allegation. The section opens "By the FTC's
  account," the two specific stops (the 11-year-old girl; the Black woman matched
  to an enrollment employees themselves logged as "a white lady with blonde
  hair") are introduced with "The complaint describes specific stops" and closed
  with "These accounts come only from the FTC. Rite Aid did not admit them." The
  11-year-old, which the round focus flagged as FTC-only, is handled exactly
  right. Every figure I checked matches the evidence record's paragraph locators
  (¶91 minor; ¶48 white-lady; ¶31 the 900-alerts/5-days and 5,000+ / 100-miles
  counts; ¶82 two-thirds unresolved; ¶23 tens of thousands enrolled).

- **The base-rate mechanism: rare target in a huge stream of faces yields mostly
  false alerts even from an accurate matcher.** Held, and marked illustrative in
  the prose, not only the caption ("Work it through with round, illustrative
  numbers, since Rite Aid never measured the real one"). I recomputed the worked
  figures: at a per-comparison false-match rate of 1 in 100,000 against 10,000
  enrolled faces, the chance one innocent shopper is flagged is 1 - (1 -
  0.00001)^10000 ~= 0.095, i.e. "about one in ten"; 1,000 shoppers -> ~95 false
  alerts ("roughly a hundred"); ~100 false to ~1 true -> "~99%" false share. All
  correct. The only real number, the NIST FMR benchmark, is anchored as "the kind
  of benchmark NIST uses," not as Rite Aid's measured rate. The table caption
  repeats the illustrative label. This is the piece's original work and it is
  sound.

- **Demographic skew.** Held at honest strength, which is the claim the round
  focus said to push hardest on. The article states NIST measured skew across 189
  algorithms "often by factors of 10 to more than 100" but "not in every
  algorithm: a few systems it tested showed no such gap at all," names Rite Aid's
  own demographic evidence as "circumstantial" (siting, low-confidence-score
  proxies), and lands on the exact honest construction the brief demanded: "NIST
  did not prove that Rite Aid misread Black or women shoppers by any particular
  factor. But demographic skew in false matches is real and often large. Rite Aid
  never checked which kind of system it had." No sentence reads as "NIST proved
  Rite Aid misread groups by 10-to-100x." No NIST figure is used as a source
  asset, so the Figure 26-without-27 crop hazard does not arise.

- **The FTC banned it for five years on a consent order without admission.** Held.
  The order terms (five-year prohibition, deletion under oath, pre-deployment
  accuracy and demographic testing) match the evidence record, and the settlement
  posture is stated plainly: "Rite Aid 'neither admit[ted] nor den[ied]' the
  FTC's claims, and the order was entered while the company was in Chapter 11."
  Rite Aid's own position is present in its own words via the position card ("We
  fundamentally disagree..."), and the two contested Rite Aid claims (pilot;
  voluntary shutdown) are weighed against independent Reuters evidence, not merely
  asserted against.

Display text: headline, dek, and all five section subheads verified descriptor by
descriptor. Dek facts (2012-2020, hundreds of stores, watchlist of suspected
shoplifters, 2023 FTC order, five years) all check; the dek adds to the headline
rather than restating it, and is built like neither banned when-ai-breaks mold.
Levine's title ("consumer-protection director") matches the record. The headline's
"scanned every shopper's face" runs slightly ahead of the body's "nearly every
customer," but describes the design accurately (indiscriminate scanning of
entering shoppers) and is within headline compression, not a material false
label; I left it.

data-nb-kind audit (against the authorship-and-stake test in nb-researcher):
FTC press release, complaint, and order are three distinct primary FTC documents;
NIST 8280 is primary for its measurements; Rite Aid's statement is primary for its
position; CNN and NBC are secondary. Reuters is labeled primary; the article cites
it only for Reuters' own firsthand investigation (its store-visit counts, its own
statistical analysis of siting), which Reuters authors and owns, so primary is
correct for the use even though the brief's shorthand called it "the independent
secondary." The label hides no missing source: both floors (>=4 primary, >=1
secondary) are met with margin regardless. No mislabel found. See the source-floor
ruling below for the s5/s6 shared-URL question.

Citations spot-checked to the evidence record's paragraph locators; all supported.
The CNN URL (s5/s6) returned HTTP 451 to this session (a legal-reasons egress gate,
not a dead link); the researcher read it and recorded Rite Aid's verbatim quotes,
and the writer's proof passed link-checking, so it resolves.

## Cut

The piece is already tight and in the voice-guide register (Joyce's plain counts
in the base-rate walk; Kirchner-Goldstein's attributed, held-apart contested
account in the pilot/shutdown dispute; Campbell's step-by-step mechanism build).
The dedicated slop pass found no sentence that fails the placeholder test: the
edge sentences all carry a fact or a reasoning step. I tested the highest-risk
edges specifically.

- The article's last sentence, "A watchlist at the door does not have to be broken
  to do harm. It only has to be pointed at a crowd," is a negative construction,
  but the misconception it corrects (that a system must malfunction to cause harm)
  is the lesson's entire earned point, so it survives as the rare earned contrast
  and states the conclusion the argument built. Kept.
- "Two of those claims sit badly with the record" is a light topic sentence, but
  it introduces a genuine, evidence-grounded contradiction rather than grading the
  piece. Kept.
- The where-now section's "property of the setup, not of Rite Aid" is an earned
  contrast (the lesson's structural claim), not reflex parallelism. Kept.

No formula against the recent-pattern notes survived: the opener does not open on
nostalgic/second-person recall or "This lesson follows/tells"; it does not close
on a "set the two things side by side" line; the takeaway does not land on a "So
next time you..." portable rule; the body carries no "this desk" or self-reference
(the two bookend cards are the template-allowed exception, and each says something
specific to this lesson). No prompt leakage: the where-now examples render the
commission's "retail, venues, and policing" as the article's own concrete nouns
rather than lifting phrasing. Punctuation is clean; no reflex em-dashes. Grammar
holds throughout, including display text and furniture prose.

One direct edit (below): I converted an unlinked signpost sentence ("A separate
lesson covers the government testing in detail") into the house-standard inline
link to the already-published `facial-recognition-wrongful-arrest` lesson, which
removes a mild self-referential signpost and satisfies the press rule to link the
earlier lesson in prose at first use rather than gesture at it.

Furniture (stat strip, position card, illustrative table, vendor-disclaimer note):
each carries distinct load across a 2,200-word piece and none reads as a stack of
blocks. No component added or removed. No chart is warranted (no verified Rite-Aid
numeric series exists, and the NIST figure asset is the flagged crop hazard).

## Reader

What the piece gives beyond its sources: a single worked, explicitly-illustrative
base-rate calculation that makes a reader feel why "usually right on every
comparison" and "wrong on almost every alert" are both true at once, then layers
demographic skew onto it at exactly the strength the record supports and no
further. The evidence record deliberately does not assemble this (it flags the
base-rate mechanism as "thin quantitatively"); the lesson builds it. The
original-work sentence in the draft handoff matches what the article actually does.
The prose sits closer to the voice-guide exemplars than to a median AI summary.
The headline, reread as the largest claim, is defended by the body.

## Edits

- Replaced the unlinked signpost sentence "A separate lesson covers the government
  testing in detail." with an inline prose link on "government's own testing"
  pointing to `../when-ai-breaks/facial-recognition-wrongful-arrest.html`, keeping
  the NIST primary citation [8] intact on the measurement.

## Required work

None blocking. The orchestrator runs `nb stamp` and `nb check` after these edits.

## Source-floor ruling (priority adjudication)

Legitimate; kept. The lesson floor of min_sources 8 is met honestly, not padded.
s5 (Rite Aid's statement, primary) and s6 (CNN's reporting, secondary) share one
CNN URL, but under the governing authorship-and-stake test they are two distinct
sources: Rite Aid authors its statement and owns the stake in its own defense
(primary for its position, and the sole cite for the load-bearing "We
fundamentally disagree" quote the commission and voice guide both require present),
while CNN authors its independent report from outside that party (secondary). The
test is explicitly "authorship and stake, not document type or domain," so the
shared domain is not disqualifying. The shared URL exists only because Rite Aid
issued its statement to press with no standalone page; the researcher procedure
(step 4) provides for recording a source at the carrier where it lives, and the
href lands the reader on the page where Rite Aid's quoted words actually appear.
This is not the padding pattern, which is a relabel hiding a missing independent
source: every independent source is genuinely present (three distinct FTC
documents, NIST, Reuters independent of the FTC, CNN, and NBC), and Rite Aid's
statement is a real, required primary the article needs regardless of the count.
No request for a genuine eighth source is routed, because manufacturing one against
an honestly-met floor would be busywork, not a fix. One non-blocking fragility
noted for the record: two entries at one identical URL is presentationally
brittle (if the CNN page rots, two of eight citations die together). It does not
change the ruling.

## Decision

approve. The incident is told in order, every FTC claim is framed as an allegation
under the consent order, the base-rate arithmetic is marked illustrative in the
prose, the demographic-skew mechanism is stated at honest strength, and the
source floor is met legitimately; the one prose issue found was fixed directly.
