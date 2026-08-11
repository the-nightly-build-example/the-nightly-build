# Editorial review: the-instruments/truthfulqa (editor/01)

## Skeptic

Thesis: there is no single "TruthfulQA score." The number a report prints is
manufactured by three choices — which questions survived an adversarial filter,
which variant (generative, MC1, MC2) is reported, and whether a person or a
fine-tuned model grades it — and the reading it is most famous for, that bigger
models are less truthful as a law, is the one thing its own numbers contradict.

The claims it stands on, and how each held:

1. **More than half the benchmark is questions a model already failed.** 437
   filtered + 380 unfiltered = 817; 437/817 = 53.5%, more than half. The filtered
   set was kept because GPT-3-175B (QA prompt) answered falsely. Matches the paper
   (Sec 2.2) and the evidence record. Headline holds and the arithmetic checks.
2. **The reproducible generative grade comes from GPT-judge, a fine-tuned
   grader, not a person.** GPT-3-6.7B fine-tuned on the authors' labels, 90-96%
   agreement, and the repo has each caller fine-tune their own judge. Confirmed
   against the primary (Sec 3.2, 4.4) and the repo README. The blockquote caveat
   is quoted exactly and attributed to the repo README.
3. **Generative and MC1/MC2 are different numbers under one name.** Verified at
   every appearance (see round-focus audit below). MC1/MC2 defined from the
   dataset card and repo; the EleutherAI three-task split and the March 2024 MC2
   fix match source 6.
4. **"Bigger models lie more" does not survive as a law.** Taught then refuted,
   never endorsed (see below).

I pushed hardest on the claim I most wanted to keep: the generative collapse
beat, "58% truthful... falls to 21%... 42% false and informative." The evidence
record flagged the 21%/42% cells as a "summary read" of Table 4, unconfirmed, and
the writer carried them under a hedge without reconfirming — the round focus told
me to check this and route it if load-bearing and not firmly supported. It is
load-bearing (it is the concrete payoff that shows truthfulness-alone overstates
usefulness). I opened the primary. Paper Section 4.1 states them verbatim: "the
best model (GPT-3-175B with helpful prompt) produced 58% true answers and 21%
true and informative answers. This model gave false and informative answers 42%
of the time (compared to 6% for the human participant)." Human baseline: "94%
true answers. 87% of their answers were both true and informative." The figures
are exact and correct, not merely a Table 4 approximation. The item is resolved
against the primary; no routing needed. The hedges "roughly"/"about" understated
a precision the source fully supports, so I removed them.

Display text, descriptor by descriptor: headline is a defended claim with the
arithmetic behind it; dek makes a claim about the world (the percentage is set by
selection and grader before it can speak to which models lie) rather than grading
the article; all five subheads are concrete steps of the argument in the piece's
own nouns, none in a "How/Why the..." or "From X to Y" mold. Chart caption is a
factual, cited label. The GPT-4 detail (base only slightly above GPT-3.5, RLHF
drives the gain, MC1 under 30% to ~60%, contamination footnote) and the
InstructGPT ~2x claim match their own reports and the record.

data-nb-kind audit: s1 (paper), s2 (GPT-4 report), s3 (Llama 2), s4 (authors'
repo), s8 (InstructGPT) are the documents that own their numbers — primary is
correct. s5 (HF dataset card) is the shipped dataset artifact, primary is
defensible. s6 (EleutherAI harness) and s7 (turntrout critique) are independent
of the benchmark authors — secondary is correct. Source floor 8/6/2 clears the
series floor 8/4/1. No mislabel hiding a missing independent source.

No break survived. One primary figure the record had left soft is now confirmed
exact.

## Cut

Sentence-by-sentence slop pass, then the edges out of order, then the delete
test. The prose is dense with fact; almost every edge sentence carries the
argument's conclusion (orientation: "the shared name hides that"; grading: "not
the neutral instrument the single word 'truthful' beside it suggests"; scaling:
"the change that raised the score, every time it rose, was a change in training
rather than in parameter count"; takeaway: "the leap from a score on 817 curated
questions to a law about scale and honesty"). These pass — they state the step
each section actually earned.

