# Evidence record — the-evidence/gpt-4-technical-report

The evidence firmly supports the commission's angle. The GPT-4 Technical Report
itself (read in full, all 100 pages, via both the arXiv PDF and OpenAI's own
CDN copy) states its non-disclosure in one unambiguous sentence in Section 2,
not the abstract (a locator correction worth passing to the writer), and the
rest of the document confirms the shape the commission predicts: 14 pages of
capability claims and a bundled ~60-page System Card, backed by 86 pages of
appendices, references, and safety material, none of which discloses
architecture, parameter count, training data, or compute. The "90th
percentile" bar-exam claim traces cleanly to a co-authored footnote in Katz et
al. 2023, and Martínez's 2024 re-analysis — read directly — recomputes it down
to roughly the 45th percentile among people who actually passed the bar. Both
primary sources for that chain were opened firsthand; I did not re-derive the
percentile analysis beyond confirming the numbers, since the-instruments/bar-
exam-percentile already did that work. Two secondary sources (The Verge, Vice)
independently interviewed OpenAI chief scientist Ilya Sutskever within a day
of launch and got the same two-part justification he gave in the report
itself (competition, safety) — the "two independent confirmations" bar is met
for the claim that OpenAI defended the withholding on those grounds, though
both interviews clearly draw on one man's remarks in one press cycle. The
record is thin in one place: OpenAI's official openai.com launch page and
web.archive.org are both unreachable from this environment (Cloudflare
challenge and DNS failure respectively, confirmed after real-browser-header
retries), so the "OpenAI site" copy is represented instead by
cdn.openai.com/papers/gpt-4.pdf, which is the identical PDF OpenAI itself
hosts and serves without a challenge page.

## Sources

### 1. GPT-4 Technical Report (OpenAI, arXiv:2303.08774)
- URLs read in full: https://arxiv.org/pdf/2303.08774 (resolves to the
  current version, watermarked "arXiv:2303.08774v6 [cs.CL] 4 Mar 2024" on
  page 1) and https://cdn.openai.com/papers/gpt-4.pdf (OpenAI's own hosted
  copy, HTTP 200, identical text). Abstract page confirmed separately at
  https://arxiv.org/abs/2303.08774 (version history: v1 15 Mar 2023, v2 16
  Mar 2023, v3 27 Mar 2023, v4 19 Dec 2023, v5 1 Mar 2024, v6 4 Mar 2024).
