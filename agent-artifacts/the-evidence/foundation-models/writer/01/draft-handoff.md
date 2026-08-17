# Draft handoff: the-evidence/foundation-models (writer 01)

## Original work

The evidence record documents the report's naming rationale and its hedge as
two separate source entries; this draft puts them next to each other as the
report's own back-to-back sentences (one note-quoted, one in prose), lets that
juxtaposition stand as fact rather than writer verdict, then hands the judgment
to Marcus and Davis's own words quoting the same hedge back at the report — so
the reader watches the same primary sentence do two different jobs (the
report's justification, the critics' rebuttal) instead of being told the
document contradicts itself. The piece also traces one document's full
lifecycle end to end, coinage through contemporaneous objection through NIST
standardization through a rescinded executive order, as a single worked case
of "ask what a document proved versus what it named" that a reader can reapply
to the next influential AI document they meet.

## Proof result

`./nb check .nb-work/the-evidence/foundation-models/library/the-evidence/foundation-models.html --series the-evidence`
(links checked): **BLOCK: 0**, verdict PUBLISHABLE.

3 WARN left standing, all `W-SENTENCE-DENSITY`, all on verbatim primary
quotations where shortening would misquote the source:
- the report's own §1.1.1 hedge ("At present, we emphasize that we do not
  fully understand the nature or quality of the foundation...")
- Dietterich's on-record "flag planting... fundraising" remark (Wired)
- Executive Order 14110's statutory definition of "dual-use foundation model"

Every other sentence-density warning from the first pass (7 total) was fixed
by splitting the writer's own prose. Word count 1,869 (band 1,200-2,200),
9 sources (7 primary, 2 secondary; template minimum is 3 primary, 1 secondary),
reading time 8 minutes.

## Notes

- Used a source asset: Fig. 19 from the report itself (arXiv PDF v3, p. 97),
  captured via `nb asset pdf`, placed in the orientation section as the
  concrete "the one chart isn't the report's own data" evidence. Alt text and
  caption checked against the rendered crop.
- Followed the evidence caution on Marcus and Davis's "149" headcount by
  omitting it entirely rather than presenting it alongside the report's 114:
  the two figures measure different populations (broader CRFM community vs.
  the report's own byline) and no source resolves the gap, so using only the
  report's own 114 avoided the conflation risk without needing to explain it
  in the body.
- Executive Order 14110 is presented strictly as "reached... a formal legal
  definition" and "reached binding federal text once, and did not stay
  there," never as currently governing law; NIST SP 800-218A (2024) carries
  the "became standard usage" claim instead, per the evidence record's
  guidance.
- No open evidence or voice question. The voice guide was a same-series
  sibling's (sparks-of-agi); I took its craft moves (evidence sitting next to
  the finding in the same breath, one worked primary example over reputation,
  a company/institution figure stated once and left standing) and left its
  subject-specific references untouched.
