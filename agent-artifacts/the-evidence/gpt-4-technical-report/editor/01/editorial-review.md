# Editorial review 01 — the-evidence/gpt-4-technical-report

Skeptic: thesis "the GPT-4 Technical Report draws its own line, in Section 2,
between what it measured (exam scores, contamination, shot counts) and what
it withholds (architecture, compute, data, method), and a reader can test any
number sourced to it by asking whether the report measured that number itself
or only repeated someone else's aside"; tested 11 claims; broke: two. (1) The
dek stated the report says it "will say nothing" about how the model was
built — the report's own phrase is "no further details," and the article's
own body argues at length that "nothing" overstates it (the Ben Schmidt
paragraph exists specifically to make that point). The dek was contradicting
the piece it headlines. Fixed by quoting the report's actual scope ("no
further details") in the dek. (2) The report's acknowledgements credit
Bommarito to Stanford CodeX, not Casetext — confirmed against both the GPT-4
report's own acknowledgements page and the Katz et al. paper's own author
affiliation list, which lists Bommarito under the same footnote numbers as
Katz (Stanford CodeX among them), not under Casetext (Gao's sole affiliation).
The article had grouped Bommarito with Casetext. Fixed by moving him into the
Stanford CodeX clause. Also caught: the Sutskever "self evident" quote is
dated to "the day GPT-4 launched," but GPT-4 launched March 14, 2023 (OpenAI's
own product release, corroborated by contemporaneous coverage) and the cited
Verge interview is byline-dated March 15 — a day later. Fixed to "the day
after." Every number rechecked directly against the arXiv PDF (pdfinfo
confirms 100 pages, page 14 ends the numbered Conclusion, page 2 carries
Section 2, Table 1's Uniform Bar Exam row reads 298/400 ~90th vs GPT-3.5's
213/400 ~10th, Table 2's MMLU row reads 86.4% at 5-shot, Table 10's Bar Exam
row reads 0.00% contamination, Table 1 lists exactly 34 exams including
fourteen AP subjects, three GRE sections, and three Leetcode tiers) held.
Katz et al.'s footnotes 2 and 3 (297 vs. "298 or higher," and the unnamed
percentile chart) were confirmed against the source PDF directly, as was
Martínez's ~45th-percentile figure against qualified attorneys. The Verge,
Vice, and Nature quotes and deks were all confirmed against the live pages.
No broken central claim and no source-kind mislabeling: every `data-nb-kind`
matches the evidence record's classification.

Cut: 2 sentences trimmed (no full sentence deleted, both trims were
clause-level); worst tell: self-narration reappearing in body prose outside
the bookends the template exempts for it — "The contamination check earlier
in this lesson traces to..." and "a population no document in this record
ever names" both pointed at the article's own apparatus ("this lesson," "this
record") rather than the report. Cut both phrases; the sentences read cleaner
without them and lose no claim. The three W-SENTENCE-DENSITY warnings are all
a short lead-in clause fused to a verbatim quote from the report's Section 2
or Katz et al.'s footnote 3 — the citation policy and the voice guide both
require lifting that exact wording rather than paraphrasing it, so they stay;
trimming inside the quotation marks would misquote the source. No formulaic
opener, dek mold, or retired Verdict block found; no prompt leakage beyond
the two self-reference phrases already cut.

Reader: this gives me a transferable test — did the report measure this
number itself (as it did with contamination, MMLU's shot count, and the exam
battery) or did it only repeat someone else's aside (as it did with the
bar-exam percentile) — that neither the report, Katz et al., nor Martínez
states outright; it is the article's own synthesis across three primary
documents. The prose sits close to the voice-guide exemplars: it quotes the
report's disclosure sentence and Katz's footnote in full rather than
paraphrasing them, and it places the report's careful work (contamination,
MMLU shot count, the ARC evaluation) in the same paragraphs as its overstated
number, so the fairness is structural rather than a closing caveat, matching
the Sanderson/Lee/Mitchell craft notes rather than a median AI summary. The
headline, reread as the largest claim, holds: "declares 'no further details'"
is Section 2's own phrase, verified against the PDF, not the writer's
characterization.

## Direct edits made (in the article)
- `nb-meta.dek` and the `<p class="nb-dekline">`: "that it will say nothing
  about how the model was built" → "that it gives no further details on how
  the model was built" — fixes a display-text claim the article's own body
  contradicts.
- Competition/safety section: "the day GPT-4 launched" → "the day after GPT-4
  launched" — GPT-4 launched March 14, 2023; the cited Verge piece is dated
  March 15.
- Bar-exam section: "Pablo Arredondo and Daniel Katz of Stanford CodeX, along
  with Michael Bommarito and Shang Gao of Casetext" → "Pablo Arredondo,
  Daniel Katz, and Michael Bommarito of Stanford CodeX, along with Shang Gao
  of Casetext" — corrects Bommarito's affiliation per the report's own
  acknowledgements and the Katz et al. paper's author list.
- Cut "earlier in this lesson" and "in this record" (two clause-level
  self-reference trims, body prose outside the exempt bookends).
- `nb-meta.words`: 1696 → 1690, reflecting the net word loss from the cuts
  above (my own rough count; the writer should confirm the exact figure by
  rerunning `nb check`, since it is the tool of record for that number).

## Required work by owner
None. All findings were fixable within a clause and are already applied.

## Final decision
No redraft required. `./nb check ... --no-check-links` after these edits
still returns `BLOCK: 0`, the same 3 W-SENTENCE-DENSITY warnings (unchanged,
all three are quote-fused sentences the citation policy requires keeping
whole), and `verdict: PUBLISHABLE`. The writer should re-run the full proof
(with link checking) once to confirm the word count and reading time after
these edits before publication, per the skill's proof-gate ownership.
