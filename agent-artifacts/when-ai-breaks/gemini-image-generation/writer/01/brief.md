# Brief 01 — writer — when-ai-breaks/gemini-image-generation

## Begin with these inputs (in order)
1. `agent-artifacts/when-ai-breaks/gemini-image-generation/editorial-direction.md`
2. `agent-artifacts/when-ai-breaks/gemini-image-generation/writing-coach/01/voice-guide.md` (reread before drafting)
3. `agent-artifacts/when-ai-breaks/gemini-image-generation/researcher/01/evidence.md`
4. `agent-artifacts/when-ai-breaks/gemini-image-generation/commission.md`
5. Article to EDIT: `library/when-ai-breaks/gemini-image-generation.html`
6. `.nb-context/`; furniture catalog `/home/user/the-nightly-build/templates/FURNITURE.md`

Follow the **writer** skill (Skill: `writer`; fallback `/home/user/the-nightly-build/skills/writer/SKILL.md`).

## What to write
A lesson of **1200–2200 words** in the desk's order: what happened (timeline with
names and exact dates, from the record) → why this class of system fails this way
(the mechanism: a hidden, context-blind diversity prompt-augmentation the model
obeyed; connect to RLHF/instruction tuning already taught) → where the same
bias-mitigation tradeoff lives today. Body first, bookends last. One `orientation` +
0–4 named flexible sections, each cited.

A **timeline** (furniture) may suit the sequence of events; use only if it clarifies.
Keep the voice on the engineering tradeoff, not the culture-war framing. Every
argument-bearing claim cited; `data-nb-kind` from evidence; mark Google's stated
account vs. reconstruction; accusations need two independent confirmations.

**Source asset:** only if the evidence record identifies a reputable, cited capture
whose argument the article actually spends — capture with
`/home/user/the-nightly-build/nb asset`, inspect it, write factual cited caption +
useful alt text. **Never** an external/hosted image URL (the proof bars it). If in
doubt, prose only.

Background links: already-published lessons only —
`../the-evidence/instructgpt.html` (the RLHF family this failure comes from), and
optionally `../when-ai-breaks/compas-recidivism.html`. **Only** add a Background link
to `../the-mechanics/instructions-are-data.html` if that lesson is already merged in
`/home/user/the-nightly-build/library-checkout` at drafting time; otherwise omit it
and teach the one needed sentence yourself. External links in **Go deeper**.

No scripts/styles/iframes; no external images. Bans per commission ("AI race" 0 etc.).

## nb-meta
series when-ai-breaks; slug gemini-image-generation; template lesson; mode open;
order null; date "2026-07-31"; tags e.g. ["bias","image-generation","google"];
measured sources/words/reading_minutes; `dek` = rendered dekline; harness
"claude-code-routine"; model "claude-sonnet-5". Set title, eyebrow "When AI Breaks",
h1, byline.

## Original work + proof
Original-work sentence in `writer/01/draft-handoff.md`. Run to `BLOCK: 0`:
```
/home/user/the-nightly-build/nb check .nb-work/when-ai-breaks/gemini-image-generation/library/when-ai-breaks/gemini-image-generation.html --series when-ai-breaks --library /home/user/the-nightly-build/library-checkout
```
If a source asset changed layout, also run `/home/user/the-nightly-build/nb preview`
and inspect. Fix or record every WARN. Return `DONE writer <path>` after `BLOCK: 0`.
Content in files.
