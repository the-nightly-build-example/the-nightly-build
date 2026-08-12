# Commission: the-instruments/mmmu

## Authorized work

Scheduled duty for 2026-08-12 returned `the-instruments` as an open section:
choose one measurement within the beat, do not repeat a published slug. This
commission selects MMMU. It is one article, on the lesson template, delivered as
one Article PR.

## The measurement and why it

MMMU: "A Massive Multi-discipline Multimodal Understanding and Reasoning Benchmark
for Expert AGI" (Xiang Yue and colleagues, CVPR 2024). It is the score behind the
line every flagship model now prints when it claims to "see": a single percentage
from a set of college-level questions that each pair text with an image (charts,
diagrams, chemical structures, medical scans, sheet music, and more), answered
multiple-choice or short-answer and graded for accuracy. When a launch post says
a model rivals experts at visual reasoning, MMMU is usually the number under the
claim. This desk teaches how that number is made and what it can and cannot
support.

The beat's job here: explain where the number comes from, step by step (who built
it, from what material, by what procedure, how a model's answers are turned into a
percentage); then show what the number can and cannot support, including at least
one real case where it misled people and what that cost.

## The angle

An MMMU percentage measures less about seeing than its billing implies, and the
reader should finish able to say what it does measure. Two properties do the
work. First, a meaningful share of MMMU questions can be answered from the text
alone, without ever looking at the image, so a strong language model banks points
the "multimodal" framing credits to vision. Second, the format is multiple
choice, which rewards option elimination and is vulnerable to the shortcuts any
multiple-choice test invites. The benchmark's own authors built the response:
MMMU-Pro re-ran the test after removing questions models could answer text-only,
expanding the candidate options to blunt guessing, and adding a vision-only
setting where the question itself is embedded in the image so the model must
actually read it. Scores dropped, and the size of the drop is the measure of how
much the original number had been crediting to sight that belonged to text and to
the multiple-choice format.

Teach the construction honestly and then teach the gap. The real case where the
number misled is the distance between a headline MMMU score used to claim
expert-level multimodal reasoning and the same models' lower MMMU-Pro scores under
conditions that force them to use the image. Give the figures, name whose numbers
they are, and state plainly what a high MMMU score does and does not license
someone to claim. Do not turn this into a takedown of the benchmark; its authors
diagnosed the problem themselves. Show what the number is worth for the narrow
thing it measures.

## Sources

Source floor for this series: at least 8 sources, at least 4 primary, at least 1
secondary. Primary here is each benchmark's own authors, and a model's own
reporting party for the claims it makes about its own scores.

Direct the researcher to read, at minimum:
- The MMMU paper (Yue et al., CVPR 2024). Read the construction: the number of
  questions, the disciplines and subject spread, where the questions came from,
  the image-type variety, the answer formats, and the paper's own analysis of how
  many questions are answerable without the image and how text-only or
  vision-blind baselines score.
- The MMMU-Pro paper (Yue et al., 2024). Read exactly what it changed (filtering
  text-answerable questions, augmenting the options, the vision-only input
  setting) and the score changes it reported for named models against plain MMMU.
- The primary reporting party for at least two named models' own MMMU claims
  (model cards, technical reports, or launch posts), so the number "in
  circulation" is quoted from whoever made the claim, not from a leaderboard
  aggregator.
- At least one independent secondary source analyzing MMMU's limits or its use in
  model comparisons. A restatement of a lab's own claim is not independent
  confirmation of it.

Every figure (question counts, per-model MMMU and MMMU-Pro scores, the text-only
baseline, the size of the drop) is checked against the primary that owns it.
Record contradictory evidence, including any defense of MMMU's validity, in full.

## Course placement and neighbors

The library already holds `the-mechanics/reading-images` (how a model turns an
image into something it can read alongside text) and many benchmark lessons in
this desk. Link `the-mechanics/reading-images` in Background rather than
re-teaching how vision-language models ingest an image; assume the reader can meet
the idea of a benchmark, a multiple-choice score, and accuracy without a fresh
lecture, but define any term specific to MMMU where it first appears. Tonight's
other new articles are in unrelated desks (grokking, image-generation,
reward-tampering, rite-aid-facial-recognition); no cross-collision to manage. Link
only already-published library pages, never tonight's siblings.

## Production policy

Profile `balanced`; no role directive is `required`. Recorded plan: writing-coach
low effort, researcher high effort, writer medium effort, editor high effort;
model class `capable`. The runtime maps `capable` to the session's capable model
and runs each role at the session's effort; no `required` directive exists to
trade down. Actual harness: `claude-code-routine`. Actual model recorded in
nb-meta: `Claude Opus 4.8`.

## nb-meta

Date 2026-08-12. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Tags are
the writer's to set as descriptive keywords (this open series configures no tag
fragments); three concise topical tags.

Recent habits to break travel with the writer and editor briefs.
