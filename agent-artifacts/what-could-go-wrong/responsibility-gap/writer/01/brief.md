# writer brief: what-could-go-wrong/responsibility-gap (01)

Inputs:
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/editorial-direction.md
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/commission.md
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/writing-coach/01/voice-guide.md
- .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/researcher/01/evidence.md — the complete claim set; treat it as the only claims available.
- .nb-work/what-could-go-wrong/responsibility-gap/library/what-could-go-wrong/responsibility-gap.html — the article to edit.
- .nb-work/what-could-go-wrong/responsibility-gap/.nb-context/ — the template contract and furniture catalogs. Documented markup only.

Output: .nb-work/what-could-go-wrong/responsibility-gap/agent-artifacts/what-could-go-wrong/responsibility-gap/writer/01/draft-handoff.md

Proof: /home/user/the-nightly-build/nb check /home/user/the-nightly-build/.nb-work/what-could-go-wrong/responsibility-gap/library/what-could-go-wrong/responsibility-gap.html --series what-could-go-wrong --repo /home/user/the-nightly-build

Work from these inputs. Do not tour the repository or the archive. Where something you need is missing, ask me (the orchestrator).

The angle, corrected by the evidence — read carefully, this reshapes the piece:
- The deployed cases do NOT actually test Matthias's and Sparrow's argument. Their gap opens only when NO human has the control and knowledge to be responsible. But the 2018 Uber system was a developmental system with a safety driver, and Tesla Autopilot is SAE Level 2 — both by design name a human supervisor as the responsible operator, which is exactly why the NTSB, NHTSA, and the Maricopa County court could locate a person (safety driver Rafaela Vasquez was charged and pleaded/sentenced; verify the outcome and dates from the record). So the honest finding is: the strong "no one can be held responsible" claim has NOT held up for legal and criminal responsibility in SUPERVISED systems, and remains UNPROVEN for the fully-autonomous, no-human-in-the-loop case the philosophers actually built the argument for. Draw exactly that line — do not let the real cases appear to refute the philosophical argument outright.
- Keep LEGAL responsibility and MORAL responsibility separate. The record closes the legal question far more firmly than the moral one. Tigard ("There Is No Techno-Responsibility Gap"), the strongest scholarly denial of the gap, still concedes the moral gap is "far less clear, and thereby less easily resolved" than the regulatory one. Quote/represent that fairly.
- The "law dissolves the gap" leg is weaker than it looks: the EU's dedicated AI Liability Directive was WITHDRAWN (2025); the Product Liability Directive that passed (2024/2853) does not apply until December 2026 and only to "products." State these facts plainly; do not present EU law as having already closed the gap.

Structure (series form): open with the argument at full strength in its defenders' terms — Matthias 2004 (control + knowledge as the classical conditions; learning automata remove both from the operator) and Sparrow 2007 (the programmer/commander/machine trilemma for autonomous weapons), in their own words. Then draw the sharp line between what has been shown in deployed systems and what is analogy about systems that do not exist. Then test against the record (Uber/Tempe, Tesla Autopilot, liability doctrine, EU instruments, Tigard's rebuttal). Then the present: who argues it now and what they want (strict liability, insurance, logging), and name the gap between confidence and proof in BOTH directions.

Boundaries (from commission): use Sparrow's argument but do not re-litigate autonomous weapons — link what-could-go-wrong/autonomous-weapons. Link automation-bias and normal-accidents rather than re-teaching. Incidents are illustration here, not a blow-by-blow retelling (tonight's when-ai-breaks piece is a different incident). Name no company as an authority; leave the reader to decide how worried to be.

Recent shapes to break: the desk opens by naming originator + year (fine — make Matthias/Sparrow do real work). It closes on a "no study has / no result reaches a real system" gap sentence (companion-dependency, negative-side-effects) — write this lesson's closing gap in its own terms (the untested fully-autonomous case), not that mold. Avoid semicolon-reversal and comma-triad deks; vary heading construction, no "clause, and clause" headings. Outline the reasoning before naming sections.

Process reminder: body first, then both bookends; number sources in first-citation order with correct data-nb-kind (Matthias, Sparrow, the NTSB/NHTSA reports, the court records, the EU instruments, and Tigard are primary; reporting is secondary); add data-nb-locator where the record gives one; use a documented furniture component (e.g. a small table separating legal vs moral responsibility across the cases, or a position/claim card) only where it beats prose and only from the supplied catalogs, built from the record; fill nb-meta (date 2026-09-22, harness "Claude Code", model = the model you run as); iterate with --no-check-links, then nb stamp and the exact nb check above until BLOCK: 0; put your one-sentence original-work statement in draft-handoff.md.
