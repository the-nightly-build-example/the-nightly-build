# Editorial review: the-instruments/clipscore (editor/01)

## Skeptic

Thesis: CLIPScore is one model's opinion of another model's output, and its
authority rests on a human-correlation credential earned on a different task
(ranking captions for real photos) than the one it is now spent on (grading
generated images for prompt alignment), where it is far weaker and inherits
CLIP's blindness to which-adjective-goes-with-which-noun. Every named failure is
read as a consequence of that one fact rather than an unrelated list of
benchmark losses. The draft states the thesis cleanly; the four claims it stands
on are legible from the article alone.

Claim 1 — the construction (CLIP-S = 2.5·max(cos,0), ViT-B/32). Held. Formula,
backbone, and the "stretch, not re-rank" role of 2.5 match Hessel et al.

Claim 2 — the credential was earned on captioning, not text-to-image. Held, and
it is the spine of the piece. Hessel's Kendall 51.2 (Flickr8K-Expert) is a
captioning number; Hu et al.'s Spearman 33.2 (TIFA, generated images) is the
direct T2I measurement, well under TIFA's own 59.7. Both verified against the
primaries. One break: the takeaway asserted the T2I number "roughly halves" the
credential. That ratio is not supported by the two figures the reader was shown
(33.2 is about 65% of 51.2, not half) and it silently compares a Kendall
coefficient with a Spearman one. The clean cross-task drop the record supports
(Kendall 51.2 vs Kendall 23.1) is never displayed. Fixed in place: the takeaway
now says the agreement "is far lower," matching the body's own "far lower" and
dropping the unsupported ratio. Direction ("far lower") is robust across either
coefficient, so no number moved and nothing was softened away from what the
record carries.

Claim 3 — below chance on compositional swaps. Held. Lin et al. Table 1 puts
CLIPScore at 7.8 group score against a 16.7 (1/6) random-chance floor and 46.0
for VQAScore. 7.8 < 16.7 makes "below chance" a true, checkable claim, and it is
the article's headline.

Claim 4 — optimizing the score gets it gamed. Held, and kept CLIP-specific as
the brief required. FuseDream's FGSM sentence ("almost identical ... yet with
much higher CLIP score ... a danger of overfitting") verified verbatim;
PickScore's 60.8 (CLIP-H) vs 70.5 vs 68.0 (human experts) verified. The DDPO
turtle case is correctly absent, since its grader was a LLaVA VLM, not CLIP.

Citations. I opened all eight hrefs as printed. Each resolves and lands on the
source itself (the canonical arXiv record). Load-bearing figures spot-checked
against the primaries' full text: Hessel 51.2 / CIDEr 43.9 / SPICE 44.9; Radford
400M and the counting quote; Lin 7.8 / 46.0 / human 85.5 / chance 16.7; Hu
33.2 / 59.7 and the counting-and-composition quote; Yuksekgonul 63 / 62 / 46 and
the 50.3→34.1 retrieval drop; Kirstain 60.8 / 70.5 / 68.0; FuseDream FGSM;
Hartwig survey framing. All matched.

Provenance question from the brief, settled. The 16.7 chance floor and the 85.5
human ceiling do not need the Winoground primary (Thrush et al.). Lin et al.'s
Table 1 carries both as its own rows (Random Chance 16.7 group; Human Evaluation
85.5 group) alongside CLIPScore and VQAScore, so citing them to source 5, as the
chart caption and body do, cites them to a source that owns them. No routing to
the researcher.

data-nb-kind audit. Seven primaries, one secondary (Hartwig, correctly
secondary — a survey reporting on CLIPScore from outside its authoring team). No
contested figure rests on the secondary. Source floor met (8 sources, 7 primary,
1 secondary).

Display-text and internal-consistency checks turned up two more breaks, both
fixed in place. The swap example called "a red cube on a blue sphere" and its
color-swap "the same five words" — the phrase is seven words; changed to "the
same words," which is what the illustration actually needs. And the teaching line
"Correlation runs from 0 for no relationship to 100 for perfect agreement" states
a false floor (Kendall and Spearman run to −100), presented as a definition to a
reader meeting correlation for the first time; reworded to name 100 and 0 as
reference points without claiming 0 is the minimum, with "well over half" (51.2
is barely over half) corrected to "just over halfway there."

