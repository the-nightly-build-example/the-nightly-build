# Commission: the-mechanics/false-premise-questions

## Assignment

Start from a behavior anyone who uses a chatbot has seen: ask it a question that
smuggles in a false assumption — a book that was never written, an event that
never happened, "why did so-and-so do a thing they never did" — and instead of
challenging the assumption, it answers as if the assumption were true, often in
fluent detail. Explain what produces that.

This is a lesson on The Mechanics: work backward from the behavior to its cause,
one step at a time, each step naming a real part of the system and what it does,
with a small concrete example where it helps. Keep going down until the reader
hits a step where nothing below it would change the answer. Mark which steps are
settled engineering and which are open even to the people who build these
systems. No code.

## The gap this closes

Nearby covered behaviors are close but not this one, and the reader should be
able to tell them apart: `the-mechanics/hallucination` (inventing facts),
`false-confidence` (stating wrong answers with unearned certainty), `sycophancy`
(changing an answer to agree once the user pushes back), `negation` (mishandling
"not"). This behavior is specifically the failure to challenge a question's
built-in assumption before answering it. Link `hallucination` and `sycophancy` at
first use to mark the boundary; do not re-teach them.

## Required contribution

Leave the reader able to predict when a model will swallow a false premise, and
to catch an explanation that skips a step. The chain the evidence should let the
writer build, without prescribing its wording:

- A question carries presuppositions: "why did X do Y" takes for granted that X
  did Y. The presupposed content sits in the prompt, so a next-token predictor
  conditions on it as given.
- The training distribution almost never follows such a question with a
  correction; it follows it with an answer. The prior therefore favors answering,
  not flagging. This is the step to make concrete with the real behavior.
- Post-training rewards being helpful and answering; it does not reliably install
  "reject the premise first." Where that leaves recent models is the open part.
- The ground: the next-token objective over a corpus where premise-corrections
  are rare. Below that, nothing changes the default.

Mark clearly what is settled (the objective and the data distribution) and what
is open (whether and when models detect false premises, whether steering or
fine-tuning fixes it, and whether "detecting the premise" is understanding or
another pattern). Use the primary evaluations for the open part rather than
asserting a verdict.

## Sources

Floor (from `nb source-policy`): at least 8 sources, at least 4 primary, at least
1 secondary. Primary means the document that owns the claim: the research papers
that define and measure false-premise / questionable-assumption question
answering and presupposition verification, and any newer primary evaluation of
current models. Read the papers and their exact results; a measured rate must
name the model and dataset it came from. Secondary explainers are context only.

## Template and metadata

Template: `lesson`. `nb-meta` tags (writer sets, 4-6, lowercase hyphenated),
candidates: false-premises, presupposition, next-token-prediction,
instruction-tuning, hallucination. Date 2026-09-21. `harness` "claude-code";
`model` the writer's actual served model.

## This run's neighbors

Four other lessons publish tonight: `the-evidence/backpropagation`,
`the-instruments/comet-score`, `what-could-go-wrong/negative-side-effects`,
`when-ai-breaks/chatgpt-data-leak`. Distinct subjects; nothing to deconflict.

## Recent shapes to break (habits, not rules)

Recent The Mechanics lessons (familiar-pattern-override, output-diversity) open
on a vivid one-line behavior, then "the probability is piled on the wrong
answer," then "the obvious fix doesn't work," and close on "what it doesn't touch"
or "more training doesn't reliably beat it." The dek mold "training presses X so
hard into its probabilities that Y" recurs. Find this piece's own order and
closer; do not default to a "the fix doesn't work" penultimate section.

## Production policy (actual)

`nb production-policy`: profile `balanced`, tier `capable`, no `required`.
Resolved for this run's isolated subagents: researcher Opus 4.8 (high),
writing-coach Sonnet (low), writer Opus 4.8 (medium), editor Opus 4.8 (high).
Efforts advisory.
