# Draft handoff: the-mechanics / speculative-decoding

Article HTML (filled in place):
`.nb-work/the-mechanics/speculative-decoding/library/the-mechanics/speculative-decoding.html`

## Proof status
- `nb stamp`: words=1691, reading_minutes=7, sources=8.
- `nb check ... --series the-mechanics`: **0 BLOCK, 0 WARN, verdict PUBLISHABLE.**
- Word band 1200–2200: 1691, comfortably inside (aim was ~1600–1900).
- Sources: 8 total, 6 primary, 2 secondary (floor 8/4/1 met).

## Headline and dek
- Title: "The same open model returns identical text two to three times faster on one service"
- Dek (nb-meta and rendered dekline are byte-identical): "A small draft model guesses the next few tokens and the big model checks them all in a single pass, so the words that would have come one at a time arrive in bursts."
- Habit checks: behavior-first (kept). No semicolon-reversal, no suspended question, no comma-triad in the dek. No final section named "How far the explanation reaches". Heading construction varied (a definitional clause, an "and" pairing, a "word for word" phrase, a "rides on" phrase).

## Structure (body first, bookends last)
Body = fixed `orientation` + 3 flex sections (flex band 0–4):
1. `orientation` — "One model, one token per pass, is the speed the fast service beats." Defines *token* and *forward pass* plainly; establishes the one-pass-per-token bottleneck and that the cost is memory-bound. Cites 1, 2.
2. `draft-and-verify` — "A small model guesses ahead, and the big model checks every guess in one pass." The trick + the accept-the-run rule + the worked table (5 guesses over "Water boils at 100": 3 kept, 1 corrected, 1 discarded → 4 tokens per target pass). Explains the burstiness. Cites 3, 2, 4.
3. `same-output` — "The checked text is the target's own, word for word." Greedy argmax match; the sampling accept/resample rule; the distribution-preserving proof; an "In plain language" note that the trick cannot change what the model says. Cites 2, 3, 5, 6.
4. `what-sets-the-speedup` — "How much faster rides on how often the guess is right." Acceptance rate α, the expected-tokens equation E = (1−α^(γ+1))/(1−α) as a bare display equation, workload dependence (code vs prose), provider choice, settled-vs-open split, and the Medusa/EAGLE variants. Cites 3, 1, 6, 4, 7, 8.

Bookends written after the body: `why` sets up the three questions (why faster, why output is unchanged, why the gain varies); `takeaway` resolves all three and closes on the "faster by making it dumber is exactly backward" landing. Neither carries citations (apparatus, per template).

## Furniture used (three pieces, each earning its place)
- One `nb-table` — the worked accept/reject example, the spine of the lesson.
- One `nb-note` ("In plain language") — states the no-quality-change guarantee.
- One `nb-math` bare display equation — the expected-tokens formula the speedup argument leans on, cited in the surrounding prose (source 3).
No charts (none warranted; none committed under spec/charts.md).

## Citation map (numbered in order of first appearance)
1 HF TGI docs · Speculation (primary) — behavior, memory-bound, 2–3x, more on code.
2 HF Assisted Generation blog (secondary) — one pass per token, weight-loading bottleneck, greedy match rule, argmax identity.
3 Leviathan et al. / Google (primary) — parallel γ+1 scoring, accept/resample rule + proof, α and expected-tokens formula, bonus token.
4 vLLM docs (primary) — deployment loop, memory-bound/low-QPS regime, provider choice.
5 Chen et al. / DeepMind (primary) — modified rejection sampling preserves the target distribution.
6 PyTorch/IBM blog (secondary) — output identical to vanilla decoding, production 2x/3x, 3–4 vs 6–8 heads (workload).
7 Medusa (primary) — extra decoding heads, 2.3–3.6x.
8 EAGLE (primary) — feature-level drafting, 2.7–3.5x, distribution preserved.

Every body section carries at least one citation; bookends carry none. Source order matches first-cite order (no W-CITE-ORDER).

## Neighbors linked, not re-taught
- Background rows link `prefill-and-decode` (why the reply phase is the slow, one-token-at-a-time job) and `first-token-latency` (what a forward pass costs). Both as plain prose links, not numbered sources, per press editorial.
- Did not re-teach attention, tokenization, or sampling from scratch; sampling is defined in one clause at the point of use.

## House-standard checks
- Banned terms: none over limit (no "machinery", "revolutionary", "transformative", "game-changing", "ai-race"; "leverage" not used). Em-dashes: 0.
- Slop edges tested: no empty closers, no invented negative-parallelism, no unearned punchlines. The one "not Y" construction in the takeaway ("a choice the provider makes, not a property of the model") corrects a real, named misconception the lesson set up.
- `<code>` reserved for none needed; literal token strings ("degrees", "sea") sit in the worked table, not inline code, since they are illustrative words rather than strings to type.

## Open items / caveats for the editor
- vLLM's mechanism sentences (source 4) were paraphrased from the rendered doc; only the memory-bound/low-QPS clause is a verbatim quote. Everything cited to source 4 is supported by the page as read.
- The worked-table numbers ("Water boils at 100" → degrees/Celsius/at/sea) are an illustrative construction of the accept/reject mechanism, not lifted from a source; the mechanism they illustrate (kept run, one correction, discard rest, γ+1 positions in one pass) is sourced to 3 and 2.
- Nothing in the draft rests on an unsourced claim.
