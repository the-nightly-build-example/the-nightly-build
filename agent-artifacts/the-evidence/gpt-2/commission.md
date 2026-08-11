# Commission: the-evidence/gpt-2

## Authorized work

Scheduled duty for 2026-08-11 returned `the-evidence` as an open section: choose
one document within the beat, do not repeat a published slug. This commission
selects the GPT-2 paper. It is one article, on the lesson template, delivered as
one Article PR.

## The document and why it

Radford, Wu, Child, Luan, Amodei, and Sutskever, "Language Models are
Unsupervised Multitask Learners" (OpenAI, February 2019): the GPT-2 paper. The
reader keeps meeting this document as a story rather than a result. "OpenAI said
GPT-2 was too dangerous to release" is one of the most-cited moments in the
public history of large language models, and almost no one who repeats it has
read what the paper measured. This desk reads the document so the reader knows
what it actually says.

The beat's job here: state what the paper is, who wrote it, and why it became
famous; walk through what it actually did (the WebText corpus, the 1.5B-parameter
model, the zero-shot evaluation across a set of language tasks, the numbers it
got, and the honest scale of each); then bring it to the present (how the staged
release is cited today as precedent, and whether the capability the "danger"
framing implied matched the measured results).

## The angle

The paper's measured contribution and the reason it is famous are two different
things, and the reader should be able to hold both. The measured result is
zero-shot multitask language modeling: one model, trained only to predict the
next token on a large web corpus, tested on tasks it was never fine-tuned for.
Its strong numbers are on language-modeling datasets; on most downstream tasks
(reading comprehension, translation, summarization, question answering) it lands
far below both fine-tuned systems and, in several cases, simple baselines. The
fame is the staged-release decision, which lived in OpenAI's accompanying blog
posts and follow-up report, not in the paper's results tables, and turned on
projected misuse of fluent synthetic text rather than on a measured capability.

Do not moralize the release decision in either direction. Show the paper's actual
numbers and their scale, show what the release documents actually claimed and
what the six-month follow-up found, and let the gap between the two speak. When
today's shorthand ("too dangerous to release") does not match what the document
showed, say so plainly, which is exactly this desk's standard.

## Sources

Source floor for this series: at least 6 sources, at least 3 primary, at least 1
secondary. Primary here is the authoring party's own documents.

Direct the researcher to read, at minimum:
- The GPT-2 paper itself (the PDF/technical report). Read the evaluation tables,
  not the abstract: which datasets are zero-shot language-modeling results and
  which are downstream tasks, the exact model sizes (117M, 345M, 762M, 1.5B), the
  WebText construction (outbound Reddit links, ~40GB, 8M documents), and the
  paper's own hedges.
- OpenAI's announcement blog "Better Language Models and Their Implications"
  (Feb 14, 2019), which is where the staged-release rationale lives.
- OpenAI's release-strategy follow-up, "Release Strategies and the Social Impacts
  of Language Models" (Solaiman et al., Nov 2019) and/or the "GPT-2: 6-Month
  Follow-Up" post, for what the staged release actually found about misuse.
- At least one independent secondary source (contemporary reporting or later
  scholarship) for how the "too dangerous" framing traveled and how it is cited
  now. A repetition of OpenAI's own claim is not independent confirmation of it.

Every figure (parameter counts, dataset sizes, per-benchmark scores, the release
timeline dates) is checked against the primary that owns it. Contested framing
("dangerous") is attributed to the exact document and party that said it.

## Course placement and neighbors

The library already holds `the-evidence/gpt-3-few-shot` (the successor paper's
few-shot result), `the-evidence/scaling-laws-kaplan`, `the-evidence/gpt-4-technical-report`,
and `the-mechanics/in-context-learning`. This lesson is the missing rung between
BERT/word2vec and GPT-3. Link the successor and the scaling paper in Background
rather than re-teaching them; do not re-explain in-context learning or the
transformer, both already taught. Tonight's other new articles are in unrelated
desks (truthfulqa, conversation-memory, technological-unemployment, bing-sydney);
no cross-collision to manage.

## Production policy

Profile `balanced`; no role directive is `required`. Recorded plan: writing-coach
low effort, researcher high effort, writer medium effort, editor high effort;
model class `capable`. Actual harness: `claude-code-routine`. Actual model:
Claude Opus 4.8, recorded in nb-meta as `model`. No required directive was traded
down.

## nb-meta

Date 2026-08-11. Harness `claude-code-routine`. Model `Claude Opus 4.8`. Tags are
the writer's to set as descriptive keywords (this open series configures no tag
fragments); three concise topical tags.

Recent habits to break travel with the writer brief.
