# Commission: the-instruments/rewardbench

## The measurement

RewardBench (Lambert et al. 2024, AI2), the standard test for reward models —
the classifiers that score which of two answers is better and that drive
preference-based post-training. The lesson teaches how the score is produced
and where the score can and cannot be trusted as a signal about the models that
depend on it.

## The angle

Explain the production of the number step by step: the benchmark holds a fixed
set of chosen-versus-rejected answer pairs across a few categories (chat, chat
hard, safety, reasoning); a reward model reads each pair and is scored on how
often it prefers the chosen answer; the reported number is that accuracy,
aggregated with a stated per-category weighting. Then draw the line the desk
requires: the benchmark measures agreement with a fixed preference labeling; it
does not measure how good the answers are for real users, and a reward model
that tops the leaderboard is not by that fact a reward model that yields a
better chatbot.

The misled-people case is the concrete one: reward models sitting near the top
of RewardBench have shown limits in downstream use, and the benchmark's own
authors and follow-up work have documented ways the score can be gamed or
misread. Report what the primaries actually show — the recent RewardBench 2
release that widened the tests after saturation, published preference-model
sycophancy findings, and the length/formatting bias analyses.

## Teach, in this order

1. What a reward model is and where it sits in the post-training pipeline: the
   piece the rest depends on. Keep it short and link earlier lessons for the
   RLHF machinery rather than re-teaching it.
2. How the number is made: the fixed chosen-vs-rejected pairs, the per-category
   split, the aggregation, and the leaderboard update rule. Give the counts of
   pairs and categories, not magnitudes.
3. What the number supports and what it does not: agreement with a fixed
   labeling versus downstream chatbot quality; documented gaming and biases;
   what RewardBench 2 changed after saturation.

## Sources

Series policy requires at least eight sources, at least four primary and at
least one secondary. The RewardBench paper is the anchor primary. RewardBench 2
(Malik et al. 2025) or the AI2 follow-up documenting saturation is a primary
for the "what changed" section. The Sharma et al. sycophancy study is a
primary for the preference-model preference for agreement. A published
length-bias or formatting-bias study on reward models is a primary for that
line. The researcher resolves the exact set; the commission's four-primary
minimum is a floor, not a ceiling.

## Boundaries and neighbors

The 2026-08-24 edition runs this alongside the-evidence/retrieval-augmented-
generation, the-mechanics/first-token-latency, what-could-go-wrong/algorithmic-
monoculture, and when-ai-breaks/nyc-mycity-chatbot. No topic overlap with those.

Within the-instruments, chatbot-arena-elo (human preference at chat level),
llm-as-a-judge (LLMs grading other LLMs), and alpacaeval (a static preference
benchmark) already teach neighboring instruments. This lesson stays on the
reward-model layer specifically — what a reward model is, and what its
leaderboard score does and doesn't tell you about the chatbot trained against
it — and links those earlier pieces in Background for shared machinery.

## Production record

Template: lesson. Series: the-instruments (open section, self-chosen topic).
Production policy resolved to the balanced profile: writing-coach effort low,
researcher effort high, writer effort medium, editor effort high, model
"capable" for every role. Roles run as delegated agents on the shared checkout;
each invocation records the actual model and effort used. No `required`
directive applies.
