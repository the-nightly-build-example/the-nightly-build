# Editorial review: the-mechanics / speculative-decoding (editor 01)

## Decision

Approved: no required change remains. The draft was sound on substance and
structure; the edits below were mine to make in place, and I made them.

## What I changed, and why

**Slop at edges (deleted, not repaired).**
- Cut the section opener "Start with the part that is not in dispute." from the
  orientation section. It passed nothing the noun test wants: "start with the X
  that is not in dispute" fits any article. The concrete sentence after it (a
  service serving the same weights at two-to-three-times speeds) is the real
  opener, and the settled-vs-open split the desk requires is still marked
  explicitly in the final section ("separate the settled part from the part that
  varies").
- Cut ", and this is the heart of the method" from the sampling paragraph. It
  grades the argument instead of continuing it (the "this is the whole point"
  family). The sentence now states plainly that sampling needs more care, then
  shows exactly why in the next two sentences, which is the earning.

**The worked accept/reject table (brief's focus).**
- Reframed the caption so it reads as an illustration of the mechanism, never as
  measured data. It now opens "A worked example of one target pass..." and closes
  "The token values are illustrative, chosen to show the accept-and-reject rule
  rather than measured from a run." The citation to source 3 (Leviathan) stays:
  the claim the caption rests on is the parallel-pass economics (four tokens for
  one big-model pass), which is source 3's γ+1 result. The greedy match the table
  shows is source 2's argmax rule, taught in the same section.

## Substance verified against evidence.md

Every body claim traces to a source, and each inline number matches the source it
points at:
- Behavior and 2–3x, more on code: source 1 (and 2, 6). Matches.
- One forward pass per token, weight-loading bottleneck: source 2. Matches.
- Parallel γ+1 scoring in one pass, accept-the-run, corrected token, α and the
  expected-tokens formula E = (1−α^(γ+1))/(1−α): source 3. The equation is
  byte-for-byte the source's; the two limits stated in prose (→1 as α→0, →γ+1 as
  α→1) are correct.
- Serving-framework loop (propose / verify batch / commit / resample): source 4
  (vLLM), the partly-paraphrased source. The sentence built on it states only the
  loop the page supports; it asserts no figure or verbatim fact the paraphrase
  does not carry. No change needed.
- Greedy argmax identity: source 2. Sampling accept rule min(1, p/q) and the
  adjusted-distribution resample: source 3. Distribution-preserving guarantee:
  sources 3 (proof) and 5 (DeepMind), both primary; the "identical to vanilla
  decoding" gloss: source 6. The identical-output guarantee therefore rests on
  primary sources.
- Workload split (3–4 vs 6–8): source 6. Provider deploys in the memory-bound,
  low-QPS regime: source 4. Medusa 2.3–3.6x: source 7. EAGLE 2.7–3.5x on a 70B
  chat model, distribution held: source 8. All match.

URLs spot-checked live: the two method papers, both variants, the TGI doc and the
PyTorch guide return 200; the vLLM doc returned a 429 throttle (rate-limited, not
a dead link) and is the researcher's recorded, resolving source.

No claim had to be hedged or cut for want of a source. Nothing in the piece rests
on an unsourced statement, and I invented no source.

## Standards checks

- Headline behavior-first, subject-verb, concrete, no colon subtitle. Dek adds the
  mechanism and the burstiness without restating the speed claim, and carries none
  of the three banned molds (no semicolon reversal, no suspended question, no comma
  triad).
- Section headings are four differently-built steps (an appositive, one "and"
  pairing, a "word for word" tag, a "rides on" phrase); none is a scaffolding slot
  and none is the retired "How far the explanation reaches" shape.
- Three-part lesson shape intact (Why this matters / body / The takeaway). The body
  closes on a fact (EAGLE's numbers), not a verdict restatement; the takeaway lands
  the judgment. The "not Y" lines in the note and takeaway each correct a real,
  named misconception (draft substitutes for target; provider choice vs model
  property; "faster by making it dumber"), so they earn their place.
- No banned terms, no em-dashes. Neighbors (prefill-and-decode, first-token-latency)
  are linked in Background, not re-taught or numbered.

## Proof

`nb check --series the-mechanics`: verdict PUBLISHABLE, 0 BLOCK, 0 WARN. Word count
in band. (Final stamped figures recorded in the article's nb-meta.)
