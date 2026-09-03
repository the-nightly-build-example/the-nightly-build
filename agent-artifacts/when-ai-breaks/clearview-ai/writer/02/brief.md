# writer brief: when-ai-breaks/clearview-ai (02) — revision

Inputs:
  - .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/editor/01/editorial-review.md — the required work to apply
  - .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/researcher/02/evidence.md — the new source for the Court-of-Appeal-permission fact
  - .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/researcher/01/evidence.md — the standing evidence record
  - .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/writing-coach/01/voice-guide.md
  - .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/editorial-direction.md
  - .nb-work/when-ai-breaks/clearview-ai/library/when-ai-breaks/clearview-ai.html — the article to edit in place (carries the editor's 01 direct edits)

Output: .nb-work/when-ai-breaks/clearview-ai/agent-artifacts/when-ai-breaks/clearview-ai/writer/02/draft-handoff.md

Proof: ./nb check .nb-work/when-ai-breaks/clearview-ai/library/when-ai-breaks/clearview-ai.html --series when-ai-breaks --library /home/user/library-checkout
       (iterate with --no-check-links; run the full command, links included, to BLOCK: 0 before handoff)

Apply exactly these required items; preserve all other settled work (including the
editor's 01 edits):
1. The "Court of Appeal permission to appeal" sentence: re-cite it to the new
   source in researcher/02 (Ashfords LLP case note — a SECONDARY source; add it as
   a new source with data-nb-kind="secondary" and drop the old citation 9 from
   this sentence). The source gives the grant date as 19 December 2025 and reports
   it as a procedural fact, NOT attributed to the Commissioner — so drop or restate
   the draft's "According to the Commissioner" framing accordingly. Keep the
   finding-of-unlawfulness vs enforcement distinction intact.
   (If you prefer, the editor noted the paragraph stands without this sentence —
   but since it is now sourced, keeping it re-cited is fine.)
2. Reconcile the Dutch fine date: the chart gives May 2024 (decision) and the table
   gives Sep 2024 (announcement). Make the two consistent, or label each clearly
   (decision vs announcement) so they no longer read as a contradiction. Use the
   dates the evidence record supports; do not invent one.

Do not introduce new claims beyond researcher 01+02. Re-run the complete proof to
BLOCK: 0. In draft-handoff, add one line per required item resolved and note any
warning intentionally left. Confirm nb-meta still has date 2026-09-03, harness
claude-code-routine, model claude-opus-4-8; re-stamp before the final check if
counts changed.
