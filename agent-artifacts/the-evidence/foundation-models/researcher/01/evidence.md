# Evidence: the-evidence/foundation-models (researcher 01)

The angle holds up under direct reading. The report itself, read start to finish
in its current arXiv text, is a 214-page, 114-author position paper with no
original experiment: its own "Author Contributions" note describes 26 sections
each written by a subset of a self-organized Stanford community, and its single
data-derived chart (Fig. 19) compiles numbers from Brown et al. 2020 and GPU spec
sheets rather than reporting anything CRFM measured. Section 1.1.1, "Naming,"
states the word "foundation" was chosen deliberately, in the report's own words,
to "connote the significance of architectural stability, safety, and security."
That rationale drew immediate, substantive pushback within a month of
publication from named researchers across several institutions, not only from
critics of large models generally — Thomas Dietterich's on-record remark that
the framing "does smack of flag planting" and Gary Marcus and Ernest Davis's
essay-length rebuttal both land on exactly the "self-serving naming" claim the
commission wants shown, not asserted. The term's later spread into standing
federal technical guidance (NIST, 2024) supports "became standard usage,"
though the evidence is thinner on why "foundation model" specifically beat
rival terms like "large language model" — no source explains the mechanism of
adoption, only documents the fact of it. The record is also thin on one nuance
worth handling carefully in the draft: the term's one clear entry into binding
U.S. law (Executive Order 14110, 2023) was rescinded fifteen months later, so
that specific citation supports "was written into federal regulation," not
"remains federal law today."

### Sources

```text
URL:         https://arxiv.org/abs/2108.07258
Kind:        primary — arXiv's own structured record of the paper (author list,
             version history, abstract, category); the paper's own metadata.
Establishes: version history — v1 filed 2021-08-16, v2 2021-08-18, v3 (current)
             2022-07-12. Structured author list totals 114 <author> entries
             (counted directly from the API XML), ending with Percy Liang as
             corresponding author. arXiv comment field: "Authored by the Center
             for Research on Foundation Models (CRFM) at the Stanford Institute
             for Human-Centered Artificial Intelligence (HAI)."
Paraphrase:  The document is Stanford CRFM's, has gone through three arXiv
             revisions, and its author count is a verifiable 114, not the
             128 or 132 an automated summary first guessed (both discarded
             below).
Locators:    Atom API response for id_list=2108.07258, <author> tags; <arxiv:comment>.
Quote:       none needed — figures, not prose.
```

```text
URL:         https://arxiv.org/pdf/2108.07258
Kind:        primary — the report itself (arXiv v3, current version).
Establishes: What the document is and does. Read in full via extracted text
             (214 numbered pages per pdfinfo and the printed footer on the
             References' final page). Abstract defines the term. §1.1.1
             "Naming" explains the word choice. Table of contents shows six
             top-level sections (Introduction, Capabilities, Applications,
             Technology, Society, Conclusion) with 26 subsections and no
             Methods/Results section. "Author Contributions" (p.14) states
             each of the 26 sections was written by a subset of authors and
             "not all the views expressed in this report are held by all the
             authors." "Conflict of Interest" note: CRFM "receives funding
             from Google, Microsoft, and the McGovern Foundation as of July
             2022." Fig. 19's caption states its numbers are "obtained from
             relevant papers [Brown et al. 2020]" and GPU spec sheets — the
             report's one quantitative chart is a compilation, not original
             measurement. A full-text search for "we conduct," "we trained,"
             "our experiment," and "we ran" returns no original-experiment
             language anywhere in the document.
Paraphrase:  A large, multi-author survey and research agenda, organized as a
             taxonomy across four parts, that names and frames a category
             rather than reporting a new empirical finding.
Locators:    p.1 (abstract); p.3, §1 (introduction, footnote 2); pp.6-7,
             §1.1.1 "Naming"; p.2 (contents); p.13, Fig. 4 (roadmap); p.14
             ("Author Contributions"); p.161-162 (Conclusion, Acknowledgments,
             Conflict of Interest); p.97 area, Fig. 19 and caption (§4.5).
Quote:       "AI is undergoing a paradigm shift with the rise of models (e.g.,
             BERT, DALL-E, GPT-3) trained on broad data (generally using
             self-supervision at scale) that can be adapted to a wide range of
             downstream tasks. We call these models foundation models to
             underscore their critically central yet incomplete character."
             (p.1, abstract)

             "We introduce the term foundation models to fill a void in
             describing the paradigm shift we are witnessing... In particular,
             the word 'foundation' specifies the role these models play: a
             foundation model is itself incomplete but serves as the common
             basis from which many task-specific models are built via
             adaptation. We also chose the term 'foundation' to connote the
             significance of architectural stability, safety, and security:
             poorly-constructed foundations are a recipe for disaster and
             well-executed foundations are a reliable bedrock for future
             applications. At present, we emphasize that we do not fully
             understand the nature or quality of the foundation that
             foundation models provide; we cannot characterize whether the
             foundation is trustworthy or not." (§1.1.1, pp.6-7)

             "The writing of this report was an experiment: we had over 100
             people from different backgrounds come together to write a single
             report covering a wide range of aspects of foundation models. A
             large part of this report is a survey of existing work..." (p.12,
             §1.4)

             "The report is divided into 26 sections, each discussing one
             aspect of foundation models." (p.12, §1.4)
```

