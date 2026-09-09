# Draft handoff: when-ai-breaks/cigna-pxdx

Status at handoff: `nb check` (with `--library` and `--check-links`) returns
0 BLOCK, 0 WARN, verdict PUBLISHABLE. Words 1740 (band 1200-2200). Sources 8
(5 primary, 3 secondary). All source URLs and both Go-deeper links returned HTTP
200 on 2026-09-09.

## Headline and dek
- Title: "Cigna doctors denied over 300,000 claims in two months without opening
  the files"
- Dek (equals the rendered dekline and nb-meta.dek): "Its PxDx software flagged
  claims whose procedure did not match an approved diagnosis, and medical
  directors signed the denials in batches at about 1.2 seconds each."

Plain actor-and-failure headline with the concrete volume figure, per the desk
habit note. No "Two X did the same Y" mold, no colon subtitle, no comma-tail
reversal in the dek. The 1.2-seconds figure is held for the dek so it does not
repeat the headline.

## Structure (fixed orientation + 3 flex, then bookends)
1. orientation — "A list matches the procedure to the diagnosis": what PxDx is
   (procedure-to-diagnosis code match), the legal review requirement it sits
   inside (Cal. Code Regs. tit. 10 § 2695.7(d)), and the precision point that it
   is code-matching software, not a learned model (Cigna's own words).
2. what-the-record-shows — "What the reporting found in Cigna's own data": the
   incident in order with named doctors, per-doctor counts, the two on-record
   quotes, and the Kisting-Leung complaint case ($198 ultrasound).
3. cignas-account — "Cigna says the software denies payment, not care": the
   steelman in Cigna's own words (note card), the standing limit the court
   found, the throughput point the objections do not answer, and the aftermath
   (House committee, state regulators, March 2025 ruling, discovery).
4. a-signature-that-reviewed-nothing — why the rubber-stamp fails the purpose of
   review, and where the same shape lives now (prior authorization, claims
   adjudication). Michigan MiDAS linked as prose, not re-taught.

Final body heading avoids the forbidden "How far the X reaches" form and varies
construction from the recent library.

## Furniture (two pieces, each earning its place)
- `nb-stat-strip` in section 2: 300,000+ denials / 1.2 s per case / 121,000 by
  one doctor. Each figure is stated and cited in the adjacent prose (Source 1).
- `nb-note` labelled "Cigna's account" in section 3: Cigna's verbatim rebuttal
  (software, not AI; no denial of care), attributed and cited (Source 3). Carries
  the steelman so the disputed cause is presented at full strength.

No chart (none earned; no committed chart-N.py). No timeline: the datable events
are aftermath, and the stat strip plus prose carry the incident without it.

## Sources, numbered in order of first appearance
1. ProPublica / Capitol Forum investigation, Mar 25 2023 (primary)
2. Kisting-Leung v. Cigna class-action complaint, Jul 24 2023 (primary)
3. Cigna Healthcare statement, Jul 27 2023 (primary)
4. ProPublica / Capitol Forum congressional-investigation follow-up, May 16 2023 (secondary)
5. Georgetown litigation tracker case record / Mar 31 2025 order (primary)
6. STAT News lawsuit report, Jul 24 2023 (secondary)
7. House Energy & Commerce Committee letter, May 16 2023 (primary)
8. NFP analysis of the Mar 31 2025 ruling (secondary)

Every figure was verified against primary reporting and quoted, not recalled:
300,000+/1.2 s (S1, echoed in S2 complaint), per-doctor counts and both quotes
(S1), $198 ultrasound and the 0.2% appeal allegation and the CA "thorough, fair,
and objective" duty (S2), "software (not AI or an algorithm)"/~50 procedures/no
denial of care (S3), 80% MA overturn context (S7), standing finding and discovery
status (S5), "abuse of discretion" (S8). See researcher/01/evidence.md.

## Judgment calls the editor should know
- Precision on mechanism: the piece never calls PxDx "AI" or "machine learning."
  It is described as code-matching software, and Cigna's on-record denial of AI
  is quoted. This is deliberate per the commission.
- Fair presentation of the dispute: Cigna's account is given its own note and
  prose, and the court's standing finding (that some named plaintiffs did not
  show their claims ran through PxDx) is stated plainly. The Kisting-Leung facts
  are attributed to the complaint as allegations, not asserted as settled.
- What settles the disputed cause: the piece says the figures Cigna does not
  contest (its own throughput data) are what the argument rests on, and that a
  court has let the core claims proceed while the individual denials remain
  contested in discovery.
- michigan-midas is linked once in prose at first use (no numbered source) and
  once as Background reading, not re-taught. The "meaningful human review" idea
  is taught fresh here because the course had not defined it.

## Open items / limits
- None blocking. The complaint PDF is a binary court filing; its text was
  extracted locally (pypdf) to quote paragraphs 1, 2, 4, 17, 26-30 accurately.
- The 80% overturn figure (S7) is Medicare Advantage context the committee itself
  cited, not a PxDx-specific rate; the prose says so.