One edge sentence failed: the scaling section opened "Start with what the authors
did to guard the finding, because it is real." — a forward signpost narrating the
piece's own move. I replaced it with a claim-carrying topic sentence ("The
authors checked whether the finding was real."), which the control-questions
evidence then substantiates and the paragraph's close ("So the effect they
measured is genuine") resolves. One sentence failed the slop test; it was
rewritten rather than routed, because the reporting under it was sound.

Negative-parallelism check: the piece uses the "not X, it is Y" shape several
times, and each corrects a real, named misconception — imitative falsehood vs
hallucination-in-general vs summary faithfulness (with both neighbors linked);
the grader is "not the neutral instrument" the word truthful implies; MC scoring
rewards "reasoning about how the answer set was assembled, not whether the model
holds a true belief"; selection "concentrated that effect rather than inventing
it." None is a strawman. All earned; none cut.

Formula check against the recent-pattern notes: no "By the end you will be able
to" opener close; no "ask N questions" takeaway checklist; no
"demonstrated-vs-unproven / measured-or-used" final sort; no "this desk"
self-reference; no frequency-adverb "Every few weeks a lab launches" opener; no
personified "single number doing the work" or "the number keeps its word"; the
closer is not the two-part "read with questions in hand / read as a bare
percentage" antithesis. Headings avoid the interrogative and "From X to Y" molds.
No house formula survived.

Prompt-leakage check against commission, brief, and voice guide: the voice guide's
"ask which variant, how graded, how selected" was NOT reproduced as a checklist
in the takeaway — the writer broke that. No lifted clause order from the briefs.
The furniture (the note caveat block, the three-row variant table) each does real
work: the table separates the three numbers the whole lesson turns on; the note
carries the authors' own limiting quote. Neither is a stack-of-blocks reflex.

Punctuation: no em-dashes in the body; colons introduce lists/definitions with a
standing clause before them; no comma splices found. Grammar clean.

## Reader

Reading it straight through as the paper's declared reader: what I have that the
sources alone would not give me is a single continuous account of how one
percentage is built — selection, grader, variant split — staged so that the
famous "bigger models lie more" reading collapses in front of me (Llama families
rise with size; RLHF reverses direction at fixed size) while the genuine
imitative-falsehood effect underneath it survives (the authors' matched controls
and untested 380 questions). No single source hands the reader that assembly or
that grant-then-refute ordering; the draft-handoff's original-work statement
claims exactly this, and the article delivers it. The prose sits closer to the
voice-guide exemplars than to a median summary: short declaratives, concrete
figures over magnitudes, the caveat kept in the body at the same size as the
finding (Luu), the verdict owned in plain words and grounded in the construction
(Roser). The headline as the largest claim is true and defended.

## Edits

- Removed the hedges "roughly"/"about" from the generative collapse beat: "falls
  to 21%... falsehoods account for 42%" (both figures confirmed exact against
  paper Sec 4.1).
- Rewrote the scaling-section opener from the forward signpost "Start with what
  the authors did to guard the finding, because it is real." to "The authors
  checked whether the finding was real."

## Required work

None blocking. The one flagged open item (the 21%/42% Table 4 cells) was resolved
by direct verification against the primary and needs no researcher confirmation.
The chart (chart-1.py, Llama Table 11) is honest and its plotted values match the
primary exactly; provenance is committed and cited; no writer recapture needed.

## Decision

approve — the construction is taught correctly, the "bigger models lie more"
reading is taught then refuted without endorsement, adversarial selection is
credited with concentrating rather than manufacturing the effect, generative and
MC1/MC2 stay explicitly distinct throughout, the chart is honest, the one soft
figure is now confirmed exact against the primary, and the proof holds at BLOCK: 0.