```text
URL:         https://arxiv.org/pdf/2108.07258v2
Kind:        primary — the report itself, version 2 (filed 2021-08-18), the
             version current when the contemporaneous critiques below were
             written.
Establishes: Page count at the time of the objections: 212 pages (pdfinfo).
             The author block matches v3 exactly (same 114 names, same order),
             so the author count did not change across revisions; only length
             did (v1 = 211 pages, v2 = 212, v3 = 214).
Paraphrase:  Gary Marcus and Ernest Davis's contemporaneous "212-page report"
             description is accurate to the version they read, not a loose
             estimate — a useful precision check the writer can use instead of
             citing the current 214-page count as if it were what critics saw.
Locators:    Title page (author block); pdfinfo page count.
Quote:       none — a page-count verification, not a prose source.
```

```text
URL:         https://crfm.stanford.edu/report.html
Kind:        primary — CRFM's own report landing page.
Establishes: The report's official home and CRFM's own citation convention:
             "To cite an individual section of the report, please reference
             the section number. For example, for the ethics section, cite as
             (Bommasani et al., 2021, §5.6)." Confirms institutional ownership
             and that CRFM itself treats the document as a reference work to
             be cited by section, consistent with it functioning as a survey
             rather than a single bounded finding.
Paraphrase:  CRFM's own presentation of the report reinforces that it was
             built, and is used, as a sectioned reference document.
Locators:    Report landing page, citation-guidance paragraph.
Quote:       "To cite the entire report, please use the BibTeX entry provided
             below."
```

