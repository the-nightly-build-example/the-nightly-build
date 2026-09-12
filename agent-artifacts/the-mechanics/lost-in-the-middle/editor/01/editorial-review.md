# Editorial review: the-mechanics/lost-in-the-middle (editor/01)

## Skeptic

Thesis: where a fact sits in a long prompt changes whether the model uses it,
accuracy tracing a U by position for some models but not all, the cause not
settled, and the weakness not removed by a larger context window. The claims it
stands on:

1. **The U itself, at the sizes Liu measured.** GPT-3.5-Turbo runs 75.8% (first),
   53.8% (tenth, middle), 63.2% (last) across 20 documents. Checked against the
   evidence record's Numbers block and Liu Appendix G Table 6: exact. The dip is
   22 points, and the article says "more than twenty points," never the inflated
   ">30%" that secondary coverage carries. Held.

2. **The effect is model-dependent.** Claude-1.3 over the same 20 documents moves
   59.9 / 56.8 / 60.1, about four points. Matches the record. The article draws
   the right conclusion from it, that "models are lost in the middle" overstates
   the flat cases, and the title hedges to "A model's accuracy" rather than
   "models'." I pushed hardest here, because a lesson wants the clean slogan, and
   the draft does not take it. Held.

3. **The middle can fall below closed book.** No documents 56.1%, middle 53.8%,
   oracle 88.3%, all from Liu Table 1 and Table 6. The table furniture states the
   three reference points and lets the reader scale the dip. Held.

4. **Not cured by a bigger window.** Base and extended-context curves nearly
   superimpose (Liu §4.1); the "In the paper's words" quote is verbatim from the
   evidence record. Held.

5. **The mechanism is open.** Three candidates named and kept distinct: position
   encoding (pulls toward the end), attention (favors the start by construction,
   both ends in practice), training distribution (open). The draft rules RoPE
   decay insufficient by the right argument, that decay predicts recency and Liu
   found the U across schemes including ALiBi, and rules instruction tuning out by
   the MPT-30B base case. This is the step the brief and record most feared a
   writer would skip, and it is taken. Held.

6. **Persistence in current models is hedged to proxies.** The draft states
   plainly that "the U by position in a 2025 model is unmeasured here" and leans
   on RULER, NoLiMa (GPT-4o 99.3% to 69.7% at 32K), and Levy. No named
   2024-2025 model is asserted to trace the position-of-answer U. Matches the
   record's unresolved gap. Held.

Display text audited descriptor by descriptor. Headline is a defended claim, no
paired before/after, no negative parallelism. Dek names the actors
(Stanford-led group), the setup (one answer among nineteen distractors, position
the only variable), the figure (more than twenty points), and the window result;
it restates nothing in the headline and carries no banned dek mold. Every
percentage, position, and affiliation in body and furniture checks against the
owning primary. Xiao "at MIT and Meta" and Cheng-Yu Hsieh "at MIT and Google"
match the record's lead affiliations; the two Hsieh papers (Found in the Middle,
s5; RULER, s6) are cited to the right claims and not conflated.

Every `data-nb-kind` is correct: s1-s8 primary (each owns the finding it is cited
for), s9 the LangChain reference secondary (it reports Liu and cites the paper,
it does not measure). Source count 9, primary 8, secondary 1, meeting the
commission's floor.

Opened all nine citation hrefs as printed. Each lands on the source itself and
the title matches: Liu 2307.03172, Vaswani 1706.03762, Su/RoFormer 2104.09864,
Xiao 2309.17453, Hsieh/Found 2406.16008, Hsieh/RULER 2404.06654, NoLiMa
2502.05167, Levy 2402.14848, and the LangChain LongContextReorder reference,
which resolves and cites 2307.03172. No broken or redirecting link; the record
already swapped out the how-to URL that 308-redirects.

No broken central claim, no miscitation, no source-policy gap. Nothing routed to
the researcher.

## Cut

Ran the slop pass over body, display text, and furniture. The prose is clean:
one sentence failed the delete test outright.

