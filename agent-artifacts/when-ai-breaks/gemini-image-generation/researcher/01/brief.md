# Brief 01 — researcher — when-ai-breaks/gemini-image-generation

## Begin with these inputs only
- `agent-artifacts/when-ai-breaks/gemini-image-generation/editorial-direction.md`
- `agent-artifacts/when-ai-breaks/gemini-image-generation/commission.md` (incident,
  three-move angle, required contribution, source obligations, starting sources)

Do not browse the archive as background. `nb` at `/home/user/the-nightly-build/nb`.
The desk mandates working **from the record**; accusations/impact claims need two
independent confirmations by parties in a position to know.

## Task
Follow the **researcher** skill (Skill tool: `researcher`).

- **Primary — Google's own account:** Prabhakar Raghavan's 23 Feb 2024 blog post
  ("Gemini image generation got it wrong. We'll do better."); Google's original
  pause statement; the Sundar Pichai staff memo — use an outlet that published its
  **verbatim wording** and treat the quoted memo text as primary, the outlet framing
  as secondary. Gemini/Imagen 2 product/technical documentation for what the system
  was. Confirm Raghavan's **exact title**, all **dates**, and the exact wording and
  attribution of the "completely unacceptable" quote.
- **The mechanism:** establish from Google's own words (and, if needed, careful
  technical reporting) that the cause was a diversity-tuning / hidden
  prompt-augmentation applied without context-awareness — and mark clearly what is
  Google's stated account vs. outside reconstruction. Do not overclaim internal
  details Google did not confirm.
- **Which outputs were real:** distinguish outputs Google itself acknowledged from
  cherry-picked or edited screenshots. Note contested examples.
- **Secondary (context/timeline):** The Verge, NYT, Wired, BBC, AP, Ars Technica.
- Steelman both sides: the genuine bias problem Google was solving vs. the
  context-blind rule it shipped.
- Classify each source primary/secondary with reason; verify every date/title/quote;
  confirm URLs resolve.

## Source policy to meet
min 8 sources; **primary ≥ 4, secondary ≥ 1.**

## Source assets
This incident is visual. In the **Source assets** section, identify whether a
specific, reputable, non-copyright-fraught capture of an acknowledged output (or a
Google figure) could carry the argument better than prose, and what a crop must
retain/omit — or write `None found`. Do not prescribe using an external image URL in
the article; the writer will decide and, if used, capture with `nb asset` from a
cited source. Note that active/externally-hosted images are barred by the proof.

## Output (write only this)
`agent-artifacts/when-ai-breaks/gemini-image-generation/researcher/01/evidence.md`
(stable sections). Return `DONE researcher <path>` (or `BLOCKED`/`REQUEST`).
