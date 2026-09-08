# writer brief: the-mechanics/attribute-binding (01)

Inputs:
- editorial-direction.md (artifact root) — house standard, paper voice, series prompt, citation standard.
- writing-coach/01/voice-guide.md — how this piece should sound; reread before drafting.
- researcher/01/evidence.md — the complete set of claims available to you; use the Numbers section exactly.
- commission.md (artifact root) — behavior, teaching list, source floor, habits not to inherit.
- The initialized article: library/the-mechanics/attribute-binding.html (edit in place; keep chrome exact).
- .nb-context/ (template contract, furniture catalogs, runtime assets).

Output: writer/01/draft-handoff.md (plus the edited article).

Proof: ./nb check .nb-work/the-mechanics/attribute-binding/library/the-mechanics/attribute-binding.html --series the-mechanics --library /tmp/claude-0/-home-user-the-nightly-build/7ee8fcf2-0447-5975-8ee1-93a43ada820c/scratchpad/library-checkout

This round's focus — three evidence notes:
- No cited primary gives a clean single-object-vs-two-object accuracy pair. Do NOT assert a "red apple works, red cube on blue sphere fails" number. The honest quantified stand-in is Attend-and-Excite's full-prompt vs minimum-object CLIP gap (~0.83 vs ~0.60-0.63); describe it accurately as what it is.
- The "encoder hands over a bag of concepts" emphasis is complicated by the evidence and must be handled as an open question, not a settled decomposition: Attend-and-Excite recovers a large share by touching only cross-attention (never the encoder), while StructureDiffusion's encoder-side fix barely moves the numbers (19.2% → 22.7% two-object color). Each fix paper favors the part it intervenes on, so this is competing-method evidence, not a controlled split of blame (recorded in the evidence Contradictions). Mark the settled part (systematic failure; cause lives in text conditioning plus cross-attention; reproduces across DALL-E 2 and Stable Diffusion, different encoders) and the open part cleanly. The 2025 survey argues the cause is architectural and incremental fixes fall short — consistent with post-fix numbers staying low.
- Source asset: the evidence identifies Attend-and-Excite Figure 2's "incorrect attribute binding" column (prompt, wrong SD image, corrected output). If you use it, confirm the exact figure and prompt at capture time (the evidence read it from a rendered summary), capture with nb asset, keep the prompt label and baseline panel, caption factually with the source. If it cannot be confirmed cleanly, omit it rather than risk a wrong caption.

Use real measured numbers from the evidence (T2I-CompBench SD v1.4 binding scores; Conwell & Ullman's ~22% relation-match rate on 1,350 DALL-E 2 images). No code. Define text encoder and cross-attention in plain words at first use; link ../the-mechanics/attention.html rather than re-teaching attention.

Habits not to inherit (from commission.md): the mechanics desk is heavy on image-gen pieces — do not echo their openers/headings; do not reuse the "the model never X before it draws a pixel" framing as a template; vary heading construction; no colon-subtitle headline.
