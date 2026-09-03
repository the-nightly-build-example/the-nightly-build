# Editorial review: what-could-go-wrong/algorithmic-collusion (editor/01)

## Skeptic

Thesis: pricing algorithms have learned, on their own, to hold prices most of
the way to monopoly and to punish undercutting, but only inside stripped-down
simulations; every condition that props the price up points away from a real
open market, and the one real case people cite (RealPage) is a shared-tool
scheme, not autonomously learned collusion. The open-market version stays an
open question.

Four claims carry it, and all held:

1. Ezrachi and Stucke's fourth scenario is a legal problem because tacit
   collusion with no provable agreement escapes Sherman Act Section 1 and its
   European counterpart. Checked against s1; the "may arrive at this
   anticompetitive outcome on their own" quote is verbatim in the source.
2. Calvano et al.'s two Q-learning agents reached 70-90% of the way to monopoly
   (~85% at the grid mid-point), sustained by learned reward-punishment
   strategies, with no communication. Every figure matches the evidence record's
   Numbers block and the primary: the Δ scale, the 70-90% band, the ~85%
   mid-grid, the ~56% under a demand shock, the ~850,000-round convergence, the
   Exp3 comparison. The annotated Δ equation reproduces (π − πN)/(πM − πN)
   correctly, and the legend labels each term as the record defines it.
3. den Boer et al. and Dorner carry real weight, not a token mention: den Boer
   gets his own section and the holds-up grid, and every "careful" bullet is his
   own objection (simulation only, irrelevant timescale, identical-synchronized
   setup, Exp3 dominance). "there is no immediate reason for alarm" and Dorner's
   "too early to adapt antitrust law" are both verbatim.
4. RealPage is held in its own register: fed shared private data through one
   common tool, pleaded under Sherman Sections 1 and 2, distinct from autonomous
   learning. The OECD "no autonomous tacit collusion cases" line is verbatim.

The three registers stay strictly apart; no claim from one does another's work.
The "coordinating against human oversight" idea is named once as speculation
past the evidence and is not built on, exactly as the brief required. The two
reported-via figures (Klein ~50%, the 2015 Amazon one-third) are attributed to
Calvano's summary, not presented firsthand.

Breaks found and fixed (mine, all within editing):
- The language-models heading claimed the LLM agents "reached the same prices"
  as the Q-learning agents — an equivalence the papers do not establish (the
  body says only "supra-competitive"). Recast the heading to "push prices up
  too," which the evidence supports.
- The body glossed RealPage as pleaded "as an agreement under Sections 1 and 2."
  Section 2 is monopolization, not agreement; the gloss over-read the primary.
  Cut "as an agreement," leaving "pleads the arrangement under Sections 1 and 2,"
  which is what s8 supports. The coordination/agreement character is carried
  correctly in the surrounding prose.
- The simulation row of the comparison table attributed the language-model claim
  to s2 (Calvano, Q-learning only). Added s4 alongside it so the LLM half of the
  cell carries its own source.

Citations opened as printed, all nine resolve to their sources: s1 Oxford ORA,
s2 AER record, s3 CPI PDF, s4/s5 arXiv, s6 Tinbergen PDF, s7 arXiv, s8 DOJ case
page, s9 OECD PDF; the two Go-deeper links resolve too. Two display titles were
wrong and I fixed them against the verified sources:
- s5 read "Strategic Collusion of LLM Agents in Multi-Commodity Competition."
  The real title is "Strategic Collusion of LLM Agents: Market Division in
  Multi-Commodity Competitions." Corrected.
- s3 and the Go-deeper card dropped the source title's terminal question mark
  ("...Competition Policy?"). Restored.
The open item from the brief, source [1]'s title, is resolved: the ORA record
shows "Sustainable and unchallenged algorithmic tacit collusion" (2020), so the
words in the label are correct; left as verified.

## Cut

