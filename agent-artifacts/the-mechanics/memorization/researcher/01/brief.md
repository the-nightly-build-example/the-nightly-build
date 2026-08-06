# researcher brief: the-mechanics/memorization (01)

Inputs:
- ../../editorial-direction.md — citation standard, series territory, declared reader
- ../../commission.md — the exact subject, angle, and required contribution

Output: ./evidence.md

Primary sources to read firsthand:
- Carlini, Tramèr, Wallace, et al., "Extracting Training Data from Large Language
  Models" (2021, arXiv 2012.07805) — read the actual extraction results from
  GPT-2 (how many verbatim sequences, what kinds, the role of duplication).
- Carlini, Ippolito, Jagielski, et al., "Quantifying Memorization Across Neural
  Language Models" (2023, arXiv 2202.07646) — read the quantified relationships:
  memorization increases with model scale, with duplication of the example, and
  with context length. Record the actual reported figures.
- Lee et al. "Deduplicating Training Data Makes Language Models Better" (2021,
  arXiv 2107.06499) — read the finding that deduplication reduces verbatim
  emission, to support the "duplication drives it" mechanism.
- A concrete real-world regurgitation case with a citable record: the New York
  Times v. OpenAI complaint (Dec 2023) exhibits showing verbatim regurgitation,
  and/or the "Scalable Extraction of Training Data from (Production) Language
  Models" work (Nashville/Carlini et al. 2023, the "poem poem poem" ChatGPT
  extraction). Read what was actually shown and the numbers.

Verify: every memorization figure (fraction memorized, duplication thresholds,
scale relationship) against its owning primary. Note where models do NOT emit
verbatim (most content is generalized) so the article frames memorization as
partial and driven, not total. Put any disagreement (e.g. what counts as
"memorization," or disputes over the NYT extraction methodology) in Contradictions.

Distinguish clearly for the writer: memorization (string stored in weights) vs
retrieval (external lookup at query time) vs hallucination (fabrication). The
record should make the boundaries traceable.

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Primary = the party that owns the claim (the study's authors; the court filing).

Environment: fetches go through a proxy; on 403/paywall retry with a
browser-style request first, and record each source's own canonical URL.

Sanity check: the full published the-mechanics slug list is in the commission's
Boundaries. Do not build the record around a duplicate angle.
