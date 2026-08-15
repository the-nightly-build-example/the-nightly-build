# Draft handoff: when-ai-breaks/google-photos-gorilla (01)

## Original work

The article turns the evidence record's separate findings into one causal
chain — the 2015 mislabel, the training-example mechanism that Gender Shades
measures in shape but not in this incident's number, and the deliberate non-fix
that Google's own Cloud Vision recognizing a gorilla exposes — to show that
Google removed the dangerous category rather than closing the accuracy gap, and
that four companies were still making that same choice eight years on. The
record holds these as discrete source summaries and contradiction notes; the
article's work is to order them into cause, measured mechanism, and persistence,
and to state the non-fix precisely as a risk decision rather than a recognition
failure.

## Proof result

`./nb check ... --series when-ai-breaks --library /home/user/library-checkout`
(links included, after `./nb stamp`):

- **BLOCK: 1** — `B-SOURCE-KIND`: 2 primary sources cited; the series asks for at
  least 4. This block is unavoidable under the orchestrator's rulings and cannot
  be cleared by writing. See "Open decision" below.
- **WARN: 1** — `W-SOURCES-MIN`: 6 sources; the series floor is 8. Same root
  cause as the block (only six sources are honestly citable). Left standing.
- All six source URLs resolve (no `B-SOURCE-DEAD`). Word count 1948, within the
  1200–2200 band. The earlier `W-SENTENCE-DENSITY` on the takeaway's closing
  sentence was fixed by splitting it.

## Open decision needed (owner: orchestrator / paper owner)

The series contract sets `sources_by_kind: primary [4, null]` and `min_sources:
8`. `B-SOURCE-KIND` enforces the primary floor and **blocks regardless of
`strict`** (the series is `strict: false`, so the min_sources floor is only a
warning, but the kind floor still blocks). `engine/nb/proof/sources.py` counts
only *cited* sources toward the mix.

The orchestrator's rulings for this round removed every primary in the record
except two:

- Forbidden as dead/unreadable: Alciné's tweets (deleted, 404), Zunger's tweets
  (account protected), and the New York Times 2023 article (403 paywall, not
  read firsthand). The record's own access notes confirm each.
- The only two link-citable, firsthand-read primaries are **Wired 2018** and
  **Gender Shades**. Both are cited. That is 2 primary, and the floor is 4.

Google's 2015 statement and Alciné's/Zunger's words survive only inside the
readable secondary coverage (Forbes, CBC, PetaPixel, The Register), so they
enter the article attributed to that coverage and counted as secondary, exactly
as the ruling directs. There is no honest path to a third or fourth primary
without expanding the claim set, which the writer role forbids.

To reach `BLOCK: 0`, one of the following is required, and none is a writing fix:

1. A new researcher artifact supplying at least two additional **readable,
   firsthand** primary documents for this incident — for example a reachable
   copy of Google's own 2015 statement (a Google blog/press page or a working
   archive), a primary source for the training-data/underrepresentation cause
   (the record currently marks it inferred, not confirmed), or a readable
   primary the 2023 retest can hang on; or
2. An owner decision to relax the `when-ai-breaks` primary floor for incidents
   whose primary record has gone dark (deleted posts, paywalled reporting); or
3. Explicit authorization to cite a specific currently-excluded primary despite
   the ruling — note that the NYT 2023 URL returns 403 and would **not** trip
   the link check, but the researcher could not read it, so citing it would
   violate "cite only what you have read."

## Open evidence/voice question

Only the one above. Everything else in the brief and rulings is satisfied: the
non-fix is stated precisely (removal of the label, not a recognition inability,
with Cloud Vision's 94% gorilla tag as the proof it was a choice); Gender Shades
is presented as mechanism with its scope stated in-line and pinned in an "In
plain language" note, never as a measurement of Google Photos; only
resolving/read URLs are cited; the racist label is reported plainly and
attributed to the record's framing; the "Why this matters" bookend avoids the
house "by the end you will be able to" opener; the closing section is titled in
this incident's nouns ("The block that outlived the apology"), not the desk's
recurring "where the weakness lives now" shape; and the headline states the
finding directly, off the comma-continuation and "X, not Y" molds.
