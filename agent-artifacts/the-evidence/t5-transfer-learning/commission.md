# Commission: the-evidence/t5-transfer-learning

## Assignment

Teach the reader the T5 paper: "Exploring the Limits of Transfer Learning with a
Unified Text-to-Text Transformer" (Colin Raffel, Noam Shazeer, Adam Roberts, and
coauthors at Google, 2019, revised 2020). This is The Evidence: read the document
so the reader knows what it actually says and did.

The lesson states what T5 is, who wrote it, and why it became a reference point.
It walks what the paper actually ran: the text-to-text framing that casts every
task as feeding the model text and reading text back, the C4 dataset the authors
built from Common Crawl, the systematic comparison of pretraining objectives,
architectures, and dataset sizes, and the final 11-billion-parameter model. Give
the real figures the reader cannot scale on their own, anchored to a comparison
they hold: the size of C4, the pretraining scale, the benchmark results the
paper reported. Show what the study is and is not evidence for.

Then bring it to now: the text-to-text framing is what the reader meets whenever
a single model is asked to translate, summarize, classify, and answer in one
interface, and T5's controlled comparison is still cited to settle claims about
what pretraining choices matter. Say plainly where later work moved past it
(decoder-only scaling, instruction tuning) and where its findings held.

## Boundary and contribution

One document, the T5 paper itself, read firsthand. Claims come from the paper,
not from coverage of it. The required contribution: the reader can say what T5
measured, how big the study was, and what the "text-to-text" idea concretely
means, and can tell when someone cites T5 for more than it showed. Do not drift
into a general history of transfer learning or a survey of every model since.

The reader is the paper's declared reader (see `editorial-direction.md`): smart,
widely read, no time in a codebase. Transformers, attention, BERT, GPT-2/GPT-3,
sequence-to-sequence, and scaling laws are already taught in this library; link
the earlier lesson at first use instead of re-teaching it. Candidates for
Background linking: the-mechanics/attention, the-evidence/bert,
the-evidence/gpt-3-few-shot, the-evidence/scaling-laws-kaplan. The writer
chooses.

## Source policy

Series and lesson floor (from `nb source-policy --series the-evidence`): at least
6 sources, at least 3 primary, at least 1 secondary. Primary is the T5 paper
itself (arXiv 1910.10683) and its released artifacts (the C4 dataset
documentation, the model card / code). Secondary reporting supplies context only.

## Production policy

From `nb production-policy --series the-evidence`: profile balanced, model tier
"capable", none required. Effort: researcher high, writer medium, editor high,
writing-coach low. No required model or effort directive to honor or trade.
Runtime: roles run as Claude Code Agent subagents; researcher, writer, and editor
on claude-opus-4-8, writing-coach on a capable model at low effort. The writer
records its actual model (claude-opus-4-8) and harness ("Claude Code") in
nb-meta. Publication date: 2026-09-07.

## This edition's neighbors

Four other lessons publish tonight; keep this piece distinct from each:
the-instruments/math-benchmark (a measurement), the-mechanics/illegal-chess-moves
(a behavior), what-could-go-wrong/sleeper-agents (a risk argument),
when-ai-breaks/replit-agent-deletes-database (an incident). No overlap in subject.

## Recent habits to break

Checked against the last eight The Evidence lessons. Break these:

- The dek mold "<Authors>'s <year> paper <did X>, then/and <measured Y>" recurs
  across dropout, constitutional-ai, denoising-diffusion, and adversarial-examples.
  Do not open the dek with "Raffel et al.'s 2020 paper...". Find the surprise T5
  actually holds and lead with it.
- Headlines that frame the finding as "the company's own report can't/does X"
  (llama-3-herd-of-models) are a recent shape; do not reach for it by reflex.
- The phrasings "measured it directly" and "in its own experiments" recur in
  recent deks. Say the specific thing instead.
- Anchoring the whole opener on one benchmark number is the recent default. A
  number may lead if it is genuinely the surprise, but vary the construction.
