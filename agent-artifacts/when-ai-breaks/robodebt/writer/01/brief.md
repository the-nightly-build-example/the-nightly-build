# writer brief: when-ai-breaks/robodebt (01)

Inputs:
- editorial-direction.md — house standard, this paper's voice, the when-ai-breaks prompt, template identity.
- writing-coach/01/voice-guide.md — how this lesson should sound, with exemplar passages.
- researcher/01/evidence.md — the complete claim set: figures by denominator, contradictions, source kinds.
- The initialized article at library/when-ai-breaks/robodebt.html and its .nb-context/ contract.

Output: writer/01/draft-handoff.md

Proof: ./nb check .nb-work/when-ai-breaks/robodebt/library/when-ai-breaks/robodebt.html --series when-ai-breaks --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --series is required in local mode; use --no-check-links while iterating, links included until BLOCK: 0)

Set nb-meta the engine cannot compute: date 2026-08-10, harness claude-code-routine, model
"Claude Opus 4.8", and tags ["government", "automation", "welfare"]. nb stamp writes the counts.

Precision points the evidence requires; the draft must respect them:
- The failure is income averaging plus the reversed burden of proof, not "automation" alone. The earlier
  manual program already used averaging and the reversed onus; removing the human check (a per-file
  compliance-officer review, roughly 20,000 files a year) scaled the error rather than creating it. Do not
  reduce the lesson to "the algorithm did it."
- Handle harm with restraint and to the record. The Royal Commission assigns no death toll and is explicit
  that causation is case-specific; the most-cited death (Rhys Cauzzo) arose from the manual-but-averaged
  process, not the automated scheme. Do not write "the algorithm killed people" or imply a body count.
- Do not enlist the 2017 Ombudsman report as an early finding of illegality; it did not find the scheme
  unlawful and was used by the department as cover. The lawfulness findings are Prygodicz (2021) and the
  Royal Commission.
- Use figures with their denominators, exactly as the evidence separates them (people versus debts versus
  dollars asserted versus recovered versus written off versus the settlement). Confirm any figure in display
  text against the evidence record's owning-primary entry.
- Sourcing caveat: the evidence was read through Internet Archive captures of the documents' own canonical
  URLs because direct fetches were blocked; cite the documents' own pages (as the evidence records them). The
  Amato holding is cited from the government and Royal Commission documents that reproduce it, not a judgment
  text; if you use the 2025 Knox settlement figure, attribute it to the government release and note it was
  subject to court approval.

Recent habits to break (from when-ai-breaks and the house record; the voice guide does not carry these):
- Do not build a run of parallel anaphora headings (tesla's "The car that... / The car that...").
- The where-it-lives-today section is required content; do not copy "The same gap, in the cars on the road
  now" (tesla) or "When the label is a proxy" (optum). Name it in Robodebt's own nouns.
- Do not reach for the headline molds "recalled X for letting Y" (tesla) or the comma-and reveal (optum).
  Find Robodebt's own surprise.
- Do not open the takeaway on a bare restated definition or "Two things are true." Resolve the opener.
