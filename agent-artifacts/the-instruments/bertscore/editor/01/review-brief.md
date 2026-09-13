# editor review-brief: the-instruments/bertscore (editor/01)

Inputs:
- ../../editorial-direction.md — the standard to edit against
- ../../commission.md — the assignment, the reader's situation, the boundaries
- ../../writer/01/brief.md — the exact writer brief (check the draft against it for leakage and for the decisions it carried)
- ../../writing-coach/01/voice-guide.md — read first; the register and the exemplar passages to check borrowed phrasing against
- ../../researcher/01/evidence.md — the claim set; reread cited passages looking for what breaks a claim
- ../../writer/01/draft-handoff.md — the original-work sentence (open on the third read) and the writer's open note
- the article: /home/user/the-nightly-build/.nb-work/the-instruments/bertscore/library/the-instruments/bertscore.html
- template context: /home/user/the-nightly-build/.nb-work/the-instruments/bertscore/.nb-context/

Output: editorial-review.md (in this directory)

Round's focus (things to check hardest for this piece):
- Recompute the rescaling arithmetic in the draft (raw-to-rescaled: 0.959→0.759, 0.931→0.576) against the evidence record's Numbers, and confirm every figure carries its scope.
- The PAWS robustness result must NOT be presented as a general robustness claim; a cited study (Hanna & Bojar) shows the opposite for subtle function-word errors. Confirm the contradiction is weighed, not hidden.
- The version-hash "compliance" question is unsourced: confirm the draft states the request exists and leaves compliance unknown, or cut it. No claim about whether practitioners follow it.
- Confirm word-overlap metrics, embeddings, and F1 are linked (Background / prior lessons), not re-taught, per the commission.
- The writer flags no per-token cosine worked example in the evidence. Judge whether the qualitative token-matching plus the rescaling arithmetic is enough to teach the mechanism; if you judge a per-token example is required to make the lesson land, route a precise researcher request rather than letting the writer invent numbers.

Recent-pattern notes (compare edges, headings, dek against the recent Instruments record):
- Headlines built on "a [metric] can hide / misled" and single-dramatic-number deks recur across the desk; flag any echo as formula.
- Deks that chain clauses with commas and close on "and", the semicolon reversal, and the suspended question are banned molds; check this dek against them.
- Section headings must be this piece's own steps, never stock labels.
