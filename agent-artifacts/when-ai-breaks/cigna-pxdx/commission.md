# Commission: when-ai-breaks/cigna-pxdx

## Authorized work
Scheduled `nb duty` for 2026-09-09 returned `when-ai-breaks` in open mode. This
commission authorizes exactly one lesson on Cigna's PxDx automated claim-review
system. Template: lesson. Series floor: >=8 sources, >=4 primary, >=1 secondary.
Word band 1200-2200. Verified against the full published library: the health
items cover care-cost prediction (`optum-health-algorithm`), discharge-date
prediction (`nh-predict`), a sepsis alarm (`epic-sepsis-model`), and treatment
recommendation (`ibm-watson-oncology`). Cigna PxDx is a distinct system and
mechanism, automated batch denial of insurance claims with cursory human review,
and is a genuine gap.

## The incident, and why it fails that way
Tell one incident in order, name people, companies, and dates, from the record,
then explain why that kind of system fails that way, and close on where the same
weakness lives today.
- What it was built to do: Cigna's "PxDx" (procedure-to-diagnosis) process
  automatically flags claims where the billed procedure does not match a list of
  accepted diagnoses for it, so they can be denied in bulk.
- What happened: a March 2023 ProPublica / The Capitol Forum investigation
  reported that Cigna physicians denied large batches of these flagged claims
  without opening the patient files, signing off in seconds each. Report the
  figures the record gives (e.g. the reported volume of denials over a set period
  and the reported average time per denial) and verify each against the primary
  reporting. Note the aftermath: lawsuits, a California regulator's attention, and
  Cigna's public disputes of the characterization.
- Who it affected: patients whose valid claims were denied and who faced appeals
  or bills; clinicians; regulators.
- Why that kind of system fails: it automates a decision the law and policy
  assume a qualified human makes individually, while preserving the appearance of
  that review. The failure is not a mis-tuned model so much as a human-in-the-loop
  that has been reduced to a rubber stamp, where throughput (denials per second)
  is itself the evidence that no individual review occurred. Teach the missing
  piece: what "meaningful human review" is supposed to add, and why speed at scale
  is the tell that it is missing (compare, without re-teaching, the "no human
  examiner" failure the course has covered elsewhere).
- Where the weakness lives today: automated prior-authorization and claims
  adjudication across insurers, and any high-volume decision pipeline where a
  required human check becomes a formality.

## What the lesson teaches (short, complete)
1. What PxDx is and how it turned a medical-review requirement into an automated
   batch-denial pipeline. Be precise: it is an automated review/flagging process,
   not necessarily a machine-learning model; do not overclaim "AI/ML".
2. The incident in order, with named actors, dates, and the reported figures from
   the record.
3. Why an automated flag plus a rubber-stamp human review fails the purpose of
   review, and where the same pattern sits in systems the reader meets.

## Boundaries and neighbors
- Distinct from `optum-health-algorithm`, `nh-predict`, `epic-sepsis-model`,
  `ibm-watson-oncology`, and from `michigan-midas` (public unemployment). Link,
  do not re-teach, any shared idea. Where a cause is disputed (Cigna's account vs
  the reporting), present the strongest version of each and say what evidence
  settles it.
- Tonight's edition also ships: the-evidence/react-reasoning-and-acting,
  the-instruments/model-flops-utilization, the-mechanics/speculative-decoding,
  what-could-go-wrong/flash-crash-risk.
- Required contribution: the reader can explain why automating a required human
  review, without changing its legal form, produces mass wrongful denials, and
  can name the same failure mode elsewhere.

## Sources plan
Work from the record. Primary: the ProPublica/Capitol Forum investigation (March
2023); Cigna's own public response/statement; a court filing from the resulting
litigation; any regulator (e.g. California DMHC) document; a primary description
of the PxDx process (e.g. from the reporting's quoted internal materials or a
company statement). Secondary: follow-up reporting that held up. Every URL must
resolve; cite only what was read. VERIFY every figure (denial counts, seconds per
review, dates) against the primary reporting; do not rely on memory. Handle a
sensitive subject factually and without sensationalism. NOTE: github.com is
blocked here (egress 403) — not relevant to these sources, but do not cite it.

## Recent patterns to break (habits, not rules)
- This desk's headlines are plain "[actor] [did failure]" lines (keep). Avoid the
  "Two X did the same Y" mold (waymo) and comma-tail reversals. Let a fresh verb
  and a concrete figure carry it (a denials-per-second or volume figure is a
  natural anchor if the record supports it).
- Do not name a final body section "How far the X reaches"; vary heading
  construction.

## Production policy (recorded)
Profile balanced. Stages, none `required`: writing-coach effort low, researcher
effort high, writer effort medium, editor effort high; model tier "capable".
Executed with capable (Claude Opus-class) models at closest available effort. No
`required` directive traded down.
