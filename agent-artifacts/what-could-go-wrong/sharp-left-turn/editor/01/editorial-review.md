# Editorial review: what-could-go-wrong/sharp-left-turn (editor/01)

## Skeptic

Thesis: the sharp left turn (Soares 2022) claims capability generalizes better
than trained-in alignment, so a system could carry its skills past the point
where its safety holds. The piece's own thesis is that this argument fuses one
narrow measured result with an unobserved predicted event, and that both the
alarm and the dismissal run past the evidence.

Load-bearing claims and how each held:

1. **Goal misgeneralization is real but toy-scale.** Tested against Langosco
   (s2) and Shah (s3). Every figure checks out: coin reward 10 / all else 0;
   100% wall walk-through (n=114); 89% color-over-shape (n=102); the 2% training
   randomization that largely closes the gap; Gopher at 280B asking a redundant
   clarifier. The piece bounds it correctly ("Every case is the same size: a
   hand-built shift ... inside an arcade game or a single prompt"). The claim
   survives, and its size is drawn honestly.

2. **The exact event the argument names has not been observed.** This is the
   spine, and it is stated plainly: "a safety property that held while a system
   was less capable and then broke when the same system became more capable, has
   not been observed in any system." No sentence lets the analogy read as
   demonstrated. I pushed hardest on the steelman: "Soares has one worked case,
   and it is us" is the strongest candidate, but it sits inside the licensed hot
   register, stays conditional ("may simply not generalize," "when that general
   competence arrives"), and the OpenMind turn is explicitly "a fictional lab."
   The cool test then re-labels it cleanly ("The coin is what a working system
   has shown. The turn is something else"). Held.

3. **Perez is stated behavior across different models, not an in-system turn.**
   Verified against s5. The piece says so in as many words: "These are stated
   behaviors, what a model says about itself when evaluated, not actions it took.
   And they are a trend across different models of different sizes, not a break
   inside one system as it crossed a capability threshold." Held exactly as the
   brief requires.

4. **The catastrophe rests on a contested analogy.** Pope (s6) gets his own
   position card and a faithful mechanical summary (culture as a one-time fix for
   an evolution-specific bottleneck; weights persist, so the mechanism is
   absent). Schaeffer (s7) gets emergence-as-mirage in his own frame, with the
   scope caveat preserved verbatim in substance ("about benchmark scores, not
   alignment ... does not prove no jump can ever happen"). Krakovna's "we can't
   actually say that it has learned a goal" (s4) is present and correctly used to
   bound the anchor. Shah's own hedge is quoted in their own words: "necessarily
   speculative," "quite implausible," "no technical reason ruling it out." All
   four skeptic voices land in their own words. Held.

5. **The demand is now mainstream (Yudkowsky & Soares 2025).** Source 9 is
   Wikipedia (secondary) and is labeled secondary. The book is paraphrased, never
   quoted as the authors' words, and the prescription is attributed to the book.
   One overreach found and fixed (see Edits): the draft firmed Wikipedia's
   "possibly with an exception for narrow AI systems like AlphaFold" into a
   definite "sparing only narrow tools." Restoring "possibly" keeps the claim
   inside what the secondary coverage supports. With that fix, the source-9
   handling is honest.

Display text audited descriptor by descriptor. Headline attributes the warning
to Soares ("Soares warns ...") and hedges the claim ("could break"), so it never
asserts the turn as fact. Dek draws the shown/analogy line and calls the turn
"still an analogy"; it is one sentence, a stance not a topic, and carries none of
the banned dek molds (no semicolon reversal, no suspended question, no comma
triad; it is two clauses on a comma-and). Krakovna's title ("research scientist
on DeepMind's alignment team"), Perez's affiliation (Anthropic), Pope, Schaeffer
(Stanford), and every date and figure match their owning primaries.

`data-nb-kind` audit: s1 Soares/MIRI, s2 Langosco, s3 Shah, s5 Perez, s6 Pope,
s7 Schaeffer, s8 Krakovna's own blog — all primary, all authored by the party
that owns the claim. s4 (AI Impacts summarizing an interview) and s9 (Wikipedia
on the book) are correctly secondary: each reports from outside the authoring
party. No mislabel, and the one place the argument most needs an outside source
(the present-day book) is honestly flagged secondary rather than dressed as the
book itself. Every href matches the evidence-record URL for its source and lands
on the source itself; the writer's proof already cleared links at BLOCK 0.

Company-as-authority check (series rule, brief): no company is named as an
authority. DeepMind, Anthropic, and Stanford appear only as the affiliations of
named researchers, and every claim is cited to a paper or a person, never to a
corporate voice. "OpenMind" is Soares's own fictional lab. Compliant.

No broken central claim, no miscitation, no missing-evidence gap. Nothing routed
to the researcher.

## Cut

One self-grading line removed. In the takeaway, "Drawing the line is the point"
grades the article's own method (the "X is the point" family the editorial
direction bans) and duplicated cargo already carried by its neighbors ("The
lesson will not answer that for you" before, "What you can now do is separate the
two things ..." after). Cut; the paragraph reads cleaner and loses nothing.

Considered and kept: "Now set the argument down and measure it" is the licensed
hinge of the two-temperature structure, not a navigational signpost, and it acts
on the argument rather than announcing a section. "By the end you will be able
to ..." in the opener is template-licensed bookend chrome (what the reader will
understand by the end). "It is a mainstream policy demand" is earned by the
bestseller and policy-call facts in the same breath, not an unearned punchline.

Prose leakage check against the writer brief and briefing stack: none. "Where
confidence outruns proof" is the substance the series asks the piece to find, not
a copied instruction label; it is applied concretely and symmetrically to alarm
and dismissal in the same paragraph. The word "spine" from the briefs never
reaches the prose.

Pattern check against the recent library: the recurring what-could-go-wrong molds
(headlines as "needs a lead nobody has held" / "no AI has been caught," closers
as "what no experiment has caught yet") are both broken. The headline is a
named-proponent warning; the closer lands on "which half anyone, alarmed or
dismissive, still owes you the evidence for." Section headings reconstruct the
argument in the piece's own nouns with varied shapes; no comma-and cadence
repeats. Furniture is restrained and earns its place: one stat strip (the CoinRun
narrowness numbers, each cited nearby) and one position card (Pope, the sharpest
counter), plus the two required bookends. Grammar and punctuation are clean,
including the two single-semicolon contrasts, which are tight parallel pairs, not
chains.

## Reader

Read straight through as the paper's smart, not-yet-scared reader, the piece
gives something no single source gives: the precise boundary between the one
narrow measured result (CoinRun, quantified) and the exact event the argument
names but no one has seen (a safety property breaking within one system at a
capability jump), with alarm and dismissal held to that same missing experiment.
Soares argues for it, Pope and Schaeffer against, Krakovna narrows it, Shah
hedges it, but the symmetric naming of the missing evidence is the article's own
synthesis, and it matches the draft-handoff's original-work sentence. The prose
sits with the voice-guide exemplars (Carlsmith/Karnofsky/Alexander: scoped,
bounded, two audible temperatures), not a median summary. The hot steelman drops
to cool at the measurement and stays there. It teaches, it does not restate.

## Edits

- Cut "Drawing the line is the point." from the takeaway (self-grading
  method-summary, redundant with its neighbors).
- Changed "sparing only narrow tools like protein folders" to "possibly sparing
  narrow tools like protein folders" (restores the "possibly" hedge from the
  secondary source, s9; the draft had firmed a tentative exception into a
  definite one).
- Ran `nb stamp`: words 2191, reading 10 min, sources 9.

## Required work

None blocking. The writer owns the re-proof after these direct edits (word count
now 2191, still inside the 1200-2200 band; no markup, source, or structural
change was made).

## Decision

approve. The shown/analogy spine is stated plainly and never lets the analogy
read as demonstrated, the skeptics speak in their own words, the secondary
attribution of the 2025 book is now honest, and no company is named as an
authority; the only issues were one self-grading line and one firmed-up hedge,
both fixed in place.
