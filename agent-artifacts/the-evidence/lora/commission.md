# Commission: the-evidence/lora

## The document

Hu, Shen, Wallis, Allen-Zhu, Li, Wang, and Chen (Microsoft), "LoRA: Low-Rank
Adaptation of Large Language Models" (2021; ICLR 2022). It freezes a pretrained
model's weights and trains, instead, a small pair of low-rank matrices added
alongside them. For GPT-3 175B the paper reports about 10,000 times fewer
trainable parameters and roughly a threefold cut in GPU memory, while matching
or beating full fine-tuning on its benchmarks, and, because the added matrices
can be folded back into the original weights, no extra cost at inference time.
The method rests on the hypothesis that the weight change during adaptation has
a low "intrinsic rank."

## Why this lesson, now

The course has taught what a parameter is (the-instruments/parameter-count),
how training adjusts weights (the-mechanics/gradient-descent), and several
things done to a model after pretraining (instructgpt, direct-preference-
optimization). It has never taught how a model gets specialized cheaply, which
is the step behind almost every open-model fine-tune, every low-cost "custom"
model, and the adapter marketplaces the reader keeps hearing about. LoRA is the
document that made that cheap, and reading it shows exactly what "fine-tuning a
model" now usually means.

## The angle to test

Walk through what the paper actually did and measured: the frozen base plus the
trainable low-rank pair, where in the network they inserted it (attention weight
matrices), the rank values they used (as small as 1 to 8 in places), and the
headline numbers with the models and tasks behind them (GPT-3 175B, GPT-2,
RoBERTa/DeBERTa on GLUE, E2E, WikiSQL). Show the scale honestly: "matches full
fine-tuning" is a result on those models and those tasks, not a law. Then bring
it to the present. LoRA and its quantized successor QLoRA (2023) are how most
fine-tuning ships today, and the "matches full fine-tuning" claim gets repeated
as if unconditional, while later work (for example "LoRA Learns Less and Forgets
Less," 2024) finds it trails full fine-tuning on harder domains such as code and
math and changes the model less. Say plainly where the paper's result holds and
where today's usage claims more than it showed. The zero-inference-latency
property (the matrices merge into the base weights) is real and worth teaching,
because it is what separates LoRA from adapters that add layers.

The researcher must verify the trainable-parameter and memory reductions against
the paper's own tables, the exact ranks reported, at least one benchmark where
LoRA matched or beat full fine-tuning, and the "intrinsic rank" framing in the
authors' own words. The 2024 limitation and the QLoRA extension must come from
their own papers.

## Boundaries

Read the primary documents: the LoRA paper, QLoRA, and the later limitation
study, plus a source for how widely LoRA/PEFT is used now. Do not re-teach what
a parameter, a weight matrix, or gradient descent is; link parameter-count and
gradient-descent in Background. This is one of five lessons tonight; the others
cover an embedding benchmark, format-constrained decoding, an AI-safety
argument, and a deployment failure. No overlap with them.

## Source policy

Series floor: 6 sources, at least 3 primary and at least 1 secondary. The LoRA,
QLoRA, and limitation papers are primary to their own claims. Meet the floor
with sources that change the reading, not padding.

## Production

Profile balanced; no stage required. This run: writing-coach and researcher on
the strong model, researcher at high effort; writer at medium effort; editor at
high effort.

## Recent habits not to inherit

- The two-clause dek joined by "and" or "but" is the house default right now.
  Build this dek a different way, and avoid the three banned dek molds in
  `spec/headlines.md`.
- Section headings starting "How...", "What...", or "Where..." are overused, and
  the-evidence keeps closing on a "Where X still..." present-day section. The
  present-day turn is required by the series; vary its phrasing and its heading.
- The "Why this matters" opener keeps ending by telling the reader "Read it and
  you can see...". Hand off to the reader some other way.
