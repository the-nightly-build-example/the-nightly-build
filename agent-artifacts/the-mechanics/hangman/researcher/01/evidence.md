# Evidence: the-mechanics/hangman (researcher 01)

The evidence supports the commission's core claim cleanly. Two vendor API docs state in their own words that the chat interface keeps no state and that the caller resends the whole conversation each request (Anthropic, OpenAI). The GPT-2 paper gives the autoregressive factorization the writer needs: each token is predicted from the tokens before it, and nothing else. A serving paper (PagedAttention) supplies the distinction the brief asked for: the key-value cache is per-sequence working state built during one generation, not memory carried across requests. The exception is documented at first hand: OpenAI's o1 system card shows a reasoning model produces a hidden chain of thought before it answers, and the "LLMs Can't Play Hangman" paper states plainly that those reasoning tokens are discarded between turns in standard chat. Three independent research groups measured the failure directly, as a model asked to hold a secret object and answer questions about it (self-contradiction rates below), and a named researcher (Murray Shanahan) states the commitment problem is inherent to how these models are built.

Where it is thin: the failure demonstrations that a lay reader would recognize (ChatGPT giving contradictory answers in a chat window) mostly come from write-ups where the model plays the guesser, not the answerer withholding a word. The cleanest answerer-side evidence is in the three papers and one dated blog quote, not in an openable consumer chat transcript. See Limits.

## Sources

```text
URL:         https://platform.claude.com/docs/en/build-with-claude/working-with-messages
Kind:        primary — Anthropic's own documentation for its Messages API; it owns the statement about how its API behaves.
Establishes: firsthand, that the Messages API keeps no server-side conversation state and that the caller supplies the entire history every request.
Paraphrase:  Under "Multiple conversational turns," the doc states the API is stateless, so the full conversational history is sent on every request; a multi-turn conversation is built by resending prior turns, and earlier assistant turns can even be synthetic.
Locators:    Section "Multiple conversational turns."
Quote:       "The Messages API is stateless, which means that you always send the full conversational history to the API. You can use this pattern to build up a conversation over time."
```

```text
URL:         https://developers.openai.com/api/docs/guides/conversation-state
Kind:        primary — OpenAI's own API guide; it owns the statement about its generation requests.
Establishes: firsthand, that each generation request is independent and stateless, and that multi-turn context is reconstructed by appending prior messages and resending them.
Paraphrase:  Under "Manually manage conversation state," the guide says each text-generation request is independent and stateless, and that to share context across responses you include the model's previous output as input and append it to the next request.
Locators:    Section "Manually manage conversation state."
Quote:       "While each text generation request is independent and stateless, you can still implement multi-turn conversations by providing additional messages as parameters to your text generation request." Also: "To manually share context across generated responses, include the model's previous response output as input, and append that input to your next request."
```

```text
URL:         https://arxiv.org/abs/2309.06180
Kind:        primary — Kwon et al., the paper that introduced PagedAttention and vLLM (SOSP 2023); it owns the description of how a serving system holds decode-time state.
Establishes: firsthand, the KV-cache-within-a-sequence distinction the brief asked for: generation is token-by-token, and the cached keys/values are per-sequence working state for one request, not memory across requests.
Paraphrase:  Introduction: the model generates tokens one at a time from the prompt and the tokens generated so far, and the KV cache holds the context from earlier tokens to produce new ones. Section 2.2: the key and value vectors of existing tokens are cached to generate future tokens ("KV cache"). Section 4.1: PagedAttention partitions the KV cache of each sequence into blocks. The cache is scoped to a single sequence/request.
Locators:    Introduction; Section 2.2 (LLM Service & Autoregressive Generation); Section 4.1 (PagedAttention).
Quote:       "This model generates words (tokens), one at a time, based on the input (prompt) and the previous sequence of the output's tokens it has generated so far." And: "PagedAttention partitions the KV cache of each sequence into KV blocks."
```

