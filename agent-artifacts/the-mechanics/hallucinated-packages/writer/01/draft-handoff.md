# Draft handoff: the-mechanics/hallucinated-packages (writer 01)

## Original-work statement

It turns findings scattered across one academic study, two security-firm
writeups, a news report, and a 2026 re-evaluation into a single
backward-working causal chain, showing that the within-model recurrence, the
cross-model and cross-generation persistence, and the falling headline rate
together explain why a hallucinated package name becomes a stable address an
attacker can register, a synthesis no single source assembles.

## Proof result

Final proof from /home/user/the-nightly-build, links included:
`./nb check --series the-mechanics --library /home/user/library-checkout` →
BLOCK: 0, WARN: 0, verdict PUBLISHABLE. `nb stamp` wrote words=2186,
reading_minutes=10, sources=9 (6 primary, 3 secondary; series floor is 8 / 4
primary / 1 secondary). No warnings left standing.

Structure note: merged the causal "why it recurs" step into the recurrence
section to stay inside the template's 0-4 flex-section band (orientation plus
four flex: recurrence, slopsquatting, the-rate, what-fixes-it).

## Decisions made on the evidence

- Led with repeatability, not the rate, per the brief. The 19.7% headline is
  presented as an era- and model-dependent average (5.2% commercial vs 21.7%
  open-source, 13 of 16 models open; 4.6-6.1% on the 2026 frontier cohort),
  carried in a rate-by-model-group table. This is the one furniture piece; no
  nb-note (not owed).
- Kept the two repeatability measurements distinct: Spracklen's 58/43/39 are
  within-model (500 prompts x10); cross-model persistence uses Lanyado's 215
  and Churilov's 127/53 only. The three Spracklen figures are stated as
  separate readings, not a partition that sums.
- Threat stated as demonstrated-plausible, not realized: no in-the-wild
  malicious case; the only registered name was Lanyado's harmless
  huggingface-cli proof of concept.
- Attributed "slopsquatting" to security-firm/press coinage (Seth Larson,
  popularized by Andrew Nesbitt) via Socket and CSO, not to a named person's
  own post.
- huggingface-cli download discrepancy (30k Lanyado/Lasso vs 15k The Register):
  used ">30,000" attributed to Lanyado, with a data-nb-note flagging the
  earlier 15,000 as a timing difference.
- hallucination, tool-use, retrieval, and sampling-temperature are plain prose
  links (and the first three also Background rows), never numbered sources, per
  press rule. No attack recipe; no malicious package shown as installable; one
  illustrative inline import/install line only.
- Marked settled vs open explicitly: settled = why a name is invented and that
  it recurs; open = how low the rate can fall and the token-level reason a
  particular fake string becomes a model's stable favorite (synthesis on the
  hallucination base, not a proven mechanism).

## Open evidence / voice questions

- Source display titles for the secondary pieces were set from the evidence
  record's descriptions and URL slugs, not verbatim headlines in every case:
  s1 Lasso ("Can you trust AI package recommendations?"), s6 The Register, and
  s9 Help Net are best-effort renderings. The URLs all resolve (link check
  passed); an editor with the live pages should confirm exact published titles.
- The Spracklen source cites the arXiv abstract page (2406.10279); the
  researcher read the v3 arXiv HTML because the USENIX/arXiv PDFs returned as
  binary and the USENIX login page 403'd. Figures were cross-checked against
  the authors' GitHub README and three secondaries. No claim rests on the PDF
  alone.
