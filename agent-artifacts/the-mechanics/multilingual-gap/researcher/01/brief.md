# researcher brief: the-mechanics/multilingual-gap (01)

Inputs:

- `commission.md` (at the artifact root) — the behavior, angle, source policy,
  neighbors, and what the piece must establish.
- `editorial-direction.md` (at the artifact root) — the citation standard, series
  territory, and declared reader.

Output: `researcher/01/evidence.md` (under this article's artifact root).

Answer these specific questions:

- A concrete, citable instance of the performance gap: a named model measurably
  weaker on the same task in a lower-resource language than in English, from a
  documented evaluation. Record the figures.
- The data-distribution cause (the lead mechanism): a real figure for how skewed
  training data is toward English / high-resource languages (for example the
  GPT-3 paper's per-language share, or Common Crawl language statistics). Pin it
  to the owning primary.
- The tokenizer token-tax cause (secondary amplifier): the per-language token-count
  inflation from Ahia et al. 2023 ("Do All Languages Cost the Same?") and Petrov
  et al. 2023 ("Language Model Tokenizers Introduce Unfairness Between
  Languages") — the multiplier by which a fixed text costs more tokens in named
  languages, and what that does to context use and price. Record an exact,
  reproducible token-count comparison if you can produce one from a real
  tokenizer; otherwise cite the papers' figures with the Numbers shape.
- The settled-versus-open seam: what is well established (data scarcity, token
  inflation) versus what is contested or moving (relative contribution of each
  cause; that larger multilingual models and better tokenizers narrow but do not
  close the gap). Record evidence for both.
- Contradictions: record in full any evidence that complicates a single-cause
  story or shows the gap closing, and anything suggesting other causes.

Meet the source policy in the commission. Prefer the document that owns each
claim. Every URL must resolve to the source's own page.