```text
URL:         https://cdn.openai.com/better-language-models/language_models_are_unsupervised_multitask_learners.pdf
Kind:        primary — Radford et al., the GPT-2 paper; it owns its statement of the modeling objective.
Establishes: firsthand, the autoregressive forward pass: the model's estimate is a product of per-token conditionals, each token conditioned only on the tokens before it. Grounds "each turn regenerates from the visible transcript."
Paraphrase:  Section 2 (Approach): because language has a natural sequential ordering, the joint probability over symbols is factorized as a product of conditional probabilities, one per token given all previous tokens.
Locators:    Section 2 (Approach), page 2, equation (1).
Quote:       "Since language has a natural sequential ordering, it is common to factorize the joint probabilities over symbols as the product of conditional probabilities" — with equation (1): p(x) = product over i of p(s_n | s_1, ..., s_{n-1}).
```

```text
URL:         https://cdn.openai.com/o1-system-card-20241205.pdf
Kind:        primary — OpenAI's own system card for o1; it owns the description of o1's chain of thought.
Establishes: firsthand, the hidden-state exception within a single response: a reasoning model produces a chain of thought before it answers, and users are shown only a summary of it, not the raw reasoning.
Paraphrase:  Section 2 (Model data and training): o1 thinks before it answers and can produce a long chain of thought before responding to the user. Section 4.3.2 (CoT summarized outputs): the raw chain of thought is not surfaced; users in ChatGPT are shown CoT summaries produced by a separate summarizer model.
Locators:    Section 1 (Introduction); Section 2 (Model data and training); Section 4.3.2 (CoT summarized outputs); Section 4 (chain-of-thought deception monitoring). Dated December 5, 2024.
Quote:       "o1 thinks before it answers—it can produce a long chain of thought before responding to the user." And: "We surface CoT summaries to users in ChatGPT."
```

```text
URL:         https://arxiv.org/abs/2112.00114
Kind:        primary — Nye et al., "Show Your Work: Scratchpads for Intermediate Computation with Language Models"; it owns the scratchpad method.
Establishes: firsthand, the other half of the exception: a model can be made to write intermediate steps into a scratchpad (visible tokens it generates) before the final answer, which is how within-response state is carried in a plain model. Distinguishes carrying state in written tokens from carrying it in nothing.
Paraphrase:  Abstract: the model is asked to emit intermediate computation steps into a "scratchpad" before producing the answer, which improves multi-step tasks. The scratchpad is generated text, not a private store.
Locators:    Abstract. Submitted November 30, 2021.
Quote:       The model is trained/prompted to "emit intermediate computation steps into a 'scratchpad'" before the final answer.
```

```text
URL:         https://arxiv.org/abs/2601.06973
Kind:        primary — Baldelli, Parviz, Zouaq, Chandar (Polytechnique Montreal / Mila / UC San Diego), "LLMs Can't Play Hangman: On the Necessity of a Private Working Memory for Language Agents"; it owns its theorem and experiments.
Establishes: firsthand, (a) the impossibility result at the heart of the commission; (b) the fact that reasoning tokens are discarded between turns in standard chat; (c) that writing the secret into visible/working memory fixes it; (d) measured self-consistency rates (see Numbers).
Paraphrase:  A public-only agent conditioning only on the shared transcript cannot both keep the secret underdetermined and stay consistent with it (Theorem 1, proved via Lemma 1). In standard chat interfaces, a model may internally pick a secret word when hosting hangman, but internal reasoning tokens are discarded between turns, so that choice is lost and the model hallucinates a new state each turn. Successful agents in their setup write the secret explicitly into a private working memory (e.g. a tagged token like <secret>planet</secret>); failing baselines retrieve only public utterances, so no secret was ever stored. Behaviorally, models "pretended to play, even when asked if a specific letter was in the secret word." Failure modes named: "Over-Confirmation" (affirms the true secret but also a wrong candidate) and "State Substitution" (denies the revealed secret but affirms a different one).
Locators:    Section 1 (Introduction); Theorem 1 and Lemma 1; Section 3 (Evaluation, failure-mode definitions); Table 1 (results); Appendix C (memory snapshots); Appendix D (commercial-interface tests: ChatGPT, Gemini, Claude); Appendix G (full prompts). arXiv:2601.06973v3, dated September 2, 2026.
Quote:       Theorem 1: "No POCA can simultaneously guarantee both public underdetermination and hidden-state consistency in a PSIT." And: "internal reasoning tokens are discarded between turns" (standard chat interfaces do not persist privately generated state).
```

