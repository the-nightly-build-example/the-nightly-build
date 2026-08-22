# writer brief: the-evidence/whisper (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson template, series direction
- ../../commission.md — the angle, the four ideas to teach, and the boundaries
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with verified exemplar passages
- ../../researcher/01/evidence.md — the complete, verified claim set; treat as the only claims available
- The initialized article to edit in place: /home/user/the-nightly-build/.nb-work/the-evidence/whisper/library/the-evidence/whisper.html
- Effective template contract and furniture catalogs: /home/user/the-nightly-build/.nb-work/the-evidence/whisper/.nb-context/

Output: ./draft-handoff.md (beside this brief)

Proof (run from /home/user/the-nightly-build): while iterating,
`./nb check .nb-work/the-evidence/whisper/library/the-evidence/whisper.html --series the-evidence --library /home/user/library-checkout --no-check-links`
then before handoff run the same command WITH links (drop `--no-check-links`) until `BLOCK: 0`. Run `./nb stamp .nb-work/the-evidence/whisper/library/the-evidence/whisper.html` before the final check.

This round's focus and decisions the inputs do not settle:
- Lead with the paper's actual claim: robustness (smaller clean-vs-messy gap), not lowest error. The evidence has the numbers (LibriSpeech test-clean tie; the 55.2% average relative error reduction across the other datasets in Table 2). Do not let the reader come away thinking Whisper is simply "the most accurate."
- Do NOT present any single figure as *the* hallucination rate. The evidence is explicit: the one controlled number (1.4%) is on aphasic speech and not general; AP's field counts are uncontrolled. State what each number measured and its scope.
- The ~438,000-hour English figure is DERIVED (a subtraction), not printed in the paper — the evidence flags it. If you use it, mark it as derived; prefer the figures the paper prints (680,000 total; 117,000 multilingual; 125,000 translation; 65% of compute on English).
- Teach word error rate here with a worked example — the evidence shows it is used but never defined in the library, so it is genuinely new. Zero-shot evaluation is already taught in the-evidence/gpt-2: link it in Background, do not re-teach.
- Break the recent Evidence dek mold. The last several deks lead with "The [X] paper [surprising verb]..." (batch-normalization, GANs, knowledge-distillation, gpt-2). Write a dek in Whisper's own nouns (hours, the robustness gap, the hallucinated text) that states the concrete finding. Vary the orientation heading away from "What 'X' actually names" / "The number on the model card."
- Source assets: the evidence flags Figure 2 and Table 2 as carrying the robustness argument better than prose. Use `nb asset` only if a captured crop genuinely lets the reader test the argument; otherwise a small table built from the evidence's verified numbers may serve. Do not stack furniture.
- Write the original-work sentence in draft-handoff.md: what this lesson does to the evidence that the evidence does not do itself.
