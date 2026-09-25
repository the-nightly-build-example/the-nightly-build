# Editorial review: what-could-go-wrong/ai-environmental-cost (editor/01)

## Correct

Thesis, stated from the draft alone: the AI-footprint numbers that travel are
per-unit ones (a single query, a single run), and per-unit is the scale the
accounting bends most, so the real, measured risk lives in the aggregate
build-out. The claims under it: (1) Strubell 2019 put the first hard carbon
number on training, and the viral "five cars" is her neural-architecture-search
row, not a training run, corrected 88-fold by Patterson; (2) the ~3 Wh query
traces to de Vries and was recomputed ~10x lower to ~0.3 Wh, with the correction
itself bounded; (3) the aggregate is measured (IEA, 415 TWh in 2024) with a
projected band, not a point; (4) both the alarm and the dismissal overreach, and
what would settle it is facility-level disclosure, with water a genuine blank.

I tried to break each against the primaries and the evidence record.

- The five-car figure. Reopened Strubell (ACL P19-1355). Table 1 confirms the
  NAS row at 626,155 lbs against the car-lifetime row at 126,000 lbs
  (~5x), the Transformer (big) row at 192 lbs, and Table 3 confirms 192. The
  article correctly attributes "five cars" to the search, not to model training,
  and states Patterson's 88-fold cut to ~3.2 t with the proxy-task and
  efficient-datacentre reasons and the once-per-problem-class point. Held.
- BERT-flight comparison. Broke. Strubell Sec 4.1 says training BERT on GPU "is
  roughly equivalent to a trans-American flight" (one-way; BERT_base GPU is
  1,438 lbs, below the round-trip NY-SF row at 1,984 lbs). The draft read
  "flying across the country and back," a round trip the source does not
  support. Fixed to "across the country."
- Per-query energy. The ~3 Wh -> ~0.3 Wh trace, the de Vries/SemiAnalysis
  A100/2,000-token origin, the three inflation reasons, and Epoch's own upward
  cases (2.4 Wh at 10k tokens, 40 at 100k) match the evidence. The correction is
  not overstated as "a query is trivial." Held.
- Grid/boundary spread. GPT-3 at 552 t (US-average grid) against BLOOM at 25 t
  (French 57 g/kWh), doubling to 50.5 t on the life-cycle boundary, all match
  Patterson and Luccioni. Held.
- Aggregate. IEA 415 TWh/2024 (~1.5%), ~12%/yr since 2017, Base Case 945 TWh by
  2030, the four-case 670-1,260 (2030) and 700-1,720 (2035) bands, the
  460 TWh/2022 crypto-inclusive earlier edition, and Masanet's 6%/550% all match
  the record with base years intact. The per-unit vs aggregate line is drawn
  explicitly and never conflated: the gap section states a cheap query says
  nothing about a regional grid and the aggregate says nothing about one query.
  Held.
- de Vries projections (85-134 TWh/yr by 2027; Google-AI ~ Ireland) are
  attributed to secondary coverage with the bot-gate stated in prose, as the
  Limits require. Held.

Headline, dek, and subheads checked against the owning documents: every quantity
(88-fold, tenfold, 415 TWh, 2024) is defensible from the piece. data-nb-kind
audited against the researcher's test: Strubell/Epoch/IEA/Patterson/Luccioni
primary, TechCrunch/Data Center Frontier/Down To Earth secondary; 8 sources, 5
primary, 3 secondary, meeting the obligation. Every source href opened via the
proof (links included) and the two internal Background links resolve to the
published the-instruments lessons whose titles the link text quotes verbatim. No
company is named as an authority (Patterson cited as the paper, IEA and Epoch as
research bodies).

## Reads well

The draft was already lean. One sentence went and one was trimmed.

- Cut "honest" from the takeaway's "the honest place to look." That rates the
  writer's own candor, the performed-carefulness tell; the sentence says the same
  thing without it.
- No slop survived the edge read. The bookend "The aim is not to tell you how
  worried to be. It is to hand you the figures that hold up..." is an antithesis,
  but it corrects a real genre expectation the series explicitly disclaims and
  sits in the one card allowed to address the reader, and it states checkable
  content, so it stays.
- Nothing traced to the briefing files or the voice-guide exemplars by clause
  order or borrowed phrasing. The Ritchie/Potter move (a disputed number set
  beside a familiar one) is present in the article's own words (415 TWh against
  Japan's electricity; per-task Wh against a phone charge), not lifted.

No stretch of the piece ran flatter than the voice guide asks; the register is
Yglesias-plain throughout, and the arithmetic is done in view rather than
asserted.

## The experience

The rendered page reads top to bottom as a course correction: the argument at
full strength, then each per-unit number taken apart against its own document,
then the measured aggregate, then the gap. The table earns its place, separating
per query / per search / per run / whole fleet with each figure's boundary and
base year in one view, and it is a distinct shape from the desk's "shown vs
guesswork" idiom. The close resolves the opener (the five-car and 10x-search
claims the reader arrived with) and lands on the aggregate and the undisclosed
water, not on a "present-day relocation" mold. The body never refers to itself;
only the two bookends address the reader.

What the piece gives beyond its sources: it puts the corrected per-unit figures
and the measured aggregate on one axis and shows that every viral number answers
the per-unit question badly while the real risk is the aggregate one, which is
measured but wide. No single source does that assembly; it matches the
draft-handoff's original-work sentence.

## Edits

- Changed the BERT comparison from "flying across the country and back" to
  "flying across the country," matching Strubell Sec 4.1 ("a trans-American
  flight," one-way; BERT is below the round-trip row).
- Cut "honest" from the takeaway ("the honest place to look" -> "the place to
  look").
- Re-ran nb stamp (words 1952, reading 8, sources 8) and nb check with links
  included: BLOCK 0, WARN 0, verdict PUBLISHABLE.

## Decision

approve. The argument is correct, fairly balances both sides before naming the
disclosure gap, keeps the per-unit/aggregate distinction clean, and leaves the
worry to the reader; the two defects were a round-trip overstatement and one
performed-carefulness word, both fixed in place.