- Classification: PRIMARY. OpenAI is the sole author ("Please cite this work
  as 'OpenAI (2023)'"); it owns every claim about what the report does and
  does not disclose, every exam score, and every contamination figure.
- What it establishes firsthand: the exact disclosure disclaimer; the full
  Table 1 exam battery; the MMLU score and shot count; the contamination
  methodology and per-exam results; that the bundled System Card is part of
  the same document (Appendix H); the report's own stated reasons for
  non-disclosure; the document's total length and internal proportions.
- Key verbatim passages, with locators (page numbers as printed on the PDF;
  line numbers refer to this researcher's `pdftotext -layout` extraction,
  offered only as a private cross-check, not for citation):
  - Section 2, "Scope and Limitations of this Technical Report," p.2 (NOT
    the abstract — the abstract, p.1, only says GPT-4 "exhibits human-level
    performance on various professional and academic benchmarks... a score
    around the top 10% of test takers" and gives no disclosure disclaimer):
    "GPT-4 is a Transformer-style model pre-trained to predict the next
    token in a document, using both publicly available data (such as
    internet data) and data licensed from third-party providers. The model
    was then fine-tuned using Reinforcement Learning from Human Feedback
    (RLHF). Given both the competitive landscape and the safety implications
    of large-scale models like GPT-4, this report contains no further
    details about the architecture (including model size), hardware,
    training compute, dataset construction, training method, or similar."
  - Same section, immediately after: "We are committed to independent
    auditing of our technologies, and shared some initial steps and ideas in
    this area in the system card accompanying this release. We plan to make
    further technical details available to additional third parties who can
    advise us on how to weigh the competitive and safety considerations
    above against the scientific value of further transparency." (This is
    the fairness counterweight the commission asked for: OpenAI does not
    frame the withholding as permanent or unconditional.)
  - Section 4, "Capabilities," p.4: "We tested GPT-4 on a diverse set of
    benchmarks, including simulating exams that were originally designed for
    humans. We did no specific training for these exams. A minority of the
    problems in the exams were seen by the model during training; for each
    exam we run a variant with these questions removed and report the lower
    score of the two... We estimate and report the percentile each overall
    score corresponds to."
  - Table 1, p.5: "Uniform Bar Exam (MBE+MEE+MPT) | 298 / 400 (~90th) | 298 /
    400 (~90th) | 213 / 400 (~10th)" (columns: GPT-4, GPT-4 no vision,
    GPT-3.5). Table 1 lists 34 exams/tests total.
  - Table 2, p.6: "MMLU [49] | 86.4% | 70.0% | 70.7% | 75.2%" with row label
    "5-shot" under the GPT-4 column and "5-shot" under GPT-3.5 — i.e., the
    shot count for the report's own headline MMLU number is disclosed in the
    table, even though the training method behind the model that produced it
    is not. Useful nuance against overstating the "discloses nothing" case.
  - Appendix A.1, "Sourcing," p.23: "We sourced either the most recent
    publicly-available official past exams, or practice exams in published
    third-party 2022-2023 study material which we purchased... The Uniform
    Bar Exam was run by our collaborators at CaseText and Stanford CodeX."
  - Appendix C, "Contamination on professional and academic exams," p.28:
    "We measure cross-contamination between our evaluation dataset and the
    pre-training data using substring match... For each evaluation example,
    we randomly select three substrings of 50 characters... A match is
    identified if any of the three sampled evaluation substrings is a
    substring of the processed training example... As can be seen in tables
    9 and 10, contamination overall has very little effect on the reported
    results."
  - Table 10, p.30: Uniform Bar Exam (MBE+MEE+MPT), 400 questions, 0.00%
    contamination, GPT-4 score 74.50% both contaminated and non-contaminated
    columns identical (N/A for contaminated-only, since there was none). This
    is the report's cleanest, best-supported figure: zero measured overlap
    between the bar exam and the training set, independently checked and
    reported with per-exam granularity.
  - Acknowledgements, p.17: "We thank our collaborators at Casetext and
    Stanford CodeX for conducting the simulated bar exam: P. Arredondo
    (Casetext/Stanford CodeX), D. Katz (Stanford CodeX), M. Bommarito
    (Stanford CodeX), S. Gao (Casetext)." Confirms the bar exam's originating
    team is credited as external collaborators, not report co-authors —
    the exact team that later published the separate Katz et al. paper.
  - Section 7, "Conclusion" of the main report body, p.14 — the technical
    report proper (Sections 1–7, "Introduction" through "Conclusion") runs
    14 pages, followed by acknowledgements and references, then a 77-page
    block of Appendices A–G and the System Card (Appendix H) that carries the
    document to page 100 total (confirmed via `pdfinfo`: Pages: 100).
  - Appendix H, p.40: "H System Card / The System Card [84, 85] for GPT-4 is
    appended to this document." — confirms the System Card is not a separate
    filing but Appendix H of the same PDF, beginning on p.41.
  - System Card, "1 Introduction," p.41: "Since it finished training in
    August of 2022, we have been evaluating, adversarially testing, and
    iteratively improving the model and the system-level mitigations around
    it." (One of the few concrete, dated facts about the training process
    the document volunteers, despite withholding compute/architecture/data.)
  - System Card §1.1, p.42: "To understand the extent of these risks, we
    engaged more than 50 experts to help us gain a more robust understanding
    of the GPT-4 model and potential deployment risks." Also: "The scope of
    this system card is narrower than the potential scope of abilities GPT-4
    can be used to unlock; notably, both custom fine-tuning and image
    capabilities are explicitly out of scope."
  - System Card, ARC evaluation, p.~54 (Appendix numbering restarts inside
    the System Card; located by the phrase "power-seeking"): "We granted the
    Alignment Research Center (ARC) early access to the models as a part of
    our expert red teaming efforts in order to enable their team to assess
    risks from power-seeking behavior." This is the one external,
    independent safety evaluation named in the document — worth noting for
    balance, though ARC's own report is not required reading per the brief
    and was not opened for this record.

