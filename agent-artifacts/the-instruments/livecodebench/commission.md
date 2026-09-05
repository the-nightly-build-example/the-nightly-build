# Commission: the-instruments/livecodebench

## Assignment
Teach the reader where a LiveCodeBench score comes from and what it can and
cannot support. The desk explains how a number used to compare AI systems is
made. LiveCodeBench is the coding benchmark that model makers now cite in launch
posts and model cards, built expressly to fight the problem that older code
benchmarks got memorized. Explain, step by step: who produces the number (the
academic team behind LiveCodeBench), from what data (programming-contest problems
collected from sites like LeetCode, AtCoder, and Codeforces), and by what
procedure (problems tagged with release dates so a model is scored only on
problems published after its training cutoff; pass@1 over held-out tests; several
scenarios beyond plain code generation).

Then show what the number can and cannot support, and give at least one real case
where a coding-benchmark number misled people and what that cost. The natural
case is the one LiveCodeBench was built to answer: contamination and saturation
of HumanEval and similar sets, where models scored high partly because the test
questions were in their training data. If the researcher finds a cleaner, better
documented case (a model's LiveCodeBench figure that used a favorable date window,
or a cross-version comparison that was not apples to apples), use that.

## Angle
The defense against contamination is a moving cutoff date, and that same moving
cutoff is what makes two LiveCodeBench numbers hard to compare: a score is only
meaningful paired with the date window and version it was measured on. Teach the
reader to ask, of any LiveCodeBench figure, which problems and which dates it
covers before trusting a comparison built on it.

## Template and form
Lesson template. Body first, then both bookends. 1200–2200 words. Sections named
for this measurement, not stock labels.

## Sources
Series floor is 8 sources, at least 4 primary and at least 1 secondary. Central
primary is the LiveCodeBench paper and its official leaderboard/site; further
primaries include the source contest sites' problem records where a specific
example is used, and any model card or launch post that reports a LiveCodeBench
number (a primary for the claim that the number was reported that way).
Secondary: independent analysis of benchmark contamination or of LiveCodeBench's
methodology. Verify every figure against the primary that owns it.

## Tags
Open item, no commissioned tag fragments. Writer sets `tags` from the subject.

## Production policy (balanced profile)
- researcher: capable / high; writer: capable / medium; editor: capable / high;
  writing-coach: capable / low. None `required`. Actual harness: Claude Code Task
  subagent, model `claude-opus-4-8`.

## This run's neighbors (keep distinct)
Publishing alongside: the-evidence/llama-3-herd-of-models (which also touches a
self-reported benchmark table), plus clock-faces, automation-bias,
grok-antisemitic-outputs. Keep contamination-as-a-measurement-problem here; the
Llama 3 lesson handles a company self-reporting a selected table. This lesson
owns the mechanics of how a contamination-resistant score is built and where it
still misleads.

## Do not repeat (recent the-instruments coverage)
- attack-success-rate (2026-09-04): shape "The number that said X" then "Four
  choices behind the percentage" then "Whoever grades decides the score" then
  "What the 100 percent actually counted." Do not clone that heading sequence or
  the "N choices behind the number" / "what the N actually counted"
  constructions.
- task-time-horizon, superglue, imo-gold, toxicity-score, simpleqa are recent.
  simpleqa already taught that a headline share was a benchmark artifact, and
  superglue already taught benchmark saturation against a human baseline; do not
  re-run those exact points. Coding benchmarks humaneval-pass-at-k, swe-bench,
  and codeforces-rating are already published; link rather than re-teach, and
  make clear how LiveCodeBench differs from each.

## Required contribution
By the end the reader can read a LiveCodeBench figure and know to check its date
window and version before comparing models on it, and can explain why a moving
cutoff both fixes contamination and complicates comparison.
