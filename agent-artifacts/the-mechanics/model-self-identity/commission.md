# Commission: the-mechanics/model-self-identity

## The behavior

Ask a chatbot which model it is or who built it, and it often answers wrong with
full confidence: a non-OpenAI model says it is ChatGPT, made by OpenAI. One
lesson, one behavior, worked backward to its cause. No code.

## Why this closes a gap tonight (and why it is not a duplicate)

The reader has been taught statelessness (conversation-memory), the training-date
limit (knowledge-cutoff), that the system prompt is just input
(instructions-are-data), and generic fabrication (hallucination). None of them
answers the specific, everyday question "why did this chatbot tell me it was
ChatGPT?" That answer is a clean mechanism lesson: a model has no way to read its
own identity off its weights, so its name has to be put in from outside, and when
it is not, the training distribution decides.

Note for all roles: two topics in tonight's run were dropped after a history
check found the material already published under an unrelated slug. This behavior
was checked against the-mechanics, when-ai-breaks, and the-instruments and is not
covered. Confirm again with `nb history` before drafting.

## What the lesson must teach (short list, taught completely, settled vs open marked)

1. The behavior, shown with a real, dated case: a specific model that identified
   itself as ChatGPT/OpenAI (the researcher verifies which and when; DeepSeek's
   late-2024 model is one reported instance). Give what was asked and what it
   said.
2. Why it happens, step by step, each step a real part of the system:
   - A model predicts the next token from patterns; it has no introspective
     access to its own weights, name, or maker. (settled)
   - Identity is supplied from outside the weights: a system/developer message
     that states the assistant's name and maker, and/or post-training on identity
     questions. Take that away and the model falls back to the base distribution.
     (settled)
   - The base distribution is saturated with text about ChatGPT/OpenAI, and some
     models are trained partly on other models' outputs (synthetic data /
     distillation), so the likeliest completion to "what are you?" is "ChatGPT."
     (mechanism settled; whether a given model's answer comes from web
     contamination or from training on another model's outputs is usually not
     knowable from outside — mark as open)
   - The knowledge cutoff compounds it: a model finished before its own launch has
     no training text about itself. (settled; link knowledge-cutoff)
   Go down until a step where nothing below changes the answer.
3. Where the weakness lives today: a model's self-report is not evidence of what
   it is or who made it, which matters when a self-identification is read as proof
   of provenance or of one company copying another.

## Distinctness and continuity

Not a published slug; verified uncovered. Link, do not re-teach:

- `../the-mechanics/knowledge-cutoff.html` — the training-date limit.
- `../the-mechanics/instructions-are-data.html` — the system prompt is input the
  model cannot distinguish from the user's text; identity injection rides on this.
- `../the-mechanics/conversation-memory.html` — statelessness; link if used.
- `../the-mechanics/hallucination.html` — generic fabrication. This lesson is a
  specific, mechanistically explained case, not generic hallucination; draw the
  line and link.
- `../the-mechanics/memorization.html` — training-data recall; link if used.

## Sources (floor: min 8; primary >=4; secondary >=1)

Primary must include: developer documentation stating how identity is set (a
model spec / system-prompt or model card that names the assistant and maker, e.g.
OpenAI's model spec and/or Anthropic's system prompt); primary evidence of the
behavior (the reproducible model output, a developer's own acknowledgement, or a
model card discussing training-data/distillation); and a primary on the mechanism
(a paper on synthetic-data/distillation contamination, and/or a paper on LLM
self-knowledge/introspection and its limits). Secondary reporting for the reported
cases. If the primary floor is hard to meet with verifiable documents, the
researcher flags exactly what is missing rather than padding. Reproduced model
outputs must be recorded honestly (model, date, that it is a single reproduction).

## Production policy (balanced; nothing marked required)

writing-coach low, researcher high, writer medium, editor high; model "capable".
No required directive; each role records the actual model and effort used.

## Tags

Open section. Suggested: model-identity, system-prompt, distillation, training-data,
self-knowledge. Writer owns the final list.

## Recent-pattern notes (habits not to inherit)

- Mechanics deks recently open with a vivid concrete failure then a comma-joined
  cause ("Ask a chatbot for a random number and it says 7"). Keep the
  concreteness; vary the construction so it is not the same comma-and mold.
- Headlines are full declarative behaviors, often a mini worked example. Good
  form; do not copy a prior lesson's rhythm.
- Headings are argument-step sentences in the piece's own nouns.

## Neighboring articles in tonight's run

the-evidence/palm, the-instruments/gaia, what-could-go-wrong/automated-escalation,
when-ai-breaks/deloitte-ai-report. No topic overlap.