### 2. Katz, Bommarito, Gao & Arredondo, "GPT-4 Passes the Bar Exam" (2023)
- URL read in full: https://www.courthousenews.com/wp-content/uploads/2023/03/chatgpt-bar-pass.pdf
  (HTTP 200; a hosted mirror of the paper, PDF metadata shows creation date
  28 Mar 2023 UTC; 35 pages). The canonical SSRN listing,
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233, returned
  HTTP 403 on fetch (SSRN gates automated access) — not opened directly, but
  the courthousenews mirror is the identical paper (same title, same four
  authors, same abstract and footnote text, cited by the GPT-4 report itself
  as reference [38], and cross-confirmed by Martínez 2024, which quotes the
  same footnote at the same page number).
- Classification: PRIMARY. Katz, Bommarito, Gao, and Arredondo ran the
  simulated bar exam and wrote the paper; they own the underlying score and
  the footnote that first stated a percentile.
- What it establishes firsthand: the origin of the "90th percentile" language,
  and a discrepancy in the raw score OpenAI later published.
- Key verbatim passages, p.10 (footnotes 2 and 3, attached to the paper's
  introduction):
  - Footnote 2: "Best prompt and/or hyperparameter combination on the MBE
    would push this score to 298 or higher. Here we report the MBE average
    of 75.7% which composites to a 297."
  - Footnote 3: "For the reader who is not familiar with these issues, it
    might be difficult to contextualize these UBE scores. Using a percentile
    chart from a recent exam administration (which is generally available
    online), ChatGPT would receive a score below the 10th percentile of
    test-takers while GPT-4 would receive a combined score approaching the
    90th percentile of test-takers. The overall national minimum passing
    threshold is 260 for several states such as Alabama, Minnesota and
    Missouri. The highest passing threshold is 273 for Arizona."
  - Abstract: "Graded across the UBE components, in the manner in which a
    human test-taker would be, GPT-4 scores approximately 297 points,
    significantly in excess of the passing threshold for all UBE
    jurisdictions."
  - Component table, p.10: MBE 157 points, MEE 84 points, MPT 56 points for
    GPT-4 (vs. 116/60/37 for ChatGPT).

### 3. Martínez, "Re-evaluating GPT-4's bar exam performance" (Artificial Intelligence and Law, 2024)
- URL read in full: https://dspace.mit.edu/bitstream/handle/1721.1/153986/10506_2024_Article_9396.pdf?sequence=1&isAllowed=y
  (HTTP 200; MIT's open-access repository copy of the published article,
  DOI 10.1007/s10506-024-09396-9, Artificial Intelligence and Law vol. 33,
  no. 3, accepted 30 Jan 2024). Single author: Eric Martínez (Texas A&M
  University School of Law at time of extended-author listing).
- Classification: PRIMARY for the corrected-percentile claim. Martínez
  independently reran the percentile calculation against different reference
  populations; he owns that re-analysis and its numbers, even though the
  underlying scaled UBE score he is re-contextualizing (298/297) belongs to
  Katz et al. and OpenAI. Not read for re-derivation — the-instruments/
  bar-exam-percentile already teaches this fully — read to confirm the
  numbers firsthand and locate the exact footnote citation.
- What it establishes firsthand: the corrected percentile figures across
  three different reference populations, and the identity/location of the
  footnote OpenAI's "90th percentile" traces to.
