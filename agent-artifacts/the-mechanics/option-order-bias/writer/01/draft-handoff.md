# Draft handoff: the-mechanics/option-order-bias (writer/01)

## Original work
The article assembles the evidence record's scattered candidate causes into one
ordered walk from the behavior down to bedrock — sequence position, the prior on
the A/B/C/D label tokens, and the scoring probe that reads the answer — and
stages Zheng's and Pezeshkpour's contradiction as a side-by-side of positions, so
the reader can see that the effect is settled while its decomposition is not; the
record lists these pieces and their disagreement but never composes them into a
single causal account.

## Proof
`./nb check .nb-work/the-mechanics/option-order-bias/library/the-mechanics/option-order-bias.html --series the-mechanics --library /home/user/library-checkout`
→ BLOCK: 0, WARN: 0, verdict PUBLISHABLE (links included). `nb stamp` run before
the final check: words 2189, reading 10 min, sources 9 (8 primary, 1 secondary).
No warnings intentionally left.

## Handling of the round's focus
- The two-mechanism split is presented as openly disputed, not resolved: Liu +
  Pezeshkpour own the position account, Zhao + Zheng own the token-prior account,
  and the two headline papers are set as adjacent position cards with a marking
  note ("The behavior is settled. Its decomposition is not.").
- The scoring probe is carried as a real third step (Robinson's MCSB framing, the
  first-token-vs-text mismatch from Wang and the "My Answer is C" group, the HF
  three-implementations table), not a footnote.
- prompt-sensitivity is linked (Background + body), not re-taught; word-order and
  instructions-are-data are linked as taught ground in prose, not numbered.

## Fetch-flagged figures re-verified before quoting
- HF blog LLaMA-65B (0.636 / 0.637 / 0.488) and the "not at all comparable" line —
  re-fetched and confirmed.
- Wang et al. mismatch rates (Gemma-7b 56.8%, Llama2-7b 51.4%, Mistral-7b 10.2%) —
  re-fetched from the HTML and confirmed.

## Open evidence question (non-blocking)
- The "My Answer is C" (s8) per-model mismatch figures could not be re-verified
  against a rendered page; I used only its abstract-level "over 60%" aggregate,
  which is confirmed. If a per-model number from that paper is wanted in the body,
  the researcher would need to extract its Table 4 from the PDF.
