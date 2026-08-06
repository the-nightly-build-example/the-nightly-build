# editor review-brief: the-mechanics/memorization (editor/01)

Inputs:
- ../../editorial-direction.md — house standard, paper voice, lesson identity, series prompt
- ../../writer/01/brief.md — the exact writer brief (check for instruction leakage)
- ../../writing-coach/01/voice-guide.md — the craft standard for this article
- ../../researcher/01/evidence.md — the evidence record (open as an opponent)
- ../../writer/01/draft-handoff.md — original-work sentence + proof notes
- ../../library/the-mechanics/memorization.html — the article to review
- ../../.nb-context/ — effective template contract, runtime assets, furniture catalogs

Proof (writer owns proof; you run nb stamp after direct cuts):
./nb check .nb-work/the-mechanics/memorization/library/the-mechanics/memorization.html --series the-mechanics --library /home/user/library-checkout

This round's focus:
- Every memorization figure MUST be tied to its definition — the "how much"
  swings ~four orders of magnitude (0.00000015% unprompted k-eidetic to ≥1%
  prompted-extractable) on the definition alone. Confirm no bare percentage
  appears without its definition and scope. Check the definition-dependence table
  against the evidence Numbers block.
- Framing: verbatim output is REAL but PARTIAL and often adversarially provoked,
  not routine. Confirm OpenAI's rebuttal ("rare bug," manipulated prompts) is
  represented fairly. Confirm the piece says "more copies → steadily more likely,"
  NOT a hard "duplication threshold."
- Boundary teaching: confirm memorization (in-weights) is kept distinct from
  retrieval (query-time external lookup) and hallucination (fabrication), with
  retrieval/hallucination/gradient-descent linked as Background, not re-taught.
  The NYT in-weights-vs-Bing-fetched split is the concrete boundary demonstration
  — judge whether prose suffices or an asset would carry it better (writer's open
  question; request the asset only if it genuinely earns its place).
- Verify the load-bearing figures against evidence: Lee dedup ~10x (a C4 sentence
  repeated >60,000x); Carlini 2023 ≥1% of The Pile for 6B GPT-J, +19 points per
  10x scale; GPT-2's 604 examples; ChatGPT "poem" attack (>10,000 for ~$200, >5%
  verbatim). Confirm none of the discarded/fabricated figures appear.
- Recent-pattern notes: headline must NOT open with "A chatbot"; vary section
  headings away from comma-and pairs. No code in the article.

Decision: approve only when no publication-blocking issue remains. Record the
review at ../../editor/01/editorial-review.md.
