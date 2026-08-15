# Editorial review: the-mechanics/repetition-loops (editor/01)

## Skeptic

The thesis is a backward descent: a model's repetition loop is a property of the
decoding rule, driven by a measured self-reinforcement effect (a phrase that has
appeared becomes likelier to appear again), while the deepest step, why a trained
model favors its own recent words at all, is genuinely unsettled. The piece rests
on five claims, and I tried to break each by opening its owning source as the
article prints it.

- **Headline / self-reinforcement (a repeated phrase makes a model likelier to
  repeat it again).** Holtzman's Figure 4 caption states it in those terms, and
  Xu et al. reproduce it on modern LMs: probability of repetition rises "almost
  monotonically" toward a ceiling, and IP1 exceeds 90% across corpora (the
  article's "more than nine cases out of ten"). Two independent primaries. Held.
- **Dek / decoding contrast (loop under greedy and beam, not under sampling).**
  Verified against Holtzman Table 1, Repetition% column, exactly: Greedy 73.66,
  Beam b=16 28.94, Top-k=640 0.28, Nucleus p=0.95 0.36, Pure sampling 0.22, Human
  0.28. The table in the article reproduces all six with the right rows. Held. The
  contrast is a real, measured distinction, not an invented one, so grouping
  greedy+beam against sampling is fair (28.94 and 73.66 against 0.36 and 0.22).
- **Open cause (Welleck's likelihood objective vs. Fu's high-inflow structure).**
  Welleck: "the likelihood objective itself is at fault, resulting in a model that
  assigns too much probability to sequences containing repeats and frequent
  words." Fu: repetition traced to "too many words predicting the same word... with
  high probability," dubbed the high-inflow problem, argued as a trait of language
  independent of objective and demonstrable in a Markov generator. Both open as
  printed; neither reduces to the other. Held as contested.
- **Fixes mapped to steps.** Fan top-k=10 and "beam search... tends to produce
  common phrases and repetitive text from the training set": verified. Keskar
  penalized sampling theta about 1.2 on the 1.63B CTRL model: verified. Welleck
  Wikitext-103 numbers (seq-rep-4 0.442 -> 0.013 vs human 0.006; token rep 0.627
  -> 0.559 vs human 0.487): verified exactly. HuggingFace no_repeat_ngram block
  and Weng's decode-vs-train survey framing: both verified. Held.

Display text audited descriptor by descriptor. Headline, dek, and all five
subheads carry only claims the body establishes; no false label. Named people
(Holtzman, Welleck, Fu, Xu, Keskar, Fan) are attributed to the work they own.
Every quantity in display text and captions traces to its owning primary.

Source labels audited against the primary/secondary test: six primaries (Holtzman,
Fan, Xu, Welleck, Fu, Keskar), each the owner of the mechanism claim it carries;
two secondaries (von Platen/HuggingFace, Weng), each explanatory. Labels correct.
Count meets policy: 8 sources, 6 primary, 2 secondary.

Every citation href opened as the article prints it. All resolve to the source
itself: the six arxiv.org/abs pages land on the correct papers, the HuggingFace
and Lilian Weng posts land on the cited write-ups, and both Background links
(sampling-temperature.html, autoregressive-generation.html) resolve in the
library, their link text matching each lesson's actual published title. The inline
"Top-k sampling" link points to sampling-temperature.html, which does teach top-k.
No break found; no miscitation to fix.

## Cut

Ran the sentence-by-sentence slop pass, then the edges, then the delete test.

- **Throat-clearing clause, cut.** In the fixes section, "and it is worth being
  clear about what it does" announced an explanation instead of giving it; the
  next two sentences do the work. Removed.
- **Reflex semicolon, repaired.** "...ignores the rest; Fan's story model drew
  from k of 10" joined a definition to an appended example where a period does the
  job. Changed to a period. The two remaining semicolons (the loop nearly
  vanishes; ... / a decode-time rule decides whether the loop is entered at all;
  ...) are tightly-bound parallel contrasts and stay.

