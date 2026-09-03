# Commission: the-instruments/task-time-horizon

## Assignment
Teach how one public number for comparing AI systems is made: METR's "task time
horizon" — the length of task (measured in how long it takes a human) that an AI
completes at a 50% success rate, and the finding that this horizon has been
doubling roughly every seven months. Primary document: Kwa et al. 2025,
"Measuring AI Ability to Complete Long Tasks" (METR). Template: lesson,
1200–2200 words, 0–4 flex sections.

## Why this number, now
This is the number behind a wave of AGI-timeline claims: "AI can now do tasks that
take humans an hour, and the length is doubling twice a year." It looks like a
clean measure of capability. This desk shows exactly how it is constructed and
what it can and cannot support.

## The number, in brief (researcher verifies every figure)
- Production, step by step: assemble a suite of tasks; measure how long each takes
  a skilled human (the "human time" x-axis); run models on the tasks and score
  success; fit a curve (logistic) of success vs human-time; read off the human-
  time length at which the model succeeds 50% of the time. That length is the
  horizon. The doubling trend is a regression across model release dates.
- The exact figures: the current horizon(s) reported, the doubling period (~7
  months, with the reported range), the task suite(s) used, and how many tasks /
  what domains. Give the real numbers.
- What it can support: relative progress on this suite at a 50% bar.
- What it cannot support: reliability (50% is a coin flip, not "can do"), real-
  world tasks outside the suite, and the straight-line extrapolation to
  multi-day/month tasks. Document METR's own stated caveats.
- The case where it misled, concrete: the public leap from "50% time horizon of ~X
  hours" to "AI can now reliably do X-hour jobs" or to a dated AGI forecast. Show
  the gap between the 50% construction and how the number gets quoted.

## Required contribution
The reader can explain that the horizon is a 50%-success human-time length fit to
a specific task suite, name what it cannot support (reliability, off-suite tasks,
the extrapolation), and recognize how the doubling headline outruns the number.

## Source obligations
Minimum 8 sources, primary >= 4, secondary >= 1. Primary: the METR paper and
METR's own writeups/task suite docs; any primary critique or replication; a
primary source for a specific misquotation/forecast. Reporting is secondary.

## Do NOT repeat published coverage (the-instruments)
Already published (do not repeat slug or topic): swe-bench, tau-bench, arc-agi,
gpqa, humanitys-last-exam, frontiermath, mmlu, mmlu-pro, needle-in-a-haystack,
context-window, humaneval-pass-at-k, chatbot-arena-elo, aime, and others. METR's
time-horizon is a meta-metric about task length, distinct from any single task
benchmark — keep it there. If SWE-bench or an agentic benchmark comes up, link,
do not re-teach it.

## This edition's neighbors (avoid overlap)
Siblings tonight: the-evidence/mixture-of-experts, the-mechanics/option-order-bias,
what-could-go-wrong/algorithmic-collusion, when-ai-breaks/clearview-ai. No topical
overlap; keep this on how the horizon number is built and misread.

## Production policy (balanced; none required)
writing-coach low, researcher high, writer medium, editor high — capable model,
this session's configured capable model. No required directive.

## Recent shapes to break
See the writer brief's shared note.
