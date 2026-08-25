# Commission: the-instruments/bfcl

## Assignment
Teach how one measurement is made and where it does not go: the Berkeley
Function-Calling Leaderboard (BFCL), from the Gorilla team at UC Berkeley.
"Function calling" is the number labs cite when they claim a model is good at
using tools and acting as an agent. Explain, step by step, where a BFCL score
comes from: who produces it, from what data (the categories of test cases),
and by what procedure the answer is graded. Then show what the number can and
cannot support, including at least one real case where a high function-calling
score misled people about real-world agent reliability, and what that cost.

## The angle this lesson owns
BFCL grades a single model turn against a known-correct tool call, and it does
it two different ways depending on the category:
- Abstract Syntax Tree (AST) matching: parse the model's proposed call and
  check the function name and argument values against the reference, without
  executing anything.
- Executable evaluation: actually run the proposed call and check the result.
- A relevance/irrelevance category: does the model correctly decline to call a
  function when none fits, or call when one does.
The lesson's job is to make the reader see that a high single-call accuracy is
not multi-step agent reliability. The published `tau-bench` lesson already
taught that eight-in-a-row success collapses a pass@1 score; BFCL mostly
measures the single call, and the multi-turn category BFCL added later is
young and still small. Also teach honestly that BFCL has revised its own test
data across versions (v1 -> v2 "live"/user-contributed -> v3 multi-turn) to
fix label errors and contamination, which is itself evidence about how much a
leaderboard number should be trusted.

## The "misled people" case
Pick the strongest real, sourceable case. Candidates for the researcher to
verify and choose among: a model topping or scoring high on function-calling
while failing real multi-step agent tasks (the τ-bench pass^k collapse is a
documented contrast); BFCL's own documented correction of buggy/mislabeled
categories between versions and what scores that changed; or a documented
instance of a leaderboard-tuned model whose function-calling score did not
carry to production. The case must have a record and a cost (wasted trust,
a wrong model choice, a corrected ranking), not just a general caution.

## Boundaries
- One measurement. Do not turn this into a survey of agent benchmarks.
- Neighbor already published: `the-instruments/tau-bench` and
  `the-mechanics/tool-use`. Link tool-use (how a model "calls" a tool without
  running it) in Background rather than re-teaching it; contrast with τ-bench
  rather than re-explaining it. No neighbor in tonight's edition overlaps.
- Reader is the course reader: smart, widely read, no codebase. Explain AST
  and "executable test" in plain words at first use.

## Required contribution
Hold BFCL's headline (a single function-calling accuracy percentage) against
what an agent actually has to do (chain many calls, recover from errors,
decline when no tool fits), so the reader can see exactly which of those a
BFCL number does and does not measure.

## Sources (researcher obligation)
Floor: at least 8 sources, at least 4 primary and at least 1 secondary.
Primary here: the BFCL leaderboard pages and the Gorilla team's own blog posts
defining each version's dataset and scoring; the released evaluation code /
dataset cards; the τ-bench paper for the reliability contrast; any paper or
release that owns a specific score or a documented correction. Read the
scoring rules from the source that owns them.

## Recent shapes to break (the-instruments)
Verified against recent library structure and prose:
- Recent instrument pieces run: [the claim in circulation] -> [what the score
  literally is] -> [an internals surprise, often with a code snippet] -> [what
  it never measured] -> [the follow-up that found it sorting wrong]. Do not
  copy this by default; let BFCL's own structure decide sections.
- Avoid the takeaway closer mold "A very low score rules X out; a very high one
  does not rule it in" — that exact frame was used recently. Say BFCL's own
  version of the point in the article's own terms.
- Avoid "the number that matters most" and "worth knowing" filler.
- Deks: no comma-triad, no semicolon reversal, no suspended question. Check
  recent deks.

## Production record
Harness: Claude Code subagents, scheduled run. Balanced production policy, no
required directives. Models/effort used:
- writing-coach: Claude Sonnet, low effort
- researcher: Claude Opus, high effort
- writer: Claude Opus, medium effort
- editor: Claude Opus, high effort