Slop pass, every sentence including display text and furniture. The draft was
clean: no empty conclusions, no vague attribution, no puffery, no self-reference
outside the two allowed bookends. The negative-parallelism constructions that
survive ("collusion and not just high prices," "the second scenario, not the
fourth," "collusion rather than coincidence") each correct a misconception the
piece actually names, so they are earned, not reflex.

Three sentences failed the delete test or leaned on nothing and were cut:
- "Almost every price online is set by software" opened the lesson on an
  unsourced sweeping claim, paired with a dated 2015 figure. Cut the
  generalization; recast the opener onto the sourced figure, kept honestly as of
  2015.
- "Firms use pricing algorithms; that much is settled" restated the adoption
  figure just given and only signposted the "open question" sentence that stands
  on its own. Cut.
- "The objections are specific, and they are worth setting against the result
  rather than around it" was throat-clearing before the holds-up grid, which is
  self-labeled and speaks for itself. Cut.

Formula pass against the recent-pattern notes: three of the five section
headings were built "clause, and clause" ("...code, and finding...", "One real
case, and it is not..."), which the headline standard flags as stamped when it
recurs within a piece. Varied the construction so one such heading remains:
"Inside the code, the cartel needs a lab" and "The one real case is not the one
the worry predicts." The dek carries none of the banned molds (no semicolon
reversal, suspended question, or comma triad); the why-this-matters bookend
avoids the "This lesson opens..." and "by the end you will be able to" formulas;
the closing section does not end on a stamped one-liner.

Punctuation: converted four semicolons joining independent clauses to periods,
per the house default for the plainer mark (two of them; the third sat in a
sentence I cut). Simplified the table caption's "Three registers the evidence
falls into" to "Three kinds of evidence" for the declared reader, who is new to
the field. Fixed one pronoun slip ("It set the two loose" -> "They," with the
authors as subject).

No borrowed phrasing from the voice-guide exemplars, and no prompt leakage: the
"registers/kinds" framing is the article's own analytical synthesis of the
evidence, not a restated instruction or a claim the piece fulfilled its brief.

## Reader

Read straight through as the paper's declared reader, the piece gives what no
single source does: it locates every result on one line from demonstrated to
conjectured. The lab result arrives with its exact size and its punishment
mechanism, the credible skeptic shows why the lab conditions do not travel,
RealPage is filed as the older shared-tool kind, and the oversight extrapolation
is marked as guesswork. This matches the draft-handoff's original-work claim
(turning a flat list of studies into a graded argument), and both survive: the
piece is a synthesis, not a restatement. The prose sits closer to the
voice-guide exemplars than a median summary, holding calibrated confidence and
ending honestly open ("Worth watching, then, and not worth panicking over")
rather than on a manufactured verdict. The headline commits to exactly what the
piece defends: learned high prices, so far only in simulation.

## Edits

- Recast the why-this-matters opener onto the sourced 2015 figure; cut the
  unsourced "Almost every price online is set by software."
- Cut "Firms use pricing algorithms; that much is settled" (restated the figure,
  signposted the next sentence).
- Cut "The objections are specific, and they are worth setting against the
  result rather than around it" (throat-clearing before the holds-up grid).
- Heading: "Language models reached the same prices..." -> "Language models push
  prices up too, and a phrase can swing them" (the equivalence was unsupported).
- Heading: "Reopening the code, and finding the cartel needs a lab" -> "Inside
  the code, the cartel needs a lab" (break the repeated comma-and mold).
- Heading: "One real case, and it is not the one the worry predicts" -> "The one
  real case is not the one the worry predicts" (same).
- Removed "as an agreement" from the RealPage Sections 1 and 2 sentence (Section
  2 is monopolization, not agreement).
- Added s4 to the table's simulation-row cell for the language-model claim.
- Fixed s5 title to "Strategic Collusion of LLM Agents: Market Division in
  Multi-Commodity Competitions."
- Restored the terminal "?" to the s3 source label and the Go-deeper CPI card.
- "It set the two loose" -> "They set the two loose" (pronoun agreement).
- Converted independent-clause semicolons to periods in the tacit-collusion
  paragraph, the Klein sentence, and the RealPage second-scenario paragraph.
- Table caption: "Three registers the evidence falls into" -> "Three kinds of
  evidence."

## Required work

None. Every finding was an editor-owned fix, made directly. No broken central
claim, missing evidence, or source-policy failure remains for the researcher or
writer. One optional, non-blocking suggestion for the writer: the evidence
record names Calvano's Figure 2 (the Δ heat-map over the α, β grid) as a source
asset that would let a reader see the 70-90% band is common across settings, not
a knife-edge, which is the exact point den Boer's rebuttal engages. Prose covers
it adequately, so this is polish, not a condition of publication. Proof re-run
after edits: BLOCK 0, WARN 0, PUBLISHABLE (link check to be run by the writer /
orchestrator).

## Decision: approve

The argument holds claim by claim, the three registers stay apart, every
citation resolves, and the prose meets the voice guide; the breaks I found were
all editor-owned and are fixed.
