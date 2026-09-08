# editor review-brief: the-mechanics/attribute-binding (01)

Inputs:
- editorial-direction.md (artifact root)
- commission.md (artifact root)
- writer/01/brief.md
- writing-coach/01/voice-guide.md
- researcher/01/evidence.md
- writer/01/draft-handoff.md
- the article: library/the-mechanics/attribute-binding.html
- .nb-context/ (template contract, furniture)

Recent-pattern notes (compare and flag formula):
- The mechanics desk is heavy on image-generation pieces. Recent openers/headings lead with a confident-wrong-output line ("A confident move the board doesn't allow"; "An image generator turns 'six apples' into 'some apples' before it draws a single pixel"). Flag any opener/heading reusing that "the model never X before it draws a pixel" mold.
- Recent deks lean on the comma-and mold and sometimes a colon lead ("No board is ever put in front of the model: it predicts the next move as text, and whether ..."). Flag a dek in that shape.
- No colon-subtitle headline.

Round focus:
- Verify the piece does NOT assert a single-object-vs-two-object accuracy number ("red apple works, red cube on blue sphere fails" as a figure). The honest quantified stand-in is Attend-and-Excite's full-prompt vs minimum-object CLIP gap (~0.83 vs ~0.60-0.63); check it is described as what it is.
- The "encoder hands over a bag of concepts" claim must read as an OPEN question, not a settled decomposition: Attend-and-Excite fixes via cross-attention only; StructureDiffusion's encoder-side fix barely moves numbers (19.2%→22.7%). This is competing-method evidence (evidence Contradictions), not a controlled split of blame. Confirm the settled part (systematic failure; cause in text-conditioning + cross-attention; reproduces across DALL-E 2 and Stable Diffusion) and open part are marked cleanly.
- If a source asset (Attend-and-Excite Figure 2) is present: inspect the crop and the caption; the caption must be a factual cited label and the prompt/figure must match the source exactly. If it cannot be confirmed, it should have been omitted — route to writer if wrong.
- Check T2I-CompBench and Conwell & Ullman numbers against the evidence. Standard three reads, audit data-nb-kind, open every citation href.
