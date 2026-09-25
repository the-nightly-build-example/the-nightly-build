# writer brief: the-evidence/elmo (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md),
voice-guide.md (../../writing-coach/01/voice-guide.md), evidence.md (../../researcher/01/evidence.md).
Article + context under .nb-work/the-evidence/elmo/ (HTML at
library/the-evidence/elmo.html; .nb-context/ has furniture + contract).
Output: ./draft-handoff.md (+ edited article HTML)
Proof:  ./nb check .nb-work/the-evidence/elmo/library/the-evidence/elmo.html --series the-evidence --repo $(pwd)

Work from these inputs only; ask me where something is missing.

Focus: teach the four ideas in commission.md in order. Spine: fixed vectors give
one meaning per word -> ELMo made the representation depend on the sentence via a
biLSTM language model -> it lifted six tasks at once, added on top of existing
models -> BERT's fine-tuning recipe displaced ELMo's mechanism within a year
while the idea became universal. Original-work sentence in draft-handoff.md:
separate the idea ELMo is credited with (contextual representations from an LM)
from the machinery it shipped (a frozen biLSTM feeding features); the field kept
the first and dropped the second. Link word2vec, LSTM, and BERT at first use;
do not re-teach them.

Recent-pattern notes to break (the-evidence): do NOT close on a "the famous X was
not the real X" reveal section; build the idea/machinery split into the spine.
Headings distinct from each other and from "What X actually claimed"/"How small
the demonstrations were." Dek: one lean sentence, one concrete detail; no
comma-triad or "and" continuation mold.

Furniture: a table of the six tasks (metric, prior SOTA, ELMo, error reduction)
carries the results; a source asset of ELMo's results table is legitimate if you
use what it shows. Numbers from evidence Numbers exactly. nb-meta: date
2026-09-25, harness+model "Claude Opus 4.8", 4-5 concrete tags, dek identical to
rendered dekline. nb stamp, then proof to BLOCK: 0.