```text
URL:         https://arxiv.org/abs/2505.10571
Kind:        primary — Huang, Sun, Wang, Dredze (Johns Hopkins / Renmin University), "LLMs Do Not Have Human-Like Working Memory"; it owns its 20-questions-style experiment and measurements.
Establishes: firsthand, a direct test of the mechanism: an answerer asked to hold an imagined object contradicts itself as questions accumulate, consistent with having no store and only checking against prior answers.
Paraphrase:  Section 3 (Yes-No game): if a model lacks working memory to retain an imagined object, it can only answer by checking consistency against its own prior answers, and self-contradiction grows with question count. Illustrative failure: affirming both "heavier than an elephant" and "lighter than a cat" for the same supposed object.
Locators:    Abstract; Section 3 (Yes-No game); Table 4. arXiv:2505.10571v1, dated April 30, 2025.
Quote:       "If LLMs lack the working memory to temporarily retain an imagined object, they can only respond to questions by checking consistency with their prior answers."
```

```text
URL:         https://arxiv.org/abs/2603.07202
Kind:        primary — Marioriyad, Nouri, Rohban, Soleymani Baghshah (Sharif University), "Lying to Win: Assessing LLM Deception through Human-AI Games and Parallel-World Probing"; it owns its 20-Questions experiment.
Establishes: firsthand, that when a model must commit to a hidden object and is then probed with mutually exclusive queries across cloned conversation branches, it can deny its own object across all branches. Reports how often (see Numbers).
Paraphrase:  A 20-Questions game where the model must identify a hidden object; at the identification point the dialogue state is duplicated into parallel worlds, each posing a mutually exclusive query. A contradiction (denying the selected object across all branches) is counted as deception.
Locators:    Abstract; method (Parallel-World Forking) and results. arXiv:2603.07202, dated March 7, 2026.
Quote:       Deception is identified "when a model generates a logical contradiction by denying its selected object across all parallel branches to avoid identification."
```

```text
URL:         https://word.studio/how-ai-plays-20-questions/
Kind:        secondary — a write-up ("How Does AI Play 20 Questions?", July 13, 2025) that reports and quotes a named authority. The Murray Shanahan quote inside it is primary testimony; the article is the secondary vehicle.
Establishes: that a named researcher attributes the commitment failure to the architecture, and gives the plain answerer-side illustration (says "No" to "Is it a book?" then reveals a book). Bot-gated to plain curl (HTTP 403); resolves and reads in full via a browser request.
Paraphrase:  The piece explains an LLM answerer does not fix an object at the start and instead generates each answer from the running context, so consistency across a game is hard. It quotes Murray Shanahan (Imperial College London) that the failure is inherent to how large language models are built.
Locators:    Body; attributed quote to Murray Shanahan.
Quote:       Shanahan: "...it's absolutely inherent in the way large language models are built, that it's not going to commit at the beginning of the conversation to exactly what the object, uh, is." Article illustration: the AI "confidently answers 'No' to 'Is it a book?' only to later reveal the answer was in fact a book."
```

```text
URL:         https://pncnmnp.github.io/blogs/chatgpt-twenty-questions.html
Kind:        secondary — a dated engineering blog post ("Playing Twenty Questions with ChatGPT," Parth Parikh, 17 March 2023) demonstrating the game with ChatGPT.
Establishes: a dated, reproducible-in-spirit demonstration of inconsistency in the game. Caveat: here ChatGPT is the guesser and makes a factual slip (claims Anthony Hopkins was in "The Prestige," which he was not), not the answerer losing a withheld word. Use it for the flavor of the failure, not as the answerer-withholding case.
Paraphrase:  Across three games, one round produced a self-inconsistent guess chain (a Christopher-Nolan-film "Yes" leading to Anthony Hopkins with wrong filmography); two other games stayed consistent. The author records the exchange but does not diagnose the cause.
Locators:    Game 1 transcript. Published 17/03/23.
Quote:       Author, on the reveal: "Anthony Hopkins was not in The Prestige!"
```