```text
URL:         https://thegradient.pub/has-ai-found-a-new-foundation/
Kind:        primary — Gary Marcus and Ernest Davis's own essay, in their own
             words, responding directly to the report.
Establishes: The contemporaneous, well-argued objection the brief asks for.
             Published 2021-09-11 (per the article's own byline/date), roughly
             26 days after the report's first arXiv posting. Marcus is
             Professor Emeritus of Psychology and Neural Science at NYU and
             founder of Robust.AI; Davis is Professor of Computer Science at
             NYU. Their argument: the name "foundation model" oversells
             reliability the models have not earned, the report itself
             concedes this ("we do not fully understand the nature or quality
             of the foundation"), and the branding functions as more than
             description. They report, without disputing, that Georgia Tech
             professor Mark Riedl called the branding "a brilliant … PR stunt"
             and that UC Berkeley's Jitendra Malik told a CRFM-organized
             workshop the models "are castles in the air; they have no
             foundation whatsoever." They also report University of
             Washington linguist Emily Bender's tweet that the claims "suck
             the oxygen out of the room for all other kinds of research," and
             a figure — "32 faculty and 117 research scientists, postdocs, and
             students" (149 total) — for who was behind the report's
             declaration, a number that does not match the report's own
             114-name byline (flagged under Contradictions).
Paraphrase:  The strongest single primary objection available: a named,
             credentialed pair arguing in full, at essay length, that the
             coinage was premature and partly rhetorical.
Locators:    Full essay text, paragraphs beginning "The broader AI community,"
             "As Georgia Tech professor Mark Riedl," "In the final analysis,
             we have five serious concerns."
Quote:       "The first, already discussed, is that we think that relabeling
             'pretrained language models' as foundation models is misleading.
             Foundation models certainly sound cooler. But sounding cooler
             doesn't mean that those models provide the foundations AI so
             desperately needs."

             "As Georgia Tech professor Mark Riedl wrote on Twitter 'Branding
             very large pre-trained neural language models as "foundation"
             models is a brilliant … PR stunt. It presupposes them as
             inevitable to any future in AI.' But that doesn't make it so."

             "The report says, unironically, 'we do not fully understand the
             nature or quality of the foundation that foundation models
             provide', but then why grandiosely call them foundation models at
             all?"
```

```text
URL:         https://crfm.stanford.edu/commentary/2021/10/18/marcus-davis.html
Kind:        primary — the same Marcus and Davis essay, republished by CRFM
             itself as invited commentary on 2021-10-18.
Establishes: That CRFM itself hosted the objection as a direct response to its
             own report — the naming argument was answered by its authors'
             institution, not merely aired elsewhere. Text is identical to the
             Gradient original; this entry exists to record CRFM's own
             republication date and venue, distinct from the essay's original
             date above.
Paraphrase:  CRFM engaged the objection publicly and promptly rather than
             ignoring it.
Locators:    Page header ("In response to 'On the Opportunities and Risks of
             Foundation Models' (Bommasani et al., 2021)"); same body text as
             the Gradient original.
Quote:       (see thegradient.pub entry above — identical text)
```

```text
URL:         https://www.wired.com/story/stanford-proposal-ai-foundations-ignites-debate/
Kind:        secondary — Wired reporting (Will Knight), independent of CRFM
             and of the critics quoted.
Establishes: Broader, named reception. Published 2021-09-14 (updated
             2021-09-17 per the article's own correction note — the earlier
             version's title used "foundational models" in error). Direct
             quotes obtained by the reporter: Jitendra Malik ("I think the
             term 'foundation' is horribly wrong," and "These models are
             really castles in the air; they have no foundation whatsoever...
             there is this fakeness, there is no real understanding");
             Subbarao Kambhampati of Arizona State ("Calling them 'foundation
             models' completely messes up the discourse"); Thomas Dietterich
             of Oregon State, former AAAI president ("I was surprised that
             they gave these models a fancy name and created a center... That
             does smack of flag planting, which could have several benefits on
             the fundraising side"); Emily Bender of the University of
             Washington (worry that the framing favors "the data-centric
             approach to AI favored by industry" and diverts funding from
             "adjacent, really important fields"). Percy Liang, "director of
             the new Stanford research center," is quoted responding: "All of
             these critiques are welcome."
Paraphrase:  Independent reporting corroborates that the objection was
             widespread among named senior researchers within weeks, and gives
             the single most direct hit on "self-serving": Dietterich's
             "flag planting... fundraising" line.
Locators:    Article body, paragraphs on Malik, Kambhampati, Dietterich, and
             Bender; correction note at article foot.
Quote:       "But Dietterich wonders if the idea of foundation models isn't
             partly about getting funding for the resources needed to build
             and work on them... 'That does smack of flag planting, which
             could have several benefits on the fundraising side.'"
```

