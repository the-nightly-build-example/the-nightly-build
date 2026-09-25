# researcher brief: the-evidence/elmo (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md)
Output: ./evidence.md

Work from these inputs. Do not tour the repository. Ask me where something is missing.

Read the primary documents in full, with locators:
- ELMo: Peters et al., "Deep contextualized word representations" (NAACL 2018,
  arXiv:1802.05365). Record: the biLSTM-LM architecture (two layers, character
  CNN input, forward+backward LMs), that representations are a task-specific
  weighted combination of layers, and the exact six tasks and their result
  numbers from Table 1 (SQuAD, SNLI, SRL, coref, NER, SST-5) — the metric, the
  previous SOTA, ELMo's number, and the relative error reduction the paper
  states. Record the training corpus (1B Word Benchmark) and model size if given.
  Quote the paper's own sentence on why context-dependent representations help.
- BERT: Devlin et al. (arXiv:1810.04805). Record how it distinguishes
  "feature-based" (ELMo) from "fine-tuning" (BERT) approaches, and any direct
  comparison/claim over ELMo. Quote the sentence positioning BERT against ELMo.
- If a specific dataset number needs its owner (e.g. SQuAD 1.1), open that paper.

Establish the idea-vs-machinery split: the contextual-representation idea vs the
frozen-biLSTM-features mechanism, and that fine-tuning Transformers displaced the
mechanism quickly. Record the "ImageNet moment for NLP" framing only if you find
a datable, attributable source for it (name who said it); otherwise flag it.

Source floor: min 6, >=3 primary, >=1 secondary. Classify each with a reason.
Contradictions: record any claim that ELMo remained competitive, or disputes
about credit (ULMFiT, CoVe as prior contextual work). Numbers: the six-task
figures with owner and scope. Source assets: ELMo's Table 1, or its Figure of
layer weightings, are candidates. Limits: note anything you could not verify.

Report the path and the most important limit.
