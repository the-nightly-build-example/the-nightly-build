# Commission: the-evidence/resnet

## Assignment
Read "Deep Residual Learning for Image Recognition" (He, Zhang, Ren & Sun,
2015) as the document it is, for a reader who has heard that neural networks
got "deeper" but never saw what actually made depth trainable. State what the
paper is, who wrote it (Microsoft Research Asia), and why it became famous
(ImageNet/COCO 2015 sweep; one of the most-cited papers in all of science).
Walk its real method and numbers: the degradation problem it identified (deeper
plain networks did WORSE on training error, not from overfitting), the residual
/ skip-connection fix, the depths tested (up to 152 and a 1202-layer probe),
and the ImageNet results (3.57% top-5 ensemble error). Show scale honestly.
Then bring it to the present: residual connections now sit inside the very
transformer this course teaches (the "Add & Norm" step), so the paper's real
legacy is a training trick every large model uses, not the depth headline.

## Why this document, now
It is a canonical, ubiquitously cited paper, and the honest story corrects a
common misreading: residuals did not just "add layers," they solved an
optimization failure. The reader who understands why 100+ layers became
trainable understands a load-bearing part of every modern model.

## Angle boundaries
- The subject is the **document**: its problem statement, method, numbers, and
  claims, and how the record held up. Not a general "how CNNs work" explainer.
- Distinct from the published the-evidence/alexnet lesson (AlexNet won ImageNet
  2012 on GPUs; the depth-and-compute turn). ResNet is the 2015 paper about
  making depth itself trainable via residuals. Reference alexnet for the
  ImageNet-competition backdrop; do not re-tell it.
- The tie to transformers is the present-day payoff, but do NOT re-teach the
  attention mechanism or the transformer architecture (the-mechanics/attention
  and the-evidence/attention-is-all-you-need own those). Link them; state only
  that residual connections are reused there, with the paper's own concept.
- Keep the degradation-vs-overfitting distinction exact: the paper's Figure 1
  shows higher TRAINING error for the deeper plain net. That precision is the
  lesson.

## Required contribution
The reader should be able to say what problem the paper solved (deeper plain
nets were harder to optimize, shown by training error), how residual learning
addressed it, one honest scale/number (depth, error rate, or layer count with
a comparison they hold), and why the paper's real influence runs through a
training trick reused far beyond vision.

## This edition (neighbors — keep distinct)
- the-instruments/hallucination-rate — how a reliability number is manufactured
- the-mechanics/thinking-out-loud — why writing steps improves answers
- what-could-go-wrong/sharp-left-turn — a capability jump outrunning safety
- when-ai-breaks/apple-card — algorithmic credit-limit bias

## Template & policy
- Template: lesson.
- Source policy: min 6 sources; >=3 primary, >=1 secondary. Primary: the paper
  (arXiv:1512.03385), later papers analyzing residual nets (e.g. identity-
  mappings follow-up; "loss landscape" or "ensembles of shallow nets"
  analyses), and any doc establishing residuals inside transformers. Secondary:
  citation counts, histories.
- Production policy (balanced): coach low, researcher high, writer medium,
  editor high; model "capable"; none required.
- Actual harness/model this run: harness `claude-code-routine`, model
  `claude-opus-4-8` for every role. Record in nb-meta (date 2026-08-07).

## Habits not to inherit (for the writer brief)
Recent the-evidence pieces (gans, atari-dqn, alphago) open on a myth-vs-record
reveal in the headline ("The X paper credited with Y actually Z", "never
mentions") and lean on one table of the paper's printed numbers. That reveal
frame is the desk's method, but the exact "credited-with / never" headline mold
now recurs across the series — vary it. Find this paper's own opener and dek.
Check the recent library's deks and headings first.
