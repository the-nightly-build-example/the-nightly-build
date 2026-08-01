# Commission — the-evidence/gpt-4-technical-report

## Assignment
Teach what the GPT-4 Technical Report (OpenAI, March 2023, arXiv:2303.08774)
actually is and actually says. It is the document the world cites when it says
"GPT-4 scored in the 90th percentile on the bar exam" or "GPT-4 is far more
capable than GPT-3.5." Read the document itself. The lesson: this famous
"technical report" is a capabilities-and-safety report that, by its own
statement, discloses nothing about how the model was built.

## Angle
The report's own words draw the line. Show the reader (1) what it does report:
a battery of exam and benchmark scores, and safety/red-team process; and (2)
what it explicitly declines to report and why. Quote the report's own sentence
that it contains "no further details about the architecture (including model
size), hardware, training compute, dataset construction, training method, or
similar." Then show one concrete consequence: a headline number people quote
from it that the report itself hedges or that later work reads differently
(the "90th percentile" bar-exam figure is the cleanest case; the paper cites it
but the percentile was later recomputed against attorneys who passed, landing
far lower — this paper already taught that in the-instruments/bar-exam-percentile,
so link that lesson rather than re-deriving it). Do not turn this into a bar-exam
lesson; the subject is the report and what a reader can and cannot learn from it.

Land the judgment: a document that withholds method is evidence about capability
claims and safety process, not a paper anyone can reproduce or check. Citing it
as if it were a normal scientific paper imports a rigor it does not offer.

## Intended reader
The house reader: smart, widely read, no codebase time. Assume they have heard
"GPT-4" cited to settle arguments and have never opened the document.

## Required contribution
The reader leaves able to say what the GPT-4 Technical Report contains, what it
withholds, and therefore what kind of citation it can and cannot support. This
is a lesson about reading a document honestly, not about GPT-4's intelligence.

## Source obligations (the-evidence: min 6 sources; primary >=3, secondary >=1)
- PRIMARY, required: the GPT-4 Technical Report itself (arXiv:2303.08774 / OpenAI
  site). Read the abstract's disclosure disclaimer, the exams table (Table 1 /
  Appendix A), the contamination discussion, and the System Card sections.
- PRIMARY: the GPT-4 System Card (bundled with the report) for red-team/safety
  process claims.
- PRIMARY candidates: the OpenAI "GPT-4" launch page; the bar-exam study by
  Katz et al. (the source of the 90th-percentile claim) as the owning primary of
  that number; Martínez 2024 "Re-evaluating GPT-4's bar exam performance"
  (primary re-analysis) for the corrected percentile.
- SECONDARY: reputable coverage that noted the report disclosed no architecture
  (e.g., The Verge, Nature news, or similar) — for context only.
- Seek contradictory evidence: did OpenAI justify the non-disclosure (competitive
  landscape + safety)? Quote their stated reason, do not paraphrase it into a
  motive. Note any figure in the report that IS well-supported so the lesson is
  fair, not a hit piece.

## Starting sources
arXiv:2303.08774 (abstract + Appendix); OpenAI GPT-4 System Card; Martínez,
"Re-evaluating GPT-4's bar exam performance" (Artificial Intelligence and Law,
2024). Researcher verifies all and finds the rest.

## Relevant prior coverage (link, do not re-teach)
- the-evidence/sparks-of-agi — Microsoft's separate GPT-4 probing study on an
  unreleased model. Distinct document. A natural Background link; note the
  contrast (one is the vendor's official report, the other outside probing).
- the-instruments/bar-exam-percentile — already dismantled the 90th-percentile
  number. Link it; spend one sentence, do not rebuild it.
- the-instruments/mmlu — the report ships an MMLU score without method. Optional link.

## Structures NOT to repeat (recent habits)
- No "three scenarios" cold open. No colon-subtitle headline. No "X is not Y;
  it is Z" dek. No retired Verdict block. Do not open by narrating the document's
  fame in generic terms; open on the specific gap between what it claims and what
  it shows.

## Neighboring articles tonight (keep distinct)
Tonight also runs: tokens-per-second (a speed number), tool-use (mechanics),
jailbreaks (a risk argument), google-flu-trends (a failed prediction). This is
the only piece about disclosure/transparency of a document. Stay in that lane.

## Template / mode / paths
- template: lesson; mode: open; order: null; date: 2026-08-01 (UTC).
- article: .nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html
- artifacts under agent-artifacts/the-evidence/gpt-4-technical-report/

## Harness / model (resolved from production-policy: balanced)
- writer: harness claude-code-routine, model claude-sonnet-5, effort medium.
- researcher effort high; editor effort high; writing-coach effort low; all model
  claude-sonnet-5. Record harness=claude-code-routine, model=claude-sonnet-5 in nb-meta.

## Tags (nb-meta)
Suggest: ["gpt-4", "transparency", "benchmarks", "openai"]. Writer sets final.
