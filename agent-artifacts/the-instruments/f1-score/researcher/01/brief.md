# researcher brief: the-instruments/f1-score (01)

Inputs:
- ../../commission.md
- ../../editorial-direction.md   (citation standard, series territory, reader)

Output: ./evidence.md

Read the measurement's own literature. Establish the definition and history from
primary sources: precision and recall, the harmonic mean, van Rijsbergen's
F-measure (Information Retrieval, 1979) and the Fβ generalization, and a careful
analysis such as Sasaki's "The truth of the F-measure" and Powers' "Evaluation:
from precision, recall and F-measure to ROC, informedness, markedness and
correlation." Record the exact formulas and what each averaging scheme (micro,
macro, weighted) computes for multi-class problems.

For the commission's "misled people" requirement, find the strongest documented
case with primary support. Chicco & Jurman (2020) argue with data that F1 and
accuracy give misleadingly optimistic readings on imbalanced binary data where MCC
does not — pin down their exact experiments and figures. Also search for a
documented instance where a micro-vs-macro F1 choice (or the choice of positive
class) changed which system a benchmark, paper, or shared task ranked first, and
record it with its owner. Verify every formula and figure against the primary.
Record counterpoints (defenses of F1, when it is the right choice) in
Contradictions.