No sentence failed the delete test outright beyond the throat-clear above. The
edge sentences that read like punchlines all survive on content: "Two independent
groups, different models, the same shape: that the loop feeds itself is settled"
carries the settled-from-replication point the whole settled-vs-open spine depends
on; the fixes-section closer references Welleck's real numbers. Negative
parallelism is limited to two earned instances ("This is not the model running
dry" corrects the named misconception that repetition means the model ran out of
things to know; the two "rather than" clauses are real contrasts, not strawmen).
No em-dashes. Punctuation counts passed the proof.

Checked against the recent-pattern notes. The "Why this matters" opener does not
use the "by the end you will be able to" formula; it hooks on the behavior the
reader has watched and previews the three findings in this lesson's own
particulars. The takeaway does not land on a short flat one-liner; it resolves the
opener's three-part setup and ends on the open question, in this behavior's terms.
The headline avoids the recent comma-continuation and "X, not Y" molds. The dek
clears all three warned molds (no semicolon reversal, no comma triad, no suspended
question); it is a two-clause compound stating two real findings and does not
restate the headline. The five subheads are each a step of the argument in the
piece's nouns, varied in build, none a scaffolding slot.

Checked for leakage against commission, brief, and series prompt: no lifted
planning language, no "settled engineering vs open" phrasing copied, no claim that
the article fulfilled its assignment. The bookends' self-reference is the
template's documented allowance. Checked distinctive phrasing against the
voice-guide exemplars: the "point below which the accounts diverge" adapts the
Harris "reach ground and stop" structure the voice guide instructs the writer to
use, in the article's own nouns, not a borrowed clause.

Furniture: bookends, one table, one note. All documented, all doing work. The note
label ("The feedback loop, stated by the authors") names its move and carries the
Figure 4 quote with attribution. Nothing reads as a stack of blocks.

## Reader

Read straight through as the paper's reader (smart, widely read, no codebase).
What I have that the sources alone would not give me: one ordered causal chain
that no single paper holds, from the loop on the screen down through the decoding
rule and the measured self-reinforcement to the open question of why, with each
fix pinned to the exact step it reaches and a clean line drawn between what is
settled (the loop feeds itself, two independent measurements) and what is
contested (why the model leans on its own output). The draft-handoff's
original-work sentence claims exactly this synthesis, and the article delivers it.
Both answers survive, so the piece teaches rather than restates. The prose sits
with the voice-guide exemplars, not a median summary: plain sentences, one real
part each, the concrete named before the abstract, the settled/open boundary
stated flatly in Luu's manner, the descent ending at its bottom in Harris's. The
headline read as the largest claim is the piece's most-defended and
double-sourced finding.

## Visual evidence

Decision on the self-reinforcement figure (brief's third focus item): no source
asset requested. Holtzman's Figure 4 would show the rising curve well, but the
evidence records that the papers parsed only as ar5iv HTML, so a clean crop was
not reliably capturable, and there is no numeric series to build an honest chart
from. Step 3 is already carried twice: the authors' Figure 4 statement quoted in
the note, and Xu's independent measurement ("more than nine cases out of ten," a
near-monotonic climb toward a ceiling). The mechanism (probability rises with each
repetition; greedy has no exit, sampling can still draw outside the phrase) is
clear in prose. A visual would not let the reader test the argument better than
what is on the page, and requesting one would force a fresh capture pass of
uncertain yield. Not required to publish.

## Edits

- Cut "and it is worth being clear about what it does" from the repetition-penalty
  paragraph (throat-clearing that announced rather than explained).
- Changed the semicolon after "ignores the rest" to a period (reflex semicolon;
  period does the job).

## Required work

None. No item routed to researcher, writer, or orchestrator.

## Decision

approve. Every figure and citation verifies against its opened source, the
settled-vs-open boundary and the no-stacked-scales handling meet the brief's
focus, the recent-pattern molds are avoided, and the two direct edits resolved the
only prose issues; no visual is required.
