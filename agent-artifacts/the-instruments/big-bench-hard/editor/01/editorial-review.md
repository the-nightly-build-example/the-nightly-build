# Editorial review: the-instruments/big-bench-hard (editor/01)

## Skeptic

Thesis: one model-card percentage (Claude 3 Opus, 86.8% on BBH) rests on three
hidden constructions — BIG-bench's collaborative assembly, the 23-task filter
against an average expert-rater bar, and the chain-of-thought setting — and the
same card row lists GPT-4 at 83.1%, a figure OpenAI itself withheld for
contamination and a rival (Google) published, so a row read as a head-to-head is
not one for that figure.

The claims it stands on, and how each held:

- **"OpenAI withheld GPT-4's BBH score, and a rival published one anyway"
  (headline).** Held. OpenAI's GPT-4 report excludes BIG-bench for contamination
  and prints no BBH score; the Claude 3 card lists GPT-4 at 83.1% and footnote 7
  attributes it to Google's Gemini report. Verified against both primaries (s5,
  s1). Actors named, present-tense claim the piece defends. No colon-subtitle
  tell.
- **Dek: the 83.1% came from Google's report; the tasks behind it had reached
  GPT-4's training data.** Held. The provenance is exact (footnote 7). "The
  tasks behind it had already reached GPT-4's training data" is a fair
  compression: OpenAI found "portions of BIG-bench" in training and excluded the
  whole benchmark as compromised, and BBH is drawn from BIG-bench. The dek makes
  a claim about the world (not a method grade) and adds what the headline omits
  (the number, the card, the contamination reason). No banned dek mold (two
  coordinated clauses, not a comma triad or semicolon reversal).
- **204 tasks / 450 authors / 132 institutions (BIG-bench).** Held; matches the
  BIG-bench abstract (s2), which I opened.
- **23-task funnel 209 -> 78 -> 36 -> 23.** Held; matches the BBH paper (s3). The
  contested task count is handled per brief: 204 attributed to BIG-bench (s2),
  the 209 funnel start to BBH (s3), ">200" not used in prose. The three readings
  are not crossed.
- **Human bar: average 67.7%, max 94.4%, over the 23 tasks; rater count
  unstated.** Held. Ownership is right (67.7/94.4 to the BBH paper Table 2, the
  "team of expert raters" and search allowance to BIG-bench). The gap is reported
  honestly as a small, unspecified expert team allowed web search, sitting
  "almost 27 points" (94.4 - 67.7 = 26.7) under the best single rater. No implied
  lay-person baseline. The "model at 70%" hypothetical is internally correct.
- **CoT is model- and task-specific.** Held and honestly scoped: Codex-CoT 73.9%
  clears 67.7%, PaLM-CoT 65.2% does not, even though PaLM beats the bar on 10/23
  tasks individually; no model came near 94.4%. Never stated flat.
- **Contamination case and saturation (BBEH 9.8% / 44.8%).** Held against s5, s6,
  s8; the OpenAI quote is verbatim and correctly attributed.

