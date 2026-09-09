# Evidence: the-mechanics / speculative-decoding

Gathered from primary papers and official serving-framework docs, plus two
careful explainers. Every URL below was opened and confirmed to load (200 or a
readable page) on 2026-09-09. github.com is blocked in this environment, so no
source resolves to GitHub. Each entry: kind, publisher · title, resolving URL,
and the specific fact(s) it supports, with the exact quoted passage.

Numbering matches the article's Sources list (order of first citation in the
body).

---

## S1 — primary (official serving-framework doc)
**Hugging Face · Text Generation Inference — "Speculation"**
https://huggingface.co/docs/text-generation-inference/conceptual/speculation

Supports: the behavior (same model, same output, 2–3x faster), why it works
(LLMs are memory bound), and that the gain is workload-dependent.

- Quote: "The idea is to generate tokens *before* the large model actually runs,
  and only *check* if those tokens where valid."
- Quote: "So you are making *more* computations on your LLM, but if you are
  correct you produce 1, 2, 3 etc.. tokens on a single LLM pass. Since LLMs are
  usually memory bound (and not compute bound), provided your guesses are correct
  enough, this is a 2-3x faster inference (It can be much more for code oriented
  tasks for instance)."
- Quote: "Speculative decoding, assisted generation, Medusa, and others are a few
  different names for the same idea."

## S2 — secondary (careful explainer)
**Hugging Face · "Assisted Generation: a new direction toward low-latency text
generation"** — Joao Gante, 2023-05-11
https://huggingface.co/blog/assisted-generation

Supports: one forward pass per token; the forward pass is the slow, memory-bound
step; the candidate-and-validate loop; the accept-the-matching-run rule; identical
output to greedy; 2x–3x latency numbers.

- Quote: "running a model forward pass for large models is slow, and you may need
  to do hundreds of them in a sequence."
- Quote: "the bottleneck in the forward pass comes from loading the model layer
  weights into the computation cores of your device, not from performing the
  computations themselves."
- Quote (loop): "Use greedy decoding to generate a certain number of candidate
  tokens with the assistant model, producing `candidates`... Using our model, do
  a forward pass with `candidates`, obtaining `logits`."
- Quote (accept run): "Compare `next_tokens` to `candidates` and get the number
  of matching tokens... after the first mismatch, all candidates are
  invalidated."
- Quote (identical output): "if you pass the generated sequence as input and
  apply the argmax operator to the resulting logits, you will obtain the
  generated sequence back."
- Quote (numbers): "Gets up to 3x speedups in the presence of INT8 and up to 2x
  otherwise, when the model fits in the GPU memory."

## S3 — primary (method paper, the distribution-preserving guarantee)
**arXiv (Leviathan, Kalman, Matias — Google) · "Fast Inference from Transformers
via Speculative Decoding"**, 2022/2023 (ICML 2023 oral)
https://arxiv.org/abs/2211.17192
Full text opened at: https://ar5iv.labs.arxiv.org/abs/2211.17192

