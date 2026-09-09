# Editorial review: when-ai-breaks/cigna-pxdx (editor 01)

Decision: **approved — no required change remains.** Edited in place. No claim
had to be routed back to the writer; one unsupported detail was cut, and the
citations that did not own their claim were corrected.

Final proof: `./nb check ... --series when-ai-breaks` returns 0 BLOCK, 0 WARN,
verdict PUBLISHABLE. Stamped words 1688 (band 1200-2200), 8 sources.

## Accuracy: figures traced to evidence.md and its primary sources

Every figure was checked against the evidence record and the source it names.
All hold:

- 300,000+ denials over two months of 2022, ~1.2 s each — S1 (reporting),
  echoed in S2 para 2 (complaint). Article attributes to the reporting. OK.
- Per-doctor counts (Dopke 121,000; Capek ~80,000; Rossi ~63,000) and both
  on-record quotes ("10 seconds to do 50", Muney's "not reviewed by a doc") —
  S1, quoted verbatim. OK.
- $198 ultrasound, member since 2018, referral Aug 2022, denial Oct 2022,
  Cigna's own coverage policy calls it necessary at increased ovarian-cancer
  risk — S2 paras 26-30, framed as the complaint's allegations. OK.
- 0.2% appeal rate — S2 para 4, and the text says "the complaint alleges." OK.
- ~50 low-cost procedures; "software (not artificial intelligence or an
  algorithm)" — S3, quoted. OK.
- "thorough, fair, and objective" duty — S2 para 17 (cite 2) and S6 (cite 6).
  Kept separate from the Cigna-specific claims. OK.
- 80% Medicare Advantage overturn — S4 (cite 7), and the prose scopes it to
  Medicare Advantage "where the numbers are public," not to PxDx. OK.
- "Abuse of discretion" / core claims proceed / still in discovery — S8 (cite 8)
  and S5 (cite 5). OK.

### One unsupported detail cut

- "the scan found a cyst **on her left ovary**" → "the scan found a cyst."
  evidence.md (S2 note) records only "found a dermoid cyst"; no side is in the
  record. Removed the laterality rather than ship a detail the evidence does not
  carry. "a cyst" is fully supported.

### Citations corrected to the source that owns the claim

- "The denial letter still says a doctor decided" was cited to 7 (House
  committee letter). That letter says the opposite — that an algorithm stands in
  for clinician judgment. Re-pointed to 1, where the doctors' signing-off is the
  reported fact.
- The closing "where it lives today" generalization carried two citations to 7.
  The House letter is Cigna-specific and does not establish that prior
  authorization runs this way across insurers. That is the series-mandated
  synthesis, grounded in the mechanism already taught, so it now stands as
  analysis without a citation that does not support it. Source 7 remains cited
  once (the 80% figure), so no source is orphaned.

## Mechanism precision

The piece holds the line throughout. PxDx is "code-matching, not a model that
learned anything from data"; "Nothing in PxDx predicts, scores, or estimates";
the takeaway states "It is not a model." Cigna's own denial of AI is quoted. The
only occurrence of "AI" is inside source 8's actual title (NFP), which cannot be
altered. No change needed.

## Fairness on a contested subject

Left in place, confirmed sound: Cigna's account appears in its own words in prose
and in the labelled note (verbatim quote, attributed and dated); the court's
standing finding — that several named plaintiffs did not show their claims ran
through PxDx — is stated plainly; the Kisting-Leung facts are attributed to the
complaint as allegations. Reported fact, allegation, and analysis stay distinct.

## Slop cut at the edges

- Section 3 opener: "and its account deserves to be stated at full strength" —
  cut. It announced the steelman instead of being it; the steelman follows in
  the note and prose. Second "Cigna" changed to "It" to avoid the repeat.
- Section 3, a paragraph-closing aphorism: "The distance between a denial and an
  appeal is where the savings sit" — cut. It reduces to the generic mould "the
  distance between X and Y is where Z sits," grades the argument rather than
  continuing it, and imputes a savings motive the steelman brief warns against.
  The paragraph now ends on the concrete 0.2% appeal figure.
- Body's final paragraph: the redundant last sentence ("The same shape appears
  wherever a company automates the sorting...") restated the sentence before it
  and carried a decorative citation. Cut; the section now closes on the concrete
  list of systems and the shrunk-to-a-signature mechanism, not a verdict
  restatement.
- Minor tightening: "at its core it is a list" → "it is a list"; "Its whole
  value is that it catches" → "Its whole job is to catch."

The article's true last sentence (the takeaway bookend) lands the judgment, which
is the bookend's job; it uses no term the body did not set and names the
particular thing at stake. The body does not close on a verdict block.

## Headline, dek, headings

Headline is a plain actor-and-failure line anchored on the 300,000 figure — no
"Two X did the same Y", no colon subtitle. Dek adds the mechanism and holds the
1.2 s figure without restating the headline; two clauses joined by "and", not a
comma triad or reversal. Section headings are concrete and vary in construction;
the final body heading is not "How far the X reaches." All kept as written.

## Furniture and links

Stat strip and the "Cigna's account" note each earn their place and are cited.
michigan-midas is linked once in prose (not re-taught) and listed in Background;
that is the sanctioned pattern, not a re-teach. Kept.

## One WARN introduced and resolved

The rewritten closing sentence ran 42 words with three clause joins
(W-SENTENCE-DENSITY). Split into two sentences. Final check is 0 WARN.
