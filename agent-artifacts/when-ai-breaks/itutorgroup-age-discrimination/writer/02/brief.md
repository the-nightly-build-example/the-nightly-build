# writer brief: when-ai-breaks/itutorgroup-age-discrimination (02)

A revision. Apply the editor's required work using the corrected evidence. The
editor already made its own direct edits to the article (including cutting the stat
strip) — preserve those; change only what this brief names.

Inputs:
- ../../editor/01/editorial-review.md — the editor's read; "Required work" names the items
- ../02/evidence.md — the CORRECTED evidence record (researcher/02); use this, not 01, for the AI-language finding and the s8 URL
- The article to edit in place: /home/user/the-nightly-build/.nb-work/when-ai-breaks/itutorgroup-age-discrimination/library/when-ai-breaks/itutorgroup-age-discrimination.html

Output: ./draft-handoff.md (writer/02, beside this brief; do not overwrite 01)

Proof (from /home/user/the-nightly-build): iterate `--no-check-links`, then run WITH
links until `BLOCK: 0`:
`./nb check .nb-work/when-ai-breaks/itutorgroup-age-discrimination/library/when-ai-breaks/itutorgroup-age-discrimination.html --series when-ai-breaks --library /home/user/library-checkout`
Run `./nb stamp <that article path>` before the final check.

The two changes, and nothing else beyond what they require:

1. The claim that the record never uses the words "AI"/"machine learning"/"algorithm"
   is FALSE and must be corrected. Per researcher/02: the 2022 EEOC suit release DOES
   carry AI/ML wording, but ONLY as boilerplate about the agency's separate
   "Artificial Intelligence and Algorithmic Fairness Initiative" (a standalone
   paragraph and Chair Charlotte Burrows' quote), never as a description of
   iTutorGroup's software. Recast the section heading "The record never says 'AI'"
   and the sweeping "never appears" sentence to the narrower, true claim: the EEOC
   never describes iTutorGroup's OWN software as AI or machine learning — it calls it
   software "programmed to automatically reject" by a birth-date cutoff — and the
   only AI/ML wording in the record is the agency's initiative boilerplate, with the
   "AI hiring" framing coming from commentators and that branding. Keep the honest-
   mechanism lesson intact; it is stronger, not weaker, stated precisely.

2. Point source s8's href at the specific Mobley July 12, 2024 order (CourtListener
   Document 80): https://www.courtlistener.com/docket/66831340/80/mobley-v-workday-inc/
   — not the docket index. Per researcher/02 this page 403s to automated fetch but is
   a transport gate, not a dead page (it is the order's own home). If the full
   link-checked proof BLOCKS on this URL, do not silently revert: report it back with
   the exact proof line so the orchestrator can decide; a WARN you may leave with a
   one-line note in the handoff.

Preserve every other settled sentence and the editor's edits. Rerun the complete
proof. In draft-handoff.md record: the original-work sentence still holds, the two
edits made, the proof result, and any warning left with its reason.