Supports: the core method (run the target in parallel over the draft's outputs);
the accept/reject rule for greedy and sampling; the proof the target's
distribution is preserved; γ+1 parallel evaluations; the "free" extra token; the
acceptance rate α and the expected-tokens formula.

- Quote (abstract): the method uses "speculative execution and a novel sampling
  method" to "make exact decoding from the large models faster, by running them
  in parallel on the outputs of the approximation models, potentially generating
  several tokens concurrently," "without changing the distribution," "with
  identical outputs."
- Quote (speedup): "a 2X-3X acceleration compared to the standard T5X
  implementation" (T5-XXL).
- Quote (sampling accept/reject): "we instead sample x∼q(x), keeping it if
  q(x)≤p(x), and in case q(x)>p(x) we reject the sample with probability
  1−p(x)/q(x) and sample x again from an adjusted distribution
  p′(x)=norm(max(0,p(x)−q(x)))." (p = target, q = draft.)
- Quote (guarantee): "for any distributions p(x) and q(x), and x sampled in this
  way, indeed x∼p(x)." (Appendix A.1 proof.)
- Quote (parallel scoring): the target M_p is run in parallel over
  "M_p(prefix), …, M_p(prefix+[x₁,…,x_γ])", i.e. "γ+1 concurrent evaluations of
  M_p"; when all γ drafts are accepted, one additional token is produced from the
  target's own distribution (up to γ+1 tokens per run).
- Quote (acceptance rate + expected tokens): α is "the probability of accepting
  x_t∼q(x_t|x<t) by speculative sampling"; the expected number of tokens per run
  is E(# generated tokens) = (1−α^(γ+1))/(1−α), "a capped geometric variable,
  with success probability 1−α and cap γ+1."

## S4 — primary (official serving-framework doc)
**vLLM · "Speculative Decoding"** (documentation)
https://docs.vllm.ai/en/latest/features/speculative_decoding/

Supports: how it is deployed and chosen by the provider; draft proposes, target
verifies by rejection sampling; same output distribution; memory-bound / low-QPS
regime.

- Quote: "This document shows how to use Speculative Decoding with vLLM to reduce
  inter-token latency under medium-to-low QPS (queries per second), memory-bound
  workloads."
- Mechanism (paraphrased from the page): a smaller draft model proposes multiple
  candidate tokens, the larger target model verifies them via rejection sampling,
  accepted tokens advance generation and rejected ones trigger resampling, all
  while maintaining the same output distribution as standard decoding.

## S5 — primary (method paper, sampling variant + proof)
**arXiv (Chen, Borgeaud, Irving, Lespiau, Sifre, Jumper — DeepMind) ·
"Accelerating Large Language Model Decoding with Speculative Sampling"**, 2023
https://arxiv.org/abs/2302.01318

Supports: parallel scoring of a draft's short continuation; the modified
rejection sampling that preserves the target distribution; 2–2.5x on a 70B model
without changing sample quality.

- Quote (method): "parallel scoring of short continuations, generated by a faster
  but less powerful draft model," combined with "a novel modified rejection
  sampling scheme which preserves the distribution of the target model."
- Quote (guarantee): "a novel modified rejection sampling scheme which preserves
  the distribution of the target model within hardware numerics."
- Quote (speedup): "a 2-2.5x decoding speedup in a distributed setup" on
  Chinchilla (70B), "without compromising the sample quality."

## S6 — secondary (careful explainer / production report)
**PyTorch (IBM) · "A Hitchhiker's Guide to Speculative Decoding"**, 2024-11-13
https://pytorch.org/blog/hitchhikers-guide-speculative-decoding/

Supports: guess-and-check within a single forward pass; output identical to
vanilla decoding; production 2x/3x numbers; the provider chooses configuration
(how many speculative heads), and the gain rides on guesses being right.

- Quote: "Speculative decoding is an optimization technique for inference that
  makes educated guesses about future tokens while generating the current token,
  all within a single forward pass. It incorporates a verification mechanism to
  ensure the correctness of these speculated tokens, thereby guaranteeing that
  the overall output of speculative decoding is identical to that of vanilla
  decoding."
- Quote (production numbers): "we... observed 2x speedup on language models –
  Llama3 8B, Llama2 13B, and IBM Granite 7B and 3x speedup on IBM's Granite 20B
  code models."
- Quote (provider config / workload): "for language models, we find 3-4 heads
  works well in practice, whereas we found that code models can reap benefits
  from 6-8 heads." And: "if the speculator is not accurate with more heads, it
  will result in wasted compute increasing the latency and reducing the
  throughput."
- Quote (why memory helps): "if we get 3 tokens lookahead correct, we have saved
  three round trip times on HBM."

## S7 — primary (later variant)
**arXiv (Cai, Li, Geng, Peng, Lee, Chen, Dao) · "Medusa: Simple LLM Inference
Acceleration Framework with Multiple Decoding Heads"**, 2024
https://arxiv.org/abs/2401.10774

Supports: a refinement that drops the separate draft model for extra heads on the
target; tree-based verification; speedups without quality loss.

- Quote (method): adds "extra decoding heads to predict multiple subsequent
  tokens in parallel" and uses "a tree-based attention mechanism" to "construct
  multiple candidate continuations and verify them simultaneously in each
  decoding step."
- Quote (speedup): "Medusa-1 can achieve over 2.2x speedup without compromising
  generation quality, while Medusa-2 further improves the speedup to 2.3-3.6x."

## S8 — primary (later variant)
**arXiv (Li, Wei, Zhang, Zhang) · "EAGLE: Speculative Sampling Requires
Rethinking Feature Uncertainty"**, 2024
https://arxiv.org/abs/2401.15077

Supports: a variant that drafts at the feature (hidden-state) level; preserves the
generated text's distribution; 2.7x–3.5x on a 70B chat model.

- Quote (method): "autoregression at the feature (second-to-top-layer) level is
  more straightforward than at the token level," resolved by "incorporating a
  token sequence advanced by one time step."
- Quote (speedup + guarantee): for LLaMA2-Chat 70B, "a latency speedup ratio of
  2.7x-3.5x, doubled throughput, while maintaining the distribution of the
  generated text."

---

## Cross-checks against the primary papers (as instructed)

- **Identical-output guarantee.** Confirmed in three independent places: Leviathan
  proves x∼p(x) under the accept/resample rule (S3, App. A.1); Chen states the
  modified rejection sampling "preserves the distribution of the target model
  within hardware numerics" (S5); PyTorch states the output "is identical to that
  of vanilla decoding" (S6). For greedy decoding the guarantee is the argmax
  identity in S2.
- **Accept/reject mechanics.** Greedy: accept a drafted token while it equals the
  target's argmax, and discard everything after the first mismatch (S2). Sampling:
  accept with probability min(1, p(x)/q(x)); on rejection, resample from
  norm(max(0, p−q)) (S3). The target scores all γ+1 positions in one parallel
  pass and yields one bonus token when every draft is accepted (S3).
- **What sets the speedup.** The acceptance rate α governs it; expected tokens per
  target pass = (1−α^(γ+1))/(1−α) (S3). α is workload-dependent ("much more for
  code" S1; 3–4 vs 6–8 heads for language vs code S6) and the provider chooses
  whether and how to deploy it (S4).

## Notes / limits
- No claim in the draft rests on anything not quoted above.
- The Hugging Face Transformers "Generation strategies" page was opened but its
  current version no longer carries a speculative-decoding section, so it is NOT
  cited. The TGI conceptual doc (S1) is used for the serving-framework view
  instead.
- vLLM's mechanism sentences (S4) are paraphrased from the rendered page rather
  than block-quoted; the memory-bound/low-QPS sentence is an exact quote.