- **Signpost cut.** "Two cautions before going further" opened the
  distinctions paragraph and reported the piece's structure without carrying a
  fact. Deleted, and the first caution's subject made explicit so its referent
  does not dangle for a reader who arrived from a link ("This behavior is not the
  needle-in-a-haystack test").

Checked the negative-parallelism instances, since a lesson that corrects a
slogan invites the reflex. Each surviving "not X, but Y" corrects a
misconception the piece names first: RoPE decay "explains a preference for the
end, not why the very start" follows the named temptation to stop at the
encoding; "position matters, sometimes a lot, but models do not ignore the
middle" answers the "models ignore the middle" slogan the voice guide flags as
this piece's register problem. These are earned, and they stay.

Edges read out of order held up. The section closers land conclusions the
paragraphs earned ("So the encoding is part of the story, and not the whole
cause"), and the article's last sentence is the practical payoff, not a moral.
No Verdict block or finding-restating component closes the body; the takeaway
bookend carries the judgment, as press/editorial.md requires. No prompt leakage:
the title's "traces a U" is Liu's reported finding, not the commission's framing
lifted. No borrowed phrasing from the voice guide's quoted writers.

One clarity repair, not a slop cut: "giving GPT-3.5-Turbo more added roughly one
and a half points" misreads on first pass, since "more added" collides. Changed
to "more documents added," which fixes the parse without touching the figure.

Formula check against the recent-pattern notes: the first heading is not a bare
instance count, the closer heading is not a "Today's" restatement, the dek is
not a comma triad, and the headline does not stamp the paired before/after
rhythm. Furniture earns its place: the table supplies the closed-book and oracle
anchors, the quote block emphasizes the settled window result in the primary's
words, and the chart is evidence, not decoration.

## Reader

Read straight through, what I have that the sources alone would not give me: a
single backward chain from the measured behavior to three candidate causes, with
the mechanism claims adjudicated against each other, so I can say why RoPE decay
alone cannot be the cause and why the effect is steep for one model and flat for
another. The draft-handoff's original-work sentence claims exactly this
synthesis, and the article delivers it. The prose sits closer to the voice-guide
exemplars than to a median summary: it grants the true half of the slogan and
marks where it stops, states the numbers out loud at the sizes measured, and
flags the persistence question as open rather than papering it. The headline read
as the largest claim is true and correctly scoped by its indefinite "A model's."

## Visual evidence

Chart provenance (`chart-1.py`) carries the data inline: GPT-3.5-Turbo
75.8/57.2/53.8/55.4/63.2 and Claude-1.3 59.9/55.9/56.8/57.2/60.1, both exact
against the evidence record and Liu Appendix G Table 6. Read the rendered PNG:
axes labeled (position of the answer document of 20; accuracy %), legend present,
lines distinguished by dash and marker as well as color. The y-axis is truncated
to 45-80, which is honest here rather than misleading: it shows GPT-3.5-Turbo's
steep U against Claude-1.3's near-flat line, the true relationship, where a zero
baseline would compress both and hide the point the figure exists to make. The
caption is a factual cited label and the alt text matches the image. No chart
correction routed.

## Edits

- Cut the signpost sentence "Two cautions before going further." from the
  distinctions paragraph (orientation section).
- Changed "This is not the needle-in-a-haystack test" to "This behavior is not
  the needle-in-a-haystack test" so the paragraph's opening referent is explicit.
- Changed "giving GPT-3.5-Turbo more added roughly one and a half points" to
  "giving GPT-3.5-Turbo more documents added roughly one and a half points" for
  first-read clarity (figure unchanged).

## Required work

- **Writer:** re-run the proof (`nb check` with links, BLOCK: 0) after these
  prose edits, since word count shifted by a few words and the orchestrator
  stamps before the PR. No content redraft is needed.

## Decision

approve — figures, citations, chart, and effect-size calibration all check out,
the mechanism reads as genuinely open, and the two remaining prose flaws were
mine to fix and are fixed; only a fresh proof of the edited text remains.
