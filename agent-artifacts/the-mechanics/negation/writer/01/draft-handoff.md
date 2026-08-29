# Draft handoff: the-mechanics/negation (01)

## Original work

The article joins two findings the researcher's sources measured separately and
never connect — masked language models flipping from 100% to 0% true-completion
preference when "not" is inserted (Ettinger), and CLIP retrieval barely moving
when caption words are shuffled (Yuksekgonul) — into one claim that a single
weakness (negation is rare in training text and weakly rewarded by the
prediction objective) surfaces in a token-prediction system and a text-encoder
system, while explicitly demoting the generated "no elephant" case to a sound
inference rather than a measured rate and dating the crisp text failure to
masked and early autoregressive models.

## Proof result

`./nb check ... --series the-mechanics --library /home/user/library-checkout`
(full run, links included): **BLOCK: 0, WARN: 0, verdict PUBLISHABLE.**
Stamped words 1994, reading 9 min, sources 8 (6 primary, 2 secondary; policy
asks min 8 / >=4 primary / >=1 secondary). No warning left standing.

## Evidence-record constraints honored

- The image-side numbers are labeled as discriminative (retrieval/MCQ)
  measurements; the generated-image failure is presented as an inference from
  the shared CLIP-style encoder, with an explicit sentence that it is not a
  measured generation-failure statistic (section "An image model reads the
  prompt as a bag of words").
- The training-data imbalance is presented as the authors' explanation, not a
  counted corpus frequency, in both the "The training data almost never says no"
  section and the settled-list in the final section.
- The text half is dated: the crisp failure is located in masked/early
  autoregressive models, the instruction-tuning counter-current (Truong: RTE-neg
  0.525 -> 0.767; FLAN-T5-XXL beating base GPT-3; the authors' own note that
  newer chat models may already beat the paper) is stated, and the weakness is
  located in data + the prediction objective, not architecture (balanced-corpus
  learnability, 0.2 -> 1.0 after fine-tuning). The inverse-scaling caveat is kept.

## Open questions

None. No researcher request, voice-guide ambiguity, or commission decision is
outstanding.
