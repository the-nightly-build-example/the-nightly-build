# Commission: the-instruments/tau-bench

## The measurement

τ-bench (tau-bench), the score now quoted when a company says its AI "agent" can
handle real tasks: Yao, Heinecke, and colleagues at Sierra, "τ-bench: A Benchmark
for Tool-Agent-User Interaction in Real-World Domains" (2024, arXiv:2406.12045).
The reader keeps seeing agentic-capability percentages and cannot say what a
τ-bench number counts.

## Angle

Explain where the number comes from, step by step: the benchmark puts a model in a
multi-turn conversation in a domain like retail or airline customer service, gives
it tools (functions it can call against a mock database) and a simulated user
played by another language model, and scores whether the final database state
matches the correct outcome. Then the point this benchmark makes about itself:
its authors report not just how often the agent succeeds once (pass@1) but how
often it succeeds on all of k repeated attempts (pass^k), and that reliability
number collapses far below the headline. That gap is the required real case where
the single number misled: a "58% on τ-bench" that is quoted as competence is a
one-try average for a system a business would run thousands of times a day.

The reader should leave able to ask of any agent score: what state counts as
success, who plays the user, and whether the number is a single run or a
reliability rate.

## What it teaches (short, complete)

1. How a τ-bench score is produced: simulated user, tool calls against a mock
   database, success judged by final state. Walk one task through it.
2. What the number can and cannot support: pass@1 versus pass^k, and why a
   one-try average overstates a system meant to run repeatedly.
3. The misleading case, with figures: the reliability collapse (and any other
   documented τ-bench pitfall, such as simulated-user or verifier limits).

## Boundaries

- One measurement, τ-bench. Do not survey agent benchmarks; mention another only
  as a one-line contrast.
- Claims come from the τ-bench paper (and any follow-up such as τ²-bench) and from
  model reports that state a τ-bench figure, read directly.
- Established course: use `nb history --library` and LINK published neighbors
  rather than re-teach: candidates the-instruments/swe-bench,
  the-instruments/llm-as-a-judge, the-instruments/alpacaeval. The simulated user
  and the model-graded outcome connect to llm-as-a-judge; link it.

## Neighbors in tonight's edition (avoid overlap)

the-evidence/foundation-models, the-mechanics/length-control,
what-could-go-wrong/model-collapse, when-ai-breaks/biden-deepfake-robocall.

## Source policy

Template minimum 8 sources: at least 4 primary, at least 1 secondary. The τ-bench
paper, τ²-bench if used, the leaderboard/repo, and model reports stating a τ-bench
number are primary for what each owns. Reporting is secondary context. A contested
figure needs the primary.

## Production record

Series production policy: balanced profile, model tier `capable` for every stage,
none `required`; efforts writing-coach low, researcher high, writer medium, editor
high. Roles run as isolated subagents on this harness's capable-tier model;
effort set to policy where settable, else harness default. No `required` directive
traded down. In nb-meta set `harness` to `Claude Code` and `model` to `capable`
(production tier; specific model identifier kept out of the published article per
harness policy). The writing-coach guide here was reused from a same-series
sibling lesson; take its craft and register, not its subject.
