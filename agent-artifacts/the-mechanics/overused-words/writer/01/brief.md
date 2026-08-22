# writer brief: the-mechanics/overused-words (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the causal chain to teach, settled-vs-open marking, and boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/01/evidence.md — the complete, verified claim set; treat as the only claims available
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-mechanics/overused-words/library/the-mechanics/overused-words.html
- Effective template contract and furniture catalogs: /home/user/the-nightly-build/.nb-work/the-mechanics/overused-words/.nb-context/

Output: ./draft-handoff.md (beside this brief)

Proof (run from /home/user/the-nightly-build): iterate with
`./nb check .nb-work/the-mechanics/overused-words/library/the-mechanics/overused-words.html --series the-mechanics --library /home/user/library-checkout --no-check-links`
then run the same WITH links until `BLOCK: 0`. Run `./nb stamp .nb-work/the-mechanics/overused-words/library/the-mechanics/overused-words.html` before the final check.

This round's focus and decisions the inputs do not settle:
- Hold the settled/open seam the evidence draws, and do not blur it. SETTLED: post-training with RLHF measurably narrows the output distribution and cuts diversity (Kirk et al., direct base/SFT/RLHF comparison). OPEN: why *these specific* words. The honest finding the lesson lands is that the specific-word origin is unknown, and the popular "annotator dialect / delve" explanation FAILED its one direct empirical test (Juzek & Ward's ICE-corpus analysis did not support it; their surprisal test was only weakly consistent with RLHF). Present the annotator hypothesis at its real, weak strength — not as the answer, and not as merely "unconfirmed."
- Numbers: the Kobak prevalence figure moved between versions (preprint ~10% / up to ~30%; Science Advances ~13.5% / up to ~40%). Cite one version and call it a moving lower bound. The evidence flags a few figures verified only at abstract level (InstructGPT alignment-tax wording; Sadasivan's watermark drop 99.3%→9.7%; the per-word Kobak ratios from Fig. 2) — do not print those exact numbers unless the evidence record's own text supports them; when in doubt, state the qualitative claim.
- The detection consequence is population-level and correlational: the word-frequency signal cannot license a per-document "this was AI" verdict, and human writing now carries the same words. Make that limit explicit.
- Link, do not re-teach: next-token generation and the sampler (the-mechanics/autoregressive-generation and the-mechanics/sampling-temperature — the proximate cause), formatting-defaults (REQUIRED Background link; shared post-training root cause — extend past it into lexical distribution-narrowing), and RLHF (the-evidence/instructgpt). Plain prose links at first use, never numbered sources.
- No code (series rule). Mark which steps are settled engineering and which are open, but do not use a stock "What's settled / What's open" scaffold heading — work it into the argument's own headings.
- Break neighbor dek molds: recent Mechanics deks pair behavior+mechanism with a number. Lead your dek with a concrete measured fact about the words; do not copy a neighbor's construction. Vary the orientation heading.
- Do NOT let the piece become a showcase of the overused words it describes. Naming them is required; performing them is the failure.
- Furniture: a table of the most over-represented words with their measured frequency shift can genuinely help IF the evidence supports the exact figures; otherwise keep it qualitative. Don't stack furniture.
- Write the original-work sentence in draft-handoff.md.
