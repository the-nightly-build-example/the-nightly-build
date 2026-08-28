# researcher brief: the-mechanics/glitch-tokens (01)

Inputs:
- editorial-direction.md  (citation standard, the-mechanics territory, declared reader)

Output: agent-artifacts/the-mechanics/glitch-tokens/researcher/01/evidence.md

The behavior under examination: "glitch tokens" — a small set of tokens (the
canonical one is " SolidGoldMagikarp") that reliably make GPT models produce
anomalous, evasive, or wrong output, while ordinary words behave. Research the
mechanism from primary sources.

Research questions the evidence record must answer, each traced to an owning
primary (give locators):
- The documented behavior: which tokens, which models, what exactly was prompted,
  and what the models did (e.g., inability to repeat the token, substitutions,
  evasion). Source this to the original investigations, not retellings. Give exact
  token strings as the record has them.
- The origin of the tokens in the tokenizer vocabulary: that GPT-2/GPT-3-family
  byte-pair-encoding vocabularies were built from a corpus that included artifacts
  like a Reddit counting forum's usernames, so these strings became single tokens.
  Cite the primary account.
- The core mechanism: that the tokenizer's vocabulary is constructed separately
  from — and often on different data than — the model's training set, so a token
  can be in the vocabulary yet almost absent from training; its embedding stays
  near random initialization and carries no learned meaning. Establish this as the
  settled claim, with a source that owns it.
- The peer-reviewed follow-up: "Fishing for Magikarp" (Land & Bartolo, 2024) or
  equivalent work that systematically detects under-trained/under-observed tokens
  across models and tokenizers — what it measured and found. Read it.
- What remains open: the precise internal path from a near-random embedding to
  each specific weird output, and how far newer tokenizers/models (e.g., cleaned
  vocabularies) have removed these tokens.

Search for what breaks the angle: evidence that glitch behavior persists for
tokens that ARE well-trained, or that the cause is not under-training but
something else (e.g., tokenization mismatch at inference). Record it in
Contradictions in full.

Source policy: at least 8 sources, at least 4 primary, at least 1 secondary.
Classify each by authorship and stake. Confirm every URL resolves. A LessWrong
research write-up by the investigators who found the phenomenon is a primary
source for what they observed; classify with that reasoning.
