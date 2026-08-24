# writer brief: the-mechanics/first-token-latency (01)

Inputs: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/editorial-direction.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writing-coach/01/voice-guide.md
        .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/researcher/01/evidence.md
        .nb-work/the-mechanics/first-token-latency/library/the-mechanics/first-token-latency.html   the initialized article; edit it in place
        .nb-work/the-mechanics/first-token-latency/.nb-context/   effective template contract, runtime assets, and furniture catalogs
Output: .nb-work/the-mechanics/first-token-latency/agent-artifacts/the-mechanics/first-token-latency/writer/01/draft-handoff.md
Proof:  ./nb check .nb-work/the-mechanics/first-token-latency/library/the-mechanics/first-token-latency.html --series the-mechanics --library /home/user/library-checkout

Recent habits to break (paper-wide, from the last several published lessons; the
voice guide names no prior article):

- Why cards keep opening by telling the reader what they have heard ("You have
  read that...", "You keep hearing that..."). Open on this lesson's particulars.
- Why cards keep closing on "By the end you will know what A, B, C, and D."
  Avoid that enumeration.
- Why cards keep narrating themselves ("This lesson builds/lays out..."). Address
  the reader without the "this lesson [verb]" frame.
- Takeaways keep resolving with "The question was whether..." and closers built
  as "That is real, and it is what X." Avoid both.
- Headlines keep pairing two independent clauses with a comma and "and." Vary the
  construction.
- Deks: avoid the comma-triad closed with "and," the semicolon reversal, and the
  suspended "...the real question is whether."

Outline: derive this piece's sections from the behavior-to-cause chain, not the
near-fixed arc recent lessons run.

This round's focus: the record's Contradictions sharpen the commissioned angle
without breaking it. "Attention is quadratic" is quadratic in n only above the
crossover with the O(n·d²) feed-forward term; for today's d it sits at
multi-thousand tokens. At ordinary prompt lengths the pause comes from
constants and queueing more than visibly from n². Anyscale's Llama 2 70b
measurement: an extra input token costs about 1% of an output token in end-to-
end latency at prompts under a few thousand tokens. "Decode is smooth" holds
inside one request in isolation but breaks under colocation: DistServe measures
that a fresh prefill inserted into a running decode batch inflates TPOT for
every streaming user; chunked prefill (Sarathi/Sarathi-Serve) trades TTFT for
TPOT to soften that; speculative decoding accelerates decode without touching
prefill; prompt caching / PagedAttention KV sharing can collapse the pause on
repeated prompts. Report the Redis-relayed 32K→123K TTFT numbers with their
attribution and their status; if you need the underlying NVIDIA benchmark as a
first-hand primary, route back for it. This is the-mechanics: NO CODE. Link
prefill-and-decode, autoregressive-generation, and attention in Background for
shared machinery rather than re-teaching it.