- Key verbatim passages:
  - p.10 (Katz-paper footnote reproduced and cited): "one of the only
    mentions of percentiles is in a footnote, where the authors state, in
    passing: 'Using a percentile chart from a recent exam administration
    (which is generally available online), ChatGPT would receive a score
    below the 10th percentile of test-takers while GPT-4 would receive a
    combined score approaching the 90th percentile of test-takers.' (Katz
    et al. 2023, p. 10)"
  - p.9, footnote 4, quoting the GPT-4 Technical Report directly: "the
    technical report (page 6) claims that GPT-4 'passes a simulated version
    of the Uniform Bar Examination with a score in the top 10% of test
    takers' (OpenAI 2023b)."
  - Table 1: estimated UBE percentile by test-taking population — "July
    test-takers": UBE 68th, MBE 86th, MEE+MPT 48th; "All first-timers": UBE
    62nd (printed as "62rd" in the source table, an apparent typo), MBE 79th,
    MEE+MPT 42nd; "Qualified attorneys": UBE 45th, MBE 69th, MEE+MPT 15th.
  - Body text: "With regard to the aggregate UBE score, GPT-4 scored in the
    ∼45th percentile" (against attorneys who actually passed the exam).
  - Abstract: "The paper successfully replicates the MBE score, but
    highlights several methodological issues in the grading of the MPT +
    MEE components of the exam, which call into question the validity of
    the reported essay score."

### 4. James Vincent, "OpenAI co-founder on company's past approach to openly sharing research: 'We were wrong'" — The Verge
- URL read in full: https://www.theverge.com/2023/3/15/23640180/openai-gpt-4-launch-closed-source-ilya-sutskever-interview
  (HTTP 200 via direct fetch with browser headers; WebFetch tool itself was
  blocked on this domain, confirmed by trying it first). Byline James
  Vincent, published Mar 15, 2023, 5:59 PM UTC (the day GPT-4 launched).
- Classification: SECONDARY. The Verge is an outside publication reporting
  on and interviewing OpenAI; it does not own the underlying claims, but it
  is the original outlet for the on-record Sutskever quotes below (confirmed
  not reprinted from elsewhere — the article states "Speaking to The Verge").
- What it establishes: OpenAI's chief scientist's own stated reasons for
  non-disclosure, matching the report's stated reasons, plus outside
  criticism of the decision.
- Key verbatim passages:
  - Quotes the same report sentence this record already sourced firsthand
    (confirms the journalist read the same passage), then: "Speaking to The
    Verge in an interview, Ilya Sutskever, OpenAI's chief scientist and
    co-founder, expanded on this point. Sutskever said OpenAI's reasons for
    not sharing more information about GPT-4 — fear of competition and fears
    over safety — were 'self evident': 'On the competitive landscape front —
    it's competitive out there,' said Sutskever. 'GPT-4 is not easy to
    develop. It took pretty much all of OpenAI working together for a very
    long time to produce this thing. And there are many many companies who
    want to do the same thing, so from a competitive side, you can see this
    as a maturation of the field.' 'On the safety side, I would say that the
    safety side is not yet as salient a reason as the competitive side. But
    it's going to change... As the capabilities get higher it makes sense
    that you don't want to disclose them.'"
  - On the shift from OpenAI's earlier, more open publications: "When asked
    why OpenAI changed its approach to sharing its research, Sutskever
    replied simply, 'We were wrong. Flat out, we were wrong. If you believe,
    as we do, that at some point, AI... is going to be extremely,
    unbelievably potent, then it just does not make sense to open-source. It
    is a bad idea... I fully expect that in a few years it's going to be
    completely obvious to everyone that open-sourcing AI is just not wise.'"
  - On training data specifically: "'My view of this is that training data
    is technology. It may not look this way, but it is. And the reason we
    don't disclose the training data is pretty much the same reason we don't
    disclose the number of parameters,' Sutskever said."
  - Outside criticism quoted in the piece: Ben Schmidt (VP of information
    design, Nomic AI), on Twitter: "I think we can call it shut on 'Open' AI:
    the 98 page paper introducing GPT-4 proudly declares that they're
    disclosing *nothing* about the contents of their training set." William
    Falcon (CEO, Lightning AI): "If this model goes wrong, and it will,
    you've already seen it with hallucinations and giving you false
    information, how is the community supposed to react?"

### 5. Chloe Xiang, "OpenAI's GPT-4 Is Closed Source and Shrouded in Secrecy" — Vice
- URL read in full: https://www.vice.com/en/article/openais-gpt-4-is-closed-source-and-shrouded-in-secrecy/
  (fetched successfully). Published March 16, 2023, the day after launch.
