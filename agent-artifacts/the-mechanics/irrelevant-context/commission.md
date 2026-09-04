# Commission: the-mechanics/irrelevant-context

## Assignment

The Mechanics starts from one behavior a reader has seen and explains what
produces it. Tonight's behavior: take a problem a model solves correctly, then
change something that should not matter, rename the people, swap the numbers for
different ones, or add one true but irrelevant sentence, and the model's answer
gets worse. The logic of the problem is untouched; only its surface changed. Work
backward from the behavior to its cause, step by step, marking which steps are
settled and which are open. No code.

The reader should leave able to explain why a system that looks like it is
reasoning can be thrown by a detail a reasoner would ignore, name what in the
model produces that, and tell when someone's claim that a model "reasons" is
outrunning what the test showed.

## The behavior, measured

Two documents anchor it. Shi et al., "Large Language Models Can Be Easily
Distracted by Irrelevant Context" (2023), built GSM-IC by adding one irrelevant
sentence to grade-school word problems and measured the accuracy drop. Mirzadeh
et al., "GSM-Symbolic" (Apple, 2024), regenerated the same problems with
different names and numbers and measured the spread across versions, then added
an irrelevant-but-topical clause ("GSM-NoOp") and measured a larger drop. The
researcher must recover the real numbers: how far accuracy moved under a surface
change, how far it dropped with an added irrelevant clause, and across how many
models, so the reader sees the size of the effect and not a slogan.

## Work backward: the steps the lesson owes

Take the reader from the behavior down to ground:
- What the model receives: the problem is a sequence of tokens, and the model
  conditions its next token on all of them at once. It has no separate, symbolic
  representation of the problem to reason over. (Tokens and attention were taught
  earlier; link, do not re-teach.)
- Why surface matters: the model's output is shaped by how closely the whole
  prompt matches patterns seen in training. Change the names or numbers and the
  match is weaker; add a topical irrelevant sentence and its tokens pull the
  computation, because nothing gives the model a reliable filter for relevance.
- What this says about "reasoning": the settled reading is that much of the
  behavior is pattern-completion sensitive to surface form. How much genuine
  step-by-step computation sits on top of that is the open, contested part; say
  so, and represent the strongest version of each side.

## Boundaries

- The subject is sensitivity to logically-irrelevant surface change. Keep it
  distinct from published mechanics lessons the reader may have: getting-math-
  wrong is about executing arithmetic, prompt-sensitivity is about formatting and
  phrasing of the same question, and in-context-learning is about learning from
  examples. Link any the argument leans on; do not re-teach or restate them.
- Math word problems are the evidence base, so use them, but the lesson is about
  reasoning robustness, not arithmetic. Do not let it become a second
  getting-math-wrong.
- Define any term of art in plain words at first use.

## Sources to start from

Primary: Shi et al. 2023 (GSM-IC, arXiv 2302.00093) and Mirzadeh et al. 2024
(GSM-Symbolic, arXiv 2410.05229) for the effect; supporting primary work on
brittle reasoning under surface change (for example the "Alice in Wonderland"
breakdown paper, Nezhurina et al. 2024, or a memorization-versus-reasoning study)
for breadth; and a source for the settled/open reading of what the effect implies
about reasoning. At least one secondary source for how the finding was discussed.
Series policy requires at least eight sources, at least four primary. Verify every
reported drop and spread against the paper that owns it, and keep the
settled/open line honest.

## This edition's neighbors

Four other lessons tonight: the-evidence/deep-double-descent,
the-instruments/attack-success-rate, what-could-go-wrong/liars-dividend,
when-ai-breaks/houston-teacher-evaluation. No overlap; write for a reader who has
not read them.

## Recent coverage in this series, and habits not to inherit

The last five Mechanics lessons were option-order-bias,
counting-objects-in-images, quantization, hands-in-generated-images,
random-numbers. Break, do not reproduce:
- The headline that quotes a prompt and its wrong result; it is this desk's most
  frequent move. Find a different construction.
- Title Case headings appeared recently; the house is sentence case.
- The backward-from-behavior arc often ends on a "what the fixes reach" section;
  name and build the close in this piece's own terms.

Furniture rotates through the stat strip, the figure, the note, and the table. A
before/after of a surface change, or the spread across regenerated versions, may
want a table or a small figure from the verified series. Use only what makes a
step concrete.

## Production record

Production policy (the-mechanics): profile balanced; every stage required: false;
model "capable"; effort high for researcher and editor, medium for writer, low
for writing-coach. Harness: claude-code-routine. Model resolved to
claude-opus-4-8 for every role. No required directive traded down. Writer records
model claude-opus-4-8, harness claude-code-routine, date 2026-09-04.

## Tags

Suggested: reasoning, robustness, gsm-symbolic, pattern-matching. The writer may
adjust.
