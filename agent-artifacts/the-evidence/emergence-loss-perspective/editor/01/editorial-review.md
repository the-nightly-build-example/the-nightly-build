# Editorial review: the-evidence/emergence-loss-perspective (editor/01)

## Distinctness (the reason this article exists)

Read the published lesson the-evidence/emergent-abilities ("The sudden jump in AI
benchmarks was mostly in the scoring") in full via `nb history --show`. This lesson
is genuinely distinct and does not re-teach it.

- The published lesson owns Wei's definition, Schaeffer's metric-artifact rebuttal,
  the exact-match-versus-token-edit worked example (the 74510 table), the
  (1-e)^L arithmetic, and the BIG-Bench meta-analysis (92%, 39 metrics, 5). None of
  that machinery is reproduced here.
- This lesson states the mirage result in a single sentence and links the published
  lesson twice: as Background row 01 and in prose ("This desk walked through that
  rebuttal in full"). The one restatement of Schaeffer's mechanism in the
  axis-not-ruler section is one sentence built for contrast, not a re-teaching.
- The body is centered on Du 2024's own material: pre-training loss as an axis, the
  loss-versus-size finding, the ~2.2 threshold on four hard tasks, persistence under
  two continuous metrics, and the Brier random-baseline caveat. This is new ground.

Distinctness passes. Not a blocking finding.

## Skeptic

Thesis: Du 2024 answers the mirage rebuttal not by changing the metric but by
changing the x-axis; plotted against pre-training loss, four hard tasks sit at
chance until loss falls below about 2.2 and then climb, and the threshold survives
continuous metrics, though the debate stays open because Du and Schaeffer never
grade the same tasks and Du's Brier reading leans on a random baseline.

The claims it stands on, and how each held:

1. Loss, not size, tracks ability (models of different sizes at equal loss perform
   alike). Confirmed against the evidence record (Du Sec. 2) and the Du abstract,
   which I opened.
2. Four tasks (MMLU, C-Eval, GSM8K, GSM8K-Chinese) stay at chance until loss ~2.2
   while the other eight of twelve rise from the start. Matches the evidence record's
   Numbers entry exactly. The 30+/300M-32B/12-task figures in the stat strip and the
   prose match the record; LLaMA and Pythia named correctly.
3. Threshold persists under CorrectChoiceProb and Brier Score. Matches the record
   (Du Sec. 3.2) and the paper's abstract. The "In the paper's words" blockquote is
   a verbatim match to the evidence record's Sec. 3.2 quote.
4. Debate stays open: the 0.75 four-option Brier baseline, the different-tasks/
   different-models point, and Wei's stated response. Each matches the record's
   Contradictions section, and I verified Wei's arithmetic point and Miranda's two
   quoted lines against the live sources.

Display text checked descriptor by descriptor. Headline and dek make accurate,
defended claims and avoid the banned "the paper got its own X wrong" mold. Subheads
are all argument steps in the piece's own nouns, no scaffolding slots. The dek is one
sentence and clears the three banned molds (no semicolon reversal, no suspended
question, no comma triad).

Citations: opened all six source hrefs as printed. Each lands on the correct source
and supports what it is cited for: Du (s1, arXiv 2403.15796), Wei (s2), Schaeffer
(s3), the NeurIPS 2023 awards page listing the mirage paper as Outstanding Main Track
(s4), Wei's blog with the 15+23=38 exact-answer argument (s5), and the AIhub Miranda
interview with both quoted lines (s6). The two internal Background links
(emergent-abilities.html, scaling-laws-kaplan.html) both resolve to published articles
in the library. data-nb-kind labels audited: 4 primary, 2 secondary, meeting the
series floor; the Wei blog is correctly primary-for-his-own-position and the two
secondaries (award page, interview) establish fame and framing, not truth.

One break, fixed directly: the orientation paragraph named the third author "Wenyi
Dong." The owning primary (arXiv citation_author metadata and the abstract page) gives
"Yuxiao Dong." The evidence record and commission both abbreviate to "Dong" without a
first name, so the record and the primary do not disagree; the draft's "Wenyi" matched
neither. Corrected to "Yuxiao Dong" against the primary. This is a factual error in a
named person that reached display-adjacent body text; flagging it as a writer accuracy
lapse even though it is now fixed.

## Cut

Made a dedicated slop pass over body, headline, dek, subheads, captions, and
furniture prose, then walked the edges and ran the delete test.

Cuts and rewrites:

- Recast "The reader who does not open it needs only its one-line result: ..." This
  gestured at a hypothetical reader (barred in the body outside the bookends) and
  lifted the writer brief's framing almost whole ("The reader who does not open the
  link must still follow"). Prompt leakage plus a body reader-gesture. Rewrote to
  state the required mirage one-liner directly ("Its result, in one line: ...")
  without the instructional scaffolding.
- Trimmed "and it is worth being exact about where the two moves differ" from the
  axis-not-ruler opener: a method-signpost that announced what the piece would do
  next and carried no fact.
- Cut "That is the crux of the reply." A signpost grading the argument's importance;
  the paragraph now opens on its actual content.
- Removed the closing Verdict note (see Required work / decision): it restated the
  finding as a body closer, which the press bans, and duplicated both the section's
  own last sentence and the takeaway.

Three sentences failed the slop test and were cut or rewritten; the leaked sentence
is the pattern worth naming, since its phrasing tracked the brief rather than the
reporting. The rest of the prose holds: the negative-parallelism instances ("rests on
X, not on Y" in the baseline paragraph) are earned, correcting a misreading the
paragraph just built. Teaching imperatives ("Keep two things apart," "Line up all
twelve tasks") and the generic "a reader new to this" match the accepted register of
the published sibling lesson and are not held to a stricter bar here. The mid-body
"In the paper's words" note and the stat strip and task table each do deliberate work
and stay.

Note (not edited): the Why-this-matters opener ends on three "you will..." learning
outcomes. This is what the template requires the opener to state and is not the banned
enumerated-roadmap form ("This lesson explains X, Y, Z" / "First... Then... Last"), so
I left it; recording it since the commission flagged the roadmap tic.

## Reader

Read straight through as the paper's declared reader. What the piece gives beyond its
sources: the recognition that Du's real move is the horizontal axis, not the metric,
and a weighing that holds the loss-threshold finding against Du's own random baseline
and the never-the-same-tasks fact, landing that emergence is real on the loss axis for
Du's tasks and unproven as a general law. No single source performs that reframing or
weighing; each states only its own paper's claim. This matches the draft-handoff's
original-work sentence, and both answers survive. The prose sits closer to the
voice-guide exemplars (Harford's resized figures, Luu's fix-the-measure-first, Yong's
fair statement of both sides) than to a median summary: numbers carry baselines, the
loss axis and the "ruler" are named once and reused, and neither side is tipped early.
The headline holds as the largest claim.

## Edits

- Corrected author name "Wenyi Dong" to "Yuxiao Dong" against the owning primary.
- Rewrote the leaked/reader-gesture sentence in the orientation section to state the
  mirage one-liner directly.
- Cut the method-signpost clause "and it is worth being exact about where the two
  moves differ."
- Cut the signpost "That is the crux of the reply."
- Removed the closing Verdict note (nb-note nb-note-strong) from the unsettled
  section.

## Required work

- orchestrator: re-stamp and re-run the proof. The edits changed prose, removed a
  furniture component, and lowered the word count (the Verdict note and three
  clauses are gone), so the stamped words/reading-minutes counts are now stale.
  Confirm the proof still returns BLOCK: 0 with links included. No researcher or
  writer work is outstanding: no evidence gap, no broken central claim, and every
  figure verified against the record and the primaries.

## Decision

approve, with an orchestrator re-stamp and re-proof: every blocking issue (the wrong
author name and the press-barred closing Verdict note) is resolved by direct edits,
distinctness from the published mirage lesson holds, and nothing needs new reporting
or a redraft.
