# editor brief: the-mechanics/speculative-decoding (01)

Inputs (read each):
- editorial-direction.md — the concatenated governing standard (house editorial,
  slop, headlines, press voice, lesson identity, series prompt).
- commission.md — the assignment, teach-list, boundaries, sources plan.
- writer/01/draft-handoff.md — the writer's account of choices and open risks.
- writing-coach/01/voice-guide.md — how this piece should sound.
- researcher/01/evidence.md — the source record; every body claim must trace to
  a source here, and each cited URL must resolve.
- library/the-mechanics/speculative-decoding.html — the article to edit in place.

Output: editorial-review.md (this directory), recording what you cut or changed
and your decision (approved with no required change, or the specific change you
are routing back to the writer).

Proof: after editing, run
  ./nb stamp .nb-work/the-mechanics/speculative-decoding/library/the-mechanics/speculative-decoding.html
  ./nb check .nb-work/the-mechanics/speculative-decoding/library/the-mechanics/speculative-decoding.html --series the-mechanics
and leave it at verdict PUBLISHABLE with no BLOCK, word count 1200-2200.

Recent-pattern notes for this desk (catch a formula no single article shows):
- the-mechanics headlines are behavior-first; that is fine. Dek molds this desk
  has over-used and must not recur: the semicolon reversal ("X does A; Y doesn't"),
  the suspended question, and the comma triad. Check the dek against these.
- A final body section named "How far the X reaches" / "How far the explanation
  reaches" has recurred paper-wide (attribute-binding, encoded-reasoning). Reject
  that heading shape. Also check the headings are not all built as a comma-and
  clause.
- Press rule: the takeaway bookend lands the judgment; do NOT let the body close
  on a Verdict note or any block that restates the finding.

This round's focus:
- Slop at edges (first/last sentence of each paragraph, section, and the whole
  piece; test the article's last sentence hardest). Delete, do not repair.
- The worked accept/reject table: the writer flags its token values are an
  illustrative construction of the mechanism, not measured data. Make sure the
  prose and caption frame it as an illustration of how accept/reject works, cited
  to the mechanism source, and never as an empirical measurement.
- The vLLM doc (source 4) is partly paraphrased; make sure no sentence states as
  a verbatim/observed fact something the source only supports loosely. Every
  figure and the identical-output guarantee must trace to a primary source in
  evidence.md.
- The distinction from first-token-latency / prefill-and-decode / nondeterminism
  / sampling-temperature stays clean; neighbors are linked, not re-taught.
Nothing else.
