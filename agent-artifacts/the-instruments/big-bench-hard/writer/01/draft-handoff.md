# draft-handoff: the-instruments/big-bench-hard (01)

## Original work

The article traces one model-card percentage (Claude 3 Opus, 86.8% BBH) back
through the three constructions that produced it (BIG-bench's assembly, the
23-task filter against the average expert-rater, and the chain-of-thought
setting), then sets OpenAI's *withheld* GPT-4 score beside the 83.1% the Claude 3
card publishes for GPT-4 to show that a single row readers take as a head-to-head
is comparing numbers of different provenance, one of them from a test its own
maker excluded as contaminated.

## Proof result

`./nb check ... --series the-instruments --library <checkout>` (links on):
**BLOCK: 0, verdict PUBLISHABLE.** 8 sources (6 primary, 2 secondary), 1726
words, 8 min. 0 em-dashes; no banned terms.

Warnings left (3), all `W-SENTENCE-DENSITY`, left intentionally:
- The "Why this matters" opener carries two parallel enumerations: the colon-list
  naming what the lesson takes apart, and the closing question-list that poses the
  lesson's three questions (what the tasks were, who set the bar, whether the
  answers had leaked) which the takeaway resolves. The orientation paragraph's
  "three earlier decisions" colon-list previews the three body sections. Each is a
  controlled long sentence whose parallel structure is the point; splitting them
  into fragments would break the setup/resolution pairing the lesson template
  asks for. Held per `spec/editorial.md` ("A long sentence under control is good
  writing").

Contested task count handled per brief: 204 attributed to the BIG-bench paper
(s2), the 209 funnel start attributed to the BBH paper (s3); the two readings are
not crossed. "Chain-of-thought beats humans" is stated as model- and
task-specific (Codex-CoT clears 67.7%, PaLM-CoT does not but wins 10/23 tasks
individually), never flat. Human-rater bar reported honestly as the mean of a
small, unspecified expert team allowed internet search, sitting far below the
max-human 94.4%; the article states plainly that the papers never give the rater
count.

## Open question

None blocking. One decision for the editor's awareness: I did not capture the
Claude 3 card's "BIG-Bench-Hard" row as a source asset (it would show the
"3-shot CoT" label and footnote 7 provenance visually). The chart (answer-only
vs CoT against the two human lines) plus prose carry the argument, and the
card's contents are quoted and cited in the contamination section, so a second
figure read as furniture-for-its-own-sake risk outweighed the gain. Reversible
if the editor wants the row shown.
