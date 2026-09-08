# Editorial review: when-ai-breaks/waymo-recall (editor/01)

## Skeptic

Thesis: a driverless car runs a pipeline of learned steps (perceive, then
predict, then plan), each reliable on the traffic it was shown and each able to
fail on a configuration too rare for its training; Waymo's two recalls catch two
different steps failing that way, and a recall is the visible correction.

The claims it stands on, and how each held against the primaries:

- **The towed-truck collisions were a prediction failure, not a perception
  failure.** Held. NHTSA 24E-013 attributes the defect to the ADS having "incorrectly
  predicted the future motion of the towed vehicle" and never faults detection;
  the article's careful hedge ("the filing does not fault what its sensors
  returned") is exactly what the record supports. Collision date 12/11/2023,
  Phoenix, front-left contact, tow truck did not stop, second Waymo minutes
  later, no injuries — all verbatim-accurate to the filing's chronology.

- **The pole collision was a different failing module: perception plus mapping.**
  Held, and this is the piece's most important nuance. 24E-049 names two
  conditions — perception "assigned a low damage score to the object" and the map
  "did not include a hard road edge" — and two remedy components (ADS software
  and ADS map). The article states this precisely and, critically, says outright
  "The pole was not a repeat of the towed-truck bug," so it never implies the
  prediction bug recurred. Round-focus requirement met.

- **Both failures share a class: rare tail configurations / distribution shift.**
  Held. The filing's own words ("exceptionally rare," "exceptionally low
  likelihood of encountering") support the long-tail framing, and the two
  external sources (Shifts benchmark; the perception/prediction survey) are cited
  for the concepts they own.

- **Waymo owns every vehicle, so the recall meant a pushed software release with
  no owner to notify.** Held against 24E-013 p.3 ("all of which Waymo owns and
  has never sold").

Display text audited descriptor by descriptor against the two Part 573 primaries
(read in full) and the ODI opening resume: both incident dates (Dec 11, 2023 /
May 21, 2024), both filing dates (Feb 13, 2024 / June 10, 2024), both vehicle
counts (444 / 672), both recall numbers, "wooden utility pole," and the
software-and-map remedy are all correct. The 8 mph speed and the Jaguar I-Pace
model are correctly attributed to TechCrunch, and the article did **not** inherit
TechCrunch's "telephone pole" — it uses the filing's term. The ODI paragraph's
"22 incidents" and "single-party crashes and apparent traffic-law violations"
match PE24016's opening resume (22 incidents, 17 crashes, 0 injuries, opened
05/13/2024).

Citations: every `href` was opened as the article prints it. All eight land on
the source document itself — the two NHTSA Part 573 PDFs, the NHTSA ODI resume
PDF, both arXiv abstract pages, the Waymo blog post, the Reuters/Insurance
Journal report, and the TechCrunch report — none is a fetch endpoint or a
redirect wrapper. `data-nb-kind` labels check out against the sources; the floor
(8 sources, 6 primary, 2 secondary) is met with margin. The survey (s4) is
labelled primary as the source that owns the standard module definitions; even
read as secondary the primary floor still clears.

