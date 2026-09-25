# draft handoff: when-ai-breaks/babylon-health (writer 01)

## Original-work sentence

The headline was "as good as a doctor," but the number came from vignettes
Babylon designed the test around, scored by a single judge, on the conditions
its own system was built to recognize, and the failures that mattered were the
serious presentations a curated test underweights. The article makes that work
visible by setting the study's actual words ("comparable," "safer on average,"
and its own caveat that the results "cannot be directly interpreted with respect
to real-world accuracy and safety") against the marketing, then showing the
number's fragility from the record itself: 97.0% triage-safety against the
independent judge versus 81.0% against the strictest in-house GP, and Coiera's
finding that dropping the weakest of the seven doctors flips the table to humans
winning on every measure.

## Proof status

- `./nb stamp` written: words 2199, sources 11, reading 10 min.
- `./nb check ... --no-check-links`: **BLOCK: 0, WARN: 0**, PUBLISHABLE.
- `./nb check ...` (links included): **BLOCK: 0, WARN: 0**, PUBLISHABLE.

No warnings left standing. The length landed at 2199 of the 2200 band ceiling;
this is deliberate (the lesson has to carry the two-failure structure plus the
aftermath and the "where it lives now" close), and it is inside the band.

## Structure and the two failures

Kept distinct, as the brief and voice guide require:
- Failure one (oversold claim, an evidence problem): orientation +
  "The number came from a hundred scripted vignettes."
- Failure two (documented under-triage, a safety problem): "What the vignettes
  left out."
No sentence blurs the two.

Furniture: one `nb-table` (head-to-head by test set, cited to the study) and one
`nb-note` carrying Babylon's "we stand by our original science" line beside the
findings it answers. Prior lesson linked once in prose at first use
(retinopathy-field-study, for lab-vs-field); epic-sepsis-model and
ibm-watson-oncology sit in Background.

## Things the editor should know

- **Two different "81%."** I used the study's Table 3 triage-safety figure
  (81.0% against the strictest in-house GP) and deliberately did **not** use the
  marketing "81%" MRCGP exam composite, which the evidence flags as a publicised
  figure the paper never states. The article's only exam reference is the RCGP's
  rejection and the paper's own "above 72%" comparison, not a single exam score.
- **Doctor count.** Used the paper's seven (Doctors A–G) with the parenthetical
  that Coiera's review says six, per the brief.
- **No real-world under-triage rate stated.** The article says so explicitly:
  the failures are the reproduced demonstrations plus the two MHRA-logged
  incidents, with no denominator, and Babylon's "millions of uses, no reported
  harm" is named as uncontrolled and self-reported, not a safety rate.
- **Headline defensibility.** "read a heart attack as a panic attack" is the
  Watkins female-profile demonstration (s6); the MHRA also logged one missed
  heart attack (s7). "as good as a doctor" is the softer form of Babylon's
  marketing; the body shows the marketing went further ("beaten doctors on the
  exam," s2) than the study did.

## Open questions / verification notes

1. **Source display titles.** The evidence recorded each source's URL, author,
   date and publication but not the article headlines. For MedCity (s2), the two
   TechCrunch pieces (s6, s7, s9), Tech.eu (s10) and gov.uk (s8) I set the
   display title from the publisher's own URL slug, which in each case is a
   full-sentence headline. If the desk wants headlines confirmed against the live
   pages, these are the ones to spot-check; none affects a claim in the body.
2. **Lancet quote (s4).** The correspondence full text is paywalled and
   bot-gated. The quoted conclusion is carried with a `data-nb-note` recording
   that the citation was confirmed via Crossref and the quote via Coiera's own
   review and multiple contemporaneous reproductions. I rendered it as two
   verbatim fragments with a bracketed `[it]` for the system's full name; if the
   desk can open the paywalled page, worth confirming the exact wording.

No evidence gaps blocked the draft; I did not ask the orchestrator for anything.
