# Writer draft-handoff: the-mechanics/watermarks-in-generated-images (01)

**Original work.** The evidence record establishes each mechanism and flags
the exhibit-vs-framing gap as its most important finding; this draft is what
turns that into a teaching argument: it holds distributional learning and
verbatim memorization apart as two distinct, separately-sourced mechanisms
through the whole chain, then reads Getty's own paragraph-52 exhibit against
the two photographs it actually prints — not against the memorization
citation the preceding paragraph borrows — and shows that the exhibit, read
directly, supports the distributional-learning mechanism more than the
copying claim Getty built around it, while keeping that allegation
attributed to Getty throughout. No single source in the record makes that
comparison; it only becomes visible once the two mechanisms and the exhibit
are placed side by side.

**Proof result.** Final run, links included:

```
./nb check .nb-work/the-mechanics/watermarks-in-generated-images/library/the-mechanics/watermarks-in-generated-images.html --series the-mechanics --library <library checkout>
BLOCK: 0
WARN: 1
verdict: PUBLISHABLE
```

`nb stamp` has been run; nb-meta `words`, `reading_minutes`, and `sources`
are computed values (2199 / 10 / 7), and `dek` matches the rendered dekline
exactly.

**Warning intentionally left.**

- `W-SOURCES-MIN` — 7 sources cited; the-mechanics series floor is 8. This is
  a hard ceiling of what the evidence record supports, not an oversight: the
  record lists exactly 7 sources read to the citation standard (6 primary,
  1 secondary — clears `sources_by_kind`, primary ≥4 and secondary ≥1). The
  one candidate 8th source, Somepalli et al., is explicitly marked in the
  evidence record's Discarded section as read only via an abstract summary,
  "not... to the standard the other sources meet," so citing it would
  violate "cite only what you have read." The record's other near-misses are
  mirrors of the same Getty complaint already cited as source 1 (courts
  listener, Justia, Copyright Alliance) or an unverified web-search figure
  the record could not locate in either primary; using either would be
  padding the count with the same document or an unconfirmed number, which
  the standard also rules out. This is a warning, not a block (`strict:
  false` on this series, and `W-SOURCES-MIN` is non-promotable regardless),
  and BLOCK: 0 holds with it left in place.

**Open evidence question for a possible next round.** If the paper wants
`W-SOURCES-MIN` closed rather than left, the fix is a researcher task, not a
writer one: either a full read of Somepalli et al. (arXiv:2212.03860) to
bring it up to the citation standard — the record already notes its method
differs from Carlini's (semantic/style similarity vs. near-pixel-identical),
which would need its own accurate framing if used — or a fresh primary on
watermark prevalence, deduplication practice, or the litigation's current
posture that the record didn't pursue. No voice question is open; the piece
follows the voice guide's settled/open cut at the memorization step and
avoids both shapes the brief asked to break.
