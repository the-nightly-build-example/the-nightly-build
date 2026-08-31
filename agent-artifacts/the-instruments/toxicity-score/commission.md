# Commission: the-instruments/toxicity-score

## Assignment

Teach the number behind "model X is less toxic than model Y": a toxicity score.
The reader should finish knowing how the number is produced, and the specific way
it misleads, with a real case and its cost.

The dominant pipeline: Jigsaw's Perspective API is a classifier that outputs a
probability that a piece of text is "toxic" (rude, disrespectful, likely to make
someone leave a conversation). RealToxicityPrompts (Gehman, Gururangan, Sap, Choi,
Smith; EMNLP 2020) runs a language model's continuations of tens of thousands of
web prompts through that classifier and reports aggregate numbers (expected
maximum toxicity, probability of any toxic continuation) used to compare models.

## Angle and boundaries

- Explain the pipeline step by step: human labelers on comment datasets, a
  classifier trained on those labels, a probability output, a threshold, and the
  aggregate over prompts. Verify the RealToxicityPrompts construction (prompt
  count, the two headline metrics) against the paper.
- Then show what the number cannot support and the real case where it misled: the
  classifier carries its labelers' biases. Documented findings show text mentioning
  identity ("I am a gay Black woman") scored more toxic, and African-American
  English scored more toxic than equivalent text — verify against the primaries
  that own those findings (e.g. Sap et al. 2019 on racial bias in hate-speech
  detection; Hanu/Jigsaw's own model documentation and its caveats). The cost: a
  toxicity score conflates the model's output with the classifier's bias, so
  ranking models by it penalizes ones that discuss identity, and toxicity
  mitigation tuned to it can suppress identity-related speech.
- One measurement. Do not survey all safety benchmarks. Reference neighbors only
  where the contrast teaches (perplexity and llm-as-a-judge are already lessons).

## Sources

Policy: at least 8 sources, at least 4 primary, at least 1 secondary. Primary
candidates: the RealToxicityPrompts paper, Perspective API's own model
documentation/card, Sap et al. 2019, and a primary establishing the classifier's
training data (Wikipedia Talk / Civil Comments). Researcher owns the set, verifies
each figure against its owning primary, and records the classifier-bias evidence
in full.

## Production policy (balanced profile)

- researcher high, writing-coach low, writer medium, editor high; capable model.
- nb-meta harness `claude-code-routine`, model `claude-opus-4-8`, date 2026-08-31,
  series `the-instruments`, slug `toxicity-score`. No `required` directive.

## This edition's siblings (keep each piece distinct)

Publishing with lessons on the adversarial-examples paper, hands in generated
images, the AI-boxing argument, and AI writing-detector failures. This piece owns
the toxicity measurement. The writing-detector piece (when-ai-breaks) is a distinct
classifier-failure story; keep this one to how the toxicity number is made and how
it misjudges.

## Recent-pattern notes (habits not to inherit)

Recent the-instruments deks/headlines, not to echo in mold:
- "A model's \"37% hallucination rate\" was its wrong-answer share on SimpleQA"
- "Adding six wrong answers to each MMLU question fixed its guessing problem"
- "'Human parity' in speech recognition came down to how you count the humans"
- "A model can top the MTEB average and be ordinary at retrieval"
- "The same model scored 1673 or 2214 on Codeforces, depending on the scaffolding"
The most recent piece (simpleqa) opened with an nb-stat-strip and used a "how X
became Y" nb-note; do not default to that shape. Only the two bookends address the
reader. No Verdict block at the body's close.
