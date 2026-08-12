# Editorial review: the-instruments/mmmu (editor/01)

## Skeptic

Thesis: an MMMU percentage credits to vision less than its billing implies. A
meaningful share of the questions is answerable from text alone, the
multiple-choice format pays for guessing, and when the benchmark's own authors
forced the image in MMMU-Pro the scores dropped by a measurable, quantified
amount. The reader should finish able to say what the number does measure.

Claims it stands on, and how each held:

- **Flagships print MMMU scores in the sixties to advertise vision.** Held.
  Claude 3.5 Sonnet 68.3% traces to Anthropic's model card (s2), Gemini 1.5 Pro
  62.2% to the Gemini 1.5 report (s4), Qwen2-VL-72B 64.5% to the Qwen report
  (s5). These are each maker's own MMMU (val) figure, presented as a cluster,
  not as a head-to-head ranking, so no protocol-mismatch problem arises here.
- **A text-only model with no image scores 34.9%.** Held against MMMU Table 2:
  GPT-4 text-only 34.9% val, random 22.1%, GPT-4V 56.8%. Arithmetic checks:
  34.9 − 22.1 = 12.8 ("thirteen points above chance"); 56.8 − 34.9 = 21.9
  ("about 22 points"). The construction figures all reconcile: 10,861 + 689 =
  11,550; 11,264/11,550 = 97.52%; 10,861/11,550 = 94.03%.
- **The text-answerable share is a share, not the bulk of the score.** Held, and
  the piece polices its own boundary well: it states vision supplies the larger
  part, the 22-point image gain outweighs the 13-point blind gain, and the
  builders' defense (OCR/captions do not lift text-only models) is quoted in a
  note and the paragraph after it. The MMStar corroboration (GeminiPro 42.9%,
  Sphinx-X-MoE 43.6%) is correctly attributed as triangulation, not a single
  published figure.
- **MMMU-Pro's three changes drop scores.** Held. The three changes and the
  1,730-question final set match the MMMU-Pro evidence.
- **The circulating numbers also mix protocols.** Held against the Gemini 1.0
  report: Gemini Ultra 62.4% Maj@32 set beside GPT-4V 56.8% pass@1, Ultra's own
  pass@1 being 59.4%. The "not a capability gap, a difference in protocol"
  contrast is earned negative parallelism, correcting a misconception Google's
  own report created.

**One break, in display text, fixed directly.** The score-drop heading, the dek,
and the takeaway attached the abstract's "16.8% to 26.9% across models" range to
"flagship" scores ("the flagship scores fell 17 to 27 points"; "every flagship
fell 16.8 to 26.9 points"). That range's upper endpoint (26.9) is VILA-1.5-40B,
which is not a flagship and is not in the piece; the four flagships the piece
names fall roughly 17 to 19 points overall (and 19 to 22 in vision-only). So the
display text implied a flagship fell as much as 27 points, which no flagship
did. The body's own sentence already frames it correctly ("Across models, MMMU-
Pro scores landed 16.8 to 26.9 points below MMMU"). I changed the scope word
from "flagship" to "scores"/"across models" in all three display-text spots to
match the abstract and the body. No number changed; only the scope label.

**Writer's two flagged questions, adjudicated:**

- GPT-4o 69.1%: honest as printed. The sentence says "listed at 69.1% in the
  follow-up study's results table" and cites s6 (MMMU-Pro), where the figure was
  actually read; it does not claim OpenAI's own (bot-blocked) page was read. The
  value sits in MMMU-Pro Table 1's MMMU (Val) column. Attribution and wording
  stand as written.
- Headline "a third of MMMU": honest rounding. 34.9% rounds fairly to "a third"
  for display, and the exact 34.9% carries in the body. No change.

data-nb-kind audit: all eight hold. The seven labs and benchmark authors are
primary for their own claims/construction; MMStar (s7) is the one independent
secondary, correctly labeled and doing the confirmation work the angle needs.
Source floor met (8 total, 7 primary, 1 secondary).

## Cut

Two slop trims, both self-grading signposts:

- "That cuts two ways, and the honest reading holds both." → "That cuts two
  ways." The clause "the honest reading holds both" grades the article's own
  fairness rather than reasoning; the two named consequences follow immediately
  and carry the content.
- "What that percentage actually counts is the question." (an "X is the
  question" signpost) was deleted and its live content folded into the next
  sentence: "Two things about how the test is built decide what that percentage
  counts: ..." No fact lost; the referent repaired.

Edge sentences otherwise hold. Section closers carry content ("Two MMMU
percentages are comparable only when they were scored the same way";
"the rest of the test still needs the picture"). One forward bridge
("So the natural question is how many questions a model could get right with no
image at all") is a guiding question a lesson earns and answers with a number in
the next section; left in place. No em-dashes, no comma splices, no colon misuse
found. Grammar and syntax are clean throughout display text and the note.

Formula check against the recent-pattern notes: the "Why this matters" opener
does not open on nostalgia or second person and does not pivot on "this lesson
shows"; the opener does not close on a side-by-side line; the takeaway does not
land on a "next time you see a score" rule; the body carries no self-reference.
The dek is not built on either the-instruments mold ("the number behind X is
[deflating description]" / "a perfect X means the model did a trivial thing").
Headings are steps in the piece's own nouns, none in the "The X that Y" or
"noun, the appositive" molds. No prompt leakage: the reader-situation framing
("sees like an expert") is reported billing, not lifted instruction. No borrowed
phrasing from the voice-guide exemplars (Ritchie/Luu/Alexander).

## Reader

What the piece gives beyond its sources: a single worked reading that separates
one MMMU number into its parts. It isolates the image as the one changed
variable (34.9% blind → 56.8% seeing), quantifies what vision actually buys
(~22 points) against what text banks above chance (~13), then shows MMMU-Pro
measuring the inflation model by model, and finally separates that vision gap
from a second, distinct distortion (Maj@32 vs pass@1). No single source hands
the reader that assembled picture; the article builds it. The original-work
sentence claims exactly this, and the article delivers it. The prose sits closer
to the voice-guide exemplars than to a median summary: plain claims, real
figures shown before they are named, and the strong conclusions stated flatly
("the rest of the test still needs the picture"). The chart, inspected as a
reader, reinforces rather than distorts: honest full-height axis, one protocol
per series, source cited.

## Edits

- nb-meta dek: "the flagship scores fell 17 to 27 points" → "scores fell 17 to 27 points" (scope fix; kept identical to rendered dek).
- Rendered dek: same scope fix.
- Section heading: "The flagship numbers fall 17 to 27 points on MMMU-Pro" → "Scores fall 17 to 27 points on MMMU-Pro".
- Takeaway: "every flagship fell 16.8 to 26.9 points" → "scores fell 16.8 to 26.9 points across models".
- Vision-blind section: cut self-grading clause "and the honest reading holds both".
- Orientation: deleted signpost "What that percentage actually counts is the question." and folded its content into "Two things about how the test is built decide what that percentage counts: ...".

## Required work

None. All findings were fixable in prose/display text and were fixed directly.
The chart is honest and needs no writer correction. Orchestrator: run `nb stamp`
and `nb check` over the edited article before the PR (the dek edit touches
nb-meta, so a re-stamp is expected).

## Decision

Approve. The lesson teaches how the number is made and what it can and cannot
support, holds every evidence-record boundary, and the one display-text scope
error and two slop signposts were repaired in place.
