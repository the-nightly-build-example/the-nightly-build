# researcher brief: the-instruments/mlperf (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md)
Output: ./evidence.md

Work from these inputs. Do not tour the repository. Ask me where something is missing.

Read the primary documents in full, with locators:
- MLCommons MLPerf Training rules and MLPerf Inference rules (the policy docs
  that define Closed vs Open division, the Available/Preview/RDI availability
  categories, and the inference scenarios: Offline, Server, SingleStream,
  MultiStream). Record the exact definitions and the comparability constraints
  (what may be compared to what). Record the address of the current rules doc.
- The founding papers: Mattson et al., "MLPerf Training Benchmark" (arXiv:
  1910.01500) and Reddi et al., "MLPerf Inference Benchmark" (arXiv:1911.02549).
  Record what a submission measures (time-to-train to a target quality;
  throughput under a scenario), the tasks/models included, and the stated intent
  (fair, comparable, reproducible system comparison).
- A specific MLPerf results table from a named, dated round (e.g. a recent
  Training or Inference round on the MLCommons results site). Record two or three
  concrete numbers with the system (accelerator type and count), division, and
  category, so the writer can show one comparable pair and one non-comparable
  pair.

Establish the misled case: find a documented instance where an MLPerf-derived
"record" or "N times faster" claim compared across non-comparable configurations
(different system scale / division / category), from vendor marketing plus
reputable analysis. Name the vendors, the round, and the numbers. Record the
counter-explanation (what was actually different) and how MLCommons or analysts
framed it.

Source floor: min 8, >=4 primary, >=1 secondary. Classify each with a reason (an
MLCommons rules doc / results table is primary; vendor marketing is primary for
the claim it makes, secondary for whether the comparison is fair; press analysis
is secondary). Contradictions: record disputes over a specific claim in full.
Numbers: times, throughputs, chip counts, with owner, division, category, scope.
Source assets: an MLPerf results table is a candidate; say what a crop must keep.
Limits: note anything you could not verify (e.g. a marketing claim you could not
trace to a submission).

Report the path and the most important limit.
