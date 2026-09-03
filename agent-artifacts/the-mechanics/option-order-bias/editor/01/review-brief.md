# editor review-brief: the-mechanics/option-order-bias (01)

Inputs (read the voice guide first; open evidence when the first read calls for
it; open the draft-handoff original-work sentence only at the third read):
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/editorial-direction.md
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/commission.md
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/writer/01/brief.md
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/writing-coach/01/voice-guide.md
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/researcher/01/evidence.md
  - .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/writer/01/draft-handoff.md
  - .nb-work/the-mechanics/option-order-bias/library/the-mechanics/option-order-bias.html  (the article)
  - .nb-work/the-mechanics/option-order-bias/.nb-context/

Output: .nb-work/the-mechanics/option-order-bias/agent-artifacts/the-mechanics/option-order-bias/editor/01/editorial-review.md
Proof (the orchestrator stamps and checks after your edits; new prose returns to the writer):
  ./nb check .nb-work/the-mechanics/option-order-bias/library/the-mechanics/option-order-bias.html --series the-mechanics --library /home/user/library-checkout

This round's focus:
- The settled-vs-open reckoning is the heart of the piece: the effect is robustly
  measured, but Zheng and Pezeshkpour disagree on which mechanism dominates.
  Confirm the draft leaves that decomposition openly disputed and does NOT let one
  mechanism (position, label-token prior, or scoring probe) stand as the sole
  cause. The scoring probe (first-token/option-ID probability, which disagrees
  with the generated answer >50% on some models) must read as a real third cause,
  not a footnote.
- Verify the headline swing figures (Zheng +15/-12 points; Pezeshkpour 13-75%
  best-worst gap) against the owning primary. The "My Answer is C" per-model
  mismatch numbers were not re-verifiable — confirm the draft uses only the
  abstract-level "over 60%" aggregate, not an unverified per-model figure.
- prompt-sensitivity is a published sibling lesson — confirm it is linked, not
  re-taught; this piece is positional/label bias among presented options.
- Reach-ground check: the piece should stop at a step below which nothing changes
  the answer, and mark which steps are settled engineering vs open.

## Recent-pattern notes (compare edges, headings, dek, furniture against these)
- Dek molds recurring in the library: the "credited with X, but Y had already done
  it" reversal and the "the [term] now used far more loosely" tag; plus the
  spec/headlines.md-banned semicolon reversal, suspended question, and comma triad.
- Why-this-matters: the "This lesson opens/reads ..." opener and the "By the end
  you will be able to explain X, Y and Z" list formula recur — flag if present.
- The mechanics desk defaults to a short declarative "reveal" first heading, and
  pieces keep closing on a stamped present-tense one-liner — flag either if built
  to a prior article's pattern. Vary heading construction.
- Four siblings ship tonight (mixture-of-experts, task-time-horizon, algorithmic-
  collusion, clearview-ai); this piece owns the mechanism, not metric design.
