# editor review-brief: the-evidence/seq2seq (01)

Inputs:
- editorial-direction.md   (house standard, slop/headline specs, paper voice, template identity)
- commission.md            (the assignment, its boundaries, the reader's situation)
- writer/01/brief.md        (the exact writer brief incl. the corrected angle — check for leaks against it)
- writing-coach/01/voice-guide.md   (read first; how the piece should sound; check for borrowed phrasing)
- researcher/01/evidence.md   (the claim set; reread cited passages for what breaks each claim)
- writer/01/draft-handoff.md   (open its original-work sentence only on the third read)
- the drafted article at library/the-evidence/seq2seq.html
- .nb-context/ (effective template contract and furniture catalogs)

Output: agent-artifacts/the-evidence/seq2seq/editor/01/editorial-review.md
Proof (orchestrator stamps and runs after your edits): ./nb check .nb-work/the-evidence/seq2seq/library/the-evidence/seq2seq.html --series the-evidence

Recent-pattern notes (check the draft against these library habits):
- The Evidence headlines run "[Subject] [verb] [surprising quantified result]" (e.g. "LoRA matched full
  fine-tuning by training 4.7M of 175 billion weights"). Flag a rote clone of that "matched/lost/lifted by N" mold.
- Banned dek molds seen in the library: comma-triad, semicolon reversal, suspended question. Check the dek.
- Heading habit to break: two clauses joined by a comma and "and." Vary construction.
- Closer habit: older pieces restated the finding in a Verdict block; the takeaway bookend lands the judgment.
- Bookend openers must hold to this lesson's particulars, not generic importance.

This round's focus:
- Verify the CORRECTED ANGLE held: the piece must NOT have seq2seq concede or worry about the fixed-length-vector
  bottleneck. The paper claims the OPPOSITE (it was "surprised" the LSTM did well on long sentences, S3.7). The
  bottleneck diagnosis must be attributed to Bahdanau et al. (1409.0473) and the measured degradation to Cho et
  al. (1409.1259, on a single-layer non-reversed model), NOT to seq2seq. If the draft slips into "seq2seq admitted
  the bottleneck," that is a required revision.
- Check the BLEU decomposition against the record: 34.81 = reversing + 5-model ensemble + beam 12; single-model
  reversed = 30.59; SMT baseline = 33.30; SMT-rescoring = 36.5. The draft must not present 34.81 as a bare
  single-model number.
- Check scale figures (4 layers, 1000 cells/dim, ~384M params, 12M-pair WMT'14 En-Fr, 160k/80k vocab, 8 GPUs
  ~10 days) and the reversing figures (perplexity 5.8->4.7, BLEU 25.9->30.6) against the record. Check
  primary/secondary data-nb-kind on each source.
- Confirm no from-scratch LSTM re-teaching beyond what the reader needs.

Note on internal links: the prose/Background links to the-evidence/attention-is-all-you-need are VALID (that
article is published) and resolve on the library branch, not in this isolated workspace — do not treat as broken.
