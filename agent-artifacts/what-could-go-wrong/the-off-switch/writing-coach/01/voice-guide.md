# Voice guide — what-could-go-wrong / the-off-switch

## Directive

Register: a teacher who has read the primary documents and trusts the reader to
follow real reasoning, not a verdict handed down. Smart, widely read, no ML
background — so mechanism gets built from scratch, but the reader's judgment is
never pre-chewed. Second person is fine at the level of "here is how to read the
next headline," never as a device to flatter or accuse the reader of a mistake
they haven't made yet.

Moves that change sentences in this piece:

- **Argue the strong case in its own logic, not a weakened echo of it.** When you
  state the instrumental-convergence chain (goal → subgoal of staying operational
  → resistance to being switched off), write it as its defenders derive it: premise,
  then premise, then the conclusion that follows. Do not smuggle in the rebuttal by
  hedging the premises ("might," "could arguably") before the test section arrives.
  A steelman that hedges itself isn't one. Save every qualifier for where the
  evidence actually earns it.
- **The proof line is a sentence-level habit, not a paragraph transition.** Every
  time you cross from what a paper showed to what it did not, write the fact first
  in its exact conditions (which model, which prompt, how many trials, who ran it),
  then a separate sentence for what that result does not establish. Two sentences,
  not one compound one. "Palisade found o3 sabotaged the shutdown script in 79 of
  100 trials" is a fact with its conditions attached. "Whether a model would do this
  without being handed a goal that rewards it is untested" is the boundary, and it
  earns its own sentence.
- **Attribute the setup, not just the result.** A shutdown-resistance number means
  nothing until the reader knows who supplied the goal, how the scenario was built,
  and whether the model was told the stakes. Write that detail into the sentence
  carrying the number, not into a caveat two paragraphs later.
- **Hold competing readings at equal weight through sentence length and certainty,
  not just content.** If you give the alarmed reading a full sentence with a named
  source and the skeptical reading a half-sentence aside, the imbalance is the
  argument, whatever the words say. Match their construction when the evidence
  itself doesn't yet favor one.
- **Let precision carry the calm, not softened language.** Exact figures, exact
  conditions, exact titles do the work that hedge words are usually drafted in to
  do. A flat declarative sentence stating a contested fact reads calmer than a
  question or a "some argue."
- **State the stake as a fact, never as a question.** A piece that already knows
  its answer does not ask a rhetorical one to raise tension.
- **No persona and no house catchphrase.** Vary how a section closes; a phrase
  built to be quotable is a tell whether it comes from the AI-doom side or the
  dismissive side.

Recently used, do not reuse:
- The desk has closed multiple pieces with some version of "the record runs out
  before the catastrophe" or "no working system has closed the loop." If the
  evidence in this piece lands on that same honest position, reach it in this
  article's own terms and its own sentence shape, not that wording, and do not
  open on it either.
- No colon-subtitle headline ("The Off Switch: ..."). No Betteridge question
  headline — this piece answers what it asks. No "X is not Y; it is Z" thesis
  sentence, here or anywhere else in the body. Vary heading cadence rather than
  repeating a comma-and-"and" join across headings.

---

## Ajeya Cotra, "Why AI alignment could be hard with modern deep learning"
Source: https://www.cold-takes.com/why-ai-alignment-could-be-hard-with-modern-deep-learning/
Craft:
- cadence: builds one mechanism at a time — first an intuitive case (a company
  run by an eight-year-old CEO who can only judge results, not process), then the
  technical mechanism it stands in for, then the range of ways it could resolve.
  No single paragraph tries to carry both the intuition and the technical claim.
- argument: names three possible kinds of model the training process could
  produce (one that wants what it looks like it wants, one with a proxy goal, one
  that is deliberately deceiving its evaluators) and treats each as a live
  possibility rather than picking a winner up front.
- evidence: distinguishes what deep learning has actually been shown to do
  (optimize for an unintended feature that correlates with the training signal)
  from what a much more capable system might do, and never lets the second borrow
  the first's certainty.
- stance: personal and dated, not oracular — closes with "my own view is fairly
  unstable" and states which way it currently leans and why, rather than
  resolving the question for the reader.
- notice: catches that the same word ("motivation," "goal") means something
  looser and more mechanical inside a trained model than in the analogy that
  introduced it, and flags the gap explicitly instead of letting the metaphor do
  silent work for the rest of the piece.
- diction: plain engineering vocabulary throughout — "search for a computer
  program," "the training signal," never a grander synonym once the plain one is
  set.
- reader: assumes intelligence and patience, zero prior ML — every mechanism is
  built from a starting analogy before the technical term is allowed to stand on
  its own.
- the move the axes miss: it maps the live disagreement itself as a structure —
  it lists the specific empirical or conceptual question each side would need to
  be right about, rather than summarizing "some people think X, others think Y."
  The disagreement becomes something the reader can track claim by claim.
Calibration: "My own view is fairly unstable, but currently, I'd guess... I place
significant weight on the pessimistic end."

