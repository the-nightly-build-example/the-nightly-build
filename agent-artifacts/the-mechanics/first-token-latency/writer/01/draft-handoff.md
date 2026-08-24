# writer draft handoff: the-mechanics/first-token-latency (01)

## Original work

The lesson puts Anyscale's ~1% input-vs-output regression next to Vaswani's per-layer O(n^2 * d) versus O(n * d^2) split to draw the actual crossover at which the "attention is quadratic" story starts to describe the pause a chatbot user feels, then folds DistServe's colocation interference, Sarathi's chunked-prefill / TTFT-for-TPOT trade, Leviathan's decode-only speculative speedup, Kwon et al.'s PagedAttention prefix sharing, and the Anthropic/Artificial Analysis network-latency caveat into one account of what any TTFT figure is a sum of. That composition is what the evidence record, on its own, does not do.

## Proof result

Final `nb check` (with links, series the-mechanics, library /home/user/library-checkout):

- BLOCK: 0
- WARN: 0
- verdict: PUBLISHABLE

No warnings intentionally left. All eleven source URLs resolve.

## Open questions

- The 32K / 122,880-token TTFT figures (472 ms, ~2.2 s) reach the article through Wallace/Redis relaying an NVIDIA developer benchmark on GH200 NVL32 running Llama 3.1 70B. Source 5 is filed as `secondary` and its `data-nb-note` names NVIDIA as the underlying primary owner. If the argument's long-context regime needs a first-hand primary rather than a secondary relay, the researcher should be routed back for the underlying NVIDIA developer post; the piece would then swap source 5's kind and URL and keep the same numbers.
- No other open evidence or voice questions.