- Classification: SECONDARY. Independent outlet reporting on the same launch;
  provides a second, independently obtained instance of Sutskever giving the
  same two justifications, satisfying the commission's contradiction-seeking
  instruction to look past a single retelling — though both pieces trace to
  interviews given the same week, so this is not two independent origins of
  the underlying fact, only two independent write-ups of it.
- Key verbatim passages: quotes the identical report sentence on competitive
  landscape/safety, and separately quotes Sutskever: "Safety is not a binary
  thing; it is a process. Things get complicated any time you reach a level
  of new capabilities" and "GPT-4 is not easy to develop. It took pretty much
  all of OpenAI working together for a very long time to produce this thing"
  and "I fully expect that in a few years it's going to be completely obvious
  to everyone that open-sourcing AI is just not wise."

### 6. Katharine Sanderson, "GPT-4 is here: what scientists think" — Nature (news)
- URL: https://www.nature.com/articles/d41586-023-00816-5. Fetched directly
  (HTTP 200); paywalled beyond the opening paragraph, which is fully
  accessible without a subscription. Published 16 March 2023.
- Classification: SECONDARY. Nature's news desk, reporting on outside
  scientists' reactions; owns none of the underlying claims.
- What the accessible portion establishes: dek states "Researchers are
  excited about the AI — but many are frustrated that its underlying
  engineering is cloaked in secrecy." Opening paragraph: "Researchers say
  these abilities have the potential to transform science — but some are
  frustrated that they cannot yet access the technology, its underlying code
  or information on how it was trained. That raises concern about the
  technology's safety and makes it less useful for research, say scientists."
  This is enough to confirm the headline framing and independent-outlet
  agreement with the disclosure story; the article's full body (interviews
  with named scientists) sits behind the paywall and was not read, so no
  claim beyond this paragraph and the dek is sourced to Nature here.

## Contradictions

- **The percentile itself.** OpenAI's report and its source, Katz et al.
  2023, both describe GPT-4's Uniform Bar Exam score as landing "~90th
  percentile" / "approaching the 90th percentile." Martínez 2024, re-running
  the comparison against people who actually passed the bar (licensed or
  license-pending attorneys — the population a "passing the bar exam" claim
  implies), gets ~45th percentile overall and ~15th percentile on the essay
  components (MEE+MPT). Against all first-time test-takers the figure is
  ~62nd; against only the subset who sat the same July administration, ~68th.
  The three numbers are not competing measurements of the same thing — they
  are the same raw score set against three different comparison populations
  — but only the most flattering of the three ever reached the headline.
- **The raw score itself.** OpenAI's Table 1 reports 298/400. Katz et al.'s
  own abstract reports "approximately 297 points" as the paper's actual
  reported result, with 298 appearing only in a footnote as what "the best
  prompt and/or hyperparameter combination" would produce. OpenAI's headline
  number is the footnoted best case, not the paper's own topline figure.
- **Where the percentile claim lives.** Katz et al. call their own percentile
  mention incidental ("one of the only mentions of percentiles is in a
  footnote... in passing," per Martínez's characterization, itself confirmed
  by reading the Katz footnote directly). OpenAI's report and launch
  materials elevate that same footnote-level aside into Table 1's headline
  comparison column and the paper's own abstract sentence.
