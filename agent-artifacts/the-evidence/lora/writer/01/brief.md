# writer brief: the-evidence/lora (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, series prompt
- ../../commission.md — the angle, boundaries, source policy, and the recent habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/01/evidence.md — the complete set of claims available to you; use its Numbers section exactly
- article to edit: /home/user/the-nightly-build/.nb-work/the-evidence/lora/library/the-evidence/lora.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/lora/.nb-context

Output: draft-handoff.md (this directory)

Proof: ./nb check /home/user/the-nightly-build/.nb-work/the-evidence/lora/library/the-evidence/lora.html --series the-evidence --library /home/user/library-checkout

This round's focus: the honest tension is the whole lesson. "Matches full
fine-tuning" is a bounded result on the paper's own models and tasks; the
Biderman et al. (2024) study in the record shows LoRA trailing full fine-tuning
on harder domains (code, math). Present the parity claim with its scope, not as
a law. Two record cautions to respect: do not cite the uncited "97-99% of full
fine-tuning on GLUE" figure or the Gartner "85% by 2027" forecast (both
discarded, no openable primary), and do not call the 2024 study a TMLR paper
unless you confirm the venue against OpenReview; cite it by its arXiv page
otherwise. Neighbors to link in Background, not re-teach: parameter-count,
gradient-descent.
