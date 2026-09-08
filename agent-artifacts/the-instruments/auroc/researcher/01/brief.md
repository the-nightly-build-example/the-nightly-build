# researcher brief: the-instruments/auroc (01)

Inputs:
- editorial-direction.md (artifact root) — citation standard, series territory, declared reader.
- commission.md (artifact root) — the measurement, the angle, what to teach, the source floor.

Output: researcher/01/evidence.md

Research questions, answered from the primary source that owns each claim:

1. The definition and interpretation of AUROC: the ROC curve (sensitivity vs
   false-positive rate across thresholds) and the theorem that its area equals the
   probability a random positive is ranked above a random negative. Pin to a
   methodological primary (e.g., Hanley & McNeil 1982; and a source stating the
   ranking-probability / Mann-Whitney equivalence). Get sensitivity, specificity,
   PPV/precision definitions from a solid primary.
2. What AUROC is blind to: calibration (that it is threshold- and
   calibration-independent) and the operating threshold. Find a primary making
   this explicit.
3. Class imbalance: why ROC/AUROC can look strong under rare positives while
   precision/PPV is poor; the precision-recall-vs-ROC argument. Pin to Saito &
   Rehmsmeier 2015 (PLOS ONE) and/or Davis & Goadrich 2006.
4. The Epic Sepsis Model case, exact figures: Wong et al., 2021, JAMA Internal
   Medicine, "External Validation of a Widely Implemented Proprietary Sepsis
   Prediction Model in Hospitalized Patients." Get the externally measured AUROC,
   the vendor-reported AUROC range Epic claimed, the alert threshold studied, the
   sensitivity at that threshold (the missed-case fraction), the false-alarm /
   alert burden, and the cohort size and period. Also find Epic's own model
   documentation figure for the claimed AUC if reachable, and any Epic response.
5. Contradictions and limits: cases where AUROC is the right summary, and any
   dispute over the Wong et al. numbers or Epic's subsequent model changes.

For a possible ROC chart: if a cited primary provides a usable ROC series or the
sensitivity/specificity points to reconstruct one honestly, record it under
Numbers with full series and source. Otherwise say no verified series supports a
chart. Classify every source primary/secondary with the reason and meet the floor
in commission.md.