One break found and fixed directly. The dek claimed the prediction step "had
never seen a pickup towed backwards and angled across a turn lane," and the
takeaway said the truck "moves unlike anything the prediction model had been
trained on." Both assert a fact about the training set the record does not carry:
the filing establishes the configuration was *exceptionally rare*, not that the
model had *never encountered* it, and the body itself hedges correctly ("the
nearest thing it saw in training, which may be nothing like the thing in front of
it"). I brought the dek and the takeaway line back to what the record supports.
No routed break: the argument's spine holds on the sources as cited.

## Cut

Ran the slop pass over body, display text, and furniture. The prose is clean and
sober; the sentence-by-sentence pass turned up no empty conclusions, no puffery,
no decorative-analysis verbs, no vague attribution. The earned negative contrasts
the writer flagged ("The pole was not a repeat of the towed-truck bug"; "rather
than a rare edge case") each correct a misconception the piece actually names, so
they stay.

Two edge failures at the close, both cut:

- **Prompt leak in the last sentence.** The takeaway closed "The record teaches
  how the failure happens, not a body count." "Not a body count" is lifted from
  commission.md's own framing ("the honest lesson is about the failure mode and
  the recall process, not a body count"), and as a negative-parallelism final
  sentence it is the position slop tests hardest. The point underneath (no
  injuries; the mechanism is what matters) is real and sourced, so I rewrote it
  in the article's own terms rather than deleting the idea: the closer now lands
  positively on the two recalls showing the same system fail at two steps, and
  keeps the sober "neither collision hurt anyone."

- **Signpost.** "That is the durable lesson." reported where the argument stood
  without doing any of the reasoning; the sentences after it are the lesson.
  Deleted; nothing was lost.

One house-punctuation and meta trim: a timeline caption ran "The incident date
and the filing date are two months apart; the crash was December, the recall was
February" — a semicolon where a period belongs, plus a meta restatement of the
gap. Replaced with two plain sentences carrying the same December/February fact.

Recent-pattern check against the brief's notes: the opener leads on Waymo's
safety reputation, not a one-line statement of the harm, so it does not reuse the
flagged desk mold. The dek (before and after my fix) is a single claim, not the
comma-and / comma-triad mold. The four section headings vary in construction and
none uses the comma-and mold; the headline carries no colon subtitle. No formula
flagged.

Furniture: the timeline, the "In plain language" note, and the two bookends are
all documented components used for genuine purpose (the note pins the
perception/prediction definition to its source; the timeline makes the
incident-vs-filing gap visible). None reads as a decorative block. No component
added or removed.

## Reader

Read straight through as the paper's reader: what I have that the sources alone
would not give me is the pipeline as a diagnostic tool — the two recalls set side
by side so that "which step broke" becomes a way to read any AV failure, with
perception-vs-prediction and distribution shift taught in plain words and pinned
to real filings. That is more than either NHTSA form states on its own; the
draft-handoff's original-work claim (turning two separate filings into one worked
lesson on two stack stages) survives the read. The prose sits closer to the
voice-guide exemplars than to a median summary: it carries the incident on a
clock, marks reconstructed detail plainly, and holds the seriousness of the
failure mode against the fact that no one was hurt, which is the Feynman/Wise move
the guide asks for. The headline, reread as the largest claim, is a concrete,
verb-driven report of the event and is fully supported.

## Edits

- Dek (both the `nb-meta` field and the rendered dekline, kept identical):
  replaced the unsupported "had never seen a pickup towed backwards and angled
  across a turn lane" with "A pickup towed backwards and angled across a turn
  lane was too rare a shape for the step that predicts where other vehicles will
  go next."
- Takeaway: softened "moves unlike anything the prediction model had been trained
  on" to "moves unlike the ordinary traffic the prediction model was built on."
- Takeaway: deleted the signpost "That is the durable lesson."
- Takeaway: rewrote the leaked/negative-parallelism closer "The record teaches
  how the failure happens, not a body count" as a positive closing sentence, and
  dropped the imprecise "five months later" from "The pole recall."
- Timeline (Feb 13 caption): replaced the semicolon-joined meta sentence with
  "The crash was in December. The recall came two months later, in February."

## Required work

- **writer** — run the final proof (`nb check ... --library ...`) and re-stamp:
  the dek text and a handful of words in the takeaway and one caption changed, so
  `words` / `reading_minutes` in `nb-meta` need refreshing. The dek-equals-dekline
  invariant is preserved (both were edited together). No reporting, redraft,
  source asset, or chart work is owed — this is the mechanical re-proof only.
- **orchestrator** — stamp after the writer's proof, per the normal flow.

No researcher work: no evidence gap opened, no central claim broke.

## Decision

approve — the record is exact and every citation resolves to its source; the two
display-text overclaims and the closing prompt-leak were fixed in place, leaving
only the routine re-proof and stamp.
