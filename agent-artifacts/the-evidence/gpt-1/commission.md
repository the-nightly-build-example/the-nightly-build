# Commission: the-evidence/gpt-1

## Assignment
Read the June 2018 OpenAI paper "Improving Language Understanding by Generative
Pre-Training" (Radford, Narasimhan, Salimans, Sutskever) as the document that
introduced the model now called GPT-1. Teach what the paper actually did and how
its recipe became the ancestor of every later GPT.

## The document, and what to establish
- What it is and who wrote it: a 2018 OpenAI technical report, published as a
  preprint, not a peer-reviewed conference paper. Establish its status honestly.
- The method it ran, step by step: unsupervised generative pre-training of a
  decoder-only Transformer language model on a large book corpus, then
  supervised fine-tuning on each downstream task, with task-specific input
  transformations so one architecture handles classification, entailment,
  similarity, and multiple-choice.
- The scale, stated plainly: parameter count, the training corpus and its size,
  and how many downstream tasks it was evaluated on. Give the figures the paper
  reports, and anchor the parameter count against a present-day model so the
  reader feels how small it was.
- The results the paper got: the number of tasks it improved over prior state of
  the art, and the size of those gains where the paper reports them. Do not
  inflate. Some gains were small.
- The present: how the two-stage recipe scaled into GPT-2, GPT-3, and after, and
  which part of the 2018 method later practice dropped or replaced (task-specific
  fine-tuning and input transformations giving way to prompting at scale). Where
  the paper's own framing no longer matches how these models are built, say so.

## Why this document, why now
The paper is the origin of the generative-pretraining paradigm every current
language model inherits, and the course has taught the descendants
(the-evidence/gpt-2, gpt-3-few-shot, gpt-4-technical-report) without ever reading
the origin. This closes that gap and gives later lessons a fixed point to refer
back to.

## Boundaries: link, do not re-teach
- the-evidence/bert already runs the BERT-versus-GPT-1 contrast and states
  GPT-1's layer count and width. Do not rebuild that head-to-head. Reference it
  in Background and spend this lesson on GPT-1's own method, corpus, and results.
- the-evidence/attention-is-all-you-need already teaches the Transformer and
  already points forward to this paper. The decoder architecture is taught
  ground: link it, state only what GPT-1 did with it.
- Tokenization and embeddings are taught (transformers-first-principles/
  tokenization, transformers-first-principles/embeddings). Link at first use.
- Fine-tuning as a general idea appears in the-evidence/t5-transfer-learning and
  the-evidence/bert. Do not re-teach transfer learning from scratch.

## Neighbors this edition (avoid cross-piece overlap)
Tonight's edition also runs the-instruments/winogrande, which reads a
commonsense benchmark from the same BERT/GLUE era. Keep GPT-1 on the model and
its recipe; leave benchmark-artifact analysis to that piece. Do not both retell
the GLUE story.

## Sources
Lesson floor: at least 6 sources, at least 3 primary and at least 1 secondary.
Primary is the GPT-1 paper itself and other papers or model reports whose claims
you cite firsthand (e.g., the later GPT reports for the "how the recipe scaled"
claims, the BooksCorpus source, the GLUE benchmark paper). Secondary is outside
reporting or analysis used only for context. Read the GPT-1 paper in full,
including its tables.

## Production record
- Profile: balanced. Roles run as isolated Claude subagents (capable tier).
- Effort by stage: writing-coach low, researcher high, writer medium, editor high.
- The writer records the actual writer model in nb-meta `model` and sets
  `harness` to `claude-code`. Article date: 2026-09-17.

## Recent habits to break (from the current library)
- Do not build the headline or dek as the two-sentence "[Claim]. [Terse
  rebuttal]." mold now common in the paper (computing-machinery-and-intelligence,
  apple-intelligence-summaries).
- the-evidence deks have leaned on a lead figure plus a reversal (flashattention,
  mamba, imagenet-database). Find this piece's own dek; a number is not required.
- Avoid a section heading built as "The one number in the paper" (computing-
  machinery-and-intelligence) or the exact FlashAttention full-sentence-with-a-
  figure heading rhythm on every subhead. Vary how headings are built.
- Do not close the body with a Verdict block; the takeaway bookend lands the
  judgment.
