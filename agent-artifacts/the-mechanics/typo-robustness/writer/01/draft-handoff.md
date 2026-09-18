# Draft handoff: the-mechanics/typo-robustness (writer round 01)

## Original work

The evidence only juxtaposes a tension it never resolves — the folk
assumption that training data is typo-laden against Alahmari 2025's own
description of LLM training sets as "curated datasets that lack
human-induced errors, such as typos" — and the article resolves it by
grounding meaning-preservation in BPE's frequency-based merge rule instead:
a misspelling's surviving fragments ("ne", "ccess", "ary") are common,
well-trained pieces by construction, regardless of whether that exact
misspelling ever appeared in training, which lets the piece argue robustness
without leaning on the contested "typos are common in training data" premise
the evidence itself complicates.

## Proof result

`nb stamp` then the exact brief command with links included:

```
BLOCK: 0
WARN:  0
verdict: PUBLISHABLE
```

No warnings were intentionally left; the final run is clean (words: 2200,
sources: 11, reading_minutes: 10).

## Open questions

- None blocking. One judgment call worth the editor's eyes: I did not use
  the GPT-2 (50,257) or cl100k_base (100,277) vocabulary-size figures from
  the evidence record — they were true but not load-bearing for the
  argument, and cutting them helped hold the piece inside the 1200-2200 word
  band alongside the required tiktoken worked example and the settled/open
  material. If the editor wants either figure back in, something else will
  need to come out to stay in band.
- The piece treats Belinkov & Bisk 2018 (NMT, 2017-era models) as evidence
  only that subword systems carry no designed typo defense, not as evidence
  about modern chat-model robustness itself, per the record's own caution.
  Worth a second look that this line wasn't blurred anywhere.
