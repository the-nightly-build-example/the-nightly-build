# Editorial review: the-instruments/self-consistency-scoring (editor/01)

## Skeptic

Thesis: a cons@k / maj@k / self-consistency score is a majority vote over k
sampled tries; it is honest in the report that produces it, but it misleads once
it travels without its k or is set beside a single-try number, because the vote
costs k times the inference and is not the same measurement as a single try.

Claims it stands on, and how each held:

- **The two o1 numbers are a scoring-rule difference, not a capability jump**
  (74% one try, 83% over sixty-four on the 2024 AIME). Checked against source 1:
  pass@1 74% (11.1/15), consensus@64 83% (12.5/15). Holds. The headline states
  exactly these figures with the actor named.
- **The vote is built in three steps and lifts a score when the model is right
  more often than any single wrong answer recurs.** Checked against Wang et al.
  (source 2): GSM8K on PaLM-540B rises 56.5% greedy to 74.4% over forty samples
  at T=0.7, a 17.9-point gain. Holds; matches the evidence record's Table 1
  figures.
- **The number costs k times the inference, so a voted score and a single-try
  score are not comparable.** Definitional and stated across the sources. Holds.
- **Coverage (any of k correct) keeps scaling while the vote plateaus.** Checked
  against Brown et al. (source 4): SWE-bench Lite coverage 15.9% at one sample to
  56% at 250; voting plateaus once samples run into the hundreds. Holds. The
  draft read "a few hundred"; the source says "several hundred," so I aligned the
  quantity to the primary.
- **The misread is downstream, not concealment.** This is the corrected spine,
  and I pushed on it hardest. The piece states plainly that inside each report
  the single-try and voted numbers sit side by side and labeled (Minerva's
  33.6%/50.3%), and that DeepSeek's 86.7% matching o1 is a fair cons@64-to-cons@64
  comparison (source 7, Table 2: o1-0912 at cons@64 83.3, not pass@1). It locates
  the failure where a voted number is quoted without its k or against a rival's
  single-try score. This matches the evidence record's Contradictions section.
  Holds, and it does not drift back toward the concealment framing the record
  warns off.
- **The field's comparison layer moved to single-sample scoring.** Checked
  against Artificial Analysis (source 8): pass@1, best-of-k called out as
  inflating. Holds.

One break with the evidence, fixed directly. The draft said "One row above
Minerva's 50.3% sits the prior published state of the art on MATH: 6.9%." The
direction is wrong. I opened the primary (arXiv:2206.14858): the Published SOTA
row (6.9%) is printed below the Minerva 540B rows, not above, and a davinci-002
row sits between them, so "one row" is imprecise in either direction. The
evidence record is itself split on this: its Numbers/Scope line says 6.9% is
printed above the voted number, while its Contradictions section, the writer
brief, and the draft handoff all say the reverse. I rewrote the sentence to the
verified reading and dropped the false row-adjacency, keeping the numbers and
their meaning untouched. The argument that follows (a reader scanning one column
sees 6.9% and 50.3% together and reads a sevenfold leap; 50.3/6.9 is 7.29) is
unaffected.

Display text checked descriptor by descriptor. Headline: o1, 74% one try, 83%
over sixty-four, 2024 AIME, all true. Dek adds the interpretation without
restating the headline and leads on the convention rather than on a numeric
contrast, so it breaks the recent-dek mold and dodges the banned molds
(no semicolon reversal, no suspended question, no comma triad). Subheads are the
piece's own nouns and none leads with a raw number or a comma-and contrast.
Source kinds audited: 8 sources, 6 primary, 2 secondary; Han Lee and Artificial
Analysis are correctly labeled secondary (reporting from outside the authoring
party). Background links to pass@k, AIME, and MATH point out of the piece and it
does not retread them. The o1 source URL returns a bot 403, which is gated not
dead, per the brief no action is needed.

## Cut

