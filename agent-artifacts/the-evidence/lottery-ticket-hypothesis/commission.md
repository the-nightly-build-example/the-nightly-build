# Commission: the-evidence/lottery-ticket-hypothesis

## The document

Jonathan Frankle and Michael Carbin, "The Lottery Ticket Hypothesis: Finding
Sparse, Trainable Neural Networks," ICLR 2019 (best-paper award). It is famous
for a striking claim: inside a dense network sits a small subnetwork ("winning
ticket") that, trained from the original initialization, matches the full
network's accuracy. This desk reads the document so the reader knows what the
experiments actually showed and how the claim held up.

## The angle

State what the paper is, who wrote it (Frankle and Carbin at MIT CSAIL), and why
it became a touchstone in arguments about network pruning, over-parameterization,
and why big models can be shrunk. Then walk through what it actually did:

- The method, iterative magnitude pruning: train, prune the smallest-magnitude
  weights, reset the survivors to their original initial values, repeat. The
  reset to the *original* initialization is the paper's real surprise; a pruned
  net reinitialized randomly does not match it. Teach this concretely.
- The scale honestly: which networks and datasets the central result was
  demonstrated on (small vision nets on MNIST and CIFAR-10), the sparsity levels
  reached, and the accuracy matched. Small studies get cited as laws; show the
  size of the foundation.
- What "winning ticket" does and does not claim: it is an existence result found
  by pruning after training, not a way to find the subnetwork cheaply up front.
  The tickets are found in retrospect. Say this plainly, because the popular
  reading often skips it.

Then bring it to the present: how the finding gets used now, and what later work
confirmed, corrected, or complicated. The honest arc the record supports: the
original method did not transfer to large networks until Frankle's own follow-up
("Linear Mode Connectivity and the Lottery Ticket Hypothesis," 2020) introduced
rewinding to an early-training point rather than initialization; and the practical
payoff (finding a cheap trainable sparse net up front) remains limited. When
today's usage outruns what the document showed, say so.

The reader should leave able to explain what a winning ticket is, what the
experiment proved, and where the shorthand runs past the evidence.

## Template and furniture

Lesson template. The pruning-to-sparsity numbers and the reset-vs-random
comparison may want a small table or a stat strip if the evidence supplies clean
figures. A chart only from a verified series. Furniture is the writer's call with
the editor, never a quota.

## Sources and production

- Source policy: lesson under the-evidence, minimum 6 sources, at least 3
  primary, at least 1 secondary. Primary: the ICLR paper, Frankle's 2019/2020
  follow-ups, and the critique/replication literature (e.g. Liu et al.,
  "Rethinking the Value of Network Pruning"; Zhou et al., "Deconstructing Lottery
  Tickets"). Read the primary documents.
- Production policy (balanced), model/effort used this run: writing-coach capable
  (claude-opus-4-8) low; researcher capable (claude-opus-4-8) high; writer capable
  (claude-opus-4-8) medium; editor capable (claude-opus-4-8) high. Harness:
  claude-code-routine.

## This edition's neighbors (all distinct in subject)

- the-instruments/rouge (a summarization metric), the-mechanics/multilingual-gap
  (why models are worse in other languages), what-could-go-wrong/emergent-
  misalignment (a 2025 finetuning safety result), when-ai-breaks/tessa-eating-
  disorder-chatbot (a deployed-chatbot harm). No overlap with this document; keep
  each piece self-contained.
- On the shelf, the-bitter-lesson mentions pruning only in passing; this is the
  first lesson on the lottery-ticket result. Do not assume that reference taught
  it.

## Habits not to inherit

- Do not open Why-this-matters with the paper-wide "By the end you will know X.
  You will also see Y" formula.
- Do not order the body orientation -> a section named for a parameter/scale
  figure -> findings by reflex; order by what the reader needs. Do not land the
  takeaway on negative parallelism ("It is a real X. It is not yet a Y").
- Deks: avoid the banned molds in the headline standard.

## Required contribution

The article reads a celebrated existence result back against its own method and
scale, and gives the reader a way to tell "a small trainable subnetwork exists,
found by pruning after training on small vision nets" from the larger claim the
phrase now carries.
