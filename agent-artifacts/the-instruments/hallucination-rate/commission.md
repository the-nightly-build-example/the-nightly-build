# Commission: the-instruments/hallucination-rate

## Assignment
Teach how a published "hallucination rate" is made: the single percentage
("model X hallucinates 1.3% of the time") that gets quoted as if it measured
how often a chatbot is wrong. Explain, step by step, who produces the number,
from what data, by what procedure (a leaderboard like Vectara's HHEM scores
faithfulness on a narrow document-summarization task with an automated judge
model, not general truthfulness), then show what the number can and cannot
support, with at least one real case where reading it as "how often the model
lies" misled people and what that cost.

## Why this measurement, now
"Hallucination rate" is quoted constantly in AI-buying and policy conversations
as a reliability score, and almost nobody who cites it knows it usually measures
summary faithfulness on one dataset, judged by another model. The gap between
what the number measures and what people take it to mean is the desk's exact
territory.

## Angle boundaries
- The subject is the **measurement**, not hallucination the behavior. The
  the-mechanics/hallucination lesson already explains WHY models fabricate;
  reference it, do not re-teach the mechanism. This lesson owns how the RATE is
  constructed and what load it can bear.
- Distinct from the-instruments/llm-as-a-judge (which owns the position-bias
  problem of using an LLM as a judge). Here the judge model is one step in a
  larger pipeline; note the automated-judge dependency and link llm-as-a-judge
  rather than re-deriving its findings.
- Pin the pipeline to a real, citable instrument: Vectara's HHEM Hallucination
  Leaderboard is the strongest primary anchor (its method, the dataset it
  summarizes, the classifier that scores faithfulness, the exact rates it
  publishes). Use other named hallucination benchmarks (e.g. FaithBench,
  TruthfulQA as a contrast of a different thing) to show the number is not one
  agreed quantity.
- The "misled" case must be documented: e.g. a very low leaderboard rate cited
  as general reliability, or a model topping the faithfulness board while still
  fabricating citations in open use. Source it.

## Required contribution
The reader should be able to explain where a hallucination-rate number comes
from, name at least two things it cannot support (general factual accuracy;
behavior outside the summarization task; comparability across benchmarks that
define hallucination differently), and cite one concrete instance where reading
it as objective reliability cost someone something.

## This edition (neighbors — keep distinct)
- the-evidence/resnet — a landmark paper as a document
- the-mechanics/thinking-out-loud — why writing steps improves answers
- what-could-go-wrong/sharp-left-turn — a capability jump outrunning safety
- when-ai-breaks/apple-card — algorithmic credit-limit bias

## Template & policy
- Template: lesson.
- Source policy: min 8 sources; >=4 primary, >=1 secondary. Primary: the
  leaderboard's own method write-up and published rates, the benchmark/dataset
  papers, the judge-model paper, and any study auditing these rates. Secondary:
  reporting that held up.
- Production policy (balanced): coach low, researcher high, writer medium,
  editor high; model "capable"; none required.
- Actual harness/model: `claude-code-routine`, `claude-opus-4-8` for all roles.
  Record in nb-meta (date 2026-08-07).

## Habits not to inherit (for the writer brief)
The-instruments headlines almost all put two conflicting numbers side by side
("X and Y are both true", "0.3 by one measure and 2.9 by another") and lean on
a table of stacked choices. That paired-number reflex now stamps the series —
do not inherit it. Find this instrument's own opener and dek. Check the recent
library's deks and headings first.
