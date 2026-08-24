# editor review-brief: the-mechanics/first-token-latency (01)

Inputs: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editorial-direction.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/commission.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writer/01/brief.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writing-coach/01/voice-guide.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/researcher/01/evidence.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writer/01/draft-handoff.md
        .nb-work/the-mechanics/first-token-latency/library/the-mechanics/first-token-latency.html
        .nb-work/the-mechanics/first-token-latency/.nb-context/
Output: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editor/01/editorial-review.md

Recent-pattern notes:

- Why cards recently opened with "You have read that..." / "You keep hearing
  that..." shapes.
- Why cards recently closed on "By the end you will know what A, B, C, and D."
- Why cards recently narrated themselves with the "this lesson [verb]" formula.
- Takeaways recently resolved with "The question was whether..." and closers
  built as "That is real, and it is what X."
- Headlines recently paired two independent clauses with a comma and "and."
- Deks: cut the comma-triad closed with "and," the semicolon reversal, and the
  suspended "...the real question is whether."

This round's focus:

- The-mechanics forbids code; confirm there is none (inline nb-math equations
  are allowed furniture, not code).
- The 32K→122,880-token TTFT figures (472 ms → ~2.2 s) reach the article
  through Wallace/Redis relaying an NVIDIA developer benchmark; source is filed
  secondary with a data-nb-note naming NVIDIA. Confirm the note is present and
  the number is not presented as first-hand. If you judge a first-hand primary
  necessary for a central claim, route the researcher back for the NVIDIA post;
  if the claim is adequately supporting-not-central, the relayed source stands.
- Verify the two precisions stay honest: "quadratic in n" is quadratic only
  above the O(n·d²) crossover (the article contrasts O(n²·d) and O(n·d²)), and
  the "decode is smooth" claim is qualified for colocation. Check the article
  does not overclaim n² as the felt cause at ordinary prompt lengths.
