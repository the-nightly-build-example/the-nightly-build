# Editorial review: the-mechanics/prompt-sensitivity (editor/01)

## Skeptic

Thesis: a model conditions on the literal token sequence and holds no meaning
apart from that surface form, so two prompts a person calls equivalent, or two
orderings of the same examples, are different inputs and can score very
differently; when a score moves there are three distinct causes to tell apart (a
genuinely worse model, a surface form that changed the input, a grader that
missed a correctly phrased answer); the mechanism is settled and the present-day
magnitude in frontier models is open. The draft states all of this on its own,
so the thesis is legible.

Claims it stands on, and how each held:

- The worked case: a colon-to-space change moved 1-shot LLaMA-2-7B on one task
  from 0.043 to 0.826. Verified against the evidence record (Sclar Table 1,
  task280). The article keeps this 7B worked example distinct from the 76-point
  figure, which it attributes to LLaMA-2-13B in a separate section and in the
  table caption. The round's central "keep them distinct" requirement is met.
- The mechanism (token conditioning, no stored meaning) is carried from three
  directions, each cited to its owner: Webson & Pavlick (scrambled instruction
  meaning is near a no-op, answer-token choice is not), Su et al. (the delimiter
  effect traces to attention over key input tokens), Sclar §4.4 (a format's
  embedding separability tracks its spread). The Webson & Pavlick nuance is
  carried, not flattened to "surface form matters." Quotes match the record.
- Magnitude scoping: the big numbers are attributed to 2021-2023 open models
  under probability-ranking or exact-match scoring (76 pts LLaMA-2-13B; 56 pts
  GPT-3.5-Turbo across 320 formats; Lu 85 vs 50 on SST-2; Zhao 54 to 93). The
  frontier magnitude is marked open through Hua et al., with Sclar and Su
  steelmanned first (does not shrink with scale; Su still measures +/-23% on
  MMLU). Matches the record and the present-day-honesty brief.
- The grader case (Hua et al.): re-grading seven recent models, including
  GPT-4o-mini and Gemini 2.0 Flash, collapses the spread under an LLM judge
  (Gemma-2 ARC 0.25-0.90 to 0.17; rank correlation 0.30 to 0.92). Verified.

Citations: I opened all eight source hrefs as printed. Every one resolves and
lands on the paper or post it names; titles and authors match the source entries
(Sclar/Choi/Tsvetkov/Suhr; Webson & Pavlick; Su et al.; Kurt/Louf/Fourrier;
Mizrahi et al.; Lu et al.; Zhao et al.; Hua et al.). The three internal Background
links (in-context-learning, instructions-are-data, word-embeddings) resolve to
published sibling lessons, and each row's link text matches that lesson's actual
title verbatim.

data-nb-kind audit: 7 primary, 1 secondary (the Hugging Face blog, correctly
labeled secondary as a rigorous explainer that does not own the core numbers).
Meets the series floor of 8 sources, >=4 primary, >=1 secondary. No mislabeled
independent source.

Breaks found and fixed in place (no number, name, or citation-target changed):

- The 0.05 figure was labeled "the correlation between the best orders" for two
  models. The record's statistic is the permutation-performance correlation
  between the two models, not a correlation restricted to their best orders.
  Reworded to "how the orders performed on a 175-billion and on a 2.7-billion
  parameter model correlated at only 0.05," which is what the source measures.
- The ~10-point average read as LLaMA-2-13B's average ("reached 76 accuracy
  points, and averaged about 10"). The record scopes the ~10 across 50+ tasks and
  several models, not to the 13B alone. Rescoped to "across the tasks and models
  measured it averaged about 10." Both figures unchanged.

Not fixed, left as acceptable: the worked-example institutional line credits
"the University of Washington and the Allen Institute for AI" (three of four
authors; Suhr is UC Berkeley) and the Mizrahi 21-point figure is presented as a
general single-prompt overstatement though the record ties the exact number to
davinci. Both are within normal attribution latitude and the researcher's record
sanctions the 21-point figure as the representative caution; neither misstates a
claim the argument rests on.

