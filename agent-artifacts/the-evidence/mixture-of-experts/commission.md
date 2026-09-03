# Commission: the-evidence/mixture-of-experts

## Assignment
Read one famous AI document and tell the reader what it actually says: Shazeer et
al., "Outrageously Large Neural Networks: The Sparsely-Gated Mixture-of-Experts
Layer" (2017, arXiv 1701.06538) — the paper that made sparse mixture-of-experts
practical. Bring in Switch Transformer (Fedus et al. 2021) and GShard (Lepikhin
et al. 2020) as later primaries where they confirm, correct, or scale the idea.
Template: lesson, 1200–2200 words, 0–4 flex sections.

## Why this document, now
Most frontier models today are described as mixture-of-experts, and their
headline parameter counts (hundreds of billions, "a trillion") come straight from
this line of work. The public number almost always reports total parameters, not
the few actually used per token. This desk opens the founding paper and shows
what sparse MoE really does and what the big numbers mean.

## The document, in brief (researcher verifies every figure)
- The idea: instead of every input passing through the whole network, a gating
  network routes each token to a small number of "expert" sub-networks; only
  those experts compute. Parameter count grows without a proportional rise in
  per-token compute.
- The claim that made it famous: Shazeer et al. reached very large models (report
  the exact parameter count, up to ~137B in the LSTM MoE) with sub-linear compute
  growth and better language-modeling/translation results at fixed compute.
- Scale honestly: the actual sizes, expert counts, and the compute vs total-
  parameter gap in the paper. Switch Transformer's trillion-parameter figure is a
  total, with a small active fraction per token — make that distinction the spine
  of the honesty section.
- Bring to present: MoE is now standard in shipped models; the routing problems
  (load balancing, instability) later work addressed; and the recurring public
  confusion between total and active parameters. Where a "N-billion-parameter MoE"
  headline does not match what runs per token, say so plainly.

## Required contribution
The reader finishes able to explain sparse MoE (route each token to a few
experts), why it decouples parameter count from per-token compute, the honest
scale of the original result, and why an MoE model's advertised parameter count
overstates what actually runs on any given token.

## Source obligations
Minimum 6 sources, primary >= 3, secondary >= 1. Primary: the Shazeer 2017 paper,
Switch Transformer, GShard, and/or a shipped-MoE technical report (e.g. Mixtral or
DeepSeek-MoE) for the present-day usage. Claims about each paper come from that
paper. Contested/precise figures need a primary source.

## Do NOT repeat published coverage (the-evidence)
Already published in this series (do not repeat the slug or the topic): attention-
is-all-you-need, foundation-models, scaling-laws-kaplan, the-bitter-lesson,
gpt-3-few-shot, gpt-2, bert, vision-transformer, resnet, alexnet, seq2seq,
word2vec, clip, gans, lora, constitutional-ai, instructgpt, and others. No prior
lesson covers mixture-of-experts. Teach architecture terms the reader needs
(gating/router, expert, sparse vs dense) in plain words; "attention"/transformers
were taught in the mechanics desk and the attention-is-all-you-need lesson — link
rather than re-teach.

## This edition's neighbors (avoid overlap)
Four siblings publish tonight: the-instruments/task-time-horizon,
the-mechanics/option-order-bias, what-could-go-wrong/algorithmic-collusion,
when-ai-breaks/clearview-ai. No topical overlap; keep this piece on the MoE
document and its parameter-count honesty, not on evaluation metrics.

## Production policy (balanced; none required)
writing-coach low, researcher high, writer medium, editor high — capable model,
this session's configured capable model. No required directive.

## Recent shapes to break
See the writer brief's shared note.
