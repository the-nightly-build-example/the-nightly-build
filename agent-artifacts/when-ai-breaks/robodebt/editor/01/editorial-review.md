# Editorial review: when-ai-breaks/robodebt (editor/01)

## Skeptic

Thesis: Robodebt's failure was not "an algorithm ran amok" but an older design
scaled past the point where anyone could catch it. Income averaging manufactured
a fortnightly income the recipient may never have earned, a reversed burden of
proof turned that invented figure into a demand the recipient had to refute, and
removing the per-file compliance-officer check is what turned a rare, correctable
error into hundreds of thousands of debts. The same bargain still runs where a
data-match or a model score is treated as proof and the onus to disprove it is
pushed onto the individual.

The claims it stands on, and how each held:

- **The averaging arithmetic (the worked example).** This is the load-bearing
  teaching claim, so I pushed hardest here and opened the owning primary. The
  Amato consent order (s3) resolved without a block from the Commonwealth Courts
  Portal, and I read all eight pages. Every figure in the article matches the
  court's own words: $24,811 annual PAYG income divided by 366 days = $67.79/day
  (Notes 5.1), x14 = $949.05 apportioned fortnightly income (5.2), substituted
  for her actual reported earnings and aggregated to a $2,924.28 debt (Note 4),
  reassessed to $2,504.42 (Note 12), garnishee of the lesser of $3,215.38 or her
  whole refund (Order 3), "not validly made" (Declaration 1), "no probative
  material" for the equal-earnings assumption (Note 8.2), and the Commonwealth's
  concession that a real but "very substantially smaller" debt was in fact owed
  (Note 2). The article's nuance — averaging invented the amount, not always the
  whole debt — is exactly what Note 2 supports. Held.

- **Mechanism, not "automation" alone.** The article is explicit that averaging
  and the reversed onus predate the software, that the earlier manual program
  already used both, and that the new thing was removing the human check. It does
  not reduce the lesson to "the algorithm did it." Held, and central to the piece.

- **Harm to the record.** The article assigns no death toll, attributes the
  court's recorded harms (financial hardship, anxiety and distress, including
  suicidal ideation and in some cases suicide) to Prygodicz (s5), states that the
  Royal Commission was aware of suicides among people with Scheme debts but
  assigned no count and held causation case-specific, and correctly places Rhys
  Cauzzo's debt in the earlier manual-but-averaged process, not the online system.
  Checked against the evidence record's harm and Cauzzo entries; faithful. Held.

