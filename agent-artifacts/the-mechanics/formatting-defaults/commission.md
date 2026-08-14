# Commission: the-mechanics/formatting-defaults

## Authorization

Scheduled run for 2026-08-14 (Fri). `nb duty` returned the-mechanics as an open
section: choose a topic within the beat, do not repeat a published slug. One of
five articles commissioned tonight, one per due series.

## The behavior

Ask a chatbot almost anything and the answer comes back as a bulleted list with
bold headers, even when two sentences would have served. Anyone who uses these
systems has seen it. The lesson works backward from that habit to what produces
it.

## Angle

Walk the chain from the visible behavior to ground. The model produces text one
token at a time from a learned probability distribution (link the-mechanics
autoregressive-generation), and after a question-like prompt it puts high
probability on the tokens that start lists and headers. The next step down is
where that preference came from: markdown-heavy pretraining text, then
instruction-tuning data whose answers are formatted as structured lists, then the
preference-tuning stage where human raters and the reward model favor skimmable,
structured, often longer answers. The reader should be able to name each real
part and what it does, with a concrete example at each step. Reach ground: the
format is a learned output policy, not something the task requires, which is why
a system prompt or a plain instruction can turn it off. Mark what is settled
(post-training shapes format; raters prefer structure) and what is open (how much
each stage contributes, since labs do not publish the full reward details). No
code.

## Boundaries and neighbors

- Template: `lesson`. No open-item tags.
- Source policy: at least 8 sources, at least 4 primary and at least 1 secondary.
  Primary is the research that owns each claim: instruction-tuning and RLHF
  papers, the style-controlled Chatbot Arena analysis, published preference /
  annotation guidelines, and any lab documentation of formatting behavior.
- Differentiate from the-mechanics/prompt-sensitivity, which is about input
  formatting changing a model's accuracy. This piece is about the model's default
  output formatting and where it comes from. Link it, do not overlap it.
- The-mechanics/sycophancy and the-evidence/instructgpt already touch preference
  tuning; the-instruments/chatbot-arena-elo already showed markdown and length
  raising win rate. Link these as Background and build on them rather than
  re-teaching RLHF or the Arena result from scratch.
- Tonight's the-evidence/textbooks-are-all-you-need also discusses training data
  quality; keep this piece on output formatting and post-training, not data
  curation.

## Production record

- Profile: balanced. Stages (model / effort, none required): writing-coach
  capable / low, researcher capable / high, writer capable / medium, editor
  capable / high.
- Harness: each role runs as an isolated subagent on the configured capable
  model; deviations recorded per role.
- Workspace: `.nb-work/the-mechanics/formatting-defaults`.
- Article: `library/the-mechanics/formatting-defaults.html` under that workspace.
