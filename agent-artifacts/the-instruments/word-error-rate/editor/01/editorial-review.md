# Editorial review: the-instruments/word-error-rate (editor/01)

## Skeptic

Thesis: a Word Error Rate is a count of word edits against one reference on one
body of audio, so the "human parity" milestone was a claim about one benchmark
and one way of measuring the human it was compared to; the number cannot see
which errors matter or carry across corpora.

The claims it stands on, and how each held:

- **WER is edits over reference words, computed by minimum-edit alignment into
  S/D/I.** Checked against NIST sclite (s2) and Jurafsky & Martin (s3). The
  0/3/3/4 weighting (correct/insertion/deletion/substitution) is stated
  correctly and cited to sclite. The formula figure, the summed numerator, and
  the ">100%" property are attributed to J&M, which the record confirms owns the
  pedagogical statement. Holds.

- **The worked example: 1S/1D/1I over N=6 = 50%.** Re-derived by hand against the
  record. REF "the quick brown fox happily jumps" / HYP "the slow brown fox jumps
  now": quick->slow (S), happily->deletion, insertion of "now" = 3 errors / 6 =
  50%. The tie-breaking argument (4+3+3=10 beats three substitutions at 12) is
  correct and is what makes the intuitive split the unique minimum. The >100%
  case ("hello" -> "hello there my friend" = 3/1 = 300%) is correct. Table cells
  match the alignment row for row. Holds.

- **The parity figures.** Re-derived every number against the Numbers block and
  the source paraphrases. Microsoft 2016 (s1): system 5.8% SWB / 11.0% CH, human
  vendor 5.9% SWB / 11.3% CH — all correct and correctly attributed to the
  two-pass vendor pipeline. IBM (s5): three transcribers plus a fourth senior QC,
  best transcriber 5.1% SWB and "surprisingly low" 6.8% CH, gap traced to a lower
  deletion rate — correct. Microsoft 2017 (s6): improved system 5.1% SWB,
  matching IBM's best human; concession quote exact. The stat strip's four cells
  (5.1 machine SWB 2017, 5.1 human SWB IBM, 11.3 human CH Microsoft vendor, 6.8
  human CH IBM) all reconcile. The 36-of-40 train-contamination figure is IBM's
  and sits inside the s5 citation. Holds.

- **This round's focus items, verified against the record:**
  - Meaning-blindness, not "barely penalizes." The phrase "barely penalizes"
    appears nowhere. The metric-vs-hallucination passage makes the two defensible
    points and only those: corpus-level averaging hides catastrophic segments,
    and WER is meaning-blind (a fluent fabrication scores like an equal-length
    mishearing; a dropped "not" counts like a filler sound). Correct.
  - "Human parity" carries both readings: it held on clean Switchboard
    (2017 system 5.1% = IBM best human 5.1%) and did not generalize (CallHome
    human baseline moved 11.3% -> 6.8%), with Microsoft's own concession quoted
    and attributed to s6. Both present and correctly sourced.
  - The steelman (same function-word errors, same hard speakers, judges could
    not tell the transcripts apart) is stated in full, then weighed against the
    softness of the human baseline. Present.
  - No children's-speech claim anywhere. Blind spots used are the sourced three:
    noise (Whisper, s4), accents/dialect (Koenecke 0.35 vs 0.19, s8), and the
    CallHome/Switchboard gap.

- **Display text, descriptor by descriptor.** Headline states the finding with
  actors and a fresh verb, no colon subtitle, no Betteridge question. Dek adds
  the specific 11.3 -> 6.8 movement and is not a banned mold (two clauses, not a
  comma-triad; no semicolon reversal; no suspended question). Every section
  heading is a concrete step in the piece's own nouns; none uses the comma-plus-
  "and" join. Stat-strip labels, table caption, math legend, and the note's
  attribution ("Microsoft, 2017 system report") all match their owning primaries.
  The one nit: the head `<title>` reads "in speech" where the h1 and nb-meta
  title read "in speech recognition" (see Required work — non-blocking).

- **Sourcing labels.** All eight `data-nb-kind` values check out: primary for
  Microsoft 2016 (s1), NIST sclite (s2), Whisper (s4), IBM (s5), Microsoft 2017
  (s6), Koenecke (s8); secondary for J&M (s3) and Liberman (s7). The renumbering
  the brief flagged is correct in the body: s5 resolves to the IBM paper, s6 to
  the Microsoft 2017 report, and every body citation to those numbers points to
  the right owner. Policy met: 8 sources, 6 primary, 2 secondary.