```text
URL:         https://www.techbrew.com/stories/2021/08/30/stanfords-foundation-models-workshop-large-language-model-debate-resurfaces
Kind:        secondary — Morning Brew / Emerging Tech Brew reporting (Hayden
             Field), independent outlet.
Establishes: The earliest contemporaneous press coverage found — published
             2021-08-30, 14 days after the report's first posting. Reports
             CRFM's own stated rationale for the name (to emphasize
             "architectural stability, safety, and security," matching the
             report's own §1.1.1 wording) alongside named objections: Meredith
             Whittaker of the AI Now Institute — "They renamed something that
             already had a name; they're called large language models. This
             move constitutes an attempt at erasure"; Emily Bender — "Is
             'Don't' a possible answer here? If academia/gov't says 'don't'
             [use these models], will industry listen?"; Stella Biderman of
             EleutherAI, on the risk of industry-driven suppression of
             inconvenient findings.
Paraphrase:  A second, independent, earlier report confirming the naming
             objection was immediate and came from researchers outside the
             "foundation models are dangerous/unproven" camp as well as
             within it — Whittaker's complaint is specifically that renaming
             an existing category erases prior work, the sharpest documented
             form of the "self-serving" charge.
Locators:    Article body, sections quoting Whittaker, Bender, and Biderman;
             paragraph describing CRFM's stated rationale.
Quote:       "They renamed something that already had a name; they're called
             large language models. This move constitutes an attempt at
             erasure..." — Meredith Whittaker, AI Now Institute.
```

```text
URL:         https://csrc.nist.gov/pubs/sp/800/218/a/final
Kind:        primary — NIST's own publication record for its own document.
Establishes: The term's later, durable standard usage independent of Stanford.
             NIST Special Publication 800-218A, "Secure Software Development
             Practices for Generative AI and Dual-Use Foundation Models: An
             SSDF Community Profile," final, published 2024-07-26. Uses
             "foundation models" in its title and throughout, as an accepted
             technical term in official U.S. government guidance three years
             after the report coined it.
Paraphrase:  By 2024 the term had moved from one institution's coinage into
             standing federal technical guidance, on its own terms, without
             needing the original report's argument re-litigated.
Locators:    Publication metadata page: title, publication date, status field.
Quote:       none needed — a title and a status field are the evidence.
```

```text
URL:         https://www.govinfo.gov/content/pkg/FR-2023-11-01/html/2023-24283.htm
Kind:        primary — the U.S. government's own official text of Executive
             Order 14110, as published in the Federal Register.
Establishes: The term's single clearest entry into binding federal law.
             Executive Order 14110, "Safe, Secure, and Trustworthy Development
             and Use of Artificial Intelligence," signed 2023-10-30, §3(k),
             formally defines "dual-use foundation model": "an AI model that
             is trained on broad data; generally uses self-supervision;
             contains at least tens of billions of parameters; is applicable
             across a wide range of contexts; and that exhibits, or could be
             easily modified to exhibit, high levels of performance at tasks
             that pose a serious risk to security, national economic
             security, national public health or safety..."
Paraphrase:  Two years after the report, "foundation model" was precise and
             standard enough to anchor a legal definition with regulatory
             consequences, not just a description in review articles.
Locators:    §3(k), Definitions.
Quote:       (see Establishes — the full statutory definition)
```

```text
URL:         https://www.presidency.ucsb.edu/documents/executive-order-14148-initial-rescissions-harmful-executive-orders-and-actions
Kind:        primary — archival transcript of Executive Order 14148's own
             text (The American Presidency Project, UCSB; the govinfo.gov PDF
             of the same order did not extract cleanly, so this transcript
             was used to read the operative list).
Establishes: Executive Order 14110 was rescinded. EO 14148, "Initial
             Rescissions of Harmful Executive Orders and Actions," signed by
             President Trump 2025-01-20, lists at item (ggg): "Executive Order
             14110 of October 30, 2023 (Safe, Secure, and Trustworthy
             Development and Use of Artificial Intelligence)."
Paraphrase:  The federal-law citation above was in force for about fifteen
             months, not permanently — a caveat the draft should carry if it
             leans on EO 14110 as evidence the term is now settled law.
Locators:    Rescission list, item (ggg).
Quote:       "(ggg) Executive Order 14110 of October 30, 2023 (Safe, Secure,
             and Trustworthy Development and Use of Artificial Intelligence)."
```

