# Editorial review 02 — the-instruments/bleu (revision re-read)

## Scope

Round 01 required one structural fix outside the editor's surgical remit:
convert the Callison-Burch Table 4 n-gram comparison in "The evaluation
where the ranking flipped" from packed prose ("27 unigrams, 20 bigrams, 15
trigrams, 10 4-grams" vs "24, 19, 15, 12") into a table. All other round-01
findings (brevity-penalty arithmetic, WMT correlation range, Verdict-block
cut, two hedged-contrast cuts) were already fixed directly in the article
during round 01. This is a focused re-read of the writer's round-02
revision only, not a full re-litigation.

## What I re-checked

1. **The fix itself.** The two packed prose sentences are gone entirely —
   confirmed by grep, no leftover or duplicate copy of "27 unigrams, 20
   bigrams" or "24, 19, 15, 12" anywhere in the article. In their place is
   an `nb-table` with columns n / matched-more-overall / matched-fewer-overall
   and one row per n=1..4, using the same `nb-table` / `nb-table-token`
   markup as the article's existing worked-example precision table. The
   surrounding prose now states the point in one sentence before the table
   ("One hypothesis matched more reference words overall; a second matched
   fewer") and one after ("Human judges scored the hypothesis with fewer
   total matches higher on both adequacy and fluency"), matching exactly
   the pattern the round-01 review asked for and the format the primary
   worked example already used.

2. **The numbers, against the evidence record.** Table rows: 1-gram 27/24,
   2-gram 20/19, 3-gram 15/15, 4-gram 10/12. Checked against
   `researcher/01/evidence.md` Numbers section: "a hypothesis with more
   matching n-grams (27 unigrams, 20 bigrams, 15 trigrams, 10 4-grams) but
   lower human scores... than one with fewer matching n-grams (24, 19, 15,
   12) but much higher human scores" — Callison-Burch et al. 2006 Table 4,
   p.253. Exact match, all eight figures, no new or altered numbers. The
   table's "matched more overall" column correctly holds the
   lower-human-scoring hypothesis (27/20/15/10) and "matched fewer overall"
   correctly holds the higher-scoring one (24/19/15/12), consistent with
   the prose sentence that follows.

3. **A row-level nuance the writer flagged and handled correctly.** The
   "fewer overall" hypothesis actually has *more* 4-gram matches (12 vs.
   10) than the "more overall" one — the aggregate framing only holds
   summed across n, not at every row. The writer declined to use round 01's
   illustrative phrasing ("the hypothesis with fewer matches at every n
   scored higher") for exactly this reason and kept the framing the
   evidence record itself uses (aggregate more-matches-but-lower-score vs.
   fewer-matches-but-higher-score). This is the more accurate claim; no
   correction needed.

4. **Round-01 fixes still stand — no regression.** Grepped the current
   article for each: "7.1 percentage points, from 0.813 down..." present
   (not "8.7"); "&minus;0.43 to 0.83" present (not "0.88"); no `nb-note
   nb-note-strong` "Verdict" block anywhere in the body; no "not one lab's
   artifact" clause; no "claim worth checking, not a finding worth
   repeating" closing sentence. All five round-01 direct edits are intact
   and untouched by the round-02 revision.

5. **`nb-meta` and byline honesty.** The table replaced two prose sentences
   with a table plus two shorter framing sentences, which changed the word
   count. `nb-meta.words` is now 2170 (down from 2200), `nb-meta.reading_minutes`
   is 9, and the header byline reads "9 min read" — all three consistent
   with each other and with the site's own `WORDS_PER_MINUTE = 230`
   constant (2170/230 ≈ 9.4, rounds to 9). No stale count left over from
   before the table change.

6. **Proof.** Re-ran the check myself rather than trusting the handoff:

   ```
   nb check .nb-work/the-instruments/bleu/library/the-instruments/bleu.html --series the-instruments --library /home/user/the-nightly-build/library-checkout
   BLOCK: 0
   WARN:  0
   verdict: PUBLISHABLE
   ```

## Skeptic / Cut / Reader

Not repeated in full — this is a focused re-read of one markup change, per
the review brief, not a new three-read pass. The claim set is unchanged
from round 01 (writer's draft-handoff confirms no new argument or figure),
and round 01's skeptic, cut, and reader findings — thesis intact, two
arithmetic errors already fixed, original-work sentence (linking the
worked example's clipping blindness to the 2005 NIST case's synonym
mechanism) still the piece's spine — are unaffected by moving eight
numbers from prose into a table.

## Edits made directly in the article

None required this round. The revision is exactly the structural fix
requested, correctly executed, with no new issues introduced.

## Decision

Clean for publication. The one outstanding item from round 01 — the
Callison-Burch Table 4 n-gram comparison living in packed prose — is now a
table with the identical, verified numbers; word count and reading time
were kept honest through the change; every other round-01 fix remains in
place; and the proof is `BLOCK: 0 WARN: 0`.
