# Editorial review: the-instruments/livecodebench (editor/01)

## Skeptic

Thesis: a LiveCodeBench score is a model's first-try pass rate on dated
programming-contest problems, and the release date on every problem does two
opposite jobs at once. It defeats contamination, because a model can be scored
only on problems published after its training cutoff, and it defeats
comparability, because every reported score sits on a different window and
version of a benchmark that keeps growing.

The claims it stands on, and how each held:

1. **Every problem carries a release date; a model can be scored only on
   problems after its training cutoff (Sec. 3.1).** Held. The paper's normalized
   cutoff rule is quoted in the evidence and stated faithfully in the body,
   including the honest detail that the cutoff is the maker's own published date
   or, absent that, the release date.

2. **The DeepSeek collapse, ~60 on May LeetCode problems to near zero on
   September ones (Sec. 5.1).** Held, and correctly attributed. This is the
   paper's base-model statement (DS-Base-33B). The body says "about 60 percent"
   and "close to none" and never names a chat/instruct figure, so it does not
   touch the unverified chat number the record flagged. The 19.4 later in the
   piece is labeled a base-model figure throughout, matching the record. No
   base/chat conflation in the prose.

3. **The comparability case: DeepSeek reports on 1 Aug – 1 Nov 2024, Qwen on Jul
   – Nov 2024, on different dataset versions.** Held. Both figures, both windows,
   and the base-model table (19.4 / 15.5 / 12.9 / 11.6) match the evidence
   exactly, and the piece draws the correct conclusion: the two numbers are
   measured on different tests.

4. **Six dated versions, 400 / 511 / 612 / 713 / 880 / 1,055 problems.** Held.
   Every count and window matches the GitHub evidence.

5. **The fix is imperfect: vendor-supplied cutoff, future reuse of contest
   problems, LeetCode-specific contamination.** Held and present, none sanded
   off. All three limits appear in "What the date rule still lets through," each
   sourced to its owning primary or the independent survey.

6. **Differentiation from the three published coding lessons by link, not
   re-teaching.** Held. HumanEval, SWE-bench, and Codeforces-rating are each
   linked with one differentiating line. The two Background link texts match the
   linked articles' live titles verbatim; all three internal targets exist in the
   published library.

Where a claim met its evidence and broke, and the fix:

- **The source asset (Fig. 1) shows a different DeepSeek model than the body's
  marquee number, and the caption did not say so.** The body's 60 -> ~0 is the
  base model, stated in the paper's text. Figure 1 plots the *instruction-tuned*
  sibling (DS-Ins-33B, whose LeetCode line bottoms near ~17 at its September
  release, not zero), plus GPT-4-O and two other models. The old caption ("A
  DeepSeek model and GPT-4-O score high... and fall sharply on problems released
  after") sat immediately under the near-zero paragraph and, by staying vague,
  invited the reader to read the figure as the base-model collapse it is not. The
  writer's handoff defends the vagueness as avoiding conflation; the vagueness is
  what produces it. Fixed in place: the caption now says exactly what the panel
  shows — four models, each higher before its training cutoff, with an
  instruction-tuned DeepSeek model's September release and GPT-4-O's November
  cutoff marked — and a body line now introduces the chart as the paper's plot of
  the same effect across several models. No new fact introduced; DS-Ins-33B as the
  instruction-tuned sibling is in the evidence record and labeled in the figure
  itself.

- **The caption and body over-claimed GPT-4-O's post-cutoff fall.** In the
  captured code-generation panel GPT-4-O rises from its November cutoff (~33) to
  December (~52) before trending down; it does not "fall sharply on problems
  released after." The paper's text does say GPT-4-O "drops on problems released
  since November," so the claim is sourced, but printed beside a figure that
  visibly bumps up it misreads. Fixed to the sourced-and-visible truth: GPT-4-O
  "scores well on problems released before November 2023... and lower on the ones
  released after," and the caption drops "fall sharply." The claim and the number
  are unchanged.

Citations: all eight source hrefs open as printed; s5 (the GitHub repository)
returns 403 through the proxy, which is gating, not dead — the repository is the
benchmark's real home and the versions cited are its documented releases. The
figure's data-nb-url resolves to the paper PDF page 2. The headline's "only"
slightly overstates the instrument (LiveCodeBench can score any window, and the
piece's own figure scores models on pre-cutoff months to expose the drop), but it
states the design principle the piece defends and the body explains the mechanism
fully; left as the standard, defensible framing.

## Cut

A dedicated slop pass plus the edge and delete passes. The prose is mostly
concrete and the figures carry the arguing, as the voice guide directs. What
failed and was cut or repaired, five sentences in all:

- **Signpost, "The clearest way to see contamination is to watch what the date
  rule catches."** A paragraph-opener that announced an example instead of making
  a claim; the worked case stands without it. Cut.

- **Signpost + reader-gesture, "A moving target has a price, and this is where a
  reader pays it."** Section opener that names a hypothetical reader (the lesson
  body speaks to no one; only the two bookends address the reader) and states
  nothing the next sentence does not. Cut.

- **Reader-gesture, "the reader who wants to know how clean has to ask which
  problems..."** Rewritten to drop the named reader: "how clean it is depends on
  which problems, from which site, dated by whom." The fact survives; the gesture
  does not.

- **Lecture-opener, "Start with the set itself."** A "Consider/Note"-class
  opener with no content; the version table follows the plain sentence after it.
  Cut.

- **Imperative reader-address, "Now watch two labs report one."** Rewritten to a
  claim that does the work the imperative dodged: "Two labs reporting a
  LiveCodeBench number for their models picked different windows to do it."

The pattern across these is a mild habit of reader-directed signposting leaking
into the body ("watch," "start with," "this is where a reader pays it"). The
general-you worked-example imperatives ("Hand it a single puzzle," "Set
DeepSeek's 19.4 beside a Qwen number") are a legitimate teaching device in this
voice and were left. Headings, dek, and furniture were checked against the
recent-pattern notes: no clone of the attack-success-rate heading sequence, no
comma-triad / suspended-question / semicolon-reversal dek, and the four subheads
are built four different ways. No negative-parallelism slop survived scrutiny —
the "looks like a fact / is really" and "nothing changed / what changed"
contrasts are earned against misconceptions the piece names. One consistency fix:
the version table read "1 055" while the prose read "1,055"; standardized to
"1,055."

## Reader

Read straight through as the paper's reader — sharp, widely read, never ran a
benchmark — the piece hands over something the sources alone do not: the single
mechanism (the release date) tied to both of its consequences, and a portable
rule for reading any LiveCodeBench figure (name the window, the version, and
whose cutoff decided what counted). The paper, the two vendor reports, and the
survey each hold a piece of that; none welds them into the causal chain or the
reading rule. That matches the draft-handoff's original-work claim, and both
answers survive: the reader leaves able to say why a moving cutoff fixes
contamination and complicates comparison in the same move.

The prose sits closer to the voice-guide exemplars than to a median summary. It
pairs every figure with its conditions the way Luu pairs 16ms with 240ms (19.4
never appears without its window, scenario, and shot count; 60 never without May
against September), it holds its verdict to what the evidence shows the way Evans
does with her 17 centimeters ("more trustworthy is not clean"), and it spends its
words on the one limitation that matters rather than listing ten, as Bergstrom
and West do. The headline, read last as the largest claim, commits to the
mechanism the whole lesson defends.

## Edits

- Rewrote the Fig. 1 caption to state exactly what the panel shows (four models,
  each higher before its training cutoff; an instruction-tuned DeepSeek model's
  September release and GPT-4-O's November cutoff marked), removing the vague "A
  DeepSeek model" and the unsupported "fall sharply on problems released after."
- Rewrote the figure alt text to match (instruction-tuned DeepSeek model marked
  at September, GPT-4-O at November; dropped "dropping sharply").
- Softened the figure's data-nb-note from "collapses at each model's cutoff" to
  "steps down around each marked model's cutoff."
- Rewrote the post-figure paragraph: introduced the chart as the paper's plot
  across several models, and changed GPT-4-O "drops on the problems after it" to
  "lower on the ones released after" to match the visible, sourced trend.
- Cut the signpost opener "The clearest way to see contamination is to watch what
  the date rule catches."
- Cut the signpost/reader-gesture opener "A moving target has a price, and this
  is where a reader pays it."
- Rewrote "the reader who wants to know how clean has to ask..." to "how clean it
  is depends on..." (removed the named reader).
- Cut the lecture-opener "Start with the set itself."
- Rewrote "Now watch two labs report one." to "Two labs reporting a LiveCodeBench
  number for their models picked different windows to do it."
- Standardized the v6 problem count in the version table from "1 055" to "1,055".

## Required work

None blocking. All findings were fixable in place and were fixed.

- writer (optional, non-blocking): the source asset is the paper's
  code-generation panel of Fig. 1, which plots the instruction-tuned sibling, not
  the base model behind the body's 60 -> ~0. A recrop cannot separate the
  overlaid model lines, and the paper publishes no base-model chart, so the honest
  caption above is the resolution and no re-capture is requested. Noted only so the
  provenance is on the record when the proof is re-run.

## Decision

approve — the claims hold against their primaries, the citations resolve, the
figure now says exactly what it shows, and the reader-directed slop is cut; every
required change was within editing reach and is done.