## Cut

One dedicated slop pass, then the edges, the cold read, and the delete test.

- Body self-narration plus puffery: "The setting behind these numbers matters,
  and the last section returns to it." The opener announced importance without
  content and then pointed forward to another section of the piece, which the
  body must not do. Deleted and folded the real scoping into the concrete
  sentence that followed: "These swings all come from open models of 2021 to
  2023, on classification tasks, scored by..." The scoping caveat survives; the
  signpost does not.

That was the one sentence that failed the slop test outright. The rest of the
edges held on inspection. The two earned negative-parallelism instances ("the
model responds to the tokens... not to a meaning it extracted and stored" and
"the grader missing correct answers rather than the model failing") both correct
a misconception the piece names and defends, so they stay. The settled/open
markers ("This part is settled engineering," "This is the open part") are the
series' required settled-vs-open teaching move, grounded, not empty conclusions.
No vague attribution (every claim is named to its owner), no decorative-analysis
verbs, no fluff openers, no self-reference outside the two bookends the lesson
template allows.

Prompt-leakage: the three-case split and the settled/open boundary appear in the
commission and briefs, but here they are the taught substance, grounded in the
sources and written in the article's own terms, not lifted planning labels.

Voice and formula: register matches the plain, ground-the-behavior-first
direction of the voice guide (the colon case lands before the mechanism is
named; "surface form moved the score" is kept distinct from "the model is worse";
settled and open are marked flatly). No distinctive phrasing borrowed from the
Evans/Luu/Ciechanowski exemplars. Against the recent-pattern notes: the headline
avoids the "can't tell X from Y," "like any other token," and "chatbot does X
without Y" molds; the dek avoids the "[do X] and [Y], because [Z]" mold and the
three banned dek molds; the opener does not close on an enumerated section
roadmap; the takeaway does not open on a bare restated one-liner. Headings skim
as the argument's steps in order.

Furniture: the table (three atomic Sclar Table 1 pairs, caption carrying the
citation and Table 1 locator) and the note ("Three ways a score can move,"
crystallizing the article's core distinction) are both documented engine
components, each doing real work. No stack-of-blocks effect; no missed component
the material needed as inline data already carries the format strings.

## Reader

Read straight through as the paper's declared reader, I come away with a single
usable diagnostic the sources do not hand over on their own: when a model's score
moves after a reword, reformat, or reorder, I can locate the cause in what the
model actually reads, and I can separate three causes of the move, and I know the
large historical magnitudes are from older open models under constrained scoring
while the frontier magnitude is contested and turns on how the output is graded.
That synthesis across eight papers matches the original-work sentence in the
draft handoff, and neither answer collapses into a restatement of any one source.
The prose sits closer to the voice-guide exemplars than to a median summary: it
grounds the behavior in one concrete case before naming the cause, and marks the
edge of what is known plainly. The headline reads as a defensible gloss of the
task280 result (4% to 83%), with the dek supplying the exact figures and the
2023-open-model scope.

## Edits

- Reworded the Lu 0.05 statistic from "the correlation between the best orders
  for a 175-billion and a 2.7-billion parameter model" to "how the orders
  performed on a 175-billion and on a 2.7-billion parameter model correlated at
  only 0.05."
- Rescoped the Sclar ~10-point average from "reached 76 accuracy points, and
  averaged about 10" to "reached 76 accuracy points, and across the tasks and
  models measured it averaged about 10."
- Cut the signpost/puffery sentence "The setting behind these numbers matters,
  and the last section returns to it." and folded its scoping into "These swings
  all come from open models of 2021 to 2023, on classification tasks, scored
  by..."

## Required work

- orchestrator: prose changed (net one sentence shorter), so re-stamp the article
  and re-run the proof before preparing the PR.
- researcher: none.
- writer: none.

## Decision

approve — the mechanism reads as settled and the frontier magnitude as open, the
three cases stay distinct, all eight citations land on their sources, and the
three issues found were correctable in place without new reporting.
