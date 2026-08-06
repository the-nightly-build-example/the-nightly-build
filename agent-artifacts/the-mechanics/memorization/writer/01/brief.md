# writer brief: the-mechanics/memorization (01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../commission.md — subject, angle, required contribution, boundaries
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the complete set of claims available to you
- ../../library/the-mechanics/memorization.html — the initialized article to edit (relative to workspace root)
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Output: ./draft-handoff.md (and the edited article HTML)

Proof: ./nb check .nb-work/the-mechanics/memorization/library/the-mechanics/memorization.html --series the-mechanics --library /home/user/library-checkout
(run from /home/user/the-nightly-build; --no-check-links while iterating, then full command with links until BLOCK: 0)

Decisions the inputs do not carry:
- Frame verbatim output as REAL but PARTIAL and often adversarially provoked, not
  routine. OpenAI's on-record rebuttal calls regurgitation "a rare bug" and says
  the NYT used manipulated/lengthy prompts and cherry-picked (while conceding
  duplication drives it). Represent that pushback fairly (it is in Contradictions).
- Do NOT say "the duplication threshold" — the literature reports a log-linear
  relationship, not a hard cutoff. Say "more copies → steadily more likely."
- Every memorization figure MUST be tied to its definition. "How much has a model
  memorized" swings ~four orders of magnitude (0.00000015% unprompted k-eidetic to
  ≥1% prompted-extractable) purely on the definition. Never print a bare
  percentage without its definition and scope.
- Strong, verified numbers to build on: Lee dedup cuts verbatim emission ~10x (a
  C4 sentence repeated >60,000x); Carlini 2023 — 6B GPT-J memorizes ≥1% of The
  Pile, +19 points per 10x model size (R²=99.8%), 2-5x more within a family;
  GPT-2's 604 memorized examples; the ChatGPT "poem"-divergence attack (>10,000
  examples for ~$200, >5% of output verbatim). Use these exactly.
- The NYT complaint separates in-weights memorization (old articles, paras 98-107)
  from query-time retrieval via Bing (a post-cutoff Oct 2023 article, paras
  108-114). Use this as the concrete asset for the memorization-vs-retrieval
  boundary the commission requires.
- Do not print the discarded/unverified figures (the researcher flagged a
  WebFetch-summarizer fabrication "33% at 50 tokens vs 65% at 450" — it is NOT in
  the paper; never use it).
- nb-meta: date 2026-08-06; harness "claude-code-routine"; model set to the model
  you are actually running on. `nb stamp` writes counts.
- Recent habits to break: do NOT open the headline with "A chatbot"; let the
  headline state the mechanism finding. Vary headings away from comma-and pairs.
- Link, do not re-teach: retrieval (RAG, query-time external lookup — the opposite
  of in-weights memorization), hallucination (fabrication — distinct from emitting
  real stored text), and gradient-descent (how weights are fit) are prior
  the-mechanics lessons; link as Background. No code.
