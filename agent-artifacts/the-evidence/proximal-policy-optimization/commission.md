# Commission: the-evidence/proximal-policy-optimization

## Subject
The document is the Proximal Policy Optimization paper: Schulman, Wolski,
Dhariwal, Radford, Klimov, "Proximal Policy Optimization Algorithms" (OpenAI,
July 2017). It is the reinforcement-learning algorithm that later became the
optimizer inside RLHF. This desk reads the document itself.

## Why this document, now
The course has already taught the RLHF pipeline from several angles:
`deep-rl-from-human-preferences`, `instructgpt`, and `direct-preference-optimization`
are published. Every one of them runs on, or defines itself against, PPO, and
the desk never read the PPO paper on its own terms. `deepseek-r1` (published)
trains with GRPO, a PPO descendant, so the algorithm is in live circulation. This
is the "document the course just made readable" case: the reader now has the
surrounding pieces and is owed the engine under them.

## Angle / what the lesson teaches
State what the 2017 paper actually proposed and why it displaced its
predecessor. Teach, in plain words and one worked example, the single idea the
paper is famous for: the clipped surrogate objective that lets a policy take
several gradient steps on one batch of data without the update running away.
Show honestly what the paper measured (continuous-control MuJoCo tasks and Atari,
small by today's standards) versus how the name is invoked now (the default
optimizer for tuning language models, a use the paper never tested). Bring it to
the present: PPO is still the RLHF workhorse, but DPO removes it and GRPO
(DeepSeek) simplifies it; say what each keeps and drops. Where the paper's own
claims were modest or hand-wavy (it is a famously informal paper with little
theory), say so.

## The article's distinct contribution
Separate what the paper proved (a robust, simpler-to-tune policy-gradient method
on 2017 RL benchmarks) from what the field now trusts it for (aligning
billion-parameter models), and show that the bridge between the two was built
after the paper, by other work. Do not re-teach RLHF: link the published lessons
in Background and spend the words on the optimizer itself.

## Template & policy
- Template: `lesson` (fixed for this series).
- Source policy: min 6 sources; at least 3 primary, at least 1 secondary.
- Production policy (`balanced`, none `required`): researcher effort high,
  writer medium, editor high, writing-coach low. Actual models used this run:
  writing-coach on a capable model (Claude Sonnet class), researcher/writer/editor
  on a capable model (Claude Opus class). No `required` directive to honor or
  deviate from.
- Tags: none (open item; duty returned no tag fragments).

## Neighbors in this run (differentiate)
Four other lessons run tonight: `the-instruments/mmlu-pro`,
`the-mechanics/negation`, `what-could-go-wrong/treacherous-turn`,
`when-ai-breaks/workday-hiring-screening`. None overlaps PPO's subject; no
coordination needed beyond not cross-citing tonight's unpublished pieces.

## Prior coverage to stay off
`instructgpt`, `direct-preference-optimization`, `deep-rl-from-human-preferences`,
`deepseek-r1` are published and adjacent. This lesson is about the PPO paper, not
the RLHF pipeline. Link, do not re-explain, human-preference reward models and
the RLHF loop.

## Recent habits not to inherit (from the last week of The Evidence)
- Dek mold to avoid: "The <year> <org> paper that <did X> reported <limitation>
  only <where>." It has run on lora, seq2seq, clip, and rag. Write a different
  dek shape.
- Recent evidence lessons end on a "how it's used today" section titled for the
  present tense ("Now almost every fine-tune is a LoRA", "Today's RAG pipelines
  ..."). The present-day turn is required content here, but do not title it to
  that mold.
- nb-note and a single nb-table are the reflex furniture on this desk. Use
  furniture only where the clip-objective math or the benchmark-scope comparison
  actually needs it; an equation (nb-math) may serve the surrogate objective
  better than prose.