Two body self-references removed. The template confines self-reference to the two
bookends, and the body must speak to no one. The orientation section ended on
"The rest of this piece works out why it does, what the higher number costs..."
(a signpost that narrates the article); I cut it, and the section now closes on a
fact. The closing section read "the standard now, for the reason this piece has
built:"; I replaced the self-reference with "because," keeping the causal link.

One signpost trimmed. "Feeding a model more tries does raise a different number
without any ceiling in sight, and keeping the two apart matters" told the reader
the distinction matters without drawing it; the next paragraph draws it. I cut
the trailing clause.

One grammar fix: "the answer that the most of them agree on" to "the answer that
most of them agree on."

The rest of the prose survived the slop test. The negative-parallelism
constructions ("a vote among a model's own tries rather than a single try," "A
vote is not a search for the best chain. It is a way to cancel out...," "not what
a vote measures," "across models rather than within one table") are each tied to
a misconception the piece has named, so they are earned rather than reflex. No
prompt leakage: the terms the piece shares with the brief ("without its k,"
"across models") are the subject's own, and no planning label or selection rule
leaked in. No banned-term or em-dash overrun (the proof ran clean, and the body
reaches for periods and commas throughout). Four sentences were touched in total.

Furniture: the piece runs lean, three numbered steps and one comparison table,
and breaks the recurring stat-strip/figure/table/note/holds-up stack the notes
warn against. Both components earn their place: the steps carry the
construction in order, and the table is the core single-try-versus-vote contrast
across three systems, which the commission explicitly allowed. No component
restates the finding, and nothing reads as a stack of blocks.

## Reader

Read straight through as the paper's reader, someone with algebra and no
machine learning: what I have that the sources alone would not give me is the
worked ten-sample count that shows mechanically why the plurality lifts a score
and exactly when it cannot (seven wrong-but-agreeing chains beat three right
ones), plus the relocation of the misread from "labs hide the compute" to how a
voted number behaves once it circulates. The sources supply the figures; the
piece supplies the mechanism and the corrected reading. The original-work
sentence in the handoff claims exactly this, and the article delivers it, so the
piece is not a restatement of its sources. The prose sits closer to the
voice-guide exemplars than to a median summary: it counts in whole numbers before
percentages (the Our World in Data move), runs one concrete case with real
sampled answers (the Evans move), and lands its judgment in the takeaway without
dressing it up. The headline, read as the largest claim, is true and is the
lesson's actual hook.

The publication-blocking press rule is satisfied: the body carries no Verdict
note or any block restating the finding, it closes on the Artificial Analysis
paragraph, and the takeaway bookend lands the judgment.

## Edits

- Cut the orientation-section signpost sentence "The rest of this piece works out
  why it does, what the higher number costs, and why setting it beside a score
  from a single attempt gives a false reading" (body self-reference).
- Replaced "for the reason this piece has built:" with "because" in the closing
  section (body self-reference).
- Cut the trailing signpost clause "and keeping the two apart matters" from the
  ceiling section's opener.
- Rewrote "One row above Minerva's 50.3% sits the prior published state of the
  art on MATH: 6.9%, a single-try number" to "Farther down the same MATH column
  sits the prior published state of the art: 6.9%, a single-try number"
  (corrected a reversed and imprecise row direction against arXiv:2206.14858).
- Changed "plateau after a few hundred samples" to "plateau after several hundred
  samples" (aligned to Brown et al.).
- Fixed "the answer that the most of them agree on" to "the answer that most of
  them agree on" (grammar).

## Required work

None blocking publication.

- researcher (non-blocking, record hygiene): the evidence record contradicts
  itself on the Minerva Published SOTA layout. The Numbers/Scope line says 6.9%
  is "printed one region above the 50.3% voted number," while the Contradictions
  section says 50.3% sits one row above 6.9%. The primary (arXiv:2206.14858)
  shows 6.9% below the Minerva 540B rows with an intervening davinci-002 row. The
  article is now correct; the record should be reconciled before reuse.

## Decision

Approve. The corrected spine holds, the publication-blocking press rule is met,
and every break I found was mine to fix and is fixed; no item needs new reporting.
