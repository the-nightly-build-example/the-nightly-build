# editor review-brief: the-evidence/flamingo (01)

Inputs (read the voice guide first; open the evidence on the first read, the
draft-handoff's original-work sentence on the third):
- ../../editorial-direction.md — house standard, voice, series prompt, template identity.
- ../../commission.md — the assignment and the reader's situation.
- ../../writer/01/brief.md — the exact writer brief (to catch leaks and unmet items).
- ../../writing-coach/01/voice-guide.md — how this piece should sound, with exemplar passages.
- ../../researcher/01/evidence.md — the evidence record.
- ../../writer/01/draft-handoff.md — the original-work sentence and proof result.
- article: /home/user/the-nightly-build/.nb-work/the-evidence/flamingo/library/the-evidence/flamingo.html
- template context: /home/user/the-nightly-build/.nb-work/the-evidence/flamingo/.nb-context/

Output: ./editorial-review.md   (decision: approve | revise)

Two items from the writer to check specifically:
1. The writer recomputed the "~1000x less data" high end as COCO/VATEX
   (~15,600:1), saying the evidence record's Numbers section mislabels it as
   VQAv2. Verify this against the evidence record and, if needed, the cited
   primary. If the writer's recomputation is not supported by the record's own
   quoted counts, route it back (do not let a derived number stand unsupported).
2. The writer omitted the commission's "Flamingo still hallucinated / documented
   failure modes" point because the evidence gave locators but no citable
   paraphrase. Judge whether the piece needs it: if yes, this is a researcher
   request (Section 5 / Appendix D.1), not something to invent. The required
   contribution otherwise stands without it.
Also confirm: the headline count is "6 of 16" (not the paper's contradictory
"seven" caption); the piece does not speculate why the weights were withheld; and
it does not close on a "reproduced on open data" beat (clip and vision-transformer
already do).

Recent-pattern notes (habits from the recent library — catch any that recur here;
no single article shows a formula, which is why you hold these):
- Openers built on a "By the end you will know how X, why Y, and Z" triad, and
  temporal-generic scene-set first sentences.
- Takeaways that land on a tidy two-part balance ("Both things are true"; "X is a
  real result told slightly wrong").
- Over-used Evidence heading molds: "How a X becomes a Y", "From X to Y", "The X
  outlived the Y", and the "What holds up / What to be careful about" pairing
  (often the nb-holdsup block) — flag if the piece defaults to any of these.
- Deks leaning on a comma splice or comma triad (banned in `spec/headlines.md`).

Round focus: this is a foundational-document lesson; hold it to the desk's
contract (what the document is, what it did at what scale, how its use today
outruns what it showed), and hold the bookends to the lesson template (written
after the body, this lesson's particulars only, no Verdict-style closer).