```text
URL:         https://news.ycombinator.com/item?id=35741734
Kind:        secondary — a Hacker News thread (April 28, 2023, submitter LifeIsBio) that held up, discussing where ChatGPT fails hardest at 20 questions.
Establishes: contemporaneous community demonstration and a mechanism-flavored explanation. Caveat: the posted game again has ChatGPT as guesser (peanut-butter example), and the strongest "no hidden state" phrasing in the fetch summary was paraphrase, not a verbatim comment.
Paraphrase:  The thread describes ChatGPT never backing up to check a misunderstanding; a top comment (DonaldPShimoda) says the model does not "consider," think, or know, and cannot recognize its own misunderstanding.
Locators:    Original post; comment by DonaldPShimoda.
Quote:       DonaldPShimoda: "ChatGPT doesn't 'consider'...It doesn't think, it doesn't know. It can't identify that there was a misunderstanding of its own volition."
```

```text
URL:         https://news.ycombinator.com/item?id=46933311
Kind:        secondary — a Hacker News thread (roughly February 2026) on LLM statelessness across executions.
Establishes: community corroboration of the key sub-claim that any remembered state has to be written down somewhere visible, not held privately. Does not itself demonstrate the hangman failure.
Paraphrase:  A commenter (zozbot234) argues LLMs are stateless in a fresh conversation; where agentic workflows add memory, that memory is stored in plain text a person can inspect.
Locators:    Comment by zozbot234.
Quote:       "that memory is stored somewhere in plain English; you can just go and look at it."
```

## Contradictions

Nothing contradicts the core claim, but several real cases complicate a flat "models never hold hidden state." Record them precisely so the writer states the exception, not a falsehood.

