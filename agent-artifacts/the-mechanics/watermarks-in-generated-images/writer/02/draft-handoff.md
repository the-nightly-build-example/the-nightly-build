# Writer draft-handoff: the-mechanics/watermarks-in-generated-images (02, revision)

**Original work.** Unchanged from round 01, and it still holds after this
revision's corrections: the evidence record establishes each mechanism and
flags the exhibit-vs-framing gap as its most important finding; this draft is
what turns that into a teaching argument. It holds distributional learning
and verbatim memorization apart as two distinct, separately-sourced
mechanisms through the whole chain, then reads Getty's own paragraph-52
exhibit against the two photographs it actually prints, not against the
memorization citation the preceding paragraph borrows, and shows that the
exhibit, read directly, supports the distributional-learning mechanism more
than the copying claim Getty built around it, while keeping that allegation
attributed to Getty throughout. No single source in the record makes that
comparison; it only becomes visible once the two mechanisms and the exhibit
are placed side by side.

**Editorial requests resolved.**

- Corrected the false "never filtered to remove them" / "nothing removing
  it" claim in the training-data section: the section now states, sourced to
  the Stable Diffusion v1 Model Card (new source 5), that the model's first
  two training stages carried no watermark filter at all and that every
  later checkpoint resumed from that unfiltered pair, while only the
  following subset was screened at an estimated watermark probability under
  0.5, a looser cutoff than LAION's own 0.8 threshold and an estimate rather
  than a checked label — partial in scope, permissive in threshold,
  probabilistic rather than exact, as the evidence record's Contradictions
  entry frames it.
- Corrected the parallel "absence of any filter for a pervasive mark" claim
  in the closing section to match the same staged, partial account, and
  rewrote the leaked "Nothing below that level changes the answer" sentence
  in the article's own terms ("Go one level deeper and there is nothing left
  to find: the objective, the data, and how much of that data was screened
  before training account for the whole behavior"), no longer echoing the
  commission's "Ground and present day" phrasing.
- Cited the eighth primary the record now supports, Somepalli et al. (CVPR
  2023, new source 8), in the memorization section: it extends the existing
  "further gap" point (that the memorization literature never mentions
  watermarks) to a second, independently-built detection method that also
  never mentions them, which is the same pairing Getty's own footnote 6
  cites and which the memorization section already sets up for "the
  research above" reference two paragraphs later. Sources renumbered in
  first-citation order (model card = 5, Rombach/LDM = 6, Carlini = 7,
  Somepalli = 8, Getty docket = 9); `data-nb-kind="primary"` on both new
  entries, matching the evidence record.
- Preserved the editor's direct edits (source-4 "Cooper" label and body
  prose, the rewritten "Why this matters" opener) and every other settled
  finding from editor/01 untouched.

**Proof result.** Final run, links included:

```
./nb check .nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html --series the-mechanics --library <library checkout> --check-links
BLOCK: 0
WARN: 1
verdict: PUBLISHABLE
```

`nb stamp` has been run; nb-meta `words`, `reading_minutes`, and `sources`
are computed values (2367 / 10 / 9), and `dek` matches the rendered dekline
exactly. `W-SOURCES-MIN` has cleared: 9 sources against the series' 8-source
floor (8 primary, 1 secondary).

**Warning intentionally left.**

- `W-LENGTH-HIGH` — the lesson band is 1200-2200 words; the piece is now
  2367. The overage is the direct, necessary cost of this round's two
  required corrections: replacing a one-sentence false claim with the
  staged/permissive/probabilistic account the model card actually supports
  cannot be done in fewer words without losing the "partial in scope,
  permissive in threshold, probabilistic rather than exact" distinction the
  editorial review asked for, and citing the eighth primary needs its own
  sentence to say where it belongs rather than a bare citation stapled onto
  an existing claim. I trimmed both additions once for density (cutting
  redundant qualifiers and a repeated "above") before accepting the
  remainder; further cuts would have meant dropping one of the three
  required elements (scope, threshold, or the probabilistic-estimate point)
  or removing the Somepalli sentence's own explanation of what it adds,
  which the citation-standard rule against bare, unexplained citations rules
  out. `strict` is not set for this series and the finding is a WARN, not a
  block; `BLOCK: 0` holds with it in place.

No open evidence or voice question.
