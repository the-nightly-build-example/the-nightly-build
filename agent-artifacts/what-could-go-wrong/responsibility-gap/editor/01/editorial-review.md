# Editorial review: what-could-go-wrong/responsibility-gap (editor/01)

## Correct

The thesis reads cleanly from the draft alone: the responsibility gap is two
claims under one name. One is a real design problem, that opacity and many hands
make fault hard to locate. The other is the stronger claim that no human can be
held at all. The piece argues the strong claim has failed only for supervised
systems, that the fully-autonomous machine the argument was built for has not yet
killed and reached a court, and that the legal question closes faster than the
moral one. The claims under it:

1. Responsibility needs control and knowledge; a learning system removes both
   from operator and maker, and the machine is no moral agent, so blame has
   nowhere to land (Matthias, Sparrow).
2. That gap opens only where no human is assigned to supervise. The deployed
   deaths involved supervised-by-design systems (Uber developmental with a safety
   driver; Tesla Autopilot at SAE Level 2 with the driver as responsible
   operator), so they refute the strong claim only for supervised systems.
3. Where those systems killed, a human or the maker was located: Vasquez
   convicted, Uber not charged, Tesla's controls faulted and its fleet recalled.
   The many-hands problem is real and is not the same as no one being holdable.
4. EU law does not close the gap tidily: the AI Liability Directive was withdrawn
   in 2025, and the Product Liability Directive applies only from December 2026
   and only to products. Tigard, the firmest denier of the gap, concedes the
   moral side is the harder one.
5. The fully-autonomous, no-supervisor case remains untested.

I tried to break the one I most wanted to keep, the headline. **"So far, a human
has answered for every automated-driving death" did not survive the record.** In
the 2016 Williston case (NTSB/HAR-17/02) the Tesla driver, Joshua Brown, was
killed, cause fell on him and on the truck driver, and the truck driver was not
charged. No human answered for that death in the accountability sense the old
headline claimed, so "every ... has answered" overclaimed. I rewrote the headline
to the supervision-by-design claim the record does support: every investigated
automated-driving death came with a human the system named as the responsible
operator, Williston included (Brown was the assigned L2 operator). That is the
piece's actual, defensible finding, and it keeps the accountability outcome (who
was ultimately charged) apart from the design fact (who the system named). The
takeaway carried the same fault in parallel ("In every automated-driving death so
far, someone was [held]"), false for Williston; I narrowed it the same way.

The two secondary-sourced facts hold. Uber not criminally charged is cited to s6
(NPR, secondary) and phrased as reported ("a prosecutor's office that reviewed
the question found no basis for it"), not asserted from the Yavapai letter the
researcher could not read. The AILD withdrawal is cited to s9 (IAPP, secondary)
for the withdrawal itself, with s8 (the COM(2022) 496 proposal, primary) carrying
only the description of what the directive would have done; the withdrawal is
phrased as reported ("withdrawn by the European Commission in 2025 for want of
foreseeable agreement"). Correct split.

Every data-nb-kind checks out against the authoring-document test: 9 primary
(Matthias, Sparrow, both NTSB reports, the NHTSA/Tesla records, the Maricopa
charging record, the two EU instruments, Tigard) and 2 secondary (NPR, IAPP).
None claims an independent author it does not have. Every citation href resolves
(nb check with link validation, BLOCK 0). Every block quotation matches the
evidence record verbatim, with ellipses only where the record supplied the full
passage: Matthias (pp. 175, 177, 183), Sparrow (pp. 66-73), the NTSB 5.6-second
detection and misclassification and "precluded emergency braking," the NHTSA
"critical safety gap" and 467/13 and 2,031,220, the Recall 23V-838 "the driver is
the operator," and Tigard's "regulatory gaps can in principle be repaired ...
while potential gaps in moral responsibility are far less clear." The table's
three rows match the record: Uber (safety driver convicted, Uber not charged,
NTSB faulted safety culture); Williston (cause to two drivers, no liability
finding, design permitted disengagement); Tesla fleet (2,031,220 recalled, driver
the responsible operator, NHTSA weak controls). The caption is a factual cited
label; the many-hands interpretation stays in prose.

The corrected angle is intact. Supervised cases refute the strong claim only for
supervised systems; the fully-autonomous case is stated as untested in both the
the-line section and the close. Legal and moral are kept apart, with Tigard
conceding the moral gap is the harder one. AILD withdrawn; PLD later and narrower.
Matthias and Sparrow are stated at full strength in their own words before a word
against them.

## Reads well

Nothing needed cutting for slop. The edges hold under the placeholder test: the
opener's rhetorical question is the lesson's own and is answered; the closing gap
sentence is written in this lesson's terms (the untested no-supervisor case plus
the moral question), not the desk's recent "no study has tracked" mold. The
antitheses that survive ("not the same thing as no one being holdable," "not on
an empty space where accountability should have been") each correct a
misconception the piece states, which is the allowed case. No name-and-year
opener was smuggled into the dek. Headings are each a step in the piece's own
nouns, none built as "clause, and clause," and skimming them reconstructs the
argument. The new dek is a plain two-clause sentence, not a semicolon reversal,
comma triad, or suspended question.

My takeaway rewrite first ran long (a 48-word sentence, four clause joins) and
pushed the piece to 2210 words, over the band. I split it into three plain
sentences and trimmed, landing at 2200 with no density warning.

## The experience

The rendered page reads straight through. The table earns its place: it separates
who was held from the fault the same record named, across three cases, faster
than prose could. No chart is warranted; the argument is doctrinal, not a trend.
What the piece gives beyond its sources is the split itself, drawn across
philosophy, the deployed record, EU law, and the primary rebuttal: it shows the
strong "no one can be held" claim failing only for supervised systems and the
philosophers' actual scenario still untested, and it keeps the legal answer apart
from the moral one. That matches the writer's original-work sentence, and it
survives the read. The headline, reread last as its largest claim, now states
what the record supports.

## Edits

- Headline: "So far, a human has answered for every automated-driving death" -> "Every automated car that has killed came with a human assigned to watch it" (title tag, nb-meta title, h1).
- Dek: "The argument was built for a machine with no one supervising it, and every automated car that has actually killed someone came with a driver the law could name." -> "The responsibility-gap argument was built for a machine no one supervises, and no case has yet put that machine on trial." (nb-meta dek, dekline).
- Takeaway: narrowed "In every automated-driving death so far, someone was: a safety driver on probation, a fleet recalled, a manufacturer's controls named as the flaw. Those systems could be answered for because each named a human to watch it." to "It has not held where these systems killed, because each of them named a human to watch it. An Uber safety driver drew a conviction and probation. Tesla's driver-monitoring controls drew the fault, and its cars were recalled." (removes the accountability overclaim Williston contradicts; splits the dense sentence; returns the piece to band).
- Ran nb stamp (words=2200) and nb check (--series what-could-go-wrong, links included): BLOCK 0, WARN 0.

## Decision

approve. Every fault was a claim reaching past the record, and each was fixable
by narrowing it to what the record supports; the argument itself is sound and
needs no redraft.
