# researcher brief: the-mechanics/word-order (01)

Inputs:
- `../../commission.md` — the assignment, the two-or-three ideas, and the
  boundaries (embeddings and the causal mask are taught elsewhere; link them).
- `../../editorial-direction.md` — citation standard, series territory, declared reader.

Output: `evidence.md` (this directory)

Focus and known risk surface (decisions the inputs do not settle):

- The order-blindness claim needs a primary that states self-attention is
  permutation-equivariant / that a transformer without positional information
  cannot distinguish word orders. Vaswani et al. 2017 ("Attention Is All You
  Need," arXiv 1706.03762) motivates positional encodings for exactly this
  reason; record its own words on why position must be injected, and the
  sinusoidal formula's role (record what it is, not a re-derivation).
- Learned absolute position: record a primary that uses learned position
  embeddings per slot (BERT, Devlin et al.; or GPT-2, Radford et al.) so the
  "added, not computed" idea has two concrete forms.
- RoPE: Su et al., "RoFormer: Enhanced Transformer with Rotary Position
  Embedding" — record precisely what it does (rotates query/key by an angle set
  by absolute position so the attention score depends on relative offset) and
  that it is now the common choice. ALiBi: Press et al., "Train Short, Test Long"
  — record that it biases attention by distance and its extrapolation claim.
- The open ground: length extrapolation. Record what ALiBi/RoPE papers and any
  follow-up actually claim about generalizing past the trained length, and where
  they concede it is unsettled. NoPE: Kazemnejad et al. 2023 ("The Impact of
  Positional Encoding on Length Generalization") — record the finding that a
  decoder-only model can learn position without explicit encodings, and how
  strong/bounded that result is. Mark clearly, per source, what is settled
  engineering and what is open.
- Relative position origin: Shaw et al. 2018 ("Self-Attention with Relative
  Position Representations") for the relative-vs-absolute distinction.
- Search for what undercuts the angle: any evidence that attention is not truly
  order-blind in practice, or that one scheme is clearly settled as best. Record
  contradictions honestly.

For a possible figure: note whether any source carries a clean visual of a
positional-encoding pattern or an extrapolation curve that a reader could learn
from (source-asset candidate), or write None found.

Run-environment caveat: record each source's own resolving page (arXiv,
publisher, ACL Anthology), never a fetch-proxy URL.
