# writer brief: the-instruments/mmmu (01)

Inputs:
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/editorial-direction.md
  — house standard, paper voice, lesson identity, series prompt.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/commission.md
  — the measurement, the angle, source direction, nb-meta values.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/writing-coach/01/voice-guide.md
  — how this piece should sound; read before drafting and before every revision.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/researcher/01/evidence.md
  — the complete claim set; cite only from it.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/.nb-context/
  — the effective template contract, runtime assets, and furniture catalogs.
- /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/library/the-instruments/mmmu.html
  — the initialized article to edit in place.

Output: /home/user/the-nightly-build/.nb-work/the-instruments/mmmu/agent-artifacts/the-instruments/mmmu/writer/01/draft-handoff.md
(the original-work sentence, the proof result with any warning intentionally left, and any open evidence/voice question).

Proof (run from repo root /home/user/the-nightly-build, iterate with --no-check-links, then finish links-in):
- Iterate: `./nb check .nb-work/the-instruments/mmmu/library/the-instruments/mmmu.html --series the-instruments --library /home/user/library-checkout --no-check-links`
- Final: the same command WITHOUT `--no-check-links`, and run `./nb stamp .nb-work/the-instruments/mmmu/library/the-instruments/mmmu.html` first, until `BLOCK: 0`.

nb-meta to fill: date `2026-08-12`, harness `claude-code-routine`, model
`Claude Opus 4.8`, and three descriptive tags (e.g. mmmu, multimodal-benchmarks,
evaluation). Keep nb-meta `dek` identical to the rendered dekline.

This round's focus: teach how the MMMU number is made (who built it, from what
material, by what procedure, how answers become a percentage), then what it can and
cannot support, with the real misled case. Use the evidence record's figures
exactly: the construction (11,550 questions; disciplines/subjects; image types; the
~94% multiple-choice share), the vision-blind baseline (text-only GPT-4 34.9% val
against 22.1% random and 56.8% for GPT-4V), MMMU-Pro's three changes (the
text-answerable filter, options expanded 4→10, the vision-only screenshot setting)
and its overall score-drop range, and named makers' own MMMU claims quoted from
their own reports.

Hold these boundaries from the evidence record; they keep the lesson honest:
- The claim is that a meaningful share of MMMU is answerable from text alone, not
  that most of the score is text. Vision adds roughly 22 points on top of the
  ~35% text-only ceiling. Say it at that strength.
- The MMMU authors defend the benchmark (adding OCR or captions does not lift
  text-only models to parity; strong models still make basic perceptual errors).
  Report that defense fairly where you make the text-answerable point; it is in the
  evidence record's Contradictions.
- The "% answerable without the image" is triangulated across sources, not a single
  reported figure. Attribute it as the evidence record does (including MMStar's
  direct measurement); do not invent a precise single number the sources do not
  state.
- Numbers in circulation mix scoring protocols (for example a Maj@32 figure shown
  beside a pass@1 figure). That is a protocol difference, not a capability gap; do
  not present it as one. If you compare two models' numbers, make sure they are the
  same protocol or say plainly that they are not.

Link `the-mechanics/reading-images` in Background (how a vision-language model
ingests an image) rather than re-teaching it. Assume the reader can meet a
benchmark, a multiple-choice accuracy, and a percentage without a fresh lecture;
define any MMMU-specific term where it first appears. Link only already-published
library pages — do NOT link tonight's sibling articles.

Furniture: plan prose and furniture together from the catalogs under `.nb-context`.
A table or figure comparing MMMU with MMMU-Pro per model may earn its place if the
comparison is the point; build a chart only from a verified numeric series in the
evidence record, keep protocols consistent within it, and label axes and the
source. Use documented markup only.

Habits not to inherit (house formulas the recent library shares across desks):
- Do not open "Why this matters" on a nostalgic or second-person recall ("If you
  have heard one thing about...", "You may remember when..."), and do not pivot the
  opener on "This lesson shows/teaches/takes apart...". Find a fresh way in.
- Do not close the opener on a "set the two things side by side" line, and do not
  land "The takeaway" on a "So next time you [see/meet] a score..." portable rule.
  Find this lesson's own resolution.
- Do not use "this desk" or any self-reference in the body; the body narrates no
  one.
- The-instruments' recent dek molds are "The score/number behind [popular claim] is
  [deflating mechanical description]" and "A perfect X score means the model [did
  a trivial thing]." Write a dek built neither way. Vary section headings away from
  the "The X that Y" relative-noun-phrase mold and the "noun, the appositive" comma
  mold; each heading is a step in this lesson's own nouns, no scaffolding slots.
