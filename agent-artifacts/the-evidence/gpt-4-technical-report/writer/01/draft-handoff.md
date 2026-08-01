# Draft handoff — writer 01 — the-evidence/gpt-4-technical-report

## Original-work sentence
The evidence record itemizes, as separate facts, the report's disclosure
sentence, the precision of its exam/contamination/shot-count reporting, and
the three-hop citation chain behind "90th percentile" (report Table 1 ->
Katz footnote -> Martínez re-analysis). This article's one act of original
work is fusing those separate facts into a single test a reader can apply to
any number sourced to this report: did the report measure the figure itself
(as it did with contamination, exam scores, and the MMLU shot count), or did
it only repeat someone else's aside (as it did with the bar-exam
percentile)? That test, not stated anywhere in the evidence record, is what
the article teaches and what its closing paragraphs (end of the third flex
section, and the takeaway) apply.

## Paths changed
- `.nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html`
  (filled in place: header, both bookends, orientation + 3 named flex
  sections — "What the report measures itself," "Competition, safety, and
  outside review," "A number the report didn't compute itself" — one
  stat-strip, and 6 sources).
- No chart or source asset created. Considered the report's own bar chart
  (axis labeled "estimated percentile lower bound") and Martínez's Table 1
  as candidate source assets; decided against both. Rebuilding either would
  have re-derived territory the commission explicitly assigns to
  the-instruments/bar-exam-percentile ("link it, do not rebuild it"), and
  the stat-strip plus the disclosed/withheld distinction argued in prose
  already carry the "show the scale honestly" requirement without needing
  a PDF crop whose exact bounding box I could not visually verify in this
  session.

## Proof result
`./nb check ... --no-check-links`: BLOCK: 0, 3 WARN, verdict PUBLISHABLE.
Final proof `./nb check ...` (link checking on, default): BLOCK: 0, same 3
WARN, verdict PUBLISHABLE. All 6 source URLs resolved.

Warnings left intentionally (all three are W-SENTENCE-DENSITY):
- Two are a short lead-in clause fused to a verbatim quote from the GPT-4
  Technical Report's Section 2 disclosure sentence and its follow-on
  auditing-commitment sentence.
- One is a short lead-in clause fused to a verbatim quote from Katz et
  al.'s footnote 3 (the percentile's origin).
All three quotes are the evidence the article's argument turns on; the
citation policy and voice guide both require lifting the source's own
wording rather than paraphrasing it, so the sentences were not shortened.
Every other flagged long sentence (originally 5 additional instances, all
in my own prose) was split during drafting.

## Editorial requests addressed
N/A — first draft (invocation 01), no prior editorial-review.md.

## Remaining evidence or voice questions
None. The evidence record fully supported the commission's angle; no
researcher gap was hit. One locator nuance from the evidence record (the
disclosure disclaimer sits in Section 2, not the abstract) was used as
the article's opening structural beat rather than called out as a
correction, per the record's own note that it was "worth passing to the
writer."