- **Citations opened as printed.** All eight external hrefs land on the source's
  own canonical page. Six return 200. The sclite GitHub blob (s2) and the PNAS
  DOI (s8) return 403 to scripted/proxy requests but are the source's own
  browser-loadable pages, exactly as the evidence access-notes documented (both
  texts were read from mirrors); they are not broken for a reader who clicks
  them, so I do not count them broken. The three internal Background/prose links
  (whisper, bleu, rouge) use real published slugs and resolve on the library
  branch per the brief; not treated as broken.

No central claim broke, no figure conflicts with its primary, no miscitation, no
source-policy gap. Nothing routed from the skeptic read.

## Cut

The draft was already tight and on-register (Yglesias-plain, with Angwin-style
concreteness and the Silver "state the assumption, correct it" move on the
sclite tie-break). Four sentences failed the slop test and were cut or recast;
the pattern was edge-of-paragraph signposting, the failure the recent-pattern
notes and the lesson template both warn about.

- "Give the parity claim its strongest form before pushing on it." — a summary of
  the article's own method that also addresses the reader, which the lesson body
  may not do. Deleted; the paragraph now opens on the error-analysis evidence and
  the steelman still stands in full.
- "A short example makes the counting concrete." — an empty announcement of the
  example that follows ("A short X makes the Y concrete" survives the placeholder
  test, so it says nothing). Deleted; the table lead-in carries it.
- "The 'same rules' part carries more weight than it sounds." — puffery, an
  ordinary fact described as important without saying what it is. Deleted; the
  paragraph now opens on the concrete string-comparison point.
- "The 5.8 percent that opened this lesson was true." — the body referring to
  itself ("this lesson"), which the template confines to the two bookends.
  Recast to "Microsoft's 5.8 percent was true," which keeps the callback's
  referent without the self-reference.

Negative-parallelism constructions ("not a reading off a thermometer, it is a
count"; "counts words, not meaning") were checked and kept: each corrects a
misconception the piece actually names (the thermometer intuition; the belief
that a low score means an accurate transcript). The procedural second person
("you line the transcript... you tally the edits") is generic-you exposition,
endorsed by the voice guide's Silver exemplar, not reader-address, and stays.
No prompt leakage survived: the three closing questions are the lesson's own
taught payoff, not lifted commission labels; the thermometer image illustrates a
real mechanical point rather than carrying an instruction. Furniture (annotated
equation, S/D/I table, four-figure stat strip, one concession note, no verdict
block) each does distinct work and matches the lesson template.

## Reader

Read straight through as the paper's declared reader, what I have that the
sources alone would not: a single arc that turns "human parity" from a headline
into a lesson about a movable human baseline and a meaning-blind count, and then
into three questions (which speech, whose reference, normalized how) I can put to
any speech score. That matches the draft-handoff's original-work sentence, and
neither restates the sources: no single cited paper carries the mechanics, the
parity dispute, the meaning-blindness, and the blind spots together. The prose
sits closer to the voice-guide exemplars than to a median summary. The headline,
read last as the largest claim, is one the body earns.

## Edits

- Deleted method-signpost "Give the parity claim its strongest form before
  pushing on it." at the head of the steelman paragraph.
- Deleted announcement "A short example makes the counting concrete." before the
  worked-example table.
- Deleted puffery "The 'same rules' part carries more weight than it sounds." at
  the head of the normalization paragraph.
- Recast "The 5.8 percent that opened this lesson was true." to "Microsoft's 5.8
  percent was true." to remove the body's self-reference to the lesson.
- Reran `./nb check ... --no-check-links`: BLOCK 0, WARN 0, PUBLISHABLE.

## Required work

- **writer (non-blocking):** the head `<title>` element reads "'Human parity' in
  speech came down to..." while the h1 and the nb-meta `title` read "in speech
  recognition." Align the `<title>` for consistency (metadata is the writer's to
  stamp). Not publication-blocking.
- Word count: my cuts drop the body a little below the stamped words=2200; still
  well inside the 1200-2200 band. The orchestrator restamps after these edits and
  the proof recounts. Nothing to route.

No evidence gaps for the researcher and no redraft for the writer.

## Decision

approve — every focus item verifies against the record, the numbers and display
text re-derive cleanly, and the four slop cuts were within the editor's remit and
left the article clean (BLOCK 0, WARN 0).
