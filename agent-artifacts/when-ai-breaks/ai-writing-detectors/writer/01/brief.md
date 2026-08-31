# writer brief: when-ai-breaks/ai-writing-detectors (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the incident, boundaries, source policy, nb-meta values, habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- the initialized article: /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-writing-detectors/library/when-ai-breaks/ai-writing-detectors.html
- template context: /home/user/the-nightly-build/.nb-work/when-ai-breaks/ai-writing-detectors/.nb-context/

Output: draft-handoff.md (in this directory), plus the edited article.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/when-ai-breaks/ai-writing-detectors/library/when-ai-breaks/ai-writing-detectors.html --series when-ai-breaks
  (iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.)

This round's focus — precision the evidence forces (see evidence limitation and Contradictions):
- Do not conflate the two operators' responses. OpenAI FULLY WITHDREW its own AI
  Classifier (July 20 2023; it had reported 26% true-positive / 9% false-positive).
  Turnitin did NOT withdraw: it caveated (an asterisk on documents under 20% AI, a
  later admission of about a 4% sentence-level false-positive rate) but kept
  selling the detector. Say each precisely.
- The harsh false-positive figures are sample-specific and must be labeled as
  such: Liang et al.'s 61.22% is on non-native-English TOEFL essays; the
  Washington Post's ~50% is its own small test. Neither is Turnitin's general or
  document-level rate. Do not present them as one.
- Turnitin launched the detector in April 2023 claiming under 1% false positives.
  Sadasivan et al. give a theoretical limit on reliable detection and show
  paraphrasing defeats detectors. Vanderbilt disabled the tool on Aug 16 2023.
- Where perplexity/statistical-signature teaching is needed, link the existing
  lesson the-instruments/perplexity rather than re-teaching it.
- Some owning pages (OpenAI's post, turnitin.com) are 403-gated; their figures are
  cross-verified in the evidence via independent sources. Cite the owning page as
  the address; a gated page that resolves does not block the link check. No
  individual student is named in the record (source paywalled) — do not invent one.

nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
series `when-ai-breaks`, slug `ai-writing-detectors`. Dek must match the rendered
dekline exactly. Only the two bookends address the reader; no Verdict block at the
body's close.
