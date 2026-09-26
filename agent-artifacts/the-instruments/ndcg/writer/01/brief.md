# writer brief: the-instruments/ndcg (01)

Inputs:
- editorial-direction.md (../../editorial-direction.md)
- commission.md (../../commission.md) — assignment and the post-research angle refinement. Read the refinement.
- writing-coach/01/voice-guide.md (../../writing-coach/01/voice-guide.md) — reread before drafting.
- researcher/01/evidence.md (../../researcher/01/evidence.md) — complete claim set; use the Numbers section exactly (two worked examples are provided).

Output:
- /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/agent-artifacts/the-instruments/ndcg/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/the-instruments/ndcg/library/the-instruments/ndcg.html --series the-instruments --repo /home/user/the-nightly-build

Article file to edit:
/home/user/the-nightly-build/.nb-work/the-instruments/ndcg/library/the-instruments/ndcg.html

Work from these inputs. Ask the orchestrator if the record lacks something; do
not invent or expand the claim set.

## This round's focus

- Build nDCG up term by term to a worked example (use the record's arithmetic-
  verified instance; do not compute your own labels). A table is the natural home
  for the worked calculation.
- Keep the NARROW angle: a single nDCG@10 hides its choices (judged docs, grade
  scale, gain convention, discount convention, cutoff) and can move without any
  system improving. Do not argue "nDCG is bad"; respect the Sanderson 2010 and
  Wang 2013 defenses.
- Use BEIR's TREC-COVID hole experiment as the central misleading case (systems
  unchanged, filling missing labels flipped the ranking); Ferrari Dacrema can be
  a shorter second example. This is a strong source asset (BEIR Table 4) — a
  small table or figure may carry it faster than prose.
- Put the one-sentence original-work claim in draft-handoff.md; make it visible.

## Recent shapes to break (the-instruments)

- Recent openers: "When a chipmaker says ..." (mlperf), "The attack success rate
  is the number behind ..." (attack-success-rate). Do not default to those.
- Do not close the opener on "By the end you will know A, B, and C."
- Recent deks pair a number with a reversal; check yours against mlperf,
  attack-success-rate, helm, calibration-error so it is built differently.
- Check headings so they are not stamped to the recent record.

## Craft reminders

- Lesson form: Why this matters, body, The takeaway. Body first; bookends after,
  addressing the reader, no citations; the body speaks to no one and never
  mentions the lesson.
- Cite per-section (why/takeaway exempt). Number sources in first-citation order;
  carry data-nb-kind from the record; prefer real locators over homepages. Gated
  publisher pages are fine to cite at a resolving canonical address (DOI / arXiv
  abs). If the link check flags a URL, switch to a resolving page for the same
  document or ask me.
- Link mteb, the-mechanics/retrieval, and mean-average-precision in Background /
  at first use; do not re-teach them.
- Fill nb-meta: harness "Claude Code (nb-orchestrator edition)", model you run
  as, real dates for 2026-09-26. Run `nb stamp` then the exact proof until
  BLOCK: 0 (--no-check-links while iterating; full check before handoff).
  nb-meta dek and rendered dekline identical.
- Check headline/dek/subheads against the record, spec/headlines.md, spec/slop.md.

Write draft-handoff.md with the original-work sentence, the proof result (and any
warning left on purpose with its reason), and any open question. Report the
handoff path and any warning left.