- **The 2017 Ombudsman report is not an early illegality finding.** The article
  states the 2017 report did not reach lawfulness ("accurate, based on the
  information which is available to DHS," fairness "can only be answered by the
  courts"), and that the department then used it as cover. Matches s2 and the
  evidence. Held.

- **Amato vs Prygodicz vs the Royal Commission.** The individual consent finding,
  the class-wide "not validly made" declaration, and the systemic "unlawful"
  finding are kept distinct and attributed to their owners, as is the split
  between Murphy J's 2021 "stuff up over conspiracy" and the Commission's 2023
  finding of 2014 legal advice known to senior people. Held.

- **The Senate recommendation.** Correctly attributed as a committee-majority
  recommendation over a Government Senators' dissent, not adopted by the
  government of the day and acted on only after the 2022 change of government.
  The cost-versus-savings figures (~$2 billion projected against $606 million
  spent) match s4. Held.

Display text, descriptor by descriptor: headline, dek, every subhead, the stat
strip, and the note. Every figure carries its denominator and matches the owning
primary — $1.763 billion / ~433,000 and $751 million / ~381,000 to Prygodicz;
$746 million / ~381,000 / $1.751 billion written off to the Royal Commission;
~470,000 debts to the 2021 Ombudsman; $112 million and $475 million (Knox) to
Prygodicz and the AG release. The reckoning paragraph correctly labels the
Prygodicz/Commission figure gaps as different measures at different times, not a
disagreement. The `data-nb-kind` labels are right: seven primaries and one
secondary (the PM release, correctly marked secondary, with figures cited to the
Report rather than to it).

Citations opened as printed. The Amato portal file (s3) and the PM release (s7)
both resolved and landed on the source. The Royal Commission PDF (s1), both
Ombudsman PDFs (s2, s6), AustLII Prygodicz (s5), the aph Senate landing (s4), and
the AG release (s8) all returned headless 403/503 bot-blocks, exactly the block
the evidence record documents for these government and court hosts; the printed
addresses are the canonical document pages a browser reader reaches. Both
Background links and the still-running link resolve to real published articles,
and their descriptor text reuses the linked articles' own titles and dek wording.

Two breaks found, both fixable in place with the right source already at hand;
neither needed new reporting:

1. **A claim overstated its cited source (s7).** The article read "the government
   publicly accepted the findings" in July 2023, cited to the PM release. I
   re-opened the release: it says only that the government "will now consider the
   recommendations presented in the final report carefully and provide a full
   response in due course." Accepting the findings is not what that source
   establishes. Corrected the sentence to what s7 says.

2. **A miscitation (s3 for a claim s6 owns).** "In November 2019 the government
   announced it would stop raising debts on averaging alone" was cited only to the
   Amato consent order (s3), which is dated 27 November and says nothing about a
   government policy announcement. The 19 November 2019 announcement is owned by
   the 2021 Ombudsman report (s6), already cited two clauses later. Added the s6
   citation to the announcement; the Amato consent-orders clause keeps s3.

## Cut

One sentence failed the slop test and was cut: "On the central question the
finding is unambiguous." It reduces to "on the X the Y is Z," reports where the
argument stands without doing any of the reasoning, and its deletion loses no
fact — the paragraph now opens on "Averaging is not unlawful in itself; using it
as the sole basis to prove a debt is," which is stronger.

The rest of the edges held on their own. I read the first and last sentence of
each paragraph, section, and furniture component out of order. The negative-
parallelism constructions that survive each correct a misconception the piece
actually names and rests its thesis on: "Removing the human check did not invent
the error. It mass-produced it," "The weakness that carries beyond Robodebt is
the bargain, not the software that ran it," and "Averaging is not unlawful in
itself; using it as the sole basis to prove a debt is." None is a strawman. The
closing "Only the signal changes. What stays is the shape: proof asserted
cheaply, and the doubt made the citizen's to clear" states the transferable
mechanism in the article's own nouns and carries the reasoning payoff the series
close needs, so it stays.

Against the recent-pattern notes: no anaphora heading run; the where-it-lives
heading ("Where the same bargain still runs") is in Robodebt's own nouns, not the
tesla or optum molds; the headline uses "X, then Y," not "recalled X for letting
Y" or the comma-and reveal; the takeaway opens on "Robodebt did not invent a new
kind of mistake," not a restated definition or "Two things are true"; the dek is
one plain claim with none of the three banned molds. No borrowed phrasing from
the voice-guide exemplars (McKenzie, Davies, Useem) appears in the draft. No
prompt or brief leakage: the body speaks to no one, the bookends address the
reader as the lesson template allows, and no sentence claims the article did its
assignment. Punctuation is clean; the one semicolon is justified by an elided
predicate a period would strand. Furniture earns its place — the before/after
table teaches the mechanism contrast, the stat strip carries thesis figures each
cited in nearby prose, and the note gives the Commission's finding deliberate
emphasis; nothing is a stack-of-blocks filler and no retired component is used.

## Reader

What the piece gives beyond its sources: one transferable mechanism assembled
from seven government and court records — that averaging manufactures a per-period
figure the person never earned, that reversing the burden of proof converts a
statistical guess into a demand, and that removing the per-file human check is
what scaled a rare error into a mass one — carried by a worked example in a real
recipient's court-recorded arithmetic and lifted onto a system still running. No
single source assembles that synthesis. Read against the original-work sentence
in the draft handoff, both answers survive. The prose sits closer to the
voice-guide's plain-declarative exemplars (McKenzie's restraint on scale, Davies'
even volume on grave harm) than to a median AI summary. The headline is the
largest claim and the piece defends it.

## Edits

- Cut the slop signpost "On the central question the finding is unambiguous."
- Corrected "the government publicly accepted the findings" to "the government
  said it would consider the recommendations and respond in full," matching what
  the PM release (s7) actually states.
- Added the s6 citation to the November 2019 government announcement, which was
  cited only to the Amato consent order (s3) that does not establish it.

## Required work

- **orchestrator:** re-stamp the article (word count drops slightly after the
  cut; source count is unchanged at 8, since s6 was already cited).
- **writer:** re-run the proof to BLOCK 0, because prose and one citation changed.

No work for the researcher: both breaks were resolved against sources already in
hand, and no claim required new reporting.

## Decision

approve — the mechanism, the figures, the worked example, and the harm handling
all hold against the primaries, and the two citation faults and one slop sentence
were fixed in place without new reporting.
