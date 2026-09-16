# Commission: the-evidence/flashattention

## The document

Tri Dao, Daniel Y. Fu, Stefano Ermon, Atri Rudra, and Christopher Ré,
"FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness,"
NeurIPS 2022 (arXiv:2205.14135). This is the document the lesson reads. Its
claims come from the paper itself and its follow-ups, not from coverage of them.
The researcher confirms every figure below against the paper before the writer
uses it; treat the numbers here as the angle to check, not as settled text.

## Why this document, now

The reader keeps meeting the word "attention" and the claim that a model's
context window grew because of it. FlashAttention is the document behind a lot of
that, and it is routinely described in a way its own abstract contradicts: as an
approximation, a way of skipping attention work, or a change to what attention
computes. The paper says the opposite. It computes the same attention, to the
last bit, and wins by moving less data. Reading it teaches the reader something
the library has not taught yet: that running a transformer is often limited by
how fast numbers move between two kinds of memory on the chip, not by how many
multiplications the chip can do. That idea sits under a great deal of current
talk about speed, cost, and context length.

## The declared reader and the fit

The paper's own vocabulary is GPU systems engineering. The reader is smart, reads
widely, and has never written a CUDA kernel. The lesson's hardest work is making
the memory-hierarchy idea land without hand-waving and without a wall of jargon.
Everything the field takes for granted here gets built up in plain words: what
the attention step computes, why its intermediate result is large, what the two
tiers of on-chip memory are and why one is fast and small while the other is slow
and large, and what "memory-bound" means. Define each such term the first time it
is used, and no earlier.

## What the lesson teaches (a short, complete list)

Teach these ideas in an order where each rests only on the ones before it. Cut
one entirely rather than shrink another to fit; the desk publishes a short list
taught completely.

1. What attention actually computes for a sequence, and why the intermediate
   scores form a table that grows with the square of the sequence length. Keep
   this concrete with a worked size (pick one real sequence length and show the
   resulting table size). No code.
2. The two-tier memory picture on a GPU: a large slow tier and a small fast tier,
   with the real capacity and bandwidth figures the paper cites, so the reader
   can see the gap rather than take "fast" and "slow" on faith. Then "memory-
   bound": the step spends its time moving that table in and out of the slow
   tier, not computing.
3. What FlashAttention changes: it never writes the full score table to the slow
   tier. It works in tiles and keeps a running softmax so it can finish each
   block with only small quantities in the fast tier, and it recomputes cheap
   quantities in the backward pass rather than storing them. State plainly that
   this is exact, and that it does not reduce the number of multiplications (it
   can add some) but reduces the data moved.
4. The numbers the paper actually got, with their scope: the training speedups it
   reports and on which models, the memory scaling it claims (from quadratic to
   linear in sequence length), and the longer-context results it enabled. Show
   the size of each claim honestly, including where a headline number is one
   benchmark rather than a law.
5. Bring it to the present: FlashAttention-2 and FlashAttention-3, adoption into
   standard training and inference stacks, and the gap between what the paper
   showed and how it is described. Name the common misreading and correct it from
   the document: exact vs. approximate, and "fewer FLOPs" vs. "less memory
   traffic."

The original work this lesson owes is the correction in idea 5, made visible:
the reader should leave able to tell a claim that FlashAttention approximated or
skipped attention from what it did.

## Sources plan

Template floor is six sources with at least three primary and one secondary; the
series asks the same three-primary floor. Primary here means the papers that own
the claims: the 2022 FlashAttention paper first, plus FlashAttention-2 and
FlashAttention-3 for the present-day section, and the GPU vendor's own
specification for the memory capacity and bandwidth figures. Secondary reporting
may set context (adoption, reception) but no contested number rests on it. The
researcher reads the cited passages, not the abstracts, and records the exact
sequence lengths, memory figures, and speedups with their denominators and
hardware.

## Continuity and neighbors

Attention itself, the transformer, and the context window are taught in the
library; link them in Background rather than re-teaching them, and check their
exact published slugs before linking. This lesson should leave clean ground for
later pieces on inference cost and serving. Tonight's other lessons are on
unrelated desks (a speech-quality metric, watermarks in generated images, an
argument about future suffering, and an ad-delivery discrimination case); no
overlap to manage, but keep this piece self-contained.

## Recent shapes to break

The Evidence has lately opened several headlines as two sentences where the
second is a short numeric reversal. Do not reach for that mold by reflex. Vary
heading construction; recent pieces lean on short concrete noun-phrase headings,
which is fine, but avoid repeating a neighbor's exact rhythm.

## Production record

Roles run on a capable-tier model (Claude Sonnet) via isolated subagents.
Effort per the balanced profile: researcher high, writer medium, editor high,
writing-coach low. No required directive was traded down. Model and effort are
recorded here as the actual choices for this run.