## Cut

The draft was already tight; the slop pass found little. Named tells fixed:
"Notice what it was measured on" opened a body sentence with a lecturing
imperative (the Note/Consider/Imagine family) and addressed the reader, which
the lesson template confines to the two bookends; recast as a declarative pivot
("But it was measured on one task in particular:"). "The failures so far are of
reading a CLIPScore" carried a where-the-piece-has-gone signpost; changed to
"Those failures all come from reading a CLIPScore," which keeps the load-bearing
reading-versus-optimizing distinction and drops the progress marker.

Negative-parallelism sweep: three contrasts survive because each corrects a
misconception the piece actually names — "insufficient sensitivity rather than
total blindness" (backed by the 50.3→34.1 drop that proves partial sensitivity),
"selecting for CLIP's taste, not the viewer's" (the measured 60.8/70.5 gap), and
the takeaway's captioning-not-generations contrast (the thesis itself). None is
a strawman.

Naming consistency: "coin flip" was used precisely for the two-choice ARO tests
(chance 50%) and then loosely for the Winoground group metric, whose chance is
1/6. Both Winoground uses ("below a coin flip" in the body and the takeaway)
changed to "below chance," which is accurate for a 1/6 floor and stops the score
from reading against two different chance levels under one name.

Punctuation: two semicolons joining independent clauses that a period governs
better were split (the FID sentence; "one inherited blind spot; the rest"), per
the house default. The compact figure caption's parallel semicolon was left.

No formula against the recent record: the headline avoids the "X can hide Y" and
"the number came from the public set" molds; the dek avoids the "grades…, a
measure that stays silent on…" mold; no heading joins two clauses with a comma
and "and."

## Reader

Read straight through as a smart newcomer, I come away with something no single
source hands over: the reason a high CLIPScore does not promise an on-prompt
picture is one fact — it is CLIP grading CLIP, validated on captioning and then
borrowed for generation — and the word-order failure, the below-chance
Winoground result, the adversarial step, and the selection gap all fall out of
that fact. The draft-handoff's original-work sentence claims exactly this spine,
and the article delivers it; neither answer collapses into a restatement of the
sources. The prose sits with the voice-guide exemplars (Evans/Yglesias: a real
decision named before the number, worked examples carrying the abstractions),
not a median summary. The headline is the largest checkable claim and the piece
earns it.

Chart. Fig. 1 read as a reader: linear 0–100 axis, both bars labeled (7.8,
46.0), a dashed chance line at 16.7 and a dotted human line at 85.5, with the
CLIPScore bar sitting visibly below the chance line. Every value matches the
record and Lin et al. Table 1; the caption cites the data source. chart-1.py
provenance is honest and documents the floor/ceiling as group-metric properties.
No correction needed.

## Edits

- Removed the unsupported "roughly halves" ratio in the takeaway; now "is far lower," matching the body and the record's direction.
- "the same five words" → "the same words" (the swap phrase is seven words).
- Reworked "Correlation runs from 0 … to 100 …, so 51.2 … well over half the way" to name 100/0 as reference points without a false floor, and "just over halfway there."
- "Notice what it was measured on:" → "But it was measured on one task in particular:" (removed the lecture opener and the body reader-address).
- "The failures so far are of reading a CLIPScore." → "Those failures all come from reading a CLIPScore." (removed the progress signpost).
- "below a coin flip" → "below chance" in the body Winoground sentence.
- "It scores below a coin flip on the compositional swaps" → "below chance" in the takeaway.
- Split the FID semicolon into two sentences.
- "one inherited blind spot; the rest come with it" → two sentences.

## Required work

None. Every issue was reachable by editing; no claim broke past repair, no
figure needed the writer, and the chart is honest as committed. The orchestrator
runs nb stamp and the proof after these edits.

## Decision

approve — the thesis holds, every citation lands on a source that owns its
claim (the flagged floor/ceiling included), the chart is honest, and the
remaining prose and accuracy breaks were fixed in place.