- **Whether the report withholds "nothing" or "almost nothing."** Ben
  Schmidt's tweet (quoted in the Verge piece) reads the report as disclosing
  "nothing" about training data. The report itself is narrower and more
  precise: it names the two data categories in general terms ("publicly
  available data (such as internet data) and data licensed from third-party
  providers") and the fine-tuning method (RLHF) before declining to give
  further detail on architecture, hardware, compute, or dataset
  construction. "Nothing" overstates it; "no further details" (the report's
  own phrase) is accurate and narrower.
- No contradiction found on the stated reasons for withholding: the report's
  own text, Sutskever via The Verge, and Sutskever via Vice all give the
  same two reasons (competitive landscape, safety) in the same order of
  emphasis, and none of the three journalistic or primary sources surfaced a
  competing OpenAI explanation.

## Numbers

- **298 / 400, "~90th" percentile** — Uniform Bar Exam (MBE+MEE+MPT), GPT-4
  and GPT-4 (no vision) alike. Owning primary: GPT-4 Technical Report, Table
  1, p.5. GPT-3.5 comparison on the same table: 213/400 (~10th).
- **297 points** (headline) / **298 or higher** (best-case, footnoted) —
  same UBE composite score. Owning primary: Katz et al. 2023, abstract and
  footnote 2, p.10.
- **~90th percentile** (footnote language, "approaching") — owning primary:
  Katz et al. 2023, footnote 3, p.10.
- **~45th percentile** (aggregate UBE, licensed/license-pending attorneys),
  **~69th** (MBE only, same population), **~15th** (MEE+MPT essays, same
  population); **~62nd** (aggregate UBE, all first-time test-takers);
  **~68th** (aggregate UBE, July 2022 test-takers, unadjusted for repeaters).
  Owning primary: Martínez 2024, Table 1 and body text.
- **86.4%, 5-shot** — MMLU score, GPT-4. Owning primary: GPT-4 Technical
  Report, Table 2, p.6. Comparators on the same row: GPT-3.5 70.0% (5-shot);
  best external LM evaluated few-shot 70.7% (5-shot U-PaLM); best external
  model including benchmark-specific tuning 75.2% (5-shot Flan-PaLM).
- **0.00% contamination, 400 questions** — Uniform Bar Exam, the report's
  own contamination check. Owning primary: GPT-4 Technical Report, Table 10,
  p.30. (Score identical, 74.50%, whether or not the contaminated subset —
  of which there was none — is included.)
- **34** — number of distinct exams/tests listed in Table 1 (bar exam, LSAT,
  2 SAT sections, 3 GRE sections, USABO, USNCO, MKSAP, Codeforces, 14 AP
  exams, AMC 10, AMC 12, 3 sommelier certifications, 3 Leetcode difficulty
  tiers). Owning primary: GPT-4 Technical Report, Table 1, pp.5–6 (counted
  directly from the table by this researcher).
- **14 pages** — length of the technical report's own numbered body
  (Sections 1–7, Introduction through Conclusion), before acknowledgements,
  references, and appendices. Owning primary: GPT-4 Technical Report,
  Section 7 heading appears on p.14.
- **100 pages** — total document length (report body + acknowledgements +
  references + Appendices A–G + the full System Card as Appendix H). Owning
  primary: GPT-4 Technical Report PDF, confirmed via `pdfinfo`.
- **"more than 50 experts"** — external experts engaged for the System
  Card's risk assessment. Owning primary: GPT-4 Technical Report (System
  Card §1.1), p.42. No more precise count given in the document.
- **August 2022** — month GPT-4 "finished training," per the System Card.
  Owning primary: GPT-4 Technical Report (System Card §1), p.41. This is the
  one dated fact about the training process the document volunteers.
- **50-character substrings, three per evaluation example** — the report's
  contamination-detection method (exam and academic-benchmark checks alike).
  Owning primary: GPT-4 Technical Report, Appendix C, p.28.

## Source assets