## Paul Christiano, "Corrigibility"
Source: https://ai-alignment.com/corrigibility-3039e668638
Craft:
- cadence: short declarative definition first ("we say an agent is corrigible if
  it has these properties"), then each property gets its own short paragraph
  before the argument builds on all of them together.
- argument: two claims stacked in order of dependency — that a certain design can
  be made corrigible, and that a corrigible system tends to drift toward *more*
  corrigible and aligned rather than away from it. The second claim is explicitly
  marked as resting on the first.
- evidence: almost entirely reasoned from design properties, not from
  experiments, and the piece never dresses that reasoning up as empirical. It
  says outright where it is a claim about incentives rather than a result.
- stance: confident about the design argument, openly uncertain about whether it
  generalizes — the postscript states a numeric-flavored personal estimate
  ("50-50 odds") on a related question rather than asserting a settled view.
- notice: catches its own persuasive limits — "I don't expect this to be
  completely convincing, but I hope it can help my more pessimistic readers
  understand where I am coming from" — naming the argument's audience and its
  ceiling in the same breath.
- diction: technical terms (act-based agent, basin of attraction) are each
  defined at first use in a plain clause, then reused exactly, never swapped for
  a synonym.
- reader: a peer who disagrees, addressed directly and by name of position
  ("my more pessimistic readers") rather than a generic audience.
- the move the axes miss: it separates "this doesn't require special machinery"
  (a claim about what is buildable) from "I'm confident this generalizes" (a
  claim about the future), and never lets confidence in the first lend unearned
  confidence to the second.
Calibration: "This kind of corrigibility doesn't require any special machinery...
I don't expect this to be completely convincing, but I hope that it can help my
more pessimistic readers understand where I am coming from."

## Kelsey Piper, "The case for taking AI seriously as a threat to humanity"
Source: https://www.vox.com/future-perfect/2018/12/21/18126576/ai-artificial-intelligence-machine-learning-safety-alignment
Craft:
- cadence: opens on who is worried and why before a single technical claim
  appears, then moves in short numbered sections, each answering one plain
  question in the order a skeptical reader would actually ask it.
- argument: refuses to let the argument rest on a name. States what a serious
  researcher actually saw that worried them, not that a famous person is worried.
- evidence: keeps a visible seam between "this concern has been raised since the
  dawn of computing" (history of the idea) and "it has come into particular focus
  in recent years" (what specifically changed) — never merges the two into one
  claim of urgency.
- stance: takes a side while stating plainly that the field itself is split, and
  names the split by position rather than flattening it into "controversial."
- notice: catches that most public disagreement about AI risk is actually
  disagreement about different questions people don't realize they're answering
  separately, and restructures the piece around untangling that first.
- diction: no jargon without a plain-English restatement in the same sentence;
  numbers and named institutions stand in for vague authority ("researchers at
  Oxford and Berkeley," not "many experts").
- reader: a general, skeptical reader who has heard the headline claim and wants
  to know whether to believe it — addressed with "here's the big picture," an
  explicit promise of structure, not a rhetorical flourish.
- the move the axes miss: it treats confusion, not disagreement, as the thing to
  fix first — several of the reasons two informed people seem to disagree turn
  out to be that they mean different things by "AI," and naming that does more
  work than any single argument for or against the risk.
Calibration: "This concern has been raised since the dawn of computing. But it
has come into particular focus in recent years, as machine learning systems...
grew more capable."

## Senthooran Rajamanoharan and Neel Nanda, "Self-preservation or Instruction Ambiguity? Examining the Causes of Shutdown Resistance"
Source: https://www.alignmentforum.org/posts/wnzkjSmrgWZaBa2aC/self-preservation-or-instruction-ambiguity-examining-the
Craft:
- cadence: a ladder of experiments, each one changing exactly one variable from
  the last (add a warning, clarify instruction precedence, raise the stakes,
  remove the goal conflict) and reporting the compliance number at each rung
  before drawing any conclusion.
- argument: tests a specific published claim (models resist shutdown out of
  self-preservation) against an alternative explanation (the instructions were
  ambiguous about which goal took priority) by building the experiment that would
  tell the two apart, rather than arguing from priors about which is more likely.
- evidence: reports the model's own stated reasoning from its output as evidence
  for mechanism, not just the behavioral outcome, and treats that reasoning as
  data to be read carefully rather than as self-report to be trusted outright.
- stance: engages the original researchers as colleagues running a parallel
  investigation, not as a claim to debunk — names where its numbers diverge from
  the original study and offers a specific reason (prompt differences) rather
  than implying the earlier work was sloppy.
- notice: catches that a clean resolution in one engineered environment is not a
  license to generalize — "we do not claim these instructions are generally
  robust" — even though the piece's own numbers hit 100% compliance.
- diction: exact percentages and trial counts stand in every sentence where a
  vaguer magnitude would have done ("84%," "7%"), never "most" or "rarely."
  "Compliance" and "confounders" are the two technical terms and both get used
  the same way throughout, no synonym drift.
- reader: other researchers who will check the method, so every variable changed
  between experiments is named, not just the headline finding.
- the move the axes miss: it does not conclude by picking a side between
  "self-preservation" and "instruction ambiguity." It states exactly what the
  environment can and cannot distinguish and leaves the unresolved part
  unresolved, which is itself the honest finding.
Calibration: "While not ruling out self-preservation as a motivating factor, our
results reveal that this environment has too many confounders to provide
compelling evidence."
