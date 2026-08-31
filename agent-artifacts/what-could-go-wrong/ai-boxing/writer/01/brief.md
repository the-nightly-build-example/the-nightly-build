# writer brief: what-could-go-wrong/ai-boxing (01)

Inputs:
- ../../editorial-direction.md — house standard, press voice, lesson identity, series direction
- ../../commission.md — the argument, the sharp line, source policy, nb-meta values, habits not to inherit
- ../../writing-coach/01/voice-guide.md — how this piece should sound
- ../../researcher/01/evidence.md — the complete claim set; use its Numbers section exactly
- the initialized article: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/ai-boxing/library/what-could-go-wrong/ai-boxing.html
- template context: /home/user/the-nightly-build/.nb-work/what-could-go-wrong/ai-boxing/.nb-context/

Output: draft-handoff.md (in this directory), plus the edited article.

Proof: from repo root /home/user/the-nightly-build run
  ./nb check .nb-work/what-could-go-wrong/ai-boxing/library/what-could-go-wrong/ai-boxing.html --series what-could-go-wrong
  (iterate with --no-check-links, then `nb stamp` and the full check until BLOCK: 0.)

This round's focus — the line the evidence forces (see evidence limitation and Contradictions):
- Steelman correctly. The original texts are NOT doom: Armstrong-Sandberg-Bostrom
  conclude an Oracle AI "might be safer than unrestricted AI" and that
  superintelligence "may turn out to be potentially survivable." The faithful
  argument is that boxing is necessary but not sufficient, not that it is futile.
  Do not build a doom strawman to knock down.
- The persuasion-out-of-the-box claim's entire evidence base is anecdotal by its
  own author's admission, with no released transcripts. Per the fullest
  first-person record (Tuxedage), the AI won only a handful of AI-box games ever
  and gatekeepers win as the norm. Present it as contested and thin, not as a
  demonstrated result.
- Every recorded "escape" or "self-exfiltration" (Apollo, the OpenAI o1 system
  card, the Anthropic Claude 4 card) was staged inside a sandbox with the goal,
  the knowledge, and the escape route supplied by researchers; Apollo itself calls
  the scenarios "toy." Separate, each time, what the system did from what the
  setup supplied.
- Do not quote Superintelligence directly (its chapter 9 was read via a
  secondary). Source the substantive containment claims to Armstrong-Sandberg-
  Bostrom 2012, which Bostrom co-authored and the researcher read in full.
- Distinguish and link, don't re-litigate: what-could-go-wrong/the-off-switch,
  /self-replication, /deceptive-alignment. Name no company as an authority. The
  takeaway bookend lands the judgment; no Verdict block at the body's close.

nb-meta: harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
series `what-could-go-wrong`, slug `ai-boxing`. Dek must match the rendered
dekline exactly. Only the two bookends address the reader.