### Contradictions

- The report's own naming rationale claims "foundation" signals "architectural
  stability, safety, and security," in the same breath as its own admission
  that "we do not fully understand the nature or quality of the foundation
  that foundation models provide; we cannot characterize whether the
  foundation is trustworthy or not" (§1.1.1). Marcus and Davis make this
  tension the spine of their objection rather than inventing it: the name
  asserts a property the report itself declines to claim. This is the central
  claim-versus-evidence gap the commission wants shown.

- Marcus and Davis's contemporaneous headcount for who was behind the report —
  "32 faculty and 117 research scientists, postdocs, and students" (149 total)
  — does not match the report's own byline, which lists 114 named authors
  (verified directly against arXiv's structured metadata and the PDF title
  page, identical across v1, v2, and v3). The gap is likely because Marcus and
  Davis are describing the broader CRFM community that "declared" the paradigm
  shift, not literally the report's author list, but no source resolves this,
  so the draft should use the report's own 114 rather than the critics' 149 for
  the author count, and not present the two figures as measuring the same
  thing.

- The naming rationale (report, primary) and the "castles in the air" /
  "flag planting" objections (Malik, Dietterich, primary-quoted-in-secondary)
  disagree on what "foundation" is doing rhetorically: the report frames the
  word as an honest acknowledgment of incompleteness ("itself incomplete but
  serves as the common basis"); its critics read the same word as claiming
  reliability the models have not earned. Both readings cite the same
  sentence: this is a framing dispute, not a factual one, and the draft should
  present it as such rather than adjudicate which reading is "right."

- "The term became standard usage" is true of general technical use (NIST,
  2024) but not uniformly true of its one clear entry into binding law:
  Executive Order 14110 (2023) defined "dual-use foundation model" in federal
  regulation, and Executive Order 14148 (2025) rescinded it. The NIST
  publication is undated for withdrawal as of this research and is the safer
  citation for "became standard"; the executive order pair should be used, if
  at all, as an example of the term reaching regulatory text, not as evidence
  the regulation itself still stands.

### Numbers

```text
Figure: 114 named authors (Rishi Bommasani ... Percy Liang, corresponding author)
Owner:  arXiv structured metadata for 2108.07258, cross-checked against the
        PDF title page (identical author block in v1, v2, and v3)
Scope:  the report's full byline; excludes the ~30 people thanked only in
        Acknowledgments for feedback (not credited as authors)
```

```text
Figure: 211 pages (v1, filed 2021-08-16); 212 pages (v2, filed 2021-08-18);
        214 pages (v3, filed 2022-07-12, current version)
Owner:  arXiv PDFs for each version (pdfinfo page count, corroborated by the
        printed page-214 footer in v3's References section)
Scope:  full document length including references; contemporaneous critics
        (Marcus and Davis, September-October 2021) were reading v2 (212 pages)
```

```text
Figure: 26 sections across 4 parts (Capabilities, Applications, Technology,
        Society), plus Introduction and Conclusion
Owner:  the report itself, §1.4 "Overview of this report" and its table of
        contents
Scope:  the report's self-described structure; no section is a Methods or
        Results section
```

```text
Figure: 0 instances of original-experiment language ("we conducted," "we
        trained," "our experiment," "we ran") found in a full-text search of
        the report
Owner:  full-text search of the arXiv v3 PDF's extracted text
Scope:  whole document; does not prove no such passage exists, but none
        surfaced despite the search terms matching common phrasing for
        reporting a new result
```

```text
Figure: 2023-10-30 to 2025-01-20 (roughly 15 months)
Owner:  Executive Order 14110 (govinfo.gov, Federal Register) and Executive
        Order 14148 (presidency.ucsb.edu), both read directly
Scope:  the period "dual-use foundation model" was a defined term in binding
        U.S. federal executive-branch regulation
```

### Source assets

```text
Asset: Fig. 4, "Paper Roadmap" (arXiv PDF v3, p.13) — a tree diagram showing
       the report's four parts (Capabilities, Applications, Technology,
       Society) branching into their 26 numbered subsections.
Shows: The document's organization is a taxonomy, laid out as literally as a
       diagram can show it — no branch is a results or findings section.
Crop:  Keep the full four-branch tree with all part and section labels and
       numbers legible; omit the page header/footer and surrounding body text.
```

```text
Asset: Fig. 19 (arXiv PDF v3, in §4.5 Systems) — a log-scale plot of model
       parameter/FLOP growth (blue) against GPU memory and throughput growth
       (red) over time.
Shows: The one chart in the report built from external data (Brown et al.
       2020 and GPU spec sheets, per its own caption) rather than anything
       CRFM measured — concrete evidence for "not a measured finding" if the
       piece wants a single image to make that point, since a reader might
       otherwise assume a 214-page report has original data somewhere.
Crop:  Keep both series and the legend; the axis labels and the caption's
       sourcing line are load-bearing for this use and should not be cropped
       away even though the caption itself would sit outside the image.
```

### Discarded

```text
URL: https://venturebeat.com/2021/08/18/foundation-models-risk-exacerbating-mls-ethical-challenges/
     — blocked on every attempt (WebFetch: 403 Forbidden; direct request with
     a browser user agent: 429 Too Many Requests). Not used. Coverage of the
     same period and reception is already established, independently, by the
     Wired and Tech Brew sources above, so nothing appears to have been lost.
```

```text
URL: https://www.aiwiki.ai/wiki/foundation_models — a wiki-style tertiary
     summary with no visible authorship or editorial accountability; not
     opened past the search snippet. Discarded as unsuitable for sourcing any
     claim, primary or secondary.
```

```text
URL: (an earlier automated summary of arxiv.org/abs/2108.07258, and a separate
     automated summary of arxiv.org/pdf/2108.07258) gave author counts of 128
     and 132 respectively. Both are wrong and were discarded once the
     structured arXiv metadata was counted directly (114, see Numbers above).
     Recorded here as a caution: do not trust a fast automated read of this
     document's author list without counting it directly.
```

## Neighbor slugs for the writer to link

From `nb history --library /home/user/library-checkout`, exact published
slugs and titles (link at first use in prose and/or Background band; do not
re-teach their content):

```text
the-evidence/stochastic-parrots · 2026-07-28
  "The slogan 'stochastic parrots' outgrew the argument that coined it"
  (the report's own introduction cites "Bender et al. 2021" — this paper — as
  the "intense scrutiny" foundation models faced even as the report was being
  written; a natural, accurate link point.)

the-evidence/gpt-3-few-shot · 2026-07-19
  "Few-shot GPT-3 beat fine-tuning on a handful of tasks and trailed it on most"
  (GPT-3 is one of the report's three named current examples of a foundation
  model, alongside BERT and CLIP.)

the-evidence/scaling-laws-kaplan · 2026-07-25
  "OpenAI's 2020 scaling paper got the curve right and the budget wrong"

the-evidence/the-bitter-lesson · 2026-07-31
  "Rich Sutton's essay has four examples and zero citations"
```

No other the-evidence neighbor duplicates this report's ground. Tonight's four
other new lessons (the-instruments/tau-bench, the-mechanics/length-control,
what-could-go-wrong/model-collapse, when-ai-breaks/biden-deepfake-robocall)
were not touched by this research and share no claims with it.