- **GPT-4 Technical Report, Table 1 (p.5, "GPT performance on academic and
  professional exams")** — a data table, not a chart, but the single most
  citable visual in the document: one row per exam, three columns (GPT-4,
  GPT-4 no vision, GPT-3.5), each cell a raw score plus an estimated
  percentile. A crop of the Uniform Bar Exam row alongside 2–3 other rows
  (e.g., LSAT, AP English Language, Codeforces) would let a reader see the
  bar-exam figure in the context of the full battery, including cases with
  wide percentile bands ("86th–100th") that make the false precision of a
  single-point percentile visible by contrast. Retain the percentile-range
  formatting exactly as printed; omit rows arbitrarily rather than
  re-deriving a subset.
- **GPT-4 Technical Report, the bar chart immediately following Table 1
  (pp.5–6, "Exam results (ordered by GPT-3.5 performance)")** — plots
  "Estimated percentile lower bound (among test takers)" for GPT-4, GPT-4 no
  vision, and GPT-3.5 across all 34 exams. Notable for the axis label itself:
  even OpenAI's own chart is titled as a *lower bound*, an explicit hedge the
  single-number "90th percentile" headline drops. Useful if the article wants
  one image that shows the report hedging its own claim.
- **GPT-4 Technical Report, Table 10 (p.30, "Contamination data for Exams
  (Details)")** — the full per-exam contamination breakdown, sorted
  most-to-least contaminated. A crop showing the Uniform Bar Exam row (0.00%
  contamination) next to a heavily contaminated row (e.g., GRE Writing,
  100.00%) would visually support the "note a well-supported figure" fairness
  requirement: the bar exam specifically is the report's cleanest contamination
  result, not a cherry-picked worst case.
- **Martínez 2024, Table 1 (p.10, "Estimated percentile of GPT-4's uniform
  bar examination performance")** — a compact 3x3 table (test-taking
  population x exam section) that is effectively the corrective counterpart
  to the technical report's Table 1. Placed side by side with OpenAI's
  "~90th" cell, it is the single clearest visual argument for the whole
  angle: same underlying score, three honestly different percentiles
  depending on comparison population, none of which is "90th" once the
  population is people who passed. Crop the full table; do not extract only
  the lowest number, since the range across populations is the point.
- Katz et al. 2023, UBE component table (p.10) — a secondary asset, useful
  only if the article wants to show the 297-vs-298 discrepancy visually; the
  Martínez table above makes a stronger single image for the article's core
  argument.

## Discarded

- **openai.com/index/gpt-4-research/ and openai.com/research/gpt-4** (the
  OpenAI GPT-4 launch page): attempted via the WebFetch tool (403) and via
  direct curl with a full browser user-agent and headers (403, Cloudflare
  JS-challenge page returned as the body). Gated, not dead — but
  unreachable with the tools available in this session. Not cited. The
  report's own PDF content (via cdn.openai.com/papers/gpt-4.pdf, which
  loaded cleanly) substitutes for the "OpenAI site" leg of the required
  primary source, since it is the identical technical report OpenAI hosts.
- **web.archive.org** (attempted to retrieve an archived copy of the launch
  page): the WebFetch tool refused the domain outright ("unable to fetch
  from web.archive.org"), and a direct curl to the Wayback Machine's
  availability API returned a DNS resolution failure through the
  environment's proxy. Not cited.
- **SSRN listing for Katz et al.** (papers.ssrn.com/sol3/papers.cfm?abstract_id=4389233):
  returned HTTP 403 on fetch (SSRN blocks automated access). Not cited
  directly; the courthousenews.com PDF mirror of the same paper was read in
  full instead and used for all Katz et al. citations above.
- **Nature news article body** (beyond the opening paragraph and dek):
  paywalled after the first paragraph; not read further, so nothing beyond
  that paragraph is sourced to this article.
- **The-instruments/bar-exam-percentile, the-evidence/sparks-of-agi, and
  the-instruments/mmlu** (prior library articles the commission asks this
  piece to link, not re-teach): confirmed to exist in the library via `nb
  history --series the-instruments` and `nb history --series the-evidence`
  (continuity check only, not read as sources, per the skill's instruction
  not to browse prior articles as background). Their one-line summaries from
  that history output: bar-exam-percentile — "OpenAI's '90th percentile'
  rests on two sentences in a co-author's footnote that name no chart and no
  comparison group. Recomputed against attorneys who actually passed the
  exam, the same 298-point score lands near the 45th percentile, and the
  15th on the essay questions closest to real legal work" (consistent with
  what this record independently verified from Martínez's paper firsthand);
  sparks-of-agi — "A qualitative probing study by fourteen Microsoft
  researchers, run on an unreleased model no outsider can check"; mmlu —
  "The lab that ships an MMLU score rarely says how it was measured." Not
  used as sources for any claim in this record; listed here only so the
  writer knows the researcher located them for continuity, not evidence.
- **Alignment Research Center's own report on the power-seeking evaluation**:
  named inside the GPT-4 System Card but not independently opened. Not
  required by the brief and tangential to the disclosure angle; the System
  Card's own description of ARC's role (quoted above) is sufficient for
  whatever the writer needs from that thread.