Where I pushed hardest: **"chain-of-thought lifted every model tested by 13 to 17
points."** The evidence record verifies three models (PaLM 540B +12.9, Codex
+17.3, InstructGPT +16.6), all inside the range, but nothing in the record
establishes that those were *all* models measured. The universal quantifier
claimed completeness the record does not support. Fixed directly by dropping the
universal and attaching the range to the demonstrated figures ("chain-of-thought
added 13 to 17 points," then the two named models). No number changed; the range
is still the rounded Codex/PaLM span.

Citations: I opened all eight hrefs as printed plus the two Go-deeper links. All
resolve and land on the source itself: the four arXiv abstracts (s2, s3, s5, s8)
match their papers; the google/BIG-bench README carries the canary sentence (s6);
The Batch (s7) and benchmarkingagents.com (s4) carry the context they are cited
for; the Claude 3 card PDF (s1) returns HTTP 200 as application/pdf. The two
Background links resolve in the published checkout, and their display text is the
linked lessons' exact titles. `data-nb-kind` labels audit clean: 6 primary
(each the owner of its claim), 2 secondary (both cited only for context, not for
a contested figure). Floor met (8 sources / 6 primary / 2 secondary). Display
descriptors match source, title, and setting descriptor by descriptor; no wrong
label in headline, dek, subheads, or source names.

## Cut

Slop pass, every sentence including display text and furniture prose:

- **Diction tic.** "not comparable to a bare answer-only score" hit the
  recent-pattern ban on "a bare ... [number/score]." "Bare" was redundant with
  "answer-only." Cut to "an answer-only score."
- **Redundant enumeration in the bookend.** The "Why this matters" card previewed
  the lesson's coverage twice back to back — a four-item colon-list of what the
  lesson takes apart, then a three-item question-list posing nearly the same
  three questions. Cut the second (the question-list); the first, more concrete
  list carries the preview and still pairs with the takeaway's resolution. This
  clears two of the three standing W-SENTENCE-DENSITY warnings (the second was
  the redundant one).
- **Body self-reference / method signpost.** The orientation section closed with
  "This lesson walks those three in order, then follows the number to a case
  where taking it at face value missed something that had already gone wrong."
  The lesson template confines self-reference to the two bookends ("the body
  speaks to no one and never mentions the lesson"), and the sentence is a pure
  roadmap that survives the delete test with no fact lost. Cut. The section now
  ends on the concrete three-decisions list, a clean handoff to the body; the
  contamination movement is still foreshadowed in the bookend ("whether anyone
  had already seen the answers").
- **Hypothetical-reader gesture.** "A reader who meets that row learns that Opus
  outscored GPT-4..." gestures at a hypothetical reader in the body. Recast to
  the row's own terms ("The row shows that Opus outscored GPT-4..."), same
  meaning, plainer, keeps the show / does-not-show parallel.
- **Signpost.** "So it is worth being exact about that bar." announces intent
  rather than reasoning; cut, the definition of the bar follows immediately.

Edges walked on their own: the paragraph, section, and article first/last
sentences carry facts or reasoning (the funnel's "A model at 70% has passed the
average of that group and is still far short of its strongest rater," the
contamination opener's benchmark-validity premise, the takeaway's number-anchored
close). None reduce to a subject-interchangeable pattern.

Negative parallelism checked case by case and left where earned: "not OpenAI, but
Google's Gemini technical report" corrects the real, named assumption the whole
piece turns on; "hard for reasons of specialist knowledge rather than reasoning"
is the sourced reason 13 tasks were dropped; "The row reads like a head-to-head,
and for that one figure it is not" states the section's earned conclusion. No
invented strawman among them.

Prompt-leakage pass against commission, brief, evidence record, and voice guide:
no lifted instructions, planning labels, or assignment-fulfilled claims. "Same
model, same benchmark" appears in the evidence record too, but it is a sourced
fact (GPT-4, BBH, in both reports) stated in the article's own surrounding terms,
not the brief's framing — not a leak. No distinctive phrasing borrowed from the
Luu / Bergstrom-West / Willison exemplar quotations.

Furniture: the selection funnel (`nb-steps`), the chart, and the OpenAI-quote
callout (`nb-note`) each do work the prose would carry worse; none is a
formula, and no Verdict block appears (press forbids it). No missed component:
the card row is simple enough in prose, and the chart already carries the
CoT-versus-human comparison, so a second figure would read as furniture for its
own sake.

Recent-pattern comparison: opener does not use the flat "BBH is a 2022
benchmark..." definitional frame (it opens on the reader's encounter with the
number); headings avoid the "The [noun] that [verb]..." relative clause and the
wh-bank, and are built differently from one another; dek avoids the score-metaphor
mold. No "By the end you will be able to...", no "The next time..., ask...", no
"honest" as a virtue word.

**Takeaway / decode-questions check (round focus):** confirmed *not* the series'
stock decode-questions close. The takeaway hands the reader no numbered "questions
to ask about the next score." It resolves the opener's setup by stating the
lesson's findings and closes on the two specific numbers in this piece — "Read
the 86.8% and the 83.1% again and they answer different questions: measured with
different prompting, against a bar of searchable experts, and in one case on tasks
the model had already been trained on." Its three-part close is about *these* two
figures, not a portable checklist, which is the permitted setup/resolution pairing
rather than the banned close.

## Reader

Read straight through as the paper's declared reader: I now know that "X% on BBH"
compresses a benchmark assembled from hundreds of contributed tasks, a subset
kept only where models trailed a small searchable expert team's average (67.7%,
itself far under the 94.4% best rater), a prompting choice that moves the figure
13 to 17 points, and — for the GPT-4 cell specifically — a number its own maker
withheld as contaminated and a rival published. The sources alone would not hand
me that: they are three separate papers, a repo, and a model card, and the piece
is the thing that lines the 86.8% and the 83.1% up and shows the row is not the
head-to-head it looks like. The draft-handoff's original-work sentence claims the
same synthesis, and the article delivers it. Prose sits closer to the voice-guide
exemplars than a median summary: construction stated before judgment (Luu),
figures carrying the weight, one documented misled case worked through rather than
a list of worries (Bergstrom-West / Willison). The headline, reread as the largest
claim, is one the body defends.

## Edits

- Bookend "Why this matters": cut the redundant second enumeration ("The 86.8% is
  the thing to explain, and explaining it means asking what the tasks were, who
  set the bar the models had to clear, and whether anyone had already seen the
  answers."); the prior colon-list carries the preview.
- Orientation: recast "A reader who meets that row learns that Opus outscored
  GPT-4..." to "The row shows that Opus outscored GPT-4..." (removed
  hypothetical-reader gesture).
- Orientation: cut the closing self-reference/method signpost "This lesson walks
  those three in order, then follows the number to a case where taking it at face
  value missed something that had already gone wrong."
- Selection section: cut the signpost "So it is worth being exact about that bar."
- Chain-of-thought section: "chain-of-thought lifted every model tested by 13 to
  17 points" -> "chain-of-thought added 13 to 17 points" (dropped the
  completeness claim the record does not support; no number changed).
- Chain-of-thought section: "not comparable to a bare answer-only score" -> "not
  comparable to an answer-only score" (recent-pattern diction tic).

## Required work

- **writer:** re-run the proof on the edited article (`./nb check ...`), then the
  orchestrator stamps. My edits are prose-only — no em-dashes added, no banned
  terms, no links or numbers changed — so BLOCK: 0 is expected to hold. No chart
  correction: the committed `chart-1.py` and rendered PNG match the evidence
  record and the owning BBH paper (Codex 56.6/73.9, PaLM 52.3/65.2, dotted 67.7
  average-rater and dashed 94.4 max-rater lines, 0-100 scale, legend and axes
  labeled, plotted values honest).
- **researcher:** none. No evidence gap surfaced.
- **orchestrator:** none. Commission context settled the edit.

## Decision

approve — every finding was editor-fixable and fixed directly; the misled case,
the human-rater gap, the CoT scoping, the task-count readings, and the chart all
verify against the primaries, and no publication-blocking work remains. A fresh
proof and stamp are needed because I edited the article.
