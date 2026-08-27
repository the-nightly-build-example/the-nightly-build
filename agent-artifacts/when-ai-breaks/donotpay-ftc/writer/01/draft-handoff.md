# Draft handoff: when-ai-breaks/donotpay-ftc (01)

## Original-work sentence

The article separates the fluent document a subscriber could see from the never-asked question of whether the service was ever measured against a lawyer's work, and uses that separation to hold the FTC's finding at its true, narrow size — the absence of testing and substantiation, not any proven-wrong output — so a settled advertising case becomes a repeatable test the reader can apply to the next "AI that does X" claim.

## Proof result

`./nb check .../donotpay-ftc.html --series when-ai-breaks --library /home/user/library-checkout` (links included): **BLOCK: 0, WARN: 0, PUBLISHABLE.**

No warnings left standing. The three warnings from the first pass (2× sentence-density, 1× em-dash over the limit of 4) were all resolved by splitting the dense sentences and converting em-dashes to periods, commas, colons, and one parenthetical aside. `nb stamp`: words=1968, reading_minutes=9, sources=8.

## How the load-bearing constraints were handled

- **Contradictions section honored.** The "why it fails" section states outright that the FTC did *not* rule the documents were bad — it found something prior, that the company never checked. The mechanism (fluent legal prose is no evidence of legal correctness) is taught as a general failure, never attributed to the FTC as a finding of wrong outputs.
- **$193,000** is called "monetary relief" / consumer redress, never a fine, with the no-civil-penalty point stated.
- **Dates kept distinct:** September 2024 = the Operation AI Comply announcement of the proposed settlement; January 14, 2025 = the binding Decision and Order; 5–0 finalization publicized February 2025.
- **Courtroom earpiece episode kept separate** from the FTC action, explicitly flagged as sourced to Jan 2023 reporting and Browder's own words, "not the Commission's findings."
- **DoNotPay's response** carried in its own words (no-admission-of-liability, "a few hundred customers... out of millions," services "long been discontinued").
- **Background links, not re-teaching:** hallucination and mata-v-avianca appear as plain in-prose links (mechanism section) and as Background rows; the piece does not re-teach why models hallucinate.

## Sources

8 total, 5 primary (complaint, Decision & Order, 2024 Operation AI Comply release, case docket, 2025 finalization release) + 3 secondary (CBS, Fortune, ABA Journal). Numbered in first-citation order. Meets the series floor (8 / ≥4 primary / ≥1 secondary).

## Furniture

Two `nb-note` blockquotes: the FTC's core finding (Compl. para 20) and the mandated customer notice (Attachment A). No stat strip, chart, or source asset.

## Open questions / notes for editor

- **No source asset.** The evidence record flagged Complaint Exhibit A (the "World's First Robot Lawyer" homepage capture) as the strongest candidate image, and its argument would spend it. The FTC's document server blocks automated fetches (returns an anti-abuse page, HTTP-level, not a 404), so the exhibit PDF could not be downloaded to capture with `nb asset`. The marketed claims are instead quoted verbatim in prose from the evidence record. If the editor's environment can reach the FTC PDF, Exhibit A on complaint p.3 is the capture to add.
- **One voice call to confirm:** the heading "Why a fluent legal document is not a correct one" uses an "is not" contrast. It is kept because the fluent-vs-correct distinction is the section's actual teaching and names the real misconception (that the harm was defective output), which the piece spends a full section establishing. Flagging in case the editor reads it as the negative-parallelism mold.
- **Model/harness meta:** set to `claude-code-routine` / `claude-opus-4-8` (the writer model producing this draft). Confirm against the run's production record if a different id is expected.
