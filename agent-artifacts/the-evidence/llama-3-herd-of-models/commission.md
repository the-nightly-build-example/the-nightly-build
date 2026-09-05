# Commission: the-evidence/llama-3-herd-of-models

## Assignment
Teach the reader what the Llama 3 technical report, "The Llama 3 Herd of
Models" (Meta, published July 2024 on arXiv), actually says. The desk reads a
famous document so the reader knows what is in it. This one is the document
people point to when they argue about how far open-weight models trail the
closed frontier, how much a language model costs to train, and what "open" now
means for a model anyone can download.

State what the report is, who wrote it, and why it gets cited. Then walk what
Meta actually did: the model sizes it released (8B, 70B, 405B), the training
data scale, the compute it spent on the 405B, and the benchmark numbers it
reported against GPT-4, GPT-4o, and Claude 3.5 Sonnet. Show the scale honestly:
a report is a self-report, and the headline is a company measuring its own model
on evaluations it selected. Bring it to the present: how the numbers get used in
the open-vs-closed argument, whether the report's claims held as later models
shipped, and what "open weights" does and does not give the reader who downloads
the file (weights and a license with use restrictions, not training data or
training code).

## Angle
The report is evidence a company produced about its own product. The lesson's
job is to separate what Meta measured and disclosed (architecture, data volume,
compute, a large public benchmark table) from what a reader cannot verify from
the document (the training data itself, contamination controls, and any
comparison Meta chose not to run). Teach the reader to read a frontier-model
technical report as both an unusually detailed engineering record and a
positioning document, and to tell which parts are which.

## Template and form
Lesson template. Body first, then both bookends. 1200–2200 words. Flexible
sections named for this document, not stock labels.

## Sources
Series floor is 6 sources, at least 3 primary and at least 1 secondary. The
report itself (arXiv/Meta) is the central primary; the model card and license on
Meta's site are further primaries for what "open" means here. Secondary: at
least one independent outlet or benchmark maintainer for how the numbers were
received or contested (e.g. reporting on the release, an independent leaderboard,
or a contamination/benchmark-validity source). Verify every figure against the
report, not coverage of it. Contested numbers need the primary.

## Tags
Open item, no commissioned tag fragments. Leave `tags` for the writer to set
from the article's own subject.

## Production policy (balanced profile)
- researcher: model capable, effort high
- writer: model capable, effort medium
- editor: model capable, effort high
- writing-coach: model capable, effort low
None are `required`, so no directive is being traded down. Actual harness for
every role this run: Claude Code Task subagent, model `claude-opus-4-8`. The
writer records `harness` and `model` in `nb-meta`.

## This run's neighbors (keep every piece distinct)
Four other lessons publish alongside this one:
- the-instruments/livecodebench (a coding benchmark and contamination)
- the-mechanics/clock-faces (image models defaulting clocks to ~10:10)
- what-could-go-wrong/automation-bias (over-reliance on automated judgment)
- when-ai-breaks/grok-antisemitic-outputs (a deployed chatbot's July 2025 failure)
livecodebench also touches benchmark contamination; keep this lesson's treatment
of Meta's benchmark table about self-reporting and selection, and leave
contamination-as-a-measurement-problem to that piece. Do not cover the same
ground twice.

## Do not repeat (recent the-evidence coverage)
Recent lessons and their shapes to avoid inheriting:
- deep-double-descent (2026-09-04): closing section "How much of this survived"
  with an nb-holdsup block. Do not clone that heading or that "does it still
  hold" closer construction.
- mixture-of-experts (2026-09-03), constitutional-ai, segment-anything,
  adversarial-examples. mixture-of-experts already covered sparse routing and
  the 47B/13B Mixtral figure; if MoE comes up for Llama 3's dense design,
  contrast in a clause and link, do not re-teach it.
Published slugs must not repeat; `llama-3-herd-of-models` is new.

## Required contribution
By the end the reader can say what the Llama 3 report measured, at what scale,
and can separate its disclosed engineering from its selected framing, so they
can read the next model report the same way.
