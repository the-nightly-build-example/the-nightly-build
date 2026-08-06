# Editorial review: the-instruments/glue (editor/01)

## Skeptic

Thesis: the "human-level" language score is an unweighted average of nine
English tasks measured against a hurried non-expert crowd baseline, and crossing
that line is not evidence a model understands language. The piece stands on four
load-bearing claims. I stated each from the draft alone and tried to break it.

1. Two dated crossings (MT-DNN 87.6 vs 87.1 GLUE, 6 Jun 2019; DeBERTa 89.9 vs
   89.8 SuperGLUE, 6 Jan 2021). Checked every figure and date against the
   evidence Numbers block and the two Microsoft primaries. All exact: 87.6/87.1,
   89.9 single and 90.3 ensemble/89.8, both dates. "Nineteen months later"
   describes the gap between the two crossings (Jun 2019 to Jan 2021), which is
   correct; it does not claim to be the SuperGLUE launch-to-surpass interval, so
   it does not collide with the evidence's ~20-month figure. Held.

2. The score is a nine-task equal-weight macro-average across four metric units,
   paired-metric tasks averaged internally first. Matches Wang et al. 2018 and
   the evidence Numbers/tasks entries task by task; the "634 counts as much as
   393,000" line is the honest consequence. The tasks table figures all match the
   evidence (sizes, metrics, questions). Held.

3. The WNLI worked example: majority-vote floor 65.1, human 95.9, prior SOTA
   including BERT stuck at the floor, MT-DNN over the human line only after a
   method lifted WNLI to 89.0. Matches the MT-DNN blog (s1) exactly. This is the
   article's central staged mechanism and it is sourced to the primary that owns
   it. Held.

4. High scores can ride shortcuts, but model-specifically. Hypothesis-only NLI
   ~67%/~53% vs ~33% chance (Gururangan, s6) and COPA cues-only 59.6 vs 50
   (Kavumba, s7) are stated exactly; the BERT 76.5->74.5 / RoBERTa 87.7->89.0
   table matches the evidence. The article correctly frames reliance as
   "consistent with," not "every high scorer exploits shortcuts." Held.

Brief focus 1 (framing). The "misled" is located in reception and shorthand,
never pinned on the authors. "Not from the people who built the benchmarks or
topped them" says it outright; GLUE's authors read saturation as a reason to
build SuperGLUE; the DeBERTa caveat ("by no means reaching the human-level
intelligence of NLU") is quoted directly; Bender & Koller carry saturation is
not comprehension. No misattribution. Pass.

Brief focus 2 (reception on a single secondary). I tested whether the reception
claim overreaches the lone Gilbane secondary. It does not, because the overreach
claim rests on a primary, not on Gilbane: Bender & Koller (s8) explicitly name
the reading, warning against hype in which models "are being described as
'understanding' language." Gilbane is used only as the calibrated, narrow end
("careful readers kept the claim narrow"), which is exactly what a secondary
repetition can support. So "one line kept recurring... human-level understanding"
is carried by the primary and I left it standing rather than cutting it back.

Display text audited descriptor by descriptor. Headline is a defended claim, no
colon-subtitle, no two-numbers mold. Dek makes a world-claim (the line was a
hurried crowd estimate on leaky tasks), not a self-grade, and dodges the three
banned dek molds. Every subhead is a step in the piece's own nouns, none a
scaffolding slot, none a comma-and pair. Every `data-nb-kind` checked: the two
Microsoft posts, the four arXiv papers, Nangia & Bowman, and Bender & Koller are
primaries that own their claims; Gilbane is correctly the lone secondary,
third-party with no stake. The DeBERTa crossing carries an independent secondary;
the MT-DNN crossing rests on Microsoft's own dated leaderboard snapshot, primary
and acceptable. The mmlu Background link is a link plus one prose link, not
re-teaching. I did not re-open every href (proof already passed with links,
BLOCK 0); the s1 archived URL is the canonical target per the evidence note.

No break retired a claim. Nothing routed to the researcher.

## Cut

Six surgical changes, all prose, no markup touched.

Two signpost/self-grade removals. "and worth holding still to see" was a soft
"watch this" wrapped around the real payoff; the colon delivers "what got
averaged" without it. "Then the line it was measured against." was a transition
fragment announcing the next ingredient; the paragraph opens cleaner on "The
human baseline is a measurement, not a fixed ceiling." "So the honest reading is
the careful one" graded the reading instead of making it, and the sentence after
it makes the claim directly, so it went.

Three punctuation repairs toward the period default. One true comma splice
("Negation words tracked contradiction, vague hypotheses tracked entailment")
became two sentences. Two reflex semicolons joining independent clauses (the WNLI
floor/human pair, and the 33%/67% comparison where "instead" already carries the
turn) became periods.

Worst tell: none rose to a slop-level tell. The nearest thing was punctuation
reflex, semicolons and a splice standing in for the period the thoughts wanted,
now fixed. One thing I watched and let stand: the earned-contrast count sits at
the ceiling ("not one measurement / an average of nine," "a measurement, not a
fixed ceiling," "a shortcut rather than comprehension"). Each corrects a real,
named misconception that is the article's actual subject, so all three earn their
place; I flag the density only so a later round does not add a fourth. No
repeated paragraph-ending shape, no formula heading, no prompt leakage: the
"which tasks, whose baseline, what leaks" test is the article's own synthesis,
not lifted from the brief. Furniture (the annotation-artifact definition note,
the builders'-caveat blockquote, the two tables) each does deliberate work and
stays.

## Reader

Read straight through as the paper's declared reader (smart, widely read, no
codebase), the piece hands over something the nine sources do not give
separately: a working audit of a "human-level" claim, with the WNLI mechanism
staged so the reader watches a nine-task average clear the human line while the
model sits at chance on one ninth of it, plus the reusable three-question test.
That matches the draft-handoff's original-work sentence, and both answers
survive. The prose sits closer to the voice-guide exemplars than a median
summary: it grants the tempting reading its due ("Pretty good, if true"), stages
the reveal (the hidden-premise control, the COPA rebuild), and credits the
builders before showing the failure is structural, which is the Mitchell move the
guide asks for. The headline reads as the largest claim and the body defends it.

## Edits

- Cut "and worth holding still to see" from the orientation ("something more specific: what got averaged").
- Cut the transition fragment "Then the line it was measured against." opening the human-baseline paragraph.
- Changed a semicolon to a period: "majority-vote floor. Human annotators scored 95.9."
- Changed a semicolon to a period: "scores about 33%. The hypothesis-only model instead scored..."
- Fixed a comma splice: "Negation words tracked contradiction. Vague hypotheses tracked entailment."
- Cut the self-grading sentence "So the honest reading is the careful one."
- Ran `nb stamp`: words 1745 -> 1724, reading_minutes 8 -> 7, sources 9.

## Required work

None. No publication-blocking issue remains after the direct cuts.

## Decision

approve — every load-bearing claim, figure, date, and label checks against the
evidence, the "misled" is correctly located in reception and carried by a
primary, and the remaining issues were surgical prose fixes made directly.