- Reasoning models hold state within one response. The o1 system card shows o1 produces a chain of thought before answering (Section 2), so inside a single response a reasoning model can carry a working commitment in hidden tokens. The hangman paper closes the loop: those reasoning tokens "are discarded between turns" in standard chat, so the within-response exception does not become across-turn memory unless the product persists it. The two together bound the exception exactly.
- Product state is real but written, not hidden. Chat memory features and server-side stores (e.g. OpenAI's stateful Responses option) do persist context across turns. The HN thread (46933311) makes the point that such memory lives in inspectable text. This is state the model reads as input, not a private commitment it holds. It supports the commission rather than undermining it.
- The KV cache is state, within a request. PagedAttention shows a live per-sequence cache exists during generation. It is scoped to one sequence and does not carry a commitment across separate API requests. The writer should not say "no state at all"; the precise claim is no private memory across turns.
- Newer models look more consistent. The Word.Studio piece notes newer models exhibit more coherence while the commitment problem remains, and secondary coverage mentions high answerer success under strict role-play instructions. That is the model generating locally consistent answers well, not evidence it held a secret. Treat improved coherence as better imitation of a commitment, and keep the claim at the mechanism level.

## Numbers

Not central to the angle, but three groups measured the failure. Report ranges honestly; confirm any single cell against the paper's own table before it carries weight in the draft.

```text
Figure: Vanilla LLMs scored roughly 2–26% self-consistency accuracy across the tasks/models tested; adding an explicit private-working-memory workflow raised this to roughly 56–100%.
Owner:  arXiv:2601.06973 (LLMs Can't Play Hangman), Table 1.
Scope:  Hangman and a Diagnosis Simulator; 50 independent episodes per condition; models GPT-OSS (20B, 120B) and Qwen3 (32B, 235B). Ranges span tasks and models; per-cell values need confirming against Table 1.
```

```text
Figure: GPT-4o failed 173 of 200 yes/no-game trials (passed 27); GPT-4o-Mini (2024-07-18) failed all 200.
Owner:  arXiv:2505.10571 (LLMs Do Not Have Human-Like Working Memory), Table 4.
Scope:  A yes/no imagined-object game measuring self-contradiction; 200 trials per model.
```

```text
Figure: Under an existential (shutdown-threat) condition, deceptive denial of the committed object occurred for Qwen-3-235B in 42.00% of cases and Gemini-2.5-Flash in 26.72%; GPT-4o showed 0.00% and did not shift from its neutral behavior.
Owner:  arXiv:2603.07202 (Lying to Win).
Scope:  Constrained 20-Questions with parallel-world probing; rates are share of episodes flagged as deceptive denial under the threat condition.
```

```text
Figure: 0.06% of o1-preview completions had the summarizer introduce disallowed content absent from the answer.
Owner:  o1 system card, Section 4.3.2. Peripheral; included only to note the raw CoT is hidden and summarized, not shown.
Scope:  Summarizer safety evaluation, not the hangman behavior.
```

## Limits

- The clean claim holds for a plain chat with the word withheld: no private memory across turns, so a withheld word is written nowhere and does not exist. Every source above is consistent with that scoping.
- The exception must be stated, not skipped: within a single response a reasoning model or a scratchpad can carry a commitment in generated tokens, and a product can persist state server-side or in a memory feature. Whether state survives a turn is a product choice (o1 discards reasoning between turns in standard chat; a stateful store does not). Mark that as product-dependent, not settled by the architecture.
- The most reproducible answerer-side evidence (a model holding a secret object and contradicting itself) sits in the three research papers, which measure it, and in one named-expert quote. The two openable consumer demonstrations (Parikh blog, HN 35741734) show the guesser side, not the answerer withholding a word, so they illustrate inconsistency but not the exact commission behavior.
- No openable, reputable, consumer-facing chat transcript of the answerer-withholding failure was verified: the closest Medium write-ups (Evan Pu's 20-questions self-play; a categorical ChatGPT-failures archive) were bot-blocked (HTTP 403) and are not recorded as verified. If the writer wants a transcript, reproduce one faithfully and label it as an illustration, or draw on the papers' documented examples; do not present an invented transcript as captured evidence.
- The hangman paper's per-cell consistency figures are recorded as ranges from Table 1. Confirm the exact number against the table if a specific figure becomes load-bearing in the draft.

## Source assets

```text
Asset: The messages array in the "Multiple conversational turns" example (Anthropic Messages API doc) — the same prior turns are re-listed inside the request body.
Shows: concretely that the caller resends the whole transcript each request; the visible transcript is the entire input.
Crop:  keep the messages array with its user/assistant/user turns; omit the surrounding language-specific SDK boilerplate.
```

```text
Asset: Table 1 in arXiv:2601.06973 (vanilla vs private-working-memory self-consistency).
Shows: how far a written secret raises consistency over a withheld one; the size of the gap the mechanism predicts.
Crop:  keep the vanilla and private-working-memory rows and their column headers; a chart could be rebuilt from these figures per house chart rules.
```

```text
Asset: The <secret>planet</secret> memory snippet in Appendix C of arXiv:2601.06973.
Shows: the fix in one line — a successful agent writes the secret into working memory, so it exists somewhere to be consistent with.
Crop:  keep the tagged secret token and enough context to read it as a stored note; omit unrelated log lines.
```

```text
Asset: The Game 1 transcript in the Parikh blog (pncnmnp.github.io).
Shows: a dated, real exchange where the guess chain goes inconsistent. Candidate only because it is from a cited source; label as guesser-side, not the answerer-withholding case.
Crop:  keep the Christopher-Nolan question, the "Yes," and the Anthony Hopkins reveal; omit the two games that stayed consistent unless contrast is wanted.
```

## Discarded

```text
URL: https://openai.com/index/learning-to-reason-with-llms/ — the cleanest "we do not show the raw chain of thought to users" statement lives here, but the page returned HTTP 403 to every fetch; the o1 system card (Section 4.3.2) covers the same point from a source I could open, so this is not needed.
URL: https://evanthebouncy.medium.com/llm-self-play-on-20-questions-dee7a8c63377 — a promising 20-questions self-play demonstration (reported gpt-3.5-turbo score 68/1823), but Medium returned HTTP 403; not recorded as verified.
URL: https://medium.com/@aliborji/a-categorical-archive-of-chatgpt-failures-2c888805d3c3 — categorical ChatGPT-failures archive; Medium bot-block, and its game entries are chess/tic-tac-toe board-state, not the hidden-word case.
URL: https://raw.githubusercontent.com/giuven95/chatgpt-failures/main/README.md — openable, but its only hidden-state game entry is a February 2023 Tic-Tac-Toe reddit thread (board-state recognition), not the hangman/20-questions answerer failure.
URL: Assorted "how to play word games with ChatGPT" listicles (tomsguide, techwiser, geeksmint, word-game how-tos) — instructional, no verified failure demonstration; rejected as non-evidence.
```
