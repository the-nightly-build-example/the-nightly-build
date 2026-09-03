# Commission: the-mechanics/option-order-bias

## Assignment
Answer "how does it actually do that" for one behavior a reader who leans on AI has
seen: give a model a set of options (a multiple-choice question, "pick the best of
these") and its answer can change when you reorder the options — it leans toward
certain positions or certain labels. Template: lesson, 1200–2200 words, 0–4 flex
sections. No code.

## The behavior and its causes (researcher verifies mechanism and figures)
Work backward from the behavior to ground, each step a real part of the system:
  - The observed effect: reordering the options changes the pick; models show a
    measurable preference for some positions/labels independent of content. The
    canonical demonstrations: Zheng et al. 2023 ("Large Language Models Are Not
    Robust Multiple Choice Selectors" — selection bias and "token bias" toward
    option IDs) and Pezeshkpour & Hruschka 2023 ("...Sensitivity to the Order of
    Options").
  - Why, step by step: (a) the model reads the options as a token sequence, so
    position matters; (b) the answer is usually scored on the probability of the
    option label (A/B/C/D), and the model carries priors over those label tokens
    from training; (c) position effects (primacy/recency) in how the options are
    attended. Mark which steps are settled (the bias is robustly measured) and
    which are open (the exact weighting of label-prior vs position).
  - A small concrete example makes each step real: the same question, options
    permuted, the pick moving.

## Required contribution
The reader can explain why reordering options changes a model's choice, and can
tell when a benchmark score or a model's "pick" reflects the answer format rather
than the model's knowledge.

## Source obligations
Minimum 8 sources, primary >= 4, secondary >= 1. Primary: Zheng et al. 2023,
Pezeshkpour & Hruschka 2023, Robinson et al. (MCQA with LLMs), and any primary on
the debiasing fixes or on first-token-probability scoring. Mark open mechanistic
questions as open.

## Do NOT repeat published coverage (the-mechanics)
Already published (do not repeat slug or topic): prompt-sensitivity (answers
change with phrasing), reversal-curse, in-context-learning, false-confidence,
sycophancy, structured-output, negation, counting-letters, random-numbers,
nondeterminism, losing-the-thread, and others. This lesson's distinct core is
positional/label bias among presented options — not phrasing sensitivity and not
sycophancy. Link prompt-sensitivity where it helps; do not re-teach it.

## This edition's neighbors (avoid overlap)
Siblings tonight: the-evidence/mixture-of-experts, the-instruments/
task-time-horizon, what-could-go-wrong/algorithmic-collusion, when-ai-breaks/
clearview-ai. This is the only pure-mechanism piece; keep it on how the system
produces the behavior, not on benchmark-metric design (though it may note, in one
line, why this matters for benchmark scores — the instruments desk owns metrics).

## Production policy (balanced; none required)
writing-coach low, researcher high, writer medium, editor high — capable model,
this session's configured capable model. No required directive.

## Recent shapes to break
See the writer brief's shared note. The mechanics desk defaults to a short
declarative "reveal" first heading; vary heading construction across this piece.
