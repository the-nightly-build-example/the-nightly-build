# Writer brief 01 — the-evidence/gpt-4-technical-report

Load the `writer` skill and follow it. This is invocation 01 (first draft).

## Exact inputs (begin here; do not tour the repo, history, or archive)
- Editorial direction: `.nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/editorial-direction.md` (house floor, headlines
  spec, press voice, lesson identity + furniture, series prompt — the standing law).
- Commission: `.nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/commission.md` (this article's angle, reader, contribution,
  source obligations, prior-coverage links, structures NOT to repeat, tags).
- Voice guide: `.nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/writing-coach/01/voice-guide.md`.
- Evidence record: `.nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/researcher/01/evidence.md` — the COMPLETE set of claims
  available to you. Do not add claims it does not support; request more if needed.
- Initialized article (edit this file, do not recreate its skeleton):
  `.nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html`
- Template context: `.nb-work/the-evidence/gpt-4-technical-report/.nb-context/` (template-contract.yaml, runtime-assets.yaml,
  furniture/{engine,press,template}.md). Author against documented furniture only.

## Exact outputs (write only these)
- The article HTML at `.nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html` (fill it in place).
- `.nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/writer/01/draft-handoff.md` (per the skill: original-work sentence;
  paths changed; proof result + any warnings left; evidence/voice questions).
- Any chart provenance / source asset only under `.nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report/`
  (only if the evidence record supplies a verified series or an exact cited visual).

## Permitted changes / decisions you own
- All body prose and the two bookends (write bookends AFTER the body).
- Section structure: outline the reasoning first, then name sections for THIS
  piece (argument-step headings, not scaffolding). Fill required anchors once;
  add only subject-specific flexible sections (0-4 allowed).
- Source numbering in first-citation order; carry each source's primary/secondary
  kind from the evidence record into `data-nb-kind`. Never invent a locator/URL.
- Fill `nb-meta` with ACTUAL values: series=the-evidence, slug=gpt-4-technical-report, template=lesson,
  mode=open, order=null, date=2026-08-01, measured sources + words + reading_minutes,
  a dek that obeys the headlines spec, harness=claude-code-routine,
  model=claude-sonnet-5, and tags (commission suggests a set; finalize honestly).
- Keep fixed engine assets, body classes, required labels, and required HTML exactly.

## Prove and hand off (the proof gate)
Run this until `BLOCK: 0`, treating warnings as revision notes:
```
cd /home/user/the-nightly-build && ./nb check .nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html --series the-evidence --repo /home/user/the-nightly-build --library /home/user/library-checkout --no-check-links
```
Then run the FINAL proof once WITH link checking (URLs must resolve) and confirm
`BLOCK: 0`:
```
cd /home/user/the-nightly-build && ./nb check .nb-work/the-evidence/gpt-4-technical-report/library/the-evidence/gpt-4-technical-report.html --series the-evidence --repo /home/user/the-nightly-build --library /home/user/library-checkout
```
Use `./nb preview` if layout or an asset changed and inspect the rendered result.
For a chart use `./nb chart`; for a captured visual use `./nb asset` (only if the
evidence record identifies an exact cited visual the argument spends).

## Unresolved / ownership
Missing evidence -> `REQUEST researcher <one-sentence question>`. Missing voice
guidance -> `REQUEST writing-coach <question>`. Missing commission context ->
`REQUEST orchestrator <need>`. Do not write around an evidence hole.

Return exactly one line after `BLOCK: 0`:
`DONE writer .nb-work/the-evidence/gpt-4-technical-report/agent-artifacts/the-evidence/gpt-4-technical-report/writer/01/draft-handoff.md`, or a REQUEST line above.
