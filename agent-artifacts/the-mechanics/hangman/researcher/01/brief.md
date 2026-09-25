# researcher brief: the-mechanics/hangman (01)

Inputs: editorial-direction.md (../../editorial-direction.md), commission.md (../../commission.md)
Output: ./evidence.md

Work from these inputs. Do not tour the repository. Ask me where something is missing.

Read the primary documents, with locators:
- The stateless nature of chat APIs: OpenAI and/or Anthropic API documentation
  stating that the API is stateless and the full conversation must be resent each
  request, and that the model conditions only on the provided messages. Record
  the exact statements and URLs.
- The autoregressive/stateless forward pass: a model or systems doc stating each
  generation step conditions on the input token sequence and keeps no persistent
  private memory across requests (a transformer/LLM reference or a serving doc;
  KV-cache is within a single sequence, not across turns — record that
  distinction so the writer does not overclaim).
- The hidden-state exception: a reasoning-model system card or the scratchpad/
  chain-of-thought literature showing that hidden thinking tokens or a scratchpad
  CAN carry state within a response, so the writer can state the exception
  precisely. Record what is and is not persisted.
- The behavior itself: find reputable, dated demonstrations of the hangman / 20-
  questions failure (a model giving inconsistent yes/no answers, or revealing a
  word that contradicts its clues), e.g. blog posts, well-documented forum/GitHub
  threads. Record enough that the writer can present a faithful, reproducible
  illustrative transcript (not an invented one presented as captured evidence).

Establish the core mechanism: no hidden state between turns; a withheld word is
written nowhere, so it does not exist; each turn regenerates from the visible
transcript. And the precise exception (scratchpad/hidden reasoning/tool state).

Source floor: min 8, >=4 primary, >=1 secondary. Classify each with a reason.
Contradictions: record anything suggesting models DO hold hidden state in plain
chat (they do not, but memory features and reasoning tokens complicate it —
record precisely). Numbers: not central, but record any measured consistency
rates if a source has them. Limits: note that the clean claim holds for a plain
chat with the word withheld, and where products differ (memory features,
tools). Source assets: a faithful transcript screenshot is a candidate only if
from a cited source.

Report the path and the most important limit.
