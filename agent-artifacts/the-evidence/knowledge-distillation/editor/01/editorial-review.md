# Editorial review: the-evidence/knowledge-distillation (editor/01)

## Skeptic

Thesis: the 2015 Hinton, Vinyals, and Dean paper defined knowledge distillation
as one precise thing, training a small student on the teacher's full
temperature-softened probability distribution, demonstrated it on MNIST and
speech, and the word has since broadened into a family of teacher-student
methods, much of which drops the soft-target mechanism the paper measured. The
piece stands on four claims, each tested against the owning primary.

Claim 1: the method copies the whole probability distribution, not the top
label, and temperature spreads the tiny informative probabilities so they can be
learned from. Held. The soft-targets section states it correctly against Bucila
2006 (label-copying) as the contrast, and the "In the paper's words" note quotes
the BMW / garbage-truck / carrot passage verbatim against the evidence record and
the paper. The temperature gloss ("divide the scores by a number, T... a larger T
spreads the distribution out") matches the paper's softmax-at-T.

Claim 2 (headline): the MNIST student recognized a digit it was never shown.
Held on the honest figure. 67 / 146 / 74 test errors all match the paper; the
never-saw-a-3 result rests on the un-nudged 877 of 1,010 (86.8%), and the 98.6%
(996 of 1,010) is printed with its manual-bias caveat ("The headline figure
needed that manual nudge"). The headline therefore stands on the un-nudged
result, as the round's focus required.

Claim 3: the largest experiment (JFT) never distilled anything. Held and framed
correctly. The section presents JFT as the 61-specialist ensemble result (25.0 to
26.1 percent, specialists in days against the baseline's ~six months) and states
plainly that the specialists were not distilled back into one net, matching the
paper's own "we have not yet shown" sentence. No overclaim that the small net
learned from the big one here.

Claim 4 (drift): distillation became a family of methods, DistilBERT keeping the
mechanism and DeepSeek-R1 keeping only the name. Held in the narrow, sourced
form. Kim & Rush 2016 is given as the early peer-reviewed broadening (hard
targets, still called distillation); the Gou survey as the three-category
taxonomy with soft targets one of three; the DistilBERT (40% smaller / 60% faster
/ 97% retained, keeps soft targets) versus DeepSeek-R1 (800k generated samples,
SFT only, no soft targets, no temperature) contrast draws the gap between two real
cases rather than a blanket "everyone misuses the word."

Framing guardrails all held: "dark knowledge" appears nowhere (the idea is taught
as "soft targets" and "relative probabilities of incorrect answers"); JFT is not a
completed distillation; the drift does not overreach into blanket misuse.

Speech figures (58.9 / 61.1 / 60.8 frame accuracy; 10.9 / 10.7 / 10.7 WER; ~2,000
hours, 14,000 states) all verified against the evidence record. Bucila (~1000x
smaller and faster), the survey, and the IBM definition all match their entries.

One break found. The MNIST prose said the distilled net's 74 errors were "less
than half the small network's original mistakes." Half of 146 is 73, so 74 is
just over half, not under it. The figures (146, 74) are already in the article, so
I corrected the characterization to "about half" directly rather than routing it.

Citations: all seven `data-nb-kind` labels are correct (Hinton, DeepSeek-R1,
Bucila, Kim & Rush, DistilBERT primary; Gou survey and IBM secondary), meeting the
6-source / 3-primary / 1-secondary floor with margin. I opened all seven source
hrefs plus the two Go-deeper links as printed: each lands on the source itself
(the five arXiv abstract pages resolve to the correct titled papers, the Cornell
URL serves the Model Compression PDF, the IBM page is Bergmann's explainer). The
two in-body cross-links (`../the-mechanics/sampling-temperature.html`,
`../the-evidence/deepseek-r1.html`) resolve inside the library, and the Background
row titles match those articles' live headlines word for word.

## Cut

The prose is disciplined and largely clean. Sentence-by-sentence and edge passes
turned up no slop sentence that survives the placeholder test empty: the edges
carry facts or a reasoning step (the JFT closer names a real point, the speech
"end to end at real scale" line does structural work setting up the JFT contrast).
The negative-parallelism instances are earned against misconceptions the piece
actually names (Bucila copied the label / Hinton copies the distribution; JFT is
"an ensemble result, not a distilled one," which is the corrected framing). No
borrowed phrasing from the voice-guide exemplars (no France sentence, cheese
festival, coordinate analogy, or "weighing up evidence"); the worked cases are the
article's own and the paper's. No prompt leakage: the DistilBERT/DeepSeek
"method / name" split is the evidence's substantive finding, not a lifted planning
label, and the reader's-situation lines in the opener report a real fact about the
DeepSeek moment.

Against the recent-pattern notes: the "Why this matters" bookend does not reach
for the "will be able to... by the end" catchphrase; the close is in this paper's
own particulars ("the useful question is which of those two things it means"), not
the semicolon matched-split shape of the last the-evidence piece; the headline is
a direct subject-verb finding, not a comma-continuation or "X, not Y" mold; the
dek supplies author, method, and the drift without restating the headline and
avoids the semicolon-reversal, comma-triad, and suspended-question dek molds. No
cuts were needed on this pass.

Furniture: on the writer's flagged question (MNIST tabled, speech left in prose), I
judged the speech comparison the harder case, not the easier one. It is a
three-system, two-metric result, six figures carried in a single prose sentence,
and the evidence record marks exactly this comparison as the clearest single-view
proof the method transfers ensemble knowledge. The simpler three-number MNIST
result already gets a table, so leaving the denser speech comparison in prose was
the inconsistency. I added a parallel `nb-table` (baseline / ensemble / distilled
against frame accuracy and WER) built only from figures already in the article and
evidence record, with a factual cited caption. The prose is unchanged, matching the
MNIST section's prose-plus-table pattern.

## Reader

Read straight through as the paper's declared reader: what I have that no single
source gives is the precise original method worked with real numbers, the honest
scale (the largest experiment is the one where distillation was never run), and a
usable test for reading any modern "distillation" claim, does it keep the soft
targets like DistilBERT or only the name like DeepSeek. That matches the
original-work sentence's promise (a reader's test plus a reordering that puts scale
honesty on JFT and the proof on MNIST), and the article delivers both. The prose
sits closer to the voice-guide exemplars than a median summary: short declaratives,
terms defined at first use (softmax, temperature, teacher and student, soft and
hard targets), and the reasoning handed over a step at a time. The headline as the
largest claim is true on the un-nudged figure.

## Edits

- Corrected "less than half the small network's original mistakes" to "about half"
  (74 of 146 errors is 50.7%, not under half).
- Added a speech-recognition `nb-table` in the scale section (baseline / ten-model
  ensemble / distilled single network, columns for frame accuracy and word error
  rate), using figures already in the article and a factual cited caption. Prose
  left intact.

## Required work

None. Both fixes were made directly from material already in the article and
evidence record; no researcher or writer reporting is needed. The orchestrator
stamps and re-proofs after these edits.

## Decision

Approve. Every load-bearing figure verified against the owning primary, every
citation href resolves to its source, the round's framing guardrails held, and the
two defects (one arithmetic characterization, one missed table) were repairable in
place.
