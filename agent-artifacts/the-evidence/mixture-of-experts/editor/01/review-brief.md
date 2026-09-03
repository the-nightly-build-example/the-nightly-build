# editor review-brief: the-evidence/mixture-of-experts (01)

Inputs (read the voice guide first; open evidence when the first read calls for
it; open the draft-handoff original-work sentence only at the third read):
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/editorial-direction.md
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/commission.md
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/writer/01/brief.md
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/writing-coach/01/voice-guide.md
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/researcher/01/evidence.md
  - .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/writer/01/draft-handoff.md
  - .nb-work/the-evidence/mixture-of-experts/library/the-evidence/mixture-of-experts.html  (the article)
  - .nb-work/the-evidence/mixture-of-experts/.nb-context/  (effective template contract, furniture catalogs)

Output: .nb-work/the-evidence/mixture-of-experts/agent-artifacts/the-evidence/mixture-of-experts/editor/01/editorial-review.md
Proof (after your edits, the orchestrator stamps and checks; if your edits demand new prose it returns to the writer):
  ./nb check .nb-work/the-evidence/mixture-of-experts/library/the-evidence/mixture-of-experts.html --series the-evidence --library /home/user/library-checkout

This round's focus:
- The spine is the total-vs-active parameter honesty claim. Verify every
  parameter/compute figure (Switch-C 1.571T params / 890B FLOPs, Shazeer's
  4.3B/8.9M-ops, Mixtral 47B/13B) against the owning primary in the evidence
  record; a wrong display figure reaches every reader.
- The routing-dispute framing (Shazeer k=4 / GShard top-2 / Switch top-1) must
  read as the field revising its own guess, not a strawman contrast — check the
  "not X but Y" reflex here against spec/slop.md.
- Confirm GShard's flagged BLEU is not quoted, and no figure the record marked
  unverified is stated as fact.
- Furniture: an annotated equation and a reproduced Table 1 carry the mechanism —
  check the equation and every table cell against the evidence record and the
  primary; the writer noted no source asset was captured (optional Shazeer Fig 1
  routing diagram) — request it only if a reader needs it to test the argument.

## Recent-pattern notes (compare edges, headings, dek, furniture against these)
- Dek molds recurring in the library: the "credited with X, but Y had already done
  it" reversal and the "the [term] now used far more loosely" tag; plus the
  spec/headlines.md-banned semicolon reversal, suspended question, and comma triad.
- Why-this-matters: the "This lesson opens/reads ..." opener and the "By the end
  you will be able to explain X, Y and Z" list formula recur — flag if present.
- Opening body heading: the short declarative "reveal" mold recurs across desks;
  and pieces keep closing the last body section on a stamped present-tense
  one-liner. Flag a heading or closer built to a prior article's pattern.
- Four siblings ship tonight (task-time-horizon, option-order-bias, algorithmic-
  collusion, clearview-ai); this piece must not share a "the metric everyone
  misreads" framing with the instruments pieces.
