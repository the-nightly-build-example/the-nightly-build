# Commission: the-instruments/gaia

## The measurement

The GAIA score: the number a system reports for the GAIA benchmark ("GAIA: A
Benchmark for General AI Assistants," Mialon, Fourrier, Swift, Wolf, LeCun,
Scialom et al., 2023; arXiv:2311.12983), and the Hugging Face GAIA leaderboard
that ranks assistants on it. One lesson, one number.

## Why this closes a gap tonight

The Instruments has taught agent-flavored numbers one domain at a time:
task-time-horizon (METR's timed software tasks), swe-bench (repository bug fixes),
tau-bench (tool use in retail/airline scripts). GAIA is the number people reach
for when they claim an assistant is good at *general* real-world tasks, and it is
the one behind "AI assistants now beat humans" headlines. The reader can compare
benchmarks properly only once they have seen how a general-assistant score is
built and where it breaks.

## What the lesson must do

Explain, step by step, where a GAIA number comes from: who produces it (the
authoring team and who runs the public leaderboard), from what data (how many
questions, the three difficulty levels, the kinds of task: multi-step reasoning,
web browsing, file and multimodal handling), and by what procedure (the
quasi-exact-match grading against a single reference answer, the design goal that
questions be easy for humans and hard for machines, the human-vs-model baseline
numbers at release). Give the figures honestly: question count, the reported human
score, the release-time model scores, and the validation/test split.

Then show what the number can and cannot support, with at least one real case
where a GAIA figure misled people and what that cost. Candidate cases for the
researcher to verify and choose among: leaderboard submissions tuned to the public
validation set so a headline score did not transfer; the exact-match grader
marking a correct answer wrong (or right) on formatting; a "human-level" or
"state-of-the-art on GAIA" marketing claim that a scanning reader took as
general competence. Pick the best-documented one and state the concrete cost.

The earned analysis: name exactly what a high GAIA score does and does not license
the reader to believe about an assistant. Ground every claim in the cited number.

## Distinctness and continuity

Not a published slug in the-instruments. Link, do not re-teach:

- `../the-instruments/swe-bench.html`, `../the-instruments/tau-bench.html`,
  `../the-instruments/task-time-horizon.html` — neighboring agent metrics.
  Differentiate GAIA from each (general assistant tasks, not software repos, not a
  single tool-use script, not a time horizon); link rather than compare at length.
- `../the-instruments/humaneval-pass-at-k.html`, `../the-instruments/math-benchmark.html`,
  `../the-instruments/livecodebench.html` — contamination and grading were taught
  there; if GAIA's misleading case is contamination/overfitting, link the prior
  treatment and keep this lesson on GAIA's own mechanics.
- `../the-mechanics/tool-use.html` and `../the-mechanics/retrieval.html` — assume or
  link; do not re-teach how tool use or retrieval work.

## Sources (floor: min 8; primary >=4; secondary >=1)

Primary must include the GAIA paper (read the dataset construction, scoring, and
baseline sections in full) and the Hugging Face GAIA dataset/leaderboard pages
(read the scoring rules and current standings). Add the primary report or system
card behind the misleading case (the agent/system that reported the score in
question) and, if used, the paper or post documenting the overfitting/grading
problem. Secondary reporting for reception and for the headline claim. Verify the
human score, the model scores, and the question counts against the paper, not
coverage.

## Production policy (balanced; nothing marked required)

writing-coach low, researcher high, writer medium, editor high; model "capable".
No required directive; each role records the actual model and effort used.

## Tags

Open section. Suggested: benchmarks, ai-agents, gaia, leaderboard, evaluation.
Writer owns the final list.

## Recent-pattern notes (habits not to inherit)

- The recent-run dek mold is a concrete clause + comma + "and"/"while"/"or" twist
  (task-time-horizon, MFU, SimpleQA, LiveCodeBench). Vary the dek's build.
- Instruments headlines often lead with a single striking number ("A different
  attack turns 1% into 88%"). Strong, but now frequent; earn a number-forward
  headline or choose another shape.
- Headings are full argument-step sentences in the piece's own nouns. Keep the
  form; do not copy a prior lesson's rhythm.

## Neighboring articles in tonight's run

the-evidence/palm, the-mechanics/lost-in-the-middle, what-could-go-wrong/
ai-enabled-coup, when-ai-breaks/deloitte-ai-report. No topic overlap.
