# researcher brief: the-instruments/brier-score (01)

Inputs:
- ../../commission.md — the assignment, angle, boundaries, required contribution.
- ../../editorial-direction.md — citation standard, series territory, declared reader.

Output: ./evidence.md

Sourcing floor (nb source-policy): at least 8 sources, at least 4 primary, at
least 1 secondary. Read the primary documents.

Primary documents to read and record with locators:
- Glenn W. Brier, "Verification of Forecasts Expressed in Terms of Probability"
  (Monthly Weather Review, 1950). Verify the original definition and its weather
  origin. Note the historical wrinkle honestly: the original two-category
  formulation vs. the modern (probability − outcome)^2 form commonly called the
  Brier score; state which one the lesson uses.
- A primary that owns the decomposition: Murphy, "A New Vector Partition of the
  Probability Score" (1973), for reliability + resolution + uncertainty. Extract
  only the plain-language meaning of the three terms.
- The AI-forecasting studies whose Brier scores drive the current claim, read
  firsthand: Halawi et al., "Approaching Human-Level Forecasting with Language
  Models" (2024, arXiv:2402.18563) — verify the exact Brier numbers (the LLM
  system's Brier, the human/crowd comparison, the baseline), the question set, and
  the resolution window. Find and read at least one replication or critique of
  such claims and record what it disputes (question-set differences, resolution
  dates, non-replication, or confident wrong calls hidden by a good aggregate).
- A forecasting platform's own methodology that owns a Brier definition/number
  (e.g. Metaculus's or Good Judgment's scoring documentation).
- If used, a source establishing the base-rate baseline (always-predict-0.5 gives
  0.25 on balanced yes/no; and always-base-rate on a rare event) — this can be
  derived, but cite where the argument is made.

Numbers section: the always-0.5 baseline (0.25), a worked tiny example's Brier,
and each cited AI-forecasting Brier with its question set and period, each with
its owning primary and scope.

Contradictions: search hard for the case AGAINST the "LLMs approach human
forecasting" claim (non-replication, incomparable question sets, gaming via
base-rate prediction) AND the strongest case for it. Record both in full.

Source assets: note any figure/table (e.g. a reliability diagram, a Brier-by-model
table from a forecasting study) that could carry the argument. Do not prescribe crops.

Do not browse the repository for background. Confirm every URL resolves. Flag any
commission claim the evidence cannot support.
